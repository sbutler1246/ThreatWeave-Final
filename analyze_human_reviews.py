"""Analyze fixed primary and secondary reviews only after completion checks pass."""
import argparse
from pathlib import Path
from evaluation.human_analysis import analyze

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primary', type=Path, default=Path('docs/ThreatWeave_primary_completed_ratings.json'))
    parser.add_argument('--secondary', type=Path, default=Path('docs/ThreatWeave_secondary_completed_ratings.json'))
    args = parser.parse_args()
    print('HUMAN ANALYSIS:', analyze(Path(__file__).resolve().parent, args.primary, args.secondary))
