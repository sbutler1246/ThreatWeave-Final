# Process the seven held-out source reports with frozen methods

The initial run, bounded retry and source review have completed. Follow [the reviewed evaluation source import](ThreatWeave_evaluation_corpus_ingestion_step.md); do not restart extraction. The instructions below describe the original preparation and initial launch.

October 15, 2026. Development extraction, reviewed source/mitigation imports and matching 305-chunk/142-vector indexes are complete. The next operator batch processes source text from the seven reports reserved from further development tuning. This is source preparation for evaluation, not the 240-answer benchmark or a completed final experiment.

With Ollama running, execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_evaluation_corpus.py"
```

No Neo4j connection or installation is needed. This is one resumable local batch. Return the final `EVALUATION CORPUS PROCESSED` output and saved-results path. The assistant has run only offline previews and tests with simulated services. The operator performs the live model calls.

| Frozen source report | Windows |
| --- | ---: |
| AA23-165A — LockBit | 14 |
| AA23-061A — BlackSuit / Royal snapshot | 25 |
| AA24-131A — Black Basta | 7 |
| AA24-109A — Akira | 21 |
| AA25-071A — Medusa | 15 |
| AA23-352A — Play | 17 |
| AA23-075A — LockBit 3.0 | 15 |
| Total | 114 |

Prepared artifacts: `work/evaluation_corpus_chunks/20261016T040604Z-bccf59fb`. [The readable source/preflight report](ThreatWeave_evaluation_corpus_preparation_20261016T040604Z-bccf59fb.md) lists every scope. The directory uses UTC naming; preparation occurred on October 15 in America/Chicago.

Plan fingerprint: `89764a8af84a83b36f3aa17425775142376c305bddfd9ce07fc7019ded39945b`.

All technical-section spans preserve the frozen normalized sources, exact offsets and inherited contexts. Source windows contain 418–591 measured Llama tokens. Estimated prompt/schema sizes are 1201–5888 tokens; the largest total is 6844 after reserving 700 output and 256 chat tokens within the unchanged 8192-token context. These are estimates; operator runs record actual service counts. Thirteen windows have no recognized mentions, and 44 have no selectable typed relationship patterns under the frozen selector. Empty results are retained and are not negative gold labels.

The runner uses the same source-choice prompt/schema, temperature zero, Llama digest, four-relation bound, one repair and validators as the frozen development extractor. It has a separate output namespace: `work/evaluation_corpus_extraction/<run>`, with readable documents directly in `docs`. Source window IDs use `:evaluation:`; existing development outputs, graphs, pointers and indexes remain intact. There are no automatic graph writes or index changes.

Preparation and execution do not load `gold_triples.json`, `eval_queries.json`, `reference_triples.json` or benchmark review answers. Only source manifests, split IDs, frozen source text, ATT&CK identity metadata and method/settings records are inputs. The prepared summary records the source-processing protocol described in [the freeze checkpoint](ThreatWeave_evaluation_freeze_checkpoint.md). It binds current development assets and core implementation hashes; changed saved sources, prompts, settings, protocol or code block execution until explicitly versioned preparation is regenerated.

If interrupted or a case fails, use `--resume-run` with the latest printed evaluation-corpus run folder. Resume verifies the linked plan, source metadata, prompts, schemas, source choices, complete raw outputs and candidate validation artifacts. It skips successful candidate and empty windows, processes only incomplete/failed cases in a new folder and rejects development-run folders or cycles. Cases 100–114 are supported. Do not rerun an entire successful batch to select better outputs.

Source-only review and any explicitly recorded duplicate normalization follow extraction. They must not change prompts, selectors or settings based on held-out outcomes. Preserve every model prediction and review rejection for extraction scoring before fusion; accepting graph assertions is a separate operation. Scoring must report coverage gaps and failures, including annotated scopes not covered by processing, rather than restricting evaluation to successful or supported windows. No gold-based correction of model predictions is permitted.

All 45 distinct targeted offline checks passed: twelve new evaluation-corpus checks and 33 development extraction/chunking regressions. Checks cover source coverage, held-out selection, label-file/service guards, unchanged development pointer, method/configuration binding, saved artifact tampering, identical generation payloads, model mismatch, truncation repair, interruption/resume, schema tampering and case 100. Both preparation and execution-entrypoint previews passed without service calls. `git diff --check` passed.

The new evaluation-corpus import/review adapters, final shared indexes, resumable 240-answer QA runner, evaluator integration, blinded human review and statistical analysis are not yet complete. Human verification and final reporting remain pending. The existing development app can be restarted separately when needed; no additional development demonstration is required before this source batch.
