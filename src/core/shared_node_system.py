#!/usr/bin/env python3
"""
Shared Node System - Living Codex Centralized Access

This implements the Living Codex principle: "Everything is just nodes"
by providing a shared base class that all components inherit from to access
the centralized node storage.

Key Benefits:
1. Single Storage Point - All components share the same storage
2. No Node Duplication - Each node exists only once
3. Consistent Interface - All components use the same methods
4. Shared Access - Components can see and interact with each other's nodes
5. Centralized Management - One place to manage all nodes

This ensures that the Living Codex system truly embodies "Everything is just nodes"
with a single, unified storage system.
"""

from typing import Dict, List, Any, Optional
from .centralized_node_storage import centralized_storage, NodeStorageMetrics

class SharedNodeSystem:
    """
    Shared Node System Base Class
    
    This is the base class that all Living Codex components inherit from.
    Instead of each component having its own node storage, they all share
    the centralized storage through this base class.
    
    This ensures:
    - No node duplication across components
    - Single storage point for all nodes
    - Consistent interface for all components
    - Shared access to all nodes
    """
    
    def __init__(self, component_name: str):
        """
        Initialize the shared node system
        
        Args:
            component_name: Name of the component using this system
        """
        self.component_name = component_name
        self.storage = centralized_storage
        
        print(f"🔗 {component_name} connected to centralized node storage")
    
    def create_node(self, node_type: str, name: str, content: str, 
                   parent_id: Optional[str] = None, metadata: Optional[Dict] = None) -> Any:
        """Create a new node in the centralized storage"""
        return self.storage.create_node(
            node_type=node_type,
            name=name,
            content=content,
            parent_id=parent_id,
            metadata=metadata,
            component_name=self.component_name
        )
    
    def get_node(self, node_id: str) -> Optional[Any]:
        """Get a node by ID from the centralized storage"""
        return self.storage.get_node(node_id)
    
    def get_nodes_by_type(self, node_type: str) -> List[Any]:
        """Get all nodes of a specific type from the centralized storage"""
        return self.storage.get_nodes_by_type(node_type)
    
    def get_nodes_by_water_state(self, water_state: str) -> List[Any]:
        """Get all nodes with a specific water state from the centralized storage"""
        return self.storage.get_nodes_by_water_state(water_state)
    
    def get_nodes_by_fractal_layer(self, fractal_layer: int) -> List[Any]:
        """Get all nodes with a specific fractal layer from the centralized storage"""
        return self.storage.get_nodes_by_fractal_layer(fractal_layer)
    
    def get_nodes_by_chakra(self, chakra: str) -> List[Any]:
        """Get all nodes with a specific chakra from the centralized storage"""
        return self.storage.get_nodes_by_chakra(chakra)
    
    def get_children(self, parent_id: str) -> List[Any]:
        """Get all children of a specific parent node from the centralized storage"""
        return self.storage.get_children(parent_id)
    
    def get_parent(self, node_id: str) -> Optional[Any]:
        """Get the parent of a specific node from the centralized storage"""
        return self.storage.get_parent(node_id)
    
    def update_node(self, node_id: str, updates: Dict[str, Any]) -> Optional[Any]:
        """Update an existing node in the centralized storage"""
        return self.storage.update_node(
            node_id=node_id,
            updates=updates,
            component_name=self.component_name
        )
    
    def delete_node(self, node_id: str) -> bool:
        """Delete a node from the centralized storage"""
        return self.storage.delete_node(
            node_id=node_id,
            component_name=self.component_name
        )
    
    def search_nodes(self, query: str, search_fields: List[str] = None) -> List[Any]:
        """Search nodes by content in specified fields from the centralized storage"""
        return self.storage.search_nodes(query, search_fields)
    
    def get_storage_metrics(self) -> NodeStorageMetrics:
        """Get comprehensive storage metrics from the centralized storage"""
        return self.storage.get_storage_metrics()
    
    def get_all_nodes(self) -> Dict[str, Any]:
        """Get all nodes from the centralized storage (read-only access)"""
        return self.storage.get_all_nodes()
    
    def get_node_count(self) -> int:
        """Get total number of nodes from the centralized storage"""
        return self.storage.get_node_count()
    
    def get_component_nodes(self) -> List[Any]:
        """Get all nodes created by this specific component"""
        all_nodes = self.storage.get_all_nodes()
        component_nodes = []
        
        for node in all_nodes.values():
            if (hasattr(node, 'structure_info') and 
                'created_by_component' in node.structure_info and
                node.structure_info['created_by_component'] == self.component_name):
                component_nodes.append(node)
        
        return component_nodes
    
    def get_component_node_count(self) -> int:
        """Get count of nodes created by this specific component"""
        return len(self.get_component_nodes())
    
    def get_component_access_count(self) -> int:
        """Get how many times this component has accessed the storage"""
        metrics = self.storage.get_storage_metrics()
        return metrics.component_access_count.get(self.component_name, 0)
    
    def get_storage_summary(self) -> Dict[str, Any]:
        """Get a summary of the centralized storage for this component"""
        metrics = self.storage.get_storage_metrics()
        component_nodes = self.get_component_nodes()
        
        return {
            'component_name': self.component_name,
            'total_storage_nodes': metrics.total_nodes,
            'component_nodes': len(component_nodes),
            'component_access_count': self.get_component_access_count(),
            'storage_size_bytes': metrics.storage_size_bytes,
            'nodes_by_water_state': metrics.nodes_by_water_state,
            'nodes_by_fractal_layer': metrics.nodes_by_fractal_layer,
            'nodes_by_chakra': metrics.nodes_by_chakra,
            'last_updated': metrics.last_updated
        }
    
    def print_storage_summary(self):
        """Print a summary of the centralized storage for this component"""
        summary = self.get_storage_summary()
        
        print(f"\n📊 Storage Summary for {summary['component_name']}")
        print("=" * 50)
        print(f"Total Storage Nodes: {summary['total_storage_nodes']}")
        print(f"Component Nodes: {summary['component_nodes']}")
        print(f"Component Access Count: {summary['component_access_count']}")
        print(f"Storage Size: {summary['storage_size_bytes']} bytes")
        print(f"Last Updated: {summary['last_updated']}")
        
        print("\n🌊 Nodes by Water State:")
        for water_state, count in summary['nodes_by_water_state'].items():
            print(f"  {water_state}: {count}")
        
        print("\n🔢 Nodes by Fractal Layer:")
        for fractal_layer, count in summary['nodes_by_fractal_layer'].items():
            print(f"  Layer {fractal_layer}: {count}")
        
        print("\n🌀 Nodes by Chakra:")
        for chakra, count in summary['nodes_by_chakra'].items():
            print(f"  {chakra}: {count}")
    
    def get_shared_nodes(self) -> List[Any]:
        """Get all nodes that are shared between components (not just this one)"""
        all_nodes = self.storage.get_all_nodes()
        shared_nodes = []
        
        for node in all_nodes.values():
            if (hasattr(node, 'structure_info') and 
                'created_by_component' in node.structure_info and
                node.structure_info['created_by_component'] != self.component_name):
                shared_nodes.append(node)
        
        return shared_nodes
    
    def get_shared_node_count(self) -> int:
        """Get count of nodes created by other components"""
        return len(self.get_shared_nodes())
    
    def get_cross_component_relationships(self) -> Dict[str, List[str]]:
        """Get relationships between nodes from different components"""
        all_nodes = self.storage.get_all_nodes()
        relationships = {}
        
        for node in all_nodes.values():
            if node.parent_id:
                parent = self.storage.get_node(node.parent_id)
                if parent:
                    parent_component = parent.structure_info.get('created_by_component', 'unknown')
                    child_component = node.structure_info.get('created_by_component', 'unknown')
                    
                    if parent_component != child_component:
                        relationship_key = f"{parent_component} -> {child_component}"
                        if relationship_key not in relationships:
                            relationships[relationship_key] = []
                        relationships[relationship_key].append(f"{parent.name} -> {node.name}")
        
        return relationships
    
    def print_cross_component_relationships(self):
        """Print relationships between nodes from different components"""
        relationships = self.get_cross_component_relationships()
        
        if not relationships:
            print(f"\n🔗 No cross-component relationships found for {self.component_name}")
            return
        
        print(f"\n🔗 Cross-Component Relationships for {self.component_name}")
        print("=" * 60)
        
        for relationship, node_pairs in relationships.items():
            print(f"\n{relationship}:")
            for node_pair in node_pairs[:5]:  # Show first 5 relationships
                print(f"  {node_pair}")
            if len(node_pairs) > 5:
                print(f"  ... and {len(node_pairs) - 5} more")
    
    def get_storage_health(self) -> Dict[str, Any]:
        """Get health metrics for the centralized storage"""
        metrics = self.storage.get_storage_metrics()
        component_nodes = self.get_component_nodes()
        shared_nodes = self.get_shared_nodes()
        
        # Calculate health indicators
        total_nodes = metrics.total_nodes
        component_ratio = len(component_nodes) / total_nodes if total_nodes > 0 else 0
        shared_ratio = len(shared_nodes) / total_nodes if total_nodes > 0 else 0
        
        health_score = min(100, (component_ratio * 40 + shared_ratio * 40 + 20))
        
        return {
            'health_score': health_score,
            'total_nodes': total_nodes,
            'component_nodes': component_nodes,
            'shared_nodes': shared_nodes,
            'component_ratio': component_ratio,
            'shared_ratio': shared_ratio,
            'storage_size_bytes': metrics.storage_size_bytes,
            'component_access_count': self.get_component_access_count(),
            'status': 'healthy' if health_score >= 80 else 'warning' if health_score >= 60 else 'critical'
        }
    
    def print_storage_health(self):
        """Print health metrics for the centralized storage"""
        health = self.get_storage_health()
        
        print(f"\n🏥 Storage Health for {self.component_name}")
        print("=" * 50)
        print(f"Health Score: {health['health_score']:.1f}/100")
        print(f"Status: {health['status'].upper()}")
        print(f"Total Nodes: {health['total_nodes']}")
        print(f"Component Nodes: {health['component_nodes']}")
        print(f"Shared Nodes: {health['shared_nodes']}")
        print(f"Component Ratio: {health['component_ratio']:.2%}")
        print(f"Shared Ratio: {health['shared_ratio']:.2%}")
        print(f"Storage Size: {health['storage_size_bytes']} bytes")
        print(f"Access Count: {health['component_access_count']}")

# Convenience function to get the centralized storage instance
def get_centralized_storage():
    """Get the centralized storage instance"""
    return centralized_storage

# Convenience function to get storage metrics
def get_storage_metrics():
    """Get comprehensive storage metrics"""
    return centralized_storage.get_storage_metrics()

# Convenience function to get total node count
def get_total_node_count():
    """Get total number of nodes in the system"""
    return centralized_storage.get_node_count()
