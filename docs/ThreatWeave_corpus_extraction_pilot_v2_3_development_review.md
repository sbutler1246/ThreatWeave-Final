# Extraction pilot v2.3 review and v2.4 repair

Later checkpoint: [the v2.4 review and v2.5 prompt update](ThreatWeave_corpus_extraction_pilot_v2_4_development_review.md) records the completed v2.4 run and current next command. The original v2.3 review and pre-run v2.4 instructions below remain as history.

October 14, 2026. AI-assisted development review of all 26 saved candidate relations and the two empty windows. Judgments are provisional source-review findings, not human ratings, gold annotations, extraction F1 or final quality scores. These notes are not extraction, retrieval or generation inputs.

## Saved live outcome

Run: `work/corpus_extraction_pilot/20261014T233012Z-b15bc999`.

Eight windows produced candidates and two returned empty results. There were no final processing failures, HTTP failures or output-limit truncations. Windows 02, 05 and 08 required one repair each because their first replies repeated relationships. Their original replies remain saved.

The run produced **26 source-checked candidate relations, grouped into 23 unique document candidates**. All remain pending semantic review in the original records. Source alignment and permitted types did not establish correct subject/action/endpoint binding. No graph writes occurred.

There were 13 HTTP-200 generation responses and 1490 generated tokens. Total elapsed time was 29.704 seconds, including availability checking and sequential extraction/validation but excluding source/tokenizer/catalog initialization. Summed attempt time was 27.409 seconds; median window time was 2.481 seconds. Different output lengths, repairs, empty results and model-loading state prevent a controlled speed comparison with prior versions.

| Window | Report | Candidates | Attempts | Case time |
| --- | --- | ---: | ---: | ---: |
| 01 | BianLian | 4 | 1 | 6.59 s |
| 02 | BianLian | 3 | 2 | 4.06 s |
| 03 | Rhysida | 4 | 1 | 2.42 s |
| 04 | Rhysida | 4 | 1 | 2.52 s |
| 05 | Scattered Spider | 1 | 2 | 2.90 s |
| 06 | Scattered Spider | 0 | 1 | 0.47 s |
| 07 | ALPHV Blackcat | 4 | 1 | 2.37 s |
| 08 | ALPHV Blackcat | 2 | 2 | 3.31 s |
| 09 | Phobos | 0 | 1 | 0.38 s |
| 10 | Phobos | 4 | 1 | 2.44 s |

## Individual source review

IDs refer to the window directory and one-based relation position in its `candidate_extraction.json`. Exact selected units and absolute offsets remain in `quote_alignment.json`. “Supported” is a provisional reading of the cited source; “Review” needs qualification/scope/identity judgment; “Reject” identifies unsupported binding. No label approves ingestion or alters original output.

| ID | Candidate | Judgment | Reason |
| --- | --- | --- | --- |
| 01.1 | BianLian group actors USES_TECHNIQUE T1078 | Supported | The source explicitly describes access with compromised RDP credentials. “Likely acquired” concerns credential provenance. |
| 01.2 | Same actor USES_TECHNIQUE phishing / T1566 | Review | Phishing occurs in the qualified alternative about likely credential acquisition. Preserve that scope. |
| 01.3 | Same actor USES_TECHNIQUE T1566 | Review | Same assertion as 01.2 under its ID, with the same qualification. |
| 01.4 | Same actor USES_TECHNIQUE T1190 | Reject | The selected passage says “possibly leveraging” ProxyShell; categorical use violates the prompt's exclusion of speculative relationships. |
| 02.1 | Ngrok USES_TECHNIQUE T1090 | Supported | The clipped source explicitly calls Ngrok a reverse-proxy tool. This is software behavior, separate from the uncertain actor-use clause. |
| 02.2 | Ngrok USES_TECHNIQUE T1090.002 | Reject | The sentence reporting the external-proxy behavior names Rsocks, not Ngrok. Sharing a source line does not bind this ID to Ngrok. |
| 02.3 | BianLian group actors USES Windows as Software | Reject | The naming heuristic admitted Windows from “native Windows tools”; this selected use passage names PowerShell/Windows Command Shell and Windows defender, not an independent product named Windows. |
| 03.1 | Rhysida actors USES_TECHNIQUE T1078 | Supported | Compromised valid credentials for VPN authentication are explicit. |
| 03.2 | Rhysida actors USES Gootloader | Supported | The source directly says Rhysida actors used Gootloader malware. |
| 03.3 | net USES_TECHNIQUE T1016 | Reject | The annotated item is Ipconfig [T1016]; net appears elsewhere in the same paragraph. |
| 03.4 | net USES_TECHNIQUE T1482 | Reject | The annotated item is nltest [T1482]; net co-occurrence does not establish that mapping. |
| 04.1 | net USES_TECHNIQUE T1087.002 | Supported | Literal net user command with its annotation. |
| 04.2 | net USES_TECHNIQUE T1018 | Supported | Literal domain-computers command with its annotation. |
| 04.3 | net USES_TECHNIQUE T1069.002 | Supported | Literal domain-admins command with its annotation. |
| 04.4 | net USES_TECHNIQUE T1069.001 | Supported | Literal local-administrators command with its annotation. |
| 05.1 | Scattered Spider threat actors USES Scattered Spider as Software | Reject | A bare actor-name occurrence survived the qualified-actor mask. “Tools Scattered Spider repurposed” is an actor relative clause, not software named Scattered Spider. |
| 07.1 | ALPHV Blackcat affiliates USES_TECHNIQUE T1598 | Supported | Phone/SMS credential targeting and the ID are explicit. |
| 07.2 | Same actor USES_TECHNIQUE T1586 | Supported | Credential-based target-network access and the ID are explicit. |
| 07.3 | Same actor USES AnyDesk | Supported | The source directly says affiliates deploy AnyDesk. |
| 07.4 | Same actor USES Mega | Review | The actual software phrase is “Mega sync”; the unknown-name matcher supplied only its capitalized prefix. Identity is not established for that shortened endpoint. |
| 08.1 | Some ALPHV Blackcat affiliates USES TOR | Review | The TOR sentence names ALPHV Blackcat affiliates generally; “Some” comes from the preceding extortion-without-deployment sentence. The subset binding needs review. |
| 08.2 | Same actor USES S0183 | Review | Same resolved TOR assertion and subset-scope issue as 08.1. |
| 10.1 | Phobos actors USES_TECHNIQUE Windows command shell / T1059.003 | Supported | The passage connects executed commands and shell functions to actor activity and reports T1059.003. |
| 10.2 | Same actor USES_TECHNIQUE T1059.003 | Supported | Same supported assertion under the explicit ID. |
| 10.3 | Same actor USES_TECHNIQUE T1105 | Review | The ID is present, but its generic shell-capability sentence does not clearly assert an actor transfer event. Literal ID presence alone cannot settle the attribution. |
| 10.4 | Smokeloader USES_TECHNIQUE T1055.002 | Supported | API manipulation and process injection are directly described with the ID. |

