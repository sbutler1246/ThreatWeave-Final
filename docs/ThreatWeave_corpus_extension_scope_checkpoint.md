# Three-report extension: accepted retrieval scope

October 15, 2026. Both operator imports completed and their saved plans and receipts passed offline reconstruction. Human verification remains pending.

Source import: `work/corpus_extension_ingestion/20261016T001729Z-60fdb691`, with 27 verified assertions across twelve windows, 27 target entities, 23 distinct factual relationships and nineteen excluded candidates.

Mitigation import: `work/corpus_extension_mitigations/20261016T002000Z-fd9e2fc1`, with 48 direct ATT&CK references, 26 target mitigation entities, 53 source-reference combinations and three same-window three-hop chains. Transaction time was 1.695 seconds including verification. These counts include reused records; this is one processing observation, not a benchmark average.

The shared source loader now adds this extension after the six original development scopes, ten-window pilot and additional development batch. It requires the completed pinned source/mitigation receipts, exactly reconstructed source and reference records, Supported dispositions and frozen ATT&CK 17.1 associations. Repeated references and facts retain stable identities; all distinct accepted source supports remain available. Original failures and duplicate-removal provenance remain traceable.

| Shared accepted scope | Count |
| --- | ---: |
| CISA source parents | 53 |
| Direct ATT&CK reference parents | 139 |
| Reviewed pilot/batch/extension source assertions | 114 |
| Domain graph nodes in offline preview | 142 |
| Accepted directed facts in offline preview | 245 |
| Undirected training edges in offline preview | 245 |
| Retrieval child chunks in cached-tokenizer preview | 305 |

The extension contributes 27 reviewed assertions in twelve source parents. The shared reference pool adds 43 previously absent stable reference identities; five of the extension's 48 references are already included. Its 23 distinct source facts and 43 additional reference facts increase the preview from 179 to 245 directed facts. Graph nodes increase from 117 to 142. Components have sizes `[133, 5, 2, 2]`. These are expected source-derived projection counts, not a new live graph read.

Scope SHA-256: `ab3732f875177906c400d82268fbbeed719b9a26b4f3836215d713821bd9beb8`.

Offline projection SHA-256: `f9b46fcd5be4b2932279fbbe385eb090a42dfc1bfca597f0f6982695fb1af6cc`.

The cached-tokenizer text preview passed exact source spans, inherited contexts and configured limits. Maximum embedding input remains 240 WordPieces and 1000 characters. Extraction, generation, chunking, retrieval, embedding and Node2Vec settings are unchanged. Gold triples and QA reference answers are not inputs. Explicit scope options retain the preceding 41-window and original-pilot snapshots for regression checks.

All 69 distinct targeted offline checks passed: six new extension-scope checks, eight previous-batch scope checks, eight original expanded-scope checks and 47 projection/retrieval, text chunking/retrieval, combined and hybrid regressions. They verify receipt/reference tampering, exact source parity, preservation of every reviewed assertion and duplicate-recovery record, frozen settings and projection round trips using source fixtures or mocked services. The actual text-index `--preview` passed with 305 chunks. `git diff --check` passed.

Only windows containing Supported source assertions enter this extension's accepted retrieval scope. Whole selected parent text remains exact source text, including surrounding conditions and neighboring content; selection of a parent does not promote every sentence in it to an accepted graph assertion. Sixteen empty extraction windows and the nineteen excluded candidates remain coverage/review items. Eight eligible reports have their prepared technical sections attempted, but exhaustive extraction, whole fifteen-report processing, human verification and final controlled evaluation remain unfinished.

[Build the matching text index next](ThreatWeave_corpus_extension_text_index_step.md), then verify its receipt before the operator rebuilds the graph-vector index. Current saved collections still cover the earlier scope. Application queries should wait until both matching indexes are ready and the server has been restarted.
