"""Frozen-reference coverage and source-anchored transaction verification without services."""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from graph import corpus_pilot_mitigations as pilot
from import_pilot_mitigations import reference_records, write_transaction as legacy_write

REPO = Path(__file__).resolve().parents[1]


class Result:
    def __init__(self, value=None):
        self.value = value
    def single(self):
        return self.value
    def consume(self):
        return None


class Transaction:
    def __init__(self, payload):
        self.assertions = {a['assertion_id']:copy.deepcopy(a) for a in payload['source_assertions']}
        self.techniques = {p['technique']['canonical_id']:p['technique'] for p in payload['parts']}
        self.writes = []
        self.missing_edges = False
        self.incomplete_paths = False
    def run(self, query, **params):
        if query == pilot.ASSERTIONS_QUERY:
            return [{'props':self.assertions[i]} for i in params['ids'] if i in self.assertions]
        if query == pilot.EDGES_QUERY:
            return Result({'verified':len(params['facts'])-(1 if self.missing_edges else 0)})
        if query in {pilot.EXTENSIONS_QUERY,pilot.CHAINS_QUERY}:
            key = 'pairs' if query == pilot.EXTENSIONS_QUERY else 'chains'
            return Result({'verified':len(params[key])-(1 if self.incomplete_paths else 0)})
        if query.startswith('MATCH (t:Entity:Technique') and 'id' in params:
            return Result({'props':self.techniques[params['id']]})
        if query.startswith('MATCH (a:Assertion {assertion_id:$id})'):
            previous = self.assertions.get(params['id'])
            return Result({'props':previous} if previous else None)
        if query.startswith('MERGE '):
            self.writes.append((query, params))
            if query.startswith('MERGE (a:Assertion'):
                self.assertions[params['id']] = dict(params['props'])
        return Result()


class CorpusPilotMitigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = pilot.prepare(REPO)
        cls.objects = json.loads((REPO/'data/enterprise-attack-17.1.json').read_bytes())['objects']

    def test_direct_coverage_and_scope_correct_path_counts(self):
        p = self.payload
        self.assertEqual(len(p['technique_ids']), 18)
        self.assertEqual(len(p['parts']), 15)
        self.assertEqual(sum(len(part['records']) for part in p['parts']), 55)
        self.assertEqual(len({r['entity']['canonical_id'] for part in p['parts'] for r in part['records']}), 27)
        self.assertEqual(p['techniques_without_direct_references'], ['T1018','T1069.002','T1217'])
        self.assertEqual(len(p['source_reference_pairs']), 72)
        self.assertEqual(len(p['three_hop_chains']), 6)
        sources = {a['assertion_id']:a for a in p['source_assertions']}
        for chain in p['three_hop_chains']:
            actor, software = sources[chain['actor']], sources[chain['source']]
            self.assertEqual(actor['chunk_id'], software['chunk_id'])
            self.assertEqual(actor['source_doc_id'], software['source_doc_id'])
            self.assertEqual(actor['tail_id'], software['head_id'])

    def test_no_reference_cases_are_explicit_and_legacy_error_remains(self):
        technique, links = reference_records(self.objects, 'T1069.002', allow_empty=True)
        self.assertEqual(links, [])
        parent, parent_links = reference_records(self.objects, 'T1069', allow_empty=True)
        self.assertNotEqual(technique['id'], parent['id'])
        with self.assertRaisesRegex(ValueError, 'No active mitigation'):
            reference_records(self.objects, 'T1069.002')
        with self.assertRaisesRegex(ValueError, 'Expected one active'):
            reference_records(self.objects, 'T9999', allow_empty=True)

    def test_reference_direction_source_text_and_extracted_origin_separation(self):
        by_id = {o['id']:o for o in self.objects}
        for part in self.payload['parts']:
            for record in part['records']:
                a = record['assertion']
                original = by_id[a['source_stix_relationship_id']]
                self.assertEqual(original['relationship_type'], 'mitigates')
                self.assertEqual(original['target_ref'], part['technique']['stix_id'])
                self.assertEqual(original['source_ref'], record['entity']['stix_id'])
                self.assertEqual(a['origin'], 'fused')
                self.assertEqual(a['evidence_text'], original['description'])
                self.assertEqual(record['document']['text'][a['evidence_start']:a['evidence_end']], a['evidence_text'])
        self.assertTrue(all(a['origin']=='extracted' for a in self.payload['source_assertions']))

    def test_missing_or_changed_source_assertions_block_before_reference_writes(self):
        first = self.payload['source_assertions'][0]['assertion_id']
        for change in ['missing','evidence','rejected']:
            tx = Transaction(self.payload)
            if change == 'missing':
                del tx.assertions[first]
            elif change == 'evidence':
                tx.assertions[first]['evidence_text'] = 'changed'
            else:
                tx.assertions[first]['human_review_status'] = 'rejected'
            with self.subTest(change=change), self.assertRaises(ValueError):
                pilot.write_transaction(tx, self.payload)
            self.assertEqual(tx.writes, [])

    def test_transaction_verifies_references_and_is_repeatable(self):
        tx = Transaction(self.payload)
        self.assertEqual(pilot.write_transaction(tx, self.payload), (55,72,6))
        self.assertEqual(pilot.write_transaction(tx, self.payload), (55,72,6))
        self.assertEqual(len(tx.assertions), 34+55)
        a = self.payload['parts'][0]['records'][0]['assertion']
        tx.assertions[a['assertion_id']]['validation_status'] = 'human_verified'
        tx.assertions[a['assertion_id']]['human_review_status'] = 'approved'
        pilot.write_transaction(tx, self.payload)
        self.assertEqual(tx.assertions[a['assertion_id']]['validation_status'], 'human_verified')
        self.assertEqual(tx.assertions[a['assertion_id']]['human_review_status'], 'approved')
        tx.assertions[a['assertion_id']]['validation_status'] = 'rejected'
        with self.assertRaisesRegex(ValueError, 'rejected'):
            pilot.write_transaction(tx, self.payload)

    def test_missing_edges_or_incomplete_extensions_fail_verification(self):
        for key in ['missing_edges','incomplete_paths']:
            tx = Transaction(self.payload)
            setattr(tx, key, True)
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, 'rolled back'):
                pilot.write_transaction(tx, self.payload)

    def test_incomplete_import_receipt_blocks_preparation(self):
        path = REPO/'work/corpus_pilot_ingestion'/pilot.IMPORT_RUN/'import_receipt.json'
        original = Path.read_text
        def changed(target, *args, **kwargs):
            text = original(target, *args, **kwargs)
            if target == path:
                value = json.loads(text)
                value['verified_assertion_count'] = 33
                return json.dumps(value)
            return text
        with patch.object(Path, 'read_text', changed):
            with self.assertRaisesRegex(ValueError, 'completed pilot import receipt'):
                pilot.prepare(REPO)

    def test_legacy_import_still_requires_its_original_source_chain(self):
        class MissingChain:
            def run(self, *args, **kwargs):
                return Result({'paths':0})
        with self.assertRaisesRegex(ValueError, 'accepted CISA pilot chain'):
            legacy_write(MissingChain(), self.payload['parts'][0])


if __name__ == '__main__':
    unittest.main()
