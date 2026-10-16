# Development text-only QA run

Status: processed

Generated answers require semantic review. These development cases are not held-out evaluation scores.
The generator and its settings are shared with graph QA. Retrieval uses top-five cosine neighbors only, without graph expansion.
Evidence is packed under the same conservative UTF-8 byte cap; exact shared-tokenizer packing remains pending.
A successful response does not establish completeness or factual accuracy.

Model: llama3.1:8b; digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

## Question 1

According to CISA, how do LockBit Affiliates use AnyDesk? List the supplied ATT&CK mitigations for the reported technique and explain the practical guidance for each. Cite CISA observations and ATT&CK references separately.

Status: answer_ready_for_review

LockBit Affiliates use AnyDesk for remote control of victim's network devices. [E1, E2]
AnyDesk enables remote connections to network devices. [E1]
Execution Prevention (M1038) mitigates Remote Access Tools (T1219) by preventing installation and use of unapproved software. [E7, E8]
Atera Remote Monitoring & Management (RMM) enables remote connections to network devices. [E5]
Advanced Port Scanner performs network scans and finds open TCP and UDP ports for exploitation. [E6]
Backstab terminates antimalware-protected processes and EDR-protected processes. [E4]

Text chunks: 5; source passages: 8; graph paths: zero.

Source citations:

- [E1] cisa: AA23-165A / 13043:13178 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E2] cisa: AA23-165A / 12066:12132 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E3] cisa: AA23-165A / 12133:12204 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E4] cisa: AA23-165A / 13350:13524 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E5] cisa: AA23-165A / 13179:13349 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E6] cisa: AA23-165A / 12695:12872 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E7] attack: attack:17.1:relationship--54306888-1f93-4461-bcac-a56ae7073b31 / 278:393 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json
- [E8] attack: attack:17.1:relationship--54306888-1f93-4461-bcac-a56ae7073b31 / 0:100 / https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

## Question 2

According to CISA, what do BianLian group actors use Rclone for?

Status: answer_ready_for_review

BianLian group actors use Rclone to exfiltrate data to a cloud account they control. [E1]

Text chunks: 5; source passages: 7; graph paths: zero.

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

Text chunks: 5; source passages: 7; graph paths: zero.

Source citations:

- [E1] cisa: AA23-353A / 10240:10400 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
- [E2] cisa: AA23-165A / 13350:13524 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E3] cisa: AA23-165A / 12066:12132 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E4] cisa: AA23-165A / 12133:12204 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E5] cisa: AA23-165A / 13043:13178 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E6] cisa: AA23-165A / 13179:13349 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- [E7] cisa: AA23-165A / 12695:12872 / https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

