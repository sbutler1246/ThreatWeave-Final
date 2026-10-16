# Mitigation references for the new development techniques

Prepared October 13, 2026, following successful import of five CISA scopes and eight extracted assertions. The saved import receipt is `work/batch_ingestion/20261013T075757Z-df5559f6/import_receipt.json`.

The frozen Enterprise ATT&CK 17.1 snapshot has five direct mitigation associations for T1219 (Remote Access Tools) and five for T1562.001 (Disable or Modify Tools). This step imports those ten source-backed reference relationships.

| Technique | Direct mitigation IDs |
| --- | --- |
| T1219 | M1031, M1034, M1037, M1038, M1042 |
| T1562.001 | M1018, M1022, M1024, M1038, M1047 |

These are reference associations from the frozen release. A subtechnique receives only its own direct STIX `mitigates` relationships. The importer does not infer mitigation inheritance or incident effectiveness. Mitigation identities can be shared across techniques; ten relationships refer to nine distinct mitigation entities, including entities already imported for T1046.

The legacy pilot import helper now accepts a technique ID and source scope while retaining its original T1046 defaults and stable provenance IDs. The batch wrapper imports both techniques in one transaction. Source conflicts, identity conflicts, rejected prior assertions or failed path verification cause the transaction to roll back. Existing human verification statuses are preserved.

## Run

Keep the ThreatWeave Neo4j instance running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\import_batch_mitigations.py"
```

Press Enter for the default URI, username and database, then enter the database password. The script records reference source hashes, exact normalized STIX fields and relationship-description spans, STIX IDs, release and `origin=fused`. Passwords are not logged.

Expected verification: ten reference assertions and fifteen three-hop paths across AnyDesk, Atera and Backstab. AnyDesk and Atera each connect to five T1219 mitigations; Backstab connects to five T1562.001 mitigations. These counts cover the newly imported development rows; the earlier Port Scanner pilot remains separately traceable.

Prepared records and the import receipt are saved under `work/batch_mitigation_import/<run>`. Live import remains pending until the command runs. The offline preview checks the snapshot and selected relationships; it does not establish database connectivity.

## Next step

Broaden graph retrieval to all imported development scopes. The existing QA pilot still targets its original source row. The new CISA ingestion and mitigation imports alone do not change that query or complete the planned text/hybrid retrieval system.
