# Five-report source chunk preparation

Status: ready for extraction pilot. No extraction, database writes or evaluation scores were produced.

Source-only selection: BianLian, Rhysida, Scattered Spider, ALPHV Blackcat and Phobos.
Reports containing held-out evidence were excluded using split metadata. Gold labels and QA reference answers were not read.

Tokenizer artifact: 20261014T064015Z-126bb1e2
Tokenizer SHA-256: 0f19bfc2cced451a1be5707855af7f7579ccc88c6943b45c93096555a73163e9
Chunk fingerprint: b12eca347c3118448c053304dde5d81a8a5dc787f60d8d297af27dd6d7b38635

Technical sections run from the Technical Details heading to the Mitigations heading. Exact normalized source offsets and checksums are preserved.
This is a pilot subset, not the complete 15-report corpus. IOC/table content inside the technical sections is retained; row and caption support needs semantic review during extraction.
Window counts exclude inherited context and chat/system/schema overhead, which must be budgeted separately.
Line boundaries are preferred within 400–600 source tokens, targeting 500 with about 60-token overlap. Final windows may be reanchored with greater overlap to retain the minimum size; measured overlap is recorded.

| Report | All windows | Pilot windows |
| --- | ---: | ---: |
| AA23-136A | 13 | 2 |
| AA23-319A | 13 | 2 |
| AA23-320A | 10 | 2 |
| AA23-353A | 6 | 2 |
| AA24-060A | 12 | 2 |

## Selected pilot windows

### 1. AA23-136A:development:llama500:3551:5862

Offsets: 3551:5862; source tokens: 515; inherited context tokens: 16; preceding overlap: 0.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Inherited source context:

#StopRansomware: BianLian Ransomware Group
Technical Details

Exact source window:


Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 16. See the MITRE ATT&CK Tactics and Techniques section of this advisory for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
BianLian is a ransomware developer, deployer, and data extortion cybercriminal group. Since June 2022, FBI has observed BianLian group affecting organizations in multiple U.S. critical infrastructure sectors. In Australia, ASD’S ACSC has observed BianLian group predominately targeting private enterprises, including one critical infrastructure organization. BianLian group originally employed a double-extortion model in which they exfiltrated financial, client, business, technical, and personal files for leverage and encrypted victims’ systems. In 2023, FBI observed BianLian shift primarily to exfiltration-based extortion with victims’ systems left intact, and ASD’S ACSC observed BianLian shift exclusively to exfiltration-based extortion. BianLian actors warn of financial, business, and legal ramifications if payment is not made.
Initial Access
BianLian group actors gain initial access to networks by leveraging compromised Remote Desktop Protocol (RDP) credentials likely acquired from initial access brokers [T1078][T1133] or via phishing [T1566].
(New, November 20, 2024) BianLian group actors target public-facing applications of both Windows and ESXi infrastructure, possibly leveraging the ProxyShell (CVE-2021-34473, CVE-2021-34523, and CVE-2021-31207) exploit chain to gain initial access [T1190].
Command and Control
BianLian group actors implant a custom backdoor specific to each victim written in Go (see the Indicators of Compromise Section for an example) [T1587.001] and install remote management and access software for persistence and command and control [T1105][T1219].
FBI also observed BianLian group actors create and/or activate local administrator accounts [T1136.001] and change those account passwords [T1098].
(New, November 20, 2024) BianLian group actors may be using the reverse proxy tool Ngrok and/or a modified version of the open-source Rsocks utility [T1090]. The group may have used external proxy Rsocks to establish SOCKS5 network tunnels from victim networks and to mask the destination of C2 traffic [T1090.002].


### 2. AA23-136A:development:llama500:5605:7833

Offsets: 5605:7833; source tokens: 495; inherited context tokens: 16; preceding overlap: 60.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Inherited source context:

#StopRansomware: BianLian Ransomware Group
Technical Details

