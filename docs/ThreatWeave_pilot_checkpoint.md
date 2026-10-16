# ThreatWeave three-hop pilot checkpoint

Reviewed on October 13, 2026. This is a development checkpoint, not the final technical report or an evaluation of the complete system.

## Confirmed live result

Run: `S:\ThreatWeave\work\pilot_qa\20261013T071147Z-93f4a355`

The saved run and answer records confirm that the graph-only retriever returned three paths, each with three directed relationships:

`LockBit Affiliates → USES → Advanced Port Scanner → USES_TECHNIQUE → Network Service Discovery (T1046) → MITIGATED_BY → Mitigation`

The final node differs between paths:

| ATT&CK ID | Mitigation | Citation |
| --- | --- | --- |
| M1030 | Network Segmentation | E4 |
| M1031 | Network Intrusion Prevention | E5 |
| M1042 | Disable or Remove Feature or Program | E6 |

Six source passages were returned: the CISA row, its caption and headers (E1–E3), plus three normalized ATT&CK structured records with relationship descriptions (E4–E6). The ATT&CK citation text is a normalized representation of STIX fields and their exact relationship description; it is not a quotation of a mitigation webpage.

The model was `llama3.1:8b`, digest `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`. The prompt version was `graph-pilot-qa-v3`, and the reference release was Enterprise ATT&CK 17.1. Logged execution time was approximately **18.50 seconds** for this single run. The timer excludes interactive credential entry and initial source preparation. This is not a mean latency, an isolated LLM generation time, or a benchmark result.

## Answer review

The answer identifies the actor qualifier, tool, technique ID, network scanning, and finding open TCP/UDP ports for exploitation. It lists all three retrieved mitigation names and IDs, each with the corresponding ATT&CK citation. Those statements are supported by the supplied development evidence.

The answer remains incomplete for the requested question: it does not explain the practical guidance of each mitigation. The retrieved sources contain guidance on segmenting networks, using intrusion detection/prevention systems, and closing unnecessary ports/services, but those details do not appear in the generated answer. It should also explicitly introduce the mitigation statements as ATT&CK reference guidance.

This demonstrates successful retrieval and citation mapping together with an observed answer-completeness limitation. A structurally valid response with known citation IDs does not establish complete or fully faithful question answering. Do not assign extraction F1, hallucination reduction, or overall system accuracy from this single example.

## Provenance and scope

The CISA extraction is confined to development scope `AA23-165A:table4:row02`. The ATT&CK importer reads the frozen structured snapshot, maps mitigation-to-technique `mitigates` relationships into technique-to-mitigation `MITIGATED_BY` edges, and retains STIX IDs, release, source spans and hashes. These reference assertions have `origin=fused`; they must remain separate from extracted-origin predictions in extraction scoring. ATT&CK reference guidance does not establish incident-specific deployment or effectiveness of a mitigation.

The mitigation import receipt confirms three reference relationships and three verified three-hop chains. Repeated imports use stable IDs. Sources were checked against frozen records; the importer does not mark them as human verified.

Earlier GDS WCC output showed one component of three entities and 12 ms compute time **before mitigation import**. That result concerns the smaller two-hop graph, not the current six-entity graph or full intended corpus.

## Work remaining for submission

1. Generalize ingestion and retrieval beyond this single source row. Exercise additional development scopes and multiple reports while preserving evaluation split boundaries and source provenance.
2. Complete the planned structured ATT&CK integration, text retrieval, hybrid retrieval and Node2Vec branch. The current script is a graph-only pilot with an explicit source scope.
3. Freeze development choices and run the approved extraction and question-answering evaluation. Keep held-out reference answers outside generation prompts and ingestion inputs.
4. Integrate a reproducible end-to-end entry point and document setup, model/plugin versions and test results in GitHub.
5. Complete the 8–10 page technical report, 10–12 slide deck and 5–7 minute demonstration using measured results and clearly reported limitations.

Preserve the pilot run folders, including earlier incomplete answers, as development evidence. Do not treat them as held-out evaluation runs.
