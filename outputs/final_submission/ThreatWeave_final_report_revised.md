# ThreatWeave
## Evidence-grounded cybersecurity question answering with GraphRAG
Stephen Butler · CS 6338 · October 16, 2026

**Final project report. Revised documentation; see Appendix B.**

### Abstract
ThreatWeave combines source passages from CISA advisories with a provenance-aware Neo4j knowledge graph and a frozen Enterprise ATT&CK 17.1 reference. A local Llama 3.1 8B model answers questions from text retrieval, graph paths, or a combination of both. MiniLM supplies text embeddings, while Node2Vec supplies graph-neighbor candidates. The interface exposes citations and the directed paths supplied to generation so an analyst can inspect the evidence behind an answer.

The frozen experiment contains 20 questions, four retrieval conditions and three repeats, giving 240 measured outcomes after four excluded warm-ups. Collection produced 210 valid non-abstaining answers, 15 explicit abstentions and 15 generation-validation failures. Automatic evaluation preserved 639 numeric metric values, 36 evaluator failures and 45 unavailable slots. These counts describe execution and availability, not semantic accuracy.

Source-only extraction achieved precision 0.455, recall 0.067 and F1 0.117 against 149 source-scoped assertions derived from the frozen gold inventory. This misses the proposed F1 target of 0.80. Inspection also identified possible annotation-coverage or granularity gaps among five exact-reference nonmatches, limiting interpretation of false-positive counts as semantic falsehood. No labels or model outputs were changed to improve the result.

### QA finding
Full hybrid's available human completeness mean differs from text only by 0.111/5. The available marginal point estimates do not satisfy every prespecified QA threshold. Coverage-aware paired comparisons and delayed consistency results appear in Section 7. Unequal score availability, limited AI assistance for review questions and the MODE/evidence-format confound limit generalization.

| Frozen evaluation asset | Size |
|---|---:|
| CISA source windows in the shared evaluation scope | 101 |
| Direct ATT&CK reference parents | 190 |
| Text retrieval chunks / dimensions | 510 / 384 |
| Domain graph nodes / accepted directed facts | 212 / 394 |
| Graph vectors / dimensions | 212 / 128 |

Sources: frozen evaluation protocol [1], index and collection receipts [2–3], extraction analysis [4].

<PAGE>
# 1. Problem and source boundaries
Cybersecurity questions often require more than a similar paragraph. An analyst may need to establish that a report attributes a tool to a particular actor, identify the technique associated with that reported use, and then consult a separate mitigation reference. A correct technique name alone does not establish every link in that chain.

ThreatWeave keeps two kinds of evidence distinct. CISA advisory passages describe reported observations within an identified source context. ATT&CK relationships provide reference associations, including mitigation guidance. A mitigation relationship does not prove that a control worked in the incident. Likewise, a mapping for one reported use of a tool does not characterize every use of that software.

### Corpus and benchmark
The source manifest contains 15 candidate CISA advisory snapshots downloaded October 3, 2026, plus the frozen Enterprise ATT&CK 17.1 snapshot. Advisory identifiers are not reliable snapshot dates: downloaded pages can include later revisions. The manifest records URLs, retrieval metadata and raw/normalized checksums. All evidence spans refer to the frozen normalized text rather than a changing public page.

The author verified 146 extraction gold records across 39 declared complete passages from seven advisories and 61 question/reference-answer records. The question split reserves 20 final questions, 21 development questions and 20 additional held-out reserves. The final set includes eight actor/software/technique questions, eight technique/mitigation questions and four cross-report comparisons. Benchmark labels enter evaluation only; they do not enter generation or retrieval stores. [1,5]

### Separation and overlap
Development and final evaluation evidence assignments are disjoint at their declared annotation scopes. AA23-165A appears in both groups through different table rows. The final retrieval corpus includes accepted development evidence as well as separately processed evaluation sources. This is scope separation with disclosed report overlap, rather than a claim that every evaluation advisory was wholly unseen.

Seven reports were reserved from broader development expansion before held-out source processing. The frozen protocol binds source checksums, extraction and retrieval code, model identity, chunking, validators and existing development receipts. The final text and graph assets use their own matching fingerprints and namespaces. No held-out result prompted a new generator run or parameter change. [1–3]

