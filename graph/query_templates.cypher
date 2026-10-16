// Independent approved two-/three-hop templates. Supply $seed_ids.
MATCH (g:ThreatGroup)-[r1:USES]->(s:Software)-[r2:USES_TECHNIQUE]->(t:Technique)
WHERE g.canonical_id IN $seed_ids
RETURN g.canonical_id, s.canonical_id, t.canonical_id, r1.triple_key, r2.triple_key
ORDER BY g.canonical_id, s.canonical_id, t.canonical_id LIMIT 30;

MATCH (g:ThreatGroup)-[r1:USES_TECHNIQUE]->(t:Technique)-[r2:PART_OF_TACTIC]->(a:Tactic)
WHERE g.canonical_id IN $seed_ids
RETURN g.canonical_id, t.canonical_id, a.canonical_id, r1.triple_key, r2.triple_key
ORDER BY g.canonical_id, t.canonical_id, a.canonical_id LIMIT 30;

MATCH (s:Software)-[r1:USES_TECHNIQUE]->(t:Technique)-[r2:PART_OF_TACTIC]->(a:Tactic)
WHERE s.canonical_id IN $seed_ids
RETURN s.canonical_id, t.canonical_id, a.canonical_id, r1.triple_key, r2.triple_key
ORDER BY s.canonical_id, t.canonical_id, a.canonical_id LIMIT 30;

MATCH (s:Software)-[r1:USES_TECHNIQUE]->(t:Technique)-[r2:MITIGATED_BY]->(m:Mitigation)
WHERE s.canonical_id IN $seed_ids
RETURN s.canonical_id, t.canonical_id, m.canonical_id, r1.triple_key, r2.triple_key
ORDER BY s.canonical_id, t.canonical_id, m.canonical_id LIMIT 30;

MATCH (g:ThreatGroup)-[r1:USES]->(s:Software)-[r2:USES_TECHNIQUE]->(t:Technique)-[r3:MITIGATED_BY]->(m:Mitigation)
WHERE g.canonical_id IN $seed_ids
RETURN g.canonical_id, s.canonical_id, t.canonical_id, m.canonical_id,
       r1.triple_key, r2.triple_key, r3.triple_key
ORDER BY g.canonical_id, s.canonical_id, t.canonical_id, m.canonical_id LIMIT 30;
// Retrieval adapter must join accepted Assertion records and supporting
// passages for every returned triple_key before admitting a path to context.
// Each edge must have accepted validation_status and its own source_doc_id,
// chunk_id, evidence_text, and origin. Gold annotation files are never loaded.
