#!/usr/bin/env python3
"""
Vibrational Axes System
=======================

This system implements the core Living Codex principle of vibrational axes
for resonance calculation, fractal recursion, and self-similarity across scales.

Key Features:
- Vibrational axes integration with all nodes
- Resonance state tracking (individual/community)
- Fractal recursion through hasPart/isPartOf relationships
- Cross-scale mapping (Micro↔Meso↔Macro↔Meta)
- Resonance-first governance through coherence

This is Phase 5 of the metadata enhancement plan.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Set, Tuple
from datetime import datetime
import json
import math
from collections import defaultdict

from living_codex_ontology import (
    VibrationalAxis, ResonanceState, EpistemicLabel,
    canonical_registry, validate_canonical_key
)

# ============================================================================
# RESONANCE CALCULATION SYSTEM
# ============================================================================

@dataclass
class ResonanceCalculation:
    """Result of resonance calculation between nodes"""
    axis_name: str
    node_a_resonance: float
    node_b_resonance: float
    alignment_score: float
    harmonic_relationship: str
    water_metaphor: str
    coherence_contribution: float
    epistemic_label: EpistemicLabel = EpistemicLabel.PHYSICS

@dataclass
class FractalRecursionInfo:
    """Information about fractal recursion depth and relationships"""
    current_depth: int
    max_depth: int
    has_part_count: int
    is_part_of_count: int
    self_similarity_score: float
    cross_scale_mappings: Dict[str, str]
    fractal_patterns: List[str]
    epistemic_label: EpistemicLabel = EpistemicLabel.ENGINEERING

@dataclass
class CrossScaleMapping:
    """Mapping between different scales of reality"""
    micro_scale: Dict[str, Any]  # Quantum/biological level
    meso_scale: Dict[str, Any]   # Human/cultural level
    macro_scale: Dict[str, Any]   # Planetary/cosmic level
    meta_scale: Dict[str, Any]    # Transcendent/holographic level
    mapping_coherence: float
    epistemic_label: EpistemicLabel = EpistemicLabel.SPECULATIVE

# ============================================================================
# VIBRATIONAL AXES INTEGRATION SYSTEM
# ============================================================================

class VibrationalAxesSystem:
    """
    Core system for integrating vibrational axes with all nodes
    and enabling resonance-first governance
    """
    
    def __init__(self):
        self.vibrational_axes = canonical_registry.get_vibrational_axes()
        self.resonance_states = defaultdict(dict)  # node_id -> axis_name -> ResonanceState
        self.community_resonance = defaultdict(dict)  # axis_name -> scope -> ResonanceState
        self.fractal_recursion_cache = {}
        self.cross_scale_cache = {}
        
        print("🌟 Vibrational Axes System initialized")
        print(f"✨ {len(self.vibrational_axes)} vibrational axes active")
        print("✨ Resonance state tracking enabled")
        print("✨ Fractal recursion system active")
        print("✨ Cross-scale mapping enabled")
    
    def calculate_node_resonance(self, node_id: str, axis_name: str, 
                               context: Dict[str, Any]) -> float:
        """
        Calculate a node's resonance value on a specific vibrational axis
        
        Args:
            node_id: Node identifier
            axis_name: Name of the vibrational axis
            context: Context information for calculation
        
        Returns:
            Resonance value between -1.0 and 1.0
        """
        try:
            # Find the vibrational axis
            axis = self._find_vibrational_axis(axis_name)
            if not axis:
                return 0.0
            
            # Calculate resonance based on node properties and context
            resonance_value = self._calculate_axis_resonance(axis, context)
            
            # Update resonance state
            self._update_node_resonance_state(node_id, axis_name, resonance_value)
            
            return resonance_value
            
        except Exception as e:
            print(f"Error calculating resonance for {node_id} on {axis_name}: {e}")
            return 0.0
    
    def calculate_resonance_alignment(self, node_a_id: str, node_b_id: str, 
                                    axis_name: str) -> ResonanceCalculation:
        """
        Calculate resonance alignment between two nodes on a specific axis
        
        Args:
            node_a_id: First node identifier
            node_b_id: Second node identifier
            axis_name: Name of the vibrational axis
        
        Returns:
            ResonanceCalculation with alignment details
        """
        try:
            # Get resonance values for both nodes
            node_a_resonance = self._get_node_resonance(node_a_id, axis_name)
            node_b_resonance = self._get_node_resonance(node_b_id, axis_name)
            
            # Calculate alignment score
            alignment_score = self._calculate_alignment_score(
                node_a_resonance, node_b_resonance
            )
            
            # Determine harmonic relationship
            harmonic_relationship = self._determine_harmonic_relationship(alignment_score)
            
            # Get water metaphor
            water_metaphor = self._get_water_metaphor_for_alignment(alignment_score)
            
            # Calculate coherence contribution
            coherence_contribution = self._calculate_coherence_contribution(
                alignment_score, node_a_resonance, node_b_resonance
            )
            
            # Create resonance calculation result
            result = ResonanceCalculation(
                axis_name=axis_name,
                node_a_resonance=node_a_resonance,
                node_b_resonance=node_b_resonance,
                alignment_score=alignment_score,
                harmonic_relationship=harmonic_relationship,
                water_metaphor=water_metaphor,
                coherence_contribution=coherence_contribution
            )
            
            # Update community resonance
            self._update_community_resonance(axis_name, result)
            
            return result
            
        except Exception as e:
            print(f"Error calculating resonance alignment: {e}")
            return None
    
    def get_fractal_recursion_info(self, node_id: str, max_depth: int = 5) -> FractalRecursionInfo:
        """
        Get fractal recursion information for a node
        
        Args:
            node_id: Node identifier
            max_depth: Maximum recursion depth to explore
        
        Returns:
            FractalRecursionInfo with recursion details
        """
        try:
            # Check cache first
            cache_key = f"{node_id}_{max_depth}"
            if cache_key in self.fractal_recursion_cache:
                return self.fractal_recursion_cache[cache_key]
            
            # Calculate fractal recursion info
            info = self._calculate_fractal_recursion(node_id, max_depth)
            
            # Cache the result
            self.fractal_recursion_cache[cache_key] = info
            
            return info
            
        except Exception as e:
            print(f"Error getting fractal recursion info for {node_id}: {e}")
            return None
    
    def get_cross_scale_mapping(self, node_id: str) -> CrossScaleMapping:
        """
        Get cross-scale mapping for a node (Micro↔Meso↔Macro↔Meta)
        
        Args:
            node_id: Node identifier
        
        Returns:
            CrossScaleMapping with scale information
        """
        try:
            # Check cache first
            if node_id in self.cross_scale_cache:
                return self.cross_scale_cache[node_id]
            
            # Calculate cross-scale mapping
            mapping = self._calculate_cross_scale_mapping(node_id)
            
            # Cache the result
            self.cross_scale_cache[node_id] = mapping
            
            return mapping
            
        except Exception as e:
            print(f"Error getting cross-scale mapping for {node_id}: {e}")
            return None
    
    def get_resonance_coherence_score(self, axis_name: str, scope: str = "community") -> float:
        """
        Get overall coherence score for a vibrational axis
        
        Args:
            axis_name: Name of the vibrational axis
            scope: "individual" or "community"
        
        Returns:
            Coherence score between 0.0 and 1.0
        """
        try:
            if scope == "community":
                resonance_states = list(self.community_resonance.get(axis_name, {}).values())
            else:
                resonance_states = [
                    state for states in self.resonance_states.values()
                    for state in states.values()
                    if state.axis == axis_name
                ]
            
            if not resonance_states:
                return 0.0
            
            # Calculate coherence as average alignment
            alignment_scores = []
            for i, state_a in enumerate(resonance_states):
                for state_b in resonance_states[i+1:]:
                    alignment = self._calculate_alignment_score(
                        state_a.value, state_b.value
                    )
                    alignment_scores.append(alignment)
            
            if not alignment_scores:
                return 0.0
            
            # Return average alignment as coherence score
            return sum(alignment_scores) / len(alignment_scores)
            
        except Exception as e:
            print(f"Error calculating coherence score: {e}")
            return 0.0
    
    # ============================================================================
    # PRIVATE IMPLEMENTATION METHODS
    # ============================================================================
    
    def _find_vibrational_axis(self, axis_name: str) -> Optional[VibrationalAxis]:
        """Find a vibrational axis by name"""
        for axis in self.vibrational_axes:
            if axis.name == axis_name:
                return axis
        return None
    
    def _calculate_axis_resonance(self, axis: VibrationalAxis, 
                                context: Dict[str, Any]) -> float:
        """Calculate resonance value for a specific axis and context"""
        # This is a simplified calculation - in practice, this would be
        # much more sophisticated based on node properties, relationships, etc.
        
        # For now, return a value based on context properties
        if "water_state" in context:
            water_state = context["water_state"]
            if "ice" in water_state.lower():
                return -0.8  # Closer to end_a (e.g., Fear)
            elif "liquid" in water_state.lower():
                return 0.0   # Neutral
            elif "vapor" in water_state.lower():
                return 0.8   # Closer to end_b (e.g., Trust)
        
        # Default to neutral
        return 0.0
    
    def _update_node_resonance_state(self, node_id: str, axis_name: str, value: float):
        """Update a node's resonance state for a specific axis"""
        if node_id not in self.resonance_states:
            self.resonance_states[node_id] = {}
        
        # Create or update resonance state
        self.resonance_states[node_id][axis_name] = ResonanceState(
            axis=axis_name,
            value=value,
            scope="individual",
            sample_count=1,
            updated_at=datetime.now().isoformat()
        )
    
    def _get_node_resonance(self, node_id: str, axis_name: str) -> float:
        """Get a node's resonance value for a specific axis"""
        if node_id in self.resonance_states:
            if axis_name in self.resonance_states[node_id]:
                return self.resonance_states[node_id][axis_name].value
        
        # Return neutral if no resonance state found
        return 0.0
    
    def _calculate_alignment_score(self, value_a: float, value_b: float) -> float:
        """Calculate alignment score between two resonance values"""
        # Alignment is based on how close the values are
        # Perfect alignment = 1.0, complete misalignment = -1.0
        difference = abs(value_a - value_b)
        alignment = 1.0 - (difference / 2.0)  # Normalize to -1.0 to 1.0
        
        # Apply harmonic enhancement for similar values
        if difference < 0.2:  # Very close values
            alignment = min(1.0, alignment + 0.2)
        elif difference < 0.5:  # Moderately close values
            alignment = min(1.0, alignment + 0.1)
        
        return max(-1.0, min(1.0, alignment))
    
    def _determine_harmonic_relationship(self, alignment_score: float) -> str:
        """Determine harmonic relationship based on alignment score"""
        if alignment_score >= 0.8:
            return "harmonic"
        elif alignment_score >= 0.4:
            return "sympathetic"
        elif alignment_score >= -0.2:
            return "neutral"
        elif alignment_score >= -0.6:
            return "dissonant"
        else:
            return "destructive"
    
    def _get_water_metaphor_for_alignment(self, alignment_score: float) -> str:
        """Get water metaphor for alignment score"""
        if alignment_score >= 0.8:
            return "Structured/Hexagonal - Perfect coherence"
        elif alignment_score >= 0.4:
            return "Liquid - Flowing harmony"
        elif alignment_score >= -0.2:
            return "Amorphous - Balanced potential"
        elif alignment_score >= -0.6:
            return "Supercritical - Transformation needed"
        else:
            return "Plasma - Primordial chaos"
    
    def _calculate_coherence_contribution(self, alignment_score: float, 
                                        value_a: float, value_b: float) -> float:
        """Calculate how much this alignment contributes to overall coherence"""
        # Higher alignment scores contribute more to coherence
        # But also consider the magnitude of the resonance values
        magnitude_factor = (abs(value_a) + abs(value_b)) / 2.0
        alignment_factor = max(0, alignment_score)  # Only positive alignments contribute
        
        return alignment_factor * magnitude_factor
    
    def _update_community_resonance(self, axis_name: str, 
                                  calculation: ResonanceCalculation):
        """Update community resonance state for an axis"""
        if axis_name not in self.community_resonance:
            self.community_resonance[axis_name] = {}
        
        # Update community resonance for "community" scope
        if "community" not in self.community_resonance[axis_name]:
            self.community_resonance[axis_name]["community"] = ResonanceState(
                axis=axis_name,
                value=0.0,
                scope="community",
                sample_count=0,
                updated_at=datetime.now().isoformat()
            )
        
        # Update community resonance
        community_state = self.community_resonance[axis_name]["community"]
        community_state.sample_count += 1
        
        # Update value based on new calculation
        current_value = community_state.value
        new_contribution = calculation.coherence_contribution
        community_state.value = (current_value + new_contribution) / 2.0
        community_state.updated_at = datetime.now().isoformat()
    
    def _calculate_fractal_recursion(self, node_id: str, max_depth: int) -> FractalRecursionInfo:
        """Calculate fractal recursion information for a node"""
        # This is a simplified implementation
        # In practice, this would traverse the actual node graph
        
        current_depth = 0
        has_part_count = 0
        is_part_of_count = 0
        
        # Calculate self-similarity score (simplified)
        self_similarity_score = 0.7  # Placeholder
        
        # Create cross-scale mappings (simplified)
        cross_scale_mappings = {
            "micro": f"micro_{node_id}",
            "meso": f"meso_{node_id}",
            "macro": f"macro_{node_id}",
            "meta": f"meta_{node_id}"
        }
        
        # Identify fractal patterns
        fractal_patterns = ["self_similar", "recursive", "holographic"]
        
        return FractalRecursionInfo(
            current_depth=current_depth,
            max_depth=max_depth,
            has_part_count=has_part_count,
            is_part_of_count=is_part_of_count,
            self_similarity_score=self_similarity_score,
            cross_scale_mappings=cross_scale_mappings,
            fractal_patterns=fractal_patterns
        )
    
    def _calculate_cross_scale_mapping(self, node_id: str) -> CrossScaleMapping:
        """Calculate cross-scale mapping for a node"""
        # This is a simplified implementation
        # In practice, this would analyze the node's properties and relationships
        
        micro_scale = {
            "quantum_state": "superposition",
            "consciousness_level": "awake",
            "water_state": "ws.quantum_coherent"
        }
        
        meso_scale = {
            "consciousness_level": "self_aware",
            "human_consciousness": "self_aware",
            "cultural_context": "modern",
            "water_state": "ws.liquid"
        }
        
        macro_scale = {
            "consciousness_level": "transcendent",
            "cosmic_context": "galactic",
            "temporal_scale": "evolutionary",
            "water_state": "ws.vapor"
        }
        
        meta_scale = {
            "consciousness_level": "unity",
            "transcendent_level": "unity",
            "holographic_nature": "complete",
            "water_state": "ws.bose_einstein"
        }
        
        mapping_coherence = 0.8  # Placeholder
        
        return CrossScaleMapping(
            micro_scale=micro_scale,
            meso_scale=meso_scale,
            macro_scale=macro_scale,
            meta_scale=meta_scale,
            mapping_coherence=mapping_coherence
        )

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global vibrational axes system instance
vibrational_axes_system = VibrationalAxesSystem()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_vibrational_axes_system() -> VibrationalAxesSystem:
    """Get the global vibrational axes system instance"""
    return vibrational_axes_system

