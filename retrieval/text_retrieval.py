"""Source-checked nearest-neighbor text retrieval, without graph expansion."""
import importlib.metadata
import json
import math
import time
from pathlib import Path

from graph.development_retrieval import evidence_context
from retrieval.development_text import load_model, load_tokenizer, metadata, parents, prepare_records, sha, wordpieces
from schemas import EvidenceBundle, Passage

VERSION = 'development-text-retrieval-v1'


def source_bundle(records, config, configuration_hash, retrieval_ms=0):
    passages = {}
    for record in records:
        child = record['chunk']
        spans = [(child['start'], child['end'], child['text'])]+[
            (c['start'], c['end'], c['text']) for c in child['inherited_context']]
        for start, end, text in spans:
            key = (child['doc_id'], start, end)
            if key not in passages:
                passages[key] = Passage(citation_id=f'E{len(passages)+1}', doc_id=child['doc_id'],
                    chunk_id=child['chunk_id'], source_url=record['source_url'], text=text,
                    start=start, end=end, source_kind=record['source_kind'])
            elif passages[key].text != text:
                raise ValueError('Different source text claims the same document span.')
    return EvidenceBundle(passages=list(passages.values()), paths=[],
        citation_ids=[p.citation_id for p in passages.values()], retrieval_ms=retrieval_ms,
        configuration_hash=configuration_hash, corpus_version=config['corpus_version'])


def pack_hits(hits, expected, config, configuration_hash):
    """Keep source/context groups whole under the same conservative graph-QA cap."""
    selected, selected_ids, skipped, ranks = [], set(), 0, []
    cap = config['retrieval']['evidence_token_budget']
    for rank, hit in enumerate(hits[:config['retrieval']['text_candidates']], 1):
        identifier = hit['id']
        if identifier not in expected:
            raise ValueError('Text search returned an unknown source chunk.')
        record = expected[identifier]
        if hit['document'] != record['embedding_text'] or hit['metadata'] != metadata(record):
            raise ValueError('Text search returned altered source text or provenance.')
        distance = float(hit['distance'])
        if not math.isfinite(distance):
            raise ValueError('Text search returned a non-finite distance.')
        ranks.append({'rank': rank, 'chunk_id': identifier,
            'parent_extraction_chunk_id': record['chunk']['parent_extraction_chunk_id'],
            'source_kind': record['source_kind'], 'cosine_distance': distance})
        if identifier in selected_ids or len(selected) >= config['retrieval']['final_chunks']:
            continue
        trial = source_bundle(selected+[record], config, configuration_hash)
        if len(evidence_context(trial, {}).encode('utf-8')) > cap:
            skipped += 1
            continue
        selected.append(record)
        selected_ids.add(identifier)
    bundle = source_bundle(selected, config, configuration_hash)
    context = evidence_context(bundle, {})
    stats = {'candidate_ranks': ranks, 'candidate_chunk_count': len(ranks),
             'selected_chunk_ids': [r['chunk']['chunk_id'] for r in selected],
             'selected_chunk_count': len(selected), 'selected_path_count': 0,
             'evidence_utf8_bytes': len(context.encode('utf-8')), 'evidence_byte_cap': cap,
             'budget_method': 'conservative_utf8_byte_cap', 'budget_skipped_chunks': skipped,
             'search': 'normalized_MiniLM_cosine_nearest_neighbors; no graph expansion'}
    return bundle, context, stats


def checked_manifest(manifest, config, fingerprint, records_path, store):
    expected = {'fingerprint': fingerprint, 'embedding': config['text_embedding'],
                'development_scope':config.get('development_scope'),
                'chunking': config['chunking'], 'corpus_version': config['corpus_version'],
                'collection_name': 'threatweave_text_dev_'+fingerprint[:16]}
    if any(manifest.get(k) != v for k, v in expected.items()):
        raise ValueError('Saved text index does not match the configured sources/model.')
    if (Path(manifest['records_path']).resolve() != records_path.resolve()
            or Path(manifest['chroma_path']).resolve() != store.resolve()):
        raise ValueError('Saved text index points outside its expected workspace locations.')
    if sha(records_path.read_text(encoding='utf-8')) != manifest['records_sha256']:
        raise ValueError('Saved text-record checksum changed.')


