"""Source-bound development extraction; no gold labels, QA answers or graph writes."""
import hashlib
import copy
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from extraction.parser import parse_extraction, validate_chunk_document
from resolve import norm, resolve
from schemas import ALLOWED, Chunk, Document, Entity, EntityCandidate, ExtractionBatch, RelationCandidate, SourceContext


TYPE_MAP = {'intrusion-set':'ThreatGroup','tool':'Software','malware':'Software',
            'attack-pattern':'Technique','x-mitre-tactic':'Tactic',
            'course-of-action':'Mitigation','campaign':'Campaign'}


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')


def read_inputs(repo, selection_path=None):
    selection_path = selection_path or repo/'extraction/development_batch_sources.json'
    selection = json.loads(selection_path.read_text(encoding='utf-8'))
    manifest = json.loads((repo/'benchmarks/corpus_manifest.json').read_text(encoding='utf-8'))
    split = json.loads((repo/'benchmarks/split_manifest.json').read_text(encoding='utf-8'))
    config = json.loads((repo/'config.json').read_text(encoding='utf-8'))
    if config['attack_release']!='17.1':
        raise ValueError('This batch requires the frozen ATT&CK 17.1 configuration.')
    blocked = set(split['held_out_evidence_scopes'])
    blocked_docs = {s.split(':')[0] for s in blocked}
    allowed = set(split['development_evidence_scopes'])
    if blocked & allowed:
        raise ValueError('Development and held-out scope assignments overlap.')
    records = {r['doc_id']:r for r in manifest['documents']}
    prepared, seen = [], set()
    for spec in selection['sources']:
        scope, doc_id = spec['scope_id'],spec['doc_id']
        if scope in seen or scope in blocked or not scope.startswith(doc_id+':'):
            raise ValueError('Duplicate, held-out or mismatched source scope: '+scope)
        seen.add(scope)
        if spec['assignment']=='existing_development':
            if scope not in allowed:
                raise ValueError('Source is not assigned to existing development: '+scope)
        elif spec['assignment']=='additional_development':
            if doc_id in blocked_docs or ':development:' not in scope:
                raise ValueError('Additional development document contains held-out scopes: '+doc_id)
        else:
            raise ValueError('Unknown development assignment.')
        if spec['kind'] not in {'table','prose'}:
            raise ValueError('Unknown source kind.')
        record = records[doc_id]
        path = (repo/record['text_file']).resolve()
        if not path.is_relative_to(repo):
            raise ValueError('Source file escapes the repository.')
        text = path.read_text(encoding='utf-8')
        content_hash = digest(text)
        if content_hash!=record['normalized_sha256']:
            raise ValueError('Frozen source checksum changed: '+doc_id)
        if not 0<=spec['start']<spec['end']<=len(text):
            raise ValueError('Invalid document offsets: '+scope)
        document = Document(doc_id=doc_id,title=record['title'],source_url=record['source_url'],
                            publication_date=record.get('release_date'),source='cisa',
                            text=text,content_hash=content_hash)
        contexts = []
        for span in spec['contexts']:
            if not 0<=span['start']<span['end']<=len(text):
                raise ValueError('Invalid inherited-context offsets.')
            contexts.append(SourceContext(**span,text=text[span['start']:span['end']]))
        chunk = Chunk(chunk_id=scope,doc_id=doc_id,start=spec['start'],end=spec['end'],
                      text=text[spec['start']:spec['end']],inherited_context=contexts)
        validate_chunk_document(chunk,document)
        if spec['kind']=='table' and (len(contexts)!=2 or 'Tools Used by ' not in contexts[0].text
                                    or 'Tool\nIntended Use\n' not in contexts[1].text):
            raise ValueError('The source table needs its caption and column headers.')
        prepared.append({'spec':spec,'document':document,'chunk':chunk})
    if not prepared:
        raise ValueError('The development batch is empty.')
    raw = (repo/'data/enterprise-attack-17.1.json').read_bytes()
    attack_hash = hashlib.sha256(raw).hexdigest()
    if attack_hash!=manifest['attack_sha256']:
        raise ValueError('Frozen ATT&CK snapshot checksum changed.')
    catalog = []
    for obj in json.loads(raw)['objects']:
        if obj.get('type') not in TYPE_MAP or obj.get('revoked') or obj.get('x_mitre_deprecated'):
            continue
        ids = {r['external_id'] for r in obj.get('external_references',[])
               if r.get('source_name')=='mitre-attack' and r.get('external_id')}
        if len(ids)!=1:
            continue
        identifier = next(iter(ids))
        catalog.append(Entity(canonical_id='attack:'+identifier,type=TYPE_MAP[obj['type']],
                              name=obj['name'],aliases=(obj.get('aliases') or [])+(obj.get('x_mitre_aliases') or []),
                              attack_id=identifier,stix_id=obj['id'],attack_release='17.1',
                              resolution_status='canonical'))
    return prepared,config,catalog,attack_hash


