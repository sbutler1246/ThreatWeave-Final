# ThreatWeave source-only extraction evaluation

This offline analysis uses the preserved model selections before semantic acceptance/rejection and ATT&CK reference fusion. No model output, gold record, source, index, or prompt was changed.

The benchmark contains 146 verified gold records across 39 complete source scopes. Expanding their existing additional-support passages yields 149 distinct scope-specific assertions. This preserves report context.

The precision/recall/F1 values below measure exact agreement with the frozen annotated inventory. The source inspection flags possible inventory or granularity gaps among nonmatches; these metrics cannot alone establish complete semantic correctness.

| Population | TP | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| Strict validated pipeline | 10 | 12 | 139 | 0.4545 | 0.0671 | 0.1170 |
| Duplicate-normalized sensitivity | 10 | 12 | 139 | 0.4545 | 0.0671 | 0.1170 |

## Population and coverage

All 114 frozen extraction windows remain accounted for: {'empty_extraction': 49, 'candidates_ready_for_review': 61, 'validation_failed': 4}. The strict population retains all gold facts from failed/empty windows in recall; persistent schema failures do not become successful outputs. Sensitivity results use only the already documented deterministic first-support removal of duplicate selections, with original errors preserved.

There are 196 normalized candidate occurrences before semantic filtering. Eligibility counts are {'outside_complete_annotation': 173, 'complete_scope': 23}. Outside-scope and boundary-crossing candidates remain listed but are not assumed false against incomplete annotations. These figures are not corpus-wide precision or recall.

Character coverage of the complete gold scopes: {'fully_covered': 39, 'partially_or_uncovered': []}. The four-relationship/window cap and source mention/schema restrictions are extraction limits, not evidence that empty windows contain no facts.

## Strict results by advisory

| Advisory | Scopes | TP | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| AA23-061A | 1 | 1 | 0 | 10 | 1.0000 | 0.0909 | 0.1667 |
| AA23-075A | 1 | 1 | 1 | 6 | 0.5000 | 0.1429 | 0.2222 |
| AA23-165A | 29 | 0 | 0 | 58 | undefined | 0.0000 | undefined |
| AA23-352A | 1 | 0 | 1 | 12 | 0.0000 | 0.0000 | 0.0000 |
| AA24-109A | 3 | 3 | 5 | 18 | 0.3750 | 0.1429 | 0.2069 |
| AA24-131A | 1 | 0 | 0 | 10 | undefined | 0.0000 | undefined |
| AA25-071A | 3 | 5 | 5 | 25 | 0.5000 | 0.1667 | 0.2500 |

## Interpretation and reproducibility

The F1 >= 0.80 proposal target is not met by the strict source-scoped benchmark-agreement result. The extraction method was bounded for diagnostic source selections and was not exhaustive NER. No tuning or extra generation was performed after seeing benchmark labels. Development overlap at the advisory/table-scope level remains disclosed in the frozen protocol.

Source inspection of all eligible predictions found five potential gold coverage/granularity gaps: SoftPerfect, Advanced IP Scanner and NetScan with the source-cited T1016, direct Akira activity with T1090, and direct Medusa RMM activity with T1219. These remain counted as exact-gold nonmatches. Their absence from a declared complete inventory limits interpreting FP as semantic falsehood. annotation_audit.json records the source basis. No new gold labels, exclusions for better scores, or corrected model outputs were substituted.

Endpoint projection uses only exact type-compatible frozen benchmark names, source names, explicit IDs and existing aliases. Local IDs are restricted to their own advisory. It does not add aliases or change the production resolver. Saved production IDs and every projection decision are retained in predictions.json. Relation duplicates are collapsed only within one annotated scope; different report mappings remain distinct.

A true positive requires an exact canonical source-scoped triple and a literal valid evidence span/context. Annotation completeness is the pre-existing author confirmation, not a newly inferred label. Source qualifications, overlap, boundary exclusions, nonexhaustive gold coverage outside the 39 scopes, and scoring-only identity alignment limit generalization.

The existing scope-collapsing scorer is retained only as a diagnostic in results.json; it cannot distinguish identical facts asserted in different advisory scopes. This report uses scope-specific micro counts. Undefined denominators are null, never imputed.

Artifacts: protocol.json, annotation_audit.json, inputs_sha256.json, results.json, predictions.json, gold_expanded.json, scope_alignment.json, windows.json, and report.md. Every source/run artifact used by reconstruction is hashed; originals are unchanged.
