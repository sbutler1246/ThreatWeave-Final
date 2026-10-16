"""Combine verified text and graph branches in the explicit Node2Vec ablation."""
import json
import time

from graph.development_retrieval import DevelopmentGraphRetriever, evidence_context
from retrieval.development_text import sha
from retrieval.text_retrieval import DevelopmentTextRetriever, source_bundle
from schemas import EvidenceBundle, GraphPath, Passage, QueryRequest, RelationshipEdge

VERSION = 'development-combined-no-node2vec-v1'


def reciprocal_ranks(branches, k=60):
    """A source parent contributes once per branch, at its first unique rank."""
    if k <= 0:
        raise ValueError('RRF k must be positive.')
    scores, ranks = {}, {}
    for branch, keys in branches.items():
        unique = list(dict.fromkeys(keys))
        for rank, key in enumerate(unique, 1):
            scores[key] = scores.get(key, 0)+1/(k+rank)
            ranks.setdefault(key, {})[branch] = rank
    return scores, ranks


def span_key(p):
    return p.doc_id, p.start, p.end


def merge_groups(groups, config, configuration_hash):
    """Renumber citations globally; keep every selected path whole."""
    passages, paths = {}, []
    for group in groups:
        mapping = {}
        for old in group['passages']:
            key = span_key(old)
            if key in passages:
                previous = passages[key]
                if (previous.text != old.text or previous.source_url != old.source_url
                        or previous.source_kind != old.source_kind):
                    raise ValueError('Branches disagree on the same source span.')
            else:
                passages[key] = Passage(**dict(old.model_dump(), citation_id=f'E{len(passages)+1}'))
            mapping[old.citation_id] = passages[key].citation_id
        path = group.get('path')
        if path is not None:
            edges = [RelationshipEdge(**dict(e.model_dump(),
                citation_ids=list(dict.fromkeys(mapping[c] for c in e.citation_ids)))) for e in path.edges]
            paths.append(GraphPath(path_id=f'P{len(paths)+1}', edges=edges))
    return EvidenceBundle(passages=list(passages.values()), paths=paths,
        citation_ids=[p.citation_id for p in passages.values()], retrieval_ms=0,
        configuration_hash=configuration_hash, corpus_version=config['corpus_version'])


