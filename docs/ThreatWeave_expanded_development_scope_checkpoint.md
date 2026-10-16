# Expanded development scope and index preparation

Later checkpoints: [the expanded text index completed](ThreatWeave_expanded_text_index_checkpoint.md) with 95 verified chunks/vectors, and [the expanded graph index completed](ThreatWeave_expanded_graph_index_checkpoint.md) with 75 nodes, 102 directed facts and 75 verified vectors. The saved-index full-hybrid preview passed. [Fresh expanded QA](ThreatWeave_expanded_qa_step.md) is next. The source-scope preparation and original next-step instructions below remain as history.

October 14, 2026 (America/Chicago). The mitigation receipt at `work/corpus_pilot_mitigations/20261015T041247Z-529903c7/import_receipt.json` records successful verification of **55 direct ATT&CK reference assertions**, **72 source-reference combinations** and **six same-window three-hop chains**. The transaction took **3.314110 seconds**, including source/reference/path verification and any driver retries, excluding preparation/connectivity. Counts include reused graph records. This is a small development transaction observation, not full-corpus throughput, incident effectiveness or a final model-quality result. Human verification remains pending.

## Shared expanded evidence

All four development retrieval modes now derive their source pool from the same expanded scope: the original six CISA parents plus the ten reviewed extraction windows, and the union of their direct frozen ATT&CK references. The new scope is available only after checking the pinned completed source and mitigation import receipts, their saved prepared records, the source review selection and frozen sources/catalog.

| Prepared item | Count |
| --- | ---: |
| CISA source parents | 16 |
| Distinct CISA reports | 6 |
| Direct ATT&CK reference parents | 58 |
| MiniLM retrieval children | 95 |
| Expected graph domain nodes | 75 |
| Expected directed domain facts | 102 |
| Extracted-origin domain facts | 44 |
| Fused-origin reference facts | 58 |

The reference union contains the pilot's 55 relationships plus three earlier T1046 references; earlier T1219/T1562.001 references are reused. Text indexing uses exact source passages and normalized STIX descriptions, not generated fact statements or benchmark answers. The graph admits only the pinned Supported assertions for the ten new windows; the three uncertain/conditional candidates remain excluded. Local actor restrictions and software identities remain distinct where source evidence does not justify merging them.

Review dispositions and reasons are validation/provenance metadata. They are not supplied as embedding text, generation context or similarity scores. Gold triples and QA reference answers are not inputs, and benchmark assignments remain unchanged.

## Retrieval and index safeguards

New-window assertions must match their exact reviewed IDs, source evidence and provenance. A different assertion with the same endpoints is not automatically accepted. Human-verified status may be preserved; rejected assertions are excluded. The graph query also restricts nodes and seed entities to the approved domain pool, while exact source checks still determine whether each candidate path is valid.

Question seeding now keeps the longest name at an overlapping occurrence. For example, Rhysida inside Rhysida actors does not independently force a ransomware-software seed into an actor question. A separate explicit software mention elsewhere in the question still survives. New-window aliases come from validated literal source occurrences, rather than first/last-line assumptions intended for the original short table rows.

Graph projections retain the new assertions' required source-review provenance so a saved Node2Vec projection can be checked again during full-hybrid retrieval. The original six-scope regression fixtures remain independently tested. The expanded scope has a distinct identity and text fingerprint, preserving earlier saved index collections. Graph freshness checks continue to require a projection matching the accepted source pool; an older graph-vector index must be rebuilt before expanded full-hybrid use.

Scope SHA-256: `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c`.

Prepared text fingerprint: `607e1e265093bfc94fa6d7f4ddcb5317bc722705859ad6c5d0440ef8279adc5f`.

The graph source-fixture preview contains 75 nodes and 102 directed/undirected edges, with connected components of sizes 71, 2 and 2. This is an expected source-derived projection, not a fresh live Neo4j read or a fitted graph index. Its fixture hash must not be treated as the eventual live projection hash: source-fixture assertion IDs and live imported IDs can differ.

## Offline checks

All **175 offline tests pass**. New tests cover the expanded approved scope, exact text/graph parent parity, complete source/reference identities, supported-only assertion IDs and review metadata, nested actor/software names, preserved independent mentions, saved graph-projection provenance, scope revision identities and incomplete mitigation receipts. Existing six-scope regression checks and all extraction, ingestion, fusion, retrieval and generation tests also pass. Tests use service fakes; the assistant made no live Ollama/Neo4j calls or installations.

The actual cached-tokenizer text preview passes with **95 retrieval children**, a maximum of **240 WordPieces** and **1000 characters** including inherited source context. Full-parent tokenization is used only to find exact split offsets; embedding bounds apply to the resulting children. The actual graph preview passes source/identity/projection checks without fitting or writing vectors. Neither preview creates a production index.

The saved offline evidence audit is `work/development_scope_checks/20261015T042219Z-aaaa5739/preview.json`. It records scope/text/projection fingerprints, source parent IDs, the three new development questions, exact evidence bundles, context and packing statistics. No generated answers or live database presence are claimed.

| New source-only graph preview | Selected evidence | Context |
| --- | --- | ---: |
| Raccoon Stealer information theft and supplied cookie-theft mitigations | Four three-hop paths | 2795 UTF-8 bytes |
| Rhysida actors using valid accounts / T1078 and supplied mitigation guidance | Five two-hop paths | 2699 UTF-8 bytes |
| ALPHV Blackcat affiliates using AnyDesk and Mega sync before exfiltration | Two one-hop paths | 415 UTF-8 bytes |

The conservative context cap remains 3000 UTF-8 bytes, within the configured evidence-token budget. The first two previews select bounded subsets of the available mitigation references; they do not enumerate every applicable reference. All source passages retain exact document offsets. The shared cited generator remains v2, with unchanged model settings, Node2Vec parameters and retrieval limits. The new questions are source-based development smoke checks, not held-out questions or reference answers. Earlier answer demonstrations used different evidence/questions and are not directly comparable to the forthcoming expanded runs.

## Next step

Rebuild the text index with the cached MiniLM model:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\index_development_text.py"
```

Ollama and Neo4j are not required for this command. It creates the expanded fingerprinted collection, verifies all 95 stored records/vectors and runs the three updated text-retrieval smoke questions. It preserves prior collections and saves its receipt under `work/text_index_runs` and review directly in `docs`.

After that succeeds, rebuild the live-source Node2Vec index, then run matching fresh checks for all four QA modes. Expanded text indexing, live graph projection/fitting and expanded generated answers remain pending. The pilot still covers only ten of 54 prepared development extraction windows. Broader extraction, overlap/resource measurements, application UI and controlled held-out evaluation remain unfinished.
