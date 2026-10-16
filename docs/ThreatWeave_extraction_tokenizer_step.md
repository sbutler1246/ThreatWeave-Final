# Next step: verify Llama source-token counting

The four-mode development check is recorded in `docs/ThreatWeave_four_mode_v2_development_comparison.md`. The next implementation stage is preparing a broader extraction corpus rather than repeatedly tuning these three answers.

The design calls for 400–600 Llama-token extraction windows, initially 500 tokens with approximately 60-token overlap. Character counts and MiniLM WordPiece counts cannot establish that budget. This step prepares a source tokenizer from the vocabulary and merges already embedded in the installed Ollama Llama 3.1 8B model.

## Run

Keep Ollama running, then execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_extraction_tokenizer.py" --models "C:\Users\djfro\.ollama\models"
```

This installs the pinned `gguf==0.10.0` metadata-reader package and `sentencepiece==0.2.0`, which GGUF imports even for metadata-only use. Installation requires internet access. The existing NumPy, Transformers and tokenizers packages are used without dependency upgrades. No second model download is requested. Copy mode avoids cross-drive hardlink warnings.

The checker verifies the installed model manifest against the recorded Ollama digest and hashes its approximately 4.9 GB model file. It memory maps GGUF metadata without decoding model weight tensors. It derives a tokenizer from the installed vocabulary/merges, uses the Llama 3 splitting pattern in pinned Transformers 4.49.0, and checks exact source-text round trips.

Three raw Ollama prompts test local token-count agreement: numeric/contraction text, Unicode text and a frozen BianLian source excerpt. Each probe permits only one generated token. Source tokens and model BOS overhead are accounted for separately. These are source-count diagnostics, not question-answer evaluation or generated graph facts.

Checks require the serving Ollama model to match the installed model manifest and reject differing counts. A failure is saved for diagnosis; it does not publish a new ready tokenizer. Successful checks publish a versioned tokenizer artifact with checksums and a current pointer under `S:\ThreatWeave\work\extraction_tokenizer`. The review document is saved directly under `S:\ThreatWeave\docs`.

Default model storage is `%USERPROFILE%\.ollama\models`, or `OLLAMA_MODELS` if set. Both setup and checker support `--models` for an explicit path. This machine has a stale `OLLAMA_MODELS` path on S:, so the command above explicitly selects the verified installed model directory on C:. No global environment setting is changed. No Neo4j connection or database writes are involved.

## Scope

This does not yet build full-corpus chunks, run the five-report timing pilot or change retrieval/evaluation settings. It prepares the tokenizer required to make extraction windows measurable. Chat-template/system/schema overhead must be budgeted separately from source windows. The current 3000-byte retrieval evidence cap is unchanged.

Offline checks cover model-manifest binding, model-layer size, stream hashing, rejection of lossy Unicode round trips and rejection of runtime token-count disagreement. Live Ollama parity and the GGUF conversion require the command above; they have not been run by the assistant.

Verification: all 100 offline unit tests passed after adding the tokenizer guards. The three new Python source files passed compilation checks. The first test attempt encountered the Windows sandbox's temporary-directory restriction; test fixtures now use a dedicated workspace directory under `work/tokenizer_guard_tests`.
