# Extraction pilot format repair

Current checkpoint: v2.6 produced 37 candidates across all ten windows with no empty results, failures or repairs. [Source review](ThreatWeave_corpus_extraction_pilot_v2_6_development_review.md) supports the development import of 34 and excludes three uncertain/conditional candidates; human review remains pending. Both the source and 55-reference mitigation imports completed. [The expanded scope is prepared](ThreatWeave_expanded_development_scope_checkpoint.md), with all 175 offline tests and index previews passing. [The next step rebuilds the text index](ThreatWeave_expanded_text_index_step.md). The extractor remains at v2.6. The sections below preserve the v1 diagnosis and original v2 revision checkpoint.

October 14, 2026. Original failed run: `work/corpus_extraction_pilot/20261014T070814Z-199160c3`. Its records and all raw responses remain unchanged.

## Diagnosis

All ten windows failed source validation after one repair each. Ollama answered all 20 requests; this was not a connection, model-path or chunk-preparation failure. Total run time was approximately 162.45 seconds.

The v1 free-text format proved unreliable. Outputs renamed source actors using document titles, populated ATT&CK IDs with aliases/advisory IDs/file hashes, misclassified software and tactics as techniques, selected unrelated IDs and copied incomplete or paraphrased quotes. Final errors comprised six missing-endpoint/ID proof errors, three quote-location errors and one title-versus-caption attribution error. Two initial responses also hit the 700-token output limit.

The checks correctly rejected those outputs. No relationships were imported and no extraction accuracy score was measured.

## Revision

The current extractor uses `five-report-extraction-pilot-v2-source-selectors`. The model selects numbered source mentions and evidence units instead of generating names, attack_id values or quotes. The program reconstructs literal source values and exact spans.

Mention candidates come from exact actor phrases, explicit source ATT&CK IDs, literal catalog names/aliases and additional proper/executable names. Actor qualifiers and source ID namespaces are preserved. Unknown proper/executable names are software candidates only. This bounded source index is not exhaustive NER and may omit valid entities or behaviors; it does not establish final extraction recall.

Each of at most four relationships cites up to three numbered source units and, when needed, an explicit actor table caption. Repeated lines retain distinct location IDs. Multiple units retain a contiguous literal evidence span and separately record which units were selected. Endpoints and reported IDs must appear in selected units or the permitted caption, rather than elsewhere in the window. Titles/headings cannot establish actor use.

Typed patterns, source/identity checks, model digest validation, output limit 700, context 8192 and one-repair maximum remain in force. All candidates stay pending semantic review. Selecting a valid passage does not prove it asserts the relationship. No graph writes occur.

## Verification and rerun

All 123 offline tests passed. New checks cover repeated-unit offsets, subject/list evidence, rejection of title/invented/free-text selectors, unselected evidence, caption scope, actor qualifiers, ID namespaces and incompatible types. Mock-service tests cover changed-model rejection and a fresh truncation repair with failed output retained.

The actual ten-window preview passed: 40–58 source mentions per window and 2648–3332 estimated system/prompt/schema tokens, fitting context 8192 with 700 output tokens and 256 reserved chat tokens. No live model requests occurred during assistant verification; corrected live outcomes remain pending.

Keep Ollama running and start a fresh run because the format changed:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

The same ten saved windows are used. New logs and candidate/source-selector evidence go under `S:\ThreatWeave\work\corpus_extraction_pilot`; the review goes directly into `S:\ThreatWeave\docs`. Original failures are preserved. Do not use `--retry-run` on the incompatible v1 run. Later v2 failed-case retries require unchanged sources and extraction settings.
