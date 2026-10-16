# ThreatWeave human answer evaluation

Primary review: Stephen Butler, 2026-10-16, 80 repeat-one entries. Secondary review: Stephen Butler, 2026-10-16, 20 entries from five questions, method delayed_rescore.

The primary reviewer used AI assistance to inspect evidence and draft comments, then entered and confirmed the ratings. The primary export preserves the completed decisions and the documented P069 transcription correction. The author declared limited AI help with the secondary review; the extent was not quantified. The secondary method is reviewer-declared; day-level form dates cannot independently verify the elapsed delay. Same-person delayed results measure within-reviewer consistency and must not be labeled independent inter-rater agreement.

Scores use 1 (poor) through 5 (excellent). Failed responses remain N/A; meaningful abstention ratings remain numeric. Primary results and secondary consistency stay separate, with no averaging or replacement of the primary ratings.

| Condition | Numeric / 20 | Factuality | Completeness | Coherence | Failure N/A | Abstentions |
|---|---:|---:|---:|---:|---:|---:|
| text_only | 18/20 | 2.944 | 1.889 | 3.833 | 2 | 0 |
| graph_only | 20/20 | 3.500 | 1.900 | 4.000 | 0 | 5 |
| hybrid_no_node2vec | 17/20 | 3.529 | 2.000 | 3.882 | 3 | 0 |
| hybrid | 20/20 | 3.350 | 2.000 | 3.900 | 0 | 0 |

## Paired comparisons

Each comparison uses numeric repeat-one ratings for the same question in both conditions. Exploratory percentile intervals resample questions 10,000 times with seed42. N/A cases are excluded pairwise and disclosed, with no zero or perfect-score imputation. The 18 comparisons are not adjusted for multiplicity; available subsets may differ.

| Dimension | A minus B | Paired questions / 20 | Mean difference | Exploratory 95% interval |
|---|---|---:|---:|---|
| factuality | text_only minus graph_only | 18/20 | -0.556 | [-1.167, 0.000] |
| factuality | text_only minus hybrid_no_node2vec | 16/20 | -0.625 | [-1.062, -0.188] |
| factuality | text_only minus hybrid | 18/20 | -0.444 | [-0.944, 0.056] |
| factuality | graph_only minus hybrid_no_node2vec | 17/20 | -0.118 | [-0.824, 0.647] |
| factuality | graph_only minus hybrid | 20/20 | 0.150 | [-0.550, 0.950] |
| factuality | hybrid_no_node2vec minus hybrid | 17/20 | 0.118 | [-0.118, 0.412] |
| completeness | text_only minus graph_only | 18/20 | -0.111 | [-0.500, 0.278] |
| completeness | text_only minus hybrid_no_node2vec | 16/20 | -0.312 | [-0.750, 0.062] |
| completeness | text_only minus hybrid | 18/20 | -0.167 | [-0.611, 0.278] |
| completeness | graph_only minus hybrid_no_node2vec | 17/20 | -0.118 | [-0.529, 0.176] |
| completeness | graph_only minus hybrid | 20/20 | -0.100 | [-0.500, 0.300] |
| completeness | hybrid_no_node2vec minus hybrid | 17/20 | -0.059 | [-0.176, 0.000] |
| coherence | text_only minus graph_only | 18/20 | -0.167 | [-0.444, 0.111] |
| coherence | text_only minus hybrid_no_node2vec | 16/20 | -0.062 | [-0.188, 0.000] |
| coherence | text_only minus hybrid | 18/20 | -0.056 | [-0.167, 0.000] |
| coherence | graph_only minus hybrid_no_node2vec | 17/20 | 0.118 | [-0.176, 0.412] |
| coherence | graph_only minus hybrid | 20/20 | 0.100 | [-0.150, 0.350] |
| coherence | hybrid_no_node2vec minus hybrid | 17/20 | -0.059 | [-0.176, 0.000] |

## Secondary consistency

Twenty rescores represent five question clusters across four conditions. Descriptive agreement and linear weighted kappa are exploratory; N/A pairs are excluded and counted. They do not establish reliability across independent reviewers or a broad question population.

| Dimension | Numeric pairs | Exact agreement | Within one point | Mean absolute difference | Linear weighted kappa |
|---|---:|---:|---:|---:|---:|
| factuality | 19 | 0.211 | 1.000 | 0.789 | 0.275 |
| completeness | 19 | 0.789 | 1.000 | 0.211 | 0.823 |
| coherence | 19 | 0.368 | 0.895 | 0.737 | 0.153 |

## Limits

Method labels and automatic scores were withheld until both completed review files passed validation. Graph-shaped supplied evidence makes blinding partial. The same human reviewer and possible AI assistance limit independence. The twenty primary questions, failure-related missingness, schema restrictions, source context, ordinal score scale, and MODE prompt field limit causal and population claims. Ratings quantify the displayed answers, not every possible behavior of the underlying software.
