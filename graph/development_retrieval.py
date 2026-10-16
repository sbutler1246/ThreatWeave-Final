"""Bounded, source-verified graph retrieval across imported development scopes.

The evidence context uses a conservative UTF-8 byte cap equal to the configured
token budget. This is deliberately smaller than a typical BPE token budget;
exact shared-tokenizer packing remains a full-system integration task.
"""
import hashlib
import itertools
import json
import re
import time
from collections import defaultdict,deque

from extraction.development_batch import read_inputs
from graph.development_ingestion import local_identity
from import_pilot_mitigations import prepare as prepare_references
from resolve import norm,resolve
from schemas import ALLOWED,Assertion,Entity,EntityCandidate,EvidenceBundle,GraphPath,Passage,RelationshipEdge

PATH_QUERY = """
MATCH p=(anchor:Entity)-[:USES|USES_TECHNIQUE|MITIGATED_BY*1..3]->(endpoint:Entity)
WHERE all(n IN nodes(p) WHERE n:Entity)
  AND all(seed_group IN $seed_groups WHERE any(n IN nodes(p) WHERE n.canonical_id IN seed_group))
RETURN [n IN nodes(p) | properties(n)] AS nodes,
       [r IN relationships(p) | {predicate:type(r), assertion_ids:coalesce(r.assertion_ids,[])}] AS edges,
       length(p) AS hops
ORDER BY hops DESC, anchor.canonical_id, endpoint.canonical_id LIMIT $limit
"""
ASSERTION_QUERY = """
MATCH (a:Assertion)
WHERE a.assertion_id IN $ids AND a.validation_status IN ['validated','human_verified']
MATCH (d:Document {doc_id:a.source_doc_id}),(c:Chunk {chunk_id:a.chunk_id})
WHERE c.doc_id=d.doc_id
RETURN properties(a) AS assertion, properties(d) AS document, properties(c) AS chunk
ORDER BY a.validation_status DESC, a.assertion_id
"""


