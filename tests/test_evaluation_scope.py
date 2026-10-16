"""Shared final evidence parity, frozen methods and isolated text-index preparation."""
import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from evaluation import corpus_scope, text_sources
from graph.development_projection import freeze_projection, preview_projection, expected_triples
from graph.development_retrieval import DevelopmentGraphRetriever
from retrieval.development_text import load_tokenizer, split_parent
from retrieval.hybrid_retrieval import saved_projection_rows

REPO = Path(__file__).resolve().parents[1]


class EvaluationScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pointer = (REPO/'work/graph_index/current.json').read_bytes()
        original = Path.read_text
        def guarded(path,*args,**kwargs):
            if path.name in {'gold_triples.json','eval_queries.json','reference_triples.json'}:
                raise AssertionError('Labels must not enter scope or index preparation.')
            return original(path,*args,**kwargs)
        with patch.object(Path,'read_text',guarded),patch('requests.Session',side_effect=AssertionError('Services forbidden')):
            cls.graph = corpus_scope.EvaluationGraphRetriever(REPO)
            cls.selected,cls.config = text_sources.parents(REPO,scope=(cls.graph.profiles,cls.graph.references,
                                                         cls.graph.expected_entities,cls.graph.config))
            cls.tokenizer = load_tokenizer(REPO,cls.config)
            cls.records,_,cls.text_hash = text_sources.prepare_records(REPO,cls.tokenizer,selected=cls.selected,config=cls.config)
            cls.projection,cls.projection_hash,cls.edges,cls.rows = preview_projection(cls.graph)
        print('\nEvaluation fixture:',len(cls.projection['nodes']),'nodes;',len(cls.projection['edges']),'facts;',
              len(cls.records),'text chunks;',cls.config['evaluation_scope']['sha256'],flush=True)

    def test_shared_sources_are_receipt_bound_and_contain_all_seven_reports(self):
        g = self.graph
        self.assertEqual((len(g.profiles),len(g.references)),(101,190))
        self.assertEqual(len({p['document'].doc_id for p in g.profiles.values()}),15)
        pinned = [a for p in g.profiles.values() for a in p.get('accepted_assertions',{}).values()]
        held = [a for a in pinned if a.get('scope_assignment')=='evaluation']
        self.assertEqual(len(pinned),232)
        self.assertEqual(len(held),118)
        self.assertEqual(len({a['chunk_id'] for a in held}),48)
        self.assertTrue(all(':evaluation:' in a['chunk_id'] for a in held))
        self.assertEqual(g.config['development_scope']['cisa_scope_count'],53)
        self.assertEqual(g.config['evaluation_scope']['cisa_scope_count'],101)
        self.assertEqual((REPO/'work/graph_index/current.json').read_bytes(),self.pointer)

    def test_text_and_graph_have_identical_source_parent_and_reference_access(self):
        expected = set(self.graph.profiles)|{r['chunk']['chunk_id'] for r in self.graph.references.values()}
        self.assertEqual(len(self.selected),291)
        self.assertEqual({c.chunk_id for _,c,_ in self.selected},expected)
        self.assertEqual({r['chunk']['parent_extraction_chunk_id'] for r in self.records},expected)
        self.assertEqual(len(self.records),510)
        self.assertEqual(self.config['evaluation_scope'],self.graph.config['evaluation_scope'])
        self.assertTrue(all(n['type'] not in {'Document','Chunk','Assertion'} for n in self.projection['nodes']))

    def test_frozen_splitter_and_all_exact_spans_and_input_bounds_are_preserved(self):
        docs = {d.doc_id:d for d,_,_ in self.selected}
        for r in self.records:
            c = r['chunk'];d = docs[c['doc_id']]
            self.assertEqual(d.text[c['start']:c['end']],c['text'])
            self.assertLessEqual(r['wordpiece_count'],240)
            self.assertLessEqual(len(r['embedding_text']),1000)
            for context in c['inherited_context']:
                self.assertEqual(d.text[context['start']:context['end']],context['text'])
        doc,parent,_ = self.selected[0]
        expected = split_parent(doc,parent,self.tokenizer,self.config['chunking'])
        actual = [r for r in self.records if r['chunk']['parent_extraction_chunk_id']==parent.chunk_id]
        self.assertEqual([r['chunk'] for r in actual],[r['chunk'] for r in expected])

    def test_methods_and_all_generation_retrieval_embedding_settings_are_unchanged(self):
        for name in ['retrieve','_verify_record','_candidate']:
            self.assertIs(getattr(corpus_scope.EvaluationGraphRetriever,name),getattr(DevelopmentGraphRetriever,name))
        config = json.loads((REPO/'config.json').read_text(encoding='utf-8'))
        for key in ['retrieval','llm','chunking','text_embedding','node2vec']:
            self.assertEqual(self.config[key],config[key])
        self.assertNotEqual(self.config['development_scope']['sha256'],self.config['evaluation_scope']['sha256'])

    def test_projection_roundtrip_retains_every_reviewed_assertion_and_fails_on_missing_fact(self):
        rows = saved_projection_rows(SimpleNamespace(projection=self.projection),self.graph)
        projection,fingerprint = freeze_projection(self.graph,self.edges,rows)
        self.assertEqual(projection,self.projection)
        self.assertEqual(fingerprint,self.projection_hash)
        source_records = [s['source_record'] for e in projection['edges'] for s in e['support'] if 'source_record' in s]
        self.assertEqual(len(source_records),232)
        self.assertEqual(sum(a['scope_assignment']=='evaluation' for a in source_records),118)
        with self.assertRaisesRegex(ValueError,'absent'):
            freeze_projection(self.graph,self.edges[1:],rows)

    def test_changed_evaluation_provenance_is_rejected_by_frozen_verifier(self):
        row = next(r for r in self.rows if r['assertion'].get('scope_assignment')=='evaluation')
        for key in ['scope_assignment','evaluation_plan_fingerprint','source_generation_raw_file_sha256','source_review_sha256']:
            changed = copy.deepcopy(row);changed['assertion'][key]='changed'
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'pinned supported source review'):
                self.graph._verify_record(changed,row['assertion']['head_id'],row['assertion']['predicate'],row['assertion']['tail_id'])

    def test_mitigation_receipt_or_saved_identity_changes_block_expansion(self):
        folder = REPO/'work/evaluation_corpus_mitigations'/corpus_scope.MITIGATION_RUN
        payload = json.loads((folder/'prepared_records.json').read_text(encoding='utf-8'))
        original = Path.read_text
        for name in ['import_receipt.json','prepared_records.json']:
            def changed(path,*args,**kwargs):
                text = original(path,*args,**kwargs)
                if path==folder/name:
                    data = json.loads(text)
                    if name=='import_receipt.json':data['source_reference_combination_count']=202
                    else:data['evaluation_plan_fingerprint']='changed'
                    return json.dumps(data)
                return text
            with self.subTest(name=name),patch.object(Path,'read_text',changed),patch.object(
                    corpus_scope,'development_profiles',return_value=({},{},{},self.config)),patch.object(
                    corpus_scope,'prepare_evaluation_references',return_value=payload):
                with self.assertRaises(ValueError):corpus_scope.source_profiles(REPO)

    def test_text_index_preview_uses_isolated_scope_and_never_loads_embedding_model(self):
        import index_evaluation_text
        with patch('sys.argv',['index_evaluation_text.py','--preview']),patch.object(
                index_evaluation_text,'parents',return_value=(self.selected,self.config)),patch.object(
                index_evaluation_text,'load_tokenizer',return_value=self.tokenizer),patch.object(
                index_evaluation_text,'prepare_records',return_value=(self.records,self.config,self.text_hash)),patch.object(
                index_evaluation_text,'load_model',side_effect=AssertionError('Preview cannot embed')),patch.dict(
                'sys.modules',{'chromadb':None}),redirect_stdout(io.StringIO()):
            self.assertEqual(index_evaluation_text.main(),0)
        self.assertEqual((REPO/'work/graph_index/current.json').read_bytes(),self.pointer)


if __name__ == '__main__':
    unittest.main()