### Claims that require qualification
Historic and conditional language remains part of the source meaning. For example, a historic Royal/Chisel observation should not become an assertion of current use. Parent technique T1003 and sub-technique T1003.001 have different specificity. A C2 paragraph mapping ngrok to T1572 should not inherit a different technique from a neighboring exfiltration paragraph merely because the tool name is the same.

<PAGE>
# 2. Implemented architecture
ThreatWeave separates source preparation and indexing from question answering. Every generated answer retains the evidence pack, request, model identity and run metadata. Neo4j stores the accepted directed assertions; separate Chroma collections store text and graph vectors. Streamlit provides the inspection interface.

| Stage | Implemented behavior |
|---|---|
| Source preparation | Freeze text with document offsets and table/heading context |
| Extraction | Select bounded assertions, validate structure and exact supporting text |
| Resolution and review | Resolve compatible IDs/names/aliases and retain review decisions |
| Graph import | Preserve source assertions and separately attributed mitigation references |
| Indexing | Build separate 384-dimensional text and 128-dimensional graph vectors |
| Retrieval | Select text, bounded directed paths or fused evidence |
| Generation | Produce cited claims and retain terminal validation outcomes |
| Inspection | Expose source passages, query graph, metadata and export |

### Domain and provenance
The seven domain classes are ThreatGroup, Software, Technique, Tactic, Mitigation, Campaign and Document. Chunk and Assertion records support provenance. Allowed directed facts include ThreatGroup USES Software, ThreatGroup or Software USES_TECHNIQUE Technique, Technique PART_OF_TACTIC Tactic, Technique MITIGATED_BY Mitigation and ThreatGroup ASSOCIATED_WITH Campaign.

A document mention does not establish a factual relationship. Supporting assertions retain the document, selected passage, evidence text, source offsets, origin, validation status and version information. Several assertions can support a canonical edge without discarding report-specific provenance. Extraction-origin and reference-fusion facts remain distinguishable. [6]

### Local model and storage choices
The generator is local Ollama Llama 3.1 8B. The shared frozen model digest begins 46e0c10c039e; the complete digest and exact prompts remain in receipts. The text encoder is sentence-transformers/all-MiniLM-L6-v2 at frozen revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41. Node2Vec learns graph representations; the project performs no additional language-model training.

The final assets contain 510 text chunks, 212 domain nodes and 394 accepted directed facts. The graph vector build records 2,120 walks, normalized stored vectors and per-node lookup checks. Provenance/fingerprint checks bind these assets to the same evaluation scope. These integrity checks do not prove that every accepted assertion is semantically correct. [2]

<PAGE>
# 3. Extraction and entity resolution
The extraction pipeline uses token-aware windows targeting approximately 500 Llama tokens, a 400–600 token range and about 60-token overlap. Separate MiniLM retrieval children use a 240-wordpiece ceiling with 40-wordpiece overlap so the text encoder does not silently truncate the intended source window. Parent IDs and normalized offsets connect the two representations. [1,6]

The frozen extraction method selects a bounded inventory rather than exhaustive named-entity recognition. It limits selected relationships per window, requires compatible endpoint types and exact source support, and retains inherited heading or caption context. Invalid results receive the allowed repair attempt, after which persistent validation failures remain failures. Source review may select Supported assertions for import, but extraction evaluation must retain predictions before semantic acceptance/rejection and ATT&CK fusion.

### Scoring population and identity alignment
The analysis reconstructs 114 preserved source windows from the seven evaluation advisories. It accounts for 61 candidate windows, 49 empty results and four persistent duplicate-validation failures. All 39 gold passages lie fully within the union of extraction windows. Complete character coverage does not imply complete extraction.

The 146 gold records contain three existing additional-support passages. Expanding those passages yields 149 distinct source-scoped assertions. Of 196 normalized candidate occurrences before semantic filtering, 23 occur within a complete annotation scope, representing 22 unique scoped predictions. The remaining 173 occurrences lie outside the complete scopes and remain unscored; incomplete annotations do not justify treating them as false.

