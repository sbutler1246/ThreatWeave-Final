"""Import ATT&CK 17.1 mitigation references for the existing T1046 pilot.

Reads only the frozen structured ATT&CK snapshot, never gold labels or QA answers.
STIX Mitigation--mitigates-->Technique is mapped to
Technique--MITIGATED_BY-->Mitigation. Imports are atomic and repeatable.
This pilot scope does not import the full ATT&CK graph. No LLM is called.
"""
import argparse
import getpass
import hashlib
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

RELEASE = '17.1'
SNAPSHOT_HASH = '0d1c347a4d584cf7e11ef46556c33b7689341443bf86299188d46c307274323b'
SOURCE_URL = ('https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/'
              'enterprise-attack/enterprise-attack-17.1.json')
SCOPE = 'AA23-165A:table4:row02'


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def active(obj):
    return not obj.get('revoked') and not obj.get('x_mitre_deprecated')


def external_id(obj):
    refs = [r for r in obj.get('external_references', [])
            if r.get('source_name')=='mitre-attack' and r.get('external_id')]
    if len(refs)!=1:
        raise ValueError('Expected one unambiguous MITRE external ID.')
    return refs[0]['external_id']


def reference_records(objects, technique_id='T1046', *, allow_empty=False):
    """Select active structured relationships, preserving their original direction."""
    by_id = {obj['id']:obj for obj in objects}
    if len(by_id)!=len(objects):
        raise ValueError('Duplicate STIX IDs in the frozen snapshot.')
    techniques = [obj for obj in objects if obj.get('type')=='attack-pattern' and active(obj)
                  and any(r.get('source_name')=='mitre-attack' and r.get('external_id')==technique_id
                          for r in obj.get('external_references', []))]
    if len(techniques)!=1:
        raise ValueError(f'Expected one active {technique_id} technique.')
    technique = techniques[0]
    links = []
    for relationship in objects:
        if (relationship.get('type')!='relationship' or not active(relationship)
                or relationship.get('relationship_type')!='mitigates'
                or relationship.get('target_ref')!=technique['id']):
            continue
        mitigation = by_id.get(relationship.get('source_ref'))
        if mitigation is None or mitigation.get('type')!='course-of-action':
            raise ValueError('Mitigates relationship has an invalid mitigation endpoint.')
        if not active(mitigation):
            continue
        if not external_id(mitigation).startswith('M'):
            raise ValueError('Mitigation has an invalid MITRE external ID.')
        if not relationship.get('description', '').strip():
            raise ValueError('Pilot reference lacks technique-specific mitigation guidance.')
        links.append((mitigation, relationship))
    if not links and not allow_empty:
        raise ValueError(f'No active mitigation references found for {technique_id}.')
    return technique, sorted(links, key=lambda pair:external_id(pair[0]))


