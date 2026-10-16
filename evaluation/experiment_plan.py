"""Question-only experiment inputs, frozen methods/assets and seeded paired schedule."""
import json
import random
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

from evaluation.corpus_scope import EvaluationGraphRetriever
from evaluation.index_assets import checked_graph_index,checked_text_index,GRAPH_RUN,TEXT_RUN
from extraction.llama_tokenizer import sha256_file
from graph.development_projection import digest,freeze_projection
from graph_qa import DEMO_QUESTIONS
from retrieval.hybrid_retrieval import saved_projection_rows
from retrieval.development_text import load_tokenizer,wordpieces
from schemas import QueryRequest

KIND = 'final_evaluation_inputs'
CODE = ['evaluation/index_assets.py','evaluation/retrievers.py','evaluation/experiment_plan.py',
        'evaluation/experiment_runner.py','evaluation/experiment_runtime.py',
        'evaluation/corpus_scope.py','evaluation/text_sources.py','prepare_final_evaluation.py','run_final_evaluation.py']


def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))


def project_questions(dataset,split):
    """The mixed benchmark file is read only here; only these fields leave it.

    Reference answers, expected facts, paths and evidence labels are never
    included in the exported input or passed to retrieval/generation.
    """
    rows = dataset['queries']
    if len({r['id'] for r in rows})!=len(rows):raise ValueError('Duplicate benchmark question ID.')
    by_id = {r['id']:r for r in rows}
    ids = split['final_evaluation_query_ids']
    if len(ids)!=20 or len(set(ids))!=20:raise ValueError('Exactly twenty frozen final questions are required.')
    selected = []
    for identifier in ids:
        row = by_id[identifier]
        if row.get('verified') is not True or row.get('split')!='held_out' or not row['question'].strip():
            raise ValueError('Final question assignment/verification changed.')
        selected.append({key:row[key] for key in ['id','question','category']})
    if dict(Counter(r['category'] for r in selected))!=split['final_evaluation_category_counts']:
        raise ValueError('Final question category mix changed.')
    return selected


def schedule(questions,protocol):
    rng = random.Random(protocol['randomization_seed'])
    modes = protocol['modes']
    warmups = [{'case_id':'warmup-'+m,'question_id':'warmup','mode':m,'repeat':0,'measured':False} for m in modes]
    rng.shuffle(warmups)
    tasks = []
    for repeat in range(1,protocol['repeats']+1):
        block = [{'case_id':f'r{repeat}-{q["id"]}-{m}','question_id':q['id'],'mode':m,
                  'repeat':repeat,'measured':True} for q in questions for m in modes]
        rng.shuffle(block);tasks.extend(block)
    if len(tasks)!=protocol['measured_answer_runs']:raise ValueError('Measured schedule differs from frozen protocol.')
    return warmups+tasks


def audit_projection(graph,projection):
    rows = saved_projection_rows(SimpleNamespace(projection=projection),graph)
    nodes = {n['canonical_id']:n for n in projection['nodes']}
    edges = [{'head':nodes[e['head_id']],'tail':nodes[e['tail_id']],'predicate':e['predicate'],
              'assertion_ids':[s['assertion']['assertion_id'] for s in e['support']]} for e in projection['edges']]
    rebuilt,fingerprint = freeze_projection(graph,edges,rows)
    if rebuilt!=projection:raise ValueError('Saved graph differs from reconstructed source provenance.')
    return fingerprint