Exact source window:

 the reverse proxy tool Ngrok and/or a modified version of the open-source Rsocks utility [T1090]. The group may have used external proxy Rsocks to establish SOCKS5 network tunnels from victim networks and to mask the destination of C2 traffic [T1090.002].
Privilege Escalation
(New, November 20, 2024) BianLian group actors have exploited CVE-2022-37969, which affects Windows 10 and 11 systems, to escalate privileges [T1068].
Defense Evasion
BianLian group actors use PowerShell [T1059.001] and Windows Command Shell [T1059.003] to disable antivirus tools [T1562.001], specifically Windows defender and Anti-Malware Scan Interface (AMSI). BianLian actors modify the Windows Registry [T1112] to disable tamper protection for Sophos SAVEnabled, SEDEenabled, and SAVService services, which enables them to uninstall these services. See Appendix: Windows PowerShell and Command Shell Activity for additional information, including specific commands.
(New, November 20, 2024) BianLian group actors rename binaries and scheduled tasks after legitimate Windows services or security products [T1036.004]. BianLian group actors may pack executables using UPX to conceal their code in an attempt to bypass heuristic and signature-based detection methods [T1027.002].
Discovery
BianLian group actors use a combination of compiled tools, which they first download to the victim environment, to learn about the victim’s environment. BianLian group actors have used:
Advanced Port Scanner, a network scanner used to find open ports on network computers and retrieve versions of programs running on the detected ports [T1046].
SoftPerfect Network Scanner (netscan.exe), a network scanner that can ping computers, scan ports, and discover shared folders [T1135].
SharpShares to enumerate accessible network shares in a domain.
PingCastle to enumerate Active Directory (AD) [T1482].
PingCastle provides an AD map to visualize the hierarchy of trust relationships.
BianLian actors also use native Windows tools and Windows Command Shell to:
Query currently logged-in users [T1033].
Query the domain controller to identify:
All groups [T1069.002].
Accounts in the Domain Admins and Domain Computers groups [T1087.002].
All users in the domain.


### 3. AA23-319A:development:llama500:2651:5181

Offsets: 2651:5181; source tokens: 497; inherited context tokens: 15; preceding overlap: 0.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Inherited source context:

#StopRansomware: Rhysida Ransomware
Technical Details

Exact source window:


Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise, version 17. See the MITRE ATT&CK Tactics and Techniques section for tables mapped to the threat actors’ activity.
Threat actors leveraging Rhysida ransomware are known to impact “targets of opportunity,” including victims in the education, healthcare, manufacturing, information technology, and government sectors. Open source reporting details similarities between Vice Society (DEV-0832)[1] activity and the actors observed deploying Rhysida ransomware. Additionally, open source reporting[2] has confirmed observed instances of Rhysida actors operating in a ransomware-as-a-service (RaaS) capacity, where ransomware tools and infrastructure are leased out in a profit-sharing model. Any ransoms paid are then split between the group and the associates.
For additional information on Vice Society actors and associated activity, see the joint advisory #StopRansomware: Vice Society.
Initial Access
Rhysida actors have been observed leveraging external-facing remote services to initially access and persist within a network. Remote services, such as virtual private networks (VPNs), allow users to connect to internal enterprise network resources from external locations. Rhysida actors have commonly been observed authenticating to internal VPN access points with compromised valid credentials [T1078], notably due to organizations lacking MFA enabled by default.
Update April 30, 2025
Rhysida actors have also used Gootloader malware at times for initial access [TA0001].
Update End
Living off the Land
Analysis identified Rhysida actors using living off the land techniques, such as creating Remote Desktop Protocol (RDP) connections for lateral movement [T1021.001], establishing VPN access, and utilizing PowerShell [T1059.001]. Living off the land techniques include using native (built into the operating system) network administration tools to perform operations. This allows the actors to evade detection by blending in with normal Windows systems and network activities.
Ipconfig [T1016], whoami [T1033], nltest [T1482], and several net commands have been used to enumerate victim environments and gather information about domains. In one instance of using compromised credentials, actors leveraged net commands within PowerShell to identify logged-in users and perform reconnaissance on network accounts within the victim environment. Note: The following commands were not performed in the exact order listed.
net user [username] /domain [T1087.002]


