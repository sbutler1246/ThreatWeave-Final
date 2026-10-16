import unittest
from evaluation.submission_analysis import oriented_comparison,point_target,percentile

class SubmissionAnalysisTests(unittest.TestCase):
    def test_baseline_first_sign_and_interval_are_both_reversed(self):
        rows=[dict(dimension='completeness',mode_a='text_only',mode_b='hybrid',mean_question_difference=-.75,
                   exploratory_95_percent_ci=[-1.2,-.2],paired_question_count=18,included_questions=['Q1'],excluded_questions=['Q2'])]
        actual=oriented_comparison(rows,'dimension','completeness','hybrid')
        self.assertEqual(actual['mean_difference'],.75)
        self.assertEqual(actual['exploratory_95_percent_ci'],[.2,1.2])
        self.assertEqual(actual['paired_question_count'],18)
        self.assertEqual(actual['excluded_questions'],['Q2'])

    def test_success_requires_all_three_targets_and_available_values(self):
        self.assertTrue(point_target(.5,0,0))
        self.assertFalse(point_target(.6,-.01,.2))
        self.assertFalse(point_target(.6,.1,-.01))
        self.assertFalse(point_target(.49,.2,.2))
        self.assertIsNone(point_target(.8,.2,None))

    def test_latency_p95_interpolation_and_undefined_empty_set(self):
        self.assertAlmostEqual(percentile([1,2,3,4],.95),3.85)
        self.assertIsNone(percentile([],.95))
