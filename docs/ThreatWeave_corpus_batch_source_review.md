# Additional development batch: AI-assisted source review

October 15, 2026. Human verification remains pending. No graph writes or new model calls.

Original run: work/corpus_extraction_batch/20261015T170956Z-255671f4. The original 24 candidate windows, 18 empty outputs and two failures remain unchanged. Separate offline artifacts recover three unique Rhysida relations by removing one repeated link, and four Phobos relations after fixing the unrelated-affiliate validation error.

All 44 source windows were revalidated. There are 68 candidate relation occurrences; 53 Supported, 10 Review and five Reject. Only Supported candidates are eligible for a development import. All original and derived evidence remains traceable.

Empty outputs are not negative gold labels or proof of missing source facts. Coverage review is still pending, including table/command sections, recognition limits and the four-relation cap. Three windows had no recognized source mentions. This batch does not establish exhaustive extraction or final quality scores.

| Window | Candidate | Decision | Source-review reason |
| --- | ---: | --- | --- |
| 01 | 0 | supported | The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1057. No negation, uncertainty or additional condition changes this selected assertion. |
| 01 | 1 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> Windows Command Shell. No negation, uncertainty or additional condition changes this selected assertion. |
| 01 | 2 | supported | The selected exact source passage directly attributes BianLian actors -> USES -> Impacket. No negation, uncertainty or additional condition changes this selected assertion. |
| 01 | 3 | review | SessionGopher use is definite, but the asserted credential-extraction purpose and its T1552.004 mapping are qualified by likely. |
| 02 | 0 | review | The repeated SessionGopher passage qualifies the technique purpose with likely; do not promote that purpose to a definite actor technique. |
| 02 | 1 | supported | The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1021.001. No negation, uncertainty or additional condition changes this selected assertion. |
| 02 | 2 | supported | The selected exact source passage directly attributes BianLian actors -> USES -> Command Shell. No negation, uncertainty or additional condition changes this selected assertion. |
| 02 | 3 | supported | The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1012. No negation, uncertainty or additional condition changes this selected assertion. |
| 03 | 0 | reject | FTP is explicitly a file-transfer protocol here, not a named software entity; the selected Software endpoint has the wrong source role. |
| 03 | 1 | supported | The source explicitly links Rclone exfiltration to T1537; retain that source mapping and its quote without inventing additional context. |
| 03 | 2 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> Rclone. No negation, uncertainty or additional condition changes this selected assertion. |
| 03 | 3 | supported | The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1567.002. No negation, uncertainty or additional condition changes this selected assertion. |
| 07 | 0 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> Windows Command Shell. No negation, uncertainty or additional condition changes this selected assertion. |
| 08 | 0 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> Windows Command Shell. No negation, uncertainty or additional condition changes this selected assertion. |
| 08 | 1 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> net.exe. No negation, uncertainty or additional condition changes this selected assertion. |
| 10 | 0 | supported | The selected exact source passage directly attributes BianLian actors -> USES -> Advanced Port Scanner. No negation, uncertainty or additional condition changes this selected assertion. |
| 10 | 1 | supported | The selected exact source passage directly attributes BianLian actors -> USES -> SoftPerfect Network Scanner. No negation, uncertainty or additional condition changes this selected assertion. |
| 11 | 0 | review | The source says the actors may be using Ngrok; this does not establish definite use. |
| 11 | 1 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> Rclone. No negation, uncertainty or additional condition changes this selected assertion. |
| 11 | 2 | supported | The selected exact source passage directly attributes BianLian group actors -> USES -> FTP. No negation, uncertainty or additional condition changes this selected assertion. |
| 12 | 0 | supported | The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1021.004. No negation, uncertainty or additional condition changes this selected assertion. |
| 12 | 1 | supported | The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1003.003. No negation, uncertainty or additional condition changes this selected assertion. |
| 12 | 2 | supported | The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1070.001. No negation, uncertainty or additional condition changes this selected assertion. |
| 12 | 3 | supported | The literal PsExec.exe row is scoped by the explicit Tools Leveraged by Rhysida Actors caption. |
| 13 | 0 | reject | The source describes a batch script likely placing 1.ps1. It does not attribute the batch-script technique to 1.ps1 itself. |
| 14 | 0 | supported | The selected contiguous source span ties the Rhysida encryptor to post-encryption deletion of its binary, annotated T1070.004. |
| 14 | 1 | supported | The selected contiguous span ties the Rhysida encryptor cleanup command to a hidden command window, explicitly annotated T1564.003. |
| 14 | 2 | supported | The selected exact source passage directly attributes cmd.exe -> USES_TECHNIQUE -> T1112. No negation, uncertainty or additional condition changes this selected assertion. |
| 14 | 3 | supported | The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1587. No negation, uncertainty or additional condition changes this selected assertion. |
| 21 | 0 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> AZCopy. No negation, uncertainty or additional condition changes this selected assertion. |
| 21 | 1 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> ipconfig. No negation, uncertainty or additional condition changes this selected assertion. |
| 21 | 2 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> nltest. No negation, uncertainty or additional condition changes this selected assertion. |
| 21 | 3 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> 1.ps1. No negation, uncertainty or additional condition changes this selected assertion. |
| 22 | 0 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> cmd.exe. No negation, uncertainty or additional condition changes this selected assertion. |
| 22 | 1 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> ipconfig. No negation, uncertainty or additional condition changes this selected assertion. |
| 22 | 2 | supported | The selected exact source passage directly attributes Rhysida actors -> USES -> net. No negation, uncertainty or additional condition changes this selected assertion. |
| 23 | 0 | review | The source qualifies the exfiltration/encryption activity with may; definite T1486 use is not established by this selected sentence. |
| 23 | 1 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> TOR. No negation, uncertainty or additional condition changes this selected assertion. |
| 25 | 0 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES_TECHNIQUE -> T1556.006. No negation, uncertainty or additional condition changes this selected assertion. |
| 25 | 1 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES_TECHNIQUE -> T1606. No negation, uncertainty or additional condition changes this selected assertion. |
| 25 | 2 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES_TECHNIQUE -> T1219. No negation, uncertainty or additional condition changes this selected assertion. |
| 25 | 3 | reject | Discovery and lateral-movement tactic IDs annotate the activity in this sentence; their co-occurrence does not state a general PART_OF_TACTIC taxonomy relationship. |
| 26 | 0 | review | ETL-tool use is scoped to instances where data exfiltration is the goal. The unconditional actor-technique triple drops that condition. |
| 26 | 1 | review | Centralized collection is explicitly scoped to instances where exfiltration is the goal; preserve the condition before accepting an unconditional triple. |
| 26 | 2 | review | The T1530 annotation is in the same conditionally scoped ETL statement; an unconditional triple would omit that scope. |
| 26 | 3 | supported | The source directly reports actor searches for emails annotated T1114. To determine if expresses the purpose of observed searching, not uncertain occurrence. |
| 28 | 0 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> Raccoon Stealer. No negation, uncertainty or additional condition changes this selected assertion. |
| 29 | 0 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> Raccoon Stealer. No negation, uncertainty or additional condition changes this selected assertion. |
| 30 | 0 | supported | The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> Snowflake Data Cloud. No negation, uncertainty or additional condition changes this selected assertion. |
| 34 | 0 | supported | The selected exact source passage directly attributes ALPHV Blackcat/ALPHV affiliates -> USES -> Evilginx2. No negation, uncertainty or additional condition changes this selected assertion. |
| 35 | 0 | supported | The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1562.004. No negation, uncertainty or additional condition changes this selected assertion. |
| 35 | 1 | review | The source attaches T1490 to Startup-folder/Run-key persistence, creating a behavior/ID mismatch. Preserve the source but exclude this mapping pending review. |
| 35 | 2 | supported | The selected exact source passage directly attributes Phobos actors -> USES_TECHNIQUE -> T1106. No negation, uncertainty or additional condition changes this selected assertion. |
| 35 | 3 | reject | FTP names the protocol/server endpoint here, not software implementing a technique; the generated Software endpoint is inappropriate. |
| 36 | 0 | supported | The source directly describes the Phobos.exe encryption capability and annotates T1486; Phobos is the ransomware identity, not an actor. |
| 36 | 1 | review | The sentence describes instant-messaging communication but annotates T1585 (Establish Accounts). This behavior/ID mismatch needs review before import. |
| 36 | 2 | supported | An explicit Phobos actors subject is followed by They use vssadmin.exe to delete shadow copies, supporting the tool-use link. |
| 36 | 3 | supported | The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1562.004. No negation, uncertainty or additional condition changes this selected assertion. |
| 37 | 0 | supported | The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1562.004. No negation, uncertainty or additional condition changes this selected assertion. |
| 41 | 0 | supported | The selected exact source passage directly attributes Phobos actors -> USES -> Windows Management Instrumentation. No negation, uncertainty or additional condition changes this selected assertion. |
| 42 | 0 | supported | The selected exact source passage directly attributes Phobos actors -> USES -> Windows Management Instrumentation. No negation, uncertainty or additional condition changes this selected assertion. |
| 42 | 1 | supported | The source explicitly attributes deployment of additional Phobos payloads to Phobos actors; actor and software identities remain separate. |
| 42 | 2 | supported | The selected exact source passage directly attributes Phobos actors -> USES -> 1saas.exe. No negation, uncertainty or additional condition changes this selected assertion. |
| 42 | 3 | supported | The selected exact source passage directly attributes Phobos actors -> USES -> cmd.exe. No negation, uncertainty or additional condition changes this selected assertion. |
| 43 | 0 | review | The source says actors can use Universal Virus Sniffer. Capability/possibility wording does not establish observed use in this selected passage. |
| 43 | 1 | supported | The selected exact source passage directly attributes Phobos actors -> USES -> Mimikatz. No negation, uncertainty or additional condition changes this selected assertion. |
| 44 | 0 | reject | The actor used WinSCP to reach an FTP server. Treating FTP itself as Software changes the asserted tool and source role. |
| 44 | 1 | supported | The selected exact source passage directly attributes Phobos threat actors -> USES -> Phobos.exe. No negation, uncertainty or additional condition changes this selected assertion. |
