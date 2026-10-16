"""Operator-only services for the unchanged frozen QA methods."""
import copy
import json
import os
import platform
import time
from pathlib import Path

from evaluation.retrievers import build_retrievers
from graph.development_projection import read_projection
from graph_qa import generate,save
from schemas import AnswerResponse,EvidenceBundle,QueryRequest


class RecordingHttp:
    def __init__(self,http,folder):self.http,self.folder,self.count=http,Path(folder),0
    def post(self,url,**kwargs):
        self.count += 1
        save(self.folder/f'transport_request_{self.count}.json',{'url':url,'payload':kwargs['json'],'timeout':kwargs['timeout']})
        try:
            response = self.http.post(url,**kwargs)
        except Exception as error:
            save(self.folder/f'transport_error_{self.count}.json',{'type':type(error).__name__})
            raise
        (self.folder/f'transport_response_{self.count}.txt').write_text(response.text,encoding='utf-8')
        save(self.folder/f'transport_status_{self.count}.json',{'http_status':response.status_code})
        return response


class Runtime:
    def __init__(self,repo,plan,uri,user,password,database,timeout):
        self.repo,self.plan,self.database,self.timeout = Path(repo).resolve(),plan,database,timeout
        self.driver,self.http,self.stage = None,None,'setup'
        try:
            import requests
            from neo4j import GraphDatabase
            self.http=requests.Session();self.http.trust_env=False
            self.driver=GraphDatabase.driver(uri,auth=(user,password),connection_timeout=10,
                connection_acquisition_timeout=15,max_transaction_retry_time=15)
            self.driver.verify_connectivity()
            self.retrievers=build_retrievers(self.repo,self.driver,database)
            self.config=self.retrievers['graph_only'].config
            if any(r.config!=self.config for r in self.retrievers.values()):raise ValueError('Mode settings differ.')
            if self.config['evaluation_scope']!=plan['evaluation_scope']:raise ValueError('Evaluation scope changed.')
            self.process=None
            try:
                import psutil
                self.process=psutil.Process()
            except ImportError:pass
            self.runtime_info={'python':platform.python_version(),'platform':platform.platform(),
                'request_timeout_seconds':self.timeout,
                'processor':platform.processor(),'logical_cpu_count':os.cpu_count(),
                'resource_scope':'Python runner process only; Ollama, Neo4j and GPU resources not sampled.',
                'python_resource_sampling_available':self.process is not None}
            self.check_model();self.check_graph()
        except BaseException:
            self.close();raise

    def check_model(self):
        self.stage='model'
        response=self.http.get('http://localhost:11434/api/tags',timeout=(10,self.timeout));response.raise_for_status()
        model=next((m for m in response.json()['models'] if m['name']==self.config['llm']['model']),None)
        if not model or model.get('digest')!=self.plan['protocol']['model_digest']:
            raise ValueError('Ollama model is unavailable or differs from the frozen digest.')
        return model['digest']

    def check_graph(self):
        self.stage='graph_freshness'
        _,fingerprint=read_projection(self.driver,self.retrievers['graph_only'],self.database)
        if fingerprint!=self.plan['projection_sha256']:raise ValueError('Live evaluation graph changed.')

    def execute(self,task,question,folder):
        request=QueryRequest(question=question,mode=task['mode'],corpus_version=self.config['corpus_version'])
        save(folder/'question.json',request.model_dump(mode='json'))
        retriever=self.retrievers[task['mode']]
        before=self.resources()
        self.stage='retrieval';started=time.perf_counter()
        bundle=EvidenceBundle.model_validate(retriever.retrieve(request))
        if bundle.configuration_hash!=retriever.configuration_hash or bundle.corpus_version!=request.corpus_version:
            raise ValueError('Mode returned evidence from a different configuration.')
        save(folder/'evidence.json',bundle.model_dump(mode='json'))
        save(folder/'retrieval.json',copy.deepcopy(retriever.last_stats))
        (folder/'context.txt').write_text(retriever.last_context,encoding='utf-8')
        self.stage='generation';generation_start=time.perf_counter()
        if not bundle.passages or (task['mode']=='graph_only' and not bundle.paths):
            answer=AnswerResponse(answer='The retrieved evidence is insufficient to answer this question.',
                                  claims=[],evidence=bundle,abstained=True,execution_time_ms=0)
            generation={'attempts':0}
        else:
            answer,generation=generate(RecordingHttp(self.http,folder),request,bundle,retriever.last_context,
                                       self.config,folder,self.timeout)
        generation_ms=(time.perf_counter()-generation_start)*1000
        answer=AnswerResponse.model_validate(answer)
        if answer.evidence!=bundle:raise ValueError('Generator changed the supplied evidence.')
        save(folder/'answer.json',answer.model_dump(mode='json'))
        after=self.resources()
        elapsed=(time.perf_counter()-started)*1000
        answer.execution_time_ms=elapsed
        save(folder/'answer.json',answer.model_dump(mode='json'))
        resource={'python_resources_before':before,'python_resources_after':after}
        if before is not None and after is not None:
            resource['python_cpu_time_seconds']=after['cpu_time_seconds']-before['cpu_time_seconds']
        return {'status':'abstained' if answer.abstained else 'answer_ready_for_review',
                'execution_time_ms':elapsed,'retrieval_ms':bundle.retrieval_ms,'generation_ms':generation_ms,
                'configuration_hash':retriever.configuration_hash,'model_digest':self.plan['protocol']['model_digest'],
                'path_count':len(bundle.paths),'passage_count':len(bundle.passages),**resource,**generation}

    def resources(self):
        if self.process is None:return None
        try:
            memory=self.process.memory_info();cpu=self.process.cpu_times()
            return {'rss_bytes':memory.rss,'peak_working_set_bytes':getattr(memory,'peak_wset',None),
                    'cpu_time_seconds':cpu.user+cpu.system}
        except Exception:return None

    def close(self):
        if self.http is not None:self.http.close()
        if self.driver is not None:self.driver.close()
