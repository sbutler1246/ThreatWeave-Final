# Software disambiguation: limitation and future work

Status: not implemented because of project time constraints; deferred to future work. The project and its evaluation are complete. The design ideas below are unevaluated possibilities for a later extension, not remaining deliverables for this submission. This note documents the limitation without changing production identities, the frozen graph, benchmark labels or reported scores.

## Why it was not implemented

Project time constraints prevented implementation and validation of advanced automated disambiguation for software entities outside ATT&CK. The completed project therefore retains its deterministic, type-compatible ID/name/verified-alias resolver. Unknown or ambiguous software mentions remain unresolved or retain report-local identities rather than being merged on uncertain contextual evidence.

This leaves a coverage limitation: spelling variants and unverified aliases can remain separate, and the resolver does not use publisher, executable, version or source context to distinguish similarly named tools. The current policy reduces speculative merging but does not solve contextual software disambiguation. No benefit from an advanced resolver is included in the project's measured results.

Implementing the enhancement now would change entity identities and potentially the graph paths and evidence available to retrieval. It would require separately annotated identity examples, validation of merge decisions, rebuilt graph/vector assets and a new evaluation. It is documented as future work so the completed results continue to describe the system that was actually evaluated.

## Current behavior

`resolve.py` checks entity type, explicit ATT&CK ID, exact normalized names and verified aliases. Normalization applies Unicode NFKC, case folding and whitespace normalization. Unknown or ambiguous names remain unresolved. Ingestion can retain report-local software identities instead of merging them into a global entity. This limits false merges but misses spelling variants and cannot reliably distinguish unrelated programs with similar names.

## Possible future extension

A future version could add a separate candidate-review stage after exact resolution and before accepting a new identity. Exact resolution would remain the default production path until the additional stage had been evaluated.

1. Retrieve a small set of type-compatible Software candidates using normalized names, verified abbreviations and spelling similarity. Similarity proposes candidates; it does not authorize a merge. Keep identifiers, meaningful punctuation, versions and product editions available in the original mention.
2. Compare explicit source details: publisher/product family, executable name, version, description, source URL and an explicit alias statement. Record the document ID, literal quotation and exact supporting offsets for each detail. Actor co-occurrence and shared ATT&CK techniques are weak context, not proof of software identity.
3. Reject conflicting publisher/product evidence. Keep tools with the same display name separate when the source cannot establish identity. Never treat `net`, `net.exe` and a similarly named third-party product as interchangeable based on spelling alone. A product-family identity and a version-specific identity require an explicit relationship policy rather than silently discarding version information.
4. Produce a review packet containing the original mention, ranked candidate IDs, comparison features, contradictions, source spans and a recommendation to link, retain locally or defer. Do not represent an uncalibrated ranking score as a probability or claim that a threshold such as 0.80 is validated.
5. Store an approved link as a separate, provenance-bearing decision with reviewer, time and resolver version. Preserve original report-local IDs and assertions. Promote an alias to the verified catalog only after its evidence has been checked. Decisions must be reversible and must not rewrite the frozen cohort.

A later automatic-link policy could require a unique candidate with strong explicit identity evidence and no contradictory attributes. Its threshold and margin over the runner-up must be chosen on a new development set. Until validated, uncertain candidates remain local and enter review.

## Evaluation needed for a future version

Prepare new annotated mention pairs covering true aliases, typographical variants, abbreviations, common tool names, same-name different products, publisher conflicts, version distinctions and unrelated entities sharing a technique. Split by report/product family so repeated aliases do not leak across development and evaluation. Review the identity labels against original source spans.

Compare the current exact resolver against candidate assistance. Report candidate recall@k, accepted-link precision/recall, false-merge and false-split counts, abstention/review rate and coverage. False merges deserve particular attention because they can transfer an actor's technique or mitigation path to unrelated software. Report both quality and the fraction of mentions the method actually resolves.

Any changed identity decisions require new graph/vector builds and a separately versioned QA experiment. The original 240 outcomes and extraction F1 remain as originally collected. This feature could reduce identity errors; it does not by itself address the much larger missed-relation/low-recall extraction problem.
