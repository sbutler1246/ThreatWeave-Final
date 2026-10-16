"""Import direct frozen ATT&CK references for the verified corpus development pilot."""
import argparse
import getpass
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from graph.corpus_pilot_mitigations import prepare, write_transaction


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main(*, preparer=None, output_kind='corpus_pilot_mitigations', label='Corpus pilot'):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    payload = (preparer or prepare)(repo)
    references = [r for p in payload['parts'] for r in p['records']]
    mitigations = {r['entity']['canonical_id'] for r in references}
    print(f"Prepared {len(references)} direct ATT&CK reference assertions for {len(payload['parts'])} techniques; "
          f"{len(mitigations)} target mitigation entities.")
    print('No direct frozen references: '+', '.join(payload['techniques_without_direct_references']))
    print(f"Expected source-reference combinations: {len(payload['source_reference_pairs'])}; "
          f"same-window three-hop chains: {len(payload['three_hop_chains'])}.")
    output = repo/'work'/output_kind/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True, exist_ok=False)
    save(output/'prepared_records.json', payload)
    lines = ['# '+label+' direct mitigation reference preview', '',
             'Frozen Enterprise ATT&CK 17.1 associations; origin=fused, human review pending.',
             'Reference associations do not establish incident-specific effectiveness. No parent inheritance is inferred.',
             'Gold triples and QA reference answers are not inputs.', '',
             'Verified source import: '+payload['source_import_run'], '',
             f'Target reference assertions: {len(references)}; distinct mitigation entities: {len(mitigations)}.',
             f"Expected source-reference combinations: {len(payload['source_reference_pairs'])}; same-window three-hop chains: {len(payload['three_hop_chains'])}.", '',
             '| Technique | Direct references | Mitigation IDs |', '| --- | ---: | --- |']
    for part in payload['parts']:
        ids = ', '.join(r['entity']['attack_id'] for r in part['records'])
        lines.append(f"| {part['technique']['canonical_id']} | {len(part['records'])} | {ids} |")
    for identifier in payload['techniques_without_direct_references']:
        lines.append(f'| attack:{identifier} | 0 | No active direct associations in this frozen snapshot |')
    lines += ['', '## Exact reference descriptions', '']
    for part in payload['parts']:
        for record in part['records']:
            lines += ['### '+part['technique']['canonical_id']+' → '+record['entity']['canonical_id'], '',
                      'Source STIX relationship: '+record['assertion']['source_stix_relationship_id'], '',
                      record['assertion']['evidence_text'], '']
    review = repo/'docs'/('ThreatWeave_'+output_kind+'_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print('Saved reference preview: '+str(review))
    print('Saved prepared records: '+str(output))
    if args.preview:
        print('PREVIEW PASSED: Import receipt, reviewed source predictions and frozen direct references verified; no database connection.')
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
                constraints = {r['name'] for r in session.run('SHOW CONSTRAINTS YIELD name RETURN name')}
                if not {'entity_id_unique','doc_id_unique','chunk_id_unique','assertion_id_unique'} <= constraints:
                    raise ValueError('Required ThreatWeave uniqueness constraints are missing.')
                started = time.perf_counter()
                count, pairs, chains = session.execute_write(write_transaction, payload)
                seconds = time.perf_counter()-started
    except Exception as error:
        message = str(error).replace(password,'[hidden]') if password else str(error)
        save(output/'import_error.json', {'status':'import_failed','error':message})
        raise RuntimeError(message) from None
    finally:
        password = None
    receipt = {'status':'import_complete', 'reference_assertion_count':count,
               'target_mitigation_entity_count':len(mitigations), 'source_reference_combination_count':pairs,
               'same_window_three_hop_chain_count':chains,
               'techniques_without_direct_references':payload['techniques_without_direct_references'],
               'attack_release':'17.1', 'snapshot_sha256':payload['parts'][0]['snapshot_sha256'],
               'origin':'fused', 'source_import_run':payload['source_import_run'],
               'review_manifest_sha256':payload['review_manifest_sha256'], 'database':database,
               'transaction_seconds':seconds, 'human_review_status':'pending',
               'timing_scope':'execute_write including source/reference/path verification and any driver retries; preparation/connectivity excluded',
               'completed_at':datetime.now(timezone.utc).isoformat()}
    try:
        save(output/'import_receipt.json', receipt)
    except OSError as error:
        print(f'NOTE: Database committed, but receipt could not be saved: {error}')
    print(f'IMPORT COMPLETE: {count} direct ATT&CK mitigation assertions loaded or verified.')
    print(f'VERIFIED: {pairs} source-reference combinations; {chains} same-window three-hop chains.')
    print(f'Transaction time: {seconds:.3f} seconds (includes verification).')
    print('Saved records: '+str(output))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print('\nImport cancelled; saved previews remain available.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)
