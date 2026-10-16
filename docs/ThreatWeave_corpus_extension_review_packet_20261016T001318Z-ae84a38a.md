# Remaining three-report candidates: offline review packet

Original model outputs and failures are preserved. Revalidated or derived candidates are not accepted graph facts.
Semantic source review and human verification remain pending. No model/service calls or graph writes.

## 01 · AA24-038A:development:llama500:6032:8859

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:


Note: This advisory uses the MITRE ATT&CK for Enterprise framework, version 14. See Appendix C: MITRE ATT&CK Tactics and Techniques section for tables of the Volt Typhoon cyber threat actors’ activity mapped to MITRE ATT&CK® tactics and techniques. For assistance with mapping malicious cyber activity to the MITRE ATT&CK framework, see CISA and MITRE ATT&CK’s Best Practices for MITRE ATT&CK Mapping and CISA’s Decider Tool.
Overview of Activity
In May 2023, the authoring agencies—working with industry partners—disclosed information about activity attributed to Volt Typhoon (see joint advisory People’s Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection). Since then, CISA, NSA, and FBI have determined that this activity is part of a broader campaign in which Volt Typhoon actors have successfully infiltrated the networks of critical infrastructure organizations in the continental and non-continental United States and its territories, including Guam.
The U.S. authoring agencies have primarily observed compromises linked to Volt Typhoon in Communications, Energy, Transportation Systems, and Water and Wastewater Systems sector organizations’ IT networks. Some victims are smaller organizations with limited cybersecurity capabilities that provide critical services to larger organizations or key geographic locations.
Volt Typhoon actors tailor their TTPs to the victim environment; however, the U.S. authoring agencies have observed the actors typically following the same pattern of behavior across identified intrusions. Their choice of targets and pattern of behavior is not consistent with traditional cyber espionage or intelligence gathering operations, and the U.S. authoring agencies assess with high confidence that Volt Typhoon actors are pre-positioning themselves on IT networks to enable the disruption of OT functions across multiple critical infrastructure sectors (see Figure 1).
Volt Typhoon conducts extensive pre-compromise reconnaissance to learn about the target organization’s network architecture and operational protocols. This reconnaissance includes identifying network topologies, security measures, typical user behaviors, and key network and IT staff. The intelligence gathered by Volt Typhoon actors is likely leveraged to enhance their operational security. For example, in some instances, Volt Typhoon actors may have abstained from using compromised credentials outside of normal working hours to avoid triggering security alerts on abnormal account activities.
Volt Typhoon typically gains initial access to the IT network by exploiting known or zero-day vulnerabilities in public-facing network appliances (e.g., routers, virtual private networks [VPNs], and firewalls) and then connects to the victim’s network via VPN for follow-on activities.


Empty model extraction; coverage review still required.

## 02 · AA24-038A:development:llama500:8540:11244

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 on abnormal account activities.
Volt Typhoon typically gains initial access to the IT network by exploiting known or zero-day vulnerabilities in public-facing network appliances (e.g., routers, virtual private networks [VPNs], and firewalls) and then connects to the victim’s network via VPN for follow-on activities.
Volt Typhoon aims to obtain administrator credentials within the network, often by exploiting privilege escalation vulnerabilities in the operating system or network services. In some cases, Volt Typhoon has obtained credentials insecurely stored on a public-facing network appliance.
Volt Typhoon uses valid administrator credentials to move laterally to the domain controller (DC) and other devices via remote access services such as Remote Desktop Protocol (RDP).
Volt Typhoon conducts discovery in the victim’s network, leveraging LOTL binaries for stealth. A key tactic includes using PowerShell to perform targeted queries on Windows event logs, focusing on specific users and periods. These queries facilitate the discreet extraction of security event logs into .dat files, allowing Volt Typhoon actors to gather critical information while minimizing detection. This strategy, blending in-depth pre-compromise reconnaissance with meticulous post-exploitation intelligence collection, underscores their sophisticated and strategic approach to cyber operations.
Volt Typhoon achieves full domain compromise by extracting the Active Directory database (NTDS.dit) from the DC. Volt Typhoon frequently employs the Volume Shadow Copy Service (VSS) using command-line utilities such as vssadmin to access NTDS.dit. The NTDS.dit file is a centralized repository that contains critical Active Directory data, including user accounts, passwords (in hashed form), and other sensitive data, which can be leveraged for further exploitation. This method entails the creation of a shadow copy—a point-in-time snapshot—of the volume hosting the NTDS.dit file. By leveraging this snapshot, Volt Typhoon actors effectively bypass the file locking mechanisms inherent in a live Windows environment, which typically prevent direct access to the NTDS.dit file while the domain controller is operational.
Volt Typhoon likely uses offline password cracking techniques to decipher these hashes. This process involves extracting the hashes from the NTDS.dit file and then applying various password cracking methods, such as brute force attacks, dictionary attacks, or more sophisticated techniques like rainbow tables to uncover the plaintext passwords. The successful decryption of these passwords allows Volt Typhoon actors to obtain elevated access and further infiltrate and manipulate the network.


### Candidate 0

Volt Typhoon actors -> USES -> NTDS.dit
Exact supporting span: By leveraging this snapshot, Volt Typhoon actors effectively bypass the file locking mechanisms inherent in a live Windows environment, which typically prevent direct access to the NTDS.dit file while the domain controller is operational.
Review flags: []

## 03 · AA24-038A:development:llama500:10885:13980

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 the NTDS.dit file and then applying various password cracking methods, such as brute force attacks, dictionary attacks, or more sophisticated techniques like rainbow tables to uncover the plaintext passwords. The successful decryption of these passwords allows Volt Typhoon actors to obtain elevated access and further infiltrate and manipulate the network.
Volt Typhoon uses elevated credentials for strategic network infiltration and additional discovery, often focusing on gaining capabilities to access OT assets. Volt Typhoon actors have been observed testing access to domain-joint OT assets using default OT vendor credentials, and in certain instances, they have possessed the capability to access OT systems whose credentials were compromised via NTDS.dit theft. This access enables potential disruptions, such as manipulating heating, ventilation, and air conditioning (HVAC) systems in server rooms or disrupting critical energy and water controls, leading to significant infrastructure failures (in some cases, Volt Typhoon actors had the capability to access camera surveillance systems at critical infrastructure facilities). In one confirmed compromise, Volt Typhoon actors moved laterally to a control system and were positioned to move to a second control system.
Figure 1: Typical Volt Typhoon Activity
After successfully gaining access to legitimate accounts, Volt Typhoon actors exhibit minimal activity within the compromised environment (except discovery as noted above), suggesting their objective is to maintain persistence rather than immediate exploitation. This assessment is supported by observed patterns where Volt Typhoon methodically re-targets the same organizations over extended periods, often spanning several years, to continuously validate and potentially enhance their unauthorized accesses. Evidence of their meticulous approach is seen in instances where they repeatedly exfiltrate domain credentials, ensuring access to current and valid accounts. For example, in one compromise, Volt Typhoon likely extracted NTDS.dit from three domain controllers in a four-year period. In another compromise, Volt Typhoon actors extracted NTDS.dit two times from a victim in a nine-month period.
Industry reporting—identifying that Volt Typhoon actors are silent on the network following credential dumping and perform discovery to learn about the environment, but do not exfiltrate data—is consistent with the U.S. authoring agencies’ observations. This indicates their aim is to achieve and maintain persistence on the network. In one confirmed compromise, an industry partner observed Volt Typhoon actors dumping credentials at regular intervals.
In addition to leveraging stolen account credentials, the actors use LOTL techniques and avoid leaving malware artifacts on systems that would cause alerts. Their strong focus on stealth and operational security allows them to maintain long-term, undiscovered persistence. Further, Volt Typhoon’s operational security is enhanced by targeted log deletion to conceal their actions within the compromised environment.


Empty model extraction; coverage review still required.

## 04 · AA24-038A:development:llama500:13617:16082

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 the actors use LOTL techniques and avoid leaving malware artifacts on systems that would cause alerts. Their strong focus on stealth and operational security allows them to maintain long-term, undiscovered persistence. Further, Volt Typhoon’s operational security is enhanced by targeted log deletion to conceal their actions within the compromised environment.
See the below sections for Volt Typhoon TTPs observed by the U.S. authoring agencies from multiple confirmed Volt Typhoon compromises.
Observed TTPs
Reconnaissance
Volt Typhoon actors conduct extensive pre-compromise reconnaissance [TA0043] to learn about the target organization [T1591], its network [T1590], and its staff [T1589]. This includes web searches [T1593]—including victim-owned sites [T1594]—for victim host [T1592], identity, and network information, especially for information on key network and IT administrators. According to industry reporting, Volt Typhoon actors use FOFA[1], Shodan, and Censys for querying or searching for exposed infrastructure. In some instances, the U.S. authoring agencies have observed Volt Typhoon actors targeting the personal emails of key network and IT staff [T1589.002] post compromise.
Resource Development
Historically, Volt Typhoon actors use multi-hop proxies for command and control (C2) infrastructure [T1090.003]. The proxy is typically composed of virtual private servers (VPSs) [T1583.003] or small office/home office (SOHO) routers. Recently, Volt Typhoon actors used Cisco and NETGEAR end-of-life SOHO routers implanted with KV Botnet malware to support their operations [T1584.005]. (See DOJ press release U.S. Government Disrupts Botnet People’s Republic of China Used to Conceal Hacking of Critical Infrastructure for more information).
Initial Access
To obtain initial access [TA0001], Volt Typhoon actors commonly exploit vulnerabilities in networking appliances such as those from Fortinet, Ivanti Connect Secure (formerly Pulse Secure), NETGEAR, Citrix, and Cisco [T1190]. They often use publicly available exploit code for known vulnerabilities [T1588.005] but are also adept at discovering and exploiting zero-day vulnerabilities [T1587.004].
In one confirmed compromise, Volt Typhoon actors likely obtained initial access by exploiting CVE-2022-42475 in a network perimeter FortiGate 300D firewall that was not patched. There is evidence of a buffer overflow attack identified within the Secure Sockets Layer (SSL)-VPN crash logs.


### Candidate 0

Volt Typhoon actors -> USES_TECHNIQUE -> T1591
Exact supporting span: Volt Typhoon actors conduct extensive pre-compromise reconnaissance [TA0043] to learn about the target organization [T1591]
Review flags: []

### Candidate 1

