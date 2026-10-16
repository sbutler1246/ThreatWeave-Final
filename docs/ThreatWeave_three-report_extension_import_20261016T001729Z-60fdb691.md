# Reviewed three-report extension import preview

Development assertions from actual model output; AI-assisted source review, human review pending.
Only Supported dispositions are selected. Uncertain/conditional review candidates are excluded.
No benchmark gold triples or QA reference answers are inputs.

Extraction run: S:\ThreatWeave\work\corpus_extension_extraction\20261016T000937Z-0cef6551
Review manifest: S:\ThreatWeave\docs\ThreatWeave_corpus_extension_source_review.json
Review manifest SHA-256: 46424ab5d763dbd5f97b8beebce27d24a98ff9108f70fe200e1d99d45437dd21

Target records: 12 windows, 27 distinct entities, 27 assertions.
Target counts include reused records; these are not counts of newly created graph records.

## AA24-038A:development:llama500:13617:16082

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES_TECHNIQUE → Gather Victim Org Information
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1591. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Volt Typhoon actors conduct extensive pre-compromise reconnaissance [TA0043] to learn about the target organization [T1591]
- Volt Typhoon actors → USES_TECHNIQUE → Email Addresses
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1589.002. The selected assertion is definite and its endpoint roles match the source.
  Literal support: In some instances, the U.S. authoring agencies have observed Volt Typhoon actors targeting the personal emails of key network and IT staff [T1589.002] post compromise.
- Volt Typhoon actors → USES_TECHNIQUE → Multi-hop Proxy
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1090.003. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Historically, Volt Typhoon actors use multi-hop proxies for command and control (C2) infrastructure [T1090.003].
- Volt Typhoon actors → USES → KV Botnet
  Source review: The source explicitly describes Volt Typhoon actors using routers implanted with KV Botnet malware to support their operations.
  Literal support: Recently, Volt Typhoon actors used Cisco and NETGEAR end-of-life SOHO routers implanted with KV Botnet malware to support their operations [T1584.005]. (See DOJ press release U.S.

## AA24-038A:development:llama500:15793:18394

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES_TECHNIQUE → Command and Scripting Interpreter
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1059. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Instead, once Volt Typhoon actors gain access to target environments, they use hands-on-keyboard activity via the command-line [T1059] and other native tools and processes on systems [T1218] (often referred to as “LOLBins”), known as LOTL, to maintain and expand access to the victim networks.
- Volt Typhoon actors → USES → Magnet RAM Capture
  Source review: Observed use of Magnet RAM Capture is definite. The later likely-qualified analysis purpose is not part of this tool-use assertion.
  Literal support: For example, Volt Typhoon actors have been observed using Magnet RAM Capture (MRC) version 1.20 on domain controllers.

## AA24-038A:development:llama500:18096:20499

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES → FRP
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES -> FRP. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Volt Typhoon actors have also been observed implanting Fast Reverse Proxy (FRP) for command and control.[3] (See the Command and Control section).
- Volt Typhoon actors → USES_TECHNIQUE → Exploitation for Privilege Escalation
  Source review: The source explicitly attributes exploiting privilege-escalation vulnerabilities, annotated T1068, to Volt Typhoon actors; the introductory initial-access clause sets sequence, not uncertainty.
  Literal support: Volt Typhoon actors first obtain credentials from public-facing appliances after gaining initial access by exploiting privilege escalation vulnerabilities [T1068] in the operating system or network services.

## AA24-038A:development:llama500:20222:22508

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES → PuTTY
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES -> PuTTY. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Volt Typhoon actors have also been observed interacting with a PuTTY application by enumerating existing stored sessions [T1012].

## AA24-038A:development:llama500:22202:24566

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES → Mimikatz
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES -> Mimikatz. The selected assertion is definite and its endpoint roles match the source.
  Literal support: The U.S. authoring agencies have observed Volt Typhoon actors leveraging Mimikatz to harvest credentials, and industry partners have observed Volt Typhoon leveraging Impacket.[2]
- Volt Typhoon actors → USES_TECHNIQUE → System Information Discovery
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES_TECHNIQUE -> T1082. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Volt Typhoon actors have been observed using commercial tools, LOTL utilities, and appliances already present on the system for system information [T1082]

## AA24-038A:development:llama500:24254:26777

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Tasklist → USES_TECHNIQUE → Process Discovery
  Source review: The selected exact source passage directly attributes tasklist -> USES_TECHNIQUE -> T1057. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Executing tasklist /v to gather a detailed process listing [T1057]

## AA24-038A:development:llama500:28528:31303

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES → PuTTY
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES -> PuTTY. The selected assertion is definite and its endpoint roles match the source.
  Literal support: The vCenter server was adjacent to OT assets, and Volt Typhoon actors were observed interacting with the PuTTY application on the server by enumerating existing stored sessions.
- Volt Typhoon actors → USES → PsExec
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES -> PSExec. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Additionally, Volt Typhoon actors have been observed using PSExec to execute remote processes, including the automated acceptance of the end-user license agreement (EULA) through an administrative account, signified by the accepteula command flag.

## AA24-038A:development:llama500:30941:33296

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- ronf.exe → USES_TECHNIQUE → Archive via Utility
  Source review: Executing ronf.exe to compress/archive the files is definite. Likely qualifies only its possible rar.exe identity, which is not asserted here.
  Literal support: They then compressed and archived the extracted ntds.dit and accompanying registry files by executing ronf.exe, which was likely a renamed version of the archive utility rar.exe) [T1560.001].