def make_prompt(repo, item):
    original = (repo/'prompts/extraction.txt').read_text(encoding='utf-8')
    system, separator, template = original.partition('\nUSER\n')
    if not separator:
        raise ValueError('Extraction prompt is missing its USER marker.')
    system = system.removeprefix('SYSTEM\n')
    chunk = item['chunk']
    schema = ExtractionBatch.model_json_schema()
    # Whole short chunks provide exact evidence while keeping offset generation
    # reliable. Semantic support is reviewed separately, not inferred from span validity.
    properties = schema['$defs']['EvidenceSpan']['properties']
    properties['start']['const'] = 0
    properties['end']['const'] = len(chunk.text)
    properties['quote']['const'] = chunk.text
    schema['$defs']['RelationCandidate']['properties']['head']['description']='An entity local_id, never a name.'
    schema['$defs']['RelationCandidate']['properties']['tail']['description']='An entity local_id, never a name.'
    patterns = '\n'.join(f'{a} --{b}--> {c}' for a,b,c in sorted(ALLOWED))
    system += '\nPERMITTED ENDPOINT PATTERNS:\n'+patterns
    if item['spec']['kind']=='table':
        # Table roles and names are supplied by explicit structured columns, not
        # benchmark labels. The model still chooses which supported links to return.
        system = system.split('FEW-SHOT EXAMPLE 1',1)[0]
        system += '\nFor tables, return actor, software, technique, and relations. '
        system += 'Do not return an entities array. Keep the fixed source roles separate.\n'
        lines = chunk.text.splitlines()
        if len(lines)!=5 or not re.fullmatch(r'T\d{4}(?:\.\d{3})?',lines[-2]):
            raise ValueError('This table format requires five explicit source columns ending in a technique ID/label.')
        actor_name = chunk.inherited_context[0].text.partition('Tools Used by ')[2]
        if not actor_name:
            raise ValueError('Table actor is missing from the source caption.')
        slot_values = {
            'actor':{'local_id':'e1','type':'ThreatGroup','name':actor_name,'attack_id':None},
            'software':{'local_id':'e2','type':'Software','name':lines[0],'attack_id':None},
            'technique':{'local_id':'e3','type':'Technique','name':lines[-1],'attack_id':lines[-2]},
        }
        slot_schemas = {}
        for slot,values in slot_values.items():
            slot_schema = copy.deepcopy(schema['$defs']['EntityCandidate'])
            for field,value in values.items():
                slot_schema['properties'][field] = {'type':'null' if value is None else 'string','const':value}
            slot_schema['required'] = list(values)
            slot_schemas[slot] = slot_schema
        relation_options = []
        for head,predicate,tail in [('e1','USES','e2'),('e2','USES_TECHNIQUE','e3')]:
            option = copy.deepcopy(schema['$defs']['RelationCandidate'])
            for field,value in [('head',head),('predicate',predicate),('tail',tail)]:
                option['properties'][field] = {'type':'string','const':value}
            relation_options.append(option)
        schema = {'title':'SourceBoundTableExtraction','type':'object','additionalProperties':False,
                  '$defs':schema['$defs'],'properties':dict(slot_schemas,
                      relations={'type':'array','maxItems':2,'items':{'anyOf':relation_options}}),
                  'required':['actor','software','technique','relations']}
        synthetic = 'Tool Delta\nChecks network devices.\nFinds exposed services.\nNetwork Probing'
        evidence = {'start':0,'end':len(synthetic),'quote':synthetic}
        example = {
            'actor':{'local_id':'e1','type':'ThreatGroup','name':'Group Gamma','attack_id':None},
            'software':{'local_id':'e2','type':'Software','name':'Tool Delta','attack_id':None},
            'technique':{'local_id':'e3','type':'Technique','name':'Network Probing','attack_id':None},
            'relations':[
                {'head':'e1','predicate':'USES','tail':'e2','evidence':evidence,'confidence':None},
                {'head':'e2','predicate':'USES_TECHNIQUE','tail':'e3','evidence':evidence,'confidence':None}]}
        system += ('\nSynthetic table example, never facts to extract:\n'
                   'CAPTION: Tools used by Group Gamma\nCHUNK_TEXT:\n'+synthetic+
                   '\nOUTPUT:\n'+json.dumps(example))
        instruction = ('Read the row using its headers: the first line names Software, '
                       'followed by intended use, repurposed use, and explicit ATT&CK ID/label. '
                       'The caption supplies the actor. Preserve the Affiliates qualifier. '
                       'Include supported actor-to-tool USES and tool-to-behavior USES_TECHNIQUE '
                       'links. A technique ID describes behavior, not software. An ID may have '
                       'a historical label in the source: preserve that exact source spelling; '
                       'canonical identity resolution occurs after extraction.')
    else:
        instruction = ('Extract explicit facts from this prose passage. Use actor and software '
                       'names exactly as stated. Preserve qualifiers such as affiliates. '
                       'Do not add a technique or ID from general knowledge. If a relation '
                       'is uncertain, negated, hypothetical, or absent, omit it. A named '
                       'software tool used by an actor may support USES even when the passage '
                       'contains no explicit technique name or ATT&CK ID.')
    prompt = template.format(doc_id=chunk.doc_id,chunk_id=chunk.chunk_id,chunk_text=chunk.text,
                             inherited_context=json.dumps([c.model_dump() for c in chunk.inherited_context],ensure_ascii=False))
    endpoint_instruction = ('Keep the fixed actor/software/technique slots and their local_id values. '
                            'Only return source-supported relations; relations may be empty. '
                            if item['spec']['kind']=='table' else
                            'Return all endpoints in entities using local_id. ')
    prompt += ('\n'+instruction+'\nUse the entire CHUNK_TEXT as the evidence quote for '
               f'each supported relation: start=0, end={len(chunk.text)}. '
               +endpoint_instruction+'Entity names must appear '
               'literally in CHUNK_TEXT or its inherited caption. Return JSON only.')
    system += '\nOUTPUT JSON SCHEMA:\n'+json.dumps(schema,ensure_ascii=False)
    return system,prompt,schema


