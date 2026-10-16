"""Offline, source-scoped evaluation of preserved pre-review extraction outputs.

Added after collection. Never changes labels, original outputs, indexes, or prompts.
"""
from __future__ import annotations

import hashlib
import json
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.score_triples import score as legacy_score


SUCCESS = {'candidates_ready_for_review', 'empty_extraction'}
LATEST = 'work/evaluation_corpus_extraction/20261016T041738Z-f6bd403c'
PROTOCOL = 'work/final_completion/extraction_scoring_protocol.json'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def norm(value):
    return ' '.join(unicodedata.normalize('NFKC', value).casefold().split())


def triple_key(row):
    return row['head_id'], row['predicate'], row['tail_id']


def measures(tp, fp, fn):
    precision = tp / (tp + fp) if tp + fp else None
    recall = tp / (tp + fn) if tp + fn else None
    f1 = None if precision is None or recall is None else (
        2 * precision * recall / (precision + recall) if precision + recall else 0.0)
    return dict(tp=tp, fp=fp, fn=fn, precision=precision, recall=recall, f1=f1,
                undefined_metrics=[name for name, value in [('precision', precision), ('recall', recall), ('f1', f1)] if value is None])


def canonical_endpoint(entity, resolution, reference, doc_id):
    """Exact scoring-only projection into frozen benchmark identity names."""
    system_id = resolution.get('canonical_id') or f"unresolved:{entity['type']}:{norm(entity['name'])}"
    if entity.get('attack_id'):
        return 'attack:' + entity['attack_id'], system_id, 'explicit_source_attack_id'
    matches = []
    for item in reference:
        if item['type'] != entity['type']:
            continue
        identifier = item['canonical_id']
        if identifier.startswith('local:') and not identifier.startswith('local:' + doc_id + ':'):
            continue
        names = [item['name'], item.get('source_name', ''), *item.get('aliases', [])]
        if norm(entity['name']) in {norm(name) for name in names if name}:
            matches.append(identifier)
    unique = set(matches)
    if len(unique) == 1:
        return next(iter(unique)), system_id, 'exact_frozen_benchmark_typed_name'
    return system_id, system_id, 'saved_resolution_or_unresolved_name'


def contains(scope, spans):
    return bool(spans) and all(scope['start'] <= start < end <= scope['end'] for start, end in spans)


def covered_length(start, end, spans):
    spans = sorted((max(start, a), min(end, b)) for a, b in spans if a < end and start < b)
    cursor, count = start, 0
    for a, b in spans:
        if b > max(a, cursor):
            count += b - max(a, cursor)
        cursor = max(cursor, b)
    return count


def load_gold(repo):
    gold = read(repo / 'benchmarks/gold_triples.json')
    reference = read(repo / 'benchmarks/entity_reference.json')
    manifest = read(repo / 'benchmarks/corpus_manifest.json')
    assert gold['annotation_scope_complete'] is True
    assert all(row['verified'] is True for row in gold['triples'])
    documents = {}
    for item in manifest['documents']:
        text = (repo / item['text_file']).read_text(encoding='utf-8')
        assert hashlib.sha256(text.encode()).hexdigest() == item['normalized_sha256']
        assert sha(repo / item['raw_file']) == item['raw_sha256']
        documents[item['doc_id']] = text
    scopes = {}
    expanded = []
    for row in gold['triples']:
        for support in [row, *row.get('additional_support', [])]:
            if support.get('verified') is not True:
                raise ValueError('Unverified additional support.')
            scope_id = support['chunk_id']
            assert scope_id in gold['annotation_scope']
            assert gold['scope_review'][scope_id]['complete'] is True
            start, end = support['document_start'], support['document_end']
            text = documents[support['doc_id']]
            assert text[start:end] == support['source_chunk_text'], row['id']
            evidence = support['evidence']
            assert support['source_chunk_text'][evidence['start']:evidence['end']] == evidence['quote']
            if scope_id not in scopes:
                scopes[scope_id] = dict(scope_id=scope_id, doc_id=support['doc_id'], start=start, end=end, text=text[start:end])
            else:
                assert (scopes[scope_id]['start'], scopes[scope_id]['end']) == (start, end)
            expanded.append(dict(gold_id=row['id'], head_id=row['head_id'], predicate=row['predicate'],
                                 tail_id=row['tail_id'], chunk_id=scope_id, doc_id=support['doc_id'], verified=True))
    assert set(scopes) == set(gold['annotation_scope'])
    return gold, reference, documents, scopes, expanded


