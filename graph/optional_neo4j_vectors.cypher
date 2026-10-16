// Optional appendix adaptation only; online design uses Chroma.
// Requires compatible Neo4j vector-index support; not run by init.py.
CREATE VECTOR INDEX chunk_text_embeddings IF NOT EXISTS
FOR (c:Chunk) ON (c.embedding)
OPTIONS {indexConfig: {`vector.dimensions`: 384, `vector.similarity_function`: 'cosine'}};
CREATE VECTOR INDEX entity_graph_embeddings IF NOT EXISTS
FOR (n:Entity) ON (n.graph_embedding)
OPTIONS {indexConfig: {`vector.dimensions`: 128, `vector.similarity_function`: 'cosine'}};