### 4. AA23-319A:development:llama500:4860:7286

Offsets: 4860:7286; source tokens: 498; inherited context tokens: 15; preceding overlap: 60.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

Inherited source context:

#StopRansomware: Rhysida Ransomware
Technical Details

Exact source window:

. In one instance of using compromised credentials, actors leveraged net commands within PowerShell to identify logged-in users and perform reconnaissance on network accounts within the victim environment. Note: The following commands were not performed in the exact order listed.
net user [username] /domain [T1087.002]
net group “domain computers” /domain [T1018]
net group “domain admins” /domain [T1069.002]
net localgroup administrators [T1069.001]
Analysis of the master file table (MFT)[3] identified the victim system generated the ntuser.dat registry hive, which was created when the compromised user logged in to the system for the first time. This was considered anomalous due to the baseline of normal activity for the compromised user and system. Note: The MFT resides within the New Technology File System (NTFS) and houses information about a file including its size, time and date stamps, permissions, and data content.
Leveraged Tools
Table 1 lists legitimate tools Rhysida actors have repurposed for their operations. The legitimate tools listed in this joint advisory are all publicly available. Use of these tools should not be attributed as malicious without analytical evidence to support they are used at the direction of or controlled by threat actors.
Update April 30, 2025:
Recent techniques include leveraging AZCopy [T1059.009], a command-line utility that users leverage to copy blobs or files to, from, or between Azure storage accounts [T1530] and StorageExplorer-windows-x64.exe, a standalone application that allows users to manage and interact with their cloud storage.
Disclaimer: Organizations are encouraged to investigate and vet use of these tools prior to performing remediation actions.
Table 1: Tools Leveraged by Rhysida Actors
Name
Description
cmd.exe
The native command line prompt utility.
PowerShell.exe
A native command line tool used to start a Windows PowerShell session in a Command Prompt window.
powershell_ise.exe
Rhysida actors have been observed launching Windows PowerShell Integrated Scripting Environment (ISE) prior to executing a malicious script (1.ps1 from a folder in %AppData%\Local\Temp%). PowerShell ISE provides a graphical interface for editing and testing PowerShell scripts.
PsExec.exe
A tool included in the PsTools suite used to execute processes remotely. Rhysida actors heavily leveraged this tool for lateral movement and remote execution.
mstsc.exe


### 5. AA23-320A:development:llama500:2887:5261

Offsets: 2887:5261; source tokens: 502; inherited context tokens: 6; preceding overlap: 0.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Inherited source context:

Scattered Spider
Technical Details

Exact source window:


Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 17. See the MITRE ATT&CK Tactics and Techniques section of this advisory for tables of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Overview
Scattered Spider (also known as, UNC3944, Scatter Swine, Oktapus, Octo Tempest, Storm-0875, and Muddled Libra) engages in data extortion and several other criminal activities.[1] Scattered Spider threat actors use multiple social engineering techniques—including push bombing—and subscriber identity module (SIM) swap attacks, to obtain credentials, install remote access tools, and/or bypass multi-factor authentication (MFA). According to public reporting, Scattered Spider threat actors have:[2]
Posed as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees and gain access to the network [T1598] [T1656].
Posed as company IT and/or helpdesk staff to direct employees to run commercial remote access tools enabling initial access [T1204] [T1219] [T1566].
Posed as IT staff to convince employees to share their one-time password (OTP), an MFA authentication code.
Update July 29, 2025:
Posed as employees to convince IT and/or helpdesk staff to provide sensitive information, reset the employee’s password, and transfer the employee’s MFA to a device they control on separate devices.
Update End
Sent repeated MFA notification prompts leading to employees pressing the “Accept” button (also known as MFA fatigue) [T1621].[3]
Convinced cellular carriers to transfer control of a targeted user’s phone number to a SIM card in their possession, gaining control over the phone and access to MFA prompts.
Monetized access to targeted organization’s networks in numerous ways including extortion enabled by ransomware and data theft [T1657].
The FBI observed Scattered Spider threat actors, after gaining access to networks, using publicly available, legitimate remote access tunneling tools. Table 1 details a list of legitimate tools Scattered Spider repurposed and used for their criminal activity.
Note: The use of these legitimate tools alone is not indicative of malicious activity. Users should review the Scattered Spider IOCs and TTPs discussed in this advisory to determine whether they have been compromised.
Table 1: Legitimate Tools Used by Scattered Spider


