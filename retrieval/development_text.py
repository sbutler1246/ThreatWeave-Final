"""Development source chunks for MiniLM; no graph facts or answer labels are indexed."""
import hashlib
import json
import os

from graph.development_retrieval import source_profiles
from schemas import Chunk, Document, SourceContext

VERSION = 'development-text-chunks-v2-reviewed-scopes'


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def configure_cache(repo):
    os.environ['HF_HOME'] = str(repo/'work/model_cache/huggingface')
    os.environ['TORCH_HOME'] = str(repo/'work/model_cache/torch')
    os.environ['HF_HUB_DISABLE_TELEMETRY'] = '1'
    os.environ['HF_HUB_OFFLINE'] = '1'
    os.environ['ANONYMIZED_TELEMETRY'] = 'False'
    return str(repo/'work/model_cache/sentence_transformers')


def load_tokenizer(repo, config):
    cache = configure_cache(repo)
    from transformers import AutoTokenizer
    return AutoTokenizer.from_pretrained(config['text_embedding']['model'],
        revision=config['text_embedding']['revision'], cache_dir=cache,
        local_files_only=True, trust_remote_code=False, use_fast=True)


def load_model(repo, config):
    cache = configure_cache(repo)
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(config['text_embedding']['model'],
        revision=config['text_embedding']['revision'], cache_folder=cache,
        local_files_only=True, trust_remote_code=False, device='cpu')
    if model.get_sentence_embedding_dimension() != config['text_embedding']['dimension']:
        raise ValueError('Embedding dimension differs from the frozen configuration.')
    return model


def parents(repo, *, include_corpus_batch=True, include_corpus_extension=True):
    profiles, references, _, config = source_profiles(repo, include_corpus_batch=include_corpus_batch,
                                                     include_corpus_extension=include_corpus_extension)
    selected = []
    for key in sorted(profiles):
        profile = profiles[key]
        selected.append((profile['document'], profile['chunk'], {}))
    for key in sorted(references):
        record = references[key]
        raw_doc = record['document']
        doc = Document.model_validate({k: v for k, v in raw_doc.items() if k in Document.model_fields})
        raw_chunk = record['chunk']
        chunk = Chunk.model_validate({k: v for k, v in raw_chunk.items() if k in Chunk.model_fields})
        # Exact normalized identity fields accompany the exact STIX description.
        # Verbose STIX metadata stays in the provenance log, outside embedding text.
        header_end = doc.text.index('\nSTIX relationship_type:')
        chunk.inherited_context = [SourceContext(start=0, end=header_end, text=doc.text[:header_end])]
        provenance = {k: raw_doc[k] for k in ['source_snapshot_sha256',
            'source_stix_relationship_id', 'attack_release', 'normalization']}
        selected.append((doc, chunk, provenance))
    return selected, config


def embedding_text(contexts, body):
    prefix = '\n'.join(context.text for context in contexts)
    return prefix+'\n\n'+body if prefix else body


def wordpieces(tokenizer, text):
    return len(tokenizer(text, add_special_tokens=False, truncation=False, verbose=False)['input_ids'])


def split_parent(document, parent, tokenizer, settings):
    """Keep exact offsets, with bounded input including inherited source context."""
    if document.doc_id != parent.doc_id or sha(document.text) != document.content_hash:
        raise ValueError('Parent document identity or checksum mismatch.')
    if not 0 <= parent.start < parent.end <= len(document.text) or document.text[parent.start:parent.end] != parent.text:
        raise ValueError('Parent text differs from its document span.')
    for context in parent.inherited_context:
        if not 0 <= context.start < context.end <= len(document.text) or document.text[context.start:context.end] != context.text:
            raise ValueError('Inherited context differs from its document span.')
    ceiling = settings['retrieval_minilm_wordpiece_ceiling']
    character_ceiling = settings['retrieval_character_ceiling']
    overlap = settings['retrieval_overlap_wordpieces']
    if ceiling <= 0 or character_ceiling <= 0 or not 0 <= overlap < ceiling:
        raise ValueError('Invalid retrieval chunk limits.')
    if not getattr(tokenizer, 'is_fast', False):
        raise ValueError('A fast tokenizer is required for exact character offsets.')
    offsets = tokenizer(parent.text, add_special_tokens=False, truncation=False,
                        return_offsets_mapping=True, verbose=False)['offset_mapping']
    offsets = [(a, b) for a, b in offsets if b > a]
    if not offsets:
        raise ValueError('Source parent contains no WordPiece tokens.')
    prefix = embedding_text(parent.inherited_context, '')
    if len(prefix) >= character_ceiling or wordpieces(tokenizer, prefix) >= ceiling:
        raise ValueError('Inherited context leaves no room for source text.')
    children, i = [], 0
    while i < len(offsets):
        start = 0 if i == 0 else offsets[i][0]
        j = i+1
        while j < len(offsets) and offsets[j][0]-start+len(prefix) <= character_ceiling:
            j += 1
        # Include whitespace up to the next token, so offsets cover the parent.
        while j > i:
            end = offsets[j][0] if j < len(offsets) else len(parent.text)
            text = parent.text[start:end]
            input_text = embedding_text(parent.inherited_context, text)
            count = wordpieces(tokenizer, input_text)
            if len(input_text) <= character_ceiling and count <= ceiling:
                break
            j -= 1
        if j == i:
            raise ValueError('A source token cannot fit with its inherited context.')
        child_start, child_end = parent.start+start, parent.start+end
        identifier = 'retrieval:'+sha('\x1f'.join([VERSION, parent.chunk_id,
                                                  str(child_start), str(child_end)]))
        child = Chunk(chunk_id=identifier, doc_id=parent.doc_id, start=child_start,
            end=child_end, text=text, inherited_context=parent.inherited_context,
            role='retrieval', parent_extraction_chunk_id=parent.chunk_id)
        children.append({'chunk': child.model_dump(mode='json'), 'embedding_text': input_text,
                         'wordpiece_count': count})
        if j == len(offsets):
            break
        i = max(i+1, j-overlap)
    return children


def prepare_records(repo, tokenizer):
    selected, config = parents(repo)
    records = []
    for doc, parent, provenance in selected:
        for record in split_parent(doc, parent, tokenizer, config['chunking']):
            record.update(source_kind=doc.source, source_url=str(doc.source_url),
                          source_hash=doc.content_hash, title=doc.title, provenance=provenance)
            records.append(record)
    payload = {'version': VERSION, 'corpus_version': config['corpus_version'],
               'development_scope':config['development_scope'],
               'embedding': config['text_embedding'], 'chunking': config['chunking'], 'records': records}
    fingerprint = sha(json.dumps(payload, sort_keys=True, ensure_ascii=False))
    return records, config, fingerprint


def metadata(record):
    chunk = record['chunk']
    return {'doc_id': chunk['doc_id'], 'chunk_id': chunk['chunk_id'],
            'parent_extraction_chunk_id': chunk['parent_extraction_chunk_id'],
            'start': chunk['start'], 'end': chunk['end'], 'source_kind': record['source_kind'],
            'source_url': record['source_url'], 'source_hash': record['source_hash'],
            'record_sha256': sha(json.dumps(record, sort_keys=True, ensure_ascii=False))}
