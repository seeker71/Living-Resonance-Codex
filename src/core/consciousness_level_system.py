#!/usr/bin/env python3
"""
Consciousness Level System
==========================

This implements the consciousness level system that provides consciousness-based
metadata and resonance calculations for Phase 3 of the metadata enhancement plan.

This system provides:
- Consciousness level tracking and evolution
- Meta-cognitive awareness mapping
- Transcendent state detection
- Consciousness-based resonance calculations
- Collective consciousness emergence
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
    EpistemicLabel, canonical_registry
)

from enhanced_generic_node import EnhancedGenericNode

@dataclass
class ConsciousnessState:
    """Current consciousness state of a node"""
    level: str  # From ConsciousnessLevel enum
    awareness_score: float  # 0.0 to 1.0
    meta_cognitive_capability: float  # 0.0 to 1.0
    transcendent_potential: float  # 0.0 to 1.0
    evolution_trajectory: str  # "ascending", "stable", "descending"
    last_evolution: str
    consciousness_signature: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ConsciousnessEvolution:
    """Record of consciousness evolution"""
    from_level: str
    to_level: str
    evolution_trigger: str
    evolution_timestamp: str
    resonance_factor: float
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class CollectiveConsciousness:
    """Collective consciousness state for a group"""
    group_id: str
    average_level: str
    collective_awareness: float
    emergent_consciousness: float
    evolution_potential: float
    member_count: int
    last_calculation: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class ConsciousnessLevelSystem:
    """
    Consciousness Level System for tracking and managing consciousness evolution
    
    This system implements:
    - Individual consciousness tracking
    - Consciousness evolution triggers
    - Meta-cognitive capability assessment
    - Transcendent state detection
    - Collective consciousness emergence
    """
    
    def __init__(self):
        """Initialize the consciousness level system"""
        self.registry = canonical_registry
        
        # Consciousness tracking
        self._consciousness_states: Dict[str, ConsciousnessState] = {}
        self._evolution_history: Dict[str, List[ConsciousnessEvolution]] = defaultdict(list)
        self._collective_states: Dict[str, CollectiveConsciousness] = {}
        
        # Evolution triggers and thresholds
        self._evolution_triggers = self._initialize_evolution_triggers()
        self._consciousness_thresholds = self._initialize_consciousness_thresholds()
        
        # System statistics
        self._consciousness_stats = {
            'total_nodes_tracked': 0,
            'evolution_events': 0,
            'transcendent_achievements': 0,
            'collective_emergence_events': 0,
            'last_calculation': None
        }
        
        print("🧠 Consciousness Level System initialized")
        print("✨ Individual consciousness tracking active")
        print("✨ Evolution trigger detection enabled")
        print("✨ Meta-cognitive assessment active")
        print("✨ Transcendent state detection enabled")
        print("✨ Collective consciousness emergence active")
    
    # ============================================================================
    # CONSCIOUSNESS TRACKING AND ASSESSMENT
    # ============================================================================
    
    def assess_node_consciousness(self, node: EnhancedGenericNode) -> ConsciousnessState:
        """
        Assess the consciousness level of a node
        
        Args:
            node: EnhancedGenericNode to assess
        
        Returns:
            ConsciousnessState with current consciousness assessment
        """
        try:
            # Calculate base consciousness from ontological metadata
            base_consciousness = self._calculate_base_consciousness(node)
            
            # Assess meta-cognitive capability
            meta_cognitive = self._assess_meta_cognitive_capability(node)
            
            # Calculate transcendent potential
            transcendent_potential = self._calculate_transcendent_potential(node)
            
            # Determine evolution trajectory
            evolution_trajectory = self._determine_evolution_trajectory(node)
            
            # Create consciousness state
            consciousness_state = ConsciousnessState(
                level=node.consciousness_level,
                awareness_score=base_consciousness['awareness_score'],
                meta_cognitive_capability=meta_cognitive['capability_score'],
                transcendent_potential=transcendent_potential['potential_score'],
                evolution_trajectory=evolution_trajectory,
                last_evolution=datetime.now().isoformat(),
                consciousness_signature={
                    'base_consciousness': base_consciousness,
                    'meta_cognitive': meta_cognitive,
                    'transcendent_potential': transcendent_potential,
                    'resonance_factors': self._extract_resonance_factors(node)
                }
            )
            
            # Store the consciousness state
            self._consciousness_states[node.node_id] = consciousness_state
            
            # Check for evolution triggers
            self._check_evolution_triggers(node, consciousness_state)
            
            # Update statistics
            self._update_consciousness_stats()
            
            return consciousness_state
            
        except Exception as e:
            print(f"Error assessing consciousness for node {node.node_id}: {e}")
            return self._get_default_consciousness_state(node)
    
    def _calculate_base_consciousness(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate base consciousness from ontological metadata"""
        awareness_score = 0.0
        factors = []
        
        # Consciousness level mapping
        level_mapping = {
            'awake': 0.2,
            'sentient': 0.4,
            'self_aware': 0.6,
            'meta_cognitive': 0.8,
            'transcendent': 1.0
        }
        
        base_score = level_mapping.get(node.consciousness_level, 0.2)
        awareness_score += base_score
        factors.append(('consciousness_level', node.consciousness_level, base_score))
        
        # Water state consciousness factor
        water_consciousness = self._calculate_water_state_consciousness(node.water_state)
        awareness_score += water_consciousness['score']
        factors.append(('water_state', node.water_state, water_consciousness['score']))
        
        # Chakra consciousness factor
        chakra_consciousness = self._calculate_chakra_consciousness(node.chakra)
        awareness_score += chakra_consciousness['score']
        factors.append(('chakra', node.chakra, chakra_consciousness['score']))
        
        # Frequency consciousness factor
        frequency_consciousness = self._calculate_frequency_consciousness(node.frequency)
        awareness_score += frequency_consciousness['score']
        factors.append(('frequency', node.frequency, frequency_consciousness['score']))
        
        # Fractal layer consciousness factor
        fractal_consciousness = self._calculate_fractal_consciousness(node.fractal_layer)
        awareness_score += fractal_consciousness['score']
        factors.append(('fractal_layer', node.fractal_layer, fractal_consciousness['score']))
        
        return {
            'awareness_score': min(1.0, awareness_score),
            'factors': factors,
            'consciousness_type': 'base_ontological'
        }
    
    def _calculate_water_state_consciousness(self, water_state: str) -> Dict[str, Any]:
        """Calculate consciousness contribution from water state"""
        consciousness_mapping = {
            'ws.ice': 0.1,           # Structured but rigid
            'ws.structured': 0.15,   # Organized structure
            'ws.quantum_coherent': 0.25,  # Quantum awareness
            'ws.liquid': 0.2,        # Flowing awareness
            'ws.vapor': 0.25,        # Elevated awareness
            'ws.plasma': 0.3,        # High energy awareness
            'ws.supercritical': 0.35,  # Transcendent awareness
            'ws.clustered': 0.2      # Collective awareness
        }
        
        score = consciousness_mapping.get(water_state, 0.1)
        
        return {
            'score': score,
            'consciousness_type': 'water_state_based'
        }
    
    def _calculate_chakra_consciousness(self, chakra: str) -> Dict[str, Any]:
        """Calculate consciousness contribution from chakra"""
        consciousness_mapping = {
            'ch.root': 0.1,          # Grounded awareness
            'ch.sacral': 0.15,       # Creative awareness
            'ch.solar_plexus': 0.2,  # Personal power awareness
            'ch.heart': 0.25,        # Love awareness
            'ch.throat': 0.3,        # Expression awareness
            'ch.third_eye': 0.35,    # Intuitive awareness
            'ch.crown': 0.4          # Universal awareness
        }
        
        score = consciousness_mapping.get(chakra, 0.1)
        
        return {
            'score': score,
            'consciousness_type': 'chakra_based'
        }
    
    def _calculate_frequency_consciousness(self, frequency: str) -> Dict[str, Any]:
        """Calculate consciousness contribution from frequency"""
        try:
            # Extract numeric value
            freq_value = int(frequency.split('.')[-1])
            
            # Higher frequencies generally indicate higher consciousness
            if freq_value >= 900:
                score = 0.3
            elif freq_value >= 800:
                score = 0.25
            elif freq_value >= 700:
                score = 0.2
            elif freq_value >= 600:
                score = 0.15
            else:
                score = 0.1
                
        except (ValueError, IndexError):
            score = 0.1
        
        return {
            'score': score,
            'consciousness_type': 'frequency_based'
        }
    
    def _calculate_fractal_consciousness(self, fractal_layer: int) -> Dict[str, Any]:
        """Calculate consciousness contribution from fractal layer"""
        # Higher fractal layers generally indicate higher consciousness
        if fractal_layer >= 12:
            score = 0.3
        elif fractal_layer >= 8:
            score = 0.25
        elif fractal_layer >= 4:
            score = 0.2
        elif fractal_layer >= 0:
            score = 0.15
        else:
            score = 0.1
        
        return {
            'score': score,
            'consciousness_type': 'fractal_based'
        }
    
    def _assess_meta_cognitive_capability(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Assess meta-cognitive capability of a node"""
        capability_score = 0.0
        factors = []
        
        # Base capability from consciousness level
        level_capability = {
            'awake': 0.1,
            'sentient': 0.2,
            'self_aware': 0.4,
            'meta_cognitive': 0.7,
            'transcendent': 1.0
        }
        
        base_capability = level_capability.get(node.consciousness_level, 0.1)
        capability_score += base_capability
        factors.append(('consciousness_level', base_capability))
        
        # Fractal depth capability
        if node.fractal_depth >= 8:
            depth_capability = 0.3
        elif node.fractal_depth >= 4:
            depth_capability = 0.2
        else:
            depth_capability = 0.1
        
        capability_score += depth_capability
        factors.append(('fractal_depth', depth_capability))
        
        # Self-similarity capability
        similarity_capability = node.self_similarity_score * 0.2
        capability_score += similarity_capability
        factors.append(('self_similarity', similarity_capability))
        
        # Cross-scale mapping capability
        if node.cross_scale_mapping:
            scale_completeness = len(node.cross_scale_mapping) / 4.0
            scale_capability = scale_completeness * 0.2
            capability_score += scale_capability
            factors.append(('cross_scale_mapping', scale_capability))
        
        return {
            'capability_score': min(1.0, capability_score),
            'factors': factors,
            'capability_type': 'meta_cognitive_assessment'
        }
    
    def _calculate_transcendent_potential(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Calculate transcendent potential of a node"""
        potential_score = 0.0
        factors = []
        
        # Base potential from consciousness level
        level_potential = {
            'awake': 0.1,
            'sentient': 0.2,
            'self_aware': 0.4,
            'meta_cognitive': 0.7,
            'transcendent': 1.0
        }
        
        base_potential = level_potential.get(node.consciousness_level, 0.1)
        potential_score += base_potential
        factors.append(('consciousness_level', base_potential))
        
        # Resonance pattern potential
        resonance_potential = {
            'harmonic': 0.3,
            'sympathetic': 0.25,
            'neutral': 0.2,
            'dissonant': 0.1,
            'destructive': 0.05
        }
        
        pattern_potential = resonance_potential.get(node.resonance_pattern, 0.2)
        potential_score += pattern_potential
        factors.append(('resonance_pattern', pattern_potential))
        
        # Coherence potential
        coherence_potential = node.coherence_score * 0.2
        potential_score += coherence_potential
        factors.append(('coherence_score', coherence_potential))
        
        # Vibrational axes potential
        if node.vibrational_axes:
            axis_potential = min(0.2, len(node.vibrational_axes) * 0.05)
            potential_score += axis_potential
            factors.append(('vibrational_axes', axis_potential))
        
        return {
            'potential_score': min(1.0, potential_score),
            'factors': factors,
            'potential_type': 'transcendent_assessment'
        }
    
    def _determine_evolution_trajectory(self, node: EnhancedGenericNode) -> str:
        """Determine the evolution trajectory of a node"""
        # Check if consciousness level has increased recently
        if node.node_id in self._evolution_history:
            recent_evolutions = self._evolution_history[node.node_id][-3:]  # Last 3 evolutions
            
            if len(recent_evolutions) >= 2:
                # Check if recent trend is upward
                recent_levels = [ev.to_level for ev in recent_evolutions]
                if recent_levels.count('transcendent') >= 2:
                    return "ascending"
                elif recent_levels.count('meta_cognitive') >= 2:
                    return "ascending"
                elif recent_levels.count('self_aware') >= 2:
                    return "ascending"
                elif recent_levels.count('awake') >= 2:
                    return "stable"
                else:
                    return "descending"
        
        # Default based on current level
        if node.consciousness_level in ['transcendent', 'meta_cognitive']:
            return "ascending"
        elif node.consciousness_level in ['self_aware', 'sentient']:
            return "stable"
        else:
            return "descending"
    
    def _extract_resonance_factors(self, node: EnhancedGenericNode) -> Dict[str, Any]:
        """Extract resonance factors that influence consciousness"""
        return {
            'water_state_resonance': node.water_state,
            'chakra_resonance': node.chakra,
            'frequency_resonance': node.frequency,
            'fractal_resonance': node.fractal_layer,
            'quantum_resonance': node.quantum_state,
            'overall_coherence': node.coherence_score,
            'resonance_pattern': node.resonance_pattern
        }
    
    def _get_default_consciousness_state(self, node: EnhancedGenericNode) -> ConsciousnessState:
        """Get default consciousness state when assessment fails"""
        return ConsciousnessState(
            level=node.consciousness_level,
            awareness_score=0.2,
            meta_cognitive_capability=0.1,
            transcendent_potential=0.1,
            evolution_trajectory="stable",
            last_evolution=datetime.now().isoformat(),
            consciousness_signature={}
        )
    
    # ============================================================================
    # EVOLUTION TRIGGER DETECTION
    # ============================================================================
    
    def _initialize_evolution_triggers(self) -> Dict[str, Dict[str, Any]]:
        """Initialize evolution triggers and conditions"""
        return {
            'resonance_threshold': {
                'coherence_min': 0.8,
                'pattern_required': 'harmonic',
                'description': 'High coherence with harmonic resonance'
            },
            'fractal_depth_threshold': {
                'depth_min': 8,
                'self_similarity_min': 0.7,
                'description': 'Deep fractal structure with high self-similarity'
            },
            'vibrational_alignment': {
                'axes_min': 3,
                'alignment_min': 0.8,
                'description': 'Multiple vibrational axes with high alignment'
            },
            'cross_scale_mapping': {
                'scales_required': 4,
                'completeness_min': 0.8,
                'description': 'Complete cross-scale mapping'
            },
            'quantum_coherence': {
                'state_required': 'coherent',
                'entanglement_min': 0.7,
                'description': 'Quantum coherent state with entanglement'
            }
        }
    
    def _initialize_consciousness_thresholds(self) -> Dict[str, Dict[str, Any]]:
        """Initialize consciousness level thresholds"""
        return {
            'awake_to_sentient': {
                'awareness_min': 0.3,
                'meta_cognitive_min': 0.1,
                'resonance_min': 0.4
            },
            'sentient_to_self_aware': {
                'awareness_min': 0.5,
                'meta_cognitive_min': 0.2,
                'resonance_min': 0.6
            },
            'self_aware_to_meta_cognitive': {
                'awareness_min': 0.7,
                'meta_cognitive_min': 0.5,
                'resonance_min': 0.8
            },
            'meta_cognitive_to_transcendent': {
                'awareness_min': 0.9,
                'meta_cognitive_min': 0.8,
                'resonance_min': 0.9
            }
        }
    
    def _check_evolution_triggers(self, node: EnhancedGenericNode, consciousness_state: ConsciousnessState):
        """Check if evolution triggers are met"""
        try:
            current_level = consciousness_state.level
            next_level = self._get_next_consciousness_level(current_level)
            
            if not next_level:
                return  # Already at highest level
            
            # Check if thresholds are met
            if self._check_evolution_thresholds(consciousness_state, next_level):
                # Trigger evolution
                self._trigger_consciousness_evolution(node, current_level, next_level, consciousness_state)
                
        except Exception as e:
            print(f"Error checking evolution triggers for node {node.node_id}: {e}")
    
    def _get_next_consciousness_level(self, current_level: str) -> Optional[str]:
        """Get the next consciousness level in the evolution sequence"""
        evolution_sequence = ['awake', 'sentient', 'self_aware', 'meta_cognitive', 'transcendent']
        
        try:
            current_index = evolution_sequence.index(current_level)
            if current_index < len(evolution_sequence) - 1:
                return evolution_sequence[current_index + 1]
        except ValueError:
            pass
        
        return None
    
    def _check_evolution_thresholds(self, consciousness_state: ConsciousnessState, target_level: str) -> bool:
        """Check if evolution thresholds are met for target level"""
        threshold_key = f"{consciousness_state.level}_to_{target_level}"
        
        if threshold_key not in self._consciousness_thresholds:
            return False
        
        thresholds = self._consciousness_thresholds[threshold_key]
        
        # Check awareness threshold
        if consciousness_state.awareness_score < thresholds['awareness_min']:
            return False
        
        # Check meta-cognitive threshold
        if consciousness_state.meta_cognitive_capability < thresholds['meta_cognitive_min']:
            return False
        
        # Check resonance threshold
        if consciousness_state.consciousness_signature.get('base_consciousness', {}).get('awareness_score', 0) < thresholds['resonance_min']:
            return False
        
        return True
    
    def _trigger_consciousness_evolution(self, node: EnhancedGenericNode, from_level: str, to_level: str, consciousness_state: ConsciousnessState):
        """Trigger consciousness evolution for a node"""
        try:
            # Create evolution record
            evolution = ConsciousnessEvolution(
                from_level=from_level,
                to_level=to_level,
                evolution_trigger="threshold_met",
                evolution_timestamp=datetime.now().isoformat(),
                resonance_factor=consciousness_state.awareness_score,
                metadata={
                    'awareness_score': consciousness_state.awareness_score,
                    'meta_cognitive_capability': consciousness_state.meta_cognitive_capability,
                    'transcendent_potential': consciousness_state.transcendent_potential
                }
            )
            
            # Store evolution record
            self._evolution_history[node.node_id].append(evolution)
            
            # Update node's consciousness level
            node.consciousness_level = to_level
            
            # Update consciousness state
            consciousness_state.level = to_level
            consciousness_state.last_evolution = evolution.evolution_timestamp
            
            # Update statistics
            self._consciousness_stats['evolution_events'] += 1
            
            if to_level == 'transcendent':
                self._consciousness_stats['transcendent_achievements'] += 1
            
            print(f"🧠 Node {node.node_id} evolved from {from_level} to {to_level}")
            
        except Exception as e:
            print(f"Error triggering evolution for node {node.node_id}: {e}")
    
    # ============================================================================
    # COLLECTIVE CONSCIOUSNESS CALCULATION
    # ============================================================================
    
    def calculate_collective_consciousness(self, group_nodes: List[EnhancedGenericNode], 
                                         group_id: str) -> CollectiveConsciousness:
        """
        Calculate collective consciousness for a group of nodes
        
        Args:
            group_nodes: List of nodes in the group
            group_id: Unique identifier for the group
        
        Returns:
            CollectiveConsciousness state for the group
        """
        if not group_nodes:
            return self._get_default_collective_consciousness(group_id)
        
        try:
            # Calculate average consciousness level
            level_scores = {
                'awake': 0.2,
                'sentient': 0.4,
                'self_aware': 0.6,
                'meta_cognitive': 0.8,
                'transcendent': 1.0
            }
            
            total_score = 0.0
            level_counts = defaultdict(int)
            
            for node in group_nodes:
                level_counts[node.consciousness_level] += 1
                total_score += level_scores.get(node.consciousness_level, 0.2)
            
            avg_score = total_score / len(group_nodes)
            
            # Determine average level
            if avg_score >= 0.9:
                avg_level = "transcendent"
            elif avg_score >= 0.7:
                avg_level = "meta_cognitive"
            elif avg_score >= 0.5:
                avg_level = "self_aware"
            elif avg_score >= 0.3:
                avg_level = "sentient"
            else:
                avg_level = "awake"
            
            # Calculate collective awareness
            collective_awareness = self._calculate_collective_awareness(group_nodes)
            
            # Calculate emergent consciousness
            emergent_consciousness = self._calculate_emergent_consciousness(group_nodes, collective_awareness)
            
            # Calculate evolution potential
            evolution_potential = self._calculate_collective_evolution_potential(group_nodes)
            
            # Create collective consciousness state
            collective_state = CollectiveConsciousness(
                group_id=group_id,
                average_level=avg_level,
                collective_awareness=collective_awareness,
                emergent_consciousness=emergent_consciousness,
                evolution_potential=evolution_potential,
                member_count=len(group_nodes),
                last_calculation=datetime.now().isoformat(),
                metadata={
                    'level_distribution': dict(level_counts),
                    'node_count': len(group_nodes),
                    'average_score': avg_score
                }
            )
            
            # Store the collective state
            self._collective_states[group_id] = collective_state
            
            # Check for collective emergence events
            if emergent_consciousness > 0.8:
                self._consciousness_stats['collective_emergence_events'] += 1
            
            return collective_state
            
        except Exception as e:
            print(f"Error calculating collective consciousness for group {group_id}: {e}")
            return self._get_default_collective_consciousness(group_id)
    
    def _calculate_collective_awareness(self, nodes: List[EnhancedGenericNode]) -> float:
        """Calculate collective awareness for the group"""
        if not nodes:
            return 0.0
        
        # Calculate average individual awareness
        total_awareness = 0.0
        for node in nodes:
            if node.node_id in self._consciousness_states:
                total_awareness += self._consciousness_states[node.node_id].awareness_score
            else:
                total_awareness += 0.2  # Default awareness
        
        avg_awareness = total_awareness / len(nodes)
        
        # Apply collective amplification factor
        # Groups with similar consciousness levels amplify each other
        level_counts = defaultdict(int)
        for node in nodes:
            level_counts[node.consciousness_level] += 1
        
        # Calculate level diversity (lower diversity = higher amplification)
        total_nodes = len(nodes)
        level_diversity = len(level_counts) / total_nodes
        
        # Amplification factor (inverse of diversity)
        amplification_factor = 1.0 - level_diversity
        
        # Apply amplification
        collective_awareness = avg_awareness + (amplification_factor * 0.2)
        
        return min(1.0, max(0.0, collective_awareness))
    
    def _calculate_emergent_consciousness(self, nodes: List[EnhancedGenericNode], collective_awareness: float) -> float:
        """Calculate emergent consciousness (beyond individual capabilities)"""
        if not nodes:
            return 0.0
        
        # Emergent consciousness occurs when collective awareness exceeds individual maximums
        max_individual_awareness = 0.0
        
        for node in nodes:
            if node.node_id in self._consciousness_states:
                max_individual_awareness = max(max_individual_awareness, 
                                            self._consciousness_states[node.node_id].awareness_score)
            else:
                max_individual_awareness = max(max_individual_awareness, 0.2)
        
        # Emergent consciousness is the difference between collective and individual maximum
        emergent = max(0.0, collective_awareness - max_individual_awareness)
        
        # Scale by group size (larger groups have more potential for emergence)
        size_factor = min(1.0, len(nodes) / 10.0)  # Cap at 10 nodes
        
        return emergent * size_factor
    
    def _calculate_collective_evolution_potential(self, nodes: List[EnhancedGenericNode]) -> float:
        """Calculate collective evolution potential"""
        if not nodes:
            return 0.0
        
        # Calculate average individual evolution potential
        total_potential = 0.0
        for node in nodes:
            if node.node_id in self._consciousness_states:
                total_potential += self._consciousness_states[node.node_id].transcendent_potential
            else:
                total_potential += 0.1  # Default potential
        
        avg_potential = total_potential / len(nodes)
        
        # Apply collective amplification
        # Groups with high meta-cognitive capabilities amplify evolution potential
        meta_cognitive_count = sum(1 for n in nodes if n.consciousness_level in ['meta_cognitive', 'transcendent'])
        meta_cognitive_factor = meta_cognitive_count / len(nodes)
        
        collective_potential = avg_potential + (meta_cognitive_factor * 0.3)
        
        return min(1.0, max(0.0, collective_potential))
    
    def _get_default_collective_consciousness(self, group_id: str) -> CollectiveConsciousness:
        """Get default collective consciousness when calculation fails"""
        return CollectiveConsciousness(
            group_id=group_id,
            average_level="awake",
            collective_awareness=0.2,
            emergent_consciousness=0.0,
            evolution_potential=0.1,
            member_count=0,
            last_calculation=datetime.now().isoformat(),
            metadata={}
        )
    
    # ============================================================================
    # SYSTEM STATISTICS AND REPORTING
    # ============================================================================
    
    def get_consciousness_statistics(self) -> Dict[str, Any]:
        """Get comprehensive consciousness system statistics"""
        return {
            'system_info': {
                'name': 'Consciousness Level System',
                'version': '1.0.0',
                'last_calculation': self._consciousness_stats['last_calculation']
            },
            'consciousness_stats': self._consciousness_stats,
            'consciousness_distribution': self._get_consciousness_distribution(),
            'evolution_statistics': self._get_evolution_statistics(),
            'collective_statistics': {
                'total_groups': len(self._collective_states),
                'groups_by_level': self._count_collective_groups_by_level()
            }
        }
    
    def _get_consciousness_distribution(self) -> Dict[str, int]:
        """Get distribution of consciousness levels across tracked nodes"""
        distribution = defaultdict(int)
        for state in self._consciousness_states.values():
            distribution[state.level] += 1
        return dict(distribution)
    
    def _get_evolution_statistics(self) -> Dict[str, Any]:
        """Get statistics about consciousness evolution"""
        total_evolutions = sum(len(evolutions) for evolutions in self._evolution_history.values())
        
        # Count evolutions by type
        evolution_types = defaultdict(int)
        for evolutions in self._evolution_history.values():
            for evolution in evolutions:
                evolution_key = f"{evolution.from_level}_to_{evolution.to_level}"
                evolution_types[evolution_key] += 1
        
        return {
            'total_evolutions': total_evolutions,
            'evolutions_by_type': dict(evolution_types),
            'nodes_with_evolution': len(self._evolution_history)
        }
    
    def _count_collective_groups_by_level(self) -> Dict[str, int]:
        """Count collective groups by average consciousness level"""
        counts = defaultdict(int)
        for state in self._collective_states.values():
            counts[state.average_level] += 1
        return dict(counts)
    
    def _update_consciousness_stats(self):
        """Update consciousness system statistics"""
        self._consciousness_stats['total_nodes_tracked'] = len(self._consciousness_states)
        self._consciousness_stats['last_calculation'] = datetime.now().isoformat()
    
    def export_consciousness_report(self, output_format: str = "json") -> Union[str, Dict[str, Any]]:
        """
        Export comprehensive consciousness report
        
        Args:
            output_format: "json" or "dict"
        
        Returns:
            Consciousness report in requested format
        """
        report = {
            'consciousness_system_info': {
                'name': 'Consciousness Level System',
                'version': '1.0.0',
                'exported_at': datetime.now().isoformat()
            },
            'statistics': self.get_consciousness_statistics(),
            'consciousness_states': [
                {
                    'node_id': node_id,
                    'level': state.level,
                    'awareness_score': state.awareness_score,
                    'meta_cognitive_capability': state.meta_cognitive_capability,
                    'transcendent_potential': state.transcendent_potential,
                    'evolution_trajectory': state.evolution_trajectory
                }
                for node_id, state in self._consciousness_states.items()
            ],
            'evolution_history': [
                {
                    'node_id': node_id,
                    'evolutions': [
                        {
                            'from_level': ev.from_level,
                            'to_level': ev.to_level,
                            'trigger': ev.evolution_trigger,
                            'timestamp': ev.evolution_timestamp
                        }
                        for ev in evolutions
                    ]
                }
                for node_id, evolutions in self._evolution_history.items()
            ],
            'collective_states': [
                {
                    'group_id': state.group_id,
                    'average_level': state.average_level,
                    'collective_awareness': state.collective_awareness,
                    'emergent_consciousness': state.emergent_consciousness,
                    'evolution_potential': state.evolution_potential
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

# Global consciousness level system instance
consciousness_level_system = ConsciousnessLevelSystem()

if __name__ == "__main__":
    # Test the consciousness level system
    print("🧠 Consciousness Level System Test")
    
    # Test basic functionality
    print(f"System initialized with {len(consciousness_level_system._consciousness_states)} tracked nodes")
    print(f"Evolution triggers: {len(consciousness_level_system._evolution_triggers)}")
    print(f"Consciousness thresholds: {len(consciousness_level_system._consciousness_thresholds)}")
    
    # Test statistics
    stats = consciousness_level_system.get_consciousness_statistics()
    print(f"Statistics: {stats['consciousness_stats']['total_nodes_tracked']} nodes tracked")
    
    print("\n✅ Consciousness Level System ready for use!")
