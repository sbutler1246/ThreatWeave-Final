"""Cited combined text/graph QA in the explicit hybrid_no_node2vec mode."""
import argparse
import getpass
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from graph_qa import DEMO_QUESTIONS, GENERATOR_VERSION, generate, save
from graph_pilot_qa import checked_answer
from retrieval.combined_retrieval import DevelopmentCombinedRetriever
from schemas import QueryRequest


def retry_questions(repo, run_path, mode, retriever):
    folder = run_path.resolve()
    root = (repo/('work/hybrid_qa' if mode == 'hybrid' else 'work/combined_qa')).resolve()
    if not folder.is_relative_to(root) or folder == root:
        raise ValueError('Retry run must be inside this mode\'s saved workspace run folder.')
    old = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
    if old.get('mode') != mode or old.get('configuration_hash') != retriever.configuration_hash:
        raise ValueError('Retry mode/retrieval configuration changed; run a fresh demonstration.')
    if old.get('index_fingerprint') != retriever.text.manifest['fingerprint']:
        raise ValueError('Text index changed since the failed run.')
    if mode == 'hybrid' and old.get('graph_index_fingerprint') != retriever.index.manifest['index_fingerprint']:
        raise ValueError('Graph index changed since the failed run.')
    questions = [c['question'] for c in old['cases'] if c['status'] == 'failed']
    if not questions:
        raise ValueError('The selected run has no failed cases to retry.')
    return questions, old, folder


