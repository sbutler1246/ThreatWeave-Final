# Corpus pilot direct mitigation reference preview

Frozen Enterprise ATT&CK 17.1 associations; origin=fused, human review pending.
Reference associations do not establish incident-specific effectiveness. No parent inheritance is inferred.
Gold triples and QA reference answers are not inputs.

Verified source import: S:\ThreatWeave\work\corpus_pilot_ingestion\20261015T040329Z-5b1d9d11

Target reference assertions: 55; distinct mitigation entities: 27.
Expected source-reference combinations: 72; same-window three-hop chains: 6.

| Technique | Direct references | Mitigation IDs |
| --- | ---: | --- |
| attack:T1021.001 | 8 | M1018, M1026, M1028, M1030, M1032, M1035, M1042, M1047 |
| attack:T1055.002 | 1 | M1040 |
| attack:T1059.001 | 5 | M1026, M1038, M1042, M1045, M1049 |
| attack:T1059.003 | 1 | M1038 |
| attack:T1078 | 8 | M1013, M1015, M1017, M1018, M1026, M1027, M1032, M1036 |
| attack:T1087.002 | 1 | M1028 |
| attack:T1133 | 4 | M1030, M1032, M1035, M1042 |
| attack:T1204 | 5 | M1017, M1021, M1031, M1038, M1040 |
| attack:T1219 | 5 | M1031, M1034, M1037, M1038, M1042 |
| attack:T1539 | 6 | M1017, M1021, M1032, M1047, M1051, M1054 |
| attack:T1562.001 | 5 | M1018, M1022, M1024, M1038, M1047 |
| attack:T1586 | 1 | M1056 |
| attack:T1587.001 | 1 | M1056 |
| attack:T1598 | 2 | M1017, M1054 |
| attack:T1656 | 2 | M1017, M1019 |
| attack:T1018 | 0 | No active direct associations in this frozen snapshot |
| attack:T1069.002 | 0 | No active direct associations in this frozen snapshot |
| attack:T1217 | 0 | No active direct associations in this frozen snapshot |

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

### attack:T1055.002 → attack:M1040

Source STIX relationship: relationship--0e530e67-4e80-412f-8b38-fbc14085f05c

Some endpoint security solutions can be configured to block some types of process injection based on common sequences of behavior that occur during the injection process. 

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

### attack:T1087.002 → attack:M1028

Source STIX relationship: relationship--9ef08a26-d881-4a36-952b-c07808093c6b

Prevent administrator accounts from being enumerated when an application is elevating through UAC since it can lead to the disclosure of account names. The Registry key is located at <code>HKLM\ SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\EnumerateAdministrators</code>. It can be disabled through GPO: Computer Configuration > [Policies] > Administrative Templates > Windows Components > Credential User Interface: Enumerate administrator accounts on elevation.(Citation: UCF STIG Elevation Account Enumeration)

### attack:T1133 → attack:M1030

Source STIX relationship: relationship--8df2f4b5-3f60-4b8f-b4aa-dd76eb347ab0

Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls.

### attack:T1133 → attack:M1032

Source STIX relationship: relationship--e23d57b4-5bc4-4d06-9084-9c99464c4af8

Use strong two-factor or multi-factor authentication for remote service accounts to mitigate an adversary's ability to leverage stolen credentials, but be aware of [Multi-Factor Authentication Interception](https://attack.mitre.org/techniques/T1111) techniques for some two-factor authentication implementations.

### attack:T1133 → attack:M1035

Source STIX relationship: relationship--9eaaffb7-4dc4-4aac-a1d5-675b71e587df

Limit access to remote services through centrally managed concentrators such as VPNs and other managed remote access systems.

### attack:T1133 → attack:M1042

Source STIX relationship: relationship--9aaf5e70-4080-4f73-8d6d-3b19f754e9b9

Disable or block remotely available services that may be unnecessary.

### attack:T1204 → attack:M1017

Source STIX relationship: relationship--1d1525e6-74f2-447d-ba11-9e9c9c552403

Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events.

### attack:T1204 → attack:M1021

Source STIX relationship: relationship--66551074-a1e3-439c-a996-c1f7ca8136e2

