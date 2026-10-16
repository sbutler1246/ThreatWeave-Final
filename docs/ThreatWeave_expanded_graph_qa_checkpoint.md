# Expanded graph-only QA development checkpoint

AI-assisted source review, October 15, 2026 (America/Chicago). Run: `work/graph_qa/20261015T070142Z-5b1a5398`. The [generated review](ThreatWeave_graph_qa_20261015T070142Z-5b1a5398.md), original evidence, prompts and responses remain unchanged, with human semantic verification pending. These are development observations, not held-out scores.

## Processing and integrity

All three cases produced non-abstaining answers on their first generation attempt, with no execution failures or repairs. Retrieval used accepted source-supported directed graph paths, without text-vector search or Node2Vec expansion.

| Case | Selected paths | Exact source passages | Context bytes / 3000 | Output tokens | Case time |
| --- | --- | ---: | ---: | ---: | ---: |
| Raccoon Stealer | Four three-hop paths | 12 | 2795 | 304 | 4.822 s |
| Rhysida actors | Five two-hop paths | 13 | 2699 | 353 | 4.903 s |
| ALPHV affiliates | Two one-hop paths | 3 | 415 | 109 | 1.583 s |

Times include per-case retrieval, packing and generation, excluding retriever initialization and initial service checks. They are single observations, not controlled latency averages.

Independent offline audit: `work/qa_review_checks/20261015T070309Z-3ec6da63/audit.json`. All 28 supplied passage texts/offsets and URLs match freshly verified frozen sources. All 13 claims have valid citation bindings; saved raw responses reproduce displayed answers; prompt hashes, question records, path counts/hops and current graph retrieval configuration match. Questions, shared generator, model digest and options match the completed expanded full-hybrid and text-only runs. The assistant made no live service calls. Structural checks do not establish semantic entailment.

## Source review

**Raccoon Stealer:** CISA E4 directly supports theft of login credentials, browser history and cookies. The extra E1 citation provides table context. All four supplied mitigation identities and guidance pairs appear: User Training M1017 (E5/E6), Restrict Web-Based Content M1021 (E7/E8), Multi-factor Authentication M1032 (E9/E10) and Audit M1047 (E11/E12). Observation and reference citations remain separate.

The MFA claim preserves the proxy-method restriction but omits the necessary domain-binding negotiation condition, referring only to a physical second-factor key. It also omits the separate Conditional Access/Token Protection guidance. Other summaries omit domain-mismatch phishing specifics, browser security settings/extensions and impossible-travel/anomalous-login monitoring. Thus the observation and all supplied mitigation identities are covered, with remaining practical-detail and scope limitations. Four retrieved references are not an exhaustive T1539 mitigation catalog.

**Rhysida actors:** CISA E1 supports authentication to internal VPN access points using compromised valid credentials. The answer retains the actor qualifier and T1078 while compressing the source's commonly-observed framing. All five supplied mitigation identities and guidance pairs appear: Application Developer Guidance M1013, Active Directory Configuration M1015, User Training M1017, User Account Management M1018 and Privileged Account Management M1026. The push-notification claim preserves the restriction to accept only valid notifications. M1026 mentions default accounts and general network administration but omits checking unauthorized new local accounts and the explicit mechanism of limiting privileged account use across administrative tiers. Coverage is complete for the supplied identities, not for every detail or every possible reference.

**ALPHV affiliates:** E1 supports the use of AnyDesk and Mega sync after network access, in preparation for exfiltration. Both tool claims retain the affiliate qualifier and have direct source support. They omit the remote-access deployment role and after-access context. E2/E3 add report/section context rather than further behavioral evidence. The answer uses one claim per tool, without the additional combined restatement seen in the text-only output; these two tool-specific claims could still be combined concisely.

## Comparison so far

The graph-only contexts supplied the CISA observations absent from the first two text-only contexts, and the generated incident statements are supported. The text-only run instead inferred unsupported incident claims from reference guidance. Full hybrid also supplied supported observations, but omitted the supplied Rhysida M1018 reference; graph-only includes M1018 within its different selected reference subset. For Raccoon, graph-only selects Audit M1047 where full hybrid selects Update Software M1051, and both retain practical-guidance limitations. These differences must be assessed against each condition's actual evidence, rather than treating all contexts as identical.

No general mode ranking or Node2Vec benefit is established by these three development questions. The remaining hybrid-without-Node2Vec run is needed before the four-mode comparison. Gold triples and reference answers are not pipeline inputs.

## Matching settings and next step

Later checkpoint: [the final combined run and four-mode comparison are complete](ThreatWeave_expanded_four_mode_development_comparison.md). No additional demonstration is needed for this checkpoint. The settings and original next-step statement below remain as history.

- Generator: `development-shared-cited-generator-v2`; model `llama3.1:8b`.
- Model digest: `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`.
- Options: temperature 0, context 8192, output limit 700, one allowed repair.
- Shared source scope: `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c` (16 CISA parents and 58 reference parents).
- Graph-only retrieval configuration: `904f945596bce6a8d6e50a622168f7b056a204121f627a896f313af085570f36`.

[Run matching hybrid QA without Node2Vec next](ThreatWeave_expanded_combined_qa_step.md). Its offline preview passed all three questions. Keep questions, sources, model and generator unchanged while completing the comparison. No implementation changed; the prior 175-test result remains the latest suite result. Human verification, broader extraction, application integration and controlled final evaluation remain unfinished.