Volt Typhoon actors -> USES_TECHNIQUE -> T1589.002
Exact supporting span: In some instances, the U.S. authoring agencies have observed Volt Typhoon actors targeting the personal emails of key network and IT staff [T1589.002] post compromise.
Review flags: []

### Candidate 2

Volt Typhoon actors -> USES_TECHNIQUE -> T1090.003
Exact supporting span: Historically, Volt Typhoon actors use multi-hop proxies for command and control (C2) infrastructure [T1090.003].
Review flags: []

### Candidate 3

Volt Typhoon actors -> USES -> KV Botnet
Exact supporting span: Recently, Volt Typhoon actors used Cisco and NETGEAR end-of-life SOHO routers implanted with KV Botnet malware to support their operations [T1584.005]. (See DOJ press release U.S.
Review flags: []

## 05 · AA24-038A:development:llama500:15793:18394

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

In one confirmed compromise, Volt Typhoon actors likely obtained initial access by exploiting CVE-2022-42475 in a network perimeter FortiGate 300D firewall that was not patched. There is evidence of a buffer overflow attack identified within the Secure Sockets Layer (SSL)-VPN crash logs.
Once initial access is achieved, Volt Typhoon actors typically shift to establishing persistent access [TA0003]. They often use VPN sessions to securely connect to victim environments [T1133], enabling discreet follow-on intrusion activities. This tactic not only provides a stable foothold in the network but also allows them to blend in with regular traffic, significantly reducing their chances of detection.
Execution
Volt Typhoon actors rarely use malware for post-compromise execution. Instead, once Volt Typhoon actors gain access to target environments, they use hands-on-keyboard activity via the command-line [T1059] and other native tools and processes on systems [T1218] (often referred to as “LOLBins”), known as LOTL, to maintain and expand access to the victim networks. According to industry reporting, some “commands appear to be exploratory or experimental, as the operators [i.e., malicious actors] adjust and repeat them multiple times.”[2]
For more details on LOTL activity, see the Credential Access and Discovery sections and Appendix A: Volt Typhoon LOTL Activity.
Similar to LOTL, Volt Typhoon actors also use legitimate but outdated versions of network admin tools. For example, in one confirmed compromise, actors downloaded [T1105] an outdated version of comsvcs.dll on the DC in a non-standard folder. comsvcs.dll is a legitimate Microsoft Dynamic Link Library (DLL) file normally found in the System32 folder. The actors used this DLL with MiniDump and the process ID of the Local Security Authority Subsystem Service (LSASS) to dump the LSASS process memory [T1003.001] and obtain credentials (LSASS process memory space contains hashes for the current user’s operating system (OS) credentials).
The actors also use legitimate non-native network admin and forensic tools. For example, Volt Typhoon actors have been observed using Magnet RAM Capture (MRC) version 1.20 on domain controllers. MRC is a free imaging tool that captures the physical memory of a computer, and Volt Typhoon actors likely used it to analyze in-memory data for sensitive information (such as credentials) and in-transit data not typically accessible on disk. Volt Typhoon actors have also been observed implanting Fast Reverse Proxy (FRP) for command and control.[3] (See the Command and Control section).


### Candidate 0

Volt Typhoon actors -> USES_TECHNIQUE -> T1059
Exact supporting span: Instead, once Volt Typhoon actors gain access to target environments, they use hands-on-keyboard activity via the command-line [T1059] and other native tools and processes on systems [T1218] (often referred to as “LOLBins”), known as LOTL, to maintain and expand access to the victim networks.
Review flags: []

### Candidate 1

Volt Typhoon actors -> USES_TECHNIQUE -> T1218
Exact supporting span: Instead, once Volt Typhoon actors gain access to target environments, they use hands-on-keyboard activity via the command-line [T1059] and other native tools and processes on systems [T1218] (often referred to as “LOLBins”), known as LOTL, to maintain and expand access to the victim networks.
Review flags: []

### Candidate 2

comsvcs.dll -> USES_TECHNIQUE -> T1105
Exact supporting span: For example, in one confirmed compromise, actors downloaded [T1105] an outdated version of comsvcs.dll on the DC in a non-standard folder. comsvcs.dll is a legitimate Microsoft Dynamic Link Library (DLL) file normally found in the System32 folder.
Review flags: []

### Candidate 3

Volt Typhoon actors -> USES -> Magnet RAM Capture
Exact supporting span: For example, Volt Typhoon actors have been observed using Magnet RAM Capture (MRC) version 1.20 on domain controllers.
Review flags: []

## 06 · AA24-038A:development:llama500:18096:20499

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 actors likely used it to analyze in-memory data for sensitive information (such as credentials) and in-transit data not typically accessible on disk. Volt Typhoon actors have also been observed implanting Fast Reverse Proxy (FRP) for command and control.[3] (See the Command and Control section).
Persistence
Volt Typhoon primarily relies on valid credentials for persistence [T1078].
Defense Evasion
Volt Typhoon has strong operational security. Their actors primarily use LOTL for defense evasion [TA0005], which allows them to camouflage their malicious activity with typical system and network behavior, potentially circumventing simplistic endpoint security capabilities. For more information, see joint guide Identifying and Mitigating Living off the Land Techniques.
Volt Typhoon actors also obfuscate their malware. In one confirmed compromise, Volt Typhoon obfuscated FRP client files (BrightmetricAgent.exe and SMSvcService.exe) and the command-line port scanning utility ScanLine by packing the files with Ultimate Packer for Executables (UPX) [T1027.002]. FRP client applications support encryption, compression, and easy token authentication and work across multiple protocols—including transmission control protocol (TCP), user datagram protocol (UDP), hypertext transfer protocol (HTTP), and hypertext transfer protocol secure (HTTPS). The FRP client applications use the Kuai connection protocol (KCP) for error-checked and anonymous data stream delivery over UDP, with packet-level encryption support. See Appendix C and CISA Malware Analysis Report (MAR)-10448362-1.v1 for more information.
In addition to LOTL and obfuscation techniques, Volt Typhoon actors have been observed selectively clearing Windows Event Logs [T1070.001], system logs, and other technical artifacts to remove evidence [T1070.009] of their intrusion activity and masquerading file names [T1036.005].
Credential Access
Volt Typhoon actors first obtain credentials from public-facing appliances after gaining initial access by exploiting privilege escalation vulnerabilities [T1068] in the operating system or network services. In some cases, they have obtained credentials insecurely stored on the appliance [T1552]. In one instance, where Volt Typhoon likely exploited CVE-2022-42475 in an unpatched Fortinet device, Volt Typhoon actors compromised a domain admin account stored inappropriately on the device.


### Candidate 0

Volt Typhoon actors -> USES -> FRP
Exact supporting span: Volt Typhoon actors have also been observed implanting Fast Reverse Proxy (FRP) for command and control.[3] (See the Command and Control section).
Review flags: []

### Candidate 1

FRP -> USES_TECHNIQUE -> T1027.002
Exact supporting span: In one confirmed compromise, Volt Typhoon obfuscated FRP client files (BrightmetricAgent.exe and SMSvcService.exe) and the command-line port scanning utility ScanLine by packing the files with Ultimate Packer for Executables (UPX) [T1027.002].
Review flags: []

### Candidate 2

Volt Typhoon actors -> USES_TECHNIQUE -> T1068
Exact supporting span: Volt Typhoon actors first obtain credentials from public-facing appliances after gaining initial access by exploiting privilege escalation vulnerabilities [T1068] in the operating system or network services.
Review flags: []

## 07 · AA24-038A:development:llama500:20222:22508

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 cases, they have obtained credentials insecurely stored on the appliance [T1552]. In one instance, where Volt Typhoon likely exploited CVE-2022-42475 in an unpatched Fortinet device, Volt Typhoon actors compromised a domain admin account stored inappropriately on the device.
Volt Typhoon also consistently obtains valid credentials by extracting the Active Directory database file (NTDS.dit)—in some cases multiple times from the same victim over long periods [T1003.003]. NTDS.dit contains usernames, hashed passwords, and group memberships for all domain accounts, essentially allowing for full domain compromise if the hashes can be cracked offline.
To obtain NTDS.dit, the U.S. authoring agencies have observed Volt Typhoon:
Move laterally [TA0008] to the domain controller via an interactive RDP session using a compromised account with domain administrator privileges [T1021.001];
Execute the Windows-native vssadmin [T1006] command to create a volume shadow copy;
Use Windows Management Instrumentation Console (WMIC) commands [T1047] to execute ntdsutil (a LOTL utility) to copy NTDS.dit and SYSTEM registry hive from the volume shadow copy; and
Exfiltrate [TA0010] NTDS.dit and SYSTEM registry hive to crack passwords offline) [T1110.002]. (For more details, including specific commands used, see Appendix A: Volt Typhoon LOTL Activity.)
Note: A volume shadow copy contains a copy of all the files and folders that exist on the specified volume. Each volume shadow copy created on a DC includes its NTDS.dit and the SYSTEM registry hive, which provides keys to decrypt the NTDS.dit file.
Volt Typhoon actors have also been observed interacting with a PuTTY application by enumerating existing stored sessions [T1012]. Given this interaction and the exposure of cleartext-stored proxy passwords used in remote administration, Volt Typhoon actors potentially had access to PuTTY profiles that allow access to critical systems (see the Lateral Movement section).
According to industry reporting, Volt Typhoon actors attempted to dump credentials through LSASS (see Appendix B for commands used).[2]
The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]


### Candidate 0

T1021.001 -> PART_OF_TACTIC -> TA0008
Exact supporting span: Move laterally [TA0008] to the domain controller via an interactive RDP session using a compromised account with domain administrator privileges [T1021.001];
Review flags: []

### Candidate 1

LOTL -> USES_TECHNIQUE -> T1047
Exact supporting span: Use Windows Management Instrumentation Console (WMIC) commands [T1047] to execute ntdsutil (a LOTL utility) to copy NTDS.dit and SYSTEM registry hive from the volume shadow copy; and
Review flags: []

### Candidate 2

LOTL -> USES_TECHNIQUE -> T1110.002
Exact supporting span: Exfiltrate [TA0010] NTDS.dit and SYSTEM registry hive to crack passwords offline) [T1110.002]. (For more details, including specific commands used, see Appendix A: Volt Typhoon LOTL Activity.)
Review flags: []

### Candidate 3

