# Current report for submission

October 16, 2026. Use [the revised 15-page PDF](ThreatWeave_final_report_revised.pdf) and [its editable Markdown source](ThreatWeave_final_report_revised.md) as the current report.

## What changed

Appendix B explicitly states that advanced automated disambiguation for software entities outside ATT&CK was not implemented because of project time constraints. It describes the current ID/name/verified-alias approach, its limitations, and the separately evaluated future work that would be needed to add contextual matching.

The appendix also documents the later live HTTP API integration, all four successful live development requests, 26 targeted checks, and the distinction between those integration checks and the original frozen benchmark. The cover and Section 8 point readers to the appendix.

Every original table and the Sections 6-7 measured-results narrative are unchanged. The new text does not claim better extraction performance, revised QA scores or independent semantic verification.

## Preserved original files

The [original 14-page PDF](ThreatWeave_final_report.pdf), [original editable source](ThreatWeave_final_report.md), original deliverable checksums and source/evidence ZIP remain byte-for-byte unchanged. The original SUBMISSION_GUIDE.md describes that archived snapshot. The ZIP still contains the original report; download the revised PDF separately or use the current repository checkout for the updated documentation and API.

[REPORT_REVISION.json](REPORT_REVISION.json) records the original and revised report hashes, page count, change description and source of the separate API verification evidence. It supplements the original DELIVERABLES_SHA256.json rather than replacing it. The slide deck, video and original experiment outputs are unchanged.
