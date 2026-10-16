# Development graph QA run

Graph-only development demonstration; generated answers require semantic review. These are not held-out evaluation scores.
Evidence is packed under a conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.

Model: llama3.1:8b; digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

## Question 1

According to CISA, how do LockBit Affiliates use AnyDesk? List the supplied ATT&CK mitigations for the reported technique and explain the practical guidance for each. Cite CISA observations and ATT&CK references separately.

Status: answer_ready_for_review

LockBit Affiliates use AnyDesk for remote control of victim's network devices. [E1, E2, E3]
CISA observes that AnyDesk enables remote connections to network devices and remote control of victim's network devices. [E1, E2, E3]
ATT&CK recommends Network Intrusion Prevention (M1031) to mitigate Remote Access Tools (T1219). [E4, E5]
Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services. [E5]
ATT&CK recommends Limit Hardware Installation (M1034) to mitigate Remote Access Tools (T1219). [E6, E7]
Block the use of IP-based KVM devices within the network if they are not required. [E7]
ATT&CK recommends Filter Network Traffic (M1037) to mitigate Remote Access Tools (T1219). [E8, E9]
Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access software. [E9]
ATT&CK recommends Execution Prevention (M1038) to mitigate Remote Access Tools (T1219). [E10, E11]
Use application control to mitigate installation and use of unapproved software that can be used for remote access. [E11]
ATT&CK recommends Disable or Remove Feature or Program (M1042) to mitigate Remote Access Tools (T1219). [E12, E13]
Consider disabling unnecessary remote connection functionality, including both unapproved software installations and specific features built into supported applications. [E13]

Paths: 5; hop counts: [3, 3, 3, 3, 3]; source passages: 13.

Source citations:

- [E1] cisa: AA23-165A / 13043:13178 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E2] cisa: AA23-165A / 12066:12132 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E3] cisa: AA23-165A / 12133:12204 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E4] attack: attack:17.1:relationship--d5c70727-794c-4404-b30d-0d798a62ad64 / 0:108 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E5] attack: attack:17.1:relationship--d5c70727-794c-4404-b30d-0d798a62ad64 / 286:422 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--9ae55ec5-a4f8-4619-8565-fe00433c574a / 0:107 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--9ae55ec5-a4f8-4619-8565-fe00433c574a / 285:368 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--80a23356-20b7-49a3-a48e-e0c04e2bff86 / 0:102 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--80a23356-20b7-49a3-a48e-e0c04e2bff86 / 280:424 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--54306888-1f93-4461-bcac-a56ae7073b31 / 0:100 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E11] attack: attack:17.1:relationship--54306888-1f93-4461-bcac-a56ae7073b31 / 278:393 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E12] attack: attack:17.1:relationship--fa4c9d5a-3329-4138-b6e1-990cd7935b87 / 0:116 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E13] attack: attack:17.1:relationship--fa4c9d5a-3329-4138-b6e1-990cd7935b87 / 294:463 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 2

According to CISA, what do BianLian group actors use Rclone for?

Status: answer_ready_for_review

BianLian group actors use Rclone. [E1]
The purpose of using Rclone is to exfiltrate data to a cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection. [E1]

Paths: 1; hop counts: [1]; source passages: 1.

Source citations:

- [E1] cisa: AA23-136A / 27502:27690 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

## Question 3

According to CISA, what do ALPHV Blackcat/ALPHV affiliates use Evilginx2 to obtain?

Status: answer_ready_for_review

ALPHV Blackcat/ALPHV affiliates use Evilginx2 [E1]
to obtain MFA credentials, login credentials, and session cookies [E1]

Paths: 1; hop counts: [1]; source passages: 1.

Source citations:

- [E1] cisa: AA23-353A / 10240:10400 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

