# Additional development batch: accepted retrieval scope

October 15, 2026. The source and direct ATT&CK mitigation imports completed. Offline reconstruction verified both saved plans and receipts. Human verification remains pending.

Source import: `work/corpus_batch_ingestion/20261015T173114Z-643927a9`, with 53 verified assertions across 25 windows, 52 target entities and 45 distinct factual relationships. Fifteen candidates remain excluded.

Mitigation import: `work/corpus_batch_mitigations/20261015T173540Z-9792c14d`, with 51 direct references, 26 target mitigation entities, 59 source-reference combinations and four same-window three-hop chains. The transaction took 2.559 seconds including verification. These counts include reused graph records; this is one processing observation, not a benchmark average.

The shared development source loader now adds this reviewed batch after the original six scopes and ten-window pilot. Each added scope requires its completed source and mitigation receipts, exact reconstructed records, Supported source dispositions and frozen ATT&CK 17.1 references. Original validation failures and their offline-recovery metadata remain traceable in accepted assertion records. Changed or incomplete artifacts stop expansion. No gold triples or QA reference answers are used.

| Shared accepted scope | Count |
| --- | ---: |
| CISA source parents | 41 |
| Direct ATT&CK reference parents | 96 |
| Reviewed pilot and batch source assertions | 87 |
| Domain graph nodes in offline preview | 117 |
| Accepted directed facts in offline preview | 179 |
| Retrieval child chunks in cached-tokenizer preview | 215 |

The 87 reviewed source assertions comprise 34 original-pilot assertions and 53 additional assertions. Graph facts deduplicate repeated triples while retaining every distinct supporting assertion. Reference identities deduplicate shared frozen STIX relationships. The original six scopes also contribute their accepted facts. Node2Vec input excludes provenance hubs.

The existing local Rhysida actor identity appears as both `Rhysida actors` and `Rhysida Actors` in saved source windows. Scope assembly now accepts matching normalized names while continuing to check type, ATT&CK/STIX identity, release, resolution status and aliases. The expected display name follows the same ordered source records as ingestion. A different normalized name still fails. Offline graph fixtures now combine assertion IDs for repeated relationships to match the live graph representation.

Scope SHA-256: `ee0f8bbd4e91a65b103fe4b3190d75362e1e02f8b9b27c80db04a45b09f7beba`.

Offline projection SHA-256: `e2b53b7828da36f9a5737fa91be81a086eee13eb67e4a051dc5127514615607d`.

The cached-tokenizer preview passed exact span and inherited-context checks. Its maximum embedding input is 240 WordPieces and 1000 characters. Extraction, retrieval, generation and embedding settings remain frozen. Existing tests retain an explicit original-pilot scope option for historical regression checks.

All 63 distinct targeted offline checks passed after correcting one test's use of normalized rather than full provenance fields: eight new batch-scope checks, eight original expanded-scope regressions and 47 graph projection/retrieval, text chunking/retrieval, combined and hybrid checks. They verify receipt and recovery-metadata tampering, multi-support preservation, exact source parity, projection round trips, identity conflict handling, frozen settings and retrieval integrity. Service responses are simulated. `git diff --check` passed.

The previews establish local source preparation and expected scope. [The matching text index has now completed](ThreatWeave_corpus_batch_text_index_checkpoint.md), and its receipt and saved records passed offline verification. [The operator graph-vector rebuild is next](ThreatWeave_corpus_batch_graph_index_step.md). Application queries should wait until both matching indexes are ready. Broader corpus completion, human verification and controlled held-out evaluation remain unfinished.
