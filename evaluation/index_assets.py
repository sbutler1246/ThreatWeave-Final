"""Offline checks for the pinned evaluation text build and its exact source records."""
import importlib.metadata
import json
import math
import re
from pathlib import Path

from evaluation.text_sources import VERSION
from extraction.llama_tokenizer import sha256_file
from retrieval.development_text import sha

TEXT_RUN = '20261016T043755Z-ddd54a27'
SCOPE_RUN = '20261016T043617Z-a24728fc'
GRAPH_RUN = '20261016T044432Z-6c86d43a'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def checked_text_index(repo,evaluation_scope=None):
    repo = Path(repo).resolve()
    receipt_path = repo/'work/evaluation_text_index_runs'/TEXT_RUN/'index_receipt.json'
    receipt = read(receipt_path)
    snapshot = repo/'work/evaluation_scope_runs'/SCOPE_RUN
    scope = read(snapshot/'scope_receipt.json')
    if (receipt.get('status')!='ready' or receipt.get('purpose')!='evaluation_text_index'
            or receipt.get('evaluation_scope')!=scope['evaluation_scope']
            or evaluation_scope is not None and receipt['evaluation_scope']!=evaluation_scope
            or receipt.get('development_scope')!=scope['development_scope']
            or receipt.get('fingerprint')!=scope['text_fingerprint']
            or not re.fullmatch(r'[a-f0-9]{64}',receipt['fingerprint'])
            or receipt.get('chunk_count')!=scope['retrieval_chunk_count']
            or receipt.get('verified_chunk_count')!=scope['retrieval_chunk_count']
            or receipt.get('cisa_scope_count')!=scope['cisa_scope_count']
            or receipt.get('attack_reference_count')!=scope['attack_reference_count']):
        raise ValueError('A ready matching shared evaluation text index is required.')
    folder = repo/'work/evaluation_text_index'/receipt['fingerprint']
    records_path = folder/'records.json'
    store = repo/'work/chroma'
    if (Path(receipt['records_path']).resolve()!=records_path.resolve()
            or Path(receipt['chroma_path']).resolve()!=store.resolve()
            or not (store/'chroma.sqlite3').is_file()
            or receipt['collection_name']!='threatweave_text_eval_'+receipt['fingerprint'][:16]
            or sha(records_path.read_text(encoding='utf-8'))!=receipt['records_sha256']
            or sha256_file(snapshot/'records.json')!=scope['files_sha256']['records.json']):
        raise ValueError('Evaluation text asset paths, collection or saved records changed.')
    records = read(records_path)
    if records!=read(snapshot/'records.json'):
        raise ValueError('Evaluation text records differ from their prepared source snapshot.')
    config = read(repo/'config.json')
    if any(receipt[key]!=config[key] for key in ['chunking','corpus_version']) or receipt['embedding']!=config['text_embedding']:
        raise ValueError('Evaluation text model or chunking settings changed.')
    payload = {'version':VERSION,'corpus_version':receipt['corpus_version'],
               'evaluation_scope':receipt['evaluation_scope'],'development_scope':receipt['development_scope'],
               'embedding':receipt['embedding'],'chunking':receipt['chunking'],'records':records}
    if sha(json.dumps(payload,sort_keys=True,ensure_ascii=False))!=receipt['fingerprint']:
        raise ValueError('Evaluation text fingerprint differs from its exact source payload.')
    fields = ['fingerprint','collection_name','chroma_path','records_path','records_sha256','embedding',
              'chunking','corpus_version','packages','development_scope','evaluation_scope']
    manifest = read(folder/'manifest.json')
    if any(manifest.get(key)!=receipt[key] for key in fields):
        raise ValueError('Evaluation text manifest and completed receipt differ.')
    for package,version in receipt['packages'].items():
        if importlib.metadata.version(package)!=version:
            raise ValueError('Evaluation text runtime package changed: '+package)
    by_id = {r['chunk']['chunk_id']:r for r in records}
    if len(by_id)!=len(records):
        raise ValueError('Duplicate evaluation retrieval chunk IDs.')
    hits = []
    from graph_qa import DEMO_QUESTIONS
    if [q['question'] for q in receipt['smoke_queries']]!=list(DEMO_QUESTIONS):
        raise ValueError('Saved text smoke questions differ from the frozen development checks.')
    for question in receipt['smoke_queries']:
        ranks = question['hits']
        if (len(ranks)!=min(config['retrieval']['text_candidates'],len(records))
                or len({h['record']['chunk']['chunk_id'] for h in ranks})!=len(ranks)):
            raise ValueError('Saved text smoke result count differs.')
        previous = -float('inf')
        for rank,hit in enumerate(ranks,1):
            identifier = hit['record']['chunk']['chunk_id']
            if hit['rank']!=rank or identifier not in by_id or hit['record']!=by_id[identifier]:
                raise ValueError('Saved text smoke passage differs from its source record.')
            distance = float(hit['cosine_distance'])
            if not math.isfinite(distance) or not -0.0001<=distance<=2.0001 or distance<previous:
                raise ValueError('Saved text smoke cosine distances are invalid or unordered.')
            previous = distance
            hits.append(hit)
    return receipt,manifest,records,hits


