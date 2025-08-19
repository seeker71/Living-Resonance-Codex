#!/usr/bin/env python3
"""
Living Codex Phase 5 - Fractal Federation Server
Implements both current federation endpoints and new fractal expansion capabilities
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import time
from typing import Dict, Any, Optional

from fractal_storage import FractalStorage, Contribution, FractalNode

# Initialize FastAPI app
app = FastAPI(
    title="Living Codex Phase 5 - Fractal Federation",
    description="Federation server with fractal node expansion capabilities",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize fractal storage
fractal_storage = FractalStorage()

@app.get("/")
async def root():
    """Root endpoint with server information"""
    return {
        "name": "Living Codex Phase 5 - Fractal Federation",
        "version": "2.0.0",
        "status": "active",
        "fractal_levels": [1, 2],
        "endpoints": {
            "current_level": [
                "/storage/stats",
                "/contributions/{hash}",
                "/contributions/node/{node_id}",
                "/contributions/user/{user_id}",
                "/inbox",
                "/outbox"
            ],
            "next_fractal_level": [
                "/fractal/expand/{node_id}",
                "/fractal/nodes/{node_id}",
                "/fractal/subnodes/{node_id}",
                "/fractal/context/{context}",
                "/fractal/levels"
            ]
        }
    }

# ============================================================================
# CURRENT LEVEL ENDPOINTS (Phase 4 Compatibility)
# ============================================================================

@app.get("/storage/stats")
async def get_storage_stats():
    """Get storage statistics (Phase 4 compatible)"""
    try:
        stats = fractal_storage.get_storage_stats()
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting storage stats: {str(e)}")

@app.get("/contributions/{content_hash}")
async def get_contribution(content_hash: str):
    """Get contribution by content hash (Phase 4 compatible)"""
    try:
        contribution = fractal_storage.get_contribution(content_hash)
        if contribution:
            return contribution.dict()
        else:
            raise HTTPException(status_code=404, detail="Contribution not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting contribution: {str(e)}")

@app.get("/contributions/node/{node_id}")
async def get_node_contributions(node_id: str):
    """Get contributions for a specific node (Phase 4 compatible)"""
    try:
        contributions = fractal_storage.get_node_contributions(node_id)
        return contributions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting node contributions: {str(e)}")

@app.get("/contributions/user/{user_id}")
async def get_user_contributions(user_id: str):
    """Get contributions from a specific user (Phase 4 compatible)"""
    try:
        contributions = fractal_storage.get_user_contributions(user_id)
        return contributions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting user contributions: {str(e)}")

@app.post("/inbox")
async def post_to_inbox(request: Request):
    """Accept ActivityPub Create activities (Phase 4 compatible)"""
    try:
        # Parse request body
        body = await request.body()
        try:
            activity = json.loads(body)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON")
        
        # Validate ActivityPub structure
        if activity.get("type") != "Create":
            raise HTTPException(status_code=400, detail="Only Create activities supported")
        
        if "object" not in activity:
            raise HTTPException(status_code=400, detail="Missing object in activity")
        
        obj = activity["object"]
        if obj.get("type") != "Contribution":
            raise HTTPException(status_code=400, detail="Object must be of type Contribution")
        
        # Create contribution
        contribution = Contribution(
            id="",  # Will be set by storage
            node_id=obj.get("nodeId", ""),
            user_id=activity.get("actor", "anonymous"),
            content=obj.get("content", ""),
            resonance=obj.get("resonance", 0.5),
            fractal_context=obj.get("fractalContext")
        )
        
        # Store contribution
        result = fractal_storage.store_contribution(contribution)
        
        # Log for debugging
        print(f"INBOX activity: {json.dumps(activity, indent=2)}")
        print(f"Stored contribution: {json.dumps(result, indent=2)}")
        
        return JSONResponse(
            status_code=202,
            content={"status": "accepted", "result": result}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing inbox activity: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing activity: {str(e)}")

@app.get("/outbox")
async def get_outbox():
    """Get outbox of recent contributions (Phase 4 compatible)"""
    try:
        stats = fractal_storage.get_storage_stats()
        
        # Create ActivityPub OrderedCollection
        outbox = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": "/outbox",
            "type": "OrderedCollection",
            "totalItems": stats["total_contributions"],
            "orderedItems": []
        }
        
        # Add recent contributions (simplified for compatibility)
        if stats["total_contributions"] > 0:
            outbox["orderedItems"] = [
                {
                    "type": "Create",
                    "actor": "fractal@localhost",
                    "object": {
                        "type": "Contribution",
                        "nodeId": "codex:Void",
                        "content": "Fractal expansion in progress",
                        "resonance": 0.9
                    }
                }
            ]
        
        return outbox
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting outbox: {str(e)}")

# ============================================================================
# NEXT FRACTAL LEVEL ENDPOINTS (Phase 5 New Features)
# ============================================================================

@app.get("/fractal/expand/{node_id}")
async def get_fractal_expansion(node_id: str):
    """Get the complete fractal expansion of a node (Phase 5)"""
    try:
        expansion = fractal_storage.get_fractal_expansion(node_id)
        if "error" in expansion:
            raise HTTPException(status_code=404, detail=expansion["error"])
        return expansion
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting fractal expansion: {str(e)}")

@app.get("/fractal/nodes/{node_id}")
async def get_fractal_node(node_id: str):
    """Get detailed information about a fractal node (Phase 5)"""
    try:
        node = fractal_storage.get_node(node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
        
        # Add fractal context information
        node_data = node.dict()
        # Backfill any missing correspondence fields at response time
        if not node_data.get("planet"):
            node_data["planet"] = fractal_storage._core_planet_map().get(node_id)
        if not node_data.get("chakra"):
            chakra = fractal_storage._core_chakra_map().get(node_id)
            node_data["chakra"] = chakra
            info = fractal_storage._core_chakra_info().get(chakra or "")
            if info:
                node_data.setdefault("color_hex", info.get("color_hex"))
                node_data.setdefault("base_frequency_hz", info.get("base_frequency_hz"))
        if node.fractal_level == 1:
            node_data["fractal_context"] = "base_node"
            node_data["expansion_available"] = True
            node_data["subnode_count"] = len(node.subnodes)
        elif node.fractal_level == 2:
            node_data["fractal_context"] = "subnode"
            node_data["expansion_available"] = False
            node_data["parent_context"] = node.parent_id
        
        return node_data
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting fractal node: {str(e)}")

@app.get("/fractal/subnodes/{node_id}")
async def get_fractal_subnodes(node_id: str):
    """Get all subnodes of a base node (Phase 5)"""
    try:
        node = fractal_storage.get_node(node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
        
        if node.fractal_level != 1:
            raise HTTPException(status_code=400, detail="Only base nodes (level 1) have subnodes")
        
        if not node.subnodes:
            return {"subnodes": {}, "count": 0}
        
        # Group subnodes by context
        grouped_subnodes = {
            "scientific": {},
            "symbolic": {},
            "water": {}
        }
        
        for sub_id, subnode in node.subnodes.items():
            if ":scientific:" in sub_id:
                grouped_subnodes["scientific"][sub_id] = subnode.dict()
            elif ":symbolic:" in sub_id:
                grouped_subnodes["symbolic"][sub_id] = subnode.dict()
            elif ":water:" in sub_id:
                grouped_subnodes["water"][sub_id] = subnode.dict()
        
        return {
            "base_node": node.dict(),
            "subnodes": grouped_subnodes,
            "total_subnodes": len(node.subnodes),
            "contexts": ["scientific", "symbolic", "water"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting fractal subnodes: {str(e)}")

@app.get("/fractal/context/{context}")
async def get_fractal_context(context: str):
    """Get all nodes within a specific fractal context (Phase 5)"""
    try:
        valid_contexts = ["scientific", "symbolic", "water"]
        if context not in valid_contexts:
            raise HTTPException(status_code=400, detail=f"Invalid context. Must be one of: {valid_contexts}")
        
        # Find all subnodes in this context
        context_nodes = {}
        
        for node_file in fractal_storage.nodes_path.glob("*.json"):
            with open(node_file, 'r') as f:
                node_data = json.load(f)
                if node_data.get("fractal_level") == 2 and f":{context}:" in node_data.get("id", ""):
                    context_nodes[node_data["id"]] = node_data
        
        return {
            "context": context,
            "nodes": context_nodes,
            "count": len(context_nodes),
            "description": f"All {context} lens subnodes across the Living Codex"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting fractal context: {str(e)}")

@app.get("/fractal/levels")
async def get_fractal_levels():
    """Get information about available fractal levels (Phase 5)"""
    try:
        stats = fractal_storage.get_storage_stats()
        
        return {
            "fractal_levels": [1, 2],
            "current_max_level": 2,
            "level_descriptions": {
                1: "Base nodes - Core concepts of the Living Codex",
                2: "Fractal subnodes - Expanded perspectives across scientific, symbolic, and water-state lenses"
            },
            "level_statistics": {
                "level_1": {
                    "name": "Base Nodes",
                    "count": stats["total_nodes"],
                    "description": "Primary ontological concepts"
                },
                "level_2": {
                    "name": "Fractal Subnodes", 
                    "count": stats["total_subnodes"],
                    "description": "Expanded perspectives and deeper wisdom"
                }
            },
            "expansion_dimensions": {
                "scientific": "Empirical, theoretical, and experimental perspectives",
                "symbolic": "Archetypal, cultural, and personal meanings",
                "water": "Phase transitions, flow dynamics, and coherence patterns"
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting fractal levels: {str(e)}")

# ============================================================================
# COMPATIBILITY ENDPOINTS (ActivityPub Standard)
# ============================================================================

@app.get("/.well-known/webfinger")
async def webfinger():
    """WebFinger endpoint for ActivityPub compatibility"""
    return {
        "subject": "acct:fractal@localhost",
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": "http://localhost:8788/actor"
            },
            {
                "rel": "http://www.w3.org/ns/activitystreams#inbox",
                "type": "application/activity+json",
                "href": "http://localhost:8788/inbox"
            },
            {
                "rel": "http://www.w3.org/ns/activitystreams#outbox",
                "type": "application/activity+json",
                "href": "http://localhost:8788/outbox"
            }
        ]
    }

@app.get("/actor")
async def get_actor():
    """Actor endpoint for ActivityPub compatibility"""
    return {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": "http://localhost:8788/actor",
        "type": "Person",
        "name": "Living Codex Fractal Federation",
        "summary": "Phase 5 federation server with fractal node expansion",
        "inbox": "http://localhost:8788/inbox",
        "outbox": "http://localhost:8788/outbox",
        "preferredUsername": "fractal",
        "fractal_capabilities": {
            "levels": [1, 2],
            "contexts": ["scientific", "symbolic", "water"],
            "expansion": True
        }
    }

@app.get("/federation/peers")
async def get_federation_peers():
    """Get federation peer information (Phase 4 compatible)"""
    return {
        "peers": [
            {
                "id": "nodejs@localhost:8787",
                "url": "http://localhost:8787",
                "capabilities": ["phase4", "federation", "storage"],
                "status": "active"
            },
            {
                "id": "python@localhost:8788", 
                "url": "http://localhost:8788",
                "capabilities": ["phase4", "phase5", "federation", "fractal_expansion"],
                "status": "active"
            }
        ]
    }

@app.get("/federation/sync")
async def federation_sync():
    """Federation synchronization endpoint (Phase 4 compatible)"""
    return {
        "synced": True,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "fractal_levels_synced": [1, 2]
    }

if __name__ == "__main__":
    import uvicorn
    print("Living Codex Phase 5 - Fractal Federation Server")
    print("=" * 60)
    print("Starting server on http://localhost:8788")
    print("Fractal levels: 1 (base nodes) + 2 (expanded subnodes)")
    print("Contexts: scientific, symbolic, water")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=8788)
