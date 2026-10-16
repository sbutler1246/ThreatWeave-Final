# Additional development batch: text index checkpoint

October 15, 2026. Operator run `work/text_index_runs/20261015T225013Z-42adf966` completed with status `ready`, verifying 215 stored chunks and 384-dimensional vectors across 41 CISA source windows and 96 direct ATT&CK reference parents. Its recorded completion time is 5:50 p.m. America/Chicago. Human verification remains pending.

Index fingerprint: `e4e7eae1cfbeaf13d1971eeba88717e3754c780239604b3c9444a5223806875e`.

Collection: `threatweave_text_dev_e4e7eae1cfbeaf13`.

Saved records: `work/text_index/e4e7eae1cfbeaf13d1971eeba88717e3754c780239604b3c9444a5223806875e/records.json`.

Records text SHA-256: `05fd8a7a73a67c5d44f991bca22a92845e35b2ba8c952e84d9bf404f826a594b`.

Offline inspection reconstructed all 215 records using the cached tokenizer and verified exact equality with the saved records, manifest checksum, scope fingerprint, frozen embedding revision/chunking settings, run receipt and all fifteen saved ranked hits. Maximum embedding input remains 240 WordPieces and 1000 characters including inherited source context. All three saved hit lists have five records in ascending finite cosine-distance order. This inspection did not open Chroma or make new service/model queries; stored vector validation is recorded by the operator-run build receipt.

| Existing development smoke question | Saved top-five evidence | Source inspection |
| --- | --- | --- |
| Raccoon Stealer and web-session-cookie mitigations | Five ATT&CK references | No CISA observation appears in the saved top five. Incident-specific theft claims still lack CISA support in this text-only evidence. |
| Rhysida valid-account access, T1078 | Four ATT&CK references and one CISA chunk | Rank 2 includes the explicit statement that Rhysida actors use valid credentials to access victims' internal VPN access points. |
| ALPHV AnyDesk and Mega sync before exfiltration | Five CISA chunks | Rank 2 directly names AnyDesk, Mega sync and Splashtop as remote-access software deployed in preparation for exfiltration. Other results include adjacent context and an unrelated IOC/table span. |

The Rhysida source hit is present in this expanded run where the earlier index's saved top five contained only references. No retrieval settings were changed. These observations describe saved evidence coverage, not generated-answer quality, controlled comparisons or final benchmark scores. Neighboring text and incomplete evidence remain limitations.

The matching source-derived graph preview passed: 117 domain nodes, 179 directed facts, 179 undirected edges and connected-component sizes `[108, 5, 2, 2]`. This establishes the expected projection; live graph verification and vector fitting require the operator's next run.

[Rebuild the matching graph-vector index next](ThreatWeave_corpus_batch_graph_index_step.md). Prior index collections and generated answers remain saved. Full-hybrid application queries await the matching graph-vector refresh. Broader corpus completion, human verification and held-out evaluation remain pending.
