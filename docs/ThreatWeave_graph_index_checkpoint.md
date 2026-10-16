# Live development graph-vector checkpoint

The local receipt `work/graph_index_runs/20261014T043130Z-d379a905/index_receipt.json` confirms successful fitting and indexing from the live Neo4j development graph. Its UTC timestamp corresponds to the evening of October 13, 2026 in America/Chicago.

- 22 verified domain nodes; 23 accepted directed facts; 23 undirected projection edges.
- Connected-component sizes: 18, 2 and 2, calculated with NetworkX for this saved projection.
- 22 normalized 128-dimensional vectors stored in a separate graph collection; all 22 exact-vector lookups passed.
- 220 generated walks using the configured Node2Vec parameters, seed 42 and one worker.
- Graph revision verified again after fitting/storage before publishing the ready manifest.

Projection SHA-256: `0c2f3e01a65befef413411e7fb236bcb8dd72604e412c0c91651a7c82df5cdc5`.
Graph-index fingerprint: `07df4575ac49de6962341dca1887fe207f952c89b9c8452ad48906094efe8b8d`.
Collection: `threatweave_graph_dev_07df4575ac49de69` under `work/chroma`.
Raw vector SHA-256: `e4e2957ed6846346183d4efe6076be94c346b345b49fc676fe375b54b25fbbed`.
Normalized vector SHA-256: `349ec853ca00605e342fbd8db91af62685f579e3eb76bf67fe9266839282e613`.

The ready manifest, projection, node-ID map and raw/normalized arrays are saved under `work/graph_index/07df4575ac49de6962341dca1887fe207f952c89b9c8452ad48906094efe8b8d`.

This checkpoint establishes a live, source-verified development graph index. Exact-vector matches establish storage integrity, not useful neighbor relevance or improved answer quality. The scope remains six CISA development passages and their direct ATT&CK references. Full-corpus indexing and held-out evaluation remain pending.

Next: use this index for bounded Node2Vec neighbors in full hybrid QA, require accepted directed typed paths for every structural candidate, and check the live graph revision on each question. The existing `hybrid_no_node2vec` mode remains a separate comparison condition.
