# Additional development batch direct mitigation reference preview

Frozen Enterprise ATT&CK 17.1 associations; origin=fused, human review pending.
Reference associations do not establish incident-specific effectiveness. No parent inheritance is inferred.
Gold triples and QA reference answers are not inputs.

Verified source import: S:\ThreatWeave\work\corpus_batch_ingestion\20261015T173114Z-643927a9

Target reference assertions: 51; distinct mitigation entities: 26.
Expected source-reference combinations: 59; same-window three-hop chains: 4.

| Technique | Direct references | Mitigation IDs |
| --- | ---: | --- |
| attack:T1003.003 | 4 | M1017, M1026, M1027, M1041 |
| attack:T1021.001 | 8 | M1018, M1026, M1028, M1030, M1032, M1035, M1042, M1047 |
| attack:T1021.004 | 3 | M1018, M1032, M1042 |
| attack:T1070.001 | 3 | M1022, M1029, M1041 |
| attack:T1106 | 2 | M1038, M1040 |
| attack:T1112 | 1 | M1024 |
| attack:T1114 | 4 | M1032, M1041, M1047, M1060 |
| attack:T1219 | 5 | M1031, M1034, M1037, M1038, M1042 |
| attack:T1486 | 2 | M1040, M1053 |
| attack:T1537 | 4 | M1018, M1037, M1054, M1057 |
| attack:T1556.006 | 3 | M1018, M1032, M1047 |
| attack:T1562.004 | 4 | M1018, M1022, M1024, M1047 |
| attack:T1564.003 | 2 | M1033, M1038 |
| attack:T1567.002 | 1 | M1021 |
| attack:T1587 | 1 | M1056 |
| attack:T1606 | 4 | M1018, M1026, M1047, M1054 |
| attack:T1012 | 0 | No active direct associations in this frozen snapshot |
| attack:T1057 | 0 | No active direct associations in this frozen snapshot |
| attack:T1070.004 | 0 | No active direct associations in this frozen snapshot |

## Exact reference descriptions

### attack:T1003.003 → attack:M1017

Source STIX relationship: relationship--85b3d881-a9d2-45ff-a980-95d0bd9a3dd1

Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts.

### attack:T1003.003 → attack:M1026

Source STIX relationship: relationship--5e3f6da4-a327-4c42-8a12-bc5840336430

Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers.

### attack:T1003.003 → attack:M1027

Source STIX relationship: relationship--4775487a-b632-43f9-8372-83219e2aa98c

Ensure that local administrator accounts have complex, unique passwords across all systems on the network.

### attack:T1003.003 → attack:M1041

Source STIX relationship: relationship--e6b41083-5390-452d-991c-de86befbe6e1

Ensure Domain Controller backups are properly secured.(Citation: Metcalf 2015)

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

### attack:T1021.004 → attack:M1018

Source STIX relationship: relationship--b16c27b4-f94b-43e4-832d-986c03b96ffd

Limit which user accounts are allowed to login via SSH.

### attack:T1021.004 → attack:M1032

Source STIX relationship: relationship--77c5bb7d-9584-4d57-850b-6349984181a8

Require multi-factor authentication for SSH connections wherever possible, such as password protected SSH keys.

### attack:T1021.004 → attack:M1042

Source STIX relationship: relationship--0263d539-39f0-45ca-be2d-0f9198db9af0

