"""Validate schema and literal evidence; semantic support still needs review."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from schemas import Chunk, Document, ExtractionBatch

def validate_chunk_document(chunk: Chunk, document: Document):
    if chunk.doc_id!=document.doc_id or document.text[chunk.start:chunk.end]!=chunk.text:
        raise ValueError('chunk must match frozen parent document')
    for context in chunk.inherited_context:
        if context.end>len(document.text) or document.text[context.start:context.end]!=context.text:
            raise ValueError('inherited context does not match parent document')
    return chunk

def parse_extraction(raw: str, chunk: Chunk) -> ExtractionBatch:
    batch=ExtractionBatch.model_validate_json(raw)
    for relation in batch.relations:
        span=relation.evidence
        if span.end>len(chunk.text) or chunk.text[span.start:span.end]!=span.quote:
            raise ValueError('supporting quote does not match supplied chunk')
    return batch

def partition_review(batch: ExtractionBatch, threshold: float=0.80):
    """Confidence gates review only; it cannot establish semantic truth."""
    accepted=[]; review=[]
    for r in batch.relations:
        (review if r.confidence is None or r.confidence<threshold else accepted).append(r)
    return accepted,review

if __name__=='__main__':
    chunk=Chunk.model_validate_json(Path(sys.argv[1]).read_text(encoding='utf-8'))
    result=parse_extraction(Path(sys.argv[2]).read_text(encoding='utf-8'),chunk)
    print(result.model_dump_json(indent=2))
