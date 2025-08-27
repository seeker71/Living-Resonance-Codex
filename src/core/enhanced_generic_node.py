#!/usr/bin/env python3
"""
Enhanced GenericNode System
===========================

This implements the enhanced GenericNode class that integrates with the
Living Codex ontology system and includes all enhanced metadata structures.

This is part of Phase 1 of the metadata enhancement plan.
"""

from dataclasses import dataclass, asdict, field
from typing import Dict, List, Any, Optional, Set
from datetime import datetime
import hashlib
import json

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry,
    VibrationalAxis, ResonanceState, ContributionInfo, FederationInfo
)

from metadata_factory import metadata_factory

@dataclass
class EnhancedGenericNode:
    """
    Enhanced GenericNode with complete Living Codex ontological metadata
    
    This implements the core Living Codex principle: "Everything is just nodes"
    with complete ontological mapping, epistemic labeling, and fractal structure.
    """
    
    # ============================================================================
    # CORE NODE FIELDS
    # ============================================================================
    
    node_id: str                    # Unique identifier
    node_type: str                  # What it represents (determined by metadata)
    name: str                       # Human-readable name
    content: str                    # Actual content (can be anything)
    parent_id: Optional[str]        # Parent node (for hierarchical structure)
    children: List[str]             # Child node IDs (for hierarchical structure)
    
    # ============================================================================
    # ENHANCED ONTOLOGICAL METADATA
    # ============================================================================
    
    # Core ontological mappings with canonical keys
    water_state: str                # Canonical water state key (e.g., "ws.ice")
    fractal_layer: int              # Fractal layer (0-16)
    chakra: str                     # Canonical chakra key (e.g., "ch.heart")
    frequency: str                  # Canonical frequency key (e.g., "freq.639")
    
    # Consciousness and quantum systems
    consciousness_level: str        # Consciousness level
    quantum_state: str              # Quantum state metaphor
    programming_ontology_layer: str # Programming ontology layer
    
    # Epistemic labeling
    epistemic_label: str            # physics/engineering/tradition/speculative
    
    # ============================================================================
    # FRACTAL AND STRUCTURAL METADATA
    # ============================================================================
    
    fractal_depth: int              # Depth in fractal hierarchy
    has_part: List[str]             # Child node IDs
    is_part_of: Optional[str]       # Parent node ID
    self_similarity_score: float    # Self-similarity across scales
    cross_scale_mapping: Dict[str, str]  # Micro↔Meso↔Macro↔Meta mapping
    
    # ============================================================================
    # RESONANCE AND VIBRATIONAL METADATA
    # ============================================================================
    
    resonance_pattern: str          # Resonance pattern
    vibrational_axes: List[str]     # Related vibrational axes
    harmonic_relationships: List[str] # Related nodes by resonance
    dissonance_level: float         # Level of dissonance (0.0 to 1.0)
    coherence_score: float          # Overall coherence score
    
    # ============================================================================
    # STRUCTURE AND RELATIONSHIP TRACKING
    # ============================================================================
    
    structure_info: Dict[str, Any]  # Enhanced structural information
    relationship_info: Dict[str, Any]  # Relationship and connection information
    
    # ============================================================================
    # METADATA TRACKING
    # ============================================================================
    
    created_at: str                 # Creation timestamp
    updated_at: str                 # Last update timestamp
    metadata_version: str           # Metadata version
    metadata_factory_version: str   # Metadata factory version
    
    # ============================================================================
    # LIVING CODEX CORE PRINCIPLES
    # ============================================================================
    
    resonance_state: Optional[ResonanceState] = None  # Individual/community resonance
    contribution_info: Optional[ContributionInfo] = None  # Contribution and weaving
    federation_info: Optional[FederationInfo] = None  # Federation and community
    
    # ============================================================================
    # VALIDATION AND COMPUTED FIELDS
    # ============================================================================
    
    _validated: bool = field(default=False, init=False)
    _canonical_keys_validated: bool = field(default=False, init=False)
    
    def __post_init__(self):
        """Post-initialization validation and setup"""
        self._validate_canonical_keys()
        self._validate_metadata()
        self._compute_derived_fields()
        self._validated = True
    
    # ============================================================================
    # VALIDATION METHODS
    # ============================================================================
    
    def _validate_canonical_keys(self):
        """Validate that all canonical keys are valid"""
        registry = canonical_registry
        
        # Validate water state
        if not registry.get_water_state_mapping(WaterStateKey(self.water_state)):
            raise ValueError(f"Invalid water state key: {self.water_state}")
        
        # Validate chakra
        if not registry.get_chakra_mapping(ChakraKey(self.chakra)):
            raise ValueError(f"Invalid chakra key: {self.chakra}")
        
        # Validate frequency
        if not registry.get_frequency_mapping(FrequencyKey(self.frequency)):
            raise ValueError(f"Invalid frequency key: {self.frequency}")
        
        # Validate fractal layer
        if self.fractal_layer not in [layer.value for layer in FractalLayer]:
            raise ValueError(f"Invalid fractal layer: {self.fractal_layer}")
        
        # Validate consciousness level
        if self.consciousness_level not in [level.value for level in ConsciousnessLevel]:
            raise ValueError(f"Invalid consciousness level: {self.consciousness_level}")
        
        # Validate quantum state
        if self.quantum_state not in [state.value for state in QuantumState]:
            raise ValueError(f"Invalid quantum state: {self.quantum_state}")
        
        # Validate resonance pattern
        if self.resonance_pattern not in [pattern.value for pattern in ResonancePattern]:
            raise ValueError(f"Invalid resonance pattern: {self.resonance_pattern}")
        
        # Validate programming ontology layer
        if self.programming_ontology_layer not in [layer.value for layer in ProgrammingOntologyLayer]:
            raise ValueError(f"Invalid programming ontology layer: {self.programming_ontology_layer}")
        
        # Validate epistemic label
        if self.epistemic_label not in [label.value for label in EpistemicLabel]:
            raise ValueError(f"Invalid epistemic label: {self.epistemic_label}")
        
        self._canonical_keys_validated = True
    
    def _validate_metadata(self):
        """Validate metadata consistency and completeness"""
        # Ensure required fields exist
        required_fields = [
            'water_state', 'fractal_layer', 'chakra', 'frequency',
            'consciousness_level', 'quantum_state', 'programming_ontology_layer',
            'epistemic_label', 'fractal_depth', 'resonance_pattern',
            'dissonance_level', 'coherence_score'
        ]
        
        for field_name in required_fields:
            if not hasattr(self, field_name) or getattr(self, field_name) is None:
                raise ValueError(f"Missing required field: {field_name}")
        
        # Validate numeric ranges
        if not (0 <= self.fractal_layer <= 16):
            raise ValueError(f"Fractal layer must be 0-16, got: {self.fractal_layer}")
        
        if not (0.0 <= self.dissonance_level <= 1.0):
            raise ValueError(f"Dissonance level must be 0.0-1.0, got: {self.dissonance_level}")
        
        if not (0.0 <= self.coherence_score <= 1.0):
            raise ValueError(f"Coherence score must be 0.0-1.0, got: {self.coherence_score}")
        
        if not (0.0 <= self.self_similarity_score <= 1.0):
            raise ValueError(f"Self-similarity score must be 0.0-1.0, got: {self.self_similarity_score}")
    
    def _compute_derived_fields(self):
        """Compute derived fields based on ontological mappings"""
        # Get base mappings from canonical registry
        water_mapping = canonical_registry.get_water_state_mapping(WaterStateKey(self.water_state))
        chakra_mapping = canonical_registry.get_chakra_mapping(ChakraKey(self.chakra))
        frequency_mapping = canonical_registry.get_frequency_mapping(FrequencyKey(self.frequency))
        
        # Set color based on water state or chakra
        if not hasattr(self, 'color') or not self.color:
            self.color = water_mapping.get('color', chakra_mapping.get('color_hex', '#000000'))
        
        # Set planet based on water state or chakra
        if not hasattr(self, 'planet') or not self.planet:
            self.planet = water_mapping.get('planet', chakra_mapping.get('planet', 'Unknown'))
        
        # Set consciousness mode based on water state
        if not hasattr(self, 'consciousness_mode') or not self.consciousness_mode:
            self.consciousness_mode = water_mapping.get('consciousness_mode', '')
        
        # Update timestamps
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()
        
        # Set metadata versions
        if not self.metadata_version:
            self.metadata_version = '1.0.0'
        
        if not self.metadata_factory_version:
            self.metadata_factory_version = '1.0.0'
    
    # ============================================================================
    # CORE LIVING CODEX METHODS
    # ============================================================================
    
    def get_fractal_depth(self) -> int:
        """Calculate fractal depth based on parent relationships"""
        if not self.parent_id:
            return 0
        return self.fractal_depth
    
    def get_water_state(self) -> str:
        """Get water state from metadata"""
        return self.water_state
    
    def get_chakra(self) -> str:
        """Get chakra from metadata"""
        return self.chakra
    
    def get_frequency(self) -> str:
        """Get frequency from metadata"""
        return self.frequency
    
    def get_planet(self) -> str:
        """Get planet from metadata"""
        return self.planet
    
    def get_consciousness_level(self) -> str:
        """Get consciousness level from metadata"""
        return self.consciousness_level
    
    def get_quantum_state(self) -> str:
        """Get quantum state from metadata"""
        return self.quantum_state
    
    def get_epistemic_label(self) -> str:
        """Get epistemic label from metadata"""
        return self.epistemic_label
    
    def get_resonance_pattern(self) -> str:
        """Get resonance pattern from metadata"""
        return self.resonance_pattern
    
    def get_coherence_score(self) -> float:
        """Get coherence score from metadata"""
        return self.coherence_score
    
    def get_dissonance_level(self) -> float:
        """Get dissonance level from metadata"""
        return self.dissonance_level
    
    def get_self_similarity_score(self) -> float:
        """Get self-similarity score from metadata"""
        return self.self_similarity_score
    
    # ============================================================================
    # FRACTAL AND RELATIONSHIP METHODS
    # ============================================================================
    
    def add_child(self, child_id: str):
        """Add a child node to this node"""
        if child_id not in self.children:
            self.children.append(child_id)
        if child_id not in self.has_part:
            self.has_part.append(child_id)
        self._update_fractal_metadata()
    
    def remove_child(self, child_id: str):
        """Remove a child node from this node"""
        if child_id in self.children:
            self.children.remove(child_id)
            self.has_part.remove(child_id)
            self._update_fractal_metadata()
    
    def set_parent(self, parent_id: str):
        """Set the parent of this node"""
        self.parent_id = parent_id
        self.is_part_of = parent_id
        self._update_fractal_metadata()
    
    def _update_fractal_metadata(self):
        """Update fractal metadata after structural changes"""
        # Update fractal depth
        if self.parent_id:
            self.fractal_depth = 1  # In a real implementation, this would traverse up the tree
        else:
            self.fractal_depth = 0
        
        # Update self-similarity score
        self.self_similarity_score = self._calculate_self_similarity_score()
        
        # Update cross-scale mapping
        self.cross_scale_mapping = self._create_cross_scale_mapping()
        
        # Update timestamp
        self.updated_at = datetime.now().isoformat()
    
    def _calculate_self_similarity_score(self) -> float:
        """Calculate self-similarity score based on fractal properties"""
        # Base score on depth and branching
        depth_score = max(0, 1.0 - (self.fractal_depth * 0.1))  # Deeper = lower score
        branching_score = min(1.0, len(self.children) * 0.2)  # More children = higher score
        
        # Combine scores
        return (depth_score + branching_score) / 2.0
    
    def _create_cross_scale_mapping(self) -> Dict[str, str]:
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
        
        return scale_mappings.get(self.fractal_depth, scale_mappings[0])
    
    # ============================================================================
    # RESONANCE AND VIBRATIONAL METHODS
    # ============================================================================
    
    def add_vibrational_axis(self, axis_name: str):
        """Add a vibrational axis to this node"""
        if axis_name not in self.vibrational_axes:
            self.vibrational_axes.append(axis_name)
            self._update_resonance_metadata()
    
    def remove_vibrational_axis(self, axis_name: str):
        """Remove a vibrational axis from this node"""
        if axis_name in self.vibrational_axes:
            self.vibrational_axes.remove(axis_name)
            self._update_resonance_metadata()
    
    def add_harmonic_relationship(self, node_id: str):
        """Add a harmonic relationship to another node"""
        if node_id not in self.harmonic_relationships:
            self.harmonic_relationships.append(node_id)
            self._update_resonance_metadata()
    
    def remove_harmonic_relationship(self, node_id: str):
        """Remove a harmonic relationship to another node"""
        if node_id in self.harmonic_relationships:
            self.harmonic_relationships.remove(node_id)
            self._update_resonance_metadata()
    
    def _update_resonance_metadata(self):
        """Update resonance metadata after changes"""
        # Recalculate coherence score based on current state
        self.coherence_score = self._calculate_coherence_score()
        
        # Update timestamp
        self.updated_at = datetime.now().isoformat()
    
    def _calculate_coherence_score(self) -> float:
        """Calculate coherence score based on current resonance state"""
        # Base score from resonance pattern
        pattern_scores = {
            'harmonic': 1.0,
            'sympathetic': 0.9,
            'neutral': 0.5,
            'dissonant': 0.2,
            'destructive': 0.0
        }
        
        base_score = pattern_scores.get(self.resonance_pattern, 0.5)
        
        # Adjust based on vibrational axes alignment
        axis_bonus = min(0.1, len(self.vibrational_axes) * 0.02)
        
        # Adjust based on harmonic relationships
        relationship_bonus = min(0.1, len(self.harmonic_relationships) * 0.01)
        
        # Calculate final score
        final_score = base_score + axis_bonus + relationship_bonus
        
        return min(1.0, max(0.0, final_score))
    
    # ============================================================================
    # SERIALIZATION AND UTILITY METHODS
    # ============================================================================
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for storage/transmission"""
        return asdict(self)
    
    def to_json(self) -> str:
        """Convert node to JSON string"""
        return json.dumps(self.to_dict(), indent=2, default=str)
    
    def to_node(self) -> 'EnhancedGenericNode':
        """Meta-circular: this node can represent itself"""
        return self
    
    def get_content_hash(self) -> str:
        """Get content hash for integrity checking"""
        return hashlib.sha256(self.content.encode('utf-8')).hexdigest()
    
    def get_metadata_hash(self) -> str:
        """Get metadata hash for integrity checking"""
        metadata_str = json.dumps(self.to_dict(), sort_keys=True, default=str)
        return hashlib.sha256(metadata_str.encode('utf-8')).hexdigest()
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information for this node"""
        return {
            'node_id': self.node_id,
            'node_type': self.node_type,
            'name': self.name,
            'ontological_mapping': {
                'water_state': self.water_state,
                'fractal_layer': self.fractal_layer,
                'chakra': self.chakra,
                'frequency': self.frequency,
                'consciousness_level': self.consciousness_level,
                'quantum_state': self.quantum_state,
                'programming_ontology_layer': self.programming_ontology_layer
            },
            'epistemic_grounding': self.epistemic_label,
            'fractal_structure': {
                'depth': self.fractal_depth,
                'self_similarity_score': self.self_similarity_score,
                'cross_scale_mapping': self.cross_scale_mapping,
                'children_count': len(self.children),
                'parent_id': self.parent_id
            },
            'resonance_state': {
                'pattern': self.resonance_pattern,
                'coherence_score': self.coherence_score,
                'dissonance_level': self.dissonance_level,
                'vibrational_axes': self.vibrational_axes,
                'harmonic_relationships': self.harmonic_relationships
            },
            'metadata_quality': {
                'version': self.metadata_version,
                'factory_version': self.metadata_factory_version,
                'validated': self._validated,
                'canonical_keys_validated': self._canonical_keys_validated,
                'created_at': self.created_at,
                'updated_at': self.updated_at
            }
        }
    
    # ============================================================================
    # FACTORY METHODS
    # ============================================================================
    
    @classmethod
    def create_from_metadata_factory(cls, 
                                   node_type: str,
                                   name: str,
                                   content: str,
                                   parent_id: Optional[str] = None,
                                   children: List[str] = None,
                                   custom_metadata: Dict[str, Any] = None) -> 'EnhancedGenericNode':
        """
        Create an EnhancedGenericNode using the metadata factory
        
        Args:
            node_type: Type of node to create
            name: Node name
            content: Node content
            parent_id: Parent node ID
            children: List of child node IDs
            custom_metadata: Custom metadata to override defaults
            
        Returns:
            New EnhancedGenericNode instance
        """
        if children is None:
            children = []
        
        if custom_metadata is None:
            custom_metadata = {}
        
        # Get metadata template from factory
        metadata_template = metadata_factory.get_metadata_template(node_type)
        
        # Merge with custom metadata
        metadata = {**metadata_template, **custom_metadata}
        
        # Create fractal metadata
        fractal_depth = 0 if not parent_id else 1
        fractal_metadata = metadata_factory.create_fractal_metadata(
            fractal_depth=fractal_depth,
            parent_id=parent_id,
            children=children
        )
        
        # Create resonance metadata
        resonance_pattern = metadata.get('resonance_pattern', 'neutral')
        if isinstance(resonance_pattern, str):
            # Convert string to ResonancePattern enum
            try:
                resonance_pattern = ResonancePattern(resonance_pattern)
            except ValueError:
                resonance_pattern = ResonancePattern.NEUTRAL
        
        resonance_metadata = metadata_factory.create_resonance_metadata(
            resonance_pattern=resonance_pattern
        )
        
        # Create the enhanced node
        node = cls(
            node_id=f"enhanced_node_{int(datetime.now().timestamp())}",
            node_type=node_type,
            name=name,
            content=content,
            parent_id=parent_id,
            children=children,
            
            # Ontological metadata
            water_state=metadata['water_state'],
            fractal_layer=metadata['fractal_layer'],
            chakra=metadata['chakra'],
            frequency=metadata['frequency'],
            consciousness_level=metadata['consciousness_level'],
            quantum_state=metadata['quantum_state'],
            programming_ontology_layer=metadata['programming_ontology_layer'],
            epistemic_label=metadata['epistemic_label'],
            
            # Fractal metadata
            fractal_depth=fractal_metadata['fractal_depth'],
            has_part=fractal_metadata['has_part'],
            is_part_of=fractal_metadata['is_part_of'],
            self_similarity_score=fractal_metadata['self_similarity_score'],
            cross_scale_mapping=fractal_metadata['cross_scale_mapping'],
            
            # Resonance metadata
            resonance_pattern=resonance_metadata['resonance_pattern'],
            vibrational_axes=resonance_metadata['vibrational_axes'],
            harmonic_relationships=resonance_metadata['harmonic_relationships'],
            dissonance_level=resonance_metadata['dissonance_level'],
            coherence_score=resonance_metadata['coherence_score'],
            
            # Structure and relationship info
            structure_info={
                'fractal_depth': fractal_metadata['fractal_depth'],
                'node_type': node_type,
                'parent_id': parent_id,
                'children_count': len(children),
                'created_by_component': 'enhanced_generic_node',
                'created_at_timestamp': datetime.now().timestamp(),
                'fractal_relationships': fractal_metadata['fractal_relationships'],
                'sacred_geometry_patterns': []
            },
            relationship_info={
                'connections': [],
                'relationship_types': [],
                'resonance_weights': {},
                'vibrational_alignments': {}
            },
            
            # Metadata tracking
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            metadata_version=metadata.get('metadata_version', '1.0.0'),
            metadata_factory_version=metadata.get('metadata_factory_version', '1.0.0')
        )
        
        return node

