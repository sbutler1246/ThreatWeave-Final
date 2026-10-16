"""Revalidate one completed batch offline, preserving failures and derived repairs."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from extraction.corpus_batch import pending
from extraction.corpus_extension import read_prepared as prepare, OUTPUT_KIND
from extraction.corpus_batch_review import unique_selection
from extraction.corpus_pilot import aggregate_candidates, digest, save
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import make_prompt, validate_output


def check(repo, folder):
    repo, folder = Path(repo).resolve(), Path(folder).resolve()
    items, config, catalog, attack_hash, identity, prepared, plan = prepare(repo)
    # Confirms the workspace boundary, plan, settings and every recorded success.
    remaining, completed = pending(repo, items, catalog, plan, folder, output_kind=OUTPUT_KIND)
    summary = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
    if (summary.get('implementation_sha256') != sha256_file(repo/'extraction/corpus_pilot.py')
            or summary.get('retry_of') is not None or len(summary['items']) != len(items)
            or summary.get('status') not in {'processed', 'processed_with_errors'}
            or [r['scope_id'] for r in summary['items']] != plan['scope_ids']):
        raise ValueError('This review checkpoint requires a completed initial batch covering the full plan.')
    output = repo/'work/corpus_extension_review_checks'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    rows, cases = [], []
    lines = ['# Remaining three-report candidates: offline review packet', '',
             'Original model outputs and failures are preserved. Revalidated or derived candidates are not accepted graph facts.',
             'Semantic source review and human verification remain pending. No model/service calls or graph writes.', '']
    for item, row in zip(items, summary['items']):
        case = folder/row['folder']
        system, prompt, schema, index = make_prompt(item, catalog)
        if (json.loads((case/'chunk.json').read_text(encoding='utf-8')) != item['chunk'].model_dump(mode='json')
                or json.loads((case/'source_metadata.json').read_text(encoding='utf-8')) != item['preparation']
                or json.loads((case/'output_schema.json').read_text(encoding='utf-8')) != schema
                or (case/'system_prompt.txt').read_text(encoding='utf-8') != system
                or (case/'user_prompt.txt').read_text(encoding='utf-8') != prompt
                or json.loads((case/'source_choices.json').read_text(encoding='utf-8')) != dict(index, captions={k:v.model_dump(mode='json') for k,v in index['captions'].items()})
                or row['prompt_hash'] != digest({'system':system, 'prompt':prompt, 'schema':schema})):
            raise ValueError('Saved batch source, schema or original prompt changed.')
        attempt = row['attempts'][-1]['attempt']
        if attempt not in {1, 2}:
            raise ValueError('Invalid saved attempt.')
        raw_path = case/f'raw_extraction_{attempt}.json'
        raw = raw_path.read_text(encoding='utf-8')
        body = json.loads((case/f'ollama_response_{attempt}.json').read_text(encoding='utf-8'))
        if (body.get('done') is not True or body.get('done_reason') != 'stop'
                or row['attempts'][-1].get('http_status') != 200
                or body.get('error') or body.get('response') != raw):
            raise ValueError('Cannot derive candidates from an incomplete generation.')
        changes = []
        derived = raw
        if row['status'] == 'validation_failed':
            derived, changes = unique_selection(raw, index)
            if not changes:
                raise ValueError('A failed extension output requires an explicit duplicate-only derivation.')
        elif row['status'] not in {'candidates_ready_for_review', 'empty_extraction'}:
            raise ValueError('Unresolved service failure needs a separate operator-run retry.')
        batch, resolution, aligned = validate_output(derived, item, catalog, index)
        destination = output/row['folder']
        destination.mkdir()
        (destination/'derived_selection.json').write_text(derived, encoding='utf-8')
        save(destination/'candidate_extraction.json', batch.model_dump(mode='json'))
        save(destination/'identity_resolution.json', resolution)
        save(destination/'quote_alignment.json', aligned)
        candidates = batch.model_dump(mode='json')
        names = {e['local_id']:e['name'] for e in candidates['entities']}
        lines.extend(['## '+row['folder']+' · '+row['scope_id'], '',
                      'Original status: '+row['status'], 'Source: '+str(item['document'].source_url), ''])
        if row.get('error'):
            lines.extend(['Original validation error: '+row['error'], ''])
        lines.extend(['Exact source window:', '', item['chunk'].text, ''])
        for number, (relation, alignment) in enumerate(zip(candidates['relations'], aligned)):
            lines.extend([f'### Candidate {number}', '',
                          names[relation['head']]+' -> '+relation['predicate']+' -> '+names[relation['tail']],
                          'Exact supporting span: '+relation['evidence']['quote'],
                          'Review flags: '+json.dumps(alignment['review_flags']), ''])
        if not candidates['relations']:
            lines.extend(['Empty model extraction; coverage review still required.', ''])
        record = {'folder':row['folder'], 'scope_id':row['scope_id'], 'original_status':row['status'],
                  'original_error':row.get('error'), 'original_raw_sha256':sha256_file(raw_path),
                  'original_case':str(case.relative_to(repo)), 'transformations':changes,
                  'validation_recovery': 'first_support_duplicate_selection_v1' if changes else None,
                  'relation_count':len(batch.relations), 'semantic_review_status':'pending',
                  'artifact_sha256':{p.name:sha256_file(p) for p in destination.iterdir()}}
        rows.append(record)
        cases.append((item, batch, resolution, aligned))
    facts, counts = aggregate_candidates(cases)
    save(output/'unique_candidate_facts.json', facts)
    receipt = {'status':'offline_revalidation_complete', 'original_run':str(folder.relative_to(repo)),
               'original_summary_sha256':sha256_file(folder/'summary.json'), 'plan':plan,
               'original_successful_windows':completed, 'original_failed_windows':len(remaining),
               'revalidated_window_count':len(rows), 'recovered_windows':[r['folder'] for r in rows if r['original_status']=='validation_failed'],
               'service_calls':False, 'graph_writes':False, 'human_review_status':'pending',
               'semantic_review_status':'pending', **counts, 'windows':rows,
               'implementation_sha256':{name:sha256_file(repo/name) for name in [
                   'check_corpus_extension.py','extraction/corpus_extension.py','extraction/corpus_pilot.py','extraction/corpus_batch_review.py','extraction/development_batch.py',
                   'extraction/source_choices.py']}}
    save(output/'receipt.json', receipt)
    review = repo/'docs'/('ThreatWeave_corpus_extension_review_packet_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'OFFLINE REVIEW PACKET: {len(rows)} windows revalidated; {len(remaining)} recovered; '
          f'{counts["raw_candidate_relations"]} candidate relations; semantic review pending.')
    print('Saved checks: '+str(output)+'\nSaved review packet: '+str(review))
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--run', type=Path, required=True)
    args = parser.parse_args()
    check(args.repo, args.run)
