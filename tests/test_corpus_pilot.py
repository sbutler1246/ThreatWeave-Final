import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from extraction.corpus_pilot import aggregate_candidates, align_quote, make_prompt, run, validate_output
from extraction.llama_tokenizer import MODEL_DIGEST
from schemas import Chunk, Document, SourceContext


def fixture(text='Group Alpha used Tool Beta.', prefix=''):
    full = prefix+text
    document = Document(doc_id='sample', title='Source', source_url='https://example.org/source',
                        text=full, content_hash='a'*64)
    chunk = Chunk(chunk_id='sample:development:test', doc_id='sample', start=len(prefix),
                  end=len(full), text=text)
    return {'document': document, 'chunk': chunk, 'spec': {'kind': 'prose'},
            'preparation': {'source_tokens': 8, 'source_text_sha256': 'b'*64}}


def output(quote='Group Alpha used Tool Beta.'):
    return {'entities': [
        {'local_id': 'e1', 'type': 'ThreatGroup', 'name': 'Group Alpha', 'attack_id': None},
        {'local_id': 'e2', 'type': 'Software', 'name': 'Tool Beta', 'attack_id': None}],
        'quotes': [{'quote_id': 'q1', 'quote': quote}],
        'relations': [{'head': 'e1', 'predicate': 'USES', 'tail': 'e2', 'quote_id': 'q1',
                       'context_ids': [], 'confidence': None}]}


class CorpusPilotValidationTests(unittest.TestCase):
    def test_unique_quotes_align_to_exact_document_offsets(self):
        item = fixture(prefix='Heading\n')
        batch, resolution, alignment = validate_output(json.dumps(output()), item, [])
        self.assertEqual(batch.relations[0].evidence.start, 0)
        self.assertEqual(alignment[0]['document_start'], len('Heading\n'))
        self.assertEqual(item['document'].text[alignment[0]['document_start']:alignment[0]['document_end']],
                         batch.relations[0].evidence.quote)
        self.assertEqual(resolution[0]['status'], 'unresolved')

    def test_missing_and_repeated_including_overlapping_quotes_are_rejected(self):
        for text, quote in [('abc', 'missing'), ('repeat repeat', 'repeat'), ('aaa', 'aa')]:
            with self.assertRaises(ValueError):
                align_quote(text, quote)

    def test_uncited_endpoint_elsewhere_in_window_is_rejected(self):
        item = fixture('Group Alpha used Tool Beta. Group Alpha scanned ports.')
        with self.assertRaises(ValueError):
            validate_output(json.dumps(output('Group Alpha scanned ports.')), item, [])

    def test_title_does_not_prove_actor_use_but_explicit_caption_can_scope_row(self):
        item = fixture('Tool Beta enables remote control.', prefix='Group Alpha\n')
        item['chunk'].inherited_context = [SourceContext(start=0, end=11, text='Group Alpha')]
        value = output(item['chunk'].text)
        value['relations'][0]['context_ids'] = ['ctx1']
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), item, [])
        caption = 'Table 1: Tools Used by Group Alpha'
        item = fixture('Tool Beta enables remote control.', prefix=caption+'\n')
        item['chunk'].inherited_context = [SourceContext(start=0, end=len(caption), text=caption)]
        batch, _, aligned = validate_output(json.dumps(value), item, [])
        self.assertEqual(len(batch.relations), 1)
        self.assertEqual(aligned[0]['context_ids'], ['ctx1'])

    def test_forbidden_types_dangling_references_and_duplicate_relations_are_rejected(self):
        for change in ['type', 'quote', 'context', 'duplicate']:
            value = output()
            if change == 'type':
                value['entities'][1]['type'] = 'ThreatGroup'
            elif change == 'quote':
                value['relations'][0]['quote_id'] = 'q2'
            elif change == 'context':
                value['relations'][0]['context_ids'] = ['ctx9']
            else:
                value['relations'].append(dict(value['relations'][0]))
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_output(json.dumps(value), fixture(), [])

    def test_source_uncertainty_is_flagged_for_semantic_review(self):
        item = fixture('Group Alpha may use Tool Beta.')
        _, _, alignment = validate_output(json.dumps(output(item['chunk'].text)), item, [])
        self.assertIn('source_uncertainty_wording', alignment[0]['review_flags'])

    def test_deduplication_keeps_both_windows_and_exact_source_support(self):
        first = fixture('Heading\nGroup Alpha used Tool Beta.')
        second = fixture(prefix='Heading\n')
        first['chunk'].chunk_id = 'sample:development:first'
        second['chunk'].chunk_id = 'sample:development:second'
        cases = [(item, *validate_output(json.dumps(output()), item, [])) for item in [first, second]]
        facts, counts = aggregate_candidates(cases)
        self.assertEqual(counts['raw_candidate_relations'], 2)
        self.assertEqual(counts['unique_document_candidate_facts'], 1)
        self.assertEqual(counts['exact_source_support_duplicates'], 1)
        self.assertEqual(len(facts[0]['supports']), 2)
        self.assertEqual(facts[0]['semantic_review_status'], 'pending')

    def test_output_bounds_and_endpoint_proof_ids(self):
        _, _, schema = make_prompt(fixture())
        self.assertEqual(schema['properties']['relations']['maxItems'], 4)
        value = output()
        value['entities'][1]['attack_id'] = 'S0001'
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), fixture(), [])
        value = output('x'*241)
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), fixture('x'*241), [])
        for name in ['', '   ', ' Group Alpha']:
            value = output()
            value['entities'][0]['name'] = name
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_output(json.dumps(value), fixture(), [])


