"""Three-report receipt binding and mocked atomic mitigation import verification."""
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from graph import corpus_extension_mitigations as extension
from tests import test_corpus_pilot_mitigations as base

REPO = Path(__file__).resolve().parents[1]


class CorpusExtensionMitigationTests(base.CorpusPilotMitigationTests):
    @classmethod
    def setUpClass(cls):
        cls.payload = extension.prepare(REPO)
        cls.objects = json.loads((REPO/'data/enterprise-attack-17.1.json').read_bytes())['objects']

    def test_direct_coverage_and_scope_correct_path_counts(self):
        p = self.payload
        self.assertEqual(len(p['source_assertions']),27)
        self.assertEqual(len(p['technique_ids']),15)
        self.assertEqual(len(p['parts']),13)
        self.assertEqual(sum(len(part['records']) for part in p['parts']),48)
        self.assertEqual(len({r['entity']['canonical_id'] for part in p['parts'] for r in part['records']}),26)
        self.assertEqual(p['techniques_without_direct_references'],['T1057','T1082'])
        self.assertEqual(len(p['source_reference_pairs']),53)
        self.assertEqual(len(p['three_hop_chains']),3)
        sources = {a['assertion_id']:a for a in p['source_assertions']}
        references = {r['assertion']['assertion_id']:r['assertion'] for part in p['parts'] for r in part['records']}
        for chain in p['three_hop_chains']:
            actor,software,reference = sources[chain['actor']],sources[chain['source']],references[chain['reference']]
            self.assertEqual(actor['chunk_id'],software['chunk_id'])
            self.assertEqual(actor['source_doc_id'],software['source_doc_id'])
            self.assertEqual(actor['tail_id'],software['head_id'])
            self.assertEqual(software['tail_id'],reference['head_id'])

    def test_transaction_verifies_references_and_is_repeatable(self):
        tx = base.Transaction(self.payload)
        self.assertEqual(extension.write_transaction(tx,self.payload),(48,53,3))
        self.assertEqual(extension.write_transaction(tx,self.payload),(48,53,3))
        self.assertEqual(len(tx.assertions),27+48)
        a = self.payload['parts'][0]['records'][0]['assertion']
        tx.assertions[a['assertion_id']]['validation_status'] = 'human_verified'
        tx.assertions[a['assertion_id']]['human_review_status'] = 'approved'
        extension.write_transaction(tx,self.payload)
        self.assertEqual(tx.assertions[a['assertion_id']]['human_review_status'],'approved')
        self.assertEqual(tx.assertions[a['assertion_id']]['validation_status'],'human_verified')
        tx.assertions[a['assertion_id']]['human_review_status'] = 'rejected'
        with self.assertRaises(ValueError):
            extension.write_transaction(tx,self.payload)

    def test_incomplete_import_receipt_blocks_preparation(self):
        folder = REPO/'work/corpus_extension_ingestion'/extension.IMPORT_RUN
        original = Path.read_text
        for filename,key,value in [('import_receipt.json','verified_assertion_count',26),
                                    ('import_receipt.json','status','preview'),
                                    ('import_receipt.json','review_manifest_sha256','changed'),
                                    ('prepared_records.json','offline_validation_receipt_sha256','changed')]:
            def changed(target,*args,**kwargs):
                text = original(target,*args,**kwargs)
                if target==folder/filename:
                    data = json.loads(text)
                    data[key] = value
                    return json.dumps(data)
                return text
            with self.subTest(filename=filename,key=key),patch.object(Path,'read_text',changed):
                with self.assertRaises(ValueError):
                    extension.prepare(REPO)

    def test_extension_reference_preview_never_loads_database_driver(self):
        from import_corpus_pilot_mitigations import main
        root = REPO/'work/corpus_extension_mitigation_tests'
        root.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            (Path(tmp)/'docs').mkdir()
            with patch('sys.argv',['import_corpus_extension_mitigations.py','--repo',tmp,'--preview']),patch.dict(
                    'sys.modules',{'neo4j':None}),redirect_stdout(io.StringIO()):
                self.assertEqual(main(preparer=lambda repo:self.payload,output_kind='corpus_extension_mitigations',
                                      label='Three-report extension'),0)


if __name__ == '__main__':
    unittest.main()
