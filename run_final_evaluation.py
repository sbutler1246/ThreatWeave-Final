"""Operator-run frozen 240-answer evaluation batch with four excluded warmups."""
import argparse
import getpass
import math
import sys
from pathlib import Path

from evaluation.experiment_plan import read_prepared
from evaluation.experiment_runner import history,run
from evaluation.experiment_runtime import Runtime


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--preview',action='store_true')
    parser.add_argument('--resume-run',type=Path)
    parser.add_argument('--timeout',type=float,default=60)
    args=parser.parse_args()
    if not math.isfinite(args.timeout) or not 0<args.timeout<=300:parser.error('Timeout must be positive and at most 300 seconds.')
    repo=args.repo.resolve();questions,plan,prepared=read_prepared(repo)
    if args.timeout!=plan['request_timeout_seconds']:
        parser.error('Use the frozen 60-second request timeout for this experiment.')
    complete=history(repo,args.resume_run,plan,questions) if args.resume_run else {}
    print('Frozen final experiment: 20 questions x four modes x three repeats = 240 measured cases, plus four warmups.')
    print('Plan:',plan['fingerprint'],'; preserved terminal cases:',len(complete))
    if args.preview:
        print('PREVIEW PASSED: Question-only inputs, frozen code/assets and schedule verified; no retrieval, embedding or service calls.')
        return 0
    uri=input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user=input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database=input('Database name [neo4j]: ').strip() or 'neo4j'
    password=getpass.getpass('Neo4j password (typing is hidden): ')
    try:
        return run(repo,questions,plan,lambda:Runtime(repo,plan,uri,user,password,database,args.timeout),resume=args.resume_run)
    finally:password=None


if __name__=='__main__':
    try:sys.exit(main())
    except (KeyboardInterrupt,EOFError):print('Final evaluation cancelled; saved runs remain.');sys.exit(2)
    except Exception as error:print('FAIL:',type(error).__name__,'— final preparation/assets could not be verified.');sys.exit(1)
