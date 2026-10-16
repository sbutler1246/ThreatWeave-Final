# Five-report bounded extraction batch

Status: processed_with_errors

Bounded source-checked candidates only; all require semantic review. No graph writes or benchmark scores.
Four relations and up to three numbered evidence units per relation are diagnostic limits, not exhaustive annotation.
Names, types and source IDs are recovered from the saved source mention index. Unknown proper names are software candidates; this index is not exhaustive NER.
Graph-write rate, index build time and system resource measurements remain pending.

Prepared chunks: S:\ThreatWeave\work\corpus_pilot_chunks\20261014T065159Z-c4380457
Model digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e
Configuration hash: 232c1e52f76801b11f89c1e7acd3bb1125806e871c355d4cfcd2ffa40015677b

Windows: 44 selected; 24 with candidates; 18 empty; 2 failed.
Source-checked candidate relations: 61; unique document candidates: 54; repeated relations: 7; exact source-support duplicates: 3.

## AA23-136A:development:llama500:7570:9807

Status: candidates_ready_for_review
Case time: 13.29 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

 also use native Windows tools and Windows Command Shell to:
Query currently logged-in users [T1033].
Query the domain controller to identify:
All groups [T1069.002].
Accounts in the Domain Admins and Domain Computers groups [T1087.002].
All users in the domain.
Retrieve a list of all domain controllers and domain trusts.
Identify accessible devices on the network [T1018].
See Appendix: Windows PowerShell and Command Shell Activity for additional information, including specific commands.
(New, November 20, 2024) BianLian group actors use PowerShell for discovery, using PowerShell scripts to list all running processes [T1057], list all software installed [T1518], and list all local drives [T1082].
Credential Access
BianLian group uses valid accounts for lateral movement through the network and to pursue other follow-on activity. To obtain the credentials, BianLian group actors use Windows Command Shell to find unsecured credentials on the local machine [T1552.001]. FBI also observed BianLian harvest credentials from the Local Security Authority Subsystem Service (LSASS) memory [T1003.001], download RDP Recognizer (a tool that could be used to brute force RDP passwords or check for RDP vulnerabilities) to the victim system, and attempt to access an AD domain database (NTDS.dit) [T1003.003].
In one case, FBI observed BianLian actors use a portable executable version of an Impacket tool (secretsdump.py) to move laterally to a domain controller and harvest credential hashes from it. Note: Impacket is a Python toolkit for programmatically constructing and manipulating network protocols. Through the Command Shell, an Impacket user with credentials can run commands on a remote device using the Windows management protocols required to support an enterprise network. Threat actors can run portable executable files on victim systems using local user rights, assuming the executable is not blocked by an application allowlist or antivirus solution.
See Appendix: Windows PowerShell and Command Shell Activity for additional information.
(New, November 20, 2024) BianLian group actors use SessionGopher, likely to extract session information for remote access tools (RATs) [T1552.004].
Persistence and Lateral Movement


- BianLian group actors -> USES_TECHNIQUE -> T1057
  Literal support: (New, November 20, 2024) BianLian group actors use PowerShell for discovery, using PowerShell scripts to list all running processes [T1057]
- BianLian group actors -> USES -> Windows Command Shell
  Literal support: To obtain the credentials, BianLian group actors use Windows Command Shell to find unsecured credentials on the local machine [T1552.001].
- BianLian actors -> USES -> Impacket
  Literal support: In one case, FBI observed BianLian actors use a portable executable version of an Impacket tool (secretsdump.py) to move laterally to a domain controller and harvest credential hashes from it.
- BianLian group actors -> USES_TECHNIQUE -> T1552.004
  Literal support: (New, November 20, 2024) BianLian group actors use SessionGopher, likely to extract session information for remote access tools (RATs) [T1552.004].

## AA23-136A:development:llama500:9538:11781

Status: candidates_ready_for_review
Case time: 2.68 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

See Appendix: Windows PowerShell and Command Shell Activity for additional information.
(New, November 20, 2024) BianLian group actors use SessionGopher, likely to extract session information for remote access tools (RATs) [T1552.004].
Persistence and Lateral Movement
BianLian group actors use PsExec and RDP with valid accounts for lateral movement [T1021.001]. Prior to using RDP, BianLian actors used Command Shell and native Windows tools to add user accounts to the local Remote Desktop Users group, modified the added account’s password, and modified Windows firewall rules to allow incoming RDP traffic [T1562.004]. See Appendix: Windows PowerShell and Command Shell Activity for additional information.
In one case, FBI found a forensic artifact (exp.exe) on a compromised system that likely exploits the Netlogon vulnerability (CVE-2020-1472) and connects to a domain controller.
(New, November 20, 2024) In another instance, ASD’S ACSC found that BianLian group actors established network login type 3 connections to systems via Server Message Block (SMB) [T1021.002].
(New, November 20, 2024) BianLian group actors have created accounts and used them for lateral movement and persistence. In one confirmed compromise, BianLian actors created multiple domain admin accounts [T1136.002] for use in lateral movement to the domain controller. In the same compromise, the actors also created multiple Azure AD accounts [T1136.003] to maintain access to the victim systems.
(New, November 20, 2024) BianLian group actors also installed webshells [T1505.003] for persistence on a victim’s Exchange server.
Collection
FBI observed BianLian group actors using malware (system.exe) that enumerates registry values [T1012] and files [T1083] and copies clipboard data from users [T1115].
(New, November 20, 2024) BianLian group actors ran PowerShell scripts to compress and/or encrypt data [T1560] that is collected prior to exfiltration.
Exfiltration and Impact
BianLian group actors search for sensitive files using PowerShell scripts (See Appendix: Windows PowerShell and Command Shell Activity) and exfiltrate them for data extortion. Prior to January 2023, BianLian actors encrypted files [T1486] after exfiltration for double extortion.


- BianLian group actors -> USES_TECHNIQUE -> T1552.004
  Literal support: (New, November 20, 2024) BianLian group actors use SessionGopher, likely to extract session information for remote access tools (RATs) [T1552.004].
- BianLian group actors -> USES_TECHNIQUE -> T1021.001
  Literal support: BianLian group actors use PsExec and RDP with valid accounts for lateral movement [T1021.001].
- BianLian actors -> USES -> Command Shell
  Literal support: Prior to using RDP, BianLian actors used Command Shell and native Windows tools to add user accounts to the local Remote Desktop Users group, modified the added account’s password, and modified Windows firewall rules to allow incoming RDP traffic [T1562.004].
- BianLian group actors -> USES_TECHNIQUE -> T1012
  Literal support: FBI observed BianLian group actors using malware (system.exe) that enumerates registry values [T1012] and files [T1083] and copies clipboard data from users [T1115].

## AA23-136A:development:llama500:11500:13402

Status: candidates_ready_for_review
Case time: 2.95 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:


BianLian group actors search for sensitive files using PowerShell scripts (See Appendix: Windows PowerShell and Command Shell Activity) and exfiltrate them for data extortion. Prior to January 2023, BianLian actors encrypted files [T1486] after exfiltration for double extortion.
BianLian group uses File Transfer Protocol (FTP) [T1048] and Rclone, a tool used to sync files to cloud storage, to exfiltrate data [T1537]. FBI observed BianLian group actors install Rclone and other files in generic and typically unchecked folders such as programdata\vmware and music folders. ASD’S ACSC observed BianLian group actors use Mega file-sharing service to exfiltrate victim data [T1567.002].
(New, November 20, 2024) Prior to January 2024, BianLian used an encryptor (encryptor.exe) that modified all encrypted files to have the .bianlian extension. The encryptor created a ransom note in each affected directory. According to the ransom note, BianLian group specifically looked for, encrypted, and exfiltrated financial, client, business, technical, and personal files. (See Figure 1 for a legacy ransomware note).
Figure 1: BianLian Sample Legacy Ransom Note (Look at this instruction.txt)
Your network systems were attacked and encrypted. Contact us in order to restore your data. Don't make any changes in your file structure: touch no files, don't try to recover by yourself, that may lead to it's complete loss.
To contact us you have to download "tox" messenger: https://qtox.github[.]io/
Add user with the following ID to get your instructions:
A4B3B0845DA242A64BF17E0DB4278EDF4BF17E0DB4278EDF85855739667D3E2AE8B89D5439015F07E81D12D767FC
Alternative way: swikipedia@onionmail[.]org
Your ID: [Unique ID Assigned to Victim]
You should know that we have been downloading data from your network for a significant time before the attack: financial, client, business, post, technical and personal files.


- FTP -> USES_TECHNIQUE -> T1048
  Literal support: BianLian group uses File Transfer Protocol (FTP) [T1048] and Rclone, a tool used to sync files to cloud storage, to exfiltrate data [T1537].
- Rclone -> USES_TECHNIQUE -> T1537
  Literal support: BianLian group uses File Transfer Protocol (FTP) [T1048] and Rclone, a tool used to sync files to cloud storage, to exfiltrate data [T1537].
- BianLian group actors -> USES -> Rclone
  Literal support: FBI observed BianLian group actors install Rclone and other files in generic and typically unchecked folders such as programdata\vmware and music folders.
- BianLian group actors -> USES_TECHNIQUE -> T1567.002
  Literal support: ASD’S ACSC observed BianLian group actors use Mega file-sharing service to exfiltrate victim data [T1567.002].

## AA23-136A:development:llama500:13135:15163

Status: empty_extraction
Case time: 0.30 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

D767FC
Alternative way: swikipedia@onionmail[.]org
Your ID: [Unique ID Assigned to Victim]
You should know that we have been downloading data from your network for a significant time before the attack: financial, client, business, post, technical and personal files.
In 10 days - it will be posted at our site http://bianlianlbc5an4kgnay3opdemgcryg2 gnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad[.]onion with links send to your clients, partners, competitors and news agencies, that will lead to a negative impact on your company: potential financial, business and reputational loses.
(New, November 20, 2024) Newer ransomware notes state BianLian group has exfiltrated data and threaten to leak the exfiltrated data if the ransom is not paid. The ransom notes provide the Tox ID 88A612B3887D57A7FA3D48F5E3EDF952E4BE48E0972FC6456FBBCFF198CC8620E5609ED2D598, which directs the victim organization to a Tox chat via https[:]//github.com/qTox/qTox/ and includes an alternative contact email addresses n0torious@onionmail[.]org and xwikipedia@onionmail[.]org. See Figure 2 for a sample ransom note.
Figure 2: BianLian Sample Ransom Note (New November 20, 2024)
This report is left in <redacted> internal network.
Just by quickly reviewing your files we found confidential data. The files on your desktop are of that kind.
Leaking of folders like "Personal Data" is a disclosure of personal and medical information of people that intrusted you to keep it. If this leak will take place they will have to monitor their credit history and identity theft for next 3 years.
Folders like "Business files" discloses detailed financial information, supply chain and other business information. Company competitors would be interested to get it.
Spreading files like 'SQL' discloses all the company information exfiltrated from SQL data bases.
Files <redacted> is screenshot made while operating in your network. It's only an example of one among many others that we have made as proof of our job, and as a proof of vulnerability of your network.



## AA23-136A:development:llama500:14884:16865

Status: empty_extraction
Case time: 0.27 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

SQL' discloses all the company information exfiltrated from SQL data bases.
Files <redacted> is screenshot made while operating in your network. It's only an example of one among many others that we have made as proof of our job, and as a proof of vulnerability of your network.
File <redacted> is a screen shot made from opened email archive.
Those are just examples for you to understand your near prospect.
FAQ.
- Who are you?
- BianLian team. Financial motivation only.
Our website: http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad[.]onion (access through tor browser)
Mirror: http://bianlivemqbawcco4cx4a672k2fip3guyxudzurfqvdszafam3ofqgqd[.]onion
- What will happen next?
Path number 1:
In 3 days we will start emailing and calling your partners and employees with notes of your company's breach and announce this data leak at our website.
During this time your data will be sorted and prepared to be published.
After that your data will be uploaded, your competitors, partners, clients, authorities, lawyer and tax agenesis would be able to access it. We will start mailing and calling your clients.
Or that will not happen, If we will close this deal in time!!!
- What should i do?
Embrace it and pay us. After that your data will be erased from our systems, with proof's provided to you. Also you might request your network improvement report.
- What should i NOT do?
1. Don't do any silly things, don't treat it lightly too. We got proofs that your data was kept with a number of data security violations of data breach laws. The penalty payments would be huge if we will anonymously sent our briefs and notes about your network structure to the regulators.
2. Based on your position in the company call your management to speak. DO NOT try to speak speak instead of your superiors, based on our experience, that may lead to disaster.
- Why this happened?
- Your network and data were not secure enough. We took advantage of it.
- What else should i know:



