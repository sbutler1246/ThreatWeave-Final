"""Projection provenance, identity checks, graph completeness and revision hashes."""
import copy
import unittest
from pathlib import Path

from graph.development_projection import freeze_projection, preview_projection, undirected_graph
from graph.development_retrieval import DevelopmentGraphRetriever

REPO = Path(__file__).resolve().parents[1]


class ProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.retriever = DevelopmentGraphRetriever(REPO,include_corpus_pilot=False)
        cls.projection, cls.fingerprint, cls.edges, cls.records = preview_projection(cls.retriever)

    def freeze(self, edges=None, records=None):
        return freeze_projection(self.retriever, self.edges if edges is None else edges,
                                 self.records if records is None else records)

    def test_projection_contains_only_source_verified_domain_facts(self):
        graph = undirected_graph(self.projection)
        self.assertEqual(graph.number_of_nodes(), 22)
        self.assertEqual(len(self.projection['edges']), 23)
        self.assertEqual(graph.number_of_edges(), 23)
        self.assertTrue(all(n['type'] not in {'Document', 'Chunk', 'Assertion'} for n in self.projection['nodes']))
        self.assertTrue(all(e['support'] for e in self.projection['edges']))

    def test_revision_hash_is_independent_of_query_row_order(self):
        p, fingerprint = self.freeze(list(reversed(self.edges)), list(reversed(self.records)))
        self.assertEqual(p, self.projection)
        self.assertEqual(fingerprint, self.fingerprint)

    def test_missing_or_rejected_fact_cannot_produce_ready_projection(self):
        with self.assertRaisesRegex(ValueError, 'absent'):
            self.freeze(edges=self.edges[1:])
        records = copy.deepcopy(self.records)
        records[0]['assertion']['validation_status'] = 'rejected'
        with self.assertRaisesRegex(ValueError, 'accepted source evidence'):
            self.freeze(records=records)

    def test_source_quote_and_document_tampering_are_rejected(self):
        for field in ['quote', 'document']:
            records = copy.deepcopy(self.records)
            if field == 'quote':
                records[0]['assertion']['evidence_text'] = 'Invented source.'
            else:
                records[0]['document']['text'] += ' Altered.'
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.freeze(records=records)

    def test_unverified_alias_and_conflicting_name_are_rejected(self):
        for field in ['aliases', 'name']:
            edges = copy.deepcopy(self.edges)
            if field == 'aliases':
                edges[0]['head']['aliases'] = edges[0]['head'].get('aliases', [])+['Unverified Alias']
            else:
                edges[0]['head']['name'] = 'Incorrect name'
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.freeze(edges=edges)

    def test_duplicate_relationships_are_not_silently_collapsed(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate stored relationships'):
            self.freeze(edges=self.edges+[self.edges[0]])

    def test_accepted_review_status_change_invalidates_revision(self):
        records = copy.deepcopy(self.records)
        records[0]['assertion']['validation_status'] = 'human_verified'
        _, fingerprint = self.freeze(records=records)
        self.assertNotEqual(fingerprint, self.fingerprint)

    def test_incidental_database_timestamp_is_excluded_from_revision(self):
        edges = copy.deepcopy(self.edges)
        edges[0]['head']['updated_at'] = '2026-10-14T00:00:00Z'
        _, fingerprint = self.freeze(edges=edges)
        self.assertEqual(fingerprint, self.fingerprint)


if __name__ == '__main__':
    unittest.main()
