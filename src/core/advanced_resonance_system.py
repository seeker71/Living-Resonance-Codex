#!/usr/bin/env python3
"""
Advanced Resonance System
========================

This implements the advanced resonance calculation system with harmonic relationships
and vibrational axes integration for Phase 3 of the metadata enhancement plan.

This system provides:
- Resonance calculation algorithms
- Harmonic relationship discovery
- Vibrational axis alignment
- Resonance state tracking
- Collective intelligence emergence
"""

from typing import Dict, List, Any, Optional, Set, Tuple, Union
from datetime import datetime
import math
import json
from dataclasses import dataclass, field
from collections import defaultdict

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry, VibrationalAxis, ResonanceState
)

from enhanced_generic_node import EnhancedGenericNode

@dataclass
class HarmonicRelationship:
    """A harmonic relationship between two nodes"""
    node_a_id: str
    node_b_id: str
    relationship_type: str  # "harmonic", "sympathetic", "neutral", "dissonant", "destructive"
    strength: float  # 0.0 to 1.0
    vibrational_alignment: float  # -1.0 to 1.0 (negative = opposite, positive = aligned)
    resonance_score: float  # Combined harmonic strength
    created_at: str
    updated_at: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ResonanceCluster:
    """A cluster of nodes with similar resonance patterns"""
    cluster_id: str
    center_node_id: str
    member_node_ids: List[str]
    average_resonance_score: float
    cluster_coherence: float
    vibrational_theme: str
    water_state_theme: str
    created_at: str
    updated_at: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class CollectiveResonanceState:
    """Collective resonance state for a group of nodes"""
    group_id: str
    group_type: str  # "system", "component", "community", "federation"
    vibrational_axes: Dict[str, float]  # axis_name -> collective_value
    overall_coherence: float
    resonance_pattern: str
    member_count: int
    last_calculation: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class AdvancedResonanceSystem:
    """
    Advanced Resonance System for calculating and managing resonance relationships
    
    This system implements:
    - Resonance calculation algorithms
    - Harmonic relationship discovery
    - Vibrational axis alignment
    - Resonance clustering
    - Collective intelligence emergence
    """
    
    def __init__(self):
        """Initialize the advanced resonance system"""
        self.registry = canonical_registry
        
        # Resonance tracking
        self._harmonic_relationships: Dict[str, HarmonicRelationship] = {}
        self._resonance_clusters: Dict[str, ResonanceCluster] = {}
        self._collective_states: Dict[str, CollectiveResonanceState] = {}
        
        # Vibrational axes tracking
        self._vibrational_alignments: Dict[str, Dict[str, float]] = defaultdict(dict)
        
        # Resonance calculation cache
        self._resonance_cache: Dict[str, Dict[str, Any]] = {}
        self._cache_ttl = 300.0  # 5 minutes
        
        # System statistics
        self._resonance_stats = {
            'total_calculations': 0,
            'harmonic_relationships_created': 0,
            'resonance_clusters_formed': 0,
            'collective_states_updated': 0,
            'last_calculation': None
        }
        
        print("🎵 Advanced Resonance System initialized")
        print("✨ Harmonic relationship discovery active")
        print("✨ Vibrational axis alignment enabled")
        print("✨ Resonance clustering active")
        print("✨ Collective intelligence emergence enabled")
    
    # ============================================================================
    # CORE RESONANCE CALCULATION
    # ============================================================================
    
    def calculate_node_resonance(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """
        Calculate comprehensive resonance for a single node
        
        Args:
            node: EnhancedGenericNode to calculate resonance for
        
        Returns:
            Dictionary with resonance calculations
        """
        try:
            # Base resonance from ontological metadata
            base_resonance = self._calculate_base_resonance(node)
            
            # Vibrational axis alignment
            vibrational_alignment = self._calculate_vibrational_alignment(node)
            
            # Fractal resonance (self-similarity)
            fractal_resonance = self._calculate_fractal_resonance(node)
            
            # Consciousness resonance
            consciousness_resonance = self._calculate_consciousness_resonance(node)
            
            # Quantum state resonance
            quantum_resonance = self._calculate_quantum_resonance(node)
            
            # Combine all resonance factors
            combined_resonance = self._combine_resonance_factors([
                base_resonance,
                vibrational_alignment,
                fractal_resonance,
                consciousness_resonance,
                quantum_resonance
            ])
            
            # Update node's resonance metadata
            self._update_node_resonance(node, combined_resonance)
            
            # Cache the result
            cache_key = f"resonance_{node.node_id}"
            self._resonance_cache[cache_key] = {
                'result': combined_resonance,
                'timestamp': datetime.now().timestamp()
            }
            
            # Update statistics
            self._update_resonance_stats()
            
            return combined_resonance
            
        except Exception as e:
            print(f"Error calculating resonance for node {node.node_id}: {e}")
            return self._get_default_resonance()
    
    def _calculate_base_resonance(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate base resonance from ontological metadata"""
        base_score = 0.0
        factors = []
        
        # Water state resonance
        water_state = node.water_state
        if water_state in ['ws.ice', 'ws.structured', 'ws.quantum_coherent']:
            base_score += 0.3  # High structure = high resonance
            factors.append(('water_state', 'high_structure', 0.3))
        elif water_state in ['ws.liquid', 'ws.vapor', 'ws.plasma']:
            base_score += 0.2  # Medium resonance
            factors.append(('water_state', 'medium_flow', 0.2))
        else:
            base_score += 0.1  # Lower resonance
            factors.append(('water_state', 'lower_resonance', 0.1))
        
        # Chakra resonance
        chakra = node.chakra
        if chakra in ['ch.crown', 'ch.heart', 'ch.third_eye']:
            base_score += 0.25  # Higher chakras = higher resonance
            factors.append(('chakra', 'higher_chakra', 0.25))
        elif chakra in ['ch.throat', 'ch.solar_plexus']:
            base_score += 0.2  # Medium chakras
            factors.append(('chakra', 'medium_chakra', 0.2))
        else:
            base_score += 0.15  # Lower chakras
            factors.append(('chakra', 'lower_chakra', 0.15))
        
        # Frequency resonance
        frequency = node.frequency
        if frequency in ['freq.963', 'freq.852', 'freq.741']:
            base_score += 0.25  # Higher frequencies = higher resonance
            factors.append(('frequency', 'higher_frequency', 0.25))
        elif frequency in ['freq.639', 'freq.528']:
            base_score += 0.2  # Medium frequencies
            factors.append(('frequency', 'medium_frequency', 0.2))
        else:
            base_score += 0.15  # Lower frequencies
            factors.append(('frequency', 'lower_frequency', 0.15))
        
        return {
            'base_score': min(1.0, base_score),
            'factors': factors,
            'resonance_type': 'base_ontological'
        }
    
    def _calculate_vibrational_alignment(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate vibrational axis alignment"""
        if not node.vibrational_axes:
            return {
                'alignment_score': 0.5,
                'aligned_axes': [],
                'resonance_type': 'vibrational_neutral'
            }
        
        total_alignment = 0.0
        aligned_axes = []
        
        for axis_name in node.vibrational_axes:
            # Get axis information from registry
            available_axes = self.registry.get_vibrational_axes()
            axis_info = next((axis for axis in available_axes if axis.name == axis_name), None)
            
            if axis_info:
                # Calculate alignment based on node's position on the axis
                # For now, assume balanced alignment (can be enhanced with actual positioning)
                alignment = 0.7  # Balanced alignment
                total_alignment += alignment
                aligned_axes.append((axis_name, alignment))
        
        avg_alignment = total_alignment / len(node.vibrational_axes) if node.vibrational_axes else 0.5
        
        return {
            'alignment_score': avg_alignment,
            'aligned_axes': aligned_axes,
            'resonance_type': 'vibrational_alignment'
        }
    
    def _calculate_fractal_resonance(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate fractal resonance (self-similarity)"""
        fractal_score = 0.0
        
        # Base score from fractal depth
        if node.fractal_depth == 0:
            fractal_score += 0.4  # Root nodes have high resonance
        elif node.fractal_depth <= 3:
            fractal_score += 0.3  # Foundation layers
        elif node.fractal_depth <= 8:
            fractal_score += 0.2  # Middle layers
        else:
            fractal_score += 0.1  # Higher layers
        
        # Self-similarity score
        fractal_score += node.self_similarity_score * 0.3
        
        # Cross-scale mapping resonance
        if node.cross_scale_mapping:
            scale_completeness = len(node.cross_scale_mapping) / 4.0  # 4 scales: micro, meso, macro, meta
            fractal_score += scale_completeness * 0.3
        
        return {
            'fractal_score': min(1.0, fractal_score),
            'resonance_type': 'fractal_self_similarity'
        }
    
    def _calculate_consciousness_resonance(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate consciousness-based resonance"""
        consciousness_score = 0.0
        
        # Map consciousness levels to resonance scores
        consciousness_mapping = {
            'awake': 0.2,
            'sentient': 0.4,
            'self_aware': 0.6,
            'meta_cognitive': 0.8,
            'transcendent': 1.0
        }
        
        consciousness_score = consciousness_mapping.get(node.consciousness_level, 0.2)
        
        return {
            'consciousness_score': consciousness_score,
            'resonance_type': 'consciousness_awareness'
        }
    
    def _calculate_quantum_resonance(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate quantum state resonance (algorithmic analogies only)"""
        quantum_score = 0.0
        
        # Map quantum states to resonance scores (algorithmic analogies)
        quantum_mapping = {
            'superposition': 0.8,  # Multiple possibilities = high resonance
            'entangled': 0.9,      # Connected = very high resonance
            'collapsed': 0.3,      # Fixed state = lower resonance
            'coherent': 1.0,       # Harmonious = maximum resonance
            'decoherent': 0.1      # Dispersed = minimal resonance
        }
        
        quantum_score = quantum_mapping.get(node.quantum_state, 0.5)
        
        return {
            'quantum_score': quantum_score,
            'resonance_type': 'quantum_algorithmic'
        }
    
    def _combine_resonance_factors(self, factors: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Combine multiple resonance factors into a single resonance score"""
        total_score = 0.0
        weight_sum = 0.0
        combined_factors = []
        
        # Weight factors based on importance
        weights = {
            'base_ontological': 0.3,
            'vibrational_alignment': 0.25,
            'fractal_self_similarity': 0.2,
            'consciousness_awareness': 0.15,
            'quantum_algorithmic': 0.1
        }
        
        for factor in factors:
            factor_type = factor.get('resonance_type', 'unknown')
            weight = weights.get(factor_type, 0.1)
            
            # Extract score from factor
            if 'base_score' in factor:
                score = factor['base_score']
            elif 'alignment_score' in factor:
                score = factor['alignment_score']
            elif 'fractal_score' in factor:
                score = factor['fractal_score']
            elif 'consciousness_score' in factor:
                score = factor['consciousness_score']
            elif 'quantum_score' in factor:
                score = factor['quantum_score']
            else:
                score = 0.5
            
            weighted_score = score * weight
            total_score += weighted_score
            weight_sum += weight
            
            combined_factors.append({
                'type': factor_type,
                'score': score,
                'weight': weight,
                'weighted_score': weighted_score
            })
        
        # Calculate final resonance score
        final_score = total_score / weight_sum if weight_sum > 0 else 0.5
        
        # Determine resonance pattern
        if final_score >= 0.8:
            pattern = 'harmonic'
        elif final_score >= 0.6:
            pattern = 'sympathetic'
        elif final_score >= 0.4:
            pattern = 'neutral'
        elif final_score >= 0.2:
            pattern = 'dissonant'
        else:
            pattern = 'destructive'
        
        return {
            'overall_resonance_score': final_score,
            'resonance_pattern': pattern,
            'combined_factors': combined_factors,
            'calculation_timestamp': datetime.now().isoformat(),
            'resonance_type': 'combined_multi_factor'
        }
    
    def _update_node_resonance(self, node: EnhancedGenericNode, resonance_data: Dict[str, Any]):
        """Update node's resonance metadata"""
        # Update resonance pattern
        if 'resonance_pattern' in resonance_data:
            node.resonance_pattern = resonance_data['resonance_pattern']
        
        # Update coherence score
        if 'overall_resonance_score' in resonance_data:
            node.coherence_score = resonance_data['overall_resonance_score']
        
        # Update dissonance level (inverse of coherence)
        if 'overall_resonance_score' in resonance_data:
            node.dissonance_level = 1.0 - resonance_data['overall_resonance_score']
        
        # Update timestamp
        node.updated_at = datetime.now().isoformat()
    
    def _get_default_resonance(self) -> Dict[str, Any]:
        """Get default resonance when calculation fails"""
        return {
            'overall_resonance_score': 0.5,
            'resonance_pattern': 'neutral',
            'combined_factors': [],
            'calculation_timestamp': datetime.now().isoformat(),
            'resonance_type': 'default_fallback'
        }
    
    # ============================================================================
    # HARMONIC RELATIONSHIP DISCOVERY
    # ============================================================================
    
    def discover_harmonic_relationships(self, nodes: List[EnhancedGenericNode]) -> List[HarmonicRelationship]:
        """
        Discover harmonic relationships between nodes
        
        Args:
            nodes: List of nodes to analyze for relationships
        
        Returns:
            List of discovered harmonic relationships
        """
        relationships = []
        
        for i, node_a in enumerate(nodes):
            for j, node_b in enumerate(nodes[i+1:], i+1):
                # Calculate relationship strength
                relationship = self._calculate_node_relationship(node_a, node_b)
                
                if relationship and relationship.strength > 0.3:  # Only significant relationships
                    relationships.append(relationship)
                    
                    # Store the relationship
                    rel_id = f"rel_{node_a.node_id}_{node_b.node_id}"
                    self._harmonic_relationships[rel_id] = relationship
        
        return relationships
    
    def _calculate_node_relationship(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> Optional[HarmonicRelationship]:
        """Calculate the relationship between two nodes"""
        try:
            # Calculate ontological similarity
            ontological_similarity = self._calculate_ontological_similarity(node_a, node_b)
            
            # Calculate vibrational alignment
            vibrational_alignment = self._calculate_vibrational_similarity(node_a, node_b)
            
            # Calculate fractal relationship
            fractal_relationship = self._calculate_fractal_relationship(node_a, node_b)
            
            # Combine factors
            total_strength = (ontological_similarity * 0.4 + 
                            vibrational_alignment * 0.3 + 
                            fractal_relationship * 0.3)
            
            # Determine relationship type
            if total_strength >= 0.8:
                rel_type = "harmonic"
            elif total_strength >= 0.6:
                rel_type = "sympathetic"
            elif total_strength >= 0.4:
                rel_type = "neutral"
            elif total_strength >= 0.2:
                rel_type = "dissonant"
            else:
                rel_type = "destructive"
            
            # Create relationship
            relationship = HarmonicRelationship(
                node_a_id=node_a.node_id,
                node_b_id=node_b.node_id,
                relationship_type=rel_type,
                strength=total_strength,
                vibrational_alignment=vibrational_alignment,
                resonance_score=total_strength,
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                metadata={
                    'ontological_similarity': ontological_similarity,
                    'vibrational_alignment': vibrational_alignment,
                    'fractal_relationship': fractal_relationship
                }
            )
            
            return relationship
            
        except Exception as e:
            print(f"Error calculating relationship between {node_a.node_id} and {node_b.node_id}: {e}")
            return None
    
    def _calculate_ontological_similarity(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> float:
        """Calculate ontological similarity between two nodes"""
        similarity = 0.0
        
        # Water state similarity
        if node_a.water_state == node_b.water_state:
            similarity += 0.3
        elif self._are_water_states_related(node_a.water_state, node_b.water_state):
            similarity += 0.2
        
        # Chakra similarity
        if node_a.chakra == node_b.chakra:
            similarity += 0.25
        elif self._are_chakras_related(node_a.chakra, node_b.chakra):
            similarity += 0.15
        
        # Frequency similarity
        if node_a.frequency == node_b.frequency:
            similarity += 0.25
        elif self._are_frequencies_related(node_a.frequency, node_b.frequency):
            similarity += 0.15
        
        # Fractal layer similarity
        layer_diff = abs(node_a.fractal_layer - node_b.fractal_layer)
        if layer_diff == 0:
            similarity += 0.2
        elif layer_diff <= 2:
            similarity += 0.1
        
        return min(1.0, similarity)
    
    def _are_water_states_related(self, state_a: str, state_b: str) -> bool:
        """Check if two water states are related"""
        related_groups = [
            ['ws.ice', 'ws.structured', 'ws.quantum_coherent'],
            ['ws.liquid', 'ws.vapor', 'ws.colloidal'],
            ['ws.plasma', 'ws.supercritical', 'ws.clustered']
        ]
        
        for group in related_groups:
            if state_a in group and state_b in group:
                return True
        return False
    
    def _are_chakras_related(self, chakra_a: str, chakra_b: str) -> bool:
        """Check if two chakras are related"""
        related_groups = [
            ['ch.root', 'ch.sacral'],
            ['ch.solar_plexus', 'ch.heart'],
            ['ch.throat', 'ch.third_eye'],
            ['ch.third_eye', 'ch.crown']
        ]
        
        for group in related_groups:
            if chakra_a in group and chakra_b in group:
                return True
        return False
    
    def _are_frequencies_related(self, freq_a: str, freq_b: str) -> bool:
        """Check if two frequencies are related"""
        # Extract numeric values
        try:
            val_a = int(freq_a.split('.')[-1])
            val_b = int(freq_b.split('.')[-1])
            
            # Check if they're harmonically related (octaves, fifths, etc.)
            if val_a == val_b:
                return True
            elif val_a * 2 == val_b or val_b * 2 == val_a:  # Octave
                return True
            elif abs(val_a - val_b) <= 100:  # Close frequencies
                return True
            
        except (ValueError, IndexError):
            pass
        
        return False
    
    def _calculate_vibrational_similarity(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> float:
        """Calculate vibrational similarity between two nodes"""
        if not node_a.vibrational_axes or not node_b.vibrational_axes:
            return 0.5
        
        # Find common axes
        common_axes = set(node_a.vibrational_axes) & set(node_b.vibrational_axes)
        
        if not common_axes:
            return 0.3  # No common axes = lower similarity
        
        # Calculate similarity based on common axes
        similarity = 0.3 + (len(common_axes) * 0.2)
        
        return min(1.0, similarity)
    
    def _calculate_fractal_relationship(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> float:
        """Calculate fractal relationship between two nodes"""
        # Parent-child relationship
        if node_a.node_id == node_b.parent_id or node_b.node_id == node_a.parent_id:
            return 0.8
        
        # Sibling relationship (same parent)
        if node_a.parent_id and node_a.parent_id == node_b.parent_id:
            return 0.6
        
        # Same fractal layer
        if node_a.fractal_layer == node_b.fractal_layer:
            return 0.5
        
        # Adjacent layers
        if abs(node_a.fractal_layer - node_b.fractal_layer) == 1:
            return 0.4
        
        # Distant layers
        return 0.2
    
    # ============================================================================
    # RESONANCE CLUSTERING
    # ============================================================================
    
    def form_resonance_clusters(self, nodes: List[EnhancedGenericNode], 
                               min_cluster_size: int = 3) -> List[ResonanceCluster]:
        """
        Form resonance clusters from nodes
        
        Args:
            nodes: List of nodes to cluster
            min_cluster_size: Minimum size for a cluster
        
        Returns:
            List of formed resonance clusters
        """
        clusters = []
        
        # Group nodes by resonance pattern
        pattern_groups = defaultdict(list)
        for node in nodes:
            pattern_groups[node.resonance_pattern].append(node)
        
        # Form clusters for each pattern
        for pattern, pattern_nodes in pattern_groups.items():
            if len(pattern_nodes) >= min_cluster_size:
                # Find center node (highest coherence)
                center_node = max(pattern_nodes, key=lambda n: n.coherence_score)
                
                # Create cluster
                cluster = ResonanceCluster(
                    cluster_id=f"cluster_{pattern}_{len(clusters)}",
                    center_node_id=center_node.node_id,
                    member_node_ids=[n.node_id for n in pattern_nodes],
                    average_resonance_score=sum(n.coherence_score for n in pattern_nodes) / len(pattern_nodes),
                    cluster_coherence=self._calculate_cluster_coherence(pattern_nodes),
                    vibrational_theme=self._identify_vibrational_theme(pattern_nodes),
                    water_state_theme=self._identify_water_state_theme(pattern_nodes),
                    created_at=datetime.now().isoformat(),
                    updated_at=datetime.now().isoformat()
                )
                
                clusters.append(cluster)
                self._resonance_clusters[cluster.cluster_id] = cluster
        
        return clusters
    
    def _calculate_cluster_coherence(self, nodes: List[EnhancedGenericNode]) -> float:
        """Calculate coherence of a cluster"""
        if not nodes:
            return 0.0
        
        # Calculate average coherence
        avg_coherence = sum(n.coherence_score for n in nodes) / len(nodes)
        
        # Calculate coherence variance (lower variance = higher cluster coherence)
        variance = sum((n.coherence_score - avg_coherence) ** 2 for n in nodes) / len(nodes)
        coherence_penalty = variance * 0.5
        
        return max(0.0, avg_coherence - coherence_penalty)
    
    def _identify_vibrational_theme(self, nodes: List[EnhancedGenericNode]) -> str:
        """Identify the vibrational theme of a cluster"""
        if not nodes:
            return "neutral"
        
        # Count vibrational axes
        axis_counts = defaultdict(int)
        for node in nodes:
            for axis in node.vibrational_axes:
                axis_counts[axis] += 1
        
        if not axis_counts:
            return "neutral"
        
        # Find most common axis
        most_common = max(axis_counts.items(), key=lambda x: x[1])
        return most_common[0]
    
    def _identify_water_state_theme(self, nodes: List[EnhancedGenericNode]) -> str:
        """Identify the water state theme of a cluster"""
        if not nodes:
            return "neutral"
        
        # Count water states
        state_counts = defaultdict(int)
        for node in nodes:
            state_counts[node.water_state] += 1
        
        # Find most common water state
        most_common = max(state_counts.items(), key=lambda x: x[1])
        return most_common[0]
    
    # ============================================================================
    # COLLECTIVE INTELLIGENCE EMERGENCE
    # ============================================================================
    
    def calculate_collective_resonance(self, group_nodes: List[EnhancedGenericNode], 
                                     group_id: str, 
                                     group_type: str = "system") -> CollectiveResonanceState:
        """
        Calculate collective resonance for a group of nodes
        
        Args:
            group_nodes: List of nodes in the group
            group_id: Unique identifier for the group
            group_type: Type of group ("system", "component", "community", "federation")
        
        Returns:
            Collective resonance state for the group
        """
        if not group_nodes:
            return self._get_default_collective_state(group_id, group_type)
        
        try:
            # Calculate collective vibrational alignment
            vibrational_axes = self._calculate_collective_vibrational_alignment(group_nodes)
            
            # Calculate overall coherence
            overall_coherence = self._calculate_collective_coherence(group_nodes)
            
            # Determine collective resonance pattern
            resonance_pattern = self._determine_collective_pattern(overall_coherence)
            
            # Create collective state
            collective_state = CollectiveResonanceState(
                group_id=group_id,
                group_type=group_type,
                vibrational_axes=vibrational_axes,
                overall_coherence=overall_coherence,
                resonance_pattern=resonance_pattern,
                member_count=len(group_nodes),
                last_calculation=datetime.now().isoformat(),
                metadata={
                    'node_types': list(set(n.node_type for n in group_nodes)),
                    'water_states': list(set(n.water_state for n in group_nodes)),
                    'chakras': list(set(n.chakra for n in group_nodes)),
                    'fractal_layers': list(set(n.fractal_layer for n in group_nodes))
                }
            )
            
            # Store the collective state
            self._collective_states[group_id] = collective_state
            
            return collective_state
            
        except Exception as e:
            print(f"Error calculating collective resonance for group {group_id}: {e}")
            return self._get_default_collective_state(group_id, group_type)
    
    def _calculate_collective_vibrational_alignment(self, nodes: List[EnhancedGenericNode]) -> Dict[str, float]:
        """Calculate collective vibrational alignment across all axes"""
        # Get all unique vibrational axes
        all_axes = set()
        for node in nodes:
            all_axes.update(node.vibrational_axes)
        
        if not all_axes:
            return {}
        
        collective_alignment = {}
        
        for axis in all_axes:
            # Calculate average alignment for this axis
            axis_nodes = [n for n in nodes if axis in n.vibrational_axes]
            
            if axis_nodes:
                # Use coherence scores as alignment indicators
                avg_alignment = sum(n.coherence_score for n in axis_nodes) / len(axis_nodes)
                collective_alignment[axis] = avg_alignment
        
        return collective_alignment
    
    def _calculate_collective_coherence(self, nodes: List[EnhancedGenericNode]) -> float:
        """Calculate collective coherence for the group"""
        if not nodes:
            return 0.0
        
        # Calculate average individual coherence
        avg_coherence = sum(n.coherence_score for n in nodes) / len(nodes)
        
        # Calculate coherence amplification factor (emergent property)
        # Groups with similar resonance patterns amplify each other
        pattern_counts = defaultdict(int)
        for node in nodes:
            pattern_counts[node.resonance_pattern] += 1
        
        # Calculate pattern diversity (lower diversity = higher amplification)
        total_nodes = len(nodes)
        pattern_diversity = len(pattern_counts) / total_nodes
        
        # Amplification factor (inverse of diversity)
        amplification_factor = 1.0 - pattern_diversity
        
        # Apply amplification
        collective_coherence = avg_coherence + (amplification_factor * 0.2)
        
        return min(1.0, max(0.0, collective_coherence))
    
    def _determine_collective_pattern(self, coherence: float) -> str:
        """Determine collective resonance pattern based on coherence"""
        if coherence >= 0.8:
            return "harmonic"
        elif coherence >= 0.6:
            return "sympathetic"
        elif coherence >= 0.4:
            return "neutral"
        elif coherence >= 0.2:
            return "dissonant"
        else:
            return "destructive"
    
    def _get_default_collective_state(self, group_id: str, group_type: str) -> CollectiveResonanceState:
        """Get default collective state when calculation fails"""
        return CollectiveResonanceState(
            group_id=group_id,
            group_type=group_type,
            vibrational_axes={},
            overall_coherence=0.5,
            resonance_pattern="neutral",
            member_count=0,
            last_calculation=datetime.now().isoformat(),
            metadata={}
        )
    
    # ============================================================================
    # SYSTEM STATISTICS AND REPORTING
    # ============================================================================
    
    def get_resonance_statistics(self) -> Dict[str, Any]:
        """Get comprehensive resonance system statistics"""
        return {
            'system_info': {
                'name': 'Advanced Resonance System',
                'version': '1.0.0',
                'last_calculation': self._resonance_stats['last_calculation']
            },
            'resonance_stats': self._resonance_stats,
            'relationship_counts': {
                'total_relationships': len(self._harmonic_relationships),
                'by_type': self._count_relationships_by_type()
            },
            'cluster_counts': {
                'total_clusters': len(self._resonance_clusters),
                'by_pattern': self._count_clusters_by_pattern()
            },
            'collective_states': {
                'total_groups': len(self._collective_states),
                'by_type': self._count_collective_states_by_type()
            },
            'cache_info': {
                'cache_size': len(self._resonance_cache),
                'cache_ttl': self._cache_ttl
            }
        }
    
    def _count_relationships_by_type(self) -> Dict[str, int]:
        """Count relationships by type"""
        counts = defaultdict(int)
        for rel in self._harmonic_relationships.values():
            counts[rel.relationship_type] += 1
        return dict(counts)
    
    def _count_clusters_by_pattern(self) -> Dict[str, int]:
        """Count clusters by resonance pattern"""
        counts = defaultdict(int)
        for cluster in self._resonance_clusters.values():
            counts[cluster.vibrational_theme] += 1
        return dict(counts)
    
    def _count_collective_states_by_type(self) -> Dict[str, int]:
        """Count collective states by group type"""
        counts = defaultdict(int)
        for state in self._collective_states.values():
            counts[state.group_type] += 1
        return dict(counts)
    
    def _update_resonance_stats(self):
        """Update resonance system statistics"""
        self._resonance_stats['total_calculations'] += 1
        self._resonance_stats['last_calculation'] = datetime.now().isoformat()
    
    def clear_cache(self):
        """Clear resonance calculation cache"""
        self._resonance_cache.clear()
        print("🎵 Resonance cache cleared")
    
    def export_resonance_report(self, output_format: str = "json") -> Union[str, Dict[str, Any]]:
        """
        Export comprehensive resonance report
        
        Args:
            output_format: "json" or "dict"
        
        Returns:
            Resonance report in requested format
        """
        report = {
            'resonance_system_info': {
                'name': 'Advanced Resonance System',
                'version': '1.0.0',
                'exported_at': datetime.now().isoformat()
            },
            'statistics': self.get_resonance_statistics(),
            'harmonic_relationships': [
                {
                    'id': rel_id,
                    'node_a': rel.node_a_id,
                    'node_b': rel.node_b_id,
                    'type': rel.relationship_type,
                    'strength': rel.strength
                }
                for rel_id, rel in self._harmonic_relationships.items()
            ],
            'resonance_clusters': [
                {
                    'id': cluster.cluster_id,
                    'center_node': cluster.center_node_id,
                    'member_count': len(cluster.member_node_ids),
                    'coherence': cluster.cluster_coherence,
                    'theme': cluster.vibrational_theme
                }
                for cluster in self._resonance_clusters.values()
            ],
            'collective_states': [
                {
                    'group_id': state.group_id,
                    'group_type': state.group_type,
                    'coherence': state.overall_coherence,
                    'pattern': state.resonance_pattern,
                    'member_count': state.member_count
                }
                for state in self._collective_states.values()
            ]
        }
        
        if output_format.lower() == "json":
            return json.dumps(report, indent=2, default=str)
        else:
            return report

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global advanced resonance system instance
advanced_resonance_system = AdvancedResonanceSystem()

if __name__ == "__main__":
    # Test the advanced resonance system
    print("🎵 Advanced Resonance System Test")
    
    # Test basic functionality
    print(f"System initialized with {len(advanced_resonance_system._harmonic_relationships)} relationships")
    print(f"Cache TTL: {advanced_resonance_system._cache_ttl} seconds")
    
    # Test statistics
    stats = advanced_resonance_system.get_resonance_statistics()
    print(f"Statistics: {stats['resonance_stats']['total_calculations']} calculations")
    
    print("\n✅ Advanced Resonance System ready for use!")
