# Application setup checkpoint

October 15, 2026. Operator setup run `work/application_setup/20261015T073023Z-758d41cf/setup_receipt.json` is **ready**. The constrained installation succeeded, all existing package versions were preserved, and all three real Streamlit AppTest scenarios passed in 0.932 seconds according to the operator's output. These checks use synthetic evidence and forbid real service-adapter construction; they are not live query or browser-visual checks.

The assistant independently compared the receipt with the currently installed environment: all **108 previously installed packages** retain their recorded versions, **10 packages were added**, Streamlit is exactly **1.66.0**, and the receipt's `changed_existing_packages` object is empty. Every version in its saved post-install snapshot matches the current environment. This read-only verification made no Neo4j or Ollama calls and did not reinstall packages.

The checks cover initial page loading without services, a synthetic graph-only query with history/source/graph sections and disconnect, and an index-stage failure without a fabricated answer. Earlier offline engine tests cover all four mode adapters, empty-evidence abstention, source/index/model changes and privacy boundaries. Browser rendering, graph interaction and live application queries remain pending.

[Launch the application next](ThreatWeave_application_launch_step.md). The launcher serves only localhost, disables usage telemetry and does not submit a question on startup. A single live application smoke query will verify the UI-to-retrieval-to-generation path; this is separate from the already completed four-mode comparison. Its imperfect generated answers and all previous run records remain preserved.

Broader source extraction/ingestion, human semantic verification, controlled held-out evaluation and integration beyond the local interface remain unfinished. The application still uses the unchanged shared generator and limited development source pool.
