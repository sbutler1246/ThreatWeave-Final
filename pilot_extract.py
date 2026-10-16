"""Extract candidate relationships from one development source row.

This is a small integration smoke test, not full-corpus extraction or evaluation.
It reads CISA source text and split metadata, not gold triples or QA answers.
Outputs are candidate facts requiring semantic review; no graph writes occur.
Ollama API reference: https://docs.ollama.com/api/generate
"""

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


DOC_ID = "AA23-165A"
SCOPE_ID = "AA23-165A:table4:row02"
SOURCE_HASH = "7e9a69553beaaef6890dfb59db02e15242a75d14413b1e28b0307b80873a9e98"
ROW_START, ROW_END = 12695, 12872
CAPTION_START, CAPTION_END = 12066, 12132


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_id_mentions(batch, source, references):
    """Resolve an ID used as a name only when its canonical label is in the source."""
    changes = []
    for entity in batch.entities:
        records = references.get(entity.attack_id, [])
        if (entity.attack_id and entity.name == entity.attack_id and len(records) == 1
                and entity.type.value == records[0]["type"]
                and records[0]["name"] in source):
            original = entity.name
            entity.name = records[0]["name"]
            changes.append({"local_id": entity.local_id, "original_name": original,
                            "canonical_name": entity.name, "attack_id": entity.attack_id,
                            "basis": "explicit source ID and source-present ATT&CK label"})
    return changes


def has_actor_tool_technique_chain(batch):
    for first in batch.relations:
        if first.predicate.value == "USES":
            if any(second.head == first.tail and second.predicate.value == "USES_TECHNIQUE"
                   for second in batch.relations):
                return True
    return False


def validate_entities(batch, source, references, tool_name=None):
    """Check literal mentions and prevent an explicit ID from naming another entity."""
    from resolve import norm

    for entity in batch.entities:
        if entity.name not in source:
            raise ValueError(f"Entity name is not an exact source mention: {entity.name!r}")
        if tool_name and norm(entity.name) == norm(tool_name) and entity.type.value != "Software":
            raise ValueError(
                f"The source's Tool column identifies {tool_name!r} as Software, "
                f"not {entity.type.value}. Keep the tool and the ATT&CK behavior separate."
            )
        if not entity.attack_id:
            continue
        records = references.get(entity.attack_id, [])
        if len(records) != 1:
            raise ValueError(f"ATT&CK ID is absent from this source or ambiguous: {entity.attack_id}")
        record = records[0]
        accepted_names = {norm(record["name"]), *(norm(alias) for alias in record["aliases"])}
        if entity.type.value != record["type"] or norm(entity.name) not in accepted_names:
            raise ValueError(
                f"ATT&CK ID {entity.attack_id} identifies {record['type']} "
                f"{record['name']!r}, not {entity.type.value} {entity.name!r}. "
                "Represent the tool and the behavior as separate, correctly typed entities. "
                "Use local_id values, not names, for both relation endpoints."
            )


