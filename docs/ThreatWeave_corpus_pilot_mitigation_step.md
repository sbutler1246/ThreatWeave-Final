# Add direct mitigation references to the corpus pilot

October 14, 2026. The [completed source import](ThreatWeave_corpus_pilot_graph_checkpoint.md) verified 34 extracted assertions across ten windows in 3.239 seconds, including verification. Three uncertain/conditional candidates remain excluded. Human review remains pending.

Completed checkpoint: mitigation run `20261015T041247Z-529903c7` verified 55 references, 72 source-reference combinations and six three-hop chains in 3.314 seconds, including verification. [The expanded scope is prepared](ThreatWeave_expanded_development_scope_checkpoint.md); [the next step rebuilds the text index](ThreatWeave_expanded_text_index_step.md). The command and original pre-import details below are retained for reference or an intentional repeat.

The next import prepares 55 direct ATT&CK 17.1 reference assertions for 15 imported techniques, involving 27 target mitigation entities. T1018, T1069.002 and T1217 have no active direct associations in the frozen snapshot and remain explicitly uncovered. References retain `origin=fused`; they do not imply incident-specific effectiveness or import parent-technique mitigations.

## Run

Keep the ThreatWeave Neo4j database running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\import_corpus_pilot_mitigations.py"
```

Press Enter for URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, then enter the password when prompted. The password is not saved. Ollama is not required.

Expected verification: **55 direct reference assertions**, **72 source-reference combinations** and **six same-window three-hop chains**. Counts include reused graph records. The transaction checks the imported reviewed source assertions and source/reference evidence, preserves existing review decisions and rolls back on missing/conflicting records or incomplete path verification. The fixed source-import receipt and pinned review prevent automatic substitution of a different extraction run.

Prepared records, an import receipt and measured transaction time save under `work/corpus_pilot_mitigations/<run>`. The readable reference preview saves directly in `docs`. The original 167-test/pre-import [preview](ThreatWeave_corpus_pilot_mitigations_20261015T040857Z-ae3d4c5a.md) passed; the completed receipt is recorded above. The expanded scope now passes all 175 offline tests.

An offline preview is available with `--preview`; it makes no database connection. After a successful receipt, expand matching source scope profiles and text/graph indexes before running the broader four-mode QA checks. This import alone does not change existing retrieval filters or complete full-corpus extraction/evaluation.
