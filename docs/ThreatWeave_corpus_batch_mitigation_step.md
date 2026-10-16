# Additional development batch: direct ATT&CK mitigation import

Completed update: operator run `work/corpus_batch_mitigations/20261015T173540Z-9792c14d` imported or verified all 51 references and verified 59 source-reference combinations and four same-window three-hop chains. Its saved records and receipt passed offline reconstruction. [Accepted scope expansion is prepared](ThreatWeave_corpus_batch_scope_checkpoint.md); [the next operator step builds the matching text index](ThreatWeave_corpus_batch_text_index_step.md). The instructions below describe the completed import stage.

October 15, 2026. The operator source import completed in `work/corpus_batch_ingestion/20261015T173114Z-643927a9`. Offline reconstruction matches its saved prepared records and receipt: 53 verified assertions, 25 windows, 52 target entities, 45 distinct factual relationships and 15 excluded candidates. Counts include reused records. Human verification remains pending.

The next operator action, with Neo4j running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\import_corpus_batch_mitigations.py"
```

Accept the local connection defaults if appropriate and enter the password with hidden typing. No Ollama generation or installation is required. Return the completion output and saved-records path.

Offline preview passed: `work/corpus_batch_mitigations/20261015T173345Z-94df8d23/prepared_records.json`. The readable reference descriptions are in `docs/ThreatWeave_corpus_batch_mitigations_20261015T173345Z-94df8d23.md`.

The plan covers 19 accepted techniques. Sixteen have 51 direct frozen Enterprise ATT&CK 17.1 reference assertions targeting 26 distinct mitigation entities. T1012, T1057 and T1070.004 have no active direct mitigation associations in this snapshot. No parent inheritance is inferred. The plan contains 59 source-reference combinations and four same-window three-hop chains. These are target counts, not counts of newly created records or quality scores.

Preparation reconstructs the reviewed source batch and checks all stable prepared-record fields and the completed source receipt before connecting. The transaction verifies imported source assertions and their edges, writes references with origin=fused, preserves human-review status and verifies reference edges and expected paths. Missing, changed or rejected evidence and incomplete paths fail the transaction. Reference descriptions express ATT&CK guidance, not incident-specific effectiveness. Gold triples and QA reference answers are not inputs.

All 24 targeted offline checks passed: eight additional-batch mitigation checks, eight original-pilot mitigation regressions and eight existing development-scope checks. They cover receipt/artifact tampering, exact frozen reference direction/text, missing or rejected source evidence, incomplete edges/paths, repeat imports and human-review preservation using simulated transactions. `git diff --check` passed.

The preview and offline tests use no live service. The mitigation import still requires operator execution. After its receipt is verified, accepted development scope expansion and operator-run text/graph index refreshes remain necessary. Existing application indexes and the original ten-window scope remain unchanged. Broader corpus completion and final evaluation remain pending.