def validate_candidate(raw,item,catalog):
    value = json.loads(raw)
    if not isinstance(value,dict):
        raise ValueError('Extraction output must be a JSON object.')
    if item['spec']['kind']=='table' and 'entities' not in value:
        if set(value)!={'actor','software','technique','relations'}:
            raise ValueError('Table output must contain exactly actor, software, technique and relations.')
        if not isinstance(value['relations'],list):
            raise ValueError('Table relations must be a list.')
        lines = item['chunk'].text.splitlines()
        actor_name = item['chunk'].inherited_context[0].text.partition('Tools Used by ')[2]
        expected = {
            'actor':{'local_id':'e1','type':'ThreatGroup','name':actor_name,'attack_id':None},
            'software':{'local_id':'e2','type':'Software','name':lines[0],'attack_id':None},
            'technique':{'local_id':'e3','type':'Technique','name':lines[-1],'attack_id':lines[-2]},
        }
        entities = []
        for slot,fields in expected.items():
            entity = EntityCandidate.model_validate(value[slot])
            if entity.model_dump(mode='json')!=fields:
                raise ValueError('Table slot differs from its explicit source column: '+slot)
            entities.append(entity.model_dump(mode='json'))
        keys = set()
        for relation in value['relations']:
            checked = RelationCandidate.model_validate(relation)
            key = (checked.head,checked.predicate.value,checked.tail)
            if key not in {('e1','USES','e2'),('e2','USES_TECHNIQUE','e3')} or key in keys:
                raise ValueError('Invalid or duplicate table relationship endpoints/predicate.')
            keys.add(key)
        raw = json.dumps({'entities':entities,'relations':value['relations']},ensure_ascii=False)
    batch = parse_extraction(raw,item['chunk'])
    chunk = item['chunk']
    source = chunk.text+'\n'+'\n'.join(c.text for c in chunk.inherited_context)
    explicit_ids = set(re.findall(r'\b(?:TA\d{4}|T\d{4}(?:\.\d{3})?|[GSMC]\d{4})\b',source))
    by_attack = {}
    for entity in catalog:
        by_attack.setdefault(entity.attack_id,[]).append(entity)
    resolution = []
    tool_name = chunk.text.splitlines()[0] if item['spec']['kind']=='table' else None
    caption_actor = chunk.inherited_context[0].text.partition('Tools Used by ')[2] if tool_name else None
    for candidate in batch.entities:
        if candidate.name not in source:
            raise ValueError('Entity name is not a literal source mention: '+candidate.name)
        if tool_name and norm(candidate.name)==norm(tool_name) and candidate.type.value!='Software':
            raise ValueError('The Tool column names Software, not an attack behavior.')
        if candidate.type.value=='ThreatGroup':
            if caption_actor and norm(candidate.name)!=norm(caption_actor):
                raise ValueError('Preserve the full actor name and Affiliates qualifier from the caption.')
            if not caption_actor and 'affiliates' not in norm(candidate.name):
                # Check this actor's actual supporting passages. An unrelated
                # affiliate sentence elsewhere in the window cannot rename it.
                supports = [r.evidence.quote for r in batch.relations
                            if candidate.local_id in {r.head, r.tail}]
                truncated = re.compile(r'(?<!\w)'+re.escape(candidate.name)+
                    r'\s+(?:(?:ransomware|group|threat)\s+)?affiliates\b', re.I)
                if any(truncated.search(support) for support in supports):
                    raise ValueError('Preserve the affiliates qualifier in this prose actor mention.')
        if candidate.attack_id:
            matches = by_attack.get(candidate.attack_id,[])
            if candidate.attack_id not in explicit_ids or len(matches)!=1 or matches[0].type!=candidate.type:
                raise ValueError('Explicit ATT&CK ID is absent, ambiguous, or incompatible with the entity type.')
            if tool_name:
                # ID/name pairs in a table's final columns identify the behavior.
                lines = chunk.text.splitlines()
                if candidate.attack_id not in lines:
                    raise ValueError('Table ID is not an explicit column value.')
                position = lines.index(candidate.attack_id)
                label = lines[position+1] if position+1<len(lines) else ''
                canonical = matches[0]
                valid_names = {norm(label),norm(canonical.name),*(norm(a) for a in canonical.aliases)}
                if norm(candidate.name) not in valid_names:
                    raise ValueError('ATT&CK ID is attached to a different source entity.')
        result = resolve(candidate,catalog)
        if result.status=='conflict':
            raise ValueError('Identity conflict: '+result.reason)
        resolution.append({'local_id':candidate.local_id,'mention':candidate.name,
                           'status':result.status,'reason':result.reason,
                           'canonical_id':result.entity.canonical_id if result.entity else None,
                           'canonical_name':result.entity.name if result.entity else None,
                           'source_attack_id':candidate.attack_id})
    return batch,resolution


