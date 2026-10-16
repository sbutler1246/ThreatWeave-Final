"""Offline statistical checks and preserved-judge formula verification."""
import copy
import tempfile
import unittest
from pathlib import Path
from evaluation import score_analysis as analysis
from evaluation import judge_runtime as judge

REPO=Path(__file__).resolve().parents[1]


class AnalysisTests(unittest.TestCase):
    def records(self):
        return [{'question_id':f'Q{q}','mode':mode,'repeat':repeat,'metric':metric,'status':'scored',
                 'value':0.1+index*0.2+q*0.01}
                for q in (1,2,3) for index,mode in enumerate(analysis.MODES)
                for repeat in (1,2,3) for metric in judge.METRICS]

    def test_bootstrap_uses_question_pairs_and_has_correct_direction(self):
        rows=analysis.comparisons(self.records(),draws=100)
        self.assertEqual(len(rows),18)
        row=rows[0];self.assertEqual(row['paired_question_count'],3)
        self.assertAlmostEqual(row['mean_question_difference'],-0.2)
        self.assertTrue(all(abs(x+0.2)<1e-12 for x in row['exploratory_95_percent_ci']))
        self.assertEqual(rows,analysis.comparisons(self.records(),draws=100))

    def test_one_missing_repeat_excludes_whole_question_from_that_pair(self):
        records=self.records();records[0].update(status='failed',value=None)
        comparisons=analysis.comparisons(records,draws=100)
        selected=[r for r in comparisons if r['metric']=='faithfulness' and r['mode_a']=='text_only']
        self.assertTrue(all(r['paired_question_count']==2 and r['excluded_questions']==['Q1'] for r in selected))
        untouched=[r for r in comparisons if r['metric']=='faithfulness' and r['mode_a']=='graph_only']
        self.assertTrue(all(r['paired_question_count']==3 for r in untouched))

    def test_missing_scores_do_not_enter_means_as_zero(self):
        records=self.records();records[0].update(status='unavailable_answer',value=None)
        row=analysis.mode_summary(records)[0]
        self.assertEqual(row['denominator'],9);self.assertEqual(row['available_score_count'],8)
        self.assertEqual(row['statuses']['unavailable_answer'],1)
        self.assertAlmostEqual(row['available_score_mean'],sum(r['value'] for r in records if r['mode']=='text_only' and r['metric']=='faithfulness' and r['status']=='scored')/8)

    def test_too_few_paired_questions_do_not_produce_an_interval(self):
        self.assertIsNone(analysis.bootstrap([]));self.assertIsNone(analysis.bootstrap([0.1]))
        self.assertEqual(analysis.percentile([0,10],0.25),2.5)

    def test_json_extraction_retains_frozen_markdown_and_first_structure_behavior(self):
        self.assertEqual(analysis.extracted_json('Explanation. ```json\n{"statements": ["x"]}\n```'),{'statements':['x']})
        self.assertEqual(analysis.extracted_json('Text {"x": 1} trailing {"x": 2}'),{'x':1})

    def test_saved_verdict_formula_and_count_mismatch_are_audited_without_changing_score(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            folder=Path(tmp);settings={'model':'local','model_digest':'digest','judge_options':{'temperature':0}}
            for when in ('before','after'):judge.save(folder/f'model_tags_{when}.json',{'models':[{'name':'local','digest':'digest'}]})
            row={'task':{'metric':'faithfulness'},'status':'scored','value':0.5,'judge_calls':2}
            for i,text in [(1,'{"statements":["one"]}'),(2,'{"statements":[{"verdict":1},{"verdict":0}]}')]:
                judge.save(folder/f'judge_call_{i:03d}_request.json',{'phase':'faithfulness','endpoint':'/api/chat','parameters':{'model':'local','stream':False,'options':{'temperature':0}}})
                judge.save(folder/f'judge_call_{i:03d}_response.json',{'done':True,'done_reason':'stop','message':{'content':text}})
            result=analysis.audit_metric(folder,row,settings)
            self.assertTrue(result['formula_recomputed']);self.assertTrue(result['statement_verdict_count_mismatch'])
            changed=copy.deepcopy(row);changed['value']=1
            with self.assertRaises(ValueError):analysis.audit_metric(folder,changed,settings)


if __name__=='__main__':unittest.main()
