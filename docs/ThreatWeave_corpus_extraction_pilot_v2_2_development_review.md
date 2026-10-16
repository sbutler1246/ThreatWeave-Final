# Extraction pilot v2.2 semantic review and v2.3 repair

Later checkpoint: v2.3 produced 26 candidates across eight windows, with two empty results and zero final processing failures. See [the v2.3 review and current v2.4 repair](ThreatWeave_corpus_extraction_pilot_v2_3_development_review.md) for remaining attribution/qualification issues and name/ID duplicates. The remainder preserves the v2.2 review and original v2.3 checkpoint.

October 14, 2026. AI-assisted development review of every saved candidate and its selected literal source units. These judgments are provisional review notes, not human ratings, gold annotations, extraction F1 or a final quality score. Review notes are not extraction, retrieval or generation inputs.

## Processing outcome

Run: `work/corpus_extraction_pilot/20261014T231745Z-503aa727`.

All ten windows produced source-checked candidates. There were no final case failures, empty extractions, HTTP failures or output-limit truncations. Nine windows passed on their first attempt; ALPHV window 07 required one repair because its first reply repeated a relationship. The original duplicate reply remains saved.

The run contains **36 candidate relations, grouped into 34 unique document candidates**, with two repeated relations and one exact duplicate support. These are candidate counts, not verified facts. All 36 saved evidence spans were checked against the unchanged source text. Passing those checks establishes literal alignment and permitted types, not semantic correctness. No graph writes occurred.

There were 11 generation requests and 1588 generated tokens. Total recorded run time was 33.821 seconds, summed generation-attempt elapsed time was 31.509 seconds, and median case time was 2.669 seconds. Total timing includes the availability check and sequential extraction/validation, excluding source/tokenizer/catalog initialization. These are single-run observations; changes in requests, repair count, output length and model loading prevent a controlled speed comparison with earlier runs.

| Window | Report | Candidates | Attempts | Case time |
| --- | --- | ---: | ---: | ---: |
| 01 | BianLian | 4 | 1 | 7.61 s |
| 02 | BianLian | 4 | 1 | 2.68 s |
| 03 | Rhysida | 4 | 1 | 2.66 s |
| 04 | Rhysida | 4 | 1 | 2.72 s |
| 05 | Scattered Spider | 4 | 1 | 2.66 s |
| 06 | Scattered Spider | 1 | 1 | 1.08 s |
| 07 | ALPHV Blackcat | 3 | 2 | 4.38 s |
| 08 | ALPHV Blackcat | 4 | 1 | 2.50 s |
| 09 | Phobos | 4 | 1 | 2.76 s |
| 10 | Phobos | 4 | 1 | 2.53 s |

## Candidate-by-candidate review

IDs below use the window directory followed by the one-based relation position in its `candidate_extraction.json`. Exact selected units and offsets remain in the corresponding `quote_alignment.json`; the generated run review reproduces the source text.

“Supported” means the selected passage supports the relation in this provisional reading. “Review” requires unresolved qualification, identity or scope judgment. “Reject” identifies an unsupported entity/type/action binding. None of these labels approves ingestion or changes the original pending-review records.

