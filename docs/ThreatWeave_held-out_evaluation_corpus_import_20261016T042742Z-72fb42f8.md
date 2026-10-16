# Reviewed held-out evaluation corpus import preview

Held-out source assertions from actual model output; AI-assisted source review, human review pending.
Only Supported dispositions are selected. Uncertain/conditional review candidates are excluded.
No benchmark gold triples or QA reference answers are inputs.

Extraction run: S:\ThreatWeave\work\evaluation_corpus_extraction\20261016T041738Z-f6bd403c
Review manifest: S:\ThreatWeave\docs\ThreatWeave_evaluation_corpus_source_review.json
Review manifest SHA-256: fe08c2c9059e6fd3069512f40f31b1a75920499bb4dec4a2143d03cdcde3964a

Target records: 48 windows, 91 distinct entities, 118 assertions.
Target counts include reused records; these are not counts of newly created graph records.

## AA23-165A:evaluation:llama500:13738:15981

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

- LockBit Affiliates → USES → Impacket
  Source review: The exact selected source support attributes LockBit Affiliates -> USES -> Impacket, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Impacket
- LockBit Affiliates → USES → LaZagne
  Source review: The exact selected source support attributes LockBit Affiliates -> USES -> LaZagne, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LaZagne

## AA23-165A:evaluation:llama500:23461:25646

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

- LockBit affiliates → USES → Mimikatz
  Source review: The exact selected source support attributes LockBit affiliates -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LockBit affiliates have used Mimikatz to dump credentials.

## AA23-165A:evaluation:llama500:25345:27570

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

- LockBit affiliates → USES → SoftPerfect Network Scanner
  Source review: The exact selected source support attributes LockBit affiliates -> USES -> SoftPerfect Network Scanner, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.

## AA23-165A:evaluation:llama500:26834:28843

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

- LockBit affiliates → USES → StealBit
  Source review: The exact selected source support attributes LockBit affiliates -> USES -> StealBit, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LockBit affiliates use StealBit, a custom exfiltration tool first used with LockBit 2.0, to steal data from a target network.
- LockBit affiliates → USES → Rclone
  Source review: The exact selected source support attributes LockBit affiliates -> USES -> Rclone, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LockBit affiliates use (1) Rclone, an open-source command line cloud storage manager or FreeFileSync to exfiltrate and (2) MEGA, a publicly available file sharing service for data exfiltration.

## AA23-061A:evaluation:llama500:4148:6616

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

- BlackSuit actors → USES_TECHNIQUE → Phishing
  Source review: The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1566, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: According to third-party reporting, BlackSuit actors most commonly gain initial access to victim networks via phishing emails [T1566].
- BlackSuit actors → USES_TECHNIQUE → Remote Desktop Protocol
  Source review: The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1021.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: The second most common vector (around 13.3% of incidents) BlackSuit actors use for initial access is RDP compromise [T1021.001].
- BlackSuit actors → USES_TECHNIQUE → Exploit Public-Facing Application
  Source review: The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: FBI has observed BlackSuit actors gain initial access through exploiting vulnerable public-facing applications [T1190].

## AA23-061A:evaluation:llama500:6346:8622

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

- Royal actors → USES_TECHNIQUE → Protocol Tunneling
  Source review: The exact selected source support attributes Royal actors -> USES_TECHNIQUE -> T1572, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572]
- Royal threat actors → USES_TECHNIQUE → Remote Desktop Protocol
  Source review: The exact selected source support attributes Royal threat actors -> USES_TECHNIQUE -> T1021.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated August 7, 2024) Historically, Royal threat actors used RDP and legitimate operating system (OS) diagnostic tools to move laterally across a network [T1021.001].
- BlackSuit actors → USES → PsExec
  Source review: The exact selected source support attributes BlackSuit actors -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally.
- BlackSuit actors → USES_TECHNIQUE → Remote Desktop Protocol
  Source review: The exact selected source support attributes BlackSuit actors -> USES_TECHNIQUE -> T1021.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally.

## AA23-061A:evaluation:llama500:8314:10530

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

- BlackSuit actors → USES → vssadmin.exe
  Source review: The exact selected source support attributes BlackSuit actors -> USES -> vssadmin.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
