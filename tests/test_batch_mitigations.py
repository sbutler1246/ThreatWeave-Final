"""Frozen-source verification for direct technique-to-mitigation reference import."""
import copy
import json
import unittest
from pathlib import Path

from import_batch_mitigations import prepare
from import_pilot_mitigations import prepare as prepare_technique,reference_records
from schemas import Assertion,Chunk,Document
from extraction.parser import validate_chunk_document

REPO = Path(__file__).resolve().parents[1]


class BatchMitigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = prepare(REPO)
        cls.objects = json.loads((REPO/'data/enterprise-attack-17.1.json').read_bytes())['objects']

    def test_direct_association_counts_and_shared_identity(self):
        self.assertEqual([len(p['records']) for p in self.payload['parts']],[5,5])
        records = [r for p in self.payload['parts'] for r in p['records']]
        self.assertEqual(len({r['entity']['canonical_id'] for r in records}),9)
        self.assertEqual(len({r['assertion']['assertion_id'] for r in records}),10)
        self.assertEqual(self.payload['expected_path_count'],15)

    def test_reference_origin_direction_and_exact_source_spans(self):
        by_id = {o['id']:o for o in self.objects}
        for p in self.payload['parts']:
            for r in p['records']:
                a = Assertion.model_validate({k:v for k,v in r['assertion'].items() if k in Assertion.model_fields})
                doc = Document.model_validate({k:v for k,v in r['document'].items() if k in Document.model_fields})
                chunk = Chunk.model_validate({k:v for k,v in r['chunk'].items() if k in Chunk.model_fields})
                validate_chunk_document(chunk,doc)
                original = by_id[r['assertion']['source_stix_relationship_id']]
                self.assertEqual(original['relationship_type'],'mitigates')
                self.assertEqual(original['source_ref'],r['entity']['stix_id'])
                self.assertEqual(original['target_ref'],p['technique']['stix_id'])
                self.assertEqual(a.head_id,p['technique']['canonical_id'])
                self.assertEqual(a.tail_id,r['entity']['canonical_id'])
                self.assertEqual(a.origin,'fused')
                self.assertEqual(a.evidence_text,original['description'])
                self.assertEqual(doc.text[chunk.start:chunk.end],a.evidence_text)

    def test_subtechnique_does_not_inherit_parent_associations(self):
        technique,links = reference_records(self.objects,'T1562.001')
        self.assertEqual(len(links),5)
        self.assertTrue(all(rel['target_ref']==technique['id'] for _,rel in links))
        parent,_ = reference_records(self.objects,'T1562')
        self.assertNotEqual(technique['id'],parent['id'])

    def test_revoked_reference_is_excluded(self):
        _,links = reference_records(self.objects,'T1219')
        changed = copy.deepcopy(self.objects)
        next(o for o in changed if o['id']==links[0][1]['id'])['revoked']=True
        self.assertEqual(len(reference_records(changed,'T1219')[1]),4)

    def test_legacy_defaults_and_ids_remain_stable(self):
        old = prepare_technique(REPO)
        explicit = prepare_technique(REPO,'T1046')
        self.assertEqual(old['technique']['canonical_id'],'attack:T1046')
        self.assertEqual(len(old['records']),3)
        self.assertEqual(old['records'],explicit['records'])
        repeated = prepare(REPO)
        self.assertEqual([p['records'] for p in self.payload['parts']],
                         [p['records'] for p in repeated['parts']])


if __name__=='__main__':
    unittest.main()
