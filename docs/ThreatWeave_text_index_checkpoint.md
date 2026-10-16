# Development text-index checkpoint

AI-assisted inspection of the successful local index receipt `work/text_index_runs/20261014T035856Z-94adfaa4/index_receipt.json` and its ranked source matches. The UTC timestamp corresponds to the evening of October 13, 2026 in America/Chicago.

The run verified 19 text chunks across six CISA development scopes and 13 ATT&CK 17.1 mitigation references. MiniLM revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41` produced normalized 384-dimensional vectors. The collection is `threatweave_text_dev_d183d6dfdb5313bc` under `work/chroma`.

Index fingerprint: `d183d6dfdb5313bc15e23049a7e907fae3d62342492b3658ca09c5409329b495`.
Source-record file SHA-256: `8b4e08330fc86c09c110cda0123e37e3b631acc96aff9ae74b03c3952b7654dc`.

| Development search | First ranked source | Cosine distance | Top-five coverage observation |
| --- | --- | --- | --- |
| LockBit Affiliates / AnyDesk and mitigations | AA23-165A table 4 row 03 | 0.3659 | Correct incident row; three other LockBit rows and one T1219 mitigation reference, M1038. |
| BianLian / Rclone purpose | AA23-136A paragraph 27502 | 0.3836 | Correct prose passage; four other LockBit rows. |
| ALPHV affiliates / Evilginx2 credentials | AA23-353A paragraph 10240 | 0.2605 | Correct prose passage; four other LockBit rows. |

These distances are ranking outputs, not confidence probabilities. Each correct incident passage ranked first in these three development searches. The AnyDesk top-five text results contained only one mitigation reference, while the earlier graph QA retrieved five supported three-hop chains. This is a development coverage observation, not a held-out recall score or a measured improvement in answer quality.

The text QA baseline will preserve top-five nearest-neighbor retrieval without graph expansion. The complete source index contains the relevant reference material, but bounded retrieval can omit it. Generated answers must be reviewed for incomplete mitigation lists, unsupported additions and citation quality.

Next: run text-only cited QA using the same three development questions and shared Ollama generator, then review before combining text and graph retrieval. Node2Vec and the final evaluation remain pending.
