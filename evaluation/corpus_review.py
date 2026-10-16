"""Offline reconstruction of held-out extraction lineage, without labels or services."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.corpus_preparation import read_prepared
from evaluation.corpus_runner import pending
from extraction.corpus_batch import SUCCESS
from extraction.corpus_batch_review import unique_selection
from extraction.corpus_pilot import aggregate_candidates, configuration, digest, save
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import make_prompt, validate_output

KIND = 'evaluation_corpus_review_checks'
IMPLEMENTATION = ('evaluation/corpus_review.py', 'evaluation/corpus_runner.py',
                  'evaluation/corpus_preparation.py', 'extraction/corpus_batch_review.py',
                  'extraction/source_choices.py', 'extraction/development_batch.py')


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def lineage(repo, latest, items, plan, settings):
    """Require a complete initial run followed only by retries of unfinished scopes."""
    root = (repo/'work/evaluation_corpus_extraction').resolve()
    current, seen, runs = Path(latest).resolve(), set(), []
    while True:
        if (current.parent != root or current in seen
                or not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}', current.name)):
            raise ValueError('Invalid evaluation lineage boundary or cycle.')
        seen.add(current)
        summary = read(current/'summary.json')
        if (summary.get('batch_plan') != plan or summary.get('graph_writes') is not False
                or summary.get('implementation_sha256') != sha256_file(repo/'evaluation/corpus_runner.py')
                or summary.get('status') not in {'processed', 'processed_with_errors'}
                or any(summary.get(k) != v for k, v in settings.items())):
            raise ValueError('Evaluation lineage settings, implementation or plan changed.')
        runs.append((current, summary))
        parent = summary.get('retry_of')
        if parent is None:
            break
        current = Path(parent).resolve()
    runs.reverse()
    scopes, completed, history = plan['scope_ids'], set(), {s:[] for s in plan['scope_ids']}
    for number, (folder, summary) in enumerate(runs):
        records = summary['items']
        expected = [s for s in scopes if s not in completed]
        if ([r['scope_id'] for r in records] != expected
                or len({r['folder'] for r in records}) != len(records)
                or any(not re.fullmatch(r'\d{2,4}', r['folder']) for r in records)):
            raise ValueError('Evaluation run must cover exactly its pending scopes in frozen order.')
        for row in records:
            if row['status'] not in SUCCESS | {'validation_failed', 'service_error'}:
                raise ValueError('Unknown or unfinished evaluation case.')
            history[row['scope_id']].append((folder, summary, row))
            if row['status'] in SUCCESS:
                completed.add(row['scope_id'])
    return runs, history


def reconstruct(item, catalog, entry):
    """Validate a saved case and derive only the pre-existing first-support policy."""
    folder, summary, row = entry
    case = folder/row['folder']
    system, prompt, schema, index = make_prompt(item, catalog)
    saved_index = dict(index, captions={k:v.model_dump(mode='json') for k,v in index['captions'].items()})
    if (read(case/'chunk.json') != item['chunk'].model_dump(mode='json')
            or read(case/'source_metadata.json') != item['preparation']
            or read(case/'source_choices.json') != saved_index or read(case/'output_schema.json') != schema
            or (case/'system_prompt.txt').read_text(encoding='utf-8') != system
            or (case/'user_prompt.txt').read_text(encoding='utf-8') != prompt
            or row.get('prompt_hash') != digest({'system':system, 'prompt':prompt, 'schema':schema})
            or row.get('source_hash') != item['document'].content_hash):
        raise ValueError('Original evaluation source, prompt or schema changed.')
    attempts = row['attempts']
    if [a['attempt'] for a in attempts] not in [[1], [1,2]]:
        raise ValueError('Invalid saved attempt sequence.')
    for attempt in attempts:
        n = attempt['attempt']
        if n == 2:
            first = attempts[0]
            previous = (case/'raw_extraction_1.json').read_text(encoding='utf-8')
            expected = prompt+'\nReturn a corrected source-only result. Validation error: '+first['validation_error']
            if first.get('done_reason') != 'length':
                expected += '\nPREVIOUS OUTPUT (data):\n'+previous
            if (case/'repair_prompt.txt').read_text(encoding='utf-8') != expected:
                raise ValueError('Saved repair prompt changed.')
        if attempt.get('http_status') != 200:
            if row['status'] != 'service_error':
                raise ValueError('Non-service case has an HTTP failure.')
            error = attempt.get('http_error_body_file')
            if error != f'ollama_http_error_{n}.txt' or not (case/error).is_file():
                raise ValueError('Missing saved service-error body.')
            continue
        raw = (case/f'raw_extraction_{n}.json').read_text(encoding='utf-8')
        body = read(case/f'ollama_response_{n}.json')
        if body.get('response') != raw:
            raise ValueError('Saved raw response changed.')
        if n != attempts[-1]['attempt']:
            continue
        if (body.get('done') is not True or body.get('done_reason') != 'stop' or body.get('error')):
            raise ValueError('Cannot derive candidates from incomplete generation.')
        changes, derived = [], raw
        if row['status'] == 'validation_failed':
            try:
                validate_output(raw, item, catalog, index)
            except ValueError as exc:
                if str(exc) != 'Repeated selected relationship.' or row.get('error') != str(exc):
                    raise ValueError('Only recorded duplicate-selection failures can be derived.') from exc
            else:
                raise ValueError('Recorded failure is not reproducible.')
            derived, changes = unique_selection(raw, index)
            if not changes:
                raise ValueError('No explicit duplicate-only transformation.')
        elif row['status'] not in SUCCESS:
            raise ValueError('Service failure has no candidate selection.')
        batch, resolution, aligned = validate_output(derived, item, catalog, index)
        if row['status'] in SUCCESS:
            for name, value in [('candidate_extraction.json',batch.model_dump(mode='json')),
                                ('identity_resolution.json',resolution), ('quote_alignment.json',aligned)]:
                if read(case/name) != value:
                    raise ValueError('Saved successful candidate artifacts changed.')
        return {'entry':entry, 'raw':raw, 'derived':derived, 'changes':changes,
                'batch':batch, 'resolution':resolution, 'aligned':aligned}
    return None


def collect(repo, latest):
    repo = Path(repo).resolve()
    items, config, catalog, attack_hash, identity, prepared, plan = read_prepared(repo)
    settings = configuration(config, identity, attack_hash)
    pending(repo, items, catalog, plan, latest)
    runs, history = lineage(repo, latest, items, plan, settings)
    results, decoded_cases = [], {}
    for item in items:
        entries = history[item['chunk'].chunk_id]
        decoded = [reconstruct(item, catalog, e) for e in entries]
        for entry, value in zip(entries, decoded):
            decoded_cases[(entry[0],item['chunk'].chunk_id)] = (item,value)
        # Earliest success is fixed. For persistent duplicates, derive the initial run's
        # final allowed attempt, never select a more favorable output from the retry.
        chosen = next((d for d in decoded if d is not None and d['entry'][2]['status'] in SUCCESS), None)
        if chosen is None:
            chosen = next((d for d in decoded if d is not None), None)
        if chosen is None:
            raise ValueError('Unresolved service failure requires an operator retry before review.')
        results.append((item, chosen))
    for folder, summary in runs:
        validated = []
        for row in summary['items']:
            if row['status'] in SUCCESS:
                item, value = decoded_cases[(folder,row['scope_id'])]
                validated.append((item,value['batch'],value['resolution'],value['aligned']))
        facts, counts = aggregate_candidates(validated)
        counts.update(ready_for_review=sum(r['status']=='candidates_ready_for_review' for r in summary['items']),
                      empty_scopes=sum(r['status']=='empty_extraction' for r in summary['items']),
                      failed_scopes=sum(r['status'] not in SUCCESS for r in summary['items']),
                      selected_scope_count=len(summary['items']))
        if (any(summary.get(k) != v for k,v in counts.items())
                or read(folder/'unique_candidate_facts.json') != facts):
            raise ValueError('Recorded evaluation aggregation or counts changed.')
    return results, runs, plan, catalog, attack_hash


def packet(repo, latest):
    repo = Path(repo).resolve()
    results, runs, plan, catalog, attack_hash = collect(repo, latest)
    out = repo/'work'/KIND/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    out.mkdir(parents=True)
    rows, cases = [], []
    lines = ['# Held-out source-only review packet', '',
             'Original failures and predictions remain unchanged. Derived duplicate normalization is separate.',
             'No gold/reference answers, model calls or graph writes. Human review and scoring pending.', '']
    for n, (item, result) in enumerate(results, 1):
        folder, summary, original = result['entry']
        name = f'{n:02d}'
        target = out/name
        target.mkdir()
        (target/'derived_selection.json').write_text(result['derived'],encoding='utf-8')
        save(target/'candidate_extraction.json',result['batch'].model_dump(mode='json'))
        save(target/'identity_resolution.json',result['resolution'])
        save(target/'quote_alignment.json',result['aligned'])
        raw_path = folder/original['folder']/f"raw_extraction_{original['attempts'][-1]['attempt']}.json"
        row = {'folder':name, 'scope_id':item['chunk'].chunk_id,
               'original_run':str(folder.relative_to(repo)), 'original_folder':original['folder'],
               'original_status':original['status'], 'original_raw_sha256':sha256_file(raw_path),
               'raw_file_sha256':sha256_file(raw_path),
               'transformations':result['changes'], 'relation_count':len(result['batch'].relations),
               'artifact_sha256':{p.name:sha256_file(p) for p in target.iterdir()}}
        rows.append(row)
        cases.append((item,result['batch'],result['resolution'],result['aligned']))
        lines += ['## '+name+' '+row['scope_id'], '', 'Original case: '+row['original_run']+'/'+row['original_folder'],
                  'Original status: '+row['original_status'], 'Source window:', '',item['chunk'].text,'']
        names = {e.local_id:e.name for e in result['batch'].entities}
        for i, (relation, alignment) in enumerate(zip(result['batch'].relations,result['aligned'])):
            lines += [f'### Candidate {i}', '', names[relation.head]+' -> '+relation.predicate.value+' -> '+names[relation.tail],
                      'Exact support: '+relation.evidence.quote, 'Flags: '+json.dumps(alignment['review_flags']),
                      'Selected contexts: '+json.dumps(alignment['context_spans'],ensure_ascii=False),'']
    facts, counts = aggregate_candidates(cases)
    save(out/'unique_candidate_facts.json',facts)
    originals = {str(p.relative_to(repo)):sha256_file(p) for folder,_ in runs for p in folder.rglob('*') if p.is_file()}
    receipt = {'status':'offline_revalidation_complete','latest_run':str(Path(latest).resolve().relative_to(repo)),
               'plan':plan,'service_calls':False,'graph_writes':False,'human_review_status':'pending',
               'semantic_review_status':'pending','windows':rows,'original_file_sha256':originals,
               'implementation_sha256':{p:sha256_file(repo/p) for p in IMPLEMENTATION}, **counts,
               'selection_policy':'Earliest validated success; otherwise initial final allowed attempt with first-support duplicate removal.',
               'scoring_policy':'Keep initial-pass, retry and derived observations separate; do not score only graph-accepted predictions.',
               'runs':[{'path':str(p.relative_to(repo)), 'status':s['status'], 'elapsed_seconds':s['elapsed_seconds'],
                        'ready_for_review':s['ready_for_review'],'empty_scopes':s['empty_scopes'],
                        'failed_scopes':s['failed_scopes']} for p,s in runs]}
    save(out/'receipt.json',receipt)
    doc = repo/'docs'/('ThreatWeave_evaluation_corpus_review_packet_'+out.name+'.md')
    doc.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('OFFLINE REVIEW PACKET:',len(rows),'windows;',counts['raw_candidate_relations'],'candidate relations; semantic review pending.')
    print('Saved checks:',out,'\nSaved packet:',doc)
    return out