Endpoint alignment for scoring uses exact type-compatible benchmark/source names, explicit IDs and existing frozen aliases. Local entities remain restricted to their own report. The analysis retains original production IDs and every projection decision. It does not introduce fuzzy aliases, remove qualifications, change production resolution, or transfer a technique mapping between sources. Duplicate relations collapse within one scope only. [4]

### Failure preservation
The strict analysis counts only schema-valid outputs as predictions while retaining every gold assertion in the recall denominator. A sensitivity analysis includes the already documented deterministic first-support normalization of duplicate selections. Both preserve original attempts and validation errors. Neither performs new extraction or chooses the best retry after seeing scores.

A true positive requires an exact scoped triple and valid literal support. Thus this assessment measures agreement with the frozen annotated inventory at its stated granularity. It is not a corpus-wide estimate of extraction precision, nor a measurement of the reviewed/fused graph alone.

<PAGE>
# 4. Four retrieval conditions
All conditions use the common accepted source scope, the frozen generator and the same final questions. They differ in retrieval and evidence representation. The text branch has access to both CISA evidence and relevant attributed ATT&CK reference text, avoiding an artificial baseline that lacks mitigation knowledge.

| Condition | Evidence selection |
|---|---|
| Text only | Normalized MiniLM cosine retrieval of source chunks without graph expansion |
| Graph only | Entity seeding and accepted directed paths, with insufficient-evidence abstention if retrieval is empty |
| Hybrid without Node2Vec | Text plus structural graph paths, fused without graph-vector neighbor expansion |
| Full hybrid | Text plus structural graph paths and Node2Vec neighbor candidates, followed by the same evidence-selection policy |

### Directed paths and fusion
Graph retrieval permits up to three hops, enabling an actor/software/technique/mitigation path. Limits include five seeds, five neighbors per seed, 30 candidate paths, five text candidates and six final paths. Full hybrid uses Node2Vec neighbors to propose expansion candidates, then requires accepted directed source-supported paths. Graph-vector similarity itself never establishes an incident fact.

Reciprocal rank fusion uses k=60 and groups evidence by source document and parent extraction chunk. Whole path/text-context groups preserve the selected support rather than treating a similar node as evidence. Logs retain candidate ranks, selected paths, skipped groups, branch coverage and the exact context supplied to generation. [6]

### Node2Vec settings
The graph projection is simple, undirected and unweighted for fitting, with Document/Chunk/Assertion hubs excluded. Directed assertions remain authoritative for retrieval. Fixed settings use 128 dimensions, walk length 20, ten walks per node, context window ten, p=q=1, five epochs, five negative samples, seed 42 and one worker. Separate graph and text vectors avoid comparing unrelated embedding spaces.

### Important deviations and confounds
The implemented common evidence budget is a conservative **3,000 UTF-8 byte cap**, despite the configuration field and design discussing tokens. This report states the actual policy and does not claim a measured 3,000-token context. The generator also receives a MODE field and different evidence formats. Consequently, a difference between conditions cannot be attributed solely to retrieval or to Node2Vec. These limitations were documented before final QA generation. [1]

<PAGE>
# 5. Frozen experiment and evaluation method
The final assignment contains 20 questions, four conditions and three measured repeats. Seed-42 ordering and one excluded warm-up per mode produce 240 measured outcomes plus four warm-ups. The frozen plan binds method files, model identity, parameters and matching index fingerprints. Reference answers enter scoring after collection and never enter generation.

Collection preserved 210 valid non-abstaining answers, 15 graph-only abstentions with empty evidence, and 15 generation-validation failures. The failed cases exhausted the two allowed attempts: nine repeated-citation-ID errors and six repeated-claim errors. Their final transports returned completed HTTP 200 responses. They remain validation failures rather than successful answers or output-limit failures. Repairs are logged and counted separately from question/mode/repeat observations. [3]

### Automated scoring
The separate hash-locked evaluation environment uses RAGAS 0.2.15. Faithfulness, response relevancy and context recall use the unchanged saved answers and complete supplied generator context. Available inputs include 225 validated responses, including abstentions; the 15 generation failures have no valid response and remain unavailable. A local synthetic integration probe preceded final scoring.

| Automatic metric-slot outcome | Count | Share of all 720 slots |
|---|---:|---:|
| Numeric score | 639 | 88.75% |
| Judge output-limit failure | 36 | 5.00% |
| Unavailable after generation failure | 45 | 6.25% |

