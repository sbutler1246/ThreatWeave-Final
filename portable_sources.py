"""Load the complete, hash-bound accepted development scope on any checkout.

Original run paths in assertion properties remain provenance strings. They are
never followed. This adapter avoids requiring historical extraction working folders.
"""
import hashlib
import json
from pathlib import Path


def load_bundle(repo):
    repo = Path(repo).resolve()
    folder = repo / 'data/portable'
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    raw = (folder / 'development_sources.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != manifest['files_sha256']['development_sources.json']:
        raise ValueError('Portable source bundle checksum changed.')
    bundle = json.loads(raw)
    if bundle['version'] != 1:
        raise ValueError('Unsupported portable source bundle.')
    # Bind the bundle to the frozen project config rather than accepting another model/prompt policy.
    config = json.loads((repo / 'config.json').read_text(encoding='utf-8'))
    if config != {k: v for k, v in bundle['config'].items() if k != 'development_scope'}:
        raise ValueError('Portable sources belong to a different configuration.')
    return bundle


def source_profiles(repo, **options):
    if any(value is False for value in options.values()):
        raise ValueError('Portable scope includes the complete development scope.')
    from schemas import Document, Chunk
    bundle = load_bundle(repo)
    profiles = {}
    for key, value in bundle['profiles'].items():
        doc = Document.model_validate(value['document'])
        chunk = Chunk.model_validate(value['chunk'])
        if hashlib.sha256(doc.text.encode()).hexdigest() != doc.content_hash:
            raise ValueError('Portable source document checksum differs.')
        if doc.text[chunk.start:chunk.end] != chunk.text or chunk.doc_id != doc.doc_id:
            raise ValueError('Portable chunk/source binding differs.')
        for context in chunk.inherited_context:
            if doc.text[context.start:context.end] != context.text:
                raise ValueError('Portable inherited source context differs.')
        profiles[key] = dict(value, document=doc, chunk=chunk,
            allowed_triples={tuple(t) for t in value['allowed_triples']})
    identity = {'profiles': {key: {'source_hash': p['document'].content_hash,
        'triples': sorted(p['allowed_triples']), 'assertions': p.get('accepted_assertions', {})}
        for key, p in sorted(profiles.items())}, 'reference_ids': sorted(bundle['references'])}
    fingerprint = hashlib.sha256(json.dumps(identity, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    if fingerprint != bundle['config']['development_scope']['sha256']:
        raise ValueError('Portable scope differs from the original accepted scope.')
    return profiles, bundle['references'], bundle['entities'], bundle['config']


def install():
    """Install the explicit portable source provider BEFORE importing the application.

    The original retrieval, generation and evidence verification code stays intact.
    Fresh indexes bind to the same development scope fingerprint.
    """
    import graph.development_retrieval as graph
    graph.source_profiles = source_profiles


def check(repo):
    from graph.development_retrieval import DevelopmentGraphRetriever
    from graph.development_projection import freeze_projection
    bundle = load_bundle(repo)
    install()
    retriever = DevelopmentGraphRetriever(Path(repo).resolve())
    records, edges = [], {}
    for item in bundle['items']:
        doc, chunk = item['document'], item['chunk']
        for assertion in item['assertions']:
            signature = assertion['head_id'], assertion['predicate'], assertion['tail_id']
            record = dict(assertion=assertion, document=doc, chunk=chunk)
            if retriever._verify_record(record, *signature) is None:
                raise ValueError('Portable accepted assertion is outside its scope.')
            records.append(record)
            edges.setdefault(signature, dict(head=bundle['entities'][signature[0]], tail=bundle['entities'][signature[2]],
                predicate=signature[1], assertion_ids=[]))['assertion_ids'].append(assertion['assertion_id'])
    for reference in bundle['references'].values():
        assertion = reference['assertion']
        signature = assertion['head_id'], assertion['predicate'], assertion['tail_id']
        record = {key: reference[key] for key in ('assertion', 'document', 'chunk')}
        if retriever._verify_record(record, *signature) is None:
            raise ValueError('Portable ATT&CK reference is outside its scope.')
        records.append(record)
        edges.setdefault(signature, dict(head=bundle['entities'][signature[0]], tail=bundle['entities'][signature[2]],
            predicate=signature[1], assertion_ids=[]))['assertion_ids'].append(assertion['assertion_id'])
    projection, fingerprint = freeze_projection(retriever, list(edges.values()), records)
    return bundle, projection, fingerprint
