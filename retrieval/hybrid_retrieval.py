"""Full development hybrid retrieval with validated Node2Vec path expansion."""
import hashlib
import json
import time

from graph.development_projection import EDGE_QUERY, freeze_projection
from graph.development_retrieval import ASSERTION_QUERY, PATH_QUERY, matches_groups, seed_groups
from retrieval.combined_retrieval import DevelopmentCombinedRetriever, combine
from retrieval.development_text import sha
from retrieval.graph_vectors import GraphVectorIndex, neighbor_priority, rank_candidates, require_current_projection
from schemas import QueryRequest

DOMAIN_PATH_QUERY = PATH_QUERY.replace('WHERE all(n IN nodes(p) WHERE n:Entity)',
    'WHERE all(n IN nodes(p) WHERE n:Entity AND n.canonical_id IN $domain_ids)')
EXPANSION_QUERY = DOMAIN_PATH_QUERY.replace('RETURN [n IN nodes(p)',
    'AND any(n IN nodes(p) WHERE n.canonical_id IN $neighbor_ids)\nRETURN [n IN nodes(p)').replace(
    'length(p) AS hops', 'length(p) AS hops, reduce(s=0.0, n IN nodes(p) | s+coalesce($neighbor_priority[n.canonical_id],0.0)) AS structural_score').replace(
    'ORDER BY hops DESC', 'ORDER BY structural_score DESC, hops DESC')


def source_mentions(graph):
    mentions = []
    for profile in graph.profiles.values():
        if 'source_mentions' in profile:
            mentions.extend(profile['source_mentions'])
            continue
        lines = profile['chunk'].text.splitlines()
        if len(lines) < 5 or not profile['chunk'].inherited_context:
            continue
        for head, predicate, tail in profile['allowed_triples']:
            if predicate == 'USES':
                mentions.append({'id': tail, 'text': lines[0]})
            if predicate == 'USES_TECHNIQUE':
                mentions.append({'id': tail, 'text': lines[-1]})
    return mentions


def saved_projection_rows(index, graph):
    """Validate saved source records for an offline preview, without live claims."""
    rows = []
    for edge in index.projection['edges']:
        for support in edge['support']:
            assertion = support['assertion']
            if assertion['origin'] == 'fused':
                reference = graph.references[assertion['assertion_id']]
                a = dict(reference['assertion'], **assertion)
                rows.append({'assertion': a, 'document': reference['document'], 'chunk': reference['chunk']})
            else:
                profile = graph.profiles[assertion['chunk_id']]
                d, c = profile['document'].model_dump(mode='json'), profile['chunk'].model_dump(mode='json')
                c['inherited_context_json'] = json.dumps(c.pop('inherited_context'))
                first = support['passages'][0]
                a = dict(support.get('source_record',{}), **assertion)
                a.update(source_hash=support['source_hash'], evidence_start=first['start'],
                    evidence_end=first['end'], triple_key=hashlib.sha256('\x1f'.join(
                        [edge['head_id'], edge['predicate'], edge['tail_id']]).encode()).hexdigest())
                rows.append({'assertion': a, 'document': d, 'chunk': c})
    return rows


def enumerate_paths(projection, nodes, max_hops=3):
    adjacency, paths = {}, []
    for edge in projection['edges']:
        adjacency.setdefault(edge['head_id'], []).append(edge)
    def visit(chain, edges):
        if edges:
            paths.append({'nodes': [nodes[n] for n in chain], 'edges': edges})
        if len(edges) >= max_hops:
            return
        for edge in adjacency.get(chain[-1], []):
            if edge['tail_id'] not in chain:
                visit(chain+[edge['tail_id']], edges+[{'predicate': edge['predicate'],
                    'assertion_ids': [s['assertion']['assertion_id'] for s in edge['support']]}])
    for identifier in sorted(nodes):
        visit([identifier], [])
    return paths


