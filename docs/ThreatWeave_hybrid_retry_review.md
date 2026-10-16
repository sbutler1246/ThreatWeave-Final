# Full hybrid retry review and next check

Reviewed October 14, 2026. This is an AI-assisted development review of saved output and evidence, not a human rating or held-out evaluation score.

Run: `work/hybrid_qa/20261014T060837Z-e15b3a98`.
Original run: `work/hybrid_qa/20261014T055940Z-bba7b219`.
The original failure and raw responses remain unchanged.

## Processing result

The revised shared generator (`development-shared-cited-generator-v2`) completed the failed AnyDesk case on its first attempt. It used 347 output tokens within the unchanged 700-token limit. Total case time was approximately 9.08 seconds, including retrieval and generation and excluding initialization.

Retrieval supplied five three-hop paths, five text hits and 16 source passages. Node2Vec was enabled and graph freshness checks passed. The answer includes all five supplied T1219 mitigation names and IDs, each with practical guidance and the correct identity/description citation pair. CISA observations and ATT&CK references use separate citation groups. The output-size failure is resolved for this retry.

## Semantic findings

The answer still requires qualification and scope review:

| Claim | Finding against saved evidence |
| --- | --- |
| AnyDesk use, E1–E3 | Remote control of victim devices is supported. The answer combines that repurposed use with the table's intended-use column about remote connections; those roles should remain distinct. |
| Execution Prevention, M1038, E4–E5 | Application control is supported. The answer strengthens “mitigate” to “prevent” and omits the restriction to unapproved software usable for remote access. |
| Filter Network Traffic, M1037, E6–E7 | Firewalls and proxies are supported, but the answer omits the destination scope: sites and services used by remote access software. |
| Network Intrusion Prevention, M1031, E8–E9 | The source specifies systems using network signatures and says they may be able to prevent traffic. The answer omits the mechanism and uncertainty, overstating the source. |
| Limit Hardware Installation, M1034, E10–E11 | Blocking IP-based KVM devices is supported, but “if they are not required” is omitted. |
| Disable or Remove Feature or Program, M1042, E12–E13 | The main action is supported. The answer omits the examples covering unapproved installations and features within supported applications. |

Conclusion: successful processing and complete mitigation enumeration, with remaining faithfulness and guidance-detail limitations. Citation validity alone does not establish semantic correctness. No formal correctness score is assigned.

## Next development check

Run all three existing development questions with the same revised generator. This checks AnyDesk together with BianLian/Rclone and ALPHV/Evilginx2, whose prior successful outputs used generator v1. It is a fresh development run, not a final four-condition benchmark.

Keep Neo4j and Ollama running, then execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\hybrid_qa.py" --demo
```

Accept the connection defaults and enter the Neo4j password when prompted. New records are saved under `S:\ThreatWeave\work\hybrid_qa`; the generated review document is saved under `S:\ThreatWeave\docs`. Review the complete answers and source qualifiers after execution. Existing records are preserved.

All four retrieval conditions must eventually be rerun with the same frozen generator for a controlled comparison; these development checks do not complete the full-corpus or held-out evaluation requirements.
