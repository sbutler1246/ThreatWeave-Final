# Import direct mitigation references for the three-report extension

Completed update: operator run `20261016T002000Z-fd9e2fc1` imported or verified all 48 references and verified 53 source-reference combinations and three same-window three-hop chains. Its saved records and completed receipt passed offline reconstruction. [The accepted retrieval scope is expanded](ThreatWeave_corpus_extension_scope_checkpoint.md); [the next operator step builds the matching text index](ThreatWeave_corpus_extension_text_index_step.md). The instructions below describe the completed mitigation-import stage.

October 15, 2026. The operator source import completed in `work/corpus_extension_ingestion/20261016T001729Z-60fdb691`. Offline reconstruction matches its saved records and completed receipt: 27 verified assertions across twelve windows, 27 target entities, 23 distinct factual relationships and nineteen excluded candidates. Its transaction took 1.009 seconds including verification. Counts include reused records; the timing is one processing observation, not a benchmark average. Human verification remains pending.

With Neo4j running, execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\import_corpus_extension_mitigations.py"
```

Accept the local connection defaults if appropriate and enter the password with hidden typing. No Ollama generation or new installation is needed. Return the completion output and saved-records path. The operator performs the live transaction.

Offline preview passed: `work/corpus_extension_mitigations/20261016T001819Z-cc101b72/prepared_records.json`. [The readable reference preview](ThreatWeave_corpus_extension_mitigations_20261016T001819Z-cc101b72.md) contains every exact frozen reference description. This preview is not a completed import receipt.

The plan covers fifteen accepted source techniques. Thirteen have 48 direct Enterprise ATT&CK 17.1 reference assertions targeting 26 distinct mitigation entities. T1057 and T1082 have no active direct mitigation associations in this frozen snapshot; no parent inheritance is inferred. The source-supported plan contains 53 source-reference combinations and three same-window actor-to-software-to-technique-to-mitigation chains. These target counts include reused records and do not imply newly created records, incident-specific effectiveness or quality scores.

Preparation reconstructs the supported source selection and verifies every stable saved source-record field and its completed receipt before connecting. Reference selection reads only the frozen ATT&CK snapshot, not gold triples or QA answers. The transaction verifies source assertions and their factual edges, imports references with origin=fused while preserving human-review states, then verifies every reference edge, source-reference pair and same-window chain. Missing, changed or rejected source/reference evidence and incomplete paths fail the transaction. Repeating a successful import reuses stable assertion identities.

The assistant has only generated previews and used simulated transactions; no live database or model service was called. After the operator mitigation import, its saved receipt must be verified before the extension enters the accepted retrieval scope. Scope expansion and operator-run text/graph index refreshes are still pending. Current application indexes remain the preceding 41-window/96-reference development snapshot. Human review, missing-fact coverage assessment and controlled held-out quality/performance evaluation remain unfinished.

All 25 distinct targeted offline checks passed: nine extension mitigation checks, eight additional-batch regressions and eight original-pilot regressions. They cover source receipt/record tampering, direct frozen reference direction/text, missing or rejected source assertions, missing edges/incomplete paths, repeated imports, human-review preservation and preview without loading the database driver. The actual extension mitigation entrypoint's `--preview` also passed. `git diff --check` passed.
