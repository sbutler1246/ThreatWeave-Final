# Development full hybrid QA run

Status: processed_with_errors

Mode: hybrid. Node2Vec enabled: True.
Generated answers require semantic review. These are development cases, not held-out scores.
RRF combines source-parent ranks; whole paths and text/context groups share a conservative UTF-8 byte cap.

Model: llama3.1:8b; digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

## Question 1

According to CISA, how do LockBit Affiliates use AnyDesk? List the supplied ATT&CK mitigations for the reported technique and explain the practical guidance for each. Cite CISA observations and ATT&CK references separately.

Status: failed

ValueError: Generation did not finish within the configured output budget.

Source citations:

- [E1] cisa: AA23-165A / 13043:13178 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E2] cisa: AA23-165A / 12066:12132 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E3] cisa: AA23-165A / 12133:12204 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E4] attack: attack:17.1:relationship--54306888-1f93-4461-bcac-a56ae7073b31 / 0:100 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E5] attack: attack:17.1:relationship--54306888-1f93-4461-bcac-a56ae7073b31 / 278:393 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E6] attack: attack:17.1:relationship--80a23356-20b7-49a3-a48e-e0c04e2bff86 / 0:102 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E7] attack: attack:17.1:relationship--80a23356-20b7-49a3-a48e-e0c04e2bff86 / 280:424 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--d5c70727-794c-4404-b30d-0d798a62ad64 / 0:108 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E9] attack: attack:17.1:relationship--d5c70727-794c-4404-b30d-0d798a62ad64 / 286:422 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E10] attack: attack:17.1:relationship--9ae55ec5-a4f8-4619-8565-fe00433c574a / 0:107 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E11] attack: attack:17.1:relationship--9ae55ec5-a4f8-4619-8565-fe00433c574a / 285:368 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E12] attack: attack:17.1:relationship--fa4c9d5a-3329-4138-b6e1-990cd7935b87 / 0:116 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E13] attack: attack:17.1:relationship--fa4c9d5a-3329-4138-b6e1-990cd7935b87 / 294:463 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E14] cisa: AA23-165A / 13350:13524 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E15] cisa: AA23-165A / 13179:13349 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E16] cisa: AA23-165A / 12695:12872 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

## Question 2

According to CISA, what do BianLian group actors use Rclone for?

Status: answer_ready_for_review

BianLian group actors use Rclone to exfiltrate data. [E1]
The intended use of Rclone is to exfiltrate data to a cloud account they control on the same service. [E1]
BianLian group actors use Rclone to avoid typical file transfers/downloads and network-based exfiltration detection. [E1]

Paths: 1; hops: [1]; text hits: 5; passages: 7.

Source citations:

- [E1] cisa: AA23-136A / 27502:27690 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a
- [E2] cisa: AA23-165A / 13179:13349 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E3] cisa: AA23-165A / 12066:12132 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E4] cisa: AA23-165A / 12133:12204 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E5] cisa: AA23-165A / 13350:13524 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E6] cisa: AA23-165A / 13043:13178 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E7] cisa: AA23-165A / 12695:12872 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

## Question 3

According to CISA, what do ALPHV Blackcat/ALPHV affiliates use Evilginx2 to obtain?

Status: answer_ready_for_review

ALPHV Blackcat/ALPHV affiliates use Evilginx2 to obtain MFA credentials, login credentials, and session cookies. [E1]

Paths: 1; hops: [1]; text hits: 5; passages: 7.

Source citations:

- [E1] cisa: AA23-353A / 10240:10400 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E2] cisa: AA23-165A / 13350:13524 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E3] cisa: AA23-165A / 12066:12132 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E4] cisa: AA23-165A / 12133:12204 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E5] cisa: AA23-165A / 13043:13178 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E6] cisa: AA23-165A / 13179:13349 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E7] cisa: AA23-165A / 12695:12872 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

