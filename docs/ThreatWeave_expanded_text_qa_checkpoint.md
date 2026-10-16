# Expanded text-only QA development checkpoint

AI-assisted source review, October 15, 2026 (America/Chicago). Run: `work/text_qa/20261015T065624Z-68b5c1cc`. The [generated review](ThreatWeave_text_qa_20261015T065624Z-68b5c1cc.md), original prompts, responses, evidence and receipts remain unchanged, with human semantic verification pending. This checkpoint records development findings, not final benchmark scores.

## Processing and integrity

All three cases produced non-abstaining answers on their first generation attempt, with zero execution failures or repairs. The first two answers nevertheless contain unsupported incident claims.

| Case | Selected text chunks | Source passages | Source types | Context bytes / 3000 | Output tokens | Case time |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| Raccoon Stealer / web session cookies | 5 | 10 | ATT&CK only | 2489 | 445 | 14.220 s |
| Rhysida actors / valid accounts | 5 | 10 | ATT&CK only | 1880 | 333 | 4.538 s |
| ALPHV affiliates / AnyDesk and Mega sync | 4 | 6 | CISA only | 2971 | 141 | 2.145 s |

All cases have zero graph paths. Times include query embedding, retrieval, packing and generation, excluding model/index initialization. These single observations do not establish comparative speed or final latency averages.

The independent offline audit at `work/qa_review_checks/20261015T065849Z-65ea99e6/audit.json` passed structural/source-integrity checks: all 26 supplied passage texts and offsets match freshly verified frozen source documents, source URLs match, all 16 claims have valid citation bindings, saved raw responses reproduce displayed answers, and all three prompt hashes match. It also records the semantic failures separately. A valid citation binding means that the ID exists in the evidence; it does not mean the text supports the claim. The assistant called neither Ollama nor Neo4j.

## Source review

### Raccoon Stealer

The opening claim attributes Raccoon Stealer behavior to CISA, listing login credentials, session cookies and other sensitive data, but cites E1: an ATT&CK auditing recommendation about detecting stolen cookies. No supplied passage identifies Raccoon Stealer or provides a CISA observation. This is unsupported attribution and incident content, not a supported partial answer. The generator should have acknowledged that the incident observation was unavailable while answering the supported reference portion.

All five supplied mitigation identities appear with their correct IDs and identity/guidance citation pairs: Audit M1047, Software Configuration M1054, Restrict Web-Based Content M1021, Multi-factor Authentication M1032 and User Training M1017. Their core practical actions are supported. The answer preserves the proxy-method restriction for the physical second factor and includes the separate token-binding guidance, which the full-hybrid answer omitted or broadened. It splits MFA guidance into two claims despite the prompt's one-claim-per-mitigation preference. It compresses auditing anomalies, cookie lifetime/non-persistence, browser security settings and domain-mismatch phishing details. This is coverage of the supplied five references, not all possible T1539 mitigations.

### Rhysida actors

The opening claim says Rhysida actors gain access by exploiting inactive or unnecessary accounts, citing E1. E1 recommends auditing accounts and removing those no longer needed; it does not describe Rhysida activity. No CISA passage is supplied. The answer converts general defensive guidance into an actor-specific observation and does not acknowledge the evidence gap.

The remaining five mitigation claims are supported by the supplied identity/guidance pairs: User Account Management M1018, Account Use Policies M1036, Application Developer Guidance M1013, Privileged Account Management M1026 and Active Directory Configuration M1015. All five supplied identities appear. The M1026 summary omits checks for enabled default/unauthorized accounts and restrictions on privileged use across administrative tiers. The unsupported opening remains a material error despite useful reference guidance.

### ALPHV affiliates

E4 directly supports deployment of remote access software including AnyDesk and Mega sync after network access, in preparation for exfiltration. All three claims retain the affiliate qualifier and are supported in their core observation by E4. However, the two individual tool claims and their combined restatement are semantically repetitive, and they omit the explicit remote-access deployment description and after-access context. The additional E1 citation describes later exfiltration and other activity, not the requested AnyDesk/Mega sync deployment; it adds no direct support for those claims.

## Comparison with the expanded full-hybrid run

The questions, shared generator version, model digest, generation options and text-index fingerprint match [the expanded full-hybrid run](ThreatWeave_expanded_hybrid_qa_checkpoint.md). Retrieval configuration hashes differ by condition as intended. The shared evidence pool is unchanged, but each condition selects a different bounded evidence context.

| Case | Full hybrid | Text only |
| --- | --- | --- |
| Raccoon Stealer | Retrieved and cited a supporting CISA observation; four supplied mitigation identities covered, with a broadened MFA claim and omitted details. | No CISA observation retrieved; invented CISA attribution in the opening. Five supplied mitigation identities covered; proxy-method scope and token binding retained. |
| Rhysida actors | Retrieved and cited the compromised-credential VPN observation; omitted supplied M1018 guidance. | No CISA observation retrieved; inferred actor behavior from an account-management recommendation. All five supplied mitigation identities covered. |
| ALPHV affiliates | Supported deployment/purpose observation, with repetition and additional supported exfiltration detail. | Supported but repetitive core observation, with less deployment/context detail and an unnecessary citation. |

The first two text contexts lacked incident evidence and the generator failed to limit its answer accordingly. Full hybrid supplied that missing evidence in these cases, but it also had generation limitations. Different retrieved mitigation subsets and incomplete four-mode results prevent a general quality conclusion. These observations do not establish a Node2Vec benefit; the no-Node2Vec comparison remains pending. No gold triples or reference answers entered retrieval or generation.

## Recorded settings and next step

Later checkpoint: [matching graph-only QA completed](ThreatWeave_expanded_graph_qa_checkpoint.md). [Hybrid without Node2Vec](ThreatWeave_expanded_combined_qa_step.md) is next. The settings and original next-step statement below remain as history.

- Generator: `development-shared-cited-generator-v2`; model `llama3.1:8b`.
- Model digest: `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`.
- Options: temperature 0, context 8192, output limit 700; one allowed repair.
- Shared source scope: `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c` (16 CISA parents and 58 reference parents).
- Text index: `607e1e265093bfc94fa6d7f4ddcb5317bc722705859ad6c5d0440ef8279adc5f`.
- Text-only retrieval configuration: `da9c0ee5dc2081b37d87b5a9bc05dfe0cfe3a891db95e7084c755f9d5d949500`.

Keep generator/retrieval settings and sources unchanged while collecting the remaining conditions. [Run matching graph-only QA next](ThreatWeave_expanded_graph_qa_step.md), then hybrid without Node2Vec. Preserve these unsupported claims in the comparison before considering generator or evidence-coverage changes. The graph-only source-fixture preview passed for all three questions. No implementation changed; the previous 175-test result remains the latest suite result. Human verification, broader extraction, application integration and controlled final evaluation remain unfinished.
