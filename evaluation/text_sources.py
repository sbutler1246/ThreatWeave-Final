"""Shared source-only evaluation chunks using the frozen MiniLM splitter."""
import json

from evaluation.corpus_scope import source_profiles
from retrieval.development_text import split_parent, sha
from schemas import Chunk, Document, SourceContext

VERSION = 'evaluation-shared-source-text-index-v1'


def parents(repo,*,scope=None):
    profiles,references,_,config = source_profiles(repo) if scope is None else scope
    selected = [(p['document'],p['chunk'],{}) for _,p in sorted(profiles.items())]
    for _,record in sorted(references.items()):
        raw_doc,raw_chunk = record['document'],record['chunk']
        doc = Document.model_validate({k:v for k,v in raw_doc.items() if k in Document.model_fields})
        chunk = Chunk.model_validate({k:v for k,v in raw_chunk.items() if k in Chunk.model_fields})
        header_end = doc.text.index('\nSTIX relationship_type:')
        chunk.inherited_context = [SourceContext(start=0,end=header_end,text=doc.text[:header_end])]
        provenance = {k:raw_doc[k] for k in ['source_snapshot_sha256','source_stix_relationship_id','attack_release','normalization']}
        selected.append((doc,chunk,provenance))
    return selected,config


def prepare_records(repo,tokenizer,*,selected=None,config=None):
    if selected is None:
        selected,config = parents(repo)
    if config is None or 'evaluation_scope' not in config:
        raise ValueError('Explicit shared evaluation scope is required.')
    records = []
    for doc,parent,provenance in selected:
        for record in split_parent(doc,parent,tokenizer,config['chunking']):
            record.update(source_kind=doc.source,source_url=str(doc.source_url),source_hash=doc.content_hash,
                          title=doc.title,provenance=provenance)
            records.append(record)
    payload = {'version':VERSION,'corpus_version':config['corpus_version'],
               'evaluation_scope':config['evaluation_scope'],'development_scope':config['development_scope'],
               'embedding':config['text_embedding'],'chunking':config['chunking'],'records':records}
    fingerprint = sha(json.dumps(payload,sort_keys=True,ensure_ascii=False))
    return records,config,fingerprint
