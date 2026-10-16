from copy import deepcopy
import unittest

from evaluation.human_analysis import agreement, bootstrap, guard_completed, primary_comparisons, validate_review


def document(kind, prefix, count):
    return dict(packet_kind=kind, review_status='completed', reviewer='Reviewer A', review_date='2026-10-16',
                packet_fingerprint='synthetic', secondary_method='delayed_rescore' if kind == 'secondary' else None,
                ratings=[dict(review_id=f'{prefix}{n:03d}', factuality=4, completeness=2, coherence=4,
                              not_ratable_dimensions=[], not_ratable_reason=None, notes='', entry_complete=True)
                         for n in range(1, count + 1)])


class HumanAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.primary = document('primary', 'P', 80)
        self.secondary = document('secondary', 'S', 20)

    def test_requires_completed_secondary_before_unblinding(self):
        self.secondary['review_status'] = 'in_progress'
        with self.assertRaisesRegex(ValueError, 'completed review'):
            guard_completed(self.primary, self.secondary)

    def test_same_person_not_independent(self):
        self.secondary['secondary_method'] = 'independent'
        with self.assertRaisesRegex(ValueError, 'cannot be labeled independent'):
            guard_completed(self.primary, self.secondary)
        self.secondary['secondary_method'] = 'delayed_rescore'
        self.assertEqual(len(guard_completed(self.primary, self.secondary)[1]), 20)

    def test_na_requires_null_and_explanation(self):
        row = self.primary['ratings'][0]
        row['not_ratable_dimensions'] = ['factuality']
        row['factuality'] = None
        with self.assertRaisesRegex(ValueError, 'reason'):
            validate_review(self.primary, 'primary', 80, 'P')
        row['not_ratable_reason'] = 'No valid answer.'
        self.assertEqual(len(validate_review(self.primary, 'primary', 80, 'P')), 80)
        row['factuality'] = 5
        with self.assertRaisesRegex(ValueError, 'null'):
            validate_review(self.primary, 'primary', 80, 'P')

    def test_packet_or_review_ids_mismatch_rejected(self):
        self.secondary['packet_fingerprint'] = 'another'
        with self.assertRaisesRegex(ValueError, 'fingerprints'):
            guard_completed(self.primary, self.secondary)
        self.primary['ratings'][0]['review_id'] = 'P002'
        with self.assertRaisesRegex(ValueError, 'IDs'):
            validate_review(self.primary, 'primary', 80, 'P')

    def test_ordinal_scale_rejects_boolean(self):
        self.primary['ratings'][0]['factuality'] = True
        with self.assertRaisesRegex(ValueError, 'integers'):
            validate_review(self.primary, 'primary', 80, 'P')

    def test_weighted_agreement_and_degenerate_kappa(self):
        self.assertEqual(agreement([(1, 1), (5, 5)])['linear_weighted_kappa'], 1)
        self.assertIsNone(agreement([(4, 4), (4, 4)])['linear_weighted_kappa'])
        self.assertEqual(agreement([(1, 2), (5, 4)])['within_one'], 1)
        self.assertEqual(agreement([(1, 2), (5, 4)])['mean_absolute_difference'], 1)
        self.assertIsNone(agreement([])['exact_agreement'])

    def test_pairing_does_not_zero_impute_missing_case(self):
        rows = []
        for q in ['Q1', 'Q2', 'Q3']:
            for mode, value in [('text_only', 2), ('graph_only', 3), ('hybrid_no_node2vec', 3), ('hybrid', 4)]:
                rows.append(dict(question_id=q, mode=mode, factuality=value, completeness=value, coherence=value))
        rows[0]['completeness'] = None
        result = next(r for r in primary_comparisons(rows, draws=20)
                      if r['dimension'] == 'completeness' and r['mode_a'] == 'text_only' and r['mode_b'] == 'hybrid')
        self.assertEqual(result['paired_question_count'], 2)
        self.assertEqual(result['excluded_questions'], ['Q1'])
        self.assertEqual(result['mean_question_difference'], -2)
        self.assertEqual(result['exploratory_95_percent_ci'], [-2, -2])
        self.assertIsNone(bootstrap([1]))


if __name__ == '__main__':
    unittest.main()
