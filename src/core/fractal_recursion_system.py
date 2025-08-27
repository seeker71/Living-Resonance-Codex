#!/usr/bin/env python3
"""
Fractal Recursion System
========================

This system implements the core Living Codex principle of fractal recursion
through hasPart/isPartOf relationships and self-similarity across scales.

Key Features:
- Fractal recursion through hasPart/isPartOf relationships
- Self-similarity across scales (Micro↔Meso↔Macro↔Meta)
- Holographic node exploration at infinite depths
- Cross-scale mapping and transformation
- Fractal pattern recognition and generation

This is Phase 5 of the metadata enhancement plan.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Set, Tuple
from datetime import datetime
import json
import math
from collections import defaultdict, deque

from living_codex_ontology import (
    FractalLayer, EpistemicLabel, canonical_registry
)

# ============================================================================
# FRACTAL RECURSION DATA STRUCTURES
# ============================================================================

@dataclass
class FractalNode:
    """A node in the fractal recursion hierarchy"""
    node_id: str
    name: str
    fractal_layer: FractalLayer
    has_part: List[str] = field(default_factory=list)
    is_part_of: Optional[str] = None
    fractal_depth: int = 0
    self_similarity_score: float = 0.0
    cross_scale_mapping: Dict[str, str] = field(default_factory=dict)
    fractal_patterns: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    epistemic_label: EpistemicLabel = EpistemicLabel.ENGINEERING

@dataclass
class FractalExploration:
    """Result of fractal exploration at a specific depth"""
    depth: int
    nodes_found: List[str]
    patterns_discovered: List[str]
    self_similarity_score: float
    cross_scale_coherence: float
    exploration_path: List[str]
    epistemic_label: EpistemicLabel = EpistemicLabel.ENGINEERING

@dataclass
class CrossScaleTransformation:
    """Transformation between different scales of reality"""
    from_scale: str  # micro, meso, macro, meta
    to_scale: str
    transformation_type: str  # expansion, contraction, reflection, rotation
    transformation_matrix: Dict[str, Any]
    coherence_preservation: float
    epistemic_label: EpistemicLabel = EpistemicLabel.SPECULATIVE

# ============================================================================
# FRACTAL RECURSION SYSTEM
# ============================================================================

class FractalRecursionSystem:
    """
    Core system for implementing fractal recursion and self-similarity
    across all scales of the Living Codex
    """
    
    def __init__(self):
        self.fractal_nodes = {}  # node_id -> FractalNode
        self.fractal_relationships = defaultdict(set)  # node_id -> set of related nodes
        self.cross_scale_mappings = {}  # node_id -> CrossScaleMapping
        self.fractal_patterns = set()
        self.exploration_cache = {}
        
        print("🌟 Fractal Recursion System initialized")
        print("✨ Fractal recursion through hasPart/isPartOf enabled")
        print("✨ Self-similarity across scales active")
        print("✨ Cross-scale mapping and transformation enabled")
        print("✨ Holographic exploration at infinite depths enabled")
    
    def add_fractal_node(self, node_id: str, name: str, fractal_layer: FractalLayer,
                        has_part: List[str] = None, is_part_of: Optional[str] = None,
                        metadata: Dict[str, Any] = None) -> bool:
        """
        Add a new fractal node to the system
        
        Args:
            node_id: Unique node identifier
            name: Human-readable name
            fractal_layer: Layer in the fractal hierarchy
            has_part: List of child node IDs
            is_part_of: Parent node ID
            metadata: Additional metadata
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if node_id in self.fractal_nodes:
                print(f"Warning: Node {node_id} already exists, updating...")
            
            # Create fractal node
            fractal_node = FractalNode(
                node_id=node_id,
                name=name,
                fractal_layer=fractal_layer,
                has_part=has_part or [],
                is_part_of=is_part_of,
                fractal_depth=0,  # Will be calculated
                self_similarity_score=0.0,  # Will be calculated
                cross_scale_mapping={},  # Will be calculated
                fractal_patterns=[],  # Will be discovered
                metadata=metadata or {},
                epistemic_label=EpistemicLabel.ENGINEERING
            )
            
            # Add to system
            self.fractal_nodes[node_id] = fractal_node
            
            # Update relationships
            self._update_fractal_relationships(fractal_node)
            
            # Calculate fractal properties
            self._calculate_fractal_properties(node_id)
            
            print(f"✅ Fractal node '{name}' added (ID: {node_id})")
            return True
            
        except Exception as e:
            print(f"Error adding fractal node {node_id}: {e}")
            return False
    
    def add_child_relationship(self, parent_id: str, child_id: str) -> bool:
        """
        Add a hasPart relationship between parent and child nodes
        
        Args:
            parent_id: Parent node identifier
            child_id: Child node identifier
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if parent_id not in self.fractal_nodes:
                print(f"Error: Parent node {parent_id} not found")
                return False
            
            if child_id not in self.fractal_nodes:
                print(f"Error: Child node {child_id} not found")
                return False
            
            # Add hasPart relationship
            if child_id not in self.fractal_nodes[parent_id].has_part:
                self.fractal_nodes[parent_id].has_part.append(child_id)
            
            # Add isPartOf relationship
            self.fractal_nodes[child_id].is_part_of = parent_id
            
            # Update fractal properties
            self._calculate_fractal_properties(parent_id)
            self._calculate_fractal_properties(child_id)
            
            print(f"✅ Child relationship added: {parent_id} hasPart {child_id}")
            return True
            
        except Exception as e:
            print(f"Error adding child relationship: {e}")
            return False
    
    def remove_child_relationship(self, parent_id: str, child_id: str) -> bool:
        """
        Remove a hasPart relationship between parent and child nodes
        
        Args:
            parent_id: Parent node identifier
            child_id: Child node identifier
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if parent_id not in self.fractal_nodes:
                print(f"Error: Parent node {parent_id} not found")
                return False
            
            if child_id not in self.fractal_nodes:
                print(f"Error: Child node {child_id} not found")
                return False
            
            # Remove hasPart relationship
            if child_id in self.fractal_nodes[parent_id].has_part:
                self.fractal_nodes[parent_id].has_part.remove(child_id)
            
            # Remove isPartOf relationship
            if self.fractal_nodes[child_id].is_part_of == parent_id:
                self.fractal_nodes[child_id].is_part_of = None
            
            # Update fractal properties
            self._calculate_fractal_properties(parent_id)
            self._calculate_fractal_properties(child_id)
            
            print(f"✅ Child relationship removed: {parent_id} no longer hasPart {child_id}")
            return True
            
        except Exception as e:
            print(f"Error removing child relationship: {e}")
            return False
    
    def explore_fractal_depth(self, node_id: str, max_depth: int = 5) -> FractalExploration:
        """
        Explore a node at a specific fractal depth
        
        Args:
            node_id: Node identifier to explore
            max_depth: Maximum depth to explore
        
        Returns:
            FractalExploration with exploration results
        """
        try:
            # Check cache first
            cache_key = f"{node_id}_{max_depth}"
            if cache_key in self.exploration_cache:
                return self.exploration_cache[cache_key]
            
            if node_id not in self.fractal_nodes:
                print(f"Error: Node {node_id} not found")
                return None
            
            # Perform fractal exploration
            exploration = self._perform_fractal_exploration(node_id, max_depth)
            
            # Cache the result
            self.exploration_cache[cache_key] = exploration
            
            return exploration
            
        except Exception as e:
            print(f"Error exploring fractal depth for {node_id}: {e}")
            return None
    
    def get_cross_scale_mapping(self, node_id: str) -> Dict[str, Dict[str, Any]]:
        """
        Get cross-scale mapping for a node (Micro↔Meso↔Macro↔Meta)
        
        Args:
            node_id: Node identifier
        
        Returns:
            Dictionary with scale mappings
        """
        try:
            if node_id not in self.fractal_nodes:
                print(f"Error: Node {node_id} not found")
                return {}
            
            # Get or calculate cross-scale mapping
            if node_id not in self.cross_scale_mappings:
                self.cross_scale_mappings[node_id] = self._calculate_cross_scale_mapping(node_id)
            
            return self.cross_scale_mappings[node_id]
            
        except Exception as e:
            print(f"Error getting cross-scale mapping for {node_id}: {e}")
            return {}
    
    def transform_across_scales(self, node_id: str, from_scale: str, 
                              to_scale: str, transformation_type: str = "expansion") -> CrossScaleTransformation:
        """
        Transform a node from one scale to another
        
        Args:
            node_id: Node identifier
            from_scale: Source scale (micro, meso, macro, meta)
            to_scale: Target scale
            transformation_type: Type of transformation
        
        Returns:
            CrossScaleTransformation with transformation details
        """
        try:
            if node_id not in self.fractal_nodes:
                print(f"Error: Node {node_id} not found")
                return None
            
            # Perform cross-scale transformation
            transformation = self._perform_cross_scale_transformation(
                node_id, from_scale, to_scale, transformation_type
            )
            
            return transformation
            
        except Exception as e:
            print(f"Error transforming across scales: {e}")
            return None
    
    def get_fractal_statistics(self) -> Dict[str, Any]:
        """Get overall fractal system statistics"""
        try:
            total_nodes = len(self.fractal_nodes)
            total_relationships = sum(len(node.has_part) for node in self.fractal_nodes.values())
            
            # Calculate average fractal depth
            depths = [node.fractal_depth for node in self.fractal_nodes.values()]
            avg_depth = sum(depths) / len(depths) if depths else 0
            
            # Calculate average self-similarity
            similarities = [node.self_similarity_score for node in self.fractal_nodes.values()]
            avg_similarity = sum(similarities) / len(similarities) if similarities else 0
            
            # Count nodes by fractal layer
            layer_counts = defaultdict(int)
            for node in self.fractal_nodes.values():
                layer_counts[node.fractal_layer.name] += 1
            
            return {
                "total_nodes": total_nodes,
                "total_relationships": total_relationships,
                "average_fractal_depth": avg_depth,
                "average_self_similarity": avg_similarity,
                "nodes_by_layer": dict(layer_counts),
                "fractal_patterns": list(self.fractal_patterns),
                "cross_scale_mappings": len(self.cross_scale_mappings)
            }
            
        except Exception as e:
            print(f"Error getting fractal statistics: {e}")
            return {}
    
    # ============================================================================
    # PRIVATE IMPLEMENTATION METHODS
    # ============================================================================
    
    def _update_fractal_relationships(self, fractal_node: FractalNode):
        """Update fractal relationship tracking"""
        # Add to fractal relationships
        self.fractal_relationships[fractal_node.node_id] = set()
        
        # Add hasPart relationships
        for child_id in fractal_node.has_part:
            if child_id in self.fractal_nodes:
                self.fractal_relationships[fractal_node.node_id].add(child_id)
        
        # Add isPartOf relationships
        if fractal_node.is_part_of and fractal_node.is_part_of in self.fractal_nodes:
            self.fractal_relationships[fractal_node.is_part_of].add(fractal_node.node_id)
    
    def _calculate_fractal_properties(self, node_id: str):
        """Calculate fractal properties for a node"""
        if node_id not in self.fractal_nodes:
            return
        
        node = self.fractal_nodes[node_id]
        
        # Calculate fractal depth
        node.fractal_depth = self._calculate_node_depth(node_id)
        
        # Calculate self-similarity score
        node.self_similarity_score = self._calculate_self_similarity(node_id)
        
        # Calculate cross-scale mapping
        node.cross_scale_mapping = self._calculate_node_cross_scale_mapping(node_id)
        
        # Discover fractal patterns
        node.fractal_patterns = self._discover_fractal_patterns(node_id)
    
    def _calculate_node_depth(self, node_id: str) -> int:
        """Calculate the fractal depth of a node"""
        if node_id not in self.fractal_nodes:
            return 0
        
        node = self.fractal_nodes[node_id]
        
        # Base case: root nodes have depth 0
        if not node.is_part_of:
            return 0
        
        # Recursive case: depth = parent depth + 1
        parent_depth = self._calculate_node_depth(node.is_part_of)
        return parent_depth + 1
    
    def _calculate_self_similarity(self, node_id: str) -> float:
        """Calculate self-similarity score for a node"""
        if node_id not in self.fractal_nodes:
            return 0.0
        
        node = self.fractal_nodes[node_id]
        
        # Base similarity based on fractal layer
        base_similarity = 1.0 - (node.fractal_depth * 0.1)
        
        # Enhance similarity based on hasPart relationships
        if node.has_part:
            child_similarities = []
            for child_id in node.has_part:
                if child_id in self.fractal_nodes:
                    child_similarity = self._calculate_self_similarity(child_id)
                    child_similarities.append(child_similarity)
            
            if child_similarities:
                avg_child_similarity = sum(child_similarities) / len(child_similarities)
                base_similarity = (base_similarity + avg_child_similarity) / 2
        
        return max(0.0, min(1.0, base_similarity))
    
    def _calculate_node_cross_scale_mapping(self, node_id: str) -> Dict[str, str]:
        """Calculate cross-scale mapping for a node"""
        # This is a simplified implementation
        # In practice, this would analyze the node's properties and relationships
        
        return {
            "micro": f"micro_{node_id}",
            "meso": f"meso_{node_id}",
            "macro": f"macro_{node_id}",
            "meta": f"meta_{node_id}"
        }
    
    def _discover_fractal_patterns(self, node_id: str) -> List[str]:
        """Discover fractal patterns for a node"""
        patterns = []
        
        if node_id not in self.fractal_nodes:
            return patterns
        
        node = self.fractal_nodes[node_id]
        
        # Check for self-similarity patterns
        if node.self_similarity_score > 0.8:
            patterns.append("self_similar")
        
        # Check for recursive patterns
        if node.has_part:
            patterns.append("recursive")
        
        # Check for holographic patterns
        if node.fractal_depth == 0 and node.has_part:
            patterns.append("holographic")
        
        # Check for cross-scale patterns
        if node.cross_scale_mapping:
            patterns.append("cross_scale")
        
        # Add patterns to global set
        for pattern in patterns:
            self.fractal_patterns.add(pattern)
        
        return patterns
    
    def _perform_fractal_exploration(self, node_id: str, max_depth: int) -> FractalExploration:
        """Perform fractal exploration at a specific depth"""
        if node_id not in self.fractal_nodes:
            return None
        
        # Use BFS to explore fractal structure
        visited = set()
        queue = deque([(node_id, 0)])  # (node_id, depth)
        nodes_found = []
        patterns_discovered = set()
        exploration_path = []
        
        while queue:
            current_id, current_depth = queue.popleft()
            
            if current_id in visited or current_depth > max_depth:
                continue
            
            visited.add(current_id)
            nodes_found.append(current_id)
            exploration_path.append(current_id)
            
            # Get current node
            current_node = self.fractal_nodes.get(current_id)
            if not current_node:
                continue
            
            # Discover patterns
            for pattern in current_node.fractal_patterns:
                patterns_discovered.add(pattern)
            
            # Add children to queue
            for child_id in current_node.has_part:
                if child_id not in visited:
                    queue.append((child_id, current_depth + 1))
        
        # Calculate exploration metrics
        self_similarity_score = sum(
            self.fractal_nodes[node_id].self_similarity_score 
            for node_id in nodes_found
        ) / len(nodes_found) if nodes_found else 0.0
        
        cross_scale_coherence = self._calculate_exploration_coherence(nodes_found)
        
        return FractalExploration(
            depth=max_depth,
            nodes_found=nodes_found,
            patterns_discovered=list(patterns_discovered),
            self_similarity_score=self_similarity_score,
            cross_scale_coherence=cross_scale_coherence,
            exploration_path=exploration_path
        )
    
    def _calculate_exploration_coherence(self, node_ids: List[str]) -> float:
        """Calculate coherence score for an exploration"""
        if not node_ids:
            return 0.0
        
        # Calculate average self-similarity
        similarities = [
            self.fractal_nodes[node_id].self_similarity_score 
            for node_id in node_ids 
            if node_id in self.fractal_nodes
        ]
        
        if not similarities:
            return 0.0
        
        return sum(similarities) / len(similarities)
    
    def _calculate_cross_scale_mapping(self, node_id: str) -> Dict[str, Dict[str, Any]]:
        """Calculate cross-scale mapping for a node"""
        # This is a simplified implementation
        # In practice, this would analyze the node's properties and relationships
        
        return {
            "micro": {
                "quantum_state": "superposition",
                "consciousness_level": "awake",
                "water_state": "ws.quantum_coherent"
            },
            "meso": {
                "consciousness_level": "self_aware",
                "human_consciousness": "self_aware",
                "cultural_context": "modern",
                "water_state": "ws.liquid"
            },
            "macro": {
                "consciousness_level": "transcendent",
                "cosmic_context": "galactic",
                "temporal_scale": "evolutionary",
                "water_state": "ws.vapor"
            },
            "meta": {
                "consciousness_level": "unity",
                "transcendent_level": "unity",
                "holographic_nature": "complete",
                "water_state": "ws.bose_einstein"
            }
        }
    
    def _perform_cross_scale_transformation(self, node_id: str, from_scale: str, 
                                          to_scale: str, transformation_type: str) -> CrossScaleTransformation:
        """Perform cross-scale transformation"""
        # This is a simplified implementation
        # In practice, this would perform complex transformations
        
        transformation_matrix = {
            "scale_factor": 1.0,
            "rotation": 0.0,
            "reflection": False,
            "coherence_preservation": 0.8
        }
        
        coherence_preservation = 0.8  # Placeholder
        
        return CrossScaleTransformation(
            from_scale=from_scale,
            to_scale=to_scale,
            transformation_type=transformation_type,
            transformation_matrix=transformation_matrix,
            coherence_preservation=coherence_preservation
        )

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global fractal recursion system instance
fractal_recursion_system = FractalRecursionSystem()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_fractal_recursion_system() -> FractalRecursionSystem:
    """Get the global fractal recursion system instance"""
    return fractal_recursion_system

