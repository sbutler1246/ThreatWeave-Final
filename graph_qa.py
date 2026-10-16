"""Read-only graph QA across the imported development scopes, with cited answers."""
import argparse
import getpass
import hashlib
import json
import sys
import time
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4
from typing import Literal
from pydantic import Field, model_validator

from graph.development_retrieval import DevelopmentGraphRetriever
from graph_pilot_qa import SYSTEM as PILOT_SYSTEM,checked_answer,generated_model
from schemas import QueryRequest, StrictModel

GENERATOR_VERSION = 'development-shared-cited-generator-v2'


class CompactClaim(StrictModel):
    text: str = Field(min_length=1, max_length=280)
    citations: list[str] = Field(min_length=1, max_length=4)


class CompactAnswer(StrictModel):
    answer: Literal['See cited claims.']
    claims: list[CompactClaim] = Field(max_length=8)
    abstained: bool

    @model_validator(mode='after')
    def distinct_claims(self):
        from resolve import norm
        texts = [norm(c.text) for c in self.claims]
        if any(not text for text in texts):
            raise ValueError('Claims cannot contain only whitespace.')
        if len(texts) != len(set(texts)):
            raise ValueError('Repeated claims are not allowed; combine related facts concisely.')
        if any(len(c.citations) != len(set(c.citations)) for c in self.claims):
            raise ValueError('Repeated citation IDs within a claim are not allowed.')
        return self

BASELINE_DEMO_QUESTIONS = [
    'According to CISA, how do LockBit Affiliates use AnyDesk? List the supplied ATT&CK mitigations for the reported technique and explain the practical guidance for each. Cite CISA observations and ATT&CK references separately.',
    'According to CISA, what do BianLian group actors use Rclone for?',
    'According to CISA, what do ALPHV Blackcat/ALPHV affiliates use Evilginx2 to obtain?',
]
DEMO_QUESTIONS = [
    'According to CISA, what information does Raccoon Stealer steal? Explain the supplied ATT&CK mitigations for its web session cookie technique, citing observations and references separately.',
    'According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.',
    'According to CISA, how do ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration?',
]
SYSTEM = PILOT_SYSTEM+"""
For each mitigation, cite its identity passage and its guidance passage. Describe
the actual practical guidance, rather than only saying it mitigates the technique.
If CISA and the frozen reference use different names for the same technique ID,
attribute each name to its source. Preserve actor qualifiers from prose as well
as tables. Answer the requested parts; omit unrelated actors or software.
Graph paths can contain one, two or three hops. A shorter source-backed path
does not justify inventing a technique, mitigation or longer incident chain.
Only describe the mitigations in the supplied evidence; retrieval is bounded.
Output answer exactly as "See cited claims."; do not duplicate the answer there.
Write concise, non-repeating claims, aiming for at most 30 words per claim.
Combine each mitigation's name, ID and actual guidance into ONE claim, citing
its identity and guidance passages. Do not split its label and advice into
separate claims. Combine closely related observed behavior into one claim.
Preserve qualifications such as "may" and include the practical mechanism.
Use only the citation IDs necessary for the claim, at most four per claim.
For prose describing an actor's activity, attribute the purpose to that actor;
do not characterize observed adversarial activity as a tool's general intended use.
"""


