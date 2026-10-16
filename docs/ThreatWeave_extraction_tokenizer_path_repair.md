# Extraction tokenizer path and dependency repair

October 14, 2026. Original failed run: `work/extraction_tokenizer/20261014T063530Z-413806c3`. Its records are preserved.

GGUF 0.10.0 installed successfully. The checker stopped before any probes because `OLLAMA_MODELS` selected `S:\Knowledge Engineering\Ollama\Models`, which does not exist. The expected model manifest exists in `C:\Users\djfro\.ollama\models`; its SHA-256 matches the recorded development model digest.

An assistant-run offline inspection verified the model manifest and full model-layer checksum, then exposed a second dependency issue: GGUF 0.10.0 imports SentencePiece from its package initializer, although that dependency is absent from its declared requirements. SentencePiece is not installed in the application environment. The first live failure did not reach this import.

The setup script now accepts `--models`, forwards that explicit directory to the checker and installs pinned `sentencepiece==0.2.0` alongside GGUF. It uses copy mode because the uv cache on S: and Python environment on C: cannot share hardlinks. The original hardlink warning was harmless and installation succeeded.

The checker records the resolved model directory and checks the required SentencePiece version before hashing the model. Global environment settings, graph/text indexes and generation settings are unchanged.

Keep Ollama running and retry:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_extraction_tokenizer.py" --models "C:\Users\djfro\.ollama\models"
```

The already installed GGUF package is reused; the missing SentencePiece package is added. The retry creates new records and a new review document inside ThreatWeave. GGUF conversion, exact source round trips and live raw Ollama parity remain pending until the dependencies are available and the retry runs.

All 100 offline unit tests passed during the path repair. These tests do not establish live tokenizer parity.