def checked_graph_index(repo,evaluation_scope=None):
    """Audit saved vectors and build receipts; never query a live database or fit."""
    import hashlib
    import platform
    import numpy as np
    import networkx as nx
    from graph.development_projection import digest,undirected_graph
    from graph.node2vec_training import training_parameters,training_environment
    from retrieval.graph_vectors import IDENTITY_FIELDS
    repo = Path(repo).resolve()
    text,_,_,_ = checked_text_index(repo,evaluation_scope)
    config = read(repo/'config.json')
    receipt = read(repo/'work/evaluation_graph_index_runs'/GRAPH_RUN/'index_receipt.json')
    pointer = read(repo/'work/evaluation_graph_index/current.json')
    fingerprint = pointer['index_fingerprint']
    if not re.fullmatch(r'[a-f0-9]{64}',fingerprint):
        raise ValueError('Invalid evaluation graph fingerprint.')
    folder = repo/'work/evaluation_graph_index'/fingerprint
    if Path(pointer['manifest_path']).resolve()!=folder/'manifest.json':
        raise ValueError('Evaluation graph pointer escapes its expected location.')
    manifest = read(folder/'manifest.json')
    fields = IDENTITY_FIELDS+['evaluation_scope','text_index_fingerprint']
    if (digest({k:manifest[k] for k in fields})!=fingerprint
            or manifest.get('index_fingerprint')!=fingerprint
            or manifest.get('version')!='evaluation-graph-vector-index-v1'
            or manifest.get('evaluation_scope')!=text['evaluation_scope']
            or manifest.get('text_index_fingerprint')!=text['fingerprint']
            or manifest.get('live_projection_verified') is not True
            or manifest.get('dimension')!=128 or manifest.get('normalized') is not True
            or manifest.get('node2vec_parameters')!=training_parameters(config)
            or manifest.get('python')!=platform.python_version()
            or manifest.get('training_source_sha256')!=sha256_file(repo/'graph/node2vec_training.py')
            or manifest.get('corpus_version')!=config['corpus_version']
            or manifest.get('attack_release')!=config['attack_release']):
        raise ValueError('Evaluation graph identity/configuration differs from the shared text scope.')
    environment = training_environment(config['node2vec'])
    if any(environment[k]!=v for k,v in manifest['training_environment'].items()):
        raise ValueError('Graph training environment differs from the frozen settings.')
    for package,version in manifest['packages'].items():
        if importlib.metadata.version(package)!=version:
            raise ValueError('Evaluation graph runtime package changed: '+package)
    for field,name in [('projection_path','projection.json'),('vectors_path','vectors.npz')]:
        path = folder/name
        if Path(manifest[field]).resolve()!=path or sha256_file(path)!=manifest[field.replace('_path','_file_sha256')]:
            raise ValueError('Evaluation graph asset path or file hash changed.')
    projection = read(folder/'projection.json')
    if digest(projection)!=manifest['projection_sha256'] or projection['scope']!=text['evaluation_scope']['name']:
        raise ValueError('Evaluation graph projection identity changed.')
    with np.load(folder/'vectors.npz',allow_pickle=False) as arrays:
        ids = arrays['node_ids'].tolist();raw=arrays['raw_vectors'].copy();vectors=arrays['normalized_vectors'].copy()
    if (ids!=manifest['node_ids'] or ids!=sorted(n['canonical_id'] for n in projection['nodes'])
            or len(set(ids))!=len(ids) or raw.shape!=(len(ids),128) or vectors.shape!=raw.shape
            or not np.isfinite(raw).all() or not np.isfinite(vectors).all()
            or (np.linalg.norm(raw,axis=1)<=0).any()
            or not np.allclose(np.linalg.norm(vectors,axis=1),1,atol=1e-5)
            or not np.allclose(vectors,raw/np.linalg.norm(raw,axis=1,keepdims=True),atol=1e-6)
            or hashlib.sha256(raw.tobytes()).hexdigest()!=manifest['raw_vector_sha256']
            or hashlib.sha256(vectors.tobytes()).hexdigest()!=manifest['normalized_vector_sha256']):
        raise ValueError('Evaluation graph vector values or node bindings changed.')
    graph = undirected_graph(projection)
    components = {n:'component:'+digest(sorted(c))[:16] for c in nx.connected_components(graph) for n in c}
    if components!=manifest['component_by_node']:
        raise ValueError('Evaluation graph component assignments changed.')
    expected = {'status':'ready','purpose':'live_evaluation_node2vec_index','index_fingerprint':fingerprint,
                'collection_name':'threatweave_graph_eval_'+fingerprint[:16], 'manifest_path':str(folder/'manifest.json'),
                'evaluation_scope':text['evaluation_scope'],'text_index_fingerprint':text['fingerprint'],
                'projection_sha256':manifest['projection_sha256'],'node_count':len(ids),
                'directed_fact_count':len(projection['edges']),'undirected_edge_count':graph.number_of_edges(),
                'component_sizes':sorted((len(c) for c in nx.connected_components(graph)),reverse=True),
                'exact_vector_lookup_count':len(ids),'dimension':128,'normalized':True,
                'walk_count':len(ids)*config['node2vec']['num_walks']}
    if any(receipt.get(k)!=v for k,v in expected.items()):
        raise ValueError('Evaluation graph ready receipt differs from its saved assets.')
    for key in ['collection_name','packages','python','training_environment','node2vec_parameters',
                'raw_vector_sha256','normalized_vector_sha256','walk_count','walk_sha256']:
        if receipt[key]!=manifest[key]:raise ValueError('Graph build/manifest metadata differ.')
    lookups = receipt['smoke_lookups']
    if (sorted(r['canonical_id'] for r in lookups)!=ids
            or any(r['top_match']!=r['canonical_id'] or not math.isfinite(r['cosine_distance'])
                   or abs(r['cosine_distance'])>1e-4 for r in lookups)):
        raise ValueError('Saved exact-vector lookup results are inconsistent.')
    if Path(manifest['chroma_path']).resolve()!=repo/'work/chroma':
        raise ValueError('Evaluation graph store path changed.')
    return receipt,manifest,projection,ids,raw,vectors