## AA23-136A:development:llama500:16592:18416

Status: empty_extraction
Case time: 0.32 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

 in the company call your management to speak. DO NOT try to speak speak instead of your superiors, based on our experience, that may lead to disaster.
- Why this happened?
- Your network and data were not secure enough. We took advantage of it.
- What else should i know:
Our business depends on the reputation even more than many others. If we will take money and spread your information- we will have issues with payments in future. So, we will stick to our promises and reputation. That works in both ways: if we said that we will email all your staff and publicly spread all your data- we will.
Contact us using "Tox" messenger.
The contact of the user that you should add for further instructions: 88A612B3887D57A7FA3D48F5E3EDF952E4BE48E0972FC6456FBBCFF198CC8620E5609ED2D598
Link to download "Tox" messenger: https://github.com/qTox/qTox/releases/download/v1.17.6/setup-qtox-x86_64-release.exe
Alternative way: N0torious@onionmail.org
Your ID: <redacted>
Now you should contact us.
(New, November 20, 2024) BianLian group engages in additional techniques to pressure the victim into paying the ransom; for example, printing the ransom note to printers on the compromised network. Employees of victim companies have also reported receiving threatening telephone calls from individuals associated with BianLian group.
Indicators of Compromise (IOC)
See Table 1 for IOCs obtained from FBI investigations as of March 2023.
Table 1: BianLian Ransomware and Data Extortion Group IOCs
Name
SHA-256 Hash
Description
def.exe
7b15f570a23a5c5ce8ff942da60834a9d0549ea3ea9f34f900a09331325df893
Malware associated with BianLian intrusions, which is an example of a possible backdoor developed by BianLian group.
encryptor.exe
1fd07b8d1728e416f897bef4f1471126f9b18ef108eb952f4b75050da22e8e43
Example of a BianLian encryptor.
exp.exe



## AA23-136A:development:llama500:18276:20181

Status: candidates_ready_for_review
Case time: 1.07 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

 by BianLian group.
encryptor.exe
1fd07b8d1728e416f897bef4f1471126f9b18ef108eb952f4b75050da22e8e43
Example of a BianLian encryptor.
exp.exe
0c1eb11de3a533689267ba075e49d93d55308525c04d6aff0d2c54d1f52f5500
Possible NetLogon vulnerability (CVE-2020-1472) exploitation.
system.exe
40126ae71b857dd22db39611c25d3d5dd0e60316b72830e930fba9baf23973ce
Enumerates registry and files. Reads clipboard data.
MITRE ATT&CK Techniques
See Table 2 to Table 14 for all referenced threat actor tactics and techniques in this advisory.
Table 2: Resource Development
Technique Title
ID
Use
Develop Capabilities: Malware
T1587.001
BianLian group actors developed a custom backdoor used in their intrusions.
Table 3: Initial Access
Technique Title
ID
Use
External Remote Services
T1133
BianLian group actors used RDP with valid accounts as a means of gaining initial access and for lateral movement.
Phishing
T1566
BianLian group actors used phishing to obtain valid user credentials for initial access.
Valid Accounts
T1078
BianLian group actors used RDP with valid accounts as a means of gaining initial access and for lateral movement.
(New, November 20, 2024) Exploit Public-Facing Application
T1190
BianLian group actors are targeting public-facing applications of both Windows and ESXi infrastructure, possibly leveraging the ProxyShell exploit chain to gain initial access.
Table 4: Execution
Technique Title
ID
Use
Command and Scripting Interpreter: PowerShell
T1059.001
BianLian group actors used PowerShell to disable AMSI on Windows. See Appendix: Windows PowerShell and Command Shell Activity for additional information.
Command and Scripting Interpreter: Windows Command Shell
T1059.003
BianLian group actors used Windows Command Shell to disable antivirus tools, for discovery, and to execute their tools on victim networks. See Appendix: Windows PowerShell and Command Shell Activity for additional information.


- BianLian group actors -> USES -> Windows Command Shell
  Literal support: BianLian group actors used Windows Command Shell to disable antivirus tools, for discovery, and to execute their tools on victim networks.

## AA23-136A:development:llama500:19858:22033

Status: candidates_ready_for_review
Case time: 1.64 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

 for additional information.
Command and Scripting Interpreter: Windows Command Shell
T1059.003
BianLian group actors used Windows Command Shell to disable antivirus tools, for discovery, and to execute their tools on victim networks. See Appendix: Windows PowerShell and Command Shell Activity for additional information.
Scheduled Task/Job: Scheduled Task
T1053.005
BianLian group actors used a Scheduled Task run as SYSTEM (the highest privilege Windows accounts) to execute a Dynamic Link Library (DLL) file daily. See Appendix: Windows PowerShell and Command Shell Activity for additional information.
Table 5: Persistence
Technique Title
ID
Use
Account Manipulation
T1098
BianLian group actors changed the password of an account they created.
BianLian actors modified the password of an account they added to the local Remote Desktop Users group.
Create Account: Local Account
T1136.001
BianLian group actors created/activated a local administrator account.
BianLian group actors used net.exe to add a user account to the local Remote Desktop Users group. (See Appendix: Windows PowerShell and Command Shell Activity for more information.)
(New, November 20, 2024) Create Account: Domain Account
T1136.002
BianLian actors created multiple domain admin accounts that were used for lateral movement.
(New, November 20, 2024) Create Account: Cloud Account
T1136.003
BianLian actors created multiple Azure AD accounts to maintain access to the victim systems.
(New, November 20, 2024) Server Software Component: Web Shell
T1505.003
BianLian group actors installed a webshell on a victim Exchange server.
Table 6: Privilege Escalation
Technique Title
ID
Use
(New, November 20, 2024) Exploitation for Privilege Escalation
T1068
BianLian group actors exploited CVE-2022-37969, which affects Windows 10 and 11 systems.
Table 7: Defense Evasion
Technique Title
ID
Use
Modify Registry
T1112
BianLian group actors modified the registry to disable user authentication for RDP connections, allow a user to receive help from Remote Assistance, and disable tamper protection for Sophos SAVEnabled, SEDEenabled, and SAVService services, which enables them to uninstall these services.


- BianLian group actors -> USES -> Windows Command Shell
  Literal support: BianLian group actors used Windows Command Shell to disable antivirus tools, for discovery, and to execute their tools on victim networks.
- BianLian group actors -> USES -> net.exe
  Literal support: BianLian group actors used net.exe to add a user account to the local Remote Desktop Users group. (See Appendix: Windows PowerShell and Command Shell Activity for more information.)

## AA23-136A:development:llama500:21743:23976

Status: empty_extraction
Case time: 0.47 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

2
BianLian group actors modified the registry to disable user authentication for RDP connections, allow a user to receive help from Remote Assistance, and disable tamper protection for Sophos SAVEnabled, SEDEenabled, and SAVService services, which enables them to uninstall these services.
Impair Defenses: Disable or Modify Tools
T1562.001
BianLian group actors disabled Windows defender, AMSI, and Sophos SAVEnabled and SEDEenabled tamper protection services. See Appendix: Windows PowerShell and Command Shell Activity for additional information.
Impair Defenses: Disable or Modify System Firewall
T1562.004
BianLian group actors added modified firewalls to allow RDP traffic by adding new rules to the Windows firewall that allow incoming RDP traffic and enable a pre-existing Windows firewall rule group named Remote Desktop.
(New, November 20, 2024) Obfuscated Files or Information: Software Packing
T1027.002
BianLian group actors may pack executables using UPX, to conceal their code in an attempt to bypass heuristic and signature-based detection methods.
(New, November 20, 2024) Masquerading: Masquerade Task or Service
T1036.004
BianLian group actors rename binaries and scheduled tasks after legitimate Windows services or security products.
Table 8: Credential Access
Technique Title
ID
Use
OS Credential Dumping: LSASS Memory
T1003.001
BianLian group actors accessed credential material stored in the process memory of the LSASS. See Appendix: Windows PowerShell and Command Shell Activity for additional information.
OS Credential Dumping: NTDS
T1003.003
BianLian group actors attempted to access or create a copy of the Active Directory domain database in order to steal credential information and to obtain other information about domain members such as devices, users, and access rights.
Unsecured Credentials: Credentials In Files
T1552.001
BianLian group actors searched local file systems and remote file shares for files containing insecurely stored credentials.
(New, November 20, 2024) Unsecured Credentials: Private Keys
T1552.004
BianLian group actors uses SessionGopher, likely to extract session information for RATs.
Table 9: Discovery
Technique Title
ID
Use
Account Discovery: Domain Account
T1087.002



## AA23-136A:development:llama500:23752:25983

Status: candidates_ready_for_review
Case time: 1.39 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

) Unsecured Credentials: Private Keys
T1552.004
BianLian group actors uses SessionGopher, likely to extract session information for RATs.
Table 9: Discovery
Technique Title
ID
Use
Account Discovery: Domain Account
T1087.002
BianLian group actors queried the domain controller to identify accounts in the Domain Admins and Domain Computers groups. This information can help adversaries determine which domain accounts exist to aid in follow-on activity.
Domain Trust Discovery
T1482
BianLian group actors used PingCastle to enumerate the AD and map trust relationships.
BianLian group actors retrieved a list of domain trust relationships used to identify lateral movement opportunities in Windows multi-domain/forest environments.
File and Directory Discovery
T1083
BianLian group used malware (system.exe) that enumerates files.
Network Service Discovery
T1046
BianLian actors used Advanced Port Scanner and SoftPerfect Network Scanner to ping computers, scan ports, and identify program versions running on ports.
Network Share Discovery
T1135
BianLian actors used SoftPerfect Network Scanner, which can discover shared folders.
BianLian group actors used SharpShares to enumerate accessible network shares in a domain.
Permission Groups Discovery: Domain Groups
T1069.002
BianLian group actors queried the domain controller to identify groups.
Query Registry
T1012
BianLian group used malware (system.exe) that enumerates registry.
Remote System Discovery
T1018
BianLian group actors attempted to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for lateral movement.
BianLian group actors retrieved a list of domain controllers.
System Owner User Discovery
T1033
BianLian group actors queried currently logged-in users on a machine.
(New, November 20, 2024) Process Discovery
T1057
BianLian group actors run PowerShell scripts to list all running processes.
(New, November 20, 2024) Software Discovery
T1518
BianLian group actors run PowerShell scripts to list all software installed.
(New, November 20, 2024) System Information Discovery
T1082
BianLian group actors run PowerShell scripts to list all local drives.
Table 10: Lateral Movement
Technique Title
ID


- BianLian actors -> USES -> Advanced Port Scanner
  Literal support: BianLian actors used Advanced Port Scanner and SoftPerfect Network Scanner to ping computers, scan ports, and identify program versions running on ports.
- BianLian actors -> USES -> SoftPerfect Network Scanner
  Literal support: BianLian actors used SoftPerfect Network Scanner, which can discover shared folders.

## AA23-136A:development:llama500:25733:28112

Status: candidates_ready_for_review
Case time: 2.33 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Exact source window:

Lian group actors run PowerShell scripts to list all software installed.
(New, November 20, 2024) System Information Discovery
T1082
BianLian group actors run PowerShell scripts to list all local drives.
Table 10: Lateral Movement
Technique Title
ID
Use
Remote Services: Remote Desktop Protocol
T1021.001
BianLian group actors used RDP with valid accounts for lateral movement.
(New, November 20, 2024) Remote Services: SMB/Windows Admin Shares
T1021.002
BianLian group actors used SMB to establish network login connections for lateral movement.
Table 11: Collection
Technique Title
ID
Use
Clipboard Data
T1115
BianLian group actors’ malware collects data stored in the clipboard from users copying information within or between applications.
(New, November 20, 2024) Archive Collected Data
T1560
BianLian group actors run PowerShell scripts to compress and/or encrypt data that is collected prior to exfiltration.
Table 12: Command and Control
Technique Title
ID
Use
Ingress Tool Transfer
T1105
BianLian group actors transferred tools or other files from an external system into a compromised environment.
Remote Access Software
T1219
BianLian group actors used legitimate desktop support and remote access software to establish an interactive command and control channel to target systems within networks.
(New, November 20, 2024) Proxy
T1090
BianLian group actors may be using the reverse proxy tool Ngrok and/or a modified version of the open-source Rsocks utility.
(New, November 20, 2024) Proxy: External Proxy
T1090.002
BianLian group actors may have used external proxy rsocks to establish SOCKS5 network tunnels from victim networks and to mask the destination of C2 traffic.
Table 13: Exfiltration
Technique Title
ID
Use
Transfer Data to Cloud Account
T1537
BianLian group actors used Rclone to exfiltrate data to a cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection.
Exfiltration Over Alternative Protocol
T1048
BianLian group actors exfiltrated data via FTP.
Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1567.002
BianLian group actors exfiltrated data via Mega public file-sharing service.
Table 14: Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
(Updated, November 20, 2024) Prior to January 2024, BianLian group actors encrypted data on target systems.


