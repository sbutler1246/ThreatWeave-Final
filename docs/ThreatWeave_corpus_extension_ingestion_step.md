# Import supported three-report extension assertions

Completed update: operator run `20261016T001729Z-60fdb691` imported or verified all 27 assertions across twelve windows. Its saved prepared records and completed receipt passed offline reconstruction. [The direct mitigation import is prepared next](ThreatWeave_corpus_extension_mitigation_step.md). The instructions below describe the completed source-import stage.

October 15, 2026. The operator extraction completed in `work/corpus_extension_extraction/20261016T000937Z-0cef6551`: 16 windows with candidates, 16 empty outputs and one validation failure across 33 windows. Original successful outputs contained 43 relation occurrences and 39 unique document candidate facts. Processing took 76.50 seconds, including service availability and sequential extraction/validation; this is one run observation, not an average or quality score.

Window 08 repeated the same actor-to-Mimikatz link using two supports, including in its one repair attempt. The existing offline duplicate-only derivation retains the first support, records removal of the later selection and revalidates three relations. Its original failure and model outputs remain unchanged. No new generation was needed.

All 33 windows were revalidated into separate artifacts at `work/corpus_extension_review_checks/20261016T001318Z-ae84a38a`. There are now seventeen revalidated candidate windows and sixteen empty windows. These contain 46 relation occurrences, 41 unique document candidate facts, five repeated occurrences and no exact repeated source supports. [AI-assisted source review](ThreatWeave_corpus_extension_source_review.md) selected 27 Supported, held nine for Review and rejected ten. Human verification remains pending. Per-candidate decisions and attachment checksums are in `docs/ThreatWeave_corpus_extension_source_review.json`.

With Neo4j running, execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\ingest_corpus_extension.py"
```

Accept the local connection defaults if appropriate, then enter the password with hidden typing. No Ollama generation or installation is needed. Share `IMPORT COMPLETE` and the saved-records path. The operator performs the database transaction.

The verified offline preview is `work/corpus_extension_ingestion/20261016T001509Z-93d5efb1/prepared_records.json`. [The readable preview](ThreatWeave_three-report_extension_import_20261016T001509Z-93d5efb1.md) lists every selected assertion and exclusion. It targets 27 assertions across 12 source windows, 27 distinct entities and 23 distinct factual relationships. Counts include reused records and are not counts of newly created graph records. Two Supported assertions from the recovered window are selected; its third candidate, which confuses systeminfo with a deleted systeminfo.dat output file, is rejected.

Exclusions cover NTDS.dit typed as software, LOTL treated as a named software entity, systeminfo.dat confused with the systeminfo executable, a downloaded DLL or spawned tool assigned the initiating action, taxonomy inferred from incident annotation co-occurrence, uncertain or possible tool use, an attempted use, a disjunctive payload description, and ambiguous mapping of broad source behavior to more specific ATT&CK techniques. Observed ronf.exe compression remains Supported because likely qualifies only its possible rar.exe identity; that alias is not invented. Original observations and source annotations remain intact.

Before connecting, preparation reconstructs the frozen sources, prepared windows, exact prompts/schema/source choices and model configuration. It verifies every source-review disposition, original raw response, separately derived candidate, exact evidence alignment and the recorded offline validation implementation. It selects only Supported candidates. Original-vs-derived provenance includes the original failed status, exact raw-file checksum, normalized raw-output hash, offline receipt checksum and recorded duplicate-removal transformation.

The transaction checks existing identities and frozen records, preserves existing human-review status, merges source assertions and factual edges, and verifies every selected assertion/edge. Conflicts or incomplete verification cause rollback. Stable assertion identities make a repeated successful import reuse existing records. Artifacts save under `work/corpus_extension_ingestion/<run>` with a completed `import_receipt.json`; the saved preview is not an import receipt.

After source import, direct ATT&CK mitigation coverage and accepted retrieval scope expansion still need preparation, followed by operator-run index refreshes. Current application indexes remain the preceding 41-window/96-reference development snapshot. No extension mitigation/scope expansion has been implemented yet.

All 25 distinct targeted offline checks passed: eight new extension-ingestion checks, six original additional-batch ingestion regressions, eight original pilot-ingestion regressions and three duplicate-recovery checks. They cover exact selected source/mention spans, recovery provenance, exclusion decisions, missing review dispositions, raw/derived/policy tampering, simulated transaction verification/rollback and preview without loading a database driver. The actual extension import entrypoint's `--preview` also passed without connecting. `git diff --check` passed.

Sixteen empty results are not negative labels or proof of absent source facts. The frozen selector supplied no selectable relation patterns in sixteen windows. Recognition, table/command coverage, source qualifiers and the four-relation limit remain coverage assessment items. All eight eligible development reports now have their prepared technical sections attempted (87 windows across the original and extension selections); this does not establish exhaustive extraction or complete processing of the fifteen-report corpus. Held-out reports remain excluded from development expansion. Human verification and controlled final quality/performance evaluation remain pending.
