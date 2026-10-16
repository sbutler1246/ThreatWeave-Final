"""Run five small source-bound development extractions across three CISA reports."""
import argparse
import sys
from pathlib import Path
from extraction.development_batch import make_prompt,read_inputs,run_batch,select_retry_items


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--preview',action='store_true')
    parser.add_argument('--timeout',type=int,default=60)
    parser.add_argument('--retry-run',type=Path,help='Retry only failed scopes from a previous batch; save a new run.')
    args = parser.parse_args()
    if args.timeout<=0:
        parser.error('--timeout must be positive')
    repo = args.repo.resolve()
    items,config,catalog,attack_hash = read_inputs(repo)
    if args.retry_run:
        items = select_retry_items(repo,items,args.retry_run,config,attack_hash)
        if not items:
            print('No failed scopes to retry.')
            return 0
    print(f'ThreatWeave development batch: {len(items)} chunks across {len({i["document"].doc_id for i in items})} reports.',flush=True)
    if args.preview:
        for item in items:
            make_prompt(repo,item)
            print('\n'+item['chunk'].chunk_id+'\n'+item['chunk'].text)
        print('\nPREVIEW PASSED: Frozen checksums, split boundaries, schema and source spans verified.')
        return 0
    return run_batch(repo,items,config,catalog,attack_hash,timeout=args.timeout,retry_run=args.retry_run)


if __name__=='__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt,EOFError):
        print('\nBatch cancelled; existing results remain in work/development_batch.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)
