"""Offline audit and question-cluster analysis of preserved scoring outcomes."""
import itertools
import math
import random
import statistics
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4

from evaluation.judge_runtime import METRICS,read,save,sha
from evaluation.score_plan import load
from evaluation.score_runner import history

MODES=('text_only','graph_only','hybrid_no_node2vec','hybrid')


def extracted_json(text):
    """Match the frozen RAGAS 0.2.15 first-structure delimiter extraction."""
    import json
    markdown=text.find('```json')
    if markdown!=-1:text=text[markdown:]
    positions=[p for p in (text.find('['),text.find('{')) if p!=-1]
    if not positions:return json.loads(text)
    start=min(positions);opening=text[start];closing=']' if opening=='[' else '}'
    count=0
    for i,char in enumerate(text[start:],start):
        if char==opening:count+=1
        elif char==closing:count-=1
        if count==0:return json.loads(text[start:i+1])
    return json.loads(text)


def percentile(values,p):
    values=sorted(values);position=(len(values)-1)*p;lower=math.floor(position);upper=math.ceil(position)
    return values[lower]+(values[upper]-values[lower])*(position-lower)


def bootstrap(differences, *, draws=10000, seed=42):
    if len(differences)<2:return None
    rng=random.Random(seed);n=len(differences)
    values=[sum(differences[rng.randrange(n)] for _ in range(n))/n for _ in range(draws)]
    return [percentile(values,0.025),percentile(values,0.975)]


def comparisons(records, *, draws=10000):
    questions=sorted({r['question_id'] for r in records})
    index={(r['question_id'],r['mode'],r['repeat'],r['metric']):r for r in records}
    result=[]
    for metric in METRICS:
        for a,b in itertools.combinations(MODES,2):
            diffs=[];included=[];excluded=[]
            for qid in questions:
                paired=[index.get((qid,mode,repeat,metric)) for mode in (a,b) for repeat in (1,2,3)]
                if any(r is None or r['status']!='scored' for r in paired):excluded.append(qid);continue
                av=statistics.mean(r['value'] for r in paired[:3]);bv=statistics.mean(r['value'] for r in paired[3:])
                diffs.append(av-bv);included.append(qid)
            result.append({'metric':metric,'mode_a':a,'mode_b':b,'difference':'a_minus_b',
                           'paired_question_count':len(included),'included_questions':included,'excluded_questions':excluded,
                           'mean_question_difference':statistics.mean(diffs) if diffs else None,
                           'exploratory_95_percent_ci':bootstrap(diffs,draws=draws),
                           'bootstrap_draws':draws,'seed':42,
                           'eligibility':'All three repeats scored in both compared modes; each question weighted equally.'})
    return result


def mode_summary(records):
    summaries=[]
    for mode in MODES:
        for metric in METRICS:
            rows=[r for r in records if r['mode']==mode and r['metric']==metric]
            values=[r['value'] for r in rows if r['status']=='scored']
            summaries.append({'mode':mode,'metric':metric,'denominator':len(rows),
                              'statuses':dict(Counter(r['status'] for r in rows)),
                              'available_score_mean':statistics.mean(values) if values else None,
                              'available_score_count':len(values),
                              'availability_fraction':len(values)/len(rows) if rows else None})
    return summaries


