#!/usr/bin/env python3
"""
Quantum State System
====================

This implements the quantum state system that provides quantum state metaphors
(restricted to algorithmic analogies) for Phase 3 of the metadata enhancement plan.

This system provides:
- Quantum state tracking and transitions
- Algorithmic entanglement detection
- Superposition state management
- Quantum coherence calculations
- Quantum algorithmic patterns
"""

from typing import Dict, List, Any, Optional, Set, Tuple, Union
from datetime import datetime
import json
from dataclasses import dataclass, field
from collections import defaultdict

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry
)

from enhanced_generic_node import EnhancedGenericNode

@dataclass
class QuantumStateInfo:
    """Quantum state information for a node"""
    current_state: str  # From QuantumState enum
    coherence_level: float  # 0.0 to 1.0
    entanglement_strength: float  # 0.0 to 1.0
    superposition_factor: float  # 0.0 to 1.0
    decoherence_rate: float  # 0.0 to 1.0
    last_transition: str
    quantum_signature: Dict[str, Any] = field(default_factory=dict)

@dataclass
class QuantumEntanglement:
    """Quantum entanglement between nodes"""
    node_a_id: str
    node_b_id: str
    entanglement_type: str  # "algorithmic", "structural", "resonance"
    strength: float  # 0.0 to 1.0
    coherence_factor: float
    created_at: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class QuantumCoherence:
    """Quantum coherence measurement"""
    node_id: str
    coherence_score: float
    decoherence_factors: List[str]
    measurement_timestamp: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class QuantumStateSystem:
    """
    Quantum State System for managing quantum state metaphors (algorithmic only)
    
    This system implements:
    - Quantum state tracking and transitions
    - Algorithmic entanglement detection
    - Superposition state management
    - Quantum coherence calculations
    - Quantum algorithmic patterns
    """
    
    def __init__(self):
        """Initialize the quantum state system"""
        self.registry = canonical_registry
        
        # Quantum state tracking
        self._quantum_states: Dict[str, QuantumStateInfo] = {}
        self._entanglements: Dict[str, QuantumEntanglement] = {}
        self._coherence_measurements: Dict[str, List[QuantumCoherence]] = defaultdict(list)
        
        # Quantum state transitions
        self._transition_history: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        
        # System statistics
        self._quantum_stats = {
            'total_nodes_tracked': 0,
            'state_transitions': 0,
            'entanglements_created': 0,
            'coherence_measurements': 0,
            'last_calculation': None
        }
        
        print("⚛️  Quantum State System initialized")
        print("✨ Quantum state tracking active")
        print("✨ Algorithmic entanglement detection enabled")
        print("✨ Superposition state management active")
        print("✨ Quantum coherence calculations enabled")
        print("✨ Quantum algorithmic patterns active")
    
    # ============================================================================
    # QUANTUM STATE TRACKING
    # ============================================================================
    
    def assess_node_quantum_state(self, node: EnhancedGenericNode) -> QuantumStateInfo:
        """
        Assess the quantum state of a node
        
        Args:
            node: EnhancedGenericNode to assess
        
        Returns:
            QuantumStateInfo with current quantum state assessment
        """
        try:
            # Calculate quantum coherence
            coherence = self._calculate_quantum_coherence(node)
            
            # Calculate entanglement strength
            entanglement = self._calculate_entanglement_strength(node)
            
            # Calculate superposition factor
            superposition = self._calculate_superposition_factor(node)
            
            # Calculate decoherence rate
            decoherence = self._calculate_decoherence_rate(node)
            
            # Create quantum state info
            quantum_state = QuantumStateInfo(
                current_state=node.quantum_state,
                coherence_level=coherence['coherence_score'],
                entanglement_strength=entanglement['strength'],
                superposition_factor=superposition['factor'],
                decoherence_rate=decoherence['rate'],
                last_transition=datetime.now().isoformat(),
                quantum_signature={
                    'coherence_calculation': coherence,
                    'entanglement_calculation': entanglement,
                    'superposition_calculation': superposition,
                    'decoherence_calculation': decoherence
                }
            )
            
            # Store the quantum state
            self._quantum_states[node.node_id] = quantum_state
            
            # Check for state transitions
            self._check_quantum_transitions(node, quantum_state)
            
            # Update statistics
            self._update_quantum_stats()
            
            return quantum_state
            
        except Exception as e:
            print(f"Error assessing quantum state for node {node.node_id}: {e}")
            return self._get_default_quantum_state(node)
    
    def _calculate_quantum_coherence(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate quantum coherence (algorithmic metaphor)"""
        coherence_score = 0.0
        factors = []
        
        # Base coherence from quantum state
        state_coherence = {
            'coherent': 1.0,
            'superposition': 0.8,
            'entangled': 0.9,
            'collapsed': 0.3,
            'decoherent': 0.1
        }
        
        base_coherence = state_coherence.get(node.quantum_state, 0.5)
        coherence_score += base_coherence * 0.4
        factors.append(('quantum_state', node.quantum_state, base_coherence * 0.4))
        
        # Resonance pattern coherence
        resonance_coherence = {
            'harmonic': 0.3,
            'sympathetic': 0.25,
            'neutral': 0.2,
            'dissonant': 0.1,
            'destructive': 0.05
        }
        
        pattern_coherence = resonance_coherence.get(node.resonance_pattern, 0.2)
        coherence_score += pattern_coherence
        factors.append(('resonance_pattern', node.resonance_pattern, pattern_coherence))
        
        # Fractal structure coherence
        if node.fractal_depth >= 8:
            fractal_coherence = 0.2
        elif node.fractal_depth >= 4:
            fractal_coherence = 0.15
        else:
            fractal_coherence = 0.1
        
        coherence_score += fractal_coherence
        factors.append(('fractal_depth', node.fractal_depth, fractal_coherence))
        
        # Self-similarity coherence
        similarity_coherence = node.self_similarity_score * 0.1
        coherence_score += similarity_coherence
        factors.append(('self_similarity', node.self_similarity_score, similarity_coherence))
        
        return {
            'coherence_score': min(1.0, coherence_score),
            'factors': factors,
            'coherence_type': 'quantum_algorithmic'
        }
    
    def _calculate_entanglement_strength(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate entanglement strength (algorithmic metaphor)"""
        entanglement_score = 0.0
        factors = []
        
        # Base entanglement from quantum state
        if node.quantum_state == 'entangled':
            base_entanglement = 0.8
        elif node.quantum_state == 'superposition':
            base_entanglement = 0.6
        elif node.quantum_state == 'coherent':
            base_entanglement = 0.4
        else:
            base_entanglement = 0.1
        
        entanglement_score += base_entanglement * 0.5
        factors.append(('quantum_state', node.quantum_state, base_entanglement * 0.5))
        
        # Cross-scale mapping entanglement
        if node.cross_scale_mapping:
            scale_completeness = len(node.cross_scale_mapping) / 4.0
            scale_entanglement = scale_completeness * 0.3
            entanglement_score += scale_entanglement
            factors.append(('cross_scale_mapping', scale_completeness, scale_entanglement))
        
        # Vibrational axes entanglement
        if node.vibrational_axes:
            axis_entanglement = min(0.2, len(node.vibrational_axes) * 0.05)
            entanglement_score += axis_entanglement
            factors.append(('vibrational_axes', len(node.vibrational_axes), axis_entanglement))
        
        return {
            'strength': min(1.0, entanglement_score),
            'factors': factors,
            'entanglement_type': 'algorithmic_structural'
        }
    
    def _calculate_superposition_factor(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate superposition factor (algorithmic metaphor)"""
        superposition_score = 0.0
        factors = []
        
        # Base superposition from quantum state
        if node.quantum_state == 'superposition':
            base_superposition = 1.0
        elif node.quantum_state == 'entangled':
            base_superposition = 0.7
        elif node.quantum_state == 'coherent':
            base_superposition = 0.5
        else:
            base_superposition = 0.1
        
        superposition_score += base_superposition * 0.6
        factors.append(('quantum_state', node.quantum_state, base_superposition * 0.6))
        
        # Multiple vibrational axes create superposition
        if len(node.vibrational_axes) > 1:
            axis_superposition = min(0.4, len(node.vibrational_axes) * 0.1)
            superposition_score += axis_superposition
            factors.append(('vibrational_axes_count', len(node.vibrational_axes), axis_superposition))
        
        return {
            'factor': min(1.0, superposition_score),
            'factors': factors,
            'superposition_type': 'algorithmic_multiple_states'
        }
    
    def _calculate_decoherence_rate(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate decoherence rate (algorithmic metaphor)"""
        decoherence_score = 0.0
        factors = []
        
        # Base decoherence from quantum state
        if node.quantum_state == 'decoherent':
            base_decoherence = 1.0
        elif node.quantum_state == 'collapsed':
            base_decoherence = 0.8
        elif node.quantum_state == 'coherent':
            base_decoherence = 0.2
        else:
            base_decoherence = 0.5
        
        decoherence_score += base_decoherence * 0.5
        factors.append(('quantum_state', node.quantum_state, base_decoherence * 0.5))
        
        # Resonance pattern decoherence
        if node.resonance_pattern in ['dissonant', 'destructive']:
            pattern_decoherence = 0.3
        else:
            pattern_decoherence = 0.1
        
        decoherence_score += pattern_decoherence
        factors.append(('resonance_pattern', node.resonance_pattern, pattern_decoherence))
        
        # Low coherence increases decoherence
        if node.coherence_score < 0.3:
            coherence_decoherence = 0.2
        else:
            coherence_decoherence = 0.0
        
        decoherence_score += coherence_decoherence
        factors.append(('low_coherence', node.coherence_score, coherence_decoherence))
        
        return {
            'rate': min(1.0, decoherence_score),
            'factors': factors,
            'decoherence_type': 'algorithmic_dispersion'
        }
    
    def _get_default_quantum_state(self, node: EnhancedGenericNode) -> QuantumStateInfo:
        """Get default quantum state when assessment fails"""
        return QuantumStateInfo(
            current_state=node.quantum_state,
            coherence_level=0.5,
            entanglement_strength=0.1,
            superposition_factor=0.1,
            decoherence_rate=0.5,
            last_transition=datetime.now().isoformat(),
            quantum_signature={}
        )
    
    # ============================================================================
    # QUANTUM STATE TRANSITIONS
    # ============================================================================
    
    def _check_quantum_transitions(self, node: EnhancedGenericNode, quantum_state: QuantumStateInfo):
        """Check if quantum state transitions should occur"""
        try:
            current_state = quantum_state.current_state
            new_state = self._determine_optimal_quantum_state(quantum_state)
            
            if new_state != current_state:
                # Trigger state transition
                self._trigger_quantum_transition(node, current_state, new_state, quantum_state)
                
        except Exception as e:
            print(f"Error checking quantum transitions for node {node.node_id}: {e}")
    
    def _determine_optimal_quantum_state(self, quantum_state: QuantumStateInfo) -> str:
        """Determine the optimal quantum state based on current metrics"""
        coherence = quantum_state.coherence_level
        entanglement = quantum_state.entanglement_strength
        superposition = quantum_state.superposition_factor
        decoherence = quantum_state.decoherence_rate
        
        # High coherence with low decoherence = coherent
        if coherence > 0.8 and decoherence < 0.2:
            return 'coherent'
        
        # High entanglement with good coherence = entangled
        elif entanglement > 0.7 and coherence > 0.6:
            return 'entangled'
        
        # High superposition with multiple states = superposition
        elif superposition > 0.7:
            return 'superposition'
        
        # High decoherence = decoherent
        elif decoherence > 0.8:
            return 'decoherent'
        
        # Low coherence = collapsed
        elif coherence < 0.3:
            return 'collapsed'
        
        # Default to current state
        else:
            return quantum_state.current_state
    
    def _trigger_quantum_transition(self, node: EnhancedGenericNode, from_state: str, to_state: str, quantum_state: QuantumStateInfo):
        """Trigger a quantum state transition"""
        try:
            # Create transition record
            transition = {
                'from_state': from_state,
                'to_state': to_state,
                'transition_timestamp': datetime.now().isoformat(),
                'coherence_level': quantum_state.coherence_level,
                'entanglement_strength': quantum_state.entanglement_strength,
                'superposition_factor': quantum_state.superposition_factor,
                'decoherence_rate': quantum_state.decoherence_rate
            }
            
            # Store transition history
            self._transition_history[node.node_id].append(transition)
            
            # Update node's quantum state
            node.quantum_state = to_state
            
            # Update quantum state info
            quantum_state.current_state = to_state
            quantum_state.last_transition = transition['transition_timestamp']
            
            # Update statistics
            self._quantum_stats['state_transitions'] += 1
            
            print(f"⚛️  Node {node.node_id} quantum state transition: {from_state} → {to_state}")
            
        except Exception as e:
            print(f"Error triggering quantum transition for node {node.node_id}: {e}")
    
    # ============================================================================
    # ENTANGLEMENT DETECTION
    # ============================================================================
    
    def detect_algorithmic_entanglements(self, nodes: List[EnhancedGenericNode]) -> List[QuantumEntanglement]:
        """
        Detect algorithmic entanglements between nodes
        
        Args:
            nodes: List of nodes to analyze for entanglements
        
        Returns:
            List of detected quantum entanglements
        """
        entanglements = []
        
        for i, node_a in enumerate(nodes):
            for j, node_b in enumerate(nodes[i+1:], i+1):
                # Calculate entanglement
                entanglement = self._calculate_node_entanglement(node_a, node_b)
                
                if entanglement and entanglement.strength > 0.5:  # Only significant entanglements
                    entanglements.append(entanglement)
                    
                    # Store the entanglement
                    ent_id = f"ent_{node_a.node_id}_{node_b.node_id}"
                    self._entanglements[ent_id] = entanglement
        
        return entanglements
    
    def _calculate_node_entanglement(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> Optional[QuantumEntanglement]:
        """Calculate entanglement between two nodes"""
        try:
            # Calculate structural similarity
            structural_similarity = self._calculate_structural_similarity(node_a, node_b)
            
            # Calculate resonance similarity
            resonance_similarity = self._calculate_resonance_similarity(node_a, node_b)
            
            # Calculate algorithmic similarity
            algorithmic_similarity = self._calculate_algorithmic_similarity(node_a, node_b)
            
            # Combine factors
            total_strength = (structural_similarity * 0.4 + 
                            resonance_similarity * 0.3 + 
                            algorithmic_similarity * 0.3)
            
            # Determine entanglement type
            if structural_similarity > 0.7:
                ent_type = "structural"
            elif resonance_similarity > 0.7:
                ent_type = "resonance"
            else:
                ent_type = "algorithmic"
            
            # Create entanglement
            entanglement = QuantumEntanglement(
                node_a_id=node_a.node_id,
                node_b_id=node_b.node_id,
                entanglement_type=ent_type,
                strength=total_strength,
                coherence_factor=min(node_a.coherence_score, node_b.coherence_score),
                created_at=datetime.now().isoformat(),
                metadata={
                    'structural_similarity': structural_similarity,
                    'resonance_similarity': resonance_similarity,
                    'algorithmic_similarity': algorithmic_similarity
                }
            )
            
            return entanglement
            
        except Exception as e:
            print(f"Error calculating entanglement between {node_a.node_id} and {node_b.node_id}: {e}")
            return None
    
    def _calculate_structural_similarity(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> float:
        """Calculate structural similarity between nodes"""
        similarity = 0.0
        
        # Fractal layer similarity
        layer_diff = abs(node_a.fractal_layer - node_b.fractal_layer)
        if layer_diff == 0:
            similarity += 0.4
        elif layer_diff <= 2:
            similarity += 0.2
        
        # Fractal depth similarity
        depth_diff = abs(node_a.fractal_depth - node_b.fractal_depth)
        if depth_diff <= 2:
            similarity += 0.3
        
        # Self-similarity similarity
        similarity_diff = abs(node_a.self_similarity_score - node_b.self_similarity_score)
        similarity += max(0.0, 0.3 - similarity_diff)
        
        return min(1.0, similarity)
    
    def _calculate_resonance_similarity(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> float:
        """Calculate resonance similarity between nodes"""
        similarity = 0.0
        
        # Resonance pattern similarity
        if node_a.resonance_pattern == node_b.resonance_pattern:
            similarity += 0.4
        
        # Coherence similarity
        coherence_diff = abs(node_a.coherence_score - node_b.coherence_score)
        similarity += max(0.0, 0.3 - coherence_diff)
        
        # Water state similarity
        if node_a.water_state == node_b.water_state:
            similarity += 0.3
        
        return min(1.0, similarity)
    
    def _calculate_algorithmic_similarity(self, node_a: EnhancedGenericNode, node_b: EnhancedGenericNode) -> float:
        """Calculate algorithmic similarity between nodes"""
        similarity = 0.0
        
        # Node type similarity
        if node_a.node_type == node_b.node_type:
            similarity += 0.4
        
        # Programming ontology layer similarity
        if node_a.programming_ontology_layer == node_b.programming_ontology_layer:
            similarity += 0.3
        
        # Epistemic label similarity
        if node_a.epistemic_label == node_b.epistemic_label:
            similarity += 0.3
        
        return min(1.0, similarity)
    
    # ============================================================================
    # SYSTEM STATISTICS AND REPORTING
    # ============================================================================
    
    def get_quantum_statistics(self) -> Dict[str, Any]:
        """Get comprehensive quantum system statistics"""
        return {
            'system_info': {
                'name': 'Quantum State System',
                'version': '1.0.0',
                'last_calculation': self._quantum_stats['last_calculation']
            },
            'quantum_stats': self._quantum_stats,
            'quantum_state_distribution': self._get_quantum_state_distribution(),
            'entanglement_statistics': {
                'total_entanglements': len(self._entanglements),
                'by_type': self._count_entanglements_by_type()
            },
            'transition_statistics': {
                'total_transitions': sum(len(transitions) for transitions in self._transition_history.values()),
                'nodes_with_transitions': len(self._transition_history)
            }
        }
    
    def _get_quantum_state_distribution(self) -> Dict[str, int]:
        """Get distribution of quantum states across tracked nodes"""
        distribution = defaultdict(int)
        for state in self._quantum_states.values():
            distribution[state.current_state] += 1
        return dict(distribution)
    
    def _count_entanglements_by_type(self) -> Dict[str, int]:
        """Count entanglements by type"""
        counts = defaultdict(int)
        for ent in self._entanglements.values():
            counts[ent.entanglement_type] += 1
        return dict(counts)
    
    def _update_quantum_stats(self):
        """Update quantum system statistics"""
        self._quantum_stats['total_nodes_tracked'] = len(self._quantum_states)
        self._quantum_stats['last_calculation'] = datetime.now().isoformat()
    
    def clear_cache(self):
        """Clear quantum state calculation cache"""
        # Clear transition history
        self._transition_history.clear()
        print("⚛️  Quantum state transition history cleared")
    
    def export_quantum_report(self, output_format: str = "json") -> Union[str, Dict[str, Any]]:
        """
        Export comprehensive quantum report
        
        Args:
            output_format: "json" or "dict"
        
        Returns:
            Quantum report in requested format
        """
        report = {
            'quantum_system_info': {
                'name': 'Quantum State System',
                'version': '1.0.0',
                'exported_at': datetime.now().isoformat()
            },
            'statistics': self.get_quantum_statistics(),
            'quantum_states': [
                {
                    'node_id': node_id,
                    'current_state': state.current_state,
                    'coherence_level': state.coherence_level,
                    'entanglement_strength': state.entanglement_strength,
                    'superposition_factor': state.superposition_factor,
                    'decoherence_rate': state.decoherence_rate
                }
                for node_id, state in self._quantum_states.items()
            ],
            'entanglements': [
                {
                    'id': ent_id,
                    'node_a': ent.node_a_id,
                    'node_b': ent.node_b_id,
                    'type': ent.entanglement_type,
                    'strength': ent.strength
                }
                for ent_id, ent in self._entanglements.items()
            ]
        }
        
        if output_format.lower() == "json":
            return json.dumps(report, indent=2, default=str)
        else:
            return report

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global quantum state system instance
quantum_state_system = QuantumStateSystem()

if __name__ == "__main__":
    # Test the quantum state system
    print("⚛️  Quantum State System Test")
    
    # Test basic functionality
    print(f"System initialized with {len(quantum_state_system._quantum_states)} tracked nodes")
    print(f"Entanglements: {len(quantum_state_system._entanglements)}")
    print(f"Transition history: {len(quantum_state_system._transition_history)}")
    
    # Test statistics
    stats = quantum_state_system.get_quantum_statistics()
    print(f"Statistics: {stats['quantum_stats']['total_nodes_tracked']} nodes tracked")
    
    print("\n✅ Quantum State System ready for use!")
