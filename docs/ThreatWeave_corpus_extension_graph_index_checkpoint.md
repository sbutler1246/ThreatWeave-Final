# Three-report extension: graph index checkpoint

October 15, 2026. Operator run `work/graph_index_runs/20261016T003953Z-4ad94e21` completed with status `ready` at 7:39 p.m. America/Chicago. The matching development text/graph refresh is complete. Human verification remains pending.

The saved build contains 142 domain nodes, 245 accepted directed facts, 245 undirected training edges and 142 normalized 128-dimensional vectors. Component sizes are `[133, 5, 2, 2]`. The receipt records 1,420 walks and 142 successful exact-vector lookups using the frozen training parameters.

Graph index fingerprint: `01001b3705b49fd95fb1acb11b4ea1695cc11090bf96093df0eca0217f02402c`.

Live saved projection SHA-256: `1c31caf80589a8fcd1ab03433c8426be7d7348b13d6fee93133307ad239b1090`.

The published current pointer selects this manifest. Its accepted scope matches the [305-chunk text index](ThreatWeave_corpus_extension_text_index_checkpoint.md): 53 CISA windows and 139 direct ATT&CK reference parents, scope SHA-256 `ab3732f875177906c400d82268fbbeed719b9a26b4f3836215d713821bd9beb8`.

Offline audit: `work/graph_index_review_checks/20261016T004058Z-a944c70b/audit.json`. It verifies the ready receipt/current pointer, manifest identity and runtime, frozen training code/settings, projection/vector file hashes, all node/vector bindings, finite arrays and normalization, components, recorded exact-vector lookups, and source-provenance reconstruction of the entire saved projection. No live service or index query was issued by the assistant. Stored Chroma verification and live graph rechecking are recorded by the operator build; file inspection does not establish later live graph state.

The projection retains 263 assertion supports: 124 extracted and 139 fused. Of these, 253 record human review pending; ten original-development supports have no recorded human-review field. This includes all 114 reviewed pilot/batch/extension source assertions. Offline integrity verification does not confer human verification or establish embedding quality.

Restart the existing application server with `run_application.py` to load the refreshed code and assets. Stop an older server with Ctrl+C first. No further development demonstration round is needed for this refresh. Previous snapshots, collections, runs and generated answers remain saved.

The next substantive milestone is evaluation preparation: freeze the experiment protocol and source-only evaluation corpus workflow, finish the resumable four-mode runner/evaluator integration, and prepare blinded human scoring. Held-out references remain evaluator-only inputs. Missing-fact coverage assessment, human verification, final experiments, analysis and reporting remain unfinished.