| ID | Candidate | Judgment | Source reasoning |
| --- | --- | --- | --- |
| 01.1 | BianLian group actors USES RDP as Software | Reject | RDP denotes a protocol/remote service in this passage, not a named software product. |
| 01.2 | BianLian group actors USES_TECHNIQUE T1078 | Supported | Compromised RDP credentials are explicitly used for access; T1078 is literal. “Likely acquired” qualifies credential provenance. |
| 01.3 | BianLian group actors USES_TECHNIQUE T1133 | Supported | The source explicitly describes access through RDP and supplies T1133. |
| 01.4 | BianLian group actors USES_TECHNIQUE phishing / T1566 | Review | Phishing is an alternative in the clause about how compromised credentials were likely acquired. Do not erase that qualification. |
| 02.1 | Rsocks USES_TECHNIQUE T1090 | Review | The clipped unit describes a modified Rsocks utility and proxy behavior; scope to the modified version and separate the uncertain actor-use statement. |
| 02.2 | BianLian group actors USES Windows PowerShell | Review | Actual use names PowerShell; the complete “Windows PowerShell” surface occurs in an appendix reference. Its software identity/scope needs verification. |
| 02.3 | BianLian group actors USES Command Shell Activity | Reject | This is a fragment of an appendix title, not software the passage says was used. |
| 02.4 | Advanced Port Scanner USES_TECHNIQUE T1046 | Supported | The source describes port discovery and explicitly supplies T1046. |
| 03.1 | Rhysida actors USES Rhysida as Software | Reject | In the selected remote-services paragraph, “Rhysida” occurs inside the actor name; ransomware use is not asserted there. |
| 03.2 | Rhysida actors USES_TECHNIQUE malware | Reject | “Malware” describes Gootloader; it is not a named ATT&CK behavior in that sentence. |
| 03.3 | Rhysida actors USES_TECHNIQUE T1021.001 | Supported | RDP lateral movement and its technique ID are explicit. |
| 03.4 | credentials / T1589.001 PART_OF_TACTIC reconnaissance / TA0043 | Reject | Generic compromised credentials and internal reconnaissance do not assert this ATT&CK taxonomy relationship. Neither inferred ID is reported in the selected unit. |
| 04.1 | Same credentials-to-reconnaissance relationship | Reject | Repeats the unsupported taxonomy binding in the overlapping clipped paragraph. |
| 04.2 | net USES_TECHNIQUE T1087.002 | Supported | The literal net user command is annotated with T1087.002. |
| 04.3 | net USES_TECHNIQUE T1018 | Supported | The literal domain-computers command is annotated with T1018. |
| 04.4 | net USES_TECHNIQUE T1069.002 | Supported | The literal domain-admins command is annotated with T1069.002. |
| 05.1 | Posed as Software USES_TECHNIQUE T1598 | Reject | “Posed” is the list item's verb, not software. |
| 05.2 | Posed as Software USES_TECHNIQUE T1204 | Reject | Same entity-role error. |
| 05.3 | Posed as Software USES_TECHNIQUE T1219 | Reject | Same entity-role error. |
| 05.4 | Posed as Software USES_TECHNIQUE T1566 | Reject | Same entity-role error. |
| 06.1 | Scattered Spider USES TTPs. See Table | Reject | The software surface crosses a sentence boundary and contains a reference phrase. The source does not name such software. |
| 07.1 | ALPHV Blackcat affiliates USES_TECHNIQUE T1598 | Supported | Phone/SMS credential targeting and T1598 are explicit. |
| 07.2 | ALPHV Blackcat affiliates USES_TECHNIQUE T1586 | Supported | Credential-based target-network access and T1586 are explicit. |
| 07.3 | ALPHV Blackcat affiliates USES AnyDesk | Supported | The next selected paragraph directly says affiliates deploy AnyDesk. |
| 08.1 | Some ALPHV Blackcat affiliates USES ALPHV | Reject | The software token is embedded in the actor phrase. This paragraph does not assert ransomware use and describes some affiliates extorting without deployment. |
| 08.2 | Same actor USES ALPHV Blackcat | Reject | Same actor-name/software confusion. |
| 08.3 | Same actor USES Blackcat | Reject | Same confusion through another alias of the software identity. |
| 08.4 | Same actor USES TOR | Supported | The passage explicitly describes affiliate communication via TOR; retain the limited actor qualifier. |
| 09.1 | IP as Software USES_TECHNIQUE phishing / T1566 | Reject | IP is an acronym for internet protocol, not software performing phishing. The source annotates its phishing phrase with T1598, not the inferred T1566 binding. |
| 09.2 | IP as Software USES_TECHNIQUE T1110 | Reject | Actors use brute-force tools; the passage does not assign the action to software named IP. |
| 09.3 | SmokeLoader USES_TECHNIQUE malware | Reject | Generic “malware” is not a technique identity in this passage. |
| 09.4 | IP as Software USES_TECHNIQUE T1219 | Reject | Remote-access deployment is actor activity; IP is not the software subject. |
| 10.1 | Phobos actors USES Phobos as Software | Supported | The source separately describes actors running executables to deploy additional Phobos payloads, rather than merely repeating the actor name. |
| 10.2 | Phobos actors USES_TECHNIQUE Windows command shell / T1059.003 | Supported | The paragraph connects executed commands/shell functions to actor activity and provides T1059.003. |
| 10.3 | Smokeloader USES_TECHNIQUE T1055.002 | Supported | The software's API manipulation and process injection are explicitly described with the ID. |
| 10.4 | Phobos actors USES Universal Virus Sniffer | Review | The source says actors “can” evade detection using these tools; retain capability/actual-use scope rather than silently treating it as an observed use event. |

