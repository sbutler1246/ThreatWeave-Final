"""Local evaluator adapters, isolated from retrieval and final-answer generation.

Constructors that load embeddings or contact Ollama are operator-only. Import and
preview use only the standard library and saved files.
"""
import asyncio
import hashlib
import json
import math
import os
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.run_ragas import MINILM_REVISION, require_pinned_versions

MODEL = 'llama3.1:8b'
DIGEST = '46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e'
METRICS = ('faithfulness','answer_relevancy','context_recall')
PROBE = {
    'user_input':'How long does service Atlas retain logs?',
    'response':'Service Atlas retains logs for seven days.',
    'retrieved_contexts':['The maintenance report states that service Atlas retains logs for seven days.'],
    'reference':'Service Atlas retains logs for seven days.',
}


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def sha(path):
    with Path(path).open('rb') as file:
        return hashlib.file_digest(file,'sha256').hexdigest()


def save(path, value):
    path = Path(path)
    temp = path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
    temp.replace(path)


def policy(repo):
    """Check cache presence and frozen assets without importing/loading a model."""
    repo = Path(repo).resolve()
    pointer = read(repo/'work/final_evaluation_inputs/current.json')
    folder = (repo/'work/final_evaluation_inputs'/pointer['run']).resolve()
    if folder.parent != repo/'work/final_evaluation_inputs':
        raise ValueError('Invalid prepared-input boundary.')
    plan = read(folder/'plan.json')
    actual = hashlib.sha256(json.dumps({k:v for k,v in plan.items() if k!='fingerprint'},
        sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
    if actual != plan['fingerprint'] or pointer['fingerprint'] != actual or plan['protocol']['model_digest'] != DIGEST:
        raise ValueError('Frozen final plan or model identity changed.')
    for name, expected in plan['frozen_files_sha256'].items():
        if sha(repo/name) != expected:
            raise ValueError('Frozen experiment file changed: '+name)
    config = read(repo/'config.json')
    if config['text_embedding']['revision'] != MINILM_REVISION:
        raise ValueError('Evaluator and frozen embedding revisions differ.')
    cache = repo/'work/model_cache/sentence_transformers'
    snapshot = cache/'models--sentence-transformers--all-MiniLM-L6-v2/snapshots'/MINILM_REVISION
    files = sorted(p for p in snapshot.rglob('*') if p.is_file())
    if not files or not (snapshot/'model.safetensors').is_file():
        raise ValueError('The frozen MiniLM snapshot is not cached. No download will be attempted.')
    model_files = {str(p.relative_to(repo)):sha(p) for p in files}
    verification = read(repo/'evaluation/dependency_verification.json')
    if sha(repo/'evaluation/requirements.lock.txt') != verification['lock_sha256']:
        raise ValueError('Evaluator lock changed.')
    return {'version':1, 'purpose':'local_synthetic_evaluator_integration_probe',
            'final_plan_fingerprint':actual, 'model':MODEL, 'model_digest':DIGEST,
            'judge_options':{'temperature':0,'seed':42,'num_ctx':8192,'num_predict':700},
            'ollama_base_url':'http://localhost:11434', 'metrics':list(METRICS),
            'response_relevancy_metric_name':'answer_relevancy',
            'embedding_model':config['text_embedding']['model'], 'embedding_revision':MINILM_REVISION,
            'embedding_dimension':384, 'normalize_embeddings':True, 'device':'cpu',
            'cache_folder':str(cache), 'cached_files_sha256':model_files,
            'transport_timeout_seconds':60, 'metric_timeout_seconds':180,
            'transport_attempts':1, 'max_probe_judge_calls':30,
            'metric_execution':'sequential; judge requests serialized; native RAGAS JSON parsing repairs retained',
            'probe_is_not_a_benchmark':True, 'lock_sha256':verification['lock_sha256'],
            'implementation_sha256':{name:sha(repo/name) for name in (
                'evaluation/judge_runtime.py','check_evaluation.py','evaluation/run_ragas.py')}}


def complete_ollama(result):
    """Ollama uses done/done_reason, not OpenAI finish_reason."""
    generations = [g for batch in result.generations for g in batch]
    if not generations:
        return False
    for generation in generations:
        info = generation.generation_info or {}
        if not info:
            info = getattr(getattr(generation,'message',None),'response_metadata',{})
        if info.get('done') is not True or info.get('done_reason') != 'stop':
            return False
    return True


def fixed_wrapper(chat, config):
    from ragas.llms import LangchainLLMWrapper

    class FixedTemperatureJudge(LangchainLLMWrapper):
        def get_temperature(self, n):
            return 0.0

        def generate_text(self, prompt, n=1, temperature=None, stop=None, callbacks=None):
            return super().generate_text(prompt,n=n,temperature=0.0,stop=stop,callbacks=callbacks)

        async def agenerate_text(self, prompt, n=1, temperature=None, stop=None, callbacks=None):
            return await super().agenerate_text(prompt,n=n,temperature=0.0,stop=stop,callbacks=callbacks)

    return FixedTemperatureJudge(chat,run_config=config,is_finished_parser=complete_ollama)


class Recorder:
    def __init__(self, folder, limit):
        self.folder, self.limit = Path(folder), limit
        self.count = 0
        self.phase = 'initialization'
        self.lock = threading.Lock()
        self.async_lock = asyncio.Lock()

    def start(self, params):
        if self.count >= self.limit:
            raise RuntimeError('Synthetic probe judge-call limit reached; preserve diagnostics.')
        self.count += 1
        identifier = f'judge_call_{self.count:03d}'
        serializable = json.loads(json.dumps(params,default=lambda v:v.model_dump(mode='json',exclude_none=True)))
        if params['stream'] is not False or serializable['options']['temperature'] != 0:
            raise ValueError('Judge transport violated the fixed policy.')
        save(self.folder/(identifier+'_request.json'),{'phase':self.phase,'endpoint':'/api/chat','parameters':serializable})
        return identifier

    def end(self, identifier, *, response=None, error=None):
        if error is None:
            save(self.folder/(identifier+'_response.json'),response.model_dump(mode='json'))
        else:
            save(self.folder/(identifier+'_error.json'),{'error_type':type(error).__name__,'error':str(error)})


def traced_chat(settings, recorder):
    from langchain_ollama import ChatOllama

    class RecordedChat(ChatOllama):
        def _create_chat_stream(self, messages, stop=None, **kwargs):
            params = self._chat_params(messages,stop,**kwargs)
            params['stream'] = False
            with recorder.lock:
                identifier = recorder.start(params)
                try:
                    response = self._client.chat(**params)
                    recorder.end(identifier,response=response)
                except BaseException as error:
                    recorder.end(identifier,error=error);raise
            yield response

        async def _acreate_chat_stream(self, messages, stop=None, **kwargs):
            params = self._chat_params(messages,stop,**kwargs)
            params['stream'] = False
            async with recorder.async_lock:
                identifier = recorder.start(params)
                try:
                    response = await self._async_client.chat(**params)
                    recorder.end(identifier,response=response)
                except BaseException as error:
                    recorder.end(identifier,error=error);raise
            yield response

    return RecordedChat(model=settings['model'],base_url=settings['ollama_base_url'],
        **settings['judge_options'],cache=False,
        client_kwargs={'timeout':settings['transport_timeout_seconds'],'trust_env':False})


def check_model(settings, folder, name):
    import httpx
    with httpx.Client(timeout=10,trust_env=False) as client:
        response = client.get(settings['ollama_base_url']+'/api/tags')
        response.raise_for_status(); tags = response.json()
    save(folder/name,tags)
    matches = [m for m in tags.get('models',[]) if m.get('name')==settings['model']]
    if len(matches)!=1 or matches[0].get('digest')!=settings['model_digest']:
        raise ValueError('Local judge digest does not match the frozen generator identity.')


def build(settings, recorder):
    require_pinned_versions()
    from langchain_huggingface import HuggingFaceEmbeddings
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.metrics import Faithfulness,ResponseRelevancy,LLMContextRecall
    from ragas.run_config import RunConfig
    config = RunConfig(timeout=settings['metric_timeout_seconds'],max_retries=1,
                       max_wait=1,max_workers=1,seed=42)
    chat = traced_chat(settings,recorder)
    judge = fixed_wrapper(chat,config)
    embeddings = HuggingFaceEmbeddings(model_name=settings['embedding_model'],
        cache_folder=settings['cache_folder'],model_kwargs={'revision':settings['embedding_revision'],
            'device':'cpu','local_files_only':True,'trust_remote_code':False},
        encode_kwargs={'normalize_embeddings':True},show_progress=False)
    vectors = embeddings.embed_documents([PROBE['user_input']])
    if (len(vectors)!=1 or len(vectors[0])!=settings['embedding_dimension']
            or any(not math.isfinite(v) for v in vectors[0])
            or not math.isclose(sum(v*v for v in vectors[0]),1,abs_tol=1e-4)):
        raise ValueError('Cached evaluator embedding dimension/normalization check failed.')
    wrapped = LangchainEmbeddingsWrapper(embeddings,run_config=config)
    metrics = [Faithfulness(llm=judge),ResponseRelevancy(llm=judge,embeddings=wrapped),LLMContextRecall(llm=judge)]
    for metric in metrics:
        metric.init(config)
    return metrics


async def score_probe(metrics, recorder, folder):
    from ragas import SingleTurnSample
    sample = SingleTurnSample(**PROBE)
    rows = []
    for metric in metrics:
        recorder.phase = metric.name
        started = time.perf_counter()
        print('Checking local evaluator:',metric.name,flush=True)
        try:
            value = float(await metric.single_turn_ascore(sample,timeout=180))
            row = {'metric':metric.name,'status':'scored' if math.isfinite(value) else 'undefined',
                   'value':value if math.isfinite(value) else None}
            if not math.isfinite(value):
                row['reason'] = 'Metric returned a nonfinite value; retained as unavailable.'
        except Exception as error:
            row = {'metric':metric.name,'status':'failed','value':None,
                   'error_type':type(error).__name__,'error':str(error)}
        row['elapsed_ms'] = (time.perf_counter()-started)*1000
        rows.append(row);save(folder/(metric.name+'_result.json'),row)
    return rows


def probe(repo, *, preview=False):
    repo = Path(repo).resolve()
    settings = policy(repo)
    if preview:
        print('EVALUATOR PREVIEW PASSED: frozen plan, evaluator lock and cached MiniLM snapshot verified.')
        print('Synthetic probe only; no final questions, model loading or service calls.')
        return 0
    if Path(os.sys.prefix).resolve() != repo/'.venv-eval':
        raise ValueError('Run with S:\\ThreatWeave\\.venv-eval\\Scripts\\python.exe.')
    os.environ.update(RAGAS_DO_NOT_TRACK='true',HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1',
                      HF_HUB_DISABLE_TELEMETRY='1',LANGCHAIN_TRACING_V2='false',
                      LANGSMITH_TRACING='false',LANGCHAIN_TRACING='false')
    folder = repo/'work/evaluation_probe_runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    save(folder/'policy.json',settings);save(folder/'synthetic_input.json',PROBE)
    summary = {'status':'started','purpose':'synthetic_evaluator_integration_only',
               'final_benchmark_rows_scored':0,'human_ratings_status':'pending'}
    save(folder/'summary.json',summary)
    print('Saved evaluator probe:',folder,flush=True)
    recorder = Recorder(folder,settings['max_probe_judge_calls'])
    import logging
    handler = logging.FileHandler(folder/'evaluator.log',encoding='utf-8')
    logging.getLogger().addHandler(handler)
    try:
        require_pinned_versions()
        check_model(settings,folder,'model_tags_before.json')
        print('Loading the cached local evaluator embedding model...',flush=True)
        metrics = build(settings,recorder)
        summary['metrics'] = asyncio.run(score_probe(metrics,recorder,folder))
        check_model(settings,folder,'model_tags_after.json')
        if policy(repo) != settings:
            raise ValueError('Frozen files, cached weights or evaluator implementation changed during probe.')
        summary['status'] = 'passed' if all(r['status']=='scored' for r in summary['metrics']) else 'needs_review'
    except (Exception,KeyboardInterrupt) as error:
        summary.update(status='failed',error_type=type(error).__name__,error=str(error))
    finally:
        logging.getLogger().removeHandler(handler);handler.close()
        summary.update(judge_calls=recorder.count,finished_at=datetime.now(timezone.utc).isoformat())
        save(folder/'summary.json',summary)
        save(folder/'files_sha256.json',{p.name:sha(p) for p in folder.iterdir() if p.is_file()})
    print('EVALUATOR PROBE '+summary['status'].upper()+': synthetic integration only; no final benchmark scores.',flush=True)
    print('Saved probe records:',folder,flush=True)
    return 0 if summary['status']=='passed' else 1
