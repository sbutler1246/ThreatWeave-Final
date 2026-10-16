# Final matching development condition: hybrid without Node2Vec

Completed: [the expanded four-mode comparison](ThreatWeave_expanded_four_mode_development_comparison.md) reviews this final run and all 12 cases. All produced non-abstaining answers without execution failures, with semantic limitations recorded and human verification pending. No additional run is needed for this checkpoint. The instructions below preserve the preceding step.

[Full hybrid](ThreatWeave_expanded_hybrid_qa_checkpoint.md), [text-only](ThreatWeave_expanded_text_qa_checkpoint.md) and [graph-only](ThreatWeave_expanded_graph_qa_checkpoint.md) runs are recorded. The final condition combines text retrieval and accepted graph paths with Node2Vec disabled.

Keep Neo4j and Ollama running, then run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\combined_qa.py" --demo
```

Press Enter for URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, then enter the instance password. Typing is hidden and the password is not saved. The mode should print `hybrid_no_node2vec`.

This uses the same three questions, expanded source pool, text index and shared v2 generator. Preserve the model and options: `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`, temperature 0, context 8192 and output limit 700. Results save under `work/combined_qa`, with a generated review directly in `docs`.

The assistant's `combined_qa.py --demo --preview` passed using source-based graph fixtures and the actual cached text index, without live service calls:

| Case | Graph paths | Selected text hits | Exact source passages | Context bytes / 3000 |
| --- | --- | ---: | ---: | ---: |
| Raccoon Stealer | Four three-hop paths | 4 | 12 | 2795 |
| Rhysida actors | Five two-hop paths | 4 | 13 | 2699 |
| ALPHV affiliates | Two one-hop paths | 3 | 6 | 2306 |

Selected text hits can duplicate spans already supplied by graph paths, so they do not imply that new evidence was added. Preview checks local retrieval readiness; the live run must verify accepted source evidence and generate its own answers.

Review incident attribution, missing-evidence behavior, practical mitigation conditions, coverage and repetition against the actual saved context. Compare supported facts and selected reference sets with full hybrid before attributing any effect to Node2Vec. Preserve all four original runs and document development findings separately from human ratings and final held-out scores. Consider generator changes only after the matching comparison is recorded; any changed generator requires new matching runs. Broader extraction, the application and final evaluation remain unfinished.
