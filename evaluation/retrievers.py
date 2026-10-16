"""Evaluation asset loaders with the frozen retrieval/packing methods inherited."""
import json
from pathlib import Path

from evaluation.corpus_scope import EvaluationGraphRetriever
from evaluation.index_assets import checked_text_index,checked_graph_index
from retrieval.development_text import load_model,load_tokenizer,metadata,sha
from retrieval.text_retrieval import DevelopmentTextRetriever,VERSION as TEXT_VERSION
from retrieval.graph_vectors import GraphVectorIndex
from retrieval.combined_retrieval import DevelopmentCombinedRetriever,VERSION as COMBINED_VERSION
from retrieval.hybrid_retrieval import DevelopmentHybridRetriever,DOMAIN_PATH_QUERY,EXPANSION_QUERY,source_mentions


class EvaluationTextRetriever(DevelopmentTextRetriever):
    def __init__(self,repo,config):
        import numpy as np
        import chromadb
        from chromadb.config import Settings
        self.repo,self.config = Path(repo).resolve(),config
        receipt,self.manifest,records,_ = checked_text_index(self.repo,config['evaluation_scope'])
        fingerprint = receipt['fingerprint']
        self.tokenizer = load_tokenizer(self.repo,config)
        self.client = chromadb.PersistentClient(path=str(self.repo/'work/chroma'),settings=Settings(anonymized_telemetry=False))
        self.collection = self.client.get_collection(self.manifest['collection_name'],embedding_function=None)
        expected = {'hnsw:space':'cosine','index_fingerprint':fingerprint,
                    'model_revision':config['text_embedding']['revision'],'dimension':384}
        if any(self.collection.metadata.get(k)!=v for k,v in expected.items()):
            raise ValueError('Evaluation text collection metadata changed.')
        self.by_id = {r['chunk']['chunk_id']:r for r in records}
        stored = self.collection.get(include=['documents','metadatas','embeddings'])
        if (len(stored['ids'])!=len(records) or set(stored['ids'])!=set(self.by_id)
                or any(len(stored[k])!=len(records) for k in ['documents','metadatas','embeddings'])):
            raise ValueError('Evaluation text collection contents changed.')
        for identifier,document,meta in zip(stored['ids'],stored['documents'],stored['metadatas']):
            if document!=self.by_id[identifier]['embedding_text'] or meta!=metadata(self.by_id[identifier]):
                raise ValueError('Evaluation text/source binding changed.')
        self.model = load_model(self.repo,config)
        expected_vectors = self.model.encode([self.by_id[i]['embedding_text'] for i in stored['ids']],
            normalize_embeddings=True,convert_to_numpy=True,show_progress_bar=False)
        actual = np.asarray(stored['embeddings'])
        if (actual.shape!=expected_vectors.shape or not np.isfinite(actual).all()
                or not np.allclose(actual,expected_vectors,atol=1e-5,rtol=1e-5)):
            raise ValueError('Evaluation text vectors differ from their exact source embeddings.')
        self.special_tokens = self.tokenizer.num_special_tokens_to_add(pair=False)
        self.configuration_hash = sha(json.dumps(config,sort_keys=True)+fingerprint+TEXT_VERSION)
        self.last_context,self.last_stats = '',{}


class EvaluationGraphVectorIndex(GraphVectorIndex):
    def __init__(self,repo,config):
        import numpy as np
        import chromadb
        from chromadb.config import Settings
        repo = Path(repo).resolve()
        _,self.manifest,self.projection,ids,_,vectors = checked_graph_index(repo,config['evaluation_scope'])
        self.nodes = {n['canonical_id']:n for n in self.projection['nodes']}
        self.vectors = dict(zip(ids,vectors))
        self.client = chromadb.PersistentClient(path=str(repo/'work/chroma'),settings=Settings(anonymized_telemetry=False))
        self.collection = self.client.get_collection(self.manifest['collection_name'],embedding_function=None)
        expected = {'index_fingerprint':self.manifest['index_fingerprint'],
                    'projection_sha256':self.manifest['projection_sha256'],'dimension':128,
                    'hnsw:space':'cosine','corpus_version':config['corpus_version']}
        if any(self.collection.metadata.get(k)!=v for k,v in expected.items()):
            raise ValueError('Evaluation graph collection metadata changed.')
        stored = self.collection.get(include=['documents','metadatas','embeddings'])
        if (set(stored['ids'])!=set(ids) or any(len(stored[k])!=len(ids)
                for k in ['ids','documents','metadatas','embeddings'])):
            raise ValueError('Evaluation graph collection node map changed.')
        for identifier,name,meta,vector in zip(stored['ids'],stored['documents'],stored['metadatas'],stored['embeddings']):
            if (name!=self.nodes[identifier]['name'] or meta!=self.metadata(identifier)
                    or not np.allclose(vector,self.vectors[identifier],atol=1e-6)):
                raise ValueError('Evaluation graph vector/source binding changed.')


class EvaluationCombinedRetriever(DevelopmentCombinedRetriever):
    def __init__(self,graph,text):
        if graph.config!=text.config:raise ValueError('Evaluation graph/text settings differ.')
        self.graph,self.text,self.config = graph,text,graph.config
        self.names = {k:v['name'] for k,v in graph.expected_entities.items()}
        self.configuration_hash = sha(json.dumps(self.config,sort_keys=True)+COMBINED_VERSION+
                                      graph.configuration_hash+text.configuration_hash)
        self.last_context,self.last_stats = '',{}


class EvaluationHybridRetriever(DevelopmentHybridRetriever):
    def __init__(self,graph,text,index):
        EvaluationCombinedRetriever.__init__(self,graph,text)
        self.index = index
        self.configuration_hash = sha(self.configuration_hash+index.manifest['index_fingerprint']+
                                      DOMAIN_PATH_QUERY+EXPANSION_QUERY+'development-full-hybrid-v1')
        self.mentions = source_mentions(graph)


def build_retrievers(repo,driver,database):
    graph = EvaluationGraphRetriever(repo,driver,database)
    text = EvaluationTextRetriever(repo,graph.config)
    index = EvaluationGraphVectorIndex(repo,graph.config)
    return {'text_only':text,'graph_only':graph,'hybrid_no_node2vec':EvaluationCombinedRetriever(graph,text),
            'hybrid':EvaluationHybridRetriever(graph,text,index)}
