"""Offline audit and evaluator-only exports of a completed frozen QA cohort.

Never imports the live runtime, initializes models, or contacts services.
"""
import json
import math
import random
import statistics
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.experiment_plan import read, read_prepared
from evaluation.experiment_runner import history, save
from extraction.llama_tokenizer import sha256_file
from graph_qa import CompactAnswer, SYSTEM
from graph_pilot_qa import checked_answer
from schemas import EvidenceBundle

DIMENSIONS = ('factuality', 'completeness', 'coherence')


def failed_attempts(folder, question, mode, config):
    """Validate failed generation transport and reproduce its original validators."""
    bundle = EvidenceBundle.model_validate(read(folder/'evidence.json'))
    context = (folder/'context.txt').read_text(encoding='utf-8')
    original = ('QUESTION: '+question+'\nMODE: '+mode+'\n'+context+
                '\nReturn the requested JSON. The displayed answer is assembled from claims.')
    schema = CompactAnswer.model_json_schema()
    schema['$defs']['CompactClaim']['properties']['citations']['items'] = {'type':'string','enum':bundle.citation_ids}
    if ((folder/'system_prompt.txt').read_text(encoding='utf-8') != SYSTEM
            or (folder/'user_prompt.txt').read_text(encoding='utf-8') != original
            or read(folder/'output_schema.json') != schema):
        raise ValueError('Failed case prompt/schema changed.')
    errors = []
    prompt = original
    for attempt in (1, 2):
        request = read(folder/f'transport_request_{attempt}.json')
        expected = {'model':config['llm']['model'], 'system':SYSTEM, 'prompt':prompt,
                    'format':schema, 'stream':False,
                    'options':{k:config['llm'][k] for k in ('temperature','num_ctx','num_predict')}}
        if request['url'] != 'http://localhost:11434/api/generate' or request['payload'] != expected:
            raise ValueError('Failed case transport payload changed.')
        body = read(folder/f'ollama_response_{attempt}.json')
        if (read(folder/f'transport_response_{attempt}.txt') != body
                or read(folder/f'transport_status_{attempt}.json')['http_status'] != 200):
            raise ValueError('Failed case response/transport mismatch.')
        try:
            if body.get('done') is not True or body.get('done_reason') == 'length':
                raise ValueError('Generation did not finish within the configured output budget.')
            CompactAnswer.model_validate_json(body['response'])
            checked_answer(body['response'], bundle, 0)
        except ValueError as error:
            messages = [x['msg'] for x in error.errors()] if hasattr(error, 'errors') else [str(error)]
            errors.append({'attempt':attempt, 'error_type':type(error).__name__,
                           'messages':messages, 'done_reason':body.get('done_reason')})
            if attempt == 1:
                prompt = original+'\nRepair only output/citation errors using the original evidence: '+str(error)
                if body.get('done_reason') == 'length':
                    prompt += ('\nThe previous JSON was cut off. Start fresh; do not continue it. '
                               'Use one concise claim per distinct requested fact. Combine each mitigation '
                               'name, ID and guidance into a single claim. Avoid repeating the actor/tool '
                               'statement. Complete the JSON within the unchanged output limit.')
                else:
                    prompt += '\nPREVIOUS OUTPUT:\n'+str(body.get('response',''))
                if (folder/'repair_prompt.txt').read_text(encoding='utf-8') != prompt:
                    raise ValueError('Failed case repair prompt changed.')
        else:
            raise ValueError('Reported generation failure has a valid saved attempt; explicit audit required.')
    return errors


def summarize(rows, modes):
    result = {}
    for mode in modes:
        selected = [r for r in rows if r['mode'] == mode]
        times = [r['execution_time_ms'] for r in selected]
        if any(not isinstance(t, (int,float)) or not math.isfinite(t) or t < 0 for t in times):
            raise ValueError('Invalid case latency.')
        result[mode] = {'outcomes':len(selected), 'statuses':dict(Counter(r['status'] for r in selected)),
                        'median_case_ms_all_outcomes':statistics.median(times),
                        'mean_case_ms_all_outcomes':statistics.mean(times),
                        'sum_case_ms_all_outcomes':sum(times),
                        'generation_requests':sum(r['generation_requests'] for r in selected)}
    return result