- FRP → USES_TECHNIQUE → Proxy
  Source review: The selected exact source passage directly attributes FRP -> USES_TECHNIQUE -> T1090. The selected assertion is definite and its endpoint roles match the source.
  Literal support: They have also been observed setting up FRP clients [T1090] on a victim’s corporate infrastructure to establish covert communications channels [T1573] for command and control.
- Volt Typhoon actors → USES → FRP
  Source review: The selected exact source passage directly attributes Volt Typhoon actors -> USES -> FRP. The selected assertion is definite and its endpoint roles match the source.
  Literal support: In one instance, Volt Typhoon actors implanted the FRP client with filename SMSvcService.exe on a Shortel Enterprise Contact Center (ECC) server and a second FRP client with filename Brightmetricagent.exe on another server.
- Volt Typhoon actors → USES_TECHNIQUE → Archive via Utility
  Source review: The selected contiguous passage explicitly ties Volt Typhoon actors to file compression/archive execution annotated T1560.001. Likely qualifies the utility rename, not the observed compression.
  Literal support: In another compromise, Volt Typhoon actors leveraged WMIC to create and use temporary directories (C:\Users\Public\pro, C:\Windows\Temp\tmp, C:\Windows\Temp\tmp\Active Directory and C:\Windows\Temp\tmp\registry) to stage the extracted ntds.dit and SYSTEM registry hives from ntdsutil execution volume shadow copies (see the Credential Access section) obtained from two DCs. They then compressed and archived the extracted ntds.dit and accompanying registry files by executing ronf.exe, which was likely a renamed version of the archive utility rar.exe) [T1560.001].

## AA24-038A:development:llama500:33045:35669

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

- Volt Typhoon actors → USES → FRP
  Source review: The source directly describes Volt Typhoon actors using an intermediary server for their FRP operations, supporting actual FRP use.
  Literal support: In the same compromise, Volt Typhoon actors exploited a Paessler Router Traffic Grapher (PRTG) server as an intermediary for their FRP operations.
- netsh → USES_TECHNIQUE → Modify Registry
  Source review: The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1112. The selected assertion is definite and its endpoint roles match the source.
  Literal support: To facilitate this, they used the netsh command, a legitimate Windows command, to create a PortProxy registry modification [T1112] on the PRTG server [T1090.001].
- netsh → USES_TECHNIQUE → Internal Proxy
  Source review: The selected exact source passage directly attributes netsh -> USES_TECHNIQUE -> T1090.001. The selected assertion is definite and its endpoint roles match the source.
  Literal support: To facilitate this, they used the netsh command, a legitimate Windows command, to create a PortProxy registry modification [T1112] on the PRTG server [T1090.001].

## AA23-144A:development:llama500:2866:5312

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a

- FRP → USES_TECHNIQUE → Proxy
  Source review: The selected exact source passage directly attributes FRP -> USES_TECHNIQUE -> T1090. The selected assertion is definite and its endpoint roles match the source.
  Literal support: The actor has used Earthworm and a custom Fast Reverse Proxy (FRP) client with hardcoded C2 callbacks [T1090] to ports 8080, 8443, 8043, 8000, and 10443 with various filenames including, but not limited to: cisco_up.exe, cl64.exe, vm3dservice.exe, watchdogd.exe, Win.exe, WmiPreSV.exe, and WmiPrvSE.exe.

## AA22-321A:development:llama500:1806:4233

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

