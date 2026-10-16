"""Reviewed scope parity, pinned evidence, graph previews and seed disambiguation."""
import copy
import hashlib
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from graph.development_projection import freeze_projection, preview_projection
from graph.development_retrieval import DevelopmentGraphRetriever, seed_groups
from graph_qa import DEMO_QUESTIONS
from retrieval.development_text import parents
from retrieval.hybrid_retrieval import saved_projection_rows, source_mentions

REPO = Path(__file__).resolve().parents[1]


class ExpandedDevelopmentScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = DevelopmentGraphRetriever(REPO,include_corpus_batch=False)
        cls.projection, cls.fingerprint, cls.edges, cls.rows = preview_projection(cls.graph)

    def test_reviewed_expansion_has_expected_sources_references_and_domain_only_graph(self):
        self.assertEqual(len(self.graph.profiles), 16)
        self.assertEqual(len(self.graph.references), 58)
        self.assertEqual(len(self.projection['nodes']), 75)
        self.assertEqual(len(self.projection['edges']), 102)
        approved = [a for p in self.graph.profiles.values() for a in p.get('accepted_assertions',{}).values()]
        self.assertEqual(len(approved), 34)
        self.assertTrue(all(a['source_review_disposition']=='supported' for a in approved))
        self.assertNotIn('attack:T1566', self.graph.expected_entities)
        self.assertTrue(all(n['type'] not in {'Document','Chunk','Assertion'} for n in self.projection['nodes']))

    def test_text_and_graph_use_the_same_source_parents_and_reference_pool(self):
        selected, config = parents(REPO,include_corpus_batch=False)
        actual = {chunk.chunk_id for _,chunk,_ in selected}
        expected = set(self.graph.profiles) | {r['chunk']['chunk_id'] for r in self.graph.references.values()}
        self.assertEqual(actual, expected)
        self.assertEqual(config['development_scope'], self.graph.config['development_scope'])
        for doc, chunk, _ in selected:
            self.assertEqual(doc.text[chunk.start:chunk.end], chunk.text)

    def test_all_new_demo_questions_have_bounded_source_fixture_evidence(self):
        for question in DEMO_QUESTIONS:
            with self.subTest(question=question):
                bundle = self.graph.preview(question)
                self.assertTrue(bundle.paths)
                self.assertLessEqual(len(self.graph.last_context.encode('utf-8')), self.graph.byte_cap)
                self.assertTrue(all(set(e.citation_ids) <= set(bundle.citation_ids) for p in bundle.paths for e in p.edges))
        first = self.graph.preview(DEMO_QUESTIONS[0])
        self.assertTrue(any(len(p.edges)==3 for p in first.paths))
        self.assertTrue(any(p.source_kind=='attack' for p in first.passages))
        second = self.graph.preview(DEMO_QUESTIONS[1])
        self.assertTrue(all(any(e.head_id=='attack:T1078' or e.tail_id=='attack:T1078' for e in p.edges) for p in second.paths))
        third = self.graph.preview(DEMO_QUESTIONS[2])
        tails = {self.graph.expected_entities[p.edges[-1].tail_id]['name'] for p in third.paths}
        self.assertEqual(tails, {'AnyDesk','Mega sync'})

    def test_nested_software_name_does_not_override_full_actor_but_independent_mention_survives(self):
        entities = list(self.graph.expected_entities.values())
        software = next(e['canonical_id'] for e in entities if e['name']=='Rhysida' and e['type']=='Software')
        actor = next(e['canonical_id'] for e in entities if e['name']=='Rhysida actors' and e['type']=='ThreatGroup')
        first = {i for group in seed_groups('Rhysida actors use valid accounts (T1078).',entities) for i in group}
        self.assertIn(actor, first)
        self.assertNotIn(software, first)
        second = {i for group in seed_groups('Compare Rhysida actors with Rhysida ransomware.',entities) for i in group}
        self.assertIn(actor, second)
        self.assertIn(software, second)

    def test_only_pinned_assertions_and_review_metadata_can_enter_new_scopes(self):
        row = next(r for r in self.rows if r['assertion'].get('source_review_sha256'))
        a = row['assertion']
        triple = a['head_id'], a['predicate'], a['tail_id']
        changed = copy.deepcopy(row)
        changed['assertion']['assertion_id'] = 'not-the-reviewed-model-output'
        self.assertIsNone(self.graph._verify_record(changed, *triple))
        changed = copy.deepcopy(row)
        changed['assertion']['source_review_sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'pinned supported source review'):
            self.graph._verify_record(changed, *triple)

    def test_saved_projection_retains_review_provenance_for_full_hybrid_revalidation(self):
        rows = saved_projection_rows(SimpleNamespace(projection=self.projection), self.graph)
        restored, fingerprint = freeze_projection(self.graph, self.edges, rows)
        self.assertEqual(fingerprint, self.fingerprint)
        self.assertEqual(restored, self.projection)
        self.assertEqual(sum('source_record' in s for e in restored['edges'] for s in e['support']),34)

    def test_expanded_scope_changes_runtime_identity_from_original_baseline(self):
        baseline = DevelopmentGraphRetriever(REPO,include_corpus_pilot=False)
        self.assertEqual(len(baseline.profiles),6)
        self.assertNotEqual(baseline.configuration_hash, self.graph.configuration_hash)
        self.assertNotEqual(baseline.config['development_scope']['sha256'],self.graph.config['development_scope']['sha256'])

    def test_incomplete_mitigation_receipt_prevents_scope_expansion(self):
        receipt = REPO/'work/corpus_pilot_mitigations/20261015T041247Z-529903c7/import_receipt.json'
        original = Path.read_text
        def changed(target, *args, **kwargs):
            text = original(target, *args, **kwargs)
            if target == receipt:
                value = json.loads(text)
                value['reference_assertion_count'] = 54
                return json.dumps(value)
            return text
        with patch.object(Path, 'read_text', changed):
            with self.assertRaisesRegex(ValueError, 'completed corpus-pilot mitigation import receipt'):
                DevelopmentGraphRetriever(REPO)


if __name__ == '__main__':
    unittest.main()
