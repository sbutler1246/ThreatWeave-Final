# Node2Vec dependency setup

The combined development run completed; its review is saved in `docs/ThreatWeave_combined_qa_development_review.md`. It now supplies all five AnyDesk mitigation references, while the Rclone answer has an “intended use” wording issue that remains recorded for review.

Run in PowerShell:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_node2vec.py"
```

The setup installs `requirements-node2vec.txt` into the existing Python 3.12 application environment using uv. It retains the text-stage direct pins and adds node2vec 0.5.0, Gensim 4.4.0, NetworkX 3.7 and SciPy 1.17.1. NetworkX and SciPy match the inspected installed environment. Gensim 4.4.0 supports that SciPy range and provides a Windows/Python 3.12 wheel; runtime compatibility is still checked locally by the command. Internet access is needed for package installation. Neo4j and Ollama are not required for this synthetic setup check.

The command fits an eight-node synthetic undirected graph twice using the configured parameters: dimension 128, walk length 20, ten walks per node, window 10, p=q=1, five epochs, five negative samples, seed 42 and one worker. Python hash randomization and numerical-library thread counts are fixed before the training child process starts. Node and edge insertion order is sorted. Additional Word2Vec settings are recorded in the receipt, including skip-gram, minimum count one and the sampling/learning-rate settings.

The check requires identical raw vectors and walks for the two fits in that process. It also checks normalization, saves the synthetic vectors, tests a separate 128-dimensional Chroma probe and revalidates the existing text index against its frozen sources and embeddings. This synthetic repeatability check does not guarantee identical fits across hardware or software versions.

Resolved package versions are saved under `work/node2vec_setup`; each check has its own timestamped receipt and isolated synthetic Chroma probe. A review document is automatically written directly into `docs`. These are development direct pins and a resolved environment snapshot, not the final transitive application lock. The evaluator environment remains separate.

Expected final message:

```text
READY: Node2Vec dependencies, graph-vector probe and text-index regression checks passed.
```

This step establishes dependency and synthetic fitting readiness. It does not read Neo4j, fit vectors for the ThreatWeave graph, create the production graph collection or enable full-hybrid QA. After it passes, build a frozen undirected projection excluding Document/provenance hubs, retain the graph revision and node-ID map, and validate the separate production vector index. Full hybrid must require those matching artifacts; the existing combined mode stays labeled `hybrid_no_node2vec`.

References: [Node2Vec implementation and seed/worker options](https://github.com/eliorc/node2vec), [Gensim 4.4.0 dependency metadata](https://raw.githubusercontent.com/piskvorky/gensim/4.4.0/setup.py), [Windows/Python 3.12 distribution](https://pypi.org/project/gensim/4.4.0/), and [Gensim reproducibility settings](https://radimrehurek.com/gensim/models/word2vec.html).