def extract_occurrences(results, reference, documents, scopes):
    occurrences = []
    windows = []
    by_document = defaultdict(list)
    for scope in scopes.values():
        by_document[scope['doc_id']].append(scope)
    for item, value in results:
        chunk = item['chunk']
        folder, summary, original = value['entry']
        case = folder / original['folder']
        assert documents[chunk.doc_id][chunk.start:chunk.end] == chunk.text
        windows.append(dict(window_id=chunk.chunk_id, doc_id=chunk.doc_id, start=chunk.start, end=chunk.end,
                            status=original['status'], relation_count=len(value['batch'].relations),
                            original_case=str(case), duplicate_normalization=value['changes']))
        entities = {e['local_id']: e for e in value['batch'].model_dump(mode='json')['entities']}
        resolved = {e['local_id']: e for e in value['resolution']}
        for relation, alignment in zip(value['batch'].model_dump(mode='json')['relations'], value['aligned']):
            head, head_system, head_reason = canonical_endpoint(entities[relation['head']], resolved[relation['head']], reference, chunk.doc_id)
            tail, tail_system, tail_reason = canonical_endpoint(entities[relation['tail']], resolved[relation['tail']], reference, chunk.doc_id)
            evidence = relation['evidence']
            literal = chunk.text[evidence['start']:evidence['end']] == evidence['quote']
            spans = [(chunk.start + unit['start'], chunk.start + unit['end']) for unit in alignment['selected_units']]
            literal = literal and all(documents[chunk.doc_id][a:b] == unit['text'] for (a, b), unit in zip(spans, alignment['selected_units']))
            for context in alignment['context_spans']:
                # Caption contexts use absolute document offsets in saved artifacts.
                if all(key in context for key in ('start', 'end')):
                    quote = context.get('text', context.get('quote', ''))
                    literal = literal and documents[chunk.doc_id][context['start']:context['end']] == quote
            eligible = [s['scope_id'] for s in by_document[chunk.doc_id] if contains(s, spans)]
            if len(eligible) > 1:
                raise ValueError('Overlapping complete annotation scopes require explicit ownership.')
            overlapping = [s['scope_id'] for s in by_document[chunk.doc_id]
                           if any(a < s['end'] and s['start'] < b for a, b in spans)]
            occurrences.append(dict(
                occurrence_id=f'{chunk.chunk_id}:relation:{alignment["relation_index"]}',
                doc_id=chunk.doc_id, window_id=chunk.chunk_id, chunk_id=eligible[0] if eligible else None,
                head_id=head, predicate=relation['predicate'], tail_id=tail,
                head_name=entities[relation['head']]['name'], tail_name=entities[relation['tail']]['name'],
                system_head_id=head_system, system_tail_id=tail_system,
                head_alignment=head_reason, tail_alignment=tail_reason,
                evidence_valid=literal, evidence=evidence, document_evidence_spans=spans,
                context_spans=alignment['context_spans'], review_flags=alignment.get('review_flags', []),
                eligibility='complete_scope' if eligible else ('crosses_annotation_boundary' if overlapping else 'outside_complete_annotation'),
                overlapping_scopes=overlapping, original_status=original['status'],
                strict_eligible=original['status'] in SUCCESS, original_case=str(case), origin='extracted'))
    return occurrences, windows


def evaluate(occurrences, gold, scopes, *, strict):
    rows = [r for r in occurrences if r['chunk_id'] is not None and (r['strict_eligible'] or not strict)]
    details = []
    for scope_id in sorted(scopes):
        expected_rows = [g for g in gold if g['chunk_id'] == scope_id]
        expected = {triple_key(g) for g in expected_rows}
        selected = [r for r in rows if r['chunk_id'] == scope_id]
        actual = {triple_key(r) for r in selected}
        supported = {triple_key(r) for r in selected if r['evidence_valid']}
        correct = expected & supported
        result = measures(len(correct), len(actual - correct), len(expected - correct))
        details.append(dict(scope_id=scope_id, doc_id=scopes[scope_id]['doc_id'], **result,
                            prediction_occurrences=len(selected), unique_predictions=len(actual),
                            matched_gold_ids=sorted({g['gold_id'] for g in expected_rows if triple_key(g) in correct}),
                            missed_gold_ids=sorted({g['gold_id'] for g in expected_rows if triple_key(g) not in correct}),
                            false_positive_triples=[list(key) for key in sorted(actual - correct)]))
    total = measures(*(sum(d[key] for d in details) for key in ['tp', 'fp', 'fn']))
    by_document = []
    for doc_id in sorted({s['doc_id'] for s in scopes.values()}):
        doc_rows = [r for r in details if r['doc_id'] == doc_id]
        by_document.append(dict(doc_id=doc_id, scope_count=len(doc_rows),
                                **measures(*(sum(d[key] for d in doc_rows) for key in ['tp', 'fp', 'fn']))))
    legacy = legacy_score(rows, gold, list(scopes))
    return dict(**total, eligible_prediction_occurrences=len(rows),
                unique_scope_predictions=sum(d['unique_predictions'] for d in details),
                scopes=details, documents=by_document, scope_collapsing_legacy_diagnostic=legacy)