The automated judge uses the same model family as generation, so shared biases are possible. Available-score means must accompany coverage counts. Missing metrics remain null with reasons; the analysis does not impute them or silently replace failed answers. Saved verdicts support independent formula reconstruction without new model calls. [7]

### Human ratings and paired analysis
Primary review scores the prespecified first repeat for every question/condition: 80 entries. The rubric uses factuality, completeness and coherence on a 1–5 scale, or N/A with a reason when not ratable. Mode names and execution order are hidden, but graph-shaped evidence makes blinding partial. The author entered and confirmed the primary ratings. There was limited AI assistance for review questions. This is not an independent human panel.

The planned secondary set contains five prespecified questions across all four conditions, giving 20 entries. The author selected a delayed rescore. Agreement measures describe same-reviewer consistency and must not be called inter-rater reliability. Primary ratings remain separate. Paired comparisons average within question and use 10,000 question-cluster bootstrap samples with seed 42. Intervals are exploratory with only 20 questions and missing outcomes.

<PAGE>
# 6. Source-only extraction results
The strict source-scoped result falls below the proposal target of F1 ≥0.80. Low recall is the dominant limitation: only ten of the 149 annotated scoped assertions match a valid selected prediction. The four-relationship/window selector and missed links make the imported graph unsuitable as evidence of exhaustive extraction. [4]

| Population | TP | FP* | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| Strict validated pipeline | 10 | 12 | 139 | 0.4545 | 0.0671 | 0.1170 |
| Duplicate-normalized sensitivity | 10 | 12 | 139 | 0.4545 | 0.0671 | 0.1170 |

*FP denotes exact nonagreement with the frozen scoped inventory. It does not establish semantic falsehood for every nonmatch.

| Advisory | Complete scopes | TP | FP | FN |
|---|---:|---:|---:|---:|
| AA23-061A | 1 | 1 | 0 | 10 |
| AA23-075A | 1 | 1 | 1 | 6 |
| AA23-165A | 29 | 0 | 0 | 58 |
| AA23-352A | 1 | 0 | 1 | 12 |
| AA24-109A | 3 | 3 | 5 | 18 |
| AA24-131A | 1 | 0 | 0 | 10 |
| AA25-071A | 3 | 5 | 5 | 25 |

### Annotation and granularity limitations
Inspection of all 23 eligible prediction occurrences found five potential inventory gaps: source-cited T1016 mappings for SoftPerfect, Advanced IP Scanner and NetScan, a direct Akira/T1090 assertion, and a direct Medusa/T1219 assertion. The frozen gold retains some constituent or two-hop facts without those direct assertions. These candidates remain exact-reference nonmatches. No gold correction, favorable exclusion or replacement model output enters the reported scores.

Other nonmatches expose extraction/linking errors, including assigning a nearby scanner technique to net, attaching an RDP technique to PsExec, inferring a tactic from neighboring activity IDs, and confusing software with the actor using it. These patterns support preserving sentence/table-row boundaries and explicit endpoint typing in future work. They do not justify retuning this completed cohort.

Precision, recall and F1 are micro values over the scoped counts. Outside-scope candidates remain retained but unscored. Undefined per-advisory denominators remain undefined. A legacy scorer that collapses identical triples across scopes is a diagnostic only; the primary result retains source context.

<PAGE>
# 7. Human QA results
The author completed all 80 repeat-one entries, then completed 20 entries as a declared delayed rescore. Primary ratings remain the result population; secondary scores do not replace or average into them. Each human score uses a 1–5 scale. The counts below show numeric observations out of 20 assigned questions. Failed responses remain N/A with reasons. [9]

| Condition | Factuality (n/20) | Completeness (n/20) | Coherence (n/20) |
|---|---|---|---|
| Text only | 2.944 (18/20) | 1.889 (18/20) | 3.833 (18/20) |
| Graph only | 3.500 (20/20) | 1.900 (20/20) | 4.000 (20/20) |
| No Node2Vec | 3.529 (17/20) | 2.000 (17/20) | 3.882 (17/20) |
| Full hybrid | 3.350 (20/20) | 2.000 (20/20) | 3.900 (20/20) |

