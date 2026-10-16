"""Offline scoring-plan preparation; no query engine, models or service calls."""
import math
import random
import re
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4

from evaluation.judge_runtime import METRICS,PROBE,policy,read,save,sha

REVIEW = '20261016T052517Z-4778a10b'
PROBE_RUN = '20261016T054257Z-ff74edd0'
KIND = 'final_scoring_inputs'
CODE = ('evaluation/score_plan.py','evaluation/score_runner.py','score_final_evaluation.py')


def digest(value):
    import hashlib,json
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()


def checked_probe(repo,settings):
    folder = repo/'work/evaluation_probe_runs'/PROBE_RUN
    files = read(folder/'files_sha256.json')
    actual = {p.name:sha(p) for p in folder.iterdir() if p.is_file() and p.name!='files_sha256.json'}
    if files!=actual or read(folder/'policy.json')!=settings or read(folder/'synthetic_input.json')!=PROBE:
        raise ValueError('Passed evaluator probe artifacts/policy changed.')
    summary = read(folder/'summary.json')
    if (summary['status']!='passed' or summary['final_benchmark_rows_scored']!=0
            or [r['metric'] for r in summary['metrics']]!=list(METRICS)
            or any(r['status']!='scored' or not math.isfinite(r['value']) for r in summary['metrics'])):
        raise ValueError('The synthetic probe did not pass all three metrics.')
    for suffix in ('before','after'):
        matches = [m for m in read(folder/f'model_tags_{suffix}.json')['models'] if m.get('name')==settings['model']]
        if len(matches)!=1 or matches[0]['digest']!=settings['model_digest']:
            raise ValueError('Saved probe judge identity differs.')
    requests = sorted(folder.glob('judge_call_*_request.json'))
    if len(requests)!=summary['judge_calls']:
        raise ValueError('Saved probe judge request count differs.')
    for request in requests:
        row = read(request); params = row['parameters']
        if (row['endpoint']!='/api/chat' or params['model']!=settings['model'] or params['stream'] is not False
                or any(params['options'].get(k)!=v for k,v in settings['judge_options'].items())):
            raise ValueError('Saved probe judge settings differ.')
        response = read(request.with_name(request.name.replace('_request','_response')))
        if response.get('done') is not True or response.get('done_reason')!='stop':
            raise ValueError('Saved probe contains an incomplete judge reply.')
    return folder


