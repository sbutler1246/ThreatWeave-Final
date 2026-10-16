# Import the reviewed held-out source assertions

The source import has completed and its saved payload/receipt passed offline reconstruction. Continue with [the direct evaluation mitigation import](ThreatWeave_evaluation_corpus_mitigation_step.md). The source-import instructions below remain the historical preparation record.

October 15, 2026 (America/Chicago). Extraction and bounded retry have finished. No further extraction run is needed for this checkpoint. With Neo4j running, execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\ingest_evaluation_corpus.py"
```

Enter the same Neo4j URI, username and database used for the earlier imports, then the password at the hidden prompt. Ollama is not needed. This is one operator execution with an atomic transaction and verification of every selected assertion. Return the final `IMPORT COMPLETE` output and saved-records path. The assistant has run only offline reconstruction, tests with simulated services, and an import preview.

The source review selects 118 Supported assertion occurrences across 48 source windows and 91 target entities, representing 99 distinct directed entity facts. Counts include reused entities and facts. Twenty-four candidates are held for review and 54 are rejected; human verification remains pending. Every original and derived prediction remains available for scoring.

| Frozen source report | Supported assertion occurrences |
| --- | ---: |
| AA23-165A | 6 |
| AA23-061A | 11 |
| AA24-131A | 18 |
| AA24-109A | 45 |
| AA25-071A | 26 |
| AA23-352A | 8 |
| AA23-075A | 4 |
| Total | 118 |

The initial run `work/evaluation_corpus_extraction/20261016T041122Z-a67a194f` attempted 114 windows: sixty produced validated candidates, 49 were empty, four failed duplicate-relationship validation and one had an Ollama HTTP 500 connection failure. The bounded retry `20261016T041738Z-f6bd403c` recovered the connection-failure window with four candidates; the four duplicate failures persisted. Initial and retry execution times were 220.10 and 23.86 seconds, with 123 and nine recorded generation attempts respectively. Availability checks and source preparation are outside those generation-attempt counts; preparation is outside the reported run times.

Offline reconstruction uses the pre-existing first-support duplicate-removal procedure from development, with no model calls or new extraction rules. The four original failures yield nine derived relation occurrences. Their initial run's final allowed outputs are used; retry outputs are preserved rather than searched for more favorable candidates. Earliest validated successes are retained, including all 49 empty results. The review packet contains 196 candidates across 65 nonempty windows, 161 unique document facts, 35 repeated relation occurrences and seven exact support duplicates. These are candidate counts, not precision/recall or final benchmark scores.

Current verified review artifacts: `work/evaluation_corpus_review_checks/20261016T042430Z-c7db26d2`. The earlier packet remains preserved as a superseded reconstruction checkpoint. [The source review](ThreatWeave_evaluation_corpus_source_review.md) records every disposition; [its machine-readable manifest](ThreatWeave_evaluation_corpus_source_review.json) binds the frozen plan, original raw-file hashes, all derived artifacts and the validation receipt. The receipt inventories both original runs, including unsuccessful attempts and the service failure. Reconstruction also checks saved per-run aggregates, all prompts, schemas, source choices, metadata, complete replies and evidence alignment.

Review exclusions include table headings and hash-column labels classified as software, protocol names classified as software, affected products confused with attacker tools, credential stores confused with tools, actor actions assigned to ransomware software, and technique IDs attached to the wrong tool. Conditional actions and ambiguous table/actor identities remain excluded pending human review. An uncertainty flag alone does not decide a claim: Medusa's observed remote-access-tool use and Play's valid-account abuse remain Supported because surrounding uncertainty modifies a different assertion. No endpoint, source passage, prompt, model setting or label was corrected.

The new importer reconstructs the entire linked history and rechecks the pinned review before selecting Supported assertions. It records `scope_assignment=evaluation`, the frozen evaluation-plan fingerprint, review reasons and hashes, original generation status, original raw-file hashes and explicit duplicate transformations. Source window IDs use `:evaluation:`. It uses the existing atomic writer, preserves prior human-review status and rejects conflicting identities or a verification shortfall. Shared source/entity identities may be reused in Neo4j; evaluation assertions remain explicitly scoped, and subsequent retrieval must use its own pinned assertion/source allowlist. The development indexes and graph pointer are not rebuilt by this action.

No gold triples, reference answers or benchmark question text enter this review/import pipeline. Extraction scoring must retain initial-pass, retry and derived observations separately and include rejected candidates and missing/empty coverage; it must not evaluate only the 118 graph-accepted assertions. The final shared evaluation scope/indexes, direct ATT&CK mitigation import, 240-answer experiment, metric integration, blinded human scoring and analysis remain pending.

All 23 targeted offline checks passed: twelve new lineage/import checks and eleven existing duplicate-review/import checks. They cover frozen selection, service/label isolation, preservation of empty outputs and failed generations, earliest-result selection, cycle/boundary rejection, exact source and mention spans, explicit evaluation provenance, artifact/code tampering, complete dispositions, mocked atomic verification and a preview without the database driver. The offline import preview passed. No live import has been run by the assistant.
