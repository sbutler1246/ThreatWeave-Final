"""Load versioned Node2Vec assets and retrieve same-component seed neighbors."""
import hashlib
import importlib.metadata
import json
import math
import platform
import re
from pathlib import Path

from graph.development_projection import digest, undirected_graph
from graph.node2vec_training import training_parameters

IDENTITY_FIELDS = ['version', 'projection_sha256', 'node2vec_parameters', 'word2vec_parameters',
    'packages', 'python', 'training_source_sha256', 'training_environment',
    'raw_vector_sha256', 'normalized_vector_sha256', 'component_by_node']


def require_current_projection(manifest, projection_hash):
    if manifest['projection_sha256'] != projection_hash:
        raise ValueError('Live accepted graph differs from the fitted Node2Vec projection. Rebuild index_development_graph.py before full hybrid.')


def neighbor_priority(neighbors, k=60):
    scores = {}
    for seed, hits in neighbors.items():
        for rank, hit in enumerate(hits, 1):
            identifier = hit['canonical_id']
            scores[identifier] = max(scores.get(identifier, 0), 1/(k+rank))
    return scores


def path_key(path):
    return tuple((path['nodes'][i]['canonical_id'], e['predicate'],
                  path['nodes'][i+1]['canonical_id']) for i, e in enumerate(path['edges']))


def rank_candidates(base, expanded, priority, limit):
    by_key = {}
    for path in expanded+base:
        by_key.setdefault(path_key(path), path)
    score = lambda p: sum(priority.get(n, 0) for n in {node['canonical_id'] for node in p['nodes']})
    ordered = sorted(by_key.values(), key=lambda p: (-score(p), -len(p['edges']), path_key(p)))[:limit]
    return ordered, {path_key(p): score(p) for p in ordered}