- BianLian group actors -> USES -> Ngrok
  Literal support: BianLian group actors may be using the reverse proxy tool Ngrok and/or a modified version of the open-source Rsocks utility.
- BianLian group actors -> USES -> Rclone
  Literal support: BianLian group actors used Rclone to exfiltrate data to a cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection.
- BianLian group actors -> USES -> FTP
  Literal support: BianLian group actors exfiltrated data via FTP.

## AA23-319A:development:llama500:6993:9365

Status: candidates_ready_for_review
Case time: 3.13 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

AppData%\Local\Temp%). PowerShell ISE provides a graphical interface for editing and testing PowerShell scripts.
PsExec.exe
A tool included in the PsTools suite used to execute processes remotely. Rhysida actors heavily leveraged this tool for lateral movement and remote execution.
mstsc.exe
A native tool that establishes an RDP connection to a host.
PuTTY.exe
Rhysida actors have been observed creating Secure Shell (SSH) PuTTy connections for lateral movement. In one example, analysis of PowerShell console host history for a compromised user account revealed Rhysida actors leveraged PuTTy to remotely connect to systems via SSH [T1021.004].
PortStarter
A back door script written in Go that provides functionality for modifying firewall settings and opening ports to pre-configured command and control (C2) servers.[1]
secretsdump
A script used to extract credentials and other confidential information from a system. Rhysida actors have been observed using this for NTDS dumping [T1003.003] in various instances.
ntdsutil.exe
A standard Windows tool used to interact with the NTDS database. Rhysida actors used this tool to extract and dump the NTDS.dit database from the domain controller containing hashes for all Active Directory (AD) users.
Note: It is strongly recommended that organizations conduct domain wide password resets and double Kerberos TGT password resets if any indication is found that the NTDS.dit file was compromised.
AnyDesk
A common software that can be maliciously used by threat actors to obtain remote access and maintain persistence [T1219]. AnyDesk also supports remote file transfer.
wevtutil.exe
A standard Windows Event Utility tool used to view event logs. Rhysida actors used this tool to clear a significant number of Windows event logs, including system, application, and security logs [T1070.001].
PowerView
A PowerShell tool used to gain situational awareness of Windows domains. Review of PowerShell event logs identified Rhysida actors using this tool to conduct additional reconnaissance-based commands and harvest credentials.
AZCopy
A command-line utility that you can use to copy blobs or files to, from, or between Azure storage accounts.
StorageExplorer-windows-x64.exe
A standalone application that allows users to manage and interact with their cloud storage.
Update End
Rhysida Ransomware Characteristics
Execution


- Rhysida actors -> USES_TECHNIQUE -> T1021.004
  Literal support: In one example, analysis of PowerShell console host history for a compromised user account revealed Rhysida actors leveraged PuTTy to remotely connect to systems via SSH [T1021.004].
- Rhysida actors -> USES_TECHNIQUE -> T1003.003
  Literal support: Rhysida actors have been observed using this for NTDS dumping [T1003.003] in various instances.
- Rhysida actors -> USES_TECHNIQUE -> T1070.001
  Literal support: Rhysida actors used this tool to clear a significant number of Windows event logs, including system, application, and security logs [T1070.001].
- Rhysida Actors -> USES -> PsExec
  Literal support: PsExec.exe

## AA23-319A:development:llama500:9072:10856

Status: candidates_ready_for_review
Case time: 1.08 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

Copy
A command-line utility that you can use to copy blobs or files to, from, or between Azure storage accounts.
StorageExplorer-windows-x64.exe
A standalone application that allows users to manage and interact with their cloud storage.
Update End
Rhysida Ransomware Characteristics
Execution
In one investigation, Rhysida actors created two folders in the C:\ drive labeled in and out, which served as a staging directory (central location) for hosting malicious executables. The in folder contained file names in accordance with host names on the victim’s network, likely imported through a scanning tool. The out folder contained various files listed in Table 2 below. Rhysida actors deployed these tools and scripts to assist system and network-wide encryption.
Table 2: Malicious Executables Associated with Rhysida Infections
File Name
Hash (SHA256 & MD5)
Description
StorageExplorer-windows-x64.exe
e66fd750c8bec06fca11b6e2919a3d66bc6c0fc1
A standalone application that allows users to manage and interact with their cloud storage.
conhost.exe
6633fa85bb234a75927b23417313e51a4c155e12f71da3959e168851a600b010
A ransomware binary.
S_0.bat
1c4978cd5d750a2985da9b58db137fc74d28422f1e087fd77642faa7efe7b597
A batch script likely used to place 1.ps1 on victim systems for ransomware staging purposes [T1059.003].
1.ps1
4e34b9442f825a16d7f6557193426ae7a18899ed46d3b896f6e4357367276183
Identifies an extension block list of files to encrypt and not encrypt.
Table 3: Malicious Executables Associated with Rhysida Infections
File Name
Hash (SHA256)
Description
S_1.bat
97766464d0f2f91b82b557ac656ab82e15 cae7896b1d8c98632ca53c15cf06c4
A batch script that copies conhost.exe (the encryption binary) on an imported list of host names within the C:\Windows\Temp directory of each system.


- 1.ps1 -> USES_TECHNIQUE -> T1059.003
  Literal support: A batch script likely used to place 1.ps1 on victim systems for ransomware staging purposes [T1059.003].

## AA23-319A:development:llama500:10658:12483

Status: candidates_ready_for_review
Case time: 3.02 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

b557ac656ab82e15 cae7896b1d8c98632ca53c15cf06c4
A batch script that copies conhost.exe (the encryption binary) on an imported list of host names within the C:\Windows\Temp directory of each system.
S_2.bat
918784e25bd24192ce4e999538be96898558660659e3c624a5f27857784cd7e1
Executes conhost.exe on compromised victim systems, which encrypts and appends the extension of. Rhysida across the environment.
Rhysida ransomware uses a Windows 64-bit Portable Executable (PE) or common object file format (COFF) compiled using MinGW via the GNU Compiler Collection (GCC), which supports various programming languages such as C, C++, and Go. The cryptographic ransomware application first injects the PE into running processes on the compromised system [T1055.002]. Additionally, third party researchers identified evidence of Rhysida actors developing custom tools with program names set to “Rhysida-0.1” [T1587].
Encryption
After mapping the network, the ransomware encrypts data using a 4096-bit RSA encryption key with a ChaCha20 algorithm [T1486]. The algorithm features a 256-bit key, a 32-bit counter, and a 96-bit nonce along with a four-by-four matrix of 32-bit words in plain text. Registry modification commands [T1112] are not obfuscated, displayed as plain-text strings and executed via cmd.exe.
Rhysida’ s encryptor runs a file to encrypt and modify all targeted files to display a .rhysida extension.[4] Following encryption, a PowerShell command deletes the binary [T1070.004] from the network using a hidden command window [T1564.003]. The Rhysida encryptor allows arguments -d (select a directory) and -sr (file deletion), defined by the authors of the code as parseOptions.[5] After the lines of binary strings complete their tasks, they delete themselves through the control panel to evade detection.
Data Extortion


- Rhysida -> USES_TECHNIQUE -> T1070.004
  Literal support: Rhysida’ s encryptor runs a file to encrypt and modify all targeted files to display a .rhysida extension.[4] Following encryption, a PowerShell command deletes the binary [T1070.004] from the network using a hidden command window [T1564.003].
- Rhysida -> USES_TECHNIQUE -> T1564.003
  Literal support: Rhysida’ s encryptor runs a file to encrypt and modify all targeted files to display a .rhysida extension.[4] Following encryption, a PowerShell command deletes the binary [T1070.004] from the network using a hidden command window [T1564.003].
- cmd.exe -> USES_TECHNIQUE -> T1112
  Literal support: Registry modification commands [T1112] are not obfuscated, displayed as plain-text strings and executed via cmd.exe.
- Rhysida actors -> USES_TECHNIQUE -> T1587
  Literal support: Additionally, third party researchers identified evidence of Rhysida actors developing custom tools with program names set to “Rhysida-0.1” [T1587].

## AA23-319A:development:llama500:12199:14452

Status: empty_extraction
Case time: 0.32 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

 The Rhysida encryptor allows arguments -d (select a directory) and -sr (file deletion), defined by the authors of the code as parseOptions.[5] After the lines of binary strings complete their tasks, they delete themselves through the control panel to evade detection.
Data Extortion
Rhysida actors reportedly engage in “double extortion” [T1657]—demanding a ransom payment to decrypt victim data and threatening to publish the sensitive exfiltrated data unless the ransom is paid.[4],[6] Rhysida actors direct victims to send ransom payments in Bitcoin to cryptocurrency wallet addresses provided by the threat actors. As shown in Figure 1, Rhysida ransomware drops a ransom note named “CriticalBreachDetected” as a PDF file—the note provides each company with a unique code and instructions to contact the group via a Tor-based portal.
Figure 1: Rhysida Ransom Note
Identified in analysis and listed in open-source reporting, the contents of the ransom note are embedded as plain-text in the ransom binary, offering network defenders an opportunity to deploy string-based detection for alerting on evidence of the ransom note. Rhysida threat actors may target systems that do not use command-line operating systems. The format of the PDF ransom notes could indicate that Rhysida actors only target systems that are compatible with handling PDF documents.[7]
Indicators of Compromise
On November 10, 2023, Sophos published TTPs and IOCs identified from analysis of six separate incidents among others indicators that are listed on GitHub.[8],[9] Additional IOCs were obtained from FBI, CISA, and the MS-ISAC’s investigations and analysis.
Update April 30, 2025:
Many indicators provided in this advisory’s initial publication are now removed because they are outdated. For historic reference see AA23-319A #StopRansomware: Rhysida Ransomware.
Update End
The email addresses listed in Table 4 are associated with Rhysida actors’ operations. Rhysida actors have been observed creating Onion Mail email accounts for services or victim communication, commonly in the format: [First Name][Last Name]@onionmail[.]org.
Table 4: Email Addresses Used to Support Rhysida Operations
Email Address
rhysidaeverywhere@onionmail[.]org
rhysidaofficial@onionmail[.]org



## AA23-319A:development:llama500:14258:15684

Status: empty_extraction
Case time: 0.43 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

 the format: [First Name][Last Name]@onionmail[.]org.
Table 4: Email Addresses Used to Support Rhysida Operations
Email Address
rhysidaeverywhere@onionmail[.]org
rhysidaofficial@onionmail[.]org
Rhysida actors have been observed using the following URLs and URIs listed in Table 5 to support their operations.
Update April 30, 2025:
Table 5: URLs/URIs Used to Support Rhysida Operations
URLs/URIs
776c5589[.]schedule[.]newhomessection[.]com
hxxps[:]//oij89jiiuguygh.blob.core.windows[.]net/
776c5589[.]schedule[.]newhomessection[.]com
hxxps[:]//e57thgdfge.blob.core.windows[.]net/
Rhysida actors have also been observed using the following file paths listed in Table 6 to support their operations.
Table 6: File Paths Used to Support Rhysida Operations
File Path
C:\in
C:\out
C:\out\PSTools.zip\
Disclaimer: Organizations are encouraged to investigate the use of the files in Table 7 for related signs of compromise prior to performing remediation actions.
Table 7: Files Used to Support Rhysida Operations
File Name
Hash (SHA256 & SHA1)
1.exe
a506fd44ee7a6d16fe8929201bc7887b966d6d14
1.ps1
4e34b9442f825a16d7f6557193426ae7a18899ed46d3b896f6e4357367276183
111.exe
64eabaa3ee1084e8e8cac9e68139453b00000904
Advanced IP Scanner
b26cfde4ca74d5d5377889bba5b60b5fc72dda75
Advanced Port Scanner
3477a173e2c1005a81d042802ab0f22cc12a4d55
advanced_ip_scanner.exe
39950150074e5b22d0ef0c30ab4c72287e003908
Advanced_IP_Scanner_2.5.3850.exe