def prepare(repo):
    sys.path.insert(0, str(repo))
    from schemas import ALLOWED, Chunk, Document, ExtractionBatch, SourceContext
    from extraction.parser import parse_extraction, validate_chunk_document

    manifest = json.loads((repo / "benchmarks/corpus_manifest.json").read_text(encoding="utf-8"))
    split = json.loads((repo / "benchmarks/split_manifest.json").read_text(encoding="utf-8"))
    if (SCOPE_ID not in split["development_evidence_scopes"]
            or SCOPE_ID in split["held_out_evidence_scopes"]):
        raise ValueError("Pilot scope is not exclusively assigned to development.")
    record = next(item for item in manifest["documents"] if item["doc_id"] == DOC_ID)
    text_path = (repo / record["text_file"]).resolve()
    if not text_path.is_relative_to(repo):
        raise ValueError("Source file must be inside the repository.")
    text = text_path.read_text(encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != SOURCE_HASH or digest != record["normalized_sha256"]:
        raise ValueError("Source checksum differs from the frozen pilot snapshot.")
    document = Document(
        doc_id=DOC_ID, title=record["title"], source_url=record["source_url"],
        publication_date=record.get("release_date"), source="cisa", text=text,
        content_hash=digest,
    )
    context = SourceContext(
        start=CAPTION_START, end=CAPTION_END,
        text=text[CAPTION_START:CAPTION_END],
    )
    header_start = CAPTION_END + 1
    header_end = text.index("\n7-zip\n", CAPTION_END) + 1
    headers = SourceContext(start=header_start, end=header_end,
                            text=text[header_start:header_end])
    chunk = Chunk(
        chunk_id=SCOPE_ID, doc_id=DOC_ID, start=ROW_START, end=ROW_END,
        text=text[ROW_START:ROW_END], inherited_context=[context, headers], role="extraction",
    )
    validate_chunk_document(chunk, document)
    if not chunk.text.startswith("Advanced Port Scanner\n"):
        raise ValueError("The selected source row does not match the pilot metadata.")

    source = chunk.text + "\n" + context.text
    source_ids = set(re.findall(r"\b(?:TA\d{4}|T\d{4}(?:\.\d{3})?|[GSMC]\d{4})\b", source))
    attack_bytes = (repo / "data/enterprise-attack-17.1.json").read_bytes()
    attack_hash = hashlib.sha256(attack_bytes).hexdigest()
    if attack_hash != manifest["attack_sha256"]:
        raise ValueError("Frozen ATT&CK snapshot checksum does not match the manifest.")
    type_map = {"intrusion-set": "ThreatGroup", "tool": "Software", "malware": "Software",
                "attack-pattern": "Technique", "x-mitre-tactic": "Tactic",
                "course-of-action": "Mitigation", "campaign": "Campaign"}
    references = {}
    for obj in json.loads(attack_bytes)["objects"]:
        if obj.get("revoked") or obj.get("x_mitre_deprecated") or obj.get("type") not in type_map:
            continue
        for ref in obj.get("external_references", []):
            identifier = ref.get("external_id")
            if ref.get("source_name") == "mitre-attack" and identifier in source_ids:
                references.setdefault(identifier, []).append({
                    "name": obj["name"], "type": type_map[obj["type"]],
                    "aliases": (obj.get("aliases") or []) + (obj.get("x_mitre_aliases") or []),
                })

    config = json.loads((repo / "config.json").read_text(encoding="utf-8"))
    original = (repo / "prompts/extraction.txt").read_text(encoding="utf-8")
    system, separator, template = original.partition("\nUSER\n")
    if not separator:
        raise ValueError("Extraction prompt is missing its USER template marker.")
    system = system.removeprefix("SYSTEM\n")
    schema = ExtractionBatch.model_json_schema()
    definitions = schema["$defs"]
    definitions["EntityCandidate"]["properties"]["type"]["description"] = (
        "Software is a named tool/program. Technique is an attack behavior. "
        "ThreatGroup is a named actor, preserving an affiliates qualifier. "
        "Tactic is an explicitly named high-level objective, not a technique name."
    )
    for endpoint in ("head", "tail"):
        definitions["RelationCandidate"]["properties"][endpoint]["description"] = (
            "Must be a local_id of an entity in this same entities list; never an entity name."
        )
    # For this short source row, use the complete row as the exact evidence span.
    # This does not establish that an extracted relationship is semantically true.
    evidence = schema["$defs"]["EvidenceSpan"]["properties"]
    evidence["start"]["const"] = 0
    evidence["end"]["const"] = len(chunk.text)
    evidence["quote"]["const"] = chunk.text
    patterns = "\n".join(f"{a} --{b}--> {c}" for a, b, c in sorted(ALLOWED))
    system += "\nPERMITTED ENDPOINT PATTERNS:\n" + patterns
    example_row = "Tool Delta\nChecks network devices.\nFinds exposed services.\nNetwork Probing"
    example_evidence = {"start": 0, "end": len(example_row), "quote": example_row}
    table_example = {
        "entities": [
            {"local_id": "e1", "type": "ThreatGroup", "name": "Group Gamma", "attack_id": None},
            {"local_id": "e2", "type": "Software", "name": "Tool Delta", "attack_id": None},
            {"local_id": "e3", "type": "Technique", "name": "Network Probing", "attack_id": None},
        ],
        "relations": [
            {"head": "e1", "predicate": "USES", "tail": "e2", "evidence": example_evidence, "confidence": None},
            {"head": "e2", "predicate": "USES_TECHNIQUE", "tail": "e3", "evidence": example_evidence, "confidence": None},
        ],
    }
    system += ("\nFEW-SHOT EXAMPLE 3 (synthetic table; never source or gold data)\n"
               "INHERITED_CONTEXT: Tools used by Group Gamma\nCHUNK_TEXT:\n" + example_row
               + "\nOUTPUT:\n" + json.dumps(table_example)
               + "\nThe actor is supplied by the source caption. Both links require that same table scope.")
    system += "\nOUTPUT JSON SCHEMA:\n" + json.dumps(schema, ensure_ascii=False)
    prompt = template.format(
        doc_id=chunk.doc_id, chunk_id=chunk.chunk_id, chunk_text=chunk.text,
        inherited_context=json.dumps([item.model_dump() for item in chunk.inherited_context],
                                     ensure_ascii=False),
    )
    prompt += (
        "\nSMALL TABLE-ROW PILOT: Use the entire CHUNK_TEXT as each supporting quote. "
        f"Evidence start=0, end={len(chunk.text)}. "
        "The inherited source caption establishes the row's actor scope. "
        "Read INHERITED_CONTEXT as source evidence as well as CHUNK_TEXT. "
        "The actor named in the caption is eligible for the entities list even when "
        "its name is not repeated inside the individual table row. "
        "Consider actor-to-tool USES links supported by the caption and row, and "
        "tool-to-behavior USES_TECHNIQUE links supported by the repurposed use and ID label. "
        "Preserve all explicitly supported links during format repair. "
        "Read the row using the supplied table headers: first line is the tool name "
        "(Software); second is its intended use; third is its repurposed use by the "
        "caption's actor. The remaining lines give an ATT&CK ID and its label. "
        "A T-prefixed ATT&CK ID denotes a Technique (behavior), not the tool. "
        "Keep a tool's name separate from the behavior's name. "
        "Include every relation endpoint in entities and refer to its local_id. "
        "Extract only relationships explicitly supported by this row and caption. "
        "Entity names must occur exactly in this supplied source text. "
        "ATT&CK IDs may only be used when explicitly supplied in this source. "
        "The synthetic examples are instructions, not facts to extract."
    )
    return (document, chunk, context, config, system, prompt, schema, parse_extraction,
            references, attack_hash)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--ollama-url", default="http://localhost:11434")
    parser.add_argument("--timeout", type=int, default=60,
                        help="Seconds to wait for an Ollama response per attempt")
    parser.add_argument("--preview", action="store_true",
                        help="Validate and display source input without calling Ollama")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    repo = args.repo.resolve()
    prepared = prepare(repo)
    (document, chunk, context, config, system, prompt, schema, parse_extraction,
     references, attack_hash) = prepared

    print("ThreatWeave extraction pilot", flush=True)
    print(f"Source: {document.title} ({DOC_ID})", flush=True)
    print(f"Development scope: {SCOPE_ID}", flush=True)
    print("Source caption: " + context.text, flush=True)
    print("Source headers:\n" + chunk.inherited_context[1].text, flush=True)
    print("\nSource row:\n" + chunk.text, flush=True)
    if args.preview:
        print("\nPREVIEW PASSED: Source checksum, development split, and spans are valid.")
        return 0

    import requests
    base_url = args.ollama_url.rstrip("/")
    llm = config["llm"]
    tags_response = requests.get(base_url + "/api/tags", timeout=(5, 10))
    tags_response.raise_for_status()
    model = next((entry for entry in tags_response.json().get("models", [])
                  if entry.get("name") == llm["model"]), None)
    if not model or not model.get("digest"):
        raise ValueError(f"Installed model and digest not found for {llm['model']}.")
    if llm.get("digest") and llm["digest"] != model["digest"]:
        raise ValueError("Installed model digest does not match config.json.")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = repo / "work/pilot_extraction" / (stamp + "-" + uuid4().hex[:8])
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "chunk.json", chunk.model_dump(mode="json"))
    write_json(output / "source_metadata.json", {
        "doc_id": document.doc_id, "title": document.title,
        "source_url": str(document.source_url), "content_hash": document.content_hash,
        "source_file": str(Path("data") / f"{DOC_ID}.txt"),
        "scope_id": SCOPE_ID, "scope_assignment": "development",
    })
    (output / "system_prompt.txt").write_text(system, encoding="utf-8")
    (output / "user_prompt.txt").write_text(prompt, encoding="utf-8")
    settings = {
        "temperature": llm["temperature"], "num_ctx": llm["num_ctx"],
        "num_predict": llm["num_predict"],
    }
    run = {
        "purpose": "single_development_row_integration_smoke_test",
        "started_at_utc": stamp, "model": llm["model"],
        "model_digest": model["digest"], "options": settings,
        "source_hash": document.content_hash, "scope_id": SCOPE_ID,
        "attack_release": "17.1", "attack_snapshot_hash": attack_hash,
        "prompt_hash": hashlib.sha256((system + "\n" + prompt).encode()).hexdigest(),
        "semantic_review_status": "pending", "status": "started", "attempts": [],
    }
    write_json(output / "run.json", run)
    original_prompt = prompt
    for attempt in range(1, 3):
        print(f"\nCalling {llm['model']} (attempt {attempt}/2)...", flush=True)
        start = time.perf_counter()
        raw = ""
        info = {"attempt": attempt}
        run["attempts"].append(info)
        try:
            response = requests.post(base_url + "/api/generate", json={
                "model": llm["model"], "system": system, "prompt": prompt,
                "format": schema, "stream": False, "options": settings,
            }, timeout=(5, args.timeout))
            response.raise_for_status()
            payload = response.json()
            write_json(output / f"ollama_response_{attempt}.json", payload)
            raw = payload.get("response")
            if not isinstance(raw, str):
                raise ValueError("Ollama did not return a response string.")
            (output / f"raw_extraction_{attempt}.json").write_text(raw, encoding="utf-8")
            elapsed = round(time.perf_counter() - start, 3)
            info.update({"elapsed_seconds": elapsed,
                    "done_reason": payload.get("done_reason"),
                    "prompt_eval_count": payload.get("prompt_eval_count"),
                    "eval_count": payload.get("eval_count")})
            if payload.get("done") is not True or payload.get("done_reason") == "length":
                raise ValueError("Generation did not finish within the output budget.")
            batch = parse_extraction(raw, chunk)
            source = chunk.text + "\n" + context.text
            info["identity_normalization"] = normalize_id_mentions(batch, source, references)
            validate_entities(batch, source, references, chunk.text.splitlines()[0])
            write_json(output / "candidate_extraction.json", batch.model_dump(mode="json"))
            run.pop("error", None)
            complete_chain = has_actor_tool_technique_chain(batch)
            run.update(status=("candidate_chain_ready_for_review" if complete_chain
                               else "partial_extraction_pilot_incomplete" if batch.relations
                               else "empty_extraction_pilot_incomplete"),
                       has_actor_tool_technique_chain=complete_chain,
                       entity_count=len(batch.entities), relation_count=len(batch.relations))
            write_json(output / "run.json", run)
            names = {entity.local_id: entity.name for entity in batch.entities}
            lines = [f"{names[r.head]} --{r.predicate.value}--> {names[r.tail]}"
                     for r in batch.relations]
            summary = ("Candidate relationships — semantic review pending:\n"
                       + ("\n".join(lines) if lines else "No relationships returned.")
                       + "\n\nSource caption:\n" + context.text
                       + "\n\nSource row:\n" + chunk.text + "\n")
            (output / "review.txt").write_text(summary, encoding="utf-8")
            if not batch.relations:
                print("\nEMPTY EXTRACTION: No usable relationships; the extraction pilot remains incomplete.")
                print("Saved results: " + str(output))
                return 1
            if not complete_chain:
                print(f"\nPARTIAL EXTRACTION: {len(batch.entities)} entities; {len(batch.relations)} candidate relationships.")
                print("The actor-to-tool-to-technique chain is incomplete; semantic review is pending.")
                for line in lines:
                    print("  " + line)
                print("Saved results: " + str(output))
                return 1
            print(f"\nPILOT COMPLETE: {len(batch.entities)} entities; {len(batch.relations)} candidate relationships.")
            print("Schema and literal evidence checks passed; semantic review is pending.")
            for line in lines:
                print("  " + line)
            print("Saved results: " + str(output))
            return 0
        except requests.RequestException as error:
            info.update(elapsed_seconds=round(time.perf_counter() - start, 3),
                        service_error=f"{type(error).__name__}: {error}")
            run.update(status="service_error", error=f"{type(error).__name__}: {error}")
            write_json(output / "run.json", run)
            print(f"FAIL: Ollama request failed: {error}")
            print("Saved diagnostics: " + str(output))
            print("For a slow response, retry with --timeout 180.")
            return 1
        except ValueError as error:
            info.update(elapsed_seconds=round(time.perf_counter() - start, 3),
                        validation_error=str(error))
            run.update(status="validation_failed", error=str(error))
            write_json(output / "run.json", run)
            if attempt == 2:
                print("FAIL: Extraction remained invalid after one repair: " + str(error))
                print("Saved diagnostics: " + str(output))
                return 1
            print("Validation failed; requesting one schema/evidence repair.", flush=True)
            prompt = (original_prompt + "\nREPAIR: The previous output failed validation. "
                      + "Correct this error using only the original source:\n" + str(error)
                      + "\nPREVIOUS OUTPUT:\n" + str(raw)
                      + "\nReturn corrected JSON only. Do not add unsupported facts.")
            (output / "repair_prompt.txt").write_text(prompt, encoding="utf-8")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nPilot cancelled.")
        sys.exit(2)
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        sys.exit(1)
