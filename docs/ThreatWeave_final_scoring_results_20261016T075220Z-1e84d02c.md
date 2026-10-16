# Automated final scoring results (human review pending)

All 720 slots were recorded: 639 numeric scores, 36 evaluator failures and 45 unavailable slots from fifteen original generation failures. No scores were imputed and no failed check was regenerated. All 36 evaluator failures ended at the fixed 700-token output limit: 33 faithfulness and three context-recall checks.

Means below describe only available scores. Missingness differs by method and is not assumed random. These values are supplementary same-model judgments, not human-verified answer quality.

| Condition | Metric | Mean of available scores | Numeric / 60 | Evaluator failures | No valid answer |
|---|---|---:|---:|---:|---:|
| text_only | faithfulness | 0.5681 | 40/60 | 14 | 6 |
| text_only | answer_relevancy | 0.5546 | 54/60 | 0 | 6 |
| text_only | context_recall | 0.6590 | 54/60 | 0 | 6 |
| graph_only | faithfulness | 0.5031 | 53/60 | 7 | 0 |
| graph_only | answer_relevancy | 0.3355 | 60/60 | 0 | 0 |
| graph_only | context_recall | 0.6096 | 57/60 | 3 | 0 |
| hybrid_no_node2vec | faithfulness | 0.5976 | 47/60 | 6 | 7 |
| hybrid_no_node2vec | answer_relevancy | 0.4928 | 53/60 | 0 | 7 |
| hybrid_no_node2vec | context_recall | 0.5928 | 53/60 | 0 | 7 |
| hybrid | faithfulness | 0.6255 | 52/60 | 6 | 2 |
| hybrid | answer_relevancy | 0.4861 | 58/60 | 0 | 2 |
| hybrid | context_recall | 0.7096 | 58/60 | 0 | 2 |

## Paired question comparisons

Each included question has numeric scores for all three repeats in both compared conditions. First average repeats within each question; then average the paired question differences. Intervals resample paired questions 10,000 times with seed42 and use percentile 2.5/97.5 endpoints. Missing values are not imputed. Question IDs excluded from each comparison are in paired_comparisons.json.

These are exploratory 95% intervals, with no multiple-comparison adjustment. The paired subset can differ across comparisons and cannot represent missing questions without further assumptions. Twenty questions across a limited advisory corpus also limit generalization.

| Metric | A minus B | Paired questions / 20 | Mean difference | Exploratory 95% interval |
|---|---|---:|---:|---|
| faithfulness | text_only minus graph_only | 10/20 | 0.0900 | [-0.1454, 0.3319] |
| faithfulness | text_only minus hybrid_no_node2vec | 9/20 | -0.1086 | [-0.2377, 0.0340] |
| faithfulness | text_only minus hybrid | 9/20 | -0.1236 | [-0.2403, -0.0107] |
| faithfulness | graph_only minus hybrid_no_node2vec | 13/20 | -0.1053 | [-0.2927, 0.0722] |
| faithfulness | graph_only minus hybrid | 14/20 | -0.1836 | [-0.3171, -0.0514] |
| faithfulness | hybrid_no_node2vec minus hybrid | 14/20 | -0.0620 | [-0.2099, 0.0464] |
| answer_relevancy | text_only minus graph_only | 17/20 | 0.2106 | [0.0788, 0.3423] |
| answer_relevancy | text_only minus hybrid_no_node2vec | 15/20 | 0.0626 | [-0.0040, 0.1245] |
| answer_relevancy | text_only minus hybrid | 16/20 | 0.0615 | [-0.0038, 0.1238] |
| answer_relevancy | graph_only minus hybrid_no_node2vec | 17/20 | -0.1454 | [-0.2766, -0.0236] |
| answer_relevancy | graph_only minus hybrid | 18/20 | -0.1394 | [-0.2717, -0.0194] |
| answer_relevancy | hybrid_no_node2vec minus hybrid | 16/20 | 0.0168 | [-0.0098, 0.0472] |
| context_recall | text_only minus graph_only | 16/20 | 0.0642 | [-0.1128, 0.2569] |
| context_recall | text_only minus hybrid_no_node2vec | 15/20 | 0.1315 | [-0.0185, 0.3056] |
| context_recall | text_only minus hybrid | 16/20 | -0.0432 | [-0.2465, 0.1687] |
| context_recall | graph_only minus hybrid_no_node2vec | 17/20 | 0.0458 | [-0.0801, 0.1585] |
| context_recall | graph_only minus hybrid | 17/20 | -0.0472 | [-0.1760, 0.0686] |
| context_recall | hybrid_no_node2vec minus hybrid | 16/20 | -0.0987 | [-0.2046, -0.0188] |

## Audit and interpretation limits

Saved artifact/input/receipt checks passed for all 720 tasks. Request settings, response correspondence and pre/post model identity were checked. 414 faithfulness/context-recall formulas were independently recomputed from saved judge verdicts without model calls. Relevancy scores were checked for bounds, request bindings and noncommittal behavior; cosine values were not independently recomputed because that would require embedding inference.
There are 0 numeric faithfulness results with different statement/verdict counts. These flags do not alter frozen native scores; they identify an additional judge-completeness limitation for interpretation.
Graph-only empty-evidence abstentions remain scored responses. Original collection failures and evaluator output truncation are separate events. The four prompts retain a MODE field, and evidence formats differ. No Python/service/GPU resource measurements are available from collection. Human ratings and extraction precision/recall/F1 are still pending. Do not claim overall method superiority from these conditional means.