## AA23-319A:development:llama500:15559:16518

Status: empty_extraction
Case time: 0.37 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

5a81d042802ab0f22cc12a4d55
advanced_ip_scanner.exe
39950150074e5b22d0ef0c30ab4c72287e003908
Advanced_IP_Scanner_2.5.3850.exe
1556232c5b6a998a4765a8f53d48a059cd617c59
c:\s$\conhost.exe
e5d4a2e704ee880273aa4e8114fe9927b0019ff8
conhost.exe
1f76997e8a902c1cd3b1e6c68f17f694c61c5445
Gootloader
c4d5a0c3ea69b2f3af0784df143d2b6d38e7b833def9e84ae9a54b2d25a91f5a
main.dll
ae90d0819ab92e6a1bf7bfab1fa9057221bc0b3a
main.dll
d0397d33239229e955eb37842ad84defbe70398bfd953c1b9657967540415aa3
Merchandise Planning
0c829b3dccd425f090288cb9decc1bd11107e8be2323430aa2ee38e1ee01f716
StorageExplorer-windows-x64.exe
e66fd750c8bec06fca11b6e2919a3d66bc6c0fc1
Update End
Table 8: Files Used to Support Rhysida Operations
File Name
Hash (SHA256)
Eula.txt
8329bcbadc7f81539a4969ca13f0be5b8eb7652b912324a1926fc9bfb6ec005a
Sock5.sh
48f559e00c472d9ffe3965ab92c6d298f8fb3a3f0d6d203cd2069bfca4bf3a57
PsExec64.exe
edfae1a69522f87b12c6dac3225d930e4848832e3c551ee1e7d31736bf4525ef
PsExec.exe



## AA23-319A:development:llama500:16407:17306

Status: empty_extraction
Case time: 0.37 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

d203cd2069bfca4bf3a57
PsExec64.exe
edfae1a69522f87b12c6dac3225d930e4848832e3c551ee1e7d31736bf4525ef
PsExec.exe
078163d5c16f64caa5a14784323fd51451b8c831c73396b967b4e35e6879937b
PsGetsid64.exe
201d8e77ccc2575d910d47042a986480b1da28cf0033e7ee726ad9d45ccf4daa
PsGetsid.exe
a48ac157609888471bf8578fb8b2aef6b0068f7e0742fccf2e0e288b0b2cfdfb
PsInfo64.exe
de73b73eeb156f877de61f4a6975d06759292ed69f31aaf06c9811f3311e03e7
PsInfo.exe
951b1b5fd5cb13cde159cebc7c60465587e2061363d1d8847ab78b6c4fba7501
PsLoggedon64.exe
fdadb6e15c52c41a31e3c22659dd490d5b616e017d1b1aa6070008ce09ed27ea
PsLoggedon.exe
d689cb1dbd2e4c06cd15e51a6871c406c595790ddcdcd7dc8d0401c7183720ef
PsService64.exe
554f523914cdbaed8b17527170502199c185bd69a41c81102c50dbb0e5e5a78d
PsService.exe
d3a816fe5d545a80e4639b34b90d92d1039eb71ef59e6e81b3c0e043a45b751c
psfile64.exe
be922312978a53c92a49fefd2c9f9cc098767b36f0e4d2e829d24725df65bc21
psfile.exe



## AA23-319A:development:llama500:17198:18151

Status: empty_extraction
Case time: 0.37 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

81b3c0e043a45b751c
psfile64.exe
be922312978a53c92a49fefd2c9f9cc098767b36f0e4d2e829d24725df65bc21
psfile.exe
4243dc8b991f5f8b3c0f233ca2110a1e03a1d716c3f51e88faf1d59b8242d329
pskill64.exe
7ba47558c99e18c2c6449be804b5e765c48d3a70ceaa04c1e0fae67ff1d7178d
pskill.exe
5ef168f83b55d2cbd2426afc5e6fa8161270fa6a2a312831332dc472c95dfa42
pslist64.exe
d3247f03dcd7b9335344ebba76a0b92370f32f1cb0e480c734da52db2bd8df60
pslist.exe
ed05f5d462767b3986583188000143f0eb24f7d89605523a28950e72e6b9039a
psloglist64.exe
5e55b4caf47a248a10abd009617684e969dbe5c448d087ee8178262aaab68636
psloglist.exe
dcdb9bd39b6014434190a9949dedf633726fdb470e95cc47cdaa47c1964b969f
pspasswd64.exe
8d950068f46a04e77ad6637c680cccf5d703a1828fbd6bdca513268af4f2170f
pspasswd.exe
6ed5d50cf9d07db73eaa92c5405f6b1bf670028c602c605dfa7d4fcb80ef0801
psping64.exe
d1f718d219930e57794bdadf9dda61406294b0759038cef282f7544b44b92285
psping.exe
355b4a82313074999bd8fa1332b1ed00034e63bd2a0d0367e2622f35d75cf140



## AA23-319A:development:llama500:18035:19290

Status: empty_extraction
Case time: 0.36 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

dda61406294b0759038cef282f7544b44b92285
psping.exe
355b4a82313074999bd8fa1332b1ed00034e63bd2a0d0367e2622f35d75cf140
psshutdown64.exe
4226738489c2a67852d51dbf96574f33e44e509bc265b950d495da79bb457400
psshutdown.exe
13fd3ad690c73cf0ad26c6716d4e9d1581b47c22fb7518b1d3bf9cfb8f9e9123
pssuspend64.exe
4bf8fbb7db583e1aacbf36c5f740d012c8321f221066cc68107031bd8b6bc1ee
pssuspend.exe
95a922e178075fb771066db4ab1bd70c7016f794709d514ab1c7f11500f016cd
PSTools.zip
a9ca77dfe03ce15004157727bb43ba66f00ceb215362c9b3d199f000edaa8d61
Pstools.chm
2813b6c07d17d25670163e0f66453b42d2f157bf2e42007806ebc6bb9d114acc
psversion.txt
8e43d1ddbd5c129055528a93f1e3fab0ecdf73a8a7ba9713dc4c3e216d7e5db4
psexesvc.exe
This artifact is created when a user establishes a connection using psexec. It is removed after the connection is terminated, which is why there is no hash available for this executable.
Sock5.sh
48f559e00c472d9ffe3965ab92c6d298f8fb3a3f0d6d203cd2069bfca4bf3a57
MITRE ATT&CK Tactics and Techniques
See Table 9 to Table 19 for all referenced threat actor tactics and techniques in this advisory. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.



## AA23-319A:development:llama500:19026:21144

Status: candidates_ready_for_review
Case time: 2.93 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

9 to Table 19 for all referenced threat actor tactics and techniques in this advisory. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Additional notable TTPs have been published by the Check Point Incident Response Team.[10]
Table 9: Resource Development
Technique Title
ID
Use
Develop Capabilities
T1587
Rhysida actors have been observed developing resources and custom tools, particularly with program names set to “Rhysida-0.1” to gain access to victim systems.
Table 10: Initial Access
Technique Title
ID
Use
Valid Accounts
T1078
Rhysida actors are known to use valid credentials to access internal VPN access points of victims.
Update April 30, 2025:
Table 11: Execution
Technique Title
ID
Use
Command and Scripting Interpreter: Cloud API
T1059.009
Rhysida actors leverage AZCopy, a command-line utility that users leverage to copy blobs or files to, from, or between Azure storage accounts.
Command and Scripting Interpreter: PowerShell
T1059.001
Rhysida actors used PowerShell commands (ipconfig, nltest, net) and various scripts to execute malicious actions.
Command and Scripting Interpreter: Windows Command Shell
T1059.003
Rhysida actors used batch scripting to place 1.ps1 on victim systems to automate ransomware execution.
Update End
Table 12: Privilege Escalation
Technique Title
ID
Use
Process Injection: Portable Executable Injection
T1055.002
Rhysida actors injected a Windows 64-bit PE cryptographic ransomware application into running processes on compromised systems.
Table 13: Defense Evasion
Technique Title
ID
Use
Indicator Removal: Clear Windows Event Logs
T1070.001
Rhysida actors used wevtutil.exe to clear Windows event logs, including system, application, and security logs.
Indicator Removal: File Deletion
T1070.004
Rhysida actors used PowerShell commands to delete binary strings.
Hide Artifacts: Hidden Window
T1564.003
Rhysida actors have executed hidden PowerShell windows.
Table 14: Credential Access
Technique Title
ID
Use
OS Credential Dumping: NTDS


- Rhysida actors -> USES -> AZCopy
  Literal support: Rhysida actors leverage AZCopy, a command-line utility that users leverage to copy blobs or files to, from, or between Azure storage accounts.
- Rhysida actors -> USES -> ipconfig
  Literal support: Rhysida actors used PowerShell commands (ipconfig, nltest, net) and various scripts to execute malicious actions.
- Rhysida actors -> USES -> nltest
  Literal support: Rhysida actors used PowerShell commands (ipconfig, nltest, net) and various scripts to execute malicious actions.
- Rhysida actors -> USES -> 1.ps1
  Literal support: Rhysida actors used batch scripting to place 1.ps1 on victim systems to automate ransomware execution.

## AA23-319A:development:llama500:20899:23542

Status: validation_failed
Case time: 5.65 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Exact source window:

004
Rhysida actors used PowerShell commands to delete binary strings.
Hide Artifacts: Hidden Window
T1564.003
Rhysida actors have executed hidden PowerShell windows.
Table 14: Credential Access
Technique Title
ID
Use
OS Credential Dumping: NTDS
T1003.003
Rhysida actors have been observed using secretsdump to extract credentials and other confidential information from a system, then dumping NTDS credentials.
Modify Registry
T1112
Rhysida actors were observed running registry modification commands via cmd.exe.
Table 15: Discovery
Technique Title
ID
Use
System Network Configuration Discovery
T1016
Rhysida actors used the ipconfig command to enumerate victim system network settings.
Remote System Discovery
T1018
Rhysida actors used the command net group “domain computers” /domain to enumerate servers on a victim domain.
System Owner/User Discovery
T1033
Rhysida actors leveraged whoami and various net commands within PowerShell to identify logged-in users.
Permission Groups Discovery: Local Groups
T1069.001
Rhysida actors used the command net localgroup administrators to identify accounts with local administrator rights.
Permission Groups Discovery: Domain Groups
T1069.002
Rhysida actors used the command net group “domain admins” /domain to identify domain administrators.
Account Discovery: Domain Account
T1087.002
Rhysida actors used the command net user [username] /domain to identify account information.
Domain Trust Discovery
T1482
Rhysida actors used the Windows utility nltest to enumerate domain trusts.
Table 16: Lateral Movement
Technique Title
ID
Use
Remote Services: Remote Desktop Protocol
T1021.001
Rhysida actors are known to use RDP for lateral movement.
Remote Services: SSH
T1021.004
Rhysida actors used compromised user credentials to leverage PuTTy and remotely connect to victim systems via SSH.
Table 17: Collection
Technique Title
ID
Use
Remote Access Software
T1219
Rhysida actors have been observed using the AnyDesk software to obtain remote access to victim systems and maintain persistence.
Table 18: Command and Control
Technique Title
ID
Use
Remote Access Software
T1219
Rhysida actors have been observed using the AnyDesk software to obtain remote access to victim systems and maintain persistence.
Table 19: Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
Rhysida actors encrypted victim data using a 4096-bit RSA encryption key that implements a ChaCha20 algorithm.
Financial Theft
T1657
Rhysida actors reportedly engage in “double extortion”— demanding a ransom payment to decrypt victim data and threatening to publish the sensitive exfiltrated data unless the ransom is paid.


Error: Repeated selected relationship.

## AA23-320A:development:llama500:6860:9044

Status: candidates_ready_for_review
Case time: 1.75 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

