# QA source and benchmark review — October 5, 2026

Stephen Butler manually validated all 61 questions first, then requested Codex to cross-check them. Review completion was recorded on October 5, 2026. Every QA record names Stephen Butler as the human reviewer and retains the subsequent AI cross-check details with verification_method=human_review_with_ai_crosscheck. This checks benchmark questions and reference answers. No system-generated answers, human scores, or performance results are claimed.

## Corrections

- Q033 and Q038 now specify different ngrok paragraphs and purposes, resolving their identical original questions.
- Q030 retains historical observation; Q038 and Q039 retain the source qualification “in some instances.”
- Q034 explicitly treats the FileZilla/Archive via Utility mapping as reported by the source, without inventing an archiving capability.
- Q050–Q053 references now include the requested actor-to-tool link. All Q050–Q057 lists cover every direct active mitigation link in frozen ATT&CK 17.1.
- Q058–Q061 explain the mapping comparison, including parent technique versus LSASS sub-technique where relevant.
- All questions now carry exact document/passage path attribution and source URLs; all assignments are recorded.

## Split

Final test: 20 questions (8/8/4); development: 21; held-out reserves: 20. Held-out CISA scopes: 18; development CISA scopes: 21; shared scopes: 0. AA23-165A is present in both sets using separate table rows. Final labels must not tune prompts/retrieval or enter retrieval stores.

## Per-question decisions

|Question|Decision|Assignment|Review finding|
|---|---|---|---|
|Q001|passed|final_evaluation|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q002|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q003|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q004|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q005|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q006|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q007|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q008|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q009|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q010|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q011|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q012|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q013|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q014|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q015|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q016|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q017|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q018|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q019|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q020|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q021|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q022|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q023|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q024|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q025|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q026|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q027|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q028|passed|reserve|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q029|passed|development|The exact Table 4 caption establishes LockBit affiliate use; the selected row names the tool and technique ID. The reference includes both facts and limits the mapping to reported repurposed use.|
|Q030|passed_after_correction|final_evaluation|Historical Royal observation retained; Chisel is in the named tool list linked to T1572 for C2 communication.|
|Q031|passed|final_evaluation|Akira use of Mimikatz is explicitly in the T1003 credential-scraping sentence; the preceding LSASS/Kerberoasting wording is not reassigned to this tool.|
|Q032|passed|reserve|Akira use of LaZagne is explicitly in the same T1003 credential-scraping sentence.|
|Q033|passed_after_correction|final_evaluation|Question restricted to paragraph 11788: encrypted ngrok C2 tunnels are mapped to T1572. Distinct from Q038.|
|Q034|passed_after_correction|reserve|The source groups FileZilla and WinRAR for collecting data with T1560.001. Retain that source-reported mapping without claiming FileZilla itself archives files.|
|Q035|passed|reserve|The source groups WinRAR and FileZilla for collecting data with T1560.001; no uncited capability is substituted.|
|Q036|passed|reserve|WinSCP is explicitly named in Akira exfiltration activity mapped to T1048.|
|Q037|passed|reserve|RClone is explicitly named in Akira exfiltration activity mapped to T1048; canonical Rclone capitalization does not alter the entity.|
|Q038|passed_after_correction|reserve|Question restricted to paragraph 12198 and the in some instances ngrok exfiltration sentence mapped to T1090. Distinct from Q033.|
|Q039|passed_after_correction|final_evaluation|The in some instances qualification is retained for Black Basta affiliate deployment of Backstab against EDR with T1562.001.|
|Q040|passed|final_evaluation|Play use of Mimikatz is explicit; T1003 mapping is supported by the Play additional_support passage of GT062, not borrowed from Akira.|
|Q041|passed|final_evaluation|LockBit 3.0 affiliate rclone use and T1567.002 mapping are explicit; actor identity is kept distinct from generic LockBit affiliates.|
|Q042|passed|reserve|Medusa Mimikatz use for LSASS dumping is explicitly mapped to T1003.001; TA0006 is a tactic, not another technique.|
|Q043|passed|reserve|Medusa uses Rclone for exfiltration to its C2 servers with the advisory citation T1567.002. That citation is not assigned to Bandizip archiving.|
|Q044|passed|final_evaluation|Medusa use of PsExec and its cited T1569.002 mapping are explicit; the neighboring RDP technique is not assigned to PsExec.|
|Q045|passed|reserve|The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool.|
|Q046|passed|reserve|The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool.|
|Q047|passed|reserve|The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool.|
|Q048|passed|reserve|The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool.|
|Q049|passed|reserve|The FBI-identification list names the tool within the Medusa RMM paragraph mapped to T1219. The question keeps that paragraph scope; neighboring RDP, PsExec, and encryption references are not intrinsic behaviors of every listed tool.|
|Q050|passed_after_correction|final_evaluation|All 3 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link.|
|Q051|passed_after_correction|final_evaluation|All 10 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link.|
|Q052|passed_after_correction|final_evaluation|All 4 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link.|
|Q053|passed_after_correction|final_evaluation|All 1 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate. Reference corrected to explicitly include the requested LockBit affiliate-to-tool link.|
|Q054|passed_after_correction|final_evaluation|All 8 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate.|
|Q055|passed_after_correction|final_evaluation|All 1 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate.|
|Q056|passed_after_correction|final_evaluation|All 5 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate.|
|Q057|passed_after_correction|final_evaluation|All 7 direct active mitigation links were checked against the complete frozen STIX snapshot. Advisory mapping and reference recommendations remain separate.|
|Q058|passed_after_correction|final_evaluation|Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports.|
|Q059|passed_after_correction|final_evaluation|Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports.|
|Q060|passed_after_correction|final_evaluation|Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports.|
|Q061|passed_after_correction|final_evaluation|Both independent source paths and document-specific supporting passages checked. Reference explicitly explains how the two mappings compare; no relationship is transferred between reports.|
