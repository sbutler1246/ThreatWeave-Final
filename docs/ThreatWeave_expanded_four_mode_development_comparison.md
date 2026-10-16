# Expanded four-mode development comparison

Completed October 15, 2026 (America/Chicago). All four planned development runs are collected and their saved answers/evidence have undergone AI-assisted inspection. **All 12 cases produced non-abstaining answers on their first attempt, with zero execution failures or repairs.** This completes this comparison checkpoint; no additional demonstration run is required for it. Human semantic verification and controlled final evaluation remain unfinished.

## Runs and matching conditions

| Mode | Saved run | Generated claims |
| --- | --- | ---: |
| Text only | `work/text_qa/20261015T065624Z-68b5c1cc` | 16 |
| Graph only | `work/graph_qa/20261015T070142Z-5b1a5398` | 13 |
| Hybrid without Node2Vec | `work/combined_qa/20261015T070609Z-60180e2e` | 19 |
| Full hybrid | `work/hybrid_qa/20261015T043615Z-462852fb` | 16 |

Every mode used the same three source-based development questions about Raccoon Stealer, Rhysida actors and ALPHV affiliates, and the same shared generator `development-shared-cited-generator-v2`. Model: `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`. Options: temperature 0, context 8192, output limit 700, maximum one repair. Responses allow at most eight claims, 280 characters per claim and four citations per claim.

The shared pool contains 16 CISA source parents and 58 direct frozen ATT&CK reference parents. Its scope SHA-256 is `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c`. Text-enabled modes share index `607e1e265093bfc94fa6d7f4ddcb5317bc722705859ad6c5d0440ef8279adc5f` (95 chunks, 384 dimensions). Full hybrid uses graph index `da85cd77a7811edf7d5ca4e9db82a2a6b1669ef614f9d0115483bbb3124a8fc0` (75 nodes, 128 dimensions) and projection `3b5d61276de1b58773079a2c80dcac52d1c00eeeafbb73c68d3956e244678982` (102 accepted directed facts). Graph-only retrieval does not use either vector index.

The independent offline aggregate audit is saved at `work/qa_review_checks/20261015T070808Z-61d0afa2/audit.json`. It rechecked all 12 saved cases, **118 passage occurrences** against freshly verified frozen document spans/URLs, **64 claims** for valid citation bindings, raw response/displayed answer agreement, prompt hashes, question/mode records and shared model/generator settings. Repeated passages across cases/modes are counted as occurrences, not 118 unique sources. The assistant made no live service calls. Valid source spans and citation IDs do not prove claim entailment.

All original run records and generated reviews retain their pending human semantic-review status. No gold triples or QA reference answers were inputs to retrieval or generation. Earlier six-scope demonstrations use different questions/evidence and remain historical rather than matching baselines for this expanded comparison.

## Source review across modes

| Development case | Text only | Graph only | Hybrid without Node2Vec | Full hybrid |
| --- | --- | --- | --- | --- |
| Raccoon information theft and cookie-theft guidance | No CISA passage supplied; opening falsely attributes actor/software behavior to CISA. Five supplied mitigation identities covered; proxy-method scope and token binding retained. | CISA observation supported; all four supplied mitigation identities covered. MFA proxy restriction retained, but domain-bound negotiation condition and token binding omitted. | CISA observation supported; all four supplied mitigation identities covered. Domain-bound key mechanism retained, with other guidance details omitted. | CISA observation supported; all four supplied mitigation identities covered. MFA claim loses proxy-method restriction and omits token binding. |
| Rhysida valid-account access and guidance | No CISA passage supplied; opening infers Rhysida behavior from an account-management recommendation. All five supplied mitigation identities covered. | Compromised-credential VPN observation supported; all five supplied mitigation identities covered. Operational details compressed. | VPN observation supported; all five supplied mitigation identities covered. Operational details compressed. | VPN observation supported; five of six supplied mitigation identities covered, with M1018 omitted despite available evidence. |
| ALPHV AnyDesk/Mega sync use | Core tool-use observation supported, with a redundant combined restatement, unnecessary citation and missing deployment/context details. | Both tool-use observations supported in two claims, with deployment/context details omitted. | Core observation supported but repeated; five extra claims drift into other report activity, including an unclear installation clause. | Core observation supported but repeated; additional supported exfiltration detail. |

These findings assess claims against each mode's actual supplied context. Covering all supplied mitigation identities does not mean preserving every practical detail or retrieving every relevant reference. The text-only incident statements are unsupported by their supplied evidence even if some words overlap facts elsewhere in the frozen corpus. The generator should have acknowledged missing incident evidence while answering the supported reference portion.

Detailed earlier source inspections are preserved in the [text-only checkpoint](ThreatWeave_expanded_text_qa_checkpoint.md), [graph-only checkpoint](ThreatWeave_expanded_graph_qa_checkpoint.md) and [full-hybrid checkpoint](ThreatWeave_expanded_hybrid_qa_checkpoint.md).

## Final no-Node2Vec run review

The [generated combined review](ThreatWeave_combined_qa_20261015T070609Z-60180e2e.md) records mode `hybrid_no_node2vec`, with Node2Vec disabled. Its retrieval configuration hash is `d79f99952d7f78fcd4e5f161a97f726ea14e8743417666a0978e1cf19826f513`. All three cases record live Neo4j graph evidence; the subsequent audit used saved files only.