class DevelopmentTextRetriever:
    def __init__(self, repo):
        self.repo = repo
        _, config = parents(repo)
        self.tokenizer = load_tokenizer(repo, config)
        records, self.config, fingerprint = prepare_records(repo, self.tokenizer)
        folder = repo/'work/text_index'/fingerprint
        manifest_path = folder/'manifest.json'
        if not manifest_path.is_file():
            raise ValueError('No index for the current sources/configuration. Run index_development_text.py first.')
        self.manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        records_path, store = folder/'records.json', repo/'work/chroma'
        checked_manifest(self.manifest, self.config, fingerprint, records_path, store)
        if json.loads(records_path.read_text(encoding='utf-8')) != records:
            raise ValueError('Saved text records differ from the frozen source spans.')
        for name, version in self.manifest['packages'].items():
            if importlib.metadata.version(name) != version:
                raise ValueError(f'{name} differs from the indexed environment; review and rebuild the index.')
        if not (store/'chroma.sqlite3').is_file():
            raise ValueError('Persistent Chroma index is missing.')
        import chromadb
        import numpy as np
        from chromadb.config import Settings
        self.client = chromadb.PersistentClient(path=str(store), settings=Settings(anonymized_telemetry=False))
        self.collection = self.client.get_collection(self.manifest['collection_name'], embedding_function=None)
        expected_metadata = {'hnsw:space': 'cosine', 'index_fingerprint': fingerprint,
                             'model_revision': config['text_embedding']['revision'], 'dimension': 384}
        if any(self.collection.metadata.get(k) != v for k, v in expected_metadata.items()):
            raise ValueError('Chroma collection metadata differs from the text manifest.')
        self.by_id = {r['chunk']['chunk_id']: r for r in records}
        stored = self.collection.get(include=['documents', 'metadatas', 'embeddings'])
        if (len(stored['ids']) != len(records) or set(stored['ids']) != set(self.by_id)
                or any(len(stored[k]) != len(records) for k in ['documents', 'metadatas', 'embeddings'])):
            raise ValueError('Stored text collection contents differ from the source manifest.')
        for identifier, text, meta in zip(stored['ids'], stored['documents'], stored['metadatas']):
            record = self.by_id[identifier]
            if text != record['embedding_text'] or meta != metadata(record):
                raise ValueError('Stored text or source metadata was altered.')
        self.model = load_model(repo, config)
        # Verify vector/source binding, not just vector dimensions or length.
        expected_vectors = self.model.encode([self.by_id[i]['embedding_text'] for i in stored['ids']],
            normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)
        actual = np.asarray(stored['embeddings'])
        if (actual.shape != expected_vectors.shape or not np.isfinite(actual).all()
                or not np.allclose(actual, expected_vectors, atol=1e-5, rtol=1e-5)):
            raise ValueError('Stored vectors differ from embeddings of their frozen source records.')
        self.special_tokens = self.tokenizer.num_special_tokens_to_add(pair=False)
        self.configuration_hash = sha(json.dumps(self.config, sort_keys=True)+fingerprint+VERSION)
        self.last_context, self.last_stats = '', {}

    def retrieve(self, request):
        if request.mode.value != 'text_only' or request.corpus_version != self.config['corpus_version']:
            raise ValueError('Text retriever requires text_only and its frozen corpus version.')
        if wordpieces(self.tokenizer, request.question)+self.special_tokens > self.model.max_seq_length:
            raise ValueError('Question exceeds the MiniLM input limit; shorten it instead of silently truncating it.')
        started = time.perf_counter()
        vector = self.model.encode([request.question], normalize_embeddings=True, convert_to_numpy=True)
        count = min(self.config['retrieval']['text_candidates'], len(self.by_id))
        result = self.collection.query(query_embeddings=vector.tolist(), n_results=count,
                                       include=['documents', 'metadatas', 'distances'])
        if any(len(result[k]) != 1 for k in ['ids', 'documents', 'metadatas', 'distances']):
            raise ValueError('Text query returned an unexpected result shape.')
        size = len(result['ids'][0])
        if any(len(result[k][0]) != size for k in ['documents', 'metadatas', 'distances']):
            raise ValueError('Text query returned inconsistent result columns.')
        hits = [dict(id=i, document=d, metadata=m, distance=s) for i, d, m, s in zip(
            result['ids'][0], result['documents'][0], result['metadatas'][0], result['distances'][0])]
        bundle, self.last_context, self.last_stats = pack_hits(hits, self.by_id, self.config, self.configuration_hash)
        bundle.retrieval_ms = (time.perf_counter()-started)*1000
        self.last_stats.update(index_fingerprint=self.manifest['fingerprint'], retrieval_ms=bundle.retrieval_ms)
        return bundle
