# Reproduce ThreatWeave on your own computer

All commands below run inside **your own copy** of this repository. Nothing is downloaded from the author's computer. Source snapshots, benchmark labels, accepted source assertions, collected answers, ratings and metric receipts are in GitHub. Python packages and model weights come from their public distributors.

The repository is **public**, so readers can clone it or download GitHub's ZIP without access to the author's account or computer. The nested `outputs/ThreatWeave_submission_v2.zip` is the original submission archive; use the current repository checkout for the portable tools added after publication.

## 1. Get your own copy

Install [Python 3.12](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads), or use GitHub Desktop's **Clone repository**. In a terminal:

```text
git clone https://github.com/sbutler1246/ThreatWeave-Final.git
cd ThreatWeave-Final
python --version
```

On Windows, use `py -3.12` instead of `python` if needed. With GitHub's **Code → Download ZIP**, extract the ZIP and open a terminal in the extracted folder instead. No drive letter, username, pre-existing virtual environment or author-owned service is required.

## 2. Recompute the published results

This workflow needs **only Python's standard library**. It needs no installation, database, Ollama, model weights or internet after obtaining the repository:

```text
python -S reproduce_results.py
```

Expect `PASS: Published statistics match.` New results are written to `outputs/reproduction/<timestamp>/results.json` and `report.md`. A missing file, changed frozen input or numerical mismatch exits unsuccessfully. The script leaves original evidence and results untouched.

It verifies the preserved source/archive checksums, re-joins 80 primary ratings and 20 delayed rescores, recomputes means and consistency, repeats the 18 human and 18 automatic paired comparisons with their original bootstrap settings, checks all 720 native metric slots and independently recomputes 414 judge-verdict formulas. It also recomputes extraction metrics, timing summaries, reported gains and point targets. Extraction must give TP=10, FP=12, FN=139 and F1=0.11695906432748539. The QA and extraction targets remain unmet.

This is reproduction of the **analysis of collected observations**. The preserved aligned pre-review extraction predictions remain inputs. Native answer-relevancy cosine values are hash-verified inputs; this command does not rerun embedding inference, models or human judgments.

Historical Windows paths inside receipts are provenance strings. The analysis command maps recognized project paths to files in **this checkout**, rejects paths outside it and never falls back to the original computer.

## 3. Run the saved application demonstration

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-replay.txt
.venv\Scripts\python.exe -m streamlit run demo_replay.py --server.address=127.0.0.1 --server.port=8502 --browser.gatherUsageStats=false
```

On macOS/Linux, use `.venv/bin/python` in place of `.venv\Scripts\python.exe`. Open `http://127.0.0.1:8502`, then choose either saved Rhysida run. This is an explicitly labeled replay, with the original answer, citations, source passages and returned graph. It makes no new database/model calls. Stop it with Ctrl+C.

## 4. Build and run your own live application

The live app supports text only, graph only, hybrid without Node2Vec and full hybrid. This UI uses the original **development scope**: 53 CISA windows, 139 ATT&CK reference parents, 142 domain nodes and 245 directed facts. The final experiment's expanded shared evaluation scope (101 windows, 190 reference parents, 212 nodes, 394 facts) is a different scope; the saved-results command above reproduces that experiment's reported statistics.

Use a new Python 3.12 environment. Application requirements are direct version pins; the checked Windows environment is also recorded in the reproduction verification record. Other operating systems and hardware require their own verification. Downloads, installation and index construction can take time and substantial disk/memory; the Llama 3.1 8B model alone is several GB. No measured minimum RAM/GPU requirement was established in this study. CPU text embeddings are used; Ollama selects its available local hardware.

Windows PowerShell, in your checkout:

```powershell
python -m venv .venv-live
.venv-live\Scripts\python.exe -m pip install -r requirements-portable.txt
.venv-live\Scripts\python.exe -m pip check
.venv-live\Scripts\python.exe portable.py doctor
```

For the exact tested Windows package resolution, replace `requirements-portable.txt` with `requirements-portable-windows.lock.txt`. That file pins all resolved versions; it is a version lock, not a distribution-hash lock. On macOS/Linux substitute `.venv-live/bin/python` and use the direct requirements file, since the Windows resolution is platform-specific. Do not install the separate RAGAS evaluator lock over this application environment.

### Install your own services

