# Extraction pilot v2.5 review and v2.6 source-context repair

Later checkpoint: [the completed v2.6 source review and supported-only import](ThreatWeave_corpus_extraction_pilot_v2_6_development_review.md) records all 37 new candidates and the current next command. The older findings and pre-run instructions below remain as history.

October 14, 2026. AI-assisted development review of all 37 saved candidates. Findings are provisional source readings, not human verification, gold labels, precision/recall, extraction F1 or final quality scores. This document is not an extraction, retrieval or generation input.

## Completed live run

Run: `work/corpus_extraction_pilot/20261014T234930Z-28d2b8bb`, using `five-report-extraction-pilot-v2.5-explicit-evidence-menu`.

All ten frozen windows produced candidates, with zero empty extractions and zero processing failures. All ten requests returned HTTP 200 and completed on their first attempt; there were no repairs or output-limit truncations. There were 1872 generated tokens. Total elapsed time was 35.747 seconds, summed attempt time was 33.368 seconds and median window time was 3.203 seconds. Total timing includes availability checking and sequential extraction/validation, excluding source/tokenizer/catalog initialization.

The saved aggregator reports **37 raw candidates and 37 unique document candidates**, with zero repeated candidates or exact duplicate supports under its recorded identities. One source-declared alias pair is nevertheless represented separately; the reported count does not establish 37 semantically distinct facts. No cross-window duplicate was observed, so this run establishes no overlap benefit.

Provisional dispositions: **29 Supported, seven Review and one Reject**. All original records remain pending semantic review. No graph writes occurred. Four-relation limits and bounded mention/evidence rules still constrain coverage; ten nonempty windows do not establish exhaustive extraction. Timing differences from v2.4 are not controlled speed comparisons because input/output lengths, repairs, empty results and model state differ.

| Window | Report | Candidates | Attempts | Case time |
| --- | --- | ---: | ---: | ---: |
| 01 | BianLian | 4 | 1 | 6.949 s |
| 02 | BianLian | 4 | 1 | 3.264 s |
| 03 | Rhysida | 4 | 1 | 2.959 s |
| 04 | Rhysida | 4 | 1 | 3.158 s |
| 05 | Scattered Spider | 4 | 1 | 3.251 s |
| 06 | Scattered Spider | 4 | 1 | 3.492 s |
| 07 | ALPHV Blackcat | 4 | 1 | 3.249 s |
| 08 | ALPHV Blackcat | 1 | 1 | 1.063 s |
| 09 | Phobos | 4 | 1 | 3.043 s |
| 10 | Phobos | 4 | 1 | 2.974 s |

## Individual source review

IDs identify the window directory and one-based relation in `candidate_extraction.json`. Exact selected units and absolute source offsets remain saved. Supported is an AI-assisted source reading, not ingestion approval or a human rating. Review flags are lexical aids and do not replace relation-specific judgment.

