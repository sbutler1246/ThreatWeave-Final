# ThreatWeave

**Stephen Butler | CS 6338 | Final project artifacts, October 16, 2026**

ThreatWeave is a development GraphRAG application for answering cybersecurity questions using CISA advisories and MITRE ATT&CK. It combines a Neo4j knowledge graph, Chroma vector retrieval, MiniLM text embeddings, Node2Vec graph embeddings, and a local Ollama Llama 3.1 8B model.

## Current completion status

The frozen final experiment is collected and automatically scored: 240 measured outcomes, with 210 valid non-abstaining answers, 15 abstentions and 15 generation-validation failures. All 720 automatic metric slots remain accounted for: 639 numeric values, 36 evaluator output-limit failures and 45 unavailable slots. The collected answers will not be regenerated. These execution counts do not establish semantic correctness.

[Source-only extraction evaluation](docs/ThreatWeave_extraction_results_20261016T171118Z-dc75fabd.md) is complete, including the per-predicate breakdown. Exact agreement with 149 source-scoped annotated assertions gives TP10, FP12, FN139, precision 0.4545, recall 0.0671 and F1 0.1170. The proposed F1 target of 0.80 is not met. Five exact nonmatches may expose annotation coverage or granularity gaps; frozen labels and outputs remain unchanged. Predictions outside the 39 complete gold scopes remain retained but unscored.

All 80 primary human-review entries and all 20 secondary entries are complete. Both completed exports passed validation before the condition key was opened. The author performed the delayed rescore. There was limited AI assistance for review questions. This measures within-reviewer consistency, not independent inter-rater reliability. The original progress files remain preserved.

Full hybrid's available primary human means are factuality 3.350, completeness 2.000 and coherence 3.900 out of 5 (20/20 each). Text-only completeness is 1.889 (18/20), a marginal gain of 0.111 points, below the proposed 0.50 target. The paired completeness difference is +0.167 across 18 shared questions, with exploratory 95% interval [-0.278, 0.611]. Automatic faithfulness is 0.626 (52/60) versus 0.568 (40/60), with unequal availability. The joint QA target is not met. The results do not establish general method superiority.

The final report (14 pages), final slides (16 slides), 5:34 narrated demo, captions and transcript are in `outputs/final_submission`. The demo uses authentic saved application states with visible replay/synthetic-narration labels. The source/evidence ZIP is `outputs/ThreatWeave_submission_v2.zip`. These local deliverables are ready for the user's submission; no external upload or repository push has been performed. See [the submission status](docs/ThreatWeave_final_submission_status.md) and [the package guide](outputs/final_submission/SUBMISSION_GUIDE.md).

New offline analysis entry points are `analyze_extraction.py` and `analyze_human_reviews.py`. The latter expects both completed rating exports and `docs/ThreatWeave_secondary_method_declaration.json`. The latest analysis is `work/human_scoring_analysis/20261016T174034Z-7c181a33`; earlier preliminary reports are superseded after the reviewer clarified secondary AI assistance. The separate `demo_replay.py` displays preserved development outputs through the original result renderer without constructing live adapters. Forty-three targeted application/scoring/reporting checks passed. Additional live UI flows and independent semantic review remain limitations, not completed checks.

## Historical development checkpoints

The dated records below preserve what was complete or pending at each earlier checkpoint. The current status above takes precedence over their historical next-step instructions.

This repository contains the published Milestone 2 design checkpoint, reviewed benchmark data, and a working development pipeline. The design document covers Sections 1–8 in 10 pages. Full-corpus ingestion, application integration and final model performance evaluation remain unfinished.

As of October 15, the [expanded four-mode development comparison](docs/ThreatWeave_expanded_four_mode_development_comparison.md) is complete: all 12 cases produced non-abstaining answers on their first attempt, with zero execution failures. The questions, model digest and shared generator settings match across modes. An independent offline audit checked all 118 supplied passage occurrences against frozen sources and all 64 claims for valid citation bindings. These are integrity and processing results, not final quality scores. No further demonstration run is needed for this checkpoint.

