"""Offline scoring/resume/coverage checks; no services or embeddings."""
import asyncio
import copy
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from evaluation import score_runner as runner
from evaluation import score_plan as planning
from evaluation import judge_runtime as judge

REPO=Path(__file__).resolve().parents[1]


class FakeBackend:
    seen=[]
    failure=None
    interruption=None
    guard_failure=None
    def __init__(self,plan,folder):pass
    def check_model(self,folder,name):
        if self.guard_failure==name:raise ValueError('Changed model digest')
    async def score(self,task,sample,folder):
        self.seen.append(task['task_id'])
        if self.interruption==task['task_id']:raise KeyboardInterrupt()
        if self.failure==task['task_id']:raise RuntimeError('Retained evaluator error')
        if task['metric']=='answer_relevancy':return float('nan')
        return 0.75
    def calls(self):return 1


class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=REPO/'work');self.repo=Path(self.temp.name)
        (self.repo/'evaluation').mkdir()
        hashes={}
        for name in planning.CODE:
            p=self.repo/name;p.write_text('frozen',encoding='utf-8');hashes[name]=judge.sha(p)
        self.rows=[{'case_id':f'r1-Q{i:03d}-text_only','mode':'text_only',
                    'sample':{'user_input':'Synthetic question?','response':'Synthetic answer.' if i<3 else None,
                              'retrieved_contexts':['Synthetic source.'],'reference':'Verified synthetic reference.'}}
                   for i in (1,2,3)]
        tasks=[{'task_id':r['case_id']+'--'+m,'case_id':r['case_id'],'metric':m,
                'eligible':r['sample']['response'] is not None} for r in self.rows for m in judge.METRICS]
        self.plan={'tasks':tasks,'frozen_files_sha256':hashes,'judge_policy':{'implementation_sha256':{}},'fingerprint':'test-plan'}
        FakeBackend.seen=[];FakeBackend.failure=None;FakeBackend.interruption=None;FakeBackend.guard_failure=None
        self.guard=patch('evaluation.score_runner.verify');self.guard.start()

    def tearDown(self):self.guard.stop();self.temp.cleanup()
    def run_batch(self,resume=None):
        with redirect_stdout(io.StringIO()):
            code=runner.run(self.repo,self.plan,self.rows,resume=resume,factory=FakeBackend)
        folders=sorted((self.repo/'work/final_scoring_runs').iterdir(),key=lambda p:p.stat().st_mtime_ns)
        return code,folders[-1]

    def test_full_denominator_unavailable_failures_and_nans_are_distinct(self):
        FakeBackend.failure=self.plan['tasks'][0]['task_id']
        code,folder=self.run_batch();self.assertEqual(code,0)
        summary=judge.read(folder/'summary.json')
        self.assertEqual(summary['terminal_count'],9)
        self.assertEqual(summary['statuses'],{'failed':1,'undefined':2,'scored':3,'unavailable_answer':3})
        self.assertEqual(len(FakeBackend.seen),6)
        complete=runner.history(self.repo,folder,self.plan,self.rows)
        self.assertTrue(all(x['value'] is None for x in complete.values() if x['status']!='scored'))
        self.assertEqual(sum(sum(v.values()) for v in summary['coverage'].values()),9)

    def test_interrupted_metric_only_is_resumed_and_terminal_failures_not_retried(self):
        FakeBackend.failure=self.plan['tasks'][0]['task_id'];FakeBackend.interruption=self.plan['tasks'][2]['task_id']
        code,first=self.run_batch();self.assertEqual(code,2)
        self.assertEqual(judge.read(first/'summary.json')['terminal_count'],2)
        FakeBackend.interruption=None;FakeBackend.seen=[]
        code,second=self.run_batch(first);self.assertEqual(code,0)
        self.assertEqual(len(FakeBackend.seen),4)
        self.assertNotIn(self.plan['tasks'][0]['task_id'],FakeBackend.seen)
        self.assertEqual(len(runner.history(self.repo,second,self.plan,self.rows)),9)
        self.assertTrue((first/self.plan['tasks'][2]['task_id']/'receipt.json').is_file())

    def test_completed_resume_does_not_initialize_backend(self):
        _,folder=self.run_batch();FakeBackend.seen=[]
        with patch.object(FakeBackend,'__init__',side_effect=AssertionError('No repeat model setup')):
            code,_=self.run_batch(folder)
        self.assertEqual(code,0);self.assertEqual(FakeBackend.seen,[])

    def test_saved_score_tampering_is_rejected(self):
        _,folder=self.run_batch();p=folder/self.plan['tasks'][0]['task_id']/'result.json'
        value=judge.read(p);value['value']=1;judge.save(p,value)
        with self.assertRaises(ValueError):runner.history(self.repo,folder,self.plan,self.rows)

    def test_resume_boundary_and_cycle_are_rejected(self):
        _,folder=self.run_batch()
        with self.assertRaises(ValueError):runner.history(self.repo,self.repo,self.plan,self.rows)
        p=folder/'summary.json';s=judge.read(p);s['resume_of']=str(folder);judge.save(p,s)
        with self.assertRaises(ValueError):runner.history(self.repo,folder,self.plan,self.rows)

    def test_post_metric_model_change_blocks_automatic_resume(self):
        FakeBackend.guard_failure='model_tags_after.json';code,folder=self.run_batch()
        self.assertEqual(code,1);s=judge.read(folder/'summary.json')
        self.assertTrue(s['integrity_error']);self.assertEqual(s['results'][0]['status'],'failed')
        self.assertIsNone(s['results'][0]['value'])
        with self.assertRaises(ValueError):runner.history(self.repo,folder,self.plan,self.rows)

    def test_unavailable_only_cohort_never_initializes_models(self):
        self.plan['tasks']=[t for t in self.plan['tasks'] if not t['eligible']]
        with patch.object(FakeBackend,'__init__',side_effect=AssertionError('No model calls for missing answers')):
            code,folder=self.run_batch()
        self.assertEqual(code,0)
        self.assertEqual(judge.read(folder/'summary.json')['statuses'],{'unavailable_answer':3})

    def test_failed_metric_cancels_orphaned_requests_before_next_task(self):
        class Metric:
            async def single_turn_ascore(self,*args,**kwargs):
                async def orphan():
                    try:await asyncio.sleep(60)
                    finally:events.append('cancelled')
                asyncio.create_task(orphan());await asyncio.sleep(0)
                raise RuntimeError('One relevance subrequest failed')
        events=[];backend=runner.LocalScorer.__new__(runner.LocalScorer)
        backend.metrics={'answer_relevancy':Metric()};backend.recorder=judge.Recorder(self.repo,30)
        async def check():
            with self.assertRaises(RuntimeError):
                # SingleTurnSample import is simulated to keep this test
                # independent of the heavyweight evaluator environment.
                with patch.dict('sys.modules',{'ragas':type('Module',(),{'SingleTurnSample':lambda **kw:kw})}):
                    await backend.score({'metric':'answer_relevancy'},self.rows[0]['sample'],self.repo)
            self.assertEqual(events,['cancelled'])
        asyncio.run(check())


if __name__=='__main__':unittest.main()
