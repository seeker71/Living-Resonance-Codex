#!/usr/bin/env python3
"""
Living Codex Fractal Bootstrap System - Simplified Working Version
Demonstrates how the 16 bootstrap nodes can represent the complete ontological framework.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import hashlib
import time
import json

class CodexNode(BaseModel):
    """
    Living Codex node using the recursive bootstrap foundation.
    Every concept is built from the 16 fundamental bootstrap nodes.
    """
    
    # Core identity using bootstrap references
    symbol: str  # Reference to symbolic representation node
    name: str    # Reference to name representation node
    meta: str    # Reference to type/structure node
    links: List[str] = Field(default_factory=list)  # References to connected nodes
    
    # Optional metadata for performance/querying
    id: Optional[str] = None
    created_at: str = Field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    updated_at: str = Field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    
    def model_post_init(self, __context):
        if not self.id:
            # Generate ID from content hash
            content = f"{self.symbol}:{self.name}:{self.meta}:{':'.join(sorted(self.links))}"
            self.id = hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def add_link(self, node_ref: str):
        """Add a link to another node"""
        if node_ref not in self.links:
            self.links.append(node_ref)
            self.updated_at = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")

class CodexBootstrapStorage:
    """
    Storage system for Living Codex nodes using bootstrap foundation.
    Maps the complete ontological framework in a fractal, recursive way.
    """
    
    def __init__(self):
        self.nodes: Dict[str, CodexNode] = {}
        self._initialize_bootstrap_foundation()
        self._initialize_codex_core()
        self._initialize_water_states()
        self._initialize_chakra_system()
        self._initialize_planetary_correspondences()
    
    def _initialize_bootstrap_foundation(self):
        """Initialize the 16 fundamental bootstrap nodes"""
        
        # Core bootstrap nodes
        bootstrap_nodes = {
            "identity": CodexNode(symbol="105_100_101_110_116_105_116_121", name="identity", meta="identity", links=[]),
            "node": CodexNode(symbol="110_111_100_101", name="node", meta="identity", links=["identity"]),
            "seq": CodexNode(symbol="115_101_113", name="seq", meta="identity", links=["identity", "node"]),
            "bag": CodexNode(symbol="98_97_103", name="bag", meta="identity", links=["identity", "node"]),
            "symbol": CodexNode(symbol="115_121_109_98_111_108", name="symbol", meta="identity", links=["identity", "node"]),
            "name": CodexNode(symbol="110_97_109_101", name="name", meta="identity", links=["identity", "node"]),
            "meta": CodexNode(symbol="109_101_116_97", name="meta", meta="identity", links=["identity", "node"]),
            "char": CodexNode(symbol="99_104_97_114", name="char", meta="identity", links=["identity", "node", "symbol"]),
            "word": CodexNode(symbol="119_111_114_100", name="word", meta="identity", links=["identity", "node", "seq", "char"]),
            "number": CodexNode(symbol="110_117_109_98_101_114", name="number", meta="identity", links=["identity", "node", "symbol"]),
            "language": CodexNode(symbol="108_97_110_103", name="language", meta="identity", links=["identity", "node", "symbol"]),
            "link": CodexNode(symbol="108_105_110_107", name="link", meta="identity", links=["identity", "node"]),
            "is_meta": CodexNode(symbol="105_115_95_109_101_116_97", name="is_meta", meta="identity", links=["identity", "node", "link"]),
            "has_property": CodexNode(symbol="104_97_115_95_112_114_111_112", name="has_property", meta="identity", links=["identity", "node", "link"]),
            "instance": CodexNode(symbol="105_110_115_116_97_110_99_101", name="instance", meta="identity", links=["identity", "node"]),
            "type": CodexNode(symbol="116_121_112_101", name="type", meta="identity", links=["identity", "node"])
        }
        
        # Store bootstrap nodes
        for node_id, node in bootstrap_nodes.items():
            node.id = node_id
            self.nodes[node_id] = node
    
    def _initialize_codex_core(self):
        """Initialize the core Living Codex nodes (Seed Layer)"""
        
        # Core ontological nodes using bootstrap foundation
        core_nodes = {
            "void": CodexNode(symbol="118_111_105_100", name="void", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "field": CodexNode(symbol="102_105_101_108_100", name="field", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "pattern": CodexNode(symbol="112_97_116_116_101_114_110", name="pattern", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "flow": CodexNode(symbol="102_108_111_119", name="flow", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "memory": CodexNode(symbol="109_101_109_111_114_121", name="memory", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "resonance": CodexNode(symbol="114_101_115_111_110_97_110_99_101", name="resonance", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "transformation": CodexNode(symbol="116_114_97_110_115_102_111_114_109_97_116_105_111_110", name="transformation", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "unity": CodexNode(symbol="117_110_105_116_121", name="unity", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "emergence": CodexNode(symbol="101_109_101_114_103_101_110_99_101", name="emergence", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "awareness": CodexNode(symbol="97_119_97_114_101_110_101_115_115", name="awareness", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "node_concept": CodexNode(symbol="110_111_100_101_95_99_111_110_99_101_112_116", name="node_concept", meta="codex_core", links=["identity", "node", "type", "has_property"]),
            "codex": CodexNode(symbol="99_111_100_101_120", name="codex", meta="codex_core", links=["identity", "node", "type", "has_property"])
        }
        
        # Store core nodes
        for node_id, node in core_nodes.items():
            node.id = f"codex:{node_id}"
            self.nodes[node_id] = node
    
    def _initialize_water_states(self):
        """Initialize the 12 water states as nodes"""
        
        water_states = [
            "crystalline", "liquid", "vapor", "plasma", "supercritical",
            "structured_hexagonal", "colloidal", "amorphous", "clustered",
            "quantum_coherent", "lattice_ice_polymorphs", "bose_einstein_like"
        ]
        
        for i, state in enumerate(water_states):
            # Create water state node
            water_node = CodexNode(
                symbol=f"119_97_116_101_114_{state}",
                name=state,
                meta="water_state",
                links=["identity", "node", "type", "has_property", "number"]
            )
            water_node.id = f"water:{state}"
            self.nodes[f"water:{state}"] = water_node
            
            # Create frequency node for this water state
            freq_node = CodexNode(
                symbol=f"102_114_101_113_{i+1}",
                name=str(i + 1),
                meta="number",
                links=["identity", "node", "type", "instance"]
            )
            freq_node.id = f"freq:{i+1}"
            self.nodes[f"freq:{i+1}"] = freq_node
            
            # Link water state to frequency
            water_node.add_link(f"freq:{i+1}")
    
    def _initialize_chakra_system(self):
        """Initialize the chakra system as nodes"""
        
        chakras = [
            "root", "sacral", "solar_plexus", "heart", "throat", "third_eye", "crown"
        ]
        
        for i, chakra in enumerate(chakras):
            # Create chakra node
            chakra_node = CodexNode(
                symbol=f"99_104_97_107_114_97_{chakra}",
                name=chakra,
                meta="chakra",
                links=["identity", "node", "type", "has_property", "number"]
            )
            chakra_node.id = f"chakra:{chakra}"
            self.nodes[f"chakra:{chakra}"] = chakra_node
            
            # Create chakra frequency node
            chakra_freq_node = CodexNode(
                symbol=f"99_104_97_107_114_97_102_{i+1}",
                name=str(396 + (i * 21)),  # Solfeggio frequencies
                meta="number",
                links=["identity", "node", "type", "instance"]
            )
            chakra_freq_node.id = f"chakraf:{chakra}"
            self.nodes[f"chakraf:{chakra}"] = chakra_freq_node
            
            # Link chakra to frequency
            chakra_node.add_link(f"chakraf:{chakra}")
    
    def _initialize_planetary_correspondences(self):
        """Initialize planetary correspondences as nodes"""
        
        planets = [
            "mars", "venus", "saturn", "moon", "mercury", "jupiter", "sun"
        ]
        
        for planet in planets:
            planet_node = CodexNode(
                symbol=f"112_108_97_110_101_116_{planet}",
                name=planet,
                meta="planet",
                links=["identity", "node", "type", "has_property"]
            )
            planet_node.id = f"planet:{planet}"
            self.nodes[f"planet:{planet}"] = planet_node
    
    def create_codex_node(self, name: str, water_state: str, chakra: str, 
                         planet: str, color_hex: str, frequency: float) -> str:
        """Create a complete Living Codex node with all correspondences"""
        
        # Create the main node
        node_symbol = "_".join([str(ord(c)) for c in name.lower()])
        node = CodexNode(
            symbol=node_symbol,
            name=name,
            meta="codex_node",
            links=["identity", "node", "type", "has_property"]
        )
        
        # Add water state link
        if f"water:{water_state}" in self.nodes:
            node.add_link(f"water:{water_state}")
        
        # Add chakra link
        if f"chakra:{chakra}" in self.nodes:
            node.add_link(f"chakra:{chakra}")
        
        # Add planet link
        if f"planet:{planet}" in self.nodes:
            node.add_link(f"planet:{planet}")
        
        # Add color and frequency as properties
        color_node = CodexNode(
            symbol=f"99_111_108_111_114_{color_hex.replace('#', '')}",
            name=color_hex,
            meta="color",
            links=["identity", "node", "type", "instance"]
        )
        color_node.id = f"color:{color_hex}"
        self.nodes[f"color:{color_hex}"] = color_node
        node.add_link(f"color:{color_hex}")
        
        freq_node = CodexNode(
            symbol=f"102_114_101_113_{int(frequency)}",
            name=str(int(frequency)),
            meta="number",
            links=["identity", "node", "type", "instance"]
        )
        freq_node.id = f"freq:{int(frequency)}"
        self.nodes[f"freq:{int(frequency)}"] = freq_node
        node.add_link(f"freq:{int(frequency)}")
        
        # Store the node
        node_id = node.id
        self.nodes[node_id] = node
        return node_id
    
    def get_node_network(self, node_id: str, depth: int = 2) -> Dict[str, Any]:
        """Get a node and its network up to specified depth"""
        if depth <= 0:
            return {"id": node_id, "depth": 0}
        
        node = self.nodes.get(node_id)
        if not node:
            return {"error": "Node not found"}
        
        result = {
            "id": node_id,
            "symbol": node.symbol,
            "name": node.name,
            "meta": node.meta,
            "depth": depth,
            "links": []
        }
        
        # Recursively get linked nodes
        for link_id in node.links[:10]:  # Limit to prevent infinite recursion
            linked_node = self.get_node_network(link_id, depth - 1)
            result["links"].append(linked_node)
        
        return result
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get comprehensive statistics about the Living Codex system"""
        total_nodes = len(self.nodes)
        
        # Count nodes by meta type
        meta_counts = {}
        for node in self.nodes.values():
            meta = node.meta
            meta_counts[meta] = meta_counts.get(meta, 0) + 1
        
        # Count core Living Codex nodes
        codex_core_count = sum(1 for node in self.nodes.values() if node.meta == "codex_core")
        water_state_count = sum(1 for node in self.nodes.values() if node.meta == "water_state")
        chakra_count = sum(1 for node in self.nodes.values() if node.meta == "chakra")
        
        return {
            "total_nodes": total_nodes,
            "meta_type_counts": meta_counts,
            "living_codex_stats": {
                "core_nodes": codex_core_count,
                "water_states": water_state_count,
                "chakras": chakra_count,
                "planets": 7
            },
            "bootstrap_foundation": 16,
            "fractal_layers": [
                "Bootstrap Foundation (16 nodes)",
                "Core Ontology (12 nodes)", 
                "Water States (12 nodes)",
                "Chakra System (7 nodes)",
                "Planetary Correspondences (7 nodes)"
            ]
        }

