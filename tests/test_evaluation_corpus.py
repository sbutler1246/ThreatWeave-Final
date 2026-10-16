"""Held-out source isolation, frozen protocol and mocked resumable extraction."""
import copy
import io
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from evaluation import corpus_preparation as preparation, corpus_runner as runner
from extraction.corpus_chunking import digest, load_verified_tokenizer
from extraction.corpus_pilot import configuration, run as development_run, save
from test_corpus_pilot import HttpFixture, Response, TokenizerFixture, fixture

REPO = Path(__file__).resolve().parents[1]


class EvaluationCorpusPreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = preparation.prepare(REPO)
        cls.items,cls.config,cls.catalog,cls.attack_hash,cls.identity,cls.plan = cls.prepared
        cls.checks = preparation.preflight(cls.items,cls.config,cls.catalog,load_verified_tokenizer(REPO)[0])

    def test_all_seven_reports_have_distinct_evaluation_window_ids(self):
        self.assertEqual([(d['doc_id'],d['chunk_count']) for d in self.identity['documents']],
                         [('AA23-165A',14),('AA23-061A',25),('AA24-131A',7),('AA24-109A',21),
                          ('AA25-071A',15),('AA23-352A',17),('AA23-075A',15)])
        self.assertEqual(len(self.items),114)
        self.assertEqual(len(set(self.plan['scope_ids'])),114)
        self.assertTrue(all(':evaluation:' in s for s in self.plan['scope_ids']))
        self.assertTrue(set(self.plan['scope_ids']).isdisjoint(self.plan['excluded_prior_scope_ids']))
        self.assertEqual(len(self.plan['excluded_development_reports']),8)
        self.assertEqual(self.plan['fingerprint'],digest({k:v for k,v in self.plan.items() if k!='fingerprint'}))

    def test_exact_technical_coverage_with_no_source_gaps(self):
        for d in self.identity['documents']:
            covered = set()
            for item in self.items:
                if item['document'].doc_id!=d['doc_id']:
                    continue
                doc,chunk = item['document'],item['chunk']
                self.assertEqual(doc.text[chunk.start:chunk.end],chunk.text)
                self.assertTrue(d['technical_start']<=chunk.start<chunk.end<=d['technical_end'])
                self.assertTrue(400<=item['preparation']['source_tokens']<=600)
                for c in chunk.inherited_context:
                    self.assertEqual(doc.text[c.start:c.end],c.text)
                covered.update(range(chunk.start,chunk.end))
            self.assertEqual(covered,set(range(d['technical_start'],d['technical_end'])))

    def test_frozen_methods_budgets_and_scoring_rules(self):
        p = self.identity['protocol']
        self.assertEqual(configuration(self.config,self.identity,self.attack_hash)['options'],
                         {'temperature':0,'num_ctx':8192,'num_predict':700})
        self.assertEqual(p['measured_answer_runs'],240)
        self.assertEqual(p['human_review_answer_count'],80)
        self.assertEqual(p['human_review_repeat'],1)
        self.assertEqual(p['reports_with_preexisting_bounded_development_evidence'],['AA23-165A'])
        self.assertIn('before review filtering',p['extraction_scoring'])
        self.assertIn('MODE',p['mode_label_policy'])
        self.assertIn('UTF-8 byte',p['packing_policy'])
        self.assertTrue(all(r['within_budget'] and r['estimated_total_tokens']<=8192 for r in self.checks))
        self.assertEqual(sum(not r['mention_count'] for r in self.checks),13)
        self.assertEqual(self.plan['protocol_sha256'],digest(p))

    def test_preparation_never_reads_labels_answers_or_changes_development_pointer(self):
        forbidden = {'gold_triples.json','eval_queries.json','reference_triples.json','author_review.md','qa_review_report.md'}
        original = Path.read_text
        pointer = REPO/'work/graph_index/current.json'
        before = pointer.read_bytes()
        def guarded(path,*args,**kwargs):
            if path.name in forbidden:
                raise AssertionError('Label file must not enter source preparation: '+path.name)
            return original(path,*args,**kwargs)
        with patch.object(Path,'read_text',guarded),patch('requests.Session',side_effect=AssertionError('Services forbidden')):
            self.assertEqual(preparation.prepare(REPO)[-1],self.plan)
        self.assertEqual(pointer.read_bytes(),before)

    def test_changed_selection_or_source_fails(self):
        m = json.loads((REPO/'benchmarks/corpus_manifest.json').read_text(encoding='utf-8'))
        s = json.loads((REPO/'benchmarks/split_manifest.json').read_text(encoding='utf-8'))
        for change in ['missing','duplicate','unblocked']:
            manifest,split = copy.deepcopy(m),copy.deepcopy(s)
            if change=='missing':
                manifest['documents'] = [d for d in manifest['documents'] if d['doc_id']!='AA23-061A']
            elif change=='duplicate':
                manifest['documents'].append(copy.deepcopy(manifest['documents'][0]))
            else:
                split['held_out_evidence_scopes'] = [i for i in split['held_out_evidence_scopes'] if not i.startswith('AA23-061A:')]
            with self.subTest(change=change),self.assertRaises(ValueError):
                preparation.selection(manifest,split)
        original = Path.read_text
        def changed(path,*args,**kwargs):
            text = original(path,*args,**kwargs)
            return text+'changed' if path==REPO/'data/AA23-061A.txt' else text
        with patch.object(Path,'read_text',changed),self.assertRaisesRegex(ValueError,'source checksum changed'):
            preparation.prepare(REPO)

    def test_saved_preparation_and_protocol_tampering_blocks_execution(self):
        with patch.object(preparation,'prepare',return_value=self.prepared),patch.object(
                preparation,'preflight',return_value=self.checks):
            values = preparation.read_prepared(REPO)
            root = values[-2]
            original = Path.read_text
            for name in ['summary.json','preflight.json','chunks.json']:
                def changed(path,*args,**kwargs):
                    text = original(path,*args,**kwargs)
                    if path==root/name:
                        data = json.loads(text)
                        if name=='summary.json':
                            data['identity']['protocol']['model_digest'] = 'changed'
                        elif name=='preflight.json':
                            data[0]['prompt_hash'] = 'changed'
                        else:
                            data[0]['chunk']['text'] = 'changed'
                        return json.dumps(data)
                    return text
                with self.subTest(name=name),patch.object(Path,'read_text',changed),self.assertRaises(ValueError):
                    preparation.read_prepared(REPO)