| ID | Candidate | Judgment | Source finding |
| --- | --- | --- | --- |
| 01.1 | BianLian group actors USES_TECHNIQUE T1078 | Supported | u010 explicitly reports access using compromised RDP credentials. Likely concerns credential provenance, not whether the actors used credentials. |
| 01.2 | Same actor USES_TECHNIQUE T1133 | Supported | Same source explicitly reports RDP-based initial access with this ID. |
| 01.3 | Same actor USES_TECHNIQUE T1566 | Review | Phishing is within the qualified credential-acquisition alternatives; preserve that uncertainty rather than asserting categorical use. |
| 01.4 | Same actor USES_TECHNIQUE T1587.001 | Supported | u013 describes the actors' victim-specific custom Go backdoor and explicitly reports this annotation. |
| 02.1 | Rsocks USES_TECHNIQUE T1090.002 | Review | u002 says the group may have used Rsocks for SOCKS5 tunnels. The selected behavior is inside an uncertain event, as in v2.4. |
| 02.2 | BianLian group actors USES_TECHNIQUE T1059.001 | Supported | u006 explicitly reports actor use of PowerShell and this ID. |
| 02.3 | Same actor USES_TECHNIQUE T1059.003 | Supported | Same assertion explicitly names Windows Command Shell and its ID. |
| 02.4 | Same actor USES_TECHNIQUE T1562.001 | Supported | Same assertion reports disabling antivirus tools with this ID. |
| 03.1 | Threat actors USES Rhysida | Review | u003 says Threat actors leveraging Rhysida ransomware. The generic selected actor loses its source restriction and should not become an unrestricted actor identity. |
| 03.2 | Rhysida actors USES_TECHNIQUE T1078 | Supported | u011 directly reports VPN authentication using compromised valid credentials. |
| 03.3 | Rhysida actors USES at | Reject | In u014, at is the preposition in at times. Literal catalog-name matching does not make it software use. |
| 03.4 | Rhysida actors USES Gootloader | Supported | u014 explicitly reports the actors using Gootloader malware for initial access. |
| 04.1 | net USES_TECHNIQUE T1087.002 | Supported | u004 gives the net user domain command and its annotation. |
| 04.2 | net USES_TECHNIQUE T1018 | Supported | u005 gives the domain-computers group command and its annotation. |
| 04.3 | net USES_TECHNIQUE T1069.002 | Supported | u006 gives the domain-admins group command and its annotation. |
| 04.4 | net USES_TECHNIQUE T1069.001 | Supported | u007 gives the local-administrators command and its annotation. |
| 05.1 | Scattered Spider threat actors USES_TECHNIQUE T1598 | Supported | Public-reporting subject u005 scopes phone/SMS credential targeting in u006. Retain the reporting attribution. |
| 05.2 | Same actor USES_TECHNIQUE T1656 | Supported | Same subject/list item describes impersonating IT/helpdesk staff with this annotation. |
| 05.3 | Same actor USES_TECHNIQUE T1204 | Supported | u005 scopes the employee-execution item u007 and this ID. |
| 05.4 | Same actor USES_TECHNIQUE T1219 | Supported | Same item explicitly describes running commercial remote access tools with this ID. |
| 06.1 | Scattered Spider USES AveMaria | Review | Caption u037 scopes row u040, but that row explicitly says AveMaria is also known as WarZone [S0670]. The saved unresolved AveMaria identity remains separate from resolved WarZone. Resolve the source-declared alias before counting distinct facts. |
| 06.2 | Scattered Spider USES WarZone | Supported | Same caption/row directly supports use. Frozen catalog resolution identifies S0670; it is the alias counterpart of 06.1. |
| 06.3 | Raccoon Stealer USES_TECHNIQUE T1217 | Supported | Row u042 and its description report stealing browser history, annotated in u044. The contiguous saved quote includes the description's action. |
| 06.4 | Same software USES_TECHNIQUE T1539 | Supported | Same row description reports stealing cookies, annotated in u045. |
| 07.1 | ALPHV Blackcat affiliates USES_TECHNIQUE T1598 | Supported | Named affiliates in u004 scope adjacent Actors continuation u005 and its phone/SMS credential-targeting annotation. |
| 07.2 | Same actor USES_TECHNIQUE T1586 | Supported | Same continuation reports credentials used to access the target network with this ID. |
| 07.3 | Same actor USES Evilginx2 | Supported | u011 explicitly reports affiliate use of the named framework. |
| 07.4 | Same actor USES_TECHNIQUE T1557 | Supported | Same assertion reports the adversary-in-the-middle attack and this ID. |
| 08.1 | ALPHV Blackcat affiliates USES TOR | Supported | u005 explicitly names these affiliates communicating with victims via TOR [S0183], without importing Some from the preceding sentence. |
| 09.1 | Phobos actors USES_TECHNIQUE T1598 | Supported | u009 explicitly reports phishing campaigns for initial access with this annotation. |
| 09.2 | Phobos actors USES_TECHNIQUE T1133 | Review | u011 begins If Phobos actors gain successful RDP authentication. The conditional is not a confirmed access event, and the selected actor drops If. The old uncertainty-word list did not flag it. |
| 09.3 | Threat actors USES Phobos | Review | u012 restricts its subject to Threat actors leveraging Phobos. The generic selected actor loses that restriction. |
| 09.4 | Threat actors USES_TECHNIQUE T1219 | Review | The remote-access assertion is explicit, but the same subject restriction is missing from the selected actor identity. |
| 10.1 | Phobos actors USES Phobos | Supported | u004 explicitly reports actor deployment of additional Phobos payloads. The software endpoint occurs independently of the actor phrase. |
| 10.2 | Same actor USES 1saas.exe | Supported | Same sentence explicitly says the actors run this executable. |
| 10.3 | Same actor USES cmd.exe | Supported | Same explicit executable-use assertion. Catalog resolution is distinct from a source-reported ATT&CK ID. |
| 10.4 | Smokeloader USES_TECHNIQUE T1055.002 | Supported | u009 directly reports API manipulation enabling process injection and gives this ID. |

