# Combined text/graph development review

AI-assisted review of `work/combined_qa/20261014T041454Z-bc234586`, its generated answers and saved source passages. Original run records remain intact, with formal human review and held-out evaluation pending.

Mode: `hybrid_no_node2vec`. All three cases generated non-abstaining answers on the first attempt, with zero execution failures. Model digest matches the preceding graph and text demonstrations: `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e` for `llama3.1:8b`. Temperature 0, context 8192 and output limit 700 were unchanged.

| Case | Retrieved evidence | Review finding | Single-run case time |
| --- | --- | --- | --- |
| AnyDesk / LockBit Affiliates | Five three-hop paths, five text hits, 16 source passages | Actor/tool attribution cites row plus context. All five mitigation identities and guidance are present with separate ATT&CK citations. Some guidance is condensed. | 11.57 seconds |
| Rclone / BianLian | One one-hop path, five text hits, seven source passages | Exfiltration and detection-avoidance details are supported. The phrase “intended use” incorrectly frames an observed adversarial purpose as general software intent. | 2.60 seconds |
| Evilginx2 / ALPHV affiliates | One one-hop path, five text hits, seven source passages | Supported answer covering the three credential/session artifacts in the source. | 1.27 seconds |

## Review details

AnyDesk's combined answer includes M1038 Execution Prevention, M1031 Network Intrusion Prevention, M1034 Limit Hardware Installation, M1037 Filter Network Traffic and M1042 Disable or Remove Feature or Program. Its mitigation claims cite the corresponding reference identity and guidance passages. M1038 omits the specific application-control mechanism; M1031 shortens the network-signature IDS/IPS guidance and its qualified wording. These condensed descriptions should receive human completeness review; the supplied source detail remains available in the citations.

The text-only AnyDesk answer omitted mitigation guidance and had citation weaknesses. This combined development answer improves coverage in this case. It does not establish general quality gains, statistical significance or the project's final success targets.

The Rclone phrase “The intended use of Rclone is…” is too broad. CISA describes what BianLian actors used it for. The accurate reading is “BianLian actors used Rclone to exfiltrate data to a cloud account they control on the same service.” The surrounding exfiltration and detection-avoidance statements are supported. Preserve the original answer for evaluation; no result has been silently rewritten.

Timings are one observation per case, excluding model/index initialization. They are not benchmark averages. No human rubric score or RAGAS score is assigned here.

Next: verify Node2Vec dependencies, then build the actual undirected domain-graph projection and separate 128-dimensional graph-vector index before enabling full hybrid. The current successful combined mode remains available as the required no-Node2Vec comparison condition.
