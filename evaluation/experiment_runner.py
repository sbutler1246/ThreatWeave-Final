"""Append-only controlled QA execution with strict resume and preserved failures."""
import json
import math
import re
import time
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4

from evaluation.experiment_plan import read,verify_files
from extraction.llama_tokenizer import sha256_file
from graph.development_projection import digest
from graph_qa import CompactAnswer,SYSTEM
from graph_pilot_qa import checked_answer
from schemas import AnswerResponse,EvidenceBundle,QueryRequest

KIND='final_evaluation_runs'
TERMINAL={'answer_ready_for_review','abstained','failed'}


def save(path,value):
    path=Path(path);temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');temp.replace(path)


def validate_case(folder,row,task,question,config):
    if row['task']!=task or row['question_sha256']!=digest(question) or row['status'] not in TERMINAL:
        raise ValueError('Saved final case identity/status changed.')
    if not row['files_sha256'] or any('/' in name or '\\' in name or name=='case_receipt.json' for name in row['files_sha256']):
        raise ValueError('Invalid final case attachment set.')
    files={p.name:sha256_file(p) for p in folder.iterdir() if p.is_file() and p.name!='case_receipt.json'}
    if files!=row['files_sha256'] or read(folder/'case_receipt.json')!=row:
        raise ValueError('Saved final case artifacts changed.')
    expected=QueryRequest(question=question,mode=task['mode'],corpus_version=config['corpus_version']).model_dump(mode='json')
    if read(folder/'question.json')!=expected:raise ValueError('Saved final question changed.')
    if row['status']=='failed':return
    bundle=EvidenceBundle.model_validate(read(folder/'evidence.json'))
    answer=AnswerResponse.model_validate(read(folder/'answer.json'))
    if (answer.evidence!=bundle or bundle.corpus_version!=config['corpus_version']
            or bundle.configuration_hash!=row['configuration_hash']
            or answer.execution_time_ms!=row['execution_time_ms'] or not math.isfinite(row['execution_time_ms'])
            or ('abstained' if answer.abstained else 'answer_ready_for_review')!=row['status']):
        raise ValueError('Saved final answer/evidence differs.')
    attempts=row['attempts']
    if attempts==0:
        if (bundle.passages and (task['mode']!='graph_only' or bundle.paths)) or answer.claims or not answer.abstained:
            raise ValueError('Invalid empty-evidence abstention.')
        return
    if attempts not in {1,2}:raise ValueError('Invalid final generator attempt count.')
    context=(folder/'context.txt').read_text(encoding='utf-8')
    prompt='QUESTION: '+question+'\nMODE: '+task['mode']+'\n'+context+'\nReturn the requested JSON. The displayed answer is assembled from claims.'
    schema=CompactAnswer.model_json_schema()
    schema['$defs']['CompactClaim']['properties']['citations']['items']={'type':'string','enum':bundle.citation_ids}
    if ((folder/'user_prompt.txt').read_text(encoding='utf-8')!=prompt
            or (folder/'system_prompt.txt').read_text(encoding='utf-8')!=SYSTEM or read(folder/'output_schema.json')!=schema):
        raise ValueError('Saved final generation prompt/schema differs.')
    for n in range(1,attempts+1):
        request=read(folder/f'transport_request_{n}.json')
        p=prompt if n==1 else (folder/'repair_prompt.txt').read_text(encoding='utf-8')
        payload={'model':config['llm']['model'],'system':SYSTEM,'prompt':p,'format':schema,'stream':False,
                 'options':{k:config['llm'][k] for k in ['temperature','num_ctx','num_predict']}}
        if request['url']!='http://localhost:11434/api/generate' or request['payload']!=payload:
            raise ValueError('Saved generator payload differs from the frozen method.')
    body=read(folder/f'ollama_response_{attempts}.json')
    transport=json.loads((folder/f'transport_response_{attempts}.txt').read_text(encoding='utf-8'))
    if (body!=transport or body.get('done') is not True or body.get('done_reason')=='length'
            or read(folder/f'transport_status_{attempts}.json')['http_status']!=200):
        raise ValueError('Saved final generation was not complete.')
    CompactAnswer.model_validate_json(body['response'])
    checked=checked_answer(body['response'],bundle,0)
    if (checked.answer.replace('retrieved pilot evidence','retrieved evidence')!=answer.answer
            or checked.claims!=answer.claims or checked.abstained!=answer.abstained):
        raise ValueError('Saved final answer differs from the original model reply.')


def history(repo,latest,plan,questions):
    root=(Path(repo)/'work'/KIND).resolve();folder=Path(latest).resolve();seen=set();runs=[]
    tasks={t['case_id']:t for t in plan['schedule']};qmap={q['id']:q['question'] for q in questions}
    config=read(Path(repo)/'config.json')
    while True:
        if (folder.parent!=root or folder in seen or not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}',folder.name)):
            raise ValueError('Invalid final-run resume boundary or cycle.')
        seen.add(folder);summary=read(folder/'summary.json')
        if summary.get('integrity_error'):
            raise ValueError('A prior run failed the final graph/file integrity check; preserve it for explicit audit before continuing.')
        if summary.get('plan_fingerprint')!=plan['fingerprint'] or read(folder/'plan.json')!=plan or read(folder/'questions.json')!=questions:
            raise ValueError('Resume experiment plan/questions changed.')
        rows=summary['cases']
        if len({r['task']['case_id'] for r in rows})!=len(rows):raise ValueError('Duplicate final case in saved run.')
        runs.append((folder,rows))
        if summary.get('resume_of') is None:break
        folder=Path(summary['resume_of']).resolve()
    complete={}
    for folder,rows in reversed(runs):
        for row in rows:
            task=row['task'];identifier=task['case_id']
            if identifier not in tasks or task!=tasks[identifier]:raise ValueError('Unexpected final case identity.')
            if identifier in complete and task['measured']:raise ValueError('A completed final observation was regenerated.')
            if row['status'] not in TERMINAL:continue
            question=qmap[task['question_id']] if task['measured'] else plan['warmup_question']
            validate_case(folder/identifier,row,task,question,config)
            if task['measured'] or row['status']!='failed':complete[identifier]={'run':str(folder),**row}
    return complete


