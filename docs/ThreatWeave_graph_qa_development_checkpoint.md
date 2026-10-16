# Multi-source graph QA development checkpoint

Reviewed on October 13, 2026 against the saved answers and displayed source passages from `work/graph_qa/20261013T083053Z-2293dce7`.
Review method: AI-assisted inspection of this development demonstration. Formal human ratings and held-out evaluation remain pending; original run records retain their pending-review status.

| Development question | Retrieved paths | Evidence passages | Single-run retrieval and generation time | Review finding |
| --- | --- | --- | --- | --- |
| LockBit Affiliates / AnyDesk | Five paths, each three hops | 13 | 12.21 seconds | Source-supported use; all five supplied ATT&CK mitigation identities and practical guidance included, with separate CISA and ATT&CK citations. |
| BianLian / Rclone | One path, one hop | 1 | 2.14 seconds | Source-supported cloud exfiltration purpose and detection-avoidance explanation. |
| ALPHV affiliates / Evilginx2 | One path, one hop | 1 | 1.38 seconds | Source-supported MFA credentials, login credentials and session cookies; sentence formatting is fragmented across two claims. |

All three cases generated answers on the first attempt; zero execution failures were recorded. The AnyDesk answer repeats its CISA observation, a minor presentation issue. No benchmark accuracy, hallucination reduction or human quality score is inferred from this run. Timings are individual observations, not averages or latency guarantees.

The AnyDesk chain is actor → software → technique → mitigation. Shorter source-supported paths answer the two prose questions without adding unsupported technique or mitigation links.
The five supplied T1219 mitigation references are M1031, M1034, M1037, M1038 and M1042 from the frozen ATT&CK 17.1 snapshot. They describe technique-level guidance, not CISA observations of mitigation deployment in these incidents.

Generator: `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`; temperature 0, context 8192, output limit 700.
Configuration hash: `19cfcbb4c5e4f0df515355986387cd3869d3081173b3c61cea836b9319a94af0`.
Evidence packing currently uses a conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.

Next stage: install and verify the frozen MiniLM text embedding and local Chroma storage, then implement text retrieval before comparing it with graph retrieval and building hybrid search. Node2Vec, full-corpus ingestion, the user interface and final evaluation remain pending.
