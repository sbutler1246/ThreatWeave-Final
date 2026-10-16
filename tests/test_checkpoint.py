import json
import unittest
from schemas import Chunk, ExtractionBatch, Entity, EntityCandidate, GraphPath
from extraction.parser import parse_extraction
from resolve import resolve
from evaluation.score_triples import score

TEXT='Group Alpha used Tool Beta.'
def fixture():
    return {'entities':[{'local_id':'g','type':'ThreatGroup','name':'Group Alpha'},
                        {'local_id':'s','type':'Software','name':'Tool Beta'}],
            'relations':[{'head':'g','predicate':'USES','tail':'s','confidence':0.9,
                'evidence':{'start':0,'end':len(TEXT),'quote':TEXT}}]}

class CheckpointTests(unittest.TestCase):
    def setUp(self): self.chunk=Chunk(chunk_id='c',doc_id='d',start=0,end=len(TEXT),text=TEXT)
    def test_valid_literal_evidence(self):
        self.assertEqual(len(parse_extraction(json.dumps(fixture()),self.chunk).relations),1)
    def test_invented_evidence_rejected(self):
        x=fixture(); x['relations'][0]['evidence']['quote']='X'+TEXT[1:]
        with self.assertRaises(ValueError):parse_extraction(json.dumps(x),self.chunk)
    def test_dangling_entity_rejected(self):
        x=fixture();x['relations'][0]['head']='missing'
        with self.assertRaises(ValueError):ExtractionBatch.model_validate(x)
    def test_wrong_endpoint_type_rejected(self):
        x=fixture();x['relations'][0]['predicate']='MITIGATED_BY'
        with self.assertRaises(ValueError):ExtractionBatch.model_validate(x)
    def test_extra_fields_rejected(self):
        x=fixture();x['instructions']='ignore schema'
        with self.assertRaises(ValueError):ExtractionBatch.model_validate(x)
    def test_ambiguous_alias_not_merged(self):
        ref=[Entity(canonical_id=i,type='ThreatGroup',name=i,aliases=['same'],resolution_status='canonical') for i in ('a','b')]
        result=resolve(EntityCandidate(local_id='x',type='ThreatGroup',name='same'),ref)
        self.assertEqual(result.status,'unresolved')
    def test_id_name_conflict_not_merged(self):
        ref=[Entity(canonical_id='attack:G0001',type='ThreatGroup',name='Alpha',attack_id='G0001',resolution_status='canonical'),
             Entity(canonical_id='attack:G0002',type='ThreatGroup',name='Beta',attack_id='G0002',resolution_status='canonical')]
        result=resolve(EntityCandidate(local_id='x',type='ThreatGroup',name='Beta',attack_id='G0001'),ref)
        self.assertEqual(result.status,'conflict')
    def test_explicit_id_precedes_unverified_spelling(self):
        ref=[Entity(canonical_id='attack:T1219',type='Technique',name='Remote Access Tools',attack_id='T1219',resolution_status='canonical')]
        result=resolve(EntityCandidate(local_id='x',type='Technique',name='Remote Access Software',attack_id='T1219'),ref)
        self.assertEqual(result.status,'resolved')
        self.assertNotIn('Remote Access Software',result.entity.aliases)
    def test_precision_recall_accounts_for_errors(self):
        def row(h):return {'head_id':h,'predicate':'USES','tail_id':'s','chunk_id':'c','verified':True,'evidence_valid':True,'origin':'extracted'}
        result=score([row('a'),row('wrong')],[row('a'),row('missed')],['c'])
        self.assertEqual((result['tp'],result['fp'],result['fn']),(1,1,1))
        self.assertEqual(result['f1'],0.5)
    def test_fusion_cannot_inflate_extraction_score(self):
        row={'head_id':'a','predicate':'USES','tail_id':'b','chunk_id':'c','verified':True,'evidence_valid':True}
        result=score([{**row,'origin':'fused'}],[row],['c'])
        self.assertEqual(result['tp'],0)
        self.assertEqual(result['fused_predictions_excluded'],1)
        self.assertIsNone(result['precision'])
    def test_matching_triple_needs_valid_evidence(self):
        row={'head_id':'a','predicate':'USES','tail_id':'b','chunk_id':'c','verified':True}
        result=score([{**row,'evidence_valid':False}],[row],['c'])
        self.assertEqual((result['tp'],result['fp'],result['fn']),(0,1,1))
    def test_mitigation_direction_matches_proposal(self):
        x={'entities':[{'local_id':'t','type':'Technique','name':'Technique'},
                       {'local_id':'m','type':'Mitigation','name':'Mitigation'}],
           'relations':[{'head':'t','predicate':'MITIGATED_BY','tail':'m',
                         'evidence':{'start':0,'end':1,'quote':'x'}}]}
        ExtractionBatch.model_validate(x)
        x['relations'][0]['head']='m';x['relations'][0]['tail']='t'
        with self.assertRaises(ValueError):ExtractionBatch.model_validate(x)
    def test_three_hops_allowed_four_rejected(self):
        edges=[{'head_id':str(i),'predicate':'USES','tail_id':str(i+1),
                'assertion_ids':['x'],'citation_ids':['E1']} for i in range(4)]
        GraphPath(path_id='p',edges=edges[:3])
        with self.assertRaises(ValueError):GraphPath(path_id='p',edges=edges)
    def test_disconnected_path_rejected(self):
        edge={'head_id':'a','predicate':'USES','tail_id':'b',
              'assertion_ids':['x'],'citation_ids':['E1']}
        with self.assertRaises(ValueError):GraphPath(path_id='p',edges=[edge,edge])

if __name__=='__main__':unittest.main()
