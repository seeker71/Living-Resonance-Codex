#!/usr/bin/env python3
"""
Fractal Storage System for Living Codex Phase 5
Expands nodes into fractal subnodes while maintaining content-addressed storage
"""

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class FractalNode(BaseModel):
    """Represents a fractal node with nested subnodes"""
    id: str
    name: str
    water_state: str
    archetype: List[str] = []
    resonance: float = 0.5
    fractal_level: int = 1
    subnodes: Dict[str, 'FractalNode'] = {}
    parent_id: Optional[str] = None
    chakra: Optional[str] = None
    color_hex: Optional[str] = None
    base_frequency_hz: Optional[float] = None
    planet: Optional[str] = None
    created_at: str = Field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    updated_at: str = Field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))

class Contribution(BaseModel):
    """Represents a community contribution to a node"""
    id: str
    node_id: str
    user_id: str
    content: str
    resonance: float
    timestamp: str = Field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    fractal_context: Optional[str] = None  # Which fractal level this applies to

class FractalStorage:
    """Content-addressed storage system with fractal node expansion"""
    
    def __init__(self, storage_path: str = "./fractal-storage"):
        self.storage_path = Path(storage_path)
        self.contributions_path = self.storage_path / "contributions"
        self.nodes_path = self.storage_path / "nodes"
        self.manifest_path = self.storage_path / "manifest.json"
        
        self.ensure_storage_exists()
        # try to bootstrap from Graph API first, then fallback
        try:
            import requests
            api = os.getenv("GRAPH_API_URL", "http://localhost:8000")
            r = requests.get(f"{api}/nodes", timeout=2)
            if r.ok:
                nodes = {n.get("id"): n for n in r.json() if n.get("id", "").startswith("codex:")}
                self.initialize_fractal_nodes(bootstrap=nodes)
            else:
                self.initialize_fractal_nodes()
        except Exception:
            self.initialize_fractal_nodes()

    def _core_chakra_info(self) -> Dict[str, Dict[str, Any]]:
        return {
            "Root": {"color_hex": "#8B0000", "base_frequency_hz": 396.0},
            "Sacral": {"color_hex": "#FF7F50", "base_frequency_hz": 417.0},
            "SolarPlexus": {"color_hex": "#FFD700", "base_frequency_hz": 528.0},
            "Heart": {"color_hex": "#32CD32", "base_frequency_hz": 639.0},
            "Throat": {"color_hex": "#1E90FF", "base_frequency_hz": 741.0},
            "ThirdEye": {"color_hex": "#8A2BE2", "base_frequency_hz": 852.0},
            "Crown": {"color_hex": "#EE82EE", "base_frequency_hz": 963.0},
        }

    def _core_chakra_map(self) -> Dict[str, str]:
        return {
            "codex:Transformation": "Root",
            "codex:Resonance": "Sacral",
            "codex:Memory": "SolarPlexus",
            "codex:Flow": "Heart",
            "codex:Pattern": "Throat",
            "codex:Field": "ThirdEye",
            "codex:Void": "Crown",
        }

    def _core_planet_map(self) -> Dict[str, str]:
        return {
            "codex:Transformation": "Mars",
            "codex:Resonance": "Venus",
            "codex:Memory": "Saturn",
            "codex:Flow": "Moon",
            "codex:Pattern": "Mercury",
            "codex:Field": "Jupiter",
            "codex:Void": "Sun",
        }

    def _apply_core_defaults(self, node_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        chakra_map = self._core_chakra_map()
        chakra_info = self._core_chakra_info()
        planet_map = self._core_planet_map()
        chakra = data.get("chakra") or chakra_map.get(node_id)
        if chakra:
            data["chakra"] = chakra
            info = chakra_info.get(chakra)
            if info:
                data.setdefault("color_hex", info.get("color_hex"))
                data.setdefault("base_frequency_hz", info.get("base_frequency_hz"))
        if not data.get("planet") and node_id in planet_map:
            data["planet"] = planet_map[node_id]
        return data
    
    def ensure_storage_exists(self):
        """Create storage directory structure"""
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.contributions_path.mkdir(exist_ok=True)
        self.nodes_path.mkdir(exist_ok=True)
        
        if not self.manifest_path.exists():
            self.create_initial_manifest()
    
    def create_initial_manifest(self):
        """Create initial storage manifest"""
        manifest = {
            "version": "2.0.0",
            "fractal_level": 2,  # Now supporting 2 levels
            "total_contributions": 0,
            "total_nodes": 0,
            "total_subnodes": 0,
            "total_users": 0,
            "total_size": 0,
            "last_updated": time.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "contributions": {},
            "nodes": {},
            "fractal_expansions": {}
        }
        
        with open(self.manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
    
    def initialize_fractal_nodes(self, bootstrap: Optional[Dict[str, Any]] = None):
        """Initialize the base nodes with fractal expansion potential"""
        CHAKRA_INFO = self._core_chakra_info()

        base_nodes = {
            "codex:Void": {
                "name": "Void",
                "water_state": "Plasma",
                "archetype": ["Primordial", "Chaos", "Potential"],
                "resonance": 1.0,
                "fractal_level": 1
            },
            "codex:Field": {
                "name": "Field",
                "water_state": "Vapor",
                "archetype": ["Connectivity", "Information", "Flow"],
                "resonance": 0.8,
                "fractal_level": 1
            },
            "codex:Pattern": {
                "name": "Pattern",
                "water_state": "Structured",
                "archetype": ["Order", "Repetition", "Structure"],
                "resonance": 0.9,
                "fractal_level": 1
            },
            "codex:Flow": {
                "name": "Flow",
                "water_state": "Liquid",
                "archetype": ["Movement", "Change", "Adaptation"],
                "resonance": 0.7,
                "fractal_level": 1
            },
            "codex:Memory": {
                "name": "Memory",
                "water_state": "Ice",
                "archetype": ["Preservation", "History", "Storage"],
                "resonance": 0.6,
                "fractal_level": 1
            },
            "codex:Resonance": {
                "name": "Resonance",
                "water_state": "Clustered",
                "archetype": ["Harmony", "Vibration", "Synchronization"],
                "resonance": 0.9,
                "fractal_level": 1
            },
            "codex:Transformation": {
                "name": "Transformation",
                "water_state": "Supercritical",
                "archetype": ["Change", "Evolution", "Metamorphosis"],
                "resonance": 0.8,
                "fractal_level": 1
            },
            "codex:Unity": {
                "name": "Unity",
                "water_state": "LiquidCrystalBoundary",
                "archetype": ["Wholeness", "Integration", "Oneness"],
                "resonance": 0.7,
                "fractal_level": 1
            },
            "codex:Emergence": {
                "name": "Emergence",
                "water_state": "VaporLiquidEquilibrium",
                "archetype": ["Novelty", "Complexity", "Spontaneity"],
                "resonance": 0.6,
                "fractal_level": 1
            },
            "codex:Awareness": {
                "name": "Awareness",
                "water_state": "ReflectiveSurface",
                "archetype": ["Consciousness", "Observation", "Reflection"],
                "resonance": 0.8,
                "fractal_level": 1
            },
            "codex:Node": {
                "name": "Node",
                "water_state": "SteamSpark",
                "archetype": ["Connection", "Intersection", "Junction"],
                "resonance": 0.7,
                "fractal_level": 1
            },
            "codex:Codex": {
                "name": "Codex",
                "water_state": "AllStates",
                "archetype": ["Knowledge", "Wisdom", "Integration"],
                "resonance": 1.0,
                "fractal_level": 1
            }
        }

        # If bootstrap data present, override chakra/color/planet/frequency
        if bootstrap:
            for nid, meta in bootstrap.items():
                if nid in base_nodes:
                    base_nodes[nid]["chakra"] = meta.get("chakra")
                    base_nodes[nid]["color_hex"] = meta.get("colorHex")
                    base_nodes[nid]["base_frequency_hz"] = meta.get("baseFrequencyHz")
                    base_nodes[nid]["planet"] = meta.get("planet")

        # Apply defaults where missing
        for _id in list(base_nodes.keys()):
            base_nodes[_id] = self._apply_core_defaults(_id, base_nodes[_id])

        # Create base nodes
        for node_id, node_data in base_nodes.items():
            # Ensure all defaults applied before persisting
            node_data = self._apply_core_defaults(node_id, node_data)
            fractal_node = FractalNode(id=node_id, **node_data)
            self.store_node(fractal_node)

            # Expand into fractal subnodes
            self.expand_node_fractally(fractal_node)
    
    def expand_node_fractally(self, base_node: FractalNode):
        """Expand a base node into fractal subnodes across three dimensions"""
        node_name = base_node.name
        
        # Scientific Lens Subnodes
        scientific_subnodes = {
            f"{base_node.id}:scientific:empirical": {
                "id": f"{base_node.id}:scientific:empirical",
                "name": f"{node_name} Empirical",
                "water_state": "Structured",
                "archetype": ["Measurement", "Observation", "Data"],
                "resonance": base_node.resonance * 0.8,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            },
            f"{base_node.id}:scientific:theoretical": {
                "id": f"{base_node.id}:scientific:theoretical",
                "name": f"{node_name} Theoretical",
                "water_state": "Vapor",
                "archetype": ["Hypothesis", "Model", "Framework"],
                "resonance": base_node.resonance * 0.9,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            },
            f"{base_node.id}:scientific:experimental": {
                "id": f"{base_node.id}:scientific:experimental",
                "name": f"{node_name} Experimental",
                "water_state": "Liquid",
                "archetype": ["Testing", "Validation", "Discovery"],
                "resonance": base_node.resonance * 0.7,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            }
        }
        
        # Symbolic Lens Subnodes
        symbolic_subnodes = {
            f"{base_node.id}:symbolic:archetypal": {
                "id": f"{base_node.id}:symbolic:archetypal",
                "name": f"{node_name} Archetypal",
                "water_state": "Plasma",
                "archetype": ["Myth", "Symbol", "Collective"],
                "resonance": base_node.resonance * 0.9,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            },
            f"{base_node.id}:symbolic:cultural": {
                "id": f"{base_node.id}:symbolic:cultural",
                "name": f"{node_name} Cultural",
                "water_state": "Clustered",
                "archetype": ["Tradition", "Society", "Heritage"],
                "resonance": base_node.resonance * 0.8,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            },
            f"{base_node.id}:symbolic:personal": {
                "id": f"{base_node.id}:symbolic:personal",
                "name": f"{node_name} Personal",
                "water_state": "ReflectiveSurface",
                "archetype": ["Individual", "Subjective", "Experience"],
                "resonance": base_node.resonance * 0.7,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            }
        }
        
        # Water-State Lens Subnodes
        water_state_subnodes = {
            f"{base_node.id}:water:phase": {
                "id": f"{base_node.id}:water:phase",
                "name": f"{node_name} Phase",
                "water_state": "VaporLiquidEquilibrium",
                "archetype": ["Transition", "Boundary", "Change"],
                "resonance": base_node.resonance * 0.8,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            },
            f"{base_node.id}:water:flow": {
                "id": f"{base_node.id}:water:flow",
                "name": f"{node_name} Flow",
                "water_state": "Liquid",
                "archetype": ["Movement", "Direction", "Current"],
                "resonance": base_node.resonance * 0.9,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            },
            f"{base_node.id}:water:coherence": {
                "id": f"{base_node.id}:water:coherence",
                "name": f"{node_name} Coherence",
                "water_state": "LiquidCrystalBoundary",
                "archetype": ["Alignment", "Harmony", "Order"],
                "resonance": base_node.resonance * 0.8,
                "fractal_level": 2,
                "parent_id": base_node.id,
                "chakra": base_node.chakra,
                "color_hex": base_node.color_hex,
                "base_frequency_hz": base_node.base_frequency_hz,
                "planet": base_node.planet
            }
        }
        
        # Store all subnodes
        all_subnodes = {**scientific_subnodes, **symbolic_subnodes, **water_state_subnodes}
        
        for subnode_id, subnode_data in all_subnodes.items():
            subnode = FractalNode(**subnode_data)
            self.store_node(subnode)
            base_node.subnodes[subnode_id] = subnode
        
        # Update base node with subnodes
        self.store_node(base_node)
    
    def store_node(self, node: FractalNode):
        """Store a node in the fractal storage system"""
        # Windows-safe filename (replace colons with underscores)
        safe_filename = node.id.replace(':', '_') + '.json'
        node_path = self.nodes_path / safe_filename
        
        with open(node_path, 'w') as f:
            json.dump(node.model_dump(), f, indent=2)
        
        # Update manifest
        self.update_manifest_node(node)
    
    def store_contribution(self, contribution: Contribution) -> Dict[str, Any]:
        """Store a contribution with content-addressed hashing"""
        # Generate content hash
        content_string = f"{contribution.node_id}:{contribution.user_id}:{contribution.content}:{contribution.resonance}"
        content_hash = hashlib.sha256(content_string.encode()).hexdigest()
        
        # Store contribution
        contribution.id = content_hash
        contribution_path = self.contributions_path / f"{content_hash}.json"
        
        with open(contribution_path, 'w') as f:
            json.dump(contribution.model_dump(), f, indent=2)
        
        # Update manifest
        self.update_manifest_contribution(contribution, content_hash)
        
        return {
            "success": True,
            "content_hash": content_hash,
            "url": f"/contributions/{content_hash}",
            "size": len(content_string.encode())
        }
    
    def get_node(self, node_id: str) -> Optional[FractalNode]:
        """Retrieve a node by ID"""
        # Windows-safe filename (replace colons with underscores)
        safe_filename = node_id.replace(':', '_') + '.json'
        node_path = self.nodes_path / safe_filename
        
        if node_path.exists():
            with open(node_path, 'r') as f:
                node_data = json.load(f)
                # Backfill any missing core defaults for robustness
                node_data = self._apply_core_defaults(node_id, node_data)
                return FractalNode(**node_data)
        return None
    
    def get_contribution(self, content_hash: str) -> Optional[Contribution]:
        """Retrieve a contribution by content hash"""
        contribution_path = self.contributions_path / f"{content_hash}.json"
        
        if contribution_path.exists():
            with open(contribution_path, 'r') as f:
                contribution_data = json.load(f)
                return Contribution(**contribution_data)
        return None
    
    def get_node_contributions(self, node_id: str) -> Dict[str, Any]:
        """Get all contributions for a specific node"""
        contributions = []
        
        # Load manifest to find contributions
        with open(self.manifest_path, 'r') as f:
            manifest = json.load(f)
        
        for contrib_hash, contrib_data in manifest.get("contributions", {}).items():
            if contrib_data.get("node_id") == node_id:
                contribution = self.get_contribution(contrib_hash)
                if contribution:
                    contributions.append(contribution.model_dump())
        
        return {
            "contributions": contributions,
            "count": len(contributions)
        }
    
    def get_user_contributions(self, user_id: str) -> Dict[str, Any]:
        """Get all contributions from a specific user"""
        contributions = []
        
        # Load manifest to find contributions
        with open(self.manifest_path, 'r') as f:
            manifest = json.load(f)
        
        for contrib_hash, contrib_data in manifest.get("contributions", {}).items():
            if contrib_data.get("user_id") == user_id:
                contribution = self.get_contribution(contrib_hash)
                if contribution:
                    contributions.append(contribution.model_dump())
        
        return {
            "contributions": contributions,
            "count": len(contributions)
        }
    
    def get_fractal_expansion(self, node_id: str) -> Dict[str, Any]:
        """Get the fractal expansion of a node (all subnodes)"""
        node = self.get_node(node_id)
        if not node:
            return {"error": "Node not found"}
        
        if node.fractal_level == 1 and node.subnodes:
            return {
                "base_node": node.model_dump(),
                "subnodes": {sub_id: sub.model_dump() for sub_id, sub in node.subnodes.items()},
                "total_subnodes": len(node.subnodes),
                "fractal_levels": [1, 2]
            }
        elif node.fractal_level == 2:
            parent = self.get_node(node.parent_id) if node.parent_id else None
            return {
                "subnode": node.model_dump(),
                "parent": parent.model_dump() if parent else None,
                "fractal_level": 2
            }
        else:
            return {"error": "No fractal expansion available"}
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get comprehensive storage statistics including fractal data"""
        with open(self.manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Count nodes by fractal level
        level_1_nodes = 0
        level_2_nodes = 0
        
        for node_file in self.nodes_path.glob("*.json"):
            with open(node_file, 'r') as f:
                node_data = json.load(f)
                if node_data.get("fractal_level") == 1:
                    level_1_nodes += 1
                elif node_data.get("fractal_level") == 2:
                    level_2_nodes += 1
        
        return {
            "version": manifest.get("version", "2.0.0"),
            "fractal_level": manifest.get("fractal_level", 2),
            "total_contributions": manifest.get("total_contributions", 0),
            "total_nodes": level_1_nodes,
            "total_subnodes": level_2_nodes,
            "total_users": manifest.get("total_users", 0),
            "total_size": manifest.get("total_size", 0),
            "last_updated": manifest.get("last_updated", ""),
            "fractal_expansion": {
                "level_1_nodes": level_1_nodes,
                "level_2_nodes": level_2_nodes,
                "total_fractal_dimensions": 3  # scientific, symbolic, water
            }
        }
    
    def update_manifest_node(self, node: FractalNode):
        """Update manifest with node information"""
        with open(self.manifest_path, 'r') as f:
            manifest = json.load(f)
        
        manifest["nodes"][node.id] = {
            "name": node.name,
            "fractal_level": node.fractal_level,
            "parent_id": node.parent_id,
            "chakra": node.chakra,
            "color_hex": node.color_hex,
            "base_frequency_hz": node.base_frequency_hz,
            "planet": node.planet,
            "updated_at": node.updated_at
        }
        
        manifest["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        
        with open(self.manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
    
    def update_manifest_contribution(self, contribution: Contribution, content_hash: str):
        """Update manifest with contribution information"""
        with open(self.manifest_path, 'r') as f:
            manifest = json.load(f)
        
        manifest["contributions"][content_hash] = {
            "node_id": contribution.node_id,
            "user_id": contribution.user_id,
            "resonance": contribution.resonance,
            "timestamp": contribution.timestamp,
            "fractal_context": contribution.fractal_context
        }
        
        manifest["total_contributions"] = len(manifest["contributions"])
        manifest["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        
        # Update user count
        users = set()
        for contrib_data in manifest["contributions"].values():
            users.add(contrib_data.get("user_id", ""))
        manifest["total_users"] = len(users)
        
        with open(self.manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