- Hive actors → USES_TECHNIQUE → External Remote Services
  Source review: The selected exact source passage directly attributes Hive actors -> USES_TECHNIQUE -> T1133. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Hive actors have gained initial access to victim networks by using single factor logins via Remote Desktop Protocol (RDP), virtual private networks (VPNs), and other remote network connection protocols [T1133].
- Hive actors → USES_TECHNIQUE → Spearphishing Attachment
  Source review: The selected exact source passage directly attributes Hive actors -> USES_TECHNIQUE -> T1566.001. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Hive actors have also gained initial access to victim networks by distributing phishing emails with malicious attachments [T1566.001] and by exploiting the following vulnerabilities against Microsoft Exchange servers [T1190]:
- Hive actors → USES_TECHNIQUE → Exploit Public-Facing Application
  Source review: The selected exact source passage directly attributes Hive actors -> USES_TECHNIQUE -> T1190. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Hive actors have also gained initial access to victim networks by distributing phishing emails with malicious attachments [T1566.001] and by exploiting the following vulnerabilities against Microsoft Exchange servers [T1190]:
- Hive → USES_TECHNIQUE → Impair Defenses
  Source review: The selected exact source passage directly attributes Hive -> USES_TECHNIQUE -> T1562. The selected assertion is definite and its endpoint roles match the source.
  Literal support: After gaining access, Hive ransomware attempts to evade detention by executing processes to:
Identify processes related to backups, antivirus/anti-spyware, and file copying and then terminating those processes to facilitate file encryption [T1562].

## AA22-321A:development:llama500:3953:6298

Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-321a

- Hive → USES_TECHNIQUE → Modify Registry
  Source review: The selected exact source passage directly attributes Hive -> USES_TECHNIQUE -> T1112. The selected assertion is definite and its endpoint roles match the source.
  Literal support: Prior to encryption, Hive ransomware removes virus definitions and disables all portions of Windows Defender and other common antivirus programs in the system registry [T1112].

## Excluded candidates

- 02.1: NTDS.dit is the Active Directory database file accessed or stolen in this passage, not a Software entity used by the actor.
- 05.2: The source annotates native tools/processes with T1218, but the selected passage does not describe proxy execution of malicious content. Hold this broad behavior/ID mapping for review.
- 05.3: Actors download comsvcs.dll in the T1105 passage; the downloaded DLL is not the subject performing the ingress transfer.
- 06.2: The passage describes actors packing FRP client files with UPX. Passive packaging is not an explicit FRP-performed action; review this Software-to-technique interpretation before import.
- 07.1: Co-occurring incident tactic and technique annotations do not explicitly state a general PART_OF_TACTIC taxonomy relationship.
- 07.2: LOTL names a general living-off-the-land approach, not software. The passage attributes the T1047 command execution to WMIC, not LOTL.
- 07.3: LOTL is an activity category, not software performing offline password cracking. Its occurrence in the appendix title does not support this endpoint.
- 08.3: The source describes deletion of the output file systeminfo.dat, not the systeminfo executable performing deletion. A substring match is not the required software endpoint.
- 09.1: The selected span describes deletion of systeminfo.dat. It does not state that the systeminfo executable performs T1070.004.
- 09.3: The source annotates ping network-connectivity checks with T1016.001, but the selected span does not establish Internet connectivity, the specific frozen technique. Hold the behavior/ID scope for review.
- 09.4: The source records an attempt to use Advanced IP Scanner. Confirmed tool use or execution is not established by this selected passage; preserve the attempt qualification.
- 11.3: The incident collection and archive annotations do not state a general technique-to-tactic taxonomy relationship. Do not infer PART_OF_TACTIC from co-occurrence.
- 11.4: The passage qualifies exfiltration with likely and does not state a general technique-to-tactic taxonomy relationship.
- 17.1: This is a comparison in a defensive detection caveat warning against attributing proxy activity to Volt Typhoon. Hold the indirect FRP attribution rather than treat the caveat as a definite use observation.
- 17.2: The passage establishes downloading comsvcs.dll. It does not explicitly establish executing or using the DLL, so the unconditional USES relationship needs review.
- 22.1: The T1047 annotation belongs to WMIC commands that execute ntdsutil.exe. The spawned tool is not the subject performing the WMI technique.
- 30.2: The source says data exfiltration likely uses a combination including Rclone. This does not establish definite Rclone use.
- 31.1: The reinfection passage allows either Hive ransomware or another variant. Preserve that payload disjunction rather than select Hive as the definite payload of the described reinfections.
- 33.1: The source says a possible combination of Rclone and Mega.nz. Definite Rclone use is not established by this selected statement.
