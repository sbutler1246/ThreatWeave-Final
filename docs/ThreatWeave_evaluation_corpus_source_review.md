# Seven-report held-out source review

AI-assisted source review; human verification pending. No gold triples, reference answers or QA question text were read. Every generated candidate remains available for scoring before graph filtering. Original failures and source predictions are preserved.

196 reviewed candidate occurrences: 118 Supported, 24 held for review, 54 rejected.

The review accepts definite actor/tool and actor-or-tool/technique uses with exact source support and correct endpoint roles. Conditional assertions, ambiguous identities and table-boundary attribution are held. Wrong roles, heading fragments, protocols misclassified as software and unsupported co-occurrence links are rejected. Static technique/tactic candidates are retained outside the observed-use import. No selected endpoint, prompt, source or generation setting was corrected.

## 02 AA23-165A:evaluation:llama500:4484:6401

- 0: **reject** — Non-LockBit affiliates → USES → LockBit. The selected Software LockBit is a prefix of LockBit 3.0; the clause states availability of LockBit 3.0 and does not separately establish use of generic LockBit.
  Exact support: Non-LockBit affiliates able to use LockBit 3.0 after its builder was leaked. [2, 6]
- 1: **review** — Non-LockBit affiliates → USES → LockBit 3.0. Able to use describes availability after a builder leak, not a definite observed use by the selected affiliates.
  Exact support: Non-LockBit affiliates able to use LockBit 3.0 after its builder was leaked. [2, 6]

## 05 AA23-165A:evaluation:llama500:9561:12066

- 0: **reject** — LockBit affiliates → USES → LockBit. An influx of affiliates following competition among RaaS operations does not assert that the affiliates used this Software endpoint.
  Exact support: LockBit competed with other RaaS operations, like Hive RaaS, to fill the gap in the cybercriminal market leading to an influx of LockBit affiliates.

## 06 AA23-165A:evaluation:llama500:11762:14040

- 0: **reject** — LockBit Affiliates → USES → Repurposed Use. Repurposed Use is a column heading, not a software tool used by the affiliates.
  Exact support: Repurposed Use by LockBit Affiliates

## 07 AA23-165A:evaluation:llama500:13738:15981

- 0: **reject** — LockBit Affiliates → USES → FTP. FTP is the transfer protocol in the FileZilla description, not a named Software tool. The source row names FileZilla; endpoints cannot be corrected during review.
  Exact support: Performs cross-platform File Transfer Protocol (FTP) to a site, server, or host.
- 1: **supported** — LockBit Affiliates → USES → Impacket. The exact selected source support attributes LockBit Affiliates -> USES -> Impacket, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Impacket
- 2: **supported** — LockBit Affiliates → USES → LaZagne. The exact selected source support attributes LockBit Affiliates -> USES -> LaZagne, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LaZagne

## 11 AA23-165A:evaluation:llama500:21591:23692

- 0: **review** — LockBit affiliates → USES → UACMe. The source says may use UACMe; this conditional assertion is excluded from definite graph facts.
  Exact support: LockBit affiliates may use ucmDccwCOM Method in UACMe, a GitHub collection of User Account Control (UAC) bypass techniques.

## 12 AA23-165A:evaluation:llama500:23461:25646

- 0: **review** — LockBit affiliates → USES → 123.bat. The source says affiliates may deploy 123.bat; conditional deployment is retained for review.
  Exact support: LockBit affiliates may deploy a batch script, 123.bat, to disable and uninstall antivirus software.
- 1: **review** — LockBit affiliates → USES → Microsoft Sysinternals ProDump. The source says may use ProDump; definite observed use is not asserted.
  Exact support: LockBit affiliates may use Microsoft Sysinternals ProDump to dump the contents of lsass.exe.
- 2: **reject** — LockBit affiliates → USES → lsass.exe. lsass.exe is the process whose contents are dumped, not the tool the affiliates use in this clause.
  Exact support: LockBit affiliates may use Microsoft Sysinternals ProDump to dump the contents of lsass.exe.
- 3: **supported** — LockBit affiliates → USES → Mimikatz. The exact selected source support attributes LockBit affiliates -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LockBit affiliates have used Mimikatz to dump credentials.

## 13 AA23-165A:evaluation:llama500:25345:27570

- 0: **supported** — LockBit affiliates → USES → SoftPerfect Network Scanner. The exact selected source support attributes LockBit affiliates -> USES -> SoftPerfect Network Scanner, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.
- 1: **review** — LockBit affiliates → USES → AdFind. The source says may use AdFind; the selected relation drops that uncertainty.
  Exact support: LockBit affiliates may use SoftPerfect Network Scanner, Advanced Port Scanner, and AdFind to enumerate connected machines in the network.
- 2: **review** — LockBit affiliates → USES → Cobalt Strike. The source says may use Cobalt Strike; definite observed use is not asserted.
  Exact support: LockBit affiliates may use Cobalt Strike and target SMB shares for lateral movement.

## 14 AA23-165A:evaluation:llama500:26834:28843

- 0: **supported** — LockBit affiliates → USES → StealBit. The exact selected source support attributes LockBit affiliates -> USES -> StealBit, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LockBit affiliates use StealBit, a custom exfiltration tool first used with LockBit 2.0, to steal data from a target network.
- 1: **supported** — LockBit affiliates → USES → Rclone. The exact selected source support attributes LockBit affiliates -> USES -> Rclone, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LockBit affiliates use (1) Rclone, an open-source command line cloud storage manager or FreeFileSync to exfiltrate and (2) MEGA, a publicly available file sharing service for data exfiltration.

## 15 AA23-061A:evaluation:llama500:4148:6616

- 0: **supported** — BlackSuit actors → USES_TECHNIQUE → T1566. The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1566, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: According to third-party reporting, BlackSuit actors most commonly gain initial access to victim networks via phishing emails [T1566].
- 1: **reject** — BlackSuit → USES_TECHNIQUE → T1566.001. Victims install delivery malware after phishing; the clause does not say that BlackSuit ransomware software itself performs spearphishing attachment delivery.
  Exact support: According to open source reporting, victims have unknowingly installed malware that delivers BlackSuit ransomware after receiving phishing emails containing malicious PDF documents [T1566.001] and malvertising [T1566.002].[2]