This provisional reading has 14 Supported, six Review and six Reject dispositions over 26 raw candidates. It is not a precision/recall score. The TOR subset attribution is treated more cautiously here than in earlier provisional notes: the literal “Some” and TOR assertions are in different sentences. Earlier logs and notes remain intact.

## Empty windows and duplicates

Window 06 contains explicit “Tools Used by Scattered Spider” and “Malware Used by Scattered Spider” tables. Its saved schema had 20 source/type patterns, including caption/row choices. The empty reply was not caused by missing source or a zero-choice schema. Fleetdeck.io and other rows provide relevant source material, but this run selected none. This is a qualitative omission, not an exhaustive false-negative count.

Window 09 contains explicit Phobos actor access behavior and technique annotations, including phishing and IP-scanner activity. Its saved schema had four source/type patterns. It also returned empty on its first attempt. The bounded mention/actor rules and model selection both limit coverage; an empty result does not demonstrate that the source has no usable relationships.

All three repeated candidates were **within-window name/ID duplication**, with identical source support:

- Window 01: phishing and T1566 resolve to the same technique; both supports span 4654–4859.
- Window 08: TOR and S0183 resolve to the same software; both span 5323–5657.
- Window 10: Windows command shell and T1059.003 resolve to the same technique; both span 4570–4998.

These account for 26 raw versus 23 unique candidates and all three exact duplicate supports. No cross-window duplicate candidate was observed, so these counts establish no overlap benefit. The three initial-response repair events are separate from these final canonical duplicates.

## v2.4 repair

Current implementation: `five-report-extraction-pilot-v2.4-local-evidence-selectors`.

The repair keeps the measured source windows unchanged and narrows the evidence/identity combinations inside each window:

- Evidence units now split at sentence boundaries and separators following bracketed annotations. Separate annotated list items no longer let net inherit Ipconfig/nltest IDs; separate sentences no longer let Ngrok inherit the Rsocks-only external-proxy ID. Exact source offsets and original line identity are retained.
- A controlled adjacent pair allows a named actor sentence followed by Actors/The actors/They in the same original line. It does not carry an actor into a sentence naming a different actor. Table row scopes account for descriptions split into multiple units, keeping their original row association.
- Explicit software lists retain full literal names with lowercase components, such as “Mega sync,” and suppress shorter unknown-name prefixes. Generic “Windows tools” wording no longer supplies a standalone Windows software candidate. Known actor aliases are excluded from the unknown-software fallback unless independently declared in a software context.
- Independently occurring full actor phrases retain their respective qualifiers, even if one phrase also occurs inside a longer qualified phrase elsewhere. A subset qualifier is not silently copied to a separate sentence's general actor phrase.
- Each evidence alternative offers one selector per resolved typed identity. Technique/tactic alternatives prefer the literal ID; software alternatives prefer a literal name when available. Runtime duplicate checking also compares resolved identities, so name/ID variants cannot consume multiple relationship slots. Original model replies are preserved when a duplicate causes a repair or final failure.

These are source and identity constraints, not semantic approval. Speculation, negation, compound-clause attribution, actor scope and valid omissions remain review concerns. More granular units can omit valid cross-sentence relationships; the bounded anaphora/table rules do not provide exhaustive coreference or NER. No claim of general extraction recall or final quality is justified.

All **144 offline tests** pass. New tests cover exact Unicode offsets after sentence/list splitting, cross-tool ID rejection, controlled actor continuation, independently qualified actors, full software names, canonical duplicates and table descriptions with multiple sentences. The actual ten-window preview passes with 12–27 indexed mentions and 1682–3858 estimated system/prompt/schema tokens, plus 700 output tokens and 256 reserved chat tokens within context 8192. Frozen source/tokenizer/catalog checks pass. The assistant made no live service calls or installations.

All 26 original supports remain aligned to their source text, and all saved runs/generated reviews remain unchanged. Prepared source fingerprint: `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`. Gold triples and QA reference answers are not inputs. No graph writes or benchmark scores were produced.

## Next command

With Ollama running, start a fresh run. Evidence-unit IDs and extraction configuration changed, so do not retry an older run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

The v2.4 live processing and semantic outcome remain pending. Full-corpus ingestion, refreshed indexes, application integration and controlled held-out evaluation remain unfinished.
