"""Append-only local scoring of preserved final answers, one terminal metric at a time."""
import asyncio
import logging
import math
import os
import re
import time
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4

from evaluation import judge_runtime as judge
from evaluation.score_plan import digest,verify

KIND = 'final_scoring_runs'
TERMINAL = {'scored','undefined','failed','unavailable_answer'}


def validate(folder,row,task,sample):
    if row['task']!=task or row['input_sha256']!=digest(sample) or row['status'] not in TERMINAL:
        raise ValueError('Saved metric identity/status changed.')
    files = row['files_sha256']
    if not files or any('/' in name or '\\' in name or name=='receipt.json' for name in files):
        raise ValueError('Invalid metric attachment set.')
    if files!={p.name:judge.sha(p) for p in folder.iterdir() if p.is_file() and p.name!='receipt.json'}:
        raise ValueError('Saved metric files changed.')
    if judge.read(folder/'receipt.json')!=row or judge.read(folder/'input.json')!=sample:
        raise ValueError('Saved metric receipt/input changed.')
    if judge.read(folder/'result.json')!={k:v for k,v in row.items() if k!='files_sha256'}:
        raise ValueError('Saved metric result changed.')
    if row['status']=='scored':
        if not isinstance(row['value'],(float,int)) or not math.isfinite(row['value']):
            raise ValueError('Nonfinite saved score.')
    elif row['value'] is not None:
        raise ValueError('A missing metric was given a fabricated score.')
    if (row['status']=='unavailable_answer') == task['eligible']:
        raise ValueError('Metric availability changed.')


def history(repo,latest,plan,rows):
    root = (Path(repo)/'work'/KIND).resolve();folder = Path(latest).resolve();seen=set();runs=[]
    tasks={t['task_id']:t for t in plan['tasks']};samples={r['case_id']:r['sample'] for r in rows}
    while True:
        if folder.parent!=root or folder in seen or not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}',folder.name):
            raise ValueError('Invalid scoring resume boundary or cycle.')
        seen.add(folder);summary=judge.read(folder/'summary.json')
        if summary.get('integrity_error'):raise ValueError('A scoring run failed integrity checks; preserve it for explicit audit.')
        if summary['plan_fingerprint']!=plan['fingerprint'] or judge.read(folder/'plan.json')!=plan:
            raise ValueError('Scoring resume plan differs.')
        if len({r['task']['task_id'] for r in summary['results']})!=len(summary['results']):
            raise ValueError('Duplicate metric task in saved run.')
        runs.append((folder,summary))
        if summary.get('resume_of') is None:break
        folder=Path(summary['resume_of']).resolve()
    complete={}
    for folder,summary in reversed(runs):
        for row in summary['results']:
            task=row['task'];identifier=task['task_id']
            if identifier not in tasks or task!=tasks[identifier]:raise ValueError('Unexpected saved metric task.')
            if identifier in complete:raise ValueError('A terminal scoring observation was regenerated.')
            if row['status'] not in TERMINAL:continue
            validate(folder/identifier,row,task,samples[task['case_id']])
            complete[identifier]={'run':str(folder),**row}
    return complete


def coverage(complete,rows):
    modes={r['case_id']:r['mode'] for r in rows};result={}
    for row in complete.values():
        key=modes[row['task']['case_id']]+'/'+row['task']['metric']
        result.setdefault(key,Counter())[row['status']]+=1
    return {k:dict(v) for k,v in sorted(result.items())}


class MetricRecorder(judge.Recorder):
    def start(self,params):
        if self.count>=self.limit:raise RuntimeError('Per-metric judge-call limit reached; preserve diagnostics.')
        return super().start(params)


class LocalScorer:
    def __init__(self,plan,folder):
        judge.require_pinned_versions();self.settings=plan['judge_policy'];self.folder=folder
        self.recorder=MetricRecorder(folder,plan['max_judge_calls_per_metric'])
        self.metrics={m.name:m for m in judge.build(self.settings,self.recorder)}

    def check_model(self,folder,name):
        judge.check_model(self.settings,folder,name)

    async def score(self,task,sample,folder):
        from ragas import SingleTurnSample
        self.recorder.folder=folder;self.recorder.count=0;self.recorder.phase=task['metric']
        baseline=set(asyncio.all_tasks())
        try:
            return await self.metrics[task['metric']].single_turn_ascore(SingleTurnSample(**sample),timeout=180)
        finally:
            # A failed relevance subrequest can leave gather siblings alive.
            # Cancel/drain them before moving the shared recorder to another task.
            pending=asyncio.all_tasks()-baseline
            for child in pending:child.cancel()
            if pending:await asyncio.gather(*pending,return_exceptions=True)

    def calls(self):return self.recorder.count


