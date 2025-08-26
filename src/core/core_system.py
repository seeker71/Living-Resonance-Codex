#!/usr/bin/env python3
"""
Living Codex Core System - Fractal Holographic Architecture
Following the Living Codex specification principles:
- Everything is just nodes
- Fractal self-similarity at every level
- Meta-circular self-description
- Generic node structure with infinite flexibility
"""

import logging
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timezone
from dataclasses import dataclass, field
import hashlib
import json

logger = logging.getLogger(__name__)

@dataclass
class GenericNode:
    """
    Generic node structure following Living Codex principles
    Everything is just nodes - including structure itself
    """
    node_id: str
    node_type: str  # What it represents (can be anything)
    name: str       # Human-readable name
    content: str    # Actual content/description
    parent_id: Optional[str] = None
    children: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    structure_info: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    
    def __post_init__(self):
        """Generate ID if not provided"""
        if not self.node_id:
            content_hash = f"{self.node_type}:{self.name}:{self.content}"
            self.node_id = hashlib.sha256(content_hash.encode()).hexdigest()[:16]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            'node_id': self.node_id,
            'node_type': self.node_type,
            'name': self.name,
            'content': self.content,
            'parent_id': self.parent_id,
            'children': self.children,
            'metadata': self.metadata,
            'structure_info': self.structure_info,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GenericNode':
        """Create from dictionary representation"""
        # Handle datetime conversion
        created_at = datetime.fromisoformat(data['created_at']) if isinstance(data['created_at'], str) else data['created_at']
        updated_at = datetime.fromisoformat(data['updated_at']) if isinstance(data['updated_at'], str) else data['updated_at']
        
        return cls(
            node_id=data['node_id'],
            node_type=data['node_type'],
            name=data['name'],
            content=data['content'],
            parent_id=data.get('parent_id'),
            children=data.get('children', []),
            metadata=data.get('metadata', {}),
            structure_info=data.get('structure_info', {}),
            created_at=created_at,
            updated_at=updated_at
        )


