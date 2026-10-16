# Reviewed corpus batch import preview

Development assertions from actual model output; AI-assisted source review, human review pending.
Only Supported dispositions are selected. Uncertain/conditional review candidates are excluded.
No benchmark gold triples or QA reference answers are inputs.

Extraction run: S:\ThreatWeave\work\corpus_extraction_batch\20261015T170956Z-255671f4
Review manifest: S:\ThreatWeave\docs\ThreatWeave_corpus_batch_source_review.json
Review manifest SHA-256: 52e33242dbfcfd532f7c3acb6b64b1dc8989612dac640c48b14b0621397e567e

Target records: 25 windows, 52 distinct entities, 53 assertions.
Target counts include reused records; these are not counts of newly created graph records.

## AA23-136A:development:llama500:7570:9807

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES_TECHNIQUE → Process Discovery
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1057. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: (New, November 20, 2024) BianLian group actors use PowerShell for discovery, using PowerShell scripts to list all running processes [T1057]
- BianLian group actors → USES → Windows Command Shell
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> Windows Command Shell. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: To obtain the credentials, BianLian group actors use Windows Command Shell to find unsecured credentials on the local machine [T1552.001].
- BianLian actors → USES → Impacket
  Source review: The selected exact source passage directly attributes BianLian actors -> USES -> Impacket. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: In one case, FBI observed BianLian actors use a portable executable version of an Impacket tool (secretsdump.py) to move laterally to a domain controller and harvest credential hashes from it.

## AA23-136A:development:llama500:9538:11781

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES_TECHNIQUE → Remote Desktop Protocol
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1021.001. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian group actors use PsExec and RDP with valid accounts for lateral movement [T1021.001].
- BianLian actors → USES → Command Shell
  Source review: The selected exact source passage directly attributes BianLian actors -> USES -> Command Shell. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Prior to using RDP, BianLian actors used Command Shell and native Windows tools to add user accounts to the local Remote Desktop Users group, modified the added account’s password, and modified Windows firewall rules to allow incoming RDP traffic [T1562.004].
- BianLian group actors → USES_TECHNIQUE → Query Registry
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1012. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: FBI observed BianLian group actors using malware (system.exe) that enumerates registry values [T1012] and files [T1083] and copies clipboard data from users [T1115].

## AA23-136A:development:llama500:11500:13402

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- Rclone → USES_TECHNIQUE → Transfer Data to Cloud Account
  Source review: The source explicitly links Rclone exfiltration to T1537; retain that source mapping and its quote without inventing additional context.
  Literal support: BianLian group uses File Transfer Protocol (FTP) [T1048] and Rclone, a tool used to sync files to cloud storage, to exfiltrate data [T1537].
- BianLian group actors → USES → Rclone
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> Rclone. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: FBI observed BianLian group actors install Rclone and other files in generic and typically unchecked folders such as programdata\vmware and music folders.
- BianLian group actors → USES_TECHNIQUE → Exfiltration to Cloud Storage
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES_TECHNIQUE -> T1567.002. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: ASD’S ACSC observed BianLian group actors use Mega file-sharing service to exfiltrate victim data [T1567.002].

## AA23-136A:development:llama500:18276:20181

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES → Windows Command Shell
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> Windows Command Shell. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian group actors used Windows Command Shell to disable antivirus tools, for discovery, and to execute their tools on victim networks.

## AA23-136A:development:llama500:19858:22033

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES → Windows Command Shell
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> Windows Command Shell. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian group actors used Windows Command Shell to disable antivirus tools, for discovery, and to execute their tools on victim networks.
- BianLian group actors → USES → Net
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> net.exe. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian group actors used net.exe to add a user account to the local Remote Desktop Users group. (See Appendix: Windows PowerShell and Command Shell Activity for more information.)

## AA23-136A:development:llama500:23752:25983

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian actors → USES → Advanced Port Scanner
  Source review: The selected exact source passage directly attributes BianLian actors -> USES -> Advanced Port Scanner. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian actors used Advanced Port Scanner and SoftPerfect Network Scanner to ping computers, scan ports, and identify program versions running on ports.