class EvaluationCorpusRunnerTests(unittest.TestCase):
    def setUp(self):
        root = REPO/'work/evaluation_corpus_tests'
        root.mkdir(parents=True,exist_ok=True)
        tmp = tempfile.TemporaryDirectory(dir=root)
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name)
        (self.repo/'docs').mkdir()
        self.config = {'llm':{'model':'llama3.1:8b','temperature':0,'num_ctx':8192,'num_predict':700}}
        self.identity = {'fingerprint':'f'*64}
        self.items = [fixture('Group Alpha actors used Tool Beta.') for _ in range(2)]
        for i,item in enumerate(self.items):
            item['chunk'].chunk_id = 'sample:evaluation:'+str(i)
        self.plan = {'purpose':'held_out_seven_report_source_extraction',
                     'scope_ids':[i['chunk'].chunk_id for i in self.items],
                     'configuration_hash':digest(configuration(self.config,self.identity,'a'*64))}

    def generate(self,items,responses,resume=None,http=None,engine=runner.run):
        http = http or HttpFixture()
        with patch('requests.Session',return_value=http),patch.object(http,'post',side_effect=responses),patch(
                'evaluation.corpus_runner.load_verified_tokenizer',return_value=(TokenizerFixture(),{})),patch(
                'extraction.corpus_pilot.load_verified_tokenizer',return_value=(TokenizerFixture(),{})),redirect_stdout(io.StringIO()):
            code = engine(self.repo,items,self.config,[],'a'*64,self.identity,self.repo/'prepared',
                          retry_of=resume,batch_plan=self.plan)
        kind = 'evaluation_corpus_extraction' if engine is runner.run else 'corpus_extraction_batch'
        roots = [p for p in (self.repo/'work'/kind).iterdir() if p!=resume]
        folder = max(roots,key=lambda p:p.stat().st_mtime_ns)
        return code,folder,http

    def empty(self):
        return Response({'done':True,'done_reason':'stop','response':'{"relations":[]}'})

    def test_serving_model_rejection_occurs_before_generation(self):
        code,folder,http = self.generate(self.items,[],http=HttpFixture(digest='wrong'))
        self.assertEqual(code,1)
        self.assertEqual(http.posts,[])
        self.assertEqual(json.loads((folder/'summary.json').read_text())['items'],[])

    def test_same_generation_payload_as_frozen_development_engine(self):
        # Let the identical fixture provide a truncated first response and one valid repair.
        one,two = HttpFixture(),HttpFixture()
        for engine,http in [(runner.run,one),(development_run,two)]:
            with patch('requests.Session',return_value=http),patch('evaluation.corpus_runner.load_verified_tokenizer',
                    return_value=(TokenizerFixture(),{})),patch('extraction.corpus_pilot.load_verified_tokenizer',
                    return_value=(TokenizerFixture(),{})),redirect_stdout(io.StringIO()):
                self.assertEqual(engine(self.repo,[self.items[0]],self.config,[],'a'*64,self.identity,
                                        self.repo/'prepared',batch_plan=self.plan),0)
        self.assertEqual(one.posts,two.posts)
        self.assertEqual(len(one.posts),2)
        self.assertNotIn('INCOMPLETE_MARKER',one.posts[1]['prompt'])
        self.assertEqual(one.posts[0]['options'],{'temperature':0,'num_ctx':8192,'num_predict':700})

    def test_failed_windows_resume_and_completed_empty_windows_are_preserved(self):
        code,first,_ = self.generate(self.items,[self.empty(),Response({'error':'offline'},503)])
        self.assertEqual(code,1)
        rest,count = runner.pending(self.repo,self.items,[],self.plan,first)
        self.assertEqual((rest,count),([self.items[1]],1))
        code,second,_ = self.generate(rest,[self.empty()],resume=first)
        self.assertEqual(code,0)
        self.assertEqual(runner.pending(self.repo,self.items,[],self.plan,second),([],2))
        self.assertFalse((self.repo/'work/corpus_extension_extraction').exists())

    def test_resume_accepts_case_100_and_rejects_saved_schema_tampering(self):
        _,folder,_ = self.generate([self.items[0]],[self.empty()])
        summary = json.loads((folder/'summary.json').read_text())
        shutil.copytree(folder/'01',folder/'100')
        summary['items'][0]['folder'] = '100'
        save(folder/'summary.json',summary)
        self.assertEqual(runner.pending(self.repo,self.items,[],self.plan,folder),([self.items[1]],1))
        save(folder/'100/output_schema.json',{})
        with self.assertRaisesRegex(ValueError,'source or prompt changed'):
            runner.pending(self.repo,self.items,[],self.plan,folder)

    def test_interrupted_window_remains_pending(self):
        with self.assertRaises(KeyboardInterrupt):
            self.generate(self.items,[self.empty(),KeyboardInterrupt()])
        folder = next((self.repo/'work/evaluation_corpus_extraction').iterdir())
        self.assertEqual(runner.pending(self.repo,self.items,[],self.plan,folder),([self.items[1]],1))

    def test_plan_tampering_cycles_and_development_run_roots_are_rejected(self):
        _,folder,_ = self.generate(self.items,[self.empty(),self.empty()])
        changed = dict(self.plan,scope_ids=list(reversed(self.plan['scope_ids'])))
        with self.assertRaises(ValueError):
            runner.pending(self.repo,self.items,[],changed,folder)
        summary = json.loads((folder/'summary.json').read_text())
        summary['retry_of'] = str(folder)
        save(folder/'summary.json',summary)
        with self.assertRaises(ValueError):
            runner.pending(self.repo,self.items,[],self.plan,folder)
        with self.assertRaises(ValueError):
            runner.pending(self.repo,self.items,[],self.plan,folder,output_kind='corpus_extension_extraction')
        with self.assertRaises(ValueError):
            runner.run(self.repo,[],self.config,[],'a'*64,self.identity,self.repo,output_kind='../outside')


if __name__ == '__main__':
    unittest.main()
