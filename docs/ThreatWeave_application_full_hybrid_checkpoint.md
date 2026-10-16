# Full-hybrid application check

October 15, 2026. The operator's second live application check completed in **Full hybrid** mode at `work/application_qa/20261015T165813Z-950f9f1f`. It produced six non-abstaining claims on its first generation attempt. The assistant inspected the website and audited saved records without submitting another question or calling Neo4j/Ollama.

## Evidence and answer

The saved answer and both prompts exactly match the earlier full-hybrid Rhysida case at `work/hybrid_qa/20261015T043615Z-462852fb/02`. The model digest and shared v2 generator are unchanged. All 15 supplied passage texts, offsets and URLs match freshly verified frozen documents, all six claims have valid citation bindings, the raw response reproduces the displayed answer, and its prompt hash matches.

Retrieval selected five two-hop graph paths, four text hits and 15 distinct supplied passages within 2954/3000 UTF-8 bytes. The record confirms live graph freshness against the fitted graph index, Node2Vec enabled, and the expected text/graph fingerprints. Its nine base candidates and five expansion candidates still merge to nine unique paths; this does not establish a Node2Vec quality benefit.

The CISA VPN/compromised-credential observation is supported. Five mitigation identities appear with their corresponding reference citations, but **User Account Management M1018 is omitted despite being supplied in E14/E15**. The password-policy summary compresses immediate default-credential changes, periodic secured SSH-key updates and password-reuse conditions. Push-notification wording also compresses the explicit only-valid restriction. These are the same generation limitations documented in the completed four-mode comparison, not a new retrieval failure. Human semantic verification remains pending.

The 47.359-second application time includes service/index initialization and verification as well as retrieval and generation; it must not be compared directly with CLI timings that exclude initialization.

## Browser checks

The repaired graph renders seven nodes and six directed edges for the returned paths. The full-hybrid answer remained visible in Answer history when the sidebar mode changed to Graph only and back to Full hybrid. No query was submitted during that switch, and the selected answer remained labeled Full hybrid. This verifies retention across that live mode change. It does not establish persistence across browser/session restart; the earlier reset cause remains unresolved, with saved records intact.

The page was left showing the full-hybrid result and its graph. Screenshot: `work/application_browser_checks/full_hybrid_verified.jpg`. Audit: `work/application_browser_checks/full_hybrid_live_review.json`. Original query records and pending human-review status remain unchanged.

## Next implementation stage

Two live application paths—graph only and full hybrid—now reproduce their corresponding CLI answers. Four-mode adapter/history checks pass with synthetic services, and browser source inspection, export, graph selection, zoom/reset and pan have been checked. Live text-only/ablation UI queries and multiple-live-answer navigation remain unverified, but another four-mode demonstration round is not required to finish this development comparison.

The next major project stage is broader corpus processing: extend beyond the ten reviewed extraction windows while preserving frozen sources, split boundaries, prior accepted records and gold/reference-answer isolation. Human review, final quality/performance evaluation and final documentation remain unfinished. The interface's supported-answer limitations must remain visible rather than being treated as final accuracy results.
