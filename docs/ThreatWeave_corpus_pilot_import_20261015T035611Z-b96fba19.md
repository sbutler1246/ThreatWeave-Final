# Reviewed corpus pilot import preview

Development assertions from actual model output; AI-assisted source review, human review pending.
Only Supported dispositions are selected. Uncertain/conditional review candidates are excluded.
No benchmark gold triples or QA reference answers are inputs.

Extraction run: S:\ThreatWeave\work\corpus_extraction_pilot\20261015T035023Z-f4b7051e
Review manifest: S:\ThreatWeave\docs\ThreatWeave_corpus_pilot_v2_6_review.json
Review manifest SHA-256: f0a401e7c60247173bf6e891c6596c99f252e020734746d5f75dc1cc6dc71a7d

Target records: 10 windows, 39 distinct entities, 34 assertions.
Target counts include reused records; these are not counts of newly created graph records.

## AA23-136A:development:llama500:3551:5862

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES_TECHNIQUE → Valid Accounts
  Source review: The actor uses compromised RDP credentials; likely qualifies credential provenance, not the reported credential use.
  Literal support: BianLian group actors gain initial access to networks by leveraging compromised Remote Desktop Protocol (RDP) credentials likely acquired from initial access brokers [T1078][T1133] or via phishing [T1566].
- BianLian group actors → USES_TECHNIQUE → External Remote Services
  Source review: The source explicitly reports actor initial access through RDP with T1133.
  Literal support: BianLian group actors gain initial access to networks by leveraging compromised Remote Desktop Protocol (RDP) credentials likely acquired from initial access brokers [T1078][T1133] or via phishing [T1566].
- BianLian group actors → USES_TECHNIQUE → Malware
  Source review: The source describes the actor-specific custom Go backdoor and explicitly annotates T1587.001.
  Literal support: BianLian group actors implant a custom backdoor specific to each victim written in Go (see the Indicators of Compromise Section for an example) [T1587.001] and install remote management and access software for persistence and command and control [T1105][T1219].

## AA23-136A:development:llama500:5605:7833

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a

- BianLian group actors → USES_TECHNIQUE → PowerShell
  Source review: Explicit actor use of PowerShell with T1059.001.
  Literal support: BianLian group actors use PowerShell [T1059.001] and Windows Command Shell [T1059.003] to disable antivirus tools [T1562.001]
- BianLian group actors → USES_TECHNIQUE → Windows Command Shell
  Source review: Explicit actor use of Windows Command Shell with T1059.003.
  Literal support: BianLian group actors use PowerShell [T1059.001] and Windows Command Shell [T1059.003] to disable antivirus tools [T1562.001]
- BianLian group actors → USES_TECHNIQUE → Disable or Modify Tools
  Source review: The actors disable antivirus tools, explicitly annotated T1562.001.
  Literal support: BianLian group actors use PowerShell [T1059.001] and Windows Command Shell [T1059.003] to disable antivirus tools [T1562.001]

## AA23-319A:development:llama500:2651:5181

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

- Threat actors leveraging Rhysida ransomware → USES → Rhysida
  Source review: The full source subject Threat actors leveraging Rhysida ransomware preserves the restriction and explicitly describes their use of that ransomware.
  Literal support: Threat actors leveraging Rhysida ransomware are known to impact “targets of opportunity,” including victims in the education, healthcare, manufacturing, information technology, and government sectors.
- Rhysida actors → USES_TECHNIQUE → Valid Accounts
  Source review: The source directly reports actor VPN authentication using compromised valid credentials.
  Literal support: Rhysida actors have commonly been observed authenticating to internal VPN access points with compromised valid credentials [T1078]
- Rhysida actors → USES → Gootloader
  Source review: The source explicitly reports actor use of Gootloader malware; at times is not a software endpoint.
  Literal support: Rhysida actors have also used Gootloader malware at times for initial access [TA0001].
- Rhysida actors → USES_TECHNIQUE → Remote Desktop Protocol
  Source review: The source directly reports actors creating RDP connections for lateral movement with T1021.001.
  Literal support: Analysis identified Rhysida actors using living off the land techniques, such as creating Remote Desktop Protocol (RDP) connections for lateral movement [T1021.001]

## AA23-319A:development:llama500:4860:7286

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

