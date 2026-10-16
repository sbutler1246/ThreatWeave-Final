"""Plain display models and an offline, dependency-free interactive query graph."""
import json
from pathlib import Path
from uuid import uuid4

MODE_LABELS = {'hybrid': 'Full hybrid', 'text_only': 'Text only',
               'graph_only': 'Graph only', 'hybrid_no_node2vec': 'Hybrid without Node2Vec'}


def query_graph(answer, entities):
    passages = {p.citation_id: p for p in answer.evidence.passages}
    nodes, edges = {}, {}
    ranks = {'ThreatGroup': 0, 'Software': 1, 'Technique': 2, 'Mitigation': 3}
    for path in answer.evidence.paths:
        for depth, edge in enumerate(path.edges):
            for identifier, fallback in ((edge.head_id, depth), (edge.tail_id, depth+1)):
                entity = entities.get(identifier, {})
                kind = entity.get('type', 'Entity')
                nodes[identifier] = {'id': identifier, 'name': entity.get('name', identifier),
                    'type': kind, 'column': ranks.get(kind, fallback)}
            key = (edge.head_id, edge.predicate.value, edge.tail_id)
            record = edges.setdefault(key, {'head': edge.head_id, 'tail': edge.tail_id,
                'predicate': edge.predicate.value, 'assertions': [], 'citations': [], 'sources': []})
            for target, values in (('assertions', edge.assertion_ids), ('citations', edge.citation_ids)):
                record[target] = list(dict.fromkeys(record[target]+values))
            kinds = {passages[c].source_kind for c in record['citations']}
            record['sources'] = sorted(kinds)
            record['origin'] = ('ATT&CK reference' if kinds == {'attack'} else
                                'CISA observation' if kinds == {'cisa'} else 'Mixed sources')
    return {'nodes': list(nodes.values()), 'edges': list(edges.values())}


def graph_html(answer, entities):
    data = json.dumps(query_graph(answer, entities), ensure_ascii=True)
    # Source strings stay data: prevent even a literal closing script tag.
    data = data.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    template = (Path(__file__).parent/'application_graph.html').read_text(encoding='utf-8')
    return template.replace('__ROOT_ID__', 'tw-'+uuid4().hex).replace('__GRAPH_DATA__', data)


def add_history(history, result, limit=30):
    """Keep answer snapshots independent of subsequent mutable retriever state."""
    import copy
    return (history+[copy.deepcopy(result.as_dict())])[-limit:]