- 2: **supported** — BlackSuit actors → USES_TECHNIQUE → T1021.001. The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1021.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: The second most common vector (around 13.3% of incidents) BlackSuit actors use for initial access is RDP compromise [T1021.001].
- 3: **supported** — BlackSuit actors → USES_TECHNIQUE → T1190. The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: FBI has observed BlackSuit actors gain initial access through exploiting vulnerable public-facing applications [T1190].

## 16 AA23-061A:evaluation:llama500:6346:8622

- 0: **supported** — Royal actors → USES_TECHNIQUE → T1572. The exact selected source support attributes Royal actors -> USES_TECHNIQUE -> T1572, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572]
- 1: **supported** — Royal threat actors → USES_TECHNIQUE → T1021.001. The exact selected source support attributes Royal threat actors -> USES_TECHNIQUE -> T1021.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated August 7, 2024) Historically, Royal threat actors used RDP and legitimate operating system (OS) diagnostic tools to move laterally across a network [T1021.001].
- 2: **supported** — BlackSuit actors → USES → PsExec. The exact selected source support attributes BlackSuit actors -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally.
- 3: **supported** — BlackSuit actors → USES_TECHNIQUE → T1021.001. The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1021.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally.

## 17 AA23-061A:evaluation:llama500:8314:10530

- 0: **review** — BlackSuit actors → USES_TECHNIQUE → T1486. T1486 is attached to a preparatory Restart Manager step before encryption. The selected support does not directly describe encryption by the actor; preserve this source-mapping ambiguity.
  Exact support: Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
- 1: **supported** — BlackSuit actors → USES → vssadmin.exe. The exact selected source support attributes BlackSuit actors -> USES -> vssadmin.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
Use Windows Volume Shadow Copy service (vssadmin.exe) to delete shadow copies to inhibit system recovery.[1]

## 20 AA23-061A:evaluation:llama500:12363:13460

- 0: **reject** — Royal Operators → USES → Royal. Royal occurs inside Royal Operators in a table caption and does not denote a separately used Software endpoint.
  Exact support: Table 4: Tools Used by Royal Operators
- 1: **reject** — Royal Operators → USES → SHA256. SHA256 is the table hash column, not software used by the actor.
  Exact support: Table 4: Tools Used by Royal Operators
Tool
SHA256

## 21 AA23-061A:evaluation:llama500:13347:14347

- 0: **review** — Royal Operators → USES → Ransomware Executable. Ransomware Executable is a generic artifact description. A stable named software identity is not established by the selected row.
  Exact support: Ransomware Executable
- 1: **supported** — Royal Operators → USES → Ursnif. The exact selected source support attributes Royal Operators -> USES -> Ursnif, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Ursnif/Gozi
- 2: **supported** — Royal Operators → USES → PsExec. The exact selected source support attributes Royal Operators -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: PsExec (Microsoft Sysinternals)

## 22 AA23-061A:evaluation:llama500:14225:15219

- 0: **reject** — Royal Operators → USES → Royal. Royal occurs in Royal Operators in a table title; that title does not assert use of software Royal.
  Exact support: Table 5: Batch Script Tools Used by Royal Operators

## 23 AA23-061A:evaluation:llama500:15072:16294

- 0: **supported** — Royal Operators → USES → runanddelete.bat. The exact selected source support attributes Royal Operators -> USES -> runanddelete.bat, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: runanddelete.bat
- 1: **reject** — Royal Operators → USES → Royal. An IOC section heading names Royal and BlackSuit; it does not assert Royal Operators use software Royal.
  Exact support: Royal and BlackSuit IOCs as of June 2023 (New November 13, 2023)
- 2: **review** — Royal Operators → USES → conhost.exe. The command crosses into Table 6 while the selected actor caption is from Table 5. The following description identifies a Chisel client; keep this attribution and executable-identity ambiguity for review.
  Exact support: C:\Users\Public\conhost.exe client 149.28.73.161:443 R:149.28.73.161:43657:socks
- 3: **reject** — Royal Operators → USES → Ransomware Filepath. Ransomware Filepath is a table description, not a software name.
  Exact support: Ransomware Filepath

## 27 AA23-061A:evaluation:llama500:19628:21225

- 0: **review** — Royal and BlackSuit Ransomware → USES → nircmd.exe. The caption combines Royal and BlackSuit Ransomware into one ThreatGroup endpoint. The tool is listed, but this composite actor identity needs human review.
  Exact support: nircmd.exe
- 1: **review** — Royal and BlackSuit Ransomware → USES → nsudo.exe. The caption combines Royal and BlackSuit Ransomware into one ThreatGroup endpoint; do not treat it as one resolved actor.
  Exact support: nsudo.exe
- 2: **review** — Royal and BlackSuit Ransomware → USES → debug.ps1. The selected text says potentially debug.ps1 in a later URL table; the inherited Table 8 actor caption crosses a table boundary and does not remove that uncertainty.
  Exact support: URLs from malicious PowerShell on P0, potentially debug.ps1
- 3: **reject** — Royal and BlackSuit Ransomware → USES → ps1. ps1 is the extension inside debug.ps1, not an independently used software tool.
  Exact support: URLs from malicious PowerShell on P0, potentially debug.ps1

## 33 AA23-061A:evaluation:llama500:26384:27829

- 0: **review** — Black Suit Ransomware (1 of 3) → USES → Putty.exe. The complete row says Putty.exe was possibly used for C2; the selected shorter span drops that uncertainty. The actor identity also includes a table-part suffix.
  Exact support: Putty.exe.
- 1: **review** — Black Suit Ransomware (1 of 3) → USES → Cobalt Strike. Cobalt Strike is listed, but the selected ThreatGroup includes the table fragment (1 of 3) and inherited caption crosses into Table 14. Do not silently normalize the actor identity.
  Exact support: Cobalt Strike – Host name
