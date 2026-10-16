"""Expand development scope only from the pinned source and mitigation import receipts."""
import json

from graph.corpus_pilot_mitigations import prepare as prepare_references
from resolve import norm
from schemas import Chunk, Document

MITIGATION_RUN = '20261015T041247Z-529903c7'


def expand(repo, profiles, references, entities, *, preparer=None,
           mitigation_kind='corpus_pilot_mitigations', mitigation_run=MITIGATION_RUN):
    payload = (preparer or prepare_references)(repo)
    folder = repo/'work'/mitigation_kind/mitigation_run
    receipt = json.loads((folder/'import_receipt.json').read_text(encoding='utf-8'))
    saved = json.loads((folder/'prepared_records.json').read_text(encoding='utf-8'))
    for key in ['source_assertions','source_reference_pairs','three_hop_chains','technique_ids',
                'techniques_without_direct_references','source_import_run','review_manifest_sha256']:
        if saved.get(key) != payload[key]:
            raise ValueError('Imported mitigation scope differs from the verified source/reference plan.')
    if ([{k:p[k] for k in ['technique','snapshot_sha256','records']} for p in saved['parts']]
            != [{k:p[k] for k in ['technique','snapshot_sha256','records']} for p in payload['parts']]):
        raise ValueError('Imported frozen reference records changed.')
    records = [r for part in payload['parts'] for r in part['records']]
    expected = {'status':'import_complete', 'origin':'fused', 'attack_release':'17.1',
                'snapshot_sha256':payload['parts'][0]['snapshot_sha256'],
                'reference_assertion_count':len(records),
                'target_mitigation_entity_count':len({r['entity']['canonical_id'] for r in records}),
                'source_reference_combination_count':len(payload['source_reference_pairs']),
                'same_window_three_hop_chain_count':len(payload['three_hop_chains']),
                'techniques_without_direct_references':payload['techniques_without_direct_references'],
                'source_import_run':payload['source_import_run'],
                'review_manifest_sha256':payload['review_manifest_sha256']}
    if any(receipt.get(k) != value for k,value in expected.items()):
        raise ValueError('A matching completed corpus-pilot mitigation import receipt is required.')
    source = json.loads((repo/payload['source_import_run']/'prepared_records.json').read_text(encoding='utf-8'))
    def add_entity(entity):
        old = entities.get(entity['canonical_id'])
        if old and (norm(old['name']) != norm(entity['name']) or any(old.get(k) != entity.get(k) for k in
                       ['type','attack_id','stix_id','attack_release','resolution_status','aliases'])):
            raise ValueError('Expanded source identity conflicts with the original development scope.')
        entities[entity['canonical_id']] = entity
    for item in source['items']:
        doc = Document.model_validate({k:v for k,v in item['document'].items() if k in Document.model_fields})
        raw = item['chunk']
        chunk = Chunk.model_validate(dict({k:v for k,v in raw.items() if k in Chunk.model_fields},
                                          inherited_context=json.loads(raw['inherited_context_json'])))
        if chunk.chunk_id in profiles:
            raise ValueError('Expanded source scope duplicates an existing parent ID.')
        profiles[chunk.chunk_id] = {'document':doc, 'chunk':chunk,
            'allowed_triples':{(a['head_id'],a['predicate'],a['tail_id']) for a in item['assertions']},
            'accepted_assertions':{a['assertion_id']:a for a in item['assertions']},
            'source_mentions':[{'id':m['canonical_id'],'text':m['evidence_text']} for m in item['mentions']]}
        for entity in item['entities']:
            add_entity(entity)
    for record in records:
        key = record['assertion']['assertion_id']
        if key in references and references[key] != record:
            raise ValueError('Expanded ATT&CK reference conflicts with the original development scope.')
        references[key] = record
        add_entity(record['entity'])