Use Windows Volume Shadow Copy service (vssadmin.exe) to delete shadow copies to inhibit system recovery.[1]

## AA23-061A:evaluation:llama500:13347:14347

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

- Royal Operators → USES → Ursnif
  Source review: The exact selected source support attributes Royal Operators -> USES -> Ursnif, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Ursnif/Gozi
- Royal Operators → USES → PsExec
  Source review: The exact selected source support attributes Royal Operators -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: PsExec (Microsoft Sysinternals)

## AA23-061A:evaluation:llama500:15072:16294

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

- Royal Operators → USES → runanddelete.bat
  Source review: The exact selected source support attributes Royal Operators -> USES -> runanddelete.bat, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: runanddelete.bat

## AA24-131A:evaluation:llama500:4174:6733

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

- Black Basta affiliates → USES_TECHNIQUE → Phishing
  Source review: The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1566, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates primarily use spearphishing [T1566] to obtain initial access.
- Black Basta affiliates → USES_TECHNIQUE → Exploit Public-Facing Application
  Source review: The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Starting in February 2024, Black Basta affiliates began exploiting ConnectWise vulnerability CVE-2024-1709 [CWE-288] [T1190].
- Black Basta affiliates → USES → SoftPerfect
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> SoftPerfect, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- Black Basta affiliates → USES → netscan.exe
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> netscan.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.

## AA24-131A:evaluation:llama500:6550:8835

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

- Black Basta affiliates → USES → BITSAdmin
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> BITSAdmin, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- Black Basta affiliates → USES → PsExec
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.

## AA24-131A:evaluation:llama500:8514:10969

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

- Black Basta affiliates → USES → SoftPerfect
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> SoftPerfect, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- Black Basta affiliates → USES → netscan.exe
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> netscan.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- Black Basta affiliates → USES → Mimikatz
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use credential scraping tools like Mimikatz for privilege escalation.
- Black Basta affiliates → USES_TECHNIQUE → Exploitation for Privilege Escalation
  Source review: The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1068, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: According to cybersecurity researchers, Black Basta affiliates have also exploited ZeroLogon (CVE-2020-1472 [CWE-330]), NoPac (CVE-2021-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]

## AA24-131A:evaluation:llama500:10786:13129

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

- Black Basta affiliates → USES → BITSAdmin
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> BITSAdmin, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- Black Basta affiliates → USES_TECHNIQUE → PowerShell
  Source review: The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1059.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486].
- Black Basta affiliates → USES_TECHNIQUE → Disable or Modify Tools
  Source review: The exact selected source support attributes Black Basta affiliates -> USES_TECHNIQUE -> T1562.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486].

## AA24-131A:evaluation:llama500:15045:17380

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

- Black Basta affiliates → USES → Mimikatz
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.

## AA24-131A:evaluation:llama500:15803:17845

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

- Black Basta affiliates → USES → Backstab
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> Backstab, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates have deployed a tool called Backstab to disable endpoint detection and response (EDR) tooling.
- Black Basta affiliates → USES → AnyDesk
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> AnyDesk, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
- Black Basta affiliates → USES → Microsoft’s Quick Assist
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> Microsoft’s Quick Assist, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
- Black Basta affiliates → USES → Quick Assist
  Source review: The exact selected source support attributes Black Basta affiliates -> USES -> Quick Assist, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.

## AA24-109A:evaluation:llama500:4787:6854

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES_TECHNIQUE → Exploit Public-Facing Application
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: FBI and cybersecurity researchers1 observed Akira threat actors obtaining initial access to organizations through a virtual private network (VPN) service without multifactor authentication (MFA) configured,2 mostly using known Common Vulnerabilities and Exposures (CVEs) [T1190]
- Akira threat actors → USES_TECHNIQUE → Spearphishing Attachment
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1566.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002]
- Akira threat actors → USES_TECHNIQUE → Spearphishing Link
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1566.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002]
- Akira threat actors → USES → SharpDomainSpray
  Source review: The exact selected source support attributes Akira threat actors -> USES -> SharpDomainSpray, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].