### Paired completeness comparisons
Each row compares the same question in both conditions using numeric repeat-one ratings. The effect is condition minus text only. Exploratory percentile intervals resample questions 10,000 times with seed 42. N/A exclusions are pairwise, so paired sample sizes and marginal means can differ.

| Condition minus text | Paired n/20 | Completeness difference | Exploratory 95% CI |
|---|---|---|---|
| Graph only | 18 | 0.111 | [-0.278, 0.500] |
| No Node2Vec | 16 | 0.312 | [-0.062, 0.750] |
| Full hybrid | 18 | 0.167 | [-0.278, 0.611] |

The interval estimates describe this small source-specific benchmark. They do not identify a retrieval-only effect because the MODE prompt field and evidence formats also differ. The full set of 18 human comparisons, included/excluded question IDs and rating inputs is preserved in the human analysis artifact. [9]

### Review boundary
The author entered and confirmed primary ratings. There was limited AI assistance for review questions. Graph-shaped evidence makes method blinding partial. The secondary review uses the same author. Assistance in the project does not constitute independent human replication. The original progress export is preserved alongside the corrected P069 failed-response N/A transcription.

<PAGE>
# 7.1 Automatic QA results
Automatic evaluation is supplementary and uses the preserved generator evidence rather than an improved context. The judge can share generator biases. Parenthesized counts show numeric scores out of 60 measured outcomes per condition. Available means do not silently convert missing outcomes to zero or perfect scores. [7]

| Condition | Faithfulness (n/60) | Relevancy (n/60) | Context recall (n/60) |
|---|---|---|---|
| Text only | 0.568 (40/60) | 0.555 (54/60) | 0.659 (54/60) |
| Graph only | 0.503 (53/60) | 0.335 (60/60) | 0.610 (57/60) |
| No Node2Vec | 0.598 (47/60) | 0.493 (53/60) | 0.593 (53/60) |
| Full hybrid | 0.626 (52/60) | 0.486 (58/60) | 0.710 (58/60) |

### Outcome coverage by metric
The 720 metric slots include 639 numeric scores, 36 judge output-limit failures and 45 slots without a valid generated answer. Judge failures and answer failures remain separate.

| Condition | Metric | Numeric | Judge fail | Answer N/A | Undefined |
|---|---|---|---|---|---|
| Text only | Faithfulness | 40 | 14 | 6 | 0 |
| Text only | Relevancy | 54 | 0 | 6 | 0 |
| Text only | Recall | 54 | 0 | 6 | 0 |
| Graph only | Faithfulness | 53 | 7 | 0 | 0 |
| Graph only | Relevancy | 60 | 0 | 0 | 0 |
| Graph only | Recall | 57 | 3 | 0 | 0 |
| No Node2Vec | Faithfulness | 47 | 6 | 7 | 0 |
| No Node2Vec | Relevancy | 53 | 0 | 7 | 0 |
| No Node2Vec | Recall | 53 | 0 | 7 | 0 |
| Full hybrid | Faithfulness | 52 | 6 | 2 | 0 |
| Full hybrid | Relevancy | 58 | 0 | 2 | 0 |
| Full hybrid | Recall | 58 | 0 | 2 | 0 |

Relevancy uses the saved RAGAS answer_relevancy adapter. Context recall checks reference facts against supplied context. Paired automatic comparisons require three numeric repeats in both conditions and average them within question, giving a smaller eligible population. [7]

<PAGE>
# 7.2 Proposed targets and paired effects
The available marginal point estimates do not satisfy every prespecified QA threshold. The completeness difference is 0.111 points on the five-point scale, the human factuality difference is 0.406, and the automatic faithfulness difference is 0.057. These are full-hybrid minus text-only available marginal means, with the unequal coverage shown above.

| Prespecified requirement | Available-mean difference |
|---|---|
| Human completeness gain at least 0.5 | 0.111 |
| No lower human factuality mean | 0.406 |
| No lower automatic faithfulness mean | 0.057 |

### Paired full-hybrid effects
Paired question comparisons use only shared eligible observations and weight questions equally. Human comparisons use the first repeat; automatic faithfulness requires every repeat in both conditions. The scales differ: human ratings are 1–5 and automatic faithfulness is 0–1.

