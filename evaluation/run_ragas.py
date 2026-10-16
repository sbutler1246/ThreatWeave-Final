"""RAGAS adapter specification as a callable runner; integration not executed.

The Windows/Python 3.12 evaluator dependencies are frozen in requirements.lock.txt.
The lock was dependency-resolved; live Ollama/model evaluation is not yet run.
Never pass the gold reference to the query engine; supply it here only.
"""
from importlib.metadata import version
import os

PINNED_PACKAGES = {
    'ragas': '0.2.15',
    'langchain-ollama': '0.2.3',
    'langchain-huggingface': '0.1.2',
    'sentence-transformers': '3.4.1',
}
MINILM_REVISION = '1110a243fdf4706b3f48f1d95db1a4f5529b4d41'

def require_pinned_versions():
    """Reject accidental evaluator upgrades before generating scores."""
    for package, expected in PINNED_PACKAGES.items():
        actual = version(package)
        if actual != expected:
            raise RuntimeError(f'{package}: expected {expected}, found {actual}')

def build_local_evaluators(base_url='http://localhost:11434'):
    """Construct local adapters; model download/service checks remain runtime work."""
    require_pinned_versions()
    os.environ.setdefault('RAGAS_DO_NOT_TRACK', 'true')
    from langchain_ollama import ChatOllama
    from langchain_huggingface import HuggingFaceEmbeddings
    from ragas.llms import LangchainLLMWrapper
    from ragas.embeddings import LangchainEmbeddingsWrapper
    judge = ChatOllama(model='llama3.1:8b', base_url=base_url,
        temperature=0, num_ctx=8192, num_predict=700, seed=42)
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'revision': MINILM_REVISION, 'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True})
    return LangchainLLMWrapper(judge), LangchainEmbeddingsWrapper(embeddings)

def evaluate_logged_answers(records,judge,embeddings):
    require_pinned_versions()
    os.environ.setdefault('RAGAS_DO_NOT_TRACK', 'true')
    from ragas import EvaluationDataset,evaluate
    from ragas.metrics import Faithfulness,ResponseRelevancy,LLMContextRecall
    required={'user_input','response','retrieved_contexts','reference'}
    for row in records:
        if not required<=row.keys(): raise ValueError('Missing logged evaluation fields')
        if not isinstance(row['retrieved_contexts'],list):raise ValueError('Contexts must be the actual supplied passage list')
    dataset=EvaluationDataset.from_list(records)
    return evaluate(dataset=dataset,metrics=[Faithfulness(llm=judge),
        ResponseRelevancy(llm=judge,embeddings=embeddings),LLMContextRecall(llm=judge)],
        llm=judge,embeddings=embeddings,raise_exceptions=False)
