#!/usr/bin/env python3
"""
Living Codex Persistence System
Handles complete system state persistence and restoration
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from collections import defaultdict

class LivingCodexPersistence:
    """
    Comprehensive persistence system for the Living Codex
    Handles saving and restoring all system state
    """
    
    def __init__(self, persistence_file: str = "living_codex_complete_state.json"):
        self.persistence_file = Path(persistence_file)
        self.state = {}
        self.last_save_time = None
        self.last_load_time = None
        
        print(f"🌟 Living Codex Persistence System initialized")
        print(f"   📁 Persistence file: {self.persistence_file}")
        print(f"   💾 State persistence enabled")
        print(f"   🔄 Auto-restoration enabled")
    
    def save_system_state(self, universal_system, fractal_system, ai_system, 
                         self_gen_system, vibrational_system, governance_system) -> bool:
        """
        Save complete system state to file
        
        Args:
            universal_system: Universal Knowledge Representation System
            fractal_system: Fractal Recursion System
            ai_system: Advanced AI Integration System
            self_gen_system: Self-Generating System
            vibrational_system: Vibrational Axes System
            governance_system: Resonance Governance System
        
        Returns:
            True if save successful, False otherwise
        """
        try:
            print(f"\n💾 Saving complete Living Codex system state...")
            
            # Collect state from all systems
            state = {
                "metadata": {
                    "save_timestamp": datetime.now().isoformat(),
                    "system_version": "2.0.0",
                    "total_systems": 6
                },
                "universal_system": {
                    "universal_concepts": self._serialize_concepts(universal_system.universal_concepts),
                    "concept_transformations": self._serialize_transformations(universal_system.concept_transformations),
                    "meta_circular_architectures": self._serialize_architectures(universal_system.meta_circular_architectures),
                    "knowledge_expansions": self._serialize_expansions(universal_system.knowledge_expansions),
                    "concept_to_node_mapping": universal_system.concept_to_node_mapping,
                    "node_to_concept_mapping": universal_system.node_to_concept_mapping
                },
                "fractal_system": {
                    "fractal_nodes": self._serialize_fractal_nodes(fractal_system.fractal_nodes),
                    "fractal_relationships": dict(fractal_system.fractal_relationships),
                    "cross_scale_mappings": fractal_system.cross_scale_mappings,
                    "fractal_patterns": list(fractal_system.fractal_patterns),
                    "exploration_cache": fractal_system.exploration_cache
                },
                "ai_system": {
                    "ai_agents": self._serialize_ai_agents(ai_system.ai_agents),
                    "consciousness_decisions": self._serialize_decisions(ai_system.consciousness_decisions),
                    "autonomous_explorations": self._serialize_explorations(ai_system.autonomous_explorations),
                    "ai_evolutions": self._serialize_evolutions(ai_system.ai_evolutions),
                    "agent_consciousness_history": dict(ai_system.agent_consciousness_history)
                },
                "self_gen_system": {
                    "discovered_concepts": self._serialize_concepts(self_gen_system.discovered_concepts),
                    "generated_specifications": self._serialize_specifications(self_gen_system.generated_specifications),
                    "ontological_evolutions": self._serialize_evolutions(self_gen_system.ontological_evolutions),
                    "concept_relationships": dict(self_gen_system.concept_relationships),
                    "evolution_history": self_gen_system.evolution_history
                },
                "vibrational_system": {
                    "vibrational_axes": vibrational_system.vibrational_axes,
                    "resonance_states": dict(vibrational_system.resonance_states),
                    "community_resonance": dict(vibrational_system.community_resonance),
                    "fractal_recursion_cache": vibrational_system.fractal_recursion_cache,
                    "cross_scale_cache": vibrational_system.cross_scale_cache
                },
                "governance_system": {
                    "resonance_decisions": self._serialize_decisions(governance_system.resonance_decisions),
                    "coherence_fields": self._serialize_fields(governance_system.coherence_fields),
                    "collective_intelligence": self._serialize_intelligence(governance_system.collective_intelligence),
                    "node_resonance_history": dict(governance_system.node_resonance_history),
                    "system_coherence_history": governance_system.system_coherence_history,
                    "governance_rules": governance_system.governance_rules
                }
            }
            
            # Save to file
            with open(self.persistence_file, 'w') as f:
                json.dump(state, f, indent=2, default=str)
            
            self.state = state
            self.last_save_time = datetime.now()
            
            # Calculate statistics
            total_concepts = len(state["universal_system"]["universal_concepts"])
            total_fractal_nodes = len(state["fractal_system"]["fractal_nodes"])
            total_ai_agents = len(state["ai_system"]["ai_agents"])
            
            print(f"✅ System state saved successfully!")
            print(f"   📊 Statistics:")
            print(f"      - Universal concepts: {total_concepts}")
            print(f"      - Fractal nodes: {total_fractal_nodes}")
            print(f"      - AI agents: {total_ai_agents}")
            print(f"      - File size: {self.persistence_file.stat().st_size / 1024:.1f} KB")
            print(f"      - Timestamp: {self.last_save_time.isoformat()}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to save system state: {e}")
            return False
    
    def load_system_state(self, universal_system, fractal_system, ai_system,
                         self_gen_system, vibrational_system, governance_system) -> bool:
        """
        Restore system state from file
        
        Args:
            universal_system: Universal Knowledge Representation System
            fractal_system: Fractal Recursion System
            ai_system: Advanced AI Integration System
            self_gen_system: Self-Generating System
            vibrational_system: Vibrational Axes System
            governance_system: Resonance Governance System
        
        Returns:
            True if load successful, False otherwise
        """
        try:
            if not self.persistence_file.exists():
                print(f"⚠️ No persistence file found: {self.persistence_file}")
                return False
            
            print(f"\n🔄 Loading Living Codex system state...")
            
            # Load state from file
            with open(self.persistence_file, 'r') as f:
                state = json.load(f)
            
            self.state = state
            self.last_load_time = datetime.now()
            
            # Restore universal system
            print(f"   🔄 Restoring universal system...")
            universal_system.universal_concepts = self._deserialize_concepts(state["universal_system"]["universal_concepts"])
            universal_system.concept_transformations = self._deserialize_transformations(state["universal_system"]["concept_transformations"])
            universal_system.meta_circular_architectures = self._deserialize_meta_circular_architectures(state["universal_system"]["meta_circular_architectures"])
            universal_system.knowledge_expansions = self._deserialize_expansions(state["universal_system"]["knowledge_expansions"])
            universal_system.concept_to_node_mapping = state["universal_system"]["concept_to_node_mapping"]
            universal_system.node_to_concept_mapping = state["universal_system"]["node_to_concept_mapping"]
            
            # Restore fractal system
            print(f"   🔄 Restoring fractal system...")
            fractal_system.fractal_nodes = self._deserialize_fractal_nodes(state["fractal_system"]["fractal_nodes"])
            fractal_system.fractal_relationships = defaultdict(set)
            for k, v in state["fractal_system"]["fractal_relationships"].items():
                fractal_system.fractal_relationships[k] = set(v)
            fractal_system.cross_scale_mappings = state["fractal_system"]["cross_scale_mappings"]
            fractal_system.fractal_patterns = set(state["fractal_system"]["fractal_patterns"])
            fractal_system.exploration_cache = state["fractal_system"]["exploration_cache"]
            
            # Restore AI system
            print(f"   🔄 Restoring AI system...")
            ai_system.ai_agents = self._deserialize_ai_agents(state["ai_system"]["ai_agents"])
            ai_system.consciousness_decisions = self._deserialize_decisions(state["ai_system"]["consciousness_decisions"])
            ai_system.autonomous_explorations = self._deserialize_explorations(state["ai_system"]["autonomous_explorations"])
            ai_system.ai_evolutions = self._deserialize_evolutions(state["ai_system"]["ai_evolutions"])
            ai_system.agent_consciousness_history = defaultdict(list)
            for k, v in state["ai_system"]["agent_consciousness_history"].items():
                ai_system.agent_consciousness_history[k] = v
            
            # Restore self-generating system
            print(f"   🔄 Restoring self-generating system...")
            self_gen_system.discovered_concepts = self._deserialize_concepts(state["self_gen_system"]["discovered_concepts"])
            self_gen_system.generated_specifications = self._serialize_specifications(state["self_gen_system"]["generated_specifications"])
            self_gen_system.ontological_evolutions = self._deserialize_evolutions(state["self_gen_system"]["ontological_evolutions"])
            self_gen_system.concept_relationships = defaultdict(set)
            for k, v in state["self_gen_system"]["concept_relationships"].items():
                self_gen_system.concept_relationships[k] = v
            self_gen_system.evolution_history = state["self_gen_system"]["evolution_history"]
            
            # Restore vibrational system
            print(f"   🔄 Restoring vibrational system...")
            vibrational_system.vibrational_axes = state["vibrational_system"]["vibrational_axes"]
            vibrational_system.resonance_states = defaultdict(dict)
            for k, v in state["vibrational_system"]["resonance_states"].items():
                vibrational_system.resonance_states[k] = v
            vibrational_system.community_resonance = defaultdict(dict)
            for k, v in state["vibrational_system"]["community_resonance"].items():
                vibrational_system.community_resonance[k] = v
            vibrational_system.fractal_recursion_cache = state["vibrational_system"]["fractal_recursion_cache"]
            vibrational_system.cross_scale_cache = state["vibrational_system"]["cross_scale_cache"]
            
            # Restore governance system
            print(f"   🔄 Restoring governance system...")
            governance_system.resonance_decisions = self._deserialize_decisions(state["governance_system"]["resonance_decisions"])
            governance_system.coherence_fields = self._serialize_fields(state["governance_system"]["coherence_fields"])
            governance_system.collective_intelligence = self._serialize_intelligence(state["governance_system"]["collective_intelligence"])
            governance_system.node_resonance_history = defaultdict(list)
            for k, v in state["governance_system"]["node_resonance_history"].items():
                governance_system.node_resonance_history[k] = v
            governance_system.system_coherence_history = state["governance_system"]["system_coherence_history"]
            governance_system.governance_rules = state["governance_system"]["governance_rules"]
            
            # Calculate statistics
            total_concepts = len(universal_system.universal_concepts)
            total_fractal_nodes = len(fractal_system.fractal_nodes)
            total_ai_agents = len(ai_system.ai_agents)
            
            print(f"✅ System state restored successfully!")
            print(f"   📊 Statistics:")
            print(f"      - Universal concepts: {total_concepts}")
            print(f"      - Fractal nodes: {total_fractal_nodes}")
            print(f"      - AI agents: {total_ai_agents}")
            print(f"      - Load time: {self.last_load_time.isoformat()}")
            print(f"      - Original save time: {state['metadata']['save_timestamp']}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to load system state: {e}")
            return False
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get information about the current persistence state"""
        info = {
            "persistence_file": str(self.persistence_file),
            "file_exists": self.persistence_file.exists(),
            "last_save_time": self.last_save_time.isoformat() if self.last_save_time else None,
            "last_load_time": self.last_load_time.isoformat() if self.last_load_time else None,
            "current_state_size": len(self.state) if self.state else 0
        }
        
        if self.persistence_file.exists():
            info["file_size_bytes"] = self.persistence_file.stat().st_size
            info["file_size_mb"] = round(info["file_size_bytes"] / (1024 * 1024), 2)
            info["file_modified"] = datetime.fromtimestamp(self.persistence_file.stat().st_mtime).isoformat()
        
        return info
    
    def _serialize_concepts(self, concepts: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize concepts for JSON storage"""
        serialized = {}
        for k, v in concepts.items():
            if hasattr(v, '__dict__'):
                # Handle enums properly
                concept_dict = {}
                for attr_name, attr_value in v.__dict__.items():
                    if hasattr(attr_value, 'value'):  # Enum
                        concept_dict[attr_name] = attr_value.value
                    else:
                        concept_dict[attr_name] = attr_value
                serialized[k] = concept_dict
            else:
                serialized[k] = v
        return serialized
    
    def _deserialize_concepts(self, concepts: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize concepts from JSON storage, reconstructing UniversalConcept objects."""
        deserialized = {}
        from universal_knowledge_representation_system import UniversalConcept
        from living_codex_ontology import EpistemicLabel, ConsciousnessLevel # Import necessary enums

        for concept_id, concept_data in concepts.items():
            if isinstance(concept_data, dict):
                try:
                    # Reconstruct UniversalConcept object
                    # Handle enum types for EpistemicLabel and ConsciousnessLevel
                    epistemic_label_value = concept_data.get('epistemic_label', EpistemicLabel.SPECULATIVE.value)
                    if isinstance(epistemic_label_value, str) and 'EpistemicLabel.' in epistemic_label_value:
                        epistemic_label_value = epistemic_label_value.split('.')[-1]
                    epistemic_label = EpistemicLabel(epistemic_label_value)

                    consciousness_requirements_values = concept_data.get('consciousness_requirements', [])
                    consciousness_requirements = []
                    for cr_value in consciousness_requirements_values:
                        if isinstance(cr_value, str) and 'ConsciousnessLevel.' in cr_value:
                            cr_value = cr_value.split('.')[-1]
                        try:
                            consciousness_requirements.append(ConsciousnessLevel(cr_value))
                        except ValueError:
                            print(f"⚠️ Warning: Invalid ConsciousnessLevel value '{cr_value}' for concept {concept_id}")
                            # Fallback or skip invalid values
                            pass

                    concept = UniversalConcept(
                        concept_id=concept_id,
                        name=concept_data.get('name', 'Unknown Concept'),
                        description=concept_data.get('description', 'No description'),
                        concept_type=concept_data.get('concept_type', 'abstract'),
                        ontological_properties=concept_data.get('ontological_properties', {}),
                        vibrational_axes=concept_data.get('vibrational_axes', []),
                        fractal_relationships=concept_data.get('fractal_relationships', {}),
                        consciousness_requirements=consciousness_requirements,
                        epistemic_foundations=[EpistemicLabel(ef_val.split('.')[-1] if isinstance(ef_val, str) and 'EpistemicLabel.' in ef_val else ef_val) for ef_val in concept_data.get('epistemic_foundations', [])],
                        creation_timestamp=concept_data.get('creation_timestamp', datetime.now().isoformat()),
                        last_updated=concept_data.get('last_updated', datetime.now().isoformat()),
                        living_node_id=concept_data.get('living_node_id'),
                        epistemic_label=epistemic_label
                    )
                    deserialized[concept_id] = concept
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct concept {concept_id}: {e}")
                    # Fallback to dictionary if reconstruction fails
                    deserialized[concept_id] = concept_data
            else:
                deserialized[concept_id] = concept_data
        return deserialized
    
    def _serialize_transformations(self, transformations: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize transformations for JSON storage"""
        return self._serialize_concepts(transformations)
    
    def _deserialize_transformations(self, transformations: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize transformations from JSON storage"""
        return self._deserialize_concepts(transformations)
    
    def _serialize_architectures(self, architectures: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize architectures for JSON storage"""
        return self._serialize_concepts(architectures)
    
    def _deserialize_meta_circular_architectures(self, architectures: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize meta-circular architectures from JSON storage"""
        deserialized = {}
        for arch_id, arch_data in architectures.items():
            if isinstance(arch_data, dict):
                try:
                    from universal_knowledge_representation_system import MetaCircularArchitecture
                    from living_codex_ontology import EpistemicLabel
                    
                    # Extract properties
                    system_components = arch_data.get('system_components', [])
                    self_descriptions = arch_data.get('self_descriptions', [])
                    meta_implementations = arch_data.get('meta_implementations', [])
                    circular_relationships = arch_data.get('circular_relationships', [])
                    architecture_confidence = arch_data.get('architecture_confidence', 0.5)
                    completeness_score = arch_data.get('completeness_score', 0.5)
                    created_at = arch_data.get('created_at', datetime.now().isoformat())
                    epistemic_label_value = arch_data.get('epistemic_label', 'speculative')
                    
                    # Handle epistemic label
                    if isinstance(epistemic_label_value, str) and 'EpistemicLabel.' in epistemic_label_value:
                        epistemic_label_value = epistemic_label_value.split('.')[-1]
                    epistemic_label = EpistemicLabel(epistemic_label_value)
                    
                    # Create MetaCircularArchitecture object
                    architecture = MetaCircularArchitecture(
                        architecture_id=arch_id,
                        system_components=system_components,
                        self_descriptions=self_descriptions,
                        meta_implementations=meta_implementations,
                        circular_relationships=circular_relationships,
                        architecture_confidence=architecture_confidence,
                        completeness_score=completeness_score,
                        created_at=created_at,
                        epistemic_label=epistemic_label
                    )
                    
                    deserialized[arch_id] = architecture
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct meta-circular architecture {arch_id}: {e}")
                    deserialized[arch_id] = arch_data
            else:
                deserialized[arch_id] = arch_data
        
        return deserialized
    
    def _serialize_expansions(self, expansions: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize expansions for JSON storage"""
        return self._serialize_concepts(expansions)
    
    def _deserialize_expansions(self, expansions: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize knowledge expansions from JSON storage"""
        deserialized = {}
        for expansion_id, expansion_data in expansions.items():
            if isinstance(expansion_data, dict):
                try:
                    from universal_knowledge_representation_system import InfiniteKnowledgeExpansion
                    from living_codex_ontology import EpistemicLabel
                    
                    # Extract properties
                    expansion_type = expansion_data.get('expansion_type', 'generic')
                    new_concepts_discovered = expansion_data.get('new_concepts_discovered', [])
                    knowledge_boundaries_pushed = expansion_data.get('knowledge_boundaries_pushed', [])
                    expansion_confidence = expansion_data.get('expansion_confidence', 0.5)
                    infinite_potential_score = expansion_data.get('infinite_potential_score', 0.5)
                    created_at = expansion_data.get('created_at', datetime.now().isoformat())
                    epistemic_label_value = expansion_data.get('epistemic_label', 'speculative')
                    
                    # Handle epistemic label
                    if isinstance(epistemic_label_value, str) and 'EpistemicLabel.' in epistemic_label_value:
                        epistemic_label_value = epistemic_label_value.split('.')[-1]
                    epistemic_label = EpistemicLabel(epistemic_label_value)
                    
                    # Create InfiniteKnowledgeExpansion object
                    expansion = InfiniteKnowledgeExpansion(
                        expansion_id=expansion_id,
                        expansion_type=expansion_type,
                        new_concepts_discovered=new_concepts_discovered,
                        knowledge_boundaries_pushed=knowledge_boundaries_pushed,
                        expansion_confidence=expansion_confidence,
                        infinite_potential_score=infinite_potential_score,
                        created_at=created_at,
                        epistemic_label=epistemic_label
                    )
                    
                    deserialized[expansion_id] = expansion
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct knowledge expansion {expansion_id}: {e}")
                    deserialized[expansion_id] = expansion_data
            else:
                deserialized[expansion_id] = expansion_data
        
        return deserialized
    
    def _serialize_fractal_nodes(self, nodes: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize fractal nodes for JSON storage"""
        return self._serialize_concepts(nodes)
    
    def _deserialize_fractal_nodes(self, nodes: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize fractal nodes from JSON storage"""
        deserialized = {}
        for node_id, node_data in nodes.items():
            if isinstance(node_data, dict):
                # Reconstruct FractalNode object
                try:
                    from fractal_recursion_system import FractalNode, FractalLayer
                    from living_codex_ontology import EpistemicLabel

                    # Extract basic properties
                    name = node_data.get('name', 'Unknown Node')
                    fractal_layer_value = node_data.get('fractal_layer', 2)
                    # Handle both enum values and string representations
                    if isinstance(fractal_layer_value, str) and 'FractalLayer.' in fractal_layer_value:
                        # Extract the numeric value from the enum string
                        try:
                            fractal_layer_value = int(fractal_layer_value.split('.')[-1])
                        except (ValueError, IndexError):
                            fractal_layer_value = 2  # Default fallback
                    fractal_layer = FractalLayer(fractal_layer_value)
                    has_part = node_data.get('has_part', [])
                    is_part_of = node_data.get('is_part_of')
                    fractal_depth = node_data.get('fractal_depth', 0)
                    self_similarity_score = node_data.get('self_similarity_score', 0.0)
                    cross_scale_mapping = node_data.get('cross_scale_mapping', {})
                    fractal_patterns = node_data.get('fractal_patterns', [])
                    metadata = node_data.get('metadata', {})
                    epistemic_label_value = node_data.get('epistemic_label', 'engineering')
                    # Handle both enum values and string representations
                    if isinstance(epistemic_label_value, str) and 'EpistemicLabel.' in epistemic_label_value:
                        try:
                            epistemic_label_value = epistemic_label_value.split('.')[-1]
                        except IndexError:
                            epistemic_label_value = 'engineering'
                    epistemic_label = EpistemicLabel(epistemic_label_value)

                    # Create the fractal node object
                    node = FractalNode(
                        node_id=node_id,
                        name=name,
                        fractal_layer=fractal_layer,
                        has_part=has_part,
                        is_part_of=is_part_of,
                        fractal_depth=fractal_depth,
                        self_similarity_score=self_similarity_score,
                        cross_scale_mapping=cross_scale_mapping,
                        fractal_patterns=fractal_patterns,
                        metadata=metadata,
                        epistemic_label=epistemic_label
                    )

                    deserialized[node_id] = node
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct fractal node {node_id}: {e}")
                    # Fallback to dictionary if reconstruction fails
                    deserialized[node_id] = node_data
            else:
                deserialized[node_id] = node_data

        return deserialized
    
    def _serialize_ai_agents(self, agents: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize AI agents for JSON storage"""
        return self._serialize_concepts(agents)
    
    def _deserialize_ai_agents(self, agents: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize AI agents from JSON storage"""
        return self._deserialize_concepts(agents)
    
    def _serialize_decisions(self, decisions: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize decisions for JSON storage"""
        return self._serialize_concepts(decisions)
    
    def _deserialize_decisions(self, decisions: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize decisions from JSON storage"""
        return self._deserialize_concepts(decisions)
    
    def _serialize_explorations(self, explorations: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize explorations for JSON storage"""
        return self._serialize_concepts(explorations)
    
    def _deserialize_explorations(self, explorations: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize explorations from JSON storage"""
        return self._deserialize_concepts(explorations)
    
    def _serialize_evolutions(self, evolutions: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize evolutions for JSON storage"""
        return self._serialize_concepts(evolutions)
    
    def _deserialize_evolutions(self, evolutions: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize evolutions from JSON storage"""
        return self._deserialize_concepts(evolutions)
    
    def _serialize_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize fields for JSON storage"""
        return self._serialize_concepts(fields)
    
    def _deserialize_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize fields from JSON storage"""
        return self._deserialize_concepts(fields)
    
    def _serialize_intelligence(self, intelligence: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize intelligence for JSON storage"""
        return self._serialize_concepts(intelligence)
    
    def _deserialize_intelligence(self, intelligence: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize intelligence from JSON storage"""
        return self._deserialize_concepts(intelligence)
    
    def _serialize_specifications(self, specifications: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize specifications for JSON storage"""
        return self._serialize_concepts(specifications)
    
    def _deserialize_specifications(self, specifications: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize specifications from JSON storage"""
        return self._deserialize_concepts(specifications)

    def _serialize_consciousness_states(self, states: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize consciousness quantum states"""
        serialized = {}
        for state_id, state in states.items():
            if hasattr(state, '__dict__'):
                serialized[state_id] = {
                    'consciousness_level': state.consciousness_level.value,
                    'quantum_state': state.quantum_state.value,
                    'water_state': state.water_state.value,
                    'frequency': state.frequency.value,
                    'chakra': state.chakra.value,
                    'coherence_level': state.coherence_level,
                    'resonance_strength': state.resonance_strength,
                    'created_at': state.created_at,
                    'epistemic_label': state.epistemic_label.value
                }
            else:
                serialized[state_id] = state
        return serialized
    
    def _deserialize_consciousness_states(self, states: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize consciousness quantum states"""
        deserialized = {}
        from advanced_consciousness_integration_system import ConsciousnessQuantumState
        from living_codex_ontology import ConsciousnessLevel, QuantumState, WaterStateKey, FrequencyKey, ChakraKey, EpistemicLabel
        
        for state_id, state_data in states.items():
            if isinstance(state_data, dict):
                try:
                    state = ConsciousnessQuantumState(
                        consciousness_level=ConsciousnessLevel(state_data.get('consciousness_level', 'awake')),
                        quantum_state=QuantumState(state_data.get('quantum_state', 'collapsed')),
                        water_state=WaterStateKey(state_data.get('water_state', 'ws.liquid')),
                        frequency=FrequencyKey(state_data.get('frequency', 'freq.639')),
                        chakra=ChakraKey(state_data.get('chakra', 'ch.heart')),
                        coherence_level=state_data.get('coherence_level', 0.5),
                        resonance_strength=state_data.get('resonance_strength', 0.5),
                        created_at=state_data.get('created_at', datetime.now().isoformat()),
                        epistemic_label=EpistemicLabel(state_data.get('epistemic_label', 'speculative'))
                    )
                    deserialized[state_id] = state
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct consciousness state {state_id}: {e}")
                    deserialized[state_id] = state_data
            else:
                deserialized[state_id] = state_data
        return deserialized
    
    def _serialize_resonance_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize resonance fields"""
        serialized = {}
        for field_id, field in fields.items():
            if hasattr(field, '__dict__'):
                serialized[field_id] = {
                    'field_id': field.field_id,
                    'field_name': field.field_name,
                    'resonance_pattern': field.resonance_pattern.value,
                    'water_state': field.water_state.value,
                    'frequency': field.frequency.value,
                    'chakra': field.chakra.value,
                    'coherence_radius': field.coherence_radius,
                    'resonance_strength': field.resonance_strength,
                    'field_participants': field.field_participants,
                    'field_geometry': field.field_geometry,
                    'created_at': field.created_at,
                    'epistemic_label': field.epistemic_label.value
                }
            else:
                serialized[field_id] = field
        return serialized
    
    def _deserialize_resonance_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize resonance fields"""
        deserialized = {}
        from advanced_consciousness_integration_system import ResonanceField
        from living_codex_ontology import ResonancePattern, WaterStateKey, FrequencyKey, ChakraKey, EpistemicLabel
        
        for field_id, field_data in fields.items():
            if isinstance(field_data, dict):
                try:
                    field = ResonanceField(
                        field_id=field_data.get('field_id', field_id),
                        field_name=field_data.get('field_name', 'Unknown Field'),
                        resonance_pattern=ResonancePattern(field_data.get('resonance_pattern', 'harmonic')),
                        water_state=WaterStateKey(field_data.get('water_state', 'ws.liquid')),
                        frequency=FrequencyKey(field_data.get('frequency', 'freq.639')),
                        chakra=ChakraKey(field_data.get('chakra', 'ch.heart')),
                        coherence_radius=field_data.get('coherence_radius', 5.0),
                        resonance_strength=field_data.get('resonance_strength', 0.5),
                        field_participants=field_data.get('field_participants', []),
                        field_geometry=field_data.get('field_geometry', {}),
                        created_at=field_data.get('created_at', datetime.now().isoformat()),
                        epistemic_label=EpistemicLabel(field_data.get('epistemic_label', 'speculative'))
                    )
                    deserialized[field_id] = field
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct resonance field {field_id}: {e}")
                    deserialized[field_id] = field_data
            else:
                deserialized[field_id] = field_data
        return deserialized
    
    def _serialize_consciousness_coherence_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize consciousness coherence fields"""
        serialized = {}
        for field_id, field in fields.items():
            if hasattr(field, '__dict__'):
                serialized[field_id] = {
                    'field_id': field.field_id,
                    'field_name': field.field_name,
                    'consciousness_levels': [level.value for level in field.consciousness_levels],
                    'quantum_states': [state.value for state in field.quantum_states],
                    'water_states': [state.value for state in field.water_states],
                    'coherence_score': field.coherence_score,
                    'resonance_patterns': [pattern.value for pattern in field.resonance_patterns],
                    'field_geometry': field.field_geometry,
                    'participants': field.participants,
                    'created_at': field.created_at,
                    'epistemic_label': field.epistemic_label.value
                }
            else:
                serialized[field_id] = field
        return serialized
    
    def _deserialize_consciousness_coherence_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize consciousness coherence fields"""
        deserialized = {}
        from advanced_consciousness_integration_system import CoherenceField
        from living_codex_ontology import ConsciousnessLevel, QuantumState, WaterStateKey, ResonancePattern, EpistemicLabel
        
        for field_id, field_data in fields.items():
            if isinstance(field_data, dict):
                try:
                    field = CoherenceField(
                        field_id=field_data.get('field_id', field_id),
                        field_name=field_data.get('field_name', 'Unknown Coherence Field'),
                        consciousness_levels=[ConsciousnessLevel(level) for level in field_data.get('consciousness_levels', [])],
                        quantum_states=[QuantumState(state) for state in field_data.get('quantum_states', [])],
                        water_states=[WaterStateKey(state) for state in field_data.get('water_states', [])],
                        coherence_score=field_data.get('coherence_score', 0.5),
                        resonance_patterns=[ResonancePattern(pattern) for pattern in field_data.get('resonance_patterns', [])],
                        field_geometry=field_data.get('field_geometry', {}),
                        participants=field_data.get('participants', []),
                        created_at=field_data.get('created_at', datetime.now().isoformat()),
                        epistemic_label=EpistemicLabel(field_data.get('epistemic_label', 'speculative'))
                    )
                    deserialized[field_id] = field
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct coherence field {field_id}: {e}")
                    deserialized[field_id] = field_data
            else:
                deserialized[field_id] = field_data
        return deserialized
    
    def _serialize_consciousness_evolutions(self, evolutions: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize consciousness evolutions"""
        serialized = {}
        for evolution_id, evolution in evolutions.items():
            if hasattr(evolution, '__dict__'):
                serialized[evolution_id] = {
                    'evolution_id': evolution.evolution_id,
                    'starting_state': evolution.starting_state.consciousness_level.value if evolution.starting_state else 'unknown',
                    'target_state': evolution.target_state.consciousness_level.value if evolution.target_state else 'unknown',
                    'evolution_path': [state.consciousness_level.value for state in evolution.evolution_path],
                    'evolution_confidence': evolution.evolution_confidence,
                    'resonance_requirements': [pattern.value for pattern in evolution.resonance_requirements],
                    'water_state_transitions': [state.value for state in evolution.water_state_transitions],
                    'created_at': evolution.created_at,
                    'epistemic_label': evolution.epistemic_label.value
                }
            else:
                serialized[evolution_id] = evolution
        return serialized
    
    def _deserialize_consciousness_evolutions(self, evolutions: Dict[str, Any]) -> Dict[str, Any]:
        """Deserialize consciousness evolutions"""
        deserialized = {}
        from advanced_consciousness_integration_system import ConsciousnessEvolution
        from living_codex_ontology import ResonancePattern, WaterStateKey, EpistemicLabel
        
        for evolution_id, evolution_data in evolutions.items():
            if isinstance(evolution_data, dict):
                try:
                    # For now, create a simplified evolution object
                    evolution = ConsciousnessEvolution(
                        evolution_id=evolution_data.get('evolution_id', evolution_id),
                        starting_state=None,  # Would need to reconstruct full state
                        target_state=None,    # Would need to reconstruct full state
                        evolution_path=[],    # Would need to reconstruct full states
                        evolution_confidence=evolution_data.get('evolution_confidence', 0.5),
                        resonance_requirements=[ResonancePattern(pattern) for pattern in evolution_data.get('resonance_requirements', [])],
                        water_state_transitions=[WaterStateKey(state) for state in evolution_data.get('water_state_transitions', [])],
                        created_at=evolution_data.get('created_at', datetime.now().isoformat()),
                        epistemic_label=EpistemicLabel(evolution_data.get('epistemic_label', 'speculative'))
                    )
                    deserialized[evolution_id] = evolution
                except Exception as e:
                    print(f"⚠️ Warning: Could not reconstruct consciousness evolution {evolution_id}: {e}")
                    deserialized[evolution_id] = evolution_data
            else:
                deserialized[evolution_id] = evolution_data
        return deserialized
