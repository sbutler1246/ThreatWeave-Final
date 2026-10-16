"""Frozen source-only preparation for seven held-out reports; no benchmark answers."""
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
from extraction.llama_tokenizer import MODEL_DIGEST
from extraction.corpus_extension import DOCUMENTS as DEVELOPMENT_EXTENSION_DOCUMENTS

DOCUMENTS = ('AA23-165A', 'AA23-061A', 'AA24-131A', 'AA24-109A', 'AA25-071A', 'AA23-352A', 'AA23-075A')
PREPARED_KIND = 'evaluation_corpus_chunks'
OUTPUT_KIND = 'evaluation_corpus_extraction'


def selection(manifest, split):
    identifiers = [d['doc_id'] for d in manifest['documents']]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError('Duplicate source document IDs in the frozen manifest.')
    if set(identifiers) != set(DOCUMENTS)|set(PILOT_DOCUMENTS)|set(DEVELOPMENT_EXTENSION_DOCUMENTS):
        raise ValueError('The frozen fifteen-report source universe changed.')
    blocked = {scope.split(':')[0] for scope in split['held_out_evidence_scopes']}
    remaining = set(identifiers).intersection(blocked)
    if remaining != set(DOCUMENTS) or not set(DOCUMENTS).issubset(blocked):
        raise ValueError('Frozen held-out report selection changed.')
    return DOCUMENTS, sorted(set(identifiers)-set(DOCUMENTS))


def frozen_protocol(repo, config):
    """Bind current development assets and predeclare evaluation rules without reading labels."""
    text_run = repo/'work/text_index_runs/20261016T002500Z-41e31bf5/index_receipt.json'
    graph_run = repo/'work/graph_index_runs/20261016T003953Z-4ad94e21/index_receipt.json'
    text = json.loads(text_run.read_text(encoding='utf-8'))
    graph = json.loads(graph_run.read_text(encoding='utf-8'))
    pointer = json.loads((repo/'work/graph_index/current.json').read_text(encoding='utf-8'))
    if (text.get('status')!='ready' or graph.get('status')!='ready'
            or text['development_scope']!=graph['development_scope']
            or pointer.get('index_fingerprint')!=graph['index_fingerprint']):
        raise ValueError('A matching verified development snapshot is required before held-out extraction.')
    graph_folder = repo/'work/graph_index'/graph['index_fingerprint']
    if Path(pointer['manifest_path']).resolve() != (graph_folder/'manifest.json').resolve():
        raise ValueError('Development graph pointer escapes its frozen workspace path.')
    projection = json.loads((graph_folder/'projection.json').read_text(encoding='utf-8'))
    if digest(projection) != graph['projection_sha256']:
        raise ValueError('Saved development projection changed before the freeze.')
    overlap = sorted(set(DOCUMENTS).intersection(s['doc_id'] for s in projection['cisa_sources']))
    split = json.loads((repo/'benchmarks/split_manifest.json').read_text(encoding='utf-8'))
    final_ids = split['final_evaluation_query_ids']
    if (len(final_ids)!=20 or len(set(final_ids))!=20 or config['evaluation']['repeats']!=3
            or split['final_evaluation_category_counts'] != config['evaluation']['qa_minimum_mix']):
        raise ValueError('Frozen final question/repeat assignment changed.')
    code = ['schemas.py','resolve.py','graph_qa.py','graph_pilot_qa.py','application_engine.py',
            'extraction/source_choices.py','extraction/development_batch.py','extraction/corpus_chunking.py',
            'extraction/corpus_pilot.py','graph/development_retrieval.py','graph/development_projection.py',
            'graph/node2vec_training.py','retrieval/development_text.py','retrieval/text_retrieval.py',
            'retrieval/combined_retrieval.py','retrieval/graph_vectors.py','retrieval/hybrid_retrieval.py',
            'evaluation/corpus_preparation.py','evaluation/corpus_runner.py',
            'prepare_evaluation_corpus.py','extract_evaluation_corpus.py']
    return {'version':1, 'stage':'source_processing_and_method_freeze; final_evaluation_indexes_not_built',
            'model_digest':MODEL_DIGEST, 'config_sha256':sha256_file(repo/'config.json'),
            'implementation_sha256':{name:sha256_file(repo/name) for name in code},
            'development_snapshot':{'scope':text['development_scope'], 'text_fingerprint':text['fingerprint'],
                                    'graph_fingerprint':graph['index_fingerprint'],
                                    'text_receipt_sha256':sha256_file(text_run),
                                    'graph_receipt_sha256':sha256_file(graph_run)},
            'reports_with_preexisting_bounded_development_evidence':overlap,
            'overlap_policy':'report overlap retained and disclosed; final/development question evidence assignments remain frozen and disjoint',
            'question_ids':final_ids, 'modes':['text_only','graph_only','hybrid_no_node2vec','hybrid'],
            'repeats':3, 'measured_answer_runs':240, 'warmup':'one per mode, excluded from measured runs',
            'randomization_seed':42, 'human_review_repeat':1, 'human_review_answer_count':80,
            'secondary_review':'five questions across four modes, or delayed 25 percent re-score',
            'packing_policy':'same conservative 3000 UTF-8 byte cap in every mode; below designed token ceiling',
            'mode_label_policy':'retain frozen MODE prompt field; mode differences are not purely retrieval effects',
            'isolation':'source text and split IDs only; no gold triples or reference answers in processing',
            'tuning_policy':'no prompt, selector, generation, retrieval or embedding tuning from held-out results',
            'extraction_scoring':'score frozen model predictions before review filtering and fusion; preserve rejected predictions, failures and empty windows',
            'graph_policy':'source-only reviewed Supported assertions, with excluded dispositions retained separately',
            'error_policy':'retain failures and undefined metrics; do not substitute modes or scores',
            'analysis':'paired question-level comparisons; 10000 question-cluster bootstrap samples; exploratory 95 percent intervals'}


