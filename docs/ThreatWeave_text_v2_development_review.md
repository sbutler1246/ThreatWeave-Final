# Text-only generator-v2 development review

AI-assisted review on October 14, 2026, of saved answers, evidence and retrieval ranks. This is a development observation, not a human rating or held-out benchmark score. Original generated records remain unchanged with their pending semantic-review status.

Text run: `work/text_qa/20261014T061730Z-8c20bcb9`.
Full-hybrid comparison: `work/hybrid_qa/20261014T061415Z-0d56a1a6`.

## Processing and source findings

All three text-only cases produced non-abstaining answers on their first attempt, with zero execution failures. Each case selected five text chunks and no graph paths.

| Case | Text-only answer review | Case time | Output tokens |
| --- | --- | --- | --- |
| LockBit Affiliates / AnyDesk | Lists one of the five supplied T1219 mitigations, M1038. Its cited identity is correct, but the practical mechanism is omitted and wording is strengthened. Adds three unrelated tool statements. | 3.61 seconds | 245 |
| BianLian / Rclone | Supported cloud-exfiltration purpose; omits the same-service and detection-avoidance details. Identical answer text to the full-hybrid v2 run. | 0.96 seconds | 66 |
| ALPHV affiliates / Evilginx2 | Supported answer covering MFA credentials, login credentials and session cookies. Identical answer text to the full-hybrid v2 run. | 1.03 seconds | 73 |

Times include per-case retrieval, packing and generation, excluding initialization. These are single-run observations, not latency averages.

## AnyDesk retrieval and generation

The five text matches were the AnyDesk row, Backstab row, Atera row, Advanced Port Scanner row and the M1038 description. The description inherited its mitigation identity as source context. The packed evidence contains eight exact passages, including the table caption and headers.

M1031, M1034, M1037 and M1042 were absent from this top-five evidence bundle. The omission occurred in nearest-neighbor retrieval; no chunks were dropped for budget reasons. The packed context used 1151 of the shared 3000 UTF-8 byte cap. Expanding the context cap alone would not recover references outside the retrieved candidates.

The generated answer correctly attributes remote control of victim devices to LockBit Affiliates using E1 and the caption E2. It describes AnyDesk's general connection capability separately, avoiding the full-hybrid answer's combined intended/repurposed-use sentence.

M1038 is correctly identified with its description E7 and identity E8. However, the answer says prevention of unapproved software installation/use, while E7 specifies application control to mitigate installation/use of software usable for remote access. It omits both the application-control mechanism and the remote-access scope, and strengthens “mitigate” to “prevent.” Thus even the single retrieved mitigation lacks faithful practical guidance.

The claims about Atera, Advanced Port Scanner and Backstab are supported by their respective source rows, but do not answer the AnyDesk question. They are relevance problems rather than invented source facts.

## Comparison limits

Both runs use the same three questions, shared generator v2, Ollama digest, generation options and text-index fingerprint. Full hybrid supplied five three-hop AnyDesk paths with all five mitigation identities and descriptions, and enumerated all five in its answer. Its remaining source qualifications and scope issues are recorded in `docs/ThreatWeave_hybrid_v2_development_checkpoint.md`.

This contrast identifies a coverage limitation of the current text-only top-five retrieval on this development question. It does not establish a general hybrid advantage or isolate the contribution of Node2Vec. Matching graph-only and no-Node2Vec outputs are still needed, followed later by the controlled held-out evaluation.

Recorded shared settings: `development-shared-cited-generator-v2`; `llama3.1:8b`; model digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`; temperature 0; context 8192; output limit 700; one repair maximum. Text index: `d183d6dfdb5313bc15e23049a7e907fae3d62342492b3658ca09c5409329b495`. Text retrieval configuration hash: `0087b92a1bbc67f7011bb7f64d4760207fbab9ade4e704efef075ee07480b04a`.

## Next check: matching graph-only run

Keep Neo4j and Ollama running, then execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\graph_qa.py" --demo
```

Accept the connection defaults and enter the Neo4j password when prompted. The command uses the same three development questions and shared generator v2. It saves new results in `S:\ThreatWeave\work\graph_qa` and the generated review document in `S:\ThreatWeave\docs`. It preserves prior v1 results.

After reviewing this run, repeat the existing no-Node2Vec comparison with v2. Full-corpus ingestion, extraction scoring, application integration and final evaluation remain unfinished.
