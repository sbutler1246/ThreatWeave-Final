# Development batch: first-run review and table correction

Reviewed October 13, 2026. Run: `work/development_batch/20261013T073802Z-c6fd876b`.

## Observed result

Two of five scopes produced schema-valid candidates. Three LockBit table scopes failed after one repair each. These are observed development failures; they are not final benchmark results. The original model responses, summary and source inputs remain preserved.

The AnyDesk output initially represented a technique using the ID string as its name, then changed the actor-to-tool relationship to the invalid `ASSOCIATED_WITH` predicate during repair. The Atera output used a missing endpoint and then attached T1219 to the software. The Backstab output used missing endpoints, assigned a technique ID to software and selected an invalid `USES` relationship from software to technique.

## Prose candidate review

The following generated relationships are explicitly supported by their saved source passages:

| Scope | Candidate | Source review |
| --- | --- | --- |
| AA23-136A:development:paragraph:27502 | BianLian group actors → USES → Rclone | The passage explicitly says the actors used Rclone to exfiltrate data. |
| AA23-353A:development:paragraph:10240 | ALPHV Blackcat/ALPHV affiliates → USES → Evilginx2 | The passage explicitly says the affiliates use the framework to obtain credentials and session cookies. |

This is AI-assisted source inspection, not a claim of human verification. The model's confidence of 1.0 does not establish correctness. The group qualifiers remain intact. Post-extraction identity resolution maps the exact Rclone mention to ATT&CK S1040; the actor mentions and Evilginx2 remain unresolved in the selected active reference catalog. Preserve unresolved mentions as source-scoped local identities during any later ingestion rather than inventing canonical mappings.

## Table-format correction

The table output now has named `actor`, `software` and `technique` slots. Slot names, types and explicit IDs are constrained by the source's caption and column values. Each generated relationship must use the slot IDs with the applicable schema predicate. The model may return an empty relationship list. The adapter reorganizes generated slots into an `ExtractionBatch`; it does not add or repair relationships.

This is structured table ingestion with source-derived role constraints. It must be described separately from unconstrained entity discovery in prose. It uses no gold relationship labels. ATT&CK historical labels are retained in the source slots; canonical identity resolution still uses the explicit source ID and frozen release 17.1.

## Retry the failed scopes

The new option selects only `validation_failed` or `service_error` scopes from the specified prior run and verifies their development membership and frozen source checksums. It writes a new run, preserving the previous records. The installed model digest must also match the original batch.

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\batch_extract.py" --retry-run "S:\ThreatWeave\work\development_batch\20261013T073802Z-c6fd876b"
```

Expected input count: three table scopes. Candidate counts and live success remain unknown until this retry runs. Review the new relationships before Neo4j ingestion.
