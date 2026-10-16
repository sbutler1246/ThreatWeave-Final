# Llama source-tokenizer check

Status: ready

Reads the existing Ollama model vocabulary; model weights are not loaded by the checker.
Raw Ollama probes test token-count agreement and source round trips. This does not validate extraction quality.

Records: S:\ThreatWeave\work\extraction_tokenizer\20261014T064015Z-126bb1e2

Model digest: 46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e

- Probe 1: local source tokens 17; expected raw count 18; reported 18; passed.
- Probe 2: local source tokens 19; expected raw count 20; reported 20; passed.
- Probe 3: local source tokens 486; expected raw count 487; reported 487; passed.

Full-corpus chunking and the five-report extraction timing/overlap pilot remain pending.
