# Evaluation source-processing and method freeze

October 15, 2026. This checkpoint records decisions before any new held-out source generation. It freezes source processing and prespecifies the experiment method. It does not claim that final evaluation indexes, the QA batch runner or metric integration are already built.

The machine-readable protocol is embedded in `work/evaluation_corpus_chunks/20261016T040604Z-bccf59fb/summary.json` under `identity.protocol`; its digest is bound into the extraction plan. Frozen inputs include the fifteen-report manifest, split metadata, Llama digest, chunk parameters, source-choice implementation, validators, generation/retrieval/embedding code and current development index receipts. No benchmark questions' reference text or gold triples were read by this preparation.

The preserved development snapshot contains 53 CISA windows, 139 reference parents, 305 text chunks and 142 graph vectors covering 245 directed facts. Source-only held-out results will be saved separately. The final evaluation snapshot must bind its own reviewed source/reference selection and resulting index fingerprints before QA execution.

| Prespecified item | Rule |
| --- | --- |
| Final QA assignment | Existing twenty IDs and 8/8/4 category mix from the frozen split |
| Conditions | Text only, graph only, hybrid without Node2Vec, full hybrid |
| Repetition | Three measured repeats: 240 answer runs |
| Warm-up | One per mode, excluded from measured runs |
| Ordering | Record randomization seed 42 and keep question/mode/repeat identities |
| Primary human scoring | Repeat 1 for each question/mode: eighty blinded answers |
| Secondary review | Five questions across four modes, or delayed 25 percent re-score |
| Analysis | Paired question-level comparisons; 10,000 question-cluster bootstrap samples; exploratory 95 percent intervals |
| Extraction scoring | Model predictions before manual review filtering and ATT&CK fusion; retain rejected predictions, failures, empty outputs and uncovered-scope accounting |
| Reference isolation | Gold/reference answers enter scoring only, never extraction/retrieval/generation |
| Error accounting | Preserve failures/undefined values; no mode substitution or fabricated scores |

The exact current generator is retained. Its MODE prompt field is visible to the model, so differences cannot be attributed solely to retrieval; this confound must be stated in the final analysis. The common context packer uses a conservative 3,000 UTF-8 byte cap, below the designed token ceiling. Report its actual policy rather than describe it as a measured 3,000-token context. No prompt, selector, generation, retrieval or embedding tuning will be based on held-out results.

Seven reports are reserved from broader development expansion. AA23-165A also contains an earlier explicitly permitted bounded development table scope; this overlap is recorded in the protocol. Original development/final evidence assignments remain disjoint at their declared annotation scopes. Report-level source overlap is disclosed and does not authorize tuning on final questions or references.

Source review may accept Supported assertions for the graph, with exclusions retained. The extraction assessment must not score only that accepted subset: rejected generated predictions remain predictions, and missing gold facts remain relevant to recall. Any implementation defect found during evaluation needs explicit version/error reporting; it is not a reason to silently edit earlier predictions, labels, prompts or answers.

This checkpoint introduces no live service call, new package installation, gold-based graph construction or final scores. The next operator action is [source extraction of the seven held-out reports](ThreatWeave_evaluation_corpus_step.md).
