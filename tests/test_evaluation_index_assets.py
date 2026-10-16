"""Saved text checks and simulated graph publication with no fitting or services."""
import copy
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from evaluation import index_assets
import index_evaluation_graph as builder
from graph.development_projection import digest
from graph.node2vec_training import training_environment

REPO = Path(__file__).resolve().parents[1]


class EvaluationTextAssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt,cls.manifest,cls.records,cls.hits = index_assets.checked_text_index(REPO)
        cls.receipt_path = REPO/'work/evaluation_text_index_runs'/index_assets.TEXT_RUN/'index_receipt.json'

    def altered(self,target,change):
        original = Path.read_text
        def read(path,*args,**kwargs):
            text = original(path,*args,**kwargs)
            if path==target:
                value = json.loads(text);change(value);return json.dumps(value)
            return text
        return patch.object(Path,'read_text',read)

    def test_all_records_and_saved_smoke_hits_match_pinned_snapshot(self):
        self.assertEqual(len(self.records),510)
        self.assertEqual(len(self.hits),15)
        self.assertEqual(self.receipt['evaluation_scope']['cisa_scope_count'],101)
        self.assertEqual(self.receipt['evaluation_scope']['attack_reference_count'],190)
        self.assertTrue(self.manifest['collection_name'].startswith('threatweave_text_eval_'))

    def test_failed_receipt_changed_counts_and_foreign_paths_are_rejected(self):
        for key,value in [('status','failed'),('verified_chunk_count',509),('records_path',str(REPO/'outside.json'))]:
            with self.subTest(key=key),self.altered(self.receipt_path,lambda r:r.update({key:value})):
                with self.assertRaises(ValueError):index_assets.checked_text_index(REPO)

    def test_changed_source_records_or_manifest_scope_are_rejected(self):
        for target,change in [(Path(self.receipt['records_path']),lambda r:r[0].update(title='changed')),
                              (Path(self.receipt['records_path']).parent/'manifest.json',lambda r:r.update(evaluation_scope={}))]:
            with self.subTest(target=target),self.altered(target,change):
                with self.assertRaises(ValueError):index_assets.checked_text_index(REPO)

    def test_different_graph_scope_cannot_use_the_text_index(self):
        scope = copy.deepcopy(self.receipt['evaluation_scope']);scope['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'matching shared'):
            index_assets.checked_text_index(REPO,scope)

    def test_changed_smoke_source_and_invalid_distances_are_rejected(self):
        for field in ['record','distance']:
            def changed(r):
                hit = r['smoke_queries'][0]['hits'][0]
                if field=='record':hit['record']['title']='changed'
                else:hit['cosine_distance']=float('nan')
            with self.subTest(field=field),self.altered(self.receipt_path,changed):
                with self.assertRaises(ValueError):index_assets.checked_text_index(REPO)

    def test_runtime_package_change_is_rejected(self):
        with patch.object(index_assets.importlib.metadata,'version',return_value='different'):
            with self.assertRaisesRegex(ValueError,'runtime package changed'):
                index_assets.checked_text_index(REPO)


class Collection:
    def __init__(self,corrupt=False):
        self.metadata = {};self.values = {k:[] for k in ['ids','documents','metadatas','embeddings']};self.corrupt=corrupt
    def get(self,include):
        return self.values
    def upsert(self,**values):
        self.values = values
        if self.corrupt:self.values['embeddings'][0]=[0.0]*128
    def count(self):
        return len(self.values['ids'])
    def query(self,query_embeddings,**kwargs):
        import numpy as np
        n = next(i for i,v in enumerate(self.values['embeddings']) if np.allclose(v,query_embeddings[0]))
        return {'ids':[[self.values['ids'][n]]],'distances':[[0.0]]}


class Driver:
    def __enter__(self):return self
    def __exit__(self,*args):return False
    def verify_connectivity(self):pass


class EvaluationGraphPublicationTests(unittest.TestCase):
    def execute(self,root,*,changed=False,corrupt=False):
        import numpy as np
        root = Path(root)
        (root/'docs').mkdir()
        (root/'graph').mkdir()
        (root/'graph/node2vec_training.py').write_bytes((REPO/'graph/node2vec_training.py').read_bytes())
        (root/'work/graph_index').mkdir(parents=True)
        development = root/'work/graph_index/current.json'
        development.write_text('{"preserved":"development"}',encoding='utf-8')
        config = json.loads((REPO/'config.json').read_text(encoding='utf-8'))
        config.update(development_scope={'name':'development','sha256':'a'*64},
                      evaluation_scope={'name':'evaluation','sha256':'b'*64})
        retriever = SimpleNamespace(config=config,profiles={'source':{}},references={'reference':{}},scope_name='evaluation')
        nodes = [{'canonical_id':'local:a','type':'Software','name':'Tool A'},
                 {'canonical_id':'local:b','type':'Software','name':'Tool B'}]
        projection = {'nodes':nodes,'edges':[{'head_id':'local:a','tail_id':'local:b','predicate':'USES'}]}
        fingerprint = digest(projection)
        vectors = np.zeros((2,128));vectors[0,0]=1;vectors[1,1]=1
        fitted = {'node_ids':['local:a','local:b'],'vectors':vectors,'normalized_vectors':vectors,
                  'word2vec_parameters':{'fixture':True},'walk_sha256':'f'*64,'walk_count':20}
        collection = Collection(corrupt)
        def get_collection(name,embedding_function,metadata):
            self.assertTrue(name.startswith('threatweave_graph_eval_'))
            collection.metadata=metadata;return collection
        client = SimpleNamespace(get_or_create_collection=get_collection)
        chroma = SimpleNamespace(PersistentClient=lambda **_:client)
        neo4j = SimpleNamespace(GraphDatabase=SimpleNamespace(driver=lambda *a,**k:Driver()))
        required = {'node2vec':'0.5.0','gensim':'4.4.0','networkx':'3.7','numpy':'1.26.4','scipy':'1.17.1','chromadb':'1.0.15'}
        reads = [(projection,fingerprint),(projection,'0'*64 if changed else fingerprint)]
        with patch('sys.argv',['index_evaluation_graph.py','--repo',str(root)]),patch.object(
                builder,'EvaluationGraphRetriever',return_value=retriever),patch.object(
                builder,'checked_text_index',return_value=({'fingerprint':'c'*64},{},[],[])),patch.object(
                builder,'read_projection',side_effect=reads) as read_live,patch.object(
                builder,'fit_projection',return_value=fitted),patch.object(
                builder.importlib.metadata,'version',side_effect=lambda p:required[p]),patch.dict(
                os.environ,training_environment(config['node2vec'])),patch.dict('sys.modules',{
                'neo4j':neo4j,'chromadb':chroma,'chromadb.config':SimpleNamespace(Settings=lambda **_:None)}),patch(
                'builtins.input',return_value=''),patch.object(builder.getpass,'getpass',return_value='fixture'),redirect_stdout(io.StringIO()):
            result = builder.main()
        self.assertEqual(development.read_text(encoding='utf-8'),'{"preserved":"development"}')
        return result,read_live.call_count

    def test_success_publishes_only_evaluation_assets_with_scope_and_text_binding(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            result,calls = self.execute(tmp)
            self.assertEqual((result,calls),(0,2))
            root = Path(tmp);pointer = json.loads((root/'work/evaluation_graph_index/current.json').read_text(encoding='utf-8'))
            path = Path(pointer['manifest_path']);self.assertEqual(path.parent.parent,root/'work/evaluation_graph_index')
            manifest = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(manifest['evaluation_scope']['sha256'],'b'*64)
            self.assertEqual(manifest['text_index_fingerprint'],'c'*64)
            self.assertEqual(manifest['version'],'evaluation-graph-vector-index-v1')
            self.assertTrue(manifest['live_projection_verified'])
            receipt = json.loads(next((root/'work/evaluation_graph_index_runs').glob('*/index_receipt.json')).read_text(encoding='utf-8'))
            self.assertEqual((receipt['status'],receipt['exact_vector_lookup_count']),('ready',2))

    def test_changed_live_projection_does_not_publish_ready_pointer(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            result,calls = self.execute(tmp,changed=True)
            self.assertEqual((result,calls),(1,2))
            self.assertFalse((Path(tmp)/'work/evaluation_graph_index/current.json').exists())

    def test_wrong_stored_vector_binding_blocks_publication(self):
        with tempfile.TemporaryDirectory(dir=REPO/'work') as tmp:
            result,calls = self.execute(tmp,corrupt=True)
            self.assertEqual(result,1)
            self.assertFalse((Path(tmp)/'work/evaluation_graph_index/current.json').exists())


if __name__ == '__main__':unittest.main()
