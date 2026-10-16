"""Source-only, token-measured extraction windows for a five-report pilot."""
import hashlib
import json
import re
from pathlib import Path

from extraction.llama_tokenizer import MODEL_DIGEST, restore_llama3_decoder, sha256_file, validate_roundtrip
from extraction.parser import validate_chunk_document
from schemas import Chunk, Document, SourceContext

PILOT_DOCUMENTS = ('AA23-136A', 'AA23-319A', 'AA23-320A', 'AA23-353A', 'AA24-060A')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode('utf-8')).hexdigest()


def load_verified_tokenizer(repo):
    from importlib.metadata import version
    from tokenizers import Tokenizer
    root = (repo/'work/extraction_tokenizer').resolve()
    pointer = json.loads((root/'current.json').read_text(encoding='utf-8'))
    if not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}', pointer['run']):
        raise ValueError('Invalid source-tokenizer run pointer.')
    folder = root/pointer['run']
    summary = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
    if (summary.get('status') != 'ready' or summary.get('model_digest') != MODEL_DIGEST
            or pointer.get('model_digest') != MODEL_DIGEST):
        raise ValueError('A ready tokenizer for the recorded Llama model is required.')
    probes = summary.get('probes', [])
    if len(probes) != 3 or any(p.get('status') != 'passed'
            or p.get('reported_raw_prompt_tokens') != p.get('expected_raw_prompt_tokens') for p in probes):
        raise ValueError('Tokenizer runtime count probes did not all pass.')
    if version('tokenizers') != summary['packages']['tokenizers']:
        raise ValueError('Tokenizers package changed since the verified source-count probes.')
    if summary.get('tokenizer_file') != 'tokenizer.json':
        raise ValueError('Unexpected tokenizer artifact filename.')
    artifact = folder/'tokenizer.json'
    actual = sha256_file(artifact)
    if actual != summary.get('tokenizer_sha256') or actual != pointer.get('tokenizer_sha256'):
        raise ValueError('Verified source-tokenizer artifact checksum changed.')
    tokenizer = Tokenizer.from_file(str(artifact))
    # Preserve the verified artifact. Correct only its legacy decoder in memory;
    # vocabulary, merges, splitting, token IDs and verified counts are unchanged.
    restore_llama3_decoder(tokenizer)
    derived_hash = hashlib.sha256(tokenizer.to_str().encode('utf-8')).hexdigest()
    return tokenizer, {
        'run': pointer['run'], 'sha256': actual, 'model_digest': MODEL_DIGEST,
        'tokenizers_version': version('tokenizers'),
        'decoder_policy': 'llama3-bytelevel-v1', 'derived_tokenizer_sha256': derived_hash,
    }


def technical_bounds(text):
    starts = list(re.finditer(r'(?im)^technical details[ \t]*$', text))
    if len(starts) != 1:
        raise ValueError('Expected one standalone Technical Details heading.')
    heading = starts[0]
    ends = list(re.finditer(r'(?im)^mitigations[ \t]*$', text[heading.end():]))
    if not ends:
        raise ValueError('No standalone Mitigations heading follows Technical Details.')
    start, end = heading.end(), heading.end()+ends[0].start()
    if not text[start:end].strip():
        raise ValueError('The technical section is empty.')
    return start, end, SourceContext(start=heading.start(), end=heading.end(), text=heading.group())


def contexts_for(document, heading, start):
    contexts = [heading]
    # Preserve the title as a source span, not a manufactured actor attribution.
    title = document.text.find(document.title)
    if title >= 0 and title < heading.start:
        contexts.insert(0, SourceContext(start=title, end=title+len(document.title), text=document.title))
    captions = list(re.finditer(r'(?m)^Table \d+[^\n]*', document.text[heading.end:start]))
    if captions:
        caption = captions[-1]
        begin, end = heading.end+caption.start(), heading.end+caption.end()
        if start-begin <= 2000:
            contexts.append(SourceContext(start=begin, end=end, text=document.text[begin:end]))
    return contexts


