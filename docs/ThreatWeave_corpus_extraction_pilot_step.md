# Run the five-report extraction timing pilot

Current checkpoint: v2.6 produced 37 candidates across all ten windows with zero empty results, failures or repairs. [Source review](ThreatWeave_corpus_extraction_pilot_v2_6_development_review.md) supports the development import of 34 and excludes three uncertain/conditional candidates; human verification remains pending. Source and mitigation imports completed. [The expanded development scope](ThreatWeave_expanded_development_scope_checkpoint.md) now passes all 175 offline tests and prepares 95 text chunks from 16 CISA scopes and 58 references. [The next step rebuilds the text index](ThreatWeave_expanded_text_index_step.md). The extractor remains at v2.6; no new extraction run is needed for this step.

For an intentional extraction repeat, keep Ollama running and run `extract_corpus_pilot.py` normally. Do not use `--retry-run` on earlier configurations. Repeats preserve prior records, and their candidates require a separate review before ingestion; the prepared import remains pinned to the reviewed v2.6 run.

## Historical v1 instructions

The remaining text records the original free-text format and its initial offline verification. Its six-entity/four-quote response structure and 116-test checkpoint have been superseded by the current source-selector format described in the repair document.

## Run

Keep Ollama running, then execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

No Neo4j connection, password or additional installation is required. The runner reads the current prepared chunk-run pointer, verifies all saved window records against freshly recomputed source windows and checks frozen source/tokenizer/ATT&CK identity hashes. Gold triples and QA reference answers are not read. It requires the serving `llama3.1:8b` digest to match the verified tokenizer model.

## Candidate output and validation

The new prompt uses short supporting quotes instead of reproducing an entire 500-token window in every relationship. The diagnostic limits are six entities, four relationships and four quotes per window; quotes are at most 240 characters and entity names at most 120 characters. These bounds help control response size under the unchanged 700-token generation limit. They do not guarantee completeness or establish final extraction-recall scores.

Each quote must occur exactly once in the window. The validator computes its half-open character offsets and absolute document offsets, checks typed endpoints and literal endpoint/ID mentions in cited support, and performs the existing source/identity validation. A title or heading alone cannot prove actor use; an explicitly scoped actor table caption can support the row if its exact context is cited. Canonical identity resolution uses the frozen ATT&CK entity catalog; it does not add mitigation relationships or benchmark labels to extracted output.

Every candidate remains pending semantic review, regardless of confidence. Literal source matches and valid identities do not establish that the source actually asserts the generated relationship. Source uncertainty wording is flagged for review. Empty extraction is allowed when no relation is supported. Do not treat an empty result as an execution failure or automatically accept every source-matched candidate.

The runner allows one schema/source repair, then saves failures without silently completing partial output. A response reaching the output-token limit receives a fresh repair using the original evidence; incomplete text remains saved but is not copied into that repair prompt. Model/service errors and invalid outputs are recorded separately.

## Timing, duplicate handling and records

Each attempt records elapsed time, model token counts, completion reason, raw response and available Ollama duration. Per-window timing includes prompt preflight, generation, validation and local record writes. Initialization is excluded. Total run time includes the availability check and sequential extraction/validation. No warmup or benchmark averaging is claimed.

Candidates are aggregated by document and typed resolved identities, retaining all source supports and their originating windows. The summary separates raw relations, unique document candidate facts, repeated relations and exact duplicate source supports. Repeated statements with different quotes remain traceable; duplicate counts alone do not prove overlap recall. Raw per-window results are preserved.

Source/model/prompt keys are recorded for reproducibility. This initial timing run does not replay cached generated responses. Fresh timestamped records go into `S:\ThreatWeave\work\corpus_extraction_pilot`; the readable candidate/source review is saved directly in `S:\ThreatWeave\docs`. No graph writes occur.

Graph-write rate, index-build time and broader resource measurements still need later pilot stages. This is a bounded ten-window diagnostic pilot, not full 15-report extraction, extraction F1, final benchmark evaluation or proof of a general model advantage.

## Offline verification

All 116 offline unit tests passed. The actual ten-window preview passed saved-chunk/source/tokenizer/catalog checks and estimated context-budget checks. Its requests contain 1798–1845 estimated prompt/schema tokens, plus the 700-token output allowance and 256 reserved chat tokens within context 8192. Live extraction outcomes remain pending.

If individual windows fail, a later failed-case retry can use `--retry-run` with the saved extraction-pilot directory. The retry validates unchanged prepared-source identity and extraction settings, selects only recorded failed windows and saves a new linked run. A failure before any windows start requires a fresh run. Original failures are preserved.
