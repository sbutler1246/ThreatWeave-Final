"""Offline saved-output audit, reference export and review isolation checks."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from evaluation.final_review import blinded_packets, failed_attempts, summarize
from evaluation.experiment_plan import read
from setup_evaluation import setup

REPO = Path(__file__).resolve().parents[1]
SAVED = REPO/'work/final_evaluation_runs/20261016T050129Z-f6328cdf'


class ReviewTests(unittest.TestCase):
    def fixtures(self):
        qs = {f'Q{i:03d}':{'question':f'Question {i}?','reference_answer':f'Reference {i}.'} for i in range(20)}
        rows = [{'case_id':f'r{repeat}-{qid}-{mode}', 'question_id':qid,'mode':mode,'repeat':repeat,
                 'status':'answer_ready_for_review','response':'A cited answer.','supplied_context':'Saved context.'}
                for qid in qs for mode in ('text_only','graph_only','hybrid_no_node2vec','hybrid') for repeat in (1,2,3)]
        return rows, qs

    def test_blinding_preserves_all_primary_and_paired_secondary_without_labels_or_ratings(self):
        rows, qs = self.fixtures(); packets, key, selected = blinded_packets(rows, qs)
        self.assertEqual(len(packets['primary']),80); self.assertEqual(len(packets['secondary']),20)
        self.assertEqual(len(selected),5)
        for packet in packets.values():
            for row in packet:
                self.assertTrue(all(row[d] is None for d in ('factuality','completeness','coherence')))
                self.assertFalse({'mode','repeat','case_id','question_id'} & row.keys())
        self.assertTrue(all(k['repeat']==1 for k in key))
        for qid in selected:
            self.assertEqual(len([k for k in key if k['packet']=='secondary' and k['question_id']==qid]),4)
        self.assertEqual(blinded_packets(list(reversed(rows)),qs),(packets,key,selected))

    def test_failed_and_abstained_outcomes_remain_in_human_packet(self):
        rows, qs = self.fixtures(); rows[0].update(status='failed',response=None)
        rows[3].update(status='abstained',response='Insufficient evidence.')
        packets,_,_ = blinded_packets(rows,qs)
        self.assertEqual(sum(x['outcome']=='failed' for x in packets['primary']),1)
        self.assertEqual(sum(x['outcome']=='abstained' for x in packets['primary']),1)

    def test_latency_denominator_contains_all_outcomes(self):
        rows = [{'mode':'m','status':s,'execution_time_ms':t,'generation_requests':n}
                for s,t,n in [('failed',1000,2),('abstained',10,0),('answer_ready_for_review',300,1)]]
        result = summarize(rows,['m'])['m']
        self.assertEqual(result['outcomes'],3); self.assertEqual(result['median_case_ms_all_outcomes'],300)
        self.assertEqual(result['generation_requests'],3)
        rows[0]['execution_time_ms'] = float('nan')
        with self.assertRaises(ValueError):summarize(rows,['m'])

    def test_saved_failure_replays_original_repair_and_classifies_without_model_calls(self):
        folder = SAVED/'r1-Q040-text_only'
        question = read(folder/'question.json')['question']
        with patch('requests.post',side_effect=AssertionError('No live model calls')):
            result = failed_attempts(folder,question,'text_only',read(REPO/'config.json'))
        self.assertEqual(len(result),2)
        self.assertIn('Repeated citation IDs',result[-1]['messages'][0])

    def test_failed_case_prompt_tamper_is_rejected(self):
        original = read
        def changed(path):
            value = original(path)
            if path.name=='transport_request_2.json':
                value = copy.deepcopy(value);value['payload']['prompt'] += 'tampered'
            return value
        folder = SAVED/'r1-Q040-text_only'
        with patch('evaluation.final_review.read',side_effect=changed), self.assertRaises(ValueError):
            failed_attempts(folder,read(folder/'question.json')['question'],'text_only',read(REPO/'config.json'))

    def test_setup_preview_does_not_install_or_call_services(self):
        with patch('subprocess.run',side_effect=AssertionError('Preview must be offline')):
            self.assertEqual(setup(REPO,preview=True),0)

    def test_changed_evaluator_lock_is_rejected_before_install(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            root = Path(tmp);(root/'evaluation').mkdir()
            (root/'evaluation/dependency_verification.json').write_text(json.dumps({'lock_sha256':'bad'}))
            (root/'evaluation/requirements.lock.txt').write_text('changed')
            with patch('subprocess.run',side_effect=AssertionError('No install')),self.assertRaises(ValueError):
                setup(root,preview=True)


if __name__ == '__main__':unittest.main()