def prepare(repo, technique_id='T1046', *, allow_empty=False):
    sys.path.insert(0, str(repo))
    from resolve import norm
    from schemas import Assertion, Chunk, Document, Entity
    raw = (repo/'data/enterprise-attack-17.1.json').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=SNAPSHOT_HASH:
        raise ValueError('Frozen ATT&CK snapshot checksum changed; import cancelled.')
    config = json.loads((repo/'config.json').read_text(encoding='utf-8'))
    if config.get('attack_release')!=RELEASE:
        raise ValueError('Project configuration does not select ATT&CK 17.1.')
    technique, links = reference_records(json.loads(raw)['objects'],technique_id,allow_empty=allow_empty)
    records = []
    for mitigation, relationship in links:
        mid = external_id(mitigation)
        entity = Entity(canonical_id='attack:'+mid, type='Mitigation', name=mitigation['name'],
                        aliases=mitigation.get('aliases', [])+mitigation.get('x_mitre_aliases', []),
                        attack_id=mid, description=mitigation.get('description'),
                        stix_id=mitigation['id'], attack_release=RELEASE,
                        resolution_status='canonical').model_dump(mode='json', exclude_none=True)
        entity['normalized_name'] = norm(entity['name'])
        # These are normalized fields from a structured record, not a verbatim
        # quotation of a web page. The original STIX IDs and byte hash are retained.
        description = relationship['description']
        header = (f"ATT&CK release: {RELEASE}\n"
                  f"Technique: {technique['name']} ({technique_id})\n"
                  f"Mitigation: {mitigation['name']} ({mid})\n"
                  f"STIX relationship_type: mitigates\n"
                  f"STIX source_ref: {relationship['source_ref']}\n"
                  f"STIX target_ref: {relationship['target_ref']}\n\n")
        text = header+description
        doc_id = 'attack:'+RELEASE+':'+relationship['id']
        doc = Document(doc_id=doc_id,
                       title=f'ATT&CK {RELEASE}: {mid} mitigates {technique_id}',
                       source_url=SOURCE_URL,
                       source='attack', text=text, content_hash=sha(text)).model_dump(mode='json', exclude_none=True)
        doc.update(source_snapshot_sha256=SNAPSHOT_HASH, source_stix_relationship_id=relationship['id'],
                   source_record_modified=relationship.get('modified'),
                   source_file='data/enterprise-attack-17.1.json', attack_release=RELEASE,
                   normalization='Structured STIX fields followed by the exact relationship description.',
                   canonical_id='doc:'+doc_id, name=doc['title'], type='Document')
        chunk = Chunk(chunk_id=doc_id+':description', doc_id=doc_id, start=len(header),
                      end=len(text), text=description).model_dump(mode='json', exclude_none=True)
        chunk.pop('inherited_context')
        chunk['inherited_context_json'] = '[]'
        triple_key = sha('\x1f'.join(['attack:'+technique_id,'MITIGATED_BY',entity['canonical_id']]))
        aid = 'assertion:'+sha('\x1f'.join([triple_key,RELEASE,relationship['id'],SNAPSHOT_HASH]))
        assertion = Assertion(assertion_id=aid, head_id='attack:'+technique_id, predicate='MITIGATED_BY',
                              tail_id=entity['canonical_id'], source_doc_id=doc_id,
                              chunk_id=chunk['chunk_id'], evidence_text=description,
                              origin='fused', validation_status='validated').model_dump(mode='json', exclude_none=True)
        assertion.update(triple_key=triple_key, evidence_start=chunk['start'], evidence_end=chunk['end'],
                         source_url=SOURCE_URL, source_hash=doc['content_hash'],
                         source_snapshot_sha256=SNAPSHOT_HASH, source_stix_relationship_id=relationship['id'],
                         source_stix_source_ref=relationship['source_ref'],
                         source_stix_target_ref=relationship['target_ref'],
                         source_relationship_type='mitigates', attack_release=RELEASE,
                         source_review_method='active_frozen_STIX_reference_mapping',
                         human_review_status='pending', reference_only=True,
                         inherited_context_json='[]')
        records.append({'entity':entity, 'document':doc, 'chunk':chunk, 'assertion':assertion})
    return {'technique':{'canonical_id':'attack:'+technique_id, 'name':technique['name'],
                         'stix_id':technique['id'], 'attack_release':RELEASE},
            'snapshot_sha256':SNAPSHOT_HASH, 'records':records,
            'prepared_at':datetime.now(timezone.utc).isoformat()}