class Response:
    def __init__(self, body, status_code=200, text=None):
        self.body = body
        self.status_code = status_code
        self.text = json.dumps(body) if text is None else text
    def raise_for_status(self):
        if self.status_code >= 400:
            import requests
            raise requests.HTTPError(f'{self.status_code} Client Error', response=self)
    def json(self):
        if isinstance(self.body, Exception):
            raise self.body
        return self.body


class HttpFixture:
    def __init__(self, digest=MODEL_DIGEST):
        self.digest = digest
        self.posts = []
    def get(self, *args, **kwargs):
        return Response({'models': [{'name': 'llama3.1:8b', 'digest': self.digest}]})
    def post(self, *args, **kwargs):
        self.posts.append(kwargs['json'])
        if len(self.posts) == 1:
            return Response({'done': True, 'done_reason': 'length', 'response': 'INCOMPLETE_MARKER', 'eval_count': 700})
        from extraction.source_choices import make_prompt
        _, _, _, index = make_prompt(fixture('Group Alpha actors used Tool Beta.'), [])
        head = next(key for key, value in index['choices'].items() if value['name'] == 'Group Alpha actors')
        tail = next(key for key, value in index['choices'].items() if value['name'] == 'Tool Beta')
        value = {'relations': [{'head': head, 'predicate': 'USES', 'tail': tail, 'unit_ids': ['u001'], 'context_ids': []}]}
        return Response({'done': True, 'done_reason': 'stop', 'response': json.dumps(value), 'eval_count': 150})
    def close(self):
        pass


class TokenizerFixture:
    def encode(self, text, **kwargs):
        return type('Encoding', (), {'ids': [1]*100})()


class CorpusPilotRunTests(unittest.TestCase):
    def run_fixture(self, repo, http):
        config = {'llm': {'model': 'llama3.1:8b', 'temperature': 0, 'num_ctx': 8192, 'num_predict': 700}}
        with patch('requests.Session', return_value=http), patch('extraction.corpus_pilot.load_verified_tokenizer',
                return_value=(TokenizerFixture(), {})):
            result = run(repo, [fixture('Group Alpha actors used Tool Beta.')], config, [], 'a'*64, {'fingerprint': 'f'*64}, repo/'prepared')
        folder = next((repo/'work/corpus_extraction_pilot').iterdir())
        return result, folder, json.loads((folder/'summary.json').read_text())

    def temporary(self):
        root = Path(__file__).resolve().parents[1]/'work/corpus_pilot_tests'
        root.mkdir(parents=True, exist_ok=True)
        return tempfile.TemporaryDirectory(dir=root)

    def test_truncation_repair_starts_fresh_and_preserves_failed_output(self):
        with self.temporary() as tmp:
            repo = Path(tmp)
            (repo/'docs').mkdir()
            http = HttpFixture()
            result, folder, summary = self.run_fixture(repo, http)
            self.assertEqual(result, 0)
            self.assertEqual(len(http.posts), 2)
            self.assertNotIn('INCOMPLETE_MARKER', http.posts[1]['prompt'])
            self.assertIn('INCOMPLETE_MARKER', (folder/'01/raw_extraction_1.json').read_text())
            self.assertEqual(summary['items'][0]['attempts'][0]['done_reason'], 'length')
            self.assertEqual(summary['items'][0]['relation_count'], 1)
            self.assertFalse(summary['graph_writes'])

    def test_changed_serving_model_is_rejected_before_generation(self):
        with self.temporary() as tmp:
            repo = Path(tmp)
            (repo/'docs').mkdir()
            http = HttpFixture(digest='wrong')
            result, _, summary = self.run_fixture(repo, http)
            self.assertEqual(result, 1)
            self.assertEqual(http.posts, [])
            self.assertEqual(summary['status'], 'service_error')

    def test_http_rejection_keeps_body_and_does_not_request_model_repair(self):
        for response in [Response({'error': 'schema grammar rejected'}, 400),
                         Response(ValueError('not JSON'), 502, text='upstream failure')]:
            with self.subTest(status=response.status_code), self.temporary() as tmp:
                repo = Path(tmp)
                (repo/'docs').mkdir()
                http = HttpFixture()
                with patch.object(http, 'post', return_value=response) as post:
                    result, folder, summary = self.run_fixture(repo, http)
                self.assertEqual(result, 1)
                self.assertEqual(post.call_count, 1)
                record = summary['items'][0]
                self.assertEqual(record['status'], 'service_error')
                self.assertEqual(record['attempts'][0]['http_status'], response.status_code)
                error_file = folder/'01'/record['attempts'][0]['http_error_body_file']
                self.assertEqual(error_file.read_text(), response.text)
                self.assertFalse((folder/'01/repair_prompt.txt').exists())
                self.assertEqual(summary['raw_candidate_relations'], 0)
                if response.status_code == 400:
                    self.assertIn('schema grammar rejected', record['error'])


if __name__ == '__main__':
    unittest.main()
