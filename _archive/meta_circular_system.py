#!/usr/bin/env python3
"""
Meta-Circular Living Codex System
Every node and every link has a meta-node describing its structure.
The system is completely self-documenting and meta-circular.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import hashlib
import time
import json

class MetaCircularNode(BaseModel):
    """
    Meta-circular node where every component describes itself.
    Each field references a meta-node that describes its structure.
    """
    
    # Core identity - each references its own meta-node
    symbol: str      # References a meta-node describing "what is a symbol"
    name: str        # References a meta-node describing "what is a name"
    meta: str        # References a meta-node describing "what is a meta"
    links: List[str] = Field(default_factory=list)  # References meta-node "what is a link"
    
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

class MetaCircularStorage:
    """
    Storage system for meta-circular nodes.
    Every component describes itself using the same recursive structure.
    """
    
    def __init__(self):
        self.nodes: Dict[str, MetaCircularNode] = {}
        self._initialize_meta_foundations()
        self._initialize_structural_meta_nodes()
        self._initialize_type_meta_nodes()
        self._initialize_relationship_meta_nodes()
        self._initialize_codex_meta_nodes()
    
    def _initialize_meta_foundations(self):
        """
        Initialize the foundational meta-nodes that describe the basic concepts.
        These are the meta-nodes that describe what each component IS.
        """
        
        # Meta-node describing "what is identity"
        identity_meta = MetaCircularNode(
            symbol="109_101_116_97_95_105_100_101_110_116_105_116_121",  # "meta_identity"
            name="meta_identity", 
            meta="meta_meta",  # References itself through meta_meta
            links=[]
        )
        identity_meta.id = "meta:identity"
        self.nodes["meta:identity"] = identity_meta
        
        # Meta-node describing "what is a node"
        node_meta = MetaCircularNode(
            symbol="109_101_116_97_95_110_111_100_101",  # "meta_node"
            name="meta_node",
            meta="meta:identity",
            links=["meta:identity"]
        )
        node_meta.id = "meta:node"
        self.nodes["meta:node"] = node_meta
        
        # Meta-node describing "what is a symbol"
        symbol_meta = MetaCircularNode(
            symbol="109_101_116_97_95_115_121_109_98_111_108",  # "meta_symbol"
            name="meta_symbol",
            meta="meta:node",
            links=["meta:identity", "meta:node"]
        )
        symbol_meta.id = "meta:symbol"
        self.nodes["meta:symbol"] = symbol_meta
        
        # Meta-node describing "what is a name"
        name_meta = MetaCircularNode(
            symbol="109_101_116_97_95_110_97_109_101",  # "meta_name"
            name="meta_name",
            meta="meta:node",
            links=["meta:identity", "meta:node"]
        )
        name_meta.id = "meta:name"
        self.nodes["meta:name"] = name_meta
        
        # Meta-node describing "what is a meta"
        meta_meta = MetaCircularNode(
            symbol="109_101_116_97_95_109_101_116_97",  # "meta_meta"
            name="meta_meta",
            meta="meta:node",
            links=["meta:identity", "meta:node"]
        )
        meta_meta.id = "meta:meta"
        self.nodes["meta:meta"] = meta_meta
        
        # Meta-node describing "what is a link"
        link_meta = MetaCircularNode(
            symbol="109_101_116_97_95_108_105_110_107",  # "meta_link"
            name="meta_link",
            meta="meta:node",
            links=["meta:identity", "meta:node"]
        )
        link_meta.id = "meta:link"
        self.nodes["meta:link"] = link_meta
        
        # Now update the identity meta to reference meta_meta
        identity_meta.meta = "meta:meta"
        identity_meta.add_link("meta:meta")
    
    def _initialize_structural_meta_nodes(self):
        """
        Initialize meta-nodes that describe structural components.
        """
        
        # Meta-node describing "what is a sequence"
        seq_meta = MetaCircularNode(
            symbol="109_101_116_97_95_115_101_113",  # "meta_seq"
            name="meta_seq",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:link"]
        )
        seq_meta.id = "meta:seq"
        self.nodes["meta:seq"] = seq_meta
        
        # Meta-node describing "what is a bag/collection"
        bag_meta = MetaCircularNode(
            symbol="109_101_116_97_95_98_97_103",  # "meta_bag"
            name="meta_bag",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:link"]
        )
        bag_meta.id = "meta:bag"
        self.nodes["meta:bag"] = bag_meta
        
        # Meta-node describing "what is a character"
        char_meta = MetaCircularNode(
            symbol="109_101_116_97_95_99_104_97_114",  # "meta_char"
            name="meta_char",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:symbol"]
        )
        char_meta.id = "meta:char"
        self.nodes["meta:char"] = char_meta
        
        # Meta-node describing "what is a word"
        word_meta = MetaCircularNode(
            symbol="109_101_116_97_95_119_111_114_100",  # "meta_word"
            name="meta_word",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:seq", "meta:char"]
        )
        word_meta.id = "meta:word"
        self.nodes["meta:word"] = word_meta
        
        # Meta-node describing "what is a number"
        number_meta = MetaCircularNode(
            symbol="109_101_116_97_95_110_117_109_98_101_114",  # "meta_number"
            name="meta_number",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:symbol"]
        )
        number_meta.id = "meta:number"
        self.nodes["meta:number"] = number_meta
    
    def _initialize_type_meta_nodes(self):
        """
        Initialize meta-nodes that describe type and classification concepts.
        """
        
        # Meta-node describing "what is a type"
        type_meta = MetaCircularNode(
            symbol="109_101_116_97_95_116_121_112_101",  # "meta_type"
            name="meta_type",
            meta="meta:node",
            links=["meta:identity", "meta:node"]
        )
        type_meta.id = "meta:type"
        self.nodes["meta:type"] = type_meta
        
        # Meta-node describing "what is an instance"
        instance_meta = MetaCircularNode(
            symbol="109_101_116_97_95_105_110_115_116_97_110_99_101",  # "meta_instance"
            name="meta_instance",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:type"]
        )
        instance_meta.id = "meta:instance"
        self.nodes["meta:instance"] = instance_meta
        
        # Meta-node describing "what is a class/category"
        class_meta = MetaCircularNode(
            symbol="109_101_116_97_95_99_108_97_115_115",  # "meta_class"
            name="meta_class",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:type"]
        )
        class_meta.id = "meta:class"
        self.nodes["meta:class"] = class_meta
        
        # Meta-node describing "what is a property"
        property_meta = MetaCircularNode(
            symbol="109_101_116_97_95_112_114_111_112_101_114_116_121",  # "meta_property"
            name="meta_property",
            meta="meta:node",
            links=["meta:identity", "meta:node", "meta:link"]
        )
        property_meta.id = "meta:property"
        self.nodes["meta:property"] = property_meta
    
    def _initialize_relationship_meta_nodes(self):
        """
        Initialize meta-nodes that describe different types of relationships.
        """
        
        # Meta-node describing "what is an 'is_a' relationship"
        is_a_meta = MetaCircularNode(
            symbol="109_101_116_97_95_105_115_95_97",  # "meta_is_a"
            name="meta_is_a",
            meta="meta:link",
            links=["meta:identity", "meta:node", "meta:link", "meta:type"]
        )
        is_a_meta.id = "meta:is_a"
        self.nodes["meta:is_a"] = is_a_meta
        
        # Meta-node describing "what is a 'has_property' relationship"
        has_property_meta = MetaCircularNode(
            symbol="109_101_116_97_95_104_97_115_95_112_114_111_112",  # "meta_has_property"
            name="meta_has_property",
            meta="meta:link",
            links=["meta:identity", "meta:node", "meta:link", "meta:property"]
        )
        has_property_meta.id = "meta:has_property"
        self.nodes["meta:has_property"] = has_property_meta
        
        # Meta-node describing "what is a 'part_of' relationship"
        part_of_meta = MetaCircularNode(
            symbol="109_101_116_97_95_112_97_114_116_95_111_102",  # "meta_part_of"
            name="meta_part_of",
            meta="meta:link",
            links=["meta:identity", "meta:node", "meta:link"]
        )
        part_of_meta.id = "meta:part_of"
        self.nodes["meta:part_of"] = part_of_meta
        
        # Meta-node describing "what is a 'contains' relationship"
        contains_meta = MetaCircularNode(
            symbol="109_101_116_97_95_99_111_110_116_97_105_110_115",  # "meta_contains"
            name="meta_contains",
            meta="meta:link",
            links=["meta:identity", "meta:node", "meta:link"]
        )
        contains_meta.id = "meta:contains"
        self.nodes["meta:contains"] = contains_meta
        
        # Meta-node describing "what is a 'refers_to' relationship"
        refers_to_meta = MetaCircularNode(
            symbol="109_101_116_97_95_114_101_102_101_114_115_95_116_111",  # "meta_refers_to"
            name="meta_refers_to",
            meta="meta:link",
            links=["meta:identity", "meta:node", "meta:link"]
        )
        refers_to_meta.id = "meta:refers_to"
        self.nodes["meta:refers_to"] = refers_to_meta
    
    def _initialize_codex_meta_nodes(self):
        """
        Initialize meta-nodes that describe Living Codex specific concepts.
        """
        
        # Meta-node describing "what is a water state"
        water_state_meta = MetaCircularNode(
            symbol="109_101_116_97_95_119_97_116_101_114_95_115_116_97_116_101",  # "meta_water_state"
            name="meta_water_state",
            meta="meta:type",
            links=["meta:identity", "meta:node", "meta:type", "meta:property"]
        )
        water_state_meta.id = "meta:water_state"
        self.nodes["meta:water_state"] = water_state_meta
        
        # Meta-node describing "what is a chakra"
        chakra_meta = MetaCircularNode(
            symbol="109_101_116_97_95_99_104_97_107_114_97",  # "meta_chakra"
            name="meta_chakra",
            meta="meta:type",
            links=["meta:identity", "meta:node", "meta:type", "meta:property", "meta:number"]
        )
        chakra_meta.id = "meta:chakra"
        self.nodes["meta:chakra"] = chakra_meta
        
        # Meta-node describing "what is a planet"
        planet_meta = MetaCircularNode(
            symbol="109_101_116_97_95_112_108_97_110_101_116",  # "meta_planet"
            name="meta_planet",
            meta="meta:type",
            links=["meta:identity", "meta:node", "meta:type", "meta:property"]
        )
        planet_meta.id = "meta:planet"
        self.nodes["meta:planet"] = planet_meta
        
        # Meta-node describing "what is a frequency"
        frequency_meta = MetaCircularNode(
            symbol="109_101_116_97_95_102_114_101_113_117_101_110_99_121",  # "meta_frequency"
            name="meta_frequency",
            meta="meta:number",
            links=["meta:identity", "meta:node", "meta:number", "meta:property"]
        )
        frequency_meta.id = "meta:frequency"
        self.nodes["meta:frequency"] = frequency_meta
        
        # Meta-node describing "what is a color"
        color_meta = MetaCircularNode(
            symbol="109_101_116_97_95_99_111_108_111_114",  # "meta_color"
            name="meta_color",
            meta="meta:property",
            links=["meta:identity", "meta:node", "meta:property", "meta:symbol"]
        )
        color_meta.id = "meta:color"
        self.nodes["meta:color"] = color_meta
        
        # Meta-node describing "what is a codex core concept"
        codex_core_meta = MetaCircularNode(
            symbol="109_101_116_97_95_99_111_100_101_120_95_99_111_114_101",  # "meta_codex_core"
            name="meta_codex_core",
            meta="meta:type",
            links=["meta:identity", "meta:node", "meta:type", "meta:property"]
        )
        codex_core_meta.id = "meta:codex_core"
        self.nodes["meta:codex_core"] = codex_core_meta
    
    def create_meta_circular_node(self, symbol: str, name: str, meta_type: str, 
                                 links: List[str] = None, 
                                 description: str = None) -> str:
        """
        Create a new meta-circular node where every component is self-describing.
        """
        
        # Validate that meta_type exists
        if meta_type not in self.nodes:
            raise ValueError(f"Meta type '{meta_type}' not found in system")
        
        # Create the node
        node = MetaCircularNode(
            symbol=symbol,
            name=name,
            meta=meta_type,
            links=links or []
        )
        
        # Add standard links to foundational meta-nodes
        node.add_link("meta:identity")
        node.add_link("meta:node")
        
        # If description provided, create a description node
        if description:
            desc_node = MetaCircularNode(
                symbol=f"100_101_115_99_{symbol}",  # "desc_{symbol}"
                name=f"description_of_{name}",
                meta="meta:property",
                links=["meta:identity", "meta:node", "meta:property"]
            )
            desc_node.id = f"desc:{node.id}"
            self.nodes[f"desc:{node.id}"] = desc_node
            node.add_link(f"desc:{node.id}")
        
        # Store the node
        node_id = node.id
        self.nodes[node_id] = node
        return node_id
    
    def create_self_describing_symbol(self, text: str) -> str:
        """
        Create a symbol node that describes itself.
        """
        symbol_ascii = "_".join([str(ord(c)) for c in text])
        return self.create_meta_circular_node(
            symbol=symbol_ascii,
            name=f"symbol_{text}",
            meta_type="meta:symbol",
            description=f"Symbol representing the text '{text}' as ASCII codes"
        )
    
    def create_self_describing_name(self, text: str) -> str:
        """
        Create a name node that describes itself.
        """
        name_ascii = "_".join([str(ord(c)) for c in text])
        return self.create_meta_circular_node(
            symbol=name_ascii,
            name=f"name_{text}",
            meta_type="meta:name",
            description=f"Name representing the human-readable text '{text}'"
        )
    
    def create_self_describing_link(self, source_id: str, target_id: str, 
                                   relationship_type: str) -> str:
        """
        Create a link node that describes itself and the relationship.
        """
        link_symbol = f"108_105_110_107_{source_id}_{relationship_type}_{target_id}"
        return self.create_meta_circular_node(
            symbol=link_symbol,
            name=f"link_{source_id}_to_{target_id}",
            meta_type=f"meta:{relationship_type}",
            links=[source_id, target_id],
            description=f"Link from {source_id} to {target_id} via {relationship_type}"
        )
    
    def get_meta_description(self, node_id: str) -> Dict[str, Any]:
        """
        Get the complete meta-description of a node.
        """
        node = self.nodes.get(node_id)
        if not node:
            return {"error": "Node not found"}
        
        # Get the meta-node that describes this node's type
        meta_node = self.nodes.get(node.meta)
        
        result = {
            "node": {
                "id": node_id,
                "symbol": node.symbol,
                "name": node.name,
                "meta": node.meta,
                "links": node.links
            },
            "meta_description": {
                "described_by": meta_node.model_dump() if meta_node else None,
                "symbol_means": "Symbolic representation using ASCII codes",
                "name_means": "Human-readable identifier for the concept",
                "meta_means": "Reference to meta-node describing this node's type/structure",
                "links_means": "References to other nodes this node connects to"
            },
            "structure_explanation": {
                "symbol": f"The symbol '{node.symbol}' represents the ASCII codes for the concept",
                "name": f"The name '{node.name}' is the human-readable label",
                "meta": f"The meta '{node.meta}' points to the node that describes what this type of node IS",
                "links": f"The links {node.links} connect this node to {len(node.links)} other nodes"
            }
        }
        
        return result
    
    def get_system_meta_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive statistics about the meta-circular system.
        """
        total_nodes = len(self.nodes)
        
        # Count nodes by meta type
        meta_counts = {}
        for node in self.nodes.values():
            meta = node.meta
            meta_counts[meta] = meta_counts.get(meta, 0) + 1
        
        # Count meta-nodes (nodes that describe other nodes)
        meta_node_count = sum(1 for node_id in self.nodes.keys() if node_id.startswith("meta:"))
        description_node_count = sum(1 for node_id in self.nodes.keys() if node_id.startswith("desc:"))
        
        # Find self-referential nodes
        self_referential = []
        for node_id, node in self.nodes.items():
            if node_id in node.links or node.meta == node_id:
                self_referential.append(node_id)
        
        return {
            "total_nodes": total_nodes,
            "meta_node_count": meta_node_count,
            "description_node_count": description_node_count,
            "self_referential_nodes": len(self_referential),
            "meta_type_distribution": meta_counts,
            "meta_foundations": [
                "meta:identity", "meta:node", "meta:symbol", "meta:name", 
                "meta:meta", "meta:link"
            ],
            "structural_meta_nodes": [
                "meta:seq", "meta:bag", "meta:char", "meta:word", "meta:number"
            ],
            "type_meta_nodes": [
                "meta:type", "meta:instance", "meta:class", "meta:property"
            ],
            "relationship_meta_nodes": [
                "meta:is_a", "meta:has_property", "meta:part_of", 
                "meta:contains", "meta:refers_to"
            ],
            "codex_meta_nodes": [
                "meta:water_state", "meta:chakra", "meta:planet", 
                "meta:frequency", "meta:color", "meta:codex_core"
            ],
            "self_referential_examples": self_referential[:5]
        }

