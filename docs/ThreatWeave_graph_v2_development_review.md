# Graph-only generator-v2 development review

AI-assisted source inspection, October 14, 2026. This document records development observations, not human ratings or held-out benchmark scores. Original run records and their pending semantic-review status remain unchanged.

Run: `work/graph_qa/20261014T062006Z-5ad2e7b4`.
Compared with text-only `work/text_qa/20261014T061730Z-8c20bcb9` and full hybrid `work/hybrid_qa/20261014T061415Z-0d56a1a6`.

## Processing result and source findings

All three cases produced non-abstaining answers on their first attempt, with zero execution failures.

| Case | Retrieval | Output tokens | Case time | Source review |
| --- | --- | --- | --- | --- |
| LockBit Affiliates / AnyDesk | Five three-hop paths; 13 passages | 273 | 4.08 seconds | Lists all five mitigation names and IDs with correct identity/description citation pairs. Actor use and practical guidance remain incomplete or lose source qualifications. |
| BianLian / Rclone | One one-hop path; one passage | 60 | 0.88 seconds | Supported exfiltration purpose, but omits the controlled cloud account, same-service detail and detection-avoidance purpose. |
| ALPHV affiliates / Evilginx2 | One one-hop path; one passage | 142 | 1.89 seconds | All requested items are supported: MFA credentials, login credentials and session cookies. The answer repeats the actor/software wording across three claims. |

Times include retrieval, packing and generation, excluding initialization. They are individual development observations, not benchmark averages. One-hop paths are appropriate for the two direct actor/software questions.

## AnyDesk semantic limitations

The complete supporting row and all five mitigation descriptions are present in the evidence. Missing answer details therefore cannot be attributed to absent retrieved source passages in this case.

- The opening claim attributes remote connections to LockBit Affiliates. That wording comes from the intended-use column; the reported repurposed use is remote control of victim devices, which the answer omits. The table roles should remain distinct.
- M1031 says prevention is possible but omits the network-signature mechanism and changes the source's qualified “may be able” wording to “can.” The guidance lacks the actual prevention-system action.
- M1034 omits the condition that IP-based KVM devices should be blocked if not required.
- M1037 lists firewalls, application firewalls and proxies but omits what their configuration should accomplish: limiting outgoing traffic to sites and services used by remote access software.
- M1038 retains application control and the source's “mitigate” wording, but omits the restriction to software usable for remote access.
- M1042 retains the main action, but omits the examples of unapproved installations and features built into supported applications.

The mitigation citations support their identities and the underlying actions, but these omissions prevent treating the response as fully faithful and complete practical guidance.

## Current matching-generator comparison

| Development observation | Text-only | Graph-only | Full hybrid |
| --- | --- | --- | --- |
| AnyDesk mitigation identities listed | One of five | Five of five | Five of five |
| AnyDesk guidance limitations | Omits application control and remote-access scope; strengthens mitigation to prevention | Omits source conditions, mechanisms or destination scope | Omits source conditions, mechanisms or destination scope |
| AnyDesk relevance/actor wording | Adds three unrelated tool statements; separates general capability from actor remote control | Uses intended-use wording for actor use and omits remote control | Combines intended and repurposed uses |
| Rclone purpose | Cloud exfiltration; avoidance details omitted | Exfiltration only; cloud and avoidance details omitted | Cloud exfiltration; avoidance details omitted |
| Evilginx2 requested items | All three | All three | All three |

The matching runs share generator v2, questions, Ollama model digest and generation options. Graph-only already recovers all five mitigation references without Node2Vec. These observations do not establish a Node2Vec quality benefit. The remaining no-Node2Vec run will complete the four-mode development check; repeated controlled held-out evaluation is still required for final claims.

Recorded graph-only configuration hash: `19cfcbb4c5e4f0df515355986387cd3869d3081173b3c61cea836b9319a94af0`. Shared generator: `development-shared-cited-generator-v2`. Model: `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`. Temperature 0; context 8192; output limit 700; maximum one repair. ATT&CK release: 17.1.

## Next check: combined retrieval without Node2Vec

Keep Neo4j and Ollama running, then execute:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\combined_qa.py" --demo
```

Accept the connection defaults and enter the Neo4j password when prompted. This runs `hybrid_no_node2vec` with the same three development questions and shared v2 generator. New records are saved in `S:\ThreatWeave\work\combined_qa`; the generated review document is saved in `S:\ThreatWeave\docs`. Prior runs are preserved.

After source review, consolidate the four matching-generator development results. Full-corpus ingestion, extraction scoring, application integration and final evaluation remain unfinished.