- BianLian actors → USES → SoftPerfect Network Scanner
  Source review: The selected exact source passage directly attributes BianLian actors -> USES -> SoftPerfect Network Scanner. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian actors used SoftPerfect Network Scanner, which can discover shared folders.

## AA23-136A:development:llama500:25733:28112

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES → Rclone
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> Rclone. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian group actors used Rclone to exfiltrate data to a cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection.
- BianLian group actors → USES → ftp
  Source review: The selected exact source passage directly attributes BianLian group actors -> USES -> FTP. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: BianLian group actors exfiltrated data via FTP.

## AA23-319A:development:llama500:6993:9365

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

- Rhysida Actors → USES_TECHNIQUE → SSH
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1021.004. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: In one example, analysis of PowerShell console host history for a compromised user account revealed Rhysida actors leveraged PuTTy to remotely connect to systems via SSH [T1021.004].
- Rhysida Actors → USES_TECHNIQUE → NTDS
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1003.003. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors have been observed using this for NTDS dumping [T1003.003] in various instances.
- Rhysida Actors → USES_TECHNIQUE → Clear Windows Event Logs
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1070.001. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors used this tool to clear a significant number of Windows event logs, including system, application, and security logs [T1070.001].
- Rhysida Actors → USES → PsExec
  Source review: The literal PsExec.exe row is scoped by the explicit Tools Leveraged by Rhysida Actors caption.
  Literal support: PsExec.exe

## AA23-319A:development:llama500:10658:12483

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

- Rhysida → USES_TECHNIQUE → File Deletion
  Source review: The selected contiguous source span ties the Rhysida encryptor to post-encryption deletion of its binary, annotated T1070.004.
  Literal support: Rhysida’ s encryptor runs a file to encrypt and modify all targeted files to display a .rhysida extension.[4] Following encryption, a PowerShell command deletes the binary [T1070.004] from the network using a hidden command window [T1564.003].
- Rhysida → USES_TECHNIQUE → Hidden Window
  Source review: The selected contiguous span ties the Rhysida encryptor cleanup command to a hidden command window, explicitly annotated T1564.003.
  Literal support: Rhysida’ s encryptor runs a file to encrypt and modify all targeted files to display a .rhysida extension.[4] Following encryption, a PowerShell command deletes the binary [T1070.004] from the network using a hidden command window [T1564.003].
- cmd → USES_TECHNIQUE → Modify Registry
  Source review: The selected exact source passage directly attributes cmd.exe -> USES_TECHNIQUE -> T1112. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Registry modification commands [T1112] are not obfuscated, displayed as plain-text strings and executed via cmd.exe.
- Rhysida actors → USES_TECHNIQUE → Develop Capabilities
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES_TECHNIQUE -> T1587. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Additionally, third party researchers identified evidence of Rhysida actors developing custom tools with program names set to “Rhysida-0.1” [T1587].

## AA23-319A:development:llama500:19026:21144

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

- Rhysida actors → USES → AZCopy
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> AZCopy. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors leverage AZCopy, a command-line utility that users leverage to copy blobs or files to, from, or between Azure storage accounts.
- Rhysida actors → USES → ipconfig
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> ipconfig. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors used PowerShell commands (ipconfig, nltest, net) and various scripts to execute malicious actions.
- Rhysida actors → USES → Nltest
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> nltest. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors used PowerShell commands (ipconfig, nltest, net) and various scripts to execute malicious actions.
- Rhysida actors → USES → 1.ps1
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> 1.ps1. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors used batch scripting to place 1.ps1 on victim systems to automate ransomware execution.

## AA23-319A:development:llama500:20899:23542

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

