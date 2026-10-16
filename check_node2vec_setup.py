"""Verify synthetic 128-D graph vectors, repeatability, Chroma and text-index integrity."""
import argparse
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

from graph.node2vec_training import fit_projection, training_environment, training_parameters


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    repo = args.repo.resolve()
    config = json.loads((repo/'config.json').read_text(encoding='utf-8'))
    params = training_parameters(config)
    if os.environ.get('PYTHONHASHSEED') != str(params['seed']):
        # Python reads this setting at startup, not after importing NumPy/Gensim.
        return subprocess.run([sys.executable, str(Path(__file__).resolve()), '--repo', str(repo)],
                              cwd=repo, env=training_environment(params)).returncode
    folder = repo/'work/node2vec_setup'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    receipt = {'purpose': 'synthetic_node2vec_setup', 'status': 'failed',
               'python': platform.python_version(), 'node2vec_parameters': params,
               'hash_seed': os.environ['PYTHONHASHSEED'],
               'started_at': datetime.now(timezone.utc).isoformat()}
    os.environ['ANONYMIZED_TELEMETRY'] = 'False'
    try:
        if sys.version_info[:2] != (3, 12):
            raise ValueError('This setup targets Python 3.12.')
        expected = {'node2vec': '0.5.0', 'gensim': '4.4.0', 'networkx': '3.7',
                    'numpy': '1.26.4', 'scipy': '1.17.1', 'chromadb': '1.0.15'}
        versions = {name: importlib.metadata.version(name) for name in expected}
        receipt['packages'] = versions
        if versions != expected:
            raise ValueError('Installed graph-embedding package versions differ from the stage pins.')
        import numpy as np
        import networkx as nx
        import chromadb
        from chromadb.config import Settings
        from retrieval.text_retrieval import DevelopmentTextRetriever
        from schemas import QueryRequest
        from graph_qa import DEMO_QUESTIONS

        graph = nx.Graph()
        nodes = [f'probe:{i}' for i in range(8)]
        graph.add_nodes_from(nodes)
        graph.add_edges_from([(nodes[i], nodes[i+1]) for i in range(7)]+[(nodes[1], nodes[5])])
        print('Fitting a small synthetic graph twice with the configured parameters...', flush=True)
        first, second = fit_projection(graph, params), fit_projection(graph, params)
        if (first['walk_sha256'] != second['walk_sha256']
                or not np.array_equal(first['vectors'], second['vectors'])):
            raise ValueError('Repeated single-process fitting was not identical.')
        vectors = first['normalized_vectors']
        if not np.allclose(np.linalg.norm(vectors, axis=1), 1, atol=1e-5):
            raise ValueError('Graph vectors are not normalized.')
        np.savez_compressed(folder/'synthetic_vectors.npz', node_ids=np.asarray(first['node_ids']),
                            raw_vectors=first['vectors'], normalized_vectors=vectors)
        print('PASS: Repeatable single-process fit with normalized 128-dimensional vectors.', flush=True)
        client = chromadb.PersistentClient(path=str(folder/'chroma_probe'), settings=Settings(anonymized_telemetry=False))
        collection = client.create_collection('threatweave_graph_setup_probe', embedding_function=None,
                                               metadata={'hnsw:space': 'cosine', 'dimension': 128})
        collection.add(ids=first['node_ids'], embeddings=vectors.tolist(),
                       metadatas=[{'synthetic_probe': True} for _ in nodes])
        result = collection.query(query_embeddings=[vectors[0].tolist()], n_results=1, include=['distances'])
        if collection.count() != len(nodes) or result['ids'] != [[first['node_ids'][0]]]:
            raise ValueError('Synthetic graph-vector storage or exact-vector lookup failed.')
        if abs(result['distances'][0][0]) > 1e-4:
            raise ValueError('Graph-vector cosine lookup did not reproduce its exact match.')
        print('PASS: Separate local Chroma probe stores and retrieves 128-dimensional graph vectors.', flush=True)
        print('Rechecking the existing MiniLM text index after package installation...', flush=True)
        text = DevelopmentTextRetriever(repo)
        request = QueryRequest(question=DEMO_QUESTIONS[0], mode='text_only', corpus_version=config['corpus_version'])
        evidence = text.retrieve(request)
        if not evidence.passages:
            raise ValueError('The existing text index returned no evidence.')
        print('PASS: Existing text-index source/vector integrity and retrieval checks still pass.', flush=True)
        receipt.update(status='ready', synthetic_node_count=len(nodes), synthetic_edge_count=graph.number_of_edges(),
            dimension=128, repeated_fit_identical=True, repeatability_scope='two fits in the same fixed-seed process',
            walk_sha256=first['walk_sha256'], walk_count=first['walk_count'],
            vector_sha256=hashlib.sha256(first['vectors'].tobytes()).hexdigest(),
            word2vec_parameters=first['word2vec_parameters'], chroma_probe_count=collection.count(),
            text_index_regression_verified=True, text_index_fingerprint=text.manifest['fingerprint'],
            note='Synthetic setup only. Live Neo4j projection, production graph index and full-hybrid QA remain pending.')
        code = 0
    except Exception as exc:
        receipt['error'] = f'{type(exc).__name__}: {exc}'
        print('SETUP CHECK FAILED: '+receipt['error'], flush=True)
        code = 1
    receipt['finished_at'] = datetime.now(timezone.utc).isoformat()
    (folder/'setup_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    lines = ['# Node2Vec dependency setup check', '', 'Status: '+receipt['status'], '',
        'Synthetic eight-node graph only; this is not a fitted ThreatWeave domain-graph index.',
        'Configured dimensions: 128; seed: '+str(params['seed'])+'; workers: 1.',
        'Repeatability is checked within one process, not across hardware or software versions.', '',
        'Saved records: `'+str(folder)+'`', '']
    if receipt.get('error'):
        lines.extend(['Error: '+receipt['error'], ''])
    else:
        lines.extend(['Synthetic fitting, graph-vector storage and existing text-index regression checks passed.', ''])
    review = repo/'docs'/('ThreatWeave_node2vec_setup_'+folder.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'Saved setup records: {folder}\nSaved review document: {review}', flush=True)
    if code == 0:
        print('READY: Node2Vec dependencies, graph-vector probe and text-index regression checks passed.', flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
