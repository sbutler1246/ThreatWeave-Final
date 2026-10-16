"""Offline checks for the frozen evaluator version gate; no model calls."""
import unittest
from unittest.mock import patch
from evaluation.run_ragas import PINNED_PACKAGES, require_pinned_versions

class EvaluatorVersions(unittest.TestCase):
    def test_matching_versions_are_accepted(self):
        with patch('evaluation.run_ragas.version', side_effect=PINNED_PACKAGES.__getitem__):
            require_pinned_versions()

    def test_ragas_upgrade_is_rejected(self):
        def installed(name):
            return '0.4.3' if name == 'ragas' else PINNED_PACKAGES[name]
        with patch('evaluation.run_ragas.version', side_effect=installed):
            with self.assertRaisesRegex(RuntimeError, 'ragas: expected 0.2.15'):
                require_pinned_versions()

if __name__ == '__main__':
    unittest.main()