async def execute(repo,plan,rows,folder,summary,complete,factory):
    samples={r['case_id']:r['sample'] for r in rows};backend=None;interrupted=False
    try:
        pending=[t for t in plan['tasks'] if t['task_id'] not in complete]
        if any(t['eligible'] for t in pending):
            judge.check_model(plan['judge_policy'],folder,'model_tags_before_initialization.json') if factory is LocalScorer else None
            print('Loading cached scoring adapters once for this process...',flush=True)
            backend=factory(plan,folder)
        for task in pending:
            identifier=task['task_id'];sample=samples[task['case_id']]
            # Cheap code guards between tasks; complete immutable inputs are
            # rechecked at process entry and exit.
            guarded = {name:plan['frozen_files_sha256'][name] for name in (
                'evaluation/score_plan.py','evaluation/score_runner.py','score_final_evaluation.py')}
            guarded.update(plan['judge_policy']['implementation_sha256'])
            for name,expected in guarded.items():
                if judge.sha(Path(repo)/name)!=expected:
                    summary['integrity_error']=True;raise ValueError('Scoring implementation changed during execution.')
            case=folder/identifier;case.mkdir();judge.save(case/'input.json',sample)
            row={'task':task,'input_sha256':digest(sample),'status':'started','value':None}
            summary['results'].append(row);judge.save(folder/'summary.json',summary)
            print(f'SCORING {len(complete)+1}/{len(plan["tasks"])}: {identifier}',flush=True)
            started=time.perf_counter()
            try:
                if not task['eligible']:
                    row.update(status='unavailable_answer',reason='Original generation failed; no valid response exists.',judge_calls=0)
                else:
                    backend.check_model(case,'model_tags_before.json')
                    try:
                        value=float(await backend.score(task,sample,case))
                        row.update(status='scored' if math.isfinite(value) else 'undefined',value=value if math.isfinite(value) else None)
                        if not math.isfinite(value):row['reason']='Metric returned a nonfinite value; not imputed.'
                    except Exception as error:
                        row.update(status='failed',error_type=type(error).__name__,error=str(error),value=None)
                    row['judge_calls']=backend.calls()
                    # Identity changes stop the batch and invalidate this metric;
                    # an evaluator exception alone remains a terminal result.
                    backend.check_model(case,'model_tags_after.json')
            except (KeyboardInterrupt,asyncio.CancelledError):
                row.update(status='interrupted',value=None);interrupted=True;raise
            except Exception as error:
                row.update(status='failed',value=None,error_type=type(error).__name__,error=str(error))
                summary['integrity_error']=True;raise
            finally:
                row['elapsed_ms']=(time.perf_counter()-started)*1000
                judge.save(case/'result.json',row)
                row['files_sha256']={p.name:judge.sha(p) for p in case.iterdir() if p.is_file() and p.name!='receipt.json'}
                judge.save(case/'receipt.json',row);judge.save(folder/'summary.json',summary)
                if row['status'] in TERMINAL:complete[identifier]={'run':str(folder),**row}
        summary['integrity_check_started']=True
        verify(repo,plan)
        if backend is not None:backend.check_model(folder,'model_tags_after_batch.json')
        summary.update(status='attempted',final_integrity_verified=True)
    except (KeyboardInterrupt,asyncio.CancelledError):
        interrupted=True;summary['status']='interrupted'
    except Exception as error:
        summary.update(status='stopped',error_type=type(error).__name__,error=str(error))
        if summary.get('integrity_check_started'):summary['integrity_error']=True
    finally:
        summary.update(terminal_count=len(complete),statuses=dict(Counter(r['status'] for r in complete.values())),
                       coverage=coverage(complete,rows),finished_at=datetime.now(timezone.utc).isoformat())
        judge.save(folder/'summary.json',summary)
    return 2 if interrupted else (0 if summary['status']=='attempted' else 1)


def run(repo,plan,rows,*,resume=None,factory=LocalScorer):
    repo=Path(repo).resolve();verify(repo,plan)
    complete=history(repo,resume,plan,rows) if resume else {}
    if len(complete)==len(plan['tasks']) and judge.read(Path(resume)/'summary.json').get('final_integrity_verified'):
        print('SCORING ALREADY ATTEMPTED: all terminal metric observations are preserved.');return 0
    folder=repo/'work'/KIND/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True);judge.save(folder/'plan.json',plan)
    summary={'status':'started','plan_fingerprint':plan['fingerprint'],'results':[],
             'resume_of':str(Path(resume).resolve()) if resume else None,'prior_terminal_count':len(complete),
             'human_ratings_status':'pending','answer_regeneration_calls':0}
    judge.save(folder/'summary.json',summary);print('Saved scoring run:',folder,flush=True)
    os.environ.update(RAGAS_DO_NOT_TRACK='true',HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1',
                      HF_HUB_DISABLE_TELEMETRY='1',LANGCHAIN_TRACING_V2='false',LANGSMITH_TRACING='false',LANGCHAIN_TRACING='false')
    handler=logging.FileHandler(folder/'evaluator.log',encoding='utf-8');logging.getLogger().addHandler(handler)
    try:code=asyncio.run(execute(repo,plan,rows,folder,summary,complete,factory))
    finally:logging.getLogger().removeHandler(handler);handler.close()
    counts=summary.get('statuses',{})
    print(f'FINAL SCORING {summary["status"].upper()}: {summary.get("terminal_count",0)}/{len(plan["tasks"])} metric outcomes; '
          f'{counts.get("failed",0)} evaluator failures; {counts.get("undefined",0)} undefined; '
          f'{counts.get("unavailable_answer",0)} unavailable from original failures.',flush=True)
    print('Saved scoring run:',folder,flush=True)
    return code