def main(full_hybrid=False):
    mode = 'hybrid' if full_hybrid else 'hybrid_no_node2vec'
    parser = argparse.ArgumentParser(description='Full development hybrid QA with Node2Vec.' if full_hybrid else __doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--question')
    parser.add_argument('--retry-run', type=Path, help='Retry only failed cases from a saved run of this mode.')
    parser.add_argument('--preview', action='store_true', help='Use source-based graph fixtures and local text search, without service calls.')
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    if sum([bool(args.demo), bool(args.question), bool(args.retry_run)]) > 1:
        parser.error('Use one of --demo, --question or --retry-run.')
    if args.timeout <= 0:
        parser.error('--timeout must be positive.')
    repo = args.repo.resolve()
    print('Loading verified graph source profiles and the cached text index...', flush=True)
    if full_hybrid:
        from retrieval.hybrid_retrieval import DevelopmentHybridRetriever
        retriever = DevelopmentHybridRetriever(repo)
    else:
        retriever = DevelopmentCombinedRetriever(repo)
    questions = DEMO_QUESTIONS if args.demo else [args.question or DEMO_QUESTIONS[0]]
    previous, retry_folder = None, None
    if args.retry_run:
        questions, previous, retry_folder = retry_questions(repo, args.retry_run, mode, retriever)
    requests = [QueryRequest(question=q, mode=mode, corpus_version=retriever.config['corpus_version']) for q in questions]
    print('Mode: '+mode+(' (text + supported graph paths + Node2Vec neighbors).' if full_hybrid else ' (text + typed graph paths; Node2Vec disabled).'), flush=True)
    if args.preview:
        for request in requests:
            bundle = retriever.preview(request)
            stats = retriever.last_stats
            print('\nQuestion: '+request.question)
            print(f'  {len(bundle.paths)} paths; hops {stats["selected_hops"]}; {stats["selected_text_chunk_count"]} text hits; {len(bundle.passages)} source passages.')
            print(f'  Evidence context: {stats["evidence_utf8_bytes"]}/{stats["evidence_byte_cap"]} UTF-8 bytes.')
            if full_hybrid:
                print(f'  Node2Vec neighbor hits: {sum(len(h) for h in stats["node2vec"]["neighbors_by_seed"].values())}; expansion candidates: {stats["node2vec"]["expansion_candidate_count"]}.')
        print('\nPREVIEW PASSED: Saved projection/index checks passed. Current live Neo4j state and Ollama answers were not tested.' if full_hybrid else '\nPREVIEW PASSED: Source-based graph fixtures and local text search combined. Live Neo4j presence and Ollama answers remain untested.')
        return 0
    from neo4j import GraphDatabase
    import requests as http_requests
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    output = repo/('work/hybrid_qa' if full_hybrid else 'work/combined_qa')/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    summary = {'purpose': 'development_full_hybrid_qa' if full_hybrid else 'development_combined_qa', 'mode': mode,
        'node2vec_enabled': full_hybrid, 'status': 'started', 'semantic_review_status': 'pending', 'cases': [],
        'generator_version': GENERATOR_VERSION,
        'configuration_hash': retriever.configuration_hash,
        'index_fingerprint': retriever.text.manifest['fingerprint'],
        'latency_scope': 'Per-case graph/text retrieval, fusion, packing and generation; initialization excluded.'}
    if full_hybrid:
        summary.update(graph_index_fingerprint=retriever.index.manifest['index_fingerprint'],
                       projection_sha256=retriever.index.manifest['projection_sha256'])
    if previous:
        summary.update(retry_of=str(retry_folder), previous_generator_version=previous.get('generator_version'))
    save(output/'summary.json', summary)
    http = http_requests.Session()
    http.trust_env = False
    try:
        with GraphDatabase.driver(uri, auth=(user, password), connection_timeout=10,
                connection_acquisition_timeout=15, max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            retriever.graph.driver, retriever.graph.database = driver, database
            tags = http.get('http://localhost:11434/api/tags', timeout=10)
            tags.raise_for_status()
            model = next((m for m in tags.json()['models'] if m['name'] == retriever.config['llm']['model']), None)
            if not model or not model.get('digest'):
                raise ValueError('Configured Ollama model/digest is unavailable.')
            if retriever.config['llm'].get('digest') and retriever.config['llm']['digest'] != model['digest']:
                raise ValueError('Installed model differs from the pinned digest.')
            if previous and (previous.get('model_digest') != model['digest'] or previous.get('options') !=
                    {k: retriever.config['llm'][k] for k in ['temperature', 'num_ctx', 'num_predict']}):
                raise ValueError('Retry model digest or generation settings changed; run a fresh demonstration.')
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
                    stats = retriever.last_stats
                    save(folder/'evidence.json', bundle.model_dump(mode='json'))
                    save(folder/'retrieval.json', stats)
                    print(f'  Retrieved: {len(bundle.paths)} paths; hops {stats["selected_hops"]}; {stats["selected_text_chunk_count"]} text hits; {len(bundle.passages)} source passages.', flush=True)
                    if full_hybrid:
                        print(f'  Node2Vec: {sum(len(h) for h in stats["node2vec"]["neighbors_by_seed"].values())} neighbor hits; {stats["node2vec"]["expansion_candidate_count"]} supported expansion candidates.', flush=True)
                    if not bundle.passages:
                        answer = checked_answer(json.dumps({'answer': 'Insufficient evidence.', 'claims': [], 'abstained': True}), bundle, 0)
                        generation = {'attempts': 0}
                    else:
                        answer, generation = generate(http, request, bundle, retriever.last_context,
                                                      retriever.config, folder, args.timeout)
                    answer.answer = answer.answer.replace('retrieved pilot evidence', 'retrieved evidence')
                    answer.warnings = ['Development '+mode+' mode; final controlled evaluation remains pending.',
                                       'Source integrity and citation IDs checked; semantic review and final evaluation pending.']
                    answer.execution_time_ms = (time.perf_counter()-started)*1000
                    save(folder/'answer.json', answer.model_dump(mode='json'))
                    case.update(status='abstained' if answer.abstained else 'answer_ready_for_review',
                        answer=answer.answer, path_count=len(bundle.paths), hops=stats['selected_hops'],
                        text_hit_count=stats['selected_text_chunk_count'], passage_count=len(bundle.passages),
                        execution_time_ms=answer.execution_time_ms, **generation)
                    print('\n'+answer.answer, flush=True)
                    print('\nSource citations:')
                    for p in bundle.passages:
                        print(f'[{p.citation_id}] {p.source_kind.upper()}: {p.doc_id}, {p.start}:{p.end}\n  {p.source_url}\n  {p.text}')
                except Exception as exc:
                    error = str(exc).replace(password, '[hidden]') if password else str(exc)
                    case.update(status='failed', error=f'{type(exc).__name__}: {error}')
                    print('  FAIL: '+case['error'], flush=True)
                finally:
                    save(output/'summary.json', summary)
    except Exception as exc:
        error = str(exc).replace(password, '[hidden]') if password else str(exc)
        summary.update(status='service_error', error=f'{type(exc).__name__}: {error}')
        print('FAIL: '+summary['error'], flush=True)
    finally:
        password = None
        http.close()
    failures = sum(c['status'] == 'failed' for c in summary['cases'])
    service_error = summary['status'] == 'service_error'
    if not service_error:
        summary['status'] = 'processed_with_errors' if failures else 'processed'
    summary.update(failed_cases=failures, finished_at=datetime.now(timezone.utc).isoformat())
    save(output/'summary.json', summary)
    lines = ['# Development '+('full hybrid' if full_hybrid else 'combined text/graph')+' QA run', '', 'Status: '+summary['status'], '',
        'Mode: '+mode+'. Node2Vec enabled: '+str(full_hybrid)+'.',
        'Generated answers require semantic review. These are development cases, not held-out scores.',
        'RRF combines source-parent ranks; whole paths and text/context groups share a conservative UTF-8 byte cap.', '',
        'Model: '+str(summary.get('model', 'unavailable'))+'; digest: '+str(summary.get('model_digest', 'unavailable')), '']
    for number, case in enumerate(summary['cases'], 1):
        lines.extend([f'## Question {number}', '', case['question'], '', 'Status: '+case['status'], '',
                      case.get('answer', case.get('error', 'No answer saved.')), ''])
        if 'path_count' in case:
            lines.extend([f'Paths: {case["path_count"]}; hops: {case["hops"]}; text hits: {case["text_hit_count"]}; passages: {case["passage_count"]}.', ''])
        path = output/case['folder']/'evidence.json'
        if path.exists():
            passages = json.loads(path.read_text(encoding='utf-8'))['passages']
            lines.extend(['Source citations:', '']+[f'- [{p["citation_id"]}] {p["source_kind"]}: {p["doc_id"]} / {p["start"]}:{p["end"]} / {p["source_url"]}' for p in passages]+[''])
    if service_error:
        lines.extend(['Service error: '+summary['error'], ''])
    review = repo/'docs'/(('ThreatWeave_hybrid_qa_' if full_hybrid else 'ThreatWeave_combined_qa_')+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    label = 'HYBRID' if full_hybrid else 'COMBINED'
    print(f'\n{label} QA PROCESSED: {len(summary["cases"])-failures}/{len(requests)} cases produced answers or abstentions; {failures} case failures.', flush=True)
    print(f'Saved results: {output}\nSaved review document: {review}', flush=True)
    return 1 if failures or service_error else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('\nCombined QA cancelled; existing logs remain saved.')
        sys.exit(2)
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}')
        sys.exit(1)
