# Fit the live development graph-vector index

Current checkpoint: [the expanded graph-vector index completed](ThreatWeave_expanded_graph_index_checkpoint.md) for the shared 16-CISA-scope/58-reference pool. It verified 75 live nodes, 102 directed facts and all 75 stored vectors; the actual saved-index full-hybrid preview passed. All 175 offline tests passed at the implementation checkpoint. [Fresh expanded QA](ThreatWeave_expanded_qa_step.md) is next. The six-scope/22-node checkpoint and 82-test baseline below are historical.

The Node2Vec dependency check passed. Its checkpoint is saved in `docs/ThreatWeave_node2vec_setup_checkpoint.md`.

Start the ThreatWeave Neo4j instance, then run in PowerShell:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_graph.py"
```

Use the displayed defaults: URI `bolt://localhost:7687`, username `neo4j`, database `neo4j`. Enter your instance password when prompted; typing is hidden and the password is not saved. Ollama is not required for graph fitting.

## Verified graph scope

The script reads the current six development CISA scopes and their direct ATT&CK 17.1 mitigation references. It verifies accepted assertion status, node identity, aliases, source hashes, exact evidence spans and structured-reference provenance using the existing graph QA source checks. It requires all expected source-supported development facts to be present; missing or rejected facts stop fitting. It does not insert missing edges, read benchmark gold answers or write to Neo4j.

The projection contains domain endpoints only. Document, Chunk and Assertion provenance hubs are excluded. Node2Vec receives a simple undirected unweighted graph; the original directed predicates and evidence remain in the saved projection for auditing and later typed-path retrieval. Multiple accepted assertions can support one fact. Duplicate stored relationships for the same fact are rejected.

## Fitting and versioned storage

The configured parameters remain 128 dimensions, walk length 20, ten walks per node, window 10, p=q=1, five epochs, five negative samples, seed 42 and one worker. The script starts a child process with a fixed Python hash seed and numerical-library thread counts before fitting, and sorts node/edge order.

The graph revision hash covers frozen source identity, resolved node identities, accepted directed facts and source evidence/status. Incidental database timestamps are excluded. The vector-index fingerprint also records training parameters, package/Python versions, training-source hash, component mapping and the fitted vector hashes. The live projection is reread after fitting and storage; a changed graph prevents publishing a ready index manifest. Later full-hybrid retrieval must compare the live projection against this manifest and reject stale assets.

Normalized graph vectors are stored in a separate `threatweave_graph_dev_<fingerprint>` Chroma collection under `work/chroma`. Text embeddings remain in their distinct 384-dimensional collection. Metadata retains canonical node IDs, entity types, names, component IDs and the graph/index hashes. Source projections, node-ID arrays, raw/normalized vectors and file checksums are saved under `work/graph_index/<fingerprint>`. A `current.json` pointer is published only after validation. Each run also records its outcome in `work/graph_index_runs` and writes a review document directly into `docs`.

The script verifies each stored node/vector binding and exact-vector lookup. Those checks establish storage integrity, not meaningful neighbor relevance. Node2Vec similarity does not establish a source-supported fact; the next retrieval stage must require valid directed typed paths and their accepted evidence.

## Offline validation

All 82 offline tests passed. New checks cover missing/rejected facts, altered quotations/documents, conflicting identities/aliases, duplicate relationships, stable hashes under row reordering and revision changes when accepted review status changes.

A source-fixture preview contains 22 domain nodes, 23 directed facts and 23 undirected edges, with connected-component sizes 18, 2 and 2. An offline fit of that fixture produced normalized vectors of shape `(22, 128)`. These fixture checks did not publish a live index or verify Neo4j presence. The command above must confirm the actual stored graph and fit from that live snapshot.

Component sizes in this step are calculated with NetworkX for the saved projection; they are not a new Neo4j GDS result. The earlier GDS pilot remains a separate development observation.

Expected final message:

```text
READY: Live development graph projected, Node2Vec fitted and separate graph-vector index verified.
```

After this passes, integrate seed-vector neighbor lookup into full-hybrid retrieval while retaining supported paths and the same generation/context limits. Full-corpus ingestion, final controlled evaluation and the interface remain outstanding.
