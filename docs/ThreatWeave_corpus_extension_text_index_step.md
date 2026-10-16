# Build the three-report extension development text index

Completed update: operator run `20261016T002500Z-41e31bf5` is ready. [Its receipt and all 305 saved source records passed offline reconstruction](ThreatWeave_corpus_extension_text_index_checkpoint.md). [The graph-vector rebuild is next](ThreatWeave_corpus_extension_graph_index_step.md). The instructions below describe the completed text-build stage.

October 15, 2026. [The accepted scope checkpoint](ThreatWeave_corpus_extension_scope_checkpoint.md) verifies completed source/mitigation imports and shared retrieval scope expansion. The offline cached-tokenizer preview passed: 53 CISA source parents, 139 direct ATT&CK reference parents and 305 retrieval chunks.

Run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_text.py"
```

The operator runs this index build. It uses the already cached MiniLM model on the CPU; Neo4j, Ollama and another installation are not needed. The assistant has run only source/receipt checks and the source/tokenizer `--preview`, with no service call or index write.

Expected scope: 53 CISA source windows, 139 direct ATT&CK references and 305 chunks. Each embedding input remains at most 240 WordPieces and 1000 characters including inherited context. The source fingerprint creates a separate versioned collection and preserves previous collections and saved answers.

The build verifies exact stored source text/metadata and normalized 384-dimensional vectors, then records the three existing development text-retrieval smoke checks. These do not generate answers or establish quality scores. Frozen model revision, source boundaries and retrieval settings remain unchanged.

Share the `READY` output and saved run path under `work/text_index_runs`. We will inspect the receipt, exact records and saved ranked matches offline before the matching graph-vector rebuild. Application queries await both matching indexes and a server restart. Human verification, broader coverage assessment and final held-out evaluation remain pending.
