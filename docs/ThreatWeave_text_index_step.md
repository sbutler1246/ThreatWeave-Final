# Build the development text index

The local setup receipt `work/text_setup/20261014T035203Z-fc13c0f4/setup_receipt.json` confirms the pinned packages and normalized 384-dimensional MiniLM vectors, plus a two-record Chroma lookup. The UTC receipt date corresponds to the evening of October 13, 2026 in America/Chicago.

Next, run in PowerShell:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_text.py"
```

This creates a text collection containing the same six CISA development source scopes and 13 frozen ATT&CK mitigation references available to graph QA. It uses cached MiniLM files with network downloads disabled. Neo4j and Ollama do not need to be running for indexing.

The cached-tokenizer preview prepared 19 retrieval chunks. The longest embedding input was 110 WordPieces and 478 characters, below the configured ceilings of 240 WordPieces and 1000 characters. Longer future parent passages split into child chunks with up to 40 overlapping body WordPieces. Exact source offsets and parent extraction-chunk IDs are retained. Inherited table captions, column headings and structured reference identity fields retain their own source spans; they accompany the body in embedding input without being represented as a single continuous quote.

All 60 offline tests passed after this implementation. New checks cover complete parent-text coverage, overlap, context tampering and both input limits. The cached-tokenizer preview passed without creating a collection. The actual source index and ranked queries still need the command above.

Chroma receives normalized MiniLM vectors supplied by the application, with cosine distance. The collection is under `work/chroma` and has a source/configuration fingerprint in its name. Chunks, context spans and structured-reference provenance are saved in `work/text_index/<fingerprint>`. Existing matching records can be indexed again; conflicting collection configuration or altered source records stop the run. This collection contains text embeddings only; a separate Node2Vec graph collection is still pending. Gold extraction labels and QA reference answers are not indexed.

The script verifies stored text, metadata and vectors, then searches for the three existing development questions. Ranked matches and distances are saved in a timestamped `work/text_index_runs` receipt and a review document directly in `docs`. No LLM answer is generated yet. A successful vector lookup does not establish retrieval relevance, completeness or final benchmark performance; the recorded ranks remain available for review.

Expected final message:

```text
READY: Development text index built and retrieval smoke checks passed.
```

After reviewing this run, the next step is text-only cited QA, followed by hybrid search and the separate graph embeddings. Full-corpus indexing and final evaluation remain pending.

Implementation references: [Chroma accepts supplied embeddings](https://docs.trychroma.com/docs/collections/add-data), [MiniLM model](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), and [Transformers 4.49 tokenizer offsets](https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/tokenizer).