Source review found unsupported incident claims in two text-only answers whose evidence contained only ATT&CK guidance. Graph-enabled answers received supporting CISA observations, with remaining mitigation-condition omissions, incomplete guidance, repetition and relevance limitations. Node2Vec added no unique path candidates in these three cases; a general quality benefit is not established. Original outputs remain preserved and human verification is pending. The [earlier six-scope comparison](docs/ThreatWeave_four_mode_v2_development_comparison.md) remains historical because its questions and evidence differ.

[Source preparation](docs/ThreatWeave_corpus_pilot_preparation_checkpoint.md) saved 54 windows and selected ten for the pilot. Extraction v2.6 produced 37 candidates with no empty results, failures or repairs. [Source review](docs/ThreatWeave_corpus_extraction_pilot_v2_6_development_review.md) selected 34 for development import and excluded three uncertain/conditional candidates. Source and mitigation imports completed. The [expanded text index](docs/ThreatWeave_expanded_text_index_checkpoint.md) contains 95 verified chunks/vectors across 16 CISA scopes and 58 reference parents; the [expanded graph index](docs/ThreatWeave_expanded_graph_index_checkpoint.md) contains 75 domain nodes, 102 accepted directed facts and 75 verified vectors. All 175 offline tests passed at the implementation checkpoint. Earlier runs remain preserved through [the extraction repair history](docs/ThreatWeave_corpus_extraction_pilot_repair.md).

[The application interface code is prepared](docs/ThreatWeave_application_setup_step.md): all four existing modes, per-session history, exact source inspection, an interactive query graph and saved query records. [Application setup passed](docs/ThreatWeave_application_setup_checkpoint.md): Streamlit is installed, all 108 existing package versions are preserved, and the three offline UI checks passed. [The first live application check passed](docs/ThreatWeave_application_live_checkpoint.md): the operator-generated graph-only Rhysida answer and all 13 source passages were inspected. Its six claims match the earlier CLI result, with practical-guidance omissions recorded. A blank-graph display defect was fixed; seven nodes/six edges, node selection and zoom/reset now work in the browser. [The full-hybrid application check also completed](docs/ThreatWeave_application_full_hybrid_checkpoint.md), matching the earlier CLI answer/prompts with 15 verified source passages. Browser export and pan passed, and the new answer remained in history across a mode switch. Some live UI flows remain unverified; broader corpus processing is the next major implementation stage. Broader corpus processing, completed live application integration, human verification and controlled held-out quality/performance evaluation remain unfinished. Benchmark gold triples and reference answers are evaluation records, not pipeline inputs.

[The additional development batch was processed and reviewed](docs/ThreatWeave_corpus_batch_ingestion_step.md): all 44 remaining prepared windows were attempted. Two validation failures were recovered offline in separate artifacts, preserving the original outputs. Source review selected 53 Supported assertions across 25 windows, held ten for review and rejected five. Human verification remains pending. Source and [direct mitigation imports](docs/ThreatWeave_corpus_batch_mitigation_step.md) completed and their saved plans/receipts passed offline reconstruction. [Accepted scope expansion](docs/ThreatWeave_corpus_batch_scope_checkpoint.md) now includes 41 CISA windows and 96 ATT&CK reference parents. [The matching text index completed](docs/ThreatWeave_corpus_batch_text_index_checkpoint.md): all 215 saved source records match offline reconstruction; the build receipt verifies stored 384-dimensional vectors. Saved retrieval checks still lack CISA evidence for Raccoon Stealer, include the relevant Rhysida T1078 passage and include the ALPHV software-use statement. [The matching graph-vector index also completed](docs/ThreatWeave_corpus_batch_graph_index_checkpoint.md): 117 nodes, 179 directed facts and 117 verified 128-dimensional vectors. Offline asset/provenance checks passed for both indexes. [Restart the application to load the refreshed scope](docs/ThreatWeave_corpus_batch_application_step.md). Broader corpus completion, human verification and controlled final evaluation remain pending.