def prepare(repo):
    repo = Path(repo).resolve()
    graph = EvaluationGraphRetriever(repo)
    text,_,_,_ = checked_text_index(repo,graph.config['evaluation_scope'])
    receipt,manifest,projection,ids,raw,vectors = checked_graph_index(repo,graph.config['evaluation_scope'])
    if audit_projection(graph,projection)!=manifest['projection_sha256']:
        raise ValueError('Saved live projection source verification failed.')
    source_pointer = read(repo/'work/evaluation_corpus_chunks/current.json')
    source_summary = repo/'work/evaluation_corpus_chunks'/source_pointer['run']/'summary.json'
    protocol = read(source_summary)['identity']['protocol']
    for name,expected in protocol['implementation_sha256'].items():
        if sha256_file(repo/name)!=expected:raise ValueError('Frozen source/generation/retrieval implementation changed.')
    split = read(repo/'benchmarks/split_manifest.json')
    questions = project_questions(read(repo/'benchmarks/eval_queries.json'),split)
    if [q['id'] for q in questions]!=protocol['question_ids']:raise ValueError('Frozen final assignment changed.')
    tokenizer=load_tokenizer(repo,graph.config)
    special=tokenizer.num_special_tokens_to_add(pair=False)
    question_checks=[]
    for q in questions:
        QueryRequest(question=q['question'],mode='graph_only',corpus_version=graph.config['corpus_version'])
        count=wordpieces(tokenizer,q['question'])+special
        question_checks.append({'question_id':q['id'],'characters':len(q['question']),
                                'minilm_tokens_including_specials':count,'within_minilm_limit':count<=256})
    files = set(CODE)|set(protocol['implementation_sha256'])|{
        'config.json','benchmarks/eval_queries.json','benchmarks/split_manifest.json','benchmarks/corpus_manifest.json',
        'data/enterprise-attack-17.1.json','work/evaluation_graph_index/current.json','work/graph_index/current.json',
        str(source_summary.relative_to(repo)),
        f'work/evaluation_text_index_runs/{TEXT_RUN}/index_receipt.json',
        f'work/evaluation_graph_index_runs/{GRAPH_RUN}/index_receipt.json',
        str(Path(text['records_path']).relative_to(repo)),str((Path(text['records_path']).parent/'manifest.json').relative_to(repo)),
        str(Path(manifest['projection_path']).relative_to(repo)),str(Path(manifest['vectors_path']).relative_to(repo)),
        str(Path(receipt['manifest_path']).relative_to(repo))}
    files.update('data/'+p['document'].doc_id+'.txt' for p in graph.profiles.values())
    plan = {'version':1,'purpose':'frozen_final_four_mode_answer_experiment','evaluation_scope':graph.config['evaluation_scope'],
            'request_timeout_seconds':60,
            'text_index_fingerprint':text['fingerprint'],'graph_index_fingerprint':manifest['index_fingerprint'],
            'projection_sha256':manifest['projection_sha256'],'questions_sha256':digest(questions),'protocol':protocol,
            'question_input_checks':question_checks,
            'warmup_question':DEMO_QUESTIONS[1],'schedule':schedule(questions,protocol),
            'frozen_files_sha256':{str(p):sha256_file(repo/p) for p in sorted(files)},
            'latency_policy':'Initialize all retrievers/vector bindings before warmups. Measured case time covers retrieval, packing, generation/repair and initial answer/evidence persistence; excludes setup, file/model guards and final timing/receipt updates. Record retrieval_ms and generation_ms separately.',
            'resume_policy':'Skip valid terminal measured answers, abstentions and failures; rerun only interrupted/unstarted measured cases. Each resumed operator launch repeats four excluded warmups before unfinished measurements. Preserve every warmup/run/attempt.',
            'scope_policy':'All modes use the same fixed reviewed source/reference scope; generator and retrieval settings unchanged.',
            'reference_isolation':'Only id, question and category are exported from the benchmark; only question/mode/corpus_version reach QueryRequest.'}
    plan['fingerprint'] = digest(plan)
    return questions,plan


def save_prepared(repo):
    repo = Path(repo).resolve();questions,plan = prepare(repo)
    folder = repo/'work'/KIND/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    for name,value in [('questions.json',questions),('plan.json',plan)]:
        (folder/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (folder.parent/'current.json').write_text(json.dumps({'run':folder.name,'fingerprint':plan['fingerprint']},indent=2)+'\n',encoding='utf-8')
    print('PREPARED:',len(questions),'final questions; 240 measured cases and four warmups. No model/database calls.')
    print('Plan:',plan['fingerprint'],'\nSaved inputs:',folder)
    return folder


def verify_files(repo,plan,*,full=True):
    for name,expected in plan['frozen_files_sha256'].items():
        path = Path(repo)/name
        if not full and path.stat().st_size>4_000_000:continue
        if sha256_file(path)!=expected:raise ValueError('Frozen experiment file changed: '+name)


def read_prepared(repo):
    repo = Path(repo).resolve();pointer=read(repo/'work'/KIND/'current.json')
    import re
    if not re.fullmatch(r'\d{8}T\d{6}Z-[a-f0-9]{8}',pointer['run']):raise ValueError('Invalid final input pointer.')
    folder = repo/'work'/KIND/pointer['run'];plan=read(folder/'plan.json');questions=read(folder/'questions.json')
    if (digest({k:v for k,v in plan.items() if k!='fingerprint'})!=plan['fingerprint']
            or pointer['fingerprint']!=plan['fingerprint'] or digest(questions)!=plan['questions_sha256']
            or any(set(q)!={'id','question','category'} for q in questions)
            or plan['schedule']!=schedule(questions,plan['protocol'])):
        raise ValueError('Prepared final inputs, plan or schedule changed.')
    verify_files(repo,plan)
    return questions,plan,folder