| Hybrid minus text | Paired n/20 | Mean difference | Exploratory 95% CI |
|---|---|---|---|
| Human factuality | 18 | 0.444 | [-0.056, 0.944] |
| Human completeness | 18 | 0.167 | [-0.278, 0.611] |
| Human coherence | 18 | 0.056 | [-0.000, 0.167] |
| Auto faithfulness | 9 | 0.124 | [0.011, 0.240] |

The intervals are exploratory and unadjusted for multiple comparisons. A point target or positive available mean does not establish general method superiority. Missingness, partial blinding, the small benchmark and the mode/evidence-format confound constrain interpretation. Other automatic and human paired effects remain in the saved analysis tables. [7,9]

### Extraction target and error themes
The strict extraction F1 of 0.117 does not meet the proposed 0.80 target. Coverage and identity-linking weaknesses limit the graph before retrieval starts. Primary review also required source-specific actor/software/technique continuity, parent/sub-technique specificity and exclusion of unrelated mitigation content. Citations to a real passage can still fail to support the particular generated claim. No result led to retuning or regenerating this cohort.

<PAGE>
# 7.3 Delayed consistency and case timing
The secondary set contains 20 entries from five prespecified question clusters across four conditions. The same author declared a delayed rescore. Numeric pairs exclude N/A in either review and do not alter primary scores. MAE is mean absolute score difference. Linear weighted kappa is descriptive, with undefined denominators retained. [9]

| Dimension | Numeric pairs | Exact | Within 1 | MAE | Weighted κ |
|---|---|---|---|---|---|
| Factuality | 19 | 21.1% | 100.0% | 0.789 | 0.275 |
| Completeness | 19 | 78.9% | 100.0% | 0.211 | 0.823 |
| Coherence | 19 | 36.8% | 89.5% | 0.737 | 0.153 |

Review dates are 2026-10-16 for primary and 2026-10-16 for secondary. Day-level dates do not independently verify elapsed delay. Same-person agreement measures consistency rather than independent inter-rater reliability. There was limited AI assistance for review questions. The secondary review was performed by the same author. Factuality fell by 0.789 points on average, completeness by 0.211 and coherence by 0.737 across the 19 numeric pairs. This directional shift limits claims of stable scoring.

### Warm-run case durations
One warm-up per condition is excluded. The measured population contains 60 outcomes per condition, including abstentions and failed repairs. p50/p95 use linear interpolation in the sorted durations, at positions (n−1)×0.50 and (n−1)×0.95. Different statuses perform different amounts of work, so these are not equal-work successful-answer latency comparisons. [3]

| Condition | Valid | Abstain | Failed | p50 s | p95 s |
|---|---|---|---|---|---|
| Text only | 54 | 0 | 6 | 3.151 | 8.788 |
| Graph only | 45 | 15 | 0 | 3.576 | 5.905 |
| No Node2Vec | 53 | 0 | 7 | 3.084 | 8.746 |
| Full hybrid | 58 | 0 | 2 | 3.657 | 12.574 |

These durations are recorded case timings, not separate database/model-service timings. CPU/RSS sampling was unavailable and service/GPU usage was not measured. The saved development demonstrations have their own earlier timestamps and durations and are not pooled with this final benchmark.

<PAGE>
# 8. Interface, reproducibility and limitations
### Demonstration
The Streamlit interface displays cited answers, exact source passages, an interactive directed query graph, per-session history and structured run export. Earlier live graph-only and full-hybrid Rhysida runs reproduced their saved CLI evidence and answers. Their source expansion, graph selection, zoom/reset, pan, export and history across a mode switch were checked. Additional live text-only/ablation and multi-answer navigation flows remain unverified.

The submission video uses a visibly labelled saved-run replay through the original result renderer. It shows real preserved October 15 application outputs and makes no new database or model call. It is a narrated walkthrough of captured application states, not proof of current live generation latency. Original notices such as 'Human source review pending' describe that development checkpoint. Graph inspection can add display-position fields to the JSON export; answer and evidence payloads remain unchanged. [8]

