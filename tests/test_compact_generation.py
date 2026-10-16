"""Output-boundary guards and fresh repair after an interrupted JSON response."""
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from combined_qa import retry_questions
from graph_qa import CompactAnswer, GENERATOR_VERSION, generate
from schemas import EvidenceBundle, Passage, QueryRequest


class CompactGenerationTests(unittest.TestCase):
    def answer(self):
        return {'answer': 'See cited claims.', 'claims': [{'text': 'Source-supported observation.', 'citations': ['E1']}],
                'abstained': False}

    def test_compact_schema_bounds_and_duplicate_guards(self):
        CompactAnswer.model_validate(self.answer())
        for mutation in ['long_text', 'many_claims', 'many_citations', 'duplicate', 'duplicate_citation', 'answer_field', 'blank']:
            value = self.answer()
            if mutation == 'long_text':
                value['claims'][0]['text'] = 'x'*281
            elif mutation == 'many_claims':
                value['claims'] = [{'text': f'Fact {i}.', 'citations': ['E1']} for i in range(9)]
            elif mutation == 'many_citations':
                value['claims'][0]['citations'] = ['E1', 'E2', 'E3', 'E4', 'E5']
            elif mutation == 'duplicate':
                value['claims'].append({'text': 'SOURCE-SUPPORTED   OBSERVATION.', 'citations': ['E1']})
            elif mutation == 'duplicate_citation':
                value['claims'][0]['citations'] = ['E1', 'E1']
            elif mutation == 'answer_field':
                value['answer'] = 'Extra duplicated narrative.'
            else:
                value['claims'][0]['text'] = '   '
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                CompactAnswer.model_validate(value)

    def inputs(self):
        bundle = EvidenceBundle(passages=[Passage(citation_id='E1', doc_id='test', chunk_id='chunk',
            source_url='https://example.org/source', text='Source-supported observation.', start=0,
            end=29, source_kind='cisa')], citation_ids=['E1'], paths=[], retrieval_ms=0,
            configuration_hash='hash', corpus_version='test')
        request = QueryRequest(question='What was observed?', mode='hybrid', corpus_version='test')
        config = {'llm': {'model': 'test-model', 'temperature': 0, 'num_ctx': 8192, 'num_predict': 700}}
        return bundle, request, config

    def test_truncation_repair_omits_incomplete_output_and_keeps_budget(self):
        bundle, request, config = self.inputs()
        http = MagicMock()
        http.post.return_value.json.side_effect = [
            {'done': True, 'done_reason': 'length', 'response': 'INCOMPLETE_RESPONSE_MARKER'},
            {'done': True, 'done_reason': 'stop', 'response': json.dumps(self.answer())}]
        answer, metadata = generate(http, request, bundle, 'SOURCE PASSAGES', config, MagicMock(), 60)
        repair = http.post.call_args_list[1].kwargs['json']['prompt']
        self.assertIn('Start fresh', repair)
        self.assertNotIn('INCOMPLETE_RESPONSE_MARKER', repair)
        self.assertEqual(http.post.call_count, 2)
        self.assertTrue(all(call.kwargs['json']['options']['num_predict'] == 700 for call in http.post.call_args_list))
        self.assertEqual(metadata['generator_version'], GENERATOR_VERSION)
        self.assertEqual(answer.answer, 'Source-supported observation. [E1]')

    def test_two_truncated_outputs_fail_without_a_third_attempt(self):
        bundle, request, config = self.inputs()
        http = MagicMock()
        http.post.return_value.json.return_value = {'done': True, 'done_reason': 'length', 'response': 'unfinished'}
        with self.assertRaisesRegex(ValueError, 'output budget'):
            generate(http, request, bundle, 'SOURCE PASSAGES', config, MagicMock(), 60)
        self.assertEqual(http.post.call_count, 2)

    def test_unknown_citation_still_fails_compact_output(self):
        bundle, request, config = self.inputs()
        value = self.answer()
        value['claims'][0]['citations'] = ['E999']
        http = MagicMock()
        http.post.return_value.json.return_value = {'done': True, 'done_reason': 'stop', 'response': json.dumps(value)}
        with self.assertRaises(ValueError):
            generate(http, request, bundle, 'SOURCE PASSAGES', config, MagicMock(), 60)
        self.assertEqual(http.post.call_count, 2)

    def test_retry_selects_only_failed_questions_and_checks_scope(self):
        repo = Path(__file__).resolve().parents[1]
        retriever = SimpleNamespace(configuration_hash='config',
            text=SimpleNamespace(manifest={'fingerprint': 'text'}),
            index=SimpleNamespace(manifest={'index_fingerprint': 'graph'}))
        summary = {'mode': 'hybrid', 'configuration_hash': 'config', 'index_fingerprint': 'text',
            'graph_index_fingerprint': 'graph', 'cases': [
                {'status': 'failed', 'question': 'Failed question?'},
                {'status': 'answer_ready_for_review', 'question': 'Completed question?'},
                {'status': 'abstained', 'question': 'Abstained question?'}]}
        folder = repo/'work/hybrid_qa/test-retry-fixture'
        with patch.object(Path, 'read_text', return_value=json.dumps(summary)):
            questions, _, _ = retry_questions(repo, folder, 'hybrid', retriever)
            self.assertEqual(questions, ['Failed question?'])
            with self.assertRaises(ValueError):
                retry_questions(repo, repo/'docs/outside-run', 'hybrid', retriever)
            retriever.index.manifest['index_fingerprint'] = 'changed'
            with self.assertRaisesRegex(ValueError, 'Graph index changed'):
                retry_questions(repo, folder, 'hybrid', retriever)


if __name__ == '__main__':
    unittest.main()