, and other data.
Update July 29, 2025:
RattyRAT
Java-based remote access trojan, used for persistent, stealth access and internal reconnaissance.[4]
DragonForce Ransomware
Infiltrates networks, encrypts data, and demands ransom.
Update End
Scattered Spider threat actors historically evade detection on target networks by using living off the land (LOTL) techniques and allowlisted applications to navigate a targeted organization’s network, as well as frequently modifying their TTPs. For additional information on LOTL techniques, see the joint advisory, Identifying and Mitigating Living Off the Land Techniques.
Scattered Spider threat actors have observably exfiltrated data [TA0010] after gaining access and threatened to release it without deploying ransomware.
Update July 29, 2025:
Recently, this includes exfiltration to multiple sites including MEGA[.]NZ and U.S.-based data centers such as Amazon S3 [T1567.002].
Update End
Recent Scattered Spider TTPs
File Encryption
Update July 29, 2025:
The FBI has identified that Scattered Spider threat actors may exfiltrate data from targeted organization’s systems for extortion and then encrypt data on the system for ransom [T1486]. After exfiltrating and/or encrypting data, Scattered Spider threat actors communicate with targeted organizations via TOR, Tox, email, or encrypted applications.
Update End
Reconnaissance, Resource Development, and Initial Access
Scattered Spider intrusions historically began with broad phishing [T1566] and smishing [T1660] attempts against a target using organization-specific crafted domains, such as the domains listed in Table 3 [T1583.001].
Table 3: Domains Used by Scattered Spider Threat Actors
Domains
targetsname-sso[.]com
targetsname-servicedesk[.]com
targetsname-okta[.]com
Update July 29, 2025:
targetsname-cms[.]com
targetsname-helpdesk[.]com
oktalogin-targetcompany[.]com
The targeted organization’s name is often appended with either a -helpdesk or a type of single sign-on (SSO) solution to add credibility. While Scattered Spider threat actors have not been observed using these techniques recently, the group continuously evolves its TTPs and these methods could be reused.


- Scattered Spider threat actors -> USES_TECHNIQUE -> T1486
  Literal support: The FBI has identified that Scattered Spider threat actors may exfiltrate data from targeted organization’s systems for extortion and then encrypt data on the system for ransom [T1486].
- Scattered Spider threat actors -> USES -> TOR
  Literal support: After exfiltrating and/or encrypting data, Scattered Spider threat actors communicate with targeted organizations via TOR, Tox, email, or encrypted applications.

## AA23-320A:development:llama500:8738:11226

Status: empty_extraction
Case time: 0.50 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

The targeted organization’s name is often appended with either a -helpdesk or a type of single sign-on (SSO) solution to add credibility. While Scattered Spider threat actors have not been observed using these techniques recently, the group continuously evolves its TTPs and these methods could be reused.
Scattered Spider threat actors currently use a variety of methods to gain initial access to a targeted organization’s network. In some instances, the threat actors purchase employee or contractor credentials on illicit marketplaces such as Russia Market [T1597.002]. In other cases, the threat actors compromise third party services with access to several potential targeted organization’s networks [T1199]. It is common for the threat actors to gather the personally identifiable information (PII) of users with elevated access to their network using online open-source information.
While Scattered Spider initially began their activity relying upon broad phishing campaigns, the threat actors are now employing more targeted and multilayered spearphishing and vishing operations. Scattered Spider searches business-to-business websites to gather information and ultimately determine the individual’s role in a target organization [T1594].
After identifying usernames, passwords, PII [T1589], and conducting SIM swaps, the threat actors then use layered social engineering techniques [T1656] which frequently occur over several calls [T1598.004]. The social engineering attempts are designed to first learn what steps are needed to conduct password resets from helpdesks. Once that information is identified, the threat actors continue to conduct phone calls to employees and help desks to gather password reset specific information of a targeted employee.
Finally, the threat actors conduct spearphising calls to convince IT help desk personnel to reset passwords and/or transfer MFA tokens [T1078.002] [T1199] [T1566.004]. At which point, the threat actors perform account takeovers against the users in SSO environments. These social engineering attempts are enriched by access to personal information derived from social media [T1593.001], open-source information, commercial intelligence tools, and database leaks. Scattered Spider threat actor tactics and techniques also make it more difficult for network defenders to warn targeted organizations or to use threat hunting tools to proactively identify intrusions.
Update End
Execution, Persistence, and Privilege Escalation



## AA23-320A:development:llama500:10886:13401

Status: candidates_ready_for_review
Case time: 3.25 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

], open-source information, commercial intelligence tools, and database leaks. Scattered Spider threat actor tactics and techniques also make it more difficult for network defenders to warn targeted organizations or to use threat hunting tools to proactively identify intrusions.
Update End
Execution, Persistence, and Privilege Escalation
Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003]. Historically, the threat actors added a federated identity provider to the targeted organization’s SSO tenant and activated automatic account linking [T1484.002]. While the threat actors may still be using this tactic, it has not been identified as a current TTP.
The threat actors were then able to sign into any account by using a matching SSO account attribute. At this stage, Scattered Spider threat actors already controlled the identity provider and then could choose an arbitrary value for this account attribute. This activity allowed the threat actors to perform privilege escalation [TA0004] and continue logging in even when passwords were changed [T1078]. Threat actors achieve elevated privileges by leveraging internal communication tools to contact employees and social engineering.
Discovery, Lateral Movement, and Exfiltration
Once persistence is established on a target network, Scattered Spider threat actors often perform discovery, specifically searching for SharePoint sites [T1213.002], credential storage documentation [T1552.001], VMware vCenter infrastructure [T1018], backups, and instructions for setting up/logging into Virtual Private Networks (VPNs) [TA0007]. The threat actors enumerate the targeted organization’s Active Directory (AD) and then perform discovery and exfiltration of the targeted organization’s code repositories [T1213.003], code-signing certificates [T1552.004], and source code [T1083] [TA0010]. Threat actors activate Amazon Web Services (AWS) Systems Manager Inventory [T1538] to discover targets for lateral movement [TA0007] [TA0008], then move to both preexisting [T1021.007] and actor-created [T1578.002] Amazon Elastic Compute Cloud (EC2) instances. In instances where the ultimate goal is data exfiltration, Scattered Spider threat actors use actor-installed extract, transform, and load (ETL) tools [T1648] to bring data from multiple data sources into a centralized database [T1074] [T1530].


- Scattered Spider threat actors -> USES_TECHNIQUE -> T1556.006
  Literal support: Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003].
- Scattered Spider threat actors -> USES_TECHNIQUE -> T1606
  Literal support: Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003].
- Scattered Spider threat actors -> USES_TECHNIQUE -> T1219
  Literal support: Scattered Spider threat actors then register their own MFA tokens [T1556.006] [T1606] and deploy remote monitoring and management (RMM) tools [T1219] after compromising a user’s account to establish persistence [TA0003].
- T1538 -> PART_OF_TACTIC -> TA0007
  Literal support: Threat actors activate Amazon Web Services (AWS) Systems Manager Inventory [T1538] to discover targets for lateral movement [TA0007] [TA0008]

## AA23-320A:development:llama500:13144:15560

Status: candidates_ready_for_review
Case time: 3.16 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

 instances. In instances where the ultimate goal is data exfiltration, Scattered Spider threat actors use actor-installed extract, transform, and load (ETL) tools [T1648] to bring data from multiple data sources into a centralized database [T1074] [T1530].
Update July 29, 2025:
In many instances, Scattered Spider threat actors search for a targeted organization’s Snowflake access to exfiltrate large volumes of data in a short time, often running thousands of queries immediately [T1567]. According to trusted third parties, where more recent incidents are concerned, Scattered Spider threat actors may have deployed DragonForce ransomware onto targeted organizations’ networks—thereby encrypting VMware Elastic Sky X integrated (ESXi) servers [T1486].
Update End
To determine if their activities have been detected and to maintain persistence within the compromised system, Scattered Spider threat actors often search a targeted organization’s Slack, Microsoft Teams, and Microsoft Exchange Online for emails [T1114] or conversations regarding the threat actors’ intrusion and any security response. The threat actors frequently join incident remediation and response calls and teleconferences, likely to identify how security teams are hunting them and proactively develop new avenues of intrusion in response to a targeted organizations’ defenses.
Update July 29, 2025:
This is sometimes achieved by creating new identities in the environment [T1136] and is often upheld with fake social media profiles [T1585.001] to backstop newly created identities. Scattered Spider threat actors consistently use proxy networks [T1090] and rotate machine names to further hamper detection and response.
Update End
MITRE ATT&CK Tactics and Techniques
See Table 4 to Table 17 for all referenced threat actor tactics and techniques in this advisory. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Table 4: Reconnaissance
Technique Title
ID
Use
Gather Victim Identity Information
T1589
Scattered Spider threat actors gather usernames, passwords, and PII for targeted organizations.
Phishing for Information
T1598
Scattered Spider threat actors use phishing to obtain login credentials, gaining access to a targeted organization’s network.
Search Closed Sources: Purchase Technical Data
T1597.002


- Scattered Spider threat actors -> USES_TECHNIQUE -> T1648
  Literal support: In instances where the ultimate goal is data exfiltration, Scattered Spider threat actors use actor-installed extract, transform, and load (ETL) tools [T1648] to bring data from multiple data sources into a centralized database [T1074] [T1530].
- Scattered Spider threat actors -> USES_TECHNIQUE -> T1074
  Literal support: In instances where the ultimate goal is data exfiltration, Scattered Spider threat actors use actor-installed extract, transform, and load (ETL) tools [T1648] to bring data from multiple data sources into a centralized database [T1074] [T1530].
- Scattered Spider threat actors -> USES_TECHNIQUE -> T1530
  Literal support: In instances where the ultimate goal is data exfiltration, Scattered Spider threat actors use actor-installed extract, transform, and load (ETL) tools [T1648] to bring data from multiple data sources into a centralized database [T1074] [T1530].
- Scattered Spider threat actors -> USES_TECHNIQUE -> T1114
  Literal support: To determine if their activities have been detected and to maintain persistence within the compromised system, Scattered Spider threat actors often search a targeted organization’s Slack, Microsoft Teams, and Microsoft Exchange Online for emails [T1114] or conversations regarding the threat actors’ intrusion and any security response.

## AA23-320A:development:llama500:15252:17668

Status: empty_extraction
Case time: 0.59 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

attered Spider threat actors gather usernames, passwords, and PII for targeted organizations.
Phishing for Information
T1598
Scattered Spider threat actors use phishing to obtain login credentials, gaining access to a targeted organization’s network.
Search Closed Sources: Purchase Technical Data
T1597.002
Scattered Spider threat actors purchase credentials from illicit marketplaces.
Search Victim-Owned Websites
T1594
Scattered Spider threat actors search targeted organization-owned websites to gather information such as work roles and contact information.
Phishing for Information: Spearphishing Voice
T1598.004
Scattered Spider threat actors call targeted organizations to elicit sensitive and actionable information.
Search Open Websites/Domains: Social Media
T1593.001
Scattered Spider threat actors scour targeted organizations’ social media to gather further information about roles and interests of staff.
Table 5: Resource Development
Technique Title
ID
Use
Acquire Infrastructure: Domains
T1583.001
Scattered Spider threat actors create domains for use in phishing and smishing attempts against targeted organizations.
Establish Accounts: Social Media Accounts
T1585.001
Scattered Spider threat actors create fake social media profiles to backstop newly created user accounts in a targeted organization.
Table 6: Initial Access
Technique Title
ID
Use
Phishing
T1566
Scattered Spider threat actors use broad phishing attempts against a target to obtain information used to gain initial access.
Scattered Spider threat actors pose as helpdesk personnel to direct employees to install commercial remote access tools.
Phishing (Mobile)
T1660
Scattered Spider threat actors send SMS messages, known as smishing, when targeting an organization.
Phishing: Spearphishing Voice
T1566.004
Scattered Spider threat actors use voice communications to convince IT help desk personnel to reset passwords and/or MFA tokens.
Trusted Relationship
T1199
Scattered Spider threat actors abuse trusted relationships of contracted IT help desks to gain access to targeted organizations.
Valid Accounts: Domain Accounts
T1078.002
Scattered Spider threat actors obtain access to valid domain accounts to gain initial access to a targeted organization.
Table 7: Execution
Technique Title
ID
Use
Serverless Execution
T1648
Scattered Spider threat actors use ETL tools to collect data in cloud environments.
User Execution
T1204



## AA23-320A:development:llama500:17403:19823

