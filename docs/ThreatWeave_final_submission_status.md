# Final submission status

October 16, 2026. The local report, slides, demo and source/evidence package are prepared for the user's submission. No external upload or repository push has been performed.

| Item | Final local status |
|---|---|
| Frozen collection | 240 measured outcomes plus 4 excluded warm-ups; 210 valid answers, 15 abstentions, 15 generation failures |
| Automatic scoring | 639 numeric values, 36 judge failures, 45 unavailable slots out of 720 |
| Extraction evaluation | TP10, FP12, FN139 against 149 scoped assertions; precision 0.4545, recall 0.0671, F1 0.1170 |
| Primary review | 80 completed entries; 75 numeric, 5 failed responses N/A; P069 transcription correction retained |
| Secondary review | 20 completed entries; 19 numeric, 1 failed response N/A; same-author delayed rescore with limited AI assistance for review questions |
| Human analysis | Both exports validated before condition unblinding; primary results and secondary consistency remain separate |
| Report | Final 14-page PDF and editable Markdown in outputs/final_submission |
| Slides | Final 16-slide PPTX with editable charts/tables and source notes in outputs/final_submission |
| Demo | 5:34 H.264 MP4 with synthetic narration, selectable captions and transcript |
| Targeted checks | 43 application/scoring/reporting tests passed; 10 relevant human/reporting tests also passed after the assistance-declaration update |
| Submission package | outputs/ThreatWeave_submission_v2.zip, with per-file checksums and separate archive receipt |

## Findings

Full hybrid's primary available means are 3.350 factuality, 2.000 completeness and 3.900 coherence out of 5 (20 numeric entries each). Text-only completeness is 1.889 (18/20). The marginal completeness difference of +0.111 misses the proposed +0.50 threshold. Paired completeness is +0.167 across 18 shared questions, exploratory 95% interval [-0.278, 0.611]. The conjunctive QA target is not met. Extraction F1 also misses its 0.80 target.

Automatic faithfulness means are 0.626 (52/60) for full hybrid and 0.568 (40/60) for text only. Their paired estimate is +0.124 across only nine fully eligible question clusters, exploratory interval [0.011, 0.240]. Unequal availability, shared-model judging, MODE/evidence-format differences and the small benchmark prevent general superiority claims.

The delayed rescore has 19 numeric pairs per dimension. Exact agreement is 21.1% factuality, 78.9% completeness and 36.8% coherence. Linear weighted kappas are 0.275, 0.823 and 0.153. Secondary scores are lower on average. The same author performed both reviews with limited AI assistance for review questions, so these describe within-reviewer consistency. Day-level dates cannot verify elapsed delay. The user's latest declaration, AI helped a little, supersedes the earlier No AI help reply. Original rating notes remain unchanged; their completed independently wording does not establish an unassisted or independent second review.

## Authoritative records

Use work/human_scoring_analysis/20261016T174034Z-7c181a33 and work/final_completion/submission_results.json. Earlier human-analysis reports are superseded following clarification of secondary AI assistance and remain preserved privately. The completed secondary export changes only the progress document's status field; scores and comments are identical. The original progress file and conversion receipt remain preserved.

The original final answers, labels, prompts, sources and indexes remain frozen. Extraction nonmatches include five possible annotation/granularity gaps, disclosed without favorable exclusions. Claim-level unsupported-claim rates were not annotated and cannot be inferred from ordinal ratings.

## Demonstration and package boundary

The demo shows authentic saved October 15 application states through the original renderer. It makes no new model/database calls and is not a continuous live screen recording. Captured interactions include source expansion, graph selection/zoom, switching preserved runs and structured export. Graph inspection can add display-column metadata to exports without changing answer/evidence content. Earlier live graph-only/full-hybrid checks are historical; additional live text/ablation and multi-answer navigation remain unverified.

The ZIP is a reviewable source/evidence archive. It includes final artifacts, original collection/scoring/extraction records, manifests, index receipts and completed human reviews. It excludes installed environments, credentials, model/vector caches and private build scratch data. Recreating a live installation requires the documented dependencies, database and model setup. The full original workspace retains earlier development records.

## Handoff

Submit the final report, final slides, demo video and required repository/archive through the course's submission system. Historical checkpoint documents retain their original pending labels; the current report and this status supersede them. No additional human ratings are needed.
