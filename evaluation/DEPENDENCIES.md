# Frozen evaluator dependencies

**Runtime installation completed October 16, 2026:** `work/evaluation_setup_runs/20261016T052704Z-bf84a7f1` confirms the separate Windows x64 Python 3.12 environment, no broken requirements and successful pinned adapter imports. [The next step is a synthetic live evaluator probe](../docs/ThreatWeave_evaluator_probe_step.md). The installation procedure and original design adapter below remain preserved; the probe's additional local-cache, fixed-temperature, completion and recording safeguards are implemented separately in `judge_runtime.py`.

The evaluator targets **Windows x86-64 and Python 3.12**. Its exact direct pins are:

| Package | Version |
|---|---|
| RAGAS | 0.2.15 |
| langchain-ollama | 0.2.3 |
| langchain-huggingface | 0.1.2 |
| sentence-transformers | 3.4.1 |

`requirements.lock.txt` also pins every resolved transitive dependency and includes
distribution SHA-256 hashes. It was resolved with uv 0.12.9 on October 5, 2026.
Use a separate evaluator environment so these pins do not change the application
dependency draft. Other Python versions and operating systems require a new lock.

```text
python -m venv .venv-eval
.venv-eval\Scripts\python.exe -m pip install --require-hashes -r evaluation/requirements.lock.txt
```

`run_ragas.py` rejects mismatched direct versions. `build_local_evaluators()` wraps
local Ollama Llama 3.1 8B and normalized MiniLM embeddings. Both retrieval and
evaluation select MiniLM revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`.
The Ollama model digest must still be recorded before experiments; it depends on
the installed local model. Gold reference answers are provided only to the evaluator.

The dependency solver passed and the chosen RAGAS wheel's API exports were checked.
This is a reproducible software configuration, not evidence of a completed model
benchmark. Installing the full environment, downloading model weights, and live
Ollama/evaluator integration remain runtime validation work.

Sources: [RAGAS 0.2.15 package](https://pypi.org/project/ragas/0.2.15/),
[versioned model-adapter documentation](https://docs.ragas.io/en/v0.2.15/howtos/customizations/customize_models/).