def calculate_node_resonance(node_id: str, axis_name: str, 
                           context: Dict[str, Any]) -> float:
    """Calculate node resonance on a vibrational axis"""
    return vibrational_axes_system.calculate_node_resonance(node_id, axis_name, context)

def calculate_resonance_alignment(node_a_id: str, node_b_id: str, 
                                axis_name: str) -> ResonanceCalculation:
    """Calculate resonance alignment between two nodes"""
    return vibrational_axes_system.calculate_resonance_alignment(
        node_a_id, node_b_id, axis_name
    )

if __name__ == "__main__":
    # Test the vibrational axes system
    print("🌟 Testing Vibrational Axes System")
    
    # Test resonance calculation
    context = {"water_state": "ws.ice"}
    resonance = calculate_node_resonance("test_node", "Fear↔Trust", context)
    print(f"✨ Test node resonance on Fear↔Trust: {resonance}")
    
    # Test resonance alignment
    alignment = calculate_resonance_alignment("node_a", "node_b", "Fear↔Trust")
    if alignment:
        print(f"✨ Resonance alignment: {alignment.alignment_score}")
        print(f"✨ Harmonic relationship: {alignment.harmonic_relationship}")
        print(f"✨ Water metaphor: {alignment.water_metaphor}")
    
    print("✅ Vibrational Axes System test completed!")
