#!/usr/bin/env python3
import json, os
from pathlib import Path
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASS", "livingresonance123")
SEED_PATH = Path(__file__).parents[2] / "ontology" / "seed.json"

schema_cypher = [
    "CREATE CONSTRAINT node_id IF NOT EXISTS FOR (n:Node) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT axis_name IF NOT EXISTS FOR (a:Axis) REQUIRE a.name IS UNIQUE"
]

create_node = """
MERGE (n:Node {id: $id})
SET n.name=$name, n.waterState=$waterState, n.archetype=$archetype, n.layer=$layer
"""

create_axis = """
MERGE (a:Axis {name: $name})
SET a.min=$min, a.max=$max, a.default=$default
"""

rel_hasPart = """
MATCH (p:Node {id:$parent}), (c:Node {id:$child})
MERGE (p)-[:HAS_PART]->(c)
"""

rel_isPartOf = """
MATCH (c:Node {id:$child}), (p:Node {id:$parent})
MERGE (c)-[:IS_PART_OF]->(p)
"""

def main():
    try:
        # First, validate that we can read the seed file
        print(f"Loading seed from: {SEED_PATH}")
        seed = json.loads(SEED_PATH.read_text())
        print(f"✓ Seed file loaded successfully with {len(seed.get('@graph', []))} nodes")
        
        # Check if Neo4j is available
        try:
            driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
            # Test connection
            with driver.session() as s:
                s.run("RETURN 1")
            print("✓ Neo4j connection successful")
            
            # Load data into Neo4j
            with driver.session() as s:
                for stmt in schema_cypher:
                    s.run(stmt)
                for entry in seed["@graph"]:
                    s.run(create_node, id=entry["@id"], name=entry["name"],
                          waterState=entry.get("waterState"),
                          archetype=entry.get("archetype", []),
                          layer=entry.get("layer", "Seed"))
                    for child in entry.get("hasPart", []):
                        s.run(rel_hasPart, parent=entry["@id"], child=child)
                    if entry.get("isPartOf"):
                        s.run(rel_isPartOf, child=entry["@id"], parent=entry["isPartOf"])
                for ax in seed.get("axes", []):
                    s.run(create_axis, **ax)
            print("✓ Seed loaded → Neo4j")
            
        except Exception as e:
            print(f"⚠ Neo4j connection failed: {e}")
            print("  To run with Neo4j, ensure the database is running and accessible")
            print("  You can start Neo4j with: neo4j start")
            print("  Or use Docker: docker run -p 7474:7474 -p 7687:7687 neo4j:latest")
            
    except FileNotFoundError:
        print(f"✗ Error: Seed file not found at {SEED_PATH}")
        print(f"  Current working directory: {Path.cwd()}")
        print(f"  Script location: {Path(__file__)}")
        print(f"  Expected seed path: {SEED_PATH}")
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON in seed file: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    main()