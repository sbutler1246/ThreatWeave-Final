# Held-out evaluation corpus direct mitigation reference preview

Frozen Enterprise ATT&CK 17.1 associations; origin=fused, human review pending.
Reference associations do not establish incident-specific effectiveness. No parent inheritance is inferred.
Gold triples and QA reference answers are not inputs.

Verified source import: S:\ThreatWeave\work\evaluation_corpus_ingestion\20261016T042742Z-72fb42f8

Target reference assertions: 109; distinct mitigation entities: 34.
Expected source-reference combinations: 203; same-window three-hop chains: 0.

| Technique | Direct references | Mitigation IDs |
| --- | ---: | --- |
| attack:T1021.001 | 8 | M1018, M1026, M1028, M1030, M1032, M1035, M1042, M1047 |
| attack:T1027 | 4 | M1017, M1040, M1047, M1049 |
| attack:T1027.015 | 1 | M1049 |
| attack:T1046 | 3 | M1030, M1031, M1042 |
| attack:T1048 | 6 | M1018, M1022, M1030, M1031, M1037, M1057 |
| attack:T1059.001 | 5 | M1026, M1038, M1042, M1045, M1049 |
| attack:T1059.003 | 1 | M1038 |
| attack:T1059.005 | 5 | M1021, M1038, M1040, M1042, M1049 |
| attack:T1068 | 5 | M1019, M1038, M1048, M1050, M1051 |
| attack:T1078 | 8 | M1013, M1015, M1017, M1018, M1026, M1027, M1032, M1036 |
| attack:T1090 | 3 | M1020, M1031, M1037 |
| attack:T1105 | 1 | M1031 |
| attack:T1110.003 | 3 | M1027, M1032, M1036 |
| attack:T1190 | 7 | M1016, M1026, M1030, M1035, M1048, M1050, M1051 |
| attack:T1219 | 5 | M1031, M1034, M1037, M1038, M1042 |
| attack:T1480.001 | 1 | M1055 |
| attack:T1482 | 2 | M1030, M1047 |
| attack:T1484.001 | 2 | M1018, M1047 |
| attack:T1489 | 5 | M1018, M1022, M1024, M1030, M1060 |
| attack:T1490 | 4 | M1018, M1028, M1038, M1053 |
| attack:T1491.001 | 1 | M1053 |
| attack:T1562.001 | 5 | M1018, M1022, M1024, M1038, M1047 |
| attack:T1564.012 | 2 | M1013, M1049 |
| attack:T1566 | 6 | M1017, M1021, M1031, M1047, M1049, M1054 |
| attack:T1566.001 | 7 | M1017, M1018, M1021, M1031, M1047, M1049, M1054 |
| attack:T1566.002 | 5 | M1017, M1018, M1021, M1047, M1054 |
| attack:T1567.002 | 1 | M1021 |
| attack:T1572 | 2 | M1031, M1037 |
| attack:T1675 | 1 | M1018 |
| attack:T1016 | 0 | No active direct associations in this frozen snapshot |
| attack:T1018 | 0 | No active direct associations in this frozen snapshot |
| attack:T1069.001 | 0 | No active direct associations in this frozen snapshot |
| attack:T1069.002 | 0 | No active direct associations in this frozen snapshot |
| attack:T1083 | 0 | No active direct associations in this frozen snapshot |

## Exact reference descriptions

### attack:T1021.001 → attack:M1018

Source STIX relationship: relationship--8fae4ace-c3b5-4c4b-8c1a-98a32c692849

Limit remote user permissions if remote access is necessary.

### attack:T1021.001 → attack:M1026

Source STIX relationship: relationship--e7e4be4c-a6ae-44bc-b3af-9c0c41f9212e

Consider removing the local Administrators group from the list of groups allowed to log in through RDP.

### attack:T1021.001 → attack:M1028

Source STIX relationship: relationship--4b5e4611-ed5c-4223-bc75-5e272090b887

Change GPOs to define shorter timeouts sessions and maximum amount of time any single session can be active. Change GPOs to specify the maximum amount of time that a disconnected session stays active on the RD session host server.(Citation: Windows RDP Sessions)

### attack:T1021.001 → attack:M1030

Source STIX relationship: relationship--3951503f-c8e9-4331-834e-df4e4afda5fb

Do not leave RDP accessible from the internet. Enable firewall rules to block RDP traffic between network security zones within a network.

### attack:T1021.001 → attack:M1032

Source STIX relationship: relationship--96014091-aba9-4b8f-ac6a-6cdeb593cf30

Use multi-factor authentication for remote logins.(Citation: Berkley Secure)

### attack:T1021.001 → attack:M1035

Source STIX relationship: relationship--375d3b8b-0e1b-4d3b-b31f-43b0e98436a5

Use remote desktop gateways.

### attack:T1021.001 → attack:M1042

Source STIX relationship: relationship--703a5971-a542-4d7d-8bf5-7a9adb1db852

Disable the RDP service if it is unnecessary.

### attack:T1021.001 → attack:M1047

Source STIX relationship: relationship--36e86ea2-e0d4-4ade-bae8-212a78c8d569

Audit the Remote Desktop Users group membership regularly. Remove unnecessary accounts and groups from Remote Desktop Users groups.

### attack:T1027 → attack:M1017

Source STIX relationship: relationship--f4d1e337-60ba-4e28-89d1-ff206bae1750

Ensure that a finite amount of ingress points to a software deployment system exist with restricted access for those required to allow and enable newly deployed software.

### attack:T1027 → attack:M1040

Source STIX relationship: relationship--cca451aa-d4ca-4697-ac64-745841fb8658

On Windows 10+, enable Attack Surface Reduction (ASR) rules to prevent execution of potentially obfuscated payloads. (Citation: win10_asr)

### attack:T1027 → attack:M1047

Source STIX relationship: relationship--9f42ded2-e291-4856-91ab-cf5ff8be461a

Consider periodic review of common fileless storage locations (such as the Registry or WMI repository) to potentially identify abnormal and malicious data.

### attack:T1027 → attack:M1049

Source STIX relationship: relationship--ffa8f46b-615f-4b95-8ed5-90f86eaedd20

Anti-virus can be used to automatically detect and quarantine suspicious files. Consider utilizing the Antimalware Scan Interface (AMSI) on Windows 10+ to analyze commands after being processed/interpreted. (Citation: Microsoft AMSI June 2015)

### attack:T1027.015 → attack:M1049

Source STIX relationship: relationship--0b1d3aa7-eae6-4ab3-89ca-e4771696975e

Anti-virus can be used to automatically detect and quarantine suspicious files. Consider anti-virus products capable of unpacking and inspecting compressed files recursively, as well as analyzing SFX archives. 

### attack:T1046 → attack:M1030

Source STIX relationship: relationship--80f94d40-0861-4403-b206-1c864a136788

Ensure proper network segmentation is followed to protect critical servers and devices.

### attack:T1046 → attack:M1031

Source STIX relationship: relationship--651225d6-5454-4c44-8d62-776bd7ddaed2

Use network intrusion detection/prevention systems to detect and prevent remote service scans.

### attack:T1046 → attack:M1042

Source STIX relationship: relationship--32d482c4-2c0d-4688-a38b-d73b5b2962a3

Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation.

### attack:T1048 → attack:M1018

Source STIX relationship: relationship--f52e6fb6-754b-4b48-ab5b-eff0e6233d7d

Configure user permissions groups and roles for access to cloud storage.(Citation: Microsoft Azure Storage Security, 2019) Implement strict Identity and Access Management (IAM) controls to prevent access to storage solutions except for the applications, users, and services that require access.(Citation: Amazon S3 Security, 2019) Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary.(Citation: Amazon  AWS Temporary Security Credentials)

### attack:T1048 → attack:M1022

Source STIX relationship: relationship--e5ad94e4-f136-44d7-8000-7dd607538a7c

Use access control lists on cloud storage systems and objects. 

### attack:T1048 → attack:M1030

Source STIX relationship: relationship--4867dbb4-1e1b-45f6-9070-8e2c0c303638

Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network.(Citation: TechNet Firewall Design)

### attack:T1048 → attack:M1031

Source STIX relationship: relationship--7bdcd3e6-f741-4f62-9495-3111309adad8

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level.

### attack:T1048 → attack:M1037

Source STIX relationship: relationship--6eec2d79-1d59-459d-af33-b186ece9748b

Enforce proxies and use dedicated servers for services such as DNS and only allow those systems to communicate over respective ports/protocols, instead of all systems within a network. Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP allowlisting along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data.

### attack:T1048 → attack:M1057

Source STIX relationship: relationship--6c1c4fa3-7b48-4d9e-ab23-5f0c5dd4e98a

Data loss prevention can detect and block sensitive data being uploaded via web browsers.

### attack:T1059.001 → attack:M1026

Source STIX relationship: relationship--e631d85f-e93c-475f-bd40-546544c99e90

When PowerShell is necessary, consider restricting PowerShell execution policy to administrators. Be aware that there are methods of bypassing the PowerShell execution policy, depending on environment configuration.(Citation: Netspi PowerShell Execution Policy Bypass)

PowerShell JEA (Just Enough Administration) may also be used to sandbox administration and limit what commands admins/users can execute through remote PowerShell sessions.(Citation: Microsoft PS JEA)

### attack:T1059.001 → attack:M1038

Source STIX relationship: relationship--fe42b5e6-06dd-4b08-8ef8-31323f8190d2

Use application control where appropriate. PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).(Citation: Microsoft PowerShell CLM)

### attack:T1059.001 → attack:M1042

Source STIX relationship: relationship--5a580cd0-19f1-41d6-865b-786a41081a7e

It may be possible to remove PowerShell from systems when not needed, but a review should be performed to assess the impact to an environment, since it could be in use for many legitimate purposes and administrative functions.

Disable/restrict the WinRM Service to help prevent uses of PowerShell for remote execution.

### attack:T1059.001 → attack:M1045

Source STIX relationship: relationship--8fc79376-2f71-4ca1-8177-a96dea11f8c7

Set PowerShell execution policy to execute only signed scripts.

### attack:T1059.001 → attack:M1049

Source STIX relationship: relationship--758cbc32-6b33-4012-8622-cd7d218a799c

Anti-virus can be used to automatically quarantine suspicious files. 

### attack:T1059.003 → attack:M1038

Source STIX relationship: relationship--aa103bc8-1753-4b41-bf5c-a9dc0b9a2986

Use application control where appropriate.

### attack:T1059.005 → attack:M1021

Source STIX relationship: relationship--a6360da7-8678-4d7c-a866-6f2a982a23ba

Script blocking extensions can help prevent the execution of scripts and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place.

### attack:T1059.005 → attack:M1038

Source STIX relationship: relationship--1a69dce6-b39e-4cd2-a29a-18e42293c51a

Use application control where appropriate. VBA macros obtained from the Internet, based on the file's Mark of the Web (MOTW) attribute, may be blocked from executing in Office applications (ex: Access, Excel, PowerPoint, Visio, and Word) by default starting in Windows Version 2203.(Citation: Default VBS macros Blocking )

### attack:T1059.005 → attack:M1040

Source STIX relationship: relationship--875eff48-2319-4e86-b3cf-0f17d6253b9c

On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent [Visual Basic](https://attack.mitre.org/techniques/T1059/005) scripts from executing potentially malicious downloaded content (Citation: win10_asr).

### attack:T1059.005 → attack:M1042

Source STIX relationship: relationship--0f27ea83-21e7-4a9f-9c66-85fe85da5135

Turn off or restrict access to unneeded VB components.

### attack:T1059.005 → attack:M1049

Source STIX relationship: relationship--1461fa53-bc4f-4ae5-b131-3f6058e6a72a

Anti-virus can be used to automatically quarantine suspicious files. 

### attack:T1068 → attack:M1019

Source STIX relationship: relationship--c6615e27-5984-44b3-82dc-f710c6823834

Develop a robust cyber threat intelligence capability to determine what types and levels of threat may use software exploits and 0-days against a particular organization.

### attack:T1068 → attack:M1038

Source STIX relationship: relationship--dd9a12ee-30b1-4764-860d-111c73411ebe

Consider blocking the execution of known vulnerable drivers that adversaries may exploit to execute code in kernel mode. Validate driver block rules in audit mode to ensure stability prior to production deployment.(Citation: Microsoft Driver Block Rules)

### attack:T1068 → attack:M1048

Source STIX relationship: relationship--5edeca3e-96aa-45e6-b99b-044e25cb3245

Make it difficult for adversaries to advance their operation through exploitation of undiscovered or unpatched vulnerabilities by using sandboxing. Other types of virtualization and application microsegmentation may also mitigate the impact of some types of exploitation. Risks of additional exploits and weaknesses in these systems may still exist. (Citation: Ars Technica Pwn2Own 2017 VM Escape)

### attack:T1068 → attack:M1050

Source STIX relationship: relationship--267fa35c-7748-40eb-87ba-bddc0c88d643

Security applications that look for behavior used during exploitation such as Windows Defender Exploit Guard (WDEG) and the Enhanced Mitigation Experience Toolkit (EMET) can be used to mitigate some exploitation behavior. (Citation: TechNet Moving Beyond EMET) Control flow integrity checking is another way to potentially identify and stop a software exploit from occurring. (Citation: Wikipedia Control Flow Integrity) Many of these protections depend on the architecture and target application binary for compatibility and may not work for software components targeted for privilege escalation.

### attack:T1068 → attack:M1051

Source STIX relationship: relationship--22d11711-5794-42aa-a9c5-02895fe3420d

Update software regularly by employing patch management for internal enterprise endpoints and servers.

### attack:T1078 → attack:M1013

Source STIX relationship: relationship--c8acdf40-8237-487f-8255-91afa327705d

Ensure that applications do not store sensitive data or credentials insecurely. (e.g. plaintext credentials in code, published credentials in repositories, or credentials in public cloud storage).

### attack:T1078 → attack:M1015

Source STIX relationship: relationship--eed29e0f-59c1-4fab-8268-3f0571e90748

Disable legacy authentication, which does not support MFA, and require the use of modern authentication protocols instead.

### attack:T1078 → attack:M1017

Source STIX relationship: relationship--edaeb27a-9226-4805-ae45-87312a2dc013

Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications.

### attack:T1078 → attack:M1018

Source STIX relationship: relationship--555abf76-531f-4d35-9783-ed7c2a3f213b

Regularly audit user accounts for activity and deactivate or remove any that are no longer needed.

### attack:T1078 → attack:M1026

Source STIX relationship: relationship--89887815-acfc-42f9-9172-81437cf9ff69

Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. (Citation: TechNet Credential Theft) (Citation: TechNet Least Privilege) These audits should also include if default accounts have been enabled, or if new local accounts are created that have not been authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. (Citation: Microsoft Securing Privileged Access)

### attack:T1078 → attack:M1027

Source STIX relationship: relationship--4f24d075-4d6c-49d2-a213-306e4af2083d

Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment.(Citation: US-CERT Alert TA13-175A Risks of Default Passwords on the Internet) When possible, applications that use SSH keys should be updated periodically and properly secured.

Policies should minimize (if not eliminate) reuse of passwords between different user accounts, especially employees using the same credentials for personal accounts that may not be defended by enterprise security resources.

### attack:T1078 → attack:M1032

Source STIX relationship: relationship--98167cc6-96de-4f02-83b1-78d7633c4106

Implement multi-factor authentication (MFA) across all account types, including default, local, domain, and cloud accounts, to prevent unauthorized access, even if credentials are compromised. MFA provides a critical layer of security by requiring multiple forms of verification beyond just a password. This measure significantly reduces the risk of adversaries abusing valid accounts to gain initial access, escalate privileges, maintain persistence, or evade defenses within your network.

### attack:T1078 → attack:M1036

Source STIX relationship: relationship--f2d01f19-b4e7-417a-a936-11af9386b867

Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges.(Citation: Microsoft Common Conditional Access Policies)

### attack:T1090 → attack:M1020

Source STIX relationship: relationship--f229e2fb-3105-4ae5-abe1-d100209f702c

If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be domain fronting.

### attack:T1090 → attack:M1031

Source STIX relationship: relationship--d50b5687-ea69-40f9-86f3-eecd7e015bac

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific C2 protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. (Citation: University of Birmingham C2)

### attack:T1090 → attack:M1037

Source STIX relationship: relationship--a424a85c-a3c6-4d84-85f7-e55c8dbe21fc

Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network allow and block lists. It should be noted that this kind of blocking may be circumvented by other techniques like [Domain Fronting](https://attack.mitre.org/techniques/T1090/004).

### attack:T1105 → attack:M1031

Source STIX relationship: relationship--1ddae833-8280-4afa-b2b0-e250e22104fe

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools.(Citation: University of Birmingham C2)

### attack:T1110.003 → attack:M1027

Source STIX relationship: relationship--c215cce3-a2f5-4534-937c-b15d7be4588c

Refer to NIST guidelines when creating password policies. (Citation: NIST 800-63-3)

### attack:T1110.003 → attack:M1032

Source STIX relationship: relationship--64201f56-d678-4ed2-b759-c78bf9e4d82a

Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services.

### attack:T1110.003 → attack:M1036

Source STIX relationship: relationship--cff34686-cbdf-4e0b-8108-c2deaf8855a7

Set account lockout policies after a certain number of failed login attempts to prevent passwords from being guessed. Too strict a policy may create a denial of service condition and render environments un-usable, with all accounts used in the brute force being locked-out. Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges.(Citation: Microsoft Common Conditional Access Policies) Consider blocking risky authentication requests, such as those originating from anonymizing services/proxies.(Citation: Okta Block Anonymizing Services)

### attack:T1190 → attack:M1016

Source STIX relationship: relationship--4c308ec1-f0c6-4444-af7d-ff045204c326

Regularly scan externally facing systems for vulnerabilities and establish procedures to rapidly patch systems when critical vulnerabilities are discovered through scanning and through public disclosure.(Citation: OWASP Top 10)

### attack:T1190 → attack:M1026

Source STIX relationship: relationship--4d50a045-d85d-481f-ac7d-672065f1e348

Use least privilege for service accounts will limit what permissions the exploited process gets on the rest of the system.

### attack:T1190 → attack:M1030

Source STIX relationship: relationship--3b726298-74dc-4f8a-b58d-f623bc645124

Segment externally facing servers and services from the rest of the network with a DMZ or on separate hosting infrastructure.

### attack:T1190 → attack:M1035

Source STIX relationship: relationship--b7b6cc9f-50ac-4774-9dd4-3c14b408b99e

Ensure that all publicly exposed services are actually intended to be so, and restrict access to any that should only be available internally. 

### attack:T1190 → attack:M1048

Source STIX relationship: relationship--0c8fdb59-a28f-4f8f-a788-9e3e8928c6d5

Application isolation will limit what other processes and system features the exploited target can access.

### attack:T1190 → attack:M1050

Source STIX relationship: relationship--53a95297-1cce-401c-99a3-34079e878fac

Web Application Firewalls may be used to limit exposure of applications to prevent exploit traffic from reaching the application.

### attack:T1190 → attack:M1051

Source STIX relationship: relationship--d373eebb-b578-4b59-9de1-2946bf837d96

Update software regularly by employing patch management for externally exposed applications.

### attack:T1219 → attack:M1031

Source STIX relationship: relationship--d5c70727-794c-4404-b30d-0d798a62ad64

Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services.

### attack:T1219 → attack:M1034

Source STIX relationship: relationship--9ae55ec5-a4f8-4619-8565-fe00433c574a

Block the use of IP-based KVM devices within the network if they are not required. 

### attack:T1219 → attack:M1037

Source STIX relationship: relationship--80a23356-20b7-49a3-a48e-e0c04e2bff86

Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access software.

### attack:T1219 → attack:M1038

Source STIX relationship: relationship--54306888-1f93-4461-bcac-a56ae7073b31

Use application control to mitigate installation and use of unapproved software that can be used for remote access.

### attack:T1219 → attack:M1042

Source STIX relationship: relationship--fa4c9d5a-3329-4138-b6e1-990cd7935b87

Consider disabling unnecessary remote connection functionality, including both unapproved software installations and specific features built into supported applications.

### attack:T1480.001 → attack:M1055

Source STIX relationship: relationship--9a513f75-f09b-4840-8654-521fa4ff59fa

[Environmental Keying](https://attack.mitre.org/techniques/T1480/001) likely should not be mitigated with preventative controls because it may protect unintended targets from being compromised via confusion of keys by the adversary. Mitigation of this technique is also unlikely to be feasible within most contexts because there are no standard attributes from which an adversary may derive keys. If targeted, efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior if compromised.

### attack:T1482 → attack:M1030

Source STIX relationship: relationship--68949ed4-db1b-40bb-b2ca-1a91d2739295

Employ network segmentation for sensitive domains.(Citation: Harmj0y Domain Trusts).

### attack:T1482 → attack:M1047

Source STIX relationship: relationship--047e6dc3-d213-4d97-8573-9c8da28a0742

Map the trusts within existing domains/forests and keep trust relationships to a minimum.

### attack:T1484.001 → attack:M1018

Source STIX relationship: relationship--57563748-1634-4625-baa4-73a4b1d7dbfb

Consider implementing WMI and security filtering to further tailor which users and computers a GPO will apply to.(Citation: Wald0 Guide to GPOs)(Citation: Microsoft WMI Filters)(Citation: Microsoft GPO Security Filtering)

### attack:T1484.001 → attack:M1047

Source STIX relationship: relationship--19e387c4-0dd8-4c00-9195-73ed25ad061e

Identify and correct GPO permissions abuse opportunities (ex: GPO modification privileges) using auditing tools such as [BloodHound](https://attack.mitre.org/software/S0521) (version 1.5.1 and later).(Citation: GitHub Bloodhound)

### attack:T1489 → attack:M1018

Source STIX relationship: relationship--b5023b20-4243-4686-8b51-429ae7ac73cb

Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations.

### attack:T1489 → attack:M1022

Source STIX relationship: relationship--e28dc4ab-86fe-480e-9f0d-d7fab54c432d

Ensure proper process and file permissions are in place to inhibit adversaries from disabling or interfering with critical services.

### attack:T1489 → attack:M1024

Source STIX relationship: relationship--c00535d0-6e59-4293-8034-70e5bf94a74a

Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services.

### attack:T1489 → attack:M1030

Source STIX relationship: relationship--40cd458c-5a59-4a8d-a04a-3cd3faebaf66

Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions.

### attack:T1489 → attack:M1060

Source STIX relationship: relationship--b774aa5d-7731-46b4-b285-dc1c67a0d01c

Develop and enforce security policies that include the use of out-of-band communication channels for critical communications during a security incident.(Citation: TrustedSec OOB Communications)

### attack:T1490 → attack:M1018

Source STIX relationship: relationship--d62f97e9-2b94-44d9-88db-99f849a804ec

Limit the user accounts that have access to backups to only those required. In AWS environments, consider using Service Control Policies to restrict API calls to delete backups, snapshots, and images. 

### attack:T1490 → attack:M1028

Source STIX relationship: relationship--c4cd9acb-aaea-4b77-890e-f153a58623a4

Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Additionally, ensure that WinRE is enabled using the following command: <code>reagentc /enable</code>.(Citation: reagentc_cmd)

### attack:T1490 → attack:M1038

Source STIX relationship: relationship--9104be87-33ad-4a35-96db-3e2ed5c17f46

Consider using application control configured to block execution of utilities such as `diskshadow.exe` that may not be required for a given system or network to prevent potential misuse by adversaries. 

### attack:T1490 → attack:M1053

Source STIX relationship: relationship--f9e62f6d-a091-44a9-91e6-3660b89ba2b9

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.(Citation: Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. In cloud environments, enable versioning on storage objects where possible, and copy backups to other accounts or regions to isolate them from the original copies.(Citation: Unit 42 Palo Alto Ransomware in Public Clouds 2022) On ESXi servers, ensure that disk images and snapshots of virtual machines are regularly taken, with copies stored off system.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

### attack:T1491.001 → attack:M1053

Source STIX relationship: relationship--77d97059-4280-41d0-8280-596a6e2b8ff8

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.(Citation: Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

### attack:T1562.001 → attack:M1018

Source STIX relationship: relationship--dddb38c9-408c-44da-9e51-3f7cd159c43d

Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services.

### attack:T1562.001 → attack:M1022

Source STIX relationship: relationship--f36141b8-5dd8-462d-bfc3-b43e179e955c

Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with security services.

### attack:T1562.001 → attack:M1024

Source STIX relationship: relationship--a66c8397-99c0-494c-9cbe-4055e0b2f6a1

Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering with security services.

### attack:T1562.001 → attack:M1038

Source STIX relationship: relationship--7734ffaf-1cd2-40ca-8c0d-9cfd95e8d1ec

Use application control where appropriate, especially regarding the execution of tools outside of the organization's security policies (such as rootkit removal tools) that have been abused to impair system defenses. Ensure that only approved security applications are used and running on enterprise systems.

### attack:T1562.001 → attack:M1047

Source STIX relationship: relationship--f5b897b8-6833-422f-9ec8-a32e5362bedc

Periodically verify that tools are functioning appropriately – for example, that all expected hosts with EDRs or monitoring agents are checking in to the central console. Check EDRs to ensure that no unexpected exclusion paths have been added. In Microsoft Defender for Endpoint, exclusions can be reviewed with the `Get-MpPreference` cmdlet.(Citation: CodeX Microsoft Defender 2021)

### attack:T1564.012 → attack:M1013

Source STIX relationship: relationship--7acdcde3-1065-4393-ae6b-80ac95b2607d

Application developers should consider limiting the requirements for custom or otherwise difficult to manage file/folder exclusions. Where possible, install applications to trusted system folder paths that are already protected by restricted file and directory permissions.

### attack:T1564.012 → attack:M1049

Source STIX relationship: relationship--3d24da0a-7124-4043-881b-da19436c007c

Review and audit file/folder exclusions, and limit scope of exclusions to only what is required where possible.(Citation: Microsoft File Folder Exclusions)

### attack:T1566 → attack:M1017

Source STIX relationship: relationship--ee935350-f68f-4bd7-bfca-878ae48a2b97

Users can be trained to identify social engineering techniques and phishing emails.

### attack:T1566 → attack:M1021

Source STIX relationship: relationship--a205b0ce-df00-40ae-b626-7dc3e8146d45

Determine if certain websites or attachment types (ex: .scr, .exe, .pif, .cpl, etc.) that can be used for phishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk.

### attack:T1566 → attack:M1031

Source STIX relationship: relationship--76588f90-79b8-4a61-ae07-3321393e5707

Network intrusion prevention systems and systems designed to scan and remove malicious email attachments or links can be used to block activity.

### attack:T1566 → attack:M1047

Source STIX relationship: relationship--12fc907f-4ed1-4d44-a40b-12bfa8b89082

Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses.

### attack:T1566 → attack:M1049

Source STIX relationship: relationship--ed821f5e-9527-4fbb-ae76-37a79592dfb6

Anti-virus can automatically quarantine suspicious files.

### attack:T1566 → attack:M1054

Source STIX relationship: relationship--7b090d29-d49d-4967-9843-90636bfb039f

Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

### attack:T1566.001 → attack:M1017

Source STIX relationship: relationship--bfa95fdc-6f4f-48a9-a155-189c81dc9ebd

Users can be trained to identify social engineering techniques and spearphishing emails.

### attack:T1566.001 → attack:M1018

Source STIX relationship: relationship--4bd4de17-4aa2-4924-a1fd-d82a68209cf0

Apply user account management principles to limit permissions for accounts interacting with email attachments, ensuring that only necessary accounts have the ability to open or execute files. Restricting account privileges reduces the potential impact of malicious attachments by preventing unauthorized execution or spread of malware within the environment.

### attack:T1566.001 → attack:M1021

Source STIX relationship: relationship--f2f68eb7-4110-4750-9d1c-58774036672b

Block unknown or unused attachments by default that should not be transmitted over email as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some email scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious attachments.

### attack:T1566.001 → attack:M1031

Source STIX relationship: relationship--7a75d200-29f5-4f8a-b052-bcbe4e5ca236

Network intrusion prevention systems and systems designed to scan and remove malicious email attachments can be used to block activity.

### attack:T1566.001 → attack:M1047

Source STIX relationship: relationship--75122837-7638-4ff2-8cb4-fbb8001e96f2

Enable auditing and monitoring for email attachments and file transfers to detect and investigate suspicious activity. Regularly review logs for anomalies related to attachments containing potentially malicious content, as well as any attempts to execute or interact with these files. This practice helps identify spearphishing attempts before they can lead to further compromise.

### attack:T1566.001 → attack:M1049

Source STIX relationship: relationship--26d24472-ae04-46e7-9166-5d8a8f6f16f7

Anti-virus can also automatically quarantine suspicious files.

### attack:T1566.001 → attack:M1054

Source STIX relationship: relationship--985f770f-6068-4c5c-9405-0515e43aeed5

Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

### attack:T1566.002 → attack:M1017

Source STIX relationship: relationship--d4f9d2ab-70d0-4aaf-9c7f-d94fc0818ecb

Users can be trained to identify social engineering techniques and spearphishing emails with malicious links which includes phishing for consent with OAuth 2.0. Additionally, users may perform visual checks of the domains they visit; however, homographs in ASCII and in IDN domains and URL schema obfuscation may render manual checks difficult. Use email warning banners to alert users when emails contain links from external senders, prompting them to exercise caution and reducing the likelihood of falling victim to spearphishing attacks. Phishing training and other cybersecurity training may raise awareness to check URLs before visiting the sites.

### attack:T1566.002 → attack:M1018

Source STIX relationship: relationship--a3a8c9e7-ed71-46c9-aa1f-c609406652b0

Azure AD Administrators apply limitations upon the ability for users to grant consent to unfamiliar or unverified third-party applications. 

### attack:T1566.002 → attack:M1021

Source STIX relationship: relationship--239092bc-09e4-4c16-9d83-071929c9e4a4

Determine if certain websites that can be used for spearphishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk.

### attack:T1566.002 → attack:M1047

Source STIX relationship: relationship--5f90f8ec-9154-4f28-a632-fd4024e6fbce

Audit applications and their permissions to ensure access to data and resources are limited based upon necessity and principle of least privilege.

### attack:T1566.002 → attack:M1054

Source STIX relationship: relationship--005b46de-6241-413e-ba13-e0c2cc8efa77

Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing).

Furthermore, policies may enforce / install browser extensions that protect against IDN and homograph attacks.

### attack:T1567.002 → attack:M1021

Source STIX relationship: relationship--cf16ba1d-ea81-4301-a1a4-083e4a8927fe

Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services.

### attack:T1572 → attack:M1031

Source STIX relationship: relationship--17639fa3-3f77-4481-b24f-9df82fcbf324

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. 

### attack:T1572 → attack:M1037

Source STIX relationship: relationship--0927eb00-4a08-4ed1-8678-84d6e1e87b98

Consider filtering network traffic to untrusted or known bad domains and resources. 

### attack:T1675 → attack:M1018

Source STIX relationship: relationship--8c85cc49-731e-44ae-b8a0-2162444e9ee7

If not required, restrict the permissions of users to perform Guest Operations on ESXi-hosted VMs.(Citation: Broadcom Virtual Machine Guest Operations Privileges)

