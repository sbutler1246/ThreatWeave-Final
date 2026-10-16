"""Direct frozen mitigation references anchored to the verified development import."""
import json
from datetime import datetime, timezone
from pathlib import Path

from graph.corpus_pilot_ingestion import prepare as prepare_predictions
from import_pilot_mitigations import prepare as prepare_technique, write_reference_records

IMPORT_RUN = '20261015T040329Z-5b1d9d11'
ASSERTIONS_QUERY = 'UNWIND $ids AS id MATCH (a:Assertion {assertion_id:id}) RETURN properties(a) AS props'
EDGES_QUERY = '''
UNWIND $facts AS f
MATCH (h:Entity {canonical_id:f.head_id})-[r]->(t:Entity {canonical_id:f.tail_id})
WHERE type(r)=f.predicate AND f.assertion_id IN coalesce(r.assertion_ids,[])
RETURN count(DISTINCT f.assertion_id) AS verified
'''
EXTENSIONS_QUERY = '''
UNWIND $pairs AS pair
MATCH (a:Assertion {assertion_id:pair.source}),(b:Assertion {assertion_id:pair.reference})
MATCH (h:Entity {canonical_id:a.head_id})-[r:USES_TECHNIQUE]->(t:Entity {canonical_id:a.tail_id})
      -[m:MITIGATED_BY]->(target:Entity {canonical_id:b.tail_id})
WHERE a.assertion_id IN r.assertion_ids AND b.assertion_id IN m.assertion_ids AND b.head_id=t.canonical_id
RETURN count(DISTINCT pair.key) AS verified
'''
CHAINS_QUERY = '''
UNWIND $chains AS chain
MATCH (a:Assertion {assertion_id:chain.actor}),(b:Assertion {assertion_id:chain.source}),
      (c:Assertion {assertion_id:chain.reference})
MATCH (g:Entity {canonical_id:a.head_id})-[r1:USES]->(s:Entity {canonical_id:a.tail_id})
      -[r2:USES_TECHNIQUE]->(t:Entity {canonical_id:b.tail_id})
      -[r3:MITIGATED_BY]->(m:Entity {canonical_id:c.tail_id})
WHERE a.assertion_id IN r1.assertion_ids AND b.assertion_id IN r2.assertion_ids
      AND c.assertion_id IN r3.assertion_ids AND b.head_id=s.canonical_id AND c.head_id=t.canonical_id
      AND a.chunk_id=b.chunk_id AND a.source_doc_id=b.source_doc_id
RETURN count(DISTINCT chain.key) AS verified
'''


def prepare(repo, *, prediction_preparer=None, import_kind='corpus_pilot_ingestion', import_run=IMPORT_RUN):
    repo = Path(repo).resolve()
    predictions = (prediction_preparer or prepare_predictions)(repo)
    folder = repo/'work'/import_kind/import_run
    saved = json.loads((folder/'prepared_records.json').read_text(encoding='utf-8'))
    receipt = json.loads((folder/'import_receipt.json').read_text(encoding='utf-8'))
    for key in predictions.keys() - {'prepared_at'}:
        if saved.get(key) != predictions[key]:
            raise ValueError('Imported source/review selection differs from the current pinned preview.')
    facts = [a for item in predictions['items'] for a in item['assertions']]
    entities = {e['canonical_id']:e for item in predictions['items'] for e in item['entities']}
    if (receipt.get('status') != 'import_complete'
            or receipt.get('verified_assertion_count') != len(facts)
            or receipt.get('scope_count') != len(predictions['items'])
            or receipt.get('target_entity_count') != len(entities)
            or receipt.get('excluded_candidate_count') != len(predictions['excluded_candidates'])
            or receipt.get('factual_relationship_count') != len({a['triple_key'] for a in facts})
            or receipt.get('review_manifest_sha256') != predictions['review_manifest_sha256']):
        raise ValueError('A matching completed pilot import receipt is required.')
    techniques = sorted(e['attack_id'] for e in entities.values() if e['type']=='Technique')
    parts, no_references = [], []
    for identifier in techniques:
        part = prepare_technique(repo, identifier, allow_empty=True)
        if part['records']:
            parts.append(part)
        else:
            no_references.append(identifier)
    pairs, chains = [], []
    for part in parts:
        uses = [a for a in facts if a['predicate']=='USES_TECHNIQUE' and a['tail_id']==part['technique']['canonical_id']]
        for use in uses:
            for record in part['records']:
                reference = record['assertion']['assertion_id']
                pair = {'source':use['assertion_id'], 'reference':reference,
                        'key':use['assertion_id']+'|'+reference}
                pairs.append(pair)
                for actor in facts:
                    if (actor['predicate']=='USES' and actor['tail_id']==use['head_id']
                            and actor['chunk_id']==use['chunk_id'] and actor['source_doc_id']==use['source_doc_id']):
                        chains.append(dict(pair, actor=actor['assertion_id'], key=actor['assertion_id']+'|'+pair['key']))
    return {'parts':parts, 'source_assertions':facts, 'source_reference_pairs':pairs,
            'three_hop_chains':chains, 'technique_ids':techniques,
            'techniques_without_direct_references':no_references,
            'source_import_run':str(folder), 'review_manifest_sha256':predictions['review_manifest_sha256'],
            'prepared_at':datetime.now(timezone.utc).isoformat()}


def verify_assertions(tx, expected):
    rows = list(tx.run(ASSERTIONS_QUERY, ids=[a['assertion_id'] for a in expected]))
    actual = {row['props']['assertion_id']:row['props'] for row in rows}
    if len(rows) != len(expected) or len(actual) != len(expected):
        raise ValueError('Expected source/reference assertions are missing; transaction rolled back.')
    for wanted in expected:
        stored = actual.get(wanted['assertion_id'], {})
        if (stored.get('validation_status') not in {'validated','human_verified'}
                or stored.get('human_review_status') == 'rejected' or any(
                stored.get(key) != value for key,value in wanted.items()
                if key not in {'validation_status','human_review_status'})):
            raise ValueError('Stored assertion differs from reviewed/frozen evidence; transaction rolled back.')
    count = tx.run(EDGES_QUERY, facts=expected).single()
    if not count or count['verified'] != len(expected):
        raise ValueError('Stored assertion edges are missing; transaction rolled back.')


def write_transaction(tx, payload):
    verify_assertions(tx, payload['source_assertions'])
    count = sum(write_reference_records(tx, part) for part in payload['parts'])
    references = [r['assertion'] for p in payload['parts'] for r in p['records']]
    verify_assertions(tx, references)
    for query, records in [(EXTENSIONS_QUERY,payload['source_reference_pairs']),
                           (CHAINS_QUERY,payload['three_hop_chains'])]:
        if records:
            key = 'pairs' if query == EXTENSIONS_QUERY else 'chains'
            verified = tx.run(query, **{key:records}).single()
            if not verified or verified['verified'] != len(records):
                raise ValueError('Source-to-mitigation paths are incomplete; transaction rolled back.')
    return count, len(payload['source_reference_pairs']), len(payload['three_hop_chains'])