Volt Typhoon actors -> USES -> PuTTY
Exact supporting span: Volt Typhoon actors have also been observed interacting with a PuTTY application by enumerating existing stored sessions [T1012].
Review flags: []

## 08 · AA24-038A:development:llama500:22202:24566

Original status: validation_failed
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Original validation error: Repeated selected relationship.

Exact source window:

 to industry reporting, Volt Typhoon actors attempted to dump credentials through LSASS (see Appendix B for commands used).[2]
The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]
Mimikatz is a credential dumping tool and Volt Typhoon actors use it to obtain credentials. In one confirmed compromise, the Volt Typhoon used RDP to connect to a server and run Mimikatz after leveraging a compromised administrator account to deploy it.
Impacket is an open source Python toolkit for programmatically constructing and manipulating network protocols. It contains tools for Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks—as well as remote service execution.
Discovery
Volt Typhoon actors have been observed using commercial tools, LOTL utilities, and appliances already present on the system for system information [T1082], network service [T1046], group [T1069] and user [T1033] discovery.
Volt Typhoon uses at least the following LOTL tools and commands for system information, network service, group, and user discovery techniques:
cmd
certutil
dnscmd
ldifde
makecab
net user/group/use
netsh
nltest
netstat
ntdsutil
ping
PowerShell
quser
reg query/reg save
systeminfo
tasklist
wevtutil
whoami
wmic
xcopy
Some observed specific examples of discovery include:
Capturing successful logon events [T1654].
Specifically, in one incident, analysis of the PowerShell console history of a domain controller indicated that security event logs were directed to a file named user.dat, as evidenced by the executed command Get-EventLog security -instanceid 4624 -after [year-month-date] | fl * | Out-File 'C:\users\public\documents\user.dat'. This indicates the group's specific interest in capturing successful logon events (event ID 4624) to analyze user authentication patterns within the network. Additionally, file system analysis, specifically of the Master File Table (MFT), uncovered evidence of a separate file, systeminfo.dat, which was created in C:\Users\Public\Documents but subsequently deleted [T1070.004]. The presence of these activities suggests a methodical approach by Volt Typhoon actors in collecting and then possibly removing traces of sensitive log information from the compromised system.


### Candidate 0

Volt Typhoon actors -> USES -> Mimikatz
Exact supporting span: The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]
Review flags: []

### Candidate 1

Volt Typhoon actors -> USES_TECHNIQUE -> T1082
Exact supporting span: Volt Typhoon actors have been observed using commercial tools, LOTL utilities, and appliances already present on the system for system information [T1082]
Review flags: []

### Candidate 2

systeminfo -> USES_TECHNIQUE -> T1070.004
Exact supporting span: Additionally, file system analysis, specifically of the Master File Table (MFT), uncovered evidence of a separate file, systeminfo.dat, which was created in C:\Users\Public\Documents but subsequently deleted [T1070.004].
Review flags: []

## 09 · AA24-038A:development:llama500:24254:26777

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 a separate file, systeminfo.dat, which was created in C:\Users\Public\Documents but subsequently deleted [T1070.004]. The presence of these activities suggests a methodical approach by Volt Typhoon actors in collecting and then possibly removing traces of sensitive log information from the compromised system.
Executing tasklist /v to gather a detailed process listing [T1057], followed by executing taskkill /f /im rdpservice.exe (the function of this executable is not known).
Executing net user and quser for user account information [T1087.001].
Creating and accessing a file named rult3uil.log on a domain controller in C:\Windows\System32\. The rult3uil.log file contained user activities on a compromised system, showcasing a combination of window title information [T1010] and focus shifts, keypresses, and command executions across Google Chrome and Windows PowerShell, with corresponding timestamps.
Employing ping with various IP addresses to check network connectivity [T1016.001] and net start to list running services [T1007].
See Appendix A for additional LOTL examples.
In one confirmed compromise, Volt Typhoon actors attempted to use Advanced IP Scanner, which was on the network for admin use, to scan the network.
Volt Typhoon actors have been observed strategically targeting network administrator web browser data—focusing on both browsing history and stored credentials [T1555.003]—to facilitate targeting of personal email addresses (see the Reconnaissance section) for further discovery and possible network modifications that may impact the threat actor’s persistence within victim networks.
In one confirmed compromise:
Volt Typhoon actors obtained the history file from the User Data directory of a network administrator user’s Chrome browser. To obtain the history file, Volt Typhoon actors first executed an RDP session to the user’s workstation where they initially attempted, and failed, to obtain the C$ File Name: users\{redacted}\appdata\local\Google\Chrome\UserData\default\History file, as evidenced by the accompanying 1016 (reopen failed) SMB error listed in the application event log. The threat actors then disconnected the RDP session to the workstation and accessed the file C:\Users\{redacted}\Downloads\History.zip. This file presumably contained data from the User Data directory of the user’s Chrome browser, which the actors likely saved in the Downloads directory for exfiltration [T1074]. Shortly after accessing the history.zip file, the actors terminated RDP sessions.


### Candidate 0

systeminfo -> USES_TECHNIQUE -> T1070.004
Exact supporting span: a separate file, systeminfo.dat, which was created in C:\Users\Public\Documents but subsequently deleted [T1070.004].
Review flags: []

### Candidate 1

tasklist -> USES_TECHNIQUE -> T1057
Exact supporting span: Executing tasklist /v to gather a detailed process listing [T1057]
Review flags: []

### Candidate 2

ping -> USES_TECHNIQUE -> T1016.001
Exact supporting span: Employing ping with various IP addresses to check network connectivity [T1016.001] and net start to list running services [T1007].
Review flags: []

### Candidate 3

Volt Typhoon actors -> USES -> Advanced IP Scanner
Exact supporting span: In one confirmed compromise, Volt Typhoon actors attempted to use Advanced IP Scanner, which was on the network for admin use, to scan the network.
Review flags: []

## 10 · AA24-038A:development:llama500:26482:28837

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

\{redacted}\Downloads\History.zip. This file presumably contained data from the User Data directory of the user’s Chrome browser, which the actors likely saved in the Downloads directory for exfiltration [T1074]. Shortly after accessing the history.zip file, the actors terminated RDP sessions.
About four months later, Volt Typhoon actors accessed the same user’s Chrome data C$ File Name: Users\{redacted}\AppData\Local\Google\Chrome\User Data\Local State and $ File Name: Users\{redacted}\AppData\Local\Google\Chrome\User Data\Default\Login Data via SMB. The Local State file contains the Advanced Encryption Standard (AES) encryption key [T1552.004] used to encrypt the passwords stored in the Chrome browser, which would enable the actors to obtain plaintext passwords stored in the Login Data file in the Chrome browser.
In another confirmed compromise, Volt Typhoon actors accessed directories containing Chrome and Edge user data on multiple systems. Directory interaction was observed over the network to paths such as C:\Users\{redacted}\AppData\Local\Google\Chrome\User Data\ and C:\Users\{redacted}\AppData\Local\Microsoft\Edge\User Data\. They also enumerated several directories, including directories containing vulnerability testing and cyber related content and facilities data, such as construction drawings [T1083].
Lateral Movement
For lateral movement, Volt Typhoon actors have been observed predominantly employing RDP with compromised valid administrator credentials. Note: With a full on-premises Microsoft Active Directory identity compromise (see the Credential Access section), the group may be capable of using other methods such as Pass the Hash or Pass the Ticket for lateral movement [T1550].
In one confirmed compromise of a Water and Wastewater Systems Sector entity, after obtaining initial access, Volt Typhoon actors connected to the network via a VPN with administrator credentials they obtained and opened an RDP session with the same credentials to move laterally. Over a nine-month period, they moved laterally to a file server, a domain controller, an Oracle Management Server (OMS), and a VMware vCenter server. The actors obtained domain credentials from the domain controller and performed discovery, collection, and exfiltration on the file server (see the Discovery and Collection and Exfiltration sections).


Empty model extraction; coverage review still required.

## 11 · AA24-038A:development:llama500:28528:31303

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

ally to a file server, a domain controller, an Oracle Management Server (OMS), and a VMware vCenter server. The actors obtained domain credentials from the domain controller and performed discovery, collection, and exfiltration on the file server (see the Discovery and Collection and Exfiltration sections).
Volt Typhoon’s movement to the vCenter server was likely strategic for pre-positioning to OT assets. The vCenter server was adjacent to OT assets, and Volt Typhoon actors were observed interacting with the PuTTY application on the server by enumerating existing stored sessions. With this information, Volt Typhoon potentially had access to a range of critical PuTTY profiles, including those for water treatment plants, water wells, an electrical substation, OT systems, and network security devices. This would enable them to access these critical systems [T1563]. See Figure 2.
Figure 2: Volt Typhoon Lateral Movement Path File Server, DC, and OT-Adjacent Assets
Additionally, Volt Typhoon actors have been observed using PSExec to execute remote processes, including the automated acceptance of the end-user license agreement (EULA) through an administrative account, signified by the accepteula command flag.
Volt Typhoon actors may have attempted to move laterally to a cloud environment in one victim’s network but direct attribution to the Volt Typhoon group was inconclusive. During the period of the their known network presence, there were anomalous login attempts to an Azure tenant [T1021.007] potentially using credentials [T1078.004] previously compromised from theft of NTDS.dit. These attempts, coupled with misconfigured virtual machines with open RDP ports, suggested a potential for cloud-based lateral movement. However, subsequent investigations, including password changes and multifactor authentication (MFA) implementations, revealed authentication failures from non-associated IP addresses, with no definitive link to Volt Typhoon.
Collection and Exfiltration
The U.S. authoring agencies assess Volt Typhoon primarily collects information that would facilitate follow-on actions with physical impacts. For example, in one confirmed compromise, they collected [TA0009] sensitive information obtained from a file server in multiple zipped files [T1560] and likely exfiltrated [TA0010] the files via Server Message Block (SMB) [T1048] (see Figure 3). Collected information included diagrams and documentation related to OT equipment, including supervisory control and data acquisition (SCADA) systems, relays, and switchgear. This data is crucial for understanding and potentially impacting critical infrastructure systems, indicating a focus on gathering intelligence that could be leveraged in actions targeting physical assets and systems.


### Candidate 0

Volt Typhoon actors -> USES -> PuTTY
Exact supporting span: The vCenter server was adjacent to OT assets, and Volt Typhoon actors were observed interacting with the PuTTY application on the server by enumerating existing stored sessions.
Review flags: []

