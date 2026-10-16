# Development batch: source review and Neo4j import

Prepared October 13, 2026. The latest table retry (`20261013T074906Z-23e86db5`) returned three complete actor/software/technique chains with six candidate relationships. The earlier retry also succeeded and remains preserved. The original batch (`20261013T073802Z-c6fd876b`) supplies the two successful prose extractions.

AI-assisted source inspection and explicit source-role checks support all eight selected generated relationships. This is not a claim of human verification or a held-out accuracy result. The source review preview is saved separately in this project's `docs` folder.

## Import

Keep the ThreatWeave Neo4j instance running. Run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\ingest_batch.py"
```

Press Enter for the URI (`bolt://localhost:7687`), username (`neo4j`) and database (`neo4j`), then enter the database password. Passwords are neither saved nor included in logged errors.

The importer selects the latest successful output for each of the five declared development scopes. It verifies frozen sources, saved chunks, prompts, completed model responses, raw output/candidate agreement, identity resolution and source support before opening the database. It imports only actual generated relationships.

Expected target records: five source scopes across three CISA reports, ten distinct target entities and eight extracted relationship assertions. Target entity count includes reused nodes and is not a count of newly created nodes. The eight relationships are six table links plus two prose actor-to-tool links. MITRE mitigation references are not added by this step.

Each unresolved entity receives a stable source-scoped local identity. The existing LockBit Affiliates identity is reused. T1219 is stored as canonical Remote Access Tools, while the source mention Remote Access Software is preserved in occurrence and evidence records. T1562.001 resolves to Disable or Modify Tools. Rclone resolves by its verified reference name; the qualified BianLian/ALPHV actor mentions and Evilginx2 retain local identities.

The transaction uses MERGE and stable IDs, preserves existing assertion review decisions and rolls back on source/identity conflicts or failed verification. A repeat of the same selected input records adds no duplicate source assertions or domain edges. Different model outputs can produce separately traceable assertions supporting the same merged factual edge.

Every assertion retains source document/chunk, exact evidence span, inherited context, model digest/settings, prompt/raw output hashes, source review method and extraction method. They remain `origin=extracted`, with validated source checks and human review pending. Confidence values are model self-reports, not proof of support. MENTIONED_IN represents literal occurrence rather than an additional factual relationship.

Each attempt saves prepared records and a review document under the ThreatWeave folder. After a successful transaction, `work/batch_ingestion/<run>/import_receipt.json` records the verified counts. Live database execution remains pending until the command runs.

## Following step

Once this import succeeds, broaden graph retrieval beyond the original pilot scope and import the applicable direct ATT&CK mitigation references for the new techniques. The current QA pilot still restricts retrieval to `AA23-165A:table4:row02`; ingesting the batch alone does not change that restriction or complete text/hybrid retrieval.
