"""Prepare only reviewed additional candidates, including explicit offline repairs."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from extraction.corpus_batch import prepare as prepare_batch, pending
from extraction.corpus_batch_review import unique_selection
from extraction.corpus_pilot import digest
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import make_prompt, validate_output
from graph.corpus_pilot_ingestion import add_review_provenance, check_decisions, supported_batch
from graph.development_ingestion import prepare_records

REVIEW_FILE = 'docs/ThreatWeave_corpus_batch_source_review.json'


def prepare(repo, *, review_file=REVIEW_FILE, batch_preparer=None,
            review_kind='corpus_batch_review_checks', run_kind='corpus_extraction_batch',
            implementation_files=None):
    repo = Path(repo).resolve()
    review_path = repo/review_file
    review = json.loads(review_path.read_text(encoding='utf-8'))
    if review.get('purpose') != 'AI_assisted_development_source_review' or review.get('human_review_status') != 'pending':
        raise ValueError('Invalid additional-development source-review identity.')
    run = (repo/review['original_run']).resolve()
    artifacts = (repo/review['review_artifacts']).resolve()
    if (artifacts.parent != (repo/'work'/review_kind).resolve()
            or not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}', artifacts.name)):
        raise ValueError('Review artifacts must be inside the workspace review-check folder.')
    items, config, catalog, attack_hash, identity, prepared, plan = (batch_preparer or prepare_batch)(repo)
    pending(repo, items, catalog, plan, run, output_kind=run_kind)
    summary_path, receipt_path = run/'summary.json', artifacts/'receipt.json'
    if (sha256_file(summary_path) != review['original_summary_sha256']
            or sha256_file(receipt_path) != review['artifact_receipt_sha256']
            or review['configuration_hash'] != plan['configuration_hash']
            or review['batch_plan_fingerprint'] != plan['fingerprint']):
        raise ValueError('Reviewed batch, source selection or extraction settings changed.')
    summary = json.loads(summary_path.read_text(encoding='utf-8'))
    receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
    if (receipt.get('status') != 'offline_revalidation_complete' or receipt.get('plan') != plan
            or receipt.get('original_summary_sha256') != review['original_summary_sha256']
            or receipt.get('graph_writes') is not False or receipt.get('service_calls') is not False
            or len(summary['items']) != len(items) or len(review['windows']) != len(items)
            or len(receipt['windows']) != len(items)
            or [r['scope_id'] for r in summary['items']] != plan['scope_ids']):
        raise ValueError('Review must cover the complete original batch exactly once.')
    # The validator and derivation policy are part of this offline checkpoint.
    expected_files = implementation_files or {'check_corpus_batch.py','extraction/corpus_batch_review.py',
                                              'extraction/development_batch.py','extraction/source_choices.py'}
    if set(receipt['implementation_sha256']) != set(expected_files):
        raise ValueError('Recorded offline validation implementation set changed.')
    for name, expected in receipt['implementation_sha256'].items():
        if sha256_file(repo/name) != expected:
            raise ValueError('Recorded offline validation implementation changed.')
    records, excluded, total = [], [], 0
    review_hash = sha256_file(review_path)
    for item, record, row, audit in zip(items, summary['items'], review['windows'], receipt['windows']):
        scope = item['chunk'].chunk_id
        name = record['folder']
        if (not re.fullmatch(r'\d{2}', name) or any(r.get('scope_id') != scope or r.get('folder') != name
                for r in [record, row, audit])):
            raise ValueError('Reviewed batch window order or identity changed.')
        case = run/name
        system, prompt, schema, index = make_prompt(item, catalog)
        def read(path):
            return json.loads(path.read_text(encoding='utf-8'))
        saved_index = dict(index, captions={k:v.model_dump(mode='json') for k,v in index['captions'].items()})
        if (read(case/'chunk.json') != item['chunk'].model_dump(mode='json')
                or read(case/'source_metadata.json') != item['preparation']
                or read(case/'source_choices.json') != saved_index or read(case/'output_schema.json') != schema
                or (case/'system_prompt.txt').read_text(encoding='utf-8') != system
                or (case/'user_prompt.txt').read_text(encoding='utf-8') != prompt
                or record['prompt_hash'] != digest({'system':system,'prompt':prompt,'schema':schema})):
            raise ValueError('Reviewed original source, prompt, schema or source choices changed.')
        attempt = record['attempts'][-1]
        if attempt.get('attempt') not in {1, 2} or attempt.get('http_status') != 200:
            raise ValueError('Review requires a recorded completed HTTP generation.')
        raw_path = case/f"raw_extraction_{attempt['attempt']}.json"
        raw = raw_path.read_text(encoding='utf-8')
        response = read(case/f"ollama_response_{attempt['attempt']}.json")
        if (sha256_file(raw_path) != row['original_raw_sha256'] or row['original_raw_sha256'] != audit['original_raw_sha256']
                or response.get('response') != raw or response.get('done') is not True
                or response.get('done_reason') != 'stop' or response.get('error')):
            raise ValueError('Reviewed original model output changed or is incomplete.')
        derived, transformations = (unique_selection(raw, index) if record['status']=='validation_failed' else (raw, []))
        if transformations != audit['transformations']:
            raise ValueError('Reviewed selector normalization changed.')
        batch, resolutions, alignments = validate_output(derived, item, catalog, index)
        values = {'derived_selection.json':json.loads(derived), 'candidate_extraction.json':batch.model_dump(mode='json'),
                  'identity_resolution.json':resolutions, 'quote_alignment.json':alignments}
        if set(row['file_sha256']) != set(values) or row['file_sha256'] != audit['artifact_sha256']:
            raise ValueError('Review attachment set changed.')
        for filename, expected in values.items():
            path = artifacts/name/filename
            if sha256_file(path) != row['file_sha256'][filename] or read(path) != expected:
                raise ValueError('Reviewed derived candidate, evidence or identity changed.')
        selected = check_decisions(row['decisions'], batch)
        total += len(batch.relations)
        excluded.extend(dict(d, folder=name, scope_id=scope) for d in row['decisions'] if d['disposition'] != 'supported')
        if selected:
            result = prepare_records(item, supported_batch(batch, selected), catalog, summary, record, raw, run,
                                     'AI_assisted_pinned_batch_source_review_with_explicit_offline_derivation')
            add_review_provenance(result, alignments, selected, row, review_hash)
            for assertion in result['assertions']:
                assertion.update(source_generation_status=record['status'],
                    source_generation_raw_file_sha256=row['original_raw_sha256'],
                    offline_validation_receipt_sha256=review['artifact_receipt_sha256'],
                    offline_selector_normalization_json=json.dumps(transformations, ensure_ascii=False))
            records.append(result)
    count = sum(len(item['assertions']) for item in records)
    if not count or count != review['supported_count'] or total != review['candidate_count'] or len(excluded) != review['excluded_count']:
        raise ValueError('Reviewed batch selection counts differ.')
    return {'items':records, 'excluded_candidates':excluded, 'prepared_at':datetime.now(timezone.utc).isoformat(),
            'attack_release':'17.1', 'attack_snapshot_hash':attack_hash, 'model_digest':summary['model_digest'],
            'human_review_status':'pending', 'review_manifest':str(review_path), 'review_manifest_sha256':review_hash,
            'extraction_run':str(run), 'configuration_hash':plan['configuration_hash'],
            'offline_validation_receipt_sha256':review['artifact_receipt_sha256']}
