"""Check the configured MiniLM embedding and Chroma persistence; save a receipt."""
import argparse
import importlib.metadata
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--offline', action='store_true', help='Require already cached model files.')
    args = parser.parse_args()
    repo = args.repo.resolve()
    folder = repo/'work'/'text_setup'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    receipt = {'purpose': 'development_text_search_setup', 'status': 'failed',
               'python': platform.python_version(), 'executable': sys.executable,
               'started_at': datetime.now(timezone.utc).isoformat()}
    os.environ['HF_HOME'] = str(repo/'work'/'model_cache'/'huggingface')
    os.environ['TORCH_HOME'] = str(repo/'work'/'model_cache'/'torch')
    os.environ['ANONYMIZED_TELEMETRY'] = 'False'
    os.environ['HF_HUB_DISABLE_TELEMETRY'] = '1'
    if args.offline:
        os.environ['HF_HUB_OFFLINE'] = '1'
    try:
        if sys.version_info[:2] != (3, 12):
            raise ValueError('This setup targets Python 3.12.')
        expected = {'sentence-transformers': '3.4.1', 'transformers': '4.49.0',
                    'torch': '2.6.0', 'numpy': '1.26.4', 'chromadb': '1.0.15'}
        versions = {name: importlib.metadata.version(name) for name in expected}
        receipt['packages'] = versions
        for name, version in expected.items():
            if versions[name].split('+')[0] != version:
                raise ValueError(f'{name} is {versions[name]}; this stage requires {version}.')
        import numpy as np
        import chromadb
        from chromadb.config import Settings
        from sentence_transformers import SentenceTransformer

        config = json.loads((repo/'config.json').read_text(encoding='utf-8'))['text_embedding']
        receipt['embedding_configuration'] = config
        if config['dimension'] != 384 or config['normalize'] is not True or len(config['revision']) != 40:
            raise ValueError('Expected the frozen 384-dimensional, normalized MiniLM configuration.')
        print('Loading the frozen MiniLM revision (first run downloads model files)...', flush=True)
        model = SentenceTransformer(config['model'], revision=config['revision'],
                                    cache_folder=str(repo/'work'/'model_cache'/'sentence_transformers'),
                                    device='cpu', trust_remote_code=False,
                                    local_files_only=args.offline)
        if model.get_sentence_embedding_dimension() != config['dimension']:
            raise ValueError('Model embedding dimension does not match config.json.')
        samples = ['ThreatWeave setup check: network service discovery.',
                   'ThreatWeave setup check: credential theft.']
        vectors = model.encode(samples, normalize_embeddings=True, convert_to_numpy=True,
                               show_progress_bar=False)
        if vectors.shape != (2, 384) or not np.isfinite(vectors).all():
            raise ValueError('Unexpected vector shape or non-finite embedding values.')
        norms = np.linalg.norm(vectors, axis=1)
        if not np.allclose(norms, 1.0, atol=1e-5):
            raise ValueError('Embedding vectors are not normalized.')
        print('PASS: MiniLM produces normalized 384-dimensional vectors.', flush=True)

        # This isolated probe contains synthetic text only, never project evidence.
        settings = Settings(anonymized_telemetry=False)
        path = str(folder/'chroma_probe')
        client = chromadb.PersistentClient(path=path, settings=settings)
        collection = client.create_collection('threatweave_setup_probe', embedding_function=None,
                                               metadata={'hnsw:space': 'cosine'})
        collection.add(ids=['probe-network', 'probe-credentials'], documents=samples,
                       embeddings=vectors.tolist())
        reopened = chromadb.PersistentClient(path=path, settings=settings).get_collection(
            'threatweave_setup_probe', embedding_function=None)
        result = reopened.query(query_embeddings=[vectors[0].tolist()], n_results=1,
                                include=['distances'])
        if reopened.count() != 2 or result['ids'] != [['probe-network']]:
            raise ValueError('Chroma storage or nearest-vector lookup failed.')
        if abs(result['distances'][0][0]) > 1e-4:
            raise ValueError('Cosine lookup failed to reproduce the exact-vector match.')
        print('PASS: Chroma stores and retrieves the supplied vectors locally.', flush=True)
        receipt.update(status='ready', embedding_dimension=384, vector_norms=norms.tolist(),
                       chroma_probe_count=reopened.count(), top_match=result['ids'][0][0],
                       note='Synthetic setup probe; corpus indexing and text/hybrid QA remain pending.')
        exit_code = 0
    except Exception as exc:
        receipt['error'] = f'{type(exc).__name__}: {exc}'
        print(f'SETUP CHECK FAILED: {receipt["error"]}', flush=True)
        exit_code = 1
    receipt['finished_at'] = datetime.now(timezone.utc).isoformat()
    (folder/'setup_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print(f'Saved setup records: {folder}', flush=True)
    if exit_code == 0:
        print('READY: Text-search dependencies and embedding model checks passed.', flush=True)
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
