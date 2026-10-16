"""Operator-run import of reviewed held-out source assertions."""
import argparse
import getpass
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.corpus_ingestion import prepare
from graph.development_ingestion import write_transaction


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main(*, preparer=None, output_kind='evaluation_corpus_ingestion', label='held-out evaluation corpus'):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    payload = (preparer or prepare)(repo)
    assertions = [a for item in payload['items'] for a in item['assertions']]
    entities = {e['canonical_id'] for item in payload['items'] for e in item['entities']}
    print(f"Reviewed {label}: {len(payload['items'])} source windows; {len(entities)} target entities; "
          f"{len(assertions)} selected assertions; {len(payload['excluded_candidates'])} excluded candidates.")
    output = repo/'work'/output_kind/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True, exist_ok=False)
    save(output/'prepared_records.json', payload)
    lines = ['# Reviewed '+label+' import preview', '',
             'Held-out source assertions from actual model output; AI-assisted source review, human review pending.',
             'Only Supported dispositions are selected. Uncertain/conditional review candidates are excluded.',
             'No benchmark gold triples or QA reference answers are inputs.', '',
             'Extraction run: '+payload['extraction_run'],
             'Review manifest: '+payload['review_manifest'],
             'Review manifest SHA-256: '+payload['review_manifest_sha256'], '',
             f"Target records: {len(payload['items'])} windows, {len(entities)} distinct entities, {len(assertions)} assertions.",
             'Target counts include reused records; these are not counts of newly created graph records.', '']
    for item in payload['items']:
        names = {e['canonical_id']:e['name'] for e in item['entities']}
        lines += ['## '+item['chunk']['chunk_id'], '', 'Source: '+item['document']['source_url'], '']
        for assertion in item['assertions']:
            lines += [f"- {names[assertion['head_id']]} → {assertion['predicate']} → {names[assertion['tail_id']]}",
                      '  Source review: '+assertion['source_review_reason'],
                      '  Literal support: '+assertion['evidence_text']]
        lines.append('')
    lines += ['## Excluded candidates', '']
    for entry in payload['excluded_candidates']:
        lines.append(f"- {entry['folder']}.{entry['relation_index']+1}: {entry['reason']}")
    review_path = repo/'docs'/('ThreatWeave_'+label.replace(' ', '_')+'_import_'+output.name+'.md')
    review_path.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print('Saved import preview: '+str(review_path))
    print('Saved prepared records: '+str(output))
    if args.preview:
        print('PREVIEW PASSED: Source, model output, reviewed selection and provenance verified; no database connection.')
        return 0
    from neo4j import GraphDatabase
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    try:
        with GraphDatabase.driver(uri, auth=(user,password), connection_timeout=10,
                                  connection_acquisition_timeout=15, max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                names = {r['name'] for r in session.run('SHOW CONSTRAINTS YIELD name RETURN name')}
                if not {'entity_id_unique','doc_id_unique','chunk_id_unique','assertion_id_unique'} <= names:
                    raise ValueError('Required ThreatWeave uniqueness constraints are missing.')
                started = time.perf_counter()
                count = session.execute_write(write_transaction, payload)
                seconds = time.perf_counter()-started
    except Exception as error:
        message = str(error).replace(password,'[hidden]') if password else str(error)
        save(output/'import_error.json', {'status':'import_failed', 'error':message})
        raise RuntimeError(message) from None
    finally:
        password = None
    receipt = {'status':'import_complete', 'scope_count':len(payload['items']),
               'target_entity_count':len(entities), 'verified_assertion_count':count,
               'factual_relationship_count':len({a['triple_key'] for a in assertions}),
               'excluded_candidate_count':len(payload['excluded_candidates']),
               'transaction_seconds':seconds, 'verified_assertions_per_second':count/seconds if seconds > 0 else None,
               'timing_scope':'execute_write including conflict checks, verification and any driver retries; preparation/connectivity excluded',
               'database':database, 'human_review_status':'pending',
               'review_manifest_sha256':payload['review_manifest_sha256'],
               'completed_at':datetime.now(timezone.utc).isoformat()}
    try:
        save(output/'import_receipt.json', receipt)
    except OSError as error:
        print(f'NOTE: Database committed, but receipt could not be saved: {error}')
    print(f'IMPORT COMPLETE: {count} extracted assertions verified across {len(payload["items"])} windows.')
    print(f'Transaction time: {seconds:.3f} seconds (includes verification).')
    print('Saved records: '+str(output))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('\nEvaluation import cancelled; saved previews remain available.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)