class GraphVectorIndex:
    def __init__(self, repo, config):
        import numpy as np
        pointer_path = repo/'work/graph_index/current.json'
        if not pointer_path.is_file():
            raise ValueError('Full hybrid requires a ready graph-vector index; run index_development_graph.py.')
        pointer = json.loads(pointer_path.read_text(encoding='utf-8'))
        fingerprint = pointer['index_fingerprint']
        if not re.fullmatch(r'[a-f0-9]{64}', fingerprint):
            raise ValueError('Invalid graph-index fingerprint.')
        folder = repo/'work/graph_index'/fingerprint
        if Path(pointer['manifest_path']).resolve() != (folder/'manifest.json').resolve():
            raise ValueError('Graph-index pointer escapes its expected workspace location.')
        self.manifest = m = json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
        if digest({k: m[k] for k in IDENTITY_FIELDS}) != fingerprint or m['index_fingerprint'] != fingerprint:
            raise ValueError('Graph-index identity checksum mismatch.')
        if (m['dimension'] != 128 or m['normalized'] is not True or m['live_projection_verified'] is not True
                or m['corpus_version'] != config['corpus_version'] or m['attack_release'] != config['attack_release']
                or m['node2vec_parameters'] != training_parameters(config) or m['python'] != platform.python_version()):
            raise ValueError('Graph index does not match the current frozen configuration/runtime.')
        if hashlib.sha256((repo/'graph/node2vec_training.py').read_bytes()).hexdigest() != m['training_source_sha256']:
            raise ValueError('Graph-training implementation changed; rebuild its index.')
        for package, version in m['packages'].items():
            if importlib.metadata.version(package) != version:
                raise ValueError('Graph-index package versions changed; review and rebuild.')
        for field, filename in [('projection_path', 'projection.json'), ('vectors_path', 'vectors.npz')]:
            path = folder/filename
            if Path(m[field]).resolve() != path.resolve() or hashlib.sha256(path.read_bytes()).hexdigest() != m[field.replace('_path', '_file_sha256')]:
                raise ValueError('Graph-index file path or checksum mismatch.')
        self.projection = json.loads((folder/'projection.json').read_text(encoding='utf-8'))
        require_current_projection(m, digest(self.projection))
        with np.load(folder/'vectors.npz', allow_pickle=False) as arrays:
            ids = arrays['node_ids'].tolist()
            raw, vectors = arrays['raw_vectors'].copy(), arrays['normalized_vectors'].copy()
        if (ids != m['node_ids'] or ids != sorted(n['canonical_id'] for n in self.projection['nodes'])
                or len(set(ids)) != len(ids) or raw.shape != (len(ids), 128) or vectors.shape != raw.shape
                or not np.isfinite(raw).all() or not np.isfinite(vectors).all()
                or not np.allclose(np.linalg.norm(vectors, axis=1), 1, atol=1e-5)
                or not np.allclose(vectors, raw/np.linalg.norm(raw, axis=1, keepdims=True), atol=1e-6)
                or hashlib.sha256(raw.tobytes()).hexdigest() != m['raw_vector_sha256']
                or hashlib.sha256(vectors.tobytes()).hexdigest() != m['normalized_vector_sha256']):
            raise ValueError('Graph vector shapes, normalization, hashes or node-ID bindings failed.')
        import networkx as nx
        graph = undirected_graph(self.projection)
        components = {n: 'component:'+digest(sorted(c))[:16] for c in nx.connected_components(graph) for n in c}
        if components != m['component_by_node']:
            raise ValueError('Graph component metadata differs from the saved projection.')
        self.nodes = {n['canonical_id']: n for n in self.projection['nodes']}
        self.vectors = dict(zip(ids, vectors))
        import chromadb
        from chromadb.config import Settings
        store = repo/'work/chroma'
        if Path(m['chroma_path']).resolve() != store.resolve() or not (store/'chroma.sqlite3').is_file():
            raise ValueError('Graph-vector database is missing or points outside the workspace.')
        self.client = chromadb.PersistentClient(path=str(store), settings=Settings(anonymized_telemetry=False))
        self.collection = self.client.get_collection(m['collection_name'], embedding_function=None)
        expected = {'index_fingerprint': fingerprint, 'projection_sha256': m['projection_sha256'],
                    'dimension': 128, 'hnsw:space': 'cosine', 'corpus_version': config['corpus_version']}
        if m['collection_name'] != 'threatweave_graph_dev_'+fingerprint[:16] or any(self.collection.metadata.get(k) != v for k, v in expected.items()):
            raise ValueError('Graph collection metadata mismatch.')
        stored = self.collection.get(include=['documents', 'metadatas', 'embeddings'])
        if set(stored['ids']) != set(ids) or any(len(stored[k]) != len(ids) for k in ['ids', 'documents', 'metadatas', 'embeddings']):
            raise ValueError('Graph collection contents differ from the node-ID map.')
        for identifier, name, meta, vector in zip(stored['ids'], stored['documents'], stored['metadatas'], stored['embeddings']):
            if name != self.nodes[identifier]['name'] or meta != self.metadata(identifier) or not np.allclose(vector, self.vectors[identifier], atol=1e-6):
                raise ValueError('Stored graph vector or identity metadata differs from its manifest.')

    def metadata(self, identifier):
        return {'canonical_id': identifier, 'name': self.nodes[identifier]['name'],
                'entity_type': self.nodes[identifier]['type'], 'projection_sha256': self.manifest['projection_sha256'],
                'index_fingerprint': self.manifest['index_fingerprint'],
                'component_id': self.manifest['component_by_node'][identifier]}

    def neighbors(self, seed_ids, count=5):
        if count < 1:
            raise ValueError('Neighbor count must be positive.')
        excluded, neighbors = set(seed_ids), {}
        for seed in sorted(excluded):
            if seed not in self.vectors:
                raise ValueError('Linked seed is absent from the frozen graph index.')
            component = self.manifest['component_by_node'][seed]
            size = sum(c == component for c in self.manifest['component_by_node'].values())
            result = self.collection.query(query_embeddings=[self.vectors[seed].tolist()],
                n_results=min(size, count+len(excluded)), where={'component_id': component},
                include=['metadatas', 'distances'])
            if any(len(result[k]) != 1 for k in ['ids', 'metadatas', 'distances']) or any(
                    len(result[k][0]) != len(result['ids'][0]) for k in ['metadatas', 'distances']):
                raise ValueError('Graph-neighbor query returned inconsistent columns.')
            hits = []
            for identifier, meta, distance in zip(result['ids'][0], result['metadatas'][0], result['distances'][0]):
                if identifier not in self.nodes or meta != self.metadata(identifier) or self.manifest['component_by_node'][identifier] != component:
                    raise ValueError('Graph-neighbor identity or component mismatch.')
                if not math.isfinite(distance):
                    raise ValueError('Graph-neighbor query returned a non-finite distance.')
                if identifier not in excluded:
                    hits.append({'canonical_id': identifier, 'name': self.nodes[identifier]['name'],
                                 'cosine_distance': float(distance)})
            neighbors[seed] = sorted(hits, key=lambda h: (h['cosine_distance'], h['canonical_id']))[:count]
        return neighbors