Windows 01, 03 and 09 were empty in v2.4 and now contain useful assertions, alongside the issues above. No claim of exhaustive recall follows from this recovery. The explicit evidence menu remains a list of possibilities rather than semantic acceptance; the at false match demonstrates that source-aligned choices can still be wrong.

## v2.6 repair

Current version: `five-report-extraction-pilot-v2.6-source-context-identities`.

- Short catalog words of up to three letters, when not uppercase acronyms, now require local software/command context. Adverbial wording such as at times does not qualify. This check applies both when indexing catalog names and when proving a selected endpoint, preventing a real command occurrence elsewhere from licensing an unrelated prose occurrence. Literal net command syntax and explicit scheduler invocation remain available.
- Source actor phrases of the form Threat actors leveraging/using/deploying a named product retain their full software restriction, including ransomware/malware where present. Bare Threat actors/The actors/These actors are not independent named group candidates. This does not resolve these source-scoped actors to a named ATT&CK group or silently equate them with other actor mentions.
- Explicit software table rows of the form A (also known as B [Sxxxx]) assign the literal source ID to both spellings within that source index. A compatible frozen catalog identity then lets existing selector preference and duplicate checks treat them as one identity. Conflicting source IDs omit the ambiguous typed name. The catalog and its verified global aliases are unchanged; arbitrary prose co-occurrence does not establish an alias.
- Conditional evidence wording such as if/unless receives a separate `source_conditional_wording` flag, and the model instructions explicitly exclude conditional relationships. Flags request review; they do not automatically reject a whole passage or certify an unflagged relationship. Existing uncertainty flags remain, including where a definite relationship shares a passage with uncertain provenance.
- Source IDs without an active compatible frozen-catalog resolution remain recorded in the mention index but are unavailable in the executable evidence menu/schema. Actual-source checking found S1054 in window 07 was previously offered despite failing the existing catalog validator. It is now unavailable, without inventing a replacement ID or changing the frozen catalog.

No source windows, tokenizer, frozen catalog, model settings, four-relation bound or one-repair limit changed. The explicit evidence menu and empty-result option remain. No candidate is auto-filled or approved. The new actor rules and short-name heuristics are conservative and can omit valid mentions; they are not exhaustive NER or coreference resolution.

## Offline verification and preserved records

All **151 offline tests pass**. Added tests cover local short-word ambiguity versus actual commands, complete software-scoped actors, explicit row aliases without global catalog mutation, conflicting row alias IDs, conditional flags versus definite assertions, and source IDs unavailable in the frozen catalog. Service tests use mocks. No live Ollama/Neo4j calls or installations were made by the assistant.

The ten-window preview passes frozen source/tokenizer/catalog checks. Requests contain 1841–4784 estimated system/prompt/schema tokens, plus 700 output tokens and 256 reserved chat tokens within context 8192. All **127** offered literal endpoint combinations in the actual new menus were checked through the source validator; this establishes structural/source compatibility, not that each combination is semantically true. Targeted checks confirm removal of the Rhysida at option and bare generic actor options, preservation of the full Phobos actor restriction, shared S0670 identity for the explicit table aliases, and a conditional flag for the If passage.

Separately, all ten original v2.5 chunks and metadata, prompt/schema hashes, completed raw responses, schema adherence, selected endpoint values, reconstructed relationships, exact unit/absolute quote spans, identity resolutions and aggregate records were rechecked against the saved source. All 37 original supports align. Original outputs and their old review flags remain unmodified; the new rules are not retroactively applied to rewrite them.

Prepared source fingerprint: `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`. Gold triples and QA reference answers are not inputs. Graph-write rate, index-build/resource measurements, full-corpus integration, application UI and controlled held-out evaluation remain unfinished.

## Next command

With Ollama running, start a fresh v2.6 pilot over the same frozen ten windows:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

Do not use `--retry-run` with earlier configurations. v2.6 live processing and semantic outcomes remain pending.
