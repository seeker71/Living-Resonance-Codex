#!/usr/bin/env python3
"""
Generic Node System - Living Codex Foundation
=============================================

This implements the core Living Codex principle: "Everything is just nodes"
- No predefined concepts, tables, or schemas
- Structure itself is represented as nodes
- Infinite flexibility and extensibility
- Meta-circular self-reference capability
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional
from datetime import datetime
import hashlib

@dataclass
class GenericNode:
    """
    Generic Node Structure - The Foundation of Everything
    
    This implements the core Living Codex principle: "Everything is just nodes"
    """
    node_id: str                    # Unique identifier
    node_type: str                  # What it represents (determined by metadata)
    name: str                       # Human-readable name
    content: str                    # Actual content (can be anything)
    parent_id: Optional[str]        # Parent node (for hierarchical structure)
    children: List[str]             # Child node IDs (for hierarchical structure)
    metadata: Dict[str, Any]        # Flexible, extensible properties
    structure_info: Dict[str, Any]  # Fractal and structural properties
    created_at: str                 # Creation timestamp
    updated_at: str                 # Last update timestamp
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for storage/transmission"""
        return asdict(self)
    
    def to_node(self) -> 'GenericNode':
        """Meta-circular: this node can represent itself"""
        return self
    
    def get_fractal_depth(self) -> int:
        """Calculate fractal depth based on parent relationships"""
        if not self.parent_id:
            return 0
        return 1  # In a real implementation, this would traverse up the tree
    
    def get_water_state(self) -> str:
        """Get water state from metadata"""
        return self.metadata.get('water_state', 'liquid')
    
    def get_fractal_layer(self) -> int:
        """Get fractal layer from metadata"""
        return self.metadata.get('fractal_layer', 7)
    
    def get_chakra(self) -> str:
        """Get chakra from metadata"""
        return self.metadata.get('chakra', 'heart')
    
    def get_frequency(self) -> int:
        """Get frequency from metadata"""
        return self.metadata.get('frequency', 639)
    
    def get_color(self) -> str:
        """Get color from metadata"""
        return self.metadata.get('color', '#32CD32')
    
    def get_planet(self) -> str:
        """Get planet from metadata"""
        return self.metadata.get('planet', 'Moon')

class NodeSystem:
    """Basic node management system"""
    
    def __init__(self):
        self.nodes: Dict[str, GenericNode] = {}
        self.node_counter = 0
    
    def create_node(self, node_type: str, name: str, content: str, 
                   parent_id: Optional[str] = None, metadata: Optional[Dict] = None) -> GenericNode:
        """Create a new node"""
        self.node_counter += 1
        node_id = f"node_{self.node_counter:06d}"
        
        if metadata is None:
            metadata = {}
        
        structure_info = {
            'fractal_depth': 0 if not parent_id else 1,
            'node_type': node_type,
            'parent_id': parent_id,
            'children_count': 0
        }
        
        node = GenericNode(
            node_id=node_id,
            node_type=node_type,
            name=name,
            content=content,
            parent_id=parent_id,
            children=[],
            metadata=metadata,
            structure_info=structure_info,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        
        self.nodes[node_id] = node
        
        if parent_id and parent_id in self.nodes:
            self.nodes[parent_id].children.append(node_id)
        
        return node
    
    def get_node(self, node_id: str) -> Optional[GenericNode]:
        """Get a node by ID"""
        return self.nodes.get(node_id)
    
    def list_nodes(self, node_type: Optional[str] = None) -> List[GenericNode]:
        """List nodes, optionally filtered by type"""
        if node_type:
            return [node for node in self.nodes.values() if node.node_type == node_type]
        return list(self.nodes.values())
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get system status"""
        return {
            'total_nodes': len(self.nodes),
            'node_types': list(set(node.node_type for node in self.nodes.values())),
            'system_principle': 'Everything is just nodes - no predefined concepts, tables, or schemas'
        }
