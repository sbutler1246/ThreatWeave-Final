# ThreatWeave development extraction batch

Prepared October 13, 2026. This step expands the single-row extraction pilot to five source passages across three CISA advisories. It produces model-generated candidates and identity-resolution records for review. It does not measure final extraction accuracy or add facts to Neo4j.

## Selected inputs

| Report | Source | Source format | Assignment |
| --- | --- | --- | --- |
| AA23-165A — LockBit | Table 4 row03: AnyDesk | Table row with caption and headers | Existing development scope |
| AA23-165A — LockBit | Table 4 row04: Atera Remote Monitoring & Management (RMM) | Table row with caption and headers | Existing development scope |
| AA23-165A — LockBit | Table 4 row05: Backstab | Table row with caption and headers | Existing development scope |
| AA23-136A — BianLian | Prose passage at document offsets 27502:27690 | Unstructured text | Additional development scope |
| AA23-353A — ALPHV Blackcat | Prose passage at document offsets 10240:10400 | Unstructured text | Additional development scope |

Table row identifiers follow the existing benchmark scope names, not a new physical row count. Their boundaries were projected from prior source annotation metadata without annotated entity names or relationship labels. The batch reads source text directly at those offsets. Its runtime does not read gold triples, evaluation questions, reference answers, or reference triples.

Additional prose scopes are declared separately in `extraction/development_batch_sources.json`. The existing benchmark split is unchanged. Additional source documents are allowed only when they contain no held-out scopes in the existing split manifest. The script checks this before any model call. These prose passages have not been exhaustively annotated and are not scored as gold extraction scopes.

## Run

Keep Ollama running with `llama3.1:8b` installed. The existing Python 3.12 environment contains the dependencies needed for this step.

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\batch_extract.py"
```

For an offline input preview:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\batch_extract.py" --preview
```

If Ollama is slow, use `--timeout 180`. The timeout applies to each response. Each scope gets at most one schema/source repair. A failed scope is recorded separately, allowing other scopes to continue. Empty extraction is reported explicitly rather than treated as a successful relationship extraction.

## Output and review

Each execution saves a new timestamped directory under `S:\ThreatWeave\work\development_batch`. Each scope has its exact chunk and source metadata, saved prompts, model responses, extraction candidates and identity-resolution records. The batch summary includes model digest, generation settings, source hashes, counts, errors and per-attempt elapsed times.

After the first live batch exposed table-role and endpoint errors, table responses were changed to source-constrained actor/software/technique slots with optional generated relationships. The adapter converts those slots to the common candidate model without adding relationships. Prose extraction keeps its existing format. Use `--retry-run <previous run folder>` to rerun only failed scopes; a new run is saved. See [the first-run review](ThreatWeave_development_batch_first_run_review.md).

A review document is also saved directly into `S:\ThreatWeave\docs` as `ThreatWeave_development_batch_review_<run>.md`. It pairs each candidate relationship with the actual source text and inherited table context. Check factual support before importing these candidates into Neo4j.

Pydantic enforces endpoint types and literal evidence spans. Source-ID checks reject invented or incompatible ATT&CK IDs. The identity resolver uses the frozen active ATT&CK 17.1 catalog and records unresolved names without silently asserting a canonical identity. Advisory labels can differ from current canonical names: for example, the source's “Remote Access Software” label for explicit T1219 resolves to “Remote Access Tools” in the frozen 17.1 reference. The reported spelling is preserved and is not added as a verified alias.

## Verification and limitations

The offline preview passed for all five passages: source checksums, split boundaries, exact spans, inherited contexts and output schema preparation. The repository's offline tests cover held-out-scope rejection, additional-report separation, historical label resolution, subtechnique labels, tampered evidence, wrong entity/ID types, invented IDs and affiliate qualifiers.

Live execution is delegated to Stephen Butler. Candidate counts, model performance and semantic support remain unknown until the saved output is reviewed. The current three-hop QA script remains confined to the original LockBit development row; batch ingestion and broader retrieval are subsequent steps. This batch does not complete the planned full-corpus chunking, hybrid retrieval or final evaluation.
