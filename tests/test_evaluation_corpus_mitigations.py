"""Evaluation receipt binding, direct reference coverage and mocked writes."""
import copy
import io
import json
import tempfile
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from evaluation import corpus_mitigations as evaluation
from tests import test_corpus_pilot_mitigations as base

REPO = Path(__file__).resolve().parents[1]


class EvaluationCorpusMitigationTests(base.CorpusPilotMitigationTests):
    @classmethod
    def setUpClass(cls):
        original = Path.read_text
        def guarded(path,*args,**kwargs):
            if path.name in {'gold_triples.json','eval_queries.json','reference_triples.json'}:
                raise AssertionError('Evaluation labels are forbidden for reference preparation.')
            return original(path,*args,**kwargs)
        with patch.object(Path,'read_text',guarded),patch('requests.Session',side_effect=AssertionError('No services')):
            cls.payload = evaluation.prepare(REPO)
        cls.objects = json.loads((REPO/'data/enterprise-attack-17.1.json').read_bytes())['objects']
        cls.predictions = json.loads((REPO/'work/evaluation_corpus_ingestion'/evaluation.IMPORT_RUN/'prepared_records.json').read_text(encoding='utf-8'))

    def test_direct_coverage_and_scope_correct_path_counts(self):
        p = self.payload
        self.assertEqual(len(p['source_assertions']),118)
        self.assertEqual(len(p['technique_ids']),34)
        self.assertEqual(len(p['parts']),29)
        self.assertEqual(sum(len(part['records']) for part in p['parts']),109)
        self.assertEqual(len({r['entity']['canonical_id'] for part in p['parts'] for r in part['records']}),34)
        self.assertEqual(p['techniques_without_direct_references'],['T1016','T1018','T1069.001','T1069.002','T1083'])
        self.assertEqual(len(p['source_reference_pairs']),203)
        self.assertEqual(p['three_hop_chains'],[])
        self.assertEqual(p['source_scope_assignment'],'evaluation')
        self.assertTrue(all(a['scope_assignment']=='evaluation' and
                        a['evaluation_plan_fingerprint']==p['evaluation_plan_fingerprint'] for a in p['source_assertions']))
        sources = {a['assertion_id']:a for a in p['source_assertions']}
        refs = {r['assertion']['assertion_id']:r['assertion'] for part in p['parts'] for r in part['records']}
        for pair in p['source_reference_pairs']:
            self.assertEqual(sources[pair['source']]['tail_id'],refs[pair['reference']]['head_id'])
        for identifier in p['techniques_without_direct_references']:
            self.assertFalse(any(r['head_id']=='attack:'+identifier for r in refs.values()))

    def test_transaction_verifies_references_and_is_repeatable(self):
        tx = base.Transaction(self.payload)
        self.assertEqual(evaluation.write_transaction(tx,self.payload),(109,203,0))
        self.assertEqual(evaluation.write_transaction(tx,self.payload),(109,203,0))
        self.assertEqual(len(tx.assertions),227)
        reference = self.payload['parts'][0]['records'][0]['assertion']
        tx.assertions[reference['assertion_id']].update(validation_status='human_verified',human_review_status='approved')
        evaluation.write_transaction(tx,self.payload)
        self.assertEqual(tx.assertions[reference['assertion_id']]['validation_status'],'human_verified')
        self.assertEqual(tx.assertions[reference['assertion_id']]['human_review_status'],'approved')
        tx.assertions[reference['assertion_id']]['human_review_status']='rejected'
        with self.assertRaises(ValueError):
            evaluation.write_transaction(tx,self.payload)

    def test_incomplete_import_receipt_blocks_preparation(self):
        folder = REPO/'work/evaluation_corpus_ingestion'/evaluation.IMPORT_RUN
        original = Path.read_text
        for name,key,value in [('import_receipt.json','verified_assertion_count',117),
                               ('import_receipt.json','status','preview'),
                               ('import_receipt.json','review_manifest_sha256','changed'),
                               ('prepared_records.json','scope_assignment','development')]:
            def changed(path,*args,**kwargs):
                text = original(path,*args,**kwargs)
                if path==folder/name:
                    data = json.loads(text);data[key]=value;return json.dumps(data)
                return text
            with self.subTest(name=name,key=key),patch.object(Path,'read_text',changed),patch.object(
                    evaluation,'prepare_predictions',return_value=self.predictions):
                with self.assertRaises(ValueError):
                    evaluation.prepare(REPO)

    def test_development_scopes_or_changed_plan_cannot_be_used(self):
        for key,value in [('scope_assignment','development'),('evaluation_plan_fingerprint','changed')]:
            data = copy.deepcopy(self.predictions)
            data['items'][0]['assertions'][0][key]=value
            with self.subTest(key=key),patch.object(evaluation,'prepare_predictions',return_value=data):
                with self.assertRaisesRegex(ValueError,'explicitly scoped'):
                    evaluation.prepare(REPO)

    def test_evaluation_preview_does_not_require_database_driver(self):
        from import_corpus_pilot_mitigations import main
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            (Path(tmp)/'docs').mkdir()
            with patch('sys.argv',['import_evaluation_corpus_mitigations.py','--repo',tmp,'--preview']),patch.dict(
                    'sys.modules',{'neo4j':None}),redirect_stdout(io.StringIO()):
                self.assertEqual(main(preparer=lambda _:self.payload,output_kind='evaluation_corpus_mitigations',
                                      label='Held-out evaluation corpus'),0)
