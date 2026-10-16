# ThreatWeave final submission

Stephen Butler · CS 6338 · October 16, 2026

The required local deliverables are ready:

- ThreatWeave_final_report.pdf: final 14-page report with methods, measurements, paired comparisons and limitations.
- ThreatWeave_final_report.md: editable report source.
- ThreatWeave_final_slides.pptx: final 16-slide presentation with editable tables/charts and source notes.
- ThreatWeave_demo.mp4: 5-minute-34-second walkthrough of authentic saved application states, with synthetic narration and selectable English captions.
- ThreatWeave_demo_captions.srt and ThreatWeave_demo_transcript.md: accessible video companions.
- ../ThreatWeave_submission_v2.zip: source/evidence archive, including these deliverables, completed ratings, frozen source/benchmark files, original experiment/scoring records and analyses. The adjacent receipt records the archive checksum.

The report documents negative results: extraction F1 is 0.117 against a proposed 0.80, and full hybrid's available human completeness gain is 0.111 points against a proposed 0.50. The joint QA target is not met. Missing outcomes remain explicit. General superiority is not established.

Both human review exports are complete. The same author performed the secondary delayed rescore. There was limited AI assistance for review questions. It measures within-reviewer consistency rather than independent inter-rater reliability. No further ratings are needed.

## Reviewing the evidence

The authoritative human analysis is work/human_scoring_analysis/20261016T174034Z-7c181a33. The combined results are work/final_completion/submission_results.json. Extraction results are in work/extraction_scoring_analysis/20261016T171118Z-dc75fabd. Automatic analysis is in work/final_scoring_analysis/20261016T075220Z-1e84d02c. The archive manifest binds each included file to its SHA-256 checksum.

With the documented Python dependencies installed, analyze_extraction.py and analyze_human_reviews.py reconstruct analyses from saved records without new model calls. The human runner requires both completed rating exports and the method declaration. Absolute historical paths and receipt hashes refer to the original S:/ThreatWeave workspace; a relocated installation may require explicit path arguments or path adaptation. This archive is not an installed portable runtime and does not include model weights, vector caches or a live database.

## Submission boundary

The video demonstrates a labelled saved-run replay, not new live generation. The report and slides disclose this distinction. Files are prepared locally; nothing has been uploaded, pushed to GitHub or submitted to the course system by the assistant. Use these final files instead of the earlier DRAFT copies.
