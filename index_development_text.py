"""Index frozen development text in Chroma and show three retrieval smoke checks."""
import argparse
import importlib.metadata
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from graph_qa import DEMO_QUESTIONS
from retrieval.development_text import (load_model, load_tokenizer, metadata, parents,
                                       prepare_records, sha, wordpieces)


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--preview', action='store_true', help='Check cached-tokenizer chunks without creating an index.')
    args = parser.parse_args()
    repo = args.repo.resolve()
    _, config = parents(repo)
    tokenizer = load_tokenizer(repo, config)
    records, config, fingerprint = prepare_records(repo, tokenizer)
    cisa_parents = {r['chunk']['parent_extraction_chunk_id'] for r in records if r['source_kind'] == 'cisa'}
    reference_docs = {r['chunk']['doc_id'] for r in records if r['source_kind'] == 'attack'}
    print(f'ThreatWeave development text index: {len(cisa_parents)} CISA scopes; {len(reference_docs)} ATT&CK references; {len(records)} retrieval chunks.', flush=True)
    print(f'Maximum embedding input: {max(r["wordpiece_count"] for r in records)} WordPieces; {max(len(r["embedding_text"]) for r in records)} characters.', flush=True)
    if args.preview:
        print('PREVIEW PASSED: Exact source spans and configured input limits checked; no index written.')
        return 0
    import numpy as np
    import chromadb
    from chromadb.config import Settings
    output = repo/'work/text_index_runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    summary = {'purpose': 'development_text_index', 'status': 'started', 'fingerprint': fingerprint,
               'development_scope':config['development_scope'],
               'cisa_scope_count': len(cisa_parents), 'attack_reference_count': len(reference_docs),
               'chunk_count': len(records), 'corpus_version': config['corpus_version'],
               'embedding': config['text_embedding'], 'chunking': config['chunking'],
               'packages': {p: importlib.metadata.version(p) for p in
                   ['sentence-transformers', 'transformers', 'torch', 'numpy', 'chromadb']}}
    save(output/'index_receipt.json', summary)
    try:
        model = load_model(repo, config)
        special_tokens = tokenizer.num_special_tokens_to_add(pair=False)
        if max(r['wordpiece_count'] for r in records)+special_tokens > model.max_seq_length:
            raise ValueError('Embedding inputs exceed the model sequence limit; indexing cancelled.')
        print('Embedding the source chunks using the cached MiniLM model...', flush=True)
        vectors = model.encode([r['embedding_text'] for r in records], normalize_embeddings=True,
                               convert_to_numpy=True, show_progress_bar=False)
        if (vectors.shape != (len(records), 384) or not np.isfinite(vectors).all()
                or not np.allclose(np.linalg.norm(vectors, axis=1), 1, atol=1e-5)):
            raise ValueError('Invalid embedding shape, values or normalization.')
        name = 'threatweave_text_dev_'+fingerprint[:16]
        store = repo/'work/chroma'
        client = chromadb.PersistentClient(path=str(store), settings=Settings(anonymized_telemetry=False))
        expected_metadata = {'hnsw:space': 'cosine', 'index_fingerprint': fingerprint,
                             'model_revision': config['text_embedding']['revision'], 'dimension': 384}
        collection = client.get_or_create_collection(name, embedding_function=None, metadata=expected_metadata)
        if any(collection.metadata.get(k) != v for k, v in expected_metadata.items()):
            raise ValueError('Existing collection has conflicting configuration.')
        ids = [r['chunk']['chunk_id'] for r in records]
        expected_ids = set(ids)
        if len(expected_ids) != len(ids):
            raise ValueError('Duplicate retrieval-chunk identities.')
        previous = collection.get(include=['documents', 'metadatas'])
        by_id = {r['chunk']['chunk_id']: r for r in records}
        for identifier, document, meta in zip(previous['ids'], previous['documents'], previous['metadatas']):
            if identifier not in by_id or document != by_id[identifier]['embedding_text'] or meta != metadata(by_id[identifier]):
                raise ValueError('Existing collection contains unexpected or altered source records.')
        collection.upsert(ids=ids, documents=[r['embedding_text'] for r in records],
                          metadatas=[metadata(r) for r in records], embeddings=vectors.tolist())
        stored = collection.get(include=['documents', 'metadatas', 'embeddings'])
        if set(stored['ids']) != expected_ids or collection.count() != len(records):
            raise ValueError('Stored chunk identities differ from the source manifest.')
        for identifier, text, meta, vector in zip(stored['ids'], stored['documents'], stored['metadatas'], stored['embeddings']):
            if text != by_id[identifier]['embedding_text'] or meta != metadata(by_id[identifier]):
                raise ValueError('Stored chunk text or provenance differs from the source manifest.')
            if len(vector) != 384 or not np.isfinite(vector).all() or not np.isclose(np.linalg.norm(vector), 1, atol=1e-5):
                raise ValueError('Stored vector failed validation.')
        index_folder = repo/'work/text_index'/fingerprint
        index_folder.mkdir(parents=True, exist_ok=True)
        records_path = index_folder/'records.json'
        if records_path.exists() and json.loads(records_path.read_text(encoding='utf-8')) != records:
            raise ValueError('Saved index manifest conflicts with the prepared sources.')
        save(records_path, records)
        summary.update(collection_name=name, chroma_path=str(store), records_path=str(records_path),
                       records_sha256=sha(records_path.read_text(encoding='utf-8')), smoke_queries=[])
        print(f'VERIFIED: {collection.count()} source chunks and 384-dimensional stored vectors.', flush=True)
        for number, question in enumerate(DEMO_QUESTIONS, 1):
            if wordpieces(tokenizer, question)+special_tokens > model.max_seq_length:
                raise ValueError('Smoke question exceeds the embedding sequence limit.')
            query = model.encode([question], normalize_embeddings=True, convert_to_numpy=True)
            result = collection.query(query_embeddings=query.tolist(), n_results=min(config['retrieval']['text_candidates'], len(records)), include=['distances'])
            hits = [{'rank': rank, 'cosine_distance': distance, 'record': by_id[identifier]}
                    for rank, (identifier, distance) in enumerate(zip(result['ids'][0], result['distances'][0]), 1)]
            if not hits:
                raise ValueError('The populated text collection returned no matches.')
            summary['smoke_queries'].append({'question': question, 'hits': hits})
            print(f'[{number}/3] Top text match: {hits[0]["record"]["chunk"]["parent_extraction_chunk_id"]}', flush=True)
        summary.update(status='ready', verified_chunk_count=collection.count(),
                       note='Development text index and retrieval smoke checks; no LLM answers or benchmark scores.')
        save(index_folder/'manifest.json', {k: summary[k] for k in ['fingerprint', 'collection_name',
            'chroma_path', 'records_path', 'records_sha256', 'embedding', 'chunking', 'corpus_version', 'packages', 'development_scope']})
        code = 0
    except Exception as exc:
        summary.update(status='failed', error=f'{type(exc).__name__}: {exc}')
        print('INDEX FAILED: '+summary['error'], flush=True)
        code = 1
    summary['finished_at'] = datetime.now(timezone.utc).isoformat()
    save(output/'index_receipt.json', summary)
    lines = ['# Development text-index run', '', 'Status: '+summary['status'], '',
             f'CISA source scopes: {len(cisa_parents)}; ATT&CK references: {len(reference_docs)}; retrieval chunks: {len(records)}.',
             '', 'Source-only development index. Retrieval smoke checks are not answer-quality measurements.',
             'Inherited headings retain separate exact document spans; child chunks preserve parent IDs.',
             '', 'Index fingerprint: `'+fingerprint+'`', '']
    for item in summary.get('smoke_queries', []):
        lines.extend(['## Retrieval smoke question', '', item['question'], ''])
        for hit in item['hits']:
            r, c = hit['record'], hit['record']['chunk']
            lines.append(f'- Rank {hit["rank"]}: {r["source_kind"]} / {c["doc_id"]} / {c["start"]}:{c["end"]}; cosine distance {hit["cosine_distance"]:.4f}; parent `{c["parent_extraction_chunk_id"]}`.')
        lines.append('')
    if summary.get('error'):
        lines.extend(['Error: '+summary['error'], ''])
    review = repo/'docs'/('ThreatWeave_text_index_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'Saved records: {output}\nSaved review document: {review}', flush=True)
    if code == 0:
        print('READY: Development text index built and retrieval smoke checks passed.', flush=True)
    return code


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}')
        sys.exit(1)
