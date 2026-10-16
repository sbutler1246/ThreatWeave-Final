# Portable reproduction verification

October 16, 2026. Added after the original experiment and first final-repository publication. These checks do not change the original questions, labels, prompts, collected answers or scores.

## Verified locally

- Copied the repository files to a separate temporary checkout on **C:**, away from the original **S:** project. No installed environments, model caches or live vector stores were copied into that checkout.
- Created a **new empty Python 3.12 environment** and installed `requirements-portable.txt` from public package distributions. `pip check` passed. The complete resolved Windows package versions are in `requirements-portable-windows.lock.txt`.
- Ran `python -S reproduce_results.py` in that separate checkout. All preserved-input checks, human analyses, extraction statistics, native metric audits, paired intervals, timing summaries and report targets matched. The command audited 720 metric slots and recomputed 414 saved-verdict formulas with no services or inference.
- Repeated the statistics check under a Python file-access audit hook that **rejects original-project file reads**. Only the new environment and the external test harness itself were exempt. It passed.
- Validated the portable bundle with all historical extraction working folders absent: **53 CISA source windows, 139 ATT&CK references, 142 domain nodes and 245 directed facts**, matching the original development scope fingerprint `ab3732f875177906c400d82268fbbeed719b9a26b4f3836215d713821bd9beb8`.
- Downloaded the pinned MiniLM revision from public Hugging Face into the separate checkout's initially empty cache.
- Downloaded an official **Neo4j Community 5.26.0** distribution and started disposable databases on separate loopback ports. Imported **263 original accepted assertions**, their documents/chunks, identities and original mention semantics. Source-mention and live directed-projection checks passed. The existing project database was untouched.
- Built a fresh text index: **305 source chunks and 384-dimensional vectors**. Built fresh Node2Vec/Chroma graph assets: **142 normalized 128-dimensional vectors**, including exact-vector lookup checks.
- Exercised **all four live application modes** from the relocated checkout, with original-project file reads blocked. These are new development smoke answers saved separately, not replacements for the frozen experiment. The test used the existing local Ollama service/model; model weights were not redownloaded for this test.
- Rendered the portable application and saved replay with Streamlit AppTest in the new environment, with original-project reads blocked.
- **48 targeted tests passed** in the separate checkout and new environment, including path-escape rejection, source-bundle tampering, missing historical folders, schema-comment parsing, application behavior and scoring/reporting checks.

The automated workflow in `.github/workflows/reproduction.yml` separately checks the service-free statistics and source bundle on GitHub-hosted Windows and Linux runners. A workflow definition is not evidence of a successful run; inspect the repository's Actions tab for the actual status.

## Reproduction boundaries

This was a fresh environment, fresh database/index build and relocated-filesystem test on the same physical Windows computer. It is not a second person's or second physical computer's review. A fresh reader downloads their own dependencies and models and runs their own services.

The portable UI rebuilds the original **development** source scope. The frozen final experiment used a larger shared evaluation scope; its collected statistics are independently recalculated by `reproduce_results.py`. The original collectors/evaluator scripts remain historical research tools with their original receipts. A fully automated regeneration of raw extraction, the 240 model outcomes and new human judgments is not claimed.

Extraction scoring reuses the included aligned pre-review predictions. Native answer-relevancy cosines are checksum-verified, rather than recomputed with embedding inference. No new human scores are manufactured. New model outputs can differ across runtimes and hardware; a successful live smoke test does not establish answer correctness or improve the reported quality targets.

The portable adapter leaves frozen source code intact. It supplies a complete hash-bound accepted source bundle to the existing retrieval, generation and indexing implementations. Original absolute `source_run` strings remain provenance metadata; the portable workflows do not open those paths.

Start with [REPRODUCE.md](REPRODUCE.md) for the runnable commands.
