# ThreatWeave benchmark author review

All 146 GT records and all 39 declared annotation scopes were confirmed reviewed and complete by Stephen Butler on 2026-10-05. The JSON verification records and all GT checkboxes agree. Supporting passages in additional_support are included in this confirmation. This records author review, not measured extraction or QA results.

Stephen Butler manually validated all 61 QA pairs first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. The selected 20-question final set contains eight actor/software/technique, eight technique/mitigation, and four cross-report comparisons. Finalize token-aware chunk IDs before running extraction evaluation.

Stephen Butler has also confirmed and verified all 39 ATT&CK reference records (RF001–RF039) on 2026-10-05. Each record in `reference_triples.json` now identifies him as the human reviewer. These reference associations remain separate from the 146 extraction gold triples.

## Triple candidates

### GT001 | AA23-165A

LockBit affiliates → USES → Advanced Internet Protocol (IP) Scanner

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 12511–12694

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Advanced Internet Protocol (IP) Scanner
> Performs network scans and shows network devices.
> Maps a victim’s network to identify potential access vectors.
> T1046
> Network Service Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT002 | AA23-165A

Advanced Internet Protocol (IP) Scanner → USES_TECHNIQUE → Network Service Discovery

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 12511–12694

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Advanced Internet Protocol (IP) Scanner
> Performs network scans and shows network devices.
> Maps a victim’s network to identify potential access vectors.
> T1046
> Network Service Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT003 | AA23-165A

LockBit affiliates → USES → Advanced Port Scanner

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 12695–12872

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Advanced Port Scanner
> Performs network scans.
> Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
> T1046
> Network Service Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT004 | AA23-165A

Advanced Port Scanner → USES_TECHNIQUE → Network Service Discovery

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 12695–12872

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Advanced Port Scanner
> Performs network scans.
> Finds open Transmission Control Protocol (TCP) and User Data Protocol (UDP) ports for exploitation.
> T1046
> Network Service Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT005 | AA23-165A

LockBit affiliates → USES → AnyDesk

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13043–13178

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> AnyDesk
> Enables remote connections to network devices.
> Enables remote control of victim’s network devices.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT006 | AA23-165A

AnyDesk → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13043–13178

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> AnyDesk
> Enables remote connections to network devices.
> Enables remote control of victim’s network devices.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT007 | AA23-165A

LockBit affiliates → USES → Atera Remote Monitoring & Management (RMM)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13179–13349

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Atera Remote Monitoring & Management (RMM)
> Enables remote connections to network devices.
> Enables remote control of victim’s network devices.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT008 | AA23-165A

Atera Remote Monitoring & Management (RMM) → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13179–13349

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Atera Remote Monitoring & Management (RMM)
> Enables remote connections to network devices.
> Enables remote control of victim’s network devices.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT009 | AA23-165A

LockBit affiliates → USES → Backstab

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13350–13524

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Backstab
> Terminates antimalware-protected processes.
> Terminates endpoint detection and response (EDR)- protected processes.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT010 | AA23-165A

Backstab → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13350–13524

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Backstab
> Terminates antimalware-protected processes.
> Terminates endpoint detection and response (EDR)- protected processes.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT011 | AA23-165A

LockBit affiliates → USES → Bat Armor

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13525–13670

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Bat Armor
> Generates .bat files using PowerShell scripts.
> Bypasses PowerShell execution policy.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT012 | AA23-165A

Bat Armor → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13525–13670

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Bat Armor
> Generates .bat files using PowerShell scripts.
> Bypasses PowerShell execution policy.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT013 | AA23-165A

LockBit affiliates → USES → BloodHound

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13671–13873

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Bloodhound
> Performs reconnaissance of AD for attack path management.
> Enables identification of AD relationships that can be exploited to gain access onto a victim’s network.
> T1482
> Domain Trust Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT014 | AA23-165A

BloodHound → USES_TECHNIQUE → Domain Trust Discovery

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13671–13873

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Bloodhound
> Performs reconnaissance of AD for attack path management.
> Enables identification of AD relationships that can be exploited to gain access onto a victim’s network.
> T1482
> Domain Trust Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT015 | AA23-165A

LockBit affiliates → USES → Chocolatey

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13874–14039

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Chocolatey
> Handles command-line package management on Microsoft Windows.
> Facilitates installation of LockBit affiliate actors’ tools.
> T1072
> Software Deployment Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT016 | AA23-165A

Chocolatey → USES_TECHNIQUE → Software Deployment Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 13874–14039

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Chocolatey
> Handles command-line package management on Microsoft Windows.
> Facilitates installation of LockBit affiliate actors’ tools.
> T1072
> Software Deployment Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT017 | AA23-165A

LockBit affiliates → USES → Defender Control

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14040–14199

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Defender Control
> Disables Microsoft Defender.
> Enables LockBit affiliate actors to bypass Microsoft Defender.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT018 | AA23-165A

Defender Control → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14040–14199

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Defender Control
> Disables Microsoft Defender.
> Enables LockBit affiliate actors to bypass Microsoft Defender.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT019 | AA23-165A

LockBit affiliates → USES → ExtPassword

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14200–14356

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> ExtPassword
> Recovers passwords from Windows systems.
> Obtains credentials for network access and exploitation.
> T1003
> Operating System (OS) Credential Dumping

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT020 | AA23-165A

ExtPassword → USES_TECHNIQUE → OS Credential Dumping

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14200–14356

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> ExtPassword
> Recovers passwords from Windows systems.
> Obtains credentials for network access and exploitation.
> T1003
> Operating System (OS) Credential Dumping

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT021 | AA23-165A

LockBit affiliates → USES → FreeFileSync

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14601–14798

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> FreeFileSync
> Facilitates cloud-based file synchronization.
> Facilitates cloud-based file synchronization for data exfiltration.
> T1567.002
> Exfiltration Over Web Service: Exfiltration to Cloud Storage

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT022 | AA23-165A

FreeFileSync → USES_TECHNIQUE → Exfiltration to Cloud Storage

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14601–14798

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> FreeFileSync
> Facilitates cloud-based file synchronization.
> Facilitates cloud-based file synchronization for data exfiltration.
> T1567.002
> Exfiltration Over Web Service: Exfiltration to Cloud Storage

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT023 | AA23-165A

LockBit affiliates → USES → GMER

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14799–14909

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> GMER
> Removes rootkits.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT024 | AA23-165A

GMER → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 14799–14909

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> GMER
> Removes rootkits.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT025 | AA23-165A

LockBit affiliates → USES → Ligolo

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15188–15390

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Ligolo
> Establishes SOCKS5 or TCP tunnels from a reverse connection for pen testing.
> Enables connections to systems within the victim’s network via reverse tunneling.
> T1095
> Non-Application Layer Protocol

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT026 | AA23-165A

Ligolo → USES_TECHNIQUE → Non-Application Layer Protocol

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15188–15390

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Ligolo
> Establishes SOCKS5 or TCP tunnels from a reverse connection for pen testing.
> Enables connections to systems within the victim’s network via reverse tunneling.
> T1095
> Non-Application Layer Protocol

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT027 | AA23-165A

LockBit affiliates → USES → LostMyPassword

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15391–15531

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> LostMyPassword
> Recovers passwords from Windows systems.
> Obtains credentials for network access and exploitation.
> T1003
> OS Credential Dumping

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT028 | AA23-165A

LostMyPassword → USES_TECHNIQUE → OS Credential Dumping

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15391–15531

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> LostMyPassword
> Recovers passwords from Windows systems.
> Obtains credentials for network access and exploitation.
> T1003
> OS Credential Dumping

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT029 | AA23-165A

LockBit affiliates → USES → MEGA Ltd MegaSync

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15532–15734

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> MEGA Ltd MegaSync
> Facilitates cloud-based file synchronization.
> Facilitates cloud-based file synchronization for data exfiltration.
> T1567.002
> Exfiltration Over Web Service: Exfiltration to Cloud Storage

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT030 | AA23-165A

