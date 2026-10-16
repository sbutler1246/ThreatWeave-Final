# Build the matching three-report extension graph-vector index

Completed update: run `20261016T003953Z-4ad94e21` is ready. [The saved receipt, projection, provenance and all 142 vector bindings passed offline verification](ThreatWeave_corpus_extension_graph_index_checkpoint.md). Restart the application to load both matching indexes. The instructions below describe the completed build stage.

October 15, 2026. [Operator text-index run `20261016T002500Z-41e31bf5` is verified](ThreatWeave_corpus_extension_text_index_checkpoint.md) with 305 chunks across 53 CISA source windows and 139 ATT&CK reference parents. [The accepted scope checkpoint](ThreatWeave_corpus_extension_scope_checkpoint.md) records the expected matching graph.

With Neo4j running, execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_graph.py"
```

Accept the connection defaults if appropriate and enter the password with hidden typing. Ollama and a new installation are not needed. The operator performs the live graph read and local index build.

Expected source-derived projection: 142 domain nodes, 245 directed facts, 245 undirected training edges and connected-component sizes `[133, 5, 2, 2]`. The build verifies actual live source/identity/provenance records before fitting. Missing, changed or rejected required evidence prevents publication. Provenance hubs are excluded and distinct assertion supports are retained.

Frozen Node2Vec parameters remain 128 dimensions, walk length 20, ten walks per node, window 10, p=q=1, five epochs, five negative samples, seed 42 and one worker. The builder verifies stored normalized vectors and all node/vector bindings, records exact-vector lookups, rereads the live graph to check freshness and publishes a versioned manifest/current pointer only after verification. Prior collections and run records remain saved.

Share the completion output and saved run path under `work/graph_index_runs`. We will inspect the saved receipt, projection and vector files offline. After both matching indexes pass, restart the application to load the final development scope. No additional four-mode demonstration round is needed for this refresh checkpoint.

The assistant's preview is an expected source projection, not a live database read or proof of embedding quality. Human verification, coverage assessment, evaluation-corpus preparation and controlled final evaluation remain pending.
