"""Prepare report data from fixed human and preserved automatic analyses."""
import argparse
from pathlib import Path
from evaluation.submission_analysis import prepare

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--human-analysis',type=Path,required=True)
    args=p.parse_args()
    print('SUBMISSION RESULTS:',prepare(Path(__file__).resolve().parent,args.human_analysis))
