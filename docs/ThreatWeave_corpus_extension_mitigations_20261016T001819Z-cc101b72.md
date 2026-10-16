# Three-report extension direct mitigation reference preview

Frozen Enterprise ATT&CK 17.1 associations; origin=fused, human review pending.
Reference associations do not establish incident-specific effectiveness. No parent inheritance is inferred.
Gold triples and QA reference answers are not inputs.

Verified source import: S:\ThreatWeave\work\corpus_extension_ingestion\20261016T001729Z-60fdb691

Target reference assertions: 48; distinct mitigation entities: 26.
Expected source-reference combinations: 53; same-window three-hop chains: 3.

| Technique | Direct references | Mitigation IDs |
| --- | ---: | --- |
| attack:T1059 | 9 | M1021, M1026, M1033, M1038, M1040, M1042, M1045, M1047, M1049 |
| attack:T1068 | 5 | M1019, M1038, M1048, M1050, M1051 |
| attack:T1090 | 3 | M1020, M1031, M1037 |
| attack:T1090.001 | 1 | M1031 |
| attack:T1090.003 | 1 | M1037 |
| attack:T1112 | 1 | M1024 |
| attack:T1133 | 4 | M1030, M1032, M1035, M1042 |
| attack:T1190 | 7 | M1016, M1026, M1030, M1035, M1048, M1050, M1051 |
| attack:T1560.001 | 1 | M1047 |
| attack:T1562 | 7 | M1018, M1022, M1024, M1038, M1042, M1047, M1054 |
| attack:T1566.001 | 7 | M1017, M1018, M1021, M1031, M1047, M1049, M1054 |
| attack:T1589.002 | 1 | M1056 |
| attack:T1591 | 1 | M1056 |
| attack:T1057 | 0 | No active direct associations in this frozen snapshot |
| attack:T1082 | 0 | No active direct associations in this frozen snapshot |

## Exact reference descriptions

### attack:T1059 → attack:M1021

Source STIX relationship: relationship--d4dbffc2-246d-4fd4-8c3c-0e7901aaef05

Script blocking extensions can help prevent the execution of scripts and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place.

### attack:T1059 → attack:M1026

Source STIX relationship: relationship--ad32e902-6f48-4c8f-bc3d-2fc06f045eed

When PowerShell is necessary, consider restricting PowerShell execution policy to administrators. Be aware that there are methods of bypassing the PowerShell execution policy, depending on environment configuration.(Citation: Netspi PowerShell Execution Policy Bypass)

PowerShell JEA (Just Enough Administration) may also be used to sandbox administration and limit what commands admins/users can execute through remote PowerShell sessions.(Citation: Microsoft PS JEA)

### attack:T1059 → attack:M1033

Source STIX relationship: relationship--292e29e8-79d9-4b15-930e-a7e26c27ca15

Prevent user installation of unrequired command and scripting interpreters.

### attack:T1059 → attack:M1038

Source STIX relationship: relationship--87fd0088-41da-47ac-bd69-a8ac151a0d39

Use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).(Citation: Microsoft PowerShell CLM)

### attack:T1059 → attack:M1040

Source STIX relationship: relationship--e93059c7-2f60-47f5-af11-bc0a6e7e6d25

On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent [Visual Basic](https://attack.mitre.org/techniques/T1059/005) and [JavaScript](https://attack.mitre.org/techniques/T1059/007) scripts from executing potentially malicious downloaded content (Citation: win10_asr).

### attack:T1059 → attack:M1042

Source STIX relationship: relationship--6abc6901-d152-4b5f-b27d-8b973ae567cb

Disable or remove any unnecessary or unused shells or interpreters.

### attack:T1059 → attack:M1045

Source STIX relationship: relationship--2cf7243f-d5d7-473b-9cb7-27c7186565d3

Where possible, only permit execution of signed scripts.

### attack:T1059 → attack:M1047

Source STIX relationship: relationship--c8ff4bb6-92df-40ca-b975-6682d7c6ac82

Inventory systems for unauthorized command and scripting interpreter installations.

### attack:T1059 → attack:M1049

Source STIX relationship: relationship--8d56622d-547a-4daa-89b8-1c555d1ac5b7

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

### attack:T1090 → attack:M1020

Source STIX relationship: relationship--f229e2fb-3105-4ae5-abe1-d100209f702c

If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be domain fronting.

### attack:T1090 → attack:M1031

Source STIX relationship: relationship--d50b5687-ea69-40f9-86f3-eecd7e015bac

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific C2 protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. (Citation: University of Birmingham C2)

### attack:T1090 → attack:M1037

Source STIX relationship: relationship--a424a85c-a3c6-4d84-85f7-e55c8dbe21fc

Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network allow and block lists. It should be noted that this kind of blocking may be circumvented by other techniques like [Domain Fronting](https://attack.mitre.org/techniques/T1090/004).

### attack:T1090.001 → attack:M1031

Source STIX relationship: relationship--864def70-2079-4015-8852-d77e19dd086c

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific C2 protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools.(Citation: University of Birmingham C2)

### attack:T1090.003 → attack:M1037

Source STIX relationship: relationship--4735a1be-c556-4844-9554-d2313376f09a

Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network allow and block lists. It should be noted that this kind of blocking may be circumvented by other techniques like [Domain Fronting](https://attack.mitre.org/techniques/T1090/004).

### attack:T1112 → attack:M1024

Source STIX relationship: relationship--81bb4898-aaa2-4dff-9af8-a97e6b69a95a

Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

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

### attack:T1560.001 → attack:M1047

Source STIX relationship: relationship--9448e565-a9ea-44c2-9c03-8f6112cd7d1d

System scans can be performed to identify unauthorized archival utilities.

### attack:T1562 → attack:M1018

Source STIX relationship: relationship--7ef8afb4-2bfa-471b-a412-b1862418be3e

Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security/logging services.

### attack:T1562 → attack:M1022

Source STIX relationship: relationship--b8113c99-fc84-4c2d-8925-cb1f5733f6eb

Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with security/logging services.

### attack:T1562 → attack:M1024

Source STIX relationship: relationship--c0aa0cf1-4c03-4fdd-bdbb-65563bff4a81

Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering with security/logging services.

### attack:T1562 → attack:M1038

Source STIX relationship: relationship--952ec6aa-f5dd-494d-91ea-b3804b843c35

Use application control where appropriate, especially regarding the execution of tools outside of the organization's security policies (such as rootkit removal tools) that have been abused to impair system defenses. Ensure that only approved security applications are used and running on enterprise systems.

### attack:T1562 → attack:M1042

Source STIX relationship: relationship--d8efae26-9a5c-4abc-9c60-3f94f63040d2

Consider removing previous versions of tools that are unnecessary to the environment when possible.

### attack:T1562 → attack:M1047

Source STIX relationship: relationship--c6330aef-b396-4664-9258-a6bed2f4573e

Routinely check account role permissions to ensure only expected users and roles have permission to modify defensive tools and settings. Periodically verify that tools such as EDRs are functioning as expected.

### attack:T1562 → attack:M1054

Source STIX relationship: relationship--5be525da-5357-4d33-8664-ae74cc6fea02

Consider implementing policies on internal web servers, such HTTP Strict Transport Security, that enforce the use of HTTPS/network traffic encryption to prevent insecure connections.(Citation: Chromium HSTS)

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

### attack:T1589.002 → attack:M1056

Source STIX relationship: relationship--611ad683-7772-4592-bbd4-e5589591a76e

This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties.

### attack:T1591 → attack:M1056

Source STIX relationship: relationship--024d5595-aa4e-4d47-bc31-5b8ea5ed73c0

This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties.

