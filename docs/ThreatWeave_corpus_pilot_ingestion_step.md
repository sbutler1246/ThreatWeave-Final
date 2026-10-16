# Import the source-reviewed corpus pilot

October 14, 2026. The completed v2.6 extraction produced 37 candidates across all ten development windows without empty results, failures or repairs. [Source review](ThreatWeave_corpus_extraction_pilot_v2_6_development_review.md) provisionally supports 34 and leaves three uncertain/conditional candidates for review. No new extraction run is required.

The import completed with 34 extracted assertions across ten source windows/five CISA reports and 39 target entities, with three Review candidates excluded. The saved transaction time is 3.239 seconds, including verification; counts include reused records and human verification remains pending. See [the completed graph checkpoint](ThreatWeave_corpus_pilot_graph_checkpoint.md). The current next command is [the direct mitigation reference import](ThreatWeave_corpus_pilot_mitigation_step.md); the source-import command below is retained for an intentional repeat. All 167 offline tests and the reference preview pass.

## Run

Keep the ThreatWeave Neo4j instance running, then run:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\ingest_corpus_pilot.py"
```

Press Enter for the default URI (`bolt://localhost:7687`), username (`neo4j`) and database (`neo4j`). Enter the database password when prompted; typing is hidden and the password is not saved. Ollama is not needed.

The command verifies source/model/output/evidence/review checks before connecting, then imports the exact supported selection atomically. Source conflicts, missing constraints or incomplete verification stop the import. Stable IDs preserve repeated-import behavior and existing assertion review decisions.

Prepared records and an import receipt save under `work/corpus_pilot_ingestion/<run>`. The readable source preview saves directly in `docs`. The receipt records verified assertion counts and transaction time, including conflict checking, verification and any driver retries. This is a small development measurement of processed assertions, not a new-insert or full-corpus throughput benchmark.

The fixed [review manifest](ThreatWeave_corpus_pilot_v2_6_review.json) pins extraction run `20261015T035023Z-f4b7051e`; newer extraction outputs are not automatically substituted. All accepted assertions retain exact support, review reasons/flags, model/raw/prompt metadata and human-review-pending status. The source-reported AveMaria/WarZone alias resolves to S0670 without altering the frozen catalog.

An offline repeat preview is available with `--preview`; it opens no database connection. The completed preview is [saved here](ThreatWeave_corpus_pilot_import_20261015T035611Z-b96fba19.md).

## Following work

After a successful receipt, review the database counts and measured transaction time before preparing relevant mitigation references and expanded retrieval/index scopes. This import does not by itself refresh Chroma/Node2Vec indexes, change current QA scope filters, complete extraction of the other prepared windows, or run held-out evaluation.