Disable the SSH daemon on systems that do not require it, especially ESXi servers. For macOS, ensure Remote Login is disabled under Sharing Preferences.(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

### attack:T1070.001 → attack:M1022

Source STIX relationship: relationship--3642f351-831b-4c4f-b1d6-4673db4a70a1

Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities.

### attack:T1070.001 → attack:M1029

Source STIX relationship: relationship--5d1cba64-6732-4263-baee-32aa2ab81183

Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system.

### attack:T1070.001 → attack:M1041

Source STIX relationship: relationship--7bae5d92-dcc7-41c7-a116-58e9c9e84401

Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary.

### attack:T1106 → attack:M1038

Source STIX relationship: relationship--42f4db8f-ef8b-4dcc-8c8f-4d0b5219c8b7

Identify and block potentially malicious software executed that may be executed through this technique by using application control (Citation: Beechey 2010) tools, like Windows Defender Application Control(Citation: Microsoft Windows Defender Application Control), AppLocker, (Citation: Windows Commands JPCERT) (Citation: NSA MS AppLocker) or Software Restriction Policies (Citation: Corio 2008) where appropriate. (Citation: TechNet Applocker vs SRP)

### attack:T1106 → attack:M1040

Source STIX relationship: relationship--ba25a8ba-dc7a-4197-b885-d910524588b7

On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent Office VBA macros from calling Win32 APIs. (Citation: win10_asr)

### attack:T1112 → attack:M1024

Source STIX relationship: relationship--81bb4898-aaa2-4dff-9af8-a97e6b69a95a

Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

### attack:T1114 → attack:M1032

Source STIX relationship: relationship--3709ccc2-2370-4dc9-92ac-792867bbdea4

Use of multi-factor authentication for public-facing webmail servers is a recommended best practice to minimize the usefulness of usernames and passwords to adversaries.

### attack:T1114 → attack:M1041

Source STIX relationship: relationship--c15c9cbf-7ecc-4e2b-8fe1-636f381bac63

Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages.

### attack:T1114 → attack:M1047

Source STIX relationship: relationship--d60b92c6-2030-4802-8d7d-868ff15f3b0c

Enterprise email solutions have monitoring mechanisms that may include the ability to audit auto-forwarding rules on a regular basis.

In an Exchange environment, Administrators can use Get-InboxRule to discover and remove potentially malicious auto-forwarding rules.(Citation: Microsoft Tim McMichael Exchange Mail Forwarding 2) 

### attack:T1114 → attack:M1060

Source STIX relationship: relationship--bae85c8c-8b02-4a4c-8a38-c46f30c48274

Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email to prevent adversaries from collecting data through compromised email accounts.(Citation: TrustedSec OOB Communications)

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

### attack:T1486 → attack:M1040

Source STIX relationship: relationship--9c8dee77-e751-40b6-ab99-ccfe6a832e0a

On Windows 10, enable cloud-delivered protection and Attack Surface Reduction (ASR) rules to block the execution of files that resemble ransomware.(Citation: win10_asr) In AWS environments, create an IAM policy to restrict or block the use of SSE-C on S3 buckets.(Citation: Halcyon AWS Ransomware 2025)

### attack:T1486 → attack:M1053

Source STIX relationship: relationship--f8bb44c8-d368-4d56-b039-50d6419ab60a

Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data.(Citation: Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. Consider enabling versioning in cloud environments to maintain backup copies of storage objects.(Citation: Rhino S3 Ransomware Part 2)

### attack:T1537 → attack:M1018

Source STIX relationship: relationship--27fde8e9-ab78-43aa-9642-14ac0cd958ff

Limit user account and IAM policies to the least privileges required.

### attack:T1537 → attack:M1037

Source STIX relationship: relationship--a5b61b67-8d99-4bc5-86d0-00739f0be666

Implement network-based filtering restrictions to prohibit data transfers to untrusted VPCs.

### attack:T1537 → attack:M1054

Source STIX relationship: relationship--8389c9f5-ace5-4240-a694-7008313fc168

Configure appropriate data sharing restrictions in cloud services. For example, external sharing in Microsoft SharePoint and Google Drive can be turned off altogether, blocked for certain domains, or restricted to certain users.(Citation: Google Workspace External Sharing) (Citation: Microsoft 365 External Sharing)

### attack:T1537 → attack:M1057

Source STIX relationship: relationship--1844caba-e446-4c82-aa0e-9f826c523a25

Data loss prevention can prevent and block sensitive data from being shared with individuals outside an organization.(Citation: Microsoft Purview Data Loss Prevention) (Citation: Google Workspace Data Loss Prevention)

### attack:T1556.006 → attack:M1018

Source STIX relationship: relationship--21aa8534-0280-4109-8dfb-6adbc2310dd8

Ensure that proper policies are implemented to dictate the secure enrollment and deactivation of MFA for user accounts.

### attack:T1556.006 → attack:M1032

Source STIX relationship: relationship--eb985609-6a5f-4e44-9bae-bfbc1e93d978

Ensure that MFA and MFA policies and requirements are properly implemented for existing and deactivated or dormant accounts and devices. If possible, consider configuring MFA solutions to "fail closed" rather than grant access in case of serious errors.

### attack:T1556.006 → attack:M1047

Source STIX relationship: relationship--90d0d818-4a80-459c-9d57-ca9221eae57b

Review MFA actions alongside authentication logs to ensure that MFA-based logins are functioning as intended. Review user accounts to ensure that all accounts have MFA enabled.(Citation: Mandiant Cloudy Logs 2023)

### attack:T1562.004 → attack:M1018

Source STIX relationship: relationship--c9f23224-fecf-48e8-867b-1c299fb40cf3

Ensure proper user permissions are in place to prevent adversaries from disabling or modifying firewall settings.

### attack:T1562.004 → attack:M1022

Source STIX relationship: relationship--e31f5737-0105-481d-9e12-e0986f752164

Ensure proper process and file permissions are in place to prevent adversaries from disabling or modifying firewall settings.

### attack:T1562.004 → attack:M1024

Source STIX relationship: relationship--e2a9b959-8179-4ea0-99bc-8a8310bd1de2

Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings.

### attack:T1562.004 → attack:M1047

Source STIX relationship: relationship--aed677d9-a79f-4448-b6a9-3df4d647730b

Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls.

### attack:T1564.003 → attack:M1033

Source STIX relationship: relationship--61b6152c-6606-474c-926a-a874a3084ac8

Restrict the installation of software that may be abused to create hidden desktops, such as hVNC, to user groups that require it.

### attack:T1564.003 → attack:M1038

Source STIX relationship: relationship--1279ae2b-fb00-4980-a5cc-9a802ad2901d

Limit or restrict program execution using anti-virus software. On MacOS, allowlist programs that are allowed to have the plist tag. All other programs should be considered suspicious.

### attack:T1567.002 → attack:M1021

Source STIX relationship: relationship--cf16ba1d-ea81-4301-a1a4-083e4a8927fe

Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services.

### attack:T1587 → attack:M1056

Source STIX relationship: relationship--17fde86e-66f2-4432-881c-b162c0501204

This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.

### attack:T1606 → attack:M1018

Source STIX relationship: relationship--f2d946f4-04fe-4b56-8152-80644b6b22d5

Ensure that user accounts with administrative rights follow best practices, including use of privileged access workstations, Just in Time/Just Enough Administration (JIT/JEA), and strong authentication. Reduce the number of users that are members of highly privileged Directory Roles.(Citation: Microsoft SolarWinds Customer Guidance) In AWS environments, prohibit users from calling the `sts:GetFederationToken` API unless explicitly required.(Citation: Crowdstrike AWS User Federation Persistence)

### attack:T1606 → attack:M1026

Source STIX relationship: relationship--673afcb8-2fb0-4c17-9f91-8fb409943531

Restrict permissions and access to the AD FS server to only originate from privileged access workstations.(Citation: FireEye ADFS)

### attack:T1606 → attack:M1047

Source STIX relationship: relationship--da4b552e-fae2-42ef-ac2f-9b61e6ff365a

Administrators should perform an audit of all access lists and the permissions they have been granted to access web applications and services. This should be done extensively on all resources in order to establish a baseline, followed up on with periodic audits of new or updated resources. Suspicious accounts/credentials should be investigated and removed.
 
Enable advanced auditing on ADFS. Check the success and failure audit options in the ADFS Management snap-in. Enable Audit Application Generated events on the AD FS farm via Group Policy Object.(Citation: FireEye ADFS)

### attack:T1606 → attack:M1054

Source STIX relationship: relationship--ce647878-e4d9-4472-9777-b731edbd3d9a

Configure browsers/applications to regularly delete persistent web credentials (such as cookies).

