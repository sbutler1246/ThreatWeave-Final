# Graph QA across the imported development sources

Prepared October 13, 2026, after the batch mitigation import verified ten reference assertions and fifteen three-hop paths. Its receipt is `work/batch_mitigation_import/20261013T080751Z-04764d4b/import_receipt.json`.

The new `graph_qa.py` script supports the original Port Scanner scope and all five imported batch scopes across LockBit, BianLian and ALPHV Blackcat. It retrieves the actual Neo4j graph at runtime. This remains development graph-only QA; it does not implement full-corpus ingestion, vector text retrieval, Node2Vec or hybrid retrieval.

## Run the three-question demonstration

Keep Neo4j and Ollama running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\graph_qa.py" --demo
```

Enter the Neo4j connection details once. The script asks three development questions drawn from the imported source passages, not from held-out evaluation questions or reference answers.

1. How LockBit Affiliates use AnyDesk, plus the supplied ATT&CK mitigation guidance.
2. What BianLian group actors use Rclone for.
3. What ALPHV Blackcat/ALPHV affiliates use Evilginx2 to obtain.

The offline preview selects five three-hop paths and thirteen exact source passages for AnyDesk. Each reference uses separate contiguous spans for its identity and technique-specific guidance. The two prose questions each select one one-hop path and one CISA passage. Shorter paths reflect the evidence actually present; no additional technique or mitigation is inferred.

For one custom development question, use `--question "..."`. For an offline source-packing check, use `--demo --preview`. Use `--timeout 180` if local generation is slow.

## Retrieval and provenance

The retriever implements the existing `retrieve(QueryRequest) -> EvidenceBundle` interface for graph-only mode and the selected corpus version. It selects exact canonical names, verified aliases, explicit IDs and literal source occurrences. Source occurrences can locate historical labels but do not become verified canonical aliases.

Paths must contain the named entity types, with alternatives allowed within the same type for comparisons. An AnyDesk question naming LockBit Affiliates therefore requires both nodes. Retrieval is bounded to one through three hops, at most five seeds, thirty candidate paths and six selected paths. Source-scope rotation helps comparisons include both requested tools, while redundant subpaths are omitted.

Every selected edge must have an accepted matching Assertion, Document and Chunk. The retriever checks source hashes, literal spans, inherited captions, entity identity and frozen ATT&CK records. Multiple advisory edges on one path must share a CISA source scope; this prevents stitching incident facts from different rows. Structured ATT&CK mitigation assertions remain `origin=fused`, separate from advisory `origin=extracted` facts.

The model sees compact node/path context and exact source passages. The complete evidence/provenance bundle is retained in the log. Every generated claim must cite known evidence IDs; displayed answer text is assembled from those cited claims. These checks do not establish semantic correctness or completeness, so generated answers still require review.

## Context and timing limitations

This development script limits serialized evidence context to a UTF-8 byte count equal to the configured 3,000-token budget, using a deliberately conservative byte proxy. It logs the actual byte count and packing method. Exact shared-tokenizer packing remains pending before the final four-mode comparison. Ollama's prompt/evaluation token counts are logged separately.

Per-case execution timing includes retrieval and generation after authentication and initial setup. Three development examples are not a benchmark or evidence of a general accuracy improvement.

## Saved outputs

Each run saves question, evidence bundle, retrieval statistics, prompts, model responses, generated answer and summary under `work/graph_qa/<run>`. A review document is saved directly into `docs/ThreatWeave_graph_qa_<run>.md`. Failures are recorded per question; the script continues to other demonstration questions. No graph writes occur.

The offline preview passed for all three examples. Live Neo4j retrieval and the new generator prompt remain to be verified by running the command above.