### Reproduction and evidence trail
The repository retains source checksums, frozen split and protocol, model/prompt identities, separate development/evaluation index receipts, original generation attempts and terminal outcomes. Evaluation uses a separate hash-locked environment. The new extraction and human-analysis entry points reconstruct saved records offline and do not regenerate answers. The guarded human-analysis runner validates completion of both rating exports before opening the condition key.

The targeted final checks passed 43 tests covering the application adapter/interface, extraction scoring, human-review guards, automatic-score analysis and reporting comparisons. UI tests use simulated adapters; they are not additional live-service checks. Extraction artifacts retain input hashes, protocol, expanded gold, scope alignment, predictions, annotation audit and window accounting.

### Limits and next work
The 20-question benchmark is small, source-specific and partially blind. There was limited AI assistance for review questions. The secondary review uses the same author. Source snapshots can contain later advisory revisions, scope-level development overlap exists, and the gold inventory has possible completeness/granularity gaps. Missing automatic metrics and output-validation failures may create availability bias. Unsupported-claim rates were not separately annotated at claim level and cannot be inferred from ordinal answer ratings.

Node2Vec uses accepted graph structure and cannot recover an unsupported incident fact. Source acceptance itself received AI-assisted inspection and is not an independent semantic guarantee. The implemented byte cap and mode/evidence-format differences constrain interpretation. CPU/RSS sampling was unavailable, and Neo4j/Ollama/GPU resource usage was not measured. No resource or service timing values are fabricated.

Future work should audit annotation coverage, evaluate more exhaustive extraction and stronger row/sentence binding on a new development split, and isolate retrieval from prompt-format effects with independent review. Software disambiguation and the later HTTP API integration are discussed in Appendix B. Future method changes require a new experiment, preserving this cohort as collected.

<PAGE>
# References and artifact map
The following repository records supply the report's measurements and implementation claims. Public source URLs and snapshot checksums remain in the corpus manifest. Readers should use the frozen snapshot for reproducible offsets and the original advisory for attribution.

| Ref. | Repository record |
|---|---|
| [1] | docs/ThreatWeave_evaluation_freeze_checkpoint.md; work/evaluation_corpus_chunks/20261016T040604Z-bccf59fb/summary.json |
| [2] | docs/ThreatWeave_evaluation_graph_index_step.md; docs/ThreatWeave_final_evaluation_step.md; work/evaluation_text_index_runs/20261016T043755Z-ddd54a27 |
| [3] | work/final_evaluation_runs/20261016T050129Z-f6328cdf; work/final_evaluation_review_checks/20261016T052517Z-4778a10b |
| [4] | work/extraction_scoring_analysis/20261016T171118Z-dc75fabd; docs/ThreatWeave_extraction_results_20261016T171118Z-dc75fabd.md |
| [5] | benchmarks/corpus_manifest.json; benchmarks/gold_triples.json; benchmarks/eval_queries.json; benchmarks/split_manifest.json; benchmarks/author_review.md |
| [6] | schemas.py; extraction/; resolve.py; graph/; retrieval/; config.json; prompts/; streamlit_app.py; application_engine.py; application_view.py |
| [7] | work/final_scoring_analysis/20261016T075220Z-1e84d02c; evaluation/requirements.lock.txt; evaluation/score_analysis.py |
| [8] | work/application_qa/20261015T074134Z-a878f56c; work/application_qa/20261015T165813Z-950f9f1f; docs/ThreatWeave_application_full_hybrid_checkpoint.md; demo_replay.py |
| [9] | work/human_scoring_analysis/20261016T174034Z-7c181a33; work/final_completion/submission_results.json |

### Implementation dependencies
Neo4j provides the graph database. Chroma provides separate vector stores. Ollama serves Llama 3.1 8B locally. Sentence Transformers supplies all-MiniLM-L6-v2. Node2Vec fitting uses the fixed graph projection and settings in the index receipt. Streamlit supplies the interface. RAGAS 0.2.15 supplies the supplementary metric adapters in the separate evaluation environment. Exact versions and environment checks remain in their lock files and receipts.

### Authorship and assistance disclosure
Stephen Butler defined and verified the benchmark records, operated the live pipeline and entered/confirmed the human ratings. Codex assisted implementation, source cross-checks, offline artifact auditing, statistical tooling and preparation of this report, slides and demo video. The secondary review is the author's delayed rescore. AI assistance does not constitute an independent reviewer or source authority. The video uses synthetic narration over authentic captured application states.

