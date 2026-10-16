"""Source-only preparation for the three remaining non-held-out development reports."""
import hashlib
import json
import re
from pathlib import Path

from extraction.corpus_batch import prepare as prepare_previous
from extraction.corpus_chunking import PILOT_DOCUMENTS, digest, load_verified_tokenizer, split_section, technical_bounds
from extraction.corpus_pilot import configuration
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import make_prompt
from schemas import Chunk, Document

DOCUMENTS = ('AA24-038A', 'AA23-144A', 'AA22-321A')
PREPARED_KIND = 'corpus_extension_chunks'
OUTPUT_KIND = 'corpus_extension_extraction'


def selection(manifest, split):
    identifiers = [d['doc_id'] for d in manifest['documents']]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError('Duplicate source document IDs in the frozen manifest.')
    blocked = {scope.split(':')[0] for scope in split['held_out_evidence_scopes']}
    remaining = set(identifiers) - blocked - set(PILOT_DOCUMENTS)
    if blocked.intersection(DOCUMENTS) or remaining != set(DOCUMENTS):
        raise ValueError('Remaining development report selection changed or includes held-out evidence.')
    return DOCUMENTS, sorted(blocked)


def prepare(repo):
    repo = Path(repo).resolve()
    _, config, catalog, attack_hash, old_identity, _, old_plan = prepare_previous(repo)
    tokenizer, tokenizer_identity = load_verified_tokenizer(repo)
    manifest_path = repo/'benchmarks/corpus_manifest.json'
    split_path = repo/'benchmarks/split_manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    split = json.loads(split_path.read_text(encoding='utf-8'))
    selected, blocked = selection(manifest, split)
    sources = {d['doc_id']:d for d in manifest['documents']}
    params = dict(old_identity['parameters'])
    items, records, documents = [], [], []
    for doc_id in selected:
        source = sources[doc_id]
        text_path, raw_path = [(repo/source[k]).resolve() for k in ['text_file','raw_file']]
        if not all(path.is_relative_to(repo) for path in [text_path,raw_path]):
            raise ValueError('Frozen source path escapes the workspace.')
        text = text_path.read_text(encoding='utf-8')
        if (hashlib.sha256(text.encode('utf-8')).hexdigest() != source['normalized_sha256']
                or sha256_file(raw_path) != source['raw_sha256']):
            raise ValueError('Frozen extension source checksum changed: '+doc_id)
        doc = Document(doc_id=doc_id, title=source['title'], source_url=source['source_url'],
                       text=text, content_hash=source['normalized_sha256'])
        start,end,heading = technical_bounds(text)
        windows = split_section(doc,tokenizer,start,end,heading,**params)
        for record in windows:
            record.update(doc_id=doc_id, source_url=str(doc.source_url), source_hash=doc.content_hash)
            chunk = Chunk.model_validate(record['chunk'])
            items.append({'document':doc, 'chunk':chunk, 'spec':{'kind':'prose'}, 'preparation':record})
        records.extend(windows)
        documents.append({'doc_id':doc_id, 'title':doc.title, 'source_url':str(doc.source_url),
                          'source_hash':doc.content_hash, 'raw_sha256':source['raw_sha256'],
                          'technical_start':start, 'technical_end':end, 'chunk_count':len(windows)})
    identity = {'purpose':'remaining_three_development_report_preparation',
                'corpus_version':config['corpus_version'], 'tokenizer':tokenizer_identity,
                'parameters':params, 'documents':documents, 'records_sha256':digest(records),
                'manifest_sha256':sha256_file(manifest_path), 'split_manifest_sha256':sha256_file(split_path),
                'excluded_held_out_reports':blocked, 'excluded_prepared_reports':list(PILOT_DOCUMENTS),
                'previous_prepared_fingerprint':old_identity['fingerprint'],
                'selection':'All technical-section windows in the three remaining non-held-out reports; no labels or answers.'}
    identity['fingerprint'] = digest(identity)
    settings = configuration(config,identity,attack_hash)
    scopes = [i['chunk'].chunk_id for i in items]
    prior_scopes = old_plan['excluded_pilot_scope_ids'] + old_plan['scope_ids']
    if len(set(scopes)) != len(scopes) or set(scopes).intersection(prior_scopes):
        raise ValueError('Extension repeats a source window or an existing prepared scope.')
    plan = {'version':1, 'purpose':'remaining_three_development_report_extraction',
            'prepared_fingerprint':identity['fingerprint'], 'configuration_hash':digest(settings),
            'scope_ids':scopes, 'excluded_prior_scope_ids':prior_scopes,
            'document_ids':list(selected), 'excluded_held_out_reports':blocked,
            'manifest_sha256':identity['manifest_sha256'], 'split_manifest_sha256':identity['split_manifest_sha256'],
            'selection':identity['selection']}
    plan['fingerprint'] = digest(plan)
    return items,config,catalog,attack_hash,identity,plan


def preflight(items,config,catalog,tokenizer):
    checks = []
    for item in items:
        system,prompt,schema,index = make_prompt(item,catalog)
        estimated = len(tokenizer.encode(system+'\n'+prompt+'\n'+json.dumps(schema),add_special_tokens=False).ids)
        total = estimated+config['llm']['num_predict']+256
        checks.append({'scope_id':item['chunk'].chunk_id, 'doc_id':item['document'].doc_id,
                       'source_tokens':item['preparation']['source_tokens'],
                       'mention_count':len(index['mentions']), 'evidence_pattern_count':len(index['evidence_patterns']),
                       'estimated_prompt_schema_tokens':estimated, 'reserved_chat_tokens':256,
                       'output_tokens':config['llm']['num_predict'], 'context_limit':config['llm']['num_ctx'],
                       'estimated_total_tokens':total, 'within_budget':total<=config['llm']['num_ctx'],
                       'prompt_hash':digest({'system':system,'prompt':prompt,'schema':schema})})
    return checks


def read_prepared(repo):
    repo = Path(repo).resolve()
    pointer = json.loads((repo/'work'/PREPARED_KIND/'current.json').read_text(encoding='utf-8'))
    if not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}',pointer['run']):
        raise ValueError('Invalid prepared extension pointer.')
    root = (repo/'work'/PREPARED_KIND).resolve()
    folder = (root/pointer['run']).resolve()
    if folder.parent != root:
        raise ValueError('Prepared extension path escapes its workspace folder.')
    items,config,catalog,attack_hash,identity,plan = prepare(repo)
    summary = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
    checks = preflight(items,config,catalog,load_verified_tokenizer(repo)[0])
    if (pointer.get('fingerprint') != identity['fingerprint']
            or summary.get('status') != 'ready_for_operator_extraction'
            or summary.get('identity') != identity or summary.get('plan') != plan
            or summary.get('model_calls') is not False or summary.get('graph_writes') is not False
            or json.loads((folder/'chunks.json').read_text(encoding='utf-8')) != [i['preparation'] for i in items]
            or json.loads((folder/'preflight.json').read_text(encoding='utf-8')) != checks
            or any(not row['within_budget'] for row in checks)):
        raise ValueError('Prepared extension source, plan, settings or prompt preflight changed.')
    return items,config,catalog,attack_hash,identity,folder,plan
