# Extraction pilot v2 HTTP rejection and schema repair

Later checkpoint: v2.1 completed all 20 live requests with HTTP 200, but produced five empty repairs, five validation failures and zero source-checked candidates. See [the live review and current v2.2 repair](ThreatWeave_corpus_extraction_pilot_v2_1_development_review.md). The remainder preserves the HTTP-repair checkpoint.

October 14, 2026. Current implementation: `five-report-extraction-pilot-v2.1-source-selectors`.

## Observed live outcome

Run `work/corpus_extraction_pilot/20261014T073408Z-3e19e1ec` used the v2 source selectors, verified model digest and the original ten prepared windows. All ten generation requests returned HTTP 400 on their first attempt. The run finished in 6.341 seconds, including the availability check; the first generation request took 3.979 seconds and the others approximately 0.013–0.018 seconds each. These are rejection timings, not extraction throughput.

The saved run contains zero model outputs and zero candidate relationships. Source validation and semantic correctness could not be assessed. Its zero duplicate counts reflect the absence of candidates and provide no overlap finding. No graph writes occurred. The original v1 failures and this v2 rejection run remain preserved.

The existing client raised the HTTP exception before retaining the response body. The readable review therefore contains the HTTP status without the server's reason. The local server log confirms ten HTTP 400 responses at approximately 2:34 a.m. Central, but does not supply the detailed rejection reason.

## Repair and limits of diagnosis

All ten saved schemas contain `context_ids.items.enum: []` because these windows have no permitted actor table captions. This creates an empty selector enumeration even though the intended output is simply `context_ids: []`.

The upstream [llama.cpp schema converter](https://github.com/ggml-org/llama.cpp/blob/master/common/json-schema-to-grammar.cpp) visits array item schemas and converts enumerations to grammar alternatives. An empty enumeration is therefore a plausible grammar-conversion failure. This is an inference from the saved requests and upstream implementation; the original server error body is unavailable, and a corrected live run is still required to confirm the repair on the installed backend.

`extraction/source_choices.py` now requires a zero-length context array when no captions exist, using `maxItems: 0` and a string item type without an empty enumeration. Where captions exist, their exact allowed IDs remain enumerated. If no endpoints or evidence units are selectable, the schema permits only an empty relations array. Runtime endpoint, type, source-unit, caption and identity checks continue to reject unsupported selectors.

`extraction/corpus_pilot.py` now records HTTP status and saves each rejected generation response as `ollama_http_error_<attempt>.txt` inside the new run's window directory. JSON error details also appear in the summary, console and generated review. A service rejection does not trigger a model-output repair. The prompt version is advanced to v2.1, and source implementation/configuration hashes distinguish the changed schema.

## Offline verification

All 127 offline tests passed. Regression checks cover zero-caption arrays, exact caption IDs, sources without selectable endpoints, JSON and non-JSON HTTP error bodies, and preservation of service failures without requesting output repair. Existing source alignment, identity, type, model-digest and truncation-repair tests also pass. Service interactions in these tests use fixtures.

The actual ten-window preview passed the frozen source, tokenizer, catalog and context-budget checks. Estimated system/prompt/schema sizes are 2643–3327 tokens, plus the unchanged 700 output tokens and 256 reserved chat tokens, within context 8192. All ten actual schemas were also checked for nonempty enumerations, schema validity and acceptance of an empty extraction. No live service calls or installers were run during this repair.

Prepared run: `work/corpus_pilot_chunks/20261014T065159Z-c4380457`. Chunk fingerprint: `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`. Source windows, benchmark splits and source-only extraction inputs are unchanged. Gold triples and QA reference answers are not extraction inputs.

## Next live step

Keep Ollama running and execute one fresh run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

Use the normal command rather than `--retry-run`; the schema implementation/configuration differs from both saved failed runs. New logs go under `S:\ThreatWeave\work\corpus_extraction_pilot`, and the generated review saves directly in `S:\ThreatWeave\docs`.

After the user supplies the final output, inspect each candidate against its selected literal evidence and explicit actor scope, then record semantic findings, timing, failures and repeated/overlapping supports. Valid source selectors do not establish semantic correctness. Full-corpus ingestion, refreshed indexes, application integration and final evaluation remain pending.
