"""Held-out lineage, label isolation, exact review provenance and mocked import."""
import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from evaluation import corpus_review as review, corpus_ingestion as ingestion
from extraction.corpus_pilot import save, digest
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import make_prompt
from graph.development_ingestion import write_transaction
from test_corpus_pilot_ingestion import Transaction
from test_source_choices import item, selector

REPO = Path(__file__).resolve().parents[1]
LATEST = REPO/'work/evaluation_corpus_extraction/20261016T041738Z-f6bd403c'


class EvaluationLineageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=REPO/'work')
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.root = self.repo/'work/evaluation_corpus_extraction'
        self.initial = self.root/'20261016T000000Z-aaaaaaaa'
        self.retry = self.root/'20261016T000001Z-bbbbbbbb'
        self.plan = {'scope_ids':['a','b']}
        self.settings = {'model':'fixture'}

    def summary(self, folder, records, parent=None):
        folder.mkdir(parents=True,exist_ok=True)
        value = dict(self.settings,batch_plan=self.plan,graph_writes=False,
                     implementation_sha256='code',status='processed_with_errors',items=records,retry_of=parent)
        save(folder/'summary.json',value)
        return value

    def load(self):
        with patch.object(review,'sha256_file',return_value='code'):
            return review.lineage(self.repo,self.retry,[],self.plan,self.settings)

    def test_retry_must_exclude_completed_empty_windows_and_preserve_order(self):
        self.summary(self.initial,[{'scope_id':'a','folder':'01','status':'empty_extraction'},
                                   {'scope_id':'b','folder':'02','status':'service_error'}])
        self.summary(self.retry,[{'scope_id':'b','folder':'01','status':'candidates_ready_for_review'}],str(self.initial))
        runs, history = self.load()
        self.assertEqual(len(runs),2)
        self.assertEqual(len(history['a']),1)
        self.assertEqual(len(history['b']),2)
        self.summary(self.retry,[{'scope_id':'a','folder':'01','status':'empty_extraction'},
                                 {'scope_id':'b','folder':'02','status':'empty_extraction'}],str(self.initial))
        with self.assertRaisesRegex(ValueError,'pending scopes'):
            self.load()

    def test_cycles_foreign_roots_and_changed_settings_are_rejected(self):
        self.summary(self.retry,[],str(self.retry))
        with self.assertRaisesRegex(ValueError,'cycle'):
            self.load()
        value = self.summary(self.retry,[],None)
        value['model']='different'
        save(self.retry/'summary.json',value)
        with self.assertRaisesRegex(ValueError,'settings'):
            self.load()
        with self.assertRaisesRegex(ValueError,'boundary'):
            review.lineage(self.repo,self.repo/'outside',[],self.plan,self.settings)

    def case(self):
        source = item('Group Alpha actors used Tool Beta.\nGroup Alpha actors deployed Tool Beta.')
        source['preparation'] = {'source_text_sha256':'fixture'}
        system,prompt,schema,index = make_prompt(source,[])
        relation = {'head':selector(index,'Group Alpha actors','ThreatGroup'),'predicate':'USES',
                    'tail':selector(index,'Tool Beta','Software'),'unit_ids':['u001'],'context_ids':[]}
        raw = json.dumps({'relations':[relation,dict(relation,unit_ids=['u002'])]})
        folder = self.initial/'01'
        folder.mkdir(parents=True)
        for name,value in [('chunk.json',source['chunk'].model_dump(mode='json')),
                           ('source_metadata.json',source['preparation']),('output_schema.json',schema),
                           ('source_choices.json',dict(index,captions={k:v.model_dump(mode='json') for k,v in index['captions'].items()})),
                           ('ollama_response_1.json',{'done':True,'done_reason':'stop','response':raw})]:
            save(folder/name,value)
        for name,value in [('system_prompt.txt',system),('user_prompt.txt',prompt),('raw_extraction_1.json',raw)]:
            (folder/name).write_text(value,encoding='utf-8')
        row = {'folder':'01','status':'validation_failed','error':'Repeated selected relationship.',
               'prompt_hash':digest({'system':system,'prompt':prompt,'schema':schema}),
               'source_hash':source['document'].content_hash,'attempts':[{'attempt':1,'http_status':200}]}
        return source,row,folder,raw

    def test_duplicate_derivation_preserves_initial_raw_and_first_support(self):
        source,row,folder,raw = self.case()
        value = review.reconstruct(source,[],(self.initial,{},row))
        self.assertEqual(value['raw'],raw)
        self.assertEqual((folder/'raw_extraction_1.json').read_text(encoding='utf-8'),raw)
        self.assertEqual(len(value['batch'].relations),1)
        self.assertEqual(value['changes'][0]['original_relation_index'],1)
        self.assertEqual(value['changes'][0]['retained_original_relation_index'],0)
        self.assertIn('used Tool Beta',value['batch'].relations[0].evidence.quote)

    def test_changed_schema_and_incomplete_reply_cannot_be_derived(self):
        source,row,folder,raw = self.case()
        saved = (folder/'output_schema.json').read_bytes()
        save(folder/'output_schema.json',{})
        with self.assertRaisesRegex(ValueError,'schema changed'):
            review.reconstruct(source,[],(self.initial,{},row))
        (folder/'output_schema.json').write_bytes(saved)
        save(folder/'ollama_response_1.json',{'done':True,'done_reason':'length','response':raw})
        with self.assertRaisesRegex(ValueError,'incomplete'):
            review.reconstruct(source,[],(self.initial,{},row))


class EvaluationSourceIngestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        original = Path.read_text
        forbidden = {'gold_triples.json','eval_queries.json','reference_triples.json'}
        def guarded(path,*args,**kwargs):
            if path.name in forbidden:
                raise AssertionError('Evaluation labels must not enter source review/import.')
            return original(path,*args,**kwargs)
        text_receipt = json.loads((REPO/'work/text_index_runs/20261016T002500Z-41e31bf5/index_receipt.json').read_text(encoding='utf-8'))
        cls.pointers = {str(p):p.read_bytes() for p in [REPO/'work/graph_index/current.json',
                        REPO/'work/text_index'/text_receipt['fingerprint']/'manifest.json']}
        with patch.object(Path,'read_text',guarded),patch('requests.Session',side_effect=AssertionError('No services')):
            cls.collected = review.collect(REPO,LATEST)
            with patch.object(ingestion,'collect',return_value=cls.collected):
                cls.payload = ingestion.prepare(REPO)

    def prepared(self):
        with patch.object(ingestion,'collect',return_value=self.collected):
            return ingestion.prepare(REPO)

    def test_source_selection_and_evaluation_scope_are_explicit(self):
        p = self.payload
        self.assertEqual(len(p['items']),48)
        self.assertEqual(sum(len(i['assertions']) for i in p['items']),118)
        self.assertEqual(len({e['canonical_id'] for i in p['items'] for e in i['entities']}),91)
        self.assertEqual(len(p['excluded_candidates']),78)
        self.assertEqual(sum(d['disposition']=='review' for d in p['excluded_candidates']),24)
        self.assertEqual(sum(d['disposition']=='reject' for d in p['excluded_candidates']),54)
        self.assertEqual(p['scope_assignment'],'evaluation')
        for path,contents in self.pointers.items():
            self.assertEqual(Path(path).read_bytes(),contents)

    def test_original_failures_earliest_selections_empty_results_and_retry_are_retained(self):
        results,runs,plan,catalog,attack_hash = self.collected
        self.assertEqual(len(results),114)
        self.assertEqual(sum(not r['batch'].relations for _,r in results),49)
        self.assertEqual(sum(len(r['batch'].relations) for _,r in results),196)
        for n in [7,54,88,90]:
            chosen = results[n-1][1]
            self.assertEqual(chosen['entry'][0],runs[0][0])
            self.assertEqual(chosen['entry'][2]['status'],'validation_failed')
            self.assertTrue(chosen['changes'])
        self.assertEqual(results[63][1]['entry'][0],LATEST)
        self.assertEqual(len(results[63][1]['batch'].relations),4)
        self.assertEqual([s['failed_scopes'] for _,s in runs],[5,4])

    def test_exact_source_spans_pending_human_status_and_original_raw_hashes(self):
        chosen = {item['chunk'].chunk_id:result for item,result in self.collected[0]}
        for item in self.payload['items']:
            text = item['document']['text']
            result = chosen[item['chunk']['chunk_id']]
            folder,summary,row = result['entry']
            raw_path = folder/row['folder']/f"raw_extraction_{row['attempts'][-1]['attempt']}.json"
            for a in item['assertions']:
                self.assertEqual(text[a['evidence_start']:a['evidence_end']],a['evidence_text'])
                self.assertEqual(a['scope_assignment'],'evaluation')
                self.assertEqual(a['source_review_disposition'],'supported')
                self.assertEqual(a['human_review_status'],'pending')
                self.assertEqual(a['raw_output_hash'],hashlib.sha256(result['raw'].encode('utf-8')).hexdigest())
                self.assertEqual(a['source_generation_raw_file_sha256'],sha256_file(raw_path))
            for m in item['mentions']:
                self.assertEqual(text[m['evidence_start']:m['evidence_end']],m['evidence_text'])

    def test_wrong_roles_conditional_claims_and_taxonomy_only_predictions_stay_excluded(self):
        excluded = {(d['folder'],d['relation_index']):d['disposition'] for d in self.payload['excluded_candidates']}
        for key in [('06',0),('41',2),('44',0),('48',3),('72',3),('74',1),('104',0)]:
            self.assertEqual(excluded[key],'reject')
        for key in [('11',0),('33',0),('73',0),('73',3),('102',0)]:
            self.assertEqual(excluded[key],'review')
        medusa = next(i for i in self.payload['items'] if i['chunk']['chunk_id'].endswith(':12220:14519'))
        self.assertEqual(len(medusa['assertions']),3)

    def test_changed_receipt_code_original_and_derived_hashes_block_import(self):
        for name in ['receipt.json','corpus_review.py','raw_extraction_2.json','derived_selection.json']:
            def altered(path):
                return '0'*64 if Path(path).name==name else sha256_file(path)
            with self.subTest(name=name),patch.object(ingestion,'sha256_file',side_effect=altered):
                with self.assertRaisesRegex(ValueError,'changed'):
                    self.prepared()

    def test_incomplete_dispositions_block_import(self):
        original = ingestion.read
        def altered(path):
            data = original(path)
            if Path(path).name==Path(ingestion.REVIEW_FILE).name:
                data['windows'][6]['decisions'].pop()
            return data
        with patch.object(ingestion,'read',side_effect=altered),self.assertRaisesRegex(ValueError,'every candidate'):
            self.prepared()

    def test_atomic_mock_import_retains_scope_and_rejects_verification_shortfall(self):
        tx = Transaction(118)
        self.assertEqual(write_transaction(tx,self.payload),118)
        stored = [p['props'] for q,p in tx.calls if q.startswith('MERGE (a:Assertion')]
        self.assertEqual(len({a['assertion_id'] for a in stored}),118)
        self.assertTrue(all(a['scope_assignment']=='evaluation' for a in stored))
        with self.assertRaisesRegex(ValueError,'rolled back'):
            write_transaction(Transaction(117),self.payload)

    def test_operator_preview_has_no_database_dependency_and_correct_scope_label(self):
        from ingest_evaluation_corpus import main
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            (Path(tmp)/'docs').mkdir()
            output = io.StringIO()
            with patch('sys.argv',['ingest_evaluation_corpus.py','--repo',tmp,'--preview']),patch.dict(
                    'sys.modules',{'neo4j':None}),redirect_stdout(output):
                self.assertEqual(main(preparer=lambda _:self.payload),0)
            self.assertIn('held-out evaluation corpus',output.getvalue())
            doc = next((Path(tmp)/'docs').glob('*.md')).read_text(encoding='utf-8')
            self.assertIn('Held-out source assertions',doc)
            self.assertNotIn('Development assertions',doc)


if __name__ == '__main__':
    unittest.main()
