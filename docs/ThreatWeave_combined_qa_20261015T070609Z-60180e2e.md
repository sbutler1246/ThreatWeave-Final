# Development combined text/graph QA run

Status: processed

Mode: hybrid_no_node2vec. Node2Vec enabled: False.
Generated answers require semantic review. These are development cases, not held-out scores.
RRF combines source-parent ranks; whole paths and text/context groups share a conservative UTF-8 byte cap.

Model: llama3.1:8b; digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

## Question 1

According to CISA, what information does Raccoon Stealer steal? Explain the supplied ATT&CK mitigations for its web session cookie technique, citing observations and references separately.

Status: answer_ready_for_review

Raccoon Stealer steals information including login credentials, browser history, and cookies. [E4]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is Audit (M1047), which involves implementing auditing for authentication activities and user logins to detect the use of stolen session cookies. [E5, E6]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is Restrict Web-Based Content (M1021), which involves restricting or blocking web-based content that could be used to extract session cookies or credentials stored in browsers. [E7, E8]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is User Training (M1017), which involves training users to identify aspects of phishing attempts and not to run untrusted JavaScript in their browser. [E9, E10]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is Multi-factor Authentication (M1032), which involves implementing a physical second factor key that uses the target login domain as part of the negotiation protocol. [E11, E12]

Paths: 4; hops: [3, 3, 3, 3]; text hits: 4; passages: 12.

Source citations:

- [E1] cisa: AA23-320A / 6480:6658 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E2] cisa: AA23-320A / 23:39 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E3] cisa: AA23-320A / 2870:2887 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E4] cisa: AA23-320A / 6635:6756 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- [E5] attack: attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 0:90 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 268:510 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 0:111 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 289:539 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 0:98 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 276:605 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E11] attack: attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 0:112 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E12] attack: attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 290:733 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 2

According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.

Status: answer_ready_for_review

Rhysida actors use valid accounts (T1078) for access by authenticating to internal VPN access points with compromised valid credentials. [E1, E2, E3]
Application Developer Guidance (M1013) mitigates Valid Accounts (T1078) by ensuring applications do not store sensitive data or credentials insecurely. [E4, E5]
User Account Management (M1018) mitigates Valid Accounts (T1078) by regularly auditing user accounts for activity and deactivating or removing any that are no longer needed. [E6, E7]
Active Directory Configuration (M1015) mitigates Valid Accounts (T1078) by disabling legacy authentication and requiring modern authentication protocols. [E8, E9]
Privileged Account Management (M1026) mitigates Valid Accounts (T1078) by auditing domain and local accounts, their permission levels, and default accounts, and following best practices for design and administration of an enterprise network. [E10, E11]
User Training (M1017) mitigates Valid Accounts (T1078) by training users to only accept valid push notifications and to report suspicious push notifications. [E12, E13]

Paths: 5; hops: [2, 2, 2, 2, 2]; text hits: 4; passages: 13.

Source citations:

- [E1] cisa: AA23-319A / 3892:4022 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
- [E2] cisa: AA23-319A / 23:58 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
- [E3] cisa: AA23-319A / 2634:2651 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
- [E4] attack: attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 0:105 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E5] attack: attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 283:479 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 0:98 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 276:374 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--eed29e0f-59c1-4fab-8268-3f0571e90748 / 0:105 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--eed29e0f-59c1-4fab-8268-3f0571e90748 / 283:405 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--89887815-acfc-42f9-9172-81437cf9ff69 / 0:104 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E11] attack: attack:17.1:relationship--89887815-acfc-42f9-9172-81437cf9ff69 / 282:881 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E12] attack: attack:17.1:relationship--edaeb27a-9226-4805-ae45-87312a2dc013 / 0:88 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E13] attack: attack:17.1:relationship--edaeb27a-9226-4805-ae45-87312a2dc013 / 266:469 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 3

According to CISA, how do ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration?

Status: answer_ready_for_review

ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration. [E1, E2, E3]
ALPHV Blackcat affiliates use AnyDesk in preparation of data exfiltration. [E1, E2, E3]
ALPHV Blackcat affiliates use Mega sync in preparation of data exfiltration. [E1, E2, E3]
After gaining access, ALPHV Blackcat affiliates create a user account 'aadmin' and use Kerberos token generation for domain access. [E4]
ALPHV Blackcat affiliates use Evilginx2 to obtain MFA credentials, login credentials, and session cookies. [E5, E6]
To evade detection, ALPHV Blackcat affiliates employ allowlisted applications such as Metasploit. [E5]
After installing on the domain controller, ALPHV Blackcat affiliates clear logs on the exchange server. [E5]
ALPHV Blackcat affiliates use Mega.nz or Dropbox to move, exfiltrate, and/or download victim data. [E5]

Paths: 2; hops: [1, 1]; text hits: 3; passages: 6.

Source citations:

- [E1] cisa: AA23-353A / 3948:4124 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E2] cisa: AA23-353A / 23:54 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E3] cisa: AA23-353A / 3061:3078 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E4] cisa: AA23-353A / 3836:4785 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E5] cisa: AA23-353A / 4583:5323 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E6] cisa: AA23-353A / 10240:10400 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

