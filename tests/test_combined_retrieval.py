"""Fusion deduplication, path integrity, rank arithmetic and mode boundaries."""
import copy
import unittest
from unittest.mock import MagicMock

from retrieval.combined_retrieval import DevelopmentCombinedRetriever, combine, reciprocal_ranks
from schemas import Chunk, EvidenceBundle, GraphPath, Passage, QueryRequest, RelationshipEdge, SourceContext


class CombinedRetrievalTests(unittest.TestCase):
    def setUp(self):
        self.config = {'corpus_version': 'test', 'retrieval': {'rrf_k': 60,
            'final_chunks': 5, 'final_paths': 6, 'evidence_token_budget': 3000}}
        url = 'https://example.org/source'
        values = [('cisa-doc', 'parent-row', 30, 'Tool row.', 'cisa'),
                  ('cisa-doc', 'parent-row', 0, 'Actor heading', 'cisa'),
                  ('ref-doc-1', 'parent-ref-1', 0, 'Mitigation one.', 'attack'),
                  ('ref-doc-1', 'parent-ref-1', 30, 'Guidance one.', 'attack'),
                  ('ref-doc-2', 'parent-ref-2', 0, 'Mitigation two.', 'attack'),
                  ('ref-doc-2', 'parent-ref-2', 30, 'Guidance two.', 'attack')]
        passages = [Passage(citation_id=f'E{i}', doc_id=d, chunk_id=c, start=s,
            end=s+len(text), text=text, source_kind=kind, source_url=url)
            for i, (d, c, s, text, kind) in enumerate(values, 1)]
        paths = []
        for i in range(2):
            paths.append(GraphPath(path_id=f'P{i+1}', edges=[
                RelationshipEdge(head_id='group', predicate='USES', tail_id='tool',
                                 assertion_ids=['use'], citation_ids=['E1', 'E2']),
                RelationshipEdge(head_id='tool', predicate='USES_TECHNIQUE', tail_id='tech',
                                 assertion_ids=['technique'], citation_ids=['E1', 'E2']),
                RelationshipEdge(head_id='tech', predicate='MITIGATED_BY', tail_id=f'mit-{i}',
                                 assertion_ids=[f'mitigation-{i}'], citation_ids=[f'E{3+2*i}', f'E{4+2*i}'])]))
        self.graph = EvidenceBundle(passages=passages, paths=paths,
            citation_ids=[p.citation_id for p in passages], retrieval_ms=0,
            configuration_hash='graph', corpus_version='test')
        records = []
        for parent, body, heading in [('parent-ref-2', passages[5], passages[4]),
                                      ('parent-row', passages[0], passages[1])]:
            child = Chunk(chunk_id='child-'+parent, doc_id=body.doc_id, start=body.start,
                end=body.end, text=body.text, role='retrieval', parent_extraction_chunk_id=parent,
                inherited_context=[SourceContext(start=heading.start, end=heading.end, text=heading.text)])
            records.append({'chunk': child.model_dump(mode='json'),
                            'source_url': str(body.source_url), 'source_kind': body.source_kind})
        self.text = records
        self.names = {'group': 'Actor', 'tool': 'Tool', 'tech': 'Technique',
                      'mit-0': 'Mitigation one', 'mit-1': 'Mitigation two'}

    def merged(self, graph=None, text=None):
        return combine(self.graph if graph is None else graph,
            self.text if text is None else text, self.config, 'combined', self.names)

    def test_rrf_duplicate_parents_contribute_once_per_branch(self):
        x, y = ('doc', 'x'), ('doc', 'y')
        scores, ranks = reciprocal_ranks({'graph': [x, x, y], 'text': [y, x]}, 60)
        self.assertAlmostEqual(scores[x], 1/61+1/62)
        self.assertEqual(ranks[x], {'graph': 1, 'text': 2})
        self.assertEqual(ranks[y], {'graph': 2, 'text': 1})
        with self.assertRaises(ValueError):
            reciprocal_ranks({'graph': [x]}, 0)

    def test_shared_spans_are_deduplicated_and_all_path_citations_remapped(self):
        bundle, _, stats = self.merged()
        self.assertEqual(len(bundle.passages), 6)
        self.assertEqual(len(bundle.paths), 2)
        self.assertTrue(all(len(p.edges) == 3 for p in bundle.paths))
        self.assertTrue(all(set(e.citation_ids) <= set(bundle.citation_ids)
                            for p in bundle.paths for e in p.edges))
        self.assertEqual(len({(p.doc_id, p.start, p.end) for p in bundle.passages}), 6)
        self.assertFalse(stats['node2vec_enabled'])

    def test_parent_supported_by_both_branches_prioritizes_its_whole_path(self):
        self.config['retrieval']['final_paths'] = 1
        bundle, _, stats = self.merged()
        self.assertEqual(len(bundle.paths), 1)
        self.assertEqual(bundle.paths[0].edges[-1].tail_id, 'mit-1')
        self.assertEqual(len(bundle.paths[0].edges), 3)
        self.assertEqual(stats['selected_path_count'], 1)

    def test_budget_never_leaves_a_partial_path(self):
        self.config['retrieval']['evidence_token_budget'] = 50
        bundle, context, stats = self.merged()
        self.assertEqual(bundle.paths, [])
        self.assertEqual(bundle.passages, [])
        self.assertLessEqual(len(context.encode('utf-8')), 50)
        self.assertTrue(stats['skipped_groups'])

    def test_empty_graph_branch_keeps_text_and_records_that_fact(self):
        empty = self.graph.model_copy(update={'paths': [], 'passages': [], 'citation_ids': []})
        bundle, _, stats = self.merged(graph=empty)
        self.assertEqual(bundle.paths, [])
        self.assertTrue(bundle.passages)
        self.assertTrue(stats['graph_branch_empty'])

    def test_conflicting_source_span_or_corpus_version_is_rejected(self):
        altered = copy.deepcopy(self.text)
        altered[1]['chunk']['text'] = 'Bad quote'
        with self.assertRaisesRegex(ValueError, 'disagree'):
            self.merged(text=altered)
        wrong = self.graph.model_copy(update={'corpus_version': 'other'})
        with self.assertRaisesRegex(ValueError, 'corpus'):
            self.merged(graph=wrong)

    def test_full_hybrid_does_not_silently_use_ablation(self):
        retriever = DevelopmentCombinedRetriever.__new__(DevelopmentCombinedRetriever)
        retriever.config = self.config
        retriever.graph = MagicMock()
        request = QueryRequest(question='A test question', mode='hybrid', corpus_version='test')
        with self.assertRaisesRegex(ValueError, 'full hybrid'):
            retriever.retrieve(request)
        retriever.graph.retrieve.assert_not_called()


if __name__ == '__main__':
    unittest.main()