def source_profiles(repo, *, include_corpus_pilot=True, include_corpus_batch=True, include_corpus_extension=True):
    import pilot_extract
    items,config,catalog,_ = read_inputs(repo)
    document,chunk,*_ = pilot_extract.prepare(repo)
    items = [{'document':document,'chunk':chunk,'spec':{'kind':'table'}}]+items
    profiles,entities = {},{}
    for item in items:
        doc,c = item['document'],item['chunk']
        if item['spec']['kind']=='table':
            lines = c.text.splitlines()
            actor = c.inherited_context[0].text.partition('Tools Used by ')[2]
            candidates = [EntityCandidate(local_id='g',type='ThreatGroup',name=actor),
                          EntityCandidate(local_id='s',type='Software',name=lines[0]),
                          EntityCandidate(local_id='t',type='Technique',name=lines[-1],attack_id=lines[-2])]
            links = [('g','USES','s'),('s','USES_TECHNIQUE','t')]
        else:
            match = re.match(r'^(.*?) (?:used|use) (?:the open-source framework )?([\w.-]+) to ',c.text)
            if not match:
                raise ValueError('Development prose lacks the reviewed explicit use construction.')
            candidates = [EntityCandidate(local_id='g',type='ThreatGroup',name=match[1]),
                          EntityCandidate(local_id='s',type='Software',name=match[2])]
            links = [('g','USES','s')]
        ids = {}
        for candidate in candidates:
            resolved = resolve(candidate,catalog)
            if resolved.status=='conflict':
                raise ValueError('Source-profile identity conflict.')
            entity = resolved.entity or Entity(canonical_id=local_identity(doc.doc_id,candidate),
                type=candidate.type,name=candidate.name,resolution_status='local')
            ids[candidate.local_id] = entity.canonical_id
            entities[entity.canonical_id] = entity.model_dump(mode='json',exclude_none=True)
        profiles[c.chunk_id] = {'document':doc,'chunk':c,
                               'allowed_triples':{(ids[h],p,ids[t]) for h,p,t in links}}
    references = {}
    for entity in list(entities.values()):
        if entity['type']=='Technique':
            for record in prepare_references(repo,entity['attack_id'])['records']:
                references[record['assertion']['assertion_id']] = record
                entities[record['entity']['canonical_id']] = record['entity']
    if include_corpus_pilot:
        from graph.corpus_pilot_scope import expand
        expand(repo, profiles, references, entities)
        if include_corpus_batch:
            from graph.corpus_batch_scope import expand as expand_batch
            expand_batch(repo, profiles, references, entities)
            if include_corpus_extension:
                from graph.corpus_extension_scope import expand as expand_extension
                expand_extension(repo, profiles, references, entities)
    identity = {'profiles': {key:{'source_hash':p['document'].content_hash,
                    'triples':sorted(p['allowed_triples']), 'assertions':p.get('accepted_assertions',{})}
                    for key,p in sorted(profiles.items())}, 'reference_ids':sorted(references)}
    scope_hash = hashlib.sha256(json.dumps(identity,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    config = dict(config, development_scope={'name':('expanded_reviewed_development_sources' if include_corpus_pilot
                else 'six_development_CISA_scopes_and_direct_ATTACK_references'),
                'sha256':scope_hash,'cisa_scope_count':len(profiles),'attack_reference_count':len(references)})
    return profiles,references,entities,config


def seed_groups(question,entities,mentions=(),max_seeds=5):
    text = norm(question)
    extra = defaultdict(list)
    for mention in mentions:
        extra[mention['id']].append(mention['text'])
    occurrences = []
    for entity in entities:
        names = [entity['name']]+(entity.get('aliases') or [])+extra[entity['canonical_id']]
        if entity.get('attack_id'):
            names.append(entity['attack_id'])
        for name in names:
            if name:
                for match in re.finditer(r'(?<!\w)'+re.escape(norm(name))+r'(?!\w)',text):
                    occurrences.append((match.start(),match.end(),entity['canonical_id'],entity['type']))
    matches = {}
    for start,end,identifier,kind in occurrences:
        if any(a <= start and end <= b and b-a > end-start for a,b,_,_ in occurrences):
            continue
        matches[(identifier,kind)] = max(matches.get((identifier,kind),0), end-start)
    groups = defaultdict(list)
    ordered = [(length,identifier,kind) for (identifier,kind),length in matches.items()]
    for _,identifier,kind in sorted(ordered,key=lambda r:(-r[0],r[1]))[:max_seeds]:
        groups[kind].append(identifier)
    return list(groups.values())


def matches_groups(nodes,groups):
    ids = {n['canonical_id'] for n in nodes}
    return bool(groups) and all(ids.intersection(group) for group in groups)


def evidence_context(bundle,names):
    """Compact context; the complete provenance bundle remains in the saved log."""
    lines = ['SOURCE PASSAGES']
    for p in bundle.passages:
        lines.extend([f'[{p.citation_id}; {p.source_kind.upper()}]',p.text])
    ids = []
    for path in bundle.paths:
        for edge in path.edges:
            for identifier in [edge.head_id,edge.tail_id]:
                if identifier not in ids:
                    ids.append(identifier)
    short = {identifier:f'N{i+1}' for i,identifier in enumerate(ids)}
    lines.append('GRAPH NODES')
    lines.extend(f'{short[i]}: {names.get(i,i)} ({i.split(":",1)[1]})' if i.startswith('attack:')
                 else f'{short[i]}: {names.get(i,i)}' for i in ids)
    lines.append('GRAPH PATHS')
    for path in bundle.paths:
        parts = [short[path.edges[0].head_id]]
        for edge in path.edges:
            parts.append(f" --{edge.predicate.value}[{','.join(edge.citation_ids)}]--> {short[edge.tail_id]}")
        lines.append(path.path_id+': '+''.join(parts))
    return '\n'.join(lines)


class DevelopmentGraphRetriever:
    def __init__(self,repo,driver=None,database='neo4j', *, include_corpus_pilot=True, include_corpus_batch=True,
                 include_corpus_extension=True):
        self.repo,self.driver,self.database = repo,driver,database
        self.profiles,self.references,self.expected_entities,self.config = source_profiles(
            repo,include_corpus_pilot=include_corpus_pilot,include_corpus_batch=include_corpus_batch,
            include_corpus_extension=include_corpus_extension)
        self.scope_name = self.config['development_scope']['name']
        settings = self.config['retrieval']
        self.max_seeds = settings['max_seeds']
        self.max_candidates = settings['max_candidate_paths']
        self.max_paths = settings['final_paths']
        self.byte_cap = settings['evidence_token_budget']
        self.max_hops = settings['max_hops']
        if not 1<=self.max_hops<=3:
            raise ValueError('Development retriever supports one to three hops.')
        self.configuration_hash = hashlib.sha256((json.dumps(self.config,sort_keys=True)+PATH_QUERY+
             'development-graph-retrieval-v2-reviewed-scopes;context-cap=utf8-bytes;domain-filter;longest-name-spans').encode()).hexdigest()
        self.last_context,self.last_stats = '',{}

    def _verify_record(self,row,head,predicate,tail):
        props,d,c = row['assertion'],row['document'],row['chunk']
        assertion = Assertion.model_validate({k:v for k,v in props.items() if k in Assertion.model_fields})
        if assertion.validation_status not in {'validated','human_verified'} or props.get('human_review_status')=='rejected':
            return None
        triple = (head,predicate,tail)
        if (assertion.head_id,assertion.predicate.value,assertion.tail_id)!=triple:
            raise ValueError('Graph assertion endpoints differ from its stored relationship.')
        if props.get('triple_key')!=hashlib.sha256('\x1f'.join(triple).encode()).hexdigest():
            raise ValueError('Stored assertion triple key differs from its endpoints.')
        if assertion.origin=='extracted':
            profile = self.profiles.get(assertion.chunk_id)
            if profile is None:
                return None
            doc,chunk = profile['document'],profile['chunk']
            if triple not in profile['allowed_triples']:
                raise ValueError('Stored factual edge is not supported by this development source scope.')
            if 'accepted_assertions' in profile:
                expected = profile['accepted_assertions'].get(assertion.assertion_id)
                if expected is None:
                    return None
                if any(props.get(k) != value for k,value in expected.items()
                       if k not in {'validation_status','human_review_status'}):
                    raise ValueError('Stored assertion differs from its pinned supported source review.')
            if (d.get('doc_id')!=doc.doc_id or d.get('text')!=doc.text or d.get('source_url')!=str(doc.source_url)
                    or d.get('content_hash')!=doc.content_hash or d.get('source')!='cisa'):
                raise ValueError('Stored CISA Document differs from its frozen source.')
            if any(c.get(k)!=getattr(chunk,k) for k in ['chunk_id','doc_id','start','end','text']):
                raise ValueError('Stored CISA Chunk differs from its frozen source.')
            if json.loads(c.get('inherited_context_json','[]'))!=[x.model_dump() for x in chunk.inherited_context]:
                raise ValueError('Stored CISA inherited context differs from its frozen source.')
            start,end = props['evidence_start'],props['evidence_end']
            if (assertion.source_doc_id!=doc.doc_id or props.get('source_hash')!=doc.content_hash
                    or not chunk.start<=start<end<=chunk.end or doc.text[start:end]!=assertion.evidence_text):
                raise ValueError('CISA assertion quote does not match the recorded source span.')
            spans = [(start,end,assertion.evidence_text)]+[(x.start,x.end,x.text) for x in chunk.inherited_context]
            passages = [dict(doc_id=doc.doc_id,chunk_id=chunk.chunk_id,source_url=str(doc.source_url),
                             text=text,start=a,end=b,source_kind='cisa') for a,b,text in spans]
            return {'assertion':assertion,'passages':passages,'scope':chunk.chunk_id}
        reference = self.references.get(assertion.assertion_id)
        if reference is None:
            return None
        immutable = ['head_id','predicate','tail_id','source_doc_id','chunk_id','evidence_text','origin',
                     'triple_key','evidence_start','evidence_end','source_url','source_hash','attack_release',
                     'source_snapshot_sha256','source_stix_relationship_id','source_stix_source_ref',
                     'source_stix_target_ref','source_relationship_type','reference_only']
        if any(props.get(k)!=reference['assertion'][k] for k in immutable):
            raise ValueError('ATT&CK assertion differs from its frozen structured reference.')
        expected_d,expected_c = reference['document'],reference['chunk']
        if any(d.get(k)!=expected_d[k] for k in ['doc_id','source','source_url','text','content_hash',
                                                'source_snapshot_sha256','source_stix_relationship_id','attack_release']):
            raise ValueError('Stored ATT&CK Document differs from its frozen reference.')
        if any(c.get(k)!=expected_c[k] for k in ['chunk_id','doc_id','start','end','text']):
            raise ValueError('Stored ATT&CK Chunk differs from its frozen reference.')
        # Separate contiguous source spans identify the mitigation and quote its
        # guidance; intermediate STIX metadata stays in the full provenance log.
        header_end = d['text'].index('\nSTIX relationship_type:')
        spans = [(0,header_end,d['text'][:header_end]),(c['start'],c['end'],c['text'])]
        passages = [dict(doc_id=d['doc_id'],chunk_id=c['chunk_id'],source_url=d['source_url'],
                         text=text,start=a,end=b,source_kind='attack') for a,b,text in spans]
        return {'assertion':assertion,'passages':passages,'scope':None}

    def _candidate(self,path,records):
        if not 1<=len(path['edges'])<=self.max_hops or len(path['nodes'])!=len(path['edges'])+1:
            raise ValueError('Invalid graph path length.')
        for node in path['nodes']:
            entity = Entity.model_validate({k:v for k,v in node.items() if k in Entity.model_fields})
            expected = self.expected_entities.get(entity.canonical_id)
            if expected is None:
                return None
            if any(node.get(k)!=expected.get(k) for k in ['type','name','attack_id','stix_id','attack_release','resolution_status']):
                raise ValueError('Stored graph entity differs from its source-resolved identity.')
        pools = []
        for i,edge in enumerate(path['edges']):
            left,right = path['nodes'][i],path['nodes'][i+1]
            if (left['type'],edge['predicate'],right['type']) not in ALLOWED:
                raise ValueError('Graph path contains an invalid relationship type pattern.')
            pool = []
            for identifier in edge['assertion_ids']:
                if identifier in records:
                    verified = self._verify_record(records[identifier],left['canonical_id'],edge['predicate'],right['canonical_id'])
                    if verified:
                        pool.append(verified)
            if not pool:
                return None
            pools.append(pool)
        for choice in itertools.product(*pools):
            scopes = {x['scope'] for x in choice if x['scope'] is not None}
            if len(scopes)<=1:
                return {'nodes':path['nodes'],'records':list(choice),
                        'scope':next(iter(scopes)) if scopes else path['nodes'][0]['canonical_id']}
        return None

    def _bundle(self,candidates,retrieval_ms=0):
        passages,paths = {},[]
        for candidate in candidates:
            edges = []
            for record in candidate['records']:
                citations = []
                for p in record['passages']:
                    key = (p['doc_id'],p['start'],p['end'])
                    if key not in passages:
                        passages[key] = Passage(citation_id=f'E{len(passages)+1}',**p)
                    citations.append(passages[key].citation_id)
                a = record['assertion']
                edges.append(RelationshipEdge(head_id=a.head_id,predicate=a.predicate,tail_id=a.tail_id,
                             assertion_ids=[a.assertion_id],citation_ids=citations))
            paths.append(GraphPath(path_id=f'P{len(paths)+1}',edges=edges))
        return EvidenceBundle(passages=list(passages.values()),paths=paths,
                              citation_ids=[p.citation_id for p in passages.values()],
                              retrieval_ms=retrieval_ms,configuration_hash=self.configuration_hash,
                              corpus_version=self.config['corpus_version'])

    def assemble(self,path_rows,record_rows,groups,retrieval_ms=0,path_priority=None):
        records = {r['assertion']['assertion_id']:r for r in record_rows}
        candidates,seen = [],set()
        for path in path_rows:
            if not matches_groups(path['nodes'],groups):
                continue
            candidate = self._candidate(path,records)
            if candidate:
                key = tuple((r['assertion'].head_id,r['assertion'].predicate.value,r['assertion'].tail_id)
                            for r in candidate['records'])
                if key not in seen:
                    candidate['key']=key
                    candidates.append(candidate)
                    seen.add(key)
        # Prefer full supported chains; remove redundant shorter subpaths.
        maximal = [c for c in candidates if not any(len(other['key'])>len(c['key']) and
                   any(other['key'][i:i+len(c['key'])]==c['key'] for i in range(len(other['key'])-len(c['key'])+1))
                   for other in candidates)]
        buckets = defaultdict(deque)
        priority = path_priority or {}
        for candidate in sorted(maximal,key=lambda c:(-len(c['key']),c['scope'],-priority.get(c['key'],0),c['key'])):
            buckets[candidate['scope']].append(candidate)
        order = []
        while any(buckets.values()):
            for key in sorted(buckets):
                if buckets[key]:
                    order.append(buckets[key].popleft())
        selected,names = [],{k:v['name'] for k,v in self.expected_entities.items()}
        skipped = 0
        for candidate in order:
            if len(selected)>=self.max_paths:
                break
            trial = self._bundle(selected+[candidate],retrieval_ms)
            if len(evidence_context(trial,names).encode('utf-8'))>self.byte_cap:
                skipped += 1
                continue
            selected.append(candidate)
        bundle = self._bundle(selected,retrieval_ms)
        self.last_context = evidence_context(bundle,names)
        self.last_stats = {'candidate_path_count':len(candidates),'selected_path_count':len(selected),
                           'selected_hops':[len(p.edges) for p in bundle.paths],
                           'evidence_utf8_bytes':len(self.last_context.encode('utf-8')),
                           'evidence_byte_cap':self.byte_cap,'budget_method':'conservative_utf8_byte_cap',
                           'budget_skipped_paths':skipped,'seed_groups':groups}
        return bundle

    def retrieve(self,request):
        if request.mode.value!='graph_only' or request.corpus_version!=self.config['corpus_version']:
            raise ValueError('This development retriever supports graph_only with its frozen corpus version.')
        started = time.perf_counter()
        with self.driver.session(database=self.database,default_access_mode='READ') as session:
            def read(tx):
                entities = [dict(r['entity']) for r in tx.run(
                    'MATCH (e:Entity) WHERE e.canonical_id IN $ids RETURN properties(e) AS entity ORDER BY e.canonical_id LIMIT 5000',
                    ids=sorted(self.expected_entities))]
                mentions = [r.data() for r in tx.run(
                    'MATCH (e:Entity)-[m:MENTIONED_IN]->(:Document) WHERE m.chunk_id IN $scopes '
                    'RETURN e.canonical_id AS id,m.evidence_text AS text',scopes=list(self.profiles))]
                groups = seed_groups(request.question,entities,mentions,self.max_seeds)
                query = PATH_QUERY.replace('WHERE all(n IN nodes(p) WHERE n:Entity)',
                    'WHERE all(n IN nodes(p) WHERE n:Entity AND n.canonical_id IN $domain_ids)')
                paths = [r.data() for r in tx.run(query,seed_groups=groups,limit=self.max_candidates,
                    domain_ids=sorted(self.expected_entities))] if groups else []
                ids = sorted({identifier for p in paths for e in p['edges'] for identifier in e['assertion_ids']})
                rows = [r.data() for r in tx.run(ASSERTION_QUERY,ids=ids)] if ids else []
                return paths,rows,groups
            paths,rows,groups = session.execute_read(read)
        bundle = self.assemble(paths,rows,groups)
        bundle.retrieval_ms = (time.perf_counter()-started)*1000
        return bundle

    def preview(self,question):
        """Offline source fixtures only; no claim of current live graph presence."""
        from graph.development_projection import preview_projection
        from retrieval.hybrid_retrieval import enumerate_paths, source_mentions
        projection, _, _, records = preview_projection(self)
        paths = enumerate_paths(projection, self.expected_entities, self.max_hops)
        groups = seed_groups(question,list(self.expected_entities.values()),source_mentions(self),self.max_seeds)
        return self.assemble(paths,records,groups)