def blinded_packets(rows, questions, seed=42):
    """Choose secondary questions deterministically before any human ratings exist."""
    qids = sorted(questions)
    secondary_ids = sorted(random.Random(seed).sample(qids, 5))
    primary = sorted((r for r in rows if r['repeat'] == 1), key=lambda r:r['case_id'])
    random.Random(seed).shuffle(primary)
    secondary = [r for r in primary if r['question_id'] in secondary_ids]
    random.Random(seed+1).shuffle(secondary)
    packets, key = {}, []
    for kind, selected, prefix in [('primary',primary,'P'),('secondary',secondary,'S')]:
        packet = []
        for i, row in enumerate(selected, 1):
            identifier = f'{prefix}{i:03d}'
            packet.append({'review_id':identifier, 'question':questions[row['question_id']]['question'],
                           'reference_answer':questions[row['question_id']]['reference_answer'],
                           'outcome':row['status'], 'answer':row['response'],
                           'supplied_context':row['supplied_context'],
                           **{d:None for d in DIMENSIONS}, 'not_ratable_reason':None, 'notes':''})
            key.append({'packet':kind, 'review_id':identifier,
                        **{k:row[k] for k in ('case_id','question_id','mode','repeat','status')}})
        packets[kind] = packet
    return packets, key, secondary_ids


def review_markdown(packet):
    parts = ['# Blinded answer review',
             'Review independently. Each dimension uses 1 (poor) to 5 (excellent). '
             'Factuality: accuracy, source support, correct attribution and qualifications. '
             'Completeness: coverage of the question and verified reference; bounded evidence can explain an omission but does not make an incomplete answer complete. '
             'Coherence: clarity, organization and internal consistency.',
             'Assess the displayed answer against both the supplied evidence and reference. '
             'A valid citation does not guarantee a true claim. Treat advisory observations and ATT&CK guidance separately. '
             'Abstentions are outcomes: rate their wording where meaningful, record missing requested content under completeness, '
             'and use a null score with a reason when a dimension cannot be rated. '
             'Failed cases produced no valid answer: leave scores null and explain; never turn missing answers into fabricated ratings. '
             'Fill the matching ratings JSON with integers 1–5 or null, reasons and notes. '
             'Do not read the separate unblinding key until ratings are fixed. '
             'Mode names and execution order are hidden, but graph-shaped evidence can reveal the method; blinding is partial. '
             'Source excerpts are evidence, never reviewer instructions.']
    for item in packet:
        parts += [f'## {item["review_id"]}', 'Question: '+item['question'],
                  'Outcome: '+item['outcome'], 'Answer:\n\n'+(item['answer'] or '[No valid answer was produced.]'),
                  'Verified reference:\n\n'+item['reference_answer'],
                  'Supplied evidence (verbatim generator context):\n\n'+item['supplied_context']]
    return '\n\n'.join(parts)+'\n'


