#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
from pathlib import Path
import os, json

try:
    from neo4j import GraphDatabase
except Exception:
    GraphDatabase = None  # Optional dependency

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASS", "livingresonance123")

ROOT = Path(__file__).parents[2]
SEED_PATH = ROOT / "ontology" / "seed.json"
SCHEMA_PATH = ROOT / "ontology" / "schema.json"

app = FastAPI(title="Living Codex Graph API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _neo4j_driver():
    if GraphDatabase is None:
        return None
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        # probe
        with driver.session() as s:
            s.run("RETURN 1")
        return driver
    except Exception:
        return None


def _seed() -> Dict[str, Any]:
    return json.loads(SEED_PATH.read_text())


def _schema() -> Dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text())


def _core_correspondence_map() -> Dict[str, Dict[str, Any]]:
    mapping: Dict[str, Dict[str, Any]] = {}
    for row in _schema().get("coreCorrespondence", []):
        nid = row.get("node")
        if nid:
            mapping[nid] = {
                "chakra": row.get("chakra"),
                "colorHex": row.get("colorHex"),
                "baseFrequencyHz": row.get("baseFrequencyHz"),
                "planet": row.get("planet"),
            }
    return mapping


def _project_node(record: Dict[str, Any]) -> Dict[str, Any]:
    # Neo4j node projection → API node fields; backfill from schema core map if missing
    n = record.get("n", {})
    nid = n.get("id")
    node = {
        "id": nid,
        "name": n.get("name"),
        "waterState": n.get("waterState"),
        "archetype": n.get("archetype"),
        "layer": n.get("layer"),
        "chakra": n.get("chakra"),
        "colorHex": n.get("colorHex"),
        "baseFrequencyHz": n.get("baseFrequencyHz"),
        "planet": n.get("planet"),
    }
    if nid:
        core_map = _core_correspondence_map().get(nid, {})
        for k, v in core_map.items():
            if not node.get(k):
                node[k] = v
    return node


@app.get("/nodes")
def get_nodes(ids: Optional[str] = None, layer: Optional[str] = None):
    driver = _neo4j_driver()
    id_list: Optional[List[str]] = None
    if ids:
        id_list = [x.strip() for x in ids.split(",") if x.strip()]

    if driver:
        with driver.session() as s:
            if id_list:
                recs = s.run(
                    "MATCH (n:Node) WHERE n.id IN $ids RETURN n", ids=id_list
                ).data()
            elif layer:
                recs = s.run(
                    "MATCH (n:Node {layer:$layer}) RETURN n", layer=layer
                ).data()
            else:
                recs = s.run("MATCH (n:Node) RETURN n LIMIT 500").data()
        return [_project_node(r) for r in recs]

    # Fallback to seed.json
    seed = _seed()
    nodes = []
    for e in seed.get("@graph", []):
        if id_list and e.get("@id") not in id_list:
            continue
        if layer and e.get("layer") != layer:
            continue
        nodes.append({
            "id": e.get("@id"),
            "name": e.get("name"),
            "waterState": e.get("waterState"),
            "archetype": e.get("archetype", []),
            "layer": e.get("layer", "Seed"),
            "chakra": e.get("chakra"),
            "colorHex": e.get("colorHex"),
            "baseFrequencyHz": e.get("baseFrequencyHz"),
            "planet": e.get("planet"),
        })
    return nodes


@app.get("/nodes/{node_id}")
def get_node(node_id: str):
    driver = _neo4j_driver()
    if driver:
        with driver.session() as s:
            rec = s.run("MATCH (n:Node {id:$id}) RETURN n", id=node_id).single()
            if not rec:
                raise HTTPException(404, "Node not found")
            node = _project_node(rec.data())
            # relationships
            children = s.run(
                "MATCH (n:Node {id:$id})-[:HAS_PART]->(c:Node) RETURN c.id as id",
                id=node_id,
            ).value()
            parents = s.run(
                "MATCH (n:Node {id:$id})<-[:IS_PART_OF]-(c:Node) RETURN c.id as id",
                id=node_id,
            ).value()
            node.update({"children": children, "parents": parents})
            return node

    # Fallback seed
    seed = _seed()
    graph = seed.get("@graph", [])
    entry = next((e for e in graph if e.get("@id") == node_id), None)
    if not entry:
        raise HTTPException(404, "Node not found")
    node = {
        "id": entry.get("@id"),
        "name": entry.get("name"),
        "waterState": entry.get("waterState"),
        "archetype": entry.get("archetype", []),
        "layer": entry.get("layer", "Seed"),
        "chakra": entry.get("chakra"),
        "colorHex": entry.get("colorHex"),
        "baseFrequencyHz": entry.get("baseFrequencyHz"),
        "planet": entry.get("planet"),
    }
    # parents/children from references
    parents = []
    children = []
    if entry.get("isPartOf"):
        parents.append(entry.get("isPartOf"))
    for e in graph:
        if node_id in e.get("hasPart", []):
            parents.append(e.get("@id"))
    children = entry.get("hasPart", [])
    node.update({"children": children, "parents": parents})
    return node


@app.get("/axes")
def get_axes():
    driver = _neo4j_driver()
    if driver:
        with driver.session() as s:
            recs = s.run("MATCH (a:Axis) RETURN a").data()
        return [r["a"] for r in recs]
    return _seed().get("axes", [])


@app.get("/core-correspondence")
def core_correspondence():
    return _schema().get("coreCorrespondence", [])


if __name__ == "__main__":
    import uvicorn
    print("Living Codex Graph API Server")
    print("=" * 40)
    print("Starting server on http://localhost:8000")
    print("Available endpoints:")
    print("  /nodes - Get all nodes")
    print("  /nodes/{node_id} - Get specific node")
    print("  /axes - Get axes")
    print("  /core-correspondence - Get core correspondences")
    print("=" * 40)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