# Test the meta-circular system
if __name__ == "__main__":
    print("Meta-Circular Living Codex System")
    print("=" * 50)
    
    # Create meta-circular storage
    storage = MetaCircularStorage()
    
    # Create some self-describing nodes
    print("\nCreating self-describing nodes...")
    
    # Create a self-describing symbol
    symbol_node_id = storage.create_self_describing_symbol("hello")
    print(f"Self-describing symbol created: {symbol_node_id}")
    
    # Create a self-describing name
    name_node_id = storage.create_self_describing_name("greeting")
    print(f"Self-describing name created: {name_node_id}")
    
    # Create a self-describing link
    link_node_id = storage.create_self_describing_link(symbol_node_id, name_node_id, "refers_to")
    print(f"Self-describing link created: {link_node_id}")
    
    # Show system statistics
    print("\nMeta-Circular System Statistics:")
    stats = storage.get_system_meta_stats()
    print(json.dumps(stats, indent=2))
    
    # Show meta-description of a node
    print(f"\nMeta-description of symbol node:")
    meta_desc = storage.get_meta_description(symbol_node_id)
    print(json.dumps(meta_desc, indent=2))
    
    print("\n" + "="*50)
    print("Meta-circular system successfully created!")
    print("Every node and link now has meta-nodes describing their structure.")
    print("The system is completely self-documenting and meta-circular.")
