#!/usr/bin/env python3
"""
Recursive Node System for Living Codex
Everything is a node, every component is a node, every relationship is a node.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import hashlib
import time
import json

class RecursiveNode(BaseModel):
    """
    The fundamental unit: everything is a node.
    Each component (symbol, name, meta, links) is itself a node.
    """
    
    # Core identity - each is a node reference
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

class RecursiveStorage:
    """
    Storage system for recursive nodes.
    Every node is stored by its ID, creating a self-referential graph.
    """
    
    def __init__(self, storage_path: str = "./recursive-storage"):
        self.storage_path = storage_path
        self.nodes: Dict[str, RecursiveNode] = {}
        self.node_cache: Dict[str, RecursiveNode] = {}
        
        # Initialize with fundamental node types
        self._initialize_fundamental_nodes()
    
    def _initialize_fundamental_nodes(self):
        """Initialize the most basic node types that everything else builds upon"""
        
        # Create fundamental type nodes first
        type_node = RecursiveNode(
            symbol="116_121_112_101",  # "type" in ASCII
            name="type",
            meta="fundamental_type",
            links=[]
        )
        type_node.id = "type"
        self.nodes["type"] = type_node
        
        # Create other fundamental nodes
        fundamental_types = {
            "node": RecursiveNode(
                symbol="110_111_100_101",  # "node" in ASCII
                name="node", 
                meta="fundamental_type",
                links=["type"]
            ),
            "link": RecursiveNode(
                symbol="108_105_110_107",  # "link" in ASCII
                name="link",
                meta="fundamental_type", 
                links=["type"]
            ),
            "symbol": RecursiveNode(
                symbol="115_121_109_98_111_108",  # "symbol" in ASCII
                name="symbol",
                meta="fundamental_type",
                links=["type"]
            ),
            "name": RecursiveNode(
                symbol="110_97_109_101",  # "name" in ASCII
                name="name",
                meta="fundamental_type",
                links=["type"]
            ),
            "meta": RecursiveNode(
                symbol="109_101_116_97",  # "meta" in ASCII
                name="meta",
                meta="fundamental_type",
                links=["type"]
            ),
            "character_type": RecursiveNode(
                symbol="99_104_97_114_97_99_116_101_114",  # "character" in ASCII
                name="character_type",
                meta="fundamental_type",
                links=["type"]
            ),
            "word_type": RecursiveNode(
                symbol="119_111_114_100",  # "word" in ASCII
                name="word_type",
                meta="fundamental_type",
                links=["type"]
            ),
            "sentence_type": RecursiveNode(
                symbol="115_101_110_116_101_110_99_101",  # "sentence" in ASCII
                name="sentence_type",
                meta="fundamental_type",
                links=["type"]
            )
        }
        
        # Store fundamental nodes
        for node_id, node in fundamental_types.items():
            node.id = node_id
            self.nodes[node_id] = node
    
    def create_node(self, symbol: str, name: str, meta: str, links: List[str] = None) -> str:
        """Create a new node and return its ID"""
        node = RecursiveNode(
            symbol=symbol,
            name=name,
            meta=meta,
            links=links or []
        )
        
        node_id = node.id
        self.nodes[node_id] = node
        return node_id
    
    def get_node(self, node_id: str) -> Optional[RecursiveNode]:
        """Get a node by ID"""
        return self.nodes.get(node_id)
    
    def get_node_by_name(self, name: str) -> Optional[RecursiveNode]:
        """Get a node by name (useful for fundamental types)"""
        for node in self.nodes.values():
            if node.name == name:
                return node
        return None
    
    def create_character_node(self, char: str) -> str:
        """Create a node representing a single character"""
        ascii_val = str(ord(char))
        return self.create_node(
            symbol=ascii_val,
            name=char,
            meta="character",
            links=["character_type"]
        )
    
    def create_word_node(self, word: str) -> str:
        """Create a node representing a word"""
        # Create character nodes for each character
        char_nodes = []
        for char in word:
            char_node_id = self.create_character_node(char)
            char_nodes.append(char_node_id)
        
        # Create word node
        word_encoding = "_".join([str(ord(c)) for c in word])
        word_node_id = self.create_node(
            symbol=word_encoding,
            name=word,
            meta="word",
            links=char_nodes + ["word_type"]
        )
        
        return word_node_id
    
    def create_sentence_node(self, sentence: str) -> str:
        """Create a node representing a sentence"""
        # Split into words and create word nodes
        words = sentence.split()
        word_nodes = []
        for word in words:
            word_node_id = self.create_word_node(word)
            word_nodes.append(word_node_id)
        
        # Create sentence node
        sentence_encoding = "_".join([str(ord(c)) for c in sentence])
        sentence_node_id = self.create_node(
            symbol=sentence_encoding,
            name=sentence,
            meta="sentence",
            links=word_nodes + ["sentence_type"]
        )
        
        return sentence_node_id
    
    def create_link_node(self, source_id: str, target_id: str, relationship_type: str) -> str:
        """Create a link node connecting two nodes"""
        link_encoding = f"link_{source_id}_{target_id}_{relationship_type}"
        link_node_id = self.create_node(
            symbol=link_encoding,
            name=f"link_{relationship_type}",
            meta="link",
            links=[source_id, target_id, relationship_type]
        )
        
        # Add this link to both source and target nodes
        source_node = self.get_node(source_id)
        target_node = self.get_node(target_id)
        
        if source_node:
            source_node.add_link(link_node_id)
        if target_node:
            target_node.add_link(link_node_id)
        
        return link_node_id
    
    def get_node_network(self, node_id: str, depth: int = 2) -> Dict[str, Any]:
        """Get a node and its network up to specified depth"""
        if depth <= 0:
            return {"id": node_id, "depth": 0}
        
        node = self.get_node(node_id)
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
    
    def search_nodes(self, query: str, search_type: str = "name") -> List[str]:
        """Search for nodes by various criteria"""
        results = []
        query_lower = query.lower()
        
        for node_id, node in self.nodes.items():
            if search_type == "name" and query_lower in node.name.lower():
                results.append(node_id)
            elif search_type == "meta" and query_lower in node.meta.lower():
                results.append(node_id)
            elif search_type == "symbol" and query in node.symbol:
                results.append(node_id)
        
        return results
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get statistics about the storage system"""
        total_nodes = len(self.nodes)
        
        # Count nodes by meta type
        meta_counts = {}
        for node in self.nodes.values():
            meta = node.meta
            meta_counts[meta] = meta_counts.get(meta, 0) + 1
        
        return {
            "total_nodes": total_nodes,
            "meta_type_counts": meta_counts,
            "fundamental_types": ["type", "node", "link", "symbol", "name", "meta"],
            "storage_path": self.storage_path
        }

# Example usage and testing
if __name__ == "__main__":
    print("Recursive Node System Demo")
    print("=" * 40)
    
    # Create storage
    storage = RecursiveStorage()
    
    # Create a simple example
    print("Creating character nodes...")
    char_a = storage.create_character_node("A")
    char_b = storage.create_character_node("B")
    
    print("Creating word node...")
    word_ab = storage.create_word_node("AB")
    
    print("Creating link between characters...")
    link_ab = storage.create_link_node(char_a, char_b, "follows")
    
    print("Creating sentence node...")
    sentence = storage.create_sentence_node("A B")
    
    print("\nStorage Statistics:")
    stats = storage.get_storage_stats()
    print(json.dumps(stats, indent=2))
    
    print("\nNode Network Example (char A):")
    network = storage.get_node_network(char_a, depth=2)
    print(json.dumps(network, indent=2))
    
    print("\nSearch Results:")
    search_results = storage.search_nodes("A", "name")
    print(f"Nodes with 'A' in name: {search_results}")
