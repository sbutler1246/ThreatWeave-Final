"""Operator-run bounded extraction of seven held-out source reports."""
import argparse
import math
import sys
from pathlib import Path

from evaluation.corpus_runner import pending, run
from evaluation.corpus_preparation import OUTPUT_KIND, read_prepared


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--preview',action='store_true')
    parser.add_argument('--resume-run',type=Path)
    parser.add_argument('--timeout',type=float,default=60)
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or args.timeout<=0:
        parser.error('--timeout must be positive and finite.')
    repo = args.repo.resolve()
    items,config,catalog,attack_hash,identity,prepared,plan = read_prepared(repo)
    resume = args.resume_run.resolve() if args.resume_run else None
    completed = 0
    if resume:
        items,completed = pending(repo,items,catalog,plan,resume,output_kind=OUTPUT_KIND)
    print(f"Frozen held-out corpus batch: {len(plan['scope_ids'])} windows; {completed} completed; {len(items)} to process.",flush=True)
    print('Plan fingerprint: '+plan['fingerprint'],flush=True)
    print('Prepared records: '+str(prepared),flush=True)
    if args.preview:
        print('PREVIEW PASSED: Saved sources, exact selection, frozen settings and prompt budgets verified; no service calls.')
        return 0
    if not items:
        print('BATCH ALREADY PROCESSED: Saved candidates still require semantic source review.')
        return 0
    return run(repo,items,config,catalog,attack_hash,identity,prepared,args.timeout,resume,
               batch_plan=plan,output_kind=OUTPUT_KIND)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt,EOFError):
        print('Extraction cancelled; saved records remain. Resume with the printed batch folder.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}',flush=True)
        sys.exit(1)