MEGA Ltd MegaSync → USES_TECHNIQUE → Exfiltration to Cloud Storage

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15532–15734

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> MEGA Ltd MegaSync
> Facilitates cloud-based file synchronization.
> Facilitates cloud-based file synchronization for data exfiltration.
> T1567.002
> Exfiltration Over Web Service: Exfiltration to Cloud Storage

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT031 | AA23-165A

LockBit affiliates → USES → Microsoft Sysinternals ProcDump

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15735–16016

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Microsoft Sysinternals ProcDump
> Monitors applications for central processing unit (CPU) spikes and generates crash dumps during a spike.
> Obtains credentials by dumping the contents of Local Security Authority Subsystem Service (LSASS).
> T1003.001
> OS Credential Dumping: LSASS Memory

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT032 | AA23-165A

Microsoft Sysinternals ProcDump → USES_TECHNIQUE → LSASS Memory

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 15735–16016

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Microsoft Sysinternals ProcDump
> Monitors applications for central processing unit (CPU) spikes and generates crash dumps during a spike.
> Obtains credentials by dumping the contents of Local Security Authority Subsystem Service (LSASS).
> T1003.001
> OS Credential Dumping: LSASS Memory

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT033 | AA23-165A

LockBit affiliates → USES → PasswordFox

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 16511–16660

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PasswordFox
> Recovers passwords from Firefox Browser.
> Obtains credentials for network access and exploitation.
> T1555.003
> Credentials from Web Browsers

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT034 | AA23-165A

PasswordFox → USES_TECHNIQUE → Credentials from Web Browsers

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 16511–16660

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PasswordFox
> Recovers passwords from Firefox Browser.
> Obtains credentials for network access and exploitation.
> T1555.003
> Credentials from Web Browsers

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT035 | AA23-165A

LockBit affiliates → USES → PCHunter

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 16661–16848

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PCHunter
> Enables advanced task management including system processes and kernels.
> Terminates and circumvents EDR processes and services.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT036 | AA23-165A

PCHunter → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 16661–16848

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PCHunter
> Enables advanced task management including system processes and kernels.
> Terminates and circumvents EDR processes and services.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT037 | AA23-165A

LockBit affiliates → USES → PowerTool

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 16849–17040

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PowerTool
> Removes rootkits, as well as detecting, analyzing, and fixing kernel structure modifications.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT038 | AA23-165A

PowerTool → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 16849–17040

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PowerTool
> Removes rootkits, as well as detecting, analyzing, and fixing kernel structure modifications.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT039 | AA23-165A

LockBit affiliates → USES → Process Hacker

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17041–17161

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Process Hacker
> Removes rootkits.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT040 | AA23-165A

Process Hacker → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17041–17161

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Process Hacker
> Removes rootkits.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT041 | AA23-165A

LockBit affiliates → USES → PuTTY Link (Plink)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17162–17307

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PuTTY Link (Plink)
> Automates Secure Shell (SSH) actions on Windows.
> Enables LockBit affiliate actors to avoid detection.
> T1572
> Protocol Tunneling

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT042 | AA23-165A

PuTTY Link (Plink) → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17162–17307

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> PuTTY Link (Plink)
> Automates Secure Shell (SSH) actions on Windows.
> Enables LockBit affiliate actors to avoid detection.
> T1572
> Protocol Tunneling

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT043 | AA23-165A

LockBit affiliates → USES → Seatbelt

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17436–17599

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Seatbelt
> Performs numerous security-oriented checks.
> Performs numerous security-oriented checks to enumerate system information.
> T1082
> System Information Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT044 | AA23-165A

Seatbelt → USES_TECHNIQUE → System Information Discovery

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17436–17599

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Seatbelt
> Performs numerous security-oriented checks.
> Performs numerous security-oriented checks to enumerate system information.
> T1082
> System Information Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT045 | AA23-165A

LockBit affiliates → USES → ScreenConnect (also known as ConnectWise)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17600–17808

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> ScreenConnect (also known as ConnectWise)
> Enables remote connections to network devices for management.
> Enables LockBit affiliate actors to remotely connect to a victim’s systems.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT046 | AA23-165A

ScreenConnect (also known as ConnectWise) → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17600–17808

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> ScreenConnect (also known as ConnectWise)
> Enables remote connections to network devices for management.
> Enables LockBit affiliate actors to remotely connect to a victim’s systems.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT047 | AA23-165A

LockBit affiliates → USES → SoftPerfect Network Scanner

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17809–18008

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> SoftPerfect Network Scanner
> Performs network scans for systems management.
> Enables LockBit affiliate actors to obtain information about a victim’s systems and network.
> T1046
> Network Service Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT048 | AA23-165A

SoftPerfect Network Scanner → USES_TECHNIQUE → Network Service Discovery

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 17809–18008

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> SoftPerfect Network Scanner
> Performs network scans for systems management.
> Enables LockBit affiliate actors to obtain information about a victim’s systems and network.
> T1046
> Network Service Discovery

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT049 | AA23-165A

LockBit affiliates → USES → Splashtop

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18009–18231

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Splashtop
> Enables remote connections to network devices for management.
> Enables LockBit affiliate actors to remotely connect to systems over Remote Desktop Protocol (RDP).
> T1021.001
> Remote Services: Remote Desktop Protocol

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT050 | AA23-165A

Splashtop → USES_TECHNIQUE → Remote Desktop Protocol

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18009–18231

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> Splashtop
> Enables remote connections to network devices for management.
> Enables LockBit affiliate actors to remotely connect to systems over Remote Desktop Protocol (RDP).
> T1021.001
> Remote Services: Remote Desktop Protocol

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT051 | AA23-165A

LockBit affiliates → USES → TDSSKiller

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18232–18348

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> TDSSKiller
> Removes rootkits.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT052 | AA23-165A

TDSSKiller → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18232–18348

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> TDSSKiller
> Removes rootkits.
> Terminates and removes EDR software.
> T1562.001
> Impair Defenses: Disable or Modify Tools

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT053 | AA23-165A

LockBit affiliates → USES → TeamViewer

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18349–18526

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> TeamViewer
> Enables remote connections to network devices for management.
> Enables LockBit affiliate actors to remotely connect to a victim’s systems.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT054 | AA23-165A

TeamViewer → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18349–18526

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> TeamViewer
> Enables remote connections to network devices for management.
> Enables LockBit affiliate actors to remotely connect to a victim’s systems.
> T1219
> Remote Access Software

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT055 | AA23-165A

LockBit affiliates → USES → ThunderShell

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18527–18760

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> ThunderShell
> Facilitates remote access via Hypertext Transfer Protocol (HTTP) requests.
> Enables LockBit affiliate actors to remotely access systems while encrypting network traffic.
> T1071.001
> Application Layer Protocol: Web Protocols

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT056 | AA23-165A

ThunderShell → USES_TECHNIQUE → Web Protocols

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18527–18760

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> ThunderShell
> Facilitates remote access via Hypertext Transfer Protocol (HTTP) requests.
> Enables LockBit affiliate actors to remotely access systems while encrypting network traffic.
> T1071.001
> Application Layer Protocol: Web Protocols

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT057 | AA23-165A

LockBit affiliates → USES → WinSCP

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18761–18956

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> WinSCP
> Facilitates file transfer using SSH File Transfer Protocol for Microsoft Windows.
> Enables data exfiltration via the SSH File Transfer Protocol.
> T1048
> Exfiltration Over Alternative Protocol

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT058 | AA23-165A

WinSCP → USES_TECHNIQUE → Exfiltration Over Alternative Protocol

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a) | Normalized document offsets 18761–18956

Inherited source caption: Table 4: Freeware and Open-Source Tools Used by LockBit Affiliates

> WinSCP
> Facilitates file transfer using SSH File Transfer Protocol for Microsoft Windows.
> Enables data exfiltration via the SSH File Transfer Protocol.
> T1048
> Exfiltration Over Alternative Protocol

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT059 | AA23-061A

Royal actors → USES → Chisel

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Source support and identities were verified by Stephen Butler on 2026-10-04. The full Royal paragraph scope is complete. The relationship retains historical/advisory context; it does not establish that every use of the software employs this technique.

### GT060 | AA23-061A