## AA24-109A:evaluation:llama500:6537:8882

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES_TECHNIQUE → Password Spraying
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1110.003, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].
- Akira threat actors → USES_TECHNIQUE → Visual Basic
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1059.005, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors frequently execute malicious commands by using Visual Basic (VB) scripts (event-driven programming languages that allow documents to contain macros to improve functionality through autonomous task execution) [T1059.005].

## AA24-109A:evaluation:llama500:8607:10825

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- SoftPerfect → USES_TECHNIQUE → System Network Configuration Discovery
  Source review: The exact selected source support attributes SoftPerfect -> USES_TECHNIQUE -> T1016, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- Advanced IP Scanner → USES_TECHNIQUE → System Network Configuration Discovery
  Source review: The exact selected source support attributes Advanced IP Scanner -> USES_TECHNIQUE -> T1016, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- NetScan → USES_TECHNIQUE → System Network Configuration Discovery
  Source review: The exact selected source support attributes NetScan -> USES_TECHNIQUE -> T1016, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

## AA24-109A:evaluation:llama500:10612:12792

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES_TECHNIQUE → Exploitation for Privilege Escalation
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1068, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: 1003.003].11 Akira threat actors have also been observed leveraging services like Veeam.Backup.MountService.exe for privilege escalation (CVE-2024-40711) [T1068].
- AnyDesk → USES_TECHNIQUE → Remote Access Tools
  Source review: The exact selected source support attributes AnyDesk -> USES_TECHNIQUE -> T1219, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: To pivot laterally, Akira threat actors use legitimate remote access tools like AnyDesk or LogMeIn [T1219].
- ngrok → USES_TECHNIQUE → Protocol Tunneling
  Source review: The exact selected source support attributes Ngrok -> USES_TECHNIQUE -> T1572, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572]

## AA24-109A:evaluation:llama500:12528:14948

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → ngrok
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
- Akira threat actors → USES_TECHNIQUE → Proxy
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1090, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

## AA24-109A:evaluation:llama500:14693:17032

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira → USES_TECHNIQUE → Inhibit System Recovery
  Source review: The exact selected source support attributes Akira -> USES_TECHNIQUE -> T1490, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].

## AA24-109A:evaluation:llama500:16749:19037

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES_TECHNIQUE → Exfiltration to Cloud Storage
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1567.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use it maliciously to exfiltrate data to compromised cloud services [T1567.002].
- Akira threat actors → USES_TECHNIQUE → Exfiltration Over Alternative Protocol
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1048, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].

## AA24-109A:evaluation:llama500:18804:21019

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES_TECHNIQUE → Exfiltration Over Alternative Protocol
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1048, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].
- Akira threat actors → USES_TECHNIQUE → Compression
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1027.015, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use an archive feature within the 7-zip tool to compress data to evade detection [T1027.015].15
- Akira threat actors → USES_TECHNIQUE → Network Service Discovery
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1046, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use the tool maliciously for reconnaissance [T1046].17

## AA24-109A:evaluation:llama500:20761:22564

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES_TECHNIQUE → Inhibit System Recovery
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1490, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: A Windows executable used by Akira threat actors to delete VSS copies [T1490].
- Akira threat actors → USES_TECHNIQUE → Obfuscated Files or Information
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1027, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: A packer-as-a-service obfuscation tool used by Akira threat actors to hinder analysis [T1027].
- Akira threat actors → USES_TECHNIQUE → Exploitation for Privilege Escalation
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1068, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors used the malware to implement the Bring Your Own Vulnerable Driver (BYOVD) tactic [T1068].
- Akira threat actors → USES_TECHNIQUE → Ingress Tool Transfer
  Source review: The exact selected source support attributes Akira threat actors -> USES_TECHNIQUE -> T1105, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Malware that Akira threat actors used as the loader/installer for POORTRY [T1105].

## AA24-109A:evaluation:llama500:26404:27411

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Nltest → USES_TECHNIQUE → Remote System Discovery
  Source review: The exact selected source support attributes nltest -> USES_TECHNIQUE -> T1018, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: nltest /dclist: [T1018]
- Nltest → USES_TECHNIQUE → Domain Trust Discovery
  Source review: The exact selected source support attributes nltest -> USES_TECHNIQUE -> T1482, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: nltest /DOMAIN_TRUSTS [T1482]
