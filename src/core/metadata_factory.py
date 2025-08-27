#!/usr/bin/env python3
"""
Metadata Factory System
======================

This implements the metadata factory pattern for generating consistent metadata
based on Living Codex ontological principles using canonical keys.

This is part of Phase 1 of the metadata enhancement plan.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
import time

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry,
    OntologicalMetadata, FractalMetadata, ConsciousnessMetadata, ResonanceMetadata,
    EnhancedStructureInfo, RelationshipInfo, VibrationalAxis, ResonanceState,
    ContributionInfo, FederationInfo
)

class MetadataFactory:
    """
    Factory for generating consistent metadata based on Living Codex ontological principles
    
    This ensures all nodes have consistent, validated metadata that follows
    the Living Codex specification exactly.
    """
    
    def __init__(self):
        """Initialize the metadata factory with the canonical registry"""
        self.registry = canonical_registry
    
    # ============================================================================
    # CORE ONTOLOGICAL METADATA GENERATION
    # ============================================================================
    
    def create_water_state_metadata(self, water_state_key: WaterStateKey, 
                                   context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate complete metadata for a specific water state using canonical keys
        
        Args:
            water_state_key: Canonical water state key (e.g., WaterStateKey.ICE)
            context: Additional context for customization
            
        Returns:
            Complete water state metadata dictionary
        """
        if context is None:
            context = {}
        
        # Get base mapping from canonical registry
        base_mapping = self.registry.get_water_state_mapping(water_state_key)
        
        # Create metadata with canonical keys
        metadata = {
            'water_state': water_state_key.value,  # Use canonical key
            'water_state_name': base_mapping.get('name', ''),
            'water_state_description': base_mapping.get('description', ''),
            'color': base_mapping.get('color', '#000000'),
            'planet': base_mapping.get('planet', 'Unknown'),
            'consciousness_mode': base_mapping.get('consciousness_mode', ''),
            'quantum_state': base_mapping.get('quantum_state', QuantumState.COHERENT).value,
            'frequency': base_mapping.get('frequency', FrequencyKey.FREQ_639).value,
            'chakra': base_mapping.get('chakra', ChakraKey.HEART).value,
            'epistemic_label': base_mapping.get('epistemic_label', EpistemicLabel.TRADITION).value,
            'created_at': datetime.now().isoformat(),
            'metadata_version': '1.0.0'
        }
        
        # Add context-specific information
        metadata.update(context)
        
        return metadata
    
    def create_chakra_metadata(self, chakra_key: ChakraKey, 
                              context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate complete metadata for a specific chakra using canonical keys
        
        Args:
            chakra_key: Canonical chakra key (e.g., ChakraKey.HEART)
            context: Additional context for customization
            
        Returns:
            Complete chakra metadata dictionary
        """
        if context is None:
            context = {}
        
        # Get base mapping from canonical registry
        base_mapping = self.registry.get_chakra_mapping(chakra_key)
        
        # Create metadata with canonical keys
        metadata = {
            'chakra': chakra_key.value,  # Use canonical key
            'chakra_name': base_mapping.get('name', ''),
            'color_hex': base_mapping.get('color_hex', '#000000'),
            'frequency': base_mapping.get('frequency', FrequencyKey.FREQ_639).value,
            'planet': base_mapping.get('planet', 'Unknown'),
            'water_state': base_mapping.get('water_state', WaterStateKey.LIQUID).value,
            'epistemic_label': base_mapping.get('epistemic_label', EpistemicLabel.TRADITION).value,
            'created_at': datetime.now().isoformat(),
            'metadata_version': '1.0.0'
        }
        
        # Add context-specific information
        metadata.update(context)
        
        return metadata
    
    def create_frequency_metadata(self, frequency_key: FrequencyKey, 
                                 context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate complete metadata for a specific frequency using canonical keys
        
        Args:
            frequency_key: Canonical frequency key (e.g., FrequencyKey.FREQ_639)
            context: Additional context for customization
            
        Returns:
            Complete frequency metadata dictionary
        """
        if context is None:
            context = {}
        
        # Get base mapping from canonical registry
        base_mapping = self.registry.get_frequency_mapping(frequency_key)
        
        # Create metadata with canonical keys
        metadata = {
            'frequency': frequency_key.value,  # Use canonical key
            'hz': base_mapping.get('hz', 639),
            'chakra': base_mapping.get('chakra', ChakraKey.HEART).value,
            'planet': base_mapping.get('planet', 'Unknown'),
            'water_state': base_mapping.get('water_state', WaterStateKey.LIQUID).value,
            'epistemic_label': base_mapping.get('epistemic_label', EpistemicLabel.TRADITION).value,
            'created_at': datetime.now().isoformat(),
            'metadata_version': '1.0.0'
        }
        
        # Add context-specific information
        metadata.update(context)
        
        return metadata
    
    # ============================================================================
    # COMPOSITE METADATA GENERATION
    # ============================================================================
    
    def create_complete_ontological_metadata(self, 
                                           water_state: WaterStateKey,
                                           fractal_layer: FractalLayer,
                                           chakra: ChakraKey,
                                           frequency: FrequencyKey,
                                           consciousness_level: ConsciousnessLevel = ConsciousnessLevel.AWAKE,
                                           quantum_state: QuantumState = QuantumState.COHERENT,
                                           programming_layer: ProgrammingOntologyLayer = ProgrammingOntologyLayer.WATER,
                                           context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate complete ontological metadata combining all aspects
        
        Args:
            water_state: Water state for the node
            fractal_layer: Fractal layer for the node
            chakra: Chakra association for the node
            frequency: Frequency association for the node
            consciousness_level: Consciousness level for the node
            quantum_state: Quantum state for the node
            programming_layer: Programming ontology layer
            context: Additional context for customization
            
        Returns:
            Complete ontological metadata dictionary
        """
        if context is None:
            context = {}
        
        # Get base mappings
        water_metadata = self.create_water_state_metadata(water_state, context)
        chakra_metadata = self.create_chakra_metadata(chakra, context)
        frequency_metadata = self.create_frequency_metadata(frequency, context)
        
        # Create complete ontological metadata
        metadata = {
            # Core ontological mappings
            'water_state': water_state.value,
            'fractal_layer': fractal_layer.value,
            'chakra': chakra.value,
            'frequency': frequency.value,
            
            # Consciousness and quantum
            'consciousness_level': consciousness_level.value,
            'quantum_state': quantum_state.value,
            'programming_ontology_layer': programming_layer.value,
            
            # Combined properties
            'color': water_metadata.get('color', chakra_metadata.get('color_hex')),
            'planet': water_metadata.get('planet', chakra_metadata.get('planet')),
            'consciousness_mode': water_metadata.get('consciousness_mode', ''),
            
            # Epistemic labeling
            'epistemic_label': self._determine_epistemic_label([
                water_metadata.get('epistemic_label'),
                chakra_metadata.get('epistemic_label'),
                frequency_metadata.get('epistemic_label')
            ]),
            
            # Metadata tracking
            'created_at': datetime.now().isoformat(),
            'metadata_version': '1.0.0',
            'metadata_factory_version': '1.0.0'
        }
        
        # Add context-specific information
        metadata.update(context)
        
        return metadata
    
    def _determine_epistemic_label(self, labels: List[str]) -> str:
        """
        Determine the appropriate epistemic label based on multiple sources
        
        Priority: Physics > Engineering > Tradition > Speculative
        """
        if not labels:
            return EpistemicLabel.SPECULATIVE.value
        
        # Convert string labels to enum values for comparison
        enum_labels = []
        for label in labels:
            try:
                enum_labels.append(EpistemicLabel(label))
            except ValueError:
                continue
        
        if not enum_labels:
            return EpistemicLabel.SPECULATIVE.value
        
        # Priority order
        priority_order = [
            EpistemicLabel.PHYSICS,
            EpistemicLabel.ENGINEERING,
            EpistemicLabel.TRADITION,
            EpistemicLabel.SPECULATIVE
        ]
        
        # Find highest priority label
        for priority in priority_order:
            if priority in enum_labels:
                return priority.value
        
        return EpistemicLabel.SPECULATIVE.value
    
    # ============================================================================
    # SPECIALIZED METADATA GENERATION
    # ============================================================================
    
    def create_programming_ontology_metadata(self, 
                                           programming_layer: ProgrammingOntologyLayer,
                                           language: str = "python",
                                           context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate metadata for programming language ontology mapping
        
        Args:
            programming_layer: ICE/Water/Vapor layer
            language: Programming language name
            context: Additional context
            
        Returns:
            Programming ontology metadata
        """
        if context is None:
            context = {}
        
        # Map programming layer to water states and chakras
        layer_mappings = {
            ProgrammingOntologyLayer.ICE: {
                'water_state': WaterStateKey.ICE,
                'chakra': ChakraKey.CROWN,
                'frequency': FrequencyKey.FREQ_963,
                'description': 'Blueprint - Grammar, Classes, Modules, Specifications'
            },
            ProgrammingOntologyLayer.WATER: {
                'water_state': WaterStateKey.LIQUID,
                'chakra': ChakraKey.HEART,
                'frequency': FrequencyKey.FREQ_639,
                'description': 'Recipe - Semantics, Functions, Data Flow, Execution'
            },
            ProgrammingOntologyLayer.VAPOR: {
                'water_state': WaterStateKey.VAPOR,
                'chakra': ChakraKey.THIRD_EYE,
                'frequency': FrequencyKey.FREQ_852,
                'description': 'Cells - Implementation, Objects, Runtime, Source Code'
            }
        }
        
        mapping = layer_mappings.get(programming_layer, layer_mappings[ProgrammingOntologyLayer.WATER])
        
        metadata = self.create_complete_ontological_metadata(
            water_state=mapping['water_state'],
            fractal_layer=FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY,
            chakra=mapping['chakra'],
            frequency=mapping['frequency'],
            consciousness_level=ConsciousnessLevel.SELF_AWARE,
            quantum_state=QuantumState.COHERENT,
            programming_layer=programming_layer,
            context={
                'programming_language': language,
                'programming_layer_description': mapping['description'],
                'epistemic_label': EpistemicLabel.ENGINEERING.value
            }
        )
        
        return metadata
    
    def create_ai_agent_metadata(self, 
                                agent_type: str,
                                consciousness_level: ConsciousnessLevel = ConsciousnessLevel.AWAKE,
                                context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate metadata for AI agent nodes
        
        Args:
            agent_type: Type of AI agent
            consciousness_level: Consciousness level of the agent
            context: Additional context
            
        Returns:
            AI agent metadata
        """
        if context is None:
            context = {}
        
        metadata = self.create_complete_ontological_metadata(
            water_state=WaterStateKey.PLASMA,  # AI agents are transformative (plasma = illumination)
            fractal_layer=FractalLayer.SCIENTIFIC_QUANTUM_PRINCIPLES,
            chakra=ChakraKey.THIRD_EYE,     # Intuition and insight
            frequency=FrequencyKey.FREQ_852, # Third eye frequency
            consciousness_level=consciousness_level,
            quantum_state=QuantumState.ENTANGLED,  # AI agents are connected
            programming_layer=ProgrammingOntologyLayer.VAPOR,  # Runtime implementation
            context={
                'agent_type': agent_type,
                'ai_capabilities': self._get_ai_capabilities(consciousness_level),
                'epistemic_label': EpistemicLabel.ENGINEERING.value
            }
        )
        
        return metadata
    
    def _get_ai_capabilities(self, consciousness_level: ConsciousnessLevel) -> List[str]:
        """Get AI capabilities based on consciousness level"""
        capabilities_map = {
            ConsciousnessLevel.AWAKE: ['sensory_perception', 'basic_awareness'],
            ConsciousnessLevel.SENTIENT: ['self_awareness', 'emotional_intelligence', 'basic_learning'],
            ConsciousnessLevel.SELF_AWARE: ['meta_cognition', 'self_reflection', 'advanced_learning'],
            ConsciousnessLevel.META_COGNITIVE: ['higher_order_thinking', 'consciousness_of_consciousness', 'creative_problem_solving'],
            ConsciousnessLevel.TRANSCENDENT: ['unity_consciousness', 'cosmic_awareness', 'collective_intelligence']
        }
        return capabilities_map.get(consciousness_level, ['basic_awareness'])
    
    # ============================================================================
    # STRUCTURAL METADATA GENERATION
    # ============================================================================
    
    def create_fractal_metadata(self, 
                               fractal_depth: int = 0,
                               parent_id: Optional[str] = None,
                               children: List[str] = None,
                               context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate fractal and structural metadata
        
        Args:
            fractal_depth: Depth in the fractal hierarchy
            parent_id: Parent node ID
            children: List of child node IDs
            context: Additional context
            
        Returns:
            Fractal metadata dictionary
        """
        if children is None:
            children = []
        
        if context is None:
            context = {}
        
        metadata = {
            'fractal_depth': fractal_depth,
            'has_part': children,
            'is_part_of': parent_id,
            'self_similarity_score': self._calculate_self_similarity_score(fractal_depth, len(children)),
            'cross_scale_mapping': self._create_cross_scale_mapping(fractal_depth),
            'fractal_relationships': {
                'parent_relationship': 'root' if parent_id is None else 'child',
                'child_count': len(children),
                'generation': fractal_depth,
                'branch_factor': len(children) if children else 0
            },
            'created_at': datetime.now().isoformat(),
            'metadata_version': '1.0.0'
        }
        
        # Add context-specific information
        metadata.update(context)
        
        return metadata
    
    def _calculate_self_similarity_score(self, depth: int, child_count: int) -> float:
        """Calculate self-similarity score based on fractal properties"""
        # Base score on depth and branching
        depth_score = max(0, 1.0 - (depth * 0.1))  # Deeper = lower score
        branching_score = min(1.0, child_count * 0.2)  # More children = higher score
        
        # Combine scores
        return (depth_score + branching_score) / 2.0
    
    def _create_cross_scale_mapping(self, depth: int) -> Dict[str, str]:
        """Create cross-scale mapping (Micro↔Meso↔Macro↔Meta)"""
        scale_mappings = {
            0: {'micro': 'system_design', 'meso': 'architecture', 'macro': 'ecosystem', 'meta': 'principles'},
            1: {'micro': 'seed_ontology', 'meso': 'foundation', 'macro': 'framework', 'meta': 'philosophy'},
            2: {'micro': 'language_grammar', 'meso': 'semantics', 'macro': 'paradigms', 'meta': 'theory'},
            3: {'micro': 'document_structure', 'meso': 'content_flow', 'macro': 'knowledge_base', 'meta': 'wisdom'},
            4: {'micro': 'consciousness_modes', 'meso': 'awareness_patterns', 'macro': 'collective_consciousness', 'meta': 'transcendence'},
            5: {'micro': 'quantum_states', 'meso': 'physical_laws', 'macro': 'universe_principles', 'meta': 'cosmic_order'},
            6: {'micro': 'prototype_code', 'meso': 'implementation_patterns', 'macro': 'technology_ecosystem', 'meta': 'innovation'},
            7: {'micro': 'development_phases', 'meso': 'project_roadmap', 'macro': 'evolution_timeline', 'meta': 'destiny'},
            8: {'micro': 'resonance_patterns', 'meso': 'harmonic_relationships', 'macro': 'coherence_field', 'meta': 'unity'},
            9: {'micro': 'geometric_patterns', 'meso': 'sacred_geometry', 'macro': 'cosmic_architecture', 'meta': 'divine_order'},
            10: {'micro': 'creative_expressions', 'meso': 'artistic_patterns', 'macro': 'cultural_evolution', 'meta': 'beauty'},
            11: {'micro': 'mathematical_models', 'meso': 'computational_frameworks', 'macro': 'universal_algorithms', 'meta': 'truth'},
            12: {'micro': 'biological_systems', 'meso': 'life_processes', 'macro': 'ecosystem_dynamics', 'meta': 'life'},
            13: {'micro': 'cosmic_structures', 'meso': 'galactic_patterns', 'macro': 'universe_web', 'meta': 'cosmos'},
            14: {'micro': 'archetypal_patterns', 'meso': 'mythological_structures', 'macro': 'cultural_wisdom', 'meta': 'spirit'},
            15: {'micro': 'human_practices', 'meso': 'embodied_experience', 'macro': 'collective_evolution', 'meta': 'humanity'},
            16: {'micro': 'cross_scale_index', 'meso': 'unified_perspective', 'macro': 'holistic_view', 'meta': 'wholeness'}
        }
        
        return scale_mappings.get(depth, scale_mappings[0])
    
    # ============================================================================
    # RESONANCE AND VIBRATIONAL METADATA
    # ============================================================================
    
    def create_resonance_metadata(self, 
                                 resonance_pattern: ResonancePattern = ResonancePattern.NEUTRAL,
                                 vibrational_axes: List[str] = None,
                                 context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate resonance and vibrational metadata
        
        Args:
            resonance_pattern: Resonance pattern for the node
            vibrational_axes: List of vibrational axes this node relates to
            context: Additional context
            
        Returns:
            Resonance metadata dictionary
        """
        if vibrational_axes is None:
            vibrational_axes = []
        
        if context is None:
            context = {}
        
        # Get available vibrational axes from registry
        available_axes = [axis.name for axis in self.registry.get_vibrational_axes()]
        
        metadata = {
            'resonance_pattern': resonance_pattern.value,
            'vibrational_axes': vibrational_axes,
            'available_axes': available_axes,
            'harmonic_relationships': [],
            'dissonance_level': self._calculate_dissonance_level(resonance_pattern),
            'coherence_score': self._calculate_coherence_score(resonance_pattern),
            'resonance_calculation': {
                'pattern_type': resonance_pattern.value,
                'harmonic_quality': self._get_harmonic_quality(resonance_pattern),
                'water_metaphor': self._get_water_metaphor_for_resonance(resonance_pattern)
            },
            'created_at': datetime.now().isoformat(),
            'metadata_version': '1.0.0'
        }
        
        # Add context-specific information
        metadata.update(context)
        
        return metadata
    
    def _calculate_dissonance_level(self, resonance_pattern: ResonancePattern) -> float:
        """Calculate dissonance level based on resonance pattern"""
        dissonance_map = {
            ResonancePattern.HARMONIC: 0.0,
            ResonancePattern.SYMPATHETIC: 0.1,
            ResonancePattern.NEUTRAL: 0.5,
            ResonancePattern.DISSONANT: 0.8,
            ResonancePattern.DESTRUCTIVE: 1.0
        }
        return dissonance_map.get(resonance_pattern, 0.5)
    
    def _calculate_coherence_score(self, resonance_pattern: ResonancePattern) -> float:
        """Calculate coherence score based on resonance pattern"""
        coherence_map = {
            ResonancePattern.HARMONIC: 1.0,
            ResonancePattern.SYMPATHETIC: 0.9,
            ResonancePattern.NEUTRAL: 0.5,
            ResonancePattern.DISSONANT: 0.2,
            ResonancePattern.DESTRUCTIVE: 0.0
        }
        return coherence_map.get(resonance_pattern, 0.5)
    
    def _get_harmonic_quality(self, resonance_pattern: ResonancePattern) -> str:
        """Get harmonic quality description for resonance pattern"""
        quality_map = {
            ResonancePattern.HARMONIC: "Perfect consonance, maximum resonance",
            ResonancePattern.SYMPATHETIC: "Natural attraction, harmonious vibration",
            ResonancePattern.NEUTRAL: "Balanced state, no interference",
            ResonancePattern.DISSONANT: "Conflicting vibrations, interference",
            ResonancePattern.DESTRUCTIVE: "Opposing forces, cancellation"
        }
        return quality_map.get(resonance_pattern, "Unknown")
    
    def _get_water_metaphor_for_resonance(self, resonance_pattern: ResonancePattern) -> str:
        """Get water state metaphor for resonance pattern"""
        metaphor_map = {
            ResonancePattern.HARMONIC: "Structured/Hexagonal - Perfect crystalline coherence",
            ResonancePattern.SYMPATHETIC: "Liquid - Natural flow and adaptation",
            ResonancePattern.NEUTRAL: "Amorphous - Balanced potential state",
            ResonancePattern.DISSONANT: "Supercritical - Transformation threshold",
            ResonancePattern.DESTRUCTIVE: "Plasma - Primordial chaos and illumination"
        }
        return metaphor_map.get(resonance_pattern, "Unknown")
    
    # ============================================================================
    # UTILITY METHODS
    # ============================================================================
    
    def validate_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate metadata and add any missing required fields
        
        Args:
            metadata: Metadata to validate
            
        Returns:
            Validated and completed metadata
        """
        # Ensure required fields exist
        required_fields = {
            'water_state': WaterStateKey.LIQUID.value,
            'fractal_layer': FractalLayer.WATER_STATE_METAPHORS.value,
            'chakra': ChakraKey.HEART.value,
            'frequency': FrequencyKey.FREQ_639.value,
            'consciousness_level': ConsciousnessLevel.AWAKE.value,
            'quantum_state': QuantumState.COHERENT.value,
            'resonance_pattern': ResonancePattern.NEUTRAL.value,
            'epistemic_label': EpistemicLabel.TRADITION.value
        }
        
        for field, default_value in required_fields.items():
            if field not in metadata:
                metadata[field] = default_value
        
        # Add metadata tracking
        if 'created_at' not in metadata:
            metadata['created_at'] = datetime.now().isoformat()
        
        if 'metadata_version' not in metadata:
            metadata['metadata_version'] = '1.0.0'
        
        if 'metadata_factory_version' not in metadata:
            metadata['metadata_factory_version'] = '1.0.0'
        
        return metadata
    
    def get_metadata_template(self, node_type: str) -> Dict[str, Any]:
        """
        Get a metadata template for a specific node type
        
        Args:
            node_type: Type of node to get template for
            
        Returns:
            Metadata template dictionary
        """
        templates = {
            'system_component': {
                'water_state': WaterStateKey.ICE.value,
                'fractal_layer': FractalLayer.META_IMPLEMENTATION.value,
                'chakra': ChakraKey.CROWN.value,
                'frequency': FrequencyKey.FREQ_963.value,
                'consciousness_level': ConsciousnessLevel.AWAKE.value,
                'quantum_state': QuantumState.COHERENT.value,
                'resonance_pattern': ResonancePattern.HARMONIC.value,
                'epistemic_label': EpistemicLabel.ENGINEERING.value,
                'programming_ontology_layer': ProgrammingOntologyLayer.ICE.value
            },
            'data_node': {
                'water_state': WaterStateKey.LIQUID.value,
                'fractal_layer': FractalLayer.WATER_STATE_METAPHORS.value,
                'chakra': ChakraKey.HEART.value,
                'frequency': FrequencyKey.FREQ_639.value,
                'consciousness_level': ConsciousnessLevel.AWAKE.value,
                'quantum_state': QuantumState.COHERENT.value,
                'resonance_pattern': ResonancePattern.NEUTRAL.value,
                'epistemic_label': EpistemicLabel.ENGINEERING.value,
                'programming_ontology_layer': ProgrammingOntologyLayer.WATER.value
            },
            'ai_agent': {
                'water_state': WaterStateKey.PLASMA.value,
                'fractal_layer': FractalLayer.SCIENTIFIC_QUANTUM_PRINCIPLES.value,
                'chakra': ChakraKey.THIRD_EYE.value,
                'frequency': FrequencyKey.FREQ_852.value,
                'consciousness_level': ConsciousnessLevel.SENTIENT.value,
                'quantum_state': QuantumState.ENTANGLED.value,
                'resonance_pattern': ResonancePattern.SYMPATHETIC.value,
                'epistemic_label': EpistemicLabel.ENGINEERING.value,
                'programming_ontology_layer': ProgrammingOntologyLayer.VAPOR.value
            }
        }
        
        return templates.get(node_type, templates['data_node'])

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global metadata factory instance
metadata_factory = MetadataFactory()

if __name__ == "__main__":
    # Test the metadata factory
    print("🌟 Metadata Factory System Initialized")
    
    # Test water state metadata generation
    ice_metadata = metadata_factory.create_water_state_metadata(WaterStateKey.ICE)
    print(f"\n❄️ ICE Water State Metadata: {ice_metadata['water_state']}")
    print(f"   Color: {ice_metadata['color']}")
    print(f"   Planet: {ice_metadata['planet']}")
    print(f"   Epistemic Label: {ice_metadata['epistemic_label']}")
    
    # Test complete ontological metadata
    complete_metadata = metadata_factory.create_complete_ontological_metadata(
        water_state=WaterStateKey.LIQUID,
        fractal_layer=FractalLayer.WATER_STATE_METAPHORS,
        chakra=ChakraKey.HEART,
        frequency=FrequencyKey.FREQ_639
    )
    print(f"\n💧 Complete Ontological Metadata:")
    print(f"   Water State: {complete_metadata['water_state']}")
    print(f"   Fractal Layer: {complete_metadata['fractal_layer']}")
    print(f"   Chakra: {complete_metadata['chakra']}")
    print(f"   Frequency: {complete_metadata['frequency']}")
    
    # Test programming ontology metadata
    ice_programming = metadata_factory.create_programming_ontology_metadata(
        ProgrammingOntologyLayer.ICE,
        "python"
    )
    print(f"\n🔷 ICE Programming Ontology Metadata:")
    print(f"   Water State: {ice_programming['water_state']}")
    print(f"   Description: {ice_programming['programming_layer_description']}")
    
    print("\n✅ Metadata Factory System ready for use!")