Status: candidates_ready_for_review
Case time: 1.15 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

 obtain access to valid domain accounts to gain initial access to a targeted organization.
Table 7: Execution
Technique Title
ID
Use
Serverless Execution
T1648
Scattered Spider threat actors use ETL tools to collect data in cloud environments.
User Execution
T1204
Scattered Spider threat actors impersonating helpdesk personnel direct employees to run commercial remote access tools thereby enabling access to the targeted organization’s network.
Table 8: Persistence
Technique Title
ID
Use
Persistence
TA0003
Scattered Spider threat actors seek to maintain persistence on a targeted organization’s network.
Create Account
T1136
Scattered Spider threat actors create new user identities in the targeted organization.
Modify Authentication Process: Multi-Factor Authentication
T1556.006
Scattered Spider threat actors may modify MFA tokens to gain access to a targeted organization’s network.
Valid Accounts
T1078
Scattered Spider threat actors abuse and control valid accounts to maintain network access even when passwords are changed.
Table 9: Privilege Escalation
Technique Title
ID
Use
Privilege Escalation
TA0004
Scattered Spider threat actors escalate account privileges when on a targeted organization’s network.
Domain Policy Modification: Domain Trust Modification
T1484.002
Scattered Spider threat actors add a federated identity provider to the targeted organization’s SSO tenant and activate automatic account linking.
Table 10: Defense Evasion
Technique Title
ID
Use
Modify Cloud Compute Infrastructure: Create Cloud Instance
T1578.002
Scattered Spider threat actors create cloud instances for use during lateral movement and data collection.
Impersonation
T1656
Scattered Spider threat actors pose as company IT and/or helpdesk staff to gain access to targeted organization’s networks.
Scattered Spider threat actors use social engineering to convince IT helpdesk personnel to reset passwords and/or MFA tokens.
Table 11: Credential Access
Technique Title
ID
Use
Credential Access
TA0006
Scattered Spider threat actors use tools, such as Raccoon Stealer, to obtain login credentials.
Forge Web Credentials
T1606
Scattered Spider threat actors may forge MFA tokens to gain access to a targeted organization’s network.
Multi-Factor Authentication Request Generation
T1621
Scattered Spider sends repeated MFA notification prompts to lead employees to accept the prompt and gain access to the target network.


- Scattered Spider threat actors -> USES -> Raccoon Stealer
  Literal support: Scattered Spider threat actors use tools, such as Raccoon Stealer, to obtain login credentials.

## AA23-320A:development:llama500:19523:21935

Status: candidates_ready_for_review
Case time: 2.54 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:


T1606
Scattered Spider threat actors may forge MFA tokens to gain access to a targeted organization’s network.
Multi-Factor Authentication Request Generation
T1621
Scattered Spider sends repeated MFA notification prompts to lead employees to accept the prompt and gain access to the target network.
Unsecured Credentials: Credentials in Files
T1552.001
Scattered Spider threat actors search for insecurely stored credentials on targeted organization’s systems.
Unsecured Credentials: Private Keys
T1552.004
Scattered Spider threat actors search for insecurely stored private keys on targeted organization’s systems.
SIM Swap
T1451
Scattered Spider threat actors steal OTPs, credentials, and security answers.
Table 12: Discovery
Technique Title
ID
Use
Discovery
TA0007
Upon gaining access to a targeted network, Scattered Spider threat actors seek out SharePoint sites, credential storage documentation, VMware vCenter, infrastructure backups and enumerate AD to identify useful information to support further operations.
Browser Information Discovery
T1217
Scattered Spider threat actors use tools (e.g., Raccoon Stealer) to obtain browser histories.
Cloud Service Dashboard
T1538
Scattered Spider threat actors leverage AWS Systems Manager Inventory to discover targets for lateral movement.
File and Directory Discovery
T1083
Scattered Spider threat actors search a compromised network to discover files and directories for further information or exploitation.
Remote System Discovery
T1018
Scattered Spider threat actors search for infrastructure, such as remote systems, to exploit.
Steal Web Session Cookie
T1539
Scattered Spider threat actors use tools, such as Raccoon Stealer, to obtain browser cookies.
Table 13: Lateral Movement
Technique Title
ID
Use
Lateral Movement
TA0008
Scattered Spider threat actors laterally move across a target network upon gaining access and establishing persistence.
Remote Services: Cloud Services
T1021.007
Scattered Spider threat actors use pre-existing cloud instances for lateral movement and data collection.
Table 14: Collection
Technique Title
ID
Use
Data from Information Repositories: Code Repositories
T1213.003
Scattered Spider threat actors search code repositories for data collection and exfiltration.
Data from Information Repositories: SharePoint
T1213.002
Scattered Spider threat actors search SharePoint repositories for information.
Data Staged
T1074


- Scattered Spider threat actors -> USES -> Raccoon Stealer
  Literal support: Scattered Spider threat actors use tools (e.g., Raccoon Stealer) to obtain browser histories.

## AA23-320A:development:llama500:21657:23828

Status: candidates_ready_for_review
Case time: 1.15 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Exact source window:

: Code Repositories
T1213.003
Scattered Spider threat actors search code repositories for data collection and exfiltration.
Data from Information Repositories: SharePoint
T1213.002
Scattered Spider threat actors search SharePoint repositories for information.
Data Staged
T1074
Scattered Spider threat actors stage data from multiple data sources into a centralized database before exfiltration.
Email Collection
T1114
Scattered Spider threat actors search targeted organization’s emails to determine if the organization has detected the intrusion and initiated any security response.
Data from Cloud Storage
T1530
Scattered Spider threat actors search data in cloud storage for collection and exfiltration.
Table 15: Command and Control
Technique Title
ID
Use
Remote Access Software
T1219
Impersonating helpdesk personnel, Scattered Spider threat actors direct employees to run commercial remote access tools thereby enabling access to, and command and control of, the targeted organization’s network.
Scattered Spider threat actors leverage third-party software to facilitate lateral movement and maintain persistence on a target organization’s network.
Proxy
T1090
Scattered Spider threat actors use proxy networks to disguise the source of malicious traffic.
Table 16: Exfiltration
Technique Title
ID
Use
Exfiltration
TA0010
Scattered Spider threat actors exfiltrate data from a target network for data extortion.
Exfiltration Over Web Service
T1567
Scattered Spider threat actors exfiltrate data using the Snowflake Data Cloud.
Table 17: Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
Scattered Spider threat actors recently began encrypting data on a target network and demanding a ransom for decryption.
Scattered Spider threat actors have been observed encrypting VMware ESXi servers.
Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1567.002
Scattered Spider threat actors exfiltrate data to multiple sites including U.S.-based data centers and MEGA[.]NZ.
Financial Theft
T1657
Scattered Spider threat actors monetized access to targeted organization’s networks in numerous ways including extortion-enabled ransomware and data theft.


- Scattered Spider threat actors -> USES -> Snowflake Data Cloud
  Literal support: Scattered Spider threat actors exfiltrate data using the Snowflake Data Cloud.

## AA23-353A:development:llama500:6620:7679

Status: empty_extraction
Case time: 0.40 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Exact source window:

b500edf
Tunneler Tool
conhost.exe
824d0e31fd08220a25c06baee1044818
Anti Virus Tools Killer
ibmModule.dll
eea9ab1f36394769d65909f6ae81834b
CobaltStrike BEACON
ConnectivityDiagnos.exe
944153fb9692634d6c70899b83676575
ALPHV Windows Encryptor
7O3cCX9YcHMV2.exe
61804a029e9b1753d58a6bf0274c25a6
MeshCentral Agent
WPEHOSTSVC64.exe
83deea3b61b6a734e7e4a566dbb6bffa
ScreenConnect & attacker tools installer
deployService.exe
8738b8637a20fa65c6e64d84d1cfe570
Suspected Proxy Tool
socks32.exe
Table 2: SHA256 Hashes
SHA256
Description
c64300cf8bacc4e42e74715edf3f8c3287a780c9c0a38b0d9675d01e7e231f16
ALPHV Windows Encryptor
1f5e4e2c78451623cfbf32cf517a92253b7abfe0243297c5ddf7dd1448e460d5
Anti Virus Tools Killer
3670dd4663adca40f168f3450fa9e7e84bc1a612d78830004020b73bd40fcd71
CobaltStrike BEACON
af28b78c64a9effe3de0e5ccc778527428953837948d913d64dbd0fa45942021
CobaltStrike BEACON
bbfe7289de6ab1f374d0bcbeecf31cad2333b0928ea883ca13b9e733b58e27b1
ALPHV Linux Encryptor
5d1df950b238825a36fa6204d1a2935a5fbcfe2a5991a7fc69c74f476df67905
SimpleHelp Remote Management tool



## AA23-353A:development:llama500:7546:8804

Status: empty_extraction
Case time: 0.37 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Exact source window:

733b58e27b1
ALPHV Linux Encryptor
5d1df950b238825a36fa6204d1a2935a5fbcfe2a5991a7fc69c74f476df67905
SimpleHelp Remote Management tool
bd9edc3bf3d45e3cdf5236e8f8cd57a95ca3b41f61e4cd5c6c0404a83519058e
Tunneler Tool
732e24cb5d7ab558effc6dc88854f756016352c923ff5155dcb2eece35c19bc0
Anti Virus Tools Killer
Table 3: SHA1 Hashes
SHA1
Description
3dd0f674526f30729bced4271e6b7eb0bb890c52
ALPHV Windows Encryptor
d6d442e8b3b0aef856ac86391e4a57bcb93c19ad
Anti Virus Tools Killer
6b52543e4097f7c39cc913d55c0044fcf673f6fc
CobaltStrike BEACON
004ba0454feb2c4033ff0bdb2ff67388af0c41b6
CobaltStrike BEACON
430bd437162d4c60227288fa6a82cde8a5f87100
SimpleHelp Remote Management tool
1376ac8b5a126bb163423948bd1c7f861b4bfe32
Tunneler Tool
380f941f8047904607210add4c6da2da8f8cd398
Anti Virus Tools Killer
Table 4: Network Indicators
Indicator Type
Network Indicator
Description
Domain
resources.docusong[.]com
Command and Control Server
Domain
Fisa99.screenconnect[.]com
ScreenConnect Remote Access
IP Address
5.199.168.24
Command and Control Server
IP Address
91.92.254.193
SimpleHelp Remote Access
Domain
pcrendal[.]com
Command and Control Server
Domain
instance-qqemas-relay[.]screenconnect[.]com
ScreenConnect Remote Access
Domain
instance-rbjvws-relay.screenconnect[.]com



## AA23-353A:development:llama500:8594:10523

Status: empty_extraction
Case time: 0.45 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Exact source window:

254.193
SimpleHelp Remote Access
Domain
pcrendal[.]com
Command and Control Server
Domain
instance-qqemas-relay[.]screenconnect[.]com
ScreenConnect Remote Access
Domain
instance-rbjvws-relay.screenconnect[.]com
ScreenConnect Remote Access
IP Address
5.199.168[.]233
IP Address used by Threat Actor
IP Address
92.223.89[.]55
IP Address used by Threat Actor
IP Address
185.195.59[.]218
IP Address used by Threat Actor
IP Address
51.159.103[.]112
IP Address used by Threat Actor
IP Address
45.32.141[.]168
Command and Control Server
IP Address
45.77.0[.]92
Command and Control Server
MITRE ATT&CK TACTICS AND TECHNIQUES
See Table 5 through Table 7 for all referenced threat actor tactics and techniques in this advisory.
Table 5: ALPHV Blackcat/ALPHV Threat Actors ATT&CK Techniques - Reconnaissance
Technique Title
ID
Use
Phishing for Information
T1598
ALPHV Blackcat affiliates pose as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees to access the target network.
Table 6: ALPHV Blackcat/ALPHV Threat Actors ATT&CK Techniques – Resource Development
Technique Title
ID
Use
Compromise Accounts
T1586
ALPHV Blackcat affiliates use compromised accounts to gain access to victims’ networks.
Table 7: ALPHV Blackcat/ALPHV Threat Actors ATT&CK Techniques – Credential Access
Technique Title
ID
Use
Obtain Credentials from Passwords Stores
T1555
ALPHV Blackcat affiliates obtain passwords from local networks, deleted servers, and domain controllers.
Steal or Force Kerberos Tickets
T1558
ALPHV Blackcat/ALPHV affiliates use Kerberos token generation for domain access.
Adversary-in-the-Middle
T1557
ALPHV Blackcat/ALPHV affiliates use the open-source framework Evilginx2 to obtain MFA credentials, login credentials, and session cookies for targeted networks.
INCIDENT RESPONSE
If compromise is detected, organizations should:
Quarantine or take offline potentially affected hosts.



