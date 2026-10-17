# Live API verification

October 16, 2026 (America/Chicago). This is an application integration addition after the frozen experiment. It does not change the original 240 outcomes, labels, identities, fitted evaluation assets or reported statistics.

## Implemented path

`python portable.py api` launches `live_api:app` on loopback. Startup constructs the existing `ApplicationEngine` with the portable source provider and local connection settings. Queries use the four original retrieval modes and strict request/response contracts. Shutdown releases database and HTTP clients. Connection credentials can be supplied by environment or a hidden password prompt. Error bodies are sanitized and preserve distinctions between configuration conflict, missing prerequisites and generation failure.

The original `api.py` is preserved as the design-contract artifact, with its original manifest checksum. It is not the live server entry point. The new entry point resolves the missing engine-injection concern without rewriting experimental source artifacts. [Setup and request example](../REPRODUCE.md#live-http-api).

## Checks completed

- Eight HTTP adapter tests passed, covering all four modes through the real `ApplicationEngine` with simulated services, strict request validation, corpus mismatch, abstention, sanitized failure statuses, startup/shutdown and the supported launcher.
- Thirteen existing application tests and five portable-source/path tests passed: 26 targeted checks in total.
- FastAPI 0.115.12, Starlette 0.46.2 and Uvicorn 0.34.2 were installed in a separate workspace dependency folder over the existing reproduction environment. HTTPX was 0.28.1 and Pydantic was 2.13.5. `pip check` reported no broken requirements. This was not a second clean dependency installation.
- A Uvicorn server on an ephemeral loopback port accepted actual HTTP requests using the existing relocated development checkout's rebuilt MiniLM/Chroma and Node2Vec assets, the disposable Neo4j database and local Ollama. The app was created with `create_live_app(lambda: build_engine(relocated_checkout))`; the preserved source directory and asset paths are in the receipt. This uses the new HTTP routes and the original application engine; it does not replace the frozen experiment or claim a new independent machine reproduction.

| Mode | HTTP | Abstained | Claims | Evidence passages |
|---|---:|---|---:|---:|
| Text only | 200 | No | 5 | 11 |
| Graph only | 200 | No | 6 | 13 |
| Hybrid without Node2Vec | 200 | No | 6 | 15 |
| Full hybrid | 200 | No | 6 | 15 |

All four requests used the documented Rhysida development question. Health and OpenAPI also returned successfully. Responses and original per-query records are preserved in [the four-mode live receipt folder](../outputs/api_verification/20261017T030754Z/receipt.json). The earlier text-only check remains separately preserved. HTTP success and contract validation do not establish semantic accuracy or general benchmark performance.

The HTTP server stopped and its engine was released after the check. The disposable graph database was also stopped; its test port was verified closed. The existing Ollama service was left as it was.

The workflow definition now runs the lightweight API tests on Windows and Linux. The checks recorded here were completed locally before publication; remote workflow status must be checked separately. The local API regression tests, live smoke check, dependency check and diff-whitespace check passed. Original manifest-tracked files remain unchanged except the already permitted adapted publication README.

## Remaining scope

The new API is a local development service. The single-question four-mode smoke check does not cover every question, concurrent load, network deployment or independent semantic review. Software disambiguation remains the original exact resolver. Advanced contextual disambiguation was not implemented because of project time constraints and is documented as [a limitation and future-work item](ThreatWeave_software_disambiguation_plan.md), not a pending deliverable for this completed submission.
