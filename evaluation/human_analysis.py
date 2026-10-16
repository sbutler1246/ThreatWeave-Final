"""Guarded analysis of completed human reviews; unblinds only after both are fixed."""
from __future__ import annotations

import itertools
import json
import math
import random
import statistics
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.extraction_analysis import sha

DIMENSIONS = ('factuality', 'completeness', 'coherence')
MODES = ('text_only', 'graph_only', 'hybrid_no_node2vec', 'hybrid')
PACKET = 'work/final_evaluation_review_checks/20261016T052517Z-4778a10b'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def validate_review(document, kind, count, prefix):
    if document.get('packet_kind') != kind or document.get('review_status') != 'completed':
        raise ValueError(f'{kind}: completed review export required before unblinding.')
    if not str(document.get('reviewer', '')).strip():
        raise ValueError(f'{kind}: reviewer is required.')
    date.fromisoformat(document['review_date'])
    rows = document.get('ratings', [])
    expected = {f'{prefix}{i:03d}' for i in range(1, count + 1)}
    if len(rows) != count or {r.get('review_id') for r in rows} != expected:
        raise ValueError(f'{kind}: exact complete review IDs required.')
    state = document.get('progress_state', {}).get('ratings', {})
    for row in rows:
        if row.get('entry_complete') is not True:
            raise ValueError(f'{kind}: {row["review_id"]} is unfinished.')
        na = set(row.get('not_ratable_dimensions', []))
        if not na.issubset(DIMENSIONS):
            raise ValueError('Unknown N/A dimension.')
        if na and not str(row.get('not_ratable_reason') or '').strip():
            raise ValueError('N/A requires a reason.')
        for dimension in DIMENSIONS:
            value = row.get(dimension)
            if dimension in na:
                if value is not None:
                    raise ValueError('N/A must have a null numeric score.')
            elif type(value) is not int or not 1 <= value <= 5:
                raise ValueError('Numeric ratings must be integers 1 through 5.')
        if row['review_id'] in state:
            saved = state[row['review_id']]
            values = {d: 'NA' if d in na else str(row[d]) for d in DIMENSIONS}
            if any(saved.get(d) != value for d, value in values.items()):
                raise ValueError('Progress and exported ratings disagree.')
            if (saved.get('reason') or None) != row.get('not_ratable_reason') or saved.get('notes', '') != row.get('notes', ''):
                raise ValueError('Progress and exported comments disagree.')
    return rows


def guard_completed(primary, secondary):
    p = validate_review(primary, 'primary', 80, 'P')
    s = validate_review(secondary, 'secondary', 20, 'S')
    if primary.get('packet_fingerprint') != secondary.get('packet_fingerprint'):
        raise ValueError('Primary and secondary packet fingerprints differ.')
    method = secondary.get('secondary_method')
    same_reviewer = primary['reviewer'].strip().casefold() == secondary['reviewer'].strip().casefold()
    if method == 'independent':
        if same_reviewer:
            raise ValueError('Same reviewer cannot be labeled independent.')
    elif method == 'delayed_rescore':
        if not same_reviewer or date.fromisoformat(secondary['review_date']) < date.fromisoformat(primary['review_date']):
            raise ValueError('Delayed rescore requires the original reviewer and a non-earlier date.')
    else:
        raise ValueError('Secondary method must be independent or delayed_rescore.')
    return p, s


def percentile(values, fraction):
    values = sorted(values)
    position = (len(values) - 1) * fraction
    lo, hi = math.floor(position), math.ceil(position)
    return values[lo] + (values[hi] - values[lo]) * (position - lo)


def bootstrap(values, draws=10000, seed=42):
    if len(values) < 2:
        return None
    rng = random.Random(seed)
    sampled = [statistics.mean(values[rng.randrange(len(values))] for _ in values) for _ in range(draws)]
    return [percentile(sampled, .025), percentile(sampled, .975)]


def primary_comparisons(rows, draws=10000):
    indexed = {(r['question_id'], r['mode']): r for r in rows}
    questions = sorted({r['question_id'] for r in rows})
    output = []
    for dimension in DIMENSIONS:
        for mode_a, mode_b in itertools.combinations(MODES, 2):
            values, included, excluded = [], [], []
            for qid in questions:
                a, b = indexed.get((qid, mode_a)), indexed.get((qid, mode_b))
                if a is None or b is None or a[dimension] is None or b[dimension] is None:
                    excluded.append(qid)
                    continue
                values.append(a[dimension] - b[dimension])
                included.append(qid)
            output.append(dict(dimension=dimension, mode_a=mode_a, mode_b=mode_b,
                               difference='a_minus_b', paired_question_count=len(values),
                               included_questions=included, excluded_questions=excluded,
                               mean_question_difference=statistics.mean(values) if values else None,
                               exploratory_95_percent_ci=bootstrap(values, draws=draws),
                               bootstrap_draws=draws, seed=42,
                               eligibility='Repeat-one numeric ratings in both compared conditions; no N/A imputation.'))
    return output


