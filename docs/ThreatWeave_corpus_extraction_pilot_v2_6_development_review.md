# Extraction pilot v2.6 source review and graph import checkpoint

Later checkpoint: the [source graph import completed](ThreatWeave_corpus_pilot_graph_checkpoint.md) with 34 verified assertions; [the next step adds direct frozen mitigation references](ThreatWeave_corpus_pilot_mitigation_step.md). The review and original pre-import instructions below remain as history.

October 14, 2026 (America/Chicago). Run: `work/corpus_extraction_pilot/20261015T035023Z-f4b7051e`. The timestamp in the directory is UTC.

All ten frozen windows produced candidates on their first attempt: zero empty results, processing failures, repairs or truncations. The run produced 37 raw candidates and 37 distinct document candidates under the saved resolver, with zero repeated candidates or exact duplicate supports. Source inspection provisionally supports **34 relationships**, with **three requiring review** and **zero rejected relationships**. These are AI-assisted development dispositions, not human verification, formal precision/recall, extraction F1 or final quality scores.

## Timing and changes observed

There were ten HTTP-200 generation responses and 1804 generated tokens. Total elapsed time was 41.540 seconds, summed attempt time was 38.929 seconds and median window time was 3.112 seconds. The first window took 13.292 seconds. Total timing includes availability checking and sequential extraction/validation, excluding source/tokenizer/catalog initialization. These are single-run observations without controlled warmup or averaging; changed prompt/output lengths and model state prevent a controlled speed comparison.

| Window | Report | Candidates | Attempts | Case time |
| --- | --- | ---: | ---: | ---: |
| 01 | BianLian | 4 | 1 | 13.292 s |
| 02 | BianLian | 4 | 1 | 3.275 s |
| 03 | Rhysida | 4 | 1 | 3.053 s |
| 04 | Rhysida | 4 | 1 | 3.171 s |
| 05 | Scattered Spider | 4 | 1 | 3.271 s |
| 06 | Scattered Spider | 4 | 1 | 3.494 s |
| 07 | ALPHV Blackcat | 4 | 1 | 2.329 s |
| 08 | ALPHV Blackcat | 1 | 1 | 1.057 s |
| 09 | Phobos | 4 | 1 | 3.051 s |
| 10 | Phobos | 4 | 1 | 2.982 s |

The at-times false software match is absent. Full software-restricted actor phrases are retained for Rhysida and Phobos, without merging them into the other named actor phrases. AveMaria now resolves through the source-declared WarZone [S0670] alias; no separate duplicate alias assertion consumes a slot. The conditional Phobos RDP assertion is correctly flagged but still generated, demonstrating that prompt exclusions alone do not guarantee omission. No cross-window duplicate occurred, so overlap benefit remains unmeasured. Four-relation bounds and conservative mention/evidence rules limit completeness even when every window is nonempty.

## Individual dispositions

IDs identify the window directory and one-based relationship position. Original logs and their pending semantic-review status remain unchanged. The separate [pinned review manifest](ThreatWeave_corpus_pilot_v2_6_review.json) records every disposition, source-review reason and hashes binding the review to the exact saved model output and evidence. The expanded graph uses this metadata to verify its supported-only scope; review labels/reasons are not embedding text, generation context or similarity scores. Gold triples and QA reference answers remain excluded from the pipeline.

