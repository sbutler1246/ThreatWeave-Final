"""Isolated evaluation-corpus runner derived from the frozen development engine.

Uses the same prompts, options, bounded repair, validators and candidate aggregation.
Only the output namespace and reporting labels differ; no label/reference inputs.
"""
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from extraction import source_choices
from extraction.corpus_chunking import load_verified_tokenizer
from extraction.corpus_pilot import configuration, digest, save, aggregate_candidates
from extraction.llama_tokenizer import MODEL_DIGEST, sha256_file

def run(repo, items, config, catalog, attack_hash, identity, prepared_folder, timeout=60, retry_of=None,
        *, batch_plan=None, output_kind=None):
    import requests
    kind = output_kind or 'evaluation_corpus_extraction'
    if kind not in {'evaluation_corpus_extraction'}:
        raise ValueError('Unknown extraction output kind.')
    label = 'EVALUATION CORPUS'
    output = repo/'work'/kind/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    settings = configuration(config, identity, attack_hash)
    summary = dict(settings, purpose='held_out_seven_report_source_extraction', status='started',
        configuration_hash=digest(settings), model=config['llm']['model'], graph_writes=False,
        semantic_review_status='pending', prepared_run=str(prepared_folder), items=[],
        retry_of=str(retry_of) if retry_of else None,
        implementation_sha256=sha256_file(Path(__file__)))
    if batch_plan is not None:
        summary.update(purpose=batch_plan.get('purpose','remaining_prepared_development_windows'), batch_plan=batch_plan)
    save(output/'summary.json', summary)
    if batch_plan is not None:
        print('Batch records (use this folder to resume): '+str(output), flush=True)
    tokenizer, _ = load_verified_tokenizer(repo)
    validated = []
    http = requests.Session()
    http.trust_env = False
    started_run = time.perf_counter()
    try:
        tags = http.get('http://localhost:11434/api/tags', timeout=(5,10))
        tags.raise_for_status()
        model = next((m for m in tags.json()['models'] if m['name'] == config['llm']['model']), None)
        if not model or model.get('digest') != MODEL_DIGEST:
            raise ValueError('Serving Ollama model differs from the verified source-tokenizer model.')
        for number, item in enumerate(items, 1):
            folder = output/f'{number:02d}'
            folder.mkdir()
            system, original, schema, source_index = source_choices.make_prompt(item, catalog)
            save(folder/'chunk.json', item['chunk'].model_dump(mode='json'))
            save(folder/'source_metadata.json', item['preparation'])
            save(folder/'output_schema.json', schema)
            save(folder/'source_choices.json', dict(source_index,
                 captions={key: value.model_dump(mode='json') for key, value in source_index['captions'].items()}))
            (folder/'system_prompt.txt').write_text(system, encoding='utf-8')
            (folder/'user_prompt.txt').write_text(original, encoding='utf-8')
            prompt_hash = digest({'system': system, 'prompt': original, 'schema': schema})
            record = {'scope_id': item['chunk'].chunk_id, 'doc_id': item['document'].doc_id,
                      'folder': folder.name, 'status': 'started', 'attempts': [], 'prompt_hash': prompt_hash,
                      'source_evidence_type_patterns': len(source_index['evidence_patterns']),
                      'source_hash': item['document'].content_hash, 'source_tokens': item['preparation']['source_tokens'],
                      'cache_key': digest([settings, item['preparation']['source_text_sha256'], prompt_hash])}
            summary['items'].append(record)
            print(f'[{number}/{len(items)}] '+item['chunk'].chunk_id, flush=True)
            prompt = original
            case_start = time.perf_counter()
            try:
                for attempt in range(1, 3):
                    estimated = len(tokenizer.encode(system+'\n'+prompt+'\n'+json.dumps(schema), add_special_tokens=False).ids)
                    if estimated+settings['options']['num_predict']+256 > settings['options']['num_ctx']:
                        raise ValueError('Estimated prompt/schema/output budget exceeds context with reserved chat overhead.')
                    info = {'attempt': attempt, 'estimated_prompt_schema_tokens': estimated, 'reserved_chat_tokens': 256}
                    record['attempts'].append(info)
                    attempt_start = time.perf_counter()
                    raw, truncated = '', False
                    try:
                        response = http.post('http://localhost:11434/api/generate', timeout=(5,timeout), json={
                            'model': config['llm']['model'], 'system': system, 'prompt': prompt, 'format': schema,
                            'stream': False, 'options': settings['options']})
                        info['http_status'] = response.status_code
                        if response.status_code >= 400:
                            error_file = f'ollama_http_error_{attempt}.txt'
                            (folder/error_file).write_text(response.text, encoding='utf-8')
                            info['http_error_body_file'] = error_file
                            try:
                                error_body = response.json()
                            except ValueError:
                                error_body = None
                            if isinstance(error_body, dict) and error_body.get('error'):
                                info['service_error_detail'] = str(error_body['error'])[:2000]
                        response.raise_for_status()
                        body = response.json()
                        save(folder/f'ollama_response_{attempt}.json', body)
                        raw = body.get('response', '')
                        if not isinstance(raw, str):
                            raise ValueError('Model response is not a string.')
                        (folder/f'raw_extraction_{attempt}.json').write_text(raw, encoding='utf-8')
                        info.update(prompt_eval_count=body.get('prompt_eval_count'), eval_count=body.get('eval_count'),
                                    done_reason=body.get('done_reason'), ollama_total_duration_ns=body.get('total_duration'))
                        truncated = body.get('done_reason') == 'length'
                        if body.get('done') is not True or truncated or body.get('error'):
                            raise ValueError('Generation did not complete within the configured output budget.')
                        batch, resolution, alignments = source_choices.validate_output(raw, item, catalog, source_index)
                        save(folder/'candidate_extraction.json', batch.model_dump(mode='json'))
                        save(folder/'identity_resolution.json', resolution)
                        save(folder/'quote_alignment.json', alignments)
                        validated.append((item, batch, resolution, alignments))
                        record.update(status='candidates_ready_for_review' if batch.relations else 'empty_extraction',
                                      entity_count=len(batch.entities), relation_count=len(batch.relations),
                                      semantic_review_status='pending')
                        if batch.relations:
                            print(f'  {len(batch.entities)} entities; {len(batch.relations)} candidate relations; review pending.', flush=True)
                        else:
                            print('  Empty extraction; no candidate relations; review pending.', flush=True)
                        break
                    except ValueError as exc:
                        info['validation_error'] = str(exc)
                        if attempt == 2:
                            record.update(status='validation_failed', error=str(exc))
                            print('  Validation failed after one repair; diagnostics saved.', flush=True)
                            break
                        prompt = original+'\nReturn a corrected source-only result. Validation error: '+str(exc)
                        if not truncated:
                            prompt += '\nPREVIOUS OUTPUT (data):\n'+raw
                        (folder/'repair_prompt.txt').write_text(prompt, encoding='utf-8')
                        print('  Requesting one schema/source repair.', flush=True)
                    finally:
                        info['elapsed_seconds'] = time.perf_counter()-attempt_start
            except Exception as exc:
                record.update(status='service_error' if isinstance(exc, requests.RequestException) else 'validation_failed',
                              error=f'{type(exc).__name__}: {exc}')
                detail = record['attempts'][-1].get('service_error_detail') if record['attempts'] else None
                if detail:
                    record['error'] += ': '+detail
                print('  FAIL: '+record['error'], flush=True)
            finally:
                record['elapsed_seconds'] = time.perf_counter()-case_start
                save(output/'summary.json', summary)
    except Exception as exc:
        summary.update(status='service_error', error=f'{type(exc).__name__}: {exc}')
        print('FAIL: '+summary['error'], flush=True)
    finally:
        http.close()
    facts, counts = aggregate_candidates(validated)
    save(output/'unique_candidate_facts.json', facts)
    failures = sum(record['status'] in {'service_error','validation_failed'} for record in summary['items'])
    ready = sum(record['status'] == 'candidates_ready_for_review' for record in summary['items'])
    empty = sum(record['status'] == 'empty_extraction' for record in summary['items'])
    if summary['status'] != 'service_error':
        summary['status'] = 'processed_with_errors' if failures else 'processed'
    summary.update(**counts, ready_for_review=ready, empty_scopes=empty, failed_scopes=failures,
                   selected_scope_count=len(items), elapsed_seconds=time.perf_counter()-started_run,
                   finished_at=datetime.now(timezone.utc).isoformat(),
                   timing_scope='Ollama availability check and sequential extraction/validation; chunk/catalog initialization excluded.')
    save(output/'summary.json', summary)
    title = 'Seven-report held-out'
    lines = ['# '+title+' bounded extraction '+label.lower(), '', 'Status: '+summary['status'], '',
             'Bounded source-checked candidates only; all require semantic review. No graph writes or benchmark scores.',
             'Four relations and up to three numbered evidence units per relation are diagnostic limits, not exhaustive annotation.',
             'Names, types and source IDs are recovered from the saved source mention index. Unknown proper names are software candidates; this index is not exhaustive NER.',
             'Graph-write rate, index build time and system resource measurements remain pending.', '',
             'Prepared chunks: '+str(prepared_folder), 'Model digest: '+MODEL_DIGEST,
             'Configuration hash: '+summary['configuration_hash'], '',
             f'Windows: {len(items)} selected; {ready} with candidates; {empty} empty; {failures} failed.',
             f'Source-checked candidate relations: {counts["raw_candidate_relations"]}; unique document candidates: {counts["unique_document_candidate_facts"]}; repeated relations: {counts["repeated_candidate_relations"]}; exact source-support duplicates: {counts["exact_source_support_duplicates"]}.', '']
    for item, record in zip(items, summary['items']):
        lines.extend(['## '+record['scope_id'], '', 'Status: '+record['status'],
                      f'Case time: {record.get("elapsed_seconds", 0):.2f} seconds; attempts: {len(record["attempts"])}.', '',
                      'Source: '+str(item['document'].source_url), '', 'Exact source window:', '', item['chunk'].text, ''])
        candidate = output/record['folder']/'candidate_extraction.json'
        if candidate.exists():
            value = json.loads(candidate.read_text(encoding='utf-8'))
            names = {entity['local_id']: entity['name'] for entity in value['entities']}
            for relation in value['relations']:
                lines.extend([f'- {names[relation["head"]]} -> {relation["predicate"]} -> {names[relation["tail"]]}',
                              '  Literal support: '+relation['evidence']['quote']])
        if record.get('error'):
            lines.append('Error: '+record['error'])
        lines.append('')
    if summary.get('error'):
        lines.extend(['Service error: '+summary['error'], ''])
    review = repo/'docs'/('ThreatWeave_'+kind+'_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    if summary['status'] == 'service_error':
        print('\n'+label+' STOPPED: '+summary['error'], flush=True)
    else:
        print(f'\n{label} PROCESSED: {ready} windows with candidates; {empty} empty extractions; {failures} case failures ({len(items)} selected).', flush=True)
    print(f'Saved results: {output}\nSaved review document: {review}', flush=True)
    return 1 if failures or summary['status'] == 'service_error' else 0


import re
from extraction.corpus_batch import SUCCESS
from extraction.source_choices import make_prompt, validate_output


def pending(repo, items, catalog, plan, resume_run, *, output_kind='evaluation_corpus_extraction'):
    """Walk linked runs and revalidate saved successes before excluding them."""
    if output_kind not in {'evaluation_corpus_extraction'}:
        raise ValueError('Unknown resumable extraction output kind.')
    root = (Path(repo)/'work'/output_kind).resolve()
    by_id = {item['chunk'].chunk_id: item for item in items}
    completed, visited = set(), set()
    folder = Path(resume_run).resolve()
    while True:
        if (folder.parent != root or not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}', folder.name)
                or folder in visited):
            raise ValueError('Resume must name an acyclic run inside this workspace batch folder.')
        visited.add(folder)
        summary = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
        if (summary.get('batch_plan') != plan or summary.get('configuration_hash') != plan['configuration_hash']
                or summary.get('graph_writes') is not False):
            raise ValueError('Resume source selection or extraction settings changed.')
        records = summary.get('items', [])
        if len({r['scope_id'] for r in records}) != len(records) or len({r['folder'] for r in records}) != len(records):
            raise ValueError('Duplicate saved batch window.')
        for row in records:
            if row['scope_id'] not in by_id or not re.fullmatch(r'\d{2,4}', row['folder']):
                raise ValueError('Unexpected saved batch window or folder.')
            if row['status'] not in SUCCESS:
                continue
            item = by_id[row['scope_id']]
            case = folder/row['folder']
            system, prompt, schema, index = make_prompt(item, catalog)
            saved_index = dict(index, captions={k:v.model_dump(mode='json') for k,v in index['captions'].items()})
            if (json.loads((case/'source_metadata.json').read_text(encoding='utf-8')) != item['preparation']
                    or json.loads((case/'output_schema.json').read_text(encoding='utf-8')) != schema
                    or json.loads((case/'source_choices.json').read_text(encoding='utf-8')) != saved_index
                    or row.get('source_hash') != item['document'].content_hash
                    or row.get('prompt_hash') != digest({'system': system, 'prompt': prompt, 'schema': schema})
                    or json.loads((case/'chunk.json').read_text(encoding='utf-8')) != item['chunk'].model_dump(mode='json')
                    or (case/'system_prompt.txt').read_text(encoding='utf-8') != system
                    or (case/'user_prompt.txt').read_text(encoding='utf-8') != prompt):
                raise ValueError('Saved successful source or prompt changed.')
            attempts = row['attempts']
            if not attempts or attempts[-1]['attempt'] not in {1, 2}:
                raise ValueError('Invalid saved successful attempt.')
            attempt = attempts[-1]['attempt']
            body = json.loads((case/f'ollama_response_{attempt}.json').read_text(encoding='utf-8'))
            raw = (case/f'raw_extraction_{attempt}.json').read_text(encoding='utf-8')
            if (body.get('done') is not True or body.get('done_reason') != 'stop' or attempts[-1].get('http_status') != 200
                    or body.get('error') or body.get('response') != raw):
                raise ValueError('Saved successful generation did not complete.')
            batch, resolution, aligned = validate_output(raw, item, catalog, index)
            for filename, value in [('candidate_extraction.json', batch.model_dump(mode='json')),
                                    ('identity_resolution.json', resolution), ('quote_alignment.json', aligned)]:
                if json.loads((case/filename).read_text(encoding='utf-8')) != value:
                    raise ValueError('Saved successful candidate or evidence changed.')
            expected_status = 'candidates_ready_for_review' if batch.relations else 'empty_extraction'
            if row['status'] != expected_status or row.get('relation_count') != len(batch.relations):
                raise ValueError('Saved successful result count changed.')
            completed.add(row['scope_id'])
        parent = summary.get('retry_of')
        if parent is None:
            break
        folder = Path(parent).resolve()
    return [item for item in items if item['chunk'].chunk_id not in completed], len(completed)