[The remaining three eligible development reports were extracted](docs/ThreatWeave_corpus_extension_step.md): 33 windows from two Volt Typhoon advisories and Hive produced sixteen candidate windows, sixteen empty results and one duplicate-selection failure. Separate offline recovery preserves the original failure/output and yields 46 reviewed candidate occurrences. [Source review and the completed source import](docs/ThreatWeave_corpus_extension_ingestion_step.md) select 27 Supported assertions across twelve windows, hold nine for review and reject ten; human verification is pending. [The direct mitigation import completed](docs/ThreatWeave_corpus_extension_mitigation_step.md): 48 references for thirteen techniques, with no direct frozen references for T1057 or T1082. Both receipts passed offline reconstruction. [Shared accepted scope](docs/ThreatWeave_corpus_extension_scope_checkpoint.md) contains 53 CISA windows and 139 reference parents. [The 305-chunk text index](docs/ThreatWeave_corpus_extension_text_index_checkpoint.md) and [matching 142-node/245-fact graph index](docs/ThreatWeave_corpus_extension_graph_index_checkpoint.md) are ready; offline source/artifact verification passed for both. Restart the application to load them. Evaluation preparation is the next substantive milestone. Sixteen extension windows have no selectable typed relation patterns under the frozen selector, so coverage remains limited. Held-out reports and original runs are preserved; human verification and final evaluation remain pending.

[The seven held-out source reports and bounded retry were processed](docs/ThreatWeave_evaluation_corpus_ingestion_step.md). All 114 windows were attempted; the connection-failure window recovered on retry and four persistent duplicate-selection failures were separately normalized using the existing first-support policy. Every initial/retry output remains preserved, including 49 empty windows. Source-only review of 196 candidates selects 118 Supported assertions across 48 windows, holds 24 for review and rejects 54. The evaluation-scoped source import completed and its saved payload/receipt passed offline reconstruction. [The direct mitigation import is prepared](docs/ThreatWeave_evaluation_corpus_mitigation_step.md): 109 references covering 29 techniques, with five explicit coverage gaps and 203 source-reference combinations. The live mitigation import completed and its saved payload/receipt passed offline scope reconstruction. [The method freeze](docs/ThreatWeave_evaluation_freeze_checkpoint.md) remains unchanged. Graph-accepted candidates are not the extraction-scoring population: all predictions, errors and coverage gaps remain relevant. Final evaluation indexes, the 240-answer experiment, scoring and human verification remain pending.

[The shared evaluation text index completed](docs/ThreatWeave_evaluation_graph_index_step.md). All 510 saved records match the prepared source snapshot, and its manifest/runtime and fifteen ranked smoke hits passed offline verification. All four conditions will share 101 CISA windows and 190 direct reference parents. The matching graph preview contains 212 domain nodes and 394 directed facts. Existing development assets remain separate. The graph build is prepared in its own namespace with the frozen methods, parameters and explicit scope/text fingerprint bindings; seventeen targeted asset/publication/projection checks passed. The live evaluation graph index subsequently completed; final QA/scoring/human-review stages remain pending.

[The shared evaluation graph index also completed](docs/ThreatWeave_final_evaluation_step.md): 212 live domain nodes, 394 accepted directed facts, 212 verified vectors and 2,120 walks. Offline vector/receipt/source-provenance checks passed, matching the ready 510-chunk text index and common evaluation scope. The frozen batch uses twenty assigned questions, four conditions, three repeats, seed42 ordering, excluded warm-ups and preserved terminal failures. Question-only inputs isolate reference answers from generation; methods/settings and assets are bound in the final plan. All 32 collection/index checks passed.

