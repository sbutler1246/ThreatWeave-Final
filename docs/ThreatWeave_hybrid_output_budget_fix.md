# Hybrid development output-budget repair

Reviewed October 14, 2026: `work/hybrid_qa/20261014T055940Z-bba7b219` completed two cases and failed the AnyDesk case. The original run and raw outputs remain unchanged.

## Cause

AnyDesk retrieval passed: five three-hop paths, five text hits and 16 source passages were saved. Both generation attempts reported `done_reason: length` and `eval_count: 700`. The model produced separate mitigation identity and guidance claims plus repeated actor/tool observations, then stopped before completing the final mitigation and JSON structure. The repair copied the incomplete response, and the second attempt repeated the same oversized structure.

This was an output-length failure, not a Neo4j connection, Node2Vec fitting or graph freshness failure. The Rclone answer remains recorded with its misleading “intended use” wording; the Evilginx2 answer is supported by its source. Those processing successes are not formal correctness scores.

## Shared generator revision

The shared current generator is now `development-shared-cited-generator-v2` for graph-only, text-only, the no-Node2Vec comparison and full hybrid:

- The unused JSON `answer` field is fixed to `See cited claims.`; user-facing text still comes exclusively from cited claims.
- The response schema allows at most eight claims, 280 characters per claim and four citation IDs per claim. Duplicate claims and repeated citation IDs are rejected.
- Prompt instructions combine each mitigation's name, ID and practical guidance in one claim, discourage repeated observations, preserve conditional wording and attribute a prose purpose to the observed actor rather than general software intent.
- A response cut off by the token limit receives one fresh format repair using the original evidence. Its incomplete text is saved but is not copied into that repair prompt. Other format/citation errors retain the usual repair with prior output.
- The 700-token output limit, temperature 0, context 8192, retrieval limits and one-repair maximum remain unchanged. Responses reaching the output limit are still rejected; no partial JSON is accepted or silently completed.

These changes address response size and framing. They do not guarantee complete or semantically correct answers. All earlier development runs retain their old generator version; controlled final comparisons must rerun every condition using the same frozen current generator.

## Retry only the failed case

Keep Neo4j and Ollama running, then run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\hybrid_qa.py" --retry-run "S:\ThreatWeave\work\hybrid_qa\20261014T055940Z-bba7b219"
```

Accept the connection defaults and enter your Neo4j password. This selects only the failed AnyDesk question. It verifies the prior retrieval configuration, text/graph index fingerprints, model digest and generation settings. It creates a new timestamped run linked by `retry_of`; it does not overwrite or reclassify the earlier run's failure. New logs go under `work/hybrid_qa`, and the new review document is written directly into `docs`.

The two previously completed cases are preserved. Their semantic issues remain available for review; the retry does not relabel them as outputs of the revised generator. A fresh `--demo` run can later exercise all three questions under v2.

## Verification

All 96 offline tests passed. New checks cover response bounds, duplicate detection, rejection of unknown citation IDs, a fresh truncation repair, an unchanged output budget, the two-attempt maximum and failed-case-only retry selection with workspace/index guards.

The actual retry preview selected only AnyDesk, retained five three-hop paths and 16 passages, and preserved the 2959/3000-byte evidence context. No Neo4j or Ollama calls occurred in that preview. The corrected live generation still needs the retry command above.
