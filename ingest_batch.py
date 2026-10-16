"""Import source-reviewed development predictions, preserving source/model provenance."""
import argparse
import getpass
import json
import sys
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4

from graph.development_ingestion import prepare,write_transaction


def save(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--preview',action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    payload = prepare(repo)
    facts = [a for item in payload['items'] for a in item['assertions']]
    entities = {e['canonical_id'] for item in payload['items'] for e in item['entities']}
    print(f"ThreatWeave reviewed batch: {len(payload['items'])} source scopes, {len(entities)} target entities, {len(facts)} extracted relationships.")
    lines = ['# Reviewed development batch import','',
             'AI-assisted source review and explicit source-role checks; human verification remains pending.',
             'No held-out benchmark labels or reference answers were used.','']
    for item in payload['items']:
        names = {e['canonical_id']:e['name'] for e in item['entities']}
        print('  '+item['chunk']['chunk_id']+' from '+Path(item['run_path']).name)
        lines += ['## '+item['chunk']['chunk_id'],'','Selected run: '+item['run_path'],'',
                  'Source: '+item['document']['source_url'],'','Source text:','',item['chunk']['text'],'']
        for context in json.loads(item['chunk']['inherited_context_json']):
            lines += ['Inherited source context:','',context['text'],'']
        lines += ['Supported generated relationships:','']
        for a in item['assertions']:
            lines.append(f"- {names[a['head_id']]} → {a['predicate']} → {names[a['tail_id']]}")
        lines += ['','Identity resolution:','']
        for entity in item['identity_resolution']:
            lines.append(f"- {entity['source_name']} → {entity['canonical_id']} ({entity['resolution_status']})")
        lines.append('')
    output = repo/'work/batch_ingestion'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True,exist_ok=False)
    save(output/'prepared_records.json',payload)
    review = repo/'docs'/('ThreatWeave_reviewed_batch_'+output.name+'.md')
    review.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('Saved source review: '+str(review))
    if args.preview:
        print('PREVIEW PASSED: Generated output, source support, canonical IDs and provenance verified; no database connection made.')
        return 0
    from neo4j import GraphDatabase
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    try:
        with GraphDatabase.driver(uri,auth=(user,password),connection_timeout=10,
                                  connection_acquisition_timeout=15,max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                names = {r['name'] for r in session.run('SHOW CONSTRAINTS YIELD name RETURN name')}
                if not {'entity_id_unique','doc_id_unique','chunk_id_unique','assertion_id_unique'}<=names:
                    raise ValueError('Required ThreatWeave uniqueness constraints are missing.')
                count = session.execute_write(write_transaction,payload)
    except Exception as error:
        message = str(error).replace(password,'[hidden]') if password else str(error)
        save(output/'import_error.json',{'status':'import_failed','error':message})
        raise RuntimeError(message) from None
    finally:
        password = None
    receipt = {'status':'import_complete','scope_count':len(payload['items']),
               'target_entity_count':len(entities),'verified_assertion_count':count,
               'factual_relationship_count':len({a['triple_key'] for a in facts}),
               'database':database,'human_review_status':'pending',
               'completed_at':datetime.now(timezone.utc).isoformat()}
    try:
        save(output/'import_receipt.json',receipt)
    except OSError as error:
        print(f'NOTE: Database committed, but receipt could not be saved: {error}')
    print(f"IMPORT COMPLETE: {len(payload['items'])} source scopes; {count} extracted assertions verified.")
    print(f"VERIFIED: {receipt['factual_relationship_count']} source-supported relationships.")
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