Chisel → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Source support and identities were verified by Stephen Butler on 2026-10-04. The full Royal paragraph scope is complete. The relationship retains historical/advisory context; it does not establish that every use of the software employs this technique.

### GT061 | AA24-109A

Akira threat actors → USES → Mimikatz

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT062 | AA24-109A

Mimikatz → USES_TECHNIQUE → OS Credential Dumping

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT063 | AA24-109A

Akira threat actors → USES → LaZagne

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT064 | AA24-109A

LaZagne → USES_TECHNIQUE → OS Credential Dumping

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT065 | AA24-109A

Akira threat actors → USES → ngrok

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 11788–12162

> The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572], to initiate encrypted sessions that bypass perimeter monitoring. They also use PowerShell and Windows Management Instrumentation Command-line (WMIC) [T1059.001] to disable services and execute malicious scripts.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT066 | AA24-109A

ngrok → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 11788–12162

> The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572], to initiate encrypted sessions that bypass perimeter monitoring. They also use PowerShell and Windows Management Instrumentation Command-line (WMIC) [T1059.001] to disable services and execute malicious scripts.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT067 | AA24-109A

Akira threat actors → USES → FileZilla

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT068 | AA24-109A

FileZilla → USES_TECHNIQUE → Archive via Utility

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT069 | AA24-109A

Akira threat actors → USES → WinRAR

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT070 | AA24-109A

WinRAR → USES_TECHNIQUE → Archive via Utility

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT071 | AA24-109A

Akira threat actors → USES → WinSCP

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT072 | AA24-109A

WinSCP → USES_TECHNIQUE → Exfiltration Over Alternative Protocol

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT073 | AA24-109A

Akira threat actors → USES → Rclone

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT074 | AA24-109A

Rclone → USES_TECHNIQUE → Exfiltration Over Alternative Protocol

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT075 | AA24-109A

ngrok → USES_TECHNIQUE → Proxy

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 12198–12791

> Akira threat actors leverage tools such as FileZilla and WinRAR to collect data [T1560.001] and WinSCP and RClone to exfiltrate data [T1048]. To establish C2 channels, threat actors leverage readily available tools like AnyDesk, MobaXterm, RustDesk, and Cloudflare Tunnel. These tools enable exfiltration through various protocols such as File Transfer Protocol (FTP), Secure File Transfer Protocol (SFTP), and cloud storage services like Mega [T1537], to connect to exfiltration servers. In some instances, Akira threat actors use Ngrok to create secure tunnels for data exfiltration [T1090].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT076 | AA24-131A

Black Basta affiliates → USES → Backstab

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT077 | AA24-131A

Backstab → USES_TECHNIQUE → Disable or Modify Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT078 | AA23-352A

Play ransomware actors → USES → Mimikatz

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: This paragraph contains 12 eligible relationships in the permitted schema: GT078, GT118-GT127, and the existing Mimikatz → USES_TECHNIQUE → OS Credential Dumping (T1003) record GT062. GT062 already retains this Play paragraph in additional_support; the author confirmed the Play supporting passage and complete scope on 2026-10-05, without creating a duplicate canonical triple.

### GT079 | AA23-075A

LockBit 3.0 affiliates → USES → Rclone

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Seven eligible relationships in this paragraph are represented by GT079, GT080, and GT128-GT132. Review StealBit and MEGA use, the reported T1567.002 mappings, and the final generic file-sharing statement (T1567). StealBit previously being used with LockBit 2.0 is retained as source qualification, not merged into the LockBit 3.0 actor identity. TA0010 identifies a tactic, so it is not treated as a technique. The author confirmed all seven relationships and scope completion on 2026-10-05.

### GT080 | AA23-075A

Rclone → USES_TECHNIQUE → Exfiltration to Cloud Storage

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT081 | AA25-071A

Medusa actors → USES → Mimikatz

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Eight eligible relationships in the permitted schema are represented by GT081, GT082, and GT133-GT138. Review Windows Task Manager and comsvcs.dll use and their T1003.001 mappings, Medusa actor use of T1003.001, and local Group Policy Editor use. GT138 preserves disabling Windows Defender during LSASS exfiltration and re-enabling it afterward. TA0006 is the Credential Access tactic, not a technique. No additional technique ID is assumed for the uncited Defender sentence. The author confirmed review of all eight relationships and the full scope on 2026-10-05.

### GT082 | AA25-071A

Mimikatz → USES_TECHNIQUE → LSASS Memory

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT083 | AA25-071A

Medusa actors → USES → Rclone

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 17253–17441

> (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: This paragraph has four eligible relationships represented by GT083, GT139, GT140, and GT080 (Rclone → USES_TECHNIQUE → T1567.002). GT080 already retains this Medusa paragraph in additional_support; the author confirmed that support without duplicating the canonical triple. Bandizip creates archives; Rclone facilitates exfiltration to Medusa C2 servers. The author confirmed all four relationships and full scope completion on 2026-10-05.

### GT084 | AA25-071A

Medusa actors → USES → PsExec

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: eHorus, N-able, and BeyondTrust are now recorded in GT141-GT146, each with Medusa actor use and the paragraph-supported T1219 relationship. Their identities retain the source names without guessing vendor products. The author confirmed these records and full paragraph scope completion on 2026-10-05. Preserve the distinction between identifying files for encryption and a claim that a named remote-access tool itself performs encryption.

### GT085 | AA25-071A

PsExec → USES_TECHNIQUE → Service Execution

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT086 | AA25-071A

Medusa actors → USES → AnyDesk

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT087 | AA25-071A

AnyDesk → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT088 | AA25-071A

Medusa actors → USES → Atera

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT089 | AA25-071A

Atera → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT090 | AA25-071A

Medusa actors → USES → ConnectWise

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT091 | AA25-071A

ConnectWise → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT092 | AA25-071A

Medusa actors → USES → SimpleHelp

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT093 | AA25-071A

SimpleHelp → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT094 | AA25-071A

Medusa actors → USES → Splashtop

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT095 | AA25-071A

Splashtop → USES_TECHNIQUE → Remote Access Tools

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

### GT096 | AA23-061A

Royal actors → USES → Secure Shell (SSH) client

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: User explicitly confirmed Royal actors used this named tool in the source paragraph. Historical/advisory scope is retained; local identity does not assert an ATT&CK product match. SSH client is a generic source description, not a specific product. The full paragraph scope is complete.

### GT097 | AA23-061A

Royal actors → USES → PuTTY

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: User explicitly confirmed Royal actors used this named tool in the source paragraph. Historical/advisory scope is retained; local identity does not assert an ATT&CK product match. The full paragraph scope is complete.

### GT098 | AA23-061A

Royal actors → USES → OpenSSH

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: User explicitly confirmed Royal actors used this named tool in the source paragraph. Historical/advisory scope is retained; local identity does not assert an ATT&CK product match. The full paragraph scope is complete.

### GT099 | AA23-061A

Royal actors → USES → MobaXterm

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: User explicitly confirmed Royal actors used this named tool in the source paragraph. Historical/advisory scope is retained; local identity does not assert an ATT&CK product match. The full paragraph scope is complete.

### GT100 | AA23-061A

Secure Shell (SSH) client → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Human review confirmed that the paragraph T1572 annotation applies to this listed tool's reported use by Royal actors. The full paragraph scope is complete. This is an advisory-specific mapping, not a claim about intrinsic capability or every use of the tool. SSH client remains a generic source description, not a specific product.

### GT101 | AA23-061A

PuTTY → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Human review confirmed that the paragraph T1572 annotation applies to this listed tool's reported use by Royal actors. The full paragraph scope is complete. This is an advisory-specific mapping, not a claim about intrinsic capability or every use of the tool.

### GT102 | AA23-061A

OpenSSH → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Human review confirmed that the paragraph T1572 annotation applies to this listed tool's reported use by Royal actors. The full paragraph scope is complete. This is an advisory-specific mapping, not a claim about intrinsic capability or every use of the tool.

### GT103 | AA23-061A

MobaXterm → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Human review confirmed that the paragraph T1572 annotation applies to this listed tool's reported use by Royal actors. The full paragraph scope is complete. This is an advisory-specific mapping, not a claim about intrinsic capability or every use of the tool.

### GT104 | AA23-061A

Royal actors → USES_TECHNIQUE → Protocol Tunneling

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a) | Normalized document offsets 6445–6615

