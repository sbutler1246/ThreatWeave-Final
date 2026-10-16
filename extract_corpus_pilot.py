"""Run the ten-window source-only extraction timing pilot with Ollama."""
import argparse
import json
import sys
from pathlib import Path

from extraction.corpus_pilot import configuration, digest, read_prepared, run
from extraction.source_choices import make_prompt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--prepared-run', type=Path)
    parser.add_argument('--retry-run', type=Path)
    parser.add_argument('--timeout', type=float, default=60)
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error('--timeout must be positive.')
    repo = args.repo.resolve()
    items, config, catalog, attack_hash, identity, prepared = read_prepared(repo, args.prepared_run)
    retry = None
    if args.retry_run:
        retry = args.retry_run.resolve()
        root = (repo/'work/corpus_extraction_pilot').resolve()
        if not retry.is_relative_to(root) or retry == root:
            raise ValueError('Retry run must be inside this workspace extraction-pilot folder.')
        previous = json.loads((retry/'summary.json').read_text(encoding='utf-8'))
        if previous.get('configuration_hash') != digest(configuration(config, identity, attack_hash)):
            raise ValueError('Retry extraction settings or prepared source identity changed.')
        failed = {item['scope_id'] for item in previous['items'] if item['status'] in {'service_error','validation_failed'}}
        items = [item for item in items if item['chunk'].chunk_id in failed]
        if {item['chunk'].chunk_id for item in items} != failed or not items:
            raise ValueError('No matching failed windows to retry; use a fresh run for an availability-check failure.')
    print(f'ThreatWeave extraction timing pilot: {len(items)} source windows across {len({item["document"].doc_id for item in items})} reports.', flush=True)
    if args.preview:
        from extraction.corpus_chunking import load_verified_tokenizer
        tokenizer, _ = load_verified_tokenizer(repo)
        for item in items:
            system, prompt, schema, index = make_prompt(item, catalog)
            tokens = len(tokenizer.encode(system+'\n'+prompt+'\n'+json.dumps(schema), add_special_tokens=False).ids)
            if tokens+config['llm']['num_predict']+256 > config['llm']['num_ctx']:
                raise ValueError('Pilot prompt exceeds its reserved context budget.')
            print(f'  {item["chunk"].chunk_id}: {item["preparation"]["source_tokens"]} source tokens; {len(index["mentions"])} mentions; {tokens} estimated prompt/schema tokens.', flush=True)
        print('PREVIEW PASSED: Saved chunks, frozen source/tokenizer/catalog hashes and prompt budgets verified; no service calls.', flush=True)
        return 0
    return run(repo, items, config, catalog, attack_hash, identity, prepared, args.timeout, retry)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('Pilot cancelled; existing saved records are preserved.', flush=True)
        sys.exit(2)
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}', flush=True)
        sys.exit(1)
