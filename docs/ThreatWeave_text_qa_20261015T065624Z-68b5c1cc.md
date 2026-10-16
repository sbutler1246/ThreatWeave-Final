# Development text-only QA run

Status: processed

Generated answers require semantic review. These development cases are not held-out evaluation scores.
The generator and its settings are shared with graph QA. Retrieval uses top-five cosine neighbors only, without graph expansion.
Evidence is packed under the same conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.
A successful response does not establish completeness or factual accuracy.

Model: llama3.1:8b; digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

## Question 1

According to CISA, what information does Raccoon Stealer steal? Explain the supplied ATT&CK mitigations for its web session cookie technique, citing observations and references separately.

Status: answer_ready_for_review

According to CISA, Raccoon Stealer steals information such as login credentials, session cookies, and other sensitive data. [E1]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is Audit (M1047), which involves implementing auditing for authentication activities and user logins to detect the use of stolen session cookies. [E2, E1]
Another ATT&CK mitigation for Steal Web Session Cookie (T1539) is Software Configuration (M1054), which involves configuring browsers or tasks to regularly delete persistent cookies. [E4, E3]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is also Restrict Web-Based Content (M1021), which involves restricting or blocking web-based content that could be used to extract session cookies or credentials stored in browsers. [E6, E5]
A physical second factor key that uses the target login domain as part of the negotiation protocol will prevent session cookie theft through proxy methods. [E7]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is also Multi-factor Authentication (M1032), which involves implementing Conditional Access policies with Token Protection to bind session tokens to their originating device and user. [E8, E7]
The ATT&CK mitigation for Steal Web Session Cookie (T1539) is also User Training (M1017), which involves training users to identify aspects of phishing attempts and not to run untrusted JavaScript in their browser. [E10, E9]

Text chunks: 5; source passages: 10; graph paths: zero.

Source citations:

- [E1] attack: attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 268:510 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E2] attack: attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 0:90 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E3] attack: attack:17.1:relationship--248a0d72-d9cd-43d3-985f-a33a49a79e8b / 285:810 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E4] attack: attack:17.1:relationship--248a0d72-d9cd-43d3-985f-a33a49a79e8b / 0:107 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E5] attack: attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 289:539 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 0:111 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 290:733 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 0:112 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 276:605 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 0:98 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 2

According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.

Status: answer_ready_for_review

Rhysida actors use valid accounts (T1078) for access by exploiting inactive or unnecessary accounts. [E1]
User Account Management (M1018) mitigation: Regularly audit user accounts for activity and deactivate or remove any that are no longer needed. [E2, E1]
Account Use Policies (M1036) mitigation: Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges. [E4, E3]
Application Developer Guidance (M1013) mitigation: Ensure that applications do not store sensitive data or credentials insecurely. [E6, E5]
Privileged Account Management (M1026) mitigation: Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [E8, E7]
Active Directory Configuration (M1015) mitigation: Disable legacy authentication, which does not support MFA, and require the use of modern authentication protocols instead. [E10, E9]

Text chunks: 5; source passages: 10; graph paths: zero.

Source citations:

- [E1] attack: attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 276:374 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E2] attack: attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 0:98 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E3] attack: attack:17.1:relationship--f2d01f19-b4e7-417a-a936-11af9386b867 / 273:451 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E4] attack: attack:17.1:relationship--f2d01f19-b4e7-417a-a936-11af9386b867 / 0:95 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E5] attack: attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 283:479 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 0:105 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--89887815-acfc-42f9-9172-81437cf9ff69 / 282:881 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--89887815-acfc-42f9-9172-81437cf9ff69 / 0:104 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--eed29e0f-59c1-4fab-8268-3f0571e90748 / 283:405 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--eed29e0f-59c1-4fab-8268-3f0571e90748 / 0:105 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 3

According to CISA, how do ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration?

Status: answer_ready_for_review

ALPHV Blackcat affiliates use AnyDesk before data exfiltration. [E4, E1]
ALPHV Blackcat affiliates use Mega sync before data exfiltration. [E4, E1]
ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration. [E4, E1]

Text chunks: 4; source passages: 6; graph paths: zero.

Source citations:

- [E1] cisa: AA23-353A / 5039:5986 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E2] cisa: AA23-353A / 23:54 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E3] cisa: AA23-353A / 3061:3078 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E4] cisa: AA23-353A / 3836:4785 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E5] cisa: AA23-353A / 4583:5323 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E6] cisa: AA23-353A / 10240:10400 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

