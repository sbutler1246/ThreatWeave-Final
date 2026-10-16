# Source-selector v2.1 live review and v2.2 repair

Later checkpoint: v2.2 processed all ten windows and produced 36 candidates, but semantic review found substantial role and attribution errors. See [the v2.2 review and current v2.3 repair](ThreatWeave_corpus_extraction_pilot_v2_2_development_review.md). The remainder preserves the v2.1 review and original v2.2 checkpoint.

October 14, 2026. AI-assisted diagnostic review of saved source text and raw responses; this is not a human rating, extraction F1 measurement or final evaluation.

## Live outcome

Run: `work/corpus_extraction_pilot/20261014T224921Z-f599539f`.

The HTTP schema repair worked on this run: all 20 generation requests returned HTTP 200 and completed with `done_reason: stop`. There were no service failures or output-limit truncations. Every window needed its one permitted repair.

The final outcome was **zero windows with source-checked candidates, five empty extractions, and five validation failures**. The console's “5/10 windows produced candidates or empty extractions” referred entirely to empty results. It does not mean five useful extractions. No graph writes occurred.

Total recorded run time was 52.038 seconds, including the availability check and sequential extraction/validation; chunk/catalog initialization was excluded. The summed generation-attempt elapsed time was 49.631 seconds, and the median per-window elapsed time was 4.119 seconds. There were 2530 generated tokens across all attempts. These are single-run observations with different output lengths and repair behavior, not a throughput benchmark.

| Window | Report | Final result | Case time | Diagnostic observation |
| --- | --- | --- | ---: | --- |
| 01 | BianLian | Validation failure | 15.04 s | Selected `BianLian actors` against a unit saying `BianLian group actors`; T1190 was also selected against a unit containing different IDs. The repair repeated the same result. |
| 02 | BianLian | Empty repair | 3.32 s | Initial Ngrok/Rsocks selections cited a clipped passage without the selected full actor phrase. The repair returned no relations. |
| 03 | Rhysida | Validation failure | 4.92 s | Mixed Rhysida and Vice Society endpoints across unrelated source units. The repair repeated the same result. |
| 04 | Rhysida | Empty repair | 3.18 s | Selected multiple tools against the first prose unit, which lacked the selected actor and most tools. |
| 05 | Scattered Spider | Empty repair | 2.62 s | Selected IT, an actor name typed as software, an alias and SIM against list units lacking their full endpoint proof. |
| 06 | Scattered Spider | Empty repair | 2.67 s | Selected tool rows but cited the general cautionary note. The body contains actual actor-scoped table captions that were not cited. |
| 07 | ALPHV Blackcat | Validation failure | 5.02 s | First response assigned all techniques to one unit, including an absent ID. The repair used ASSOCIATED_WITH with a Software endpoint. It also proposed IT as used software. |
| 08 | ALPHV Blackcat | Validation failure | 4.93 s | Used generic `The threat actors`, an encryptor name from elsewhere and an incompatible USES-to-Technique combination. |
| 09 | Phobos | Validation failure | 5.25 s | Used the literal phrase `If Phobos actors` against a different unit and repeatedly selected technique endpoints with incompatible predicates. |
| 10 | Phobos | Empty repair | 2.74 s | Cited the clipped opening unit for executable names from later prose and proposed ASSOCIATED_WITH to a Tactic. |

## Source validation and semantics

All-or-nothing window validation correctly rejected mixed valid/invalid batches. The raw Rhysida proposal for `Rhysida actors -> USES_TECHNIQUE -> T1078` has direct supporting source text about compromised VPN credentials. The ALPHV T1598 and T1586 proposals also have supporting phone/SMS credential-access prose. These observations do not rescue the failed windows or add accepted candidates.