[The final answer collection completed and passed offline audit](docs/ThreatWeave_final_evaluation_checkpoint.md): all 240 measured outcomes plus four warm-ups are saved. There are 210 valid non-abstaining answers, fifteen graph-only empty-evidence abstentions and fifteen generation-validation failures (nine repeated-citation errors and six repeated-claim errors). These are operational outcomes, not semantic quality scores. The completed cohort will not be regenerated. Evaluator-only inputs preserve 225 available responses and the exact supplied context; fifteen unavailable failures remain in the cohort denominator. Eighty primary and twenty secondary blinded human-review entries have blank ratings. Seven additional offline checks passed. The next operator step installs the separate hash-locked scoring environment; extraction scoring, live automated evaluation, human ratings, paired analysis and reporting remain pending.

[The separate scoring environment is now installed](docs/ThreatWeave_evaluator_probe_step.md): saved checks confirm Windows x64 Python 3.12, consistent dependencies and successful pinned adapter imports. A synthetic local check of all three metrics is prepared with cached embeddings, fixed judge settings, explicit Ollama completion checks and saved diagnostics. Its offline preview and seven targeted simulated tests passed. It contains no final benchmark question and produces no benchmark scores. Live evaluator integration and the remaining scoring/review/analysis stages are pending.

[The live synthetic evaluator probe passed](docs/ThreatWeave_final_scoring_step.md): all three metrics returned finite values across six recorded local judge calls, and saved policy/identity/completion/artifact checks passed offline audit. The resumable final scoring batch is prepared: 675 eligible metric checks on 225 available responses and 45 explicit unavailable slots for the fifteen original failures, preserving all 240 observations. Its offline preview and eight simulated runner checks passed. No final benchmark scores have yet been computed; the next operator command scores the already collected answers. Extraction scoring, human ratings, paired analysis and reporting remain pending.

[Final automatic scoring and its offline analysis completed](docs/ThreatWeave_human_answer_review_step.md): all 720 metric outcomes are preserved, with 639 numeric scores, 36 evaluator output-limit failures and 45 slots unavailable from fifteen original generation failures. All saved metric/input/receipt bindings, judge settings and model identities passed audit; 414 verdict-based metric formulas were independently reproduced without model calls. Available-score summaries and all eighteen paired question comparisons with 10,000-draw exploratory bootstrap intervals are saved, with missing coverage and limitations explicit. Six additional audit/statistical checks passed. Standalone primary (80 entries) and secondary (20 entries) browser forms are prepared with blank human ratings, progress export and method blinding; offline JavaScript state/export checks passed. Human ratings, extraction metrics and final combined reporting remain pending.

## Design and submission files

