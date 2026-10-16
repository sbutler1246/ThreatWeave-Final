# Assignment alignment

Source: the twelve assignment/rubric screenshots supplied in this chat.

| Category | Points | Design coverage | Checkpoint status |
|---|---:|---|---|
| Architecture and data flow | 25 | Section 2 diagram, offline/online phases, inputs/outputs/protocols, error and version behavior | Designed; adapters planned |
| Extraction and entity resolution | 20 | Sections 3–4 domain schema, confidence review, chunking, exact spans, few-shot prompts, ID/name/alias resolution | Parser/models/resolver included and unit tested |
| Embedding and hybrid retrieval | 20 | Sections 5–6 Node2Vec objective, parameters, vector separation, query-to-node bridge, bounded retrieval and fusion | Designed; service integration planned |
| Evaluation and benchmarks | 20 | Section 7 pre-fusion precision/recall/F1, RAGAS configuration, human 1–5 rubric, controlled four-mode evaluation | 146 author-verified gold triples across 39 complete scopes; all 61 QA references author-validated; selected final set is 20 questions with 8/8/4 mix; evaluator dependencies hash-locked and API checked; performance evaluation remains planned |
| Repository and data models | 15 | Section 8 Pydantic snippets/composition diagram, API contracts, schema/init scripts | Published GitHub checkpoint and file contents verified October 5, 2026; live Neo4j integration remains planned |

The assignment appendix is a reference template to adapt, not an instruction to change the approved project to biomedical data or OpenAI embeddings. Native Neo4j vector scripts are optional; Chroma is the committed index choice.
