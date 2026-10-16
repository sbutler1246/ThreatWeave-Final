"""Frozen schedule, reference isolation, real generator with fake services and resume."""
import copy
import io
import json
import tempfile
import unittest
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from evaluation import experiment_plan as planning,experiment_runner as runner
from evaluation.experiment_runtime import Runtime
from evaluation import retrievers
from evaluation.index_assets import checked_graph_index,checked_text_index
from extraction.llama_tokenizer import MODEL_DIGEST,sha256_file
from graph.development_projection import digest
from graph.development_retrieval import evidence_context
from graph_qa import generate
from retrieval.text_retrieval import DevelopmentTextRetriever
from retrieval.graph_vectors import GraphVectorIndex
from retrieval.combined_retrieval import DevelopmentCombinedRetriever
from retrieval.hybrid_retrieval import DevelopmentHybridRetriever
from retrieval.development_text import metadata
from schemas import EvidenceBundle,Passage,GraphPath,RelationshipEdge,QueryRequest

REPO=Path(__file__).resolve().parents[1]
MODES=['text_only','graph_only','hybrid_no_node2vec','hybrid']


def question_fixture():
    categories=['actor_software_technique']*8+['technique_mitigation']*8+['cross_report_comparison']*4
    rows=[{'id':f'Q{i+1:03d}','question':'What software does Group Alpha use?', 'category':c,
           'verified':True,'split':'held_out','reference_answer':'GOLD_LEAK_SENTINEL',
           'expected_facts':['FACT_LEAK_SENTINEL'],'required_paths':['PATH_LEAK_SENTINEL']} for i,c in enumerate(categories)]
    split={'final_evaluation_query_ids':[q['id'] for q in rows],
           'final_evaluation_category_counts':dict(Counter(categories))}
    return {'queries':rows},split


class PlanTests(unittest.TestCase):
    def test_only_explicit_question_fields_leave_the_mixed_dataset(self):
        data,split=question_fixture();questions=planning.project_questions(data,split)
        self.assertEqual(len(questions),20)
        self.assertTrue(all(set(q)=={'id','question','category'} for q in questions))
        for sentinel in ['GOLD_LEAK_SENTINEL','FACT_LEAK_SENTINEL','PATH_LEAK_SENTINEL']:
            self.assertNotIn(sentinel,json.dumps(questions))

    def test_changed_assignment_duplicate_ids_and_unverified_questions_are_rejected(self):
        for kind in ['duplicate','unverified','category','missing']:
            data,split=question_fixture()
            if kind=='duplicate':data['queries'].append(copy.deepcopy(data['queries'][0]))
            if kind=='unverified':data['queries'][0]['verified']=False
            if kind=='category':data['queries'][0]['category']='cross_report_comparison'
            if kind=='missing':split['final_evaluation_query_ids'].pop()
            with self.subTest(kind=kind),self.assertRaises(ValueError):planning.project_questions(data,split)

    def test_seeded_schedule_preserves_240_paired_runs_and_four_excluded_warmups(self):
        data,split=question_fixture();questions=planning.project_questions(data,split)
        protocol={'randomization_seed':42,'modes':MODES,'repeats':3,'measured_answer_runs':240}
        tasks=planning.schedule(questions,protocol)
        self.assertEqual(tasks,planning.schedule(questions,protocol))
        self.assertEqual(len(tasks),244)
        self.assertEqual(len({t['case_id'] for t in tasks}),244)
        self.assertEqual(Counter(t['mode'] for t in tasks if t['measured']),{m:60 for m in MODES})
        self.assertEqual(Counter(t['repeat'] for t in tasks if t['measured']),{1:80,2:80,3:80})
        self.assertTrue(all(not t['measured'] and t['repeat']==0 for t in tasks[:4]))
        self.assertEqual(len({(t['question_id'],t['mode'],t['repeat']) for t in tasks if t['measured']}),240)

    def test_inherited_retrieval_neighbor_and_packing_methods_are_unchanged(self):
        self.assertIs(retrievers.EvaluationTextRetriever.retrieve,DevelopmentTextRetriever.retrieve)
        self.assertIs(retrievers.EvaluationGraphVectorIndex.neighbors,GraphVectorIndex.neighbors)
        self.assertIs(retrievers.EvaluationCombinedRetriever._retrieve,DevelopmentCombinedRetriever._retrieve)
        self.assertIs(retrievers.EvaluationHybridRetriever._retrieve,DevelopmentHybridRetriever._retrieve)

    def test_operator_cannot_change_the_frozen_timeout_between_cases(self):
        import run_final_evaluation
        with patch('sys.argv',['run_final_evaluation.py','--preview','--timeout','61']),patch.object(
                run_final_evaluation,'read_prepared',return_value=([],{'request_timeout_seconds':60},REPO)),redirect_stdout(io.StringIO()):
            with patch('sys.stderr',io.StringIO()),self.assertRaises(SystemExit) as error:run_final_evaluation.main()
        self.assertEqual(error.exception.code,2)


