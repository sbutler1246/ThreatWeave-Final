# Alignment with the submitted ThreatWeave proposal

Authority: Stephen Butler’s five-page CS 6338 Milestone 1 proposal, SHA-256 `ca09acbe52677561221103cc725b0104a3194d08a061464feeeba01c1f5f76fa`.
The assignment screenshots control the eight-section Milestone 2 structure and required PDF/repository deliverables. The proposal controls project commitments.

| Commitment in submitted proposal | Corrected design/checkpoint |
|---|---|
| Seven classes with canonical_id/name/type | Restored node names and the exact ontology; provenance helpers remain implementation records |
| ThreatGroup ASSOCIATED_WITH Campaign | Restored that direction; removed unapproved campaign-use predicates |
| Technique PART_OF_TACTIC Tactic; Technique MITIGATED_BY Mitigation | Restored exact predicates and mitigation direction |
| MENTIONED_IN occurrence; SUPPORTED_BY specific attribute evidence | Specified claim_key/evidence_text and prohibited co-occurrence inference |
| 400–600-token extraction windows with about 60-token overlap | Restored; separate MiniLM retrieval children avoid 256-wordpiece truncation |
| Node2Vec 128 dimensions, length-20 walks, ten walks/node, p=q=1 | Restored initial settings; seed recorded; tuning only on development queries |
| Five text hits, five neighbors/seed, maximum three hops, 3,000 context tokens | Restored limits and added the three-hop group/software/technique/mitigation template |
| Text baseline gets the same CISA and relevant ATT&CK evidence | Explicit attributed ATT&CK reference text available in the text collection |
| 20+ held-out QA: ≥8 actor/software/technique, ≥8 technique/mitigation, ≥4 cross-report | Candidate pool now has 49/8/4; validator enforces the verified minimum mix |
| Extraction scored before fusion; TP requires valid evidence | Scorer excludes fused facts, requires evidence_valid, and marks undefined denominators |
| Blind 1–5 scores; independent five-question review if possible, otherwise delayed 25% re-score | Restored exact protocol and single-rater limitation |
| Extraction F1 ≥0.80; hybrid completeness gain ≥0.5/5 without lower factuality/faithfulness | Restored as targets only; paired analysis/bootstrap intervals planned |
| Streamlit history, context inspection, live per-query graph | Restored all three planned interaction features |
| Five-report overlap/timing pilot; Royal March 2023 initial candidate | Candidate snapshots remain provisional; downloaded Royal/BlackSuit update is flagged |
| Working pipeline October 10; final deadline October 17, 2026 | Preserved as planned gates, never described as completed work |

No related-work comparison or optional incident-specific extension has been added.
The checkpoint contains 146 author-verified extracted gold triples in 39 author-confirmed complete scopes and 61 author-validated QA pairs, plus 39 separate fused mitigation references. The final benchmark selects 20 questions with the 8/8/4 mix, separate from 21 development questions and 20 held-out reserves. The author manually validated the material first, then requested a Codex cross-check. Completion was confirmed on October 5, 2026; both stages remain recorded. The checkpoint was published to https://github.com/sbutler1246/ThreatWeave and its uploaded file contents were verified on October 5, 2026. Pilot/service integration, final corpus/chunk alignment, and performance evaluation remain planned.
