# Prepare the five-report extraction pilot

The source-tokenizer runtime check passed. This next step creates source-only extraction-window records for the planned five-report timing/overlap pilot.

## Run

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\prepare_corpus_pilot.py"
```

No running services, password or package installation is required. The command reads frozen CISA snapshots, the verified tokenizer artifact, chunking configuration and split metadata. It does not read gold triples or QA reference answers, extract candidate facts, query the model or write to Neo4j.

## Selection and windows

The five reports contain no held-out evidence scopes: BianLian (AA23-136A), Rhysida (AA23-319A), Scattered Spider (AA23-320A), ALPHV Blackcat (AA23-353A) and Phobos (AA24-060A). This is a broader development pilot, not the complete 15-report corpus or the final benchmark set.

For each report, the prepared technical section starts after its standalone Technical Details heading and ends before its standalone Mitigations heading. Original normalized source text and offsets remain intact. Raw and normalized source checksums are verified. IOC and technique-table content within this section is retained; tables and contextual actor attribution require careful semantic review during extraction.

Windows prefer line endings within the configured 400–600 source-token range, targeting 500 tokens and about 60-token overlap. Inherited title/heading/nearby caption context is stored as separate exact source spans and measured separately. Final windows may be anchored at the section end with greater overlap to avoid an undersized trailing fragment; actual overlap and that exception are recorded. No source characters are dropped.

The verified tokenizer artifact is preserved. An in-memory byte-level decoder correction preserves leading spaces without changing token IDs or token counts; the derived tokenizer hash and correction policy are included in the chunk fingerprint.

## Assistant preview

| Report | Prepared windows | Source-token range | Selected pilot windows |
| --- | ---: | ---: | ---: |
| AA23-136A | 13 | 464–579 | 2 |
| AA23-319A | 13 | 448–590 | 2 |
| AA23-320A | 10 | 450–524 | 2 |
| AA23-353A | 6 | 490–504 | 2 |
| AA24-060A | 12 | 465–508 | 2 |
| Total | 54 | 448–590 | 10 |

The first two technical windows per report are selected deterministically. Selection does not depend on model outputs or evaluation labels. The preview verified frozen-source checksums, held-out report exclusion, exact spans, Unicode round trips, measured token bounds and overlap. All 106 offline unit tests passed, including coverage, final-window handling and leading-space preservation checks.

## Saved records and subsequent work

The command creates a new timestamped directory under `S:\ThreatWeave\work\corpus_pilot_chunks`, with all 54 window records, the ten-window pilot subset, settings, source hashes, tokenizer identity and a preparation summary. It publishes a current chunk-run pointer and saves a readable source-window review directly into `S:\ThreatWeave\docs`.

The next stage will extract bounded candidates from these ten windows and record per-attempt time, schema/source failures, model/prompt hashes and overlap deduplication. The old small-chunk batch prompt forces an entire-window evidence quote and should not be reused unchanged for these longer windows under the 700-token output budget. A longer-window extractor needs short literal supporting quotes with validated source offsets.

Graph-write throughput, indexing time and resource use still require later pilot stages; chunk preparation alone does not complete the timing/overlap pilot. The existing development graph and indexes remain unchanged. Full-corpus ingestion, refreshed indexes, application integration and final controlled evaluation remain pending.