### Candidate 1

Volt Typhoon actors -> USES -> PSExec
Exact supporting span: Additionally, Volt Typhoon actors have been observed using PSExec to execute remote processes, including the automated acceptance of the end-user license agreement (EULA) through an administrative account, signified by the accepteula command flag.
Review flags: []

### Candidate 2

T1560 -> PART_OF_TACTIC -> TA0009
Exact supporting span: For example, in one confirmed compromise, they collected [TA0009] sensitive information obtained from a file server in multiple zipped files [T1560] and likely exfiltrated [TA0010] the files via Server Message Block (SMB) [T1048] (see Figure 3).
Review flags: ["source_uncertainty_wording"]

### Candidate 3

T1048 -> PART_OF_TACTIC -> TA0010
Exact supporting span: For example, in one confirmed compromise, they collected [TA0009] sensitive information obtained from a file server in multiple zipped files [T1560] and likely exfiltrated [TA0010] the files via Server Message Block (SMB) [T1048] (see Figure 3).
Review flags: ["source_uncertainty_wording"]

## 12 · AA24-038A:development:llama500:30941:33296

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 diagrams and documentation related to OT equipment, including supervisory control and data acquisition (SCADA) systems, relays, and switchgear. This data is crucial for understanding and potentially impacting critical infrastructure systems, indicating a focus on gathering intelligence that could be leveraged in actions targeting physical assets and systems.
Figure 3: Volt Typhoon Attack Path for Exfiltration of Data from File Server
In another compromise, Volt Typhoon actors leveraged WMIC to create and use temporary directories (C:\Users\Public\pro, C:\Windows\Temp\tmp, C:\Windows\Temp\tmp\Active Directory and C:\Windows\Temp\tmp\registry) to stage the extracted ntds.dit and SYSTEM registry hives from ntdsutil execution volume shadow copies (see the Credential Access section) obtained from two DCs. They then compressed and archived the extracted ntds.dit and accompanying registry files by executing ronf.exe, which was likely a renamed version of the archive utility rar.exe) [T1560.001].
Command and Control
Volt Typhoon actors have been observed leveraging compromised SOHO routers and virtual private servers (VPS) to proxy C2 traffic. For more information, see DOJ press release U.S. Government Disrupts Botnet People’s Republic of China Used to Conceal Hacking of Critical Infrastructure).
They have also been observed setting up FRP clients [T1090] on a victim’s corporate infrastructure to establish covert communications channels [T1573] for command and control. In one instance, Volt Typhoon actors implanted the FRP client with filename SMSvcService.exe on a Shortel Enterprise Contact Center (ECC) server and a second FRP client with filename Brightmetricagent.exe on another server. These clients, when executed via PowerShell [T1059.001], open reverse proxies between the compromised system and Volt Typhoon C2 servers. Brightmetricagent.exe has additional capabilities. The FRP client can locate servers behind a network firewall or obscured through Network Address Translation (NAT) [T1016]. It also contains multiplexer libraries that can bi-directionally stream data over NAT networks and contains a command-line interface (CLI) library that can leverage command shells such as PowerShell, Windows Management Instrumentation (WMI), and Z Shell (zsh) [T1059.004]. See Appendix C and MAR-10448362-1.v1 for more information.


### Candidate 0

ronf.exe -> USES_TECHNIQUE -> T1560.001
Exact supporting span: They then compressed and archived the extracted ntds.dit and accompanying registry files by executing ronf.exe, which was likely a renamed version of the archive utility rar.exe) [T1560.001].
Review flags: ["source_uncertainty_wording"]

### Candidate 1

FRP -> USES_TECHNIQUE -> T1090
Exact supporting span: They have also been observed setting up FRP clients [T1090] on a victim’s corporate infrastructure to establish covert communications channels [T1573] for command and control.
Review flags: []

### Candidate 2

Volt Typhoon actors -> USES -> FRP
Exact supporting span: In one instance, Volt Typhoon actors implanted the FRP client with filename SMSvcService.exe on a Shortel Enterprise Contact Center (ECC) server and a second FRP client with filename Brightmetricagent.exe on another server.
Review flags: []

### Candidate 3

Volt Typhoon actors -> USES_TECHNIQUE -> T1560.001
Exact supporting span: In another compromise, Volt Typhoon actors leveraged WMIC to create and use temporary directories (C:\Users\Public\pro, C:\Windows\Temp\tmp, C:\Windows\Temp\tmp\Active Directory and C:\Windows\Temp\tmp\registry) to stage the extracted ntds.dit and SYSTEM registry hives from ntdsutil execution volume shadow copies (see the Credential Access section) obtained from two DCs. They then compressed and archived the extracted ntds.dit and accompanying registry files by executing ronf.exe, which was likely a renamed version of the archive utility rar.exe) [T1560.001].
Review flags: ["source_uncertainty_wording"]

## 13 · AA24-038A:development:llama500:33045:35669

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 NAT networks and contains a command-line interface (CLI) library that can leverage command shells such as PowerShell, Windows Management Instrumentation (WMI), and Z Shell (zsh) [T1059.004]. See Appendix C and MAR-10448362-1.v1 for more information.
In the same compromise, Volt Typhoon actors exploited a Paessler Router Traffic Grapher (PRTG) server as an intermediary for their FRP operations. To facilitate this, they used the netsh command, a legitimate Windows command, to create a PortProxy registry modification [T1112] on the PRTG server [T1090.001]. This key alteration redirected specific port traffic to Volt Typhoon’s proxy infrastructure, effectively converting the PRTG’s server into a proxy for their C2 traffic [T1584.004] (see Appendix B for details).
DETECTION/HUNT RECOMMENDATIONS
Apply Living off the Land Detection Best Practices
Apply the prioritized detection and hardening best practice recommendations provided in joint guide Identifying and Mitigating Living off the Land Techniques. Many organizations lack security and network management best practices (such as established baselines) that support detection of malicious LOTL activity—this makes it difficult for network defenders to discern legitimate behavior from malicious behavior and conduct behavior analytics, anomaly detection, and proactive hunting. Conventional IOCs associated with the malicious activity are generally lacking, complicating network defenders’ efforts to identify, track, and categorize this sort of malicious behavior. This advisory provides guidance for a multifaceted cybersecurity strategy that enables behavior analytics, anomaly detection, and proactive hunting, which are part of a comprehensive approach to mitigating cyber threats that employ LOTL techniques.
Review Application, Security, and System Event Logs
Routinely review application, security, and system event logs, focusing on Windows Extensible Storage Engine Technology (ESENT) Application Logs. Due to Volt Typhoon’s ability for long-term undetected persistence, network defenders should assume significant dwell time and review specific application event log IDs, which remain on endpoints for longer periods compared to security event logs and other ephemeral artifacts. Focus on Windows ESENT logs because certain ESENT Application Log event IDs (216, 325, 326, and 327) may indicate actors copying NTDS.dit.
See Table 1 for examples of ESENT and other key log indicators that should be investigated. Please note that incidents may not always have exact matches listed in the Event Detail column due to variations in event logging and TTPs.


### Candidate 0

Volt Typhoon actors -> USES -> FRP
Exact supporting span: In the same compromise, Volt Typhoon actors exploited a Paessler Router Traffic Grapher (PRTG) server as an intermediary for their FRP operations.
Review flags: []

### Candidate 1

netsh -> USES_TECHNIQUE -> T1112
Exact supporting span: To facilitate this, they used the netsh command, a legitimate Windows command, to create a PortProxy registry modification [T1112] on the PRTG server [T1090.001].
Review flags: []

### Candidate 2

netsh -> USES_TECHNIQUE -> T1090.001
Exact supporting span: To facilitate this, they used the netsh command, a legitimate Windows command, to create a PortProxy registry modification [T1112] on the PRTG server [T1090.001].
Review flags: []

## 14 · AA24-038A:development:llama500:35388:37325

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

, and 327) may indicate actors copying NTDS.dit.
See Table 1 for examples of ESENT and other key log indicators that should be investigated. Please note that incidents may not always have exact matches listed in the Event Detail column due to variations in event logging and TTPs.
Table 1: Key Log Indicators for Detecting Volt Typhoon Activity
Event ID (Log)
Event Detail
Description
216 (Windows ESENT Application Log)
A database location change was detected from 'C:\Windows\NTDS\ntds.dit' to '\\?\GLOBALROOT\Device\{redacted}VolumeShadowCopy1\Windows\NTDS\ntds.dit'
A change in the NTDS.dit database location is detected. This could suggest an initial step in NTDS credential dumping where the database is being prepared for extraction.
325 (Windows ESENT Application Log)
The database engine created a new database (2, C:\Windows\Temp\tmp\Active Directory\ntds.dit).
Indicates creation of a new NTDS.dit file in a non-standard directory. Often a sign of data staging for exfiltration. Monitor for unusual database operations in temp directories.
637 (Windows ESENT Application Log)
C:\Windows\Temp\tmp\Active Directory\ntds.jfm-++- (0) New flush map file “C:\Windows\Temp\tmp\Active Directory\ntds.jfm” will be created to enable persisted lost flush detection.
A new flush map file is being created for NTDS.dit. This may suggest ongoing operations related to NTDS credential dumping, potentially capturing uncommitted changes to the NTDS.dit file.
326 (Windows ESENT Application Log)
NTDS-++-12460,D,100-++--++-1-++-
C:\$SNAP_{redacted}_VOLUMEC$\Windows\NTDS\ntds.dit-++-0-++- [1] The database engine attached a database. Began mounting of C:\Windows\NTDS\ntds.dit file created from volume shadow copy process
Represents the mounting of an NTDS.dit file from a volume shadow copy. This is a critical step in NTDS credential dumping, indicating active manipulation of a domain controller’s data.
327 (Windows ESENT Application Log)


Empty model extraction; coverage review still required.

## 15 · AA24-038A:development:llama500:37047:39344

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

