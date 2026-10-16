# Full hybrid development QA

Current expanded-scope instructions: [fresh expanded QA](ThreatWeave_expanded_qa_step.md). Both expanded indexes and the saved-index preview passed; [the graph checkpoint](ThreatWeave_expanded_graph_index_checkpoint.md) records the new 75-node/102-fact projection and three new development questions. The six-scope examples and test counts below are historical.

The actual development graph-vector index passed; its checkpoint is saved in `docs/ThreatWeave_graph_index_checkpoint.md`.

Keep Neo4j and Ollama running, then run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\hybrid_qa.py" --demo
```

Accept the defaults: Neo4j URI `bolt://localhost:7687`, username `neo4j`, database `neo4j`. Enter the instance password when prompted. It is not saved.

## Full hybrid behavior

This command selects `hybrid`, with text retrieval, supported graph paths and the fitted Node2Vec graph index. `combined_qa.py` remains the separate `hybrid_no_node2vec` condition. Missing, mismatched or stale graph assets block full hybrid rather than silently changing modes.

Startup verifies the graph manifest identity, file checksums, node-ID map, vector shapes/normalization/hashes, component labels, training implementation and package/Python versions. The persisted Chroma node metadata and vectors must match their saved assets. The text branch independently verifies its MiniLM index and source records.

For each question, the graph branch reads and verifies the current accepted development projection. Its hash must match the fitted graph index. Explicit names, frozen aliases and verified source labels resolve at most five seeds. Each seed's saved 128-dimensional vector searches only the graph collection and its connected component, returning up to five neighbors after excluding all already linked seeds. Neighbor distances are recorded as retrieval outputs, not confidence probabilities or incident evidence.

The live path queries preserve the question's seed constraints, directions and supported predicates, and stay within the indexed domain and three hops. An additional query admits paths containing retrieved neighbor IDs. Base and expansion candidates are deduplicated, ranked using distinct neighbor rank support and bounded at 30. Within the existing graph evidence packer, neighbor priority can reorder whole paths without changing source validation. All selected edges still require accepted assertions and exact source evidence. The graph revision is checked again after the path reads, to detect a graph change during retrieval.

Text retrieval retains five nearest MiniLM chunks. Source-parent rank fusion, exact-span deduplication, global citation remapping and whole-group evidence packing are shared with the no-Node2Vec mode. Limits remain six paths, five text hits and the conservative 3000 UTF-8 byte cap. Exact generator-tokenizer accounting is still pending. Text and graph vectors remain in separate 384-dimensional and 128-dimensional collections; question embeddings are never compared directly to Node2Vec vectors.

The same cited Ollama generator and settings are used across the development conditions. Generated answers still require semantic review; Node2Vec similarity does not validate a claim. No benchmark reference answers are used for retrieval or generation.

## Offline checks

All 91 offline tests passed. Checks include stale revision rejection before neighbor lookup, missing full-hybrid assets, component/identity boundaries, exclusion of all seeds, non-finite distances, candidate caps, actual priority propagation into the source evidence packer, directed hop bounds and citation integrity.

The preview used the saved verified live projection, actual Node2Vec vectors and real text index without connecting to Neo4j or Ollama:

| Development case | Final graph paths | Text hits | Source passages | Node2Vec neighbor hits | Neighbor-matched path candidates |
| --- | --- | --- | --- | --- | --- |
| AnyDesk | Five three-hop paths | 5 | 16 | 10 across two seeds | 4 |
| Rclone | One one-hop path | 5 | 7 | 0 | 0 |
| Evilginx2 | One one-hop path | 5 | 7 | 0 | 0 |

The two prose components contain only their actor and software nodes, both linked as seeds; no additional same-component neighbors remain. Zero expansion is a legitimate result and does not justify inventing a longer chain. AnyDesk's evidence context was 2959 bytes; the prose cases were 1177 and 1154 bytes, all below the cap.

The preview establishes saved-index/source packing, not current live graph freshness or generated-answer quality. The command above performs the live checks and generation. A small development graph can yield similar final evidence across full hybrid and the ablation; differences in quality must be measured rather than assumed.

## Saved outputs

Each run saves questions, exact evidence, both branch details, neighbors by seed, candidate counts, source fusion ranks, selected groups, graph/index hashes, prompts, model digest, raw outputs and answers under `work/hybrid_qa`. The review document is automatically saved directly into `docs`. Per-case timings include graph freshness checks, neighbor search, path/text retrieval, fusion, packing and generation; startup validation/model loading is excluded.

Next, review the live answers before scaling beyond the development scopes and freezing the full-corpus, four-mode evaluation setup. The interface, complete ingestion, final dependency lock and controlled evaluation remain outstanding.

Cypher references: [Dynamic map access](https://neo4j.com/docs/cypher-manual/current/expressions/map-expressions/) and [list/reduce functions](https://neo4j.com/docs/cypher-manual/current/functions/list/).