| ID | Candidate | Judgment | Source finding |
| --- | --- | --- | --- |
| 01.1 | BianLian group actors USES_TECHNIQUE T1078 | Supported | The actor uses compromised RDP credentials; likely qualifies credential provenance, not the reported credential use. |
| 01.2 | BianLian group actors USES_TECHNIQUE T1133 | Supported | The source explicitly reports actor initial access through RDP with T1133. |
| 01.3 | BianLian group actors USES_TECHNIQUE T1566 | Review | Phishing is within qualified alternatives for likely credential acquisition; do not import as categorical use. |
| 01.4 | BianLian group actors USES_TECHNIQUE T1587.001 | Supported | The source describes the actor-specific custom Go backdoor and explicitly annotates T1587.001. |
| 02.1 | Rsocks USES_TECHNIQUE T1090.002 | Review | The source says may have used Rsocks for SOCKS5 tunnels; the selected behavior remains inside an uncertain event. |
| 02.2 | BianLian group actors USES_TECHNIQUE T1059.001 | Supported | Explicit actor use of PowerShell with T1059.001. |
| 02.3 | BianLian group actors USES_TECHNIQUE T1059.003 | Supported | Explicit actor use of Windows Command Shell with T1059.003. |
| 02.4 | BianLian group actors USES_TECHNIQUE T1562.001 | Supported | The actors disable antivirus tools, explicitly annotated T1562.001. |
| 03.1 | Threat actors leveraging Rhysida ransomware USES Rhysida | Supported | The full source subject Threat actors leveraging Rhysida ransomware preserves the restriction and explicitly describes their use of that ransomware. |
| 03.2 | Rhysida actors USES_TECHNIQUE T1078 | Supported | The source directly reports actor VPN authentication using compromised valid credentials. |
| 03.3 | Rhysida actors USES Gootloader | Supported | The source explicitly reports actor use of Gootloader malware; at times is not a software endpoint. |
| 03.4 | Rhysida actors USES_TECHNIQUE T1021.001 | Supported | The source directly reports actors creating RDP connections for lateral movement with T1021.001. |
| 04.1 | net USES_TECHNIQUE T1087.002 | Supported | Literal net user domain command with its T1087.002 annotation. |
| 04.2 | net USES_TECHNIQUE T1018 | Supported | Literal net domain-computers group command with T1018. |
| 04.3 | net USES_TECHNIQUE T1069.002 | Supported | Literal net domain-admins group command with T1069.002. |
| 04.4 | Rhysida actors USES Windows PowerShell Integrated Scripting Environment | Supported | The source directly reports actors launching Windows PowerShell Integrated Scripting Environment before executing a malicious script. |
| 05.1 | Scattered Spider threat actors USES_TECHNIQUE T1598 | Supported | The explicit public-reporting subject scopes the phone/SMS credential-targeting list item with T1598; retain that attribution. |
| 05.2 | Scattered Spider threat actors USES_TECHNIQUE T1656 | Supported | The same explicit subject/list reports IT/helpdesk impersonation and T1656. |
| 05.3 | Scattered Spider threat actors USES_TECHNIQUE T1204 | Supported | The named subject scopes employee execution of remote access tools and T1204. |
| 05.4 | Scattered Spider threat actors USES_TECHNIQUE T1219 | Supported | The same subject/list item explicitly reports remote access tools and T1219. |
| 06.1 | Scattered Spider USES AveMaria | Supported | The Malware Used by Scattered Spider caption scopes AveMaria, explicitly also known as WarZone [S0670]; the source alias now shares that catalog identity. |
| 06.2 | Scattered Spider USES Raccoon Stealer | Supported | The explicit actor-use malware caption scopes the Raccoon Stealer [S1148] row. |
| 06.3 | Raccoon Stealer USES_TECHNIQUE T1217 | Supported | The Raccoon Stealer row description says it steals browser history, annotated T1217; the contiguous literal quote includes the action. |
| 06.4 | Raccoon Stealer USES_TECHNIQUE T1539 | Supported | The same row description reports stealing cookies, annotated T1539. |
| 07.1 | ALPHV Blackcat affiliates USES_TECHNIQUE T1598 | Supported | Named affiliates scope the adjacent Actors continuation, which explicitly reports phone/SMS credential targeting and T1598. |
| 07.2 | ALPHV Blackcat affiliates USES_TECHNIQUE T1586 | Supported | The same controlled continuation explicitly reports credentials used for target access and T1586. |
| 07.3 | ALPHV Blackcat affiliates USES AnyDesk | Supported | The source directly says affiliates deploy remote access software including AnyDesk. |
| 07.4 | ALPHV Blackcat affiliates USES Mega sync | Supported | The same deployment list names the complete software phrase Mega sync. |
| 08.1 | ALPHV Blackcat affiliates USES TOR | Supported | The source directly names ALPHV Blackcat affiliates communicating with victims via TOR [S0183], without a copied Some qualifier. |
| 09.1 | Phobos actors USES_TECHNIQUE T1598 | Supported | The source explicitly reports Phobos actors initial access through phishing campaigns with T1598. |
| 09.2 | Phobos actors USES_TECHNIQUE T1133 | Review | The passage begins If Phobos actors gain successful RDP authentication; a conditional is not a confirmed T1133 access event. |
| 09.3 | Threat actors leveraging Phobos USES Phobos | Supported | The full source subject Threat actors leveraging Phobos preserves its restriction and explicitly describes use of Phobos. |
| 09.4 | Threat actors leveraging Phobos USES_TECHNIQUE T1219 | Supported | That restricted source subject explicitly reports deployed remote access tools with T1219. |
| 10.1 | Phobos actors USES Phobos | Supported | The actors explicitly deploy additional Phobos payloads; the software mention occurs independently of the qualified actor name. |
| 10.2 | Phobos actors USES 1saas.exe | Supported | The source directly says Phobos actors run 1saas.exe. |
| 10.3 | Phobos actors USES cmd.exe | Supported | The source directly says Phobos actors run cmd.exe; catalog resolution is separate from a source-reported ID. |
| 10.4 | Smokeloader USES_TECHNIQUE T1055.002 | Supported | The source directly reports Smokeloader API manipulation enabling process injection and T1055.002. |

