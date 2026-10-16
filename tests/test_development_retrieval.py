"""Source integrity, relevant paths, scope separation and evidence packing."""
import copy
import hashlib
import json
import unittest
from pathlib import Path

from graph.development_retrieval import DevelopmentGraphRetriever,matches_groups,seed_groups
from graph_pilot_qa import checked_answer
from graph_qa import BASELINE_DEMO_QUESTIONS as DEMO_QUESTIONS

REPO = Path(__file__).resolve().parents[1]


class DevelopmentRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.retriever = DevelopmentGraphRetriever(REPO,include_corpus_pilot=False)
        cls.paths,cls.records,cls.mentions = [],[],[]
        for scope,profile in cls.retriever.profiles.items():
            doc,chunk = profile['document'],profile['chunk']
            d = doc.model_dump(mode='json')
            c = chunk.model_dump(mode='json')
            c['inherited_context_json']=json.dumps(c.pop('inherited_context'))
            edges = []
            for head,predicate,tail in profile['allowed_triples']:
                key = hashlib.sha256('\x1f'.join([head,predicate,tail]).encode()).hexdigest()
                aid = 'fixture:'+scope+':'+predicate
                a = {'assertion_id':aid,'head_id':head,'predicate':predicate,'tail_id':tail,
                     'source_doc_id':doc.doc_id,'chunk_id':scope,'evidence_text':chunk.text,
                     'evidence_start':chunk.start,'evidence_end':chunk.end,
                     'source_hash':doc.content_hash,'triple_key':key,
                     'origin':'extracted','validation_status':'validated'}
                cls.records.append({'assertion':a,'document':d,'chunk':c})
                edges.append((head,predicate,tail,aid))
            for head,predicate,tail,aid in edges:
                if predicate!='USES':
                    continue
                one = {'nodes':[cls.retriever.expected_entities[head],cls.retriever.expected_entities[tail]],
                       'edges':[{'predicate':predicate,'assertion_ids':[aid]}]}
                cls.paths.append(one)
                for h,p,t,a in edges:
                    if h!=tail or p!='USES_TECHNIQUE':
                        continue
                    two = {'nodes':one['nodes']+[cls.retriever.expected_entities[t]],
                           'edges':one['edges']+[{'predicate':p,'assertion_ids':[a]}]}
                    cls.paths.append(two)
                    for ref in cls.retriever.references.values():
                        if ref['assertion']['head_id']==t:
                            cls.records.append({'assertion':ref['assertion'],'document':ref['document'],'chunk':ref['chunk']})
                            cls.paths.append({'nodes':two['nodes']+[ref['entity']],
                                              'edges':two['edges']+[{'predicate':'MITIGATED_BY','assertion_ids':[ref['assertion']['assertion_id']]}]})

    def bundle(self,question,paths=None,records=None):
        groups = seed_groups(question,list(self.retriever.expected_entities.values()))
        return self.retriever.assemble(self.paths if paths is None else paths,
                                       self.records if records is None else records,groups)

    def test_named_actor_and_software_constrain_paths(self):
        bundle = self.bundle(DEMO_QUESTIONS[0])
        self.assertEqual(len(bundle.paths),5)
        self.assertTrue(all(len(p.edges)==3 for p in bundle.paths))
        self.assertEqual(len(bundle.passages),13)
        anydesk = next(k for k,v in self.retriever.expected_entities.items() if v['name']=='AnyDesk')
        self.assertTrue(all(p.edges[0].tail_id==anydesk for p in bundle.paths))
        self.assertLessEqual(self.retriever.last_stats['evidence_utf8_bytes'],self.retriever.byte_cap)

    def test_prose_questions_use_only_the_supported_one_hop_path(self):
        for question in DEMO_QUESTIONS[1:]:
            with self.subTest(question=question):
                bundle = self.bundle(question)
                self.assertEqual(len(bundle.paths),1)
                self.assertEqual(len(bundle.paths[0].edges),1)
                self.assertEqual(len(bundle.passages),1)
                self.assertEqual(bundle.passages[0].source_kind,'cisa')

    def test_unknown_named_entity_produces_no_evidence(self):
        bundle = self.bundle('What does Unknown Actor Omega use?')
        self.assertEqual(bundle.paths,[])
        self.assertEqual(bundle.passages,[])

    def test_assertion_quote_tampering_is_rejected(self):
        records = copy.deepcopy(self.records)
        r = next(r for r in records if r['assertion']['chunk_id']=='AA23-165A:table4:row03' and r['assertion']['predicate']=='USES')
        r['assertion']['evidence_text']='Unverified text.'
        with self.assertRaisesRegex(ValueError,'quote does not match'):
            self.bundle(DEMO_QUESTIONS[0],records=records)

    def test_reference_version_tampering_is_rejected(self):
        records = copy.deepcopy(self.records)
        for r in records:
            if r['assertion']['head_id']=='attack:T1219' and r['assertion']['origin']=='fused':
                r['assertion']['attack_release']='18.0'
        with self.assertRaisesRegex(ValueError,'frozen structured reference'):
            self.bundle(DEMO_QUESTIONS[0],records=records)

    def test_rejected_source_assertion_does_not_enter_the_answer(self):
        records = copy.deepcopy(self.records)
        for r in records:
            if r['assertion']['chunk_id']=='AA23-165A:table4:row03' and r['assertion']['predicate']=='USES':
                r['assertion']['validation_status']='rejected'
        self.assertEqual(self.bundle(DEMO_QUESTIONS[0],records=records).paths,[])

    def test_source_scope_cannot_be_reassigned_to_another_row(self):
        records = copy.deepcopy(self.records)
        wrong = next(r for r in records if r['assertion']['chunk_id']=='AA23-165A:table4:row03' and r['assertion']['predicate']=='USES_TECHNIQUE')
        wrong['assertion']['chunk_id']='AA23-165A:table4:row04'
        with self.assertRaisesRegex(ValueError,'not supported by this development source scope'):
            self.bundle(DEMO_QUESTIONS[0],records=records)

    def test_budget_reduces_context_without_unknown_citations(self):
        old = self.retriever.byte_cap
        try:
            self.retriever.byte_cap=1500
            bundle = self.bundle(DEMO_QUESTIONS[0])
            self.assertGreater(len(bundle.paths),0)
            self.assertLess(len(bundle.paths),5)
            self.assertLessEqual(len(self.retriever.last_context.encode('utf-8')),1500)
            known = set(bundle.citation_ids)
            self.assertTrue(all(set(e.citation_ids)<=known for p in bundle.paths for e in p.edges))
        finally:
            self.retriever.byte_cap=old

    def test_comparison_retrieves_both_named_tools(self):
        bundle = self.bundle('Compare AnyDesk and Atera Remote Monitoring & Management (RMM).')
        software = {self.retriever.expected_entities[p.edges[0].tail_id]['name'] for p in bundle.paths}
        self.assertEqual(software,{'AnyDesk','Atera Remote Monitoring & Management (RMM)'})

    def test_all_passages_are_exact_parent_document_spans(self):
        bundle = self.bundle(DEMO_QUESTIONS[0])
        documents = {p['document'].doc_id:p['document'].text for p in self.retriever.profiles.values()}
        documents.update({r['document']['doc_id']:r['document']['text'] for r in self.retriever.references.values()})
        for passage in bundle.passages:
            self.assertEqual(documents[passage.doc_id][passage.start:passage.end],passage.text)

    def test_unknown_answer_citation_is_rejected(self):
        bundle = self.bundle(DEMO_QUESTIONS[0])
        raw = json.dumps({'answer':'Unverified claim.','claims':[{'text':'Unverified claim.','citations':['E999']}], 'abstained':False})
        with self.assertRaisesRegex(ValueError,'unknown answer citation'):
            checked_answer(raw,bundle,0)
