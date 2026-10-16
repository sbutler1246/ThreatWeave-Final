# Import direct mitigation references for the held-out source assertions

The operator's mitigation import completed, and offline scope reconstruction verified its saved payload/receipt. Continue with [the shared evaluation text index](ThreatWeave_evaluation_text_index_step.md). The instructions below record the completed preparation step.

October 15, 2026 (America/Chicago). The operator's source import completed: 118 extracted assertions across 48 windows, 91 target entities and 99 distinct directed facts; 78 candidates remain excluded. The transaction took 2.029 seconds including verification. These are operational counts, not extraction accuracy or completed human verification.

Saved source import: `work/evaluation_corpus_ingestion/20261016T042742Z-72fb42f8`. Offline preparation reconstructed the current frozen review and compared every imported payload field except its preparation timestamp, checked all receipt counts, and matched the review manifest hash `fe08c2c9059e6fd3069512f40f31b1a75920499bb4dec4a2143d03cdcde3964a`. The audit is saved at `work/evaluation_corpus_import_review_checks/20261016T042958Z-201ad7ae/audit.json`. This verifies saved evidence and the operator's receipt; it does not claim a new assistant-run live database query.

With Neo4j running, execute this one command:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\import_evaluation_corpus_mitigations.py"
```

Use the same connection details as the preceding import and enter the password at the hidden prompt. Ollama is not needed. Return the final `IMPORT COMPLETE`, `VERIFIED` and saved-records lines.

The prepared payload contains 109 direct frozen ATT&CK reference assertions for 29 of the 34 selected techniques, involving 34 mitigation entities. It verifies 203 source-reference combinations. Target counts include references/entities that may already exist from development imports; this is not a count of newly created records. The new output namespace is `work/evaluation_corpus_mitigations/<run>`.

No direct active associations exist in the frozen snapshot for T1016, T1018, T1069.001, T1069.002 or T1083. Those gaps remain explicit; no parent-technique inheritance is substituted. The current accepted evaluation-source subset yields zero same-window actor → software → technique → mitigation chains. The 203 source-technique/reference combinations remain valid paths; no missing three-hop chains are fabricated or repaired by changing predictions.

The preview passed and is preserved at `work/evaluation_corpus_mitigations/20261016T042905Z-0fd20c07`, with its readable report directly in `docs`. All 27 targeted offline mitigation checks passed, including ten evaluation-specific checks and seventeen existing pilot/extension regressions. Checks cover label/service isolation, direct association direction and exact descriptions, explicit coverage gaps, source/receipt binding, evaluation-scope/plan mismatches, simulated atomic verification, repeatability and preservation of human review. Preparation requires explicitly evaluation-scoped assertions with the same frozen evaluation-plan fingerprint, a matching completed source import, and the unchanged ATT&CK 17.1 snapshot. It records the source receipt and prepared-record hashes. The transaction rechecks every source assertion and factual edge before writing references, then verifies the reference assertions/edges and all expected paths before commit. Conflicts, rejected assertions, missing edges or incomplete paths fail verification. Existing human verification is preserved.

These references retain `origin=fused` and their exact STIX relationship IDs and descriptions. They are shared reference associations, not incident observations or evidence that a mitigation was effective in a particular incident. Extracted source assertions retain `scope_assignment=evaluation`. Gold triples, reference answers and benchmark question text are not inputs. Development indexes and the graph pointer are not rebuilt by this action.

After this reference import, the next substantive stage is the pinned shared evaluation scope and matching indexes. The 240-answer experiment, metric integration, blinded human review, statistical analysis and final reporting remain pending. Extraction scoring must retain all generated predictions and exclusions before fusion.
