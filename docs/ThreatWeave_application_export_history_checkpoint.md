# Application export, history and pan checks

Later checkpoint: [the full-hybrid application result passed its integration check and retained history across a live mode switch](ThreatWeave_application_full_hybrid_checkpoint.md). The earlier reset observation below remains as history; its cause was not established.

October 15, 2026. The assistant inspected the existing live Rhysida result without submitting another question or calling Neo4j/Ollama.

The browser's **Download this result** action produced `S:\Downloads\threatweave-answer.json`. Parsed JSON exactly matches `work/application_qa/20261015T074134Z-a878f56c/display.json`, including its six claims, 13 passages, request, graph/retrieval metadata and model digest. Its top-level fields contain no connection-settings object. The original saved answer is unchanged.

Actual graph panning was verified by dragging empty SVG space: the scene changed to `translate(68.0672268907563 0) scale(1)`. Reset view restored `translate(0 0) scale(1)`.

The offline Streamlit UI suite now has four passing tests, completed in 1.029 seconds with normal Windows file access. The new test uses synthetic adapters to submit all four modes, navigate back to the first of four answer snapshots, verify an export control exists and clear visible history without closing the engine or issuing extra queries. The sandboxed attempt hung while initializing the test runtime and was stopped; the normal-access rerun passed. No real service adapter was constructed by these tests.

The browser's visible history was empty after selecting Full hybrid for the next question. The cause is not established: offline mode/history tests pass, and session resets legitimately lose the documented session-only visible history. The original run and exact downloaded export remain intact. Retention across a subsequent live result/mode change still needs a browser check; do not label this behavior fully verified.

The existing page is prepared with **Full hybrid** and the same Rhysida question. The operator should click **Ask ThreatWeave** to perform the next live application check, keeping Neo4j and Ollama running. If the connection has reset, re-enter the password in the application. No new comparison round or benchmark evaluation is being requested.

Receipt: `work/application_browser_checks/export_history_pan_review.json`. Broader corpus processing, human source verification and controlled final evaluation remain unfinished.