def select_retry_items(repo,items,run_path,config,attack_hash):
    run_path = run_path.resolve()
    if not run_path.is_relative_to((repo/'work/development_batch').resolve()):
        raise ValueError('Retry run must be inside this repository work/development_batch folder.')
    previous = json.loads((run_path/'summary.json').read_text(encoding='utf-8'))
    if previous.get('attack_snapshot_hash')!=attack_hash or previous.get('model')!=config['llm']['model']:
        raise ValueError('Retry run uses a different snapshot or model.')
    failed = {r['scope_id']:r for r in previous['items'] if r['status'] in {'validation_failed','service_error'}}
    selected = []
    for item in items:
        old = failed.get(item['chunk'].chunk_id)
        if old:
            if old['source_hash']!=item['document'].content_hash:
                raise ValueError('Failed source scope has changed since the previous run.')
            selected.append(item)
    if len(selected)!=len(failed):
        raise ValueError('Retry run contains a failed scope outside the current development selection.')
    return selected


def run_batch(repo,items,config,catalog,attack_hash,timeout=60,retry_run=None):
    import requests
    http = requests.Session()
    http.trust_env = False
    llm = config['llm']
    tags = http.get('http://localhost:11434/api/tags',timeout=(5,10))
    tags.raise_for_status()
    model = next((m for m in tags.json().get('models',[]) if m.get('name')==llm['model']),None)
    if not model or not model.get('digest'):
        raise ValueError('Configured Ollama model/digest is not available.')
    if llm.get('digest') and llm['digest']!=model['digest']:
        raise ValueError('Installed model digest differs from the pinned configuration.')
    if retry_run:
        previous = json.loads((retry_run/'summary.json').read_text(encoding='utf-8'))
        if previous.get('model_digest')!=model['digest']:
            raise ValueError('Installed model digest differs from the batch being retried.')
    output = repo/'work/development_batch'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True,exist_ok=False)
    options = {k:llm[k] for k in ['temperature','num_ctx','num_predict']}
    summary = {'purpose':'development_extraction_batch','status':'running',
               'semantic_review_status':'pending','model':llm['model'],'model_digest':model['digest'],
               'options':options,'attack_snapshot_hash':attack_hash,'attack_release':'17.1',
               'scope_assignment':'development','graph_writes':False,'items':[]}
    summary.update(prompt_version='development-batch-v2-table-slots',
                   retry_of=str(retry_run.resolve()) if retry_run else None)
    save(output/'summary.json',summary)
    for number,item in enumerate(items,1):
        chunk,document = item['chunk'],item['document']
        folder = output/f'{number:02d}'
        folder.mkdir()
        system,original,schema = make_prompt(repo,item)
        save(folder/'chunk.json',chunk.model_dump(mode='json'))
        save(folder/'source_metadata.json',dict(item['spec'],title=document.title,
             source_url=str(document.source_url),source_hash=document.content_hash))
        (folder/'system_prompt.txt').write_text(system,encoding='utf-8')
        (folder/'user_prompt.txt').write_text(original,encoding='utf-8')
        save(folder/'output_schema.json',schema)
        record = {'scope_id':chunk.chunk_id,'doc_id':document.doc_id,'source_hash':document.content_hash,
                  'kind':item['spec']['kind'],'folder':folder.name,'status':'started','attempts':[],
                  'output_format':'table_slots_v1' if item['spec']['kind']=='table' else 'ExtractionBatch',
                  'prompt_hash':digest(system+'\n'+original),'semantic_review_status':'pending'}
        summary['items'].append(record)
        print(f'[{number}/{len(items)}] {chunk.chunk_id}',flush=True)
        prompt = original
        for attempt in range(1,3):
            info = {'attempt':attempt}
            record['attempts'].append(info)
            started = time.perf_counter()
            raw = ''
            try:
                response = http.post('http://localhost:11434/api/generate',timeout=(5,timeout),json={
                    'model':llm['model'],'system':system,'prompt':prompt,'format':schema,
                    'stream':False,'options':options})
                response.raise_for_status()
                body = response.json()
                save(folder/f'ollama_response_{attempt}.json',body)
                raw = body.get('response','')
                if not isinstance(raw,str):
                    raise ValueError('Ollama did not return a response string.')
                (folder/f'raw_extraction_{attempt}.json').write_text(raw,encoding='utf-8')
                if body.get('done') is not True or body.get('done_reason')=='length':
                    raise ValueError('Generation did not finish within the configured output budget.')
                if item['spec']['kind']=='table':
                    generated = json.loads(raw)
                    if not isinstance(generated,dict) or set(generated)!={'actor','software','technique','relations'}:
                        raise ValueError('Return the requested actor/software/technique table slots, not an entities array.')
                batch,resolution = validate_candidate(raw,item,catalog)
                info.update(elapsed_seconds=round(time.perf_counter()-started,3),
                            prompt_eval_count=body.get('prompt_eval_count'),eval_count=body.get('eval_count'))
                save(folder/'candidate_extraction.json',batch.model_dump(mode='json'))
                save(folder/'identity_resolution.json',resolution)
                record.update(status='candidates_ready_for_review' if batch.relations else 'empty_extraction',
                              entity_count=len(batch.entities),relation_count=len(batch.relations))
                if item['spec']['kind']=='table':
                    record['has_actor_tool_technique_chain'] = {
                        (r.head,r.predicate.value,r.tail) for r in batch.relations
                    }=={('e1','USES','e2'),('e2','USES_TECHNIQUE','e3')}
                print(f"  {len(batch.entities)} entities; {len(batch.relations)} candidate relationships; review pending.",flush=True)
                break
            except requests.RequestException as error:
                info.update(elapsed_seconds=round(time.perf_counter()-started,3),error=str(error))
                record.update(status='service_error',error=str(error))
                print('  Service error; recorded and continuing to the next scope.',flush=True)
                break
            except ValueError as error:
                info.update(elapsed_seconds=round(time.perf_counter()-started,3),validation_error=str(error))
                if attempt==2:
                    record.update(status='validation_failed',error=str(error))
                    print('  Validation failed after one repair; diagnostics saved.',flush=True)
                    break
                print('  Requesting one schema/source repair.',flush=True)
                prompt = original+'\nRepair this validation error using only the source: '+str(error)+'\nPREVIOUS OUTPUT:\n'+raw
                (folder/'repair_prompt.txt').write_text(prompt,encoding='utf-8')
            finally:
                save(output/'summary.json',summary)
    http.close()
    ready = sum(r['status']=='candidates_ready_for_review' for r in summary['items'])
    failures = sum(r['status'] in {'service_error','validation_failed'} for r in summary['items'])
    summary.update(status='batch_processed_with_errors' if failures else 'batch_processed',
                   ready_for_review=ready,failed_scopes=failures,
                   empty_scopes=sum(r['status']=='empty_extraction' for r in summary['items']),
                   candidate_relation_count=sum(r.get('relation_count',0) for r in summary['items']),
                   finished_at=datetime.now(timezone.utc).isoformat())
    save(output/'summary.json',summary)
    lines = ['# Development batch candidate review','',
             'Schema, literal evidence and identity checks are separate from semantic support.',
             'These are development candidates. No database writes or evaluation scores were produced.','']
    for item,record in zip(items,summary['items']):
        lines += ['## '+record['scope_id'],'','Status: '+record['status'],'',
                  'Source: '+str(item['document'].source_url),'',
                  'Source text:','',item['chunk'].text,'']
        for context in item['chunk'].inherited_context:
            lines += ['Inherited source context:','',context.text,'']
        candidate_path = output/record['folder']/'candidate_extraction.json'
        if candidate_path.exists():
            batch = ExtractionBatch.model_validate_json(candidate_path.read_text(encoding='utf-8'))
            names = {e.local_id:e.name for e in batch.entities}
            lines += ['Candidate relations:','']+[f'- {names[r.head]} → {r.predicate.value} → {names[r.tail]}' for r in batch.relations]+['']
    review_path = repo/'docs'/('ThreatWeave_development_batch_review_'+output.name+'.md')
    review_path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'\nBATCH PROCESSED: {ready}/{len(items)} scopes have candidates ready for semantic review; {failures} failed.',flush=True)
    print('Saved results: '+str(output))
    print('Saved review document: '+str(review_path))
    return 1 if failures else 0