- 2: **reject** — Black Suit Ransomware (1 of 3) → USES → Host. Host is part of the description Host name, not a software tool.
  Exact support: Cobalt Strike – Host name
- 3: **reject** — Black Suit Ransomware (1 of 3) → USES → C. C is the drive prefix in the AnyDesk file path, not software.
  Exact support: C:\Program Files(x86)\AnyDesk\AnyDesk.exe

## 40 AA24-131A:evaluation:llama500:4174:6733

- 0: **supported** — Black Basta affiliates → USES_TECHNIQUE → T1566. The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1566, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates primarily use spearphishing [T1566] to obtain initial access.
- 1: **supported** — Black Basta affiliates → USES_TECHNIQUE → T1190. The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Starting in February 2024, Black Basta affiliates began exploiting ConnectWise vulnerability CVE-2024-1709 [CWE-288] [T1190].
- 2: **supported** — Black Basta affiliates → USES → SoftPerfect. The exact selected source support attributes Black Basta affiliates -> USES -> SoftPerfect, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- 3: **supported** — Black Basta affiliates → USES → netscan.exe. The exact selected source support attributes Black Basta affiliates -> USES -> netscan.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.

## 41 AA24-131A:evaluation:llama500:6550:8835

- 0: **supported** — Black Basta affiliates → USES → BITSAdmin. The exact selected source support attributes Black Basta affiliates -> USES -> BITSAdmin, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- 1: **supported** — Black Basta affiliates → USES → PsExec. The exact selected source support attributes Black Basta affiliates -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- 2: **reject** — Black Basta affiliates → USES → Remote Desktop Protocol. Remote Desktop Protocol is a protocol in this clause, not a separately identified Software entity.
  Exact support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- 3: **reject** — Black Basta affiliates → USES → RDP. RDP is the protocol abbreviation, not a named Software entity.
  Exact support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.

## 42 AA24-131A:evaluation:llama500:8514:10969

- 0: **supported** — Black Basta affiliates → USES → SoftPerfect. The exact selected source support attributes Black Basta affiliates -> USES -> SoftPerfect, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- 1: **supported** — Black Basta affiliates → USES → netscan.exe. The exact selected source support attributes Black Basta affiliates -> USES -> netscan.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- 2: **supported** — Black Basta affiliates → USES → Mimikatz. The exact selected source support attributes Black Basta affiliates -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use credential scraping tools like Mimikatz for privilege escalation.
- 3: **supported** — Black Basta affiliates → USES_TECHNIQUE → T1068. The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1068, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: According to cybersecurity researchers, Black Basta affiliates have also exploited ZeroLogon (CVE-2020-1472 [CWE-330]), NoPac (CVE-2021-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]

## 43 AA24-131A:evaluation:llama500:10786:13129

- 0: **supported** — Black Basta affiliates → USES → BITSAdmin. The exact selected source support attributes Black Basta affiliates -> USES -> BITSAdmin, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- 1: **supported** — Black Basta affiliates → USES_TECHNIQUE → T1059.001. The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1059.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486].
- 2: **reject** — Black Basta Affiliates → USES → Black Basta. The table title names Black Basta Affiliates; it does not assert the use of software Black Basta.
  Exact support: Table 1: Tools Used by Black Basta Affiliates
- 3: **supported** — Black Basta affiliates → USES_TECHNIQUE → T1562.001. The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1562.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486].

## 44 AA24-131A:evaluation:llama500:12807:15323

- 0: **reject** — Black Basta affiliates → USES → ConnectWise. ConnectWise is the affected product whose vulnerability is exploited for initial access, not an attacker-operated tool in the selected relation.
  Exact support: Black Basta affiliates have exploited ConnectWise vulnerability CVE-2024-1709 to obtain initial access.
- 1: **reject** — Black Basta Affiliates → USES → Black Basta. A Black Basta ATT&CK table title and inherited actor caption do not assert use of software Black Basta.
  Exact support: Table 2: Black Basta ATT&CK Techniques for Initial Access

## 45 AA24-131A:evaluation:llama500:15045:17380

- 0: **reject** — Black Basta affiliates → USES → ConnectWise. The clause describes exploiting a ConnectWise vulnerability, not using ConnectWise as an attacker tool.
  Exact support: Black Basta affiliates have exploited ConnectWise vulnerability CVE-2024-1709 to obtain initial access.
- 1: **supported** — Black Basta affiliates → USES → Mimikatz. The exact selected source support attributes Black Basta affiliates -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.
- 2: **review** — Black Basta affiliates → USES → Zerologon. The source also identifies ZeroLogon as a vulnerability. This table labels Zerologon a tool without identifying an executable; retain the Software-type ambiguity.
  Exact support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.
- 3: **review** — Black Basta affiliates → USES → NoPac. NoPac is listed with vulnerabilities and credential tools without an executable identity. The selected Software endpoint needs source identity review.
  Exact support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.

## 46 AA24-131A:evaluation:llama500:15803:17845

- 0: **supported** — Black Basta affiliates → USES → Backstab. The exact selected source support attributes Black Basta affiliates -> USES -> Backstab, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates have deployed a tool called Backstab to disable endpoint detection and response (EDR) tooling.
- 1: **supported** — Black Basta affiliates → USES → AnyDesk. The exact selected source support attributes Black Basta affiliates -> USES -> AnyDesk, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
- 2: **supported** — Black Basta affiliates → USES → Microsoft’s Quick Assist. The exact selected source support attributes Black Basta affiliates -> USES -> Microsoft’s Quick Assist, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
- 3: **supported** — Black Basta affiliates → USES → Quick Assist. The exact selected source support attributes Black Basta affiliates -> USES -> Quick Assist, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.

## 47 AA24-109A:evaluation:llama500:4787:6854

