"""Extract remaining prepared development windows; never write graph facts."""
import argparse
import json
import math
import sys
from pathlib import Path

from extraction.corpus_batch import pending, prepare
from extraction.corpus_chunking import load_verified_tokenizer
from extraction.corpus_pilot import run
from extraction.source_choices import make_prompt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--resume-run', type=Path)
    parser.add_argument('--timeout', type=float, default=60)
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error('--timeout must be positive and finite.')
    repo = args.repo.resolve()
    items, config, catalog, attack_hash, identity, prepared, plan = prepare(repo)
    completed = 0
    resume = args.resume_run.resolve() if args.resume_run else None
    if resume:
        items, completed = pending(repo, items, catalog, plan, resume)
    print(f'Development batch: {len(plan["scope_ids"])} remaining prepared windows; '
          f'{completed} already completed; {len(items)} to process.', flush=True)
    print('Plan fingerprint: '+plan['fingerprint'], flush=True)
    tokenizer, _ = load_verified_tokenizer(repo)
    for item in items:
        system, prompt, schema, index = make_prompt(item, catalog)
        tokens = len(tokenizer.encode(system+'\n'+prompt+'\n'+json.dumps(schema), add_special_tokens=False).ids)
        if tokens+config['llm']['num_predict']+256 > config['llm']['num_ctx']:
            raise ValueError('Batch prompt exceeds its reserved context budget: '+item['chunk'].chunk_id)
        if args.preview:
            print(f'  {item["chunk"].chunk_id}: {item["preparation"]["source_tokens"]} source tokens; '
                  f'{len(index["mentions"])} mentions; {tokens} estimated prompt/schema tokens.', flush=True)
    if args.preview:
        print('PREVIEW PASSED: Frozen sources, selection, settings and all prompt budgets verified; no service calls.', flush=True)
        return 0
    if not items:
        print('BATCH ALREADY PROCESSED: Saved results still require semantic review.', flush=True)
        return 0
    return run(repo, items, config, catalog, attack_hash, identity, prepared, args.timeout, resume, batch_plan=plan)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('Batch cancelled; saved records remain. Resume using the new batch folder.', flush=True)
        sys.exit(2)
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}', flush=True)
        sys.exit(1)
