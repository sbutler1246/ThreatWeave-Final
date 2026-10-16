# Text-search setup step

The multi-source graph QA demonstration completed three development cases. Its reviewed checkpoint is saved in `docs/ThreatWeave_graph_qa_development_checkpoint.md`.
This step prepares MiniLM text embeddings and Chroma storage for the text-only baseline and subsequent hybrid search.

Run in PowerShell:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_text_search.py"
```

The setup uses the existing Python 3.12 environment and installed uv, installs the direct pins in `requirements-text.txt`, selects CPU PyTorch, downloads the configured MiniLM model revision, and checks normalized 384-dimensional embeddings plus a local Chroma vector lookup. Internet access is required for installation and the initial model download. Neo4j and Ollama are not needed for this setup check.

The direct dependency versions are sentence-transformers 3.4.1, transformers 4.49.0, torch 2.6.0, numpy 1.26.4 and chromadb 1.0.15. These are selected development versions; successful installation and runtime compatibility still need the user's local check. This file is not a full transitive dependency lock. The resolved installed environment is recorded at `work/text_setup/installed_environment.txt`; a full application lock will be finalized before experiments. The separately locked evaluator environment remains separate.

MiniLM model: `sentence-transformers/all-MiniLM-L6-v2`, revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, as frozen in `config.json`. Model caches and setup records stay inside `S:\ThreatWeave\work`. Each probe uses a separate folder and two synthetic sentences, outside the future evidence index. No graph writes or benchmark-label reads occur.

Expected final message:

```text
READY: Text-search dependencies and embedding model checks passed.
```

If installation fails, the model check stops. If the check fails, its error is saved in a timestamped `work/text_setup` receipt. Share the final error or success output to proceed. To repeat the check without package installation, run `check_text_setup.py` using the same Python. Add `--offline` to require cached model files.

Passing this step establishes dependencies and a synthetic vector-store check. It does not establish corpus indexing, text QA, hybrid retrieval, Node2Vec or benchmark performance.

Implementation references: [SentenceTransformer constructor and encoding](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html), [Chroma Python client](https://docs.trychroma.com/reference/python/client), [Chroma 1.0.15 Windows distribution](https://pypi.org/project/chromadb/1.0.15/), and [the frozen MiniLM model revision](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/tree/1110a243fdf4706b3f48f1d95db1a4f5529b4d41).