- [Milestone 2 design document](docs/ThreatWeave_GraphRAG_DesignDoc.pdf)
- [Editable design document](docs/ThreatWeave_Milestone2.md)
- [Submitted project proposal](docs/ThreatWeave_GraphRAG_Proposal.pdf)
- [Proposal alignment](proposal_alignment.md) and [grading rubric checklist](rubric_checklist.md)
- [GitHub repository](https://github.com/sbutler1246/ThreatWeave)

For Milestone 2, submit the design PDF and repository link according to the assignment instructions. The instructor needs access to the private repository to review its files.

## Included code and data

| Files | Purpose |
|---|---|
| [schemas.py](schemas.py), [json_schema/](json_schema/), [interfaces.py](interfaces.py) | Pydantic v2 data models, generated JSON schemas, and module interfaces |
| [extraction/parser.py](extraction/parser.py), [resolve.py](resolve.py) | Validate extraction structure and exact evidence; resolve type-compatible IDs, names, and verified aliases |
| [prompts/](prompts/) | Extraction and answer prompts, including two synthetic extraction examples |
| [graph/](graph/) | Neo4j schema initialization, constraints, indexes, and bounded query templates |
| [api.py](api.py), [openapi.json](openapi.json) | FastAPI contract factory and generated API specification |
| [benchmarks/](benchmarks/) | Verified triples, questions, reference answers, review records, and question assignments |
| [data/](data/), [corpus_selection.md](corpus_selection.md) | Saved CISA HTML/text sources and the frozen Enterprise ATT&CK 17.1 snapshot |
| [evaluation/](evaluation/), [tests/](tests/) | Extraction scoring, benchmark checks, evaluator configuration, and offline tests |
| [config.json](config.json) | Planned model, chunking, retrieval, and evaluation settings |

Chroma is the primary vector store. The optional Neo4j vector-index script is an appendix adaptation. Development retrieval and cited generation are implemented. The Streamlit interface and shared application adapter are coded, installed and checked offline. Live graph-only and full-hybrid answers reproduce their CLI results, and source/graph/export/history interactions have been checked. Additional UI flows, broader corpus processing and final evaluation remain pending.

## Verified benchmark records

Stephen Butler has confirmed and verified the following records; review completion is recorded as October 5, 2026.

| Records | Count | File |
|---|---:|---|
| GT001–GT146: extracted gold relationships | 146 | [gold_triples.json](benchmarks/gold_triples.json) |
| Complete CISA annotation scopes supporting the gold relationships | 39 | [author_review.md](benchmarks/author_review.md) |
| Q001–Q061: questions, reference answers, and supporting paths | 61 | [eval_queries.json](benchmarks/eval_queries.json) |
| RF001–RF039: ATT&CK technique-to-mitigation reference relationships | 39 | [reference_triples.json](benchmarks/reference_triples.json) |

The 146 extraction gold triples cover declared passages from seven advisories. The 39 RF relationships remain separate from extraction gold and describe ATT&CK mitigation recommendations. Stephen Butler manually validated the QA records before requesting a Codex cross-check.

The [split manifest](benchmarks/split_manifest.json) assigns 20 final evaluation questions, 21 development questions, and 20 held-out reserves. The final set includes eight actor/software/technique questions, eight technique/mitigation questions, and four cross-report comparisons. Development and held-out CISA evidence scopes are disjoint; one advisory appears in both groups through different table rows. See the [QA review report](benchmarks/qa_review_report.md) for per-question decisions.

The repository contains 15 candidate CISA advisory snapshots downloaded on October 3, 2026, plus Enterprise ATT&CK 17.1. Source URLs, retrieval dates, and raw/normalized checksums are recorded in the [corpus manifest](benchmarks/corpus_manifest.json). Downloaded pages may contain later updates than their advisory identifiers. Five-report source preparation, bounded extraction timing and development graph transactions are recorded above. Final corpus selection, broader graph-write/index/resource measurements and overlap assessment remain pending. Some annotation scopes also require alignment to finalized token-aware chunks before extraction evaluation.

## Run the offline checks

### Development setup and run history

The following walkthrough records the staged development work, including statements of what was pending at each checkpoint. The current status and next matching baseline check are recorded above and in the latest checkpoint.

The live single-row pilot now supports three-hop graph-only QA through imported ATT&CK mitigation references. The next development extraction batch is saved in [batch_extract.py](batch_extract.py), with five source passages across LockBit, BianLian, and ALPHV Blackcat. It produces candidates for semantic review; it does not write to Neo4j or run final evaluation. See [the batch instructions](docs/ThreatWeave_development_batch_step.md) and [the three-hop pilot checkpoint](docs/ThreatWeave_pilot_checkpoint.md).

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\batch_extract.py"
```

Keep Ollama running. Saved candidates go into `work/development_batch`, and the review document is written directly into `docs`. Existing evaluation assignments remain unchanged.

The batch ingestion and mitigation steps have now been exercised locally. [Multi-source graph QA](docs/ThreatWeave_multi_source_graph_qa_step.md) supports the six imported development scopes and up to three-hop paths:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\graph_qa.py" --demo
```

Keep Neo4j and Ollama running. This development demonstration uses three source-based questions across the imported reports. It saves generated-answer logs in `work/graph_qa` and a review document in `docs`. Text/hybrid retrieval and final benchmark evaluation remain pending.

The October 13 multi-source demonstration produced three answers with zero execution failures. AI-assisted source inspection is recorded in [the development checkpoint](docs/ThreatWeave_graph_qa_development_checkpoint.md); these are development observations, not final evaluation scores.

Prepare text-search dependencies and the configured MiniLM model with:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_text_search.py"
```

This installs the direct pins in [requirements-text.txt](requirements-text.txt) using CPU PyTorch, downloads the frozen MiniLM revision, and checks a synthetic local Chroma lookup. See [the setup instructions](docs/ThreatWeave_text_search_setup_step.md). The local setup passed; this step does not build the corpus index. The evaluator still uses its separate environment.

The local MiniLM/Chroma setup has now passed. Build the development text index with:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_text.py"
```

See [the text-index step](docs/ThreatWeave_text_index_step.md). This indexes the same six CISA source scopes and 13 ATT&CK references available to the graph demonstration. It preserves child offsets and inherited context, checks stored vectors, and records three ranked retrieval smoke queries. It uses cached model files without calling Neo4j or Ollama. Text-only generated answers and hybrid search remain pending.

The development text index has now passed its local checks; [the retrieval checkpoint](docs/ThreatWeave_text_index_checkpoint.md) records its ranked matches. Run text-only cited QA with Ollama:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\text_qa.py" --demo
```

See [the text QA step](docs/ThreatWeave_text_qa_step.md). It uses five text neighbors without graph expansion and shares the cited generator with graph QA. A `--preview` run verifies the local index and source packing without calling Ollama. Logs go to `work/text_qa` and generated review documents to `docs`. Hybrid retrieval and final evaluation remain pending.

The first text-only run completed three cases; [its semantic review](docs/ThreatWeave_text_qa_development_review.md) records an incomplete AnyDesk answer and two supported prose answers. Next, run the explicit combined mode without Node2Vec:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\combined_qa.py" --demo
```

Keep Neo4j and Ollama running. See [the combined QA step](docs/ThreatWeave_combined_qa_step.md). This implements `hybrid_no_node2vec` using source-parent rank fusion, exact-span deduplication, global citation remapping and whole supported paths. Full hybrid still requires its separate graph embeddings. A `--preview` run uses offline graph source fixtures and the live local text index; it does not call either service. Results go to `work/combined_qa` and review documents to `docs`.

The combined development run completed three cases; [its review](docs/ThreatWeave_combined_qa_development_review.md) records supported AnyDesk mitigation coverage and a Rclone wording issue. Prepare the graph-embedding dependencies next:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\setup_node2vec.py"
```

See [the Node2Vec setup step](docs/ThreatWeave_node2vec_setup_step.md). It installs development pins, fits a synthetic graph, checks a separate 128-dimensional vector-store probe and revalidates the existing text index. The real Neo4j projection and full-hybrid graph index remain pending.

The Node2Vec setup passed; [its checkpoint](docs/ThreatWeave_node2vec_setup_checkpoint.md) records the synthetic checks. Fit the actual development domain graph with Neo4j running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_graph.py"
```

See [the live graph-index step](docs/ThreatWeave_graph_index_step.md). It reads accepted source-verified facts, excludes provenance hubs, fits an undirected Node2Vec projection and publishes a separate versioned graph-vector collection. It records graph/vector fingerprints and verifies the graph again before publishing. A `--preview` run checks source-derived fixtures only. Full-hybrid retrieval integration remains pending.

The live development graph index now passed its checks; [the checkpoint](docs/ThreatWeave_graph_index_checkpoint.md) records 22 nodes and 23 accepted facts. Run full hybrid QA with both services running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\hybrid_qa.py" --demo
```

See [the full-hybrid QA step](docs/ThreatWeave_full_hybrid_qa_step.md). It validates the separate graph-vector index, checks the live projection for freshness, retrieves up to five Node2Vec neighbors per seed and admits only source-supported directed paths. A `--preview` run checks the saved projection, real local indexes and packing without service calls. Results go to `work/hybrid_qa`, with review documents in `docs`. The prior `combined_qa.py` remains the no-Node2Vec condition. Full-corpus ingestion and final four-mode evaluation remain pending.

The first live full-hybrid demonstration completed two cases; AnyDesk generation reached the 700-token limit twice. [The output-budget repair](docs/ThreatWeave_hybrid_output_budget_fix.md) records the failure and shared generator v2, which uses compact non-repeating claims under the unchanged budget. Retry only the failed case:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\hybrid_qa.py" --retry-run "S:\ThreatWeave\work\hybrid_qa\20261014T055940Z-bba7b219"
```

Retry runs preserve old results and link their new logs to the prior run. All current development modes share generator v2; prior v1 runs are historical development observations, not paired final evaluation results.

### Check supporting components

From the repository root, use Python 3.12 with Pydantic v2. These checks require no running database, model server, or downloaded model weights.

```text
python -m pip install "pydantic>=2,<3"
python -m unittest discover -s tests -v
python evaluation/check_benchmarks.py
```

On October 5, 2026, all 16 offline tests passed, and the benchmark structural checks passed. Tests cover schema/evidence validation, identity conflicts, graph path constraints, extraction scoring, and the evaluator version gate. The benchmark checks validate record structure, evidence spans, supporting paths, question assignments, and category counts. These results do not measure model accuracy or answer quality. See [validation_report.json](validation_report.json).

The extraction parser accepts a chunk JSON file and a corresponding extraction-output JSON file. Supply those actual input files when using its command-line interface; the repository does not include ready-made `chunk.json` or `extraction_output.json` inputs.

## Service and evaluator setup

The root [requirements.txt](requirements.txt) is an application dependency draft. The separately locked evaluator targets Windows x86-64 with Python 3.12 and pins RAGAS 0.2.15, langchain-ollama 0.2.3, langchain-huggingface 0.1.2, and sentence-transformers 3.4.1. Its transitive dependencies and distribution hashes are recorded in [evaluation/requirements.lock.txt](evaluation/requirements.lock.txt).

Follow [evaluation/DEPENDENCIES.md](evaluation/DEPENDENCIES.md) to create a separate evaluator environment. Dependency resolution and inspection of the RAGAS wheel's API exports passed. Full evaluator installation, model downloads, and live evaluation remain pending. `build_local_evaluators()` defines local judge/embedding adapters, and `evaluate_logged_answers()` evaluates logged pipeline outputs; neither has been validated with live model services.

Neo4j initialization requires the Neo4j Python driver and a running database. Set `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD`, and optionally `NEO4J_DATABASE`, then run `python graph/init.py`. This script applies schema statements; it does not ingest the advisory corpus or benchmark records. Live database initialization has not been tested.

The default FastAPI app reports `not_configured` at `/health` and returns HTTP 503 at `/query` until a real `QueryEngine` is injected. Serving the API requires FastAPI/Uvicorn. End-to-end API and service integration remain pending.

## Planned implementation and evaluation

1. Complete the corpus pilot and align extraction/retrieval chunks with the verified annotation scopes.
2. Freeze the application dependencies and record the installed Ollama model digest. The evaluator lock, ATT&CK release, and shared MiniLM revision are already recorded.
3. Implement and integrate ingestion, Neo4j, Chroma, Ollama, and Streamlit, including bounded retrieval and cited answers.
4. Evaluate the four designed conditions: `text_only`, `graph_only`, `hybrid`, and `hybrid_no_node2vec`, with the same questions, source access, generator settings, and context budgets.
5. Measure extraction precision/recall/F1 before ATT&CK fusion; evaluate generated answers with RAGAS and human factuality, completeness, and coherence ratings on a 1–5 scale.

Only supported extracted predictions count toward extraction true positives; fused RF relationships are excluded. Reference answers are evaluation labels and must not enter retrieval or generation. Final evaluation questions must not be used for tuning.

The checkpoint establishes reviewed evaluation data and tested supporting components. Live pipeline execution, benchmark scores, and human ratings of generated answers have not been completed.