def agreement(pairs):
    if not pairs:
        return dict(count=0, exact_agreement=None, within_one=None, mean_absolute_difference=None,
                    mean_secondary_minus_primary=None, linear_weighted_kappa=None)
    n = len(pairs)
    observed_cost = sum(abs(a - b) / 4 for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    expected_cost = sum(ca[a] / n * cb[b] / n * abs(a - b) / 4 for a in range(1, 6) for b in range(1, 6))
    return dict(count=n, exact_agreement=sum(a == b for a, b in pairs) / n,
                within_one=sum(abs(a - b) <= 1 for a, b in pairs) / n,
                mean_absolute_difference=sum(abs(a - b) for a, b in pairs) / n,
                mean_secondary_minus_primary=statistics.mean(b - a for a, b in pairs),
                linear_weighted_kappa=1 - observed_cost / expected_cost if expected_cost else None)


def report(summary, mode_rows, paired, consistency):
    def val(value):
        return 'Unavailable' if value is None else f'{value:.3f}'
    lines = ['# ThreatWeave human answer evaluation', '',
             f'Primary review: {summary["primary_reviewer"]}, {summary["primary_date"]}, 80 repeat-one entries. Secondary review: {summary["secondary_reviewer"]}, {summary["secondary_date"]}, 20 entries from five questions, method {summary["secondary_method"]}.', '',
             'The primary reviewer used AI assistance to inspect evidence and draft comments, then entered and confirmed the ratings. The primary export preserves the completed decisions and the documented P069 transcription correction. The author declared limited AI help with the secondary review; the extent was not quantified. The secondary method is reviewer-declared; day-level form dates cannot independently verify the elapsed delay. Same-person delayed results measure within-reviewer consistency and must not be labeled independent inter-rater agreement.', '',
             'Scores use 1 (poor) through 5 (excellent). Failed responses remain N/A; meaningful abstention ratings remain numeric. Primary results and secondary consistency stay separate, with no averaging or replacement of the primary ratings.', '',
             '| Condition | Numeric / 20 | Factuality | Completeness | Coherence | Failure N/A | Abstentions |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for mode in MODES:
        rows = [r for r in mode_rows if r['mode'] == mode]
        lookup = {r['dimension']: r for r in rows}
        first = rows[0]
        lines.append(f'| {mode} | {first["numeric_count"]}/20 | {val(lookup["factuality"]["mean"])} | {val(lookup["completeness"]["mean"])} | {val(lookup["coherence"]["mean"])} | {first["failed_count"]} | {first["abstained_count"]} |')
    lines += ['', '## Paired comparisons', '',
              'Each comparison uses numeric repeat-one ratings for the same question in both conditions. Exploratory percentile intervals resample questions 10,000 times with seed42. N/A cases are excluded pairwise and disclosed, with no zero or perfect-score imputation. The 18 comparisons are not adjusted for multiplicity; available subsets may differ.', '',
              '| Dimension | A minus B | Paired questions / 20 | Mean difference | Exploratory 95% interval |',
              '|---|---|---:|---:|---|']
    for row in paired:
        ci = row['exploratory_95_percent_ci']
        interval = 'Unavailable' if ci is None else f'[{ci[0]:.3f}, {ci[1]:.3f}]'
        lines.append(f'| {row["dimension"]} | {row["mode_a"]} minus {row["mode_b"]} | {row["paired_question_count"]}/20 | {val(row["mean_question_difference"])} | {interval} |')
    lines += ['', '## Secondary consistency', '',
              'Twenty rescores represent five question clusters across four conditions. Descriptive agreement and linear weighted kappa are exploratory; N/A pairs are excluded and counted. They do not establish reliability across independent reviewers or a broad question population.', '',
              '| Dimension | Numeric pairs | Exact agreement | Within one point | Mean absolute difference | Linear weighted kappa |',
              '|---|---:|---:|---:|---:|---:|']
    for dimension in DIMENSIONS:
        row = consistency[dimension]
        lines.append(f'| {dimension} | {row["count"]} | {val(row["exact_agreement"])} | {val(row["within_one"])} | {val(row["mean_absolute_difference"])} | {val(row["linear_weighted_kappa"])} |')
    lines += ['', '## Limits', '',
              'Method labels and automatic scores were withheld until both completed review files passed validation. Graph-shaped supplied evidence makes blinding partial. The same human reviewer and possible AI assistance limit independence. The twenty primary questions, failure-related missingness, schema restrictions, source context, ordinal score scale, and MODE prompt field limit causal and population claims. Ratings quantify the displayed answers, not every possible behavior of the underlying software.', '']
    return '\n'.join(lines)


def analyze(repo, primary_path, secondary_path):
    repo = Path(repo).resolve()
    primary_path, secondary_path = Path(primary_path).resolve(), Path(secondary_path).resolve()
    primary, secondary = read(primary_path), read(secondary_path)
    primary_rows, secondary_rows = guard_completed(primary, secondary)
    declaration_path = repo / 'docs/ThreatWeave_secondary_method_declaration.json'
    declaration = read(declaration_path)
    if (declaration.get('reviewer') != secondary['reviewer'] or
            declaration.get('secondary_method') != secondary['secondary_method'] or
            type(declaration.get('ai_help_with_scores_or_comments')) is not bool):
        raise ValueError('Secondary assistance declaration must match the completed review.')
    # Do not move either read above the completed-review guard.
    folder = repo / PACKET
    manifest = read(folder / 'packet_files_sha256.json')
    if sha(folder / 'unblinding_key.json') != manifest['unblinding_key.json']:
        raise ValueError('Unblinding key hash changed.')
    if primary['packet_fingerprint'] != manifest['unblinding_key.json']:
        raise ValueError('Review exports belong to another frozen packet.')
    key = read(folder / 'unblinding_key.json')
    mapping = {(r['packet'], r['review_id']): r for r in key}
    joined = {}
    for kind, rows in [('primary', primary_rows), ('secondary', secondary_rows)]:
        joined[kind] = []
        for row in rows:
            binding = mapping[(kind, row['review_id'])]
            if binding['repeat'] != 1 or binding['mode'] not in MODES:
                raise ValueError('Review identity is not a frozen repeat-one observation.')
            if binding['status'] == 'failed' and any(row[d] is not None for d in DIMENSIONS):
                raise ValueError(f'{kind} {row["review_id"]}: failed response must remain N/A.')
            joined[kind].append({**row, **{k:binding[k] for k in ['case_id', 'question_id', 'mode', 'repeat', 'status']}})
    modes = []
    for mode in MODES:
        rows = [r for r in joined['primary'] if r['mode'] == mode]
        assert len(rows) == 20
        for dimension in DIMENSIONS:
            values = [r[dimension] for r in rows if r[dimension] is not None]
            modes.append(dict(mode=mode, dimension=dimension, denominator=20, numeric_count=len(values),
                              mean=statistics.mean(values) if values else None,
                              median=statistics.median(values) if values else None,
                              failed_count=sum(r['status'] == 'failed' for r in rows),
                              abstained_count=sum(r['status'] == 'abstained' for r in rows)))
    primary_by_case = {r['case_id']: r for r in joined['primary']}
    consistency = {}
    for dimension in DIMENSIONS:
        pairs, missing = [], []
        for row in joined['secondary']:
            other = primary_by_case[row['case_id']]
            if row[dimension] is None or other[dimension] is None:
                missing.append(row['review_id'])
            else:
                pairs.append((other[dimension], row[dimension]))
        consistency[dimension] = dict(**agreement(pairs), excluded_secondary_ids=missing)
    paired = primary_comparisons(joined['primary'])
    summary = dict(status='completed', primary_reviewer=primary['reviewer'], primary_date=primary['review_date'],
                   secondary_reviewer=secondary['reviewer'], secondary_date=secondary['review_date'],
                   secondary_method=secondary['secondary_method'], primary_entries=80, secondary_entries=20,
                   primary_statuses=dict(Counter(r['status'] for r in joined['primary'])),
                   secondary_question_count=len({r['question_id'] for r in joined['secondary']}),
                   primary_ai_assistance=True, secondary_ai_assistance=declaration['ai_help_with_scores_or_comments'],
                   secondary_assistance_basis=declaration['basis'],
                   secondary_assistance_extent=declaration.get('extent', 'Not quantified.'),
                   unblinding_guard='Both completed files validated before reading the key or method-specific saved scores.')
    output = repo / 'work/human_scoring_analysis' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ-') + uuid4().hex[:8])
    output.mkdir(parents=True, exist_ok=False)
    inputs = {str(path):sha(path) for path in [primary_path, secondary_path, declaration_path, folder/'unblinding_key.json', folder/'packet_files_sha256.json', Path(__file__)]}
    for name, value in [('summary.json', summary), ('mode_summary.json', modes), ('paired_comparisons.json', paired),
                        ('secondary_consistency.json', consistency), ('unblinded_reviews.json', joined), ('inputs_sha256.json', inputs)]:
        (output / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = report(summary, modes, paired, consistency)
    (output / 'report.md').write_text(text, encoding='utf-8')
    (repo / 'docs' / f'ThreatWeave_human_results_{output.name}.md').write_text(text, encoding='utf-8')
    (output / 'files_sha256.json').write_text(json.dumps({p.name:sha(p) for p in output.iterdir() if p.is_file()}, indent=2)+'\n', encoding='utf-8')
    return output