- Net → USES_TECHNIQUE → Domain Groups
  Source review: The exact selected source support attributes net -> USES_TECHNIQUE -> T1069.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: net group “Domain admins” /dom [T1069.002]
- Net → USES_TECHNIQUE → Local Groups
  Source review: The exact selected source support attributes net -> USES_TECHNIQUE -> T1069.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: net localgroup “Administrators” /dom [T1069.001]

## AA24-109A:evaluation:llama500:28777:31133

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → ngrok
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: After using Ngrok to establish encrypted sessions, Akira threat actors use PowerShell and WMIC to disable services and execute malicious scripts.
- Akira threat actors → USES → Cobalt Strike
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Cobalt Strike, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use commercial penetration testing tools, namely Cobalt Strike, during their operations to achieve lateral movement, perform C2 procedures, and gain elevated privileges.
- Akira threat actors → USES → cmd
  Source review: The exact selected source support attributes Akira threat actors -> USES -> cmd.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use the Windows command shell (cmd.exe) to run batch scripts and native commands for execution, persistence, lateral movement, and to disable or manipulate security controls for evasion.
- Akira threat actors → USES → PSEXESVC.exe
  Source review: The exact selected source support attributes Akira threat actors -> USES -> PSEXESVC.exe, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use PSEXESVC.exe to enable remote code execution and deploy payloads.

## AA24-109A:evaluation:llama500:30823:33030

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → POORTRY
  Source review: The exact selected source support attributes Akira threat actors -> USES -> POORTRY, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use POORTRY malware written as a signed vulnerable Windows driver to deploy BYOVD techniques to obtain elevated privileges.

## AA24-109A:evaluation:llama500:32784:35082

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → Mimikatz
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
- Akira threat actors → USES → SharpDomainSpray
  Source review: The exact selected source support attributes Akira threat actors -> USES -> SharpDomainSpray, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use tools like SharpDomainSpray for password spraying.
- Akira threat actors → USES → LaZagne
  Source review: The exact selected source support attributes Akira threat actors -> USES -> LaZagne, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use LaZagne to recover stored passwords on Windows, Linux, and macOS systems.
- Akira threat actors → USES → NetExec
  Source review: The exact selected source support attributes Akira threat actors -> USES -> NetExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use NetExec with the --dpapi option to dump credentials from the Windows Credential Manager and web browsers.

## AA24-109A:evaluation:llama500:34797:37085

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → NetExec
  Source review: The exact selected source support attributes Akira threat actors -> USES -> NetExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- Akira threat actors → USES → Mimikatz
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.

## AA24-109A:evaluation:llama500:36883:38919

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → Nltest
  Source review: The exact selected source support attributes Akira threat actors -> USES -> nltest, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use nltest /DOMAIN_TRUSTS commands to enumerate domain trusts.
- Akira threat actors → USES → Mimikatz
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use Mimikatz to view and save authentication credentials, such as Kerberos tickets.
- Akira threat actors → USES → ngrok
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.

## AA24-109A:evaluation:llama500:37679:39746

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

- Akira threat actors → USES → WinRAR
  Source review: The exact selected source support attributes Akira threat actors -> USES -> WinRAR, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use tools like WinRAR to compress files.
- Akira threat actors → USES → ngrok
  Source review: The exact selected source support attributes Akira threat actors -> USES -> Ngrok, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
- Akira threat actors → USES → WinSCP
  Source review: The exact selected source support attributes Akira threat actors -> USES -> WinSCP, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Akira threat actors use file transfer tools like WinSCP to transfer data.

## AA25-071A:evaluation:llama500:4851:6963

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES_TECHNIQUE → Phishing
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1566, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
- Medusa actors → USES_TECHNIQUE → Exploit Public-Facing Application
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1190, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
Exploitation of unpatched software vulnerabilities [T1190] through Common Vulnerabilities and Exposures (CVEs) such as:

## AA25-071A:evaluation:llama500:8653:10741

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES_TECHNIQUE → PowerShell
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1059.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- Medusa actors → USES_TECHNIQUE → Windows Command Shell
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1059.003, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- Medusa actors → USES_TECHNIQUE → Network Service Discovery
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1046, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- Medusa actors → USES_TECHNIQUE → File and Directory Discovery
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1083, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].

