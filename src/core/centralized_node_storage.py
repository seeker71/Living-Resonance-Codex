#!/usr/bin/env python3
"""
Centralized Node Storage - Living Codex Single Storage Point

This implements the Living Codex principle: "Everything is just nodes"
by providing a single, centralized storage point for all nodes across all components.

Key Principles:
1. Single Storage Point - All nodes stored in one location
2. Single Interface - One consistent way to access and manage nodes
3. No Duplication - Each node exists only once
4. Shared Access - All components can access all nodes
5. Centralized Management - One place to manage the entire node universe

This ensures that the Living Codex system truly embodies "Everything is just nodes"
rather than "Everything is separate node systems."
"""

import threading
import time
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib
import json

from .generic_node_system import GenericNode

@dataclass
class NodeStorageMetrics:
    """Metrics for the centralized node storage system"""
    total_nodes: int
    nodes_by_type: Dict[str, int]
    nodes_by_water_state: Dict[str, int]
    nodes_by_fractal_layer: Dict[int, int]
    nodes_by_chakra: Dict[str, int]
    storage_size_bytes: int
    last_updated: str
    component_access_count: Dict[str, int]

class CentralizedNodeStorage:
    """
    Centralized Node Storage System
    
    This is the single storage point for all nodes in the Living Codex system.
    All components share this storage, ensuring no duplication and consistent access.
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Singleton pattern to ensure only one storage instance exists"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the centralized storage system"""
        if hasattr(self, '_initialized'):
            return
        
        self._initialized = True
        self._nodes: Dict[str, GenericNode] = {}
        self._node_counter = 0
        self._component_access: Dict[str, int] = {}
        self._node_type_index: Dict[str, Set[str]] = {}
        self._water_state_index: Dict[str, Set[str]] = {}
        self._fractal_layer_index: Dict[int, Set[str]] = {}
        self._chakra_index: Dict[str, Set[str]] = {}
        self._parent_child_index: Dict[str, Set[str]] = {}
        
        # Initialize indexes
        self._initialize_indexes()
        
        print("🌟 Centralized Node Storage initialized")
        print("✨ Single storage point for all Living Codex nodes")
        print("🔗 All components will share this storage")
        print("🚫 No node duplication allowed")
    
    def _initialize_indexes(self):
        """Initialize all indexing structures"""
        self._node_type_index = {}
        self._water_state_index = {}
        self._fractal_layer_index = {}
        self._chakra_index = {}
        self._parent_child_index = {}
    
    def _update_indexes(self, node: GenericNode, operation: str = "add"):
        """Update all indexes when nodes are added/removed/modified"""
        if operation == "add":
            # Update type index
            if node.node_type not in self._node_type_index:
                self._node_type_index[node.node_type] = set()
            self._node_type_index[node.node_type].add(node.node_id)
            
            # Update water state index
            water_state = node.metadata.get('water_state', 'liquid')
            if water_state not in self._water_state_index:
                self._water_state_index[water_state] = set()
            self._water_state_index[water_state].add(node.node_id)
            
            # Update fractal layer index
            fractal_layer = node.metadata.get('fractal_layer', 7)
            if fractal_layer not in self._fractal_layer_index:
                self._fractal_layer_index[fractal_layer] = set()
            self._fractal_layer_index[fractal_layer].add(node.node_id)
            
            # Update chakra index
            chakra = node.metadata.get('chakra', 'heart')
            if chakra not in self._chakra_index:
                self._chakra_index[chakra] = set()
            self._chakra_index[chakra].add(node.node_id)
            
            # Update parent-child index
            if node.parent_id:
                if node.parent_id not in self._parent_child_index:
                    self._parent_child_index[node.parent_id] = set()
                self._parent_child_index[node.parent_id].add(node.node_id)
        
        elif operation == "remove":
            # Remove from all indexes
            if node.node_type in self._node_type_index:
                self._node_type_index[node.node_type].discard(node.node_id)
            
            water_state = node.metadata.get('water_state', 'liquid')
            if water_state in self._water_state_index:
                self._water_state_index[water_state].discard(node.node_id)
            
            fractal_layer = node.metadata.get('fractal_layer', 7)
            if fractal_layer in self._fractal_layer_index:
                self._fractal_layer_index[fractal_layer].discard(node.node_id)
            
            chakra = node.metadata.get('chakra', 'heart')
            if chakra in self._chakra_index:
                self._chakra_index[chakra].discard(node.node_id)
            
            if node.parent_id and node.parent_id in self._parent_child_index:
                self._parent_child_index[node.parent_id].discard(node.node_id)
    
    def create_node(self, node_type: str, name: str, content: str, 
                   parent_id: Optional[str] = None, metadata: Optional[Dict] = None,
                   component_name: str = "unknown") -> GenericNode:
        """Create a new node in the centralized storage"""
        with self._lock:
            self._node_counter += 1
            node_id = f"node_{self._node_counter:06d}"
            
            if metadata is None:
                metadata = {}
            
            # Ensure required metadata fields exist
            if 'water_state' not in metadata:
                metadata['water_state'] = 'liquid'
            if 'fractal_layer' not in metadata:
                metadata['fractal_layer'] = 7
            if 'chakra' not in metadata:
                metadata['chakra'] = 'heart'
            if 'frequency' not in metadata:
                metadata['frequency'] = 639
            if 'color' not in metadata:
                metadata['color'] = '#32CD32'
            if 'planet' not in metadata:
                metadata['planet'] = 'Moon'
            if 'consciousness_mode' not in metadata:
                metadata['consciousness_mode'] = 'Flow, Adaptation'
            if 'quantum_state' not in metadata:
                metadata['quantum_state'] = 'coherent'
            if 'resonance_score' not in metadata:
                metadata['resonance_score'] = 1.0
            if 'epistemic_label' not in metadata:
                metadata['epistemic_label'] = 'general'
            if 'programming_ontology_layer' not in metadata:
                metadata['programming_ontology_layer'] = 'general'
            
            structure_info = {
                'fractal_depth': 0 if not parent_id else 1,
                'node_type': node_type,
                'parent_id': parent_id,
                'children_count': 0,
                'created_by_component': component_name,
                'created_at_timestamp': time.time()
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
            
            # Store the node
            self._nodes[node_id] = node
            
            # Update indexes
            self._update_indexes(node, "add")
            
            # Update component access count
            self._component_access[component_name] = self._component_access.get(component_name, 0) + 1
            
            return node
    
    def get_node(self, node_id: str) -> Optional[GenericNode]:
        """Get a node by ID"""
        return self._nodes.get(node_id)
    
    def get_nodes_by_type(self, node_type: str) -> List[GenericNode]:
        """Get all nodes of a specific type"""
        node_ids = self._node_type_index.get(node_type, set())
        return [self._nodes[node_id] for node_id in node_ids if node_id in self._nodes]
    
    def get_nodes_by_water_state(self, water_state: str) -> List[GenericNode]:
        """Get all nodes with a specific water state"""
        node_ids = self._water_state_index.get(water_state, set())
        return [self._nodes[node_id] for node_id in node_ids if node_id in self._nodes]
    
    def get_nodes_by_fractal_layer(self, fractal_layer: int) -> List[GenericNode]:
        """Get all nodes with a specific fractal layer"""
        node_ids = self._fractal_layer_index.get(fractal_layer, set())
        return [self._nodes[node_id] for node_id in node_ids if node_id in self._nodes]
    
    def get_nodes_by_chakra(self, chakra: str) -> List[GenericNode]:
        """Get all nodes with a specific chakra"""
        node_ids = self._chakra_index.get(chakra, set())
        return [self._nodes[node_id] for node_id in node_ids if node_id in self._nodes]
    
    def get_children(self, parent_id: str) -> List[GenericNode]:
        """Get all children of a specific parent node"""
        child_ids = self._parent_child_index.get(parent_id, set())
        return [self._nodes[child_id] for child_id in child_ids if child_id in self._nodes]
    
    def get_parent(self, node_id: str) -> Optional[GenericNode]:
        """Get the parent of a specific node"""
        node = self._nodes.get(node_id)
        if node and node.parent_id:
            return self._nodes.get(node.parent_id)
        return None
    
    def update_node(self, node_id: str, updates: Dict[str, Any], component_name: str = "unknown") -> Optional[GenericNode]:
        """Update an existing node"""
        with self._lock:
            node = self._nodes.get(node_id)
            if not node:
                return None
            
            # Update fields
            for key, value in updates.items():
                if hasattr(node, key):
                    setattr(node, key, value)
            
            # Update timestamp
            node.updated_at = datetime.now().isoformat()
            
            # Update structure info
            if 'updated_by_component' not in node.structure_info:
                node.structure_info['updated_by_component'] = []
            node.structure_info['updated_by_component'].append({
                'component': component_name,
                'timestamp': time.time(),
                'updates': list(updates.keys())
            })
            
            # Update indexes if metadata changed
            if 'metadata' in updates:
                self._update_indexes(node, "remove")
                self._update_indexes(node, "add")
            
            # Update component access count
            self._component_access[component_name] = self._component_access.get(component_name, 0) + 1
            
            return node
    
    def delete_node(self, node_id: str, component_name: str = "unknown") -> bool:
        """Delete a node"""
        with self._lock:
            node = self._nodes.get(node_id)
            if not node:
                return False
            
            # Remove from indexes
            self._update_indexes(node, "remove")
            
            # Remove the node
            del self._nodes[node_id]
            
            # Update component access count
            self._component_access[component_name] = self._component_access.get(component_name, 0) + 1
            
            return True
    
    def search_nodes(self, query: str, search_fields: List[str] = None) -> List[GenericNode]:
        """Search nodes by content in specified fields"""
        if search_fields is None:
            search_fields = ['name', 'content']
        
        results = []
        query_lower = query.lower()
        
        for node in self._nodes.values():
            for field in search_fields:
                if hasattr(node, field):
                    field_value = getattr(node, field)
                    if isinstance(field_value, str) and query_lower in field_value.lower():
                        results.append(node)
                        break
        
        return results
    
    def get_storage_metrics(self) -> NodeStorageMetrics:
        """Get comprehensive storage metrics"""
        nodes_by_type = {}
        nodes_by_water_state = {}
        nodes_by_fractal_layer = {}
        nodes_by_chakra = {}
        
        for node in self._nodes.values():
            # Count by type
            node_type = node.node_type
            nodes_by_type[node_type] = nodes_by_type.get(node_type, 0) + 1
            
            # Count by water state
            water_state = node.metadata.get('water_state', 'liquid')
            nodes_by_water_state[water_state] = nodes_by_water_state.get(water_state, 0) + 1
            
            # Count by fractal layer
            fractal_layer = node.metadata.get('fractal_layer', 7)
            nodes_by_fractal_layer[fractal_layer] = nodes_by_fractal_layer.get(fractal_layer, 0) + 1
            
            # Count by chakra
            chakra = node.metadata.get('chakra', 'heart')
            nodes_by_chakra[chakra] = nodes_by_chakra.get(chakra, 0) + 1
        
        # Calculate storage size
        storage_size = len(json.dumps([node.to_dict() for node in self._nodes.values()]).encode('utf-8'))
        
        return NodeStorageMetrics(
            total_nodes=len(self._nodes),
            nodes_by_type=nodes_by_type,
            nodes_by_water_state=nodes_by_water_state,
            nodes_by_fractal_layer=nodes_by_fractal_layer,
            nodes_by_chakra=nodes_by_chakra,
            storage_size_bytes=storage_size,
            last_updated=datetime.now().isoformat(),
            component_access_count=self._component_access.copy()
        )
    
    def get_all_nodes(self) -> Dict[str, GenericNode]:
        """Get all nodes (read-only access)"""
        return self._nodes.copy()
    
    def get_node_count(self) -> int:
        """Get total number of nodes"""
        return len(self._nodes)
    
    def clear_storage(self, component_name: str = "unknown"):
        """Clear all nodes (use with caution)"""
        with self._lock:
            self._nodes.clear()
            self._initialize_indexes()
            self._node_counter = 0
            self._component_access[component_name] = self._component_access.get(component_name, 0) + 1
            print("⚠️  Centralized Node Storage cleared by component:", component_name)
    
    def export_storage(self) -> Dict[str, Any]:
        """Export all storage data for backup/analysis"""
        return {
            'storage_metrics': self.get_storage_metrics(),
            'nodes': {node_id: node.to_dict() for node_id, node in self._nodes.items()},
            'indexes': {
                'node_type_index': {k: list(v) for k, v in self._node_type_index.items()},
                'water_state_index': {k: list(v) for k, v in self._water_state_index.items()},
                'fractal_layer_index': {k: list(v) for k, v in self._fractal_layer_index.items()},
                'chakra_index': {k: list(v) for k, v in self._chakra_index.items()},
                'parent_child_index': {k: list(v) for k, v in self._parent_child_index.items()}
            },
            'component_access': self._component_access.copy(),
            'export_timestamp': datetime.now().isoformat()
        }

# Global instance
centralized_storage = CentralizedNodeStorage()