## Supported-only development import

The extractor remains at `five-report-extraction-pilot-v2.6-source-context-identities`. No new extraction run is needed for this step. The next stage imports only the 34 Supported relationships from this exact run and excludes:

- **01.3:** phishing in the qualified likely credential-acquisition alternatives.
- **02.1:** Rsocks behavior inside a may-have-used event.
- **09.2:** RDP authentication inside an If condition.

The uncertainty flags on 01.1 and 01.2 are retained even though source review supports the reported credential/RDP use: likely qualifies credential provenance. The selection therefore uses explicit relationship-specific dispositions rather than dropping every sentence containing an uncertainty word. The import records source-review reasons and flags; all assertions remain `origin=extracted`, source-validated, and human review pending.

The offline preview prepared ten source windows across five reports, **39 distinct target entities and 34 extracted assertions**, with three candidates excluded. Target counts include records that may already exist. Local source-scoped identities remain distinct where the source does not justify an equivalence; the source-declared AveMaria alias uses the compatible frozen catalog identity without modifying global verified aliases.

The importer pins the original summary and per-window output/evidence hashes. Before opening Neo4j, it verifies frozen source/tokenizer/catalog identity, source preparation, extraction configuration, prompt/schema and source-choice agreement, completed raw model responses, reconstructed candidates, exact evidence alignments, resolutions, all candidate dispositions and aggregation. Endpoint occurrences come from selected supporting units/captions; a software occurrence embedded only in an actor name is not used as independent software evidence.

Each imported assertion retains the exact source span, selected units/context, original relation position, source review reason/hash, model options/digest, prompt/raw-output hashes and extraction run. The transaction reuses the established conflict checks, stable identifiers and MERGE behavior. It preserves prior human verification and refuses rejected/conflicting assertions. Missing constraints or failed verification stop the import; transaction failures roll back. Repeating the same selection does not create duplicate assertions, and later model output is never selected automatically in place of this reviewed run.

The live command saves prepared records and a readable preview before asking for the database password. A successful import records verified counts and transaction time, including conflict checks, verification and any driver retries. Its rate measures processed reviewed assertions, including reused records, rather than newly inserted records or full-corpus throughput. No service passwords are saved. The assistant has made no live Ollama/Neo4j calls or installations.

## Offline verification and remaining work

All **159 offline tests pass**. Import tests cover the exact supported/excluded selection, exact evidence and review provenance, independent software occurrences, stable assertion IDs and alias resolution, incomplete/invalid review coverage, changed model output, transaction verification counts and preview execution without loading the database driver. Existing extraction, ingestion, retrieval and generation tests also pass. The actual import preview passes with 34 selected assertions and three exclusions; its saved records are under `work/corpus_pilot_ingestion/20261015T035611Z-b96fba19` and its [readable preview](ThreatWeave_corpus_pilot_import_20261015T035611Z-b96fba19.md) is in docs.

Prepared source fingerprint remains `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`. Gold triples and QA reference answers are not inputs. The original extraction runs and generated reviews remain preserved.

Live graph import and its timing remain pending until the operator runs the command. This is a ten-window development pilot, not extraction of all 54 prepared windows or the full 15-report candidate corpus. Importing these records does not refresh Chroma/Node2Vec indexes or expand existing QA scope filters. Mitigation fusion, broader source coverage, overlap/resource/index measurements, application UI and controlled held-out evaluation remain unfinished.

## Next command

Keep the ThreatWeave Neo4j database running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\ingest_corpus_pilot.py"
```

Press Enter for URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, then enter the password when prompted. Ollama is not required for this import. Detailed instructions: [corpus pilot import step](ThreatWeave_corpus_pilot_ingestion_step.md).
