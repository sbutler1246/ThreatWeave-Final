// Neo4j 5.x node constraints; Chroma remains the approved vector index.
CREATE CONSTRAINT entity_id_unique IF NOT EXISTS FOR (n:Entity) REQUIRE n.canonical_id IS UNIQUE;
CREATE CONSTRAINT doc_id_unique IF NOT EXISTS FOR (n:Document) REQUIRE n.doc_id IS UNIQUE;
CREATE CONSTRAINT chunk_id_unique IF NOT EXISTS FOR (n:Chunk) REQUIRE n.chunk_id IS UNIQUE;
CREATE CONSTRAINT assertion_id_unique IF NOT EXISTS FOR (n:Assertion) REQUIRE n.assertion_id IS UNIQUE;
CREATE INDEX entity_name IF NOT EXISTS FOR (n:Entity) ON (n.normalized_name);
CREATE INDEX chunk_doc IF NOT EXISTS FOR (n:Chunk) ON (n.doc_id);
CREATE INDEX assertion_triple IF NOT EXISTS FOR (n:Assertion) ON (n.triple_key);
CREATE FULLTEXT INDEX entity_text IF NOT EXISTS FOR (n:Entity) ON EACH [n.name, n.aliases];
// No biomedical sample data is inserted. Optional vector indexes are separate.
