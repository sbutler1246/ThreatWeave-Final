# Text-only QA development review

AI-assisted inspection of `work/text_qa/20261014T040530Z-d3543a5e`, including saved answers, exact evidence and raw model responses. Formal human scoring and held-out evaluation remain pending. Original run records are preserved with their pending semantic-review status.

The run produced three non-abstaining answers with zero execution failures. That is a processing outcome, not three correct/complete answers. Model: `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`; temperature 0, context 8192, output limit 700.

| Development case | Review finding | Attempts | Single-run case time |
| --- | --- | --- | --- |
| AnyDesk / LockBit Affiliates and mitigations | Incomplete answer with citation weaknesses; mitigation guidance omitted. | 2 | 52.88 seconds |
| Rclone / BianLian | Supported cloud-exfiltration purpose; omits the passage's detection-avoidance detail. | 1 | 1.26 seconds |
| Evilginx2 / ALPHV affiliates | Supported answer covering MFA credentials, login credentials and session cookies. | 1 | 1.21 seconds |

## AnyDesk findings

The top-five text matches supplied the AnyDesk row, three other LockBit tool rows and M1038 identity/guidance. The final answer did not describe even the retrieved M1038 guidance. Thus both bounded reference retrieval and generation incompleteness contributed to the result.

- The actor-to-tool claims cite the row alone or the caption alone. The row names AnyDesk, while the caption establishes LockBit Affiliates; the prompt required both for that attribution.
- The claim about AnyDesk and T1219 cites E5, which is the Atera row. The underlying AnyDesk-to-T1219 association is present in E1, but the actual selected citation does not support that specific software claim.
- The answer repeats the same actor/tool statement and lists no mitigations, despite a multipart question.
- Attempt one reached the 700-token output limit while repeating claims; it was rejected. The single permitted output/citation repair completed, but format/citation-ID validation did not correct these semantic problems. The first raw output, repair prompt and final output remain saved.

The earlier graph-only AnyDesk development answer included five mitigation identities and their practical guidance. This contrast is useful for diagnosing retrieval and generation. It is not a held-out quality score or proof of a general advantage. Single-run timings include retrieval/generation and the allowed repair; initialization is excluded. They are not benchmark latency averages.

## Next stage

Combine the verified text and graph branches using source-parent rank fusion, deduplicate source passages, and preserve complete supported paths. This next mode is explicitly `hybrid_no_node2vec`, one of the approved comparison conditions. Full hybrid still requires its separate 128-dimensional graph embeddings. Keep the original text-only run as evidence of this development limitation; do not rewrite it as a successful quality result.
