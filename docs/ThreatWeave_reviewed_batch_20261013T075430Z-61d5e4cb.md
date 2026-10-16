# Reviewed development batch import

AI-assisted source review and explicit source-role checks; human verification remains pending.
No held-out benchmark labels or reference answers were used.

## AA23-165A:table4:row03

Selected run: S:\ThreatWeave\work\development_batch\20261013T074906Z-23e86db5

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Source text:

AnyDesk
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software

Inherited source context:

Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

Inherited source context:

Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID


Supported generated relationships:

- LockBit Affiliates → USES → AnyDesk
- AnyDesk → USES_TECHNIQUE → Remote Access Tools

Identity resolution:

- LockBit Affiliates → local:AA23-165A:lockbit-affiliates (local)
- AnyDesk → local:AA23-165A:software:f084e63e6a62 (local)
- Remote Access Software → attack:T1219 (canonical)

## AA23-165A:table4:row04

Selected run: S:\ThreatWeave\work\development_batch\20261013T074906Z-23e86db5

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Source text:

Atera Remote Monitoring & Management (RMM)
Enables remote connections to network devices.
Enables remote control of victim’s network devices.
T1219
Remote Access Software

Inherited source context:

Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

Inherited source context:

Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID


Supported generated relationships:

- LockBit Affiliates → USES → Atera Remote Monitoring & Management (RMM)
- Atera Remote Monitoring & Management (RMM) → USES_TECHNIQUE → Remote Access Tools

Identity resolution:

- LockBit Affiliates → local:AA23-165A:lockbit-affiliates (local)
- Atera Remote Monitoring & Management (RMM) → local:AA23-165A:software:66a07ba808e8 (local)
- Remote Access Software → attack:T1219 (canonical)

## AA23-165A:table4:row05

Selected run: S:\ThreatWeave\work\development_batch\20261013T074906Z-23e86db5

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a

Source text:

Backstab
Terminates antimalware-protected processes.
Terminates endpoint detection and response (EDR)- protected processes.
T1562.001
Impair Defenses: Disable or Modify Tools

Inherited source context:

Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

Inherited source context:

Tool
Intended Use
Repurposed Use by LockBit Affiliates
MITRE ATT&CK ID


Supported generated relationships:

- LockBit Affiliates → USES → Backstab
- Backstab → USES_TECHNIQUE → Disable or Modify Tools

Identity resolution:

- LockBit Affiliates → local:AA23-165A:lockbit-affiliates (local)
- Backstab → local:AA23-165A:software:e0937ebfa805 (local)
- Impair Defenses: Disable or Modify Tools → attack:T1562.001 (canonical)

## AA23-136A:development:paragraph:27502

Selected run: S:\ThreatWeave\work\development_batch\20261013T073802Z-c6fd876b

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

Source text:

BianLian group actors used Rclone to exfiltrate data to a cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection.

Supported generated relationships:

- BianLian group actors → USES → Rclone

Identity resolution:

- BianLian group actors → local:AA23-136A:bianlian-group-actors (local)
- Rclone → attack:S1040 (canonical)

## AA23-353A:development:paragraph:10240

Selected run: S:\ThreatWeave\work\development_batch\20261013T073802Z-c6fd876b

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

Source text:

ALPHV Blackcat/ALPHV affiliates use the open-source framework Evilginx2 to obtain MFA credentials, login credentials, and session cookies for targeted networks.

Supported generated relationships:

- ALPHV Blackcat/ALPHV affiliates → USES → Evilginx2

Identity resolution:

- ALPHV Blackcat/ALPHV affiliates → local:AA23-353A:alphv-blackcat-alphv-affiliates (local)
- Evilginx2 → local:AA23-353A:software:9a41c1bd67a5 (local)