DS\ntds.dit file created from volume shadow copy process
Represents the mounting of an NTDS.dit file from a volume shadow copy. This is a critical step in NTDS credential dumping, indicating active manipulation of a domain controller’s data.
327 (Windows ESENT Application Log)
C:\Windows\Temp\tmp\Active Directory\ntds.dit-++-1-++- [1] The database engine detached a database (2, C:\Windows\Temp\tmp\Active Directory\ntds.dit). Completion of mounting of ntds.dit file to C:\Windows\Temp\tmp\Active Director
The detachment of a database, particularly in a temp directory, could indicate the completion of a credential dumping process, potentially as part of exfiltration preparations.
21 (Windows Terminal Services Local Session Manager Operational Log)
Remote Desktop Services: Session logon succeeded: User: {redacted}\{redacted} Session ID: {redacted} Source Network Address: {redacted}
Successful authentication to a Remote Desktop Services session.
22 (Windows Terminal Services Local Session Manager Operational Log)
Remote Desktop Services: Shell start notification received: User: {redacted}\{redacted} Session ID: {redacted} Source Network Address: {redacted}
Successful start of a new Remote Desktop session. This may imply lateral movement or unauthorized remote access, especially if the user or session is unexpected.
23 (Windows Terminal Services Local Session Manager Operational Log)
Remote Desktop Services: Session logoff succeeded: User: {redacted}\{redacted} Session ID: {redacted}
Successful logoff of Remote Desktop session.
24 (Windows Terminal Services Local Session Manager Operational Log)
Remote Desktop Services: Session has been disconnected: User: {redacted}\{redacted} Session ID: {redacted} Source Network Address: {redacted}
Remote Desktop session disconnected by user or due to network connectivity issues.
25 (Windows Terminal Services Local Session Manager Operational Log)
Remote Desktop Services: Session reconnection succeeded: User: {redacted}\{redacted} Session ID: {redacted} Source Network Address: {redacted}
Successful reconnection to a Remote Desktop Services session. This may imply lateral movement or unauthorized remote access, especially if the user or session is unexpected.
1017 (Windows System Log)
Handle scavenged.
Share Name: C$
File Name:


Empty model extraction; coverage review still required.

## 16 · AA24-038A:development:llama500:39055:41394

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

redacted} Source Network Address: {redacted}
Successful reconnection to a Remote Desktop Services session. This may imply lateral movement or unauthorized remote access, especially if the user or session is unexpected.
1017 (Windows System Log)
Handle scavenged.
Share Name: C$
File Name:
users\{redacted}\downloads\History.zip Durable: 1 Resilient or Persistent: 0 Guidance: The server closed a handle that was previously reserved for a client after 60 seconds.
Indicates the server closed a handle for a client. While common in network operations, unusual patterns or locations (like History.zip in a user’s downloads) may suggest data collection from a local system.
1102 (Windows Security Log)
All
All Event ID 1102 entries should be investigated as logs are generally not cleared and this is a known Volt Typhoon tactic to cover their tracks.
Monitor and Review OT System Logs
Review access logs for communication paths between IT and OT networks, looking for anomalous accesses or protocols.
Measure the baseline of normal operations and network traffic for the industrial control system (ICS) and assess traffic anomalies for malicious activity.
Configure intrusion detection systems (IDS) to create alarms for any ICS network traffic outside normal operations.
Track and monitor audit trails on critical areas of ICS.
Set up security incident and event monitoring (SIEM) to monitor, analyze, and correlate event logs from across the ICS network to identify intrusion attempts.
Review CISA’s Recommended Cybersecurity Practices for Industrial Control Systems and the joint advisory, NSA and CISA Recommend Immediate Actions to Reduce Exposure Across all Operational Technologies and Control Systems, for further OT system detection and mitigation guidance.
Use gait to Detect Possible Network Proxy Activities
Use gait[4] to detect network proxy activities. Developed by Sandia National Labs, gait is a publicly available Zeek[5] extension. The gait extension can help enrich Zeek’s network connection monitoring and SSL logs by including additional metadata in the logs. Specifically, gait captures unique TCP options and timing data such as a TCP, transport layer security (TLS), and Secure Shell (SSH) layer inferred round trip times (RTT), aiding in the identification of the software used by both endpoints and intermediaries.


Empty model extraction; coverage review still required.

## 17 · AA24-038A:development:llama500:41087:43719

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 by including additional metadata in the logs. Specifically, gait captures unique TCP options and timing data such as a TCP, transport layer security (TLS), and Secure Shell (SSH) layer inferred round trip times (RTT), aiding in the identification of the software used by both endpoints and intermediaries.
While the gait extension for Zeek is an effective tool for enriching network monitoring logs with detailed metadata, it is not specifically designed to detect Volt Typhoon actor activities. The extension’s capabilities extend to general anomaly detection in network traffic, including—but not limited to—proxying activities. Therefore, while gait can be helpful in identifying tactics similar to those used by Volt Typhoon, such as proxy networks and FRP clients for C2 communication, not all proxying activities detected by using this additional metadata are necessarily indicative of Volt Typhoon presence. It serves as a valuable augmentation to current security stacks for a broader spectrum of threat detection.
For more information, see Sandia National Lab’s gait GitHub page sandialabs/gait: Zeek Extension to Collect Metadata for Profiling of Endpoints and Proxies.
Review Logins for Impossible Travel
Examine VPN or other account logon times, frequency, duration, and locations. Logons from two geographically distant locations within a short timeframe from a single user may indicate an account is being used maliciously. Logons of unusual frequency or duration may indicate a threat actor attempting to access a system repeatedly or maintain prolonged sessions for the purpose of data extraction.
Review Standard Directories for Unusual Files
Review directories, such as C:\windows\temp\ and C:\users\public\, for unexpected or unusual files. Monitor these temporary file storage directories for files typically located in standard system paths, such as the System32 directory. For example, Volt Typhoon has been observed downloading comsvcs.dll to a non-standard folder (this file is normally found in the System32 folder).
INCIDENT RESPONSE
If compromise, or potential compromise, is detected, organizations should assume full domain compromise because of Volt Typhoon’s known behavioral pattern of extracting the NTDS.dit from the DCs. Organizations should immediately implement the following immediate, defensive countermeasures:
Sever the enterprise network from the internet. Note: this step requires the agency to understand its internal and external connections. When making the decision to sever internet access, knowledge of connections must be combined with care to avoid disrupting critical functions.


### Candidate 0

Volt Typhoon -> USES -> FRP
Exact supporting span: Therefore, while gait can be helpful in identifying tactics similar to those used by Volt Typhoon, such as proxy networks and FRP clients for C2 communication, not all proxying activities detected by using this additional metadata are necessarily indicative of Volt Typhoon presence.
Review flags: []

### Candidate 1

Volt Typhoon -> USES -> comsvcs.dll
Exact supporting span: For example, Volt Typhoon has been observed downloading comsvcs.dll to a non-standard folder (this file is normally found in the System32 folder).
Review flags: []

## 18 · AA24-038A:development:llama500:43343:46216

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 Organizations should immediately implement the following immediate, defensive countermeasures:
Sever the enterprise network from the internet. Note: this step requires the agency to understand its internal and external connections. When making the decision to sever internet access, knowledge of connections must be combined with care to avoid disrupting critical functions.
If you cannot sever from the internet, shutdown all non-essential traffic between the affected enterprise network and the internet.
Reset credentials of privileged and non-privileged accounts within the trust boundary of each compromised account.
Reset passwords for all domain users and all local accounts, such as Guest, HelpAssistant, DefaultAccount, System, Administrator, and krbtgt. The krbtgt account is responsible for handling Kerberos ticket requests as well as encrypting and signing them. The krbtgt account should be reset twice because the account has a two-password history. The first account reset for the krbtgt needs to be allowed to replicate prior to the second reset to avoid any issues. See CISA’s Eviction Guidance for Networks Affected by the SolarWinds and Active Directory/M365 Compromise for more information. Although tailored to FCEB agencies compromised in the 2020 SolarWinds Orion supply chain compromise, the steps are applicable to organizations with Windows AD compromise.
Review access policies to temporarily revoke privileges/access for affected accounts/devices. If it is necessary to not alert the attacker (e.g., for intelligence purposes), then privileges can be reduced for affected accounts/devices to “contain” them.
Reset the relevant account credentials or access keys if the investigation finds the threat actor’s access is limited to non-elevated permissions.
Monitor related accounts, especially administrative accounts, for any further signs of unauthorized access.
Audit all network appliance and edge device configurations with indicators of malicious activity for signs of unauthorized or malicious configuration changes. Organizations should ensure they audit the current network device running configuration and any local configurations that could be loaded at boot time. If configuration changes are identified:
Change all credentials being used to manage network devices, to include keys and strings used to secure network device functions (SNMP strings/user credentials, IPsec/IKE preshared keys, routing secrets, TACACS/RADIUS secrets, RSA keys/certificates, etc.).
Update all firmware and software to the latest version.
Report the compromise to an authoring agency (see the Contact Information section).
For organizations with cloud or hybrid environments, apply best practices for identity and credential access management.
Verify that all accounts with privileged role assignments are cloud native, not synced from Active Directory.


Empty model extraction; coverage review still required.

## 19 · AA24-038A:development:llama500:45851:48255

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Exact source window:

 all firmware and software to the latest version.
Report the compromise to an authoring agency (see the Contact Information section).
For organizations with cloud or hybrid environments, apply best practices for identity and credential access management.
Verify that all accounts with privileged role assignments are cloud native, not synced from Active Directory.
Audit conditional access policies to ensure Global Administrators and other highly privileged service principals and accounts are not exempted.
Audit privileged role assignments to ensure adherence to the principle of least privilege when assigning privileged roles.
Leverage just-in-time and just-enough access mechanisms when administrators need to elevate to a privileged role.
In hybrid environments, ensure federated systems (such as AD FS) are configured and monitored properly.
Audit Enterprise Applications for recently added applications and examine the API permissions assigned to each.
Reconnect to the internet. Note: The decision to reconnect to the internet depends on senior leadership’s confidence in the actions taken. It is possible—depending on the environment—that new information discovered during pre-eviction and eviction steps could add additional eviction tasks.
Minimize and control use of remote access tools and protocols by applying best practices from joint Guide to Securing Remote Access Software and joint Cybersecurity Information Sheet: Keeping PowerShell: Security Measures to Use and Embrace.
Consider sharing technical information with an authoring agency and/or a sector-specific information sharing and analysis center.
For more information on incident response and remediation, see:
Joint advisory Technical Approaches to Uncovering and Remediating Malicious Activity. This advisory provides incident response best practices.
CISA’s Federal Government Cybersecurity Incident and Vulnerability Response Playbooks. Although tailored to U.S. Federal Civilian Executive Branch (FCEB) agencies, the playbooks are applicable to all organizations. The incident response playbook provides procedures to identify, coordinate, remediate, recover, and track successful mitigations from incidents.
Joint Water and Wastewater Sector - Incident Response Guide. This joint guide provides incident response best practices and information on federal resources for Water and Wastewater Systems Sector organizations.


