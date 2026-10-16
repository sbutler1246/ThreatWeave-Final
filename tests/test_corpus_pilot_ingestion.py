"""Pinned development selection, provenance, and import transaction checks; no services."""
import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from graph.corpus_pilot_ingestion import check_decisions, prepare, sha256_file
from graph.development_ingestion import write_transaction
from schemas import ExtractionBatch

REPO = Path(__file__).resolve().parents[1]


class Result:
    def __init__(self, value=None):
        self.value = value
    def single(self):
        return self.value
    def consume(self):
        return None


class Transaction:
    def __init__(self, count):
        self.count = count
        self.calls = []
    def run(self, query, **params):
        self.calls.append((query, params))
        return Result({'verified':self.count} if query.startswith('UNWIND $facts') else None)


class CorpusPilotIngestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = prepare(REPO)

    def test_exact_review_selection_excludes_uncertain_and_conditional_candidates(self):
        p = self.payload
        self.assertEqual(len(p['items']), 10)
        self.assertEqual(sum(len(i['assertions']) for i in p['items']), 34)
        self.assertEqual({(e['folder'], e['relation_index']) for e in p['excluded_candidates']},
                         {('01',2), ('02',0), ('09',1)})
        self.assertEqual(len({e['canonical_id'] for i in p['items'] for e in i['entities']}), 39)
        self.assertEqual(p['human_review_status'], 'pending')

    def test_all_assertions_keep_exact_evidence_and_review_provenance(self):
        for item in self.payload['items']:
            source = item['document']['text']
            for a in item['assertions']:
                self.assertEqual(source[a['evidence_start']:a['evidence_end']], a['evidence_text'])
                self.assertEqual(a['origin'], 'extracted')
                self.assertEqual(a['validation_status'], 'validated')
                self.assertEqual(a['human_review_status'], 'pending')
                self.assertEqual(a['source_review_sha256'], self.payload['review_manifest_sha256'])
                self.assertTrue(a['source_review_reason'])
                self.assertTrue(json.loads(a['selected_units_json']))
                self.assertTrue(all(not isinstance(v, dict) for v in a.values()))
            for m in item['mentions']:
                self.assertEqual(source[m['evidence_start']:m['evidence_end']], m['evidence_text'])

    def test_software_occurrence_uses_independent_mention_instead_of_actor_name(self):
        item = self.payload['items'][-1]
        mention = next(m for m in item['mentions'] if m['evidence_text'] == 'Phobos')
        quote_start = item['assertions'][0]['evidence_start']
        self.assertGreater(mention['evidence_start'], quote_start+len('Phobos actors'))

    def test_repeat_preparation_has_stable_assertions_and_keeps_source_alias_identity(self):
        repeated = prepare(REPO)
        self.assertEqual(self.payload['items'], repeated['items'])
        software = next(e for e in self.payload['items'][5]['entities'] if e['canonical_id'] == 'attack:S0670')
        self.assertEqual(software['name'], 'WarzoneRAT')
        mention = next(m for m in self.payload['items'][5]['mentions'] if m['canonical_id'] == 'attack:S0670')
        self.assertEqual(mention['evidence_text'], 'AveMaria')

    def test_missing_duplicate_or_unsupported_review_entries_are_blocked(self):
        batch = ExtractionBatch(entities=[], relations=[])
        self.assertEqual(check_decisions([], batch), [])
        decision = {'relation_index':0, 'disposition':'supported', 'reason':'fixture'}
        for entries in [[decision], [decision, decision]]:
            with self.assertRaisesRegex(ValueError, 'every candidate'):
                check_decisions(entries, batch)
        real_batch = ExtractionBatch.model_validate_json(
            (REPO/'work/corpus_extraction_pilot/20261015T035023Z-f4b7051e/08/candidate_extraction.json').read_text(encoding='utf-8'))
        with self.assertRaisesRegex(ValueError, 'reason'):
            check_decisions([dict(decision, disposition='automatic')], real_batch)

    def test_changed_raw_reply_is_blocked_before_import(self):
        def changed(path):
            return '0'*64 if Path(path).name == 'raw_extraction_1.json' else sha256_file(path)
        with patch('graph.corpus_pilot_ingestion.sha256_file', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'model output changed'):
                prepare(REPO)

    def test_transaction_verifies_all_selected_assertions_and_rejects_incomplete_count(self):
        tx = Transaction(34)
        self.assertEqual(write_transaction(tx, self.payload), 34)
        stored = [p['props'] for query, p in tx.calls if query.startswith('MERGE (a:Assertion')]
        self.assertEqual(len(stored), 34)
        self.assertEqual(len({a['assertion_id'] for a in stored}), 34)
        self.assertTrue(all(a['source_review_disposition'] == 'supported' for a in stored))
        with self.assertRaisesRegex(ValueError, 'rolled back'):
            write_transaction(Transaction(33), self.payload)

    def test_preview_does_not_load_database_driver(self):
        from ingest_corpus_pilot import main
        root = REPO/'work/corpus_pilot_ingestion_tests'
        root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            (Path(tmp)/'docs').mkdir()
            with patch('ingest_corpus_pilot.prepare', return_value=copy.deepcopy(self.payload)), \
                 patch('sys.argv', ['ingest_corpus_pilot.py','--repo',tmp,'--preview']), \
                 patch.dict('sys.modules', {'neo4j':None}), redirect_stdout(io.StringIO()):
                self.assertEqual(main(), 0)
            self.assertEqual(len(list((Path(tmp)/'work/corpus_pilot_ingestion').glob('*/prepared_records.json'))), 1)


if __name__ == '__main__':
    unittest.main()
