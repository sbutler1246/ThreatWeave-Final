# Build the additional-batch development text index

Completed update: operator run `20261015T225013Z-42adf966` is ready; the saved receipt, manifest and all 215 source records passed offline reconstruction. [The checkpoint](ThreatWeave_corpus_batch_text_index_checkpoint.md) records saved retrieval coverage. [The graph-vector rebuild is next](ThreatWeave_corpus_batch_graph_index_step.md). The instructions below describe the completed text-build stage.

October 15, 2026. [The accepted scope checkpoint](ThreatWeave_corpus_batch_scope_checkpoint.md) verifies the completed source/mitigation imports and shared scope expansion. The offline cached-tokenizer preview passed: 41 CISA windows, 96 direct ATT&CK reference parents and 215 retrieval chunks.

Run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_text.py"
```

This uses the already cached MiniLM model on the CPU. No Neo4j/Ollama connection or installation is needed. The operator runs the index build. The assistant has run only its `--preview` source/tokenizer checks.

The build creates a collection keyed by the expanded source fingerprint, verifies all stored source text/metadata and normalized 384-dimensional vectors, and records three existing text-retrieval smoke queries. Those queries do not generate answers or measure final answer quality. Prior collections, saved answers and historical receipts remain preserved.

Expected scope: 41 CISA parents, 96 ATT&CK references and 215 chunks, each at most 240 WordPieces and 1000 characters including inherited context. Keep the frozen embedding revision, source boundaries and retrieval settings.

Return the `READY` output and saved run path under `work/text_index_runs`. We will inspect the receipt and ranked source matches offline, then prepare the matching graph-vector refresh. Full-hybrid application queries require both matching indexes. Human review and broader/final evaluation remain pending.
