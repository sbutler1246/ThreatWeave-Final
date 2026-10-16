# Extraction pilot v2.4 review and v2.5 prompt update

Later checkpoint: [the v2.5 review and v2.6 source-context repair](ThreatWeave_corpus_extraction_pilot_v2_5_development_review.md) records the completed v2.5 run and current next command. This document preserves the earlier review and pre-run instructions.

October 14, 2026. AI-assisted development review of all 24 saved candidates and the three empty windows. Judgments are provisional source readings, not human verification, benchmark labels, extraction F1 or final quality scores. These notes are not extraction, retrieval or generation inputs.

## Saved live outcome

Run: `work/corpus_extraction_pilot/20261014T234322Z-d5a41a92`, using `five-report-extraction-pilot-v2.4-local-evidence-selectors`.

Seven windows produced candidates and three returned empty results. There were no final processing failures, HTTP failures or output-limit truncations. Windows 08 and 10 each required one repair because their first replies repeated a relationship. Both original replies remain saved. Window 08 initially repeated its sole TOR relationship four times; window 10 repeated cmd.exe. These repair events are separate from duplicates in final accepted output.

The final output contains **24 source-checked relations and 24 unique document candidates**, with zero repeated candidates and zero exact duplicate supports. The provisional review below has **23 Supported, one Review and zero Reject** dispositions. Original records still mark all candidates pending semantic review; no graph writes occurred. These counts do not establish precision or completeness.

The run received 12 HTTP-200 generation responses and generated 1262 tokens. Total elapsed time was 27.096 seconds, including availability checking and sequential extraction/validation but excluding source/tokenizer/catalog initialization. Summed attempt time was 24.717 seconds; median window time was 2.558 seconds. Different output lengths, empty results, repairs, model state and prompt versions prevent a controlled speed comparison with earlier runs.

| Window | Report | Candidates | Attempts | Case time |
| --- | --- | ---: | ---: | ---: |
| 01 | BianLian | 0 | 1 | 4.510 s |
| 02 | BianLian | 4 | 1 | 2.566 s |
| 03 | Rhysida | 0 | 1 | 0.415 s |
| 04 | Rhysida | 4 | 1 | 2.494 s |
| 05 | Scattered Spider | 4 | 1 | 2.550 s |
| 06 | Scattered Spider | 4 | 1 | 2.619 s |
| 07 | ALPHV Blackcat | 4 | 1 | 2.371 s |
| 08 | ALPHV Blackcat | 1 | 2 | 2.903 s |
| 09 | Phobos | 0 | 1 | 0.390 s |
| 10 | Phobos | 3 | 2 | 3.932 s |

## Individual source review

IDs identify the window directory and one-based position in `candidate_extraction.json`. Selected evidence units and absolute offsets remain in `quote_alignment.json`. Supported means the selected source asserts the candidate relationship; it does not approve ingestion or imply human verification. Catalog identities are separate from IDs explicitly reported by the source.

| ID | Candidate | Judgment | Source finding |
| --- | --- | --- | --- |
| 02.1 | Rsocks USES_TECHNIQUE T1090.002 | Review | u002 says the group **may have used** Rsocks to establish SOCKS5 tunnels. The selected software-behavior relationship is inside that uncertain event; it needs qualification review before categorical use. The uncertainty flag is retained. |
| 02.2 | BianLian group actors USES_TECHNIQUE T1059.001 | Supported | u006 explicitly connects actor use of PowerShell with its ID. |
| 02.3 | BianLian actors USES_TECHNIQUE T1112 | Supported | u008 explicitly describes actor modification of the Windows Registry with this ID. Preserve this literal actor phrase. |
| 02.4 | Advanced Port Scanner USES_TECHNIQUE T1046 | Supported | u015 describes scanning open ports and retrieving running-program versions, with this annotation. |
| 04.1 | net USES_TECHNIQUE T1087.002 | Supported | u004 gives the net user domain command with this ID. |
| 04.2 | net USES_TECHNIQUE T1018 | Supported | u005 gives the domain-computers group command with this ID. |
| 04.3 | net USES_TECHNIQUE T1069.002 | Supported | u006 gives the domain-admins group command with this ID. |
| 04.4 | net USES_TECHNIQUE T1069.001 | Supported | u007 gives the local-administrators command with this ID. |
| 05.1 | Scattered Spider threat actors USES_TECHNIQUE T1598 | Supported | Explicit public-reporting subject in u005 scopes the phone/SMS credential-targeting item in u006. Preserve that reporting attribution. |
| 05.2 | Same actor USES_TECHNIQUE T1204 | Supported | u005 scopes u007, which describes directing employees to run remote access tools with this annotation. |
| 05.3 | Same actor USES_TECHNIQUE T1219 | Supported | Same explicit subject/list assertion and remote access tools annotation. |
| 05.4 | Same actor USES_TECHNIQUE T1566 | Supported | Same explicit subject/list assertion, with the reported T1566 annotation. |
| 06.1 | Scattered Spider USES Mimikatz | Supported | u004 explicitly captions tools used by this actor; u011 names Mimikatz [S0002]. |
| 06.2 | Scattered Spider USES Pulseway | Supported | Same actor-use caption scopes the Pulseway row u015. |
| 06.3 | Scattered Spider USES Splashtop | Supported | Same actor-use caption scopes the Splashtop row u019. |
| 06.4 | Scattered Spider USES Tactical.RMM | Supported | Same actor-use caption scopes the Tactical.RMM row u021. |
| 07.1 | ALPHV Blackcat affiliates USES_TECHNIQUE T1598 | Supported | Named affiliates in u004 scope the adjacent Actors continuation u005, which reports phone/SMS credential targeting with this ID. |
| 07.2 | Same actor USES_TECHNIQUE T1586 | Supported | Same controlled continuation explicitly reports credentials used to access the target network with this ID. |
| 07.3 | Same actor USES AnyDesk | Supported | u007 explicitly says affiliates deploy remote access software including AnyDesk. |
| 07.4 | Same actor USES Mega sync | Supported | u007 names the complete source software phrase, Mega sync. |
| 08.1 | ALPHV Blackcat affiliates USES TOR | Supported | u005 explicitly names these affiliates communicating with victims via TOR [S0183]. It does not import Some from the preceding sentence. |
| 10.1 | Phobos actors USES 1saas.exe | Supported | u004 explicitly says these actors run the executable to deploy additional payloads. |
| 10.2 | Same actor USES cmd.exe | Supported | Same explicit executable-use assertion. Local catalog resolution to S0106 does not mean the source reported that ID. |
| 10.3 | Smokeloader USES_TECHNIQUE T1055.002 | Supported | u009 directly describes API manipulation enabling process injection and reports this ID. |

