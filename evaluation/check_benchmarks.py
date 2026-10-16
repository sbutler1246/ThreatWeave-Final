"""Structural readiness gate. Reviewer provenance is explicit; no model scores are run."""
import json
from pathlib import Path

def check(root):
    root=Path(root)
    g=json.loads((root/'gold_triples.json').read_text(encoding='utf-8'))
    q=json.loads((root/'eval_queries.json').read_text(encoding='utf-8'))
    errors=[]; ids=set(); keys=set()
    if sum(t.get('verified') is True for t in g['triples'])<50: errors.append('Need at least 50 verified unique gold triples')
    if sum(t.get('verified') is True for t in q['queries'])<20: errors.append('Need at least 20 reviewed multi-hop QA pairs')
    if not g['annotation_scope']:errors.append('Missing complete annotation scope')
    if g.get('annotation_scope_complete') is not True:errors.append('Complete human annotation of scope is required')
    for t in g['triples']:
        try:
            signature=(t['head_id'],t['predicate'],t['tail_id'])
            if t['id'] in ids or signature in keys:errors.append('Duplicate triple ID or canonical fact')
            ids.add(t['id']);keys.add(signature)
            if t['verified'] is not True or not t['reviewer'] or not t['verified_at']:
                errors.append('Triple needs human verification record')
            if t['chunk_id'] not in g['annotation_scope']:errors.append('Triple outside scope')
            span=t['evidence']; chunk=t['source_chunk_text']
            if span['start']<0 or span['end']>len(chunk) or chunk[span['start']:span['end']]!=span['quote']:
                errors.append('Triple evidence span mismatch')
        except (KeyError,TypeError):errors.append('Incomplete gold triple record')
    references_file=root/'reference_triples.json'
    references=json.loads(references_file.read_text(encoding='utf-8'))['triples'] if references_file.exists() else []
    by_id={t.get('id'):t for t in [*g['triples'],*references]}
    path_ids=set(by_id)
    query_ids=set();question_texts=set();query_scopes={}
    for item in q['queries']:
        try:
            if item['id'] in query_ids:errors.append('Duplicate query ID')
            query_ids.add(item['id'])
            normalized_question=item['question'].strip().casefold()
            if normalized_question in question_texts:errors.append('Duplicate question wording')
            question_texts.add(normalized_question)
            if item['verified'] is not True or not item['reviewer'] or not item['verified_at']:
                errors.append('QA needs explicit reviewer verification record')
            if not item['question'] or not item['reference_answer'] or not item['expected_facts']:
                errors.append('QA requires question, answer, and expected facts')
            if not item['required_paths']: errors.append('QA requires a supporting multi-hop path')
            scopes=set();expected_facts=set()
            for path in item['required_paths']:
                if len(path) not in (2,3):errors.append('Required benchmark path must contain two or three edges')
                if not all(edge['triple_id'] in path_ids for edge in path):
                    errors.append('Unknown gold triple in path');continue
                endpoints=[]
                for edge in path:
                    t=by_id[edge['triple_id']]
                    fact=f"{t['head_id']} {t['predicate']} {t['tail_id']}"
                    if t.get('origin','extracted')=='extracted':
                        supports=[s for s in [t,*t.get('additional_support',[])]
                                  if s['doc_id']==edge.get('source_doc_id') and s['chunk_id']==edge.get('source_chunk_id')]
                        if len(supports)!=1:errors.append('QA edge needs an exact supporting document and scope')
                        else:scopes.add(supports[0]['chunk_id'])
                        if item.get('category')=='cross_report_comparison':fact=edge.get('source_doc_id','')+': '+fact
                    expected_facts.add(fact)
                    pair=(t['head_id'],t['tail_id'])
                    if edge['direction']=='reverse': pair=pair[::-1]
                    elif edge['direction']!='forward':errors.append('Unknown edge direction')
                    endpoints.append(pair)
                if any(a[1]!=b[0] for a,b in zip(endpoints,endpoints[1:])):errors.append('Disconnected path')
            query_scopes[item['id']]=scopes
            if set(item.get('evidence_scopes',[]))!=scopes:errors.append('QA declared scopes do not match supporting paths')
            if set(item['expected_facts'])!=expected_facts:errors.append('QA expected facts do not match scoped paths')
        except (KeyError,TypeError):errors.append('Incomplete QA record')
    from collections import Counter
    split_file=root/'split_manifest.json'
    selected=q['queries']
    if split_file.exists():
        manifest=json.loads(split_file.read_text(encoding='utf-8'))
        final_ids=set(manifest['final_evaluation_query_ids'])
        development_ids=set(manifest['development_query_ids'])
        reserve_ids=set(manifest['held_out_reserve_query_ids'])
        if final_ids & development_ids or final_ids & reserve_ids or development_ids & reserve_ids:
            errors.append('A question appears in multiple benchmark groups')
        if final_ids | development_ids | reserve_ids != query_ids:errors.append('Split manifest does not cover every question exactly once')
        selected=[t for t in q['queries'] if t['id'] in final_ids]
        if len(selected)<20:errors.append('Need at least 20 selected final evaluation questions')
        held_scopes=set();dev_scopes=set()
        for item in q['queries']:
            expected_role='final_evaluation' if item['id'] in final_ids else ('development' if item['id'] in development_ids else 'reserve')
            expected_split='development' if expected_role=='development' else 'held_out'
            if item.get('benchmark_role')!=expected_role or item.get('split')!=expected_split:
                errors.append('QA assignment does not match split manifest')
            (dev_scopes if expected_split=='development' else held_scopes).update(query_scopes.get(item['id'],set()))
        if held_scopes & dev_scopes:errors.append('Final evidence scope leaked into development')
        if set(manifest['held_out_evidence_scopes'])!=held_scopes or set(manifest['development_evidence_scopes'])!=dev_scopes:
            errors.append('Split manifest scopes do not match query evidence')
    else:errors.append('Missing recorded development/held-out split manifest')
    categories=Counter(t.get('category') for t in selected if t.get('verified') is True)
    for category,minimum in {'actor_software_technique':8,'technique_mitigation':8,'cross_report_comparison':4}.items():
        if categories[category]<minimum:errors.append(f'Need {minimum}+ reviewed final {category} questions')
    return errors

if __name__=='__main__':
    from collections import Counter
    errors=check(Path(__file__).resolve().parents[1]/'benchmarks')
    for error,count in Counter(errors).items(): print(f'{error} ({count})')
    if not errors:print('Benchmark structure passed: complete gold scope, reviewed QA paths/references, final category mix, and disjoint evidence scopes. Reviewer provenance remains explicit; no performance test was run.')
    raise SystemExit(1 if errors else 0)