def predicate_summary(occurrences, gold, scopes, *, strict):
    """Describe the same scoped scoring population by relation, without relabeling."""
    predicates = sorted({g['predicate'] for g in gold} | {r['predicate'] for r in occurrences if r['chunk_id'] is not None})
    output = []
    for predicate in predicates:
        result = evaluate([r for r in occurrences if r['predicate'] == predicate],
                          [g for g in gold if g['predicate'] == predicate], scopes, strict=strict)
        output.append(dict(predicate=predicate, **{key:result[key] for key in
                          ['tp', 'fp', 'fn', 'precision', 'recall', 'f1', 'undefined_metrics',
                           'eligible_prediction_occurrences', 'unique_scope_predictions']}))
    return output


def markdown(result):
    def val(value):
        return 'undefined' if value is None else f'{value:.4f}'
    primary, sensitivity = result['strict_pipeline'], result['duplicate_normalized_sensitivity']
    lines = ['# ThreatWeave source-only extraction evaluation', '',
             'This offline analysis uses the preserved model selections before semantic acceptance/rejection and ATT&CK reference fusion. No model output, gold record, source, index, or prompt was changed.', '',
             f'The benchmark contains {result["gold_record_count"]} verified gold records across {result["annotation_scope_count"]} complete source scopes. Expanding their existing additional-support passages yields {result["gold_scope_assertions"]} distinct scope-specific assertions. This preserves report context.', '',
             'The precision/recall/F1 values below measure exact agreement with the frozen annotated inventory. The source inspection flags possible inventory or granularity gaps among nonmatches; these metrics cannot alone establish complete semantic correctness.', '',
             '| Population | TP | FP | FN | Precision | Recall | F1 |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for label, item in [('Strict validated pipeline', primary), ('Duplicate-normalized sensitivity', sensitivity)]:
        lines.append(f'| {label} | {item["tp"]} | {item["fp"]} | {item["fn"]} | {val(item["precision"])} | {val(item["recall"])} | {val(item["f1"])} |')
    lines += ['', '## Population and coverage', '',
              f'All {result["window_count"]} frozen extraction windows remain accounted for: {result["window_status_counts"]}. The strict population retains all gold facts from failed/empty windows in recall; persistent schema failures do not become successful outputs. Sensitivity results use only the already documented deterministic first-support removal of duplicate selections, with original errors preserved.', '',
              f'There are {result["all_pre_review_candidate_occurrences"]} normalized candidate occurrences before semantic filtering. Eligibility counts are {result["eligibility_counts"]}. Outside-scope and boundary-crossing candidates remain listed but are not assumed false against incomplete annotations. These figures are not corpus-wide precision or recall.', '',
              f'Character coverage of the complete gold scopes: {result["scope_character_coverage"]}. The four-relationship/window cap and source mention/schema restrictions are extraction limits, not evidence that empty windows contain no facts.', '',
              '## Strict results by advisory', '',
              '| Advisory | Scopes | TP | FP | FN | Precision | Recall | F1 |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    for row in primary['documents']:
        lines.append(f'| {row["doc_id"]} | {row["scope_count"]} | {row["tp"]} | {row["fp"]} | {row["fn"]} | {val(row["precision"])} | {val(row["recall"])} | {val(row["f1"])} |')
    lines += ['', '## Strict results by predicate', '',
              '| Predicate | TP | FP | FN | Precision | Recall | F1 |',
              '|---|---:|---:|---:|---:|---:|---:|']
    for row in primary['predicates']:
        lines.append(f'| {row["predicate"]} | {row["tp"]} | {row["fp"]} | {row["fn"]} | {val(row["precision"])} | {val(row["recall"])} | {val(row["f1"])} |')
    lines += ['', '## Interpretation and reproducibility', '',
              'The F1 >= 0.80 proposal target is not met by the strict source-scoped benchmark-agreement result. The extraction method was bounded for diagnostic source selections and was not exhaustive NER. No tuning or extra generation was performed after seeing benchmark labels. Development overlap at the advisory/table-scope level remains disclosed in the frozen protocol.', '',
              'Source inspection of all eligible predictions found five potential gold coverage/granularity gaps: SoftPerfect, Advanced IP Scanner and NetScan with the source-cited T1016, direct Akira activity with T1090, and direct Medusa RMM activity with T1219. These remain counted as exact-gold nonmatches. Their absence from a declared complete inventory limits interpreting FP as semantic falsehood. annotation_audit.json records the source basis. No new gold labels, exclusions for better scores, or corrected model outputs were substituted.', '',
              'Endpoint projection uses only exact type-compatible frozen benchmark names, source names, explicit IDs and existing aliases. Local IDs are restricted to their own advisory. It does not add aliases or change the production resolver. Saved production IDs and every projection decision are retained in predictions.json. Relation duplicates are collapsed only within one annotated scope; different report mappings remain distinct.', '',
              'A true positive requires an exact canonical source-scoped triple and a literal valid evidence span/context. Annotation completeness is the pre-existing author confirmation, not a newly inferred label. Source qualifications, overlap, boundary exclusions, nonexhaustive gold coverage outside the 39 scopes, and scoring-only identity alignment limit generalization.', '',
              'The existing scope-collapsing scorer is retained only as a diagnostic in results.json; it cannot distinguish identical facts asserted in different advisory scopes. This report uses scope-specific micro counts. Undefined denominators are null, never imputed.', '',
              'Artifacts: protocol.json, annotation_audit.json, inputs_sha256.json, results.json, predictions.json, gold_expanded.json, scope_alignment.json, windows.json, and report.md. Every source/run artifact used by reconstruction is hashed; originals are unchanged.', '']
    return '\n'.join(lines)


def analyze(repo):
    from evaluation.corpus_review import collect
    repo = Path(repo).resolve()
    protocol = read(repo / PROTOCOL)
    results, runs, plan, catalog, attack_hash = collect(repo, repo / LATEST)
    gold, reference, documents, scopes, expanded = load_gold(repo)
    occurrences, windows = extract_occurrences(results, reference, documents, scopes)
    coverage = []
    for scope_id, scope in sorted(scopes.items()):
        related = [w for w in windows if w['doc_id'] == scope['doc_id'] and w['start'] < scope['end'] and scope['start'] < w['end']]
        length = scope['end'] - scope['start']
        amount = covered_length(scope['start'], scope['end'], [(w['start'], w['end']) for w in related])
        coverage.append(dict(**scope, covered_characters=amount, total_characters=length,
                             fully_covered=amount == length, overlapping_windows=[w['window_id'] for w in related],
                             statuses=dict(Counter(w['status'] for w in related))))
    counts = Counter(r['eligibility'] for r in occurrences)
    result = dict(created_at_utc=datetime.now(timezone.utc).isoformat(),
                  protocol_sha256=sha(repo / PROTOCOL), gold_record_count=len(gold['triples']),
                  annotation_scope_count=len(scopes),
                  gold_scope_assertions=len({(r['chunk_id'], *triple_key(r)) for r in expanded}),
                  all_pre_review_candidate_occurrences=len(occurrences), window_count=len(windows),
                  window_status_counts=dict(Counter(w['status'] for w in windows)), eligibility_counts=dict(counts),
                  scope_character_coverage=dict(fully_covered=sum(r['fully_covered'] for r in coverage),
                                                partially_or_uncovered=[r['scope_id'] for r in coverage if not r['fully_covered']]),
                  strict_pipeline=evaluate(occurrences, expanded, scopes, strict=True),
                  duplicate_normalized_sensitivity=evaluate(occurrences, expanded, scopes, strict=False))
    for name, strict in [('strict_pipeline', True), ('duplicate_normalized_sensitivity', False)]:
        result[name]['predicates'] = predicate_summary(occurrences, expanded, scopes, strict=strict)
        assert all(sum(p[key] for p in result[name]['predicates']) == result[name][key] for key in ['tp', 'fp', 'fn'])
    run_name = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ-') + uuid4().hex[:8]
    output = repo / 'work/extraction_scoring_analysis' / run_name
    output.mkdir(parents=True, exist_ok=False)
    inputs = {str((repo / p).relative_to(repo)): sha(repo / p) for p in
              [PROTOCOL, 'work/final_completion/extraction_annotation_audit.json', 'benchmarks/gold_triples.json', 'benchmarks/entity_reference.json',
               'benchmarks/corpus_manifest.json', 'evaluation/extraction_analysis.py', 'evaluation/score_triples.py']}
    for folder, _ in runs:
        for path in sorted(folder.rglob('*')):
            if path.is_file():
                inputs[str(path.relative_to(repo))] = sha(path)
    for item in read(repo / 'benchmarks/corpus_manifest.json')['documents']:
        for key in ['text_file', 'raw_file']:
            inputs[item[key]] = sha(repo / item[key])
    for name, value in [('protocol.json', protocol), ('annotation_audit.json', read(repo / 'work/final_completion/extraction_annotation_audit.json')), ('inputs_sha256.json', inputs), ('results.json', result),
                        ('predictions.json', occurrences), ('gold_expanded.json', expanded),
                        ('scope_alignment.json', coverage), ('windows.json', windows)]:
        (output / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    report = markdown(result)
    (output / 'report.md').write_text(report, encoding='utf-8')
    (repo / 'docs' / f'ThreatWeave_extraction_results_{run_name}.md').write_text(report, encoding='utf-8')
    assert all(sha(repo / name) == digest for name, digest in inputs.items())
    return output, result