The legitimate-tool warning in the Scattered Spider report does not negate its report-specific actor-use caption. These candidates do not imply that every installation of these products is malicious. Actor qualifiers, unresolved software identities and public-reporting attribution remain part of the source interpretation.

## Empty windows and coverage limits

All three empty replies completed with `done_reason=stop`, consuming five or six generated tokens. They were valid abstentions, not timeouts, truncations or processing failures. Each had available evidence/type combinations:

- **01, BianLian: eight patterns.** The source mixes uncertain access/proxy claims with explicit custom-backdoor, remote-management and local-account activity. Returning no relationships misses usable material; it does not establish that every available pattern is supported.
- **03, Rhysida: seven patterns.** The source directly describes valid-credential VPN authentication and actor use of Gootloader. The four net relationships extracted in window 04 do not replace these distinct assertions.
- **09, Phobos: six patterns.** The source contains actor phishing/IP-scanner access activity as well as conditional RDP and related software descriptions. This window remained empty while window 10 supplied different Phobos facts.

Window 06's actor-caption table now produced candidates. No final Ngrok/Rsocks cross-sentence binding, net/Ipconfig/nltest cross-item binding, bare actor-name software, shortened Mega endpoint or copied Some qualifier was observed in this run. This is a finding about the saved output, not a guarantee of general behavior.

The four-relation bound also limits coverage in nonempty windows. No exhaustive source annotation or false-negative count was performed. No cross-window duplicate fact appeared, so the duplicate count establishes no overlap benefit. Graph-write rate, index-build time and broader resource measurements remain pending.

## v2.5 prompt update and offline verification

Current implementation: `five-report-extraction-pilot-v2.5-explicit-evidence-menu`.

The v2.4 prompt showed the source units and mentions but referred to allowed evidence combinations supplied only through the response schema. That may make valid selection difficult; this run does not prove it caused the empty replies. v2.5 also prints the exact same evidence/type alternatives as an `EVIDENCE_OPTIONS` menu in the model-visible prompt. The instructions distinguish possible combinations from asserted facts, require checking the source action, allow empty output and explicitly prohibit repeating the same relationship to fill the response limit.

No source windows, mention rules, evidence patterns, endpoint identities, response schema, validator, model settings or output limits changed. No candidates are auto-filled from the menu. This is a prompt experiment to test valid selection and abstention behavior, not a repair that guarantees additional facts or semantic accuracy. A fresh live run is required because the prompt/configuration identity changed; empty results are not reclassified as failed cases.

All **145 offline tests passed**. The new synthetic test checks parity between model-visible options and schema alternatives, tests all offered endpoint combinations, preserves negative examples as possibilities requiring semantic judgment, and verifies that abstention remains allowed even when options exist. Service tests use mocks; the assistant made no live Ollama/Neo4j calls or installations.

The actual ten-window preview passed frozen source/tokenizer/catalog checks and context budgets: 1839–4792 estimated system/prompt/schema tokens, plus 700 output tokens and 256 reserved chat tokens within context 8192. The additional menu increases prompt size; its live timing and output effects remain unmeasured.

Separately, all ten v2.4 chunks, final raw replies, completed response records, reconstructed candidates, identity resolutions, selected source units, absolute quote spans and aggregate counts were rechecked offline. They match the saved records. All 24 source supports remain aligned; the evidence patterns match the unchanged v2.4 patterns. Original runs and generated reviews remain unmodified.

Prepared source fingerprint: `b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635`. Gold triples and QA reference answers are not inputs. Full-corpus ingestion, refreshed indexes, application integration and controlled held-out evaluation remain unfinished.

## Next command

With Ollama running, start a fresh v2.5 run over the same frozen ten windows:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_pilot.py"
```

Do not use `--retry-run` on earlier versions. v2.5 live outcomes remain pending.
