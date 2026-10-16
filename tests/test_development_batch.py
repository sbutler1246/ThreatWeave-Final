"""Regression checks on source boundaries and extraction/resolution failure cases."""
import json
import unittest
from pathlib import Path

from extraction.development_batch import make_prompt,read_inputs,validate_candidate,select_retry_items

REPO = Path(__file__).resolve().parents[1]


class SelectionInput:
    """Supply a selection fixture without creating operating-system temp files."""
    def __init__(self,value):
        self.value = value

    def read_text(self,encoding='utf-8'):
        return json.dumps(self.value)


class DevelopmentBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items,cls.config,cls.catalog,cls.attack_hash = read_inputs(REPO)

    def table_output(self,item_index=0):
        item = self.items[item_index]
        chunk = item['chunk']
        lines = chunk.text.splitlines()
        actor = chunk.inherited_context[0].text.partition('Tools Used by ')[2]
        return {'entities':[
            {'local_id':'actor','type':'ThreatGroup','name':actor,'attack_id':None},
            {'local_id':'tool','type':'Software','name':lines[0],'attack_id':None},
            {'local_id':'behavior','type':'Technique','name':lines[-1],'attack_id':lines[-2]}],
            'relations':[{'head':'actor','predicate':'USES','tail':'tool',
                          'evidence':{'start':0,'end':len(chunk.text),'quote':chunk.text},'confidence':None},
                         {'head':'tool','predicate':'USES_TECHNIQUE','tail':'behavior',
                          'evidence':{'start':0,'end':len(chunk.text),'quote':chunk.text},'confidence':None}]}

    def test_source_selection_and_spans(self):
        self.assertEqual(len(self.items),5)
        self.assertEqual(len({i['document'].doc_id for i in self.items}),3)
        self.assertEqual([i['spec']['kind'] for i in self.items],['table']*3+['prose']*2)
        for item in self.items:
            chunk,document = item['chunk'],item['document']
            self.assertEqual(document.text[chunk.start:chunk.end],chunk.text)
            for context in chunk.inherited_context:
                self.assertEqual(document.text[context.start:context.end],context.text)

    def test_held_out_scope_is_blocked(self):
        selection = json.loads((REPO/'extraction/development_batch_sources.json').read_text(encoding='utf-8'))
        selection['sources'][0]['scope_id']='AA23-165A:table4:row01'
        with self.assertRaisesRegex(ValueError,'held-out'):
            read_inputs(REPO,SelectionInput(selection))

    def test_additional_report_with_held_out_scopes_is_blocked(self):
        selection = json.loads((REPO/'extraction/development_batch_sources.json').read_text(encoding='utf-8'))
        selection['sources'][-1].update(doc_id='AA24-109A',scope_id='AA24-109A:development:paragraph:1')
        with self.assertRaisesRegex(ValueError,'contains held-out'):
            read_inputs(REPO,SelectionInput(selection))

    def test_historical_label_resolves_using_explicit_id(self):
        batch,resolution = validate_candidate(json.dumps(self.table_output()),self.items[0],self.catalog)
        row = next(r for r in resolution if r['local_id']=='behavior')
        self.assertEqual(batch.entities[-1].name,'Remote Access Software')
        self.assertEqual(row['canonical_id'],'attack:T1219')
        self.assertEqual(row['canonical_name'],'Remote Access Tools')
        self.assertEqual(row['status'],'resolved')

    def test_subtechnique_source_label_is_preserved(self):
        batch,resolution = validate_candidate(json.dumps(self.table_output(2)),self.items[2],self.catalog)
        self.assertEqual(batch.entities[-1].name,'Impair Defenses: Disable or Modify Tools')
        self.assertEqual(resolution[-1]['canonical_id'],'attack:T1562.001')

    def test_source_quote_tampering_is_rejected(self):
        value = self.table_output()
        value['relations'][0]['evidence']['quote']='x'*len(self.items[0]['chunk'].text)
        with self.assertRaisesRegex(ValueError,'quote does not match'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)

    def test_model_cannot_assign_behavior_id_to_software(self):
        value = self.table_output()
        value['entities'][1]['attack_id']='T1219'
        with self.assertRaisesRegex(ValueError,'incompatible'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)

    def test_model_cannot_invent_id_or_remove_affiliates(self):
        value = self.table_output()
        value['entities'][1]['attack_id']='S0358'
        with self.assertRaisesRegex(ValueError,'absent'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)
        value = self.table_output()
        value['entities'][0]['name']='LockBit'
        with self.assertRaisesRegex(ValueError,'Affiliates'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)

    def test_prose_affiliate_suffix_cannot_be_removed_from_supporting_actor(self):
        from schemas import Chunk, Document
        for full_name in ['Group Alpha affiliates', 'Group Alpha ransomware affiliates']:
            text = full_name+' used Tool Beta.'
            item = {'spec': {'kind': 'prose'},
                    'chunk': Chunk(chunk_id='sample:test', doc_id='sample', start=0, end=len(text), text=text),
                    'document': Document(doc_id='sample', title='Sample', text=text,
                        source_url='https://example.org/source', content_hash='a'*64)}
            value = {'entities': [
                {'local_id':'e1','type':'ThreatGroup','name':'Group Alpha','attack_id':None},
                {'local_id':'e2','type':'Software','name':'Tool Beta','attack_id':None}],
                'relations':[{'head':'e1','predicate':'USES','tail':'e2','confidence':None,
                    'evidence':{'start':0,'end':len(text),'quote':text}}]}
            with self.subTest(full_name=full_name), self.assertRaisesRegex(ValueError, 'affiliates qualifier'):
                validate_candidate(json.dumps(value), item, [])

    def test_prompts_do_not_import_reference_labels(self):
        for item in self.items:
            system,prompt,schema = make_prompt(REPO,item)
            self.assertIn(item['chunk'].text,prompt)
            self.assertEqual(schema['$defs']['EvidenceSpan']['properties']['quote']['const'],item['chunk'].text)
            self.assertNotIn('expected_facts',system+prompt)
            self.assertNotIn('gold_triples',system+prompt)
            self.assertNotIn('reference_answer',system+prompt)

    def slot_output(self,item_index=0):
        batch = self.table_output(item_index)
        slots = {'actor':'e1','tool':'e2','behavior':'e3'}
        for entity in batch['entities']:
            entity['local_id']=slots[entity['local_id']]
        for relation in batch['relations']:
            relation['head']=slots[relation['head']]
            relation['tail']=slots[relation['tail']]
        return dict(zip(['actor','software','technique'],batch['entities']),relations=batch['relations'])

    def test_table_slots_keep_ids_on_the_correct_entities(self):
        value = self.slot_output()
        batch,resolution = validate_candidate(json.dumps(value),self.items[0],self.catalog)
        self.assertEqual(len(batch.relations),2)
        self.assertEqual(resolution[-1]['canonical_id'],'attack:T1219')
        value['software']['attack_id']='T1219'
        with self.assertRaisesRegex(ValueError,'slot differs'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)

    def test_table_slots_do_not_force_relationships(self):
        value = self.slot_output()
        value['relations']=[]
        batch,_ = validate_candidate(json.dumps(value),self.items[0],self.catalog)
        self.assertEqual(batch.relations,[])

    def test_observed_invalid_predicates_and_endpoints_are_rejected(self):
        for change in ['predicate','endpoint','duplicate']:
            value = self.slot_output()
            if change=='predicate': value['relations'][0]['predicate']='ASSOCIATED_WITH'
            if change=='endpoint': value['relations'][1]['tail']='T1219'
            if change=='duplicate': value['relations'].append(value['relations'][0])
            with self.assertRaisesRegex(ValueError,'Invalid or duplicate'):
                validate_candidate(json.dumps(value),self.items[0],self.catalog)

    def test_table_slots_reject_missing_or_wrong_source_roles(self):
        value = self.slot_output()
        value.pop('actor')
        with self.assertRaisesRegex(ValueError,'exactly'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)
        value = self.slot_output()
        value['technique']['name']='T1219'
        with self.assertRaisesRegex(ValueError,'slot differs'):
            validate_candidate(json.dumps(value),self.items[0],self.catalog)

    def test_table_schema_exposes_only_source_roles_and_valid_links(self):
        _,_,schema = make_prompt(REPO,self.items[0])
        self.assertEqual(set(schema['properties']),{'actor','software','technique','relations'})
        self.assertEqual(schema['properties']['software']['properties']['attack_id']['const'],None)
        self.assertEqual(schema['properties']['technique']['properties']['attack_id']['const'],'T1219')
        options = schema['properties']['relations']['items']['anyOf']
        self.assertEqual({r['properties']['predicate']['const'] for r in options},{'USES','USES_TECHNIQUE'})
        self.assertNotIn('minItems',schema['properties']['relations'])

    def test_retry_rejects_a_run_outside_the_repository(self):
        with self.assertRaisesRegex(ValueError,'inside this repository'):
            select_retry_items(REPO,self.items,REPO.parent/'unrelated_run',self.config,self.attack_hash)


if __name__=='__main__':
    unittest.main()
