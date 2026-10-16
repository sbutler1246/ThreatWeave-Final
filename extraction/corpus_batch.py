"""Select remaining prepared development windows without changing pilot settings."""
import json
import re
from pathlib import Path

from extraction.corpus_pilot import configuration, digest, read_prepared
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import make_prompt, validate_output

PILOT_RUN = '20261015T035023Z-f4b7051e'
REVIEW_FILE = 'docs/ThreatWeave_corpus_pilot_v2_6_review.json'
SUCCESS = {'candidates_ready_for_review', 'empty_extraction'}


def prepare(repo):
    repo = Path(repo).resolve()
    items, config, catalog, attack_hash, identity, prepared = read_prepared(repo, selection='all')
    review_path = repo/REVIEW_FILE
    review = json.loads(review_path.read_text(encoding='utf-8'))
    baseline_path = repo/'work/corpus_extraction_pilot'/PILOT_RUN/'summary.json'
    baseline = json.loads(baseline_path.read_text(encoding='utf-8'))
    settings_hash = digest(configuration(config, identity, attack_hash))
    expected = [item['chunk'].chunk_id for item in items if item['preparation']['pilot_selected']]
    if (review.get('run') != PILOT_RUN or review.get('summary_sha256') != sha256_file(baseline_path)
            or baseline.get('status') != 'processed' or baseline.get('configuration_hash') != settings_hash
            or baseline.get('graph_writes') is not False
            or [row['scope_id'] for row in baseline['items']] != expected
            or any(row['status'] not in SUCCESS for row in baseline['items'])):
        raise ValueError('The completed pinned pilot must match the frozen sources and extraction settings.')
    remaining = [item for item in items if not item['preparation']['pilot_selected']]
    plan = {'version': 1, 'prepared_fingerprint': identity['fingerprint'],
            'configuration_hash': settings_hash, 'baseline_run': PILOT_RUN,
            'baseline_summary_sha256': sha256_file(baseline_path),
            'review_manifest_sha256': sha256_file(review_path),
            'excluded_pilot_scope_ids': expected,
            'scope_ids': [item['chunk'].chunk_id for item in remaining],
            'selection': 'All remaining prepared technical windows; no labels or reference answers.'}
    plan['fingerprint'] = digest(plan)
    return remaining, config, catalog, attack_hash, identity, prepared, plan


def pending(repo, items, catalog, plan, resume_run, *, output_kind='corpus_extraction_batch'):
    """Walk linked runs and revalidate saved successes before excluding them."""
    if output_kind not in {'corpus_extraction_batch','corpus_extension_extraction'}:
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
        if len({r['scope_id'] for r in records}) != len(records):
            raise ValueError('Duplicate saved batch window.')
        for row in records:
            if row['scope_id'] not in by_id or not re.fullmatch(r'\d{2}', row['folder']):
                raise ValueError('Unexpected saved batch window or folder.')
            if row['status'] not in SUCCESS:
                continue
            item = by_id[row['scope_id']]
            case = folder/row['folder']
            system, prompt, schema, index = make_prompt(item, catalog)
            if (row.get('source_hash') != item['document'].content_hash
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
            if (body.get('done') is not True or body.get('done_reason') == 'length'
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