- 0: **supported** — Akira threat actors → USES_TECHNIQUE → T1190. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: FBI and cybersecurity researchers1 observed Akira threat actors obtaining initial access to organizations through a virtual private network (VPN) service without multifactor authentication (MFA) configured,2 mostly using known Common Vulnerabilities and Exposures (CVEs) [T1190]
- 1: **supported** — Akira threat actors → USES_TECHNIQUE → T1566.001. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1566.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002]
- 2: **supported** — Akira threat actors → USES_TECHNIQUE → T1566.002. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1566.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002]
- 3: **supported** — Akira threat actors → USES → SharpDomainSpray. The exact selected source support attributes Akira threat actors -> USES -> SharpDomainSpray, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].

## 48 AA24-109A:evaluation:llama500:6537:8882

- 0: **supported** — Akira threat actors → USES_TECHNIQUE → T1110.003. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1110.003, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].
- 1: **review** — Akira threat actors → USES_TECHNIQUE → T1021.004. Indicators suggest this SSH initial-access behavior. The selected definite relation drops that source uncertainty.
  Exact support: In other incidents, indicators suggest that Akira threat actors gained initial access through the Secure Shell (SSH) protocol by exploiting a router’s IP address [T1021.004].
- 2: **supported** — Akira threat actors → USES_TECHNIQUE → T1059.005. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1059.005, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors frequently execute malicious commands by using Visual Basic (VB) scripts (event-driven programming languages that allow documents to contain macros to improve functionality through autonomous task execution) [T1059.005].
- 3: **reject** — net → USES_TECHNIQUE → T1016. T1016 is attributed to SoftPerfect/Advanced IP Scanner/NetScan. The following net commands are mapped to different techniques; net is not the subject of T1016 here.
  Exact support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

## 49 AA24-109A:evaluation:llama500:8607:10825

- 0: **reject** — net → USES_TECHNIQUE → T1016. T1016 belongs to the preceding network scanning tools. The net commands in the next sentence are mapped to T1059.003, T1018 and T1482.
  Exact support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- 1: **supported** — SoftPerfect → USES_TECHNIQUE → T1016. The exact selected source support attributes SoftPerfect -> USES_TECHNIQUE -> T1016, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- 2: **supported** — Advanced IP Scanner → USES_TECHNIQUE → T1016. The exact selected source support attributes Advanced IP Scanner -> USES_TECHNIQUE -> T1016, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- 3: **supported** — NetScan → USES_TECHNIQUE → T1016. The exact selected source support attributes NetScan -> USES_TECHNIQUE -> T1016, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

## 50 AA24-109A:evaluation:llama500:10612:12792

- 0: **supported** — Akira threat actors → USES_TECHNIQUE → T1068. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1068, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: 1003.003].11 Akira threat actors have also been observed leveraging services like Veeam.Backup.MountService.exe for privilege escalation (CVE-2024-40711) [T1068].
- 1: **supported** — AnyDesk → USES_TECHNIQUE → T1219. The exact selected source support attributes AnyDesk -> USES_TECHNIQUE -> T1219, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: To pivot laterally, Akira threat actors use legitimate remote access tools like AnyDesk or LogMeIn [T1219].
- 2: **supported** — Ngrok → USES_TECHNIQUE → T1572. The exact selected source support attributes Ngrok -> USES_TECHNIQUE -> T1572, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572]
- 3: **reject** — FileZilla → USES_TECHNIQUE → T1560.001. The clause groups FileZilla with WinRAR for collecting data, but does not establish that FileZilla performs the archive-compression technique T1560.001. Do not transfer the technique from WinRAR by co-occurrence.
  Exact support: Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048].

## 51 AA24-109A:evaluation:llama500:12528:14948

- 0: **supported** — Akira threat actors → USES → Ngrok. The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
- 1: **supported** — Akira threat actors → USES_TECHNIQUE → T1090. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1090, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
- 2: **reject** — Akira → USES_TECHNIQUE → T1090.003. The ransom note instructs the victim to contact actors through Tor; this does not establish that Akira software itself implements multi-hop proxying.
  Exact support: The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].
- 3: **reject** — Akira → USES_TECHNIQUE → T1573.002. The victim contact instructions do not establish that Akira software itself uses asymmetric encrypted-channel technique T1573.002.
  Exact support: The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].

## 52 AA24-109A:evaluation:llama500:14693:17032

- 0: **supported** — Akira → USES_TECHNIQUE → T1490. The exact selected source support attributes Akira -> USES_TECHNIQUE -> T1490, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].

## 53 AA24-109A:evaluation:llama500:16749:19037

- 0: **supported** — Akira threat actors → USES_TECHNIQUE → T1567.002. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1567.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use it maliciously to exfiltrate data to compromised cloud services [T1567.002].
- 1: **reject** — Archive → USES_TECHNIQUE → T1560.001. Archive is a generic description of an archive utility, not an identified software product.
  Exact support: Archive utility used to split compromised data into segments and to compress [T1560.001] files into .RAR format prior to exfiltration.
- 2: **supported** — Akira threat actors → USES_TECHNIQUE → T1048. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1048, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].

## 54 AA24-109A:evaluation:llama500:18804:21019

- 0: **supported** — Akira threat actors → USES_TECHNIQUE → T1048. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1048, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].
- 1: **supported** — Akira threat actors → USES_TECHNIQUE → T1027.015. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1027.015, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use an archive feature within the 7-zip tool to compress data to evade detection [T1027.015].15
- 2: **supported** — Akira threat actors → USES_TECHNIQUE → T1046. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1046, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use the tool maliciously for reconnaissance [T1046].17

## 55 AA24-109A:evaluation:llama500:20761:22564

- 0: **supported** — Akira threat actors → USES_TECHNIQUE → T1490. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1490, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: A Windows executable used by Akira threat actors to delete VSS copies [T1490].
- 1: **supported** — Akira threat actors → USES_TECHNIQUE → T1027. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1027, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: A packer-as-a-service obfuscation tool used by Akira threat actors to hinder analysis [T1027].
- 2: **supported** — Akira threat actors → USES_TECHNIQUE → T1068. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1068, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors used the malware to implement the Bring Your Own Vulnerable Driver (BYOVD) tactic [T1068].
- 3: **supported** — Akira threat actors → USES_TECHNIQUE → T1105. The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1105, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Malware that Akira threat actors used as the loader/installer for POORTRY [T1105].

