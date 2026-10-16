# Corpus pilot graph import checkpoint

Later checkpoint: [the mitigation import completed and expanded development scope is prepared](ThreatWeave_expanded_development_scope_checkpoint.md). [Rebuilding the text index](ThreatWeave_expanded_text_index_step.md) is the current next step. The source receipt and original pre-mitigation instructions below remain as history.

October 14, 2026 (America/Chicago). User-run import: `work/corpus_pilot_ingestion/20261015T040329Z-5b1d9d11`. Directory timestamps are UTC.

The saved receipt records a completed import of **34 extracted assertions across ten source windows**, 39 target entities, 34 factual relationship keys and three excluded uncertain/conditional candidates. The receipt's review-manifest hash matches the pinned source review, and its saved prepared records match fresh offline reconstruction of the reviewed extraction. These checks validate the saved evidence/receipt; the assistant did not connect to Neo4j.

The transaction took **3.238944 seconds**, including conflict checks, assertion verification and any driver retries. The recorded rate is about **10.50 verified assertions/second**. Preparation/connectivity are excluded. This single small development transaction processed target records that can be reused; it is not a measurement of newly inserted records, full-corpus throughput or final model quality. Human verification remains pending.

## Next stage: direct mitigation references

[The prepared reference step](ThreatWeave_corpus_pilot_mitigation_step.md) selects only direct active STIX `mitigates` associations for techniques in the verified supported import. The frozen Enterprise ATT&CK 17.1 snapshot supplies **55 reference assertions for 15 of the 18 imported techniques**, involving **27 distinct target mitigation entities**. Target counts include previously imported records. The reference assertions use `origin=fused`; extracted-origin evaluation remains separate.

| Technique | Direct references |
| --- | ---: |
| T1018 | 0 |
| T1021.001 | 8 |
| T1055.002 | 1 |
| T1059.001 | 5 |
| T1059.003 | 1 |
| T1069.002 | 0 |
| T1078 | 8 |
| T1087.002 | 1 |
| T1133 | 4 |
| T1204 | 5 |
| T1217 | 0 |
| T1219 | 5 |
| T1539 | 6 |
| T1562.001 | 5 |
| T1586 | 1 |
| T1587.001 | 1 |
| T1598 | 2 |
| T1656 | 2 |

T1018, T1069.002 and T1217 have no active direct mitigation associations in this frozen snapshot. That does not establish that no defenses exist. No parent-technique inheritance, inferred mitigation, incident effectiveness or unsupported actor-use relationship is added.

The prepared references yield **72 source-assertion/reference combinations** (two edges from an actor or software source endpoint through its technique to a mitigation), plus **six same-window three-hop actor/software/technique/mitigation chains**. The six chains are supported by the Scattered Spider/Raccoon Stealer/T1539 assertions from the same window. These counts are scoped support combinations, not new source facts, human ratings or final retrieval scores. Source assertions without a supporting actor/software chain are not forced into a three-hop path.

Before any reference writes, the transaction rechecks the 34 exact imported source assertions, their accepted review state, provenance and connected domain edges. It writes only frozen references with compatible technique identity, preserves prior human verification and rejects conflicting/rejected reference assertions. It then verifies every reference assertion/edge and each expected two-edge/three-edge support combination. Verification failures roll back the transaction. Stable reference IDs reuse prior imports; no source assertion is relabeled as fused.

The original pilot/batch mitigation entry points retain their source-chain gates and defaults. Their common frozen-record writer is reused; an opt-in empty-reference case records gaps without suppressing unknown-technique or malformed-source errors.

## Verification and saved preview

All **167 offline tests pass**. New tests cover exact direct-reference coverage, missing direct associations without inherited links, original STIX direction and quote spans, extracted/fused separation, missing/changed/rejected source assertions, repeat import IDs, preserved human verification, rejected reference assertions, missing edges, incomplete paths, an incomplete source-import receipt and the legacy chain gate. Database transaction tests use fakes; the assistant made no live service calls or installations.

The actual offline preview passes. [The readable preview](ThreatWeave_corpus_pilot_mitigations_20261015T040857Z-ae3d4c5a.md) lists all direct mitigation IDs and exact relationship descriptions. Prepared records are saved under `work/corpus_pilot_mitigations/20261015T040857Z-ae3d4c5a`. The preview revalidates the completed source-import receipt, reviewed generated predictions and frozen snapshot; it opens no database connection. Gold triples and QA reference answers are not inputs.

Live mitigation import remains pending. Afterwards, retrieval scope profiles, matching text/graph indexes and all four development QA modes still need expansion and verification. The extraction pilot covers ten of 54 prepared development windows; broader extraction, overlap assessment, resource/index measurements, application UI and controlled held-out evaluation remain unfinished.

## Next command

With the ThreatWeave Neo4j instance running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\import_corpus_pilot_mitigations.py"
```

Press Enter for the default URI, username and database, then enter the Neo4j password. Ollama is not needed.