### 6. AA23-320A:development:llama500:4957:7101

Offsets: 4957:7101; source tokens: 484; inherited context tokens: 6; preceding overlap: 60.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

Inherited source context:

Scattered Spider
Technical Details

Exact source window:

 used for their criminal activity.
Note: The use of these legitimate tools alone is not indicative of malicious activity. Users should review the Scattered Spider IOCs and TTPs discussed in this advisory to determine whether they have been compromised.
Table 1: Legitimate Tools Used by Scattered Spider
Tool
Intended Use
Fleetdeck.io
Enables remote monitoring and management of systems.
Level.io
Enables remote monitoring and management of systems.
Mimikatz [S0002]
Extracts credentials from a system.
Ngrok [S0508]
Enables remote access to a local web server by tunneling over the internet.
Pulseway
Enables remote monitoring and management of systems.
Screenconnect
Enables remote connections to network devices for management.
Splashtop
Enables remote connections to network devices for management.
Tactical.RMM
Enables remote monitoring and management of systems.
Tailscale
Provides virtual private networks (VPNs) to secure network communications.
TeamViewer
Enables remote connections to network devices for management.
Update July 29, 2025:
Teleport.sh
Enables remote access to a local system by tunneling over the internet.
AnyDesk
Enables remote access to network devices for management, bypassing security alerts due to AnyDesk being a legitimate application.
Teleport.sh
Enables remote access to a local system by tunneling over the internet.
Update End
In addition to using legitimate tools, Scattered Spider also uses malware as part of its TTPs. See Table 2 for some of the malware used by Scattered Spider.
Table 2: Malware Used by Scattered Spider
Malware
Use
AveMaria (also known as WarZone [S0670])
Enables remote access to a targeted organization’s systems.
Raccoon Stealer [S1148]
Steals information including login credentials [TA0006], browser history [T1217], cookies [T1539], and other data.
VIDAR Stealer
Steals information including login credentials, browser history, cookies, and other data.
Update July 29, 2025:
RattyRAT
Java-based remote access trojan, used for persistent, stealth access and internal reconnaissance.[4]
DragonForce Ransomware
Infiltrates networks, encrypts data, and demands ransom.
Update End


### 7. AA23-353A:development:llama500:3078:5323

Offsets: 3078:5323; source tokens: 490; inherited context tokens: 17; preceding overlap: 0.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Inherited source context:

#StopRansomware: ALPHV Blackcat
TECHNICAL DETAILS

Exact source window:


