# Development graph QA run

Graph-only development demonstration; generated answers require semantic review. These are not held-out evaluation scores.
Evidence is packed under a conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.

Model: llama3.1:8b; digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

## Question 1

According to CISA, what information does Raccoon Stealer steal? Explain the supplied ATT&CK mitigations for its web session cookie technique, citing observations and references separately.

Status: answer_ready_for_review

According to CISA, Raccoon Stealer steals information including login credentials, browser history, and cookies. [E1, E4]
User Training (M1017) mitigates Steal Web Session Cookie (T1539) by training users to identify phishing attempts and not run untrusted JavaScript. [E5, E6]
Restrict Web-Based Content (M1021) mitigates Steal Web Session Cookie (T1539) by restricting or blocking web-based content that could be used to extract session cookies or credentials. [E7, E8]
Multi-factor Authentication (M1032) mitigates Steal Web Session Cookie (T1539) by preventing session cookie theft through proxy methods using a physical second factor key. [E9, E10]
Audit (M1047) mitigates Steal Web Session Cookie (T1539) by implementing auditing for authentication activities and user logins to detect the use of stolen session cookies. [E11, E12]

Paths: 4; hop counts: [3, 3, 3, 3]; source passages: 12.

Source citations:

- [E1] cisa: AA23-320A / 6480:6658 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E2] cisa: AA23-320A / 23:39 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E3] cisa: AA23-320A / 2870:2887 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E4] cisa: AA23-320A / 6635:6756 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E5] attack: attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 0:98 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 276:605 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 0:111 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 289:539 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 0:112 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 290:733 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E11] attack: attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 0:90 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E12] attack: attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 268:510 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 2

According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.

Status: answer_ready_for_review

Rhysida actors use valid accounts (T1078) for access by authenticating to internal VPN access points with compromised valid credentials. [E1, E2, E3]
Application Developer Guidance (M1013) mitigates Valid Accounts (T1078) by ensuring applications do not store sensitive data or credentials insecurely. [E4, E5]
Active Directory Configuration (M1015) mitigates Valid Accounts (T1078) by disabling legacy authentication and requiring modern authentication protocols. [E6, E7]
User Training (M1017) mitigates Valid Accounts (T1078) by training users to only accept valid push notifications and report suspicious ones. [E8, E9]
User Account Management (M1018) mitigates Valid Accounts (T1078) by regularly auditing user accounts for activity and deactivating or removing unnecessary ones. [E10, E11]
Privileged Account Management (M1026) mitigates Valid Accounts (T1078) by auditing domain and local accounts, permission levels, and default accounts, and following best practices for enterprise network design and administration. [E12, E13]

Paths: 5; hop counts: [2, 2, 2, 2, 2]; source passages: 13.

Source citations:

- [E1] cisa: AA23-319A / 3892:4022 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
- [E2] cisa: AA23-319A / 23:58 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
- [E3] cisa: AA23-319A / 2634:2651 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
- [E4] attack: attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 0:105 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E5] attack: attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 283:479 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--eed29e0f-59c1-4fab-8268-3f0571e90748 / 0:105 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--eed29e0f-59c1-4fab-8268-3f0571e90748 / 283:405 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--edaeb27a-9226-4805-ae45-87312a2dc013 / 0:88 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--edaeb27a-9226-4805-ae45-87312a2dc013 / 266:469 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 0:98 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E11] attack: attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 276:374 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E12] attack: attack:17.1:relationship--89887815-acfc-42f9-9172-81437cf9ff69 / 0:104 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E13] attack: attack:17.1:relationship--89887815-acfc-42f9-9172-81437cf9ff69 / 282:881 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 3

According to CISA, how do ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration?

Status: answer_ready_for_review

ALPHV Blackcat affiliates use Mega sync before data exfiltration. [E1, E2, E3]
ALPHV Blackcat affiliates use AnyDesk before data exfiltration. [E1, E2, E3]

Paths: 2; hop counts: [1, 1]; source passages: 3.

Source citations:

- [E1] cisa: AA23-353A / 3948:4124 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E2] cisa: AA23-353A / 23:54 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E3] cisa: AA23-353A / 3061:3078 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

