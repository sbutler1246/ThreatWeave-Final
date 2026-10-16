"""Additional-batch receipt binding and atomic reference verification, without services."""
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from graph import corpus_batch_mitigations as batch
from tests import test_corpus_pilot_mitigations as base

REPO = Path(__file__).resolve().parents[1]


class CorpusBatchMitigationTests(base.CorpusPilotMitigationTests):
    @classmethod
    def setUpClass(cls):
        cls.payload = batch.prepare(REPO)
        cls.objects = json.loads((REPO/'data/enterprise-attack-17.1.json').read_bytes())['objects']

    def test_direct_coverage_and_scope_correct_path_counts(self):
        p = self.payload
        self.assertEqual(len(p['source_assertions']), 53)
        self.assertEqual(len(p['technique_ids']), 19)
        self.assertEqual(len(p['parts']), 16)
        self.assertEqual(sum(len(part['records']) for part in p['parts']), 51)
        self.assertEqual(len({r['entity']['canonical_id'] for part in p['parts'] for r in part['records']}), 26)
        self.assertEqual(p['techniques_without_direct_references'], ['T1012','T1057','T1070.004'])
        self.assertEqual(len(p['source_reference_pairs']), 59)
        self.assertEqual(len(p['three_hop_chains']), 4)
        sources = {a['assertion_id']:a for a in p['source_assertions']}
        for chain in p['three_hop_chains']:
            actor, software = sources[chain['actor']], sources[chain['source']]
            self.assertEqual(actor['chunk_id'], software['chunk_id'])
            self.assertEqual(actor['source_doc_id'], software['source_doc_id'])
            self.assertEqual(actor['tail_id'], software['head_id'])

    def test_transaction_verifies_references_and_is_repeatable(self):
        tx = base.Transaction(self.payload)
        self.assertEqual(batch.write_transaction(tx, self.payload), (51,59,4))
        self.assertEqual(batch.write_transaction(tx, self.payload), (51,59,4))
        self.assertEqual(len(tx.assertions), 53+51)
        a = self.payload['parts'][0]['records'][0]['assertion']
        tx.assertions[a['assertion_id']]['validation_status'] = 'human_verified'
        tx.assertions[a['assertion_id']]['human_review_status'] = 'approved'
        batch.write_transaction(tx, self.payload)
        self.assertEqual(tx.assertions[a['assertion_id']]['human_review_status'], 'approved')
        self.assertEqual(tx.assertions[a['assertion_id']]['validation_status'], 'human_verified')
        tx.assertions[a['assertion_id']]['human_review_status'] = 'rejected'
        with self.assertRaises(ValueError):
            batch.write_transaction(tx, self.payload)

    def test_incomplete_import_receipt_blocks_preparation(self):
        folder = REPO/'work/corpus_batch_ingestion'/batch.IMPORT_RUN
        original = Path.read_text
        for filename, key, value in [
                ('import_receipt.json','verified_assertion_count',52),
                ('import_receipt.json','status','preview'),
                ('prepared_records.json','offline_validation_receipt_sha256','changed')]:
            def changed(target, *args, **kwargs):
                text = original(target, *args, **kwargs)
                if target == folder/filename:
                    data = json.loads(text)
                    data[key] = value
                    return json.dumps(data)
                return text
            with self.subTest(filename=filename, key=key), patch.object(Path, 'read_text', changed):
                with self.assertRaises(ValueError):
                    batch.prepare(REPO)


if __name__ == '__main__':
    unittest.main()
