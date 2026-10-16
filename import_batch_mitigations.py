"""Import direct ATT&CK 17.1 mitigations for the new development techniques."""
import argparse
import getpass
import json
import sys
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4

from import_pilot_mitigations import prepare as prepare_technique,write_transaction as write_technique

TECHNIQUE_SCOPES = {
    'T1219':['AA23-165A:table4:row03','AA23-165A:table4:row04'],
    'T1562.001':['AA23-165A:table4:row05'],
}


def prepare(repo):
    parts = [prepare_technique(repo,identifier) for identifier in TECHNIQUE_SCOPES]
    return {'parts':parts,'technique_scopes':TECHNIQUE_SCOPES,
            'prepared_at':datetime.now(timezone.utc).isoformat(),
            'expected_path_count':sum(len(p['records'])*len(TECHNIQUE_SCOPES[p['technique']['canonical_id'].split(':',1)[1]]) for p in parts)}


def write_transaction(tx,payload):
    reference_count = 0
    for part in payload['parts']:
        identifier = part['technique']['canonical_id'].split(':',1)[1]
        reference_count += write_technique(tx,part,scope=payload['technique_scopes'][identifier][0])
    assertion_ids = [r['assertion']['assertion_id'] for p in payload['parts'] for r in p['records']]
    scopes = [s for values in payload['technique_scopes'].values() for s in values]
    # Use accepted source assertions rather than a representative edge property
    # to verify each development row's three-hop path.
    verified = tx.run(
        'MATCH p=(g:Entity:ThreatGroup)-[r1:USES]->(s:Entity:Software)'
        '-[r2:USES_TECHNIQUE]->(t:Entity:Technique)-[r3:MITIGATED_BY]->(m:Entity:Mitigation) '
        'MATCH (a1:Assertion),(a2:Assertion),(a3:Assertion) '
        'WHERE a1.assertion_id IN r1.assertion_ids AND a2.assertion_id IN r2.assertion_ids '
        'AND a3.assertion_id IN r3.assertion_ids AND a3.assertion_id IN $ids '
        "AND all(a IN [a1,a2,a3] WHERE a.validation_status IN ['validated','human_verified']) "
        'AND a1.chunk_id IN $scopes AND a2.chunk_id=a1.chunk_id '
        'AND a2.source_doc_id=a1.source_doc_id '
        'AND a1.head_id=g.canonical_id AND a1.tail_id=s.canonical_id '
        "AND a1.predicate='USES' AND a1.origin='extracted' "
        'AND a2.head_id=s.canonical_id AND a2.tail_id=t.canonical_id '
        "AND a2.predicate='USES_TECHNIQUE' AND a2.origin='extracted' "
        'AND a3.head_id=t.canonical_id AND a3.tail_id=m.canonical_id '
        "AND a3.predicate='MITIGATED_BY' AND a3.origin='fused' AND a3.attack_release='17.1' "
        'RETURN count(DISTINCT p) AS paths',ids=assertion_ids,scopes=scopes).single()
    if not verified or verified['paths']!=payload['expected_path_count']:
        raise ValueError('Expected development three-hop chains were not all verified; transaction rolled back.')
    return reference_count,verified['paths']


def save(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--preview',action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    payload = prepare(repo)
    count = sum(len(p['records']) for p in payload['parts'])
    print('ThreatWeave mitigation import: frozen ATT&CK 17.1 / new development techniques')
    for part in payload['parts']:
        print(f"  {part['technique']['canonical_id']}: {part['technique']['name']} — {len(part['records'])} direct mitigation references")
    print(f"Prepared: {count} reference assertions; expected {payload['expected_path_count']} development three-hop paths.")
    if args.preview:
        print('PREVIEW PASSED: Frozen snapshot, direct STIX associations, source spans and stable IDs verified.')
        return 0
    from neo4j import GraphDatabase
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    output = repo/'work/batch_mitigation_import'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True,exist_ok=False)
    save(output/'prepared_records.json',payload)
    try:
        with GraphDatabase.driver(uri,auth=(user,password),connection_timeout=10,
                                  connection_acquisition_timeout=15,max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                names = {r['name'] for r in session.run('SHOW CONSTRAINTS YIELD name RETURN name')}
                if not {'entity_id_unique','doc_id_unique','chunk_id_unique','assertion_id_unique'}<=names:
                    raise ValueError('Required ThreatWeave uniqueness constraints are missing.')
                reference_count,path_count = session.execute_write(write_transaction,payload)
    except Exception as error:
        message = str(error).replace(password,'[hidden]') if password else str(error)
        save(output/'import_error.json',{'status':'import_failed','error':message})
        raise RuntimeError(message) from None
    finally:
        password = None
    receipt = {'status':'import_complete','technique_ids':list(TECHNIQUE_SCOPES),
               'reference_assertion_count':reference_count,'development_three_hop_path_count':path_count,
               'attack_release':'17.1','snapshot_sha256':payload['parts'][0]['snapshot_sha256'],
               'origin':'fused','database':database,'completed_at':datetime.now(timezone.utc).isoformat()}
    try:
        save(output/'import_receipt.json',receipt)
    except OSError as error:
        print(f'NOTE: Database committed, but receipt could not be saved: {error}')
    print(f'IMPORT COMPLETE: {reference_count} ATT&CK mitigation assertions loaded or verified.')
    print(f'VERIFIED: {path_count} three-hop paths across the three new LockBit rows.')
    print('Saved records: '+str(output))
    return 0


if __name__=='__main__':
    try:
        sys.exit(main())
    except (KeyboardInterrupt,EOFError):
        print('\nImport cancelled.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)