Empty model extraction; coverage review still required.

## 20 · AA23-144A:development:llama500:2866:5312

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:


This advisory uses the MITRE ATT&CK for Enterprise framework, version 13. See the Appendix: MITRE ATT&CK Techniques for all referenced tactics and techniques.
Background
The authoring agencies are aware of recent People’s Republic of China (PRC) state-sponsored cyber activity and have identified potential indicators associated with these techniques. This advisory will help net defenders hunt for this activity on their systems. It provides many network and host artifacts associated with the activity occurring after the network has been initially compromised, with a focus on command lines used by the cyber actor. An Indicators of compromise (IOCs) summary is included at the end of this advisory.
Especially for living off the land techniques, it is possible that some command lines might appear on a system as the result of benign activity and would be false positive indicators of malicious activity. Defenders must evaluate matches to determine their significance, applying their knowledge of the system and baseline behavior. Additionally, if creating detection logic based on these commands, network defenders should account for variability in command string arguments, as items such as ports used may differ across environments.
Artifacts
Network Artifacts
The actor has leveraged compromised small office/home office (SOHO) network devices as intermediate infrastructure to obscure their activity by having much of the command and control (C2) traffic emanate from local ISPs in the geographic area of the victim. Owners of SOHO devices should ensure that network management interfaces are not exposed to the Internet to avoid them being re-purposed as redirectors by malicious actors. If they must be exposed to the Internet, device owners and operators should ensure they follow zero trust principles and maintain the highest level of authentication and access controls possible.
The actor has used Earthworm and a custom Fast Reverse Proxy (FRP) client with hardcoded C2 callbacks [T1090] to ports 8080, 8443, 8043, 8000, and 10443 with various filenames including, but not limited to: cisco_up.exe, cl64.exe, vm3dservice.exe, watchdogd.exe, Win.exe, WmiPreSV.exe, and WmiPrvSE.exe.
Host Artifacts
Windows Management Instrumentation (WMI/WMIC)
The actor has executed the following command to gather information about local drives [T1082]:
cmd.exe /C "wmic path win32_logicaldisk get caption,filesystem,freespace,size,volumename"


### Candidate 0

FRP -> USES_TECHNIQUE -> T1090
Exact supporting span: The actor has used Earthworm and a custom Fast Reverse Proxy (FRP) client with hardcoded C2 callbacks [T1090] to ports 8080, 8443, 8043, 8000, and 10443 with various filenames including, but not limited to: cisco_up.exe, cl64.exe, vm3dservice.exe, watchdogd.exe, Win.exe, WmiPreSV.exe, and WmiPrvSE.exe.
Review flags: []

## 21 · AA23-144A:development:llama500:5058:7282

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

SE.exe.
Host Artifacts
Windows Management Instrumentation (WMI/WMIC)
The actor has executed the following command to gather information about local drives [T1082]:
cmd.exe /C "wmic path win32_logicaldisk get caption,filesystem,freespace,size,volumename"
This command does not require administrative credentials to return results. The command uses a command prompt [T1059.003] to execute a Windows Management Instrumentation Command Line (WMIC) query, collecting information about the storage devices on the local host, including drive letter, file system (e.g., new technology file system [NTFS]), free space and drive size in bytes, and an optional volume name. Windows Management Instrumentation (WMI) is a built-in Windows tool that allows a user to access management information from hosts in an enterprise environment. The command line version of WMI is called WMIC.
By default, WMI Tracing is not enabled, so the WMI commands being executed and the associated user might not be available. Additional information on WMI events and tracing can be found in the References section of the advisory.
Ntds.dit Active Directory Database
The actor may try to exfiltrate the ntds.dit file and the SYSTEM registry hive from Windows domain controllers (DCs) out of the network to perform password cracking [T1003.003]. (The ntds.dit file is the main Active Directory (AD) database file and, by default, is stored at %SystemRoot%\NTDS\ntds.dit. This file contains information about users, groups, group memberships, and password hashes for all users in the domain; the SYSTEM registry hive contains the boot key that is used to encrypt information in the ntds.dit file.) Although the ntds.dit file is locked while in use by AD, a copy can be made by creating a Volume Shadow Copy and extracting the ntds.dit file from the Shadow Copy. The SYSTEM registry hive may also be obtained from the Shadow Copy. The following example commands show the actor creating a Shadow Copy and then extracting a copy of the ntds.dit file from it.
cmd /c vssadmin create shadow /for=C: > C:\Windows\Temp\<filename>.tmp cmd /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\Windows\NTDS\ntds.dit C:\Windows\Temp > C:\Windows\Temp\<filename>.tmp


Empty model extraction; coverage review still required.

## 22 · AA23-144A:development:llama500:7090:8977

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

admin create shadow /for=C: > C:\Windows\Temp\<filename>.tmp cmd /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\Windows\NTDS\ntds.dit C:\Windows\Temp > C:\Windows\Temp\<filename>.tmp
The built-in Ntdsutil.exe tool performs all these actions using a single command. There are several ways to execute Ntdsutil.exe, including running from an elevated command prompt (cmd.exe), using WMI/WMIC, or PowerShell. Defenders should look for the execution of Ntdsutil.exe commands using long, short, or a combination of the notations. For example, the long notation command activate instance ntds ifm can also be executed using the short notation ac i ntds i. Table 1 provides the long and short forms of the arguments used in the sample Ntdsutil.exe command, along with a brief description of the arguments.
Table 1: Ntdsutil.exe command syntax
Long form
Short form
Description
activate instance %
ac i %
Sets variable % as the active instance for ntdsutil to use
ifm
i
Install from media (ifm). Creates installation media to be used with DCPromo so the server will not need to copy data from another Domain Controller on the network
The actor has executed WMIC commands [T1047] to create a copy of the ntds.dit file and SYSTEM registry hive using ntdsutil.exe. Each of the following actor commands is a standalone example; multiple examples are provided to show how syntax and file paths may differ per environment.
wmic process call create "ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\pro
wmic process call create "cmd.exe /c ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\Pro"
wmic process call create "cmd.exe /c mkdir C:\Windows\Temp\tmp & ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\tmp\"
"cmd.exe" /c wmic process call create "cmd.exe /c mkdir C:\windows\Temp\McAfee_Logs & ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\McAfee_Logs\"


### Candidate 0

ntdsutil.exe -> USES_TECHNIQUE -> T1047
Exact supporting span: The actor has executed WMIC commands [T1047] to create a copy of the ntds.dit file and SYSTEM registry hive using ntdsutil.exe.
Review flags: []

## 23 · AA23-144A:development:llama500:8817:10877

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

\"
"cmd.exe" /c wmic process call create "cmd.exe /c mkdir C:\windows\Temp\McAfee_Logs & ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\McAfee_Logs\"
cmd.exe /Q /c wmic process call create "cmd.exe /c mkdir C:\Windows\Temp\tmp & ntdsutil \"ac i ntds\" ifm \"create full C:\Windows\Temp\tmp\" 1> \\127.0.0.1\ADMIN$\ 2>&1
Note: The <timestamp value> would be an epoch timestamp following the format like “__1684956600.123456”.
Each actor command above creates a copy of the ntds.dit database and the SYSTEM and SECURITY registry hives in the C:\Windows\Temp\<folder> directory, where <folder> is replaced with the path specified in the command (e.g., pro, tmp, or McAfee_Logs). By default, the hidden ADMIN$ share is mapped to C:\Windows\, so the last command will direct standard output and error messages from the command to a file within the folder specified.
The actor has also saved the files directly to the C:\Windows\Temp and C:\Users\Public directories, so the entirety of those directory structures should be analyzed. Ntdsutil.exe creates two subfolders in the directory specified in the command: an Active Directory folder that contains the ntds.dit and ntds.jfm files, and a registry folder that contains the SYSTEM and SECURITY hives. Defenders should look for this folder structure across their network:
<path specified in command>\Active Directory\ntds.dit
<path specified in command>\Active Directory\ntds.jfm
<path specified in command>\registry\SECURITY
<path specified in command>\registry\SYSTEM
When one of the example commands is executed, several successive log entries are created in the Application log, under the ESENT Source. Associated events can be viewed in Windows Event Viewer by navigating to: Windows Logs | Application. To narrow results to relevant events, select Filter Current Log from the Actions menu on the right side of the screen. In the Event sources dropdown, check the box next to ESENT, then limit the logs to ID numbers 216, 325, 326, and 327. Clicking the OK box will apply the filters to the results.


Empty model extraction; coverage review still required.

## 24 · AA23-144A:development:llama500:10640:12844

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

 Log from the Actions menu on the right side of the screen. In the Event sources dropdown, check the box next to ESENT, then limit the logs to ID numbers 216, 325, 326, and 327. Clicking the OK box will apply the filters to the results.
Since ESENT logging is used extensively throughout Windows, defenders should focus on events that reference ntds.dit. If such events are present, the events’ details should contain the file path where the file copies were created. Since these files can be deleted, or enhanced logging may not be configured on hosts, the file path can greatly aid in a hunt operation. Identifying the user associated with this activity is also a critical step in a hunt operation as other actions by the compromised—or actor-created—user account can be helpful to understand additional actor TTPs, as well as the breadth of the actor's actions.
Note: If an actor can exfiltrate the ntds.dit and SYSTEM registry hive, the entire domain should be considered compromised, as the actor will generally be able to crack the password hashes for domain user accounts, create their own accounts, and/or join unauthorized systems to the domain. If this occurs, defenders should follow guidance for removing malicious actors from victim networks, such as CISA's Eviction Guidance for Network Affected by the SolarWinds and Active Directory/M365 Compromise.
In addition to the above TTPs used by the actor to copy the ntds.dit file, the following tools could be used by an actor to obtain the same information:
Secretsdump.py
Note: This script is a component of Impacket, which the actor has been known to use
Invoke-NinjaCopy (PowerShell)
DSInternals (PowerShell)
FgDump
Metasploit
Best practices for securing ntds.dit include hardening Domain Controllers and monitoring event logs for ntdsutil.exe and similar process creations. Additionally, any use of administrator privileges should be audited and validated to confirm the legitimacy of executed commands.
PortProxy
The actor has used the following commands to enable port forwarding [T1090] on the host:
"cmd.exe /c "netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=9999 connectaddress= connectport=8443 protocol=tcp""


