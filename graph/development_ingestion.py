"""Prepare and atomically import source-reviewed development predictions."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from extraction.development_batch import read_inputs,validate_candidate
from resolve import norm,resolve
from schemas import Assertion,Entity,ExtractionBatch


def stable_hash(*values):
    return hashlib.sha256('\x1f'.join(values).encode('utf-8')).hexdigest()


def local_identity(document_id,candidate):
    if candidate.type.value=='ThreatGroup':
        suffix = re.sub(r'[^a-z0-9]+','-',norm(candidate.name)).strip('-')
        return f'local:{document_id}:{suffix}'
    return f'local:{document_id}:{candidate.type.value.lower()}:'+hashlib.sha256(candidate.name.encode()).hexdigest()[:12]


def check_source_support(item,batch):
    """Only accept the reviewed positive table/prose constructions in this batch."""
    chunk = item['chunk']
    entities = {e.local_id:e for e in batch.entities}
    if not batch.relations:
        raise ValueError('An empty extraction cannot be imported as reviewed facts.')
    signatures = {(entities[r.head].type.value,entities[r.head].name,r.predicate.value,
                   entities[r.tail].type.value,entities[r.tail].name) for r in batch.relations}
    if len(signatures)!=len(batch.relations):
        raise ValueError('Duplicate candidate relationships require review.')
    if item['spec']['kind']=='table':
        actor = chunk.inherited_context[0].text.partition('Tools Used by ')[2]
        lines = chunk.text.splitlines()
        allowed = {('ThreatGroup',actor,'USES','Software',lines[0]),
                   ('Software',lines[0],'USES_TECHNIQUE','Technique',lines[-1])}
        if not signatures<=allowed:
            raise ValueError('Candidate does not match the reviewed table roles and source scope.')
        return 'frozen_table_roles_and_ID_validation'
    if len(batch.entities)!=2 or len(batch.relations)!=1:
        raise ValueError('This prose importer accepts only the reviewed explicit actor-to-tool construction.')
    relation = batch.relations[0]
    actor,tool = entities[relation.head],entities[relation.tail]
    if actor.type.value!='ThreatGroup' or tool.type.value!='Software' or relation.predicate.value!='USES':
        raise ValueError('Prose candidate has an unsupported endpoint/predicate pattern.')
    pattern = (r'^'+re.escape(actor.name)+r' (?:used|use) '
               r'(?:the open-source framework )?'+re.escape(tool.name)+r' to ')
    if not re.match(pattern,chunk.text):
        raise ValueError('Prose does not explicitly assert this actor used this software.')
    return 'AI_assisted_source_review_and_explicit_use_clause_check'


def prepare_item(item,batch,catalog,summary,record,raw,run_path):
    return prepare_records(item,batch,catalog,summary,record,raw,run_path,
                           check_source_support(item,batch))


def prepare_records(item,batch,catalog,summary,record,raw,run_path,review_method):
    """Serialize records after a caller has validated its specific source-review gate."""
    document,chunk = item['document'],item['chunk']
    entities,mentions,ids,resolutions = [],[],{},[]
    for candidate in batch.entities:
        result = resolve(candidate,catalog)
        if result.status=='conflict' or (candidate.attack_id and result.status!='resolved'):
            raise ValueError('Conflicting or unresolved explicit identity: '+candidate.name)
        entity = result.entity or Entity(canonical_id=local_identity(document.doc_id,candidate),
                    type=candidate.type,name=candidate.name,resolution_status='local')
        props = entity.model_dump(mode='json',exclude_none=True)
        props['normalized_name'] = norm(entity.name)
        entities.append(props)
        ids[candidate.local_id] = entity.canonical_id
        location = next((part for part in [chunk]+chunk.inherited_context if candidate.name in part.text),None)
        if location is None:
            raise ValueError('Source entity mention is missing.')
        start = location.start+location.text.index(candidate.name)
        mentions.append({'canonical_id':entity.canonical_id,'source_doc_id':document.doc_id,
                         'chunk_id':chunk.chunk_id,'evidence_text':candidate.name,
                         'evidence_start':start,'evidence_end':start+len(candidate.name)})
        resolutions.append({'source_name':candidate.name,'canonical_id':entity.canonical_id,
                            'canonical_name':entity.name,'lookup_status':result.status,
                            'resolution_status':entity.resolution_status})
    assertions = []
    raw_hash = hashlib.sha256(raw.encode('utf-8')).hexdigest()
    for relation in batch.relations:
        head,tail,predicate = ids[relation.head],ids[relation.tail],relation.predicate.value
        key = stable_hash(head,predicate,tail)
        aid = 'assertion:'+stable_hash(key,document.doc_id,chunk.chunk_id,relation.evidence.quote,
                                      summary['model_digest'],record['prompt_hash'],raw_hash)
        props = Assertion(assertion_id=aid,head_id=head,predicate=predicate,tail_id=tail,
                          source_doc_id=document.doc_id,chunk_id=chunk.chunk_id,
                          evidence_text=relation.evidence.quote,origin='extracted',
                          validation_status='validated',confidence=relation.confidence).model_dump(mode='json',exclude_none=True)
        props.update(triple_key=key,evidence_start=chunk.start+relation.evidence.start,
                     evidence_end=chunk.start+relation.evidence.end,
                     source_url=str(document.source_url),source_hash=document.content_hash,
                     inherited_context_json=json.dumps([c.model_dump() for c in chunk.inherited_context]),
                     model=summary['model'],model_digest=summary['model_digest'],
                     model_options_json=json.dumps(summary['options'],sort_keys=True),
                     prompt_hash=record['prompt_hash'],raw_output_hash=raw_hash,
                     source_review_method=review_method,human_review_status='pending',
                     source_run=str(run_path),extraction_method=(
                         'source_constrained_table_slots_and_LLM_links' if item['spec']['kind']=='table'
                         else 'LLM_prose_extraction'),scope_assignment='development')
        assertions.append(props)
    doc = document.model_dump(mode='json',exclude_none=True)
    doc.update(canonical_id='doc:'+document.doc_id,name=document.title,type='Document')
    c = chunk.model_dump(mode='json',exclude_none=True)
    c['inherited_context_json'] = json.dumps(c.pop('inherited_context'))
    return {'document':doc,'chunk':c,'entities':entities,'mentions':mentions,
            'assertions':assertions,'identity_resolution':resolutions,
            'run_path':str(run_path),'kind':item['spec']['kind']}


def prepare(repo):
    items,config,catalog,attack_hash = read_inputs(repo)
    run_root = (repo/'work/development_batch').resolve()
    folders = sorted((p for p in run_root.iterdir() if p.is_dir()),reverse=True)
    selected = {}
    allowed = {i['chunk'].chunk_id:i for i in items}
    for folder in folders:
        path = folder/'summary.json'
        if not path.exists():
            continue
        summary = json.loads(path.read_text(encoding='utf-8'))
        if summary.get('purpose')!='development_extraction_batch':
            continue
        for record in summary['items']:
            scope = record['scope_id']
            if scope in allowed and scope not in selected and record['status']=='candidates_ready_for_review':
                selected[scope] = (folder,summary,record)
    prepared,model_digests = [],set()
    for scope,item in allowed.items():
        if scope not in selected:
            raise ValueError('No successful candidate output for development scope: '+scope)
        folder,summary,record = selected[scope]
        if (summary.get('attack_snapshot_hash')!=attack_hash or summary.get('model')!=config['llm']['model']
                or record.get('source_hash')!=item['document'].content_hash or not summary.get('model_digest')):
            raise ValueError('Candidate run differs from frozen source/reference/model metadata.')
        model_digests.add(summary['model_digest'])
        subfolder = (folder/record['folder']).resolve()
        if not subfolder.is_relative_to(folder.resolve()):
            raise ValueError('Candidate folder escapes its recorded run.')
        expected_chunk = item['chunk'].model_dump(mode='json')
        stored_chunk = json.loads((subfolder/'chunk.json').read_text(encoding='utf-8'))
        if stored_chunk!=expected_chunk:
            raise ValueError('Saved chunk differs from the frozen development source.')
        system = (subfolder/'system_prompt.txt').read_text(encoding='utf-8')
        prompt = (subfolder/'user_prompt.txt').read_text(encoding='utf-8')
        if hashlib.sha256((system+'\n'+prompt).encode()).hexdigest()!=record['prompt_hash']:
            raise ValueError('Saved extraction prompt checksum changed.')
        attempts = [a for a in record['attempts'] if not a.get('validation_error') and not a.get('error')]
        if not attempts:
            raise ValueError('No successful recorded model attempt.')
        raw = (subfolder/f"raw_extraction_{attempts[-1]['attempt']}.json").read_text(encoding='utf-8')
        response = json.loads((subfolder/f"ollama_response_{attempts[-1]['attempt']}.json").read_text(encoding='utf-8'))
        if response.get('response')!=raw or response.get('done') is not True or response.get('done_reason')=='length':
            raise ValueError('Saved raw extraction differs from a completed recorded model response.')
        batch,resolution = validate_candidate(raw,item,catalog)
        saved = ExtractionBatch.model_validate_json((subfolder/'candidate_extraction.json').read_text(encoding='utf-8'))
        if batch.model_dump()!=saved.model_dump():
            raise ValueError('Candidate differs from the recorded model output.')
        if json.loads((subfolder/'identity_resolution.json').read_text(encoding='utf-8'))!=resolution:
            raise ValueError('Saved identity resolution differs from the frozen reference catalog.')
        prepared.append(prepare_item(item,batch,catalog,summary,record,raw,folder))
    if len(model_digests)!=1:
        raise ValueError('Selected runs use different model digests; review their compatibility.')
    return {'items':prepared,'prepared_at':datetime.now(timezone.utc).isoformat(),
            'attack_release':'17.1','attack_snapshot_hash':attack_hash,
            'model_digest':next(iter(model_digests)),'human_review_status':'pending'}


def preserve_review(previous,props):
    props = dict(props)
    if previous:
        immutable = ['head_id','predicate','tail_id','source_doc_id','chunk_id','evidence_text',
                     'origin','source_hash','model_digest','prompt_hash','raw_output_hash']
        if any(previous.get(k)!=props[k] for k in immutable):
            raise ValueError('Existing assertion conflicts with this model/source record.')
        if previous.get('validation_status')=='rejected':
            raise ValueError('A rejected assertion requires review before reimport.')
        if previous.get('validation_status')=='human_verified':
            props['validation_status']='human_verified'
        if previous.get('human_review_status'):
            props['human_review_status']=previous['human_review_status']
    return props


def write_transaction(tx,payload):
    now = payload['prepared_at']
    all_assertions = []
    for item in payload['items']:
        doc,chunk = item['document'],item['chunk']
        prior = tx.run('MATCH (d:Document {doc_id:$id}) RETURN d.content_hash AS hash',id=doc['doc_id']).single()
        if prior and prior['hash']!=doc['content_hash']:
            raise ValueError('Existing Document has different frozen content.')
        tx.run('MERGE (d:Document {doc_id:$id}) ON CREATE SET d.created_at=$now SET d += $props',
               id=doc['doc_id'],now=now,props=doc).consume()
        prior = tx.run('MATCH (c:Chunk {chunk_id:$id}) RETURN properties(c) AS props',id=chunk['chunk_id']).single()
        if prior and any(prior['props'].get(k)!=chunk[k] for k in ['doc_id','start','end','text','inherited_context_json']):
            raise ValueError('Existing Chunk has different frozen content or context.')
        tx.run('MERGE (c:Chunk {chunk_id:$id}) ON CREATE SET c.created_at=$now SET c += $props',
               id=chunk['chunk_id'],now=now,props=chunk).consume()
        for entity in item['entities']:
            label = entity['type']
            if label not in {'ThreatGroup','Software','Technique'}:
                raise ValueError('Unsupported development entity type.')
            prior = tx.run('MATCH (e:Entity {canonical_id:$id}) RETURN properties(e) AS props',
                           id=entity['canonical_id']).single()
            if prior and (any(prior['props'].get(k)!=entity[k] for k in ['type','normalized_name'])
                          or (entity.get('attack_release') and prior['props'].get('attack_release')!=entity['attack_release'])):
                raise ValueError('Existing entity has a conflicting identity or ATT&CK release.')
            props = {k:v for k,v in entity.items() if k!='aliases'}
            tx.run('MERGE (e:Entity {canonical_id:$id}) ON CREATE SET e.created_at=$now, e.aliases=$aliases '
                   f'SET e:{label} SET e += $props',id=entity['canonical_id'],now=now,aliases=entity['aliases'],props=props).consume()
        for mention in item['mentions']:
            tx.run('MATCH (e:Entity {canonical_id:$id}),(d:Document {doc_id:$doc}) '
                   'MERGE (e)-[m:MENTIONED_IN {chunk_id:$chunk}]->(d) SET m += $props',
                   id=mention['canonical_id'],doc=mention['source_doc_id'],chunk=mention['chunk_id'],props=mention).consume()
        for assertion in item['assertions']:
            prior = tx.run('MATCH (a:Assertion {assertion_id:$id}) RETURN properties(a) AS props',
                           id=assertion['assertion_id']).single()
            props = preserve_review(prior['props'] if prior else None,assertion)
            tx.run('MERGE (a:Assertion {assertion_id:$id}) ON CREATE SET a.created_at=$now SET a += $props',
                   id=props['assertion_id'],now=now,props=props).consume()
            predicate = props['predicate']
            if predicate not in {'USES','USES_TECHNIQUE'}:
                raise ValueError('Unsupported development predicate.')
            edge_props = {k:v for k,v in props.items() if k not in ['assertion_id','head_id','tail_id','predicate']}
            tx.run('MATCH (h:Entity {canonical_id:$head}),(t:Entity {canonical_id:$tail}) '
                   f'MERGE (h)-[r:{predicate}]->(t) SET r += $props, r.assertion_ids = CASE '
                   'WHEN $aid IN coalesce(r.assertion_ids,[]) THEN r.assertion_ids '
                   'ELSE coalesce(r.assertion_ids,[]) + [$aid] END',head=props['head_id'],tail=props['tail_id'],
                   aid=props['assertion_id'],props=edge_props).consume()
            all_assertions.append(props)
    # Verify every source assertion is connected to its matching stored factual edge.
    count = tx.run('UNWIND $facts AS f MATCH (h:Entity {canonical_id:f.head_id})-[r]->'
                   '(t:Entity {canonical_id:f.tail_id}) MATCH (a:Assertion {assertion_id:f.assertion_id}) '
                   'WHERE type(r)=f.predicate AND f.assertion_id IN r.assertion_ids '
                   "AND a.validation_status IN ['validated','human_verified'] AND a.origin='extracted' "
                   'AND a.head_id=f.head_id AND a.tail_id=f.tail_id AND a.predicate=f.predicate '
                   'AND a.chunk_id=f.chunk_id AND a.source_hash=f.source_hash '
                   'RETURN count(DISTINCT a) AS verified',facts=all_assertions).single()
    if not count or count['verified']!=len(all_assertions):
        raise ValueError('Stored development assertion verification failed; transaction rolled back.')
    return count['verified']
