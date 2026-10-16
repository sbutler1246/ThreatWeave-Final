# Verified Llama source-tokenizer checkpoint

October 14, 2026. User-run records: `work/extraction_tokenizer/20261014T064015Z-126bb1e2`. Status: ready. Original failed path/dependency run is preserved.

The installed Ollama model manifest and model-layer checksum were verified. Three source-text round trips passed, and local token counts matched raw Ollama prompt counts exactly:

| Probe | Source tokens | Start-token overhead | Ollama raw prompt tokens |
| --- | ---: | ---: | ---: |
| Numeric/contraction text | 17 | 1 | 18 |
| Unicode text | 19 | 1 | 20 |
| Frozen BianLian excerpt | 486 | 1 | 487 |

Model: `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`. Model-layer SHA-256: `667b0c1932bc6ffc593ed1d03f895bf2dc8dc6df21db3042284a6f4416b06a29`. Vocabulary size: 128256. Verified tokenizer artifact SHA-256: `0f19bfc2cced451a1be5707855af7f7579ccc88c6943b45c93096555a73163e9`.

Runtime packages: Transformers 4.49.0, tokenizers 0.21.4, GGUF 0.10.0, SentencePiece 0.2.0 and NumPy 1.26.4. The explicit model directory was `C:\Users\djfro\.ollama\models`.

## Larger-source decoder correction

Preparing complete technical sections exposed a legacy GGUF-converter decoder operation that removes a leading space. The initial three probes did not begin with an ordinary space and therefore did not detect this. Full-section round trips passed, but some overlapping source substrings failed.

The Llama 3 byte-level decoder is now restored without changing vocabulary, merges, splitting, encoding token IDs or counts. Corpus preparation checks the verified artifact checksum first, then corrects the decoder in memory and records the resulting derived tokenizer hash and `llama3-bytelevel-v1` policy. The original ready artifact and raw probe records remain unchanged. Future tokenizer setup exports the corrected decoder and includes leading/trailing spaces in the numeric probe.

A regression test reproduces leading-space loss and verifies exact Unicode/whitespace decoding after correction with identical token IDs. The actual five-report source preview now passes, covering 54 measured extraction windows. All 106 offline tests passed.

Source counts are now usable for the extraction-window pilot. They exclude inherited context and system/schema/chat-template overhead. This check does not establish extraction correctness or final evaluation quality; the existing retrieval byte cap is unchanged.

Next: `docs/ThreatWeave_corpus_pilot_preparation_step.md`.
