"""Audit saved final answers and prepare evaluator-only scoring/review files."""
import argparse
from pathlib import Path
from evaluation.final_review import prepare

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    args = parser.parse_args()
    prepare(Path(__file__).resolve().parent,args.run)
