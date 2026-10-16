# Load the refreshed development indexes in the application

Restart checkpoint: the operator confirmed the app was running, and a fresh browser session loaded the expected initial page without a visible startup error. No query was submitted. [The remaining corpus inventory](ThreatWeave_corpus_coverage_inventory.md) identifies three additional reports eligible for development source preparation and seven reports excluded from further development expansion because they contain held-out evidence.

October 15, 2026. The [text index](ThreatWeave_corpus_batch_text_index_checkpoint.md) and [graph-vector index](ThreatWeave_corpus_batch_graph_index_checkpoint.md) are ready and share the same accepted scope: 41 CISA windows and 96 ATT&CK reference parents. They contain 215 text chunks and 117 graph vectors covering 179 directed facts.

Restart the local application using the existing environment:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\run_application.py"
```

If an older ThreatWeave server is still running, stop it with Ctrl+C in its terminal before relaunching. The launcher disables file watching, so a browser refresh or adapter reconnect alone does not reliably reload changed Python modules in an old process. Keep this terminal open. Neo4j and Ollama are needed when the operator later submits graph-enabled questions.

Open or refresh [ThreatWeave](http://127.0.0.1:8501). Restarting can reset browser-session history; saved run records remain on disk. The initial page performs no application query. Connection credentials are entered when needed. The app verifies the accepted scope and index assets, and full hybrid additionally checks the live graph for freshness when queried.

This step reloads the refreshed development assets. No additional four-mode demonstration is required for the index-refresh checkpoint. Fresh live application behavior on this expanded scope remains unverified until exercised by the operator. Broader corpus completion, human review and controlled held-out evaluation remain pending.