> Historically, Royal actors were observed leveraging Chisel, Secure Shell (SSH) client, PuTTY, OpenSSH, and MobaXterm [T1572], to communicate with their C2 infrastructure.

- [x] Source supports the complete relationship and actor scope.
- [x] Canonical/local identity is correct.
- [x] All other eligible facts in this annotation scope are recorded.

Review note: Human review confirmed that the paragraph attributes T1572 to Royal actors. This attribution is supported by the sentence context rather than graph inference alone. The full paragraph scope is complete.

### GT105 | AA24-109A

Akira threat actors → USES → SoftPerfect

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Actor attribution uses paragraph context: actors refers back to Akira threat actors named in the preceding sentences; the full paragraph is retained as evidence. Stephen Butler confirmed this attribution on 2026-10-04. The software name is retained locally without assuming an ATT&CK identity or a more specific product.

### GT106 | AA24-109A

Akira threat actors → USES → Advanced IP Scanner

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Actor attribution uses paragraph context: actors refers back to Akira threat actors named in the preceding sentences; the full paragraph is retained as evidence. Stephen Butler confirmed this attribution on 2026-10-04. The software name is retained locally without assuming an ATT&CK identity or a more specific product.

### GT107 | AA24-109A

Akira threat actors → USES → NetScan

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 8222–8881

> According to the authoring organizations and open source reporting, Akira threat actors leverage post-exploitation techniques, such as Kerberoasting,8 to extract credentials stored in the process memory of the Local Security Authority Subsystem Service (LSASS)9 [T1003.001]. Akira threat actors also use credential scraping tools [T1003], like Mimikatz and LaZagne, to aid in privilege escalation. For network discovery and reconnaissance, actors use tools like SoftPerfect, Advanced IP Scanner, and NetScan [T1016]. net Windows commands [T1059.003] are used to identify domain controllers [T1018] and gather information on domain trust relationships [T1482].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Actor attribution uses paragraph context: actors refers back to Akira threat actors named in the preceding sentences; the full paragraph is retained as evidence. Stephen Butler confirmed this attribution on 2026-10-04. The software name is retained locally without assuming an ATT&CK identity or a more specific product.

### GT108 | AA24-109A

Akira threat actors → USES → PowerShell

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 11788–12162

> The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572], to initiate encrypted sessions that bypass perimeter monitoring. They also use PowerShell and Windows Management Instrumentation Command-line (WMIC) [T1059.001] to disable services and execute malicious scripts.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Stephen Butler confirmed the explicit tool-use fact on 2026-10-04. They refers back to Akira threat actors in the preceding sentence; the full paragraph is retained. Software identity is preserved locally without asserting an ATT&CK software match. PowerShell software is distinct from the Technique named PowerShell (T1059.001).

### GT109 | AA24-109A

Akira threat actors → USES → Windows Management Instrumentation Command-line (WMIC)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | Normalized document offsets 11788–12162

> The authoring organizations observed Akira threat actors establishing command and control (C2) communications by using tunneling utilities, such as Ngrok [T1572], to initiate encrypted sessions that bypass perimeter monitoring. They also use PowerShell and Windows Management Instrumentation Command-line (WMIC) [T1059.001] to disable services and execute malicious scripts.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Stephen Butler confirmed the explicit tool-use fact on 2026-10-04. They refers back to Akira threat actors in the preceding sentence; the full paragraph is retained. Software identity is preserved locally without asserting an ATT&CK software match. Source groups WMIC beside T1059.001 (PowerShell); ATT&CK identifies Windows Management Instrumentation as T1047. This record verifies tool use only, not either technique mapping.

### GT110 | AA24-131A

Black Basta affiliates → USES → PowerShell software

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Full paragraph retained as evidence. Preserve Black Basta affiliate/advisory scope. The source explicitly reports affiliate use of PowerShell software; no ATT&CK software identity is assumed.

### GT111 | AA24-131A