- Net → USES_TECHNIQUE → Domain Account
  Source review: Literal net user domain command with its T1087.002 annotation.
  Literal support: net user [username] /domain [T1087.002]
- Net → USES_TECHNIQUE → Remote System Discovery
  Source review: Literal net domain-computers group command with T1018.
  Literal support: net group “domain computers” /domain [T1018]
- Net → USES_TECHNIQUE → Domain Groups
  Source review: Literal net domain-admins group command with T1069.002.
  Literal support: net group “domain admins” /domain [T1069.002]
- Rhysida actors → USES → Windows PowerShell Integrated Scripting Environment
  Source review: The source directly reports actors launching Windows PowerShell Integrated Scripting Environment before executing a malicious script.
  Literal support: Rhysida actors have been observed launching Windows PowerShell Integrated Scripting Environment (ISE) prior to executing a malicious script (1.ps1 from a folder in %AppData%\Local\Temp%).

## AA23-320A:development:llama500:2887:5261

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider threat actors → USES_TECHNIQUE → Phishing for Information
  Source review: The explicit public-reporting subject scopes the phone/SMS credential-targeting list item with T1598; retain that attribution.
  Literal support: According to public reporting, Scattered Spider threat actors have:[2]
Posed as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees and gain access to the network [T1598] [T1656].
- Scattered Spider threat actors → USES_TECHNIQUE → Impersonation
  Source review: The same explicit subject/list reports IT/helpdesk impersonation and T1656.
  Literal support: According to public reporting, Scattered Spider threat actors have:[2]
Posed as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees and gain access to the network [T1598] [T1656].
- Scattered Spider threat actors → USES_TECHNIQUE → User Execution
  Source review: The named subject scopes employee execution of remote access tools and T1204.
  Literal support: According to public reporting, Scattered Spider threat actors have:[2]
Posed as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees and gain access to the network [T1598] [T1656].
Posed as company IT and/or helpdesk staff to direct employees to run commercial remote access tools enabling initial access [T1204] [T1219] [T1566].
- Scattered Spider threat actors → USES_TECHNIQUE → Remote Access Tools
  Source review: The same subject/list item explicitly reports remote access tools and T1219.
  Literal support: According to public reporting, Scattered Spider threat actors have:[2]
Posed as company IT and/or helpdesk staff using phone calls or SMS messages to obtain credentials from employees and gain access to the network [T1598] [T1656].
Posed as company IT and/or helpdesk staff to direct employees to run commercial remote access tools enabling initial access [T1204] [T1219] [T1566].

## AA23-320A:development:llama500:4957:7101

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

- Scattered Spider → USES → WarzoneRAT
  Source review: The Malware Used by Scattered Spider caption scopes AveMaria, explicitly also known as WarZone [S0670]; the source alias now shares that catalog identity.
  Literal support: Table 2: Malware Used by Scattered Spider
Malware
Use
AveMaria (also known as WarZone [S0670])
- Scattered Spider → USES → Raccoon Stealer
  Source review: The explicit actor-use malware caption scopes the Raccoon Stealer [S1148] row.
  Literal support: Table 2: Malware Used by Scattered Spider
Malware
Use
AveMaria (also known as WarZone [S0670])
Enables remote access to a targeted organization’s systems.
Raccoon Stealer [S1148]
- Raccoon Stealer → USES_TECHNIQUE → Browser Information Discovery
  Source review: The Raccoon Stealer row description says it steals browser history, annotated T1217; the contiguous literal quote includes the action.
  Literal support: Raccoon Stealer [S1148]
Steals information including login credentials [TA0006], browser history [T1217]
- Raccoon Stealer → USES_TECHNIQUE → Steal Web Session Cookie
  Source review: The same row description reports stealing cookies, annotated T1539.
  Literal support: Raccoon Stealer [S1148]
Steals information including login credentials [TA0006], browser history [T1217], cookies [T1539]

## AA23-353A:development:llama500:3078:5323

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

- ALPHV Blackcat affiliates → USES_TECHNIQUE → Phishing for Information
  Source review: Named affiliates scope the adjacent Actors continuation, which explicitly reports phone/SMS credential targeting and T1598.
  Literal support: ALPHV Blackcat affiliates use advanced social engineering techniques and open source research on a company to gain initial access. Actors pose as company IT and/or helpdesk staff and use phone calls or SMS messages [T1598] to obtain credentials from employees to access the target network [T1586].