## AA25-071A:evaluation:llama500:10438:12511

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES → Rclone
  Source review: The exact selected source support attributes Medusa actors -> USES -> Rclone, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].
- Medusa actors → USES_TECHNIQUE → File/Path Exclusions
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1564.012, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].

## AA25-071A:evaluation:llama500:12220:14519

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES_TECHNIQUE → Remote Access Tools
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1219, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219].
- Medusa actors → USES → AnyDesk
  Source review: FBI explicitly identified Medusa actors using this remote-access software. The earlier may tailor sentence concerns choice of tools, not uncertainty about the stated FBI observation.
  Literal support: To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop.
- Medusa actors → USES → ConnectWise
  Source review: FBI explicitly identified Medusa actors using this remote-access software. The earlier may tailor sentence concerns choice of tools, not uncertainty about the stated FBI observation.
  Literal support: To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop.

## AA25-071A:evaluation:llama500:14289:16172

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES → PsExec
  Source review: The exact selected source support attributes Medusa actors -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: When provided with valid username and password credentials, Medusa actors use PsExec to:

## AA25-071A:evaluation:llama500:16025:18061

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES_TECHNIQUE → Exfiltration to Cloud Storage
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1567.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].
- Medusa actors → USES_TECHNIQUE → Group Policy Modification
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1484.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated Aug. 18, 2026) Medusa actors make changes to Active Directory Default Domain Policy settings to override Group Policy settings [T1484.001].
- Medusa actors → USES → Rclone
  Source review: The exact selected source support attributes Medusa actors -> USES -> Rclone, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].

## AA25-071A:evaluation:llama500:17810:20469

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES → PDQ Deploy
  Source review: The exact selected source support attributes Medusa actors -> USES -> PDQ Deploy, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: (Updated Aug. 18, 2026) Medusa actors use a custom PDQ Deploy playbook to:
- Medusa actors → USES_TECHNIQUE → ESXi Administration Command
  Source review: The exact selected source support attributes Medusa actors -> USES_TECHNIQUE -> T1675, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors also make use of an ESXi host profile [T1675] to change root passwords on Linux machines.
- gaze.exe → USES_TECHNIQUE → Service Stop
  Source review: The exact selected source support attributes gaze.exe -> USES_TECHNIQUE -> T1489, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: The process gaze.exe terminates all services [T1489] related to backups, security, databases, communication, file sharing, and websites, and then deletes shadow copies and encrypts files with AES-256 before dropping the ransom note.

## AA25-071A:evaluation:llama500:24695:26937

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES → Windows Command Prompt
  Source review: The exact selected source support attributes Medusa actors -> USES -> Windows Command Prompt, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors use Windows Command Prompt for filesystem enumeration.
- Medusa actors → USES → Systeminfo
  Source review: The exact selected source support attributes Medusa actors -> USES -> systeminfo, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors use the command systeminfo to gather detailed system information.
- Medusa actors → USES → netstat
  Source review: The exact selected source support attributes Medusa actors -> USES -> netstat, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors use the command netstat -a to gather a listing of network connections.
- Medusa actors → USES → Mimikatz
  Source review: The exact selected source support attributes Medusa actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors access credential material stored in process memory or LSASS using Mimikatz.

## AA25-071A:evaluation:llama500:26712:28840

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

- Medusa actors → USES → Mimikatz
  Source review: The exact selected source support attributes Medusa actors -> USES -> Mimikatz, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors access credential material stored in process memory or LSASS using Mimikatz.
- Medusa actors → USES → Windows Command Prompt
  Source review: The exact selected source support attributes Medusa actors -> USES -> Windows Command Prompt, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors use Windows Command Prompt, which can be used to control almost any aspect of a system, for ingress, network, and filesystem enumeration.
- Medusa actors → USES → PDQ Deploy
  Source review: The exact selected source support attributes Medusa actors -> USES -> PDQ Deploy, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors use PDQ Deploy and BigFix to deploy the encryptor on files across the network.
