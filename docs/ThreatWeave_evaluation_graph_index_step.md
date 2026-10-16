# Build the matching shared evaluation graph index

The live graph build completed and saved graph/vector/source checks passed. Continue with [the frozen final four-mode answer batch](ThreatWeave_final_evaluation_step.md). The graph-build instructions below remain the preparation record.

October 15, 2026 (America/Chicago). The operator's shared evaluation text build completed at `work/evaluation_text_index_runs/20261016T043755Z-ddd54a27`. Its ready receipt reports 510 stored chunks with normalized 384-dimensional embeddings and three successful retrieval smoke checks.

Offline verification independently matched all 510 saved records to the pre-build source snapshot, recomputed the complete text-payload fingerprint, checked canonical record/store paths, matched the manifest and current package versions, and matched all fifteen ranked smoke hits to their exact source records. Distances are finite and ordered. The audit is preserved at `work/evaluation_text_index_review_checks/20261016T044151Z-ad4ed2e2/audit.json`. This artifact audit performs no embedding recomputation, vector-database query or live service call.

Text fingerprint: `0fe7f0c80769a67a158d505df0d72c77e12273c02fa8e6f3dd56da436685de73`.

Shared evaluation scope: `75547d824c6b0386fdac3ed17b3a50f03b97c1eaabc2ae1692961a2d7fb5d599` — 101 CISA windows and 190 direct ATT&CK reference parents. The saved Raccoon check still retrieves five reference passages without CISA evidence; Rhysida has its CISA T1078 passage at rank two. The ALPHV check's first four hits are ALPHV CISA windows, followed by one Black Basta window. These are preserved development smoke observations, not final answer scores or evidence of improved quality. No retrieval settings were changed after inspecting them.

With Neo4j running, execute this one command:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_evaluation_graph.py"
```

Use the usual Neo4j URI, username and database and enter the password at the hidden prompt. Ollama is not needed. Return the final `READY`, verification counts and saved-records lines.

The offline graph preview passed: 212 domain nodes, 394 accepted directed facts, 394 undirected projection edges, and connected-component sizes 204, 4, 2 and 2. The source-only fixture is preserved in `work/evaluation_scope_runs/20261016T043617Z-a24728fc`. These fixture counts are expected; only the operator's live run can confirm matching stored graph support and fit the actual vectors.

The new entry point uses the frozen projection validator, source assertion allowlists and Node2Vec training implementation. It first checks the ready evaluation text index against the same scope. It reads Neo4j without writing, verifies accepted directed facts with exact source provenance, and fits a simple undirected unweighted domain projection with no Document/Chunk/Assertion hubs. Parameters remain 128 dimensions, walk length twenty, ten walks per node, window ten, p=q=1, five epochs, five negative samples, seed42 and one worker, with the same fixed thread/hash environment. A 212-node fit should produce 2,120 walks. No training or fitting has been performed by the assistant on this evaluation graph.

The build checks vector normalization, node/vector/source bindings and stored collection contents. It reads the accepted graph again before publication, requires the same projection hash and runs one exact-vector lookup per indexed node. Graph identity binds both `evaluation_scope` and the ready text fingerprint, alongside projection, training, runtime and vector hashes.

Evaluation assets use `work/evaluation_graph_index/<fingerprint>`, run receipts use `work/evaluation_graph_index_runs/<run>`, and the collection name begins `threatweave_graph_eval_`. The evaluation pointer is `work/evaluation_graph_index/current.json`. The original development pointer and assets remain intact. A ready evaluation pointer is published only after projection, storage and lookup checks succeed. A failed build preserves diagnostics and does not publish a new ready pointer.

All seventeen targeted offline checks passed: six saved-text asset checks, three simulated graph-publication checks and eight existing projection regressions. The publication tests use simulated database, fitting and vector-store results; they perform no actual training or live database operations. They verify separate evaluation output paths, scope/text identity bindings, successful double graph reads, preservation of the development pointer, blocked publication after graph changes, and blocked publication for an incorrect stored vector. Text checks reject changed records, counts, manifests, scopes, paths, runtime packages, smoke sources and invalid distances.

After the graph build is checked, final evaluation asset loading, the controlled four-mode 240-answer runner, metric integration, blinded human review, statistical analysis and reporting remain pending. Vector similarity never establishes an incident fact. Original predictions, failures, rejected candidates, source evidence and review statuses remain preserved.
