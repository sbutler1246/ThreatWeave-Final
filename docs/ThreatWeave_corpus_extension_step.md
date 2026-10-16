# Extract the remaining three development reports

Completed checkpoint: operator run `20261016T000937Z-0cef6551` processed all 33 windows. One duplicate-selection failure was recovered offline with original artifacts preserved. [Source review and the prepared import](ThreatWeave_corpus_extension_ingestion_step.md) select 27 Supported assertions and exclude nineteen pending/rejected candidates. Continue with that import; another extraction run is not needed. The instructions below describe the completed extraction stage.

October 15, 2026. Source-only preparation and offline preflight passed for the three remaining eligible development reports. Seven reports containing held-out evidence and all 54 previously prepared windows are excluded. Frozen sources, split assignments, prompts, source-selector implementation, model digest and generation settings are preserved. Gold triples and QA reference answers are not inputs.

With Ollama running, execute in a separate PowerShell terminal:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_extension.py"
```

No Neo4j connection or new installation is needed. The existing application may stay open. Wait for `BATCH PROCESSED`, then share the completion output and saved-results path. The operator runs the live extraction; the assistant has prepared sources and used simulated service responses in tests.

| Report | Source windows | Measured source tokens | Estimated prompt/schema tokens |
| --- | ---: | --- | --- |
| AA24-038A — Volt Typhoon / PRC actors | 19 | 408–540 | 1303–3236 |
| AA23-144A — Volt Typhoon / living off the land | 9 | 486–513 | 1417–1848 |
| AA22-321A — Hive | 5 | 486–522 | 1523–2147 |
| Total | 33 | 408–540 | 1303–3236 |

Preparation: `work/corpus_extension_chunks/20261016T000636Z-0bff476b`. The folder uses UTC naming; preparation occurred on October 15 in America/Chicago. Exact windows are in `chunks.json`, per-window prompt checks in `preflight.json`, and source/plan identities in `summary.json`. [The readable preparation report](ThreatWeave_corpus_extension_preparation_20261016T000636Z-0bff476b.md) records every scope. This is source preparation, not a live extraction run.

Plan fingerprint: `4a78a36d24a4195b85256c120b8d5163af46c722041114165d1fe823558c8960`.

Every window fits the unchanged 8192-token context with 700 output tokens and 256 reserved chat tokens. These are preflight estimates; actual formatted-prompt counts will come from the operator run. The runner verifies the serving Llama 3.1:8b digest before generation. Temperature remains zero; at most four relations and three supporting source units per relation are allowed, with one schema/source repair. This remains bounded diagnostic extraction.

Two windows have no recognized source mentions. Sixteen windows, including those two, have no selectable typed relation patterns under the frozen source selector. Such windows cannot yield a relation through the current constrained menu. They remain in the declared batch; empty results do not establish that the source contains no facts. Actor/pronoun recognition, commands, tables, conditional statements and the four-relation cap remain coverage limitations. This run will not establish exhaustive extraction or whole-corpus completion.

Fresh run records save under `work/corpus_extension_extraction/<run>`, with readable reports directly in `docs`. They preserve original raw generations, prompts, source choices, schemas, exact evidence alignment, identities, attempts, failures and timing. No candidates are imported automatically, and current application indexes are unaffected.

If interrupted or a window fails, use `--resume-run` with the latest printed extension-run folder. Resume verifies the prepared source/plan/configuration and linked saved results, skips previously completed candidate and empty windows, and retries only incomplete/failed windows in a new folder. The extension runner accepts only extension resume folders; original pilot and additional-batch records remain separate. A resume may process fewer than 33 windows. All linked artifacts must be included in subsequent source review.

All 33 targeted offline checks passed: nine extension preparation/runner checks, eight original additional-batch selection/resume regressions, eleven original pilot checks and five source-chunking checks. They cover exact technical-section coverage and inherited contexts, held-out/previous-window exclusion, source/plan/prompt tampering, frozen settings, output isolation, failures/resume and preserved empty results. Service replies were mocked. Both preparation preview and the actual extraction entrypoint's `--preview` passed without service calls; `git diff --check` passed.

After extraction, source review and any explicit offline validation recovery must precede further imports, mitigation coverage, scope expansion and index refreshes. Human verification, missing-fact coverage review and final held-out quality/performance evaluation remain pending.
