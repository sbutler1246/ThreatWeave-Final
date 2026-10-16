"""Run using .venv-eval; all HTTP and model embeddings are simulated."""
import asyncio
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

os.environ['RAGAS_DO_NOT_TRACK'] = 'true'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['LANGSMITH_TRACING'] = 'false'
os.environ['LANGCHAIN_TRACING_V2'] = 'false'
from langchain_core.embeddings import Embeddings
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, LLMResult
from langchain_core.prompt_values import StringPromptValue
from ollama import ChatResponse
from ragas.run_config import RunConfig
from evaluation import judge_runtime as runtime

REPO = Path(__file__).resolve().parents[1]


class FakeEmbeddings(Embeddings):
    def embed_documents(self,texts):
        return [[1.0]+[0.0]*383 for _ in texts]

    def embed_query(self,text):
        return self.embed_documents([text])[0]


def settings():
    return {'model':runtime.MODEL,'ollama_base_url':'http://localhost:11434',
            'judge_options':{'temperature':0,'seed':42,'num_ctx':8192,'num_predict':700},
            'transport_timeout_seconds':60,'metric_timeout_seconds':180,
            'embedding_model':'sentence-transformers/all-MiniLM-L6-v2',
            'embedding_revision':runtime.MINILM_REVISION,'embedding_dimension':384,
            'cache_folder':str(REPO/'work/model_cache/sentence_transformers')}


def result(reason='stop',done=True):
    return LLMResult(generations=[[ChatGeneration(message=AIMessage(content='test'),
        generation_info={'done':done,'done_reason':reason})]])


class JudgeTests(unittest.TestCase):
    def test_completion_requires_real_ollama_stop(self):
        self.assertTrue(runtime.complete_ollama(result()))
        for reason,done in [('length',True),('stop',False),(None,True)]:
            self.assertFalse(runtime.complete_ollama(result(reason,done)))
        self.assertFalse(runtime.complete_ollama(LLMResult(generations=[])))

    def test_zero_temperature_even_when_framework_requests_a_different_value(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            recorder = runtime.Recorder(tmp,3); chat = runtime.traced_chat(settings(),recorder)
            judge = runtime.fixed_wrapper(chat,RunConfig(max_retries=1))
            values=[]
            async def fake_chat(_self,**kwargs):
                values.append(kwargs['options'].temperature)
                return ChatResponse(model=runtime.MODEL,done=True,done_reason='stop',message={'role':'assistant','content':'{}'})
            with patch('ollama.AsyncClient.chat',new=fake_chat),patch('httpx.AsyncClient.send',side_effect=AssertionError('No network')):
                asyncio.run(judge.generate(StringPromptValue(text='Synthetic test.'),temperature=0.7))
            self.assertEqual(values,[0]);self.assertEqual(judge.get_temperature(n=3),0)
            saved = runtime.read(Path(tmp)/'judge_call_001_request.json')
            self.assertIs(saved['parameters']['stream'],False)
            self.assertEqual(saved['parameters']['options']['num_predict'],700)

    def test_truncated_judge_reply_cannot_be_accepted_even_if_json_is_valid(self):
        from ragas.exceptions import LLMDidNotFinishException
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            recorder = runtime.Recorder(tmp,3);judge = runtime.fixed_wrapper(runtime.traced_chat(settings(),recorder),RunConfig(max_retries=1))
            async def fake_chat(_self,**kwargs):
                return ChatResponse(model=runtime.MODEL,done=True,done_reason='length',message={'role':'assistant','content':'{}'})
            with patch('ollama.AsyncClient.chat',new=fake_chat),self.assertRaises(LLMDidNotFinishException):
                asyncio.run(judge.generate(StringPromptValue(text='Synthetic test.')))
            self.assertEqual(runtime.read(Path(tmp)/'judge_call_001_response.json')['done_reason'],'length')

    def test_three_real_metric_implementations_with_simulated_transport_and_embeddings(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            folder=Path(tmp);recorder=runtime.Recorder(folder,30); calls=[]
            async def fake_chat(_self,**kwargs):
                calls.append(recorder.phase)
                prompt=kwargs['messages'][0]['content']
                if recorder.phase=='faithfulness':
                    value={'statements':[{'statement':runtime.PROBE['response'],'reason':'Supported.','verdict':1}]} if 'verdict' in prompt else {'statements':[runtime.PROBE['response']]}
                elif recorder.phase=='answer_relevancy':
                    value={'question':runtime.PROBE['user_input'],'noncommittal':0}
                else:
                    value={'classifications':[{'statement':runtime.PROBE['reference'],'reason':'Supported.','attributed':1}]}
                return ChatResponse(model=runtime.MODEL,done=True,done_reason='stop',message={'role':'assistant','content':json.dumps(value)})
            with patch('langchain_huggingface.HuggingFaceEmbeddings',return_value=FakeEmbeddings()) as constructor,patch('ollama.AsyncClient.chat',new=fake_chat),patch('httpx.AsyncClient.send',side_effect=AssertionError('No network')),patch('httpx.Client.send',side_effect=AssertionError('No network')):
                metrics=runtime.build(settings(),recorder)
                rows=asyncio.run(runtime.score_probe(metrics,recorder,folder))
            self.assertEqual([r['metric'] for r in rows],list(runtime.METRICS))
            self.assertTrue(all(r['status']=='scored' and abs(r['value']-1)<1e-6 for r in rows))
            self.assertEqual(len(calls),6)
            args=constructor.call_args.kwargs
            self.assertTrue(args['model_kwargs']['local_files_only'])
            self.assertFalse(args['model_kwargs']['trust_remote_code'])
            self.assertEqual(args['model_kwargs']['revision'],runtime.MINILM_REVISION)
            self.assertEqual(len(list(folder.glob('judge_call_*_response.json'))),6)

    def test_nan_and_errors_are_retained_as_missing_not_zero(self):
        class BadMetric:
            name='failed_metric'
            async def single_turn_ascore(self,*args,**kwargs):raise RuntimeError('Saved test error')
        class UndefinedMetric:
            name='undefined_metric'
            async def single_turn_ascore(self,*args,**kwargs):return float('nan')
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            rows=asyncio.run(runtime.score_probe([BadMetric(),UndefinedMetric()],runtime.Recorder(tmp,1),Path(tmp)))
            self.assertEqual([r['status'] for r in rows],['failed','undefined'])
            self.assertTrue(all(r['value'] is None for r in rows))

    def test_probe_request_cap_is_enforced(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            recorder=runtime.Recorder(tmp,1)
            args={'stream':False,'options':{'temperature':0}}
            recorder.start(args)
            with self.assertRaises(RuntimeError):recorder.start(args)

    def test_digest_mismatch_stops_before_scoring(self):
        client=SimpleNamespace(get=lambda _:SimpleNamespace(raise_for_status=lambda:None,json=lambda:{'models':[{'name':runtime.MODEL,'digest':'wrong'}]}))
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp,patch('httpx.Client') as factory:
            factory.return_value.__enter__.return_value=client
            with self.assertRaises(ValueError):runtime.check_model({**settings(),'model_digest':runtime.DIGEST},Path(tmp),'tags.json')


if __name__=='__main__':unittest.main()
