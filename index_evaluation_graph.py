"""Fit and store 128-D Node2Vec vectors from accepted live shared evaluation graph facts."""
import argparse
import getpass
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from graph.development_projection import digest, preview_projection, read_projection, undirected_graph
from evaluation.corpus_scope import EvaluationGraphRetriever
from evaluation.index_assets import checked_text_index
from graph.node2vec_training import fit_projection, training_environment, training_parameters


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--preview', action='store_true', help='Validate source-derived projection fixtures; do not connect or fit/publish an index.')
    args = parser.parse_args()
    repo = args.repo.resolve()
    retriever = EvaluationGraphRetriever(repo)
    text_receipt, _, _, _ = checked_text_index(repo,retriever.config['evaluation_scope'])
    params = training_parameters(retriever.config)
    import networkx as nx
    if args.preview:
        projection, _, _, _ = preview_projection(retriever)
        graph = undirected_graph(projection)
        print(f'Shared evaluation source-fixture projection: {graph.number_of_nodes()} domain nodes; {len(projection["edges"])} directed facts; {graph.number_of_edges()} undirected edges.')
        print('Connected-component sizes: '+str(sorted((len(c) for c in nx.connected_components(graph)), reverse=True)))
        print('PREVIEW PASSED: Source/identity projection checks passed; live graph presence and production fitting remain untested.')
        return 0
    environment = training_environment(params)
    fixed = ['PYTHONHASHSEED', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS']
    if any(os.environ.get(key) != environment[key] for key in fixed):
        return subprocess.run([sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]],
                              cwd=repo, env=environment).returncode
    import numpy as np
    import chromadb
    from chromadb.config import Settings
    from neo4j import GraphDatabase
    os.environ['ANONYMIZED_TELEMETRY'] = 'False'
    packages = {p: importlib.metadata.version(p) for p in ['node2vec', 'gensim', 'networkx', 'numpy', 'scipy', 'chromadb']}
    required = {'node2vec': '0.5.0', 'gensim': '4.4.0', 'networkx': '3.7',
                'numpy': '1.26.4', 'scipy': '1.17.1', 'chromadb': '1.0.15'}
    if packages != required:
        raise ValueError('Graph-embedding package versions differ from the checked setup; run setup_node2vec.py.')
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    output = repo/'work/evaluation_graph_index_runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    summary = {'purpose': 'live_evaluation_node2vec_index', 'status': 'started', 'packages': packages,
        'python': platform.python_version(), 'training_environment': {key: os.environ[key] for key in fixed},
        'node2vec_parameters': params, 'corpus_version': retriever.config['corpus_version'],
        'attack_release': retriever.config['attack_release'], 'hash_seed': os.environ['PYTHONHASHSEED'],
        'hardware': {'platform': platform.platform(), 'machine': platform.machine(),
                     'processor': platform.processor(), 'logical_cpu_count': os.cpu_count()},
        'scope': retriever.scope_name, 'development_scope':retriever.config['development_scope'],
        'evaluation_scope':retriever.config['evaluation_scope'], 'text_index_fingerprint':text_receipt['fingerprint']}
    save(output/'index_receipt.json', summary)
    try:
        with GraphDatabase.driver(uri, auth=(user, password), connection_timeout=10,
                connection_acquisition_timeout=15, max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            projection, projection_hash = read_projection(driver, retriever, database)
            graph = undirected_graph(projection)
            summary.update(projection_sha256=projection_hash, node_count=graph.number_of_nodes(),
                directed_fact_count=len(projection['edges']), undirected_edge_count=graph.number_of_edges(),
                component_sizes=sorted((len(c) for c in nx.connected_components(graph)), reverse=True))
            save(output/'projection.json', projection)
            print(f'VERIFIED: {summary["node_count"]} live domain nodes; {summary["directed_fact_count"]} accepted source-supported facts.', flush=True)
            print('Fitting 128-dimensional Node2Vec vectors with the frozen parameters...', flush=True)
            fitted = fit_projection(graph, params)
            raw, vectors, ids = fitted['vectors'], fitted['normalized_vectors'], fitted['node_ids']
            if not np.allclose(np.linalg.norm(vectors, axis=1), 1, atol=1e-5):
                raise ValueError('Fitted vectors are not normalized.')
            raw_hash = hashlib.sha256(raw.tobytes()).hexdigest()
            normalized_hash = hashlib.sha256(vectors.tobytes()).hexdigest()
            components = {node: 'component:'+digest(sorted(component))[:16]
                          for component in nx.connected_components(graph) for node in component}
            identity = {'version': 'evaluation-graph-vector-index-v1', 'projection_sha256': projection_hash,
                'evaluation_scope':retriever.config['evaluation_scope'], 'text_index_fingerprint':text_receipt['fingerprint'],
                'node2vec_parameters': params, 'word2vec_parameters': fitted['word2vec_parameters'],
                'packages': packages, 'python': platform.python_version(),
                'training_source_sha256': hashlib.sha256((repo/'graph/node2vec_training.py').read_bytes()).hexdigest(),
                'training_environment': {key: os.environ[key] for key in fixed},
                'raw_vector_sha256': raw_hash, 'normalized_vector_sha256': normalized_hash,
                'component_by_node': components}
            fingerprint = digest(identity)
            name = 'threatweave_graph_eval_'+fingerprint[:16]
            expected_metadata = {'index_fingerprint': fingerprint, 'projection_sha256': projection_hash,
                                 'dimension': 128, 'hnsw:space': 'cosine', 'corpus_version': retriever.config['corpus_version']}
            store = repo/'work/chroma'
            client = chromadb.PersistentClient(path=str(store), settings=Settings(anonymized_telemetry=False))
            collection = client.get_or_create_collection(name, embedding_function=None, metadata=expected_metadata)
            if any(collection.metadata.get(k) != v for k, v in expected_metadata.items()):
                raise ValueError('Existing graph collection configuration conflicts with the fit.')
            entities = {n['canonical_id']: n for n in projection['nodes']}
            metas = [{'canonical_id': identifier, 'name': entities[identifier]['name'],
                      'entity_type': entities[identifier]['type'], 'projection_sha256': projection_hash,
                      'index_fingerprint': fingerprint, 'component_id': components[identifier]} for identifier in ids]
            by_id = {identifier: (entities[identifier]['name'], meta, vector)
                     for identifier, meta, vector in zip(ids, metas, vectors)}
            previous = collection.get(include=['documents', 'metadatas', 'embeddings'])
            if (len(set(previous['ids'])) != len(previous['ids']) or any(
                    len(previous[k]) != len(previous['ids']) for k in ['documents', 'metadatas', 'embeddings'])):
                raise ValueError('Existing graph collection returned inconsistent result columns.')
            for identifier, doc, meta, vector in zip(previous['ids'], previous['documents'], previous['metadatas'], previous['embeddings']):
                if identifier not in by_id or doc != by_id[identifier][0] or meta != by_id[identifier][1] or not np.allclose(vector, by_id[identifier][2], atol=1e-6):
                    raise ValueError('Existing graph-vector records conflict with their manifest.')
            collection.upsert(ids=ids, documents=[entities[i]['name'] for i in ids],
                              metadatas=metas, embeddings=vectors.tolist())
            stored = collection.get(include=['documents', 'metadatas', 'embeddings'])
            if (collection.count() != len(ids) or set(stored['ids']) != set(ids)
                    or any(len(stored[k]) != len(ids) for k in ['ids', 'documents', 'metadatas', 'embeddings'])):
                raise ValueError('Stored graph node-ID map differs from the projection.')
            for identifier, doc, meta, vector in zip(stored['ids'], stored['documents'], stored['metadatas'], stored['embeddings']):
                if doc != by_id[identifier][0] or meta != by_id[identifier][1] or not np.allclose(vector, by_id[identifier][2], atol=1e-6):
                    raise ValueError('Stored graph-vector binding failed verification.')
            # The fit and persisted collection must still refer to the live graph.
            _, current_hash = read_projection(driver, retriever, database)
            if current_hash != projection_hash:
                raise ValueError('Accepted evaluation graph changed during fitting; no ready manifest published.')
            folder = repo/'work/evaluation_graph_index'/fingerprint
            folder.mkdir(parents=True, exist_ok=True)
            save(folder/'projection.json', projection)
            np.savez_compressed(folder/'vectors.npz', node_ids=np.asarray(ids),
                                raw_vectors=raw, normalized_vectors=vectors)
            smoke = []
            for identifier in ids:
                result = collection.query(query_embeddings=[by_id[identifier][2].tolist()],
                                          n_results=1, include=['distances'])
                if result['ids'] != [[identifier]] or abs(result['distances'][0][0]) > 1e-4:
                    raise ValueError('Exact graph-vector lookup failed for '+identifier)
                smoke.append({'canonical_id': identifier, 'top_match': identifier,
                              'cosine_distance': result['distances'][0][0]})
            manifest = dict(identity, index_fingerprint=fingerprint, collection_name=name,
                chroma_path=str(store), projection_path=str(folder/'projection.json'),
                vectors_path=str(folder/'vectors.npz'),
                projection_file_sha256=hashlib.sha256((folder/'projection.json').read_bytes()).hexdigest(),
                vectors_file_sha256=hashlib.sha256((folder/'vectors.npz').read_bytes()).hexdigest(),
                node_ids=ids, dimension=128, normalized=True, corpus_version=retriever.config['corpus_version'],
                attack_release=retriever.config['attack_release'], walk_sha256=fitted['walk_sha256'],
                walk_count=fitted['walk_count'], hardware=summary['hardware'],
                built_at=datetime.now(timezone.utc).isoformat(), live_projection_verified=True)
            save(folder/'manifest.json', manifest)
            # This pointer is published only after all validations pass.
            save(repo/'work/evaluation_graph_index/current.json', {'index_fingerprint': fingerprint,
                                                       'manifest_path': str(folder/'manifest.json')})
            summary.update(status='ready', index_fingerprint=fingerprint, collection_name=name,
                manifest_path=str(folder/'manifest.json'), dimension=128,
                normalized=True, walk_count=fitted['walk_count'], walk_sha256=fitted['walk_sha256'],
                raw_vector_sha256=raw_hash, normalized_vector_sha256=normalized_hash,
                exact_vector_lookup_count=len(smoke), smoke_lookups=smoke,
                note='Scoped live evaluation graph index; final QA execution and scoring remain pending.')
            print(f'VERIFIED: {collection.count()} normalized 128-dimensional graph vectors and exact-vector lookups.', flush=True)
        code = 0
    except Exception as exc:
        message = str(exc).replace(password, '[hidden]') if password else str(exc)
        summary.update(status='failed', error=f'{type(exc).__name__}: {message}')
        print('GRAPH INDEX FAILED: '+summary['error'], flush=True)
        code = 1
    finally:
        password = None
    summary['finished_at'] = datetime.now(timezone.utc).isoformat()
    save(output/'index_receipt.json', summary)
    lines = ['# Shared evaluation graph-vector index run', '', 'Status: '+summary['status'], '',
        f'Scoped to {len(retriever.profiles)} shared evaluation CISA passages and {len(retriever.references)} direct ATT&CK references; no benchmark labels used.',
        'Neo4j was read only. Node2Vec uses an undirected domain projection; original directed typed facts remain in provenance.', '',
        'Projection SHA-256: `'+str(summary.get('projection_sha256', 'unavailable'))+'`',
        f'Nodes: {summary.get("node_count", "unavailable")}; directed facts: {summary.get("directed_fact_count", "unavailable")}; undirected edges: {summary.get("undirected_edge_count", "unavailable")}.',
        'Connected-component sizes: '+str(summary.get('component_sizes', 'unavailable')),
        'Component counts were calculated with NetworkX for this saved projection, not a new Neo4j GDS measurement.', '',
        'Graph embedding dimension: 128. Vector similarity is not evidence of an incident fact.',
        'Full-hybrid QA and final evaluation remain pending.', '']
    if summary.get('manifest_path'):
        lines.extend(['Index manifest: `'+summary['manifest_path']+'`', ''])
    if summary.get('error'):
        lines.extend(['Error: '+summary['error'], ''])
    review = repo/'docs'/('ThreatWeave_evaluation_graph_index_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'Saved records: {output}\nSaved review document: {review}', flush=True)
    if code == 0:
        print('READY: Live shared evaluation graph projected, Node2Vec fitted and separate graph-vector index verified.', flush=True)
    return code


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('\nGraph indexing cancelled; existing records remain saved.')
        sys.exit(2)
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}')
        sys.exit(1)
