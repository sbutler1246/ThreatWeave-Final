# Seven-report held-out bounded extraction evaluation corpus

Status: processed_with_errors

Bounded source-checked candidates only; all require semantic review. No graph writes or benchmark scores.
Four relations and up to three numbered evidence units per relation are diagnostic limits, not exhaustive annotation.
Names, types and source IDs are recovered from the saved source mention index. Unknown proper names are software candidates; this index is not exhaustive NER.
Graph-write rate, index build time and system resource measurements remain pending.

Prepared chunks: S:\ThreatWeave\work\evaluation_corpus_chunks\20261016T040604Z-bccf59fb
Model digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e
Configuration hash: 92bc65a2adb978f7b4d3788767000d028bd2fbb4872e5cd00212790c807fa8af

Windows: 5 selected; 1 with candidates; 0 empty; 4 failed.
Source-checked candidate relations: 4; unique document candidates: 4; repeated relations: 0; exact source-support duplicates: 0.

## AA23-165A:evaluation:llama500:13738:15981

Status: validation_failed
Case time: 6.10 seconds; attempts: 2.

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

## AA24-109A:evaluation:llama500:18804:21019

Status: validation_failed
Case time: 5.00 seconds; attempts: 2.

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

## AA24-109A:evaluation:llama500:32784:35082

Status: candidates_ready_for_review
Case time: 2.96 seconds; attempts: 1.

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


- Akira threat actors -> USES -> Mimikatz
  Literal support: Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
- Akira threat actors -> USES -> SharpDomainSpray
  Literal support: Akira threat actors use tools like SharpDomainSpray for password spraying.
- Akira threat actors -> USES -> LaZagne
  Literal support: Akira threat actors use LaZagne to recover stored passwords on Windows, Linux, and macOS systems.
- Akira threat actors -> USES -> NetExec
  Literal support: Akira threat actors use NetExec with the --dpapi option to dump credentials from the Windows Credential Manager and web browsers.

## AA23-352A:evaluation:llama500:12733:14443

Status: validation_failed
Case time: 3.62 seconds; attempts: 2.

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

## AA23-352A:evaluation:llama500:16080:17724

Status: validation_failed
Case time: 3.96 seconds; attempts: 2.

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