PowerShell software → USES_TECHNIQUE → PowerShell technique (T1059.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Full paragraph retained as evidence. Preserve Black Basta affiliate/advisory scope. PowerShell software and the Technique named PowerShell are distinct entity types. This maps the reported use, not every use of the software.

### GT112 | AA24-131A

Black Basta affiliates → USES_TECHNIQUE → PowerShell technique (T1059.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Full paragraph retained as evidence. Preserve Black Basta affiliate/advisory scope. Actor-to-technique attribution follows the explicit report of affiliates using PowerShell [T1059.001].

### GT113 | AA24-131A

Black Basta affiliates → USES_TECHNIQUE → Disable or Modify Tools (T1562.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Full paragraph retained as evidence. Preserve Black Basta affiliate/advisory scope. The advisory reports affiliates deploying Backstab in some instances to disable EDR tooling [T1562.001]. Preserve the in some instances qualification; attribution is supported by the source activity description, not graph inference alone.

### GT114 | AA24-131A

Black Basta affiliates → USES → Rclone

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The first sentence explicitly states that Black Basta affiliates use RClone for data exfiltration before encryption. Source spelling RClone is preserved in the quote; Rclone is the canonical Software name for S1040 in ATT&CK 17.1. No particular exfiltration technique ID is inferred from this sentence.

### GT115 | AA24-131A

Black Basta affiliates → USES → vssadmin.exe

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Affiliates refers back to Black Basta affiliates in the same paragraph. The source explicitly names vssadmin.exe for deletion of volume shadow copies. Retain full paragraph context and the local tool identity.

### GT116 | AA24-131A

vssadmin.exe → USES_TECHNIQUE → Inhibit System Recovery (T1490)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly links the reported vssadmin.exe use for deletion of volume shadow copies to T1490 (Inhibit System Recovery). This is the reported use in this advisory, not every use of the utility.

### GT117 | AA24-131A

Black Basta affiliates → USES_TECHNIQUE → Inhibit System Recovery (T1490)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a) | Normalized document offsets 7045–7795

> Black Basta affiliates use RClone to facilitate data exfiltration prior to encryption. Prior to exfiltration, cybersecurity researchers have observed Black Basta affiliates using PowerShell [T1059.001] to disable antivirus products, and in some instances, deploying a tool called Backstab, designed to disable endpoint detection and response (EDR) tooling [T1562.001].[3] Once antivirus programs are terminated, a ChaCha20 algorithm with an RSA-4096 public key fully encrypts files [T1486]. A .basta or otherwise random file extension is added to file names and a ransom note titled readme.txt is left on the compromised system.[4] To further inhibit system recovery, affiliates use the vssadmin.exe program to delete volume shadow copies [T1490].[5]

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source describes Black Basta affiliates inhibiting system recovery by deleting volume shadow copies, with T1490. Actor attribution follows the full paragraph context and explicit activity description.

### GT118 | AA23-352A

Play ransomware actors → USES → Cobalt Strike

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Cobalt Strike is explicitly named among the C2 applications used by Play ransomware actors. Its canonical identity is S0154 in the frozen ATT&CK 17.1 reference.

### GT119 | AA23-352A

Play ransomware actors → USES → SystemBC

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: SystemBC is explicitly named among the C2 applications used by Play ransomware actors. Retain a local Software identity because this name has no matching Software object in the frozen ATT&CK 17.1 reference.

### GT120 | AA23-352A

Play ransomware actors → USES → PsExec

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly says Play ransomware actors use tools like PsExec to assist with lateral movement and file execution. No uncited technique ID is inferred for PsExec.

### GT121 | AA23-352A

Play ransomware actors → USES → WinPEAS

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: According to open source reporting, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS). Preserve that reporting qualification and the source-provided long name.

### GT122 | AA23-352A

Play ransomware actors → USES_TECHNIQUE → Unsecured Credentials (T1552)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The ransomware actors refers to Play ransomware actors in the preceding sentence. The source explicitly describes searching for unsecured credentials and cites T1552.

### GT123 | AA23-352A

Play ransomware actors → USES_TECHNIQUE → OS Credential Dumping (T1003)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source describes Play ransomware actors using the Mimikatz credential dumper to gain domain administrator access and explicitly cites T1003. Retain this parent technique rather than inventing a sub-technique.

### GT124 | AA23-352A

WinPEAS → USES_TECHNIQUE → Command and Scripting Interpreter (T1059)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly attaches T1059 to its reported WinPEAS use. This records the advisory mapping to Command and Scripting Interpreter; it does not assert that every use of WinPEAS employs this technique. Preserve the open source reporting qualification.

### GT125 | AA23-352A

Play ransomware actors → USES_TECHNIQUE → Command and Scripting Interpreter (T1059)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The advisory explicitly describes Play ransomware actors using WinPEAS and cites T1059. Preserve the parent technique ID and the According to open source reporting qualification.

### GT126 | AA23-352A

Play ransomware actors → USES_TECHNIQUE → Lateral Tool Transfer (T1570)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: Actors refers to Play ransomware actors in the full paragraph. Distributing executables is explicitly linked to T1570 (Lateral Tool Transfer).

### GT127 | AA23-352A

Play ransomware actors → USES_TECHNIQUE → Group Policy Modification (T1484.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | Normalized document offsets 5544–6198

> Play ransomware actors use command and control (C2) applications, including Cobalt Strike and SystemBC, and tools like PsExec to assist with lateral movement and file execution. Once established on a network, the ransomware actors search for unsecured credentials [T1552] and use the Mimikatz credential dumper to gain domain administrator access [T1003]. According to open source reporting,3 to further enumerate vulnerabilities, Play ransomware actors use Windows Privilege Escalation Awesome Scripts (WinPEAS) [T1059] to search for additional privilege escalation paths. Actors then distribute executables [T1570] via Group Policy Objects [T1484.001].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source describes Play ransomware actors distributing executables via Group Policy Objects and explicitly cites T1484.001 (Group Policy Modification). Preserve the full sub-technique ID.

### GT128 | AA23-075A

LockBit 3.0 affiliates → USES → StealBit

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly says LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0. StealBit is the canonical Software name for S1200 in ATT&CK 17.1. Preserve the historical LockBit 2.0 qualification; the paragraph does not independently identify a LockBit 2.0 actor group. TA0010 is the Exfiltration tactic, not a technique ID, so no StealBit-to-technique relationship is invented.

### GT129 | AA23-075A

LockBit 3.0 affiliates → USES → MEGA

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly includes MEGA among the publicly available file-sharing services used by LockBit 3.0 affiliates to exfiltrate sensitive company data before encryption. Keep MEGA as a local named software service; no specific MEGA client or ATT&CK Software ID is assumed.

### GT130 | AA23-075A

MEGA → USES_TECHNIQUE → Exfiltration to Cloud Storage (T1567.002)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly cites T1567.002 beside MEGA in the described exfiltration activity. This records the reported use of MEGA for Exfiltration to Cloud Storage, not every legitimate use of the service.

### GT131 | AA23-075A

LockBit 3.0 affiliates → USES_TECHNIQUE → Exfiltration to Cloud Storage (T1567.002)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: LockBit 3.0 affiliates are explicitly described using rclone and MEGA to exfiltrate data before encryption, with T1567.002. Preserve the full sub-technique ID.

### GT132 | AA23-075A

LockBit 3.0 affiliates → USES_TECHNIQUE → Exfiltration Over Web Service (T1567)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a) | Normalized document offsets 6201–6862

> LockBit 3.0 affiliates use Stealbit, a custom exfiltration tool used previously with LockBit 2.0 [TA0010]; rclone, an open-source command line cloud storage manager [T1567.002]; and publicly available file sharing services, such as MEGA [T1567.002], to exfiltrate sensitive company data files prior to encryption. While rclone and many publicly available file sharing services are primarily used for legitimate purposes, they can also be used by threat actors to aid in system compromise, network exploration, or data exfiltration. LockBit 3.0 affiliates often use other publicly available file sharing services to exfiltrate data as well [T1567] (see Table 1).

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The final sentence explicitly says LockBit 3.0 affiliates often use other publicly available file-sharing services to exfiltrate data and cites T1567. Record this generic service-use fact as Exfiltration Over Web Service. Unnamed services are not invented as individually identified Software nodes. The earlier general statement about legitimate tools being usable by threat actors does not establish further LockBit-specific techniques.

### GT133 | AA25-071A

Medusa actors → USES → Windows Task Manager

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The updated paragraph explicitly names Windows Task Manager among the tools Medusa actors use for LSASS dumping to harvest credentials and aid lateral movement.

### GT134 | AA25-071A

Medusa actors → USES → comsvcs.dll

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The updated paragraph explicitly names comsvcs.dll among the software components Medusa actors use for LSASS dumping. Retain the local component identity; no command line or invocation method is supplied by this paragraph.

### GT135 | AA25-071A

Windows Task Manager → USES_TECHNIQUE → LSASS Memory (T1003.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The coordinated list of Mimikatz, Windows Task Manager, and comsvcs.dll is explicitly described as being used for LSASS dumping and linked to T1003.001. This is the reported Medusa use, not every legitimate use of Task Manager.

### GT136 | AA25-071A

comsvcs.dll → USES_TECHNIQUE → LSASS Memory (T1003.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly includes comsvcs.dll in the tools/components used for LSASS dumping, with T1003.001. Preserve the reported credential-harvesting and lateral-movement purposes without inventing further technique IDs.

### GT137 | AA25-071A

Medusa actors → USES_TECHNIQUE → LSASS Memory (T1003.001)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly describes Medusa actors performing LSASS dumping [T1003.001] to harvest credentials and aid lateral movement. TA0006 denotes the Credential Access tactic, not another technique ID.

### GT138 | AA25-071A

Medusa actors → USES → local Group Policy Editor

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 15368–15706

> (Updated Aug. 18, 2026) Medusa actors use Mimikatz, the Windows Task Manager, and comsvcs.dll for LSASS dumping [T1003.001] to harvest credentials [TA0006] and aid lateral movement. They disable Windows Defender using the local Group Policy Editor during the LSASS exfiltration and re-enable Defender when they are done with exfiltration.

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: They refers back to Medusa actors in the preceding sentence. The source explicitly says they use the local Group Policy Editor to disable Windows Defender during LSASS exfiltration and re-enable Defender after they finish exfiltration. Preserve both actions and their timing. The paragraph does not cite a defense-impairment or Group Policy technique ID for this sentence; no such mapping is added automatically.

### GT139 | AA25-071A

Medusa actors → USES → Bandizip

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 17253–17441

> (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The updated source explicitly states that Medusa actors install and use Bandizip to create archives of exfiltration files. Preserve this archiving purpose. T1567.002 describes the coordinated Rclone exfiltration activity, so it is not assigned to Bandizip. No uncited archiving technique ID is added.

### GT140 | AA25-071A

Medusa actors → USES_TECHNIQUE → Exfiltration to Cloud Storage (T1567.002)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 17253–17441

> (Updated, Aug. 18, 2026) Medusa actors install and use Bandizip to create archives of exfiltration files and Rclone to facilitate exfiltration of data to the Medusa C2 servers [T1567.002].

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly describes Medusa actors using Rclone to facilitate data exfiltration to Medusa C2 servers and cites T1567.002 (Exfiltration to Cloud Storage). This records the advisory mapping and retains its stated destination; it does not assert a particular cloud provider or assign the technique to Bandizip.

### GT141 | AA25-071A

Medusa actors → USES → eHorus

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly states that FBI identified Medusa actors using remote access software eHorus. Keep the source-provided name and FBI attribution. Do not infer a particular product or version beyond this name.

### GT142 | AA25-071A

eHorus → USES_TECHNIQUE → Remote Access Tools (T1219)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The paragraph identifies eHorus among the remote-access tools used by Medusa actors, in the RMM activity explicitly mapped to T1219. Remote Access Tools is the canonical T1219 name in the frozen ATT&CK 17.1 reference; retain the source wording remote access software. This records the reported Medusa use rather than all legitimate uses of the software. The separate RDP and PsExec citations do not automatically become technique mappings for this tool.

### GT143 | AA25-071A

Medusa actors → USES → N-able

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly states that FBI identified Medusa actors using remote access software N-able. Keep the source-provided name and FBI attribution. Do not infer a particular product or version beyond this name.

### GT144 | AA25-071A

N-able → USES_TECHNIQUE → Remote Access Tools (T1219)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The paragraph identifies N-able among the remote-access tools used by Medusa actors, in the RMM activity explicitly mapped to T1219. Remote Access Tools is the canonical T1219 name in the frozen ATT&CK 17.1 reference; retain the source wording remote access software. This records the reported Medusa use rather than all legitimate uses of the software. The separate RDP and PsExec citations do not automatically become technique mappings for this tool.

### GT145 | AA25-071A

Medusa actors → USES → BeyondTrust

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The source explicitly states that FBI identified Medusa actors using remote access software BeyondTrust. Keep the source-provided name and FBI attribution. Do not infer a particular product or version beyond this name.

### GT146 | AA25-071A

BeyondTrust → USES_TECHNIQUE → Remote Access Tools (T1219)

[Original advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a) | Normalized document offsets 13808–14518

> (Updated Aug. 18, 2026) Medusa actors use a variety of legitimate remote monitoring and management (RMM) software [T1219]. To evade detection, they may tailor their choice based on remote access tools already present in the victim environment. 2,3 FBI identified Medusa actors using remote access software AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp, and Splashtop. Medusa actors use these tools—in combination with Remote Desktop Protocol (RDP) [T1021.001] and PsExec [T1569.002]—to move laterally [TA0008] through the network and identify files for exfiltration [TA0010] and encryption [T1486]. When provided with valid username and password credentials, Medusa actors use PsExec to:

- [X] Source supports the complete relationship and actor scope.
- [X] Canonical/local identity is correct.
- [X] All other eligible facts in this annotation scope are recorded.

Review note: The paragraph identifies BeyondTrust among the remote-access tools used by Medusa actors, in the RMM activity explicitly mapped to T1219. Remote Access Tools is the canonical T1219 name in the frozen ATT&CK 17.1 reference; retain the source wording remote access software. This records the reported Medusa use rather than all legitimate uses of the software. The separate RDP and PsExec citations do not automatically become technique mappings for this tool.

## QA review

Stephen Butler manually reviewed and validated all 61 questions first, then asked Codex to cross-check the questions, reference answers, supporting paths, and assignments against the saved CISA snapshots and frozen ATT&CK 17.1 data. Review completion was confirmed on 2026-10-05. Both the initial author validation and subsequent AI cross-check are recorded. Generated model answers and their human evaluation scores remain planned.

The final set has 20 questions (8 actor/software/technique, 8 technique/mitigation, 4 cross-report); development and held-out reserves are listed in split_manifest.json.

### Q001

What is the two-hop relationship from LockBit affiliates through Advanced Internet Protocol (IP) Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Advanced Internet Protocol (IP) Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT001 → GT002

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q002

What is the two-hop relationship from LockBit affiliates through Advanced Port Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Advanced Port Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT003 → GT004

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q003

What is the two-hop relationship from LockBit affiliates through AnyDesk to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists AnyDesk among tools used by LockBit affiliates and associates its repurposed use with T1219 (Remote Access Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT005 → GT006

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q004

What is the two-hop relationship from LockBit affiliates through Atera Remote Monitoring & Management (RMM) to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Atera Remote Monitoring & Management (RMM) among tools used by LockBit affiliates and associates its repurposed use with T1219 (Remote Access Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT007 → GT008

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q005

What is the two-hop relationship from LockBit affiliates through Backstab to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Backstab among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT009 → GT010

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q006

What is the two-hop relationship from LockBit affiliates through Bat Armor to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Bat Armor among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT011 → GT012

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q007

What is the two-hop relationship from LockBit affiliates through Bloodhound to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Bloodhound among tools used by LockBit affiliates and associates its repurposed use with T1482 (Domain Trust Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT013 → GT014

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q008

What is the two-hop relationship from LockBit affiliates through Chocolatey to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Chocolatey among tools used by LockBit affiliates and associates its repurposed use with T1072 (Software Deployment Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT015 → GT016

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q009

What is the two-hop relationship from LockBit affiliates through Defender Control to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Defender Control among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT017 → GT018

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q010

What is the two-hop relationship from LockBit affiliates through ExtPassword to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists ExtPassword among tools used by LockBit affiliates and associates its repurposed use with T1003 (OS Credential Dumping in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT019 → GT020

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q011

What is the two-hop relationship from LockBit affiliates through FreeFileSync to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists FreeFileSync among tools used by LockBit affiliates and associates its repurposed use with T1567.002 (Exfiltration to Cloud Storage in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT021 → GT022

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q012

What is the two-hop relationship from LockBit affiliates through GMER to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists GMER among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT023 → GT024

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q013

What is the two-hop relationship from LockBit affiliates through Ligolo to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Ligolo among tools used by LockBit affiliates and associates its repurposed use with T1095 (Non-Application Layer Protocol in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT025 → GT026

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q014

What is the two-hop relationship from LockBit affiliates through LostMyPassword to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists LostMyPassword among tools used by LockBit affiliates and associates its repurposed use with T1003 (OS Credential Dumping in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT027 → GT028

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q015

What is the two-hop relationship from LockBit affiliates through MEGA Ltd MegaSync to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists MEGA Ltd MegaSync among tools used by LockBit affiliates and associates its repurposed use with T1567.002 (Exfiltration to Cloud Storage in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT029 → GT030

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q016

What is the two-hop relationship from LockBit affiliates through Microsoft Sysinternals ProcDump to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Microsoft Sysinternals ProcDump among tools used by LockBit affiliates and associates its repurposed use with T1003.001 (LSASS Memory in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT031 → GT032

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q017

What is the two-hop relationship from LockBit affiliates through PasswordFox to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists PasswordFox among tools used by LockBit affiliates and associates its repurposed use with T1555.003 (Credentials from Web Browsers in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT033 → GT034

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q018

What is the two-hop relationship from LockBit affiliates through PCHunter to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists PCHunter among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT035 → GT036

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q019

What is the two-hop relationship from LockBit affiliates through PowerTool to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists PowerTool among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT037 → GT038

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q020

What is the two-hop relationship from LockBit affiliates through Process Hacker to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Process Hacker among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT039 → GT040

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q021

What is the two-hop relationship from LockBit affiliates through PuTTY Link (Plink) to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists PuTTY Link (Plink) among tools used by LockBit affiliates and associates its repurposed use with T1572 (Protocol Tunneling in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT041 → GT042

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q022

What is the two-hop relationship from LockBit affiliates through Seatbelt to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Seatbelt among tools used by LockBit affiliates and associates its repurposed use with T1082 (System Information Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT043 → GT044

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q023

What is the two-hop relationship from LockBit affiliates through ScreenConnect (also known as ConnectWise) to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists ScreenConnect (also known as ConnectWise) among tools used by LockBit affiliates and associates its repurposed use with T1219 (Remote Access Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT045 → GT046

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q024

What is the two-hop relationship from LockBit affiliates through SoftPerfect Network Scanner to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists SoftPerfect Network Scanner among tools used by LockBit affiliates and associates its repurposed use with T1046 (Network Service Discovery in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT047 → GT048

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q025

What is the two-hop relationship from LockBit affiliates through Splashtop to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists Splashtop among tools used by LockBit affiliates and associates its repurposed use with T1021.001 (Remote Desktop Protocol in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT049 → GT050

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q026

What is the two-hop relationship from LockBit affiliates through TDSSKiller to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists TDSSKiller among tools used by LockBit affiliates and associates its repurposed use with T1562.001 (Disable or Modify Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT051 → GT052

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q027

What is the two-hop relationship from LockBit affiliates through TeamViewer to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists TeamViewer among tools used by LockBit affiliates and associates its repurposed use with T1219 (Remote Access Tools in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT053 → GT054

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q028

What is the two-hop relationship from LockBit affiliates through ThunderShell to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists ThunderShell among tools used by LockBit affiliates and associates its repurposed use with T1071.001 (Web Protocols in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT055 → GT056

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q029

What is the two-hop relationship from LockBit affiliates through WinSCP to an ATT&CK technique in this advisory? Explain both the software-use link and the technique mapping.

**Reviewed reference answer:** The advisory lists WinSCP among tools used by LockBit affiliates and associates its repurposed use with T1048 (Exfiltration Over Alternative Protocol in the frozen Enterprise ATT&CK 17.1 reference). This describes the advisory mapping, not all uses of that tool.

**Category:** actor_software_technique

**Benchmark assignment:** Development — may be used for tuning

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT057 → GT058

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q030

According to AA23-061A, which ATT&CK technique is connected to Royal actors through the reported use of Chisel? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** AA23-061A reports that Royal actors were historically observed using Chisel to communicate with their C2 infrastructure. The advisory associates this tool use with T1572 (Protocol Tunneling). The two links are Royal actors → USES → Chisel → USES_TECHNIQUE → T1572; this preserves the historical observation rather than asserting current use.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)

**Required paths:**

- GT059 → GT060

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Historical Royal observation retained; Chisel is in the named tool list linked to T1572 for C2 communication. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q031

According to AA24-109A, which ATT&CK technique is connected to Akira threat actors through the reported use of Mimikatz? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Akira threat actors use Mimikatz; the advisory associates the described use of Mimikatz with T1003 (OS Credential Dumping in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT061 → GT062

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Akira use of Mimikatz is explicitly in the T1003 credential-scraping sentence; the preceding LSASS/Kerberoasting wording is not reassigned to this tool. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q032

According to AA24-109A, which ATT&CK technique is connected to Akira threat actors through the reported use of LaZagne? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Akira threat actors use LaZagne; the advisory associates the described use of LaZagne with T1003 (OS Credential Dumping in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT063 → GT064

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Akira use of LaZagne is explicitly in the same T1003 credential-scraping sentence. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q033

In the AA24-109A command-and-control paragraph describing ngrok encrypted sessions that bypass perimeter monitoring, what two-hop path connects Akira actors through ngrok to the cited ATT&CK technique? Explain both source-supported links.

**Reviewed reference answer:** In the C2 paragraph of AA24-109A, Akira actors use ngrok to initiate encrypted sessions that bypass perimeter monitoring. That paragraph cites T1572 (Protocol Tunneling). The path is Akira actors → USES → ngrok → USES_TECHNIQUE → T1572.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT065 → GT066

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Question restricted to paragraph 11788: encrypted ngrok C2 tunnels are mapped to T1572. Distinct from Q038. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q034

According to AA24-109A, which ATT&CK technique is connected to Akira threat actors through the reported use of FileZilla? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** AA24-109A reports Akira actors using FileZilla, grouped with WinRAR, to collect data and cites T1560.001 (Archive via Utility). Thus the advisory-reported path is Akira actors → USES → FileZilla → USES_TECHNIQUE → T1560.001. This retains the source mapping; it does not independently establish that FileZilla performs archiving.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT067 → GT068

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The source groups FileZilla and WinRAR for collecting data with T1560.001. Retain that source-reported mapping without claiming FileZilla itself archives files. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q035

According to AA24-109A, which ATT&CK technique is connected to Akira threat actors through the reported use of WinRAR? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Akira threat actors use WinRAR; the advisory associates the described use of WinRAR with T1560.001 (Archive via Utility in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT069 → GT070

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The source groups WinRAR and FileZilla for collecting data with T1560.001; no uncited capability is substituted. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q036

According to AA24-109A, which ATT&CK technique is connected to Akira threat actors through the reported use of WinSCP? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Akira threat actors use WinSCP; the advisory associates the described use of WinSCP with T1048 (Exfiltration Over Alternative Protocol in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT071 → GT072

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: WinSCP is explicitly named in Akira exfiltration activity mapped to T1048. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q037

According to AA24-109A, which ATT&CK technique is connected to Akira threat actors through the reported use of RClone? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Akira threat actors use RClone; the advisory associates the described use of RClone with T1048 (Exfiltration Over Alternative Protocol in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT073 → GT074

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: RClone is explicitly named in Akira exfiltration activity mapped to T1048; canonical Rclone capitalization does not alter the entity. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q038

In the AA24-109A exfiltration paragraph stating that Akira actors use ngrok in some instances to create secure tunnels for data exfiltration, what two-hop path connects the actors through ngrok to the cited ATT&CK technique? Explain both links and retain the qualification.

**Reviewed reference answer:** In some instances, according to the exfiltration paragraph of AA24-109A, Akira actors use ngrok to create secure tunnels for data exfiltration. That sentence cites T1090 (Proxy). The path is Akira actors → USES → ngrok → USES_TECHNIQUE → T1090; this is distinct from the T1572 C2 mapping in the earlier paragraph.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT065 → GT075

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Question restricted to paragraph 12198 and the in some instances ngrok exfiltration sentence mapped to T1090. Distinct from Q033. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q039

According to AA24-131A, which ATT&CK technique is connected to Black Basta affiliates through the reported use of Backstab? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** AA24-131A reports Black Basta affiliates deploying Backstab in some instances to disable endpoint detection and response tooling. The source cites T1562.001 (Disable or Modify Tools). The path is Black Basta affiliates → USES → Backstab → USES_TECHNIQUE → T1562.001, with the source qualification retained.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a)

**Required paths:**

- GT076 → GT077

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The in some instances qualification is retained for Black Basta affiliate deployment of Backstab against EDR with T1562.001. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q040

According to AA23-352A, which ATT&CK technique is connected to Play ransomware actors through the reported use of Mimikatz? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Play ransomware actors use Mimikatz; the advisory associates the described use of Mimikatz with T1003 (OS Credential Dumping in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)

**Required paths:**

- GT078 → GT062

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Play use of Mimikatz is explicit; T1003 mapping is supported by the Play additional_support passage of GT062, not borrowed from Akira. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q041

According to AA23-075A, which ATT&CK technique is connected to LockBit 3.0 affiliates through the reported use of rclone? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** LockBit 3.0 affiliates use rclone; the advisory associates the described use of rclone with T1567.002 (Exfiltration to Cloud Storage in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a)

**Required paths:**

- GT079 → GT080

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: LockBit 3.0 affiliate rclone use and T1567.002 mapping are explicit; actor identity is kept distinct from generic LockBit affiliates. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q042

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of Mimikatz? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use Mimikatz; the advisory associates the described use of Mimikatz with T1003.001 (LSASS Memory in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT081 → GT082

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Medusa Mimikatz use for LSASS dumping is explicitly mapped to T1003.001; TA0006 is a tactic, not another technique. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q043

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of Rclone? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use Rclone; the advisory associates the described use of Rclone with T1567.002 (Exfiltration to Cloud Storage in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT083 → GT080

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Medusa uses Rclone for exfiltration to its C2 servers with the advisory citation T1567.002. That citation is not assigned to Bandizip archiving. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q044

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of PsExec? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use PsExec; the advisory associates the described use of PsExec with T1569.002 (Service Execution in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT084 → GT085

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Medusa use of PsExec and its cited T1569.002 mapping are explicit; the neighboring RDP technique is not assigned to PsExec. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q045

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of AnyDesk? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use AnyDesk; the advisory associates the described use of AnyDesk with T1219 (Remote Access Tools in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT086 → GT087

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q046

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of Atera? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use Atera; the advisory associates the described use of Atera with T1219 (Remote Access Tools in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT088 → GT089

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q047

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of ConnectWise? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use ConnectWise; the advisory associates the described use of ConnectWise with T1219 (Remote Access Tools in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT090 → GT091

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q048

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of SimpleHelp? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use SimpleHelp; the advisory associates the described use of SimpleHelp with T1219 (Remote Access Tools in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT092 → GT093

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q049

According to AA25-071A, which ATT&CK technique is connected to Medusa actors through the reported use of Splashtop? Explain the two-hop actor-to-software-to-technique path with evidence.

**Reviewed reference answer:** Medusa actors use Splashtop; the advisory associates the described use of Splashtop with T1219 (Remote Access Tools in Enterprise ATT&CK 17.1). Both links must be supported in the advisory context.

**Category:** actor_software_technique

**Benchmark assignment:** Held-out evaluation — reserve (shares final-test evidence)

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT094 → GT095

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q050

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Advanced Internet Protocol (IP) Scanner in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The AA23-165A Table 4 caption lists Advanced Internet Protocol (IP) Scanner as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1046 (Network Service Discovery). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1030 (Network Segmentation), M1031 (Network Intrusion Prevention), M1042 (Disable or Remove Feature or Program). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT001 → GT002 → RF001
- GT001 → GT002 → RF002
- GT001 → GT002 → RF003

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 3 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q051

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Chocolatey in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The AA23-165A Table 4 caption lists Chocolatey as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1072 (Software Deployment Tools). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1015 (Active Directory Configuration), M1017 (User Training), M1018 (User Account Management), M1026 (Privileged Account Management), M1027 (Password Policies), M1029 (Remote Data Storage), M1030 (Network Segmentation), M1032 (Multi-factor Authentication), M1033 (Limit Software Installation), M1051 (Update Software). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT015 → GT016 → RF004
- GT015 → GT016 → RF005
- GT015 → GT016 → RF006
- GT015 → GT016 → RF007
- GT015 → GT016 → RF008
- GT015 → GT016 → RF009
- GT015 → GT016 → RF010
- GT015 → GT016 → RF011
- GT015 → GT016 → RF012
- GT015 → GT016 → RF013

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 10 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q052

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Ligolo in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The AA23-165A Table 4 caption lists Ligolo as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1095 (Non-Application Layer Protocol). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1030 (Network Segmentation), M1031 (Network Intrusion Prevention), M1037 (Filter Network Traffic), M1047 (Audit). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT025 → GT026 → RF014
- GT025 → GT026 → RF015
- GT025 → GT026 → RF016
- GT025 → GT026 → RF017

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 4 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q053

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to ThunderShell in AA23-165A? Start from LockBit affiliates and follow the three-hop actor-to-software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The AA23-165A Table 4 caption lists ThunderShell as a tool used by LockBit affiliates. The selected advisory row maps its reported use to T1071.001 (Web Protocols). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1031 (Network Intrusion Prevention). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT055 → GT056 → RF018

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 1 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q054

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Splashtop in AA23-165A? Follow the two-hop software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The selected advisory row maps its reported use to T1021.001 (Remote Desktop Protocol). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1018 (User Account Management), M1026 (Privileged Account Management), M1028 (Operating System Configuration), M1030 (Network Segmentation), M1032 (Multi-factor Authentication), M1035 (Limit Access to Resource Over Network), M1042 (Disable or Remove Feature or Program), M1047 (Audit). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT050 → RF019
- GT050 → RF020
- GT050 → RF021
- GT050 → RF022
- GT050 → RF023
- GT050 → RF024
- GT050 → RF025
- GT050 → RF026

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 8 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q055

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to FreeFileSync in AA23-165A? Follow the two-hop software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The selected advisory row maps its reported use to T1567.002 (Exfiltration to Cloud Storage). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1021 (Restrict Web-Based Content). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT022 → RF027

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 1 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q056

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to PasswordFox in AA23-165A? Follow the two-hop software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The selected advisory row maps its reported use to T1555.003 (Credentials from Web Browsers). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1017 (User Training), M1018 (User Account Management), M1021 (Restrict Web-Based Content), M1027 (Password Policies), M1051 (Update Software). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT034 → RF028
- GT034 → RF029
- GT034 → RF030
- GT034 → RF031
- GT034 → RF032

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 5 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q057

Which mitigation options have direct, active mitigates relationships in Enterprise ATT&CK 17.1 to the technique mapped to Microsoft Sysinternals ProcDump in AA23-165A? Follow the two-hop software-to-technique-to-mitigation path. Distinguish advisory observations from reference recommendations.

**Reviewed reference answer:** The selected advisory row maps its reported use to T1003.001 (LSASS Memory). The direct, active mitigates relationships in Enterprise ATT&CK 17.1 connect this technique to: M1017 (User Training), M1025 (Privileged Process Integrity), M1026 (Privileged Account Management), M1027 (Password Policies), M1028 (Operating System Configuration), M1040 (Behavior Prevention on Endpoint), M1043 (Credential Access Protection). These are reference mitigation associations, not incident-specific proof of effectiveness.

**Category:** technique_mitigation

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [Frozen ATT&CK 17.1 STIX](https://github.com/mitre-attack/attack-stix-data/blob/master/enterprise-attack/enterprise-attack-17.1.json) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a)

**Required paths:**

- GT032 → RF033
- GT032 → RF034
- GT032 → RF035
- GT032 → RF036
- GT032 → RF037
- GT032 → RF038
- GT032 → RF039

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: All 7 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q058

Compare AA24-109A and AA23-352A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

**Reviewed reference answer:** AA24-109A reports Akira threat actors using Mimikatz, with advisory mappings T1003; AA23-352A reports Play ransomware actors using Mimikatz, with advisory mappings T1003. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. Both reports cite the same parent technique, T1003 (OS Credential Dumping), for their reported Mimikatz use.

**Category:** cross_report_comparison

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)

**Required paths:**

- GT061 → GT062
- GT078 → GT062

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q059

Compare AA24-109A and AA25-071A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

**Reviewed reference answer:** AA24-109A reports Akira threat actors using Mimikatz, with advisory mappings T1003; AA25-071A reports Medusa actors using Mimikatz, with advisory mappings T1003.001. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. The first report uses the parent technique T1003 (OS Credential Dumping); the Medusa report specifies T1003.001 (LSASS Memory), a sub-technique of T1003. This is a difference in specificity of the reported mapping.

**Category:** cross_report_comparison

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT061 → GT062
- GT081 → GT082

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q060

Compare AA23-352A and AA25-071A: which actors are reported using Mimikatz, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

**Reviewed reference answer:** AA23-352A reports Play ransomware actors using Mimikatz, with advisory mappings T1003; AA25-071A reports Medusa actors using Mimikatz, with advisory mappings T1003.001. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. The first report uses the parent technique T1003 (OS Credential Dumping); the Medusa report specifies T1003.001 (LSASS Memory), a sub-technique of T1003. This is a difference in specificity of the reported mapping.

**Category:** cross_report_comparison

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT078 → GT062
- GT081 → GT082

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

### Q061

Compare AA24-109A and AA25-071A: which actors are reported using Rclone, and how do their advisory software-to-technique mappings compare? Cite both reports and keep each mapping within its source context.

**Reviewed reference answer:** AA24-109A reports Akira threat actors using Rclone, with advisory mappings T1048; AA25-071A reports Medusa actors using Rclone, with advisory mappings T1567.002. These mappings describe the cited reports and do not establish that every use of the software has these behaviors. The Akira report cites T1048 (Exfiltration Over Alternative Protocol); the Medusa report cites T1567.002 (Exfiltration to Cloud Storage). These are distinct source-reported mappings for the same software.

**Category:** cross_report_comparison

**Benchmark assignment:** Held-out evaluation — selected final test

**Review provenance:** Stephen Butler manually validated this question first, then requested a Codex cross-check; review completion recorded on 2026-10-05.

**Sources:** [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a) | [CISA advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)

**Required paths:**

- GT073 → GT074
- GT083 → GT080

- [X] The question requires all supported links in its declared path(s).
- [X] The reference covers all correct answers in the declared scope.
- [X] The question is assigned to development or held-out evaluation.

Review note: Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports. Stephen Butler manually validated this question first, then requested a Codex source/reference cross-check. Review completion was recorded on 2026-10-05. No model answer or performance result was evaluated.

