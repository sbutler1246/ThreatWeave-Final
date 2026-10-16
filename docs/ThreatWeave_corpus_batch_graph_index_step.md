# Build the additional-batch graph-vector index

Completed update: operator run `20261015T230431Z-ce56e0cd` is ready. [Offline verification passed](ThreatWeave_corpus_batch_graph_index_checkpoint.md) for its receipt, projection, vector files, provenance and matching text scope. [Restart the application next](ThreatWeave_corpus_batch_application_step.md). The instructions below describe the completed build stage.

October 15, 2026. [The matching text index is verified](ThreatWeave_corpus_batch_text_index_checkpoint.md): 215 chunks across 41 CISA source windows and 96 ATT&CK reference parents. The source-derived graph preview passes with 117 domain nodes and 179 accepted directed facts.

With Neo4j running, execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_graph.py"
```

Accept the local connection defaults if appropriate, then enter the password with hidden typing. Ollama and a new installation are not needed. The operator performs the live read and index build.

The build verifies source assertions, exact evidence and reviewed provenance against the live graph before fitting. Expected source-fixture scope: 117 domain nodes, 179 directed facts, 179 undirected edges and components of sizes 108, 5, 2 and 2. Document/Chunk/Assertion provenance hubs are excluded. Repeated facts retain their distinct source supports. Missing, changed or rejected required evidence prevents publication.

Frozen Node2Vec settings remain 128 dimensions, walk length 20, ten walks per node, window 10, p=q=1, five epochs, five negative samples, seed 42 and one worker. The index builder fixes hash/thread settings, verifies stored normalized vectors and exact-vector lookups for all nodes, then rereads the live projection before publishing the versioned ready manifest and current pointer. Prior collections and records remain saved.

Expected completion: `READY: Live development graph projected, Node2Vec fitted and separate graph-vector index verified.` Share that output and the saved run path under `work/graph_index_runs`. We will inspect the receipt and saved projection offline before further application use.

The graph preview establishes expected source structure, not live graph presence or embedding quality. These steps do not complete human review, broader corpus processing or controlled held-out evaluation.
