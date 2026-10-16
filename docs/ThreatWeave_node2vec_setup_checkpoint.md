# Node2Vec setup checkpoint

The saved receipt `work/node2vec_setup/20261014T042054Z-16a552eb/setup_receipt.json` reports a successful local setup. Its UTC timestamp corresponds to October 13, 2026 in America/Chicago.

- Python 3.12.14; node2vec 0.5.0; Gensim 4.4.0; NetworkX 3.7; NumPy 1.26.4; SciPy 1.17.1; Chroma 1.0.15.
- The synthetic eight-node, eight-edge graph produced normalized 128-dimensional vectors with the configured seed 42 and one worker.
- Two fits in the same process generated identical raw vectors and walks. Walk count: 80; walk SHA-256: `db2d3398c0b9d9a88702b0e787163faa43bd01786df8b65520cc9f506506d82a`.
- The separate Chroma graph probe stored eight vectors and reproduced its exact-vector lookup.
- The existing text index passed source/vector integrity and retrieval checks; its fingerprint remains `d183d6dfdb5313bc15e23049a7e907fae3d62342492b3658ca09c5409329b495`.

This receipt establishes synthetic dependency readiness, not a fitted ThreatWeave graph index or demonstrated full-hybrid answer quality. Repeatability was checked within one fixed-seed process, not across hardware or software versions.

Next, read and verify the accepted live development facts from Neo4j, fit the domain projection and save a separate graph-vector collection with its projection fingerprint, node-ID map and provenance. Full-hybrid retrieval integration and final evaluation remain pending.