Note: This advisory uses the MITRE ATT&CK® for Enterprise framework, version 14. See the MITRE ATT&CK Tactics and Techniques section for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
ALPHV Blackcat affiliates use advanced social engineering techniques and open source research on a company to gain initial access. Actors pose as company IT and/or helpdesk staff and use phone calls or SMS messages [T1598] to obtain credentials from employees to access the target network [T1586]. ALPHV Blackcat affiliates use uniform resource locators (URLs) to live-chat with victims to convey demands and initiate processes to restore the victims’ encrypted files.
After gaining access to a victim network, ALPHV Blackcat affiliates deploy remote access software such as AnyDesk, Mega sync, and Splashtop in preparation of data exfiltration. ALPHV Blackcat affiliates create a user account, “aadmin,” and use Kerberos token generation for domain access [T1558]. After gaining access to networks, they use legitimate remote access and tunneling tools, such as Plink and Ngrok [S0508]. ALPHV Blackcat affiliates claim to use Brute Ratel C4 [S1063] and Cobalt Strike [S1054] as beacons to command and control servers. ALPHV Blackcat affiliates use the open source adversary-in-the-middle attack [T1557] framework Evilginx2, which allows them to obtain multifactor authentication (MFA) credentials, login credentials, and session cookies. The actors also obtain passwords from the domain controller, local network, and deleted backup servers to move laterally throughout the network [T1555].
To evade detection, affiliates employ allowlisted applications such as Metasploit. Once installed on the domain controller, the logs are cleared on the exchange server. Then Mega.nz or Dropbox are used to move, exfiltrate, and/or download victim data. The ransomware is then deployed, and the ransom note is embedded as a file.txt. According to public reporting, affiliates have additionally used POORTRY and STONESTOP to terminate security processes.


### 8. AA23-353A:development:llama500:5039:6758

Offsets: 5039:6758; source tokens: 496; inherited context tokens: 17; preceding overlap: 60.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Inherited source context:

#StopRansomware: ALPHV Blackcat
TECHNICAL DETAILS

Exact source window:

 Then Mega.nz or Dropbox are used to move, exfiltrate, and/or download victim data. The ransomware is then deployed, and the ransom note is embedded as a file.txt. According to public reporting, affiliates have additionally used POORTRY and STONESTOP to terminate security processes.
Some ALPHV Blackcat affiliates exfiltrate data after gaining access and extort victims without deploying ransomware. After exfiltrating and/or encrypting data, ALPHV Blackcat affiliates communicate with victims via TOR [S0183], Tox, email, or encrypted applications. The threat actors then delete victim data from the victim’s system.
ALPHV Blackcat affiliates offer to provide unsolicited cyber remediation advice as an incentive for payment, offering to provide victims with “vulnerability reports” and “security recommendations” detailing how they penetrated the system and how to prevent future re-victimization upon receipt of ransom payment. The ALPHV Blackcat encryptor results in a file with the following naming convention: RECOVER-(seven-digit extension) FILES.txt.
Figure 1: Ransom Note Instruction
INDICATORS OF COMPROMISE (IOCs)
Table 1: MD5 Hashes
MD5
Description
File Name
944153fb9692634d6c70899b83676575
ALPHV Windows Encryptor
341d43d4d5c2e526cadd88ae8da70c1c
Anti Virus Tools Killer
363.sys
34aac5719824e5f13b80d6fe23cbfa07
CobaltStrike BEACON
LMtool.exe
eea9ab1f36394769d65909f6ae81834b
CobaltStrike BEACON
Info.exe
379bf8c60b091974f856f08475a03b04
ALPHV Linux Encryptor
him
ebca4398e949286cb7f7f6c68c28e838
SimpleHelp Remote Management tool
first.exe
c04c386b945ccc04627d1a885b500edf
Tunneler Tool
conhost.exe
824d0e31fd08220a25c06baee1044818
Anti Virus Tools Killer
ibmModule.dll
eea9ab1f36394769d65909f6ae81834b


### 9. AA24-060A:development:llama500:2332:4570

Offsets: 2332:4570; source tokens: 488; inherited context tokens: 18; preceding overlap: 0.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Inherited source context:

#StopRansomware: Phobos Ransomware
TECHNICAL DETAILS

Exact source window:


