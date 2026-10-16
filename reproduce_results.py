"""Recompute published statistics using only this checkout and Python's standard library.

No services, model inference, installed third-party packages or original machine paths.
The aligned extraction predictions and native relevancy cosines are preserved inputs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path, PureWindowsPath
import statistics
import sys

ROOT = Path(__file__).resolve().parent
HUMAN = 'work/human_scoring_analysis/20261016T174034Z-7c181a33'
AUTO = 'work/final_scoring_analysis/20261016T075220Z-1e84d02c'
EXTRACTION = 'work/extraction_scoring_analysis/20261016T171118Z-dc75fabd'
PACKET = 'work/final_evaluation_review_checks/20261016T052517Z-4778a10b'
SCORING = 'work/final_scoring_runs/20261016T055210Z-1b048137'
INPUTS = 'work/final_scoring_inputs/20261016T055004Z-f1396885'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def local_path(repo, recorded):
    """Map the recorded project root to THIS checkout; never open the old location."""
    value = str(recorded).replace('\\', '/')
    if PureWindowsPath(value).is_absolute():
        old = 'S:/ThreatWeave/'
        if not value.casefold().startswith(old.casefold()):
            raise ValueError('Unrecognized historical path: ' + value)
        value = value[len(old):]
    elif Path(value).is_absolute() or PureWindowsPath(value).drive:
        raise ValueError('External path is not an input: ' + value)
    target = (repo / value).resolve()
    if not target.is_relative_to(repo.resolve()):
        raise ValueError('Input escapes the checkout: ' + value)
    return target


def equal(actual, expected, label):
    if isinstance(expected, float):
        ok = isinstance(actual, (int, float)) and math.isclose(actual, expected, rel_tol=1e-10, abs_tol=1e-12)
    elif isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            raise ValueError(label + ': dictionary keys differ')
        for key in expected:
            equal(actual[key], expected[key], label + '/' + str(key))
        return
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise ValueError(label + ': row count differs')
        for i, (a, b) in enumerate(zip(actual, expected)):
            equal(a, b, label + '/' + str(i))
        return
    else:
        ok = actual == expected
    if not ok:
        raise ValueError(f'{label}: recomputed {actual!r}, expected {expected!r}')


def check_hashes(repo, bindings):
    for name, digest in bindings.items():
        expected = digest['sha256'] if isinstance(digest, dict) else digest
        if sha(local_path(repo, name)) != expected:
            raise ValueError('Input checksum differs: ' + name)
    return len(bindings)


def human(repo):
    from evaluation.human_analysis import guard_completed, MODES, DIMENSIONS, agreement, primary_comparisons
    primary = read(repo / 'docs/ThreatWeave_primary_completed_ratings.json')
    secondary = read(repo / 'docs/ThreatWeave_secondary_completed_ratings.json')
    p, s = guard_completed(primary, secondary)
    check_hashes(repo, read(repo / HUMAN / 'inputs_sha256.json'))
    manifest = read(repo / PACKET / 'packet_files_sha256.json')
    equal(sha(repo / PACKET / 'unblinding_key.json'), primary['packet_fingerprint'], 'review fingerprint')
    equal(manifest['unblinding_key.json'], primary['packet_fingerprint'], 'key checksum')
    key = {(r['packet'], r['review_id']): r for r in read(repo / PACKET / 'unblinding_key.json')}
    joined = {}
    for kind, rows in [('primary', p), ('secondary', s)]:
        joined[kind] = []
        for row in rows:
            binding = key[kind, row['review_id']]
            if binding['repeat'] != 1 or binding['mode'] not in MODES:
                raise ValueError('Invalid review binding')
            if binding['status'] == 'failed' and any(row[d] is not None for d in DIMENSIONS):
                raise ValueError('Failed answer acquired a numeric review score')
            joined[kind].append({**row, **{k: binding[k] for k in ('case_id', 'question_id', 'mode', 'repeat', 'status')}})
    equal(joined, read(repo / HUMAN / 'unblinded_reviews.json'), 'review joins')
    modes = []
    for mode in MODES:
        rows = [r for r in joined['primary'] if r['mode'] == mode]
        equal(len(rows), 20, 'primary mode denominator')
        for dimension in DIMENSIONS:
            values = [r[dimension] for r in rows if r[dimension] is not None]
            modes.append(dict(mode=mode, dimension=dimension, denominator=20, numeric_count=len(values),
                mean=statistics.mean(values) if values else None, median=statistics.median(values) if values else None,
                failed_count=sum(r['status'] == 'failed' for r in rows),
                abstained_count=sum(r['status'] == 'abstained' for r in rows)))
    lookup = {r['case_id']: r for r in joined['primary']}
    consistency = {}
    for dimension in DIMENSIONS:
        pairs, missing = [], []
        for row in joined['secondary']:
            other = lookup[row['case_id']]
            if row[dimension] is None or other[dimension] is None:
                missing.append(row['review_id'])
            else:
                pairs.append((other[dimension], row[dimension]))
        consistency[dimension] = dict(**agreement(pairs), excluded_secondary_ids=missing)
    pairs = primary_comparisons(joined['primary'])
    for name, value in [('mode_summary', modes), ('secondary_consistency', consistency), ('paired_comparisons', pairs)]:
        equal(value, read(repo / HUMAN / (name + '.json')), 'human/' + name)
    return dict(mode_summary=modes, secondary_consistency=consistency, paired_comparisons=pairs)


def extraction(repo):
    from evaluation.extraction_analysis import load_gold, evaluate, predicate_summary
    check_hashes(repo, read(repo / EXTRACTION / 'inputs_sha256.json'))
    _, _, documents, scopes, gold = load_gold(repo)
    predictions = read(repo / EXTRACTION / 'predictions.json')
    equal(gold, read(repo / EXTRACTION / 'gold_expanded.json'), 'expanded gold')
    for row in predictions:
        chunk = read(local_path(repo, row['original_case']) / 'chunk.json')
        text = documents[row['doc_id']]
        equal(text[chunk['start']:chunk['end']], chunk['text'], 'prediction source window')
        e = row['evidence']
        equal(chunk['text'][e['start']:e['end']], e['quote'], 'prediction literal evidence')
    expected = read(repo / EXTRACTION / 'results.json')
    computed = {}
    for name, strict in [('strict_pipeline', True), ('duplicate_normalized_sensitivity', False)]:
        value = evaluate(predictions, gold, scopes, strict=strict)
        value['predicates'] = predicate_summary(predictions, gold, scopes, strict=strict)
        equal(value, expected[name], 'extraction/' + name)
        computed[name] = value
    return computed


def automatic(repo):
    from evaluation.score_analysis import mode_summary, comparisons, audit_metric
    from evaluation.score_runner import validate
    from evaluation.score_plan import digest
    plan = read(repo / INPUTS / 'plan.json')
    equal(digest({k: v for k, v in plan.items() if k != 'fingerprint'}), plan['fingerprint'], 'scoring plan fingerprint')
    samples = read(repo / INPUTS / 'samples.json')
    equal(digest(samples), plan['samples_sha256'], 'scoring samples fingerprint')
    by_case = {r['case_id']: r for r in samples}
    tasks = {r['task_id']: r for r in plan['tasks']}
    summary = read(repo / SCORING / 'summary.json')
    equal(summary['final_integrity_verified'], True, 'original scoring integrity')
    equal(summary['plan_fingerprint'], plan['fingerprint'], 'scoring run fingerprint')
    equal(read(repo / SCORING / 'plan.json'), plan, 'scoring run plan')
    equal(len(summary['results']), 720, 'metric slots')
    if len({r['task']['task_id'] for r in summary['results']}) != 720:
        raise ValueError('Duplicate metric slot')
    records, formula_count = [], 0
    for row in summary['results']:
        task = tasks[row['task']['task_id']]
        case = by_case[task['case_id']]
        folder = repo / SCORING / task['task_id']
        validate(folder, row, task, case['sample'])
        audit = audit_metric(folder, row, plan['judge_policy'])
        formula_count += bool(audit.get('formula_recomputed'))
        records.append({**{k: case[k] for k in ('case_id', 'question_id', 'mode', 'repeat')},
            'answer_status': case['status'], 'metric': task['metric'], 'status': row['status'],
            'value': row['value'], 'elapsed_ms': row['elapsed_ms'], 'judge_calls': row['judge_calls']})
    equal(records, read(repo / AUTO / 'metric_records.json'), 'native metric records')
    modes, pairs = mode_summary(records), comparisons(records)
    equal(modes, read(repo / AUTO / 'mode_summary.json'), 'automatic means')
    equal(pairs, read(repo / AUTO / 'paired_comparisons.json'), 'automatic paired bootstrap')
    equal(formula_count, 414, 'recomputed judge formulas')
    return dict(mode_summary=modes, paired_comparisons=pairs, formula_recomputed_count=formula_count,
        statuses=dict(Counter(r['status'] for r in records)))


def combined(repo, h, a, e):
    from evaluation.human_analysis import MODES, DIMENSIONS
    from evaluation.submission_analysis import percentile, oriented_comparison, point_target
    expected = read(repo / 'work/final_completion/submission_results.json')
    check_hashes(repo, expected['report_inputs_sha256'])
    cohort = read(repo / PACKET / 'outcomes.json')
    equal(len(cohort), 240, 'measured QA cohort')
    modes = []
    for mode in MODES:
        rows = [r for r in cohort if r['mode'] == mode]
        times = [r['execution_time_ms'] / 1000 for r in rows]
        equal(len(rows), 60, 'timing denominator')
        modes.append(dict(mode=mode, outcomes=60, statuses=dict(Counter(r['status'] for r in rows)),
            case_seconds_all_outcomes=dict(count=60, p50=percentile(times, .5), p95=percentile(times, .95)),
            human={r['dimension']: {k: r[k] for k in ('mean', 'numeric_count', 'denominator', 'failed_count', 'abstained_count')}
                for r in h['mode_summary'] if r['mode'] == mode},
            automatic={r['metric']: {k: r[k] for k in ('available_score_mean', 'available_score_count', 'denominator', 'statuses')}
                for r in a['mode_summary'] if r['mode'] == mode}))
    lookup = {r['mode']: r for r in modes}
    def delta(kind, metric, field):
        return lookup['hybrid'][kind][metric][field] - lookup['text_only'][kind][metric][field]
    gains = dict(human_completeness=delta('human', 'completeness', 'mean'),
        human_factuality=delta('human', 'factuality', 'mean'),
        automatic_faithfulness=delta('automatic', 'faithfulness', 'available_score_mean'))
    computed = dict(modes=modes, available_mean_gains_hybrid_minus_text=gains,
        human_paired_vs_text=[oriented_comparison(h['paired_comparisons'], 'dimension', d, m) for m in MODES[1:] for d in DIMENSIONS],
        automatic_paired_vs_text=[oriented_comparison(a['paired_comparisons'], 'metric', d, m) for m in MODES[1:]
            for d in sorted({r['metric'] for r in a['mode_summary']})],
        secondary_consistency=h['secondary_consistency'],
        proposed_qa_target_on_available_point_estimates=point_target(*gains.values()),
        proposed_extraction_target_met=e['strict_pipeline']['f1'] >= .8)
    for name, value in computed.items():
        equal(value, expected[name], 'report/' + name)
    return computed


def reproduce(repo, output):
    repo = Path(repo).resolve()
    print('Verifying preserved inputs in this checkout...', flush=True)
    manifest = read(repo / 'SUBMISSION_MANIFEST.json')
    # Only explicitly named publication documents differ from the original archive.
    adapted = set(read(repo / 'PUBLICATION_SNAPSHOT.json')['adapted_publication_documents'])
    allowed = {'README.md', 'PROJECT_FILES.md', '.gitignore', '.gitattributes',
        'docs/ThreatWeave_application_setup_step.md', 'docs/ThreatWeave_application_launch_step.md'}
    if not adapted <= allowed:
        raise ValueError('Unexpected exemption from frozen input verification')
    count = check_hashes(repo, {k: v for k, v in manifest.items() if k not in adapted})
    for folder in (HUMAN, AUTO):
        check_hashes(repo, {folder + '/' + k: v for k, v in read(repo / folder / 'files_sha256.json').items()})
    print('Recomputing 80 primary ratings, 20 rescores and paired intervals...', flush=True)
    h = human(repo)
    print('Recomputing source-scoped extraction metrics...', flush=True)
    e = extraction(repo)
    print('Auditing all 720 native metric slots and recomputing automatic comparisons...', flush=True)
    a = automatic(repo)
    result = dict(status='passed', created_at_utc=datetime.now(timezone.utc).isoformat(),
        frozen_files_verified=count, human=h, extraction=e, automatic=a, report=combined(repo, h, a, e),
        service_calls=0, model_calls=0, embedding_calls=0,
        boundaries=['Reuses preserved aligned pre-review extraction predictions; does not regenerate them.',
            'Recomputes 414 saved-verdict formulas. Native answer-relevancy cosines are verified inputs, not new embedding inference.',
            'Reproduces analysis of collected observations, not an identical new LLM experiment.'])
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / 'results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    strict = e['strict_pipeline']
    text = ('# Reproduction passed\n\n'
        f'Verified {count:,} preserved files in this checkout. Recomputed 80 primary reviews, 20 delayed rescores, '
        '18 human and 18 automatic paired comparisons, extraction metrics and final report point targets. '
        'Audited all 720 metric slots and independently recomputed 414 verdict formulas.\n\n'
        f'Extraction: TP {strict["tp"]}, FP {strict["fp"]}, FN {strict["fn"]}; F1 {strict["f1"]:.12f}.\n\n'
        'No services, model calls or embedding calls. See results.json for denominators, intervals and reproduction boundaries.\n')
    (output / 'report.md').write_text(text, encoding='utf-8')
    print('PASS: Published statistics match. New results: ' + str(output), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New output directory; must not already exist.')
    args = parser.parse_args()
    output = args.output or ROOT / 'outputs/reproduction' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    try:
        reproduce(ROOT, output)
    except (OSError, ValueError, KeyError, AssertionError) as error:
        print('FAIL: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
