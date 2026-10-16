"""Deterministic single-worker Node2Vec training for undirected projections."""
import hashlib
import json
import os


def training_parameters(config):
    params = dict(config['node2vec'])
    if (type(params['dimension']) is not int or type(params['workers']) is not int
            or params['dimension'] != 128 or params['workers'] != 1):
        raise ValueError('This graph-embedding stage requires 128 dimensions and one worker.')
    for key in ['walk_length', 'num_walks', 'window', 'epochs', 'negative']:
        if type(params[key]) is not int or params[key] <= 0:
            raise ValueError(f'Node2Vec {key} must be a positive integer.')
    if type(params['seed']) is not int or not 0 <= params['seed'] <= 4294967295:
        raise ValueError('Node2Vec seed must fit the Python hash-seed range.')
    for key in ['p', 'q']:
        if not isinstance(params[key], (int, float)) or not 0 < params[key] < float('inf'):
            raise ValueError(f'Node2Vec {key} must be finite and positive.')
    return params


def training_environment(params):
    environment = os.environ.copy()
    environment.update(PYTHONHASHSEED=str(params['seed']), OMP_NUM_THREADS='1',
                       OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1',
                       NUMEXPR_NUM_THREADS='1')
    return environment


def fit_projection(graph, params):
    params = training_parameters({'node2vec': params})
    if os.environ.get('PYTHONHASHSEED') != str(params['seed']):
        raise ValueError('Start the training process with its configured PYTHONHASHSEED.')
    import networkx as nx
    import numpy as np
    from node2vec import Node2Vec
    if graph.is_directed() or graph.is_multigraph():
        raise ValueError('Node2Vec requires the frozen simple undirected projection.')
    if not graph.number_of_nodes() or any(not isinstance(n, str) or not n for n in graph):
        raise ValueError('Projection requires nonempty string node IDs.')
    # Preserve a stable insertion order for both nodes and neighbor lists.
    stable = nx.Graph()
    nodes = sorted(graph.nodes())
    stable.add_nodes_from(nodes)
    stable.add_edges_from(sorted(tuple(sorted((a, b))) for a, b in graph.edges()))
    if any(a == b for a, b in stable.edges()):
        raise ValueError('The domain projection must not contain self-loops.')
    learner = Node2Vec(stable, dimensions=params['dimension'], walk_length=params['walk_length'],
        num_walks=params['num_walks'], p=params['p'], q=params['q'],
        workers=params['workers'], seed=params['seed'], quiet=True)
    fit_options = dict(window=params['window'], min_count=1, sg=1,
        epochs=params['epochs'], negative=params['negative'], workers=1,
        seed=params['seed'], hs=0, sample=0.001, ns_exponent=0.75,
        alpha=0.025, min_alpha=0.0001, sorted_vocab=1, shrink_windows=True)
    model = learner.fit(**fit_options)
    if set(model.wv.key_to_index) != set(nodes):
        raise ValueError('Node2Vec vocabulary differs from its projection nodes.')
    vectors = np.stack([model.wv[n] for n in nodes])
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    if vectors.shape != (len(nodes), 128) or not np.isfinite(vectors).all() or (norms <= 0).any():
        raise ValueError('Node2Vec generated invalid vectors.')
    normalized = vectors/norms
    walk_hash = hashlib.sha256(json.dumps(learner.walks, separators=(',', ':')).encode()).hexdigest()
    return {'node_ids': nodes, 'vectors': vectors, 'normalized_vectors': normalized,
            'walk_sha256': walk_hash, 'word2vec_parameters': fit_options,
            'walk_count': len(learner.walks)}
