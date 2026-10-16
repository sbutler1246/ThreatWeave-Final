import unittest

from evaluation.extraction_analysis import (
    canonical_endpoint, contains, covered_length, evaluate, measures, predicate_summary,
)


class ExtractionAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.scopes = {'A': {'doc_id': 'doc1'}, 'B': {'doc_id': 'doc2'}}
        self.fact = dict(head_id='attack:S0002', predicate='USES_TECHNIQUE', tail_id='attack:T1003')
        self.gold = [dict(self.fact, chunk_id='A', doc_id='doc1', gold_id='G1', verified=True),
                     dict(self.fact, chunk_id='B', doc_id='doc2', gold_id='G2', verified=True)]

    def prediction(self, **kwargs):
        return dict(self.fact, **{'chunk_id': 'A', 'doc_id': 'doc1', 'evidence_valid': True,
                                 'strict_eligible': True, 'origin': 'extracted', **kwargs})

    def test_same_fact_in_other_advisory_cannot_supply_missing_scope(self):
        result = evaluate([self.prediction()], self.gold, self.scopes, strict=True)
        self.assertEqual((result['tp'], result['fp'], result['fn']), (1, 0, 1))
        self.assertEqual(result['scope_collapsing_legacy_diagnostic']['fn'], 0)

    def test_literal_invalid_evidence_is_false_positive_and_missed_gold(self):
        result = evaluate([self.prediction(evidence_valid=False)], self.gold, self.scopes, strict=True)
        self.assertEqual((result['tp'], result['fp'], result['fn']), (0, 1, 2))

    def test_empty_output_does_not_remove_gold_or_impute_precision(self):
        result = evaluate([], self.gold, self.scopes, strict=True)
        self.assertEqual(result['fn'], 2)
        self.assertEqual(result['recall'], 0)
        self.assertIsNone(result['precision'])
        self.assertIsNone(result['f1'])

    def test_repeated_window_predictions_count_once_per_annotation_scope(self):
        result = evaluate([self.prediction(), self.prediction()], self.gold, self.scopes, strict=True)
        self.assertEqual(result['eligible_prediction_occurrences'], 2)
        self.assertEqual(result['unique_scope_predictions'], 1)
        self.assertEqual(result['tp'], 1)

    def test_duplicate_failed_case_is_sensitivity_only(self):
        rows = [self.prediction(strict_eligible=False)]
        strict = evaluate(rows, self.gold, self.scopes, strict=True)
        sensitivity = evaluate(rows, self.gold, self.scopes, strict=False)
        self.assertEqual(strict['tp'], 0)
        self.assertEqual(strict['fn'], 2)
        self.assertEqual(sensitivity['tp'], 1)

    def test_parent_subtechnique_not_collapsed(self):
        entity = dict(type='Technique', name='LSASS Memory', attack_id='T1003.001')
        actual, _, reason = canonical_endpoint(entity, {}, [], 'doc1')
        self.assertEqual(actual, 'attack:T1003.001')
        self.assertEqual(reason, 'explicit_source_attack_id')
        wrong = self.prediction(tail_id='attack:T1003.001')
        result = evaluate([wrong], self.gold, self.scopes, strict=True)
        self.assertEqual((result['tp'], result['fp'], result['fn']), (0, 1, 2))

    def test_frozen_local_identity_stays_in_its_document(self):
        reference = [dict(canonical_id='local:doc1:tool', type='Software', name='Tool Name')]
        entity = dict(type='Software', name='tool   name', attack_id=None)
        a, _, _ = canonical_endpoint(entity, {}, reference, 'doc1')
        b, _, _ = canonical_endpoint(entity, {}, reference, 'doc2')
        self.assertEqual(a, 'local:doc1:tool')
        self.assertNotEqual(a, b)
        entity['name'] = 'Tool Name affiliates'
        self.assertNotEqual(canonical_endpoint(entity, {}, reference, 'doc1')[0], a)

    def test_boundary_crossing_and_union_coverage(self):
        scope = {'start': 10, 'end': 30}
        self.assertTrue(contains(scope, [(10, 15), (25, 30)]))
        self.assertFalse(contains(scope, [(9, 15), (25, 30)]))
        self.assertFalse(contains(scope, []))
        self.assertEqual(covered_length(10, 30, [(0, 20), (15, 25), (23, 40)]), 20)
        self.assertEqual(covered_length(10, 30, [(0, 15), (20, 25)]), 10)

    def test_undefined_denominators(self):
        self.assertEqual(measures(0, 1, 1)['f1'], 0)
        self.assertEqual(measures(0, 0, 1)['undefined_metrics'], ['precision', 'f1'])
        self.assertEqual(measures(0, 1, 0)['undefined_metrics'], ['recall', 'f1'])

    def test_predicate_counts_reconcile_without_cross_relation_matches(self):
        rows = [self.prediction(), self.prediction(predicate='USES', evidence_valid=False)]
        grouped = predicate_summary(rows, self.gold, self.scopes, strict=True)
        total = evaluate(rows, self.gold, self.scopes, strict=True)
        for key in ['tp', 'fp', 'fn']:
            self.assertEqual(sum(row[key] for row in grouped), total[key])
        uses = next(row for row in grouped if row['predicate'] == 'USES')
        self.assertEqual((uses['tp'], uses['fp'], uses['fn']), (0, 1, 0))
        self.assertIsNone(uses['recall'])


if __name__ == '__main__':
    unittest.main()
