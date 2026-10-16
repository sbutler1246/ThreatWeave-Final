# Final answer collection completed; scoring setup next

**Scoring setup and synthetic integration subsequently completed:** the operator's `work/evaluation_setup_runs/20261016T052704Z-bf84a7f1` records verify the separate environment, dependency consistency and pinned adapter imports. The synthetic evaluator probe also passed and its saved artifacts were audited. Proceed to [the prepared final scoring batch](ThreatWeave_final_scoring_step.md). The setup command below is retained as the completed procedure.

October 16, 2026 (America/Chicago). The operator completed the frozen final answer batch at `work/final_evaluation_runs/20261016T050129Z-f6328cdf`. All **240 measured observations** were attempted, with four excluded warm-ups. The saved terminal outcomes are **210 valid non-abstaining answers, 15 explicit abstentions and 15 failures**. Valid means that the output and citation validators passed; semantic correctness has not yet been graded.

The assistant audited the saved artifacts offline. All sixty frozen experiment files still match the prepared plan. The existing history validator accepted all 244 saved terminal records, including exact answer/evidence correspondence, prompts, transport payloads, responses and attachment hashes. Final live graph verification was recorded by the operator's runner. No answers were regenerated and no new service calls, embeddings or model fitting were performed by the assistant.

Plan fingerprint: `3272f8d91a2137744003fbc9d9cf2994fd4e7cb74903bf523c65940992255abc`.

| Condition | Measured outcomes | Valid answers | Abstentions | Failures | Median case time, all outcomes | Generation requests |
|---|---:|---:|---:|---:|---:|---:|
| Text only | 60 | 54 | 0 | 6 | 3.151 s | 72 |
| Graph only | 60 | 45 | 15 | 0 | 3.576 s | 45 |
| Hybrid without Node2Vec | 60 | 53 | 0 | 7 | 3.084 s | 68 |
| Full hybrid | 60 | 58 | 0 | 2 | 3.657 s | 70 |

There were 255 measured generation requests, including repairs; this is different from 240 question/mode/repeat observations. Empty retrieval does not call generation. The fifteen graph-only abstentions are Q040, Q054, Q055, Q056 and Q057 in every repeat. Each has zero source passages and zero graph paths. These are measured coverage gaps.

All fifteen failures occurred during generation validation after both allowed attempts. Offline replay of the saved validators reproduces **nine repeated-citation-ID errors and six repeated-claim errors**. Both attempts, original errors, repair prompts, exact requests and responses remain saved. The final responses returned HTTP 200 with a completed stop; these failures are not transport errors or output truncation. They remain terminal failures in the primary experiment. No additional repair, normalization or favorable replacement answer is permitted in this cohort.

Failure counts alone do not establish which method answers more accurately. The MODE prompt field and different evidence formats remain confounds. Timings include all outcomes and therefore different amounts of work; abstentions and failed repairs cannot be interpreted as equivalent successful-answer work. Python CPU/RSS sampling was unavailable because psutil was unavailable. Neo4j, Ollama and GPU resource usage was not measured; no resource values should be fabricated.

## Prepared evaluation and human-review files

The current audited packet is `work/final_evaluation_review_checks/20261016T052517Z-4778a10b`. The earlier `20261016T052347Z-3560d56c` packet is preserved; this packet also binds the final setup helper's additional environment-isolation checks.

- `audit.json`: cohort, per-mode timing/status/request counts, individual failure diagnoses, coverage gaps and limitations.
- `outcomes.json`: all 240 observations, preserving failures and abstentions.
- `ragas_inputs.json`: 225 available validated responses, including fifteen abstentions. Each carries the question, unchanged displayed response, verified reference answer and **one context string containing the exact complete generator evidence pack**, including source text, graph nodes and graph paths. No improved or reference-derived context is substituted. Fifteen failed cases have no valid response and remain separately unavailable for automated response scoring. Report metric availability against all 240 outcomes and per mode, including NaNs/errors; do not silently use only favorable cases.
- `primary_review.md` and `primary_ratings.json`: eighty shuffled repeat-one observations, including seventy valid answers, five abstentions and five failures. Factuality, completeness and coherence ratings are blank. Each dimension uses integers 1–5, or null with a reason when not ratable. Failed cases have no valid answer and must retain explicit unratable status. Human ratings have not been performed.
- `secondary_review.md` and `secondary_ratings.json`: twenty observations for independent secondary review, or a delayed rescore if no second reviewer is available. Five questions were selected deterministically with seed42 before ratings: Q001, Q033, Q044, Q050 and Q058; all four conditions are included.
- `unblinding_key.json`: keep this separate from reviewers until ratings are fixed. Packet entries hide mode names, case identifiers and execution order. Graph-shaped evidence may reveal a condition, so blinding is partial.
- `source_files_sha256.json` and `packet_files_sha256.json`: saved source-artifact and blank-packet checksums. Preserve the blank templates and save completed ratings as separate copies, with reviewer identity/date and whether secondary review was independent or delayed. Original benchmark human-verification statuses remain unchanged.

Reference answers enter these evaluator/reviewer files only after collection. They were not supplied to retrieval or answer generation. The same-model automated judge will be supplementary and can share generator biases. It cannot substitute for human ratings.

Seven targeted offline checks passed: deterministic blinded primary/secondary pairing, absence of mode identifiers and fabricated ratings in reviewer entries, retention of failures/abstentions, complete latency denominators and nonfinite rejection, saved failure/repair replay, rejection of changed failed-case payloads, setup preview without installations/services, and rejection of a changed evaluator lock. A temporary-directory permission issue was resolved by keeping test scratch files inside the workspace; all checks then passed. The full actual saved-cohort audit also passed.

## Next operator command

Run this single command:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_evaluation.py"
```

It creates or reuses `S:\ThreatWeave\.venv-eval`, installs the exact hash-locked evaluator packages, checks dependency consistency, verifies pinned versions and imports the required adapters. The application environment is not changed. It requires internet access for package installation and can take several minutes. Detailed installation logs and a receipt are saved under `work/evaluation_setup_runs/<run>`; it prints the saved folder on completion or failure. There are **no model, embedding or Neo4j calls** in this setup. The assistant ran only its offline preview and tested that preview and lock rejection cannot invoke the installer.

Return the `EVALUATOR SETUP` result and saved-records path. Installation is the next operator launch; it does not produce quality scores. Further operator launches depend on live adapter validation, scoring runtime and any errors, so an exact remaining launch count or completion time is not yet established.

Remaining substantive work: validate the locked local evaluator against a separate probe; score the saved final outputs while preserving per-metric failures/NaNs; align source-only extraction outputs to the complete gold annotation scopes and score predictions before review filtering/fusion; obtain primary and secondary human ratings; compute paired question-level summaries and the planned 10,000 question-cluster bootstrap intervals; and write the final limitations and results. No more final-answer collection is needed for this completed cohort.