Empty model extraction; coverage review still required.

## 25 · AA23-144A:development:llama500:12637:15219

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

 the following commands to enable port forwarding [T1090] on the host:
"cmd.exe /c "netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=9999 connectaddress= connectport=8443 protocol=tcp""
"cmd.exe /c netsh interface portproxy add v4tov4 listenport=50100 listenaddress=0.0.0.0 connectport=1433 connectaddress="
where <rfc1918 internal ip address> is replaced with an IPv4 address internal to the network, omitting the < >’s.
Netsh is a built-in Windows command line scripting utility that can display or modify the network settings of a host, including the Windows Firewall. The portproxy add command is used to create a host:port proxy that will forward incoming connections on the provided listenaddress and listenport to the connectaddress and connectport. Administrative privileges are required to execute the portproxy command. Each portproxy command above will create a registry key in the HKLM\SYSTEM\CurrentControlSet\Services\PortProxy\v4tov4\tcp\ path. Defenders should look for the presences of keys in this path and investigate any anomalous entries.
Note: Using port proxies is not common for legitimate system administration since they can constitute a backdoor into the network that bypasses firewall policies. Administrators should limit port proxy usage within environments and only enable them for the period of time in which they are required.
Defenders should also use unusual IP addresses and ports in the command lines or registry entries to identify other hosts that are potentially included in actor actions. All hosts on the network should be examined for new and unusual firewall and port forwarding rules, as well as IP addresses and ports specified by the actor. If network traffic or logging is available, defenders should attempt to identify what traffic was forwarded though the port proxies to aid in the hunt operation. As previously mentioned, identifying the associated user account that made the networking changes can also aid in the hunt operation.
Firewall rule additions and changes can be viewed in Windows Event Viewer by navigating to: Applications and Service Logs | Microsoft | Windows | Windows Firewall With Advanced Security | Firewall.
In addition to host-level changes, defenders should review perimeter firewall configurations for unauthorized changes and/or entries that may permit external connections to internal hosts. The actor is known to target perimeter devices in their operations. Firewall logs should be reviewed for any connections to systems on the ports listed in any portproxy commands discovered.


Empty model extraction; coverage review still required.

## 26 · AA23-144A:development:llama500:14842:17098

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

 addition to host-level changes, defenders should review perimeter firewall configurations for unauthorized changes and/or entries that may permit external connections to internal hosts. The actor is known to target perimeter devices in their operations. Firewall logs should be reviewed for any connections to systems on the ports listed in any portproxy commands discovered.
PowerShell
The actor has used the following PowerShell [T1059.001] command to identify successful logons to the host [T1033]:
Get-EventLog security -instanceid 4624
Note: Event ID 4624 is logged when a user successfully logs on to a host and contains useful information such as the logon type (e.g., interactive or networking), associated user and computer account names, and the logon time. Event ID 4624 entries can be viewed in Windows Event Viewer by navigating to: Windows Logs | Security. PowerShell logs can be viewed in Event Viewer: Applications and Service Logs | Windows PowerShell.
This command identifies what user account they are currently leveraging to access the network, identify other users logged on to the host, or identify how their actions are being logged. If the actor is using a password spray technique [T1110.003], there may be several failed logon (Event ID 4625) events for several different user accounts, followed by one or more successful logons (Event ID 4624) within a short period of time. This period may vary by actor but can range from a few seconds to a few minutes.
If the actor is using brute force password attempts [T1110] against a single user account, there may be several Event ID 4625 entries for that account, followed by a successful logon Event ID 4624. Defenders should also look for abnormal account activity, such as logons outside of normal working hours and impossible time-and-distance logons (e.g., a user logging on from two geographically separated locations at the same time).
Impacket
The actor regularly employs the use of Impacket’s wmiexec, which redirects output to a file within the victim host's ADMIN$ share (C:\Windows\) containing an epoch timestamp in its name. The following is an example of the "dir" command being executed by wmiexec.py:
cmd.exe /Q /c *dir 1> \\127.0.0.1\ADMIN$\__1684956600.123456 2>&1


Empty model extraction; coverage review still required.

## 27 · AA23-144A:development:llama500:16923:18755

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

 epoch timestamp in its name. The following is an example of the "dir" command being executed by wmiexec.py:
cmd.exe /Q /c *dir 1> \\127.0.0.1\ADMIN$\__1684956600.123456 2>&1
Note: Discovery of an entry similar to the example above in the Windows Event Log and/or a file with a name in a similar format may be evidence of malicious activity and should be investigated further. In the event that only a filename is discovered, the epoch timestamp within the filename reflects the time of execution by default and can be used to help scope threat hunting activities.
Enumeration of the Environment
The following commands were used by the actor to enumerate the network topology [T1016], the active directory structure [T1069.002], and other information about the target environment [T1069.001], [T1082]:
arp -a
curl www.ip-api[.]com
dnscmd . /enumrecords /zone {REDACTED}
dnscmd . /enumzones
dnscmd /enumrecords {REDACTED} . /additional
ipconfig /all
ldifde.exe -f c:\windows\temp\<filename>.txt -p subtree
net localgroup administrators
net group /dom net group "Domain Admins" /dom
netsh interface firewall show all
netsh interface portproxy show all
netsh interface portproxy show v4tov4
netsh firewall show all
netsh portproxy show v4tov4
netstat -ano
reg query hklm\software\
systeminfo
tasklist /v
whoami
wmic volume list brief
wmic service brief
wmic product list brief
wmic baseboard list full
wevtutil qe security /rd:true /f:text /q:*[System[(EventID=4624) and TimeCreated[@SystemTime>='{REDACTED}']] and EventData[Data='{REDACTED}']]
Additional Credential Theft
The actor also used the following commands to identify additional opportunities for obtaining credentials in the environment [T1555], [T1003]:
dir C:\Users\{REDACTED}\.ssh\known_hosts
dir C:\users\{REDACTED}\appdata\roaming\Mozilla\firefox\profiles
mimikatz.exe


Empty model extraction; coverage review still required.

## 28 · AA23-144A:development:llama500:18586:19961

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

Exact source window:

 credentials in the environment [T1555], [T1003]:
dir C:\Users\{REDACTED}\.ssh\known_hosts
dir C:\users\{REDACTED}\appdata\roaming\Mozilla\firefox\profiles
mimikatz.exe
reg query hklm\software\OpenSSH
reg query hklm\software\OpenSSH\Agent
reg query hklm\software\realvnc
reg query hklm\software\realvnc\vncserver
reg query hklm\software\realvnc\Allusers
reg query hklm\software\realvnc\Allusers\vncserver
reg query hkcu\software\{REDACTED}\putty\session
reg save hklm\sam ss.dat
reg save hklm\system sy.dat
Additional Commands
The actor executed the following additional commands:
7z.exe a -p {REDACTED} c:\windows\temp\{REDACTED}.7z
C:\Windows\system32\pcwrun.exe
C:\Users\Administrator\Desktop\Win.exe
C:\Windows\System32\cmdbak.exe /c ping -n 1 127.0.0.1 > C:\Windows\temp\putty.log C:\Windows\Temp\tmp.log
"cmd.exe" /c dir \\127.0.0.1\C$ /od
"cmd.exe" /c ping –a –n 1 <IP address>
"cmd.exe" /c wmic /user:<username> /password:<password> process call create "net stop \"<service name>\" > C:\Windows\Temp\tmp.log"
cmd.exe /Q /c cd 1> \\127.0.0.1\ADMIN$\__<timestamp value> 2>&1
net use \\127.0.0.1\IPC$ /y /d
powershell start-process -filepath c:\windows\temp\<filename>.bat -windowstyle Hidden
rar.exe a –{REDACTED} c:\Windows\temp\{REDACTED} D:\{REDACTED}\
wmic /node:{REDACTED} /user:{REDACTED} /password:{REDACTED} cmd /c whoami
xcopy C:\windows\temp\hp d:\{REDACTED}


Empty model extraction; coverage review still required.

## 29 · AA22-321A:development:llama500:1806:4233

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

Exact source window:


Note: This advisory uses the MITRE ATT&CK® for Enterprise framework, version 12. See MITRE ATT&CK for Enterprise for all referenced tactics and techniques.
As of November 2022, Hive ransomware actors have victimized over 1,300 companies worldwide, receiving approximately US$100 million in ransom payments, according to FBI information. Hive ransomware follows the ransomware-as-a-service (RaaS) model in which developers create, maintain, and update the malware, and affiliates conduct the ransomware attacks. From June 2021 through at least November 2022, threat actors have used Hive ransomware to target a wide range of businesses and critical infrastructure sectors, including Government Facilities, Communications, Critical Manufacturing, Information Technology, and especially Healthcare and Public Health (HPH).
The method of initial intrusion will depend on which affiliate targets the network. Hive actors have gained initial access to victim networks by using single factor logins via Remote Desktop Protocol (RDP), virtual private networks (VPNs), and other remote network connection protocols [T1133]. In some cases, Hive actors have bypassed multifactor authentication (MFA) and gained access to FortiOS servers by exploiting Common Vulnerabilities and Exposures (CVE) CVE-2020-12812. This vulnerability enables a malicious cyber actor to log in without a prompt for the user’s second authentication factor (FortiToken) when the actor changes the case of the username.
Hive actors have also gained initial access to victim networks by distributing phishing emails with malicious attachments [T1566.001] and by exploiting the following vulnerabilities against Microsoft Exchange servers [T1190]:
CVE-2021-31207 - Microsoft Exchange Server Security Feature Bypass Vulnerability
CVE-2021-34473 - Microsoft Exchange Server Remote Code Execution Vulnerability
CVE-2021-34523 - Microsoft Exchange Server Privilege Escalation Vulnerability
After gaining access, Hive ransomware attempts to evade detention by executing processes to:
Identify processes related to backups, antivirus/anti-spyware, and file copying and then terminating those processes to facilitate file encryption [T1562].
Stop the volume shadow copy services and remove all existing shadow copies via vssadmin on command line or via PowerShell [T1059] [T1490].
Delete Windows event logs, specifically the System, Security and Application logs [T1070].


### Candidate 0

