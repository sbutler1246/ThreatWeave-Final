# Held-out source extraction: initial run and bounded retry

The bounded retry and offline source review are now complete. Continue with [the reviewed evaluation source import](ThreatWeave_evaluation_corpus_ingestion_step.md). The initial run and retry instructions below remain historical records.

October 15, 2026 (America/Chicago). The operator ran the frozen seven-report source extraction. Original results are preserved at `work/evaluation_corpus_extraction/20261016T041122Z-a67a194f`.

All 114 selected windows were attempted: 60 returned validated candidates, 49 returned empty selections, four failed relationship validation and one encountered an Ollama HTTP 500 connection failure. The run took 220.10 seconds including availability checking and sequential extraction/validation, excluding source preparation. The successful windows contain 183 candidate relation occurrences, 155 unique document candidate facts, 28 repeated relations and five exact source-support duplicates. These counts are not accuracy measurements or accepted graph assertions.

The offline resume preview passed against the unchanged prepared plan `89764a8af84a83b36f3aa17425775142376c305bddfd9ce07fc7019ded39945b`. It reconstructed saved prompts, source choices, schemas, source metadata, raw responses, candidate validation and evidence alignment for all 109 successful windows, including every empty result. It selected only the five failed windows for retry. No live service calls, gold-label reads, graph writes or index changes were performed by the assistant.

| Original case | Report | Failure |
| --- | --- | --- |
| 07 | AA23-165A | Repeated selected relationship after the existing one-repair allowance |
| 54 | AA24-109A | Repeated selected relationship after one repair |
| 64 | AA24-109A | Ollama HTTP 500: model connection forcibly closed |
| 88 | AA23-352A | Repeated selected relationship after one repair |
| 90 | AA23-352A | Repeated selected relationship after one repair |

An immutable inventory of 1,267 original run files, counts and failure records is saved in `work/evaluation_corpus_review_checks/20261016T041650Z-e8bd3aa5/audit.json`. Original failures and both model attempts remain intact. No duplicate normalization or semantic acceptance has yet been performed on this evaluation run.

With Ollama running, the operator's next action is one bounded resume:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_evaluation_corpus.py" --resume-run "S:\ThreatWeave\work\evaluation_corpus_extraction\20261016T041122Z-a67a194f"
```

This processes five windows and writes a new linked folder. Do not restart all 114 windows. Preserve this original initial-pass result as a separate evaluation observation; disclose retry counts, additional latency and any duplicate normalization separately. Do not repeatedly regenerate completed outputs to select better answers. If duplicate validation failures recur, inspect their existing outputs before choosing further action.

Source review, evaluation imports/indexes, the 240-answer experiment, extraction scoring, answer scoring and human ratings remain pending. Model predictions and rejected candidates must remain available for scoring before review filtering and ATT&CK fusion, as recorded in [the freeze checkpoint](ThreatWeave_evaluation_freeze_checkpoint.md).