def save(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')


def generate(http,request,bundle,context,config,folder,timeout):
    schema = CompactAnswer.model_json_schema()
    schema['$defs']['CompactClaim']['properties']['citations']['items'] = {'type':'string','enum':bundle.citation_ids}
    prompt = ('QUESTION: '+request.question+'\nMODE: '+request.mode.value+'\n'+context+
              '\nReturn the requested JSON. The displayed answer is assembled from claims.')
    (folder/'system_prompt.txt').write_text(SYSTEM,encoding='utf-8')
    (folder/'user_prompt.txt').write_text(prompt,encoding='utf-8')
    save(folder/'output_schema.json',schema)
    original = prompt
    for attempt in range(1,3):
        print(f"  Asking {config['llm']['model']} for a cited answer (attempt {attempt}/2)...",flush=True)
        response = http.post('http://localhost:11434/api/generate',timeout=(10,timeout),json={
            'model':config['llm']['model'],'system':SYSTEM,'prompt':prompt,'format':schema,
            'stream':False,'options':{k:config['llm'][k] for k in ['temperature','num_ctx','num_predict']}})
        response.raise_for_status()
        body = response.json()
        save(folder/f'ollama_response_{attempt}.json',body)
        try:
            if body.get('done') is not True or body.get('done_reason')=='length':
                raise ValueError('Generation did not finish within the configured output budget.')
            CompactAnswer.model_validate_json(body['response'])
            answer = checked_answer(body['response'],bundle,0)
            answer.answer = answer.answer.replace('retrieved pilot evidence','retrieved evidence')
            answer.warnings = [f'Development {request.mode.value} pipeline; final evaluation remains pending.',
                               'Source checks passed; generated-answer semantics require human review.']
            return answer,{'attempts':attempt,'prompt_hash':hashlib.sha256((SYSTEM+'\n'+original).encode()).hexdigest(),
                           'generator_version':GENERATOR_VERSION,
                           'prompt_eval_count':body.get('prompt_eval_count'),'eval_count':body.get('eval_count')}
        except ValueError as error:
            if attempt==2:
                raise
            prompt = original+'\nRepair only output/citation errors using the original evidence: '+str(error)
            if body.get('done_reason')=='length':
                prompt += ('\nThe previous JSON was cut off. Start fresh; do not continue it. '
                    'Use one concise claim per distinct requested fact. Combine each mitigation '
                    'name, ID and guidance into a single claim. Avoid repeating the actor/tool '
                    'statement. Complete the JSON within the unchanged output limit.')
            else:
                prompt += '\nPREVIOUS OUTPUT:\n'+str(body.get('response',''))
            (folder/'repair_prompt.txt').write_text(prompt,encoding='utf-8')
    raise RuntimeError('No model response was validated.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--question',help='A development question; defaults to the AnyDesk example')
    parser.add_argument('--demo',action='store_true',help='Run three development questions across the imported reports')
    parser.add_argument('--preview',action='store_true',help='Check local source packing without calling Neo4j/Ollama')
    parser.add_argument('--timeout',type=float,default=60)
    args = parser.parse_args()
    if args.timeout<=0:
        parser.error('--timeout must be positive')
    if args.demo and args.question:
        parser.error('Use either --demo or --question.')
    repo = args.repo.resolve()
    retriever = DevelopmentGraphRetriever(repo)
    questions = DEMO_QUESTIONS if args.demo else [args.question or DEMO_QUESTIONS[0]]
    requests = [QueryRequest(question=q,mode='graph_only',corpus_version=retriever.config['corpus_version']) for q in questions]
    print(f'ThreatWeave graph-only QA: {len(questions)} question(s); up to three hops.',flush=True)
    if args.preview:
        for request in requests:
            bundle = retriever.preview(request.question)
            print('\nQuestion: '+request.question)
            print(f'  {len(bundle.paths)} paths; hops {[len(p.edges) for p in bundle.paths]}; {len(bundle.passages)} exact source passages.')
            print(f"  Context: {retriever.last_stats['evidence_utf8_bytes']}/{retriever.byte_cap} UTF-8 bytes.")
        print('\nPREVIEW PASSED: Local source/provenance packing checked; live graph presence and model output remain untested.')
        return 0
    from neo4j import GraphDatabase
    import requests as http_requests
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    output = repo/'work/graph_qa'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True,exist_ok=False)
    summary = {'purpose':'development_multi_source_graph_qa','mode':'graph_only','status':'inputs_saved',
               'configuration_hash':retriever.configuration_hash,'generator_version':GENERATOR_VERSION,
               'attack_release':'17.1','cases':[],'semantic_review_status':'pending'}
    save(output/'summary.json',summary)
    http = http_requests.Session()
    http.trust_env = False
    try:
        with GraphDatabase.driver(uri,auth=(user,password),connection_timeout=10,
                                  connection_acquisition_timeout=15,max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            retriever.driver,retriever.database = driver,database
            tags = http.get('http://localhost:11434/api/tags',timeout=10)
            tags.raise_for_status()
            model = next((m for m in tags.json()['models'] if m['name']==retriever.config['llm']['model']),None)
            if not model or not model.get('digest'):
                raise ValueError('Configured Ollama model/digest is unavailable.')
            if retriever.config['llm'].get('digest') and retriever.config['llm']['digest']!=model['digest']:
                raise ValueError('Installed model differs from the pinned model digest.')
            summary.update(model=model['name'],model_digest=model['digest'],
                           options={k:retriever.config['llm'][k] for k in ['temperature','num_ctx','num_predict']})
            save(output/'summary.json',summary)
            for number,request in enumerate(requests,1):
                print(f'\n[{number}/{len(requests)}] '+request.question,flush=True)
                folder = output/f'{number:02d}'
                folder.mkdir()
                save(folder/'question.json',request.model_dump(mode='json'))
                case = {'question':request.question,'folder':folder.name,'status':'started'}
                summary['cases'].append(case)
                started = time.perf_counter()
                try:
                    bundle = retriever.retrieve(request)
                    save(folder/'evidence.json',bundle.model_dump(mode='json'))
                    save(folder/'retrieval.json',retriever.last_stats)
                    print(f'  Retrieved: {len(bundle.paths)} paths; hops {[len(p.edges) for p in bundle.paths]}; {len(bundle.passages)} source passages.',flush=True)
                    if not bundle.paths:
                        answer = checked_answer(json.dumps({'answer':'Insufficient evidence.','claims':[], 'abstained':True}),bundle,0)
                        answer.answer = 'The retrieved development evidence is insufficient to answer this question.'
                        generation = {'attempts':0}
                    else:
                        answer,generation = generate(http,request,bundle,retriever.last_context,retriever.config,folder,args.timeout)
                    answer.execution_time_ms = (time.perf_counter()-started)*1000
                    save(folder/'answer.json',answer.model_dump(mode='json'))
                    case.update(status='abstained' if answer.abstained else 'answer_ready_for_review',
                                answer=answer.answer,path_count=len(bundle.paths),
                                hops=[len(p.edges) for p in bundle.paths],passage_count=len(bundle.passages),
                                execution_time_ms=answer.execution_time_ms,**generation)
                    print('\n'+answer.answer,flush=True)
                    print('\nSource citations:')
                    for passage in bundle.passages:
                        print(f'[{passage.citation_id}] {passage.source_kind.upper()}: {passage.doc_id}, {passage.start}:{passage.end}')
                        print('  '+str(passage.source_url)+'\n  '+passage.text)
                except Exception as error:
                    message = str(error).replace(password,'[hidden]') if password else str(error)
                    case.update(status='failed',error=message)
                    print('  FAIL: '+message,flush=True)
                finally:
                    save(output/'summary.json',summary)
    except Exception as error:
        message = str(error).replace(password,'[hidden]') if password else str(error)
        summary.update(status='service_error',error=message)
        save(output/'summary.json',summary)
        raise RuntimeError(message) from None
    finally:
        password = None
        http.close()
    failures = sum(c['status']=='failed' for c in summary['cases'])
    summary.update(status='processed_with_errors' if failures else 'processed',failed_cases=failures,
                   finished_at=datetime.now(timezone.utc).isoformat())
    save(output/'summary.json',summary)
    lines = ['# Development graph QA run','',
             'Graph-only development demonstration; generated answers require semantic review. These are not held-out evaluation scores.',
             'Evidence is packed under a conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.',
             '',f"Model: {summary['model']}; digest: {summary['model_digest']}",'']
    for i,case in enumerate(summary['cases'],1):
        lines += [f'## Question {i}','',case['question'],'','Status: '+case['status'],'']
        if 'answer' in case:
            lines += [case['answer'],'',f"Paths: {case['path_count']}; hop counts: {case['hops']}; source passages: {case['passage_count']}.",'']
        else:
            lines += [case.get('error','No answer saved.'),'']
        evidence_path = output/case['folder']/'evidence.json'
        if evidence_path.exists():
            evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
            lines += ['Source citations:','']+[f"- [{p['citation_id']}] {p['source_kind']}: {p['doc_id']} / {p['start']}:{p['end']} / {p['source_url']}" for p in evidence['passages']]+['']
    review = repo/'docs'/('ThreatWeave_graph_qa_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'\nGRAPH QA PROCESSED: {len(summary["cases"])-failures}/{len(summary["cases"])} cases produced answers or abstentions; {failures} failed.')
    print('Saved results: '+str(output))
    print('Saved review document: '+str(review))
    return 1 if failures else 0


if __name__=='__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt,EOFError):
        print('\nGraph QA cancelled; existing logs remain saved.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)
