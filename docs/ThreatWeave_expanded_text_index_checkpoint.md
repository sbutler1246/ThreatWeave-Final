# Expanded development text index checkpoint

October 14, 2026 (America/Chicago). User-run build: `work/text_index_runs/20261015T042635Z-94f0293b`. The directory timestamp is UTC.

The build receipt is **ready** and records verification of **95 source chunks and 384-dimensional stored vectors**, covering **16 CISA source parents and 58 direct ATT&CK reference parents**. The maximum embedding input is 240 WordPieces and 1000 characters, including inherited context. The build uses the cached MiniLM revision and normalized cosine vectors in a separate fingerprinted collection; prior collections remain preserved.

Text fingerprint: `607e1e265093bfc94fa6d7f4ddcb5317bc722705859ad6c5d0440ef8279adc5f`.

Shared development scope SHA-256: `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c`.

Saved source-record SHA-256: `3da5feed2e87916b4718b2b29970e4b45e202d789897d673c6bbf16fd38f4bd5`.

Collection: `threatweave_text_dev_607e1e265093bfc9`. Manifest and source records are under `work/text_index/<fingerprint>`. [The generated build review](ThreatWeave_text_index_20261015T042635Z-94f0293b.md) preserves all ranked hits. Its original output and receipt remain unchanged.

## Ranked retrieval findings

| Development question | Top five source types | Finding |
| --- | --- | --- |
| Raccoon Stealer information theft and cookie-theft mitigations | Five ATT&CK references; zero CISA passages | All five concern T1539: M1047, M1054, M1021, M1032 and M1017. The source observation about Raccoon Stealer is absent from these hits. |
| Rhysida valid-account access / T1078 and mitigation guidance | Five ATT&CK references; zero CISA passages | All five concern T1078: M1018, M1036, M1013, M1026 and M1015. The CISA access observation is absent from these hits. |
| ALPHV affiliates using AnyDesk and Mega sync before exfiltration | Five CISA passages; zero ATT&CK references | All hits come from the ALPHV report, including the two pilot parents and the earlier development prose parent. Rank one is the later pilot window; relevant report identity alone does not establish that it contains the requested use assertion. |

These checks establish stored source integrity and successful retrieval execution, not complete question coverage or answer correctness. The first two questions require both incident observations and reference guidance; their top-five text hits provide only the latter. The fixed five-candidate baseline remains unchanged. Future generated-answer review must check whether it acknowledges missing evidence rather than inventing actor behavior. No generated answers, formal context-recall scores or final benchmark results were produced by this build.

The saved receipt, expanded source fingerprint/configuration, index manifest, all 95 saved source records and all 15 ranked hit records were independently compared with fresh offline source preparation. They match. The assistant did not query Neo4j/Ollama or reinstall anything. The latest 175-test suite already passed; this receipt/documentation step changes no implementation.

## Next step

Later checkpoint: [the expanded graph index completed](ThreatWeave_expanded_graph_index_checkpoint.md), including the actual persisted-index full-hybrid preview. [Fresh generated QA](ThreatWeave_expanded_qa_step.md) is next. The graph-pending statements below record the state at the text-index checkpoint.

The graph source-fixture preview still passes with **75 expected domain nodes, 102 directed facts and 102 undirected edges**, with connected components of sizes 71, 2 and 2. This does not establish current live graph presence. [Rebuild the live graph-vector index](ThreatWeave_expanded_graph_index_step.md) next, preserving 128 dimensions and the frozen Node2Vec parameters. The command reads Neo4j without inserting facts and publishes a fresh Chroma graph-vector index only after source/storage/freshness checks.

Expanded graph fitting and fresh matching four-mode generated QA remain pending. The completed text build does not finish broader extraction, overlap/resource evaluation, the application UI or controlled held-out evaluation. Gold triples and QA reference answers are not pipeline inputs.