def prepare(repo):
    repo = Path(repo).resolve()
    _, config, catalog, attack_hash, old_identity, _, old_plan = prepare_previous(repo)
    tokenizer, tokenizer_identity = load_verified_tokenizer(repo)
    manifest_path = repo/'benchmarks/corpus_manifest.json'
    split_path = repo/'benchmarks/split_manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    split = json.loads(split_path.read_text(encoding='utf-8'))
    selected, excluded = selection(manifest, split)
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
            raise ValueError('Frozen evaluation source checksum changed: '+doc_id)
        doc = Document(doc_id=doc_id, title=source['title'], source_url=source['source_url'],
                       text=text, content_hash=source['normalized_sha256'])
        start,end,heading = technical_bounds(text)
        windows = split_section(doc,tokenizer,start,end,heading,**params)
        for record in windows:
            record['chunk']['chunk_id'] = record['chunk']['chunk_id'].replace(':development:', ':evaluation:', 1)
            record.update(doc_id=doc_id, source_url=str(doc.source_url), source_hash=doc.content_hash)
            chunk = Chunk.model_validate(record['chunk'])
            items.append({'document':doc, 'chunk':chunk, 'spec':{'kind':'prose'}, 'preparation':record})
        records.extend(windows)
        documents.append({'doc_id':doc_id, 'title':doc.title, 'source_url':str(doc.source_url),
                          'source_hash':doc.content_hash, 'raw_sha256':source['raw_sha256'],
                          'technical_start':start, 'technical_end':end, 'chunk_count':len(windows)})
    identity = {'purpose':'held_out_seven_report_source_preparation',
                'corpus_version':config['corpus_version'], 'tokenizer':tokenizer_identity,
                'parameters':params, 'documents':documents, 'records_sha256':digest(records),
                'manifest_sha256':sha256_file(manifest_path), 'split_manifest_sha256':sha256_file(split_path),
                'excluded_development_reports':excluded, 'held_out_reports':list(selected),
                'previous_prepared_fingerprint':old_identity['fingerprint'],
                'selection':'All technical-section windows in seven held-out reports after settings freeze; no labels or reference answers.'}
    identity['protocol'] = frozen_protocol(repo,config)
    identity['fingerprint'] = digest(identity)
    settings = configuration(config,identity,attack_hash)
    scopes = [i['chunk'].chunk_id for i in items]
    prior_scopes = old_plan['excluded_pilot_scope_ids'] + old_plan['scope_ids']
    if len(set(scopes)) != len(scopes) or set(scopes).intersection(prior_scopes):
        raise ValueError('Evaluation repeats a source window or an existing prepared scope.')
    plan = {'version':1, 'purpose':'held_out_seven_report_source_extraction',
            'prepared_fingerprint':identity['fingerprint'], 'configuration_hash':digest(settings),
            'scope_ids':scopes, 'excluded_prior_scope_ids':prior_scopes,
            'document_ids':list(selected), 'excluded_development_reports':excluded,
            'manifest_sha256':identity['manifest_sha256'], 'split_manifest_sha256':identity['split_manifest_sha256'],
            'selection':identity['selection']}
    plan['protocol_sha256'] = digest(identity['protocol'])
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
        raise ValueError('Invalid prepared evaluation pointer.')
    root = (repo/'work'/PREPARED_KIND).resolve()
    folder = (root/pointer['run']).resolve()
    if folder.parent != root:
        raise ValueError('Prepared evaluation path escapes its workspace folder.')
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
        raise ValueError('Prepared evaluation source, plan, settings or prompt preflight changed.')
    return items,config,catalog,attack_hash,identity,folder,plan