def write_reference_records(tx, payload):
    """Write frozen reference records after the caller checks its source prerequisites."""
    technique = payload['technique']
    current = tx.run('MATCH (t:Entity:Technique {canonical_id:$id}) RETURN properties(t) AS props',
                     id=technique['canonical_id']).single()
    if not current or any(current['props'].get(k)!=v for k,v in technique.items()):
        raise ValueError('Existing technique identity/release does not match the frozen ATT&CK record: '+technique['canonical_id'])
    now = payload['prepared_at']
    for record in payload['records']:
        entity, doc, chunk, assertion = (record[k] for k in ['entity','document','chunk','assertion'])
        existing = tx.run('MATCH (m:Entity {canonical_id:$id}) RETURN properties(m) AS props',
                          id=entity['canonical_id']).single()
        if existing and any(existing['props'].get(k)!=entity[k]
                            for k in ['type','name','stix_id','attack_release']):
            raise ValueError('Existing mitigation has a conflicting identity or release.')
        previous_doc = tx.run('MATCH (d:Document {doc_id:$id}) RETURN d.content_hash AS hash',
                             id=doc['doc_id']).single()
        if previous_doc and previous_doc['hash']!=doc['content_hash']:
            raise ValueError('Existing reference Document has different content.')
        previous_chunk = tx.run('MATCH (c:Chunk {chunk_id:$id}) RETURN c.text AS text, c.doc_id AS doc',
                               id=chunk['chunk_id']).single()
        if previous_chunk and (previous_chunk['text']!=chunk['text'] or previous_chunk['doc']!=chunk['doc_id']):
            raise ValueError('Existing reference Chunk conflicts with the frozen record.')
        current_assertion = tx.run('MATCH (a:Assertion {assertion_id:$id}) RETURN properties(a) AS props',
                                   id=assertion['assertion_id']).single()
        assertion = dict(assertion)
        if current_assertion:
            previous = current_assertion['props']
            if any(previous.get(k)!=assertion[k] for k in [
                    'head_id','tail_id','predicate','source_doc_id','chunk_id','evidence_text',
                    'origin','source_snapshot_sha256','source_stix_relationship_id']):
                raise ValueError('Existing assertion conflicts with this frozen STIX relationship.')
            if previous.get('validation_status')=='rejected':
                raise ValueError('A rejected reference requires review before reimport.')
            if previous.get('validation_status')=='human_verified':
                assertion['validation_status'] = 'human_verified'
            if previous.get('human_review_status'):
                assertion['human_review_status'] = previous['human_review_status']
        tx.run('MERGE (m:Entity {canonical_id:$id}) ON CREATE SET m.created_at=$now '
               'SET m:Mitigation SET m += $props', id=entity['canonical_id'], now=now, props=entity).consume()
        tx.run('MERGE (d:Document {doc_id:$id}) ON CREATE SET d.created_at=$now SET d += $props',
               id=doc['doc_id'], now=now, props=doc).consume()
        tx.run('MERGE (c:Chunk {chunk_id:$id}) ON CREATE SET c.created_at=$now SET c += $props',
               id=chunk['chunk_id'], now=now, props=chunk).consume()
        tx.run('MERGE (a:Assertion {assertion_id:$id}) ON CREATE SET a.created_at=$now SET a += $props',
               id=assertion['assertion_id'], now=now, props=assertion).consume()
        edge_props = {k:v for k,v in assertion.items() if k not in ['assertion_id','head_id','tail_id','predicate']}
        tx.run('MATCH (t:Entity:Technique {canonical_id:$head}), (m:Entity:Mitigation {canonical_id:$tail}) '
               'MERGE (t)-[r:MITIGATED_BY]->(m) SET r += $props, r.assertion_ids = CASE '
               'WHEN $aid IN coalesce(r.assertion_ids, []) THEN r.assertion_ids '
               'ELSE coalesce(r.assertion_ids, []) + [$aid] END', head=assertion['head_id'],
               tail=assertion['tail_id'], aid=assertion['assertion_id'], props=edge_props).consume()
    return len(payload['records'])