Hive actors -> USES_TECHNIQUE -> T1133
Exact supporting span: Hive actors have gained initial access to victim networks by using single factor logins via Remote Desktop Protocol (RDP), virtual private networks (VPNs), and other remote network connection protocols [T1133].
Review flags: []

### Candidate 1

Hive actors -> USES_TECHNIQUE -> T1566.001
Exact supporting span: Hive actors have also gained initial access to victim networks by distributing phishing emails with malicious attachments [T1566.001] and by exploiting the following vulnerabilities against Microsoft Exchange servers [T1190]:
Review flags: []

### Candidate 2

Hive actors -> USES_TECHNIQUE -> T1190
Exact supporting span: Hive actors have also gained initial access to victim networks by distributing phishing emails with malicious attachments [T1566.001] and by exploiting the following vulnerabilities against Microsoft Exchange servers [T1190]:
Review flags: []

### Candidate 3

Hive -> USES_TECHNIQUE -> T1562
Exact supporting span: After gaining access, Hive ransomware attempts to evade detention by executing processes to:
Identify processes related to backups, antivirus/anti-spyware, and file copying and then terminating those processes to facilitate file encryption [T1562].
Review flags: []

## 30 · AA22-321A:development:llama500:3953:6298

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

Exact source window:

 processes to facilitate file encryption [T1562].
Stop the volume shadow copy services and remove all existing shadow copies via vssadmin on command line or via PowerShell [T1059] [T1490].
Delete Windows event logs, specifically the System, Security and Application logs [T1070].
Prior to encryption, Hive ransomware removes virus definitions and disables all portions of Windows Defender and other common antivirus programs in the system registry [T1112].
Hive actors exfiltrate data likely using a combination of Rclone and the cloud storage service Mega.nz [T1537]. In addition to its capabilities against the Microsoft Windows operating system, Hive ransomware has known variants for Linux, VMware ESXi, and FreeBSD.
During the encryption process, a file named *.key (previously *.key.*) is created in the root directory (C:\ or /root/). Required for decryption, this key file only exists on the machine where it was created and cannot be reproduced. The ransom note, HOW_TO_DECRYPT.txt is dropped into each affected directory and states the *.key file cannot be modified, renamed, or deleted, otherwise the encrypted files cannot be recovered [T1486]. The ransom note contains a “sales department” .onion link accessible through a TOR browser, enabling victim organizations to contact the actors through a live chat panel to discuss payment for their files. However, some victims reported receiving phone calls or emails from Hive actors directly to discuss payment.
The ransom note also threatens victims that a public disclosure or leak site accessible on the TOR site, “HiveLeaks”, contains data exfiltrated from victim organizations who do not pay the ransom demand (see figure 1 below). Additionally, Hive actors have used anonymous file sharing sites to disclose exfiltrated data (see table 1 below).
Table 1: Anonymous File Sharing Sites Used to Disclose Data
https://anonfiles[.]com
https://mega[.]nz
https://send.exploit[.]in
https://ufile[.]io
https://www.sendspace[.]com
https://privatlab[.]net
https://privatlab[.]com
Once the victim organization contacts Hive actors on the live chat panel, Hive actors communicate the ransom amount and the payment deadline. Hive actors negotiate ransom demands in U.S. dollars, with initial amounts ranging from several thousand to millions of dollars. Hive actors demand payment in Bitcoin.


### Candidate 0

Hive -> USES_TECHNIQUE -> T1112
Exact supporting span: Prior to encryption, Hive ransomware removes virus definitions and disables all portions of Windows Defender and other common antivirus programs in the system registry [T1112].
Review flags: []

### Candidate 1

Hive actors -> USES -> Rclone
Exact supporting span: Hive actors exfiltrate data likely using a combination of Rclone and the cloud storage service Mega.nz [T1537].
Review flags: ["source_uncertainty_wording"]

## 31 · AA22-321A:development:llama500:5976:8313

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

Exact source window:

atlab[.]com
Once the victim organization contacts Hive actors on the live chat panel, Hive actors communicate the ransom amount and the payment deadline. Hive actors negotiate ransom demands in U.S. dollars, with initial amounts ranging from several thousand to millions of dollars. Hive actors demand payment in Bitcoin.
Hive actors have been known to reinfect—with either Hive ransomware or another ransomware variant—the networks of victim organizations who have restored their network without making a ransom payment.
Indicators of Compromise
Threat actors have leveraged the following IOCs during Hive ransomware compromises. Note: Some of these indicators are legitimate applications that Hive threat actors used to aid in further malicious exploitation. FBI, CISA, and HHS recommend removing any application not deemed necessary for day-to-day operations. See tables 2–3 below for IOCs obtained from FBI threat response investigations as recently as November 2022.
Table 2: Known IOCs as of November 2022
Known IOCs - Files
HOW_TO_DECRYPT.txt typically in directories with encrypted files
*.key typically in the root directory, i.e., C:\ or /root
hive.bat
shadow.bat
asq.r77vh0[.]pw - Server hosted malicious HTA file
asq.d6shiiwz[.]pw - Server referenced in malicious regsvr32 execution
asq.swhw71un[.]pw - Server hosted malicious HTA file
asd.s7610rir[.]pw - Server hosted malicious HTA file
Windows_x64_encrypt.dll
Windows_x64_encrypt.exe
Windows_x32_encrypt.dll
Windows_x32_encrypt.exe
Linux_encrypt
Esxi_encrypt
Known IOCs – Events
System, Security and Application Windows event logs wiped
Microsoft Windows Defender AntiSpyware Protection disabled
Microsoft Windows Defender AntiVirus Protection disabled
Volume shadow copies deleted
Normal boot process prevented
Known IOCs – Logged Processes
wevtutil.exe cl system
wevtutil.exe cl security
wevtutil.exe cl application
vssadmin.exe delete shadows /all /quiet
wmic.exe SHADOWCOPY /nointeractive
wmic.exe shadowcopy delete
bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures
bcdedit.exe /set {default} recoveryenabled no
Table 3: Potential IOC IP Addresses as of November 2022Note: Some of these observed IP addresses are more than a year old. FBI and CISA recommend vetting or investigating these IP addresses prior to taking forward-looking action like blocking.


### Candidate 0

Hive actors -> USES -> Hive
Exact supporting span: Hive actors have been known to reinfect—with either Hive ransomware or another ransomware variant—the networks of victim organizations who have restored their network without making a ransom payment.
Review flags: []

## 32 · AA22-321A:development:llama500:8030:9146

Original status: empty_extraction
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

Exact source window:

.exe /set {default} recoveryenabled no
Table 3: Potential IOC IP Addresses as of November 2022Note: Some of these observed IP addresses are more than a year old. FBI and CISA recommend vetting or investigating these IP addresses prior to taking forward-looking action like blocking.
Potential IOC IP Addresses for Compromise or Exfil:
84.32.188[.]57
84.32.188[.]238
93.115.26[.]251
185.8.105[.]67
181.231.81[.]239
185.8.105[.]112
186.111.136[.]37
192.53.123[.]202
158.69.36[.]149
46.166.161[.]123
108.62.118[.]190
46.166.161[.]93
185.247.71[.]106
46.166.162[.]125
5.61.37[.]207
46.166.162[.]96
185.8.105[.]103
46.166.169[.]34
5.199.162[.]220
93.115.25[.]139
5.199.162[.]229
93.115.27[.]148
89.147.109[.]208
83.97.20[.]81
5.61.37[.]207
5.199.162[.]220
5.199.162[.]229;
46.166.161[.]93
46.166.161[.]123;
46.166.162[.]96
46.166.162[.]125
46.166.169[.]34
83.97.20[.]81
84.32.188[.]238
84.32.188[.]57
89.147.109[.]208
93.115.25[.]139;
93.115.26[.]251
93.115.27[.]148
108.62.118[.]190
158.69.36[.]149/span>
181.231.81[.]239
185.8.105[.]67
185.8.105[.]103
185.8.105[.]112
185.247.71[.]106
186.111.136[.]37
192.53.123[.]202


Empty model extraction; coverage review still required.

## 33 · AA22-321A:development:llama500:9038:11131

Original status: candidates_ready_for_review
Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

Exact source window:

.81[.]239
185.8.105[.]67
185.8.105[.]103
185.8.105[.]112
185.247.71[.]106
186.111.136[.]37
192.53.123[.]202
MITRE ATT&CK TECHNIQUES
See table 4 for all referenced threat actor tactics and techniques listed in this advisory.
Table 4: Hive Actors ATT&CK Techniques for Enterprise
Initial Access
Technique Title
ID
Use
External Remote Services
T1133
Hive actors gain access to victim networks by using single factor logins via RDP, VPN, and other remote network connection protocols.
Exploit Public-Facing Application
T1190
Hive actors gain access to victim network by exploiting the following Microsoft Exchange vulnerabilities: CVE-2021-34473, CVE-2021-34523, CVE-2021-31207, CVE-2021-42321.
Phishing
T1566.001
Hive actors gain access to victim networks by distributing phishing emails with malicious attachments.
Execution
Technique Title
ID
Use
Command and Scripting Interpreter
T1059
Hive actors looks to stop the volume shadow copy services and remove all existing shadow copies via vssadmin on command line or PowerShell.
Defense Evasion
Technique Title
ID
Use
Indicator Removal on Host
T1070
Hive actors delete Windows event logs, specifically, the System, Security and Application logs.
Modify Registry
T1112
Hive actors set registry values for DisableAntiSpyware and DisableAntiVirus to 1.
Impair Defenses
T1562
Hive actors seek processes related to backups, antivirus/anti-spyware, and file copying and terminates those processes to facilitate file encryption.
Exfiltration
Technique Title
ID
Use
Transfer Data to Cloud Account
T1537
Hive actors exfiltrate data from victims, using a possible combination of Rclone and the cloud storage service Mega.nz.
Impact
Technique Title
Use
Data Encrypted for Impact
T1486
Hive actors deploy a ransom note HOW_TO_DECRYPT.txt into each affected directory which states the *.key file cannot be modified, renamed, or deleted, otherwise the encrypted files cannot be recovered.
Inhibit System Recovery
T1490
Hive actors looks to stop the volume shadow copy services and remove all existing shadow copies via vssadmin via command line or PowerShell.


### Candidate 0

Hive actors -> USES -> Rclone
Exact supporting span: Hive actors exfiltrate data from victims, using a possible combination of Rclone and the cloud storage service Mega.nz.
Review flags: []

