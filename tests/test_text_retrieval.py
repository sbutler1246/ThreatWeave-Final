"""Text source integrity, atomic context packing and shared generator mode."""
import copy
import json
import unittest
from unittest.mock import MagicMock

from graph_qa import generate
from graph_pilot_qa import checked_answer
from retrieval.development_text import embedding_text, metadata, sha
from retrieval.text_retrieval import pack_hits
from schemas import Chunk, QueryRequest, SourceContext


class TextRetrievalTests(unittest.TestCase):
    def setUp(self):
        self.config = {'corpus_version': 'test-corpus',
            'retrieval': {'text_candidates': 5, 'final_chunks': 5, 'evidence_token_budget': 3000},
            'llm': {'model': 'test-model', 'temperature': 0, 'num_ctx': 8192, 'num_predict': 700}}
        heading = 'Tools used by Affiliates'
        context = SourceContext(start=0, end=len(heading), text=heading)
        full = context.text+'\nTool one source.\nTool two source.'
        self.expected, self.hits = {}, []
        for number, body in enumerate(['Tool one source.', 'Tool two source.']):
            start = full.index(body)
            child = Chunk(chunk_id=f'child-{number}', doc_id='test-doc', start=start,
                end=start+len(body), text=body, inherited_context=[context],
                role='retrieval', parent_extraction_chunk_id=f'parent-{number}')
            record = {'chunk': child.model_dump(mode='json'),
                'embedding_text': embedding_text(child.inherited_context, body),
                'wordpiece_count': 8, 'source_kind': 'cisa', 'source_url': 'https://example.org/source',
                'source_hash': sha(full), 'title': 'Test source', 'provenance': {}}
            self.expected[child.chunk_id] = record
            self.hits.append({'id': child.chunk_id, 'document': record['embedding_text'],
                              'metadata': metadata(record), 'distance': 0.2+number/10})

    def pack(self, hits=None):
        return pack_hits(self.hits if hits is None else hits, self.expected, self.config, 'test-hash')

    def test_text_bundle_has_exact_separate_spans_and_no_graph_edges(self):
        bundle, context, stats = self.pack()
        self.assertEqual(bundle.paths, [])
        self.assertEqual(len(bundle.passages), 3)
        self.assertEqual(stats['selected_chunk_count'], 2)
        self.assertEqual(stats['selected_path_count'], 0)
        self.assertEqual(stats['evidence_utf8_bytes'], len(context.encode('utf-8')))
        self.assertEqual(len([p for p in bundle.passages if p.start == 0]), 1)
        self.assertTrue(all(len(p.text) == p.end-p.start for p in bundle.passages))

    def test_changed_text_metadata_and_unknown_id_are_rejected(self):
        for mutation in ['text', 'metadata', 'id']:
            hits = copy.deepcopy(self.hits)
            if mutation == 'text':
                hits[0]['document'] = 'Invented source fact.'
            elif mutation == 'metadata':
                hits[0]['metadata']['source_hash'] = '0'*64
            else:
                hits[0]['id'] = 'foreign-chunk'
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                self.pack(hits)

    def test_small_budget_skips_whole_source_and_context_group(self):
        self.config['retrieval']['evidence_token_budget'] = 50
        bundle, context, stats = self.pack()
        self.assertEqual(bundle.passages, [])
        self.assertEqual(stats['budget_skipped_chunks'], 2)
        self.assertLessEqual(len(context.encode('utf-8')), 50)

    def test_candidate_and_final_chunk_limits_do_not_expand_search(self):
        self.config['retrieval']['text_candidates'] = 1
        bundle, _, stats = self.pack()
        self.assertEqual(stats['candidate_chunk_count'], 1)
        self.assertEqual(stats['selected_chunk_ids'], ['child-0'])
        self.assertEqual(len(bundle.passages), 2)
        self.config['retrieval']['text_candidates'] = 5
        self.config['retrieval']['final_chunks'] = 1
        _, _, stats = self.pack()
        self.assertEqual(stats['candidate_chunk_count'], 2)
        self.assertEqual(stats['selected_chunk_count'], 1)

    def test_non_finite_distance_is_rejected(self):
        hits = copy.deepcopy(self.hits)
        hits[0]['distance'] = float('nan')
        with self.assertRaisesRegex(ValueError, 'non-finite'):
            self.pack(hits)

    def test_text_answers_reject_citations_outside_retrieved_bundle(self):
        bundle, _, _ = self.pack()
        raw = json.dumps({'answer': 'Unverified answer', 'claims': [
            {'text': 'A fact.', 'citations': ['E999']}], 'abstained': False})
        with self.assertRaises(ValueError):
            checked_answer(raw, bundle, 0)

    def test_shared_generator_labels_text_mode_and_renders_cited_claims(self):
        bundle, context, _ = self.pack()
        request = QueryRequest(question='What tool is reported?', mode='text_only', corpus_version='test-corpus')
        http = MagicMock()
        http.post.return_value.json.return_value = {'done': True, 'done_reason': 'stop',
            'response': json.dumps({'answer': 'See cited claims.', 'claims': [
                {'text': 'Tool one source.', 'citations': ['E1']}], 'abstained': False})}
        answer, _ = generate(http, request, bundle, context, self.config, MagicMock(), 60)
        prompt = http.post.call_args.kwargs['json']['prompt']
        self.assertIn('MODE: text_only\n', prompt)
        self.assertNotIn('MODE: graph_only', prompt)
        self.assertEqual(answer.answer, 'Tool one source. [E1]')
        self.assertIn('text_only', answer.warnings[0])
        self.assertEqual(http.post.call_count, 1)


if __name__ == '__main__':
    unittest.main()