## 56 AA24-109A:evaluation:llama500:22442:23336

- 0: **reject** — Akira → USES → Akira. The IOC description Akira ransomware encryptor does not identify a separate ThreatGroup that uses this software. The actor was inferred from the same malware name.
  Exact support: Akira ransomware encryptor.

## 57 AA24-109A:evaluation:llama500:23225:24336

- 0: **reject** — Akira → USES → Akira. The IOC description Akira Megazord ransomware does not establish a ThreatGroup Akira using Software Akira in this selected support.
  Exact support: Akira Megazord ransomware.

## 58 AA24-109A:evaluation:llama500:24217:25330

- 0: **reject** — akira → USES → akira. The executable filenames do not assert a ThreatGroup akira using Software akira; the shared prefix is not evidence of both endpoint roles.
  Exact support: akira.exe, win.exe

## 60 AA24-109A:evaluation:llama500:26404:27411

- 0: **supported** — nltest → USES_TECHNIQUE → T1018. The exact selected source support attributes nltest -> USES_TECHNIQUE -> T1018, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: nltest /dclist: [T1018]
- 1: **supported** — nltest → USES_TECHNIQUE → T1482. The exact selected source support attributes nltest -> USES_TECHNIQUE -> T1482, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: nltest /DOMAIN_TRUSTS [T1482]
- 2: **supported** — net → USES_TECHNIQUE → T1069.002. The exact selected source support attributes net -> USES_TECHNIQUE -> T1069.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: net group “Domain admins” /dom [T1069.002]
- 3: **supported** — net → USES_TECHNIQUE → T1069.001. The exact selected source support attributes net -> USES_TECHNIQUE -> T1069.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: net localgroup “Administrators” /dom [T1069.001]

## 62 AA24-109A:evaluation:llama500:28777:31133

- 0: **supported** — Akira threat actors → USES → Ngrok. The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: After using Ngrok to establish encrypted sessions, Akira threat actors use PowerShell and WMIC to disable services and execute malicious scripts.
- 1: **supported** — Akira threat actors → USES → Cobalt Strike. The exact selected source support attributes Akira threat actors -> USES -> Cobalt Strike, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use commercial penetration testing tools, namely Cobalt Strike, during their operations to achieve lateral movement, perform C2 procedures, and gain elevated privileges.
- 2: **supported** — Akira threat actors → USES → cmd.exe. The exact selected source support attributes Akira threat actors -> USES -> cmd.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use the Windows command shell (cmd.exe) to run batch scripts and native commands for execution, persistence, lateral movement, and to disable or manipulate security controls for evasion.
- 3: **supported** — Akira threat actors → USES → PSEXESVC.exe. The exact selected source support attributes Akira threat actors -> USES -> PSEXESVC.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use PSEXESVC.exe to enable remote code execution and deploy payloads.

## 63 AA24-109A:evaluation:llama500:30823:33030

- 0: **supported** — Akira threat actors → USES → POORTRY. The exact selected source support attributes Akira threat actors -> USES -> POORTRY, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use POORTRY malware written as a signed vulnerable Windows driver to deploy BYOVD techniques to obtain elevated privileges.

## 64 AA24-109A:evaluation:llama500:32784:35082

- 0: **supported** — Akira threat actors → USES → Mimikatz. The exact selected source support attributes Akira threat actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
- 1: **supported** — Akira threat actors → USES → SharpDomainSpray. The exact selected source support attributes Akira threat actors -> USES -> SharpDomainSpray, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use tools like SharpDomainSpray for password spraying.
- 2: **supported** — Akira threat actors → USES → LaZagne. The exact selected source support attributes Akira threat actors -> USES -> LaZagne, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use LaZagne to recover stored passwords on Windows, Linux, and macOS systems.
- 3: **supported** — Akira threat actors → USES → NetExec. The exact selected source support attributes Akira threat actors -> USES -> NetExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use NetExec with the --dpapi option to dump credentials from the Windows Credential Manager and web browsers.

## 65 AA24-109A:evaluation:llama500:34797:37085

- 0: **supported** — Akira threat actors → USES → NetExec. The exact selected source support attributes Akira threat actors -> USES -> NetExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- 1: **supported** — Akira threat actors → USES → Mimikatz. The exact selected source support attributes Akira threat actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- 2: **reject** — Akira threat actors → USES → Mimikatz with the –dpapi option. Mimikatz with the dpapi option is a tool-plus-command phrase, not a distinct Software entity. Separate valid Mimikatz use is already retained from the same output.
  Exact support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- 3: **reject** — Akira threat actors → USES → Windows Credential Manager. Windows Credential Manager is the credential store being dumped, not an attacker tool used by this clause.
  Exact support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.

## 66 AA24-109A:evaluation:llama500:36883:38919

- 0: **supported** — Akira threat actors → USES → nltest. The exact selected source support attributes Akira threat actors -> USES -> nltest, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use nltest /DOMAIN_TRUSTS commands to enumerate domain trusts.
- 1: **supported** — Akira threat actors → USES → Mimikatz. The exact selected source support attributes Akira threat actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use Mimikatz to view and save authentication credentials, such as Kerberos tickets.
- 2: **supported** — Akira threat actors → USES → Ngrok. The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
- 3: **review** — Akira threat actors → USES → Cobalt Strike. The selected clause describes downloading Cobalt Strike beacons. It does not directly state subsequent use or execution, so deployment certainty needs review.
  Exact support: Akira threat actors download tools, many of which are staged in the PerfLogs directory, and use the WebClient.DownloadString() method to download Cobalt Strike beacons.

## 67 AA24-109A:evaluation:llama500:37679:39746

