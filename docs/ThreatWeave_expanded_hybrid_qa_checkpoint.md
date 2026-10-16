# Expanded full-hybrid QA development checkpoint

AI-assisted source review of run `work/hybrid_qa/20261015T043615Z-462852fb`. The [generated run review](ThreatWeave_hybrid_qa_20261015T043615Z-462852fb.md), original prompts, responses, evidence and receipts remain unchanged. Their semantic-review status remains pending human verification. This checkpoint records development findings, not human ratings or held-out scores.

## Processing and evidence checks

All three cases produced non-abstaining answers on their first generation attempt, with zero execution failures or repairs. Each run record reports live Neo4j retrieval and a successful graph-freshness check against the fitted projection. The assistant reviewed saved files without calling Neo4j or Ollama.

| Case | Graph paths | Selected text hits | Source passages | Context bytes / 3000 | Output tokens | Case time |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Raccoon Stealer / web session cookies | Four three-hop paths | 3 | 12 | 2814 | 278 | 8.824 s |
| Rhysida actors / valid accounts | Five two-hop paths | 4 | 15 | 2954 | 341 | 5.031 s |
| ALPHV affiliates / AnyDesk and Mega sync | Two one-hop paths | 3 | 6 | 2306 | 253 | 3.633 s |

Times include per-case retrieval, fusion, packing and generation, excluding initialization. They are single observations, not final benchmark latency averages. Selected text-hit counts describe final fusion, rather than all initially retrieved text candidates.

The independent offline audit at `work/qa_review_checks/20261015T043756Z-98490f2a/audit.json` passed: all 33 supplied passage texts and offsets match the freshly verified frozen source documents, source URLs match, all 16 claims have valid citation bindings, saved raw responses reproduce the displayed answers, all three prompt hashes match, and the shared questions/generator/options match current configuration. These checks establish integrity and structural validity; they do not establish semantic correctness.

## Source review findings

### Raccoon Stealer

The observation about stolen login credentials, browser history and cookies is supported directly by CISA passage E4. E2 and E3 are report/section context and add no behavioral support. The answer keeps CISA observation citations separate from ATT&CK guidance citations.

All four supplied mitigation identities and IDs appear with their corresponding identity/guidance citation pairs: Restrict Web-Based Content M1021 (E5/E6), User Training M1017 (E7/E8), Multi-factor Authentication M1032 (E9/E10), and Update Software M1051 (E11/E12). They are the supplied subset, not an exhaustive catalog of T1539 mitigations.

The M1032 claim drops the source's proxy-method restriction and describes prevention of session-cookie theft generally. This broadens the source's claim. It also omits the separate Conditional Access/Token Protection guidance about binding tokens to their original device and user. M1021 omits browser security settings and extension restrictions; M1017 compresses domain-mismatch phishing guidance into general phishing awareness. M1051 retains the update action and reduced vulnerability risk. The answer therefore has supported core observations and mitigation coverage, with material scope/detail limitations.

### Rhysida actors

CISA E1 supports the observed use of compromised valid credentials to authenticate to internal VPN access points. The answer preserves the actor qualifier and T1078, although it compresses the source's description of commonly observed behavior.

Five mitigation identities, IDs and practical actions are supported by their cited pairs: Application Developer Guidance M1013 (E4/E5), Account Use Policies M1036 (E6/E7), Active Directory Configuration M1015 (E8/E9), Password Policies M1027 (E10/E11), and User Training M1017 (E12/E13). The answer's M1027 summary omits immediate post-installation/pre-production default-credential changes, periodic properly secured SSH-key updates and the personal-versus-work password-reuse context. The M1017 wording compresses the explicit instruction to accept only valid push notifications.

User Account Management M1018 is also supplied in E14/E15, including account auditing and removal/deactivation of accounts no longer needed, but is absent from the answer. This is a generation-coverage omission despite available evidence. Six mitigation identities are supplied; the answer covers five. The answer separates CISA observations from reference guidance, but does not cover all supplied guidance.

### ALPHV affiliates

CISA E1 supports deployment of AnyDesk, Mega sync and Splashtop after network access, in preparation for data exfiltration. The answer retains the affiliate qualifier and purpose, without asserting a new technique or mitigation. The separate Mega.nz/Dropbox statement is supported by E5; it does not establish that Mega sync and Mega.nz are identical entities.

The first four claims substantially repeat the same observation rather than combining it into one concise statement. Their wording differs enough to pass the current exact-normalized duplicate check. This is a semantic repetition limitation, not a new execution failure. E2/E3 provide report/section context and are unnecessary alongside the direct observation passage. The fifth claim adds supported but less directly requested behavior.

## Retrieval interpretation

The graph branch supplied the CISA observations missing from the first two text-only top-five smoke searches. Both source types reached the full-hybrid evidence context. This demonstrates coverage in these saved contexts; it is not a causal quality comparison with generated text-only answers, which remain pending for this expanded scope.

| Case | Base candidates | Neighbor-matched expansion candidates | Deduplicated merged candidates |
| --- | ---: | ---: | ---: |
| Raccoon Stealer | 17 | 17 | 17 |
| Rhysida actors | 9 | 5 | 9 |
| ALPHV affiliates | 2 | 0 | 2 |

Expansion added no unique candidate paths beyond the base sets in these cases. Neighbor priority can still affect selection/order under packing limits; the matching no-Node2Vec run is needed to assess that effect. Similarity is not fact evidence, and these counts do not establish a Node2Vec quality benefit.

## Matching settings and next step

Later checkpoint: [matching text-only QA completed](ThreatWeave_expanded_text_qa_checkpoint.md). It produced unsupported incident claims where its contexts lacked CISA observations. [Graph-only QA](ThreatWeave_expanded_graph_qa_step.md) is next. The settings and original next-step statement below remain as run history.

- Generator: `development-shared-cited-generator-v2`; temperature 0, context 8192, output limit 700, one allowed repair.
- Model: `llama3.1:8b`; digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`.
- Shared development scope: `920801a20df03fcdb45d29534ef9b14b169f3f6ab22f4be1785f375f0b6d1b7c`.
- Text index: `607e1e265093bfc94fa6d7f4ddcb5317bc722705859ad6c5d0440ef8279adc5f`.
- Graph index: `da85cd77a7811edf7d5ca4e9db82a2a6b1669ef614f9d0115483bbb3124a8fc0`.
- Projection: `3b5d61276de1b58773079a2c80dcac52d1c00eeeafbb73c68d3956e244678982`.
- Full-hybrid configuration: `e58ce56404aea565cceb8625ae90c215ae416dcf89e525fc38c980f52d787250`.

Keep these questions, sources, model and shared generator unchanged while collecting the other three modes. [The next run is the matching text-only demonstration](ThreatWeave_expanded_text_qa_step.md). Graph-only and hybrid without Node2Vec follow. Preserve the observed limitations for comparison before considering generator changes. No implementation changed during this review; the prior 175-test result remains the latest suite result. Final evaluation, broader extraction, human review and application integration remain unfinished.