Install and start [Ollama](https://docs.ollama.com/quickstart), then download the model from Ollama's registry:

```text
ollama pull llama3.1:8b
ollama list
```

Keep Ollama available at `http://localhost:11434`. The app records the model digest and refuses a digest change within a session. A mutable model tag, different hardware/runtime and nondeterministic execution can produce different new answers. New answers do not replace the frozen experiment.

Create a **new empty Neo4j database** on your computer. [Neo4j Desktop](https://neo4j.com/download/) is one option. Neo4j Community in Docker is another; see the [official Docker instructions](https://neo4j.com/docs/operations-manual/current/docker/introduction/). The schema uses Neo4j's standard constraints, indexes and Cypher; APOC and GDS are not required. Use your own password and keep the default local connection `bolt://localhost:7687` unless you select another port.

### Download embeddings and build your own indexes

```powershell
.venv-live\Scripts\python.exe portable.py download-model
.venv-live\Scripts\python.exe portable.py check-sources
.venv-live\Scripts\python.exe portable.py import-graph
.venv-live\Scripts\python.exe portable.py index-text
.venv-live\Scripts\python.exe portable.py index-graph
.venv-live\Scripts\python.exe portable.py app
```

The importer prompts for **your** Neo4j password and refuses a nonempty database. Schema creation and accepted facts do not require an LLM call. For a different database connection, use `portable.py import-graph --uri bolt://localhost:YOUR_PORT --user YOUR_USER --database YOUR_DATABASE`, then give the same settings to graph indexing and the UI. The graph indexer prompts for its connection settings.

`download-model` retrieves the pinned MiniLM revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41` from [Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/tree/1110a243fdf4706b3f48f1d95db1a4f5529b4d41) into your checkout. Indexing then uses that local cache. Chroma and Node2Vec assets are rebuilt under your `work/`; they are not copied from the author's installed environment. Keep the checkout in place after building indexes, or rebuild them after moving it, because new index manifests bind to their actual local paths.

Open `http://127.0.0.1:8501`. Enter your own database credentials in Connection settings. Try:

> According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.

Text-only questions need the text index and Ollama. Graph-only needs the imported database and Ollama. Combined mode needs text plus graph; full hybrid also needs the graph-vector index. Missing prerequisites produce an error, with no silent fallback. New query records are saved under your `work/application_qa/`.

### What the portable source adapter does

`data/portable/development_sources.json` packages the exact validated development documents, source windows, accepted original assertions, identities and ATT&CK references. Its manifest records its checksum and original scope fingerprint. `portable_sources.py` checks its source offsets, assertion support, scope identity and directed projection. It supplies that complete scope to the original application/retrieval/indexing code, so startup does not need omitted historical extraction working folders or follow old provenance paths. Frozen generation/retrieval source files and experiment outputs are unchanged. This restores the accepted graph; it does not claim a fresh extraction from raw advisories.

### Live HTTP API

Complete the live build above before querying. In the same application environment:

```powershell
.venv-live\Scripts\python.exe -m pip install -r requirements-api.txt
.venv-live\Scripts\python.exe -m pip check
.venv-live\Scripts\python.exe portable.py api --prompt-password
```

The optional password prompt does not echo or put the password in command-line arguments. Text-only queries do not need Neo4j credentials, so `portable.py api` also works. To select a different database use `--uri`, `--user` and `--database`. `--port` defaults to 8000. Environment alternatives are `THREATWEAVE_NEO4J_URI`, `THREATWEAVE_NEO4J_USER`, `THREATWEAVE_NEO4J_DATABASE` and `THREATWEAVE_NEO4J_PASSWORD`; command-line connection options override those settings when explicitly supplied. Keep credentials out of source files and query bodies.

Open `http://127.0.0.1:8000/docs` to submit a request, or use PowerShell:

```powershell
$queryBody = @{
    question = 'According to CISA, how do Rhysida actors use valid accounts (T1078)?'
    mode = 'hybrid'
    corpus_version = 'cisa-selected-2026-10-03'
} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/query -ContentType 'application/json' -Body $queryBody
```

Allowed modes are `text_only`, `graph_only`, `hybrid_no_node2vec` and `hybrid`. The request and response use the original strict Pydantic contracts, and the engine saves new development query records separately from frozen results. The engine is shared within one API process and serializes queries. Stop with Ctrl+C to close its database and HTTP clients.

`/health` reports engine initialization, not independent database/model reachability. Each query verifies the prerequisites for its selected mode. Invalid request fields return 422; corpus/configuration conflicts return 409; unavailable services or missing/unverified indexes return 503; retrieval/generation failures return 502; propagated timeouts return 504. Public error bodies omit raw driver/model exceptions and credentials. A missing prerequisite never silently changes the retrieval mode.

The launcher binds to loopback only and serves **`live_api:app`**. Direct equivalent: `python -m uvicorn live_api:app --host 127.0.0.1 --port 8000`. The original `api.py` remains the frozen design-contract artifact. Do not use `uvicorn api:app` for live queries. `requirements-api.txt` deliberately pins a compatible FastAPI/Starlette/Uvicorn combination and can change those versions in the application environment; it does not replace the separate Windows application lock or the frozen RAGAS environment.

API regression checks (no live services needed):

```text
python -m unittest discover -s tests -p test_live_api.py -v
```

## 5. New experiments versus the original measured experiment

A fresh extraction, new model-generated answers, automatic judging and new human ratings constitute a **new experiment**. Preserve its model/dependency identities, hardware, prompts, seeds, sources, split, validation failures and raw outputs separately. Do not overwrite the original frozen cohort. The historical collection and evaluator tools are retained as research records; they are not a one-command portable regeneration pipeline. The independently runnable workflows provided here are the saved-statistics analysis, saved UI replay and fresh development application build.

## Troubleshooting

- A clone/ZIP download is denied: check the public repository URL and your network connection.
- `python` is missing or is the wrong version: install Python 3.12 and use its interpreter (`py -3.12` on Windows).
- `check-sources` fails: use a clean checkout; do not edit the frozen bundle, configuration or source snapshots.
- Model cache missing: run `portable.py download-model` in the same checkout and environment before indexing.
- Connection refused: start your local service and check the host/port/password you selected.
- Graph import says the database is nonempty: choose a new empty database. The importer does not erase one for you.
- Stale or relocated index: rebuild the text/graph indexes in the current checkout using the same environment.
- Need a service-free check: run `python -S reproduce_results.py`, or use the saved demonstration.

Historical dated setup/checkpoint documents describe the author's original machine and may contain old paths/statuses. Use this guide for an independent installation. See `REPRODUCTION_VERIFICATION.md` for exactly what was tested.