- 0: **supported** — Akira threat actors → USES → WinRAR. The exact selected source support attributes Akira threat actors -> USES -> WinRAR, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use tools like WinRAR to compress files.
- 1: **supported** — Akira threat actors → USES → Ngrok. The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
- 2: **review** — Akira threat actors → USES → Cobalt Strike. Downloading Cobalt Strike beacons is stated; actual use or execution is not stated in the selected support.
  Exact support: Akira threat actors download tools, many of which are staged in the PerfLogs directory, and use the WebClient.DownloadString() method to download Cobalt Strike beacons.
- 3: **supported** — Akira threat actors → USES → WinSCP. The exact selected source support attributes Akira threat actors -> USES -> WinSCP, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Akira threat actors use file transfer tools like WinSCP to transfer data.

## 68 AA25-071A:evaluation:llama500:4851:6963

- 0: **supported** — Medusa actors → USES_TECHNIQUE → T1566. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1566, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
- 1: **supported** — Medusa actors → USES_TECHNIQUE → T1190. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
Exploitation of unpatched software vulnerabilities [T1190] through Common Vulnerabilities and Exposures (CVEs) such as:
- 2: **reject** — Medusa actors → USES → ScreenConnect. ScreenConnect is the vulnerable target of exploitation for initial access, not an actor-operated tool in the selected support.
  Exact support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
Exploitation of unpatched software vulnerabilities [T1190] through Common Vulnerabilities and Exposures (CVEs) such as:
ScreenConnect vulnerability CVE-2024-1709 [CWE-288: Authentication Bypass Using an Alternate Path or Channel].

## 70 AA25-071A:evaluation:llama500:8653:10741

- 0: **supported** — Medusa actors → USES_TECHNIQUE → T1059.001. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1059.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- 1: **supported** — Medusa actors → USES_TECHNIQUE → T1059.003. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1059.003, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- 2: **supported** — Medusa actors → USES_TECHNIQUE → T1046. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1046, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- 3: **supported** — Medusa actors → USES_TECHNIQUE → T1083. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1083, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].

## 71 AA25-071A:evaluation:llama500:10438:12511

- 0: **supported** — Medusa actors → USES → Rclone. The exact selected source support attributes Medusa actors -> USES -> Rclone, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].
- 1: **supported** — Medusa actors → USES_TECHNIQUE → T1564.012. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1564.012, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].

## 72 AA25-071A:evaluation:llama500:12220:14519

- 0: **supported** — Medusa actors → USES_TECHNIQUE → T1219. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1219, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219].
- 1: **supported** — Medusa actors → USES → AnyDesk. FBI explicitly identified Medusa actors using this remote-access software. The earlier may tailor sentence concerns choice of tools, not uncertainty about the stated FBI observation.
  Exact support: To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop.
- 2: **supported** — Medusa actors → USES → ConnectWise. FBI explicitly identified Medusa actors using this remote-access software. The earlier may tailor sentence concerns choice of tools, not uncertainty about the stated FBI observation.
  Exact support: To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop.
- 3: **reject** — PsExec → USES_TECHNIQUE → T1021.001. T1021.001 is attached to RDP, while PsExec is explicitly tagged T1569.002. The selected PsExec-to-RDP-technique relation swaps the roles.
  Exact support: Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486].

## 73 AA25-071A:evaluation:llama500:14289:16172

- 0: **review** — T1569.002 → PART_OF_TACTIC → TA0008. This output is a technique-to-tactic association inferred from a multi-action sentence, not an observed actor/software use. Keep it outside the reviewed observed-use graph import.
  Exact support: ] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486].
- 1: **reject** — T1486 → PART_OF_TACTIC → TA0010. TA0010 describes exfiltration while T1486 describes encryption. Their co-occurrence does not make T1486 part of the exfiltration tactic.
  Exact support: ] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486].
- 2: **supported** — Medusa actors → USES → PsExec. The exact selected source support attributes Medusa actors -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: When provided with valid username and password credentials, Medusa actors use PsExec to:
- 3: **review** — T1003.001 → PART_OF_TACTIC → TA0006. The sentence links credential dumping and credential access, but this is a technique-to-tactic association rather than an observed actor/software use; exclude from this import and retain for scoring.
  Exact support: (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement.

## 74 AA25-071A:evaluation:llama500:16025:18061

- 0: **supported** — Medusa actors → USES_TECHNIQUE → T1567.002. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1567.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].
- 1: **reject** — gaze.exe → USES_TECHNIQUE → T1072. gaze.exe is the encryptor deployed by PsExec/PDQ/BigFix, not the tool performing deployment technique T1072.
  Exact support: The actors use Sysinternals PsExec, PDQ Inventory/Deploy, or BigFix [T1072] to deploy the encryptor, gaze.exe, on files across the network—with the actors disabling Windows Defender and other antivirus services on specific targets.
- 2: **supported** — Medusa actors → USES_TECHNIQUE → T1484.001. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1484.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated Aug. 18, 2026) Medusa actors make changes to Active Directory Default Domain Policy settings to override Group Policy settings [T1484.001].
- 3: **supported** — Medusa actors → USES → Rclone. The exact selected source support attributes Medusa actors -> USES -> Rclone, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].

## 75 AA25-071A:evaluation:llama500:17810:20469

- 0: **reject** — gaze.exe → USES_TECHNIQUE → T1072. The deployment tooling acts on gaze.exe; the encryptor is the deployment target, not the T1072 subject.
  Exact support: , or BigFix [T1072] to deploy the encryptor, gaze.exe, on files across the network—with the actors disabling Windows Defender and other antivirus services on specific targets.
