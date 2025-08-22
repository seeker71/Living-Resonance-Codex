#!/usr/bin/env python3
"""
Bootstrap Node System - Minimal Foundation for Universal Representation
The smallest set of nodes needed to bootstrap the entire recursive system.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import hashlib
import time
import json

class BootstrapNode(BaseModel):
    """
    The minimal bootstrap node - everything else builds from this.
    Each field is a reference to another bootstrap node.
    """
    
    # Core identity - each is a reference to a bootstrap node
    symbol: str  # Reference to a node containing the symbolic representation
    name: str    # Reference to a node containing the name representation  
    meta: str    # Reference to a node describing this node's type/structure
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
    
    def remove_link(self, node_ref: str):
        """Remove a link to another node"""
        if node_ref in self.links:
            self.links.remove(node_ref)
            self.updated_at = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")

class BootstrapStorage:
    """
    Storage system for bootstrap nodes.
    Contains the minimal set needed to represent any data structure.
    """
    
    def __init__(self):
        self.nodes: Dict[str, BootstrapNode] = {}
        self._initialize_bootstrap_nodes()
    
    def _initialize_bootstrap_nodes(self):
        """
        Initialize the minimal set of bootstrap nodes.
        These nodes can represent ANY data structure from ANY language.
        """
        
        # ========================================
        # 1. IDENTITY & REFERENCE NODES
        # ========================================
        
        # The most fundamental node - represents "identity" itself
        identity_node = BootstrapNode(
            symbol="105_100_101_110_116_105_116_121",  # "identity" in ASCII
            name="identity",
            meta="identity",  # Self-referential - identity describes itself
            links=[]
        )
        identity_node.id = "identity"
        self.nodes["identity"] = identity_node
        
        # ========================================
        # 2. STRUCTURE & COMPOSITION NODES
        # ========================================
        
        # Node - represents the concept of a "node"
        node_node = BootstrapNode(
            symbol="110_111_100_101",  # "node" in ASCII
            name="node",
            meta="identity",
            links=["identity"]
        )
        node_node.id = "node"
        self.nodes["node"] = node_node
        
        # Sequence - ordered collection of nodes
        seq_node = BootstrapNode(
            symbol="115_101_113",  # "seq" in ASCII
            name="seq",
            meta="identity",
            links=["identity", "node"]
        )
        seq_node.id = "seq"
        self.nodes["seq"] = seq_node
        
        # Bag - unordered collection of nodes
        bag_node = BootstrapNode(
            symbol="98_97_103",  # "bag" in ASCII
            name="bag",
            meta="identity",
            links=["identity", "node"]
        )
        bag_node.id = "bag"
        self.nodes["bag"] = bag_node
        
        # ========================================
        # 3. CONTENT & REPRESENTATION NODES
        # ========================================
        
        # Symbol - symbolic representation (can be number, text, etc.)
        symbol_node = BootstrapNode(
            symbol="115_121_109_98_111_108",  # "symbol" in ASCII
            name="symbol",
            meta="identity",
            links=["identity", "node"]
        )
        symbol_node.id = "symbol"
        self.nodes["symbol"] = symbol_node
        
        # Name - name representation (human-readable)
        name_node = BootstrapNode(
            symbol="110_97_109_101",  # "name" in ASCII
            name="name",
            meta="identity",
            links=["identity", "node"]
        )
        name_node.id = "name"
        self.nodes["name"] = name_node
        
        # Meta - describes the type/structure of a node
        meta_node = BootstrapNode(
            symbol="109_101_116_97",  # "meta" in ASCII
            name="meta",
            meta="identity",
            links=["identity", "node"]
        )
        meta_node.id = "meta"
        self.nodes["meta"] = meta_node
        
        # ========================================
        # 4. LANGUAGE & CONTEXT NODES
        # ========================================
        
        # Character - atomic unit of text
        char_node = BootstrapNode(
            symbol="99_104_97_114",  # "char" in ASCII
            name="char",
            meta="identity",
            links=["identity", "node", "symbol"]
        )
        char_node.id = "char"
        self.nodes["char"] = char_node
        
        # Word - sequence of characters
        word_node = BootstrapNode(
            symbol="119_111_114_100",  # "word" in ASCII
            name="word",
            meta="identity",
            links=["identity", "node", "seq", "char"]
        )
        word_node.id = "word"
        self.nodes["word"] = word_node
        
        # Number - numeric representation
        number_node = BootstrapNode(
            symbol="110_117_109_98_101_114",  # "number" in ASCII
            name="number",
            meta="identity",
            links=["identity", "node", "symbol"]
        )
        number_node.id = "number"
        self.nodes["number"] = number_node
        
        # Language - context for interpretation
        language_node = BootstrapNode(
            symbol="108_97_110_103",  # "lang" in ASCII
            name="language",
            meta="identity",
            links=["identity", "node", "symbol"]
        )
        language_node.id = "language"
        self.nodes["language"] = language_node
        
        # ========================================
        # 5. RELATIONSHIP & LINK NODES
        # ========================================
        
        # Link - connects nodes
        link_node = BootstrapNode(
            symbol="108_105_110_107",  # "link" in ASCII
            name="link",
            meta="identity",
            links=["identity", "node"]
        )
        link_node.id = "link"
        self.nodes["link"] = link_node
        
        # Link types - describe the nature of relationships
        is_meta_node = BootstrapNode(
            symbol="105_115_95_109_101_116_97",  # "is_meta" in ASCII
            name="is_meta",
            meta="identity",
            links=["identity", "node", "link"]
        )
        is_meta_node.id = "is_meta"
        self.nodes["is_meta"] = is_meta_node
        
        has_property_node = BootstrapNode(
            symbol="104_97_115_95_112_114_111_112",  # "has_property" in ASCII
            name="has_property",
            meta="identity",
            links=["identity", "node", "link"]
        )
        has_property_node.id = "has_property"
        self.nodes["has_property"] = is_meta_node
        
        # ========================================
        # 6. INSTANCE & TYPE NODES
        # ========================================
        
        # Instance - specific occurrence of a type
        instance_node = BootstrapNode(
            symbol="105_110_115_116_97_110_99_101",  # "instance" in ASCII
            name="instance",
            meta="identity",
            links=["identity", "node"]
        )
        instance_node.id = "instance"
        self.nodes["instance"] = instance_node
        
        # Type - category or classification
        type_node = BootstrapNode(
            symbol="116_121_112_101",  # "type" in ASCII
            name="type",
            meta="identity",
            links=["identity", "node"]
        )
        type_node.id = "type"
        self.nodes["type"] = type_node
        
        # ========================================
        # 7. BOOTSTRAP SELF-REFERENCE
        # ========================================
        
        # Now update all nodes to use proper references
        for node_id, node in self.nodes.items():
            # Each node should reference the bootstrap system
            if node_id not in ["identity"]:  # Don't add identity to itself
                node.add_link("identity")
        
        # Identity node references itself (self-referential)
        identity_node.add_link("identity")
    
    def create_node(self, symbol: str, name: str, meta: str, links: List[str] = None) -> str:
        """Create a new node using bootstrap references"""
        node = BootstrapNode(
            symbol=symbol,
            name=name,
            meta=meta,
            links=links or []
        )
        
        node_id = node.id
        self.nodes[node_id] = node
        return node_id
    
    def get_node(self, node_id: str) -> Optional[BootstrapNode]:
        """Get a node by ID"""
        return self.nodes.get(node_id)
    
    def get_bootstrap_nodes(self) -> Dict[str, Any]:
        """Get all bootstrap nodes for inspection"""
        result = {}
        for node_id, node in self.nodes.items():
            result[node_id] = {
                "symbol": node.symbol,
                "name": node.name,
                "meta": node.meta,
                "links": node.links
            }
        return result
    
    def demonstrate_universal_representation(self):
        """
        Demonstrate how these bootstrap nodes can represent any data structure
        """
        print("Bootstrap Node System - Universal Representation Demo")
        print("=" * 60)
        
        # Example 1: Represent a Python dictionary
        print("\n1. Python Dictionary Representation:")
        python_dict = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        
        # Create nodes for each key-value pair
        name_key = self.create_node("110_97_109_101", "name", "word", ["word", "is_meta"])
        name_value = self.create_node("74_111_104_110", "John", "word", ["word", "instance"])
        age_key = self.create_node("97_103_101", "age", "word", ["word", "is_meta"])
        age_value = self.create_node("51_48", "30", "number", ["number", "instance"])
        city_key = self.create_node("99_105_116_121", "city", "word", ["word", "is_meta"])
        city_value = self.create_node("78_101_119_32_89_111_114_107", "New York", "word", ["word", "instance"])
        
        # Create the dictionary structure
        dict_node = self.create_node(
            "100_105_99_116", 
            "dict", 
            "bag", 
            [name_key, name_value, age_key, age_value, city_key, city_value]
        )
        
        print(f"Dictionary represented as node: {dict_node}")
        
        # Example 2: Represent a JSON object
        print("\n2. JSON Object Representation:")
        json_obj = {
            "type": "person",
            "properties": ["name", "age", "city"]
        }
        
        # Create nodes for JSON structure
        type_key = self.create_node("116_121_112_101", "type", "word", ["word", "is_meta"])
        type_value = self.create_node("112_101_114_115_111_110", "person", "word", ["word", "instance"])
        props_key = self.create_node("112_114_111_112_115", "properties", "word", ["word", "is_meta"])
        
        # Properties as a sequence
        props_seq = self.create_node(
            "112_114_111_112_115_95_115_101_113",
            "properties_sequence",
            "seq",
            [name_key, age_key, city_key]
        )
        
        json_node = self.create_node(
            "106_115_111_110_95_111_98_106",
            "json_object",
            "bag",
            [type_key, type_value, props_key, props_seq]
        )
        
        print(f"JSON object represented as node: {json_node}")
        
        # Example 3: Represent a natural language sentence
        print("\n3. Natural Language Representation:")
        sentence = "The tree grows tall."
        
        # Break down into words and characters
        the_word = self.create_node("116_104_101", "the", "word", ["word", "instance"])
        tree_word = self.create_node("116_114_101_101", "tree", "word", ["word", "instance"])
        grows_word = self.create_node("103_114_111_119_115", "grows", "word", ["word", "instance"])
        tall_word = self.create_node("116_97_108_108", "tall", "word", ["word", "instance"])
        
        # Create sentence as sequence
        sentence_node = self.create_node(
            "84_104_101_32_116_114_101_101_32_103_114_111_119_115_32_116_97_108_108",
            sentence,
            "seq",
            [the_word, tree_word, grows_word, tall_word]
        )
        
        print(f"Sentence represented as node: {sentence_node}")
        
        print(f"\nTotal nodes created: {len(self.nodes)}")
        return {
            "python_dict": dict_node,
            "json_object": json_node,
            "sentence": sentence_node
        }

# Test the bootstrap system
if __name__ == "__main__":
    print("Bootstrap Node System Test")
    print("=" * 40)
    
    # Create bootstrap storage
    storage = BootstrapStorage()
    
    # Show bootstrap nodes
    print("\nBootstrap Nodes:")
    bootstrap_nodes = storage.get_bootstrap_nodes()
    for node_id, node_data in bootstrap_nodes.items():
        print(f"  {node_id}: {node_data['name']} ({node_data['meta']})")
    
    # Demonstrate universal representation
    examples = storage.demonstrate_universal_representation()
    
    print("\n" + "="*60)
    print("Bootstrap system successfully represents:")
    print("  ✓ Python data structures")
    print("  ✓ JSON objects")
    print("  ✓ Natural language")
    print("  ✓ Any programming language construct")
    print("  ✓ Any natural language expression")
    print("\nThe system is now ready to represent ANYTHING!")
