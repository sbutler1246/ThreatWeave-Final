# Five-report source preparation checkpoint

October 14, 2026. User-run records: `work/corpus_pilot_chunks/20261014T065159Z-c4380457`. Status: ready for extraction pilot.

The run saved 54 technical-section windows across BianLian, Rhysida, Scattered Spider, ALPHV Blackcat and Phobos. Two windows per report were selected deterministically, producing ten pilot windows. All five reports are outside the held-out evidence set. Frozen raw/normalized source checksums and source-tokenizer identity were verified. Source offsets and inherited source context were retained.

Chunk fingerprint: `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`.
All-window record digest: `babe89f31695703511da48fdcde9a2c985e370565bb91920e903b610448214f9`.
Verified tokenizer SHA-256: `0f19bfc2cced451a1be5707855af7f7579ccc88c6943b45c93096555a73163e9`.
Derived byte-level decoder artifact hash: `2c7dc389a96c30a2ce3ebe6c6a919796b7d5c17bd6da1f323c8a534616ca8a39`.

All 54 windows contain 448–590 measured source tokens. The ten selected windows contain 465–515 tokens, excluding inherited context and prompt overhead. No extraction, graph writes or model-quality scores were produced by this preparation step.

The saved data was independently recomputed and compared by the new extractor's offline preview. All saved windows and their pilot selection matched. The frozen ATT&CK 17.1 identity snapshot also passed its checksum check. Estimated system/prompt/schema sizes for the ten requests are 1798–1845 source-tokenizer tokens; each fits the 8192-token context when reserving the existing 700-token output budget and 256 tokens for chat overhead. This is a preflight estimate, not a measurement of the live formatted prompt.

The extraction runner is ready for a user-run live timing pilot. Its offline validation and mock-service tests passed as part of all 116 offline tests. These tests verify quote uniqueness/alignment, endpoint/source proof, caption versus title attribution, bounded output, identity/source validation, overlap aggregation, rejection of a changed serving model and a fresh repair after truncation.

Instructions: `docs/ThreatWeave_corpus_extraction_pilot_step.md`. Final corpus extraction/ingestion, refreshed indexes and benchmark evaluation remain unfinished.