- 1: **supported** — Medusa actors → USES → PDQ Deploy. The exact selected source support attributes Medusa actors -> USES -> PDQ Deploy, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: (Updated Aug. 18, 2026) Medusa actors use a custom PDQ Deploy playbook to:
- 2: **supported** — Medusa actors → USES_TECHNIQUE → T1675. The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1675, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors also make use of an ESXi host profile [T1675] to change root passwords on Linux machines.
- 3: **supported** — gaze.exe → USES_TECHNIQUE → T1489. The exact selected source support attributes gaze.exe -> USES_TECHNIQUE -> T1489, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: The process gaze.exe terminates all services [T1489] related to backups, security, databases, communication, file sharing, and websites, and then deletes shadow copies and encrypts files with AES-256 before dropping the ransom note.

## 79 AA25-071A:evaluation:llama500:24695:26937

- 0: **supported** — Medusa actors → USES → Windows Command Prompt. The exact selected source support attributes Medusa actors -> USES -> Windows Command Prompt, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors use Windows Command Prompt for filesystem enumeration.
- 1: **supported** — Medusa actors → USES → systeminfo. The exact selected source support attributes Medusa actors -> USES -> systeminfo, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors use the command systeminfo to gather detailed system information.
- 2: **supported** — Medusa actors → USES → netstat. The exact selected source support attributes Medusa actors -> USES -> netstat, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors use the command netstat -a to gather a listing of network connections.
- 3: **supported** — Medusa actors → USES → Mimikatz. The exact selected source support attributes Medusa actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors access credential material stored in process memory or LSASS using Mimikatz.

## 80 AA25-071A:evaluation:llama500:26712:28840

- 0: **supported** — Medusa actors → USES → Mimikatz. The exact selected source support attributes Medusa actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors access credential material stored in process memory or LSASS using Mimikatz.
- 1: **supported** — Medusa actors → USES → Windows Command Prompt. The exact selected source support attributes Medusa actors -> USES -> Windows Command Prompt, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors use Windows Command Prompt, which can be used to control almost any aspect of a system, for ingress, network, and filesystem enumeration.
- 2: **supported** — Medusa actors → USES → PDQ Deploy. The exact selected source support attributes Medusa actors -> USES -> PDQ Deploy, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors use PDQ Deploy and BigFix to deploy the encryptor on files across the network.
- 3: **supported** — Medusa actors → USES → Sysinternals PsExec. The exact selected source support attributes Medusa actors -> USES -> Sysinternals PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Medusa actors use Sysinternals PsExec to deploy the encryptor on files across the network.

## 83 AA23-352A:evaluation:llama500:3851:6199

- 0: **supported** — Play → USES_TECHNIQUE → T1078. The source explicitly attributes valid-account abuse to Play. Likely modifies purchase of the credentials, not whether valid accounts were abused.
  Exact support: The Play ransomware group gains initial access to victim networks through the abuse of valid accounts, likely purchased on the dark web [T1078]
- 1: **reject** — Play → USES_TECHNIQUE → T1133. Play ransomware actors, rather than the Play Software endpoint, use external-facing services in this clause.
  Exact support: Play ransomware actors have been observed using external-facing services [T1133] such as Remote Desktop Protocol (RDP) and Virtual Private Networks (VPN) for initial access.
- 2: **reject** — Play → USES_TECHNIQUE → T1190. The clause attributes exploitation to multiple groups including brokers with ties to Play operators; it does not attribute exploitation to Play ransomware software.
  Exact support: Multiple ransomware groups, including initial access brokers with ties to Play ransomware operators, exploited CVE-2024-57727 in remote monitoring and management (RMM) tool SimpleHelp [T1190] to conduct remote code execution [T1059.001] at many U.S.-based entities following the vulnerabilities’ disclosure on 16 January 2025.
- 3: **reject** — Play → USES_TECHNIQUE → T1016. The described reconnaissance is performed by Play actors using named tools, not by the Play Software endpoint.
  Exact support: Play ransomware actors use tools like AdFind to run Active Directory queries [TA0007] and Grixba,1 an information-stealer, to enumerate network information [T1016] and scan for anti-virus software [T1518.001].

## 84 AA23-352A:evaluation:llama500:5924:7968

- 0: **reject** — Play → USES_TECHNIQUE → T1059. Play actors use WinPEAS; the clause does not say Play ransomware software itself executes technique T1059.
  Exact support: reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths.
- 1: **reject** — Play → USES_TECHNIQUE → T1560.001. Play actors use WinRAR to archive data, not Play ransomware software itself.
  Exact support: Play ransomware actors often split compromised data into segments and use tools like WinRAR to compress files [T1560.001] into .RAR format for exfiltration.
- 2: **review** — PLAY → USES_TECHNIQUE → T1486. The selected span describes encrypted files and the .PLAY extension. It does not directly identify the selected PLAY Software endpoint as the encrypting subject; no endpoint correction is made.
  Exact support: Following exfiltration, files are encrypted [T1486] with AES-RSA hybrid encryption using intermittent encryption, encrypting every other file portion of 0x100000 bytes.4 (Note: System files are skipped during the encryption process.) A .PLAY extension is added to file names once encrypted.
- 3: **reject** — PLAY → USES → PLAY. The .PLAY filename extension does not establish a distinct ThreatGroup PLAY using Software PLAY.
  Exact support: Following exfiltration, files are encrypted [T1486] with AES-RSA hybrid encryption using intermittent encryption, encrypting every other file portion of 0x100000 bytes.4 (Note: System files are skipped during the encryption process.) A .PLAY extension is added to file names once encrypted.

## 85 AA23-352A:evaluation:llama500:7618:10055

- 0: **supported** — Play actors → USES → IOBit. The exact selected source support attributes Play actors -> USES -> IOBit, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Play actors have accessed IOBit to disable antivirus software.
- 1: **reject** — Play Ransomware Actors → USES → Play. The table title names Play Ransomware Actors; it does not assert use of software Play.
  Exact support: Table 1: Tools Leveraged by Play Ransomware Actors

## 86 AA23-352A:evaluation:llama500:9760:11935

- 0: **reject** — Play → USES_TECHNIQUE → T1048. Play ransomware actors use the transfer tool; the selected Software Play endpoint is not the acting subject.
  Exact support: Play ransomware actors have used it to transfer data [T1048] from a compromised network to actor-controlled accounts.
