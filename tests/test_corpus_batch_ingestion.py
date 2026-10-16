import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from graph.corpus_batch_ingestion import prepare, sha256_file
from graph.development_ingestion import write_transaction
from test_corpus_pilot_ingestion import Transaction

REPO = Path(__file__).resolve().parents[1]


class CorpusBatchIngestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = prepare(REPO)

    def test_only_supported_review_decisions_are_selected(self):
        payload = self.payload
        self.assertEqual(len(payload['items']),25)
        self.assertEqual(sum(len(i['assertions']) for i in payload['items']),53)
        self.assertEqual(len(payload['excluded_candidates']),15)
        self.assertEqual(sum(e['disposition']=='review' for e in payload['excluded_candidates']),10)
        self.assertEqual(sum(e['disposition']=='reject' for e in payload['excluded_candidates']),5)
        self.assertEqual({a['predicate'] for i in payload['items'] for a in i['assertions']},{'USES','USES_TECHNIQUE'})

    def test_every_assertion_and_mention_matches_source_and_preserves_review_provenance(self):
        for item in self.payload['items']:
            source = item['document']['text']
            for a in item['assertions']:
                self.assertEqual(source[a['evidence_start']:a['evidence_end']],a['evidence_text'])
                self.assertEqual(a['source_review_disposition'],'supported')
                self.assertEqual(a['source_review_sha256'],self.payload['review_manifest_sha256'])
                self.assertEqual(a['human_review_status'],'pending')
                self.assertEqual(a['origin'],'extracted')
                self.assertTrue(a['offline_validation_receipt_sha256'])
                self.assertFalse(any(isinstance(v,dict) for v in a.values()))
            for mention in item['mentions']:
                self.assertEqual(source[mention['evidence_start']:mention['evidence_end']],mention['evidence_text'])

    def test_recovered_candidate_keeps_original_failed_generation_hash(self):
        item = next(i for i in self.payload['items'] if i['chunk']['chunk_id'].endswith(':20899:23542'))
        path = REPO/'work/corpus_extraction_batch/20261015T170956Z-255671f4/22/raw_extraction_2.json'
        raw = path.read_text(encoding='utf-8')
        self.assertEqual(len(json.loads(raw)['relations']),4)
        self.assertEqual(len(item['assertions']),3)
        for a in item['assertions']:
            self.assertEqual(a['raw_output_hash'],hashlib.sha256(raw.encode('utf-8')).hexdigest())
            self.assertEqual(a['source_generation_raw_file_sha256'],sha256_file(path))
            self.assertEqual(a['source_generation_status'],'validation_failed')
            self.assertEqual(json.loads(a['offline_selector_normalization_json'])[0]['original_relation_index'],3)

    def test_changed_original_or_derived_output_blocks_import(self):
        for filename in ['raw_extraction_2.json','derived_selection.json']:
            def changed(path):
                return '0'*64 if Path(path).name==filename else sha256_file(path)
            with self.subTest(filename=filename),patch('graph.corpus_batch_ingestion.sha256_file',side_effect=changed):
                with self.assertRaisesRegex(ValueError,'changed'):
                    prepare(REPO)

    def test_atomic_transaction_verifies_every_assertion(self):
        tx = Transaction(53)
        self.assertEqual(write_transaction(tx,self.payload),53)
        stored = [p['props'] for query,p in tx.calls if query.startswith('MERGE (a:Assertion')]
        self.assertEqual(len({a['assertion_id'] for a in stored}),53)
        with self.assertRaisesRegex(ValueError,'rolled back'):
            write_transaction(Transaction(52),self.payload)

    def test_preview_never_loads_database_driver(self):
        from ingest_corpus_pilot import main
        root = REPO/'work/corpus_batch_ingestion_tests'
        root.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            (Path(tmp)/'docs').mkdir()
            with patch('sys.argv',['ingest_corpus_batch.py','--repo',tmp,'--preview']),patch.dict('sys.modules',{'neo4j':None}),redirect_stdout(io.StringIO()):
                self.assertEqual(main(preparer=lambda repo:self.payload,output_kind='corpus_batch_ingestion',label='corpus batch'),0)
