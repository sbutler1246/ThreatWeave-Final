"""Join preserved analyses for reporting after completed human-review validation."""
from __future__ import annotations
import json
import math
import statistics
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from evaluation.human_analysis import guard_completed, read, MODES, DIMENSIONS
from evaluation.extraction_analysis import sha

AUTO='work/final_scoring_analysis/20261016T075220Z-1e84d02c'
EXTRACTION='work/extraction_scoring_analysis/20261016T171118Z-dc75fabd'
COHORT='work/final_evaluation_review_checks/20261016T052517Z-4778a10b'

def oriented_comparison(rows, field, metric, condition, baseline='text_only'):
    matches=[r for r in rows if r[field]==metric and {r['mode_a'],r['mode_b']}=={condition,baseline}]
    if len(matches)!=1:raise ValueError('Exactly one saved paired comparison is required.')
    row=matches[0];direction=1 if row['mode_a']==condition else -1
    value=row['mean_question_difference'];ci=row['exploratory_95_percent_ci']
    interval=None if ci is None else list(ci) if direction==1 else [-ci[1],-ci[0]]
    return dict(metric=metric,condition=condition,baseline=baseline,difference='condition_minus_baseline',
                paired_question_count=row['paired_question_count'],
                mean_difference=None if value is None else direction*value,
                exploratory_95_percent_ci=interval,
                included_questions=row['included_questions'],excluded_questions=row['excluded_questions'])

def point_target(completeness_gain, factuality_gain, faithfulness_gain):
    values=(completeness_gain,factuality_gain,faithfulness_gain)
    if any(v is None or not math.isfinite(v) for v in values):return None
    return completeness_gain>=.5 and factuality_gain>=0 and faithfulness_gain>=0

def percentile(values,fraction):
    if not values:return None
    values=sorted(values);position=(len(values)-1)*fraction;lo=math.floor(position);hi=math.ceil(position)
    return values[lo]+(values[hi]-values[lo])*(position-lo)

def prepare(repo,human_folder):
    repo=Path(repo).resolve();human_folder=Path(human_folder).resolve()
    primary=repo/'docs/ThreatWeave_primary_completed_ratings.json'
    secondary=repo/'docs/ThreatWeave_secondary_completed_ratings.json'
    # No condition-specific QA records may be read above these checks.
    guard_completed(read(primary),read(secondary))
    bindings=read(human_folder/'inputs_sha256.json')
    for source in (primary,secondary):
        if bindings.get(str(source))!=sha(source):raise ValueError('Human export changed after analysis.')
    if read(human_folder/'summary.json').get('status')!='completed':raise ValueError('Completed human analysis required.')
    for folder in (human_folder,repo/AUTO):
        for name,digest in read(folder/'files_sha256.json').items():
            if sha(folder/name)!=digest:raise ValueError(f'Saved analysis artifact changed: {folder/name}')
    hm=read(human_folder/'mode_summary.json');hp=read(human_folder/'paired_comparisons.json')
    am=read(repo/AUTO/'mode_summary.json');ap=read(repo/AUTO/'paired_comparisons.json')
    cohort=read(repo/COHORT/'outcomes.json');extraction=read(repo/EXTRACTION/'results.json')
    if len(cohort)!=240:raise ValueError('All measured outcomes must remain in reporting.')
    modes=[]
    for mode in MODES:
        rows=[r for r in cohort if r['mode']==mode]
        times=[r['execution_time_ms']/1000 for r in rows]
        if len(rows)!=60 or any(not math.isfinite(t) or t<0 for t in times):raise ValueError('Invalid timing population.')
        modes.append(dict(mode=mode,outcomes=len(rows),statuses=dict(Counter(r['status'] for r in rows)),
            case_seconds_all_outcomes=dict(count=len(times),p50=percentile(times,.5),p95=percentile(times,.95)),
            human={r['dimension']:{k:r[k] for k in ('mean','numeric_count','denominator','failed_count','abstained_count')} for r in hm if r['mode']==mode},
            automatic={r['metric']:{k:r[k] for k in ('available_score_mean','available_score_count','denominator','statuses')} for r in am if r['mode']==mode}))
    human_pairs=[oriented_comparison(hp,'dimension',d,m) for m in MODES[1:] for d in DIMENSIONS]
    auto_metrics=sorted({r['metric'] for r in am})
    auto_pairs=[oriented_comparison(ap,'metric',d,m) for m in MODES[1:] for d in auto_metrics]
    lookup={r['mode']:r for r in modes}
    def delta(kind,metric,key):
        a=lookup['hybrid'][kind][metric][key];b=lookup['text_only'][kind][metric][key]
        return None if a is None or b is None else a-b
    gains=dict(human_completeness=delta('human','completeness','mean'),human_factuality=delta('human','factuality','mean'),
               automatic_faithfulness=delta('automatic','faithfulness','available_score_mean'))
    result=dict(created_at_utc=datetime.now(timezone.utc).isoformat(),human_analysis=str(human_folder),
        extraction_analysis=EXTRACTION,automatic_analysis=AUTO,modes=modes,human_paired_vs_text=human_pairs,
        automatic_paired_vs_text=auto_pairs,secondary_consistency=read(human_folder/'secondary_consistency.json'),
        extraction=extraction,available_mean_gains_hybrid_minus_text=gains,
        proposed_qa_target_on_available_point_estimates=point_target(gains['human_completeness'],gains['human_factuality'],gains['automatic_faithfulness']),
        proposed_extraction_target_met=extraction['strict_pipeline']['f1']>=.8,
        interpretation='Point targets use available marginal means only. Paired estimates/coverage remain separate. Unequal availability, small samples, AI assistance and MODE/evidence-format confounds prevent a general superiority claim.',
        timing_definition='Measured case duration after one excluded warm-up per condition. All 60 outcomes per condition include failed repairs and abstentions. P95 uses linear interpolation at (n-1)*0.95. These are not separate Neo4j/Ollama/GPU measurements.',
        unsupported_claim_rate='Not separately annotated at claim level; cannot infer this rate from ordinal answer ratings.')
    files=[primary,secondary,human_folder/'inputs_sha256.json',human_folder/'mode_summary.json',human_folder/'paired_comparisons.json',
           human_folder/'secondary_consistency.json',repo/AUTO/'mode_summary.json',repo/AUTO/'paired_comparisons.json',
           repo/COHORT/'outcomes.json',repo/EXTRACTION/'results.json',Path(__file__)]
    result['report_inputs_sha256']={str(p):sha(p) for p in files}
    target=repo/'work/final_completion/submission_results.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return target
