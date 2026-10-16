"""Cited text-only QA from the development Chroma index; no Neo4j access."""
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from graph_qa import DEMO_QUESTIONS, GENERATOR_VERSION, generate, save
from graph_pilot_qa import checked_answer
from retrieval.text_retrieval import DevelopmentTextRetriever
from schemas import QueryRequest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--demo', action='store_true', help='Run the same three development questions as graph QA.')
    parser.add_argument('--question', help='A development question; defaults to AnyDesk.')
    parser.add_argument('--preview', action='store_true', help='Verify local retrieval without calling Ollama.')
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    if args.demo and args.question:
        parser.error('Use either --demo or --question.')
    if args.timeout <= 0:
        parser.error('--timeout must be positive.')
    repo = args.repo.resolve()
    print('Loading and verifying the cached development text index...', flush=True)
    retriever = DevelopmentTextRetriever(repo)
    questions = DEMO_QUESTIONS if args.demo else [args.question or DEMO_QUESTIONS[0]]
    requests = [QueryRequest(question=q, mode='text_only', corpus_version=retriever.config['corpus_version']) for q in questions]
    if args.preview:
        for request in requests:
            bundle = retriever.retrieve(request)
            print('\nQuestion: '+request.question)
            print(f'  {retriever.last_stats["selected_chunk_count"]} selected text chunks; {len(bundle.passages)} exact source passages; zero graph paths.')
            print(f'  Evidence context: {retriever.last_stats["evidence_utf8_bytes"]}/{retriever.last_stats["evidence_byte_cap"]} UTF-8 bytes.')
        print('\nPREVIEW PASSED: Local index integrity and source packing checked; Ollama was not called.')
        return 0
    import requests as http_requests
    output = repo/'work/text_qa'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    summary = {'purpose': 'development_text_only_qa', 'mode': 'text_only', 'status': 'started',
        'generator_version': GENERATOR_VERSION,
        'configuration_hash': retriever.configuration_hash,
        'index_fingerprint': retriever.manifest['fingerprint'], 'cases': [], 'semantic_review_status': 'pending',
        'latency_scope': 'Per-case query embedding, nearest-neighbor retrieval, evidence packing and generation; excludes model/index initialization.'}
    save(output/'summary.json', summary)
    http = http_requests.Session()
    http.trust_env = False
    try:
        tags = http.get('http://localhost:11434/api/tags', timeout=10)
        tags.raise_for_status()
        model = next((m for m in tags.json()['models'] if m['name'] == retriever.config['llm']['model']), None)
        if not model or not model.get('digest'):
            raise ValueError('Configured Ollama model/digest is unavailable.')
        if retriever.config['llm'].get('digest') and retriever.config['llm']['digest'] != model['digest']:
            raise ValueError('Installed Ollama model differs from the pinned digest.')
        summary.update(model=model['name'], model_digest=model['digest'],
                       options={k: retriever.config['llm'][k] for k in ['temperature', 'num_ctx', 'num_predict']})
        for number, request in enumerate(requests, 1):
            print(f'\n[{number}/{len(requests)}] '+request.question, flush=True)
            folder = output/f'{number:02d}'
            folder.mkdir()
            save(folder/'question.json', request.model_dump(mode='json'))
            case = {'question': request.question, 'folder': folder.name, 'status': 'started'}
            summary['cases'].append(case)
            started = time.perf_counter()
            try:
                bundle = retriever.retrieve(request)
                save(folder/'evidence.json', bundle.model_dump(mode='json'))
                save(folder/'retrieval.json', retriever.last_stats)
                print(f'  Retrieved: {retriever.last_stats["selected_chunk_count"]} text chunks; {len(bundle.passages)} source passages; no graph paths.', flush=True)
                if not bundle.passages:
                    answer = checked_answer(json.dumps({'answer': 'Insufficient evidence.', 'claims': [], 'abstained': True}), bundle, 0)
                    generation = {'attempts': 0}
                else:
                    answer, generation = generate(http, request, bundle, retriever.last_context,
                                                  retriever.config, folder, args.timeout)
                answer.answer = answer.answer.replace('retrieved pilot evidence', 'retrieved evidence')
                answer.warnings = ['Development text-only baseline; final evaluation remains pending.',
                    'Top-five nearest-neighbor retrieval does not establish completeness of all mitigation references.',
                    'Source integrity and citation IDs were checked; answer semantics require review.']
                answer.execution_time_ms = (time.perf_counter()-started)*1000
                save(folder/'answer.json', answer.model_dump(mode='json'))
                case.update(status='abstained' if answer.abstained else 'answer_ready_for_review',
                            answer=answer.answer, passage_count=len(bundle.passages),
                            selected_chunk_count=retriever.last_stats['selected_chunk_count'],
                            execution_time_ms=answer.execution_time_ms, **generation)
                print('\n'+answer.answer, flush=True)
                print('\nSource citations:')
                for p in bundle.passages:
                    print(f'[{p.citation_id}] {p.source_kind.upper()}: {p.doc_id}, {p.start}:{p.end}\n  {p.source_url}\n  {p.text}')
            except Exception as exc:
                case.update(status='failed', error=f'{type(exc).__name__}: {exc}')
                print('  FAIL: '+case['error'], flush=True)
            finally:
                save(output/'summary.json', summary)
    except Exception as exc:
        summary.update(status='service_error', error=f'{type(exc).__name__}: {exc}')
        print('FAIL: '+summary['error'], flush=True)
    finally:
        http.close()
    failures = sum(c['status'] == 'failed' for c in summary['cases'])
    service_failed = summary['status'] == 'service_error'
    if not service_failed:
        summary['status'] = 'processed_with_errors' if failures else 'processed'
    summary.update(failed_cases=failures, finished_at=datetime.now(timezone.utc).isoformat())
    save(output/'summary.json', summary)
    lines = ['# Development text-only QA run', '', 'Status: '+summary['status'], '',
        'Generated answers require semantic review. These development cases are not held-out evaluation scores.',
        'The generator and its settings are shared with graph QA. Retrieval uses top-five cosine neighbors only, without graph expansion.',
        'Evidence is packed under the same conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.',
        'A successful response does not establish completeness or factual accuracy.', '',
        'Model: '+str(summary.get('model', 'unavailable'))+'; digest: '+str(summary.get('model_digest', 'unavailable')), '']
    for number, case in enumerate(summary['cases'], 1):
        lines.extend([f'## Question {number}', '', case['question'], '', 'Status: '+case['status'], '',
                      case.get('answer', case.get('error', 'No answer saved.')), ''])
        if 'passage_count' in case:
            lines.extend([f'Text chunks: {case["selected_chunk_count"]}; source passages: {case["passage_count"]}; graph paths: zero.', ''])
        path = output/case['folder']/'evidence.json'
        if path.exists():
            passages = json.loads(path.read_text(encoding='utf-8'))['passages']
            lines.extend(['Source citations:', '']+[f'- [{p["citation_id"]}] {p["source_kind"]}: {p["doc_id"]} / {p["start"]}:{p["end"]} / {p["source_url"]}' for p in passages]+[''])
    if service_failed:
        lines.extend(['Service error: '+summary['error'], ''])
    review = repo/'docs'/('ThreatWeave_text_qa_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'\nTEXT QA PROCESSED: {len(summary["cases"])-failures}/{len(requests)} cases produced answers or abstentions; {failures} case failures.', flush=True)
    print(f'Saved results: {output}\nSaved review document: {review}', flush=True)
    return 1 if failures or service_failed else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('\nText QA cancelled; existing logs remain saved.')
        sys.exit(2)
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}')
        sys.exit(1)
