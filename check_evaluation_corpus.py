"""Build a source-only held-out review packet without model or database calls."""
import argparse
from pathlib import Path
from evaluation.corpus_review import packet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--run',type=Path,required=True)
    args = parser.parse_args()
    packet(args.repo,args.run)
