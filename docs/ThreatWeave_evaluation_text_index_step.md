# Build the shared evaluation text index

The operator's 510-chunk build completed and its saved records/receipt passed offline verification. Continue with [the matching evaluation graph index](ThreatWeave_evaluation_graph_index_step.md). The build instructions below remain the preparation record.

October 15, 2026 (America/Chicago). The direct evaluation mitigation import completed: 109 reference assertions, 203 source-reference combinations and zero same-window three-hop chains. The operator's transaction took 1.483 seconds including verification. Its saved run is `work/evaluation_corpus_mitigations/20261016T043104Z-85c82c88`.

Offline reconstruction checked the complete imported reference records, source assertion selection, exact snapshot descriptions, source/reference/chain counts, review identity, source receipt/record hashes and explicit evaluation-plan fingerprint. Human verification remains pending. The shared evaluation scope is now prepared for all four conditions, using the reviewed development and held-out evidence together.

Run this one command:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_evaluation_text.py"
```

This uses the installed cached MiniLM model and Chroma package. Neither Neo4j nor Ollama is needed. Return the final `READY` and saved-records lines. The assistant has run only offline source/tokenizer previews and tests; the operator builds the actual index.

| Shared source preparation | Count |
| --- | ---: |
| CISA source reports | 15 |
| Reviewed CISA parent windows | 101 |
| Direct ATT&CK reference parents | 190 |
| Total common source parents | 291 |
| Retrieval child chunks | 510 |
| Source-fixture domain nodes | 212 |
| Source-fixture directed facts | 394 |

Shared scope SHA-256: `75547d824c6b0386fdac3ed17b3a50f03b97c1eaabc2ae1692961a2d7fb5d599`.

The offline snapshot is saved at `work/evaluation_scope_runs/20261016T043617Z-a24728fc`, including the exact 510 text records, source-fixture projection and hashed receipt. Expected text fingerprint: `0fe7f0c80769a67a158d505df0d72c77e12273c02fa8e6f3dd56da436685de73`. The fixture's connected-component sizes are 204, 4, 2 and 2. No embeddings were fitted and no live graph was queried to create this snapshot.

All 101 CISA windows and 190 reference parents are available to both graph and text retrieval. Graph evidence uses the accepted assertion allowlists and direct reference records. The text index contains their exact source passages, with separately retained heading spans and source offsets, without embedding predicted triples or review reasons. This scope follows the existing reviewed-window evidence policy; the 49 empty evaluation windows remain preserved outside this retrieval subset and must still be accounted for in extraction coverage/scoring.

The shared graph scope contains 232 explicitly reviewed extracted assertion occurrences, plus the original ten bounded development assertions, and 190 fused reference assertions. The source-derived fixture has 212 domain nodes and 394 distinct directed facts. Its fixture counts do not establish live graph presence or a fitted Node2Vec index. The operator performs the separate live graph projection/index build after the text index is checked.

The frozen MiniLM splitter is reused directly. All 510 inputs fit the unchanged ceilings of 240 measured WordPieces and 1,000 characters including inherited context. The embedding model remains all-MiniLM-L6-v2 at the recorded revision, with 384 dimensions and normalized vectors. The build verifies stored identities, exact passages, source metadata, dimensions and normalization and runs the same three development retrieval smoke questions. Those checks produce no LLM answers or final benchmark scores; no final questions or answers are read.

Evaluation text records/manifests are saved under `work/evaluation_text_index/<fingerprint>` and build receipts under `work/evaluation_text_index_runs/<run>`. The collection name begins `threatweave_text_eval_`. The shared Chroma database retains existing versioned development collections. Development source files, index manifests and graph pointer remain unchanged. The application continues to use its development assets until a separate integration selects evaluation assets.

The evaluation graph retriever inherits the frozen source-verification, candidate/path selection and retrieval methods. Its scope is supplied separately. Generation, chunking, embedding, graph-training settings and the conservative 3,000-byte evidence cap remain unchanged. The original development metadata is retained alongside a distinct `evaluation_scope` record. New index identities include that evaluation scope and the verified import-receipt hashes. No tuning has been based on held-out outputs or final labels.

All 21 targeted offline checks passed: eight new evaluation-scope checks and thirteen existing chunking/projection regressions. They cover label/service isolation, source-parent parity, exact source/context offsets, input bounds, frozen methods/settings, projection round-trip, all 232 reviewed source supports, rejected provenance/receipt mutations, missing facts, a preview without embedding/database loading, and preservation of the development graph pointer. The text preview passed.

After text indexing, the live evaluation graph index, final four-mode runner, controlled 240-answer experiment, metric integration, blinded human scoring, statistical analysis and final reporting remain pending. All original outputs, failures, empty selections, rejected candidates and human-review statuses remain preserved for analysis.