class DevelopmentHybridRetriever(DevelopmentCombinedRetriever):
    def __init__(self, repo, driver=None, database='neo4j'):
        super().__init__(repo, driver, database)
        self.index = GraphVectorIndex(repo, self.config)
        self.configuration_hash = sha(self.configuration_hash+self.index.manifest['index_fingerprint']+
                                      DOMAIN_PATH_QUERY+EXPANSION_QUERY+'development-full-hybrid-v1')
        self.mentions = source_mentions(self.graph)

    def _graph_branch(self, question, preview):
        def finish(projection, base, expanded, rows, groups, neighbors):
            priorities = neighbor_priority(neighbors, self.config['retrieval']['rrf_k'])
            paths, scores = rank_candidates(base, expanded, priorities, self.graph.max_candidates)
            bundle = self.graph.assemble(paths, rows, groups, path_priority=scores)
            details = {'seed_groups': groups, 'neighbors_by_seed': neighbors,
                'neighbor_count_per_seed': self.config['retrieval']['structural_neighbors_per_seed'],
                'base_candidate_count': len(base), 'expansion_candidate_count': len(expanded),
                'merged_candidate_count': len(paths), 'graph_index_fingerprint': self.index.manifest['index_fingerprint'],
                'projection_sha256': self.index.manifest['projection_sha256'],
                'graph_freshness_verified': not preview, 'similarity_is_fact_evidence': False}
            return bundle, details
        if preview:
            rows = saved_projection_rows(self.index, self.graph)
            # Recheck source-derived identity/evidence against the persisted snapshot.
            edges = [{'head': self.index.nodes[e['head_id']], 'tail': self.index.nodes[e['tail_id']],
                      'predicate': e['predicate'], 'assertion_ids': [s['assertion']['assertion_id'] for s in e['support']]}
                     for e in self.index.projection['edges']]
            _, fingerprint = freeze_projection(self.graph, edges, rows)
            require_current_projection(self.index.manifest, fingerprint)
            groups = seed_groups(question, list(self.index.nodes.values()), self.mentions, self.graph.max_seeds)
            seeds = sorted({i for group in groups for i in group})
            neighbors = self.index.neighbors(seeds, self.config['retrieval']['structural_neighbors_per_seed'])
            priority = neighbor_priority(neighbors, self.config['retrieval']['rrf_k'])
            all_paths = enumerate_paths(self.index.projection, self.index.nodes, self.graph.max_hops)
            valid = [p for p in all_paths if matches_groups(p['nodes'], groups)]
            base, _ = rank_candidates(valid, [], {}, self.graph.max_candidates)
            expanded, _ = rank_candidates([], [p for p in valid if any(n['canonical_id'] in priority for n in p['nodes'])], priority, self.graph.max_candidates)
            return finish(self.index.projection, base, expanded, rows, groups, neighbors)
        with self.graph.driver.session(database=self.graph.database, default_access_mode='READ') as session:
            def read(tx):
                edges = [r.data() for r in tx.run(EDGE_QUERY, ids=sorted(self.index.nodes))]
                ids = sorted({i for e in edges for i in e['assertion_ids']})
                rows = [r.data() for r in tx.run(ASSERTION_QUERY, ids=ids)]
                projection, fingerprint = freeze_projection(self.graph, edges, rows)
                require_current_projection(self.index.manifest, fingerprint)
                groups = seed_groups(question, projection['nodes'], self.mentions, self.graph.max_seeds)
                seeds = sorted({i for group in groups for i in group})
                neighbors = self.index.neighbors(seeds, self.config['retrieval']['structural_neighbors_per_seed'])
                priority = neighbor_priority(neighbors, self.config['retrieval']['rrf_k'])
                query_args = dict(seed_groups=groups, domain_ids=sorted(self.index.nodes), limit=self.graph.max_candidates)
                base = [r.data() for r in tx.run(DOMAIN_PATH_QUERY, **query_args)] if groups else []
                expanded = [r.data() for r in tx.run(EXPANSION_QUERY, **query_args,
                    neighbor_ids=sorted(priority), neighbor_priority=priority)] if priority and groups else []
                result = finish(projection, base, expanded, rows, groups, neighbors)
                # Read-committed transactions can observe concurrent changes between queries.
                final_edges = [r.data() for r in tx.run(EDGE_QUERY, ids=sorted(self.index.nodes))]
                final_ids = sorted({i for e in final_edges for i in e['assertion_ids']})
                final_rows = [r.data() for r in tx.run(ASSERTION_QUERY, ids=final_ids)]
                _, final_hash = freeze_projection(self.graph, final_edges, final_rows)
                require_current_projection(self.index.manifest, final_hash)
                return result
            return session.execute_read(read)

    def _retrieve(self, request, preview):
        if request.mode.value != 'hybrid' or request.corpus_version != self.config['corpus_version']:
            raise ValueError('Full hybrid retriever requires hybrid and its frozen corpus version.')
        started = time.perf_counter()
        graph_bundle, details = self._graph_branch(request.question, preview)
        self.text.retrieve(QueryRequest(question=request.question, mode='text_only', corpus_version=request.corpus_version))
        records = [self.text.by_id[i] for i in self.text.last_stats['selected_chunk_ids']]
        bundle, self.last_context, self.last_stats = combine(graph_bundle, records, self.config,
                                                            self.configuration_hash, self.names)
        self.last_stats.update(mode='hybrid', node2vec_enabled=True, node2vec=details,
            graph_branch=self.graph.last_stats, text_branch=self.text.last_stats,
            graph_source='saved_live_projection_preview' if preview else 'live_neo4j',
            index_fingerprint=self.text.manifest['fingerprint'])
        bundle.retrieval_ms = (time.perf_counter()-started)*1000
        self.last_stats['retrieval_ms'] = bundle.retrieval_ms
        return bundle
