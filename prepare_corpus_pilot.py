"""Prepare token-measured, source-only chunks for the five-report development pilot."""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from extraction.corpus_chunking import prepare


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--preview', action='store_true', help='Validate and summarize without saving a chunk run.')
    args = parser.parse_args()
    repo = args.repo.resolve()
    records, identity = prepare(repo)
    selected = [r for r in records if r['pilot_selected']]
    print('ThreatWeave five-report source preparation:', flush=True)
    for doc in identity['documents']:
        subset = [r for r in records if r['doc_id'] == doc['doc_id']]
        print(f'  {doc["doc_id"]}: {len(subset)} windows; source tokens {min(r["source_tokens"] for r in subset)}-{max(r["source_tokens"] for r in subset)}; two selected.', flush=True)
    print(f'Pilot: {len(selected)} windows across five reports. No model calls or graph writes.', flush=True)
    if args.preview:
        print('PREVIEW PASSED: Frozen sources, held-out exclusion, token counts, offsets and overlap checked.', flush=True)
        return 0
    output = repo/'work/corpus_pilot_chunks'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    save(output/'chunks.json', records)
    save(output/'pilot_chunks.json', selected)
    summary = dict(identity, status='ready_for_extraction_pilot', graph_writes=False, model_calls=False,
                   full_chunk_count=len(records), pilot_chunk_count=len(selected),
                   finished_at=datetime.now(timezone.utc).isoformat())
    save(output/'summary.json', summary)
    pointer = output.parent/'current.json'
    temporary = pointer.with_suffix('.tmp')
    save(temporary, {'run': output.name, 'fingerprint': identity['fingerprint']})
    temporary.replace(pointer)
    lines = ['# Five-report source chunk preparation', '',
             'Status: ready for extraction pilot. No extraction, database writes or evaluation scores were produced.', '',
             'Source-only selection: BianLian, Rhysida, Scattered Spider, ALPHV Blackcat and Phobos.',
             'Reports containing held-out evidence were excluded using split metadata. Gold labels and QA reference answers were not read.', '',
             'Tokenizer artifact: '+identity['tokenizer']['run'],
             'Tokenizer SHA-256: '+identity['tokenizer']['sha256'],
             'Chunk fingerprint: '+identity['fingerprint'], '',
             'Technical sections run from the Technical Details heading to the Mitigations heading. Exact normalized source offsets and checksums are preserved.',
             'This is a pilot subset, not the complete 15-report corpus. IOC/table content inside the technical sections is retained; row and caption support needs semantic review during extraction.',
             'Window counts exclude inherited context and chat/system/schema overhead, which must be budgeted separately.',
             'Line boundaries are preferred within 400–600 source tokens, targeting 500 with about 60-token overlap. Final windows may be reanchored with greater overlap to retain the minimum size; measured overlap is recorded.', '',
             '| Report | All windows | Pilot windows |', '| --- | ---: | ---: |']
    lines.extend(f'| {doc["doc_id"]} | {doc["chunk_count"]} | 2 |' for doc in identity['documents'])
    lines.extend(['', '## Selected pilot windows', ''])
    for number, item in enumerate(selected, 1):
        chunk = item['chunk']
        lines.extend([f'### {number}. {chunk["chunk_id"]}', '',
                      f'Offsets: {chunk["start"]}:{chunk["end"]}; source tokens: {item["source_tokens"]}; inherited context tokens: {item["inherited_context_tokens"]}; preceding overlap: {item["overlap_with_previous_tokens"]}.', '',
                      'Source: '+item['source_url'], '', 'Inherited source context:', ''])
        lines.extend(c['text'] for c in chunk['inherited_context'])
        lines.extend(['', 'Exact source window:', '', chunk['text'], ''])
    lines.extend(['Next: bounded source-only extraction of these ten windows, with candidate review, per-attempt timing, failures and overlap deduplication recorded. Index refresh and final benchmark evaluation remain pending.', ''])
    review = repo/'docs'/('ThreatWeave_corpus_pilot_chunks_'+output.name+'.md')
    review.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Saved chunk records: {output}\nSaved review document: {review}', flush=True)
    print('READY: Five-report token-measured source chunks prepared; ten pilot windows selected.', flush=True)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}', flush=True)
        sys.exit(1)
