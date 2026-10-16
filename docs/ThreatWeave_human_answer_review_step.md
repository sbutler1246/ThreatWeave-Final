# Human answer review

October 16, 2026 (America/Chicago). Automatic answer scoring finished and passed offline audit. All 720 metric slots are preserved: 639 numeric scores, 36 evaluator failures at the frozen judge output limit, and 45 unavailable slots caused by fifteen original generation failures. No failed checks were rerun or imputed. Human review is a separate required assessment and remains pending.

## Open the primary form

Open `S:\ThreatWeave\docs\ThreatWeave_primary_answer_review.html` in your browser. From PowerShell:

```powershell
Start-Process "S:\ThreatWeave\docs\ThreatWeave_primary_answer_review.html"
```

This is a local page with no service connections. It displays the fixed eighty repeat-one observations in the prepared blinded order: seventy valid non-abstaining answers, five abstentions and five failures. Method names, execution order and automatic scores are hidden. Evidence structure may reveal the method, so blinding is partial. Source material is evidence, not instructions to the reviewer. The source questions, actual displayed answers, exact supplied evidence and previously verified reference answers are unchanged.

Enter your name and review date. For each entry, rate factuality, completeness and coherence from 1 (poor) to 5 (excellent). The rating guide is available at the top of the form. Read the supplied evidence when checking support and attribution. Citation presence is not proof of factual correctness. Reference answers describe verified expected content, rather than the answer generated in this experiment.

Use N/A with an explanation when a dimension cannot be rated. Failed cases have no valid answer and should remain explicitly unratable; do not invent a replacement answer or rating. For abstentions, rate meaningful dimensions and explain missing requested information. No ratings are prefilled or inferred from automatic scores.

Browser autosave is used when available. Use **Save progress file** before pausing, closing the browser or changing devices; **Restore progress** reloads that file. The completed-export button becomes available only when every entry has three selections, each N/A has an explanation, and reviewer/date metadata are present. Choose **Export completed ratings** when finished. It downloads `ThreatWeave_primary_completed_ratings.json`; provide that file or its saved path in the conversation. The page does not automatically submit anything.

## Secondary review

`S:\ThreatWeave\docs\ThreatWeave_secondary_answer_review.html` contains the twenty fixed secondary entries. Have another reviewer complete it independently, or use it in a later separate session as the planned delayed rescore. Do not copy the primary scores. Select **Independent second reviewer** or **Delayed rescore by original reviewer** so the returned file records which was actually performed. The form requires this selection before completed export. An independent second review must not be claimed if the same person performed both sessions.

Secondary questions were selected with seed42 before human ratings: Q001, Q033, Q044, Q050 and Q058 across all four methods. The secondary IDs have a separate shuffle and do not expose the primary ratings. Completed export downloads `ThreatWeave_secondary_completed_ratings.json`. Preserve both completed exports and the original blank packet/key. Method unblinding and inter-review comparisons come after ratings are fixed.

The forms were checked with offline JavaScript execution against simulated browser elements: initially blank ratings and disabled completion; exact question display; hidden mode/case identifiers; N/A reason requirements; progress persistence/import binding; reviewer metadata; secondary method selection; and completed JSON export. Six statistical/audit unit checks also passed for paired bootstrap direction and deterministic sampling, whole-question exclusion when a repeat is missing, no zero imputation, insufficient-sample handling, frozen JSON extraction, and saved verdict-formula verification. No human scores have been created by these tests.

## Completed machine analysis and remaining work

The current automatic analysis is `work/final_scoring_analysis/20261016T075220Z-1e84d02c`, with a results report at `docs/ThreatWeave_final_scoring_results_20261016T075220Z-1e84d02c.md`. The earlier `20261016T074905Z-4e2e9cbe` analysis is preserved. The current version adds explicit implementation/formula-source hashes and report formatting; numeric outcomes are unchanged.

All 720 saved metric records and their exact input/receipt/hash bindings were audited, along with request settings, response correspondence and model identity. There were 1,326 judge requests. The 414 available faithfulness/context-recall formulas were independently reproduced from their saved verdicts without model calls. No statement/verdict count mismatch was found in the two-reply faithfulness records. Relevance bindings, bounds and native noncommittal behavior were checked; cosine values were not recomputed because that would require embedding inference. All original outputs remain preserved.

All eighteen pairwise metric comparisons use question-level repeat means and 10,000 question-cluster bootstrap draws. Each comparison includes only questions with all three numeric repeats in both methods. Its included/excluded IDs and sample size are explicit; no missingness is assumed random. Intervals are exploratory, not corrected for eighteen comparisons, and may use different question subsets. Conditional means do not by themselves establish overall method superiority or a general Node2Vec benefit. The MODE field, evidence format, same-model judge, small corpus and unmeasured hardware resources remain interpretation limits.

Still required: human primary/secondary ratings and their analysis; source-only extraction precision/recall/F1 against complete annotated scopes before filtering/fusion; and the final combined results/limitations report. Neither human answer ratings nor human verification of imported source assertions should be inferred from successful automatic scoring.