def write_transaction(tx, payload, scope=SCOPE):
    technique = payload['technique']
    chain = tx.run('MATCH (g:Entity:ThreatGroup)-[r1:USES]->(s:Entity:Software)'
                   '-[r2:USES_TECHNIQUE]->(t:Entity:Technique {canonical_id:$id}) '
                   'WHERE r1.chunk_id=$scope AND r2.chunk_id=$scope '
                   "AND r1.validation_status IN ['validated','human_verified'] "
                   "AND r2.validation_status IN ['validated','human_verified'] "
                   'RETURN count(*) AS paths', id=technique['canonical_id'], scope=scope).single()
    if not chain or chain['paths']!=1:
        raise ValueError('Expected exactly one accepted CISA pilot chain ending in '+technique['canonical_id'])
    count = write_reference_records(tx,payload)
    expected_ids = sorted(record['entity']['canonical_id'] for record in payload['records'])
    verified = tx.run('MATCH p=(g:Entity:ThreatGroup)-[r1:USES]->(s:Entity:Software)'
                      '-[r2:USES_TECHNIQUE]->(t:Entity:Technique {canonical_id:$tid})'
                      '-[r3:MITIGATED_BY]->(m:Entity:Mitigation) '
                      'MATCH (a:Assertion) WHERE a.assertion_id IN r3.assertion_ids '
                      'AND a.assertion_id IN $aids AND a.head_id=t.canonical_id '
                      "AND a.tail_id=m.canonical_id AND a.predicate='MITIGATED_BY' "
                      "AND a.origin='fused' AND a.validation_status IN ['validated','human_verified'] "
                      'AND r1.chunk_id=$scope AND r2.chunk_id=$scope '
                      'RETURN collect(DISTINCT m.canonical_id) AS ids', tid=technique['canonical_id'], scope=scope,
                      aids=[r['assertion']['assertion_id'] for r in payload['records']]).single()
    if not verified or sorted(verified['ids'])!=expected_ids:
        raise ValueError('Three-hop verification failed; transaction rolled back.')
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    payload = prepare(repo)
    print('ThreatWeave ATT&CK mitigation import: T1046 / frozen release 17.1')
    for record in payload['records']:
        m = record['entity']
        print(f"  {m['attack_id']}: {m['name']}")
        print('    '+record['assertion']['evidence_text'])
    if args.preview:
        print('PREVIEW PASSED: Snapshot, STIX direction, schema and source spans checked; no database writes.')
        return 0
    from neo4j import GraphDatabase
    uri = input('Neo4j URI [bolt://localhost:7687]: ').strip() or 'bolt://localhost:7687'
    user = input('Neo4j username [neo4j]: ').strip() or 'neo4j'
    database = input('Database name [neo4j]: ').strip() or 'neo4j'
    password = getpass.getpass('Neo4j password (typing is hidden): ')
    run_dir = repo/'work/mitigation_import'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True)
    (run_dir/'prepared_records.json').write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    try:
        with GraphDatabase.driver(uri, auth=(user,password), connection_timeout=10,
                                  connection_acquisition_timeout=15, max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                names = {r['name'] for r in session.run('SHOW CONSTRAINTS YIELD name RETURN name')}
                if not {'entity_id_unique','doc_id_unique','chunk_id_unique','assertion_id_unique'}<=names:
                    raise ValueError('Required ThreatWeave uniqueness constraints are missing.')
                count = session.execute_write(write_transaction, payload)
    except Exception as error:
        message = str(error).replace(password,'[hidden]') if password else str(error)
        raise RuntimeError(message) from None
    finally:
        password = None
    receipt = {'status':'import_complete', 'attack_release':RELEASE, 'snapshot_sha256':SNAPSHOT_HASH,
               'technique_id':'T1046', 'reference_relationship_count':count,
               'three_hop_mitigation_count':count, 'origin':'fused', 'database':database,
               'completed_at':datetime.now(timezone.utc).isoformat()}
    try:
        (run_dir/'import_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    except OSError as error:
        print(f'NOTE: Database committed, but receipt could not be saved: {error}')
    print(f'IMPORT COMPLETE: {count} mitigation nodes and {count} reference relationships loaded or verified.')
    print(f'VERIFIED: {count} three-hop chains from the CISA pilot to ATT&CK mitigation references.')
    print('Saved records: '+str(run_dir))
    print('The answer script still uses two hops; extend it after verifying this import.')
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
