"""Load the reviewed development pilot into Neo4j with source provenance.

Requires pilot_extract.py and the existing ThreatWeave repository modules.
Only the two generated relationships supported by the frozen table row are accepted.
No gold triples or QA reference answers are read or inserted.
"""

import argparse
import getpass
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def stable_hash(*parts):
    return hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()


def prepare_ingestion(repo, run_path=None):
    sys.path.insert(0, str(repo))
    import pilot_extract as pilot
    from resolve import norm, resolve
    from schemas import Assertion, Entity

    run_root = (repo / "work/pilot_extraction").resolve()
    if run_path is None:
        folders = sorted((p for p in run_root.iterdir() if p.is_dir()), reverse=True)
        if not folders:
            raise ValueError("No pilot run folders found. Run pilot_extract.py first.")
        run_path = folders[0]
    run_path = run_path.resolve()
    if not run_path.is_relative_to(run_root):
        raise ValueError("Pilot run must be inside this repository's work/pilot_extraction folder.")
    run = json.loads((run_path / "run.json").read_text(encoding="utf-8"))
    if run.get("status") != "candidate_chain_ready_for_review":
        raise ValueError("The selected pilot did not produce a complete candidate chain.")
    (document, chunk, caption, config, system, prompt, schema, parse_extraction,
     reference_ids, attack_hash) = pilot.prepare(repo)
    if (run.get("scope_id") != chunk.chunk_id or run.get("source_hash") != document.content_hash
            or run.get("attack_snapshot_hash") != attack_hash
            or run.get("model") != config["llm"]["model"] or not run.get("model_digest")):
        raise ValueError("Pilot metadata does not match the frozen source/model configuration.")
    batch_text = (run_path / "candidate_extraction.json").read_text(encoding="utf-8")
    batch = parse_extraction(batch_text, chunk)
    source = chunk.text + "\n" + caption.text
    pilot.validate_entities(batch, source, reference_ids, chunk.text.splitlines()[0])
    if not pilot.has_actor_tool_technique_chain(batch):
        raise ValueError("The candidate does not contain the required two-hop chain.")

    # Reproduce the successful raw output's schema validation and explicit-ID normalization.
    attempts = [a for a in run["attempts"] if not a.get("validation_error") and not a.get("service_error")]
    if not attempts:
        raise ValueError("No successful model attempt was recorded.")
    raw_path = run_path / f"raw_extraction_{attempts[-1]['attempt']}.json"
    raw = raw_path.read_text(encoding="utf-8")
    reproduced = parse_extraction(raw, chunk)
    pilot.normalize_id_mentions(reproduced, source, reference_ids)
    if reproduced.model_dump() != batch.model_dump():
        raise ValueError("Candidate data differs from the recorded, normalized model output.")

    actor_name = caption.text.partition("Used by ")[2]
    tool_name = chunk.text.splitlines()[0]
    tech_ids = [identifier for identifier in reference_ids if identifier.startswith("T")]
    if not actor_name or len(tech_ids) != 1:
        raise ValueError("The pilot's source roles cannot be identified unambiguously.")
    technique_name = reference_ids[tech_ids[0]][0]["name"]
    by_local = {e.local_id: e for e in batch.entities}
    expected_roles = {
        ("ThreatGroup", norm(actor_name), "USES", "Software", norm(tool_name)),
        ("Software", norm(tool_name), "USES_TECHNIQUE", "Technique", norm(technique_name)),
    }
    actual_roles = {
        (by_local[r.head].type.value, norm(by_local[r.head].name), r.predicate.value,
         by_local[r.tail].type.value, norm(by_local[r.tail].name)) for r in batch.relations
    }
    if len(batch.entities) != 3 or len(batch.relations) != 2 or actual_roles != expected_roles:
        raise ValueError("This loader accepts only the two generated facts reviewed against this source row.")

    type_map = {"intrusion-set": "ThreatGroup", "tool": "Software", "malware": "Software",
                "attack-pattern": "Technique", "x-mitre-tactic": "Tactic",
                "course-of-action": "Mitigation", "campaign": "Campaign"}
    catalog = []
    attack = json.loads((repo / "data/enterprise-attack-17.1.json").read_text(encoding="utf-8"))
    for obj in attack["objects"]:
        if obj.get("revoked") or obj.get("x_mitre_deprecated") or obj.get("type") not in type_map:
            continue
        ids = {ref["external_id"] for ref in obj.get("external_references", [])
               if ref.get("source_name") == "mitre-attack" and ref.get("external_id")}
        if len(ids) != 1:
            continue
        attack_id = next(iter(ids))
        catalog.append(Entity(
            canonical_id="attack:" + attack_id, type=type_map[obj["type"]],
            name=obj["name"], aliases=(obj.get("aliases") or []) + (obj.get("x_mitre_aliases") or []),
            attack_id=attack_id, description=obj.get("description"), stix_id=obj["id"],
            attack_release="17.1", resolution_status="canonical",
        ))

    entities, identities, mentions, resolution_log = {}, {}, [], []
    for candidate in batch.entities:
        result = resolve(candidate, catalog)
        if result.status == "conflict" or (candidate.attack_id and result.status != "resolved"):
            raise ValueError(f"Identity resolution failed for {candidate.name}: {result.reason}")
        if result.entity is not None:
            entity = result.entity
        else:
            if candidate.type.value == "ThreatGroup":
                suffix = re.sub(r"[^a-z0-9]+", "-", norm(candidate.name)).strip("-")
                identifier = f"local:{document.doc_id}:{suffix}"
            else:
                name_hash = hashlib.sha256(candidate.name.encode("utf-8")).hexdigest()[:12]
                identifier = f"local:{document.doc_id}:{candidate.type.value.lower()}:{name_hash}"
            entity = Entity(canonical_id=identifier, type=candidate.type, name=candidate.name,
                            resolution_status="local")
        props = entity.model_dump(mode="json", exclude_none=True)
        props["normalized_name"] = norm(entity.name)
        entities[entity.canonical_id] = props
        identities[candidate.local_id] = entity.canonical_id
        resolution_log.append({"mention": candidate.name, "canonical_id": entity.canonical_id,
                               "status": result.status, "reason": result.reason})
        locations = [chunk] + chunk.inherited_context
        location = next((part for part in locations if candidate.name in part.text), None)
        if location is None:
            raise ValueError("An entity's source mention is missing.")
        start = location.start + location.text.index(candidate.name)
        mentions.append({"canonical_id": entity.canonical_id, "chunk_id": chunk.chunk_id,
                         "source_doc_id": document.doc_id, "evidence_text": candidate.name,
                         "evidence_start": start, "evidence_end": start + len(candidate.name)})

    now = datetime.now(timezone.utc).isoformat()
    raw_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    assertions = []
    for relation in batch.relations:
        head, tail = identities[relation.head], identities[relation.tail]
        key = stable_hash(head, relation.predicate.value, tail)
        assertion_id = "assertion:" + stable_hash(
            key, document.doc_id, chunk.chunk_id, relation.evidence.quote,
            run["model_digest"], run["prompt_hash"], raw_hash,
        )
        assertion = Assertion(
            assertion_id=assertion_id, head_id=head, predicate=relation.predicate,
            tail_id=tail, source_doc_id=document.doc_id, chunk_id=chunk.chunk_id,
            evidence_text=relation.evidence.quote, origin="extracted",
            validation_status="validated", confidence=relation.confidence,
        ).model_dump(mode="json", exclude_none=True)
        assertion.update({
            "triple_key": key, "evidence_start": chunk.start + relation.evidence.start,
            "evidence_end": chunk.start + relation.evidence.end,
            "inherited_context_json": json.dumps([c.model_dump() for c in chunk.inherited_context]),
            "actor_scope": actor_name, "source_url": str(document.source_url),
            "source_hash": document.content_hash, "model": run["model"],
            "model_digest": run["model_digest"], "prompt_hash": run["prompt_hash"],
            "raw_output_hash": raw_hash, "source_review_method": "frozen_table_roles_and_ID_validation",
            "source_review_at": now, "human_review_status": "pending",
        })
        assertions.append(assertion)
    doc_props = document.model_dump(mode="json", exclude_none=True)
    doc_props.update(canonical_id="doc:" + document.doc_id, name=document.title, type="Document")
    chunk_props = chunk.model_dump(mode="json", exclude_none=True)
    chunk_props["inherited_context_json"] = json.dumps(chunk_props.pop("inherited_context"))
    payload = {"document": doc_props, "chunk": chunk_props, "entities": list(entities.values()),
               "mentions": mentions, "assertions": assertions, "identity_resolution": resolution_log,
               "run_path": str(run_path), "prepared_at": now}
    return payload


