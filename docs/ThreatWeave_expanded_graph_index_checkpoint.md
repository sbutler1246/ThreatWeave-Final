# Expanded development graph-vector index checkpoint

The operator's completed run `work/graph_index_runs/20261015T043104Z-376501ed/index_receipt.json` reports **ready**. Its [generated review](ThreatWeave_graph_index_20261015T043104Z-376501ed.md) and original receipts remain preserved.

| Verified item | Result |
| --- | --- |
| Shared source scope | 16 CISA parents and 58 direct ATT&CK reference parents |
| Live accepted domain projection | 75 nodes, 102 directed facts, 102 undirected training edges |
| Connected-component sizes | 71, 2, 2 |
| Training walks | 750 |
| Graph vectors | 75 normalized vectors, 128 dimensions each |
| Exact-vector lookups | All 75 returned their own node |

The frozen Node2Vec settings remain walk length 20, ten walks per node, window 10, p=q=1, five epochs, five negative samples, seed 42 and one worker. Directed source-supported facts remain separately available for path validation. The operator's script checked the live projection again after fitting; the assistant's subsequent check used saved assets only.

Shared development scope SHA-256: `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c`.

Live projection SHA-256: `3b5d61276de1b58773079a2c80dcac52d1c00eeeafbb73c68d3956e244678982`.

Graph index fingerprint: `da85cd77a7811edf7d5ca4e9db82a2a6b1669ef614f9d0115483bbb3124a8fc0`.

Graph collection: `threatweave_graph_dev_da85cd77a7811edf`. Versioned manifest, saved projection and vectors reside under `work/graph_index/<fingerprint>`.

Matching [text index](ThreatWeave_expanded_text_index_checkpoint.md): `607e1e265093bfc94fa6d7f4ddcb5317bc722705859ad6c5d0440ef8279adc5f`, with 95 normalized 384-dimensional vectors. Text and graph vectors remain in separate collections.

## Independent offline retrieval check

The assistant ran `hybrid_qa.py --demo --preview` successfully using the actual persisted graph projection, Node2Vec vectors and cached MiniLM text index. Startup checked index identity, saved files, vector bindings and matching source scope. Preview reconstructed and source-validated the saved directed projection and checked its hash before retrieval. It made no Neo4j or Ollama calls and generated no answers.

| Development case | Selected graph paths and hops | Selected text hits | Source passages | Evidence UTF-8 bytes / cap | Neighbor hits | Expansion candidates |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Raccoon Stealer / web session cookies | Four three-hop paths | 3 | 12 | 2814 / 3000 | 5 | 17 |
| Rhysida actors / valid accounts | Five two-hop paths | 4 | 15 | 2954 / 3000 | 10 | 5 |
| ALPHV affiliates / AnyDesk and Mega sync | Two one-hop paths | 3 | 6 | 2306 / 3000 | 20 | 0 |

Neighbor hits and expansion candidates describe retrieval execution, not correctness or the number of unique facts added. An expansion candidate can overlap a base path. The ALPHV question found no neighbor-matched expansion candidates. Graph similarity alone never supports an incident claim. Evidence packing selected fewer than the five initial text candidates; selected text-hit counts do not establish complete answer coverage.

All 175 offline tests passed at the implementation checkpoint. No implementation changed during this receipt/documentation step, so that suite was not rerun. The actual persisted-index preview above passed. Current live graph freshness will be checked again by the operator's QA run.

## Next step

Later checkpoint: [expanded full-hybrid QA completed](ThreatWeave_expanded_hybrid_qa_checkpoint.md), including an offline source review of all three answers. [Matching text-only QA](ThreatWeave_expanded_text_qa_step.md) is next. The following paragraph preserves the prior next-step state.

Run [the fresh expanded full-hybrid demonstration](ThreatWeave_expanded_qa_step.md). Review the generated claims and citations before collecting the other matching modes. The text-only top-five searches for the first two questions omitted CISA observations; preserve that limitation when assessing partial answers or abstention. Generated-answer quality, human source review, broader extraction, application integration and final held-out evaluation remain pending. No gold triples or reference answers were supplied to retrieval or generation.
