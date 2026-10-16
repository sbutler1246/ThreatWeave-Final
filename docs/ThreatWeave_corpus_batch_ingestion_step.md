# Import the supported additional development candidates

Update: the operator import completed in `work/corpus_batch_ingestion/20261015T173114Z-643927a9`; its prepared records and receipt passed offline reconstruction. Continue with [the direct mitigation import](ThreatWeave_corpus_batch_mitigation_step.md). The source-import command below is retained as historical procedure.

October 15, 2026. The additional 44-window extraction batch is reviewed for development use. Human verification remains pending. The prepared import selects 53 supported assertions across 25 source windows, targeting 52 distinct entities. These counts include reused records; they do not count only newly created graph records.

Keep Neo4j running, then execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\ingest_corpus_batch.py"
```

Accept the displayed local connection defaults if those match your database, then enter your Neo4j password when prompted. Password typing is hidden. No Ollama query or additional installation is needed. Share the `IMPORT COMPLETE` output and saved-records path after completion.

The runner verifies frozen source windows, original prompts, schema/source choices, original raw outputs, the recorded offline validation policy, derived selector changes, source-review attachments and every candidate disposition before connecting. It imports only the Supported decisions from `docs/ThreatWeave_corpus_batch_source_review.json`. Ten Review and five Reject candidates are excluded; eighteen empty model results add no facts. The original failed generations remain labeled as failures in their original run. Imported recovered candidates explicitly retain their generation status, original file checksum, normalized-response hash, offline validation receipt and duplicate-removal provenance.

The transaction checks existing frozen identities and source records, preserves human review status, merges assertions and factual edges, and verifies every selected assertion is attached to its corresponding edge. Conflicting existing records or incomplete verification cause rollback. Repeating a successful import reuses stable assertion identities. Existing snapshots, review records and generated answers are preserved. The operator executes the live database transaction; the assistant has only prepared records and used simulated transactions in tests.

After the source import, direct ATT&CK mitigation coverage and the accepted development retrieval scope still need expansion, followed by refreshed text/graph indexes. The current application's indexes do not automatically include this batch. Human verification, wider corpus work and controlled final evaluation remain pending.

## Extraction and review checkpoint

Original extraction: `work/corpus_extraction_batch/20261015T170956Z-255671f4`.

It processed all 44 selected windows in 83.24 seconds: 24 windows with candidates, 18 empty outputs and two validation failures. Successful outputs contained 61 candidate relations. Each failed case used both permitted attempts; there were no HTTP service failures. These are processing measurements, not quality scores or benchmark timing averages.

The Rhysida failure selected the same actor-to-net link twice with different supporting sentences. A separate offline derivation keeps the first support and removes the duplicate, retaining three candidates and recording the removed selection. The Phobos failure exposed a validator bug: an unrelated sentence mentioning affiliates caused the explicit Phobos actors subject in other evidence to be rejected. The corrected check detects a removed affiliates suffix in the actor's own supporting passage. It still rejects shortened affiliate names and preserves explicit table-caption checks. Revalidating the unchanged Phobos output yields four candidates. No further model generation was needed; the original error summaries and raw outputs are untouched.

Offline revalidation records: `work/corpus_batch_review_checks/20261015T171411Z-af0377d1`. All 44 frozen windows were revalidated, yielding 68 candidate relation occurrences and 59 unique document candidate facts. There are nine repeated occurrences across windows, including four exact repeated source supports; supports remain traceable. Source review selected 53 Supported, held ten for Review, and rejected five. Exclusions cover uncertainty/conditions, questionable source ATT&CK annotations, protocol-versus-software role errors, a batch-script-versus-payload subject error and an unsupported taxonomy relation inferred from co-occurring tactic IDs.

Review: `docs/ThreatWeave_corpus_batch_source_review.md`; per-candidate dispositions and checksums: `docs/ThreatWeave_corpus_batch_source_review.json`. These are AI-assisted development decisions, not human verification or gold labels. Empty outputs, source-selector limits, table coverage and the four-relation cap still require coverage assessment. Full fifteen-report extraction and final benchmark evaluation are not complete.

Verified import preview: `work/corpus_batch_ingestion/20261015T171828Z-f9eab0ca/prepared_records.json`; readable preview: `docs/ThreatWeave_corpus_batch_import_20261015T171828Z-f9eab0ca.md`. Preview did not connect to a database.

Across the corpus, source-selector and development-validator checks, 100 distinct offline tests passed after fixes. This includes source-boundary/qualifier checks, duplicate normalization without editing raw output, original-pilot/import regressions, exact batch selection/provenance, artifact tamper detection, simulated atomic transaction verification and preview without loading the database driver. No live database connection was used for these checks.