def combine(graph_bundle, text_records, config, configuration_hash, names):
    if graph_bundle.corpus_version != config['corpus_version']:
        raise ValueError('Graph and text corpus versions differ.')
    graph_passages = {p.citation_id: p for p in graph_bundle.passages}
    groups, graph_keys, text_keys = [], [], []
    for path in graph_bundle.paths:
        # The first citation of each verified edge is its own source quote/header.
        # Shared table captions must not reassign another row's parent identity.
        keys = list(dict.fromkeys((graph_passages[e.citation_ids[0]].doc_id,
                                  graph_passages[e.citation_ids[0]].chunk_id) for e in path.edges))
        graph_keys.extend(keys)
        citations = list(dict.fromkeys(c for e in path.edges for c in e.citation_ids))
        groups.append({'kind': 'graph', 'id': path.path_id, 'path': path, 'keys': keys,
                       'passages': [graph_passages[c] for c in citations]})
    seen_children = set()
    for record in text_records[:config['retrieval']['final_chunks']]:
        child = record['chunk']
        if child['chunk_id'] in seen_children:
            continue
        seen_children.add(child['chunk_id'])
        key = child['doc_id'], child['parent_extraction_chunk_id']
        text_keys.append(key)
        passages = source_bundle([record], config, configuration_hash).passages
        groups.append({'kind': 'text', 'id': child['chunk_id'], 'keys': [key], 'passages': passages})
    scores, ranks = reciprocal_ranks({'graph': graph_keys, 'text': text_keys}, config['retrieval']['rrf_k'])
    for group in groups:
        # Sum distinct parent scores so a complete supported path stays a unit.
        # This aggregation is an implementation choice, not an RRF theorem.
        group['score'] = sum(scores[key] for key in group['keys'])
    ordered = sorted(groups, key=lambda g: (-g['score'], g['kind'], g['id']))
    selected, skipped = [], []
    counts = {'graph': 0, 'text': 0}
    limits = {'graph': config['retrieval']['final_paths'], 'text': config['retrieval']['final_chunks']}
    byte_cap = config['retrieval']['evidence_token_budget']
    for group in ordered:
        if counts[group['kind']] >= limits[group['kind']]:
            skipped.append({'kind': group['kind'], 'id': group['id'], 'reason': 'branch_limit'})
            continue
        trial = merge_groups(selected+[group], config, configuration_hash)
        if len(evidence_context(trial, names).encode('utf-8')) > byte_cap:
            skipped.append({'kind': group['kind'], 'id': group['id'], 'reason': 'context_budget'})
            continue
        selected.append(group)
        counts[group['kind']] += 1
    bundle = merge_groups(selected, config, configuration_hash)
    context = evidence_context(bundle, names)
    stats = {'mode': 'hybrid_no_node2vec', 'node2vec_enabled': False,
        'rrf_k': config['retrieval']['rrf_k'],
        'rrf_unit': '(source doc_id, parent extraction chunk_id)',
        'rrf_group_aggregation': 'sum of distinct source-parent scores; whole-path/text-context groups',
        'source_ranks': [{'doc_id': key[0], 'parent_chunk_id': key[1],
                          'ranks': ranks[key], 'rrf_score': scores[key]} for key in sorted(scores)],
        'candidate_groups': [{'kind': g['kind'], 'id': g['id'], 'score': g['score']} for g in ordered],
        'selected_groups': [{'kind': g['kind'], 'id': g['id'], 'score': g['score']} for g in selected],
        'selected_path_count': counts['graph'], 'selected_text_chunk_count': counts['text'],
        'selected_hops': [len(p.edges) for p in bundle.paths], 'skipped_groups': skipped,
        'evidence_utf8_bytes': len(context.encode('utf-8')), 'evidence_byte_cap': byte_cap,
        'budget_method': 'conservative_utf8_byte_cap',
        'graph_branch_empty': not graph_bundle.paths}
    return bundle, context, stats


class DevelopmentCombinedRetriever:
    def __init__(self, repo, driver=None, database='neo4j'):
        self.graph = DevelopmentGraphRetriever(repo, driver, database)
        self.text = DevelopmentTextRetriever(repo)
        if self.graph.config != self.text.config:
            raise ValueError('Graph and text branch configurations differ.')
        self.config = self.graph.config
        self.names = {k: v['name'] for k, v in self.graph.expected_entities.items()}
        self.configuration_hash = sha(json.dumps(self.config, sort_keys=True)+VERSION+
            self.graph.configuration_hash+self.text.configuration_hash)
        self.last_context, self.last_stats = '', {}

    def _retrieve(self, request, preview):
        if request.mode.value != 'hybrid_no_node2vec' or request.corpus_version != self.config['corpus_version']:
            raise ValueError('This stage supports hybrid_no_node2vec only; full hybrid requires its separate graph embeddings.')
        started = time.perf_counter()
        graph_request = QueryRequest(question=request.question, mode='graph_only', corpus_version=request.corpus_version)
        text_request = QueryRequest(question=request.question, mode='text_only', corpus_version=request.corpus_version)
        graph_bundle = self.graph.preview(request.question) if preview else self.graph.retrieve(graph_request)
        self.text.retrieve(text_request)
        selected = [self.text.by_id[i] for i in self.text.last_stats['selected_chunk_ids']]
        bundle, self.last_context, self.last_stats = combine(graph_bundle, selected, self.config,
                                                            self.configuration_hash, self.names)
        self.last_stats.update(graph_branch=self.graph.last_stats, text_branch=self.text.last_stats,
                               graph_source='offline_source_fixture' if preview else 'live_neo4j',
                               index_fingerprint=self.text.manifest['fingerprint'])
        bundle.retrieval_ms = (time.perf_counter()-started)*1000
        self.last_stats['retrieval_ms'] = bundle.retrieval_ms
        return bundle

    def retrieve(self, request):
        return self._retrieve(request, False)

    def preview(self, request):
        return self._retrieve(request, True)