def write_transaction(tx, payload):
    doc = payload["document"]
    existing = tx.run("MATCH (d:Document {doc_id:$id}) RETURN d.content_hash AS hash", id=doc["doc_id"]).single()
    if existing and existing["hash"] != doc["content_hash"]:
        raise ValueError("An existing Document has different frozen text; ingestion was cancelled.")
    tx.run("MERGE (d:Document {doc_id:$id}) ON CREATE SET d.created_at=$now SET d += $props",
           id=doc["doc_id"], now=payload["prepared_at"], props=doc).consume()
    chunk = payload["chunk"]
    existing_chunk = tx.run("MATCH (c:Chunk {chunk_id:$id}) RETURN c.text AS text, c.doc_id AS doc",
                            id=chunk["chunk_id"]).single()
    if existing_chunk and (existing_chunk["text"] != chunk["text"] or existing_chunk["doc"] != chunk["doc_id"]):
        raise ValueError("An existing Chunk has different source text; ingestion was cancelled.")
    tx.run("MERGE (c:Chunk {chunk_id:$id}) ON CREATE SET c.created_at=$now SET c += $props",
           id=chunk["chunk_id"], now=payload["prepared_at"], props=chunk).consume()
    for original in payload["entities"]:
        props = dict(original)
        aliases = props.pop("aliases")
        label = props["type"]
        if label not in {"ThreatGroup", "Software", "Technique"}:
            raise ValueError("Unsupported pilot node type.")
        current = tx.run("MATCH (e:Entity {canonical_id:$id}) RETURN e.type AS type, e.normalized_name AS name, e.attack_release AS release",
                         id=props["canonical_id"]).single()
        if current and (current["type"] != label or current["name"] != props["normalized_name"]
                        or (props.get("attack_release") and current["release"] not in (None, props["attack_release"]))):
            raise ValueError("An existing entity conflicts with the resolved identity.")
        tx.run(f"MERGE (e:Entity {{canonical_id:$id}}) ON CREATE SET e.created_at=$now, e.aliases=$aliases "
               f"SET e:{label} SET e += $props", id=props["canonical_id"], now=payload["prepared_at"],
               aliases=aliases, props=props).consume()
    for mention in payload["mentions"]:
        tx.run("MATCH (e:Entity {canonical_id:$id}), (d:Document {doc_id:$doc}) "
               "MERGE (e)-[m:MENTIONED_IN {chunk_id:$chunk}]->(d) SET m += $props",
               id=mention["canonical_id"], doc=mention["source_doc_id"], chunk=mention["chunk_id"], props=mention).consume()
    for assertion in payload["assertions"]:
        tx.run("MERGE (a:Assertion {assertion_id:$id}) ON CREATE SET a.created_at=$now SET a += $props",
               id=assertion["assertion_id"], now=payload["prepared_at"], props=assertion).consume()
        predicate = assertion["predicate"]
        if predicate not in {"USES", "USES_TECHNIQUE"}:
            raise ValueError("Unsupported pilot predicate.")
        props = {k: v for k, v in assertion.items() if k not in {"assertion_id", "head_id", "tail_id", "predicate"}}
        tx.run("MATCH (h:Entity {canonical_id:$head}), (t:Entity {canonical_id:$tail}) "
               f"MERGE (h)-[r:{predicate}]->(t) "
               "SET r += $props, r.assertion_ids = CASE "
               "WHEN $aid IN coalesce(r.assertion_ids, []) THEN r.assertion_ids "
               "ELSE coalesce(r.assertion_ids, []) + [$aid] END",
               head=assertion["head_id"], tail=assertion["tail_id"], aid=assertion["assertion_id"], props=props).consume()
    group_id = next(e["canonical_id"] for e in payload["entities"] if e["type"] == "ThreatGroup")
    count = tx.run("MATCH p=(g:ThreatGroup {canonical_id:$id})-[r1:USES]->(:Software)-[r2:USES_TECHNIQUE]->(:Technique) "
                   "WHERE r1.chunk_id=$chunk AND r2.chunk_id=$chunk RETURN count(p) AS paths",
                   id=group_id, chunk=chunk["chunk_id"]).single()["paths"]
    if count != 1:
        raise ValueError("Expected exactly one pilot chain; the transaction was rolled back.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--run", type=Path, help="Specific pilot run folder; defaults to the most recent")
    parser.add_argument("--preview", action="store_true", help="Check source and prepare records without database writes")
    args = parser.parse_args()
    payload = prepare_ingestion(args.repo.resolve(), args.run)
    print("Pilot run: " + payload["run_path"])
    print("Source and identity checks passed: 3 entities and 2 source-supported relationships.")
    for entity in payload["entities"]:
        print(f"  {entity['type']}: {entity['name']} [{entity['canonical_id']}]")
    if args.preview:
        print("PREVIEW PASSED: No database connection or writes were made.")
        return 0
    from neo4j import GraphDatabase
    uri = input("Neo4j URI [bolt://localhost:7687]: ").strip() or "bolt://localhost:7687"
    user = input("Neo4j username [neo4j]: ").strip() or "neo4j"
    database = input("Database name [neo4j]: ").strip() or "neo4j"
    password = getpass.getpass("Neo4j password (typing is hidden): ")
    try:
        with GraphDatabase.driver(uri, auth=(user, password), connection_timeout=10,
                                  connection_acquisition_timeout=15, max_transaction_retry_time=15) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                names = {row["name"] for row in session.run("SHOW CONSTRAINTS YIELD name RETURN name")}
                required = {"entity_id_unique", "doc_id_unique", "chunk_id_unique", "assertion_id_unique"}
                if not required.issubset(names):
                    raise ValueError("Required ThreatWeave constraints are missing from this database.")
                session.execute_write(write_transaction, payload)
    except Exception as error:
        message = str(error).replace(password, "[hidden]") if password else str(error)
        print(f"FAIL: {type(error).__name__}: {message}")
        return 1
    finally:
        password = None
    receipt = {"status": "ingestion_complete", "database": database,
               "entity_count": 3, "factual_relationship_count": 2, "assertion_count": 2,
               "source_review_method": "frozen_table_roles_and_ID_validation",
               "human_review_status": "pending", "completed_at": datetime.now(timezone.utc).isoformat(),
               "identity_resolution": payload["identity_resolution"]}
    path = Path(payload["run_path"]) / "ingestion_receipt.json"
    try:
        path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    except OSError as error:
        print(f"NOTE: Database ingestion committed, but the local receipt could not be saved: {error}")
    print("INGESTION COMPLETE: 3 entities and 2 factual relationships; the two-hop chain was verified.")
    print("Source context and model provenance are stored. Human verification is pending.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nIngestion cancelled.")
        sys.exit(2)
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        sys.exit(1)