# ============================================================================
# TESTING AND DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    # Test the enhanced generic node system
    print("🌟 Enhanced GenericNode System Initialized")
    
    # Create a system component node
    system_node = EnhancedGenericNode.create_from_metadata_factory(
        node_type='system_component',
        name='Living Codex Core System',
        content='The core system that implements Living Codex principles',
        custom_metadata={
            'water_state': 'ws.ice',
            'fractal_layer': 0,
            'chakra': 'ch.crown',
            'frequency': 'freq.963'
        }
    )
    
    print(f"\n❄️ System Component Node Created:")
    print(f"   ID: {system_node.node_id}")
    print(f"   Water State: {system_node.water_state}")
    print(f"   Fractal Layer: {system_node.fractal_layer}")
    print(f"   Chakra: {system_node.chakra}")
    print(f"   Frequency: {system_node.frequency}")
    print(f"   Consciousness Level: {system_node.consciousness_level}")
    print(f"   Quantum State: {system_node.quantum_state}")
    print(f"   Epistemic Label: {system_node.epistemic_label}")
    print(f"   Coherence Score: {system_node.coherence_score}")
    
    # Test fractal relationships
    print(f"\n🔷 Fractal Structure:")
    print(f"   Depth: {system_node.fractal_depth}")
    print(f"   Self-Similarity Score: {system_node.self_similarity_score}")
    print(f"   Cross-Scale Mapping: {system_node.cross_scale_mapping}")
    
    # Test resonance
    print(f"\n🎵 Resonance State:")
    print(f"   Pattern: {system_node.resonance_pattern}")
    print(f"   Dissonance Level: {system_node.dissonance_level}")
    print(f"   Vibrational Axes: {system_node.vibrational_axes}")
    
    # Test system resonance
    system_resonance = system_node.get_system_resonance()
    print(f"\n🌟 System Resonance:")
    print(f"   Validated: {system_resonance['metadata_quality']['validated']}")
    print(f"   Canonical Keys Validated: {system_resonance['metadata_quality']['canonical_keys_validated']}")
    
    print("\n✅ Enhanced GenericNode System ready for use!")
