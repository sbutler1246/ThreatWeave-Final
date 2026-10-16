"""Prepare and check the seven held-out source reports without service calls."""
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from extraction.corpus_chunking import load_verified_tokenizer
from evaluation.corpus_preparation import PREPARED_KIND, prepare, preflight
from extraction.corpus_pilot import save


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--preview',action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    items,config,catalog,_,identity,plan = prepare(repo)
    checks = preflight(items,config,catalog,load_verified_tokenizer(repo)[0])
    for doc in identity['documents']:
        rows = [r for r in checks if r['doc_id']==doc['doc_id']]
        print(f"{doc['doc_id']}: {len(rows)} windows; source tokens {min(r['source_tokens'] for r in rows)}-{max(r['source_tokens'] for r in rows)}; "
              f"estimated prompt/schema tokens {min(r['estimated_prompt_schema_tokens'] for r in rows)}-{max(r['estimated_prompt_schema_tokens'] for r in rows)}.",flush=True)
    failed = [r['scope_id'] for r in checks if not r['within_budget']]
    if failed:
        raise ValueError('Prompt budget preflight failed: '+', '.join(failed))
    empty = [r['scope_id'] for r in checks if not r['mention_count']]
    print(f'{len(items)} windows; {len(empty)} without recognized mentions. No service calls or graph writes.',flush=True)
    if args.preview:
        print('PREVIEW PASSED: Frozen held-out source selection, exact token-measured spans and prompt budgets verified; no labels or services.')
        return 0
    folder = repo/'work'/PREPARED_KIND/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True,exist_ok=False)
    save(folder/'chunks.json',[i['preparation'] for i in items])
    save(folder/'preflight.json',checks)
    save(folder/'summary.json',{'status':'ready_for_operator_extraction', 'identity':identity, 'plan':plan,
                              'model_calls':False, 'graph_writes':False, 'window_count':len(items),
                              'zero_mention_scope_ids':empty, 'human_review_status':'pending',
                              'finished_at':datetime.now(timezone.utc).isoformat()})
    pointer = folder.parent/'current.json'
    temporary = pointer.with_suffix('.tmp')
    save(temporary,{'run':folder.name,'fingerprint':identity['fingerprint']})
    temporary.replace(pointer)
    lines = ['# Seven held-out reports: source preparation','',
             'No model/service calls, graph writes or evaluation scores. Human verification pending.',
             'Frozen source-only selection includes the seven held-out reports only. No benchmark labels or reference answers are loaded.',
             'Gold triples and QA reference answers were not read. Technical sections end before Mitigations.',
             'The four-relation cap and existing mention/table recognition limits remain diagnostic constraints.',
             '', 'Saved artifacts: '+str(folder), 'Prepared fingerprint: '+identity['fingerprint'],
             'Extraction plan fingerprint: '+plan['fingerprint'],'',
             '| Report | Windows | Technical source span |','| --- | ---: | --- |']
    lines += [f"| {d['doc_id']} | {d['chunk_count']} | {d['technical_start']}:{d['technical_end']} |" for d in identity['documents']]
    lines += ['',f'Total windows: {len(items)}. Windows without recognized mentions: {len(empty)}.',
              'Prompt budgets reserve 700 output tokens and 256 chat tokens within the unchanged 8192-token context.',
              'These are estimates, not live formatted-prompt measurements.', '',
              '## Per-window preflight','',
              '| Scope | Source tokens | Mentions | Evidence patterns | Estimated prompt/schema tokens |',
              '| --- | ---: | ---: | ---: | ---: |']
    lines += [f"| {r['scope_id']} | {r['source_tokens']} | {r['mention_count']} | {r['evidence_pattern_count']} | {r['estimated_prompt_schema_tokens']} |" for r in checks]
    lines += ['', 'Next: operator-run bounded extraction, followed by candidate source review before any isolated evaluation import or index refresh; no tuning from held-out outputs.']
    review = repo/'docs'/('ThreatWeave_evaluation_corpus_preparation_'+folder.name+'.md')
    review.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('Saved prepared records: '+str(folder))
    print('Saved review document: '+str(review))
    print('READY: Seven-report evaluation source preparation and prompt preflight passed.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}',flush=True)
        sys.exit(1)
