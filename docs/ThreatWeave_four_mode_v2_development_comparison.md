# Four-mode generator-v2 development comparison

AI-assisted inspection on October 14, 2026, of saved answers and exact evidence. This is a diagnostic comparison of three development questions, with one run per mode. It is not the controlled final evaluation, a formal human rating or proof of a general retrieval advantage.

## Runs and matched settings

| Mode | Saved run |
| --- | --- |
| Text-only | `work/text_qa/20261014T061730Z-8c20bcb9` |
| Graph-only | `work/graph_qa/20261014T062006Z-5ad2e7b4` |
| Combined without Node2Vec | `work/combined_qa/20261014T062313Z-12809080` |
| Full hybrid | `work/hybrid_qa/20261014T061415Z-0d56a1a6` |

All four runs used the same three questions and shared generator `development-shared-cited-generator-v2`, Llama 3.1 8B digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`, temperature 0, context 8192, output limit 700 and maximum one repair. All 12 cases produced non-abstaining answers on their first attempt, with no execution failures.

Text-enabled modes used index `d183d6dfdb5313bc15e23049a7e907fae3d62342492b3658ca09c5409329b495`. Full hybrid used graph index `07df4575ac49de6962341dca1887fe207f952c89b9c8452ad48906094efe8b8d`. Context packing uses a shared conservative 3000 UTF-8 byte cap; exact shared-tokenizer context budgeting remains unfinished. Earlier v1 runs are preserved as historical development records.

## Source review

| Development question | Text-only | Graph-only | Combined without Node2Vec | Full hybrid |
| --- | --- | --- | --- | --- |
| AnyDesk actor use and mitigation guidance | One mitigation identity; missing application-control mechanism; three unrelated tool statements | Five identities; omits actor remote-control use and guidance details | Four identities; wrongly attributes ATT&CK recommendations to CISA; missing guidance and final mitigation | Five identities; remaining qualification and scope omissions |
| Rclone purpose | Controlled-cloud-account exfiltration; avoidance details omitted | Exfiltration only; cloud and avoidance details omitted | Same answer as text-only and full hybrid | Controlled-cloud-account exfiltration; avoidance details omitted |
| Evilginx2 requested items | All three items supported | All three supported in three repetitive claims | All three items supported | All three items supported |

Every graph-enabled mode retrieved five three-hop AnyDesk paths and all five mitigation identity/description pairs. Text-only retrieved one mitigation and no graph paths. The prose questions use appropriate one-hop actor/software paths. Source availability and answer correctness are separate: retrieving complete evidence did not consistently produce complete, faithful guidance.

## New no-Node2Vec findings

The latest run supplied 16 passages: AnyDesk's row/caption/headers, all five ATT&CK identity/description pairs and three other tool rows. Its AnyDesk answer produced exactly eight claims in 378 output tokens. The raw response ended with `done_reason: stop`, not an output-token truncation.

- Four claims say “CISA advises” an ATT&CK mitigation, citing only ATT&CK passages. These are incorrect source attributions. The retrieved CISA table documents actor/tool behavior, not those mitigation recommendations.
- The answer lists M1038, M1031, M1034 and M1037, but omits M1042 despite E12–E13 supplying its identity and description.
- M1037 has no practical guidance in the answer. The model splits earlier mitigation labels and advice across multiple claims, contrary to the shared prompt; the eight-claim bound is reached with required parts still missing. Schema compliance does not establish answer completeness.
- M1038 retains the remote-access restriction, but says prevention rather than mitigation. M1031 omits network signatures and the source's uncertainty about prevention effectiveness.
- M1034 preserves the “if not required” condition, a useful detail omitted in the other graph-enabled outputs.
- The opening sentence combines AnyDesk's intended and repurposed-use columns.

The two prose outputs match text-only and full hybrid exactly: Rclone gives supported cloud exfiltration but omits the same-service and detection-avoidance details; Evilginx2 covers MFA credentials, login credentials and session cookies.

## Single-run case times

| Question | Text-only | Graph-only | Combined without Node2Vec | Full hybrid |
| --- | ---: | ---: | ---: | ---: |
| AnyDesk | 3.61 s | 4.08 s | 5.50 s | 9.15 s |
| Rclone | 0.96 s | 0.88 s | 1.07 s | 1.08 s |
| Evilginx2 | 1.03 s | 1.89 s | 1.06 s | 1.09 s |

These include retrieval, packing and generation but exclude initialization. Runs were sequential, without a randomized repeated benchmark or matched warmup protocol. Output lengths differ. They do not establish statistically reliable performance rankings.

## Interpretation and next implementation stage

The current bounded text-only search misses four relevant mitigation references for AnyDesk. Graph traversal recovers all five. Differences in answer wording and completeness remain even when the supporting passage sets are equivalent; evidence ordering and generation matter. The no-Node2Vec source-attribution failure is a generation limitation, not missing retrieved mitigation evidence. This small check does not isolate or establish a general Node2Vec benefit.

Keep these imperfections in the results. Do not replace generated answers with corrected references or treat processing success as a quality score. No formal benchmark targets have been measured.

The next stage is broader source preparation and the planned five-report extraction timing/overlap pilot. Before building 400–600 Llama-token windows with approximately 60-token overlap, verify source-token counting against the installed model. `docs/ThreatWeave_extraction_tokenizer_step.md` provides the single setup/check command. This phase must use frozen source text and split boundaries without feeding gold triples or QA reference answers into extraction.

Full-corpus extraction/ingestion, refreshed text and graph indexes, application integration, extraction F1, repeated held-out four-mode evaluation and human ratings remain unfinished.