This reading finds 14 candidates with direct support, four requiring qualification/scope review and 18 to reject. These are diagnostic review dispositions over this generated sample, not precision or recall estimates. In particular, 10/10 processing success must not be presented as a semantic quality score.

The uncertainty flag is a word-presence aid. It marks all four window-01 candidates because their shared unit contains “likely,” even where the qualifier concerns credential provenance. Conversely, it does not flag window 10's “can” capability wording. Flags cannot replace relation-specific review.

## Repetition and overlap

The two repeated relations have different causes:

- The unsupported credentials/T1589.001-to-reconnaissance/TA0043 candidate repeats across Rhysida windows 03 and 04. Its supports span document offsets 4701–5140 and 4860–5140, respectively. This is a repeated candidate from overlapping source, with different quote boundaries; it is not an exact duplicate support or a correct recovered fact.
- The unsupported ALPHV software-use candidate repeats within window 08 because ALPHV and Blackcat both resolve to `attack:S1068`. Both supports span 5323–5657. This accounts for the single exact duplicate support and is alias duplication within one window, rather than an overlap benefit.

No clearly supported cross-window repeated candidate was observed in these outputs. The run does not establish extraction recall with or without overlap. The discarded duplicate in window 07's first model response is a separate repair event and is not counted again in the final 36 candidates.

## v2.3 repair and its limits

Current implementation: `five-report-extraction-pilot-v2.3-role-filtered-selectors`.

The evidence-bound schema has a confirmed live processing baseline. The next repair addresses source mention eligibility, using general source-role rules rather than report-specific names or reference answers:

- Capitalization alone no longer makes an unknown word Software. Unknown proper names need a software naming/list/appositive context, a short row under an explicit software-use caption, a software object/technical API-use context, or an executable filename. Proper-name matching also stops across sentence punctuation.
- A catalog Technique/Tactic name or alias needs its corresponding exact ATT&CK ID in the same source unit. That ID is retained as a required literal proof for the named endpoint. Ambiguous multiple-ID name/type matches are omitted; literal ID endpoints remain available. Generic nouns are not promoted to behavior/tactic identities solely because the catalog contains the word.
- A Software alias occurring only inside a qualified actor phrase cannot supply an independent software endpoint in that evidence. A separate literal software occurrence, such as a named payload being deployed, still can.

The existing source-span, typed-pattern, model-digest and identity checks remain in force. No model-generated relation is automatically accepted. Source naming hints remain conservative heuristics and can omit real software or admit ambiguous names; these rules are not exhaustive NER or semantic understanding. Certainty, negation, clause attribution and qualified actor scope still need semantic review. The software hints themselves do not prove a USES relationship.

An offline eligibility audit maps the old proposals by exact name/type and selected units into the new menu. It excludes all 18 candidates marked Reject above and also excludes 02.2, whose full software surface came only from the appendix reference. All 14 directly supported examples and the other three Review examples remain selectable. This audit checks availability under new constraints; it does not generate a new answer, accept any candidate, measure general recall or establish future model quality.

All 138 offline tests pass. Added regressions cover capitalized verbs/reference phrases, valid unfamiliar tool names and table rows, software API contexts, local ID requirements, and actor/software name collisions with separate legitimate payload mentions. The actual ten-window preview passes, with 12–28 indexed mentions and 1660–4167 estimated system/prompt/schema tokens, plus the unchanged 700 output tokens and 256 reserved chat tokens within context 8192. All ten new schemas and their 321 literal endpoint combinations were checked, with zero empty enumerations.

Prepared windows, source hashes, tokenizer, model digest, catalog and benchmark splits are unchanged. The prepared-run fingerprint remains `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`. Original run logs and generated review documents are preserved. No live Ollama/Neo4j calls or installers were run by the assistant.

## Next live step

Keep Ollama running and create a fresh run because mention eligibility and extraction configuration changed:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

Use the normal command, not `--retry-run` on an older format. v2.3 live processing and semantic outcomes remain unconfirmed. Full-corpus extraction/ingestion, refreshed indexes, application integration and controlled final evaluation remain unfinished.
