# Extract the remaining prepared development windows

October 15, 2026. The next batch covers 44 windows from the same five non-held-out reports already prepared. It excludes the ten windows from the completed v2.6 pilot. This expands development coverage; it does not complete the fifteen-report corpus or final evaluation.

**Completed checkpoint:** The operator processed this batch in `work/corpus_extraction_batch/20261015T170956Z-255671f4`. The two failed windows were recovered in separate offline artifacts while preserving their original failures. [Source review and the prepared import](ThreatWeave_corpus_batch_ingestion_step.md) select 53 Supported assertions, hold ten for review and reject five. Use the import step next; another extraction run is not needed for this checkpoint. The following command and resume details remain historical/operator recovery instructions.

Keep Ollama running, then run this in a separate PowerShell terminal if the application is still open:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\extract_corpus_batch.py"
```

The assistant completed the offline preview and checks; the operator runs this live extraction. No additional packages or Neo4j credentials are needed. Wait for `BATCH PROCESSED`, then share the final status and saved-results path for source review.

The runner preserves the v2.6 prompt, source selector, frozen Llama digest and generation settings: temperature 0, context 8192, output 700, at most four relations per window and one schema/source repair. Four relations remains a diagnostic cap, so processing all windows does not establish exhaustive extraction or final recall. Empty output is allowed and still needs review. Three windows have no recognized source mentions under the existing selector; this may limit coverage.

Fresh records go into `work/corpus_extraction_batch/<run>` and a readable review goes directly into `docs/ThreatWeave_corpus_extraction_batch_<run>.md`. The plan binds all 44 scope IDs, the excluded ten scope IDs, prepared fingerprint, pinned pilot summary, review-manifest checksum and extraction configuration. Each run records raw responses, source windows, prompts, validations, candidate identities, attempts and timing. No candidates are automatically imported, no graph writes occur, and the application's current indexes remain the existing development snapshot.

If interrupted or some windows fail, use `--resume-run` with the most recent saved batch folder. The folder is printed at startup as well as completion. Resume checks the entire linked run history, revalidates source evidence and saved successful output, and processes only failed, interrupted or never-started windows. Completed empty extractions are also preserved. Resume creates a new linked folder; it never overwrites earlier results. An interrupted run may have no finished summary or readable review, but its saved case records can still be resumed. Each finished summary counts only windows attempted in that run; a resume may report fewer than 44, and review must include its linked predecessors.

After extraction, the next step is semantic source review of all new candidates and overlap with the original pilot. Review decisions must precede any import or index refresh. Human verification and final benchmark work remain pending. Source selection reads split metadata to exclude held-out reports; gold triples and QA reference answers do not enter extraction.

## Offline checkpoint

Preflight receipt: `work/corpus_batch_preflight/20261015T170743Z-f42a804e/receipt.json`.

Plan fingerprint: `64c42372a806926f31c2b53000d294b5699e506783b4d1d109ecf55a012a27b8`.

| Report | Additional windows |
| --- | ---: |
| BianLian / AA23-136A | 11 |
| Rhysida / AA23-319A | 11 |
| Scattered Spider / AA23-320A | 8 |
| ALPHV Blackcat / AA23-353A | 4 |
| Phobos / AA24-060A | 10 |
| Total | 44 |

All frozen source/tokenizer/catalog checks and estimated prompt budgets passed. Estimated system/prompt/schema sizes range from 1335 to 4459 tokens, plus the unchanged 700 output and 256 reserved chat tokens within context 8192. These are preflight estimates, not live formatted-prompt measurements. All 40 offline corpus tests passed, including eight new batch selection/resume checks and the original pilot/import/reference regressions. Tests used simulated service responses; no live extraction has been run for this batch yet.