## AA23-353A:development:llama500:9068:11166

Status: candidates_ready_for_review
Case time: 1.10 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Exact source window:


IP Address
45.32.141[.]168
Command and Control Server
IP Address
45.77.0[.]92
Command and Control Server
MITRE ATT&CK TACTICS AND TECHNIQUES
See Table 5 through Table 7 for all referenced threat actor tactics and techniques in this advisory.
Table 5: ALPHV Blackcat/ALPHV Threat Actors ATT&CK Techniques - Reconnaissance
Technique Title
ID
Use
Phishing for Information
T1598
ALPHV Blackcat affiliates pose as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees to access the target network.
Table 6: ALPHV Blackcat/ALPHV Threat Actors ATT&CK Techniques – Resource Development
Technique Title
ID
Use
Compromise Accounts
T1586
ALPHV Blackcat affiliates use compromised accounts to gain access to victims’ networks.
Table 7: ALPHV Blackcat/ALPHV Threat Actors ATT&CK Techniques – Credential Access
Technique Title
ID
Use
Obtain Credentials from Passwords Stores
T1555
ALPHV Blackcat affiliates obtain passwords from local networks, deleted servers, and domain controllers.
Steal or Force Kerberos Tickets
T1558
ALPHV Blackcat/ALPHV affiliates use Kerberos token generation for domain access.
Adversary-in-the-Middle
T1557
ALPHV Blackcat/ALPHV affiliates use the open-source framework Evilginx2 to obtain MFA credentials, login credentials, and session cookies for targeted networks.
INCIDENT RESPONSE
If compromise is detected, organizations should:
Quarantine or take offline potentially affected hosts.
Reimage compromised hosts.
Provision new account credentials.
Collect and review artifacts such as running processes/services, unusual authentications, and recent network connections.
Report the compromise or phishing incident to CISA via CISA’s 24/7 Operations Center (report@cisa.gov or 1-844-Say-CISA). State, local, tribal, or territorial government entities can also report to MS-ISAC (SOC@cisecurity.org or 866-787-4722).
To report spoofing or phishing attempts (or to report that you’ve been a victim), file a complaint with the FBI’s Internet Crime Complaint Center (IC3), or contact your local FBI Field Office to report an incident.


- ALPHV Blackcat/ALPHV affiliates -> USES -> Evilginx2
  Literal support: ALPHV Blackcat/ALPHV affiliates use the open-source framework Evilginx2 to obtain MFA credentials, login credentials, and session cookies for targeted networks.

## AA24-060A:development:llama500:6217:8285

Status: candidates_ready_for_review
Case time: 3.40 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

 firewall configurations using commands like netsh firewall set opmode mode=disable [T1562.004]. Additionally, Phobos actors can evade detection by using the following tools: Universal Virus Sniffer, Process Hacker, and PowerTool [T1562].
Persistence and Privilege Escalation
According to open source reporting, Phobos ransomware uses commands such as Exec.exe or the bcdedit[.]exe control mechanism. Phobos has also been observed using Windows Startup folders and Run Registry Keys such as C:/Users\Admin\AppData\Local\directory [T1490][T1547.001] to maintain persistence within compromised environments.[5]
Additionally, Phobos actors have been observed using built-in Windows API functions [T1106] to steal tokens [T1134.001], bypass access controls, and create new processes to escalate privileges by leveraging the SeDebugPrivilege process [T1134.002]. Phobos actors attempt to authenticate using cached password hashes on victim machines until they reach domain administrator access [T1003.005].
Discovery and Credential Access
Phobos actors additionally use open source tools [T1588.002] such as Bloodhound and Sharphound to enumerate the active directory [T1087.002]. Mimikatz and NirSoft, as well as Remote Desktop Passview to export browser client credentials [T1003.001][T1555.003], have also been used. Furthermore, Phobos ransomware is able to enumerate connected storage devices [T1082], running processes [T1057], and encrypt user files [T1083].
Exfiltration
Phobos actors have been observed using WinSCP and Mega.io for file exfiltration.[11] They use WinSCP to connect directly from a victim network to an FTP server [T1071.002] they control [TA0010]. Phobos actors install Mega.io [T1048] and use it to export victim files directly to a cloud storage provider [T1567.002]. Data is typically archived as either a .rar or .zip file [T1560] to be later exfiltrated. They target legal documentation, financial records, technical documents (including network architecture), and databases for commonly used password management software [T1555.005].
Impact


- netsh -> USES_TECHNIQUE -> T1562.004
  Literal support: firewall configurations using commands like netsh firewall set opmode mode=disable [T1562.004].
- Phobos -> USES_TECHNIQUE -> T1490
  Literal support: Phobos has also been observed using Windows Startup folders and Run Registry Keys such as C:/Users\Admin\AppData\Local\directory [T1490][T1547.001] to maintain persistence within compromised environments.[5]
- Phobos actors -> USES_TECHNIQUE -> T1106
  Literal support: Additionally, Phobos actors have been observed using built-in Windows API functions [T1106] to steal tokens [T1134.001]
- FTP -> USES_TECHNIQUE -> T1071.002
  Literal support: Phobos actors have been observed using WinSCP and Mega.io for file exfiltration.[11] They use WinSCP to connect directly from a victim network to an FTP server [T1071.002] they control [TA0010].

## AA24-060A:development:llama500:8001:10088

Status: validation_failed
Case time: 6.08 seconds; attempts: 2.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

.002]. Data is typically archived as either a .rar or .zip file [T1560] to be later exfiltrated. They target legal documentation, financial records, technical documents (including network architecture), and databases for commonly used password management software [T1555.005].
Impact
After the exfiltration phase, Phobos actors then hunt for backups. They use vssadmin.exe and Windows Management Instrumentation command-line utility (WMIC) to discover and delete volume shadow copies in Windows environments. This prevents victims from recovering files after encryption has taken place [T1047][T1490].
Phobos.exe contains functionality to encrypt all connected logical drives on the target host [T1486]. Each Phobos ransomware executable has unique build identifiers (IDs), affiliate IDs, as well as a unique ransom note which is embedded in the executable. After the ransom note has populated on infected workstations, Phobos ransomware continues to search for and encrypt additional files.
Most extortion [T1657] occurs via email; however, some affiliate groups have used voice calls to contact victims. In some cases, Phobos actors have used onion sites to list victims and host stolen victim data. Phobos actors use various instant messaging applications such as ICQ, Jabber, and QQ to communicate [T1585]. See Figure 2 for a list of email providers used by the following Phobos affiliates: Devos, Eight, Elbie, Eking, and Faust.[6]
Figure 1: Phobos Affiliate Providers List
INDICATORS OF COMPROMISE (IOCs)
See Table 1 through 6 for IOCs obtained from CISA and the FBI investigations from September through November 2023.
Table 1: Associated Phobos Domains
Associated Phobos Domains
adstat477d[.]xyz
demstat577d[.]xyz [12]
serverxlogs21[.]xyz
Table 2: Observed Phobos Shell Commands
Shell Commands
vssadmin delete shadows /all /quiet [T1490]
netsh advfirewall set currentprofile state off
wmic shadowcopy delete
netsh firewall set opmode mode=disable [T1562.004]
bcdedit /set {default} bootstatuspolicy ignoreallfailures [T1547.001]
bcdedit /set {default} recoveryenabled no [T1490]


Error: Preserve the affiliates qualifier in this prose actor mention.

## AA24-060A:development:llama500:9889:11600

Status: candidates_ready_for_review
Case time: 1.13 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

 off
wmic shadowcopy delete
netsh firewall set opmode mode=disable [T1562.004]
bcdedit /set {default} bootstatuspolicy ignoreallfailures [T1547.001]
bcdedit /set {default} recoveryenabled no [T1490]
wbadmin delete catalog -quiet
mshta C:\%USERPROFILE%\Desktop\info.hta [T1218.005]
mshta C:\%PUBLIC%\Desktop\info.hta
mshta C:\info.hta
The commands above are observed during the execution of a Phobos encryption executable. A Phobos encryption executable spawns a cmd.exe process, which then executes the commands listed in Table 1 with their respective Windows system executables. When the commands above are executed on a Windows system, volume shadow copies are deleted and Windows Firewall is disabled. Additionally, the system’s boot status policy is set to boot even when there are errors during the boot process, and automatic recovery options, like Windows Recovery Environment (WinRE), are disabled for the given boot entry. The system’s backup catalog is also deleted. Finally, the Phobos ransom note is displayed to the end user using mshta.exe.
Table 3: Observed Phobos Registry Keys
Registry Keys
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\<Phobos exe name>
C:/Users\Admin\AppData\Local\directory
Table 4: Observed Phobos Actor Email Addresses
Email Addresses
AlbetPattisson1981@protonmail[.]com
henryk@onionmail[.]org
atomicday@tuta[.]io
info@fobos[.]one
axdus@tuta[.]io
it.issues.solving@outlook[.]com
barenuckles@tutanota[.]com
JohnWilliams1887@gmx[.]com
Bernard.bunyan@aol[.]com
jonson_eight@gmx[.]us
bill.g@gmx[.]com
joshuabernandead@gmx[.]com
bill.g@msgsafe[.]io
LettoIntago@onionmail[.]com
bill.g@onionmail[.]org
Luiza.li@tutanota[.]com
bill.gTeam@gmx[.]com
MatheusCosta0194@gmx[.]com


- netsh -> USES_TECHNIQUE -> T1562.004
  Literal support: netsh firewall set opmode mode=disable [T1562.004]

## AA24-060A:development:llama500:11464:12620

Status: empty_extraction
Case time: 0.36 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

msgsafe[.]io
LettoIntago@onionmail[.]com
bill.g@onionmail[.]org
Luiza.li@tutanota[.]com
bill.gTeam@gmx[.]com
MatheusCosta0194@gmx[.]com
blair_lockyer@aol[.]com
mccreight.ellery@tutanota[.]com
CarlJohnson1948@gmx[.]com
megaport@tuta[.]io
cashonlycash@gmx[.]com
miadowson@tuta[.]io
chocolate_muffin@tutanota[.]com
MichaelWayne1973@tutanota[.]com
claredrinkall@aol[.]com
normanbaker1929@gmx[.]com
clausmeyer070@cock[.]li
nud_satanakia@keemail[.]me
colexpro@keemail[.]me
please@countermail[.]com
cox.barthel@aol[.]com
precorpman@onionmail[.]org
crashonlycash@gmx[.]com
recovery2021@inboxhub[.]net
everymoment@tuta[.]io
recovery2021@onionmail[.]org
expertbox@tuta[.]io
SamuelWhite1821@tutanota[.]com
fastway@tuta[.]io
SaraConor@gmx[.]com
fquatela@techie[.]com
secdatltd@gmx[.]com
fredmoneco@tutanota[.]com
skymix@tuta[.]io
getdata@gmx[.]com
sory@countermail[.]com
greenbookBTC@gmx[.]com
spacegroup@tuta[.]io
greenbookBTC@protonmail[.]com
stafordpalin@protonmail[.]com
helperfiles@gmx[.]com
starcomp@keemail[.]me
helpermail@onionmail[.]org
xdone@tutamail[.]com
helpfiles@onionmail[.]org
xgen@tuta[.]io
helpfiles102030@inboxhub[.]net
xspacegroup@protonmail[.]com



## AA24-060A:development:llama500:12481:13892

Status: empty_extraction
Case time: 0.36 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

