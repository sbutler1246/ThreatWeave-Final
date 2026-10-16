# Build the expanded development text index

Completed checkpoint: run `20261015T042635Z-94f0293b` verified all 95 source chunks and stored vectors. [The source/index review](ThreatWeave_expanded_text_index_checkpoint.md) records the ranked coverage limitations. [The current next step rebuilds the graph-vector index](ThreatWeave_expanded_graph_index_step.md). The original text-build instructions below remain available for an intentional repeat.

October 14, 2026. The source import and direct mitigation import both completed. [The expanded scope checkpoint](ThreatWeave_expanded_development_scope_checkpoint.md) records 16 CISA source parents and 58 direct ATT&CK reference parents, shared across all four development retrieval modes.

The preview and completed build contain **95 retrieval chunks**, each at most **240 WordPieces and 1000 characters**, including inherited context. Source spans and parent IDs remain exact. All 175 offline tests and the source-only graph previews pass. The expanded text index is ready; live graph fitting and matching generated QA remain pending.

## Run

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_text.py"
```

The command uses the cached MiniLM model on the CPU. Ollama, Neo4j and another installation are not needed. The index uses a new source fingerprint, preserving the earlier collection. It verifies stored text, source metadata and normalized 384-dimensional vectors, then records three ranked text-retrieval smoke checks about Raccoon Stealer, Rhysida valid-account access and ALPHV software use.

Expected summary: 16 CISA scopes, 58 ATT&CK references and 95 retrieval chunks. Receipts save under `work/text_index_runs`, index manifests under `work/text_index`, Chroma data under `work/chroma`, and the review document directly in `docs`. The preview check is available with `--preview` and writes no index.

After the text build succeeds, the live graph-vector index needs a matching rebuild before expanded full-hybrid QA. This step alone does not fit Node2Vec, generate answers, complete broader corpus extraction or run held-out evaluation.
