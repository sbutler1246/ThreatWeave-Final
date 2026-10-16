# Corpus coverage inventory after the additional development batch

Preparation update: all three eligible remaining reports now have 33 source windows prepared and checked offline. [The operator extraction step](ThreatWeave_corpus_extension_step.md) records counts, artifacts, tests and selector limitations. No live extraction has been started by the assistant. The inventory below describes the preceding source-discovery checkpoint.

October 15, 2026. The operator restarted ThreatWeave after both matching index builds. A fresh browser session loaded the ThreatWeave page at `http://127.0.0.1:8501/` with Full hybrid selected, connection settings, an empty question field and the Ask ThreatWeave control. No visible startup error appeared. No question, credential or service request was submitted by the assistant. This verifies initial page loading; live application queries on the refreshed scope remain untested.

The completed development scope contains 41 CISA source parents, 96 direct ATT&CK reference parents, 215 text chunks, 117 graph vectors and 179 accepted directed facts. The frozen corpus manifest contains fifteen advisory snapshots. Preparation and extraction of the existing five-report technical-section selection does not establish whole-corpus or exhaustive fact coverage.

The following inventory uses only the frozen corpus manifest, split metadata and normalized source text. Gold triples and QA reference answers were not read.

| Advisory | Expansion status |
| --- | --- |
| AA23-136A — BianLian | Prepared five-report development selection |
| AA23-319A — Rhysida | Prepared five-report development selection |
| AA23-320A — Scattered Spider | Prepared five-report development selection |
| AA23-353A — ALPHV Blackcat | Prepared five-report development selection |
| AA24-060A — Phobos | Prepared five-report development selection |
| AA24-038A — PRC actors / Volt Typhoon | Eligible for new development source preparation |
| AA23-144A — PRC actor living off the land / Volt Typhoon | Eligible for new development source preparation |
| AA22-321A — Hive | Eligible for new development source preparation |
| AA23-165A — LockBit | Contains held-out evidence; exclude from broader development expansion |
| AA23-061A — Blacksuit / Royal | Contains held-out evidence; exclude from broader development expansion |
| AA24-131A — Black Basta | Contains held-out evidence; exclude from broader development expansion |
| AA24-109A — Akira | Contains held-out evidence; exclude from broader development expansion |
| AA25-071A — Medusa | Contains held-out evidence; exclude from broader development expansion |
| AA23-352A — Play | Contains held-out evidence; exclude from broader development expansion |
| AA23-075A — LockBit 3.0 | Contains held-out evidence; exclude from broader development expansion |

Whole-report exclusion is the conservative development expansion rule already used by the source preparer. Earlier, explicitly bounded development scopes remain historical/current pipeline inputs as previously declared; their presence does not authorize expansion into other portions of a held-out report. Final evaluation processing needs a separately frozen protocol.

All three eligible unprepared reports have standalone Technical Details and following Mitigations headings under the existing section detector. Their exact technical spans in the frozen normalized text are AA24-038A `6032:48255`, AA23-144A `2866:19961` and AA22-321A `1806:11131`. Token-measured preparation, prompt-budget checks and selector coverage inspection have not yet been performed for these three reports. They are not yet extraction inputs or index parents.

The original five-report preparation contains 54 windows. Ten were extracted in the preserved pilot and 44 in the additional batch. The latter originally produced 24 candidate windows, 18 empty results and two validation failures; the failures were recovered offline with their original statuses and outputs preserved. The selected imports contain only reviewed Supported candidates. Eighteen empty results are not negative gold labels. Recognition/table coverage, conditional facts and the four-relation cap remain assessment items.

The next implementation stage is source-only preparation of the three eligible reports using frozen tokenization, source boundaries and extraction/retrieval settings, followed by offline preflight and an operator-run extraction. The existing 44-window extraction does not need repeating. Review must precede further imports and index refreshes. No new extraction or final evaluation was started during this inventory.
