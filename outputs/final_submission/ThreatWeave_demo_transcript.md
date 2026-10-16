# ThreatWeave demo transcript

Synthetic narration over authentic captured application states. Saved-run replay, not a new live model/database session.

## ThreatWeave

This is ThreatWeave, Stephen Butler's cybersecurity Graph RAG project for CS sixty-three thirty-eight. This demonstration uses real saved application outputs from October fifteenth. It makes no new model or database calls. Synthetic narration accompanies captured application states so the evidence workflow remains reproducible.

## A question with cited claims

The question asks how Rhysida actors used valid accounts for access and asks for separate mitigation guidance. The saved graph-only result identifies compromised credentials used at internal VPN access points. Each claim lists the evidence identifiers supplied to the model. The interface warns that a citation does not by itself establish correctness.

## The CISA observation

Opening evidence E one reveals the exact CISA passage, its advisory identifier and normalized source offsets. Here the source explicitly connects Rhysida actors, compromised valid credentials and internal VPN access. This lets the analyst check a particular incident observation instead of assuming that a generally plausible answer is supported.

## Separate ATT&CK guidance

Reference guidance has a different label. This passage comes from the frozen Enterprise ATT and CK seventeen point one snapshot and describes secure handling of credentials in applications. The relationship is a reference recommendation. It does not prove that this mitigation worked against Rhysida in the reported incident. Keeping these source roles separate is a core project requirement.

## A directed query graph

The query graph displays the accepted directed paths actually returned for this question. Selecting Valid Accounts exposes the technique identity and type. Actor-to-technique and technique-to-mitigation links remain visible as different relationships. The graph is a saved query-time snapshot rather than a continuously refreshed picture of the database.

## Graph inspection controls

The graph supports zoom, reset and panning. This captured state follows the zoom-in control. These controls help inspect a returned path, but they do not validate its meaning. The source passages remain necessary for checking whether the path supports the wording of the generated answer.

## The saved full-hybrid run

The sidebar can switch to the preserved full-hybrid run of the same question. Full hybrid combines text retrieval and structural paths with candidates proposed by Node to Vec graph neighbors. The displayed answer and timestamp belong to that original run. This replay is not a new performance measurement or a live benchmark query.

## Hybrid paths remain inspectable

The hybrid result also exposes its returned graph. Graph similarity only proposes candidates. An accepted directed path with source evidence must support a factual claim. The replay shows this distinction without changing any frozen question, source, model output or index. Additional live text-only and ablation interface flows remain unverified.

## Run details and export

Run details retain the model digest, evidence budget and retrieval metadata. The actual evidence cap is three thousand UTF-eight bytes, even though the original design discussed tokens. The download control exports the structured displayed run. Graph inspection can add display-position metadata to entity records. The saved answer and evidence remain unchanged. Original pending-review notices describe the October fifteenth development checkpoint.

## Evaluation preserves failures

The frozen evaluation contains twenty questions, four conditions and three repeats, giving two hundred forty measured outcomes. Two hundred ten returned valid non-abstaining answers, fifteen abstained and fifteen failed generation validation. Valid here refers to output validation, not semantic correctness. Automatic scoring retains missing and failed metric slots instead of filling them with invented values.

## Extraction remains a major limitation

Source-only extraction achieved precision zero point four five five, recall zero point zero six seven and F one zero point one one seven against the frozen source-scoped inventory. The proposed F one target of zero point eight was not met. Five exact-reference nonmatches may expose annotation or granularity gaps, so disagreement with the inventory is not always proof of semantic falsehood.

## Inspectability supports review

ThreatWeave demonstrates a local workflow with cited answers, exact source passages and inspectable graph paths. The preserved experiment, input hashes, validation failures and scoring records make its limitations reviewable. The project does not establish operational effectiveness or a general advantage for graph retrieval. The final report and slides provide the comparison results and their coverage limitations.