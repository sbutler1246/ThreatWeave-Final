# Independent installation

For a fresh installation on your own computer, follow [REPRODUCE.md](../REPRODUCE.md). It provides commands relative to your own checkout, a complete accepted source bundle, local model downloads and index rebuilding. No files or services are fetched from the author’s laptop.

The dated record below documents the original development session. Its installed-environment assumptions are historical; use the portable guide above for installation.

---

# Launch the local ThreatWeave interface

Later check: [the first live graph-only answer and browser graph checks completed](ThreatWeave_application_live_checkpoint.md). The Rhysida answer has supporting evidence and remaining guidance-detail omissions; a blank-graph rendering defect was repaired. The launch/check instructions below remain available for future sessions.

[Application setup passed](ThreatWeave_application_setup_checkpoint.md): Streamlit is installed, existing package versions are preserved, and all three offline UI checks passed.

Keep Neo4j and Ollama running, then launch:

```powershell
python portable.py app
```

Keep this terminal open while using the application. Open [ThreatWeave on localhost](http://127.0.0.1:8501) in your browser. The page initially shows question entry, mode selection and connection settings; it does not call Neo4j or Ollama until a question is submitted.

## First application check

Choose **Graph only**. In Connection settings, retain the default Neo4j URI `bolt://localhost:7687`, username `neo4j` and database `neo4j`, and enter the instance password. Ask:

> According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.

The first request verifies frozen development sources and initializes its selected adapter before retrieving and generating an answer. A successful query should show cited claims, source passages, the returned directed graph and a saved results location. Inspect the source expanders and the Query graph tab; test zoom, pan and node/arrow selection. A valid citation does not establish semantic correctness, so assess the answer against the shown passages.

This is one live application smoke query, not a repeat of the four-mode comparison. Results save under `work/application_qa/<run>`, including question, evidence, retrieval details, prompts/model responses when generation occurs, answer, display metadata and summary. A failed stage produces an explicit message/receipt without silently changing modes. Original comparison results are untouched.

Changing connection settings requires **Disconnect / reconnect**, then entering the desired credentials and submitting a question. **Clear visible history** clears only the browser session's visible answers; saved run records remain on disk. Questions do not include earlier answer history in their generation context. Stop the local server with Ctrl+C in its terminal when finished.

Ctrl+C stops the local app without undoing installation or deleting saved records. The launcher now handles this interruption without its own traceback. Restart using the same launch command, then refresh the browser. Browser-session history may reset; previously saved run records remain on disk. A question interrupted before completion may have an incomplete run record.

Browser appearance, interactions and live query verification remain pending until this launch/check is performed. Full hybrid is available as another mode using its existing verified index; missing or stale graph assets fail explicitly. Broader corpus processing and final quality/performance evaluation remain unfinished.