- Rhysida actors → USES → cmd
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> cmd.exe. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors were observed running registry modification commands via cmd.exe.
- Rhysida actors → USES → ipconfig
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> ipconfig. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors used the ipconfig command to enumerate victim system network settings.
- Rhysida actors → USES → Net
  Source review: The selected exact source passage directly attributes Rhysida actors -> USES -> net. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Rhysida actors used the command net group “domain computers” /domain to enumerate servers on a victim domain.

## AA23-320A:development:llama500:6860:9044

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES → Tor
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> TOR. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: After exfiltrating and/or encrypting data, Scattered Spider threat actors communicate with targeted organizations via TOR, Tox, email, or encrypted applications.

## AA23-320A:development:llama500:10886:13401

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES_TECHNIQUE → Multi-Factor Authentication
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES_TECHNIQUE -> T1556.006. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003].
- Scattered Spider threat actors → USES_TECHNIQUE → Forge Web Credentials
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES_TECHNIQUE -> T1606. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003].
- Scattered Spider threat actors → USES_TECHNIQUE → Remote Access Tools
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES_TECHNIQUE -> T1219. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003].

## AA23-320A:development:llama500:13144:15560

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES_TECHNIQUE → Email Collection
  Source review: The source directly reports actor searches for emails annotated T1114. To determine if expresses the purpose of observed searching, not uncertain occurrence.
  Literal support: To determine if their activities have been detected and to maintain persistence within the compromised system, Scattered Spider threat actors often search a targeted organization’s Slack, Microsoft Teams, and Microsoft Exchange Online for emails [T1114] or conversations regarding the threat actors’ intrusion and any security response.

## AA23-320A:development:llama500:17403:19823

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES → Raccoon Stealer
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> Raccoon Stealer. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Scattered Spider threat actors use tools, such as Raccoon Stealer, to obtain login credentials.

## AA23-320A:development:llama500:19523:21935

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES → Raccoon Stealer
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> Raccoon Stealer. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Scattered Spider threat actors use tools (e.g., Raccoon Stealer) to obtain browser histories.

## AA23-320A:development:llama500:21657:23828

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES → Snowflake Data Cloud
  Source review: The selected exact source passage directly attributes Scattered Spider threat actors -> USES -> Snowflake Data Cloud. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Scattered Spider threat actors exfiltrate data using the Snowflake Data Cloud.

## AA23-353A:development:llama500:9068:11166

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

- ALPHV Blackcat/ALPHV affiliates → USES → Evilginx2
  Source review: The selected exact source passage directly attributes ALPHV Blackcat/ALPHV affiliates -> USES -> Evilginx2. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: ALPHV Blackcat/ALPHV affiliates use the open-source framework Evilginx2 to obtain MFA credentials, login credentials, and session cookies for targeted networks.

## AA24-060A:development:llama500:6217:8285

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- netsh → USES_TECHNIQUE → Disable or Modify System Firewall
  Source review: The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1562.004. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: firewall configurations using commands like netsh firewall set opmode mode=disable [T1562.004].
- Phobos actors → USES_TECHNIQUE → Native API
  Source review: The selected exact source passage directly attributes Phobos actors -> USES_TECHNIQUE -> T1106. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Additionally, Phobos actors have been observed using built-in Windows API functions [T1106] to steal tokens [T1134.001]

## AA24-060A:development:llama500:8001:10088

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos → USES_TECHNIQUE → Data Encrypted for Impact
  Source review: The source directly describes the Phobos.exe encryption capability and annotates T1486; Phobos is the ransomware identity, not an actor.
  Literal support: Phobos.exe contains functionality to encrypt all connected logical drives on the target host [T1486].
- Phobos actors → USES → vssadmin.exe
  Source review: An explicit Phobos actors subject is followed by They use vssadmin.exe to delete shadow copies, supporting the tool-use link.
  Literal support: After the exfiltration phase, Phobos actors then hunt for backups. They use vssadmin.exe and Windows Management Instrumentation command-line utility (WMIC) to discover and delete volume shadow copies in Windows environments.
