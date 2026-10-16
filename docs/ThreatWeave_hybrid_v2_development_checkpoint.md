# Full hybrid generator-v2 development checkpoint

AI-assisted source review, October 14, 2026. This document records development observations, not human ratings or held-out benchmark scores. Original run records retain their pending semantic-review status.

Run: `work/hybrid_qa/20261014T061415Z-0d56a1a6`.
Generated review: `docs/ThreatWeave_hybrid_qa_20261014T061415Z-0d56a1a6.md`.

## Result

All three cases produced non-abstaining answers, each on its first generation attempt, with zero execution failures. The AnyDesk output is identical to the successful one-case retry. This confirms that the compact response change works on these three development questions; it does not establish general accuracy.

| Case | Paths and source passages | Output tokens | Case time | Source review |
| --- | --- | --- | --- | --- |
| LockBit Affiliates / AnyDesk | Five three-hop paths; 16 passages | 347 | 9.15 seconds | All five supplied mitigation names, IDs and citation pairs appear, with remaining qualification and scope omissions. |
| BianLian / Rclone | One one-hop path; seven passages | 66 | 1.08 seconds | Supported cloud-exfiltration purpose. The previous misleading general “intended use” framing is absent. The same-service detail and detection-avoidance purpose are omitted. |
| ALPHV affiliates / Evilginx2 | One one-hop path; seven passages | 73 | 1.09 seconds | Covers all requested items: MFA credentials, login credentials and session cookies, supported by E1. |

Each case also retrieved five text hits. One-hop paths are appropriate for the two direct actor/software questions; the AnyDesk mitigation question traverses three relationships. These single-run times include retrieval, packing and generation, excluding initialization. They are not latency averages from the final benchmark.

## AnyDesk limitations

The five mitigation identities and practical actions are present, but the answer still strengthens or compresses some source guidance:

- M1031 omits network signatures and the source's uncertainty about prevention effectiveness.
- M1034 omits the condition that IP-based KVM devices are blocked if not required.
- M1037 omits that the outgoing destinations are sites and services used by remote access software.
- M1038 strengthens mitigation to prevention and omits the remote-access restriction on the unapproved software.
- M1042 omits the source's examples of installations and built-in features.
- The opening sentence combines AnyDesk's intended-use column with the observed repurposed remote-control use.

These are the same findings documented in `docs/ThreatWeave_hybrid_retry_review.md`. No source passages or generated answers have been rewritten to hide them. Valid citation IDs do not prove that a claim preserves the source's meaning.

## Recorded settings

- Shared generator: `development-shared-cited-generator-v2`.
- Ollama model: `llama3.1:8b`.
- Model digest: `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`.
- Temperature 0; context 8192; output limit 700; maximum one repair.
- Text index: `d183d6dfdb5313bc15e23049a7e907fae3d62342492b3658ca09c5409329b495`.
- Graph index: `07df4575ac49de6962341dca1887fe207f952c89b9c8452ad48906094efe8b8d`.
- Projection SHA-256: `0c2f3e01a65befef413411e7fb236bcb8dd72604e412c0c91651a7c82df5cdc5`.
- Retrieval configuration hash: `64235453c3bdc20a3d79d7af186c79c5e87fd7cee44857949aea7d061378e638`.

## Next check: matching text-only baseline

Earlier text-only, graph-only and no-Node2Vec development outputs used generator v1. They remain historical results; they cannot isolate retrieval differences from the generator change. Rerun the existing development baseline with v2, beginning with text-only:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\text_qa.py" --demo
```

Keep Ollama running. This command requires no Neo4j connection. It uses the existing verified development text index, the same three questions and the shared v2 generator. It saves a new run under `S:\ThreatWeave\work\text_qa` and a review document under `S:\ThreatWeave\docs`.

Review the resulting coverage and source wording before proceeding to the matching graph-only and no-Node2Vec checks. These small development runs are diagnostic. Full-corpus ingestion, application integration, extraction scoring and the controlled held-out four-mode evaluation remain unfinished.