- Medusa actors → USES → Sysinternals PsExec
  Source review: The exact selected source support attributes Medusa actors -> USES -> Sysinternals PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Medusa actors use Sysinternals PsExec to deploy the encryptor on files across the network.

## AA23-352A:evaluation:llama500:3851:6199

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

- Play → USES_TECHNIQUE → Valid Accounts
  Source review: The source explicitly attributes valid-account abuse to Play. Likely modifies purchase of the credentials, not whether valid accounts were abused.
  Literal support: The Play ransomware group gains initial access to victim networks through the abuse of valid accounts, likely purchased on the dark web [T1078]

## AA23-352A:evaluation:llama500:7618:10055

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

- Play actors → USES → IOBit
  Source review: The exact selected source support attributes Play actors -> USES -> IOBit, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Play actors have accessed IOBit to disable antivirus software.

## AA23-352A:evaluation:llama500:9760:11935

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

- Play Ransomware Actors → USES → PsExec
  Source review: The exact selected source support attributes Play Ransomware Actors -> USES -> PsExec, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: PsExec

## AA23-352A:evaluation:llama500:12733:14443

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

- Play → USES → GRIXBA
  Source review: The exact selected source support attributes Play -> USES -> GRIXBA, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Play ransomware actors use tools like GRIXBA to identify network configurations and settings.

## AA23-352A:evaluation:llama500:14145:16344

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

- Play → USES → GRIXBA
  Source review: The exact selected source support attributes Play -> USES -> GRIXBA, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Play ransomware actors use tools like GRIXBA to identify network configurations and settings.
- Play → USES → GMER
  Source review: The exact selected source support attributes Play -> USES -> GMER, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
- Play → USES → IOBit
  Source review: The exact selected source support attributes Play -> USES -> IOBit, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
- Play → USES → PowerTool
  Source review: The exact selected source support attributes Play -> USES -> PowerTool, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.

## AA23-075A:evaluation:llama500:2065:4310

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

- LockBit 3.0 → USES_TECHNIQUE → Environmental Keying
  Source review: The exact selected source support attributes LockBit 3.0 -> USES_TECHNIQUE -> T1480.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LockBit 3.0 affiliates failing to enter the correct password will be unable to execute the ransomware [T1480.001].

## AA23-075A:evaluation:llama500:4080:6201

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

- LockBit 3.0 → USES_TECHNIQUE → Valid Accounts
  Source review: The exact selected source support attributes LockBit 3.0 -> USES_TECHNIQUE -> T1078, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: LockBit 3.0 attempts to spread across a victim network by using a preconfigured list of credentials hardcoded at compilation time or a compromised local account with elevated privileges [T1078].
- LockBit 3.0 → USES_TECHNIQUE → Internal Defacement
  Source review: The exact selected source support attributes LockBit 3.0 -> USES_TECHNIQUE -> T1491.001, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: After files are encrypted, LockBit 3.0 drops a ransom note with the new filename <Ransomware ID>.README.txt and changes the host’s wallpaper and icons to LockBit 3.0 branding [T1491.001].

## AA23-075A:evaluation:llama500:5977:8086

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

- Rclone → USES_TECHNIQUE → Exfiltration to Cloud Storage
  Source review: The exact selected source support attributes rclone -> USES_TECHNIQUE -> T1567.002, with matching endpoint roles. The source assertion is definite; any observed-use caption is retained as recorded context.
  Literal support: rclone, an open-source command line cloud storage manager [T1567.002]

## Excluded candidates