def run(repo,questions,plan,backend_factory,*,resume=None):
    repo=Path(repo).resolve();verify_files(repo,plan)
    complete=history(repo,resume,plan,questions) if resume else {}
    pending=[t for t in plan['schedule'] if t['case_id'] not in complete]
    if not pending and resume and read(Path(resume)/'summary.json').get('final_graph_verified') is True:
        print('FINAL BATCH ALREADY ATTEMPTED: all 240 measured outcomes are preserved. Scoring remains pending.')
        return 1 if any(r['status']=='failed' for r in complete.values() if r['task']['measured']) else 0
    # Every resumed operator process repeats excluded warmups before unfinished
    # measurements; completed measured outcomes are never regenerated.
    pending=[t for t in plan['schedule'] if not t['measured'] or t['case_id'] not in complete]
    folder=repo/'work'/KIND/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8]);folder.mkdir(parents=True)
    save(folder/'plan.json',plan);save(folder/'questions.json',questions)
    summary={'purpose':'frozen_final_answer_experiment','plan_fingerprint':plan['fingerprint'],'status':'started',
             'resume_of':str(Path(resume).resolve()) if resume else None,'cases':[],
             'prior_terminal_cases':len(complete),'human_review_status':'pending','scores_computed':False}
    save(folder/'summary.json',summary)
    print('Saved final run:',folder,flush=True)
    backend=None;qmap={q['id']:q['question'] for q in questions};interrupted=False
    try:
        backend=backend_factory()
        summary['initialization_complete_at']=datetime.now(timezone.utc).isoformat()
        summary['runtime_info']=getattr(backend,'runtime_info',{})
        save(folder/'summary.json',summary)
        for task in pending:
            verify_files(repo,plan,full=False);backend.check_model()
            identifier=task['case_id'];case=folder/identifier;case.mkdir()
            question=qmap[task['question_id']] if task['measured'] else plan['warmup_question']
            request=QueryRequest(question=question,mode=task['mode'],corpus_version=backend.config['corpus_version'])
            save(case/'question.json',request.model_dump(mode='json'))
            row={'task':task,'question_sha256':digest(question),'status':'started'};summary['cases'].append(row);save(folder/'summary.json',summary)
            print(('MEASURED ' if task['measured'] else 'WARMUP ')+identifier,flush=True)
            started=time.perf_counter()
            try:
                result=backend.execute(task,question,case)
                backend.check_model()
                row.update(result)
            except (KeyboardInterrupt,EOFError):
                row.update(status='interrupted',stage=getattr(backend,'stage','unknown'));raise
            except Exception as error:
                row.update(status='failed',stage=getattr(backend,'stage','unknown'),error_type=type(error).__name__,
                           execution_time_ms=(time.perf_counter()-started)*1000)
            finally:
                row['files_sha256']={p.name:sha256_file(p) for p in case.iterdir() if p.is_file() and p.name!='case_receipt.json'}
                save(case/'case_receipt.json',row);save(folder/'summary.json',summary)
            if row['status'] in TERMINAL and (task['measured'] or row['status']!='failed'):
                complete[identifier]={'run':str(folder),**row}
            if not task['measured'] and row['status']=='failed':
                summary['status']='warmup_failed';break
        else:
            summary['integrity_check_started']=True
            backend.check_graph();verify_files(repo,plan)
            summary.update(status='attempted',final_graph_verified=True)
    except (KeyboardInterrupt,EOFError):
        interrupted=True;summary['status']='interrupted'
    except Exception as error:
        summary.update(status='stopped',error_type=type(error).__name__,stage=getattr(backend,'stage','setup'))
        if summary.get('integrity_check_started'):summary['integrity_error']=True
    finally:
        if backend is not None:
            try:backend.close()
            except Exception as error:summary['close_error_type']=type(error).__name__
        measured=[r for r in complete.values() if r['task']['measured']]
        summary.update(measured_terminal_count=len(measured),measured_failure_count=sum(r['status']=='failed' for r in measured),
                       measured_abstention_count=sum(r['status']=='abstained' for r in measured),
                       finished_at=datetime.now(timezone.utc).isoformat())
        save(folder/'summary.json',summary)
    print(f'FINAL QA {summary["status"].upper()}: {summary["measured_terminal_count"]}/240 measured outcomes; '
          f'{summary["measured_failure_count"]} failures; {summary["measured_abstention_count"]} abstentions.',flush=True)
    print('Saved final run:',folder,flush=True)
    return 2 if interrupted else (0 if summary['status']=='attempted' and not summary['measured_failure_count'] else 1)