- 1: **reject** — Play Ransomware Actors → USES → Play. A hashes-associated-with-actors table heading is not evidence of use of software Play.
  Exact support: Table 2: Hashes Associated with Play Ransomware Actors
- 2: **supported** — Play Ransomware Actors → USES → PsExec. The exact selected source support attributes Play Ransomware Actors -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: PsExec
- 3: **reject** — Play Ransomware Actors → USES → A Windows. A Windows is a sentence fragment describing PowerTool, not a software tool name.
  Exact support: A Windows utility designed to improve speed, remove bloatware, protect privacy, and eliminate data collection, among other things.

## 87 AA23-352A:evaluation:llama500:11828:12848

- 0: **reject** — Play → USES → Play. Custom Play psexesvc identifies an executable variant; it does not assert a ThreatGroup Play uses Software Play. The selected endpoint drops the actual tool name.
  Exact support: Custom Play “psexesvc”

## 88 AA23-352A:evaluation:llama500:12733:14443

- 0: **reject** — Play → USES → Play. The clause describes actors abusing credentials. It does not assert use of software Play.
  Exact support: Play ransomware actors obtain and abuse existing account credentials to gain initial access.
- 1: **supported** — Play → USES → GRIXBA. The exact selected source support attributes Play -> USES -> GRIXBA, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Play ransomware actors use tools like GRIXBA to identify network configurations and settings.

## 89 AA23-352A:evaluation:llama500:14145:16344

- 0: **supported** — Play → USES → GRIXBA. The exact selected source support attributes Play -> USES -> GRIXBA, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Play ransomware actors use tools like GRIXBA to identify network configurations and settings.
- 1: **supported** — Play → USES → GMER. The exact selected source support attributes Play -> USES -> GMER, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
- 2: **supported** — Play → USES → IOBit. The exact selected source support attributes Play -> USES -> IOBit, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
- 3: **supported** — Play → USES → PowerTool. The exact selected source support attributes Play -> USES -> PowerTool, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.

## 90 AA23-352A:evaluation:llama500:16080:17724

- 0: **reject** — Play → USES → Play. The sentence describes Play actors encrypting data; it does not assert the selected actor-to-software self-name relation.
  Exact support: Play ransomware actors encrypt data on target systems to interrupt availability to system and network resources.

## 91 AA23-352A:evaluation:llama500:17529:18539

- 0: **reject** — Play → USES → Play. The source names Grixba as the custom data-gathering tool. It does not assert use of software Play as selected.
  Exact support: Below are copies of YARA and Suricata rules related to Play’s custom data gathering tool, Grixba:

## 100 AA23-075A:evaluation:llama500:2065:4310

- 0: **supported** — LockBit 3.0 → USES_TECHNIQUE → T1480.001. The exact selected source support attributes LockBit 3.0 -> USES_TECHNIQUE -> T1480.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LockBit 3.0 affiliates failing to enter the correct password will be unable to execute the ransomware [T1480.001].

## 101 AA23-075A:evaluation:llama500:4080:6201

- 0: **reject** — LockBit 3.0 → USES_TECHNIQUE → T1133. Affiliates deploying LockBit 3.0 gain initial access through external services; the software itself is not the subject of that initial-access behavior.
  Exact support: Affiliates deploying LockBit 3.0 ransomware gain initial access to victim networks via remote desktop protocol (RDP) exploitation [T1133]
- 1: **supported** — LockBit 3.0 → USES_TECHNIQUE → T1078. The exact selected source support attributes LockBit 3.0 -> USES_TECHNIQUE -> T1078, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: LockBit 3.0 attempts to spread across a victim network by using a preconfigured list of credentials hardcoded at compilation time or a compromised local account with elevated privileges [T1078].
- 2: **review** — LockBit 3.0 → USES_TECHNIQUE → T1486. The source says attempts to encrypt and describes exclusions. Retain the attempted-action qualification instead of importing an unqualified successful behavior.
  Exact support: LockBit 3.0 attempts to encrypt [T1486] data saved to any local or remote device, but skips files associated with core system functions.
- 3: **supported** — LockBit 3.0 → USES_TECHNIQUE → T1491.001. The exact selected source support attributes LockBit 3.0 -> USES_TECHNIQUE -> T1491.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: After files are encrypted, LockBit 3.0 drops a ransom note with the new filename <Ransomware ID>.README.txt and changes the host’s wallpaper and icons to LockBit 3.0 branding [T1491.001].

## 102 AA23-075A:evaluation:llama500:5977:8086

- 0: **review** — LockBit 3.0 → USES_TECHNIQUE → T1070.004. Deletion is conditional on build options and the source says may delete itself. Keep this conditional capability outside definite observed graph facts.
  Exact support: Once completed, LockBit 3.0 may delete itself from the disk [T1070.004] as well as any Group Policy updates that were made, depending on which options were set at compilation time.
- 1: **supported** — rclone → USES_TECHNIQUE → T1567.002. The exact selected source support attributes rclone -> USES_TECHNIQUE -> T1567.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Exact support: rclone, an open-source command line cloud storage manager [T1567.002]
- 2: **reject** — LockBit 3.0 → USES_TECHNIQUE → T1567. LockBit 3.0 affiliates use web services; the Software LockBit 3.0 endpoint is not the subject in this clause.
  Exact support: LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).
- 3: **reject** — LockBit affiliates → USES → See Table. See Table is a document navigation phrase, not software.
  Exact support: See Table 2 for a list of legitimate freeware and open-source tools LockBit affiliates have repurposed for ransomware operations:

## 104 AA23-075A:evaluation:llama500:9606:11457

- 0: **reject** — LockBit 3.0 Affiliates → USES → LockBit 3.0. The selected statement concerns mutex creation by LockBit 3.0, not affiliate use of that software. The inherited freeware-tools caption no longer governs this technical-artifact section.
  Exact support: When executed, LockBit 3.0 will create the mutex, Global\<MD4 hash of machine GUID>,