# Test the Living Codex bootstrap system
if __name__ == "__main__":
    print("Living Codex Fractal Bootstrap System - Simplified")
    print("=" * 60)
    
    # Create Living Codex storage
    storage = CodexBootstrapStorage()
    
    # Create a complete Living Codex node with all correspondences
    print("\nCreating complete Living Codex node...")
    void_node_id = storage.create_codex_node(
        name="Void",
        water_state="plasma",
        chakra="crown", 
        planet="sun",
        color_hex="#EE82EE",
        frequency=963.0
    )
    
    print(f"Void node created with ID: {void_node_id}")
    
    # Show comprehensive statistics
    print("\nLiving Codex System Statistics:")
    stats = storage.get_storage_stats()
    print(json.dumps(stats, indent=2))
    
    # Show node network
    print(f"\nVoid Node Network (depth 2):")
    network = storage.get_node_network(void_node_id, depth=2)
    print(json.dumps(network, indent=2))
    
    print("\n" + "="*60)
    print("Living Codex successfully bootstrapped using recursive nodes!")
    print("The entire ontological framework is now represented using the")
    print("16 fundamental bootstrap nodes as a foundation.")
    print("\nThis demonstrates the fractal, recursive nature of the system:")
    print("  ✓ Core ontology (12 nodes)")
    print("  ✓ Water states (12 nodes)") 
    print("  ✓ Chakra system (7 nodes)")
    print("  ✓ Planetary correspondences (7 nodes)")
    print("\nAll built from just 16 bootstrap nodes!")