- netsh → USES_TECHNIQUE → Disable or Modify System Firewall
  Source review: The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1562.004. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: netsh firewall set opmode mode=disable [T1562.004]

## AA24-060A:development:llama500:9889:11600

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- netsh → USES_TECHNIQUE → Disable or Modify System Firewall
  Source review: The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1562.004. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: netsh firewall set opmode mode=disable [T1562.004]

## AA24-060A:development:llama500:14622:16556

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos actors → USES → Windows Management Instrumentation
  Source review: The selected exact source passage directly attributes Phobos actors -> USES -> Windows Management Instrumentation. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Phobos actors used Windows Management Instrumentation command-line utility (WMIC) to prevent victims from recovering files.

## AA24-060A:development:llama500:16276:18432

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos actors → USES → Windows Management Instrumentation
  Source review: The selected exact source passage directly attributes Phobos actors -> USES -> Windows Management Instrumentation. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Phobos actors used Windows Management Instrumentation command-line utility (WMIC) to prevent victims from recovering files.
- Phobos actors → USES → Phobos
  Source review: The source explicitly attributes deployment of additional Phobos payloads to Phobos actors; actor and software identities remain separate.
  Literal support: Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.
- Phobos actors → USES → 1saas.exe
  Source review: The selected exact source passage directly attributes Phobos actors -> USES -> 1saas.exe. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.
- Phobos actors → USES → cmd
  Source review: The selected exact source passage directly attributes Phobos actors -> USES -> cmd.exe. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.

## AA24-060A:development:llama500:18199:20450

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos actors → USES → Mimikatz
  Source review: The selected exact source passage directly attributes Phobos actors -> USES -> Mimikatz. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Phobos actors used Mimikatz to export credentials.

## AA24-060A:development:llama500:20213:22160

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos threat actors → USES → Phobos.exe
  Source review: The selected exact source passage directly attributes Phobos threat actors -> USES -> Phobos.exe. No negation, uncertainty or additional condition changes this selected assertion.
  Literal support: Phobos threat actors use the Phobos.exe command to encrypt data on all logical drives connected to the network.

## Excluded candidates

- 01.4: SessionGopher use is definite, but the asserted credential-extraction purpose and its T1552.004 mapping are qualified by likely.
- 02.1: The repeated SessionGopher passage qualifies the technique purpose with likely; do not promote that purpose to a definite actor technique.
- 03.1: FTP is explicitly a file-transfer protocol here, not a named software entity; the selected Software endpoint has the wrong source role.
- 11.1: The source says the actors may be using Ngrok; this does not establish definite use.
- 13.1: The source describes a batch script likely placing 1.ps1. It does not attribute the batch-script technique to 1.ps1 itself.
- 23.1: The source qualifies the exfiltration/encryption activity with may; definite T1486 use is not established by this selected sentence.
- 25.4: Discovery and lateral-movement tactic IDs annotate the activity in this sentence; their co-occurrence does not state a general PART_OF_TACTIC taxonomy relationship.
- 26.1: ETL-tool use is scoped to instances where data exfiltration is the goal. The unconditional actor-technique triple drops that condition.
- 26.2: Centralized collection is explicitly scoped to instances where exfiltration is the goal; preserve the condition before accepting an unconditional triple.
- 26.3: The T1530 annotation is in the same conditionally scoped ETL statement; an unconditional triple would omit that scope.
- 35.2: The source attaches T1490 to Startup-folder/Run-key persistence, creating a behavior/ID mismatch. Preserve the source but exclude this mapping pending review.
- 35.4: FTP names the protocol/server endpoint here, not software implementing a technique; the generated Software endpoint is inappropriate.
- 36.2: The sentence describes instant-messaging communication but annotates T1585 (Establish Accounts). This behavior/ID mismatch needs review before import.
- 43.1: The source says actors can use Universal Virus Sniffer. Capability/possibility wording does not establish observed use in this selected passage.
- 44.1: The actor used WinSCP to reach an FTP server. Treating FTP itself as Software changes the asserted tool and source role.
