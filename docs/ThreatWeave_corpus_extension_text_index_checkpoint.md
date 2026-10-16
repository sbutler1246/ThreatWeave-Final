# Three-report extension: text index checkpoint

October 15, 2026. Operator run `work/text_index_runs/20261016T002500Z-41e31bf5` completed with status `ready` at 7:25 p.m. America/Chicago. Its receipt records 305 verified stored chunks and 384-dimensional vectors across 53 CISA source windows and 139 direct ATT&CK reference parents. Human verification remains pending.

Index fingerprint: `be0883e8cea7af855c365a4c8644366a76838fe0a895fc79b46bc24dfd8b2367`.

Records SHA-256: `0dbbc58d6b37e7c47714705512dd3e208fddd11dcb4b358c923c458728e3c038`.

Offline reconstruction verified all 305 saved records against frozen source/tokenizer preparation, along with the ready receipt, manifest checksum, scope, embedding revision, chunking settings and all fifteen saved ranked-hit records. Maximum embedding input remains 240 WordPieces and 1000 characters including inherited context. No Chroma lookup or Neo4j/Ollama call was made by the assistant; stored-vector verification is recorded by the operator build.

The three existing smoke checks retain their earlier coverage pattern: Raccoon Stealer returns five ATT&CK references and no CISA observation; Rhysida returns four references plus a rank-2 CISA passage explicitly describing valid-credential access to internal VPN access points; ALPHV returns five CISA passages, with rank 2 directly naming AnyDesk, Mega sync and Splashtop deployed before exfiltration. Neighboring unrelated content remains among those hits. This is saved retrieval coverage, not a new generated-answer evaluation or quality score.

[The matching graph rebuild has now completed](ThreatWeave_corpus_extension_graph_index_checkpoint.md): 142 nodes, 245 accepted directed facts and 142 verified vector bindings. Its saved scope matches this text index. Restart the application to load the refreshed code and assets. Previous collections and answers remain saved. Broader coverage, human verification and controlled final evaluation remain pending.
