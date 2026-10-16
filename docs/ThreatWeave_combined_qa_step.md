# Combined text and graph QA step

The text-only development review is saved in `docs/ThreatWeave_text_qa_development_review.md`. Rclone and Evilginx2 answers are supported; the AnyDesk answer omits mitigation guidance and has citation weaknesses.

Keep the ThreatWeave Neo4j instance and Ollama running, then run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\combined_qa.py" --demo
```

Use these connection values, pressing Enter to accept the displayed defaults:

- Neo4j URI: `bolt://localhost:7687`
- Username: `neo4j`
- Database: `neo4j`
- Password: your instance password; typing is hidden and it is not saved.

## Implemented mode

The mode is `hybrid_no_node2vec`: MiniLM text search plus supported typed graph paths. This is the approved ablation condition, not the full-hybrid condition. Full hybrid will require a separate Node2Vec graph collection and is not silently substituted with this mode.

Both branch configurations must match. The text branch checks its source/index manifest and stored vector binding before querying. The graph branch reads accepted source-verified assertions from Neo4j. It uses the current up-to-three-hop retrieval with bounded candidate paths; the text branch retains its top-five nearest-neighbor search. Graph service errors fail the affected run rather than silently selecting text-only mode. A legitimately empty graph result can still leave text evidence available, and that condition is logged.

## Fusion and evidence packing

The RRF unit is `(source document ID, parent extraction-chunk ID)`, so retrieval children can join graph evidence to the same source parent. Each unique parent contributes once per branch using `1 / (60 + rank)`. Graph parent ranks follow first appearance in the graph branch's existing deterministic path order; text parent ranks follow text-neighbor order. These graph ranks are not learned relevance scores.

To preserve complete paths, the implementation sums distinct parent RRF scores within each whole path or text/context group. This group aggregation is a project implementation choice. Groups are packed in descending score, with deterministic ties, at most six whole paths and five text hits. Sources appearing in both branches are deduplicated by exact document span, checked for consistent text/source metadata, and assigned new global citation IDs. Every path edge's citations are remapped to those IDs; no partial path is admitted when a group exceeds the context limit.

The combined context shares the current conservative 3000 UTF-8 byte cap. Exact generator-tokenizer accounting remains pending. The individual branch outputs are already bounded; this stage fuses those outputs rather than reranking the complete candidate universe. That implementation detail will be held consistent and documented when final conditions are frozen.

The same cited Ollama generator, model settings, output schema and one allowed repair are used by graph, text and combined QA. No reference answers or benchmark gold facts enter retrieval. Citation-ID checks still require semantic review of generated claims.

## Validation and saved results

All 74 offline tests passed, including source-span conflicts, RRF arithmetic, deduplication, citation remapping, whole-path budget enforcement, empty graph results and rejection of full-hybrid requests without its embeddings.

The local preview combined source-based graph fixtures with the real text index, without Neo4j or Ollama calls:

| Development case | Whole paths | Text hits | Source passages | Evidence bytes / cap |
| --- | --- | --- | --- | --- |
| AnyDesk | Five three-hop paths | 5 | 16 | 2959 / 3000 |
| Rclone | One one-hop path | 5 | 7 | 1177 / 3000 |
| Evilginx2 | One one-hop path | 5 | 7 | 1154 / 3000 |

The preview establishes source packing, not current live graph presence or answer quality. The command above runs live QA. It saves ranked branch details, fused source ranks, selected/skipped groups, evidence, prompts, model digest, raw outputs and answers under `work/combined_qa`. The review document is saved directly into `docs`. Per-case times exclude model/index initialization; final controlled benchmarking remains pending.

After reviewing the live combined answers, add the separate 128-dimensional Node2Vec graph embeddings for full hybrid. Full-corpus ingestion, exact context packing, the interface and final evaluation remain outstanding.

Method reference: [Cormack, Clarke and Büttcher, Reciprocal Rank Fusion (SIGIR 2009)](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf).
