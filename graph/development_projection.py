"""Read and freeze a source-verified development domain projection from Neo4j."""
import hashlib
import json

from graph.development_retrieval import ASSERTION_QUERY
from schemas import Entity

VERSION = 'development-domain-projection-v2-reviewed-scopes'
EDGE_QUERY = """
MATCH (h:Entity)-[r:USES|USES_TECHNIQUE|MITIGATED_BY]->(t:Entity)
WHERE h.canonical_id IN $ids AND t.canonical_id IN $ids
RETURN properties(h) AS head, properties(t) AS tail,
       type(r) AS predicate, coalesce(r.assertion_ids,[]) AS assertion_ids
ORDER BY h.canonical_id, type(r), t.canonical_id
"""


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode()).hexdigest()


def expected_triples(retriever):
    triples = {t for p in retriever.profiles.values() for t in p['allowed_triples']}
    triples.update((r['assertion']['head_id'], r['assertion']['predicate'], r['assertion']['tail_id'])
                   for r in retriever.references.values())
    return triples


def freeze_projection(retriever, edge_rows, assertion_rows):
    records = {}
    for row in assertion_rows:
        identifier = row['assertion']['assertion_id']
        if identifier in records and records[identifier] != row:
            raise ValueError('Duplicate assertion ID with conflicting stored evidence.')
        records[identifier] = row
    nodes, edges = {}, {}
    for row in edge_rows:
        head, tail, predicate = row['head'], row['tail'], row['predicate']
        path = {'nodes': [head, tail], 'edges': [{'predicate': predicate,
                                                'assertion_ids': row['assertion_ids']}]}
        candidate = retriever._candidate(path, records)
        if candidate is None:
            continue
        signature = head['canonical_id'], predicate, tail['canonical_id']
        if signature in edges:
            raise ValueError('Duplicate stored relationships for the same domain fact.')
        supporting = []
        for identifier in sorted(set(row['assertion_ids'])):
            if identifier not in records:
                continue
            record = retriever._verify_record(records[identifier], *signature)
            if record is None:
                continue
            raw = records[identifier]
            supporting.append({'assertion': record['assertion'].model_dump(mode='json'),
                'source_hash': raw['assertion']['source_hash'],
                'source_snapshot_sha256': raw['assertion'].get('source_snapshot_sha256'),
                'source_stix_relationship_id': raw['assertion'].get('source_stix_relationship_id'),
                'passages': record['passages']})
            profile = retriever.profiles.get(record['assertion'].chunk_id, {})
            pinned = profile.get('accepted_assertions', {}).get(identifier)
            if pinned is not None:
                supporting[-1]['source_record'] = {key:raw['assertion'].get(key) for key in pinned}
        if not supporting:
            continue
        for raw in [head, tail]:
            entity = Entity.model_validate({k: v for k, v in raw.items() if k in Entity.model_fields})
            expected = retriever.expected_entities[entity.canonical_id]
            if set(entity.aliases) != set(expected.get('aliases', [])):
                raise ValueError('Stored aliases differ from the frozen resolved identity.')
            identity = {k: expected[k] for k in ['canonical_id', 'type', 'name', 'attack_id',
                'stix_id', 'attack_release', 'resolution_status'] if k in expected}
            identity['aliases'] = sorted(entity.aliases)
            if entity.canonical_id in nodes and nodes[entity.canonical_id] != identity:
                raise ValueError('Graph node identity changed within the projection read.')
            nodes[entity.canonical_id] = identity
        edges[signature] = {'head_id': signature[0], 'predicate': signature[1],
                            'tail_id': signature[2], 'support': supporting}
    missing = expected_triples(retriever)-set(edges)
    if missing:
        raise ValueError(f'{len(missing)} required development facts are absent or lack accepted source evidence; complete/review ingestion before fitting.')
    if set(nodes) != set(retriever.expected_entities):
        raise ValueError('Projection nodes differ from the imported development source identities.')
    value = {'version': VERSION, 'scope': retriever.scope_name,
        'corpus_version': retriever.config['corpus_version'], 'attack_release': retriever.config['attack_release'],
        'cisa_sources': [{'scope_id': key, 'doc_id': p['document'].doc_id,
                          'source_hash': p['document'].content_hash} for key, p in sorted(retriever.profiles.items())],
        'nodes': [nodes[key] for key in sorted(nodes)], 'edges': [edges[key] for key in sorted(edges)],
        'projection_policy': 'simple_undirected_unweighted; domain endpoints only; no Document/Chunk/Assertion hubs; typed directed facts retained in edge provenance'}
    return value, digest(value)


