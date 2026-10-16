"""Validate a pinned development review and prepare only its supported predictions."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from extraction.corpus_pilot import aggregate_candidates, configuration, digest, read_prepared
from extraction.llama_tokenizer import sha256_file
from extraction.source_choices import ACTOR, IDENTIFIER, make_prompt, validate_output
from graph.development_ingestion import prepare_records
from schemas import ExtractionBatch

REVIEW_FILE = 'docs/ThreatWeave_corpus_pilot_v2_6_review.json'


def check_decisions(decisions, batch):
    """Every generated relationship needs exactly one explicit development disposition."""
    if (len(decisions) != len(batch.relations)
            or {d.get('relation_index') for d in decisions} != set(range(len(batch.relations)))):
        raise ValueError('Review must cover every candidate exactly once.')
    ordered = sorted(decisions, key=lambda d: d['relation_index'])
    if any(d.get('disposition') not in {'supported', 'review', 'reject'}
           or not isinstance(d.get('reason'), str) or not d['reason'].strip() for d in ordered):
        raise ValueError('Each review disposition needs a source-review reason.')
    return [d['relation_index'] for d in ordered if d['disposition'] == 'supported']


def supported_batch(batch, selected):
    relations = [batch.relations[i] for i in selected]
    used = {key for relation in relations for key in [relation.head, relation.tail]}
    return ExtractionBatch(entities=[entity for entity in batch.entities if entity.local_id in used],
                           relations=relations)


def add_review_provenance(prepared, alignments, selected, review, review_hash):
    for assertion, index in zip(prepared['assertions'], selected):
        aligned = alignments[index]
        decision = next(d for d in review['decisions'] if d['relation_index'] == index)
        assertion.update(extraction_method='LLM_source_evidence_selectors',
                         source_review_sha256=review_hash,
                         source_review_disposition='supported', source_review_reason=decision['reason'],
                         source_relation_index=index,
                         selected_units_json=json.dumps(aligned['selected_units'], ensure_ascii=False),
                         selected_unit_ids_json=json.dumps(aligned['selected_unit_ids']),
                         selected_context_spans_json=json.dumps(aligned['context_spans'], ensure_ascii=False),
                         source_review_flags_json=json.dumps(aligned['review_flags']))
    # Occurrences belong to selected source support, not the first unrelated
    # spelling elsewhere in a long source window (notably actor/software names).
    for mention in prepared['mentions']:
        name = mention['evidence_text']
        supports = [alignments[i] for assertion, i in zip(prepared['assertions'], selected)
                    if mention['canonical_id'] in {assertion['head_id'], assertion['tail_id']}]
        spans = [dict(unit, start=prepared['chunk']['start']+unit['start'])
                 for support in supports for unit in support['selected_units']]
        spans += [span for support in supports for span in support['context_spans']]
        offsets = []
        is_software = next(e['type'] for e in prepared['entities'] if e['canonical_id'] == mention['canonical_id']) == 'Software'
        for span in spans:
            text = ACTOR.sub(lambda match:' '*len(match.group()), span['text']) if is_software else span['text']
            matches = (IDENTIFIER.finditer(text) if IDENTIFIER.fullmatch(name)
                       else re.finditer(r'(?<!\w)'+re.escape(name)+r'(?!\w)', text))
            offsets += [span['start']+match.start() for match in matches if match.group() == name]
        if not offsets:
            raise ValueError('Reviewed endpoint lacks a selected source occurrence.')
        start = offsets[0]
        mention.update(evidence_start=start, evidence_end=start+len(name))


def prepare(repo):
    repo = Path(repo).resolve()
    review_path = repo/REVIEW_FILE
    review = json.loads(review_path.read_text(encoding='utf-8'))
    if (review.get('purpose') != 'AI_assisted_development_source_review'
            or review.get('human_review_status') != 'pending'
            or not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}', review.get('run', ''))):
        raise ValueError('Invalid development review identity.')
    run = repo/'work/corpus_extraction_pilot'/review['run']
    if sha256_file(run/'summary.json') != review['summary_sha256']:
        raise ValueError('Reviewed extraction summary changed.')
    summary = json.loads((run/'summary.json').read_text(encoding='utf-8'))
    items, config, catalog, attack_hash, identity, prepared_run = read_prepared(repo)
    settings_hash = digest(configuration(config, identity, attack_hash))
    if (summary.get('status') != 'processed' or summary.get('graph_writes') is not False
            or summary.get('configuration_hash') != settings_hash
            or review.get('configuration_hash') != settings_hash
            or Path(summary['prepared_run']).resolve() != prepared_run
            or len(summary['items']) != len(items)):
        raise ValueError('Reviewed source/model/extraction configuration changed.')
    rows = review['windows']
    if len(rows) != len(items) or len({r['folder'] for r in rows}) != len(items):
        raise ValueError('Review must cover each frozen pilot window once.')
    prepared, original, excluded = [], [], []
    review_hash = sha256_file(review_path)
    for item, record in zip(items, summary['items']):
        name = record['folder']
        if not re.fullmatch(r'\d{2}', name) or record['scope_id'] != item['chunk'].chunk_id:
            raise ValueError('Recorded extraction scope differs from frozen pilot selection.')
        row = next((r for r in rows if r['folder'] == name), None)
        if row is None or row['scope_id'] != record['scope_id']:
            raise ValueError('Missing reviewed source window.')
        folder = run/name
        for filename, expected in row['file_sha256'].items():
            if filename not in {'candidate_extraction.json', 'quote_alignment.json', 'raw_extraction.json'}:
                raise ValueError('Unexpected review attachment.')
            path = folder/filename
            if filename == 'raw_extraction.json':
                path = folder/f"raw_extraction_{record['attempts'][-1]['attempt']}.json"
            if sha256_file(path) != expected:
                raise ValueError('Reviewed candidate/evidence/model output changed.')
        if set(row['file_sha256']) != {'candidate_extraction.json','quote_alignment.json','raw_extraction.json'}:
            raise ValueError('Review attachments are incomplete.')
        def read(filename):
            return json.loads((folder/filename).read_text(encoding='utf-8'))
        if (read('chunk.json') != item['chunk'].model_dump(mode='json')
                or read('source_metadata.json') != item['preparation']):
            raise ValueError('Reviewed source window or metadata changed.')
        system, prompt, schema, index = make_prompt(item, catalog)
        if ((folder/'system_prompt.txt').read_text(encoding='utf-8') != system
                or (folder/'user_prompt.txt').read_text(encoding='utf-8') != prompt
                or read('output_schema.json') != schema
                or digest({'system':system,'prompt':prompt,'schema':schema}) != record['prompt_hash']):
            raise ValueError('Recorded extraction prompt/schema changed.')
        saved_index = dict(index, captions={key:value.model_dump(mode='json') for key,value in index['captions'].items()})
        if read('source_choices.json') != saved_index:
            raise ValueError('Recorded source choices changed.')
        attempt = record['attempts'][-1]
        raw = (folder/f"raw_extraction_{attempt['attempt']}.json").read_text(encoding='utf-8')
        response = read(f"ollama_response_{attempt['attempt']}.json")
        if (attempt.get('validation_error') or attempt.get('error') or attempt.get('http_status') != 200
                or response.get('response') != raw or response.get('done') is not True
                or response.get('done_reason') != 'stop'):
            raise ValueError('Reviewed output is not a completed validated model reply.')
        batch, resolutions, alignments = validate_output(raw, item, catalog, index)
        if (batch.model_dump(mode='json') != read('candidate_extraction.json')
                or resolutions != read('identity_resolution.json') or alignments != read('quote_alignment.json')):
            raise ValueError('Reconstructed candidate/evidence/identity differs from saved output.')
        original.append((item, batch, resolutions, alignments))
        selected = check_decisions(row['decisions'], batch)
        for d in row['decisions']:
            if d['disposition'] != 'supported':
                excluded.append(dict(d, folder=name, scope_id=record['scope_id']))
        if selected:
            result = prepare_records(item, supported_batch(batch, selected), catalog, summary, record, raw, run,
                                     'AI_assisted_pinned_candidate_source_review_and_literal_identity_validation')
            add_review_provenance(result, alignments, selected, row, review_hash)
            prepared.append(result)
    facts, counts = aggregate_candidates(original)
    if (facts != json.loads((run/'unique_candidate_facts.json').read_text(encoding='utf-8'))
            or any(summary.get(k) != v for k,v in counts.items())):
        raise ValueError('Recorded candidate aggregation changed.')
    actual_count = sum(len(item['assertions']) for item in prepared)
    if not actual_count or actual_count != review['supported_count'] or len(excluded) != review['excluded_count']:
        raise ValueError('Reviewed import selection counts differ.')
    return {'items':prepared, 'excluded_candidates':excluded,
            'prepared_at':datetime.now(timezone.utc).isoformat(), 'attack_release':'17.1',
            'attack_snapshot_hash':attack_hash, 'model_digest':summary['model_digest'],
            'human_review_status':'pending', 'review_manifest':str(review_path),
            'review_manifest_sha256':review_hash, 'extraction_run':str(run),
            'configuration_hash':settings_hash}
