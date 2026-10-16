import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from extraction.corpus_batch import PILOT_RUN, pending, prepare
from extraction.corpus_pilot import configuration, digest, run, save
from extraction.llama_tokenizer import sha256_file
from test_corpus_pilot import HttpFixture, Response, TokenizerFixture, fixture


class CorpusBatchTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]/'work/corpus_batch_tests'
        root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=root)
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        (self.repo/'docs').mkdir()
        self.config = {'llm': {'model': 'llama3.1:8b', 'temperature': 0, 'num_ctx': 8192, 'num_predict': 700}}
        self.identity = {'fingerprint': 'f'*64}
        self.items = []
        for n in range(3):
            item = fixture('Group Alpha actors used Tool Beta.')
            item['chunk'].chunk_id += str(n)
            item['preparation']['pilot_selected'] = n == 0
            self.items.append(item)
        baseline = self.repo/'work/corpus_extraction_pilot'/PILOT_RUN/'summary.json'
        baseline.parent.mkdir(parents=True)
        self.baseline = baseline
        save(baseline, {'status': 'processed', 'graph_writes': False,
                       'configuration_hash': digest(configuration(self.config, self.identity, 'a'*64)),
                       'items': [{'scope_id': self.items[0]['chunk'].chunk_id, 'status': 'candidates_ready_for_review'}]})
        save(self.repo/'docs/ThreatWeave_corpus_pilot_v2_6_review.json',
             {'run': PILOT_RUN, 'summary_sha256': sha256_file(baseline)})

    def prepared(self):
        with patch('extraction.corpus_batch.read_prepared', return_value=(
                self.items, self.config, [], 'a'*64, self.identity, self.repo/'prepared')):
            return prepare(self.repo)

    def generate(self, items, plan, resume=None, responses=None):
        http = HttpFixture()
        if responses is None:
            responses = [Response({'done': True, 'done_reason': 'stop', 'response': '{"relations":[]}'})]*len(items)
        with patch('requests.Session', return_value=http), patch.object(http, 'post', side_effect=responses), patch(
                'extraction.corpus_pilot.load_verified_tokenizer', return_value=(TokenizerFixture(), {})):
            run(self.repo, items, self.config, [], 'a'*64, self.identity, self.repo/'prepared',
                retry_of=resume, batch_plan=plan)
        root = self.repo/'work/corpus_extraction_batch'
        return next(path for path in root.iterdir() if path != resume)

    def test_selection_excludes_pilot_and_binds_exact_remaining_windows(self):
        items, *_, plan = self.prepared()
        self.assertEqual(items, self.items[1:])
        self.assertEqual(plan['scope_ids'], [i['chunk'].chunk_id for i in items])
        self.assertTrue(set(plan['scope_ids']).isdisjoint(plan['excluded_pilot_scope_ids']))
        unsigned = {k: v for k, v in plan.items() if k != 'fingerprint'}
        self.assertEqual(plan['fingerprint'], digest(unsigned))

    def test_changed_baseline_is_rejected(self):
        self.baseline.write_text('{}')
        with self.assertRaises(ValueError):
            self.prepared()

    def test_completed_empty_and_nonempty_windows_are_not_repeated(self):
        items, *_, plan = self.prepared()
        http = HttpFixture()
        http.post(json={})  # first response is deliberately truncated
        nonempty = http.post(json={}).json()
        first = self.generate(items, plan, responses=[Response(nonempty), Response(
            {'done': True, 'done_reason': 'stop', 'response': '{"relations":[]}'})])
        remaining, count = pending(self.repo, items, [], plan, first)
        self.assertEqual((remaining, count), ([], 2))

    def test_changed_model_configuration_is_rejected(self):
        self.config['llm']['temperature'] = 1
        with self.assertRaises(ValueError):
            self.prepared()

    def test_failed_window_is_retried_and_successes_survive_linked_runs(self):
        items, *_, plan = self.prepared()
        first = self.generate(items, plan, responses=[Response(
            {'done': True, 'done_reason': 'stop', 'response': '{"relations":[]}'}), Response({'error': 'offline'}, 503)])
        remaining, count = pending(self.repo, items, [], plan, first)
        self.assertEqual((remaining, count), ([items[1]], 1))
        second = self.generate(remaining, plan, resume=first)
        self.assertEqual(pending(self.repo, items, [], plan, second), ([], 2))

    def test_interruption_preserves_success_and_keeps_unfinished_window_pending(self):
        items, *_, plan = self.prepared()
        with self.assertRaises(KeyboardInterrupt):
            self.generate(items, plan, responses=[Response(
                {'done': True, 'done_reason': 'stop', 'response': '{"relations":[]}'}), KeyboardInterrupt()])
        folder = next((self.repo/'work/corpus_extraction_batch').iterdir())
        self.assertEqual(pending(self.repo, items, [], plan, folder), ([items[1]], 1))

    def test_tampered_success_or_changed_plan_is_rejected(self):
        items, *_, plan = self.prepared()
        folder = self.generate(items, plan)
        changed = copy.deepcopy(plan)
        changed['scope_ids'].reverse()
        with self.assertRaises(ValueError):
            pending(self.repo, items, [], changed, folder)
        (folder/'01/candidate_extraction.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'candidate or evidence changed'):
            pending(self.repo, items, [], plan, folder)

    def test_external_or_cyclic_resume_is_rejected(self):
        items, *_, plan = self.prepared()
        with self.assertRaises(ValueError):
            pending(self.repo, items, [], plan, self.repo/'outside')
        folder = self.generate(items, plan)
        summary = json.loads((folder/'summary.json').read_text())
        summary['retry_of'] = str(folder)
        save(folder/'summary.json', summary)
        with self.assertRaises(ValueError):
            pending(self.repo, items, [], plan, folder)


if __name__ == '__main__':
    unittest.main()
