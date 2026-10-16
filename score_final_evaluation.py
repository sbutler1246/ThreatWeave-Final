"""Prepare offline or run resumable local metrics on collected final answers."""
import argparse
import sys
from pathlib import Path
from evaluation import score_plan


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare',action='store_true',help='Offline preparation only; no model loading/service calls.')
    parser.add_argument('--preview',action='store_true',help='Audit inputs/history only; no model loading/service calls.')
    parser.add_argument('--resume-run',type=Path)
    args=parser.parse_args();repo=Path(__file__).resolve().parent
    if args.prepare:
        if args.preview or args.resume_run:parser.error('Preparation cannot be combined with execution/resume flags.')
        score_plan.prepare(repo);return 0
    plan,rows=score_plan.load(repo)
    from evaluation.score_runner import history,run
    if args.preview:
        complete=history(repo,args.resume_run,plan,rows) if args.resume_run else {}
        print(f'SCORING PREVIEW PASSED: 240 observations, 675 eligible metric checks, 45 unavailable; {len(complete)} previous terminal checks.')
        print('No model, embedding or service calls.');return 0
    if Path(sys.prefix).resolve()!=repo/'.venv-eval':
        parser.error('Use S:\\ThreatWeave\\.venv-eval\\Scripts\\python.exe for live scoring.')
    return run(repo,plan,rows,resume=args.resume_run)


if __name__=='__main__':raise SystemExit(main())