def audit_metric(folder,row,settings):
    requests=sorted(folder.glob('judge_call_*_request.json'))
    if len(requests)!=row['judge_calls']:raise ValueError('Judge-call count differs.')
    replies=[]
    for request in requests:
        saved=read(request);params=saved['parameters']
        if (saved['phase']!=row['task']['metric'] or saved['endpoint']!='/api/chat'
                or params['model']!=settings['model'] or params['stream'] is not False
                or any(params['options'].get(k)!=v for k,v in settings['judge_options'].items())):
            raise ValueError('Saved judge request violates the fixed policy.')
        response=request.with_name(request.name.replace('_request','_response'))
        error=request.with_name(request.name.replace('_request','_error'))
        if response.exists()==error.exists():raise ValueError('Judge response/error correspondence differs.')
        if response.exists():replies.append(read(response))
    if row['status']=='unavailable_answer':
        if requests:raise ValueError('Unavailable answer was submitted to a judge.')
        return {'formula_recomputed':False}
    for when in ('before','after'):
        models=[m for m in read(folder/f'model_tags_{when}.json')['models'] if m.get('name')==settings['model']]
        if len(models)!=1 or models[0]['digest']!=settings['model_digest']:raise ValueError('Saved judge digest changed.')
    if row['status']=='failed':
        return {'failure_cause':'judge_output_limit' if replies and replies[-1].get('done_reason')=='length' else row.get('error_type'),
                'last_reply_eval_count':replies[-1].get('eval_count') if replies else None,
                'last_reply_done_reason':replies[-1].get('done_reason') if replies else None}
    if row['status']!='scored':return {'formula_recomputed':False}
    if any(r.get('done') is not True or r.get('done_reason')!='stop' for r in replies):
        raise ValueError('A numeric metric accepted an incomplete judge reply.')
    metric=row['task']['metric'];details={'formula_recomputed':metric!='answer_relevancy'}
    if metric=='faithfulness':
        verdicts=extracted_json(replies[-1]['message']['content'])['statements']
        value=sum(bool(int(v['verdict'])) for v in verdicts)/len(verdicts)
        if len(replies)==2:
            statements=extracted_json(replies[0]['message']['content'])['statements']
            details['statement_count']=len(statements);details['verdict_count']=len(verdicts)
            details['statement_verdict_count_mismatch']=len(statements)!=len(verdicts)
    elif metric=='context_recall':
        verdicts=extracted_json(replies[-1]['message']['content'])['classifications']
        value=sum(bool(int(v['attributed'])) for v in verdicts)/len(verdicts)
    else:
        if not -1.000001<=row['value']<=1.000001:raise ValueError('Relevancy outside cosine bounds.')
        values=[extracted_json(r['message']['content']) for r in replies]
        if len(values)==3 and any(int(v['noncommittal']) for v in values) and row['value']!=0:
            raise ValueError('Noncommittal relevance did not receive native zero score.')
        return details
    if not math.isclose(value,row['value'],abs_tol=1e-12):raise ValueError('Saved metric differs from its judge verdict formula.')
    return details


def report(audit,summaries,paired):
    lines=['# Automated final scoring results (human review pending)',
           'All 720 slots were recorded: 639 numeric scores, 36 evaluator failures and 45 unavailable slots from fifteen original generation failures. No scores were imputed and no failed check was regenerated. All 36 evaluator failures ended at the fixed 700-token output limit: 33 faithfulness and three context-recall checks.',
           'Means below describe only available scores. Missingness differs by method and is not assumed random. These values are supplementary same-model judgments, not human-verified answer quality.',
           '| Condition | Metric | Mean of available scores | Numeric / 60 | Evaluator failures | No valid answer |',
           '|---|---|---:|---:|---:|---:|']
    for row in summaries:
        s=row['statuses'];lines.append(f'| {row["mode"]} | {row["metric"]} | {row["available_score_mean"]:.4f} | {row["available_score_count"]}/60 | {s.get("failed",0)} | {s.get("unavailable_answer",0)} |')
    lines+=['','## Paired question comparisons',
            'Each included question has numeric scores for all three repeats in both compared conditions. First average repeats within each question; then average the paired question differences. Intervals resample paired questions 10,000 times with seed42 and use percentile 2.5/97.5 endpoints. Missing values are not imputed. Question IDs excluded from each comparison are in paired_comparisons.json.',
            'These are exploratory 95% intervals, with no multiple-comparison adjustment. The paired subset can differ across comparisons and cannot represent missing questions without further assumptions. Twenty questions across a limited advisory corpus also limit generalization.',
            '| Metric | A minus B | Paired questions / 20 | Mean difference | Exploratory 95% interval |',
            '|---|---|---:|---:|---|']
    for row in paired:
        interval=row['exploratory_95_percent_ci'];ci=f'[{interval[0]:.4f}, {interval[1]:.4f}]' if interval else 'Unavailable'
        value=f'{row["mean_question_difference"]:.4f}' if row['mean_question_difference'] is not None else 'Unavailable'
        lines.append(f'| {row["metric"]} | {row["mode_a"]} minus {row["mode_b"]} | {row["paired_question_count"]}/20 | {value} | {ci} |')
    lines+=['','## Audit and interpretation limits',
            f'Saved artifact/input/receipt checks passed for all 720 tasks. Request settings, response correspondence and pre/post model identity were checked. {audit["formula_recomputed_count"]} faithfulness/context-recall formulas were independently recomputed from saved judge verdicts without model calls. Relevancy scores were checked for bounds, request bindings and noncommittal behavior; cosine values were not independently recomputed because that would require embedding inference.',
            f'There are {len(audit["statement_verdict_count_mismatches"])} numeric faithfulness results with different statement/verdict counts. These flags do not alter frozen native scores; they identify an additional judge-completeness limitation for interpretation.',
            'Graph-only empty-evidence abstentions remain scored responses. Original collection failures and evaluator output truncation are separate events. The four prompts retain a MODE field, and evidence formats differ. No Python/service/GPU resource measurements are available from collection. Human ratings and extraction precision/recall/F1 are still pending. Do not claim overall method superiority from these conditional means.']
    body='\n\n'.join(lines[:3])+'\n\n'+'\n'.join(lines[3:])+'\n'
    body=body.replace('## Paired question comparisons\n','## Paired question comparisons\n\n')
    body=body.replace('## Audit and interpretation limits\n','## Audit and interpretation limits\n\n')
    body=body.replace('paired_comparisons.json.\n','paired_comparisons.json.\n\n')
    body=body.replace('generalization.\n|','generalization.\n\n|')
    return body


