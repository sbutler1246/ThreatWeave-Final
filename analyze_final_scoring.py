"""Offline saved-score audit and paired question bootstrap; never calls models."""
import argparse
from pathlib import Path
from evaluation.score_analysis import analyze

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--run',type=Path,required=True)
    args=parser.parse_args();analyze(Path(__file__).resolve().parent,args.run)
