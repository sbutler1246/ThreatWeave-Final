# Remaining three development reports: AI-assisted source review

October 15, 2026. Human verification remains pending. No new model calls or graph writes.

Original extraction: work\corpus_extension_extraction\20261016T000937Z-0cef6551. Original failures/raw outputs remain unchanged.
Window 08 repeated the same actor-to-Mimikatz link with two supports. A separate duplicate-only derivation keeps the first support and records the removed selection, yielding three candidates.
All 33 frozen windows were revalidated. There are 46 relation occurrences and 41 unique document candidate facts; five repeated occurrences and no exact repeated source supports.
Source review: 27 Supported, nine Review and ten Reject. Only Supported candidates are eligible for development import. Decisions are AI-assisted, not human-verified or gold labels.
Sixteen empty results remain coverage-review items. Sixteen windows had no selectable relation patterns under the frozen selector. Extraction is bounded to four relations per window.
The frozen ATT&CK 17.1 snapshot was inspected for the scope of T1218 and T1016.001; generic native-tool use and network connectivity do not alone establish those more specific behaviors.
This review does not repair semantic errors by inventing alternate triples, actor aliases, payload identities or source annotations.

| Window | Candidate | Decision | Source-review reason |
| --- | ---: | --- | --- |
| 02 | 0 | reject | NTDS.dit is the Active Directory database file accessed or stolen in this passage, not a Software entity used by the actor. |
| 04 | 0 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1591. The selected assertion is definite and its endpoint roles match the source. |
| 04 | 1 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1589.002. The selected assertion is definite and its endpoint roles match the source. |
| 04 | 2 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1090.003. The selected assertion is definite and its endpoint roles match the source. |
| 04 | 3 | supported | The source explicitly describes Volt Typhoon actors using routers implanted with KV Botnet malware to support their operations. |
| 05 | 0 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1059. The selected assertion is definite and its endpoint roles match the source. |
| 05 | 1 | review | The source annotates native tools/processes with T1218, but the selected passage does not describe proxy execution of malicious content. Hold this broad behavior/ID mapping for review. |
| 05 | 2 | reject | Actors download comsvcs.dll in the T1105 passage; the downloaded DLL is not the subject performing the ingress transfer. |
| 05 | 3 | supported | Observed use of Magnet RAM Capture is definite. The later likely-qualified analysis purpose is not part of this tool-use assertion. |
| 06 | 0 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES -> FRP. The selected assertion is definite and its endpoint roles match the source. |
| 06 | 1 | review | The passage describes actors packing FRP client files with UPX. Passive packaging is not an explicit FRP-performed action; review this Software-to-technique interpretation before import. |
| 06 | 2 | supported | The source explicitly attributes exploiting privilege-escalation vulnerabilities, annotated T1068, to Volt Typhoon actors; the introductory initial-access clause sets sequence, not uncertainty. |
| 07 | 0 | reject | Co-occurring incident tactic and technique annotations do not explicitly state a general PART_OF_TACTIC taxonomy relationship. |
| 07 | 1 | reject | LOTL names a general living-off-the-land approach, not software. The passage attributes the T1047 command execution to WMIC, not LOTL. |
| 07 | 2 | reject | LOTL is an activity category, not software performing offline password cracking. Its occurrence in the appendix title does not support this endpoint. |
| 07 | 3 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES -> PuTTY. The selected assertion is definite and its endpoint roles match the source. |
| 08 | 0 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES -> Mimikatz. The selected assertion is definite and its endpoint roles match the source. |
| 08 | 1 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1082. The selected assertion is definite and its endpoint roles match the source. |
| 08 | 2 | reject | The source describes deletion of the output file systeminfo.dat, not the systeminfo executable performing deletion. A substring match is not the required software endpoint. |
| 09 | 0 | reject | The selected span describes deletion of systeminfo.dat. It does not state that the systeminfo executable performs T1070.004. |
| 09 | 1 | supported | The selected exact source passage directly attributes tasklist -> USES_TECHNIQUE -> T1057. The selected assertion is definite and its endpoint roles match the source. |
| 09 | 2 | review | The source annotates ping network-connectivity checks with T1016.001, but the selected span does not establish Internet connectivity, the specific frozen technique. Hold the behavior/ID scope for review. |
| 09 | 3 | review | The source records an attempt to use Advanced IP Scanner. Confirmed tool use or execution is not established by this selected passage; preserve the attempt qualification. |
| 11 | 0 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES -> PuTTY. The selected assertion is definite and its endpoint roles match the source. |
| 11 | 1 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES -> PSExec. The selected assertion is definite and its endpoint roles match the source. |
| 11 | 2 | reject | The incident collection and archive annotations do not state a general technique-to-tactic taxonomy relationship. Do not infer PART_OF_TACTIC from co-occurrence. |
| 11 | 3 | reject | The passage qualifies exfiltration with likely and does not state a general technique-to-tactic taxonomy relationship. |
| 12 | 0 | supported | Executing ronf.exe to compress/archive the files is definite. Likely qualifies only its possible rar.exe identity, which is not asserted here. |
| 12 | 1 | supported | The selected exact source passage directly attributes FRP -> USES_TECHNIQUE -> T1090. The selected assertion is definite and its endpoint roles match the source. |
| 12 | 2 | supported | The selected exact source passage directly attributes Volt Typhoon actors -> USES -> FRP. The selected assertion is definite and its endpoint roles match the source. |
| 12 | 3 | supported | The selected contiguous passage explicitly ties Volt Typhoon actors to file compression/archive execution annotated T1560.001. Likely qualifies the utility rename, not the observed compression. |
| 13 | 0 | supported | The source directly describes Volt Typhoon actors using an intermediary server for their FRP operations, supporting actual FRP use. |
| 13 | 1 | supported | The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1112. The selected assertion is definite and its endpoint roles match the source. |
| 13 | 2 | supported | The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1090.001. The selected assertion is definite and its endpoint roles match the source. |
| 17 | 0 | review | This is a comparison in a defensive detection caveat warning against attributing proxy activity to Volt Typhoon. Hold the indirect FRP attribution rather than treat the caveat as a definite use observation. |
| 17 | 1 | review | The passage establishes downloading comsvcs.dll. It does not explicitly establish executing or using the DLL, so the unconditional USES relationship needs review. |
| 20 | 0 | supported | The selected exact source passage directly attributes FRP -> USES_TECHNIQUE -> T1090. The selected assertion is definite and its endpoint roles match the source. |
| 22 | 0 | reject | The T1047 annotation belongs to WMIC commands that execute ntdsutil.exe. The spawned tool is not the subject performing the WMI technique. |
| 29 | 0 | supported | The selected exact source passage directly attributes Hive actors -> USES_TECHNIQUE -> T1133. The selected assertion is definite and its endpoint roles match the source. |
| 29 | 1 | supported | The selected exact source passage directly attributes Hive actors -> USES_TECHNIQUE -> T1566.001. The selected assertion is definite and its endpoint roles match the source. |
| 29 | 2 | supported | The selected exact source passage directly attributes Hive actors -> USES_TECHNIQUE -> T1190. The selected assertion is definite and its endpoint roles match the source. |
| 29 | 3 | supported | The selected exact source passage directly attributes Hive -> USES_TECHNIQUE -> T1562. The selected assertion is definite and its endpoint roles match the source. |
| 30 | 0 | supported | The selected exact source passage directly attributes Hive -> USES_TECHNIQUE -> T1112. The selected assertion is definite and its endpoint roles match the source. |
| 30 | 1 | review | The source says data exfiltration likely uses a combination including Rclone. This does not establish definite Rclone use. |
| 31 | 0 | review | The reinfection passage allows either Hive ransomware or another variant. Preserve that payload disjunction rather than select Hive as the definite payload of the described reinfections. |
| 33 | 0 | review | The source says a possible combination of Rclone and Mega.nz. Definite Rclone use is not established by this selected statement. |