class Response:
    def __init__(self,body,status=200):self.body,self.status_code=body,status
    @property
    def text(self):return json.dumps(self.body)
    def json(self):return copy.deepcopy(self.body)
    def raise_for_status(self):
        if self.status_code>=400:raise RuntimeError('simulated HTTP failure')


class Http:
    def __init__(self,truncate=False,error=False):self.requests=[];self.truncate=truncate;self.error=error;self.closed=False
    def post(self,url,**kwargs):
        self.requests.append(copy.deepcopy(kwargs['json']))
        if self.error:return Response({'error':'simulated'},500)
        raw=json.dumps({'answer':'See cited claims.','claims':[{'text':'Group Alpha used Tool Beta.','citations':['E1']}],'abstained':False})
        return Response({'done':True,'done_reason':'length' if self.truncate and len(self.requests)==1 else 'stop',
                         'response':raw,'prompt_eval_count':100,'eval_count':25})
    def get(self,*args,**kwargs):return Response({'models':[{'name':'llama3.1:8b','digest':MODEL_DIGEST}]})
    def close(self):self.closed=True


class Retriever:
    def __init__(self,config,empty=False):
        self.config=config;self.empty=empty;self.configuration_hash='a'*64;self.last_context='';self.last_stats={}
    def retrieve(self,request):
        text='Group Alpha used Tool Beta.'
        p=Passage(citation_id='E1',doc_id='fixture',chunk_id='fixture:source',source_url='https://example.org/source',
                  text=text,start=0,end=len(text),source_kind='cisa')
        paths=[] if self.empty else [GraphPath(path_id='P1',edges=[RelationshipEdge(head_id='local:g',predicate='USES',
                         tail_id='local:s',assertion_ids=['assertion:fixture'],citation_ids=['E1'])])]
        bundle=EvidenceBundle(passages=[] if self.empty else [p],paths=paths if request.mode.value!='text_only' else [],
                              citation_ids=[] if self.empty else ['E1'],retrieval_ms=1,
                              configuration_hash=self.configuration_hash,corpus_version=self.config['corpus_version'])
        self.last_context=evidence_context(bundle,{})
        self.last_stats={'evidence_utf8_bytes':len(self.last_context.encode()),'selected_chunk_ids':[]}
        return bundle


def fake_runtime(repo,plan,*,truncate=False,empty=False,error=False,interrupt_at=None,fail_case=None,graph_error=False):
    runtime=Runtime.__new__(Runtime)
    runtime.repo=Path(repo);runtime.plan=plan;runtime.config=planning.read(Path(repo)/'config.json')
    runtime.timeout=60;runtime.http=Http(truncate,error);runtime.driver=SimpleNamespace(close=lambda:None)
    runtime.stage='setup';runtime.process=None;runtime.runtime_info={'fixture':True}
    runtime.retrievers={m:Retriever(runtime.config,empty) for m in MODES}
    original=runtime.execute;counter={'measured':0}
    def execute(task,question,folder):
        if task['measured']:
            counter['measured']+=1
            if counter['measured']==interrupt_at:raise KeyboardInterrupt()
        if task['case_id']==fail_case:raise ValueError('simulated retrieval failure')
        return original(task,question,folder)
    def check_graph():
        runtime.stage='graph_freshness'
        if graph_error:raise ValueError('simulated changed graph')
    runtime.execute=execute;runtime.check_graph=check_graph
    return runtime


class ExecutionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=REPO/'work');self.addCleanup(self.tmp.cleanup)
        self.repo=Path(self.tmp.name)
        (self.repo/'config.json').write_bytes((REPO/'config.json').read_bytes())
        data,split=question_fixture();self.questions=planning.project_questions(data,split)[:2]
        protocol={'randomization_seed':42,'modes':MODES,'repeats':1,'measured_answer_runs':8,'model_digest':MODEL_DIGEST}
        self.plan={'protocol':protocol,'schedule':planning.schedule(self.questions,protocol),'warmup_question':'What software does Group Alpha use?',
                   'frozen_files_sha256':{'config.json':sha256_file(self.repo/'config.json')}}
        self.plan['fingerprint']=digest(self.plan)

    def run_batch(self,**kwargs):
        backend=fake_runtime(self.repo,self.plan,**kwargs)
        with redirect_stdout(io.StringIO()):code=runner.run(self.repo,self.questions,self.plan,lambda:backend)
        folder=next((self.repo/'work'/runner.KIND).iterdir())
        return code,folder,backend

    def test_reference_sentinels_never_enter_real_frozen_generator_payloads(self):
        code,folder,backend=self.run_batch()
        self.assertEqual(code,0)
        self.assertEqual(len(backend.http.requests),12)
        for request in backend.http.requests:
            self.assertEqual(request['options'],{'temperature':0,'num_ctx':8192,'num_predict':700})
            self.assertIn('MODE:',request['prompt'])
            for sentinel in ['GOLD_LEAK_SENTINEL','FACT_LEAK_SENTINEL','PATH_LEAK_SENTINEL','reference_answer']:
                self.assertNotIn(sentinel,json.dumps(request))
        saved=runner.history(self.repo,folder,self.plan,self.questions)
        self.assertEqual(len(saved),12)
        self.assertEqual(sum(r['task']['measured'] for r in saved.values()),8)

    def test_interrupt_resume_preserves_completed_cases_and_reruns_only_uncommitted_cases(self):
        code,folder,backend=self.run_batch(interrupt_at=2)
        self.assertEqual(code,2)
        prior=runner.history(self.repo,folder,self.plan,self.questions)
        self.assertEqual(sum(r['task']['measured'] for r in prior.values()),1)
        hashes={str(p):sha256_file(p) for p in folder.rglob('*') if p.is_file()}
        other=fake_runtime(self.repo,self.plan)
        with redirect_stdout(io.StringIO()):result=runner.run(self.repo,self.questions,self.plan,lambda:other,resume=folder)
        self.assertEqual(result,0)
        self.assertEqual(len(other.http.requests),11)  # four fresh excluded warmups plus seven pending measurements
        self.assertTrue(all(sha256_file(Path(p))==value for p,value in hashes.items()))
        latest=next(p for p in (self.repo/'work'/runner.KIND).iterdir() if p!=folder)
        complete=runner.history(self.repo,latest,self.plan,self.questions)
        self.assertEqual(sum(r['task']['measured'] for r in complete.values()),8)

    def test_measured_failures_remain_terminal_and_are_not_regenerated(self):
        task=next(t for t in self.plan['schedule'] if t['measured'])
        code,folder,backend=self.run_batch(fail_case=task['case_id'])
        self.assertEqual(code,1)
        complete=runner.history(self.repo,folder,self.plan,self.questions)
        self.assertEqual(complete[task['case_id']]['status'],'failed')
        factory=SimpleNamespace()
        with patch.object(factory,'start',create=True,side_effect=AssertionError('No rerun')) as call,redirect_stdout(io.StringIO()):
            self.assertEqual(runner.run(self.repo,self.questions,self.plan,call,resume=folder),1)
        call.assert_not_called()

    def test_empty_evidence_abstentions_make_no_generation_calls_and_resume_validates(self):
        code,folder,backend=self.run_batch(empty=True)
        self.assertEqual(code,0);self.assertEqual(backend.http.requests,[])
        complete=runner.history(self.repo,folder,self.plan,self.questions)
        self.assertTrue(all(r['status']=='abstained' and r['attempts']==0 for r in complete.values()))

    def test_truncation_uses_exact_existing_one_repair_and_saved_raw_responses(self):
        code,folder,backend=self.run_batch(truncate=True)
        self.assertEqual(code,0)
        rows=planning.read(folder/'summary.json')['cases']
        self.assertEqual(rows[0]['attempts'],2)
        self.assertIn('previous JSON was cut off',backend.http.requests[1]['prompt'])
        self.assertNotIn('PREVIOUS OUTPUT:',backend.http.requests[1]['prompt'])
        runner.history(self.repo,folder,self.plan,self.questions)

    def test_http_error_body_is_preserved_and_warmup_failure_stops_measured_work(self):
        code,folder,backend=self.run_batch(error=True)
        self.assertEqual(code,1)
        summary=planning.read(folder/'summary.json')
        self.assertEqual(summary['status'],'warmup_failed')
        self.assertEqual(summary['measured_terminal_count'],0)
        case=folder/summary['cases'][0]['task']['case_id']
        self.assertIn('simulated',(case/'transport_response_1.txt').read_text(encoding='utf-8'))
        self.assertEqual(planning.read(case/'transport_status_1.json')['http_status'],500)
        self.assertEqual(runner.history(self.repo,folder,self.plan,self.questions),{})

    def test_changed_graph_final_check_marks_integrity_failure_and_blocks_automatic_resume(self):
        code,folder,backend=self.run_batch(graph_error=True)
        self.assertEqual(code,1)
        self.assertTrue(planning.read(folder/'summary.json')['integrity_error'])
        with self.assertRaisesRegex(ValueError,'integrity'):runner.history(self.repo,folder,self.plan,self.questions)

    def test_model_change_after_generation_is_retained_as_failed_warmup(self):
        backend=fake_runtime(self.repo,self.plan);original=backend.check_model;calls={'n':0}
        def changed():
            calls['n']+=1
            if calls['n']==2:
                backend.stage='model';raise ValueError('simulated changed digest')
            return original()
        backend.check_model=changed
        with redirect_stdout(io.StringIO()):result=runner.run(self.repo,self.questions,self.plan,lambda:backend)
        self.assertEqual(result,1)
        folder=next((self.repo/'work'/runner.KIND).iterdir());summary=planning.read(folder/'summary.json')
        self.assertEqual((summary['status'],summary['cases'][0]['status']),('warmup_failed','failed'))
        self.assertTrue((folder/summary['cases'][0]['task']['case_id']/'answer.json').exists())
        self.assertEqual(runner.history(self.repo,folder,self.plan,self.questions),{})

    def test_failed_warmup_resume_preserves_failure_and_runs_fresh_excluded_warmups(self):
        code,folder,backend=self.run_batch(error=True)
        original={str(p):sha256_file(p) for p in folder.rglob('*') if p.is_file()}
        other=fake_runtime(self.repo,self.plan)
        with redirect_stdout(io.StringIO()):result=runner.run(self.repo,self.questions,self.plan,lambda:other,resume=folder)
        self.assertEqual(result,0);self.assertEqual(len(other.http.requests),12)
        self.assertTrue(all(sha256_file(Path(p))==h for p,h in original.items()))

    def test_changed_case_file_frozen_config_or_resume_cycle_is_rejected(self):
        code,folder,backend=self.run_batch()
        question=next(folder.glob('*/question.json'));original=question.read_bytes()
        question.write_text('{}',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'artifacts changed'):runner.history(self.repo,folder,self.plan,self.questions)
        question.write_bytes(original)
        summary=planning.read(folder/'summary.json');summary['resume_of']=str(folder);runner.save(folder/'summary.json',summary)
        with self.assertRaisesRegex(ValueError,'cycle'):runner.history(self.repo,folder,self.plan,self.questions)
        (self.repo/'config.json').write_text('{}',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Frozen experiment file changed'):planning.verify_files(self.repo,self.plan)

    def test_successful_model_output_cannot_override_its_saved_citations(self):
        code,folder,backend=self.run_batch()
        case=next(p for p in folder.iterdir() if p.is_dir())
        answer=planning.read(case/'answer.json');answer['claims'][0]['citations']=['invented'];runner.save(case/'answer.json',answer)
        row=planning.read(case/'case_receipt.json');row['files_sha256']['answer.json']=sha256_file(case/'answer.json');runner.save(case/'case_receipt.json',row)
        task=row['task'];question=self.plan['warmup_question'] if not task['measured'] else self.questions[0]['question']
        with self.assertRaises(ValueError):runner.validate_case(case,row,task,question,backend.config)


class SavedGraphTests(unittest.TestCase):
    def test_all_saved_graph_vectors_bind_the_ready_text_scope_and_receipt(self):
        receipt,manifest,projection,ids,raw,vectors=checked_graph_index(REPO)
        self.assertEqual((len(ids),len(projection['edges']),raw.shape,vectors.shape),(212,394,(212,128),(212,128)))
        self.assertEqual(receipt['walk_count'],2120)
        self.assertEqual(receipt['exact_vector_lookup_count'],212)
        self.assertEqual(manifest['evaluation_scope']['sha256'],'75547d824c6b0386fdac3ed17b3a50f03b97c1eaabc2ae1692961a2d7fb5d599')

    def test_graph_pointer_projection_and_ready_counts_cannot_be_changed(self):
        original=Path.read_text
        for name in ['current.json','projection.json','index_receipt.json']:
            def changed(path,*args,**kwargs):
                text=original(path,*args,**kwargs)
                if path.name==name and ('evaluation_graph_index' in str(path)):
                    value=json.loads(text)
                    if name=='current.json':value['manifest_path']=str(REPO/'outside.json')
                    elif name=='projection.json':value['scope']='changed'
                    else:value['node_count']=211
                    return json.dumps(value)
                return text
            with self.subTest(name=name),patch.object(Path,'read_text',changed):
                with self.assertRaises(ValueError):checked_graph_index(REPO)


class EvaluationLoaderTests(unittest.TestCase):
    def text_loader(self,corrupt=False):
        import numpy as np
        receipt,manifest,all_records,hits=checked_text_index(REPO)
        records=all_records[:2];ids=[r['chunk']['chunk_id'] for r in records]
        vectors=np.zeros((2,384));vectors[:,0]=1
        actual=vectors.copy()
        if corrupt:actual[0,0]=0
        stored={'ids':ids,'documents':[r['embedding_text'] for r in records],
                'metadatas':[metadata(r) for r in records],'embeddings':actual}
        collection=SimpleNamespace(metadata={'hnsw:space':'cosine','index_fingerprint':receipt['fingerprint'],
            'model_revision':receipt['embedding']['revision'],'dimension':384},get=lambda **_:stored)
        client=SimpleNamespace(get_collection=lambda *a,**k:collection)
        chroma=SimpleNamespace(PersistentClient=lambda **_:client)
        model=SimpleNamespace(encode=lambda text,**kwargs:vectors.copy(),max_seq_length=256)
        tokenizer=SimpleNamespace(num_special_tokens_to_add=lambda **_:2)
        config=planning.read(REPO/'config.json');config.update(evaluation_scope=receipt['evaluation_scope'],development_scope=receipt['development_scope'])
        with patch.dict('sys.modules',{'chromadb':chroma,'chromadb.config':SimpleNamespace(Settings=lambda **_:None)}),patch.object(
                retrievers,'checked_text_index',return_value=(receipt,manifest,records,hits)),patch.object(
                retrievers,'load_tokenizer',return_value=tokenizer),patch.object(retrievers,'load_model',return_value=model):
            return retrievers.EvaluationTextRetriever(REPO,config)

    def test_text_loader_uses_evaluation_collection_and_exact_embedding_bindings(self):
        loaded=self.text_loader()
        self.assertEqual(len(loaded.by_id),2)
        self.assertTrue(loaded.manifest['collection_name'].startswith('threatweave_text_eval_'))
        self.assertEqual(loaded.config['evaluation_scope']['cisa_scope_count'],101)

    def test_text_loader_rejects_a_wrong_vector_even_with_matching_dimensions(self):
        with self.assertRaisesRegex(ValueError,'exact source embeddings'):self.text_loader(corrupt=True)

    def graph_loader(self,corrupt=False):
        receipt,manifest,projection,ids,raw,vectors=checked_graph_index(REPO)
        nodes={n['canonical_id']:n for n in projection['nodes']}
        dummy=SimpleNamespace(manifest=manifest,nodes=nodes)
        stored={'ids':ids,'documents':[nodes[i]['name'] for i in ids],
                'metadatas':[GraphVectorIndex.metadata(dummy,i) for i in ids],'embeddings':vectors.copy()}
        if corrupt:stored['embeddings'][0]=[0.0]*128
        collection=SimpleNamespace(metadata={'index_fingerprint':manifest['index_fingerprint'],
            'projection_sha256':manifest['projection_sha256'],'dimension':128,'hnsw:space':'cosine',
            'corpus_version':manifest['corpus_version']},get=lambda **_:stored)
        chroma=SimpleNamespace(PersistentClient=lambda **_:SimpleNamespace(get_collection=lambda *a,**k:collection))
        config=planning.read(REPO/'config.json');config['evaluation_scope']=manifest['evaluation_scope']
        with patch.dict('sys.modules',{'chromadb':chroma,'chromadb.config':SimpleNamespace(Settings=lambda **_:None)}):
            return retrievers.EvaluationGraphVectorIndex(REPO,config)

    def test_graph_loader_uses_evaluation_assets_and_exact_node_vector_bindings(self):
        loaded=self.graph_loader()
        self.assertEqual(len(loaded.vectors),212)
        self.assertTrue(loaded.manifest['collection_name'].startswith('threatweave_graph_eval_'))

    def test_graph_loader_rejects_corrupt_stored_vectors(self):
        with self.assertRaisesRegex(ValueError,'vector/source binding'):self.graph_loader(corrupt=True)

    def test_four_modes_share_the_same_initialized_graph_text_and_index(self):
        config=planning.read(REPO/'config.json')
        graph=SimpleNamespace(config=config,expected_entities={},profiles={},configuration_hash='graph')
        text=SimpleNamespace(config=config,configuration_hash='text')
        index=SimpleNamespace(manifest={'index_fingerprint':'index'})
        with patch.object(retrievers,'EvaluationGraphRetriever',return_value=graph),patch.object(
                retrievers,'EvaluationTextRetriever',return_value=text),patch.object(
                retrievers,'EvaluationGraphVectorIndex',return_value=index):
            modes=retrievers.build_retrievers(REPO,None,'fixture')
        self.assertIs(modes['text_only'],text);self.assertIs(modes['graph_only'],graph)
        for mode in ['hybrid_no_node2vec','hybrid']:
            self.assertIs(modes[mode].graph,graph);self.assertIs(modes[mode].text,text)
        self.assertIs(modes['hybrid'].index,index)


if __name__=='__main__':unittest.main()
