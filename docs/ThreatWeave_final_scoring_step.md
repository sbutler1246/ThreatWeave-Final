# Score the preserved final answer cohort

**Completed:** `work/final_scoring_runs/20261016T055210Z-1b048137` contains all 720 terminal metric slots: 639 numeric scores, 36 judge-output-limit failures and 45 slots unavailable from original answer failures. Offline artifact and formula checks passed; the original outcomes remain fixed. Automatic paired analysis is saved. Proceed to [the browser-based human answer review](ThreatWeave_human_answer_review_step.md). Do not rerun this completed scoring cohort.

October 16, 2026 (America/Chicago). The operator's local evaluator probe completed at `work/evaluation_probe_runs/20261016T054257Z-ff74edd0`. Offline audit verified its saved file hashes, unchanged policy and synthetic input, all six completed judge requests/replies, matching pre/post model identity, and finite results for all three metrics. These synthetic results establish integration; they are not benchmark scores or evidence of system quality.

The scoring batch is prepared and its offline preview passed. It uses the existing 240 final observations from `work/final_evaluation_runs/20261016T050129Z-f6328cdf`, preserving the 210 valid answers, fifteen graph-only abstentions and fifteen generation failures. The collection, retrieval, prompts, indexes and source labels remain unchanged.

## Next operator command

With **Ollama running**, execute this one command:

```powershell
& "S:\ThreatWeave\.venv-eval\Scripts\python.exe" "S:\ThreatWeave\score_final_evaluation.py"
```

Neo4j is not needed. The batch loads the cached evaluator embeddings once, reads already saved questions/answers/context, and calls the local judge to produce metrics. It does not generate replacement benchmark answers. This is one normal operator launch for the whole cohort; interruptions may require a resume launch. Expect substantially more work than the six-request probe. Do not close the terminal while it is running. Progress prints after input checking and initialization, then once per metric task.

Return the final `FINAL SCORING` line and saved-run path. A completed run can include evaluator failures and undefined metrics; those are valid recorded outcomes requiring analysis, rather than reasons to rerun for better scores.

## Population and fixed scoring policy

There are **720 metric slots**: 240 original observations times three metrics. The **225 available responses**, including fifteen abstentions, have **675 eligible checks**. The fifteen original generation failures contribute **45 explicitly unavailable checks**, with null values and no judge call. Under this declared complete-response scoring cohort, all three metrics, including context recall, are unavailable for those failed-answer cases. No placeholder answer is supplied, and no unavailable value is replaced with zero or a perfect score. Every per-mode/metric denominator remains sixty original observations.

The metrics are faithfulness, answer relevancy and context recall. RAGAS emits `answer_relevancy` for the design's `ResponseRelevancy` class. Inputs preserve the exact displayed response, question, human-verified reference, and full original supplied evidence string containing source passages plus graph-node/path text. References enter only the evaluator. The same-model judge is supplementary and can share generator biases; human factuality/completeness/coherence ratings remain necessary.

The judge adapters, temperature0, seed42, context8192, output700, model digest, cached MiniLM revision, normalized CPU embeddings, native metric prompts/scoring formulas and parsing-repair behavior match the passed probe. Metric checks run sequentially, with judge requests serialized. Each metric is limited to 180 seconds and thirty judge requests; HTTP calls retain the sixty-second timeout and single transport attempt. Native RAGAS JSON-format repairs are recorded. Simple supported answers ordinarily use two faithfulness calls, three relevance calls and one recall call, giving roughly 1,350 judge requests before repairs or early exits. Complex outputs, truncation and unavailable metric results can change that count substantially. The conservative output budget is retained even if some judge replies fail; no settings will be tuned for better final scores.

The scoring order is a seed42 shuffle of the 240 observations, followed by the three fixed metric tasks for each observation. The metric sampler is separate from the original collection order. All models/adapters are initialized before metric timing. Metric elapsed time includes identity checks and scoring/error handling; it is evaluator overhead, not the original answer latency.

Prepared inputs: `work/final_scoring_inputs/20261016T055004Z-f1396885`. Scoring-plan fingerprint: `940b1fafe330feb9f254f0c134ca1c48864ed7c83f4bd78992406bd025148a90`. The plan binds 3,182 source/probe/implementation files in addition to the original frozen-plan and cached-weight guards. `samples.json` contains all 240 observations, including null responses for the fifteen original failures; `plan.json` contains all 720 task IDs and eligibility flags. Final inputs and the passed probe were rechecked against original saved question/answer/context/reference bindings without model or service calls.

## Saved results and interruption recovery

Every run is written to a new `work/final_scoring_runs/<run>` folder. It preserves the plan, initialization/final model tags, common evaluator log, summary and one folder per attempted metric. Each metric folder contains its exact input, pre/post model tags where eligible, judge request parameters and structured responses or exceptions, result, receipt and attachment hashes. Results distinguish `scored`, `undefined`, `failed` and `unavailable_answer`, with null values for the last three statuses. The summary reports coverage by mode and metric while keeping human review pending.

Only unstarted or interrupted metric tasks may be resumed. Completed scores, undefined values, evaluator failures and unavailable-answer slots remain terminal and are never regenerated. If interrupted, preserve the printed run folder and use the same command with `--resume-run` followed by that folder. The next process audits the linked plans, exact inputs, receipts and file hashes, creates a new folder and skips every terminal metric. Interrupted files remain in the earlier run. No full rerun is needed and no outputs are overwritten. An identity/integrity failure stops the batch and blocks automatic resume pending explicit audit.

The runner also cancels and drains remaining asynchronous subrequests after a metric fails, before changing the shared recording folder. This prevents an unfinished relevance request from appearing under a later task. Model identity is checked around every eligible metric; frozen files and cached policy are checked at entry and completion, and implementation files are checked between tasks.

Eight offline runner checks passed: full denominator/coverage accounting; distinct missing/failure/undefined values; interruption recovery preserving terminal errors; completed-run resume without model initialization; result-tamper rejection; resume-boundary/cycle rejection; identity-change rejection and blocked resume; missing-answer slots without model initialization; and cancellation of leftover subrequests. The simulated tests make no live model or embedding calls. Their initial Windows sandbox event-loop startup stalled; the same offline tests completed successfully outside that restricted test environment. The full scoring-input preview also passed with zero previous terminal checks.

After this operator batch, extraction precision/recall/F1 scoring, human ratings, paired question-level comparisons, planned bootstrap intervals and final reporting remain. Automatic scores must include their availability/error coverage and cannot alone establish superiority of any method.