@onionmail[.]org
xdone@tutamail[.]com
helpfiles@onionmail[.]org
xgen@tuta[.]io
helpfiles102030@inboxhub[.]net
xspacegroup@protonmail[.]com
helpforyou@gmx[.]com
zgen@tuta[.]io
helpforyou@onionmail[.]org
zodiacx@tuta[.]io
Table 5: Observed Phobos Actor Telegram Username
Telegram Username
@phobos_support
Table 6: Observed Phobos Actor Wickr Address
Wickr Address
Vickre me
Disclaimer: Organizations are encouraged to investigate the use of the IOCs in Table 7 for related signs of compromise prior to performing remediation actions.
Table 7: Phobos IOCs from September through December 2023
Associated IP Address
File Type
File Name
SHA 256 Hash
194.165.16[.]4 (October 2023)
Win32.exe
Ahpdate.exe [13]
0000599cbc6e5b0633c5a6261c79e4d3d81005c77845c6b0679d854884a8e02f
45.9.74[.]14 (December 2023)
147.78.47[.]224 (December 2023)
Executable and Linkable Format (ELF) [14]
1570442295
(Trojan Linux Mirai)
7451be9b65b956ee667081e1141531514b1ec348e7081b5a9cd1308a98eec8f0
185.202.0[.]111 (September 2023)
Win32.exe [15]
cobaltstrike_shellcode[.]exe (C2 activity)
185.202.0[.]111 (December 2023)
.txt [16]
f1425cff3d28afe5245459afa6d7985081bc6a62f86dce64c63daeb2136d7d2c.bin (Trojan)
Disclaimer: Organizations are encouraged to investigate the use of the file hashes in Tables 8 and 9 for related signs of compromise prior to performing remediation actions.
Table 8: Phobos Actor File Hashes Observed in October 2023



## AA24-060A:development:llama500:13641:14721

Status: empty_extraction
Case time: 0.29 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

7d2c.bin (Trojan)
Disclaimer: Organizations are encouraged to investigate the use of the file hashes in Tables 8 and 9 for related signs of compromise prior to performing remediation actions.
Table 8: Phobos Actor File Hashes Observed in October 2023
Phobos Ransomware SHA 256 Malicious Trojan Executable File Hashes
518544e56e8ccee401ffa1b0a01a10ce23e49ec21ec441c6c7c3951b01c1b19c
9215550ce3b164972413a329ab697012e909d543e8ac05d9901095016dd3fc6c
482754d66d01aa3579f007c2b3c3d0591865eb60ba60b9c28c66fe6f4ac53c52
c0539fd02ca0184925a932a9e926c681dc9c81b5de4624250f2dd885ca5c4763
Table 9: Phobos Actor File Hashes from Open Source from November 2023 [17]
Phobos Ransomware SHA 256 File Hashes
58626a9bfb48cd30acd0d95debcaefd188ae794e1e0072c5bde8adae9bccafa6
f3be35f8b8301e39dd3dffc9325553516a085c12dc15494a5e2fce73c77069ed
518544e56e8ccee401ffa1b0a01a10ce23e49ec21ec441c6c7c3951b01c1b19c
32a674b59c3f9a45efde48368b4de7e0e76c19e06b2f18afb6638d1a080b2eb3
2704e269fb5cf9a02070a0ea07d82dc9d87f2cb95e60cb71d6c6d38b01869f66
fc4b14250db7f66107820ecc56026e6be3e8e0eb2d428719156cf1c53ae139c6



## AA24-060A:development:llama500:14622:16556

Status: candidates_ready_for_review
Case time: 1.04 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

9d87f2cb95e60cb71d6c6d38b01869f66
fc4b14250db7f66107820ecc56026e6be3e8e0eb2d428719156cf1c53ae139c6
a91491f45b851a07f91ba5a200967921bf796d38677786de51a4a8fe5ddeafd2
MITRE ATT&CK TECHNIQUES
See Table 10 through 22 for all threat actor tactics and techniques referenced in this advisory.
Table 10: Phobos Threat Actors ATT&CK Techniques for Enterprise – Reconnaissance
Technique Title
ID
Use
Search Open Websites/Domains
T1593
Phobos actors perform open source research to find information about victims that can be used during targeting to create a victim profile.
Scanning IP Blocks
T1595.001
Phobos actors used IP scanning tools to include Angry IP Scanner to search for vulnerable RDP ports.
Phishing for Information
T1598
Phobos actors use phishing campaigns to social engineer information from users and gain access to vulnerable RDP ports.
Table 11: Phobos Threat Actors ATT&CK Techniques for Enterprise – Resource Development
Technique Title
ID
Use
Establish Accounts
T1585
Phobos actors establish accounts to communicate.
Obtain Capabilities: Tool
T1588.002
Phobos actors used open source tools in their attack.
Table 12: Phobos Threat Actors ATT&CK Techniques for Enterprise – Initial Access
Technique Title
ID
Use
Valid Accounts
T1078
Following successful RDP authentication, Phobos actors search for IP addresses and pair them with their associated computer to create a victim profile.
External Remote Services
T1133
Phobos actors may leverage external-facing remote services to initially access and/or persist within a network.
Phishing: Spearphishing Attachment
T1566.001
Phobos actors used a spoofed email attachment to execute attack.
Table 13: Phobos Threat Actors ATT&CK Techniques for Enterprise – Execution
Technique Title
ID
Use
Windows Management Instrumentation
T1047
Phobos actors used Windows Management Instrumentation command-line utility (WMIC) to prevent victims from recovering files.
Windows Command Shell


- Phobos actors -> USES -> Windows Management Instrumentation
  Literal support: Phobos actors used Windows Management Instrumentation command-line utility (WMIC) to prevent victims from recovering files.

## AA24-060A:development:llama500:16276:18432

Status: candidates_ready_for_review
Case time: 2.96 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

13: Phobos Threat Actors ATT&CK Techniques for Enterprise – Execution
Technique Title
ID
Use
Windows Management Instrumentation
T1047
Phobos actors used Windows Management Instrumentation command-line utility (WMIC) to prevent victims from recovering files.
Windows Command Shell
T1059.003
Phobos actors can use the previous commands to perform commands with windows shell functions.
Native API
T1106
Phobos actors used open source tools to enumerate the active directory.
Malicious File
T1204.002
Phobos actors attached a malicious email attachment to deliver ransomware.
Table 14: Phobos Threat Actors ATT&CK Techniques for Enterprise – Persistence
Technique Title
ID
Use
Registry Run Keys / Startup Folder
T1547.001
Phobos ransomware operates using the Exec.exe control mechanism and has been observed using Windows Startup folders and Run Registry Keys.
Table 15: Phobos Threat Actors ATT&CK Techniques for Enterprise – Privilege Escalation
Technique Title
ID
Use
Privilege Escalation
TA0004
Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.
Portable Executable Injection
T1055.002
Phobos actors use Smokeloader to inject code into running processes to identify an entry point through enabling a VirtualAlloc or VirtualProtect process.
Asynchronous Procedure Call
T1055.004
During phase two of execution, Phobos ransomware sends a call back from an identified entry point.
Access Token Manipulation: Token Impersonation/Theft
T1134.001
Phobos actors can use Windows API functions to steal tokens.
Create Process with Token
T1134.002
Phobos actors used Windows API functions to steal tokens, bypass access controls and create new processes.
Table 16: Phobos Threat Actors ATT&CK Techniques for Enterprise – Defense Evasion
Technique Title
ID
Use
Software Packing
T1027.002
Phobos actors deployed a portable executable (PE) to conceal code.
Embedded Payloads
T1027.009
Phobos actors embedded the ransomware as a hidden payload by using Smokeloader.
Deobfuscate/Decode Files or Information
T1140
During phase two of execution, Phobos actors’ malware stores and decrypts information.


- Phobos actors -> USES -> Windows Management Instrumentation
  Literal support: Phobos actors used Windows Management Instrumentation command-line utility (WMIC) to prevent victims from recovering files.
- Phobos actors -> USES -> Phobos
  Literal support: Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.
- Phobos actors -> USES -> 1saas.exe
  Literal support: Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.
- Phobos actors -> USES -> cmd.exe
  Literal support: Phobos actors use run commands like 1saas.exe, or cmd.exe to deploy additional Phobos payloads with escalated privileges.

## AA24-060A:development:llama500:18199:20450

Status: candidates_ready_for_review
Case time: 1.78 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:

 Payloads
T1027.009
Phobos actors embedded the ransomware as a hidden payload by using Smokeloader.
Deobfuscate/Decode Files or Information
T1140
During phase two of execution, Phobos actors’ malware stores and decrypts information.
System Binary Proxy Execution: Mshta
T1218.005
Phobos actors used Mshta to execute malicious files.
Impair Defenses
T1562
Phobos actors can use Universal Virus Sniffer, Process Hacker, and PowerTool to evade detection.
Disable or Modify System Firewall
T1562.004
Phobos ransomware has been observed bypassing organizational network defense protocols through modifying system firewall configurations.
Table 17: Phobos Threat Actors ATT&CK Techniques for Enterprise – Credential Access
Technique Title
ID
Use
OS Credential Dumping: LSASS Memory
T1003.001
Phobos actors used Mimikatz to export credentials.
OS Credential Dumping: Cached Domain Credentials
T1003.005
Phobos actors use cached domain credentials to authenticate as the domain administrator in the event a domain controller is unavailable.
Brute Force
T1110
Phobos actors may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.
Credentials from Password Stores
T1555
Phobos actors may search for common password storage locations to obtain user credentials.
Credentials from Password Stores: Credentials from Web Browsers
T1555.003
Phobos actors use Nirsoft or Passview to export client credentials from web browsers.
Phobos actors search for stored credentials in browser clients once they gain initial network access.
Credentials from Password Stores: Password Managers
T1555.005
Phobos actors targeted victim’s databases for password management software.
Table 18: Phobos Threat Actors ATT&CK Techniques for Enterprise – Discovery
Technique Title
ID
Use
Process Discovery
T1057
Phobos ransomware is able to run processes.
System Information Discovery
T1082
Phobos ransomware is able to enumerate connected storage devices.
File and Directory Discovery
T1083
Phobos ransomware can encrypt user files.
Domain Account
T1087.002
Phobos threat actor used Bloodhound and Sharphound to enumerate the active directory.
Table 19: Phobos Threat Actors ATT&CK Techniques for Enterprise – Collection


- Phobos actors -> USES -> Universal Virus Sniffer
  Literal support: Phobos actors can use Universal Virus Sniffer, Process Hacker, and PowerTool to evade detection.
- Phobos actors -> USES -> Mimikatz
  Literal support: Phobos actors used Mimikatz to export credentials.

## AA24-060A:development:llama500:20213:22160

Status: candidates_ready_for_review
Case time: 1.74 seconds; attempts: 1.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Exact source window:


T1083
Phobos ransomware can encrypt user files.
Domain Account
T1087.002
Phobos threat actor used Bloodhound and Sharphound to enumerate the active directory.
Table 19: Phobos Threat Actors ATT&CK Techniques for Enterprise – Collection
Technique Title
ID
Use
Archive Collected Data
T1560
Phobos threat actors archive data as either a .rar or .zip file to be later exfiltrated.
Table 20: Phobos Threat Actors ATT&CK Techniques for Enterprise – Command and Control
Technique Title
ID
Use
Data Obfuscation: Protocol Impersonation
T1001.003
Phobos actors used a stealth process to obfuscate C2 activity.
File Transfer Protocols
T1071.002
Phobos threat actors used WinSCP to connect the victim’s network to an FTP server.
Ingress Tool Transfer
T1105
Phobos ransomware extracts its final payload from the hashed file.
Remote Access Software
T1219
Phobos threat actors used remote access tools to establish a remote connection within victim’s network.
Table 21: Phobos Threat Actors ATT&CK Techniques for Enterprise – Exfiltration
Technique Title
ID
Use
Exfiltration
TA0010
Phobos threat actors may use exfiltration techniques to steal data from your network.
Exfiltration Over Alternative Protocol
T1048
Phobos threat actors use software to export files to a cloud.
Exfiltration to Cloud Storage
T1567.002
Phobos threat actors use Mega.io to exfiltrate data to a cloud storage service rather than over their primary command and control channel.
Table 22: Phobos Threat Actors ATT&CK Techniques for Enterprise – Impact
Technique Title
ID
Use
Data Encrypted for Impact
T1486
Phobos threat actors use the Phobos.exe command to encrypt data on all logical drives connected to the network.
Inhibit System Recovery
T1490
Phobos threat actors may delete or remove backups to include volume shadow copies from Windows environments to prevent victim data recovery response efforts.
Financial Theft
T1657
Phobos threat actor’s extort victims for financial gain.


- Phobos threat actors -> USES -> FTP
  Literal support: Phobos threat actors used WinSCP to connect the victim’s network to an FTP server.
- Phobos threat actors -> USES -> Phobos.exe
  Literal support: Phobos threat actors use the Phobos.exe command to encrypt data on all logical drives connected to the network.

