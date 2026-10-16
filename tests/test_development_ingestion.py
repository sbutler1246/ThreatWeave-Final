"""Review gates, identity separation and stable provenance records for batch import."""
import copy
import json
import unittest
from pathlib import Path

from extraction.development_batch import read_inputs,validate_candidate
from graph.development_ingestion import check_source_support,local_identity,prepare_item,preserve_review
from schemas import EntityCandidate,ExtractionBatch

REPO = Path(__file__).resolve().parents[1]


class DevelopmentIngestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items,cls.config,cls.catalog,cls.attack_hash = read_inputs(REPO)

    def table_batch(self):
        item = self.items[0]
        text = item['chunk'].text
        actor = item['chunk'].inherited_context[0].text.partition('Tools Used by ')[2]
        source = {'actor':{'local_id':'e1','type':'ThreatGroup','name':actor,'attack_id':None},
                  'software':{'local_id':'e2','type':'Software','name':'AnyDesk','attack_id':None},
                  'technique':{'local_id':'e3','type':'Technique','name':'Remote Access Software','attack_id':'T1219'},
                  'relations':[
                      {'head':'e1','predicate':'USES','tail':'e2','evidence':{'start':0,'end':len(text),'quote':text}},
                      {'head':'e2','predicate':'USES_TECHNIQUE','tail':'e3','evidence':{'start':0,'end':len(text),'quote':text}}]}
        raw = json.dumps(source)
        batch,_ = validate_candidate(raw,item,self.catalog)
        return item,batch,raw

    def prepared_table(self):
        item,batch,raw = self.table_batch()
        return prepare_item(item,batch,self.catalog,
                            {'model':'fixture','model_digest':'fixture-digest','options':{}},
                            {'prompt_hash':'fixture-prompt'},raw,Path('fixture-run'))

    def test_assertion_ids_are_stable_on_repeated_preparation(self):
        first,second = self.prepared_table(),self.prepared_table()
        self.assertEqual(first,second)
        self.assertEqual(len({a['assertion_id'] for a in first['assertions']}),2)

    def test_prior_pilot_actor_identity_is_reused(self):
        entity = EntityCandidate(local_id='x',type='ThreatGroup',name='LockBit Affiliates')
        self.assertEqual(local_identity('AA23-165A',entity),'local:AA23-165A:lockbit-affiliates')
        self.assertNotEqual(local_identity('AA23-165A',entity),local_identity('AA23-353A',entity))

    def test_source_and_canonical_names_remain_distinct(self):
        item = self.prepared_table()
        technique = next(e for e in item['entities'] if e['type']=='Technique')
        self.assertEqual(technique['name'],'Remote Access Tools')
        self.assertEqual(technique['canonical_id'],'attack:T1219')
        mention = next(m for m in item['mentions'] if m['canonical_id']=='attack:T1219')
        self.assertEqual(mention['evidence_text'],'Remote Access Software')
        self.assertEqual(item['document']['text'][mention['evidence_start']:mention['evidence_end']],mention['evidence_text'])

    def test_assertions_have_extracted_origin_and_real_source_spans(self):
        item = self.prepared_table()
        for a in item['assertions']:
            self.assertEqual(a['origin'],'extracted')
            self.assertEqual(a['validation_status'],'validated')
            self.assertEqual(a['human_review_status'],'pending')
            self.assertEqual(item['document']['text'][a['evidence_start']:a['evidence_end']],a['evidence_text'])
        actor = next(m for m in item['mentions'] if 'lockbit-affiliates' in m['canonical_id'])
        self.assertLess(actor['evidence_start'],item['chunk']['start'])

    def test_human_verified_status_is_not_downgraded(self):
        a = self.prepared_table()['assertions'][0]
        prior = dict(a,validation_status='human_verified',human_review_status='approved')
        preserved = preserve_review(prior,a)
        self.assertEqual(preserved['validation_status'],'human_verified')
        self.assertEqual(preserved['human_review_status'],'approved')

    def test_rejected_and_conflicting_assertions_are_not_overwritten(self):
        a = self.prepared_table()['assertions'][0]
        with self.assertRaisesRegex(ValueError,'rejected'):
            preserve_review(dict(a,validation_status='rejected'),a)
        with self.assertRaisesRegex(ValueError,'conflicts'):
            preserve_review(dict(a,source_hash='changed'),a)

    def test_unreviewed_additional_table_relation_is_blocked(self):
        item,batch,_ = self.table_batch()
        batch.relations[1].head='e1'
        with self.assertRaisesRegex(ValueError,'reviewed table roles'):
            check_source_support(item,batch)

    def test_negated_prose_clause_is_not_imported(self):
        item = copy.deepcopy(self.items[3])
        text = item['chunk'].text
        batch = ExtractionBatch.model_validate({'entities':[
            {'local_id':'g','type':'ThreatGroup','name':'BianLian group actors'},
            {'local_id':'s','type':'Software','name':'Rclone'}],
            'relations':[{'head':'g','predicate':'USES','tail':'s',
                          'evidence':{'start':0,'end':len(text),'quote':text}}]})
        self.assertIn('explicit_use_clause',check_source_support(item,batch))
        item['chunk'].text=text.replace(' used Rclone ',' did not use Rclone ')
        with self.assertRaisesRegex(ValueError,'does not explicitly assert'):
            check_source_support(item,batch)


if __name__=='__main__':
    unittest.main()
