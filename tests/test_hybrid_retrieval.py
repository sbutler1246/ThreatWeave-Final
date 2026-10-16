"""Node2Vec neighbor boundaries, candidate ranking and freshness guards."""
import unittest
from pathlib import Path
from unittest.mock import MagicMock
from types import SimpleNamespace

import numpy as np

from retrieval.graph_vectors import GraphVectorIndex, neighbor_priority, rank_candidates, require_current_projection
from retrieval.hybrid_retrieval import DevelopmentHybridRetriever, enumerate_paths
from graph.development_projection import preview_projection
from graph.development_retrieval import DevelopmentGraphRetriever, seed_groups


class HybridTests(unittest.TestCase):
    def index(self):
        index = GraphVectorIndex.__new__(GraphVectorIndex)
        index.nodes = {i: {'name': i, 'type': 'Software'} for i in ['seed', 'other', 'neighbor', 'foreign']}
        index.manifest = {'projection_sha256': 'projection', 'index_fingerprint': 'index',
            'component_by_node': {'seed': 'a', 'other': 'a', 'neighbor': 'a', 'foreign': 'b'}}
        index.vectors = {i: np.ones(128)/np.sqrt(128) for i in index.nodes}
        index.collection = MagicMock()
        return index

    def test_stale_projection_and_missing_assets_block_full_hybrid(self):
        with self.assertRaisesRegex(ValueError, 'Live accepted graph differs'):
            require_current_projection({'projection_sha256': 'old'}, 'new')
        require_current_projection({'projection_sha256': 'same'}, 'same')
        with self.assertRaisesRegex(ValueError, 'requires a ready graph-vector index'):
            GraphVectorIndex(Path(__file__).resolve().parent/'nonexistent-graph-index-fixture', {})

    def test_neighbors_exclude_all_seeds_and_query_their_component(self):
        index = self.index()
        ids = ['seed', 'other', 'neighbor']
        index.collection.query.return_value = {'ids': [ids], 'metadatas': [[index.metadata(i) for i in ids]],
                                               'distances': [[0.0, 0.1, 0.2]]}
        neighbors = index.neighbors(['seed', 'other'], count=5)
        self.assertTrue(all([h['canonical_id'] for h in hits] == ['neighbor'] for hits in neighbors.values()))
        self.assertEqual(index.collection.query.call_args.kwargs['where'], {'component_id': 'a'})
        self.assertEqual(len(index.collection.query.call_args.kwargs['query_embeddings'][0]), 128)

    def test_cross_component_or_altered_metadata_is_rejected(self):
        index = self.index()
        index.collection.query.return_value = {'ids': [['foreign']], 'metadatas': [[index.metadata('foreign')]],
                                               'distances': [[0.1]]}
        with self.assertRaisesRegex(ValueError, 'component mismatch'):
            index.neighbors(['seed'])
        meta = index.metadata('neighbor')
        meta['index_fingerprint'] = 'incorrect'
        index.collection.query.return_value = {'ids': [['neighbor']], 'metadatas': [[meta]], 'distances': [[0.1]]}
        with self.assertRaises(ValueError):
            index.neighbors(['seed'])

    def test_unknown_seed_and_nonfinite_distance_are_rejected(self):
        index = self.index()
        with self.assertRaisesRegex(ValueError, 'absent'):
            index.neighbors(['unknown'])
        index.collection.query.return_value = {'ids': [['neighbor']],
            'metadatas': [[index.metadata('neighbor')]], 'distances': [[float('nan')]]}
        with self.assertRaisesRegex(ValueError, 'non-finite'):
            index.neighbors(['seed'])

    def test_neighbor_rank_support_is_not_counted_repeatedly_per_seed(self):
        values = {'a': [{'canonical_id': 'n'}], 'b': [{'canonical_id': 'm'}, {'canonical_id': 'n'}]}
        scores = neighbor_priority(values)
        self.assertAlmostEqual(scores['n'], 1/61)

    def test_learned_neighbor_priority_changes_order_and_respects_candidate_cap(self):
        path = lambda tail: {'nodes': [{'canonical_id': 'seed'}, {'canonical_id': tail}],
                             'edges': [{'predicate': 'USES', 'assertion_ids': ['proof-'+tail]}]}
        base, expanded = [path('a'), path('n')], [path('n')]
        selected, scores = rank_candidates(base, expanded, {'n': 1/61}, 1)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]['nodes'][-1]['canonical_id'], 'n')
        self.assertEqual(len(scores), 1)

    def test_saved_projection_enumeration_preserves_direction_and_hop_limit(self):
        nodes = {i: {'canonical_id': i} for i in ['g', 's', 't', 'm', 'x']}
        edges = [{'head_id': a, 'tail_id': b, 'predicate': p,
                  'support': [{'assertion': {'assertion_id': a+b}}]} for a, b, p in
                 [('g', 's', 'USES'), ('s', 't', 'USES_TECHNIQUE'), ('t', 'm', 'MITIGATED_BY')]]
        paths = enumerate_paths({'edges': edges}, nodes, 3)
        self.assertTrue(any([n['canonical_id'] for n in p['nodes']] == ['g', 's', 't', 'm'] for p in paths))
        self.assertTrue(all(1 <= len(p['edges']) <= 3 for p in paths))
        self.assertFalse(any(p['nodes'][0]['canonical_id'] in {'m', 'x'} for p in paths))

    def test_neighbor_priority_reaches_the_actual_source_evidence_packer(self):
        graph = DevelopmentGraphRetriever(Path(__file__).resolve().parents[1],include_corpus_pilot=False)
        projection, _, _, records = preview_projection(graph)
        paths = enumerate_paths(projection, graph.expected_entities)
        groups = seed_groups('How do LockBit Affiliates use AnyDesk?', list(graph.expected_entities.values()))
        target = next(p for p in paths if len(p['edges']) == 3
            and p['nodes'][1]['name'] == 'AnyDesk' and p['nodes'][-1]['canonical_id'] == 'attack:M1042')
        from retrieval.graph_vectors import path_key
        graph.max_paths = 1
        bundle = graph.assemble(paths, records, groups, path_priority={path_key(target): 1})
        self.assertEqual(len(bundle.paths), 1)
        self.assertEqual(bundle.paths[0].edges[-1].tail_id, 'attack:M1042')
        self.assertTrue(all(set(e.citation_ids) <= set(bundle.citation_ids) for e in bundle.paths[0].edges))

    def test_live_staleness_stops_before_any_neighbor_lookup(self):
        graph = DevelopmentGraphRetriever(Path(__file__).resolve().parents[1],include_corpus_pilot=False)
        _, _, edges, records = preview_projection(graph)
        hybrid = DevelopmentHybridRetriever.__new__(DevelopmentHybridRetriever)
        hybrid.graph, hybrid.config, hybrid.mentions = graph, graph.config, []
        hybrid.index = MagicMock()
        hybrid.index.nodes = graph.expected_entities
        hybrid.index.manifest = {'projection_sha256': 'different-revision'}
        tx = MagicMock()
        tx.run.side_effect = [[SimpleNamespace(data=lambda r=r: r) for r in edges],
                              [SimpleNamespace(data=lambda r=r: r) for r in records]]
        graph.driver = MagicMock()
        graph.driver.session.return_value.__enter__.return_value.execute_read.side_effect = lambda read: read(tx)
        with self.assertRaisesRegex(ValueError, 'Live accepted graph differs'):
            hybrid._graph_branch('How do LockBit Affiliates use AnyDesk?', False)
        hybrid.index.neighbors.assert_not_called()


if __name__ == '__main__':
    unittest.main()