Note: This advisory uses the MITRE ATT&CK for Enterprise framework, version 14. See the MITRE ATT&CK Tactics and Techniques section for a table of the threat actors’ activity mapped to MITRE ATT&CK® tactics and techniques. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Overview
According to open source reporting, Phobos ransomware is likely connected to numerous variants (including Elking, Eight, Devos, Backmydata, and Faust ransomware) due to similar TTPs observed in Phobos intrusions. Phobos ransomware operates in conjunction with various open source tools such as Smokeloader, Cobalt Strike, and Bloodhound. These tools are all widely accessible and easy to use in various operating environments, making it (and associated variants) a popular choice for many threat actors.[3],[4]
Reconnaissance and Initial Access
Phobos actors typically gain initial access to vulnerable networks by leveraging phishing campaigns [T1598] to drop hidden payloads or using internet protocol (IP) scanning tools, such as Angry IP Scanner, to search for vulnerable Remote Desktop Protocol (RDP) ports [T1595.001] or by leveraging RDP on Microsoft Windows environments.[5],[6]
Once they discover an exposed RDP service, the actors use open source brute force tools to gain access [T1110]. If Phobos actors gain successful RDP authentication [T1133][T1078] in the targeted environment, they perform open source research to create a victim profile and connect the targeted IP addresses to their associated companies [T1593]. Threat actors leveraging Phobos have notably deployed remote access tools to establish a remote connection within the compromised network [T1219].[7]
Alternatively, threat actors send spoofed email attachments [T1566.001] that are embedded with hidden payloads [T1204.002] such as SmokeLoader, a backdoor trojan that is often used in conjunction with Phobos. After SmokeLoader’s hidden payload is downloaded onto the victim’s system, threat actors use the malware’s functionality to download the Phobos payload and exfiltrate data from the compromised system.
Execution and Privilege Escalation


### 10. AA24-060A:development:llama500:4275:6493

Offsets: 4275:6493; source tokens: 465; inherited context tokens: 18; preceding overlap: 60.

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

Inherited source context:

#StopRansomware: Phobos Ransomware
TECHNICAL DETAILS

Exact source window:

door trojan that is often used in conjunction with Phobos. After SmokeLoader’s hidden payload is downloaded onto the victim’s system, threat actors use the malware’s functionality to download the Phobos payload and exfiltrate data from the compromised system.
Execution and Privilege Escalation
Phobos actors run executables like 1saas.exe or cmd.exe to deploy additional Phobos payloads that have elevated privileges enabled [TA0004]. Additionally, Phobos actors can use the previous commands to perform various windows shell functions. The Windows command shell enables threat actors to control various aspects of a system, with multiple permission levels required for different subsets of commands [T1059.003][T1105].[8]
Smokeloader Deployment
Phobos operations feature a standard three phase process to decrypt a payload that allows the threat actors to deploy additional destructive malware.[9]
For the first phase, Smokeloader manipulates either VirtualAlloc or VirtualProtect API functions—which opens an entry point, enabling code to be injected into running processes and allowing the malware to evade network defense tools [T1055.002]. In the second phase, a stealth process is used to obfuscate command and control (C2) activity by producing requests to legitimate websites [T1001.003].[10]
Within this phase, the shellcode also sends a call from the entry point to a memory container [T1055.004] and prepares a portable executable for deployment in the final stage [T1027.002][T1105][T1140].
Finally, once Smokeloader reaches its third stage, it unpacks a program-erase cycle from stored memory, which is then sent to be extracted from a SHA 256 hash as a payload.[7] Following successful payload decryption, the threat actors can begin downloading additional malware.
Additional Phobos Defense Evasion Capabilities
Phobos ransomware actors have been observed bypassing organizational network defense protocols by modifying system firewall configurations using commands like netsh firewall set opmode mode=disable [T1562.004]. Additionally, Phobos actors can evade detection by using the following tools: Universal Virus Sniffer, Process Hacker, and PowerTool [T1562].
Persistence and Privilege Escalation


Next: bounded source-only extraction of these ten windows, with candidate review, per-attempt timing, failures and overlap deduplication recorded. Index refresh and final benchmark evaluation remain pending.
