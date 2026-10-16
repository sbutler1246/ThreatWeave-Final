# Text-only cited QA step

The development text index passed its local checks. Its reviewed retrieval checkpoint is saved in `docs/ThreatWeave_text_index_checkpoint.md`.

Keep Ollama running, then run in PowerShell:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\text_qa.py" --demo
```

Neo4j is not needed and no database credentials are requested. The script uses the existing Chroma collection and cached MiniLM model, verifies the index against freshly prepared frozen source records, checks stored vector/source binding, and retrieves five nearest text neighbors per question. It does not expand graph paths or read reference answers. Long questions exceeding MiniLM's input window are rejected rather than silently truncated.

The three questions are the same AnyDesk, Rclone and Evilginx2 development questions used by graph QA. The Ollama generator prompt, model settings, structured response schema, cited-claim rendering and one allowed output/citation repair are shared with graph QA. Model digest is recorded for every run. Claims citing IDs outside the retrieved evidence are rejected. Passing citation checks does not establish semantic correctness.

Source bodies and inherited context retain separate exact spans. Shared table captions and headers are deduplicated. Each selected child and its context are packed together under the same conservative 3000 UTF-8 byte cap used by development graph QA. Exact shared-tokenizer packing and controlled final experiment timing remain pending.

The previous AnyDesk text search returned one mitigation reference in its top five, compared with five chains from graph retrieval. Review the generated answer for omissions and unsupported attempts to fill those gaps. Responses and abstentions are recorded as process outcomes, not automatic quality passes. No hand-coded mitigation expansion or answer injection is used to improve this baseline.

Each run saves questions, ranked retrieval metadata, exact evidence, prompts, raw Ollama responses, model digest and cited answers under `work/text_qa`. The review document is written directly into `docs`. Reported per-case times include query embedding, text search, source packing and generation; model loading and initial index verification are excluded. These development timings are not final benchmark latency measurements.

The local three-question retrieval preview passed: five selected chunks per question, eight source passages for AnyDesk and seven each for Rclone and Evilginx2, all below the byte cap. Ollama was not called during that preview. Live text-only answers still need the command above.

All 67 offline tests passed. New tests check altered text/provenance rejection, candidate limits, atomic context packing, unknown citations, and correct text-only mode labeling in the shared generator. The live cached-index preview also verified source/vector binding in the existing collection.

After the run, review the saved answers before implementing hybrid retrieval and the separate Node2Vec graph embeddings.

Reference: [Chroma query results with supplied vectors](https://docs.trychroma.com/docs/querying-collections/query-and-get).