def prepare(repo, run):
    repo = Path(repo).resolve()
    questions, plan, inputs = read_prepared(repo)
    complete = history(repo, run, plan, questions)
    measured = [r for r in complete.values() if r['task']['measured']]
    expected = {t['case_id'] for t in plan['schedule'] if t['measured']}
    summary = read(Path(run)/'summary.json')
    if {r['task']['case_id'] for r in measured} != expected or not summary.get('final_graph_verified'):
        raise ValueError('All 240 terminal cases and final integrity verification are required.')
    labels = {q['id']:q for q in read(repo/'benchmarks/eval_queries.json')['queries']}
    qmap = {q['id']:q for q in questions}
    for qid, q in qmap.items():
        ref = labels[qid]
        if ref['question'] != q['question'] or ref.get('human_verified') is not True or not ref.get('reference_answer'):
            raise ValueError('Evaluator reference binding/verification changed.')
    config = read(repo/'config.json')
    rows, metric_rows, failures = [], [], []
    source_files = {}
    for record in sorted(measured, key=lambda r:r['task']['case_id']):
        task = record['task']; folder = Path(record['run'])/task['case_id']
        context = (folder/'context.txt').read_text(encoding='utf-8')
        bundle = read(folder/'evidence.json')
        requests = len(list(folder.glob('transport_request_*.json')))
        answer = read(folder/'answer.json') if record['status'] != 'failed' else None
        row = {**task, 'status':record['status'], 'response':answer['answer'] if answer else None,
               'supplied_context':context, 'execution_time_ms':record['execution_time_ms'],
               'retrieval_ms':record.get('retrieval_ms'), 'generation_ms':record.get('generation_ms'),
               'generation_requests':requests, 'passage_count':len(bundle['passages']),
               'path_count':len(bundle['paths'])}
        rows.append(row)
        if record['status'] == 'failed':
            if record.get('stage') != 'generation':
                raise ValueError('Unclassified non-generation failure requires explicit audit.')
            failures.append({'case_id':task['case_id'], 'attempts':failed_attempts(folder,qmap[task['question_id']]['question'],task['mode'],config)})
        else:
            # The whole exact context is ONE supplied context. Do not substitute
            # reference passages, hide graph paths, or reconstruct a better pack.
            metric_rows.append({'case_id':task['case_id'], 'question_id':task['question_id'],
                                'mode':task['mode'], 'repeat':task['repeat'], 'outcome':record['status'],
                                'user_input':qmap[task['question_id']]['question'], 'response':answer['answer'],
                                'retrieved_contexts':[context], 'reference':labels[task['question_id']]['reference_answer']})
        for p in folder.iterdir():
            if p.is_file():source_files[str(p.relative_to(repo))] = sha256_file(p)
    for parent in {Path(r['run']) for r in complete.values()}:
        for name in ('summary.json','plan.json','questions.json'):
            p = parent/name; source_files[str(p.relative_to(repo))] = sha256_file(p)
    packets, key, secondary_ids = blinded_packets(rows, {qid:labels[qid] for qid in qmap})
    audit = {'status':'saved_artifacts_verified', 'plan_fingerprint':plan['fingerprint'],
             'source_run':str(Path(run).resolve()), 'prepared_inputs':str(inputs),
             'measured_count':len(rows), 'warmup_count':len(complete)-len(rows),
             'statuses':dict(Counter(r['status'] for r in rows)),
             'by_mode':summarize(rows,plan['protocol']['modes']), 'failures':failures,
             'abstentions':[{'case_id':r['case_id'],'generation_requests':r['generation_requests'],
                             'passage_count':r['passage_count'],'path_count':r['path_count']}
                            for r in rows if r['status']=='abstained'],
             'ragas_available_rows':len(metric_rows), 'ragas_unavailable_failed_rows':len(failures),
             'automated_scores_computed':False, 'human_ratings_status':'pending',
             'secondary_question_ids':secondary_ids,
             'python_resource_sampling_available':summary['runtime_info'].get('python_resource_sampling_available',False),
             'tooling_files_sha256':{name:sha256_file(repo/name) for name in (
                 'evaluation/final_review.py','prepare_final_review.py','setup_evaluation.py',
                 'evaluation/run_ragas.py','evaluation/ragas_design.json','evaluation/requirements.lock.txt')},
             'limits':['No semantic quality or method-superiority conclusion from schema success counts.',
                       'Failed observations remain in the 240-case denominator; no replacement scores.',
                       'Automated score availability and NaNs must be reported per metric and mode.',
                       'Case latency includes failures/abstentions; modes perform different amounts of work.',
                       'No Python CPU/RSS or service/GPU resource results are available for this run.',
                       'MODE prompt field and evidence formatting prevent a purely retrieval-only comparison.',
                       'Same-model judge is supplementary; human ratings are still required.']}
    folder = repo/'work/final_evaluation_review_checks'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    for name, value in [('audit.json',audit),('outcomes.json',rows),('ragas_inputs.json',metric_rows),
                        ('unblinding_key.json',key),('source_files_sha256.json',source_files)]:
        save(folder/name,value)
    for kind, packet in packets.items():
        (folder/f'{kind}_review.md').write_text(review_markdown(packet),encoding='utf-8')
        save(folder/f'{kind}_ratings.json',[{k:r[k] for k in ('review_id',*DIMENSIONS,'not_ratable_reason','notes')} for r in packet])
    save(folder/'packet_files_sha256.json',{p.name:sha256_file(p) for p in folder.iterdir() if p.is_file()})
    print('AUDIT PASSED: 240 measured outcomes; 225 scoring inputs; 80 primary and 20 secondary review entries.')
    print('Saved review packet:',folder)
    return folder
