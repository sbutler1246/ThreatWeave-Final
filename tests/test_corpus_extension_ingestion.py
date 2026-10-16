"""Frozen extension review selection, recovered provenance and mocked atomic imports."""
import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from graph.corpus_extension_ingestion import prepare
from graph.development_ingestion import write_transaction
from extraction.llama_tokenizer import sha256_file
from test_corpus_pilot_ingestion import Transaction

REPO = Path(__file__).resolve().parents[1]
RUN = REPO/'work/corpus_extension_extraction/20261016T000937Z-0cef6551'
ARTIFACTS = REPO/'work/corpus_extension_review_checks/20261016T001318Z-ae84a38a'


class CorpusExtensionIngestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = prepare(REPO)

    def test_only_supported_assertions_enter_the_twelve_source_windows(self):
        p = self.payload
        self.assertEqual(len(p['items']),12)
        self.assertEqual(sum(len(i['assertions']) for i in p['items']),27)
        self.assertEqual(len({e['canonical_id'] for i in p['items'] for e in i['entities']}),27)
        self.assertEqual(len(p['excluded_candidates']),19)
        self.assertEqual(sum(d['disposition']=='review' for d in p['excluded_candidates']),9)
        self.assertEqual(sum(d['disposition']=='reject' for d in p['excluded_candidates']),10)
        self.assertEqual({i['document']['doc_id'] for i in p['items']},{'AA24-038A','AA23-144A','AA22-321A'})
        self.assertTrue(all(a['predicate'] in {'USES','USES_TECHNIQUE'} for i in p['items'] for a in i['assertions']))

    def test_exact_support_and_mention_spans_with_pending_human_review(self):
        for item in self.payload['items']:
            source = item['document']['text']
            for a in item['assertions']:
                self.assertEqual(source[a['evidence_start']:a['evidence_end']],a['evidence_text'])
                self.assertEqual(a['source_review_disposition'],'supported')
                self.assertEqual(a['source_review_sha256'],self.payload['review_manifest_sha256'])
                self.assertEqual(a['human_review_status'],'pending')
                self.assertEqual(a['origin'],'extracted')
                self.assertEqual(a['offline_validation_receipt_sha256'],sha256_file(ARTIFACTS/'receipt.json'))
            for m in item['mentions']:
                self.assertEqual(source[m['evidence_start']:m['evidence_end']],m['evidence_text'])

    def test_recovery_preserves_failed_raw_output_and_only_imports_supported_subset(self):
        item = next(i for i in self.payload['items'] if i['chunk']['chunk_id'].endswith(':22202:24566'))
        raw_path = RUN/'08/raw_extraction_2.json'
        raw = raw_path.read_text(encoding='utf-8')
        self.assertEqual(len(json.loads(raw)['relations']),4)
        self.assertEqual(len(json.loads((ARTIFACTS/'08/derived_selection.json').read_text(encoding='utf-8'))['relations']),3)
        self.assertEqual(len(item['assertions']),2)
        for a in item['assertions']:
            self.assertEqual(a['raw_output_hash'],hashlib.sha256(raw.encode('utf-8')).hexdigest())
            self.assertEqual(a['source_generation_raw_file_sha256'],sha256_file(raw_path))
            self.assertEqual(a['source_generation_status'],'validation_failed')
            change = json.loads(a['offline_selector_normalization_json'])[0]
            self.assertEqual(change['original_relation_index'],2)
            self.assertEqual(change['retained_original_relation_index'],0)
        summary = json.loads((RUN/'summary.json').read_text(encoding='utf-8'))
        self.assertEqual(summary['items'][7]['status'],'validation_failed')
        receipt = json.loads((ARTIFACTS/'receipt.json').read_text(encoding='utf-8'))
        self.assertEqual(receipt['original_summary_sha256'],sha256_file(RUN/'summary.json'))
        self.assertFalse(receipt['service_calls'])
        self.assertFalse(receipt['graph_writes'])

    def test_ambiguous_qualifications_and_wrong_endpoint_roles_are_excluded(self):
        excluded = {(d['folder'],d['relation_index']):d for d in self.payload['excluded_candidates']}
        for key in [('02',0),('05',2),('07',1),('08',2),('09',0),('22',0)]:
            self.assertEqual(excluded[key]['disposition'],'reject')
        for key in [('05',1),('06',1),('09',2),('09',3),('17',0),('17',1),('30',1),('31',0),('33',0)]:
            self.assertEqual(excluded[key]['disposition'],'review')
        # Likely qualifies rar.exe identity only: observed ronf.exe compression remains accepted.
        archive = next(i for i in self.payload['items'] if i['chunk']['chunk_id'].endswith(':30941:33296'))
        self.assertEqual(len(archive['assertions']),4)
        self.assertFalse(any(e['name']=='rar.exe' for e in archive['entities']))

    def test_tampered_raw_derived_or_validation_policy_blocks_import(self):
        for filename in ['raw_extraction_2.json','derived_selection.json','check_corpus_extension.py']:
            def changed(path):
                return '0'*64 if Path(path).name==filename else sha256_file(path)
            with self.subTest(filename=filename),patch('graph.corpus_batch_ingestion.sha256_file',side_effect=changed):
                with self.assertRaisesRegex(ValueError,'changed'):
                    prepare(REPO)

    def test_review_must_cover_all_candidate_dispositions(self):
        original = Path.read_text
        target = REPO/'docs/ThreatWeave_corpus_extension_source_review.json'
        def changed(path,*args,**kwargs):
            value = original(path,*args,**kwargs)
            if path==target:
                data = json.loads(value)
                data['windows'][3]['decisions'].pop()
                return json.dumps(data)
            return value
        with patch.object(Path,'read_text',changed),self.assertRaisesRegex(ValueError,'every candidate'):
            prepare(REPO)

    def test_mocked_atomic_transaction_verifies_all_selected_assertions(self):
        tx = Transaction(27)
        self.assertEqual(write_transaction(tx,self.payload),27)
        stored = [p['props'] for q,p in tx.calls if q.startswith('MERGE (a:Assertion')]
        self.assertEqual(len({a['assertion_id'] for a in stored}),27)
        with self.assertRaisesRegex(ValueError,'rolled back'):
            write_transaction(Transaction(26),self.payload)

    def test_extension_preview_does_not_load_database_driver(self):
        from ingest_corpus_pilot import main
        root = REPO/'work/corpus_extension_ingestion_tests'
        root.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            (Path(tmp)/'docs').mkdir()
            with patch('sys.argv',['ingest_corpus_extension.py','--repo',tmp,'--preview']),patch.dict(
                    'sys.modules',{'neo4j':None}),redirect_stdout(io.StringIO()):
                self.assertEqual(main(preparer=lambda repo:self.payload,output_kind='corpus_extension_ingestion',
                                      label='three-report extension'),0)


if __name__ == '__main__':
    unittest.main()