def prepare(repo):
    repo = Path(repo).resolve(); settings = policy(repo); probe = checked_probe(repo,settings)
    folder = repo/'work/final_evaluation_review_checks'/REVIEW
    manifest = read(folder/'packet_files_sha256.json')
    required = ('audit.json','outcomes.json','ragas_inputs.json','source_files_sha256.json')
    if any(sha(folder/name)!=manifest[name] for name in required):
        raise ValueError('Audited scoring export changed.')
    audit = read(folder/'audit.json'); outcomes = read(folder/'outcomes.json'); inputs = read(folder/'ragas_inputs.json')
    if audit['plan_fingerprint']!=settings['final_plan_fingerprint'] or len(outcomes)!=240 or len(inputs)!=225:
        raise ValueError('Unexpected final scoring population.')
    source = Path(audit['source_run']).resolve()
    if source.parent!=repo/'work/final_evaluation_runs':
        raise ValueError('Invalid source-run boundary.')
    source_files = read(folder/'source_files_sha256.json')
    for name,expected in source_files.items():
        if sha(repo/name)!=expected:
            raise ValueError('Collected final-answer artifact changed: '+name)
    labels = {q['id']:q for q in read(repo/'benchmarks/eval_queries.json')['queries']}
    by_id = {r['case_id']:r for r in inputs}
    if len(by_id)!=len(inputs) or len({r['case_id'] for r in outcomes})!=240:
        raise ValueError('Duplicate scoring input.')
    rows = []
    for outcome in outcomes:
        task = outcome['case_id']; label = labels[outcome['question_id']]; case = source/task
        question = read(case/'question.json')
        if (question['question']!=label['question'] or label.get('human_verified') is not True
                or question['mode']!=outcome['mode']):
            raise ValueError('Scoring question/reference binding differs.')
        context = (case/'context.txt').read_text(encoding='utf-8')
        response = read(case/'answer.json')['answer'] if outcome['status']!='failed' else None
        sample = {'user_input':question['question'],'response':response,
                  'retrieved_contexts':[context],'reference':label['reference_answer']}
        if response is None:
            if task in by_id:raise ValueError('Failed generation acquired a replacement scoring response.')
        else:
            exported = by_id.get(task)
            if (exported is None or any(exported[k]!=v for k,v in sample.items())
                    or any(exported[k]!=outcome[k] for k in ('question_id','mode','repeat'))):
                raise ValueError('Scoring export differs from the exact saved answer/context/reference.')
        rows.append({**{k:outcome[k] for k in ('case_id','question_id','mode','repeat','status')},'sample':sample})
    random.Random(42).shuffle(rows)
    tasks = [{'task_id':r['case_id']+'--'+metric,'case_id':r['case_id'],'metric':metric,
              'eligible':r['sample']['response'] is not None} for r in rows for metric in METRICS]
    frozen = {str((folder/name).relative_to(repo)):manifest[name] for name in required}
    frozen.update(source_files)
    frozen.update({str(p.relative_to(repo)):sha(p) for p in probe.iterdir() if p.is_file()})
    frozen.update({name:sha(repo/name) for name in CODE})
    plan = {'version':1,'purpose':'score_logged_final_answers_without_retrieval_or_regeneration',
            'judge_policy':settings,'probe_run':str(probe),'source_run':str(source),
            'review_packet':str(folder),'samples_sha256':digest(rows),'tasks':tasks,
            'eligible_metric_count':sum(t['eligible'] for t in tasks),'total_metric_count':len(tasks),
            'unavailable_metric_count':sum(not t['eligible'] for t in tasks),
            'randomization_seed':42,'metric_timeout_seconds':180,'max_judge_calls_per_metric':30,
            'metric_policy':'All three metrics on the 225 valid response records, including abstentions. All three unavailable for 15 generation failures, including context recall under this complete-response scoring cohort. No placeholder answers or zero imputation.',
            'resume_policy':'Terminal scored, undefined, failed and unavailable outcomes are never regenerated. Only interrupted/unstarted metric tasks may run in a new append-only folder.',
            'analysis_policy':'Report coverage against 240 per metric and mode. Semantic comparisons require paired question-level analysis and human review. Same-model judge is supplementary.',
            'frozen_files_sha256':frozen}
    plan['fingerprint'] = digest(plan)
    output = repo/'work'/KIND/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True);save(output/'samples.json',rows);save(output/'plan.json',plan)
    save(output.parent/'current.json',{'run':output.name,'fingerprint':plan['fingerprint']})
    print('SCORING PREPARED: 675 eligible metric checks; 45 unavailable checks; 240 original outcomes retained.')
    print('Saved scoring inputs:',output)
    return output


def verify(repo,plan,*,full=True):
    for name,expected in plan['frozen_files_sha256'].items():
        if sha(Path(repo)/name)!=expected:
            raise ValueError('Frozen scoring source/implementation changed: '+name)
    if full and policy(repo)!=plan['judge_policy']:
        raise ValueError('Validated judge policy or frozen experiment assets changed.')


def load(repo):
    repo = Path(repo).resolve(); pointer = read(repo/'work'/KIND/'current.json')
    if not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}',pointer['run']):
        raise ValueError('Invalid scoring pointer.')
    folder = repo/'work'/KIND/pointer['run'];plan = read(folder/'plan.json');rows = read(folder/'samples.json')
    if (digest({k:v for k,v in plan.items() if k!='fingerprint'})!=plan['fingerprint']
            or pointer['fingerprint']!=plan['fingerprint'] or digest(rows)!=plan['samples_sha256']):
        raise ValueError('Prepared scoring plan or samples changed.')
    verify(repo,plan)
    return plan,rows
