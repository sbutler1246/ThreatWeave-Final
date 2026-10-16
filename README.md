# ThreatWeave — Final Project

**Stephen Butler · CS 6338 · October 16, 2026**

ThreatWeave is a local GraphRAG application for cybersecurity questions grounded in CISA advisories and a frozen Enterprise ATT&CK 17.1 reference. It combines a Neo4j knowledge graph, Chroma vector stores, MiniLM text embeddings, Node2Vec graph embeddings and Ollama Llama 3.1 8B. The interface exposes cited passages and the directed graph paths supplied to generation.

This separate repository contains the final submission snapshot. The [earlier ThreatWeave repository](https://github.com/sbutler1246/ThreatWeave) preserves the Milestone 2 checkpoint. Source snapshots, benchmark labels and collected answers retain their original bytes. See [PUBLICATION_SNAPSHOT.json](PUBLICATION_SNAPSHOT.json) for the source-archive identity and the documentation adapted for publication.

## Final deliverables

- [Final report — 14 pages](outputs/final_submission/ThreatWeave_final_report.pdf)
- [Editable report](outputs/final_submission/ThreatWeave_final_report.md)
- [Final slides — 16 slides](outputs/final_submission/ThreatWeave_final_slides.pptx)
- [Demo walkthrough — 5:34 MP4](outputs/final_submission/ThreatWeave_demo.mp4)
- [Demo transcript](outputs/final_submission/ThreatWeave_demo_transcript.md) and [captions](outputs/final_submission/ThreatWeave_demo_captions.srt)
- [Complete source/evidence archive](outputs/ThreatWeave_submission_v2.zip), [archive verification](outputs/ThreatWeave_submission_v2.verification.json), and [artifact checksums](outputs/final_submission/DELIVERABLES_SHA256.json)

The demo is a labelled replay of authentic saved application states with synthetic narration. It makes no new model/database calls. A separate recording of the slide presentation in the author's voice will be added after recording. No course-portal submission is implied by repository publication.

## What was evaluated

The frozen experiment contains 20 final questions, four retrieval conditions and three repeats, giving 240 measured outcomes after four excluded warm-ups. Conditions are text only, graph only, hybrid without Node2Vec and full hybrid. They share a source scope containing 101 CISA windows and 190 ATT&CK reference parents, with 510 text chunks, 212 domain graph nodes and 394 accepted directed facts.

Collection produced 210 valid non-abstaining answers, 15 abstentions and 15 generation-validation failures. Automatic evaluation accounts for all 720 metric slots: 639 numeric values, 36 evaluator output-limit failures and 45 unavailable slots. Validation success does not establish semantic correctness.

### Main findings

| Measurement | Result |
|---|---|
| Extraction precision / recall / F1 | 0.4545 / 0.0671 / 0.1170 against 149 source-scoped assertions |
| Extraction target | F1 ≥0.80 not met |
| Full-hybrid human factuality / completeness / coherence | 3.350 / 2.000 / 3.900 out of 5, 20 numeric answers each |
| Text-only human completeness | 1.889 out of 5, 18 numeric answers |
| Available-mean completeness gain | +0.111, below the proposed +0.50 target |
| Paired completeness, hybrid minus text | +0.167, n=18 questions, exploratory 95% interval [-0.278, 0.611] |
| Automatic faithfulness, hybrid / text | 0.626 (52/60) / 0.568 (40/60) |
| Joint QA target | Not met |

All 80 primary review entries and 20 secondary entries are complete. The secondary review is the same author's declared delayed rescore. There was limited AI assistance for review questions. The reviews measure within-reviewer consistency, not independent inter-rater reliability. Secondary ratings do not replace or average into primary ratings.

The small benchmark, unequal availability, partial blinding, MODE/evidence-format differences and shared-model judging limit generalization. Five extraction nonmatches may reflect annotation/granularity gaps. No frozen labels or answers were replaced to improve the scores. The actual evidence cap is 3,000 UTF-8 bytes. Claim-level unsupported-claim rates and CPU/GPU/service resource measurements were not separately collected.

## Repository map

| Location | Contents |
|---|---|
| benchmarks/ | Frozen questions, reference answers, gold assertions and split |
| data/ | Frozen CISA source snapshots and Enterprise ATT&CK 17.1 |
| extraction/, resolve.py | Bounded assertion extraction and typed identity resolution |
| graph/, retrieval/ | Graph import, projection, indexes and evidence retrieval |
| application_engine.py, streamlit_app.py | Local application adapter and evidence inspection interface |
| demo_replay.py | Saved-run demonstration using the original renderer |
| evaluation/ | Frozen collection/scoring methods and offline analysis |
| docs/ | Final-review records and dated development checkpoints |
| work/ | Curated preserved experiment evidence, receipts and analyses |
| outputs/final_submission/ | Final report, presentation and demo artifacts |

Historical checkpoint documents and notices retain the status they had when written. The final report and this README describe the completed evaluation. config.json preserves the original design configuration; recorded runtime settings and receipts describe actual runs.

## Run the saved demonstration

Use Python 3.12. This replay needs Streamlit and Pydantic, with no Neo4j database, Ollama server or model download:

```text
python -m venv .venv
.venv\Scripts\python.exe -m pip install "pydantic>=2,<3" -r requirements-application.txt
.venv\Scripts\python.exe -m streamlit run demo_replay.py --server.address=127.0.0.1 --server.port=8502
```

Open the localhost URL shown by Streamlit. Choose either saved Rhysida run to inspect its sources, graph and export. The original renderer retains historical pending-review notices. Its graph inspection may add display-column metadata to an export without changing the answer or evidence.

## Live application and reproducibility

The live application requires the documented Neo4j, Ollama, embedding, graph/vector-index and application dependencies. Follow [application setup](docs/ThreatWeave_application_setup_step.md), [the setup checkpoint](docs/ThreatWeave_application_setup_checkpoint.md) and the preserved index receipts. Installed environments, credentials, model weights and vector-store caches are excluded. This repository is a source/evidence snapshot, not a preinstalled portable runtime.

The separately hash-locked evaluator environment is documented in [evaluation/DEPENDENCIES.md](evaluation/DEPENDENCIES.md). Do not install its pins over an application environment. The frozen QA and scoring cohort must not be rerun or tuned to improve the reported results.

Authoritative analyses:

- [Extraction analysis](work/extraction_scoring_analysis/20261016T171118Z-dc75fabd/report.md)
- [Automatic analysis](docs/ThreatWeave_final_scoring_results_20261016T075220Z-1e84d02c.md)
- [Human analysis](work/human_scoring_analysis/20261016T174034Z-7c181a33/report.md)
- [Combined result data](work/final_completion/submission_results.json)

Original run receipts retain absolute paths from S:/ThreatWeave. A relocated checkout may require explicit path arguments or path adaptation for audit entry points. Preserved output hashes bind the original inputs. Publication documentation is separate from those frozen inputs.

## Checks

Forty-three targeted application/scoring/reporting tests passed at the final checkpoint. Ten relevant human/reporting tests also passed after the method-declaration update. Existing offline checks can be run with the documented dependencies:

```text
python -m unittest discover -s tests -p test_application.py
python -m unittest discover -s tests -p test_human_analysis.py
python -m unittest discover -s tests -p test_submission_analysis.py
python evaluation/check_benchmarks.py
```

The application tests use simulated adapters. Earlier live graph-only and full-hybrid interactions are documented separately. Additional live text-only/ablation and multi-answer navigation flows remain unverified.