def add_fractal_node(node_id: str, name: str, fractal_layer: FractalLayer,
                    has_part: List[str] = None, is_part_of: Optional[str] = None,
                    metadata: Dict[str, Any] = None) -> bool:
    """Add a new fractal node"""
    return fractal_recursion_system.add_fractal_node(
        node_id, name, fractal_layer, has_part, is_part_of, metadata
    )

def explore_fractal_depth(node_id: str, max_depth: int = 5) -> FractalExploration:
    """Explore a node at a specific fractal depth"""
    return fractal_recursion_system.explore_fractal_depth(node_id, max_depth)

if __name__ == "__main__":
    # Test the fractal recursion system
    print("🌟 Testing Fractal Recursion System")
    
    # Add test nodes
    add_fractal_node("root", "Root Node", FractalLayer.FRACTAL_SYSTEM_ROOT)
    add_fractal_node("child1", "Child 1", FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY)
    add_fractal_node("child2", "Child 2", FractalLayer.SELF_REFERENTIAL_DOCUMENTATION)
    
    # Add relationships
    add_child_relationship("root", "child1")
    add_child_relationship("root", "child2")
    
    # Explore fractal depth
    exploration = explore_fractal_depth("root", max_depth=3)
    if exploration:
        print(f"✨ Fractal exploration completed:")
        print(f"   - Depth: {exploration.depth}")
        print(f"   - Nodes found: {len(exploration.nodes_found)}")
        print(f"   - Patterns: {exploration.patterns_discovered}")
        print(f"   - Self-similarity: {exploration.self_similarity_score:.3f}")
    
    # Get statistics
    stats = fractal_recursion_system.get_fractal_statistics()
    print(f"✨ System statistics: {stats}")
    
    print("✅ Fractal Recursion System test completed!")