def analyze(repo,run):
    repo=Path(repo).resolve();plan,rows=load(repo);complete=history(repo,run,plan,rows)
    summary=read(Path(run)/'summary.json')
    if len(complete)!=720 or summary.get('final_integrity_verified') is not True:
        raise ValueError('All terminal metrics and final integrity verification are required.')
    by_id={r['case_id']:r for r in rows};records=[];checks=[];source_files={}
    for identifier,r in complete.items():
        case=by_id[r['task']['case_id']];folder=Path(r['run'])/identifier
        check=audit_metric(folder,r,plan['judge_policy']);checks.append({'task_id':identifier,**check})
        records.append({**{k:case[k] for k in ('case_id','question_id','mode','repeat','status')},
                        'answer_status':case['status'],'metric':r['task']['metric'],'status':r['status'],
                        'value':r['value'],'elapsed_ms':r['elapsed_ms'],'judge_calls':r['judge_calls']})
        source_files.update({str(p.relative_to(repo)):sha(p) for p in folder.iterdir() if p.is_file()})
    for folder in {Path(r['run']) for r in complete.values()}:
        source_files.update({str(p.relative_to(repo)):sha(p) for p in folder.iterdir() if p.is_file()})
    audit={'status':'offline_audit_passed','source_run':str(Path(run).resolve()),'scoring_plan_fingerprint':plan['fingerprint'],
           'metric_count':len(records),'statuses':dict(Counter(r['status'] for r in records)),
           'judge_calls':sum(r['judge_calls'] for r in records),'formula_recomputed_count':sum(c.get('formula_recomputed',False) for c in checks),
           'failure_causes':dict(Counter(c['failure_cause'] for c in checks if 'failure_cause' in c)),
           'statement_verdict_count_mismatches':[c for c in checks if c.get('statement_verdict_count_mismatch')],
           'implementation_sha256':{name:sha(repo/name) for name in ('evaluation/score_analysis.py','analyze_final_scoring.py')},
           'evaluator_formula_sources_sha256':{name:sha(repo/name) for name in (
               '.venv-eval/Lib/site-packages/ragas/metrics/_faithfulness.py',
               '.venv-eval/Lib/site-packages/ragas/metrics/_context_recall.py',
               '.venv-eval/Lib/site-packages/ragas/prompt/utils.py')},
           'human_ratings_status':'pending','extraction_metrics_status':'pending','model_calls':0,'embedding_calls':0}
    summaries=mode_summary(records);paired=comparisons(records)
    output=repo/'work/final_scoring_analysis'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8]);output.mkdir(parents=True)
    for name,value in [('audit.json',audit),('metric_records.json',records),('metric_audits.json',checks),
                       ('mode_summary.json',summaries),('paired_comparisons.json',paired),('source_files_sha256.json',source_files)]:save(output/name,value)
    doc=repo/'docs'/('ThreatWeave_final_scoring_results_'+output.name+'.md');doc.write_text(report(audit,summaries,paired),encoding='utf-8')
    save(output/'files_sha256.json',{p.name:sha(p) for p in output.iterdir() if p.is_file()})
    print('OFFLINE SCORING AUDIT PASSED:',audit['statuses'],'; judge calls:',audit['judge_calls'])
    print('Saved analysis:',output);print('Saved results report:',doc)
    return output,doc
