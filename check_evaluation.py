"""Operator-only synthetic check of all three locked local RAGAS metrics."""
import argparse
from pathlib import Path
from evaluation.judge_runtime import probe

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview',action='store_true')
    args = parser.parse_args()
    raise SystemExit(probe(Path(__file__).resolve().parent,preview=args.preview))