def read_projection(driver, retriever, database='neo4j'):
    with driver.session(database=database, default_access_mode='READ') as session:
        def read(tx):
            edges = [r.data() for r in tx.run(EDGE_QUERY, ids=sorted(retriever.expected_entities))]
            identifiers = sorted({i for row in edges for i in row['assertion_ids']})
            rows = [r.data() for r in tx.run(ASSERTION_QUERY, ids=identifiers)] if identifiers else []
            return freeze_projection(retriever, edges, rows)
        return session.execute_read(read)


def undirected_graph(projection):
    import networkx as nx
    graph = nx.Graph()
    graph.add_nodes_from(n['canonical_id'] for n in projection['nodes'])
    graph.add_edges_from(sorted({tuple(sorted((e['head_id'], e['tail_id']))) for e in projection['edges']}))
    if any(a == b for a, b in graph.edges()):
        raise ValueError('Domain projection contains a self-loop.')
    return graph


def preview_projection(retriever):
    """Source-derived fixtures only; never publish these as a live graph index."""
    edges, records = [], []
    for scope, profile in sorted(retriever.profiles.items()):
        doc, chunk = profile['document'], profile['chunk']
        d = doc.model_dump(mode='json')
        c = chunk.model_dump(mode='json')
        c['inherited_context_json'] = json.dumps(c.pop('inherited_context'))
        if 'accepted_assertions' in profile:
            for assertion in profile['accepted_assertions'].values():
                records.append({'assertion':assertion,'document':d,'chunk':c})
                edges.append({'head':retriever.expected_entities[assertion['head_id']],
                              'tail':retriever.expected_entities[assertion['tail_id']],
                              'predicate':assertion['predicate'],'assertion_ids':[assertion['assertion_id']]})
            continue
        for head, predicate, tail in sorted(profile['allowed_triples']):
            aid = 'preview:'+scope+':'+digest([head,predicate,tail])
            assertion = dict(assertion_id=aid, head_id=head, predicate=predicate, tail_id=tail,
                source_doc_id=doc.doc_id, chunk_id=scope, evidence_text=chunk.text,
                evidence_start=chunk.start, evidence_end=chunk.end, source_hash=doc.content_hash,
                triple_key=hashlib.sha256('\x1f'.join([head, predicate, tail]).encode()).hexdigest(),
                origin='extracted', validation_status='validated')
            records.append({'assertion': assertion, 'document': d, 'chunk': c})
            edges.append({'head': retriever.expected_entities[head], 'tail': retriever.expected_entities[tail],
                          'predicate': predicate, 'assertion_ids': [aid]})
    for record in retriever.references.values():
        a = record['assertion']
        records.append({key: record[key] for key in ['assertion', 'document', 'chunk']})
        edges.append({'head': retriever.expected_entities[a['head_id']],
                      'tail': retriever.expected_entities[a['tail_id']],
                      'predicate': a['predicate'], 'assertion_ids': [a['assertion_id']]})
    # Neo4j stores one factual relationship with multiple assertion supports.
    # Repeated facts across reviewed source windows must use that same shape.
    merged = {}
    for edge in edges:
        key = edge['head']['canonical_id'], edge['predicate'], edge['tail']['canonical_id']
        if key not in merged:
            merged[key] = dict(edge, assertion_ids=[])
        merged[key]['assertion_ids'] = sorted(set(merged[key]['assertion_ids'] + edge['assertion_ids']))
    edges = list(merged.values())
    projection, fingerprint = freeze_projection(retriever, edges, records)
    return projection, fingerprint, edges, records