def split_section(document, tokenizer, start, end, heading, target=500, minimum=400, maximum=600, overlap=60):
    if not (0 < minimum <= target <= maximum and 0 <= overlap < minimum):
        raise ValueError('Invalid extraction token/overlap limits.')
    if not 0 <= start < end <= len(document.text):
        raise ValueError('Invalid extraction section offsets.')
    records, cursor = [], start
    count = lambda text: len(validate_roundtrip(tokenizer, text))
    while cursor < end:
        tail = document.text[cursor:end]
        encoding = tokenizer.encode(tail, add_special_tokens=False)
        tail_count = len(encoding.ids)
        terminal_reanchored = False
        if tail_count <= maximum:
            stop = end
            if tail_count < minimum and records:
                previous_start = records[-1]['chunk']['start']
                terminal = tokenizer.encode(document.text[previous_start:end], add_special_tokens=False)
                position = max(0, len(terminal.ids)-target)
                proposed = previous_start+terminal.offsets[position][0]
                if proposed <= previous_start or proposed > cursor:
                    raise ValueError('Unable to reanchor a final window without a source gap.')
                cursor, terminal_reanchored = proposed, True
        else:
            stop = cursor+encoding.offsets[target-1][1]
            lower = encoding.offsets[minimum-1][1]
            upper = encoding.offsets[maximum-1][1]
            candidates = [m.end() for m in re.finditer('\n', tail[lower:upper])]
            candidates = [lower+position for position in candidates]
            choices = []
            for position in candidates:
                measured = count(tail[:position])
                if minimum <= measured <= maximum:
                    choices.append((abs(measured-target), position))
            if choices:
                stop = cursor+min(choices)[1]
        if stop <= cursor:
            raise ValueError('Tokenizer offsets do not advance the source window.')
        body = document.text[cursor:stop]
        measured = count(body)
        if measured > maximum or (measured < minimum and end-start > len(body)):
            raise ValueError('A measured source window is outside the extraction limits.')
        chunk = Chunk(chunk_id=f'{document.doc_id}:development:llama{target}:{cursor}:{stop}',
                      doc_id=document.doc_id, start=cursor, end=stop, text=body,
                      inherited_context=contexts_for(document, heading, cursor))
        validate_chunk_document(chunk, document)
        overlap_count = count(document.text[cursor:records[-1]['chunk']['end']]) if records else 0
        context_count = count('\n'.join(c.text for c in chunk.inherited_context))
        records.append({'chunk': chunk.model_dump(mode='json'), 'source_tokens': measured,
                        'inherited_context_tokens': context_count, 'overlap_with_previous_tokens': overlap_count,
                        'terminal_reanchored': terminal_reanchored, 'short_section': measured < minimum,
                        'source_text_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest()})
        if stop == end:
            break
        body_encoding = tokenizer.encode(body, add_special_tokens=False)
        next_cursor = stop if overlap == 0 else cursor+body_encoding.offsets[max(0, len(body_encoding.ids)-overlap)][0]
        if not cursor < next_cursor <= stop:
            raise ValueError('Overlap must advance the source window without leaving gaps.')
        cursor = next_cursor
    return records


def prepare(repo):
    repo = repo.resolve()
    tokenizer, identity = load_verified_tokenizer(repo)
    manifest = json.loads((repo/'benchmarks/corpus_manifest.json').read_text(encoding='utf-8'))
    split = json.loads((repo/'benchmarks/split_manifest.json').read_text(encoding='utf-8'))
    blocked = {scope.split(':')[0] for scope in split['held_out_evidence_scopes']}
    if blocked.intersection(PILOT_DOCUMENTS):
        raise ValueError('A pilot document contains held-out evidence scopes.')
    config = json.loads((repo/'config.json').read_text(encoding='utf-8'))
    settings = config['chunking']
    params = {'target': settings['extraction_llama_token_target'],
              'minimum': settings['extraction_llama_token_range'][0],
              'maximum': settings['extraction_llama_token_range'][1],
              'overlap': settings['extraction_overlap_tokens']}
    all_records, documents = [], []
    catalog = {record['doc_id']: record for record in manifest['documents']}
    for doc_id in PILOT_DOCUMENTS:
        record = catalog[doc_id]
        text_path, raw_path = [(repo/record[key]).resolve() for key in ['text_file', 'raw_file']]
        if not all(path.is_relative_to(repo) for path in [text_path, raw_path]):
            raise ValueError('Frozen source path escapes the workspace.')
        text = text_path.read_text(encoding='utf-8')
        if (hashlib.sha256(text.encode('utf-8')).hexdigest() != record['normalized_sha256']
                or sha256_file(raw_path) != record['raw_sha256']):
            raise ValueError('Frozen pilot source checksum changed: '+doc_id)
        document = Document(doc_id=doc_id, title=record['title'], source_url=record['source_url'],
                            publication_date=record.get('release_date'), text=text,
                            content_hash=record['normalized_sha256'])
        start, end, heading = technical_bounds(text)
        records = split_section(document, tokenizer, start, end, heading, **params)
        if len(records) < 2:
            raise ValueError('Each pilot report must provide two overlapping windows.')
        for number, item in enumerate(records):
            item.update(doc_id=doc_id, source_url=str(document.source_url), source_hash=document.content_hash,
                        pilot_selected=number < 2)
        all_records.extend(records)
        documents.append({'doc_id': doc_id, 'title': document.title, 'source_url': str(document.source_url),
                          'source_hash': document.content_hash, 'raw_sha256': record['raw_sha256'],
                          'technical_start': start, 'technical_end': end, 'chunk_count': len(records),
                          'pilot_chunk_ids': [r['chunk']['chunk_id'] for r in records[:2]],
                          'short_sections': sum(r['short_section'] for r in records)})
    identity_data = {'purpose': 'five_report_source_chunk_preparation', 'corpus_version': config['corpus_version'],
                     'tokenizer': identity, 'parameters': params, 'documents': documents,
                     'records_sha256': digest(all_records),
                     'selection': 'First two technical-section windows per report; no labels or reference answers.'}
    identity_data['fingerprint'] = digest(identity_data)
    return all_records, identity_data
