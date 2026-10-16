# Rebuild the expanded development graph-vector index

Completed: [the expanded graph index checkpoint](ThreatWeave_expanded_graph_index_checkpoint.md) records 75 live nodes, 102 accepted directed facts and all 75 verified vectors. The actual saved-index full-hybrid preview also passed. [Fresh expanded QA](ThreatWeave_expanded_qa_step.md) is next. The rebuild instructions and pending statements below describe the preceding checkpoint.

October 14, 2026. [The expanded text index completed](ThreatWeave_expanded_text_index_checkpoint.md), verifying 95 chunks across 16 CISA source scopes and 58 direct ATT&CK references. The next step fits a matching graph-vector index from the live accepted graph.

## Run

Keep the ThreatWeave Neo4j instance running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_graph.py"
```

Press Enter for URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, then enter the password when prompted. The password is not saved. Ollama and a new installation are not required.

## Expected scope and checks

The source-fixture preview expects **75 domain nodes and 102 directed facts**: 44 extracted-origin facts and 58 fused-origin reference facts. Only accepted, source-backed typed relationships enter the projection. The three excluded uncertain/conditional pilot relationships remain excluded. Local actor qualifiers and independently resolved software identities remain separate.

The live read verifies node identities/aliases, exact source evidence, accepted review status, pinned new-window assertion IDs and reference provenance. Missing, rejected or altered required facts stop fitting. Document/Chunk/Assertion provenance hubs are excluded from Node2Vec. The simple undirected training projection retains the directed facts and their source records separately for audit and later path validation. Expected fixture components have sizes 71, 2 and 2; live verification must establish the actual accepted projection.

The frozen settings remain 128 dimensions, walk length 20, ten walks per node, window 10, p=q=1, five epochs, five negative samples, seed 42 and one worker. The process fixes the Python hash seed and numerical-library thread counts. No model or retrieval parameter tuning is introduced by this rebuild.

Vectors are normalized and stored in a separate graph Chroma collection. The script verifies every node/vector binding and exact-vector lookup, rereads the live graph to detect changes during fitting, then publishes a ready manifest/current pointer. Previous text and graph collections remain preserved. Vector similarity alone does not establish an incident relationship; retrieval still requires accepted directed source-supported paths.

Run records save under `work/graph_index_runs`, versioned vectors/projections/manifests under `work/graph_index`, and a review directly in `docs`. The expected final message is `READY: Live development graph projected, Node2Vec fitted and separate graph-vector index verified.`

## Verification and following work

All 175 offline tests previously passed, including expanded scope parity, pinned review/evidence, projection round-trip provenance and stale-index checks. The actual 75-node/102-fact source-fixture preview passes again. This documentation step changes no implementation and makes no live service calls. Live graph fitting remains pending until the operator runs the command.

After a successful graph-index receipt, run matching fresh demonstrations for all four QA modes. Text-only retrieval currently misses CISA observations in the top five results for the first two smoke questions; preserve that observed limitation for generated-answer review. These are development checks, not held-out scoring or proof of hybrid quality. Broader extraction, application integration and final controlled evaluation remain unfinished.