If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files.

### attack:T1204 → attack:M1031

Source STIX relationship: relationship--8e567361-e2de-4dc6-b953-ec82dc143f58

If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity.

### attack:T1204 → attack:M1038

Source STIX relationship: relationship--225ab1b4-f800-4a92-9949-a0f05fce6213

Application control may be able to prevent the running of executables masquerading as other files.

### attack:T1204 → attack:M1040

Source STIX relationship: relationship--3551c43c-b1b9-432b-8c3a-cf0265ca74ff

On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent executable files from running unless they meet a prevalence, age, or trusted list criteria and to prevent Office applications from creating potentially malicious executable content by blocking malicious code from being written to disk. Note: cloud-delivered protection must be enabled to use certain rules. (Citation: win10_asr)

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

### attack:T1539 → attack:M1017

Source STIX relationship: relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab

Train users to identify aspects of phishing attempts where they're asked to enter credentials into a site that has the incorrect domain for the application they are logging into. Additionally, train users not to run untrusted JavaScript in their browser, such as by copying and pasting code or dragging and dropping bookmarklets.

### attack:T1539 → attack:M1021

Source STIX relationship: relationship--44c91929-3473-443c-91be-5afa81582dfa

Restrict or block web-based content that could be used to extract session cookies or credentials stored in browsers. Use browser security settings, such as disabling third-party cookies and restricting browser extensions, to limit the attack surface.

### attack:T1539 → attack:M1032

Source STIX relationship: relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4

A physical second factor key that uses the target login domain as part of the negotiation protocol will prevent session cookie theft through proxy methods.(Citation: Evilginx 2 July 2018)

Implement Conditional Access policies with Token Protection to bind session tokens to their originating device and user. This reduces the risk of session cookie theft by ensuring that stolen tokens cannot be reused from unauthorized locations or devices.

### attack:T1539 → attack:M1047

Source STIX relationship: relationship--1a5bf948-33fd-4025-aadd-117e99512e6a

Implement auditing for authentication activities and user logins to detect the use of stolen session cookies. Monitor for impossible travel scenarios and anomalous behavior that could indicate the use of compromised session tokens or cookies.

### attack:T1539 → attack:M1051

Source STIX relationship: relationship--a27be16a-0132-4895-8f62-2bcc31cf15d7

Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies.

### attack:T1539 → attack:M1054

Source STIX relationship: relationship--248a0d72-d9cd-43d3-985f-a33a49a79e8b

Configure browsers or tasks to regularly delete persistent cookies.

Additionally, minimize the length of time a web cookie is viable to potentially reduce the impact of stolen cookies while also increasing the needed frequency of cookie theft attempts – providing defenders with additional chances at detection.(Citation: Token tactics) For example, use non-persistent cookies to limit the duration a session ID will remain on the web client cache where an attacker could obtain it.(Citation: Session Management Cheat Sheet)

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

### attack:T1586 → attack:M1056

Source STIX relationship: relationship--d06c7363-a7f6-43b1-8af8-9d3b9975160c

This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.

### attack:T1587.001 → attack:M1056

Source STIX relationship: relationship--6bf03275-b5bb-4c67-b3a6-5a4642d763e6

This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.

### attack:T1598 → attack:M1017

Source STIX relationship: relationship--3de6d2ba-842b-4f60-b177-d8082eebbb1e

Users can be trained to identify social engineering techniques and spearphishing attempts.

### attack:T1598 → attack:M1054

Source STIX relationship: relationship--727520dd-a7ee-4665-a610-201f0d5e2f0e

Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

### attack:T1656 → attack:M1017

Source STIX relationship: relationship--03981d0c-c7d5-4a65-bd8f-1b1a2c1efe2a

Train users to be aware of impersonation tricks and how to counter them, for example confirming incoming requests through an independent platform like a phone call or in-person, to reduce risk.

### attack:T1656 → attack:M1019

Source STIX relationship: relationship--7a1b9942-4be4-4460-86b0-88638a1c4944

Threat intelligence helps defenders and users be aware of and defend against common lures and active campaigns that have been used for impersonation.

