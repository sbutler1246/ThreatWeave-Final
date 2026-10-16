# Matching expanded graph-only QA

Completed: [the graph-only run and source review](ThreatWeave_expanded_graph_qa_checkpoint.md) record three supported core incident answers without execution failures, with remaining mitigation/detail limitations and human verification pending. [Hybrid without Node2Vec](ThreatWeave_expanded_combined_qa_step.md) is the final matching condition. The instructions below preserve the preceding checkpoint.

The expanded full-hybrid and text-only runs completed. [The text-only review](ThreatWeave_expanded_text_qa_checkpoint.md) records unsupported incident claims in its first two answers, where only ATT&CK guidance was supplied. [The full-hybrid review](ThreatWeave_expanded_hybrid_qa_checkpoint.md) records supported incident observations and remaining generation limitations. Human verification remains pending.

Run the matching graph-only condition next. Keep Neo4j and Ollama running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\graph_qa.py" --demo
```

Press Enter for URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, then enter the instance password. Typing is hidden and the password is not saved. This command reads accepted source-supported graph paths, without text-vector search or Node2Vec expansion. It uses the same three questions, shared v2 generator and model settings as the two completed expanded conditions.

Results save under `work/graph_qa`, with a generated review directly in `docs`. Preserve the installed model so its recorded digest matches `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e` from the completed matching runs.

The assistant's offline `graph_qa.py --demo --preview` passed without live service calls:

| Case | Source-fixture paths | Exact source passages | Context bytes / 3000 |
| --- | --- | ---: | ---: |
| Raccoon Stealer | Four three-hop paths | 12 | 2795 |
| Rhysida actors | Five two-hop paths | 13 | 2699 |
| ALPHV affiliates | Two one-hop paths | 3 | 415 |

This establishes local packing readiness, not current live presence or generated-answer quality. The live run verifies accepted source evidence. Review source attribution, mitigation guidance scope/completeness and semantic repetition in the resulting answers. Keep all conditions unchanged until the final matching hybrid-without-Node2Vec run is collected. Broader processing and final held-out evaluation remain separate and unfinished.