- 02.1: The selected Software LockBit is a prefix of LockBit 3.0; the clause states availability of LockBit 3.0 and does not separately establish use of generic LockBit.
- 02.2: Able to use describes availability after a builder leak, not a definite observed use by the selected affiliates.
- 05.1: An influx of affiliates following competition among RaaS operations does not assert that the affiliates used this Software endpoint.
- 06.1: Repurposed Use is a column heading, not a software tool used by the affiliates.
- 07.1: FTP is the transfer protocol in the FileZilla description, not a named Software tool. The source row names FileZilla; endpoints cannot be corrected during review.
- 11.1: The source says may use UACMe; this conditional assertion is excluded from definite graph facts.
- 12.1: The source says affiliates may deploy 123.bat; conditional deployment is retained for review.
- 12.2: The source says may use ProDump; definite observed use is not asserted.
- 12.3: lsass.exe is the process whose contents are dumped, not the tool the affiliates use in this clause.
- 13.2: The source says may use AdFind; the selected relation drops that uncertainty.
- 13.3: The source says may use Cobalt Strike; definite observed use is not asserted.
- 15.2: Victims install delivery malware after phishing; the clause does not say that BlackSuit ransomware software itself performs spearphishing attachment delivery.
- 17.1: T1486 is attached to a preparatory Restart Manager step before encryption. The selected support does not directly describe encryption by the actor; preserve this source-mapping ambiguity.
- 20.1: Royal occurs inside Royal Operators in a table caption and does not denote a separately used Software endpoint.
- 20.2: SHA256 is the table hash column, not software used by the actor.
- 21.1: Ransomware Executable is a generic artifact description. A stable named software identity is not established by the selected row.
- 22.1: Royal occurs in Royal Operators in a table title; that title does not assert use of software Royal.
- 23.2: An IOC section heading names Royal and BlackSuit; it does not assert Royal Operators use software Royal.
- 23.3: The command crosses into Table 6 while the selected actor caption is from Table 5. The following description identifies a Chisel client; keep this attribution and executable-identity ambiguity for review.
- 23.4: Ransomware Filepath is a table description, not a software name.
- 27.1: The caption combines Royal and BlackSuit Ransomware into one ThreatGroup endpoint. The tool is listed, but this composite actor identity needs human review.
- 27.2: The caption combines Royal and BlackSuit Ransomware into one ThreatGroup endpoint; do not treat it as one resolved actor.
- 27.3: The selected text says potentially debug.ps1 in a later URL table; the inherited Table 8 actor caption crosses a table boundary and does not remove that uncertainty.
- 27.4: ps1 is the extension inside debug.ps1, not an independently used software tool.
- 33.1: The complete row says Putty.exe was possibly used for C2; the selected shorter span drops that uncertainty. The actor identity also includes a table-part suffix.
- 33.2: Cobalt Strike is listed, but the selected ThreatGroup includes the table fragment (1 of 3) and inherited caption crosses into Table 14. Do not silently normalize the actor identity.
- 33.3: Host is part of the description Host name, not a software tool.
- 33.4: C is the drive prefix in the AnyDesk file path, not software.
- 41.3: Remote Desktop Protocol is a protocol in this clause, not a separately identified Software entity.
- 41.4: RDP is the protocol abbreviation, not a named Software entity.
- 43.3: The table title names Black Basta Affiliates; it does not assert the use of software Black Basta.
- 44.1: ConnectWise is the affected product whose vulnerability is exploited for initial access, not an attacker-operated tool in the selected relation.
- 44.2: A Black Basta ATT&CK table title and inherited actor caption do not assert use of software Black Basta.
- 45.1: The clause describes exploiting a ConnectWise vulnerability, not using ConnectWise as an attacker tool.
- 45.3: The source also identifies ZeroLogon as a vulnerability. This table labels Zerologon a tool without identifying an executable; retain the Software-type ambiguity.
- 45.4: NoPac is listed with vulnerabilities and credential tools without an executable identity. The selected Software endpoint needs source identity review.
- 48.2: Indicators suggest this SSH initial-access behavior. The selected definite relation drops that source uncertainty.
- 48.4: T1016 is attributed to SoftPerfect/Advanced IP Scanner/NetScan. The following net commands are mapped to different techniques; net is not the subject of T1016 here.
- 49.1: T1016 belongs to the preceding network scanning tools. The net commands in the next sentence are mapped to T1059.003, T1018 and T1482.
- 50.4: The clause groups FileZilla with WinRAR for collecting data, but does not establish that FileZilla performs the archive-compression technique T1560.001. Do not transfer the technique from WinRAR by co-occurrence.
- 51.3: The ransom note instructs the victim to contact actors through Tor; this does not establish that Akira software itself implements multi-hop proxying.
- 51.4: The victim contact instructions do not establish that Akira software itself uses asymmetric encrypted-channel technique T1573.002.
- 53.2: Archive is a generic description of an archive utility, not an identified software product.
- 56.1: The IOC description Akira ransomware encryptor does not identify a separate ThreatGroup that uses this software. The actor was inferred from the same malware name.
- 57.1: The IOC description Akira Megazord ransomware does not establish a ThreatGroup Akira using Software Akira in this selected support.
- 58.1: The executable filenames do not assert a ThreatGroup akira using Software akira; the shared prefix is not evidence of both endpoint roles.
- 65.3: Mimikatz with the dpapi option is a tool-plus-command phrase, not a distinct Software entity. Separate valid Mimikatz use is already retained from the same output.
- 65.4: Windows Credential Manager is the credential store being dumped, not an attacker tool used by this clause.
- 66.4: The selected clause describes downloading Cobalt Strike beacons. It does not directly state subsequent use or execution, so deployment certainty needs review.
- 67.3: Downloading Cobalt Strike beacons is stated; actual use or execution is not stated in the selected support.
- 68.3: ScreenConnect is the vulnerable target of exploitation for initial access, not an actor-operated tool in the selected support.
- 72.4: T1021.001 is attached to RDP, while PsExec is explicitly tagged T1569.002. The selected PsExec-to-RDP-technique relation swaps the roles.
- 73.1: This output is a technique-to-tactic association inferred from a multi-action sentence, not an observed actor/software use. Keep it outside the reviewed observed-use graph import.
- 73.2: TA0010 describes exfiltration while T1486 describes encryption. Their co-occurrence does not make T1486 part of the exfiltration tactic.
- 73.4: The sentence links credential dumping and credential access, but this is a technique-to-tactic association rather than an observed actor/software use; exclude from this import and retain for scoring.
- 74.2: gaze.exe is the encryptor deployed by PsExec/PDQ/BigFix, not the tool performing deployment technique T1072.
- 75.1: The deployment tooling acts on gaze.exe; the encryptor is the deployment target, not the T1072 subject.
- 83.2: Play ransomware actors, rather than the Play Software endpoint, use external-facing services in this clause.
- 83.3: The clause attributes exploitation to multiple groups including brokers with ties to Play operators; it does not attribute exploitation to Play ransomware software.
- 83.4: The described reconnaissance is performed by Play actors using named tools, not by the Play Software endpoint.
- 84.1: Play actors use WinPEAS; the clause does not say Play ransomware software itself executes technique T1059.
- 84.2: Play actors use WinRAR to archive data, not Play ransomware software itself.
- 84.3: The selected span describes encrypted files and the .PLAY extension. It does not directly identify the selected PLAY Software endpoint as the encrypting subject; no endpoint correction is made.
- 84.4: The .PLAY filename extension does not establish a distinct ThreatGroup PLAY using Software PLAY.
- 85.2: The table title names Play Ransomware Actors; it does not assert use of software Play.
- 86.1: Play ransomware actors use the transfer tool; the selected Software Play endpoint is not the acting subject.
- 86.2: A hashes-associated-with-actors table heading is not evidence of use of software Play.
- 86.4: A Windows is a sentence fragment describing PowerTool, not a software tool name.
- 87.1: Custom Play psexesvc identifies an executable variant; it does not assert a ThreatGroup Play uses Software Play. The selected endpoint drops the actual tool name.
- 88.1: The clause describes actors abusing credentials. It does not assert use of software Play.
- 90.1: The sentence describes Play actors encrypting data; it does not assert the selected actor-to-software self-name relation.
- 91.1: The source names Grixba as the custom data-gathering tool. It does not assert use of software Play as selected.
- 101.1: Affiliates deploying LockBit 3.0 gain initial access through external services; the software itself is not the subject of that initial-access behavior.
- 101.3: The source says attempts to encrypt and describes exclusions. Retain the attempted-action qualification instead of importing an unqualified successful behavior.
- 102.1: Deletion is conditional on build options and the source says may delete itself. Keep this conditional capability outside definite observed graph facts.
- 102.3: LockBit 3.0 affiliates use web services; the Software LockBit 3.0 endpoint is not the subject in this clause.
- 102.4: See Table is a document navigation phrase, not software.
- 104.1: The selected statement concerns mutex creation by LockBit 3.0, not affiliate use of that software. The inherited freeware-tools caption no longer governs this technical-artifact section.