| Case | Graph paths | Selected text hits | Supplied passages | Context bytes / 3000 | Output tokens |
| --- | --- | ---: | ---: | ---: | ---: |
| Raccoon Stealer | Four three-hop paths | 4 | 12 | 2795 | 333 |
| Rhysida actors | Five two-hop paths | 4 | 13 | 2699 | 362 |
| ALPHV affiliates | Two one-hop paths | 3 | 6 | 2306 | 367 |

**Raccoon:** E4 directly supports login-credential, browser-history and cookie theft. The four identity/guidance pairs are Audit M1047 (E5/E6), Restrict Web-Based Content M1021 (E7/E8), User Training M1017 (E9/E10), and Multi-factor Authentication M1032 (E11/E12). The answer keeps the domain-bound negotiation mechanism without making a broad prevention claim, but omits the explicit proxy-method explanation and separate token-binding guidance. It compresses anomalous/impossible-travel monitoring, browser security settings and domain-mismatch phishing details. The reference subset equals graph-only's; the source passage order differs.

**Rhysida:** E1 supports the compromised-credential VPN observation. The five supplied pairs are Application Developer Guidance M1013 (E4/E5), User Account Management M1018 (E6/E7), Active Directory Configuration M1015 (E8/E9), Privileged Account Management M1026 (E10/E11), and User Training M1017 (E12/E13). All identities appear with supported core actions. M1026 omits explicit unauthorized-new-account checks and the mechanism of limiting privileged use across administrative tiers. Its source passage set also equals graph-only's, in a different order.

**ALPHV:** E1 supports the requested AnyDesk/Mega sync deployment purpose. The first three claims restate that observation. The remaining five concern account creation/token generation, Evilginx2, Metasploit, log clearing and Mega.nz/Dropbox. Their core activity descriptions appear in E4–E6, but they are outside the requested tool-use explanation. The log-clearing claim says “After installing on the domain controller” without identifying what was installed; the cited source also has an unclear antecedent, so the answer must not infer a specific installed tool. All eight claim slots are used, although the raw generation ends normally after 367 output tokens rather than reaching the 700-token limit. Schema compliance did not enforce focus or semantic non-repetition.

## Retrieval and Node2Vec interpretation

For Raccoon and Rhysida, the no-Node2Vec condition selected the same exact source-passage sets as graph-only, in different orders. Its selected text hits did not add unique source spans beyond the graph evidence for those cases. Full hybrid selected different mitigation subsets: for Raccoon it substitutes M1051 for M1047; for Rhysida its context contains six reference identities, of which the answer omits M1018.

Full hybrid's base/expansion/merged path-candidate counts were 17/17/17 for Raccoon, 9/5/9 for Rhysida and 2/0/2 for ALPHV. Neighbor matching added **no unique candidate paths** beyond the base sets in these cases. Structural priority could still change ordering/packing; similarity itself never establishes an incident fact.

For ALPHV, full hybrid and no-Node2Vec supplied exactly the same passages in the same order. Their saved generation prompts differ only in the `MODE` label. They nevertheless produced different claim counts and amounts of unrelated detail. The model sees that mode label, so this case does not isolate a retrieval effect, and output differences cannot be attributed to additional Node2Vec evidence.

This comparison demonstrates a text-retrieval coverage gap and failure to acknowledge missing evidence in two cases, supported incident coverage in graph-enabled contexts, and persistent generation limitations. It does **not** establish a general mode ranking or a Node2Vec quality advantage. Formal precision, recall, F1, human ratings and statistical significance have not been measured here.

## Single-run case times

| Case | Text only | Graph only | Hybrid without Node2Vec | Full hybrid |
| --- | ---: | ---: | ---: | ---: |
| Raccoon Stealer | 14.220 s | 4.822 s | 4.903 s | 8.824 s |
| Rhysida actors | 4.538 s | 4.903 s | 5.077 s | 5.031 s |
| ALPHV affiliates | 2.145 s | 1.583 s | 5.068 s | 3.633 s |

These times include per-case retrieval/packing/generation, excluding initialization. Runs were sequential, with different output lengths and no randomized repeated timing or matched warmup protocol. They do not establish reliable performance rankings or full-corpus throughput.

## Checkpoint complete and remaining project work

The planned four-mode development cycle is complete. Original imperfect answers remain preserved; no generator, retrieval settings or source records were changed to improve this comparison. No implementation changed during the receipt/review steps, so the previous 175-test result remains the latest suite result. No additional live run is requested for this checkpoint.

The full project still requires broader source extraction/review/ingestion, application integration and the planned interface, human semantic verification, and controlled held-out quality/performance evaluation. The current accepted pilot covers ten reviewed extraction windows, not the full prepared corpus. Final documentation must distinguish this development checkpoint from those unfinished stages.

For a later implementation cycle, prioritize explicit handling of missing incident evidence, preservation of mitigation conditions, concise non-repeating requested claims, and the mode-label confound in any causal retrieval comparison. Those changes have not been implemented here; changing the shared generator would require new matching results under a new version. Benchmark gold/reference answers must remain evaluation-only inputs.
