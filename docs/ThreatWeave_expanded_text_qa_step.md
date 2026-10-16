# Matching expanded text-only QA

Completed: [the expanded text-only run and source review](ThreatWeave_expanded_text_qa_checkpoint.md) record three non-abstaining answers without execution failures, including unsupported incident claims in the first two answers. [Matching graph-only QA](ThreatWeave_expanded_graph_qa_step.md) is next. The instructions below preserve the preceding checkpoint.

The expanded full-hybrid run completed all three cases without execution failures. [Its source review](ThreatWeave_expanded_hybrid_qa_checkpoint.md) records supported observations, a broadened Raccoon mitigation claim, omitted Rhysida account-management guidance and repetitive ALPHV claims. Human verification remains pending.

Run the matching text-only condition next, keeping Ollama running:

```powershell
& "C:\Users\djfro\.venv\Scripts\python.exe" "S:\ThreatWeave\text_qa.py" --demo
```

This needs no Neo4j connection or password. It uses the verified expanded text index, the same three questions and shared v2 cited generator. Results save under `work/text_qa`, with a generated review directly in `docs`. Preserve the current model and generation settings so its recorded digest matches the expanded full-hybrid run.

The assistant's fresh `text_qa.py --demo --preview` passed without calling Ollama: Raccoon selected five text chunks and ten passages within 2489/3000 context bytes; Rhysida selected five chunks and ten passages within 1880/3000 bytes; ALPHV selected four chunks and six passages within 2971/3000 bytes. All have zero graph paths. This checks local retrieval readiness, not generated answers.

The first two top-five text smoke searches contained ATT&CK reference guidance but omitted CISA observation passages. Check whether generated answers acknowledge that missing incident evidence rather than inventing behavior. For ALPHV, check the stated purpose, affiliate attribution, citations and repetition. Review saved evidence as well as the displayed answers: successful processing is not a quality score.

Matching graph-only and hybrid without Node2Vec runs remain next after this baseline. Earlier demonstrations used different questions/source scope and remain historical. Do not supply benchmark gold or reference answers to the pipeline, or change generator/retrieval settings between matching runs. Broader corpus processing, the application and controlled final evaluation remain unfinished.