<PAGE>
# Appendix A. Extraction by relationship
The per-predicate results use the same strict, source-scoped population as the primary micro result. Counts sum to TP10, FP12 and FN139. No semantic acceptance filter or mitigation fusion enters this breakdown. [4]

| Predicate | TP | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| PART_OF_TACTIC | 0 | 3 | 0 | 0.0000 | undefined | undefined |
| USES | 5 | 0 | 69 | 1.0000 | 0.0676 | 0.1266 |
| USES_TECHNIQUE | 5 | 9 | 70 | 0.3571 | 0.0667 | 0.1124 |

The five matched USES predictions do not establish broad actor/software extraction accuracy: recall remains 5/74 within the annotated scopes. Technique-use mappings include nine exact-reference nonmatches and miss 70 scoped gold assertions. The three PART_OF_TACTIC predictions have no corresponding gold assertions in this population, leaving recall and the scorer's harmonic-mean F1 undefined. They remain false positives in the micro counts.

### Denominators and matching
For each relation, precision is TP/(TP+FP) and recall is TP/(TP+FN). The scorer leaves an undefined constituent metric and its harmonic F1 as null. Micro F1 is 2TP/(2TP+FP+FN) when both micro precision and recall are defined. This preserves the project's original undefined-denominator policy.

An exact triple supported in two reports or two annotation scopes counts separately by scope. Repeated predictions of the same scoped fact collapse only within that scope. Gold absence can reflect coverage/granularity disagreement as documented in the annotation audit. The breakdown is descriptive agreement with the frozen inventory and does not expand that inventory after seeing predictions.

<PAGE>
# Appendix B. Completion update and limitations
This documentation revision records a remaining limitation and a later application integration. It does not revise the original 240 measured outcomes, benchmark labels, entity identities, prompts, evaluation indexes or reported statistics. The original report and source/evidence archive remain preserved alongside this revision.

### Software disambiguation: deferred because of time constraints
Advanced automated disambiguation for software entities outside ATT&CK was not implemented because of project time constraints. The completed system uses type-compatible ATT&CK IDs, exact normalized names and verified aliases. Unknown or ambiguous mentions remain unresolved or retain report-local identities instead of being merged on uncertain evidence.

This conservative policy limits speculative merges but can leave spelling variants or unverified aliases as separate identities. It does not compare publisher, executable, version or surrounding source context to distinguish similarly named tools. These are limitations of the implemented resolver; no benefit from advanced disambiguation is included in the measured results.

A future extension could rank candidate software identities using name variants and explicit source attributes, reject contradictory product evidence and present uncertain matches for review. Validating new merge decisions would require annotated identity examples, rebuilt graph/vector assets and a separately versioned evaluation. This enhancement remains future work for a completed project. It would not by itself resolve the much larger missed-relation/low-recall extraction limitation.

### Live HTTP API: completed after the frozen experiment
The supported HTTP entry point now constructs the existing ApplicationEngine at startup, serves strict /query requests in all four retrieval modes, and closes its clients at shutdown. The documented launcher is python portable.py api. Users can install their own dependencies, run Neo4j and Ollama, and rebuild the development indexes in their own checkout; the API does not require the author's laptop.

Eight HTTP adapter tests, thirteen application tests and five portability checks passed. Separate live HTTP requests for one Rhysida development question returned 200 with cited, non-abstaining answers in text-only, graph-only, hybrid without Node2Vec and full-hybrid modes. These checks used the existing relocated development assets and local services. They establish integration for those requests, not independent semantic accuracy or improved benchmark performance. The API serves the development scope, which differs from the larger frozen evaluation scope.

### Repository evidence
The limitation and future-work discussion is in docs/ThreatWeave_software_disambiguation_plan.md. API setup is in REPRODUCE.md, with live_api.py as the supported server entry point. The original api.py remains the preserved design-contract artifact. Verification details and boundaries are in docs/ThreatWeave_live_api_verification.md; request/response records are under outputs/api_verification/20261017T030754Z. Those new checks are separate from the final benchmark and do not replace its failures or missing scores.
