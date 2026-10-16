# Independent installation

For a fresh installation on your own computer, follow [REPRODUCE.md](../REPRODUCE.md). It provides commands relative to your own checkout, a complete accepted source bundle, local model downloads and index rebuilding. No files or services are fetched from the author’s laptop.

The dated record below documents the original development session. Its installed-environment assumptions are historical; use the portable guide above for installation.

---

# Application integration and interface setup

Completed: [the setup checkpoint](ThreatWeave_application_setup_checkpoint.md) verifies Streamlit installation, preservation of all 108 existing package versions and three passing offline UI checks. [Launch the interface next](ThreatWeave_application_launch_step.md). Installation-pending statements below preserve the preceding implementation checkpoint.

October 15, 2026. The expanded four-mode development comparison is complete. The next implementation stage connects those existing pipelines to a local Streamlit interface. Application code and offline adapter checks are ready; installation, browser inspection and live UI verification remain pending. The completed comparison outputs and shared v2 generator are unchanged.

## Run this setup command

```powershell
python portable.py doctor
```

Internet access is needed to install the UI dependencies. Neo4j and Ollama are not needed for setup. The script uses the existing uv executable and Python 3.12 environment, saves all currently installed package versions as resolver constraints, and performs a dry run before installation. If those constraints conflict with the UI dependencies, it stops before installation rather than relaxing them. After installation it verifies existing versions remain unchanged and runs three offline Streamlit AppTest scenarios using synthetic evidence and fake service adapters.

The direct UI pin is [Streamlit 1.66.0](https://pypi.org/project/streamlit/1.66.0/), which supports the existing Python 3.12 environment. This is a direct pin, not a full transitive lock. The resolved environment and setup status save under `work/application_setup/<run>`. Installation failure can leave newly added packages; the script does not attempt an automatic rollback. It never rebuilds or modifies the text/graph collections.

Expected final message: `READY: Interface installed, existing packages preserved, offline UI checks passed.` Launch and live verification follow only after this setup passes. `run_application.py` then serves the UI at `http://127.0.0.1:8501`; it binds to localhost and disables usage telemetry. It does not send questions at startup. The operator will start it separately, with Ollama available and Neo4j available for graph-enabled questions.

## Implemented interface

- Question entry and the four explicit retrieval modes, with no silent fallback.
- Session-local answer history, mode/timing labels, cited claims and per-answer JSON export. History is not appended to subsequent model prompts.
- Exact source passages, source links, recorded dates where available, offsets, and separate CISA advisory versus ATT&CK guidance labels.
- A graph built only from the paths returned for that question. Zoom, pan and node/arrow selection expose canonical identities, directions, assertion IDs, citations and observation/reference source types. The displayed graph is a query-time snapshot, not a continuously refreshed graph.
- Staged errors, explicit disconnect/reconnect, and saved success/failure records under `work/application_qa`. Clearing visible history does not delete saved records.

The graph uses a bundled HTML/JavaScript template without a CDN or a new graph library. Source labels are encoded as JSON data and displayed with DOM text APIs. Streamlit's [HTML API](https://docs.streamlit.io/develop/api-reference/text/st.html) executes the trusted local graph script; user/source content is not used as executable HTML. Answer and passage content are displayed as plain text.

Neo4j credentials stay in the browser session/server memory and driver, never in saved query records or configuration. Change connection settings through disconnect/reconnect; cached adapters retain their original connection until disconnected. Text-only does not create or probe a Neo4j driver. The Ollama model digest is checked per request and held stable within a session. The adapter rechecks frozen sources, configuration and cached index asset checksums, and rejects a changed published graph pointer. Existing full-hybrid live projection checks remain intact.

## Code and verification

| File | Role |
| --- | --- |
| `application_engine.py` | QueryEngine-compatible orchestration, lazy adapters, service/model checks, saved records and stage errors |
| `streamlit_app.py` | Questions, mode selection, source inspection, history and result display |
| `application_view.py`, `application_graph.html` | Snapshot history and interactive directed graph from returned evidence |
| `setup_application.py`, `requirements-application.txt` | Constrained operator-run UI installation |
| `check_application_setup.py`, `run_application.py` | Offline UI checks and localhost launcher |

Preparation receipt: `work/application_checks/20261015T072636Z-5e75827c/check_receipt.json`.

The full offline suite collected 188 tests: **187 passed and one UI test module was skipped because Streamlit is absent**. After adding long-lived source/index-change guards, all 13 application tests passed in a targeted rerun. These cover mode preservation/no fallback, no Neo4j in text-only mode, empty-evidence abstention, model/config/index/source changes, generator evidence tampering, stage-error privacy, history snapshots, graph data encoding and resource closure. Windows blocked temporary files on the sandboxed first attempt; authorized offline test execution outside the sandbox passed. No live Neo4j or Ollama calls were made.

Python source syntax checks passed for all six application/setup modules. Graph HTML was generated from each of the three recorded graph-only answers, and Node checked all three scripts' syntax. This is not browser visual verification. The real Streamlit page/history/failure scenarios are included in `tests/test_application_ui.py` and run during setup, using [AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest) with real service construction forbidden. Actual browser interaction and live model/database queries remain untested until operator setup and launch.

## Remaining boundaries

This is the limited development-source application, not a full-corpus or final evaluated product. It reuses the unchanged bounded retrieval and cited generator, including the answer limitations documented in the [four-mode comparison](ThreatWeave_expanded_four_mode_development_comparison.md). Citation binding does not establish factual correctness. Human verification, broader source processing, final extraction/QA/performance evaluation and deployment beyond the local interface remain unfinished. The existing FastAPI contract remains separate; no API server was started or configured by this step.