- ALPHV Blackcat affiliates → USES_TECHNIQUE → Compromise Accounts
  Source review: The same controlled continuation explicitly reports credentials used for target access and T1586.
  Literal support: ALPHV Blackcat affiliates use advanced social engineering techniques and open source research on a company to gain initial access. Actors pose as company IT and/or helpdesk staff and use phone calls or SMS messages [T1598] to obtain credentials from employees to access the target network [T1586].
- ALPHV Blackcat affiliates → USES → AnyDesk
  Source review: The source directly says affiliates deploy remote access software including AnyDesk.
  Literal support: After gaining access to a victim network, ALPHV Blackcat affiliates deploy remote access software such as AnyDesk, Mega sync, and Splashtop in preparation of data exfiltration.
- ALPHV Blackcat affiliates → USES → Mega sync
  Source review: The same deployment list names the complete software phrase Mega sync.
  Literal support: After gaining access to a victim network, ALPHV Blackcat affiliates deploy remote access software such as AnyDesk, Mega sync, and Splashtop in preparation of data exfiltration.

## AA23-353A:development:llama500:5039:6758

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

- ALPHV Blackcat affiliates → USES → Tor
  Source review: The source directly names ALPHV Blackcat affiliates communicating with victims via TOR [S0183], without a copied Some qualifier.
  Literal support: After exfiltrating and/or encrypting data, ALPHV Blackcat affiliates communicate with victims via TOR [S0183]

## AA24-060A:development:llama500:2332:4570

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos actors → USES_TECHNIQUE → Phishing for Information
  Source review: The source explicitly reports Phobos actors initial access through phishing campaigns with T1598.
  Literal support: Phobos actors typically gain initial access to vulnerable networks by leveraging phishing campaigns [T1598] to drop hidden payloads or using internet protocol (IP) scanning tools, such as Angry IP Scanner, to search for vulnerable Remote Desktop Protocol (RDP) ports [T1595.001] or by leveraging RDP on Microsoft Windows environments.[5],[6]
- Threat actors leveraging Phobos → USES → Phobos
  Source review: The full source subject Threat actors leveraging Phobos preserves its restriction and explicitly describes use of Phobos.
  Literal support: Threat actors leveraging Phobos have notably deployed remote access tools to establish a remote connection within the compromised network [T1219].[7]
- Threat actors leveraging Phobos → USES_TECHNIQUE → Remote Access Tools
  Source review: That restricted source subject explicitly reports deployed remote access tools with T1219.
  Literal support: Threat actors leveraging Phobos have notably deployed remote access tools to establish a remote connection within the compromised network [T1219].[7]

## AA24-060A:development:llama500:4275:6493

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a

- Phobos actors → USES → Phobos
  Source review: The actors explicitly deploy additional Phobos payloads; the software mention occurs independently of the qualified actor name.
  Literal support: Phobos actors run executables like 1saas.exe or cmd.exe to deploy additional Phobos payloads that have elevated privileges enabled [TA0004].
- Phobos actors → USES → 1saas.exe
  Source review: The source directly says Phobos actors run 1saas.exe.
  Literal support: Phobos actors run executables like 1saas.exe or cmd.exe to deploy additional Phobos payloads that have elevated privileges enabled [TA0004].
- Phobos actors → USES → cmd
  Source review: The source directly says Phobos actors run cmd.exe; catalog resolution is separate from a source-reported ID.
  Literal support: Phobos actors run executables like 1saas.exe or cmd.exe to deploy additional Phobos payloads that have elevated privileges enabled [TA0004].
- Smokeloader → USES_TECHNIQUE → Portable Executable Injection
  Source review: The source directly reports Smokeloader API manipulation enabling process injection and T1055.002.
  Literal support: For the first phase, Smokeloader manipulates either VirtualAlloc or VirtualProtect API functions—which opens an entry point, enabling code to be injected into running processes and allowing the malware to evade network defense tools [T1055.002].

## Excluded candidates

- 01.3: Phishing is within qualified alternatives for likely credential acquisition; do not import as categorical use.
- 02.1: The source says may have used Rsocks for SOCKS5 tunnels; the selected behavior remains inside an uncertain event.
- 09.2: The passage begins If Phobos actors gain successful RDP authentication; a conditional is not a confirmed T1133 access event.