class FractalCoreSystem:
    """
    Fractal core system following Living Codex principles
    - Single table architecture (everything in nodes)
    - Fractal self-similarity at every level
    - Meta-circular self-description
    - Generic operations with infinite flexibility
    """
    
    def __init__(self):
        self.nodes: Dict[str, GenericNode] = {}  # Single table for everything
        self.components: Dict[str, Any] = {}     # Component registry
        self._initialize_fractal_system()
    
    def _initialize_fractal_system(self):
        """Initialize the fractal system with self-describing nodes"""
        logger.info("Initializing fractal core system...")
        
        # Create the system root node (fractal layer 0)
        system_root = GenericNode(
            node_id="fractal_system_root",
            node_type="system_root",
            name="Living Codex Fractal System",
            content="Root of the fractal holographic system - everything is just nodes",
            metadata={
                "fractal_layer": 0,
                "water_state": "ice",
                "frequency": 963,
                "chakra": "crown",
                "is_system_root": True
            },
            structure_info={
                "fractal_depth": 0,
                "self_similar": True,
                "meta_circular": True,
                "holographic": True,
                "system_definition": "self"
            }
        )
        
        # Create meta-implementation node (fractal layer 1)
        meta_implementation = GenericNode(
            node_id="meta_implementation",
            node_type="meta_implementation",
            name="Meta Implementation Layer",
            content="Layer that defines how the system itself is implemented",
            parent_id="fractal_system_root",
            metadata={
                "fractal_layer": 1,
                "water_state": "ice",
                "frequency": 852,
                "chakra": "third_eye",
                "is_meta_layer": True
            },
            structure_info={
                "fractal_depth": 1,
                "self_similar": True,
                "meta_circular": True,
                "holographic": True,
                "defines": "system_implementation"
            }
        )
        
        # Create system definition node (fractal layer 1)
        system_definition = GenericNode(
            node_id="system_definition",
            node_type="system_definition",
            name="System Definition Layer",
            content="Layer that defines what the system is and how it works",
            parent_id="fractal_system_root",
            metadata={
                "fractal_layer": 1,
                "water_state": "ice",
                "frequency": 741,
                "chakra": "throat",
                "is_definition_layer": True
            },
            structure_info={
                "fractal_depth": 1,
                "self_similar": True,
                "meta_circular": True,
                "holographic": True,
                "defines": "system_identity"
            }
        )
        
        # Register the core nodes
        self._register_node(system_root)
        self._register_node(meta_implementation)
        self._register_node(system_definition)
        
        # Update root children
        system_root.children = ["meta_implementation", "system_definition"]
        
        logger.info("Fractal core system initialized with root nodes")
    
    def _register_node(self, node: GenericNode):
        """Register a node in the fractal system"""
        self.nodes[node.node_id] = node
        logger.debug(f"Registered node: {node.node_id} ({node.node_type})")
    
    def register_component(self, name: str, component: Any):
        """Register a component with the core system"""
        self.components[name] = component
        logger.info(f"Registered component: {name}")
    
    def register_nodes(self, nodes_data: Dict[str, Dict[str, Any]]):
        """Register multiple nodes from a data dictionary"""
        for node_id, node_data in nodes_data.items():
            # Convert the data to GenericNode format
            node = GenericNode(
                node_id=node_id,
                node_type=node_data.get('type', 'generic'),
                name=node_data.get('title', node_id),
                content=node_data.get('content', ''),
                metadata={
                    'source': node_data.get('source', 'core_system'),
                    'category': node_data.get('category', 'generic'),
                    **node_data.get('metadata', {})
                },
                created_at=node_data.get('created_at', datetime.now(timezone.utc)),
                updated_at=node_data.get('updated_at', datetime.now(timezone.utc))
            )
            self._register_node(node)
        
        logger.info(f"Registered {len(nodes_data)} nodes with core system")
    
    def get_node(self, node_id: str) -> Optional[GenericNode]:
        """Get a node by ID"""
        return self.nodes.get(node_id)
    
    def get_nodes_by_type(self, node_type: str) -> List[GenericNode]:
        """Get all nodes of a specific type"""
        return [node for node in self.nodes.values() if node.node_type == node_type]
    
    def get_nodes_by_metadata(self, key: str, value: Any) -> List[GenericNode]:
        """Get nodes by metadata key-value pair"""
        return [node for node in self.nodes.values() if node.metadata.get(key) == value]
    
    def create_node(self, node_type: str, name: str, content: str, 
                   parent_id: Optional[str] = None, metadata: Dict[str, Any] = None,
                   structure_info: Dict[str, Any] = None) -> GenericNode:
        """Create and register a new node"""
        # Generate unique ID
        node_id = f"{node_type}_{name.lower().replace(' ', '_')}_{hash(content) % 10000}"
        
        node = GenericNode(
            node_id=node_id,
            node_type=node_type,
            name=name,
            content=content,
            parent_id=parent_id,
            metadata=metadata or {},
            structure_info=structure_info or {}
        )
        
        self._register_node(node)
        
        # Update parent's children list
        if parent_id and parent_id in self.nodes:
            if node_id not in self.nodes[parent_id].children:
                self.nodes[parent_id].children.append(node_id)
        
        return node
    
    def update_node(self, node_id: str, updates: Dict[str, Any]) -> bool:
        """Update a node's properties"""
        if node_id not in self.nodes:
            return False
        
        node = self.nodes[node_id]
        for key, value in updates.items():
            if hasattr(node, key):
                setattr(node, key, value)
        
        node.updated_at = datetime.now(timezone.utc)
        return True
    
    def delete_node(self, node_id: str) -> bool:
        """Delete a node from the system"""
        if node_id not in self.nodes:
            return False
        
        node = self.nodes[node_id]
        
        # Remove from parent's children list
        if node.parent_id and node.parent_id in self.nodes:
            if node_id in self.nodes[node.parent_id].children:
                self.nodes[node.parent_id].children.remove(node_id)
        
        # Remove the node
        del self.nodes[node_id]
        return True
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            'total_nodes': len(self.nodes),
            'component_count': len(self.components),
            'node_types': list(set(node.node_type for node in self.nodes.values())),
            'fractal_layers': list(set(node.metadata.get('fractal_layer', 0) for node in self.nodes.values())),
            'water_states': list(set(node.metadata.get('water_state', 'unknown') for node in self.nodes.values())),
            'frequencies': list(set(node.metadata.get('frequency', 0) for node in self.nodes.values())),
            'chakras': list(set(node.metadata.get('chakra', 'unknown') for node in self.nodes.values())),
            'components': list(self.components.keys())
        }
    
    def search_nodes(self, query: str, node_type: Optional[str] = None) -> List[GenericNode]:
        """Search nodes by content, name, or metadata"""
        results = []
        query_lower = query.lower()
        
        for node in self.nodes.values():
            # Skip if type filter doesn't match
            if node_type and node.node_type != node_type:
                continue
            
            # Search in name, content, and metadata
            if (query_lower in node.name.lower() or 
                query_lower in node.content.lower() or
                any(query_lower in str(v).lower() for v in node.metadata.values())):
                results.append(node)
        
        return results
    
    def get_node_hierarchy(self, node_id: str, max_depth: int = 3) -> Dict[str, Any]:
        """Get the hierarchical structure around a node"""
        if node_id not in self.nodes:
            return {}
        
        def build_hierarchy(current_id: str, depth: int = 0) -> Dict[str, Any]:
            if depth > max_depth or current_id not in self.nodes:
                return {}
            
            node = self.nodes[current_id]
            hierarchy = {
                'node_id': current_id,
                'name': node.name,
                'type': node.node_type,
                'content': node.content[:100] + '...' if len(node.content) > 100 else node.content,
                'children': []
            }
            
            # Add children (limited depth)
            for child_id in node.children[:10]:  # Limit to 10 children
                child_hierarchy = build_hierarchy(child_id, depth + 1)
                if child_hierarchy:
                    hierarchy['children'].append(child_hierarchy)
            
            return hierarchy
        
        return build_hierarchy(node_id)
    
    def export_system(self, filepath: str) -> bool:
        """Export the entire system to a JSON file"""
        try:
            export_data = {
                'exported_at': datetime.now(timezone.utc).isoformat(),
                'system_version': '1.0.0',
                'nodes': {node_id: node.to_dict() for node_id, node in self.nodes.items()},
                'components': list(self.components.keys())
            }
            
            with open(filepath, 'w') as f:
                json.dump(export_data, f, indent=2, default=str)
            
            logger.info(f"System exported to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to export system: {e}")
            return False
    
    def import_system(self, filepath: str) -> bool:
        """Import a system from a JSON file"""
        try:
            with open(filepath, 'r') as f:
                import_data = json.load(f)
            
            # Import nodes
            for node_id, node_data in import_data.get('nodes', {}).items():
                node = GenericNode.from_dict(node_data)
                self._register_node(node)
            
            logger.info(f"System imported from {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to import system: {e}")
            return False


# Global instance of the fractal core system
fractal_core_system = FractalCoreSystem()

# Legacy alias for backward compatibility
core_system = fractal_core_system
