"""Review-gated held-out assertions with explicit evaluation provenance."""
import json
from datetime import datetime, timezone
from pathlib import Path

from evaluation.corpus_review import KIND, IMPLEMENTATION, collect, read
from extraction.llama_tokenizer import sha256_file
from graph.corpus_pilot_ingestion import add_review_provenance, check_decisions, supported_batch
from graph.development_ingestion import prepare_records

REVIEW_FILE = 'docs/ThreatWeave_evaluation_corpus_source_review.json'
FILES = {'derived_selection.json','candidate_extraction.json','identity_resolution.json','quote_alignment.json'}


def prepare(repo):
    repo = Path(repo).resolve()
    path = repo/REVIEW_FILE
    review = read(path)
    if (review.get('purpose') != 'AI_assisted_frozen_evaluation_source_review'
            or review.get('human_review_status') != 'pending'):
        raise ValueError('Invalid held-out source review identity.')
    artifacts = (repo/review['review_artifacts']).resolve()
    if artifacts.parent != (repo/'work'/KIND).resolve():
        raise ValueError('Evaluation review artifacts escape workspace boundary.')
    receipt_path = artifacts/'receipt.json'
    if sha256_file(receipt_path) != review['artifact_receipt_sha256']:
        raise ValueError('Evaluation validation receipt changed.')
    receipt = read(receipt_path)
    if (receipt.get('status') != 'offline_revalidation_complete'
            or receipt.get('service_calls') is not False or receipt.get('graph_writes') is not False
            or set(receipt['implementation_sha256']) != set(IMPLEMENTATION)):
        raise ValueError('Invalid offline held-out validation receipt.')
    for filename, expected in receipt['implementation_sha256'].items():
        if sha256_file(repo/filename) != expected:
            raise ValueError('Held-out source review implementation changed.')
    results, runs, plan, catalog, attack_hash = collect(repo, repo/receipt['latest_run'])
    if (review['batch_plan_fingerprint'] != plan['fingerprint'] or receipt['plan'] != plan
            or review['configuration_hash'] != plan['configuration_hash']
            or len(review['windows']) != len(results) or len(receipt['windows']) != len(results)):
        raise ValueError('Evaluation review must cover the frozen complete selection.')
    inventory = {str(p.relative_to(repo)):sha256_file(p) for folder,_ in runs for p in folder.rglob('*') if p.is_file()}
    if inventory != receipt['original_file_sha256']:
        raise ValueError('Original evaluation artifacts changed after source review.')
    records, excluded, total = [], [], 0
    manifest_hash = sha256_file(path)
    for n, ((item, result), row, audit) in enumerate(zip(results,review['windows'],receipt['windows']),1):
        name = f'{n:02d}'
        folder, summary, original = result['entry']
        raw_path = folder/original['folder']/f"raw_extraction_{original['attempts'][-1]['attempt']}.json"
        if (any(r.get('folder') != name or r.get('scope_id') != item['chunk'].chunk_id for r in [row,audit])
                or audit['original_run'] != str(folder.relative_to(repo)) or audit['original_folder'] != original['folder']
                or audit['original_status'] != original['status'] or audit['transformations'] != result['changes']
                or audit['raw_file_sha256'] != sha256_file(raw_path)
                or row['raw_file_sha256'] != audit['raw_file_sha256']
                or set(row['file_sha256']) != FILES or row['file_sha256'] != audit['artifact_sha256']):
            raise ValueError('Reviewed evaluation source identity or derivation changed.')
        values = {'derived_selection.json':json.loads(result['derived']),
                  'candidate_extraction.json':result['batch'].model_dump(mode='json'),
                  'identity_resolution.json':result['resolution'], 'quote_alignment.json':result['aligned']}
        for filename, value in values.items():
            p = artifacts/name/filename
            if sha256_file(p) != row['file_sha256'][filename] or read(p) != value:
                raise ValueError('Reviewed evaluation candidate artifact changed.')
        selected = check_decisions(row['decisions'],result['batch'])
        total += len(result['batch'].relations)
        excluded += [dict(d,folder=name,scope_id=item['chunk'].chunk_id) for d in row['decisions'] if d['disposition']!='supported']
        if not selected:
            continue
        batch = supported_batch(result['batch'],selected)
        if (any(r.predicate.value not in {'USES','USES_TECHNIQUE'} for r in batch.relations)
                or any(e.type.value not in {'ThreatGroup','Software','Technique'} for e in batch.entities)):
            raise ValueError('Evaluation observed-use import requires actor/software/technique predicates.')
        record = prepare_records(item,batch,catalog,summary,original,result['raw'],folder,
                                 'AI_assisted_frozen_evaluation_source_review_with_explicit_duplicate_derivation')
        add_review_provenance(record,result['aligned'],selected,row,manifest_hash)
        for assertion in record['assertions']:
            assertion.update(scope_assignment='evaluation', evaluation_plan_fingerprint=plan['fingerprint'],
                             source_generation_status=original['status'],source_generation_raw_file_sha256=audit['raw_file_sha256'],
                             offline_validation_receipt_sha256=review['artifact_receipt_sha256'],
                             offline_selector_normalization_json=json.dumps(result['changes'],ensure_ascii=False))
        records.append(record)
    count = sum(len(r['assertions']) for r in records)
    if (not count or count != review['supported_count'] or total != review['candidate_count']
            or len(excluded) != review['excluded_count']):
        raise ValueError('Held-out source-review selection counts changed.')
    return {'items':records,'excluded_candidates':excluded,'prepared_at':datetime.now(timezone.utc).isoformat(),
            'attack_release':'17.1','attack_snapshot_hash':attack_hash,'model_digest':runs[0][1]['model_digest'],
            'human_review_status':'pending','scope_assignment':'evaluation','evaluation_plan_fingerprint':plan['fingerprint'],
            'review_manifest':str(path),'review_manifest_sha256':manifest_hash,
            'offline_validation_receipt_sha256':review['artifact_receipt_sha256'],
            'extraction_run':str(repo/receipt['latest_run']),'configuration_hash':plan['configuration_hash']}
