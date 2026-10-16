# Additional development batch: graph index checkpoint

October 15, 2026. Operator run `work/graph_index_runs/20261015T230431Z-ce56e0cd` completed with status `ready` at 6:04 p.m. America/Chicago. The live accepted graph was projected, frozen Node2Vec settings were fitted, and a separate versioned collection was published after verification. Human verification remains pending.

| Saved build result | Count |
| --- | ---: |
| CISA source windows | 41 |
| Direct ATT&CK reference parents | 96 |
| Domain nodes / stored vectors | 117 |
| Accepted directed facts | 179 |
| Undirected training edges | 179 |
| Dimensions per vector | 128 |
| Random walks | 1,170 |
| Successful exact-vector lookups | 117 |

Connected-component sizes: `[108, 5, 2, 2]`. The graph excludes Document/Chunk/Assertion hubs. Vector proximity alone does not establish a factual relationship or demonstrate a quality improvement.

Index fingerprint: `9f973e085a3fc0135bde264c156deecb56fbc682a634308d75da57882e36b15c`.

Live saved projection SHA-256: `af29a98151cfbcb0065bea8a6b9df4c6db8b4e8e81a5e251582a29df9b86c0d6`.

Manifest: `work/graph_index/9f973e085a3fc0135bde264c156deecb56fbc682a634308d75da57882e36b15c/manifest.json`.

The current pointer selects this manifest. Its shared scope SHA-256 is `ee0f8bbd4e91a65b103fe4b3190d75362e1e02f8b9b27c80db04a45b09f7beba`, matching the completed [215-chunk text index](ThreatWeave_corpus_batch_text_index_checkpoint.md).

Offline verification checked the ready receipt/current pointer, manifest identity, projection and vector-file hashes, frozen training implementation/settings/runtime, all node-ID/vector bindings, finite raw/normalized arrays, normalization and raw-to-normalized consistency. It reconstructed saved source rows and reproduced the exact live saved projection through the source verifier. Components, directed/undirected counts, 1,170 walks and all 117 recorded exact-vector lookup results match the manifest/receipt. No live service or index query was issued by the assistant.

The saved projection preserves 193 assertion supports: 97 extracted and 96 fused. Of these, 183 explicitly record human review pending; ten original-development supports have no recorded human-review field. None of these checks confers human verification. All 87 reviewed pilot/batch source assertions remain represented, including original-generation and offline-recovery provenance where applicable.

The live saved projection hash differs from the source-fixture preview hash because fixtures use synthetic assertion identities for the original six development scopes. Expected domain counts match, and independent verification of the actual saved projection passed. The operator build receipt also records rechecking the live graph after fitting; the assistant's file inspection does not establish its later live state.

Both matching indexes are ready for the expanded development application. [Restart the application to load them](ThreatWeave_corpus_batch_application_step.md). Earlier collections, source snapshots and generated answers remain preserved. No additional four-mode demonstration is required for this index-refresh checkpoint. Broader corpus coverage assessment/completion, human verification and controlled held-out quality/performance evaluation remain unfinished.
