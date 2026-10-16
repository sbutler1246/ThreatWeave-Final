# Fresh expanded development QA

Completed: [the expanded four-mode development comparison](ThreatWeave_expanded_four_mode_development_comparison.md) records all four planned runs, 12 non-abstaining answers and zero execution failures. Source reviews preserve unsupported incident claims and other answer limitations; human verification and final evaluation remain pending. No additional run is needed for this checkpoint. Full-hybrid instructions and pending statements below describe the preceding checkpoint.

Both expanded indexes are ready. [The graph checkpoint](ThreatWeave_expanded_graph_index_checkpoint.md) records 75 nodes, 102 accepted directed facts and 75 verified 128-dimensional vectors. [The text checkpoint](ThreatWeave_expanded_text_index_checkpoint.md) records 95 verified 384-dimensional vectors. They share 16 CISA source parents and 58 direct ATT&CK reference parents.

The saved-index full-hybrid preview passed for all three development questions without live service calls. Generated answers remain pending.

## Run the next demonstration

Keep Neo4j and Ollama running, then run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\hybrid_qa.py" --demo
```

Press Enter for URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, then enter the instance password when prompted. Password typing is hidden and the password is not saved. Startup checks both stored indexes; retrieval verifies that the current accepted graph matches the fitted projection.

This runs the full `hybrid` condition: text retrieval, source-supported directed graph paths and Node2Vec neighbor retrieval. It saves results under `work/hybrid_qa` and a review directly in `docs`. Use a fresh demonstration for the changed source pool rather than retrying a historical run.

## Fixed questions and generator

All four modes now share these exact development questions:

1. According to CISA, what information does Raccoon Stealer steal? Explain the supplied ATT&CK mitigations for its web session cookie technique, citing observations and references separately.
2. According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.
3. According to CISA, how do ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration?

Keep generator `development-shared-cited-generator-v2`, model `llama3.1:8b`, temperature zero, context 8192 and output limit 700 unchanged across the matching demonstrations. Each run records the actual model digest; matching comparisons require the same model. Answers use at most eight cited claims with at most 280 characters per claim and four citations per claim, with one repair attempt. No benchmark questions, gold triples or reference answers are inputs to this development demonstration.

## Review and following work

Inspect actual generated claims and their supplied evidence, preserving CISA incident observations separately from ATT&CK reference guidance. Check whether missing evidence leads to a partial answer or abstention. The first two text-only smoke searches returned only reference guidance in their top five hits, so successful processing alone cannot establish complete coverage. Check that ALPHV claims accurately describe the supplied AnyDesk/Mega sync observations without inferring unsupported ordering or intent.

After reviewing this fresh full-hybrid run, collect matching graph-only, text-only and hybrid-without-Node2Vec demonstrations using these same questions, source scope, model and generator settings. Preserve all outputs. Earlier six-scope runs use different evidence/questions and cannot serve as matching expanded baselines. These are development checks; final held-out evaluation and human quality ratings remain separate and unfinished.
