# First live application answer and graph repair

October 15, 2026. The operator submitted the Rhysida access-and-guidance question through the local interface in Graph only mode. Run: `work/application_qa/20261015T074134Z-a878f56c`. The assistant inspected the actual website answer, Sources, Run details and Query graph tabs, then audited its saved files without submitting another question or calling Neo4j/Ollama.

## Answer review

The run produced six non-abstaining cited claims on its first attempt. Its 13 source passages and five two-hop graph paths match the prepared development scope. Every passage text, offset and URL matches freshly verified frozen source documents; all six claims have valid citation bindings. The saved raw response reproduces the displayed answer and its prompt hash matches. The answer text and both generation prompts are identical to the earlier graph-only Rhysida case at `work/graph_qa/20261015T070142Z-5b1a5398/02`.

The CISA observation supports authentication to internal VPN access points with compromised valid credentials. The answer includes all five supplied mitigation identities and supported core actions: Application Developer Guidance M1013, Active Directory Configuration M1015, User Training M1017, User Account Management M1018 and Privileged Account Management M1026. It separates observation and guidance citations rather than attributing reference recommendations to CISA.

The main limitation is compressed M1026 guidance: it omits checking unauthorized new local accounts and the explicit restriction on privileged account use across administrative tiers. The observation also compresses the source's commonly-observed framing, and extra report/section citations do not independently establish behavior. This is AI-assisted source inspection, not final human verification or a quality score. Original answer and review status remain unchanged.

The recorded 31.430-second case time includes service/index initialization, source verification, retrieval, packing and generation. It is not directly comparable to earlier CLI times that exclude initialization.

## Browser graph defect and repair

The initial graph tab displayed controls but no nodes. Browser inspection found no SVG element and a script error while appending graph elements: Streamlit's HTML sanitization removed the static SVG container.

`application_graph.html` now keeps an ordinary HTML canvas placeholder and builds its SVG container, marker and scene with namespace-aware DOM APIs inside the existing trusted local script. Source labels remain escaped JSON data and DOM text; sanitization was not disabled. A light graph background also preserves text contrast in the application's dark theme.

Streamlit's Rerun menu refreshed the dynamically read template while preserving the current answer, history and connection. No new query was submitted. The actual browser then showed **seven nodes and six directed edges**. Selecting Rhysida actors and Valid Accounts displayed their identities; Zoom in changed the scene scale to 1.2 and Reset view restored it. JavaScript syntax validation passed. Pan was not tested in this check. The graph remains a snapshot of returned, supported paths, not a continuously refreshed database view.

Review receipt: `work/application_browser_checks/rhysida_live_review.json`.

Screenshot: `work/application_browser_checks/rhysida_graph_fixed.jpg`.

## Current application status

Later checkpoint: [the operator's full-hybrid application check completed](ThreatWeave_application_full_hybrid_checkpoint.md), with exact CLI answer/prompt parity, verified sources and retained history across a mode change. The observations below preserve the earlier graph-only checkpoint.

Later check: [browser export and pan passed, and expanded offline history/mode tests passed](ThreatWeave_application_export_history_checkpoint.md). The browser's visible history was empty after staging the next mode, with saved data intact; retention on a subsequent live result still needs verification. The observations below preserve the preceding checkpoint.

Initial page loading, one operator-run live graph-only answer, exact source display, saved records, retained answer history and graph rendering/selection/zoom have now been checked in the browser. The completed four-mode CLI comparison remains unchanged. Full-hybrid/text-only/no-Node2Vec live queries through the UI, multiple-result history navigation, browser export and pan remain unverified in this session; offline adapter/UI tests cover their implemented boundaries where applicable.

Broader source processing, human semantic verification and controlled final quality/performance evaluation remain unfinished. The application still uses the same limited development pool and shared generator with its recorded answer limitations.