Literal co-occurrence can also pass without asserting the relation. In window 07, the repair proposed `ALPHV Blackcat affiliates -> USES -> IT`; the source says the actors **pose as company IT/helpdesk staff**, which does not identify IT as software they use. In window 08, the proposal involving `ALPHV` as Software co-occurs with actor wording without establishing that software-use assertion. The Rhysida overview combines several subjects in a long paragraph, so its separate ransomware-use proposal requires closer attribution than simple paragraph co-occurrence.

The five empty windows also contain usable source material: BianLian PowerShell activity, Rhysida's explicit PowerShell ISE/PsExec activity, Scattered Spider's actor-introduced list and tool captions, and Phobos executable use. Returning an empty repair is therefore not evidence that the source lacked extractable facts. These are qualitative development findings; no exhaustive gold annotation or extraction-recall score is produced here. Review observations are not inputs to extraction, retrieval or generation.

There were zero source-checked candidate relations and therefore zero retained unique candidates, repeated candidate relations or exact duplicate supports. Those zero counts provide no overlap-quality result. Original v1 failures, v2 HTTP rejections and this v2.1 run remain preserved, including unsuccessful model outputs.

## v2.2 repair

Current implementation: `five-report-extraction-pilot-v2.2-evidence-bound-selectors`.

The previous grammar independently allowed any global head, predicate, tail and evidence IDs. The new schema instead provides alternatives binding evidence IDs to endpoints literally present in that evidence, with a compatible predicate. Evidence IDs appear first in each alternative. The model still decides whether the source asserts a relationship and may return an empty result. Enumerated combinations are source/type possibilities, not extracted or semantically approved facts.

Permitted evidence is a single source unit; a colon-introduced subject/list pair; a nested colon list of at most three units; or an explicit actor table caption with its row. Inline captions are recognized for tools/malware “Used by” or “Leveraged by”; their actor spelling and case remain literal. Table row scopes stop at subsequent tables and when the simple row/description sequence ends. A row and its description may also supply software-to-technique proof. Inherited actor captions remain explicit context references. Arbitrary neighboring paragraphs are not combined by this menu.

Runtime checks independently enforce the same combinations, source spans, endpoint/predicate types, qualified actor names and frozen identity catalog. Mention proof now requires word boundaries; a parent ID such as T1090 is not treated as explicitly reported merely because T1090.002 appears. Empty caption arrays remain constants without empty enumerations. HTTP error-body retention, the verified model digest, temperature 0, context 8192, output limit 700 and one-repair maximum remain in place.

The final console line now separately reports windows with candidates, empty extractions and failures. New window records also save their source/evidence/type pattern counts.

This remains a bounded diagnostic extractor. Unknown proper/executable names are software candidates, and source indexing can include generic terms or miss valid entities. Plain-text caption/list parsing is limited and is not exhaustive document understanding. Grammar validity and literal evidence cannot establish attribution, actual actor use, negation or certainty. All generated candidates remain pending semantic review; no final extraction-recall claim is justified.

## Verification and next command

All **134 offline tests** pass, including checks for wrong-unit selectors, incompatible types, explicit/nested lists, inline-caption boundaries, exact ID namespaces, duplicate relations, unchanged source offsets, uncertainty flags and HTTP diagnostics. Tests use synthetic inputs and service fixtures. The negated-source test deliberately demonstrates that an eligible source/type combination still needs semantic rejection.

The actual ten-window preview passes frozen source/tokenizer/catalog checks. Estimated system/prompt/schema budgets are 2594–6635 tokens, plus 700 output tokens and 256 reserved chat tokens, within context 8192. All actual schemas are checked for validity, nonempty enumerations and literal endpoint proof. Source preparation remains `work/corpus_pilot_chunks/20261014T065159Z-c4380457`, fingerprint `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`.

The revised schema has not yet been exercised against live Ollama. Keep Ollama running and start a **fresh** run because extraction settings changed:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

Do not use `--retry-run` on earlier formats. New logs save under `S:\ThreatWeave\work\corpus_extraction_pilot` and the generated review saves directly in `S:\ThreatWeave\docs`. The assistant made no live Ollama/Neo4j calls and ran no installers during this repair.
