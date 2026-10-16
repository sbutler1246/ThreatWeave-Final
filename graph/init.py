"""Apply schema using environment credentials. Does not load gold benchmarks."""
import os
from pathlib import Path
from neo4j import GraphDatabase

def initialize():
    text=Path(__file__).with_name('schema.cypher').read_text(encoding='utf-8')
    statements='\n'.join(line for line in text.splitlines() if not line.strip().startswith('//')).split(';')
    with GraphDatabase.driver(os.environ['NEO4J_URI'],auth=(os.environ['NEO4J_USER'],os.environ['NEO4J_PASSWORD'])) as driver:
        driver.verify_connectivity()
        with driver.session(database=os.getenv('NEO4J_DATABASE','neo4j')) as session:
            for statement in statements:
                if statement.strip(): session.run(statement).consume()

if __name__=='__main__': initialize()
