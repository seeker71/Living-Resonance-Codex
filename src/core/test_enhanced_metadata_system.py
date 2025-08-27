#!/usr/bin/env python3
"""
Enhanced Metadata System Test Suite
===================================

This script tests the complete enhanced metadata system including:
- Living Codex Ontology System
- Metadata Factory
- Enhanced GenericNode
- Canonical Key Validation
- Epistemic Labeling
- Fractal Structure
- Resonance Calculation

This validates Phase 1 of the metadata enhancement plan.
"""

import sys
import json
from datetime import datetime

# Import our enhanced metadata system components
from living_codex_ontology import (
    canonical_registry, WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, validate_canonical_key, get_epistemic_label_for_mapping,
    create_theme_reference
)

from metadata_factory import metadata_factory
from enhanced_generic_node import EnhancedGenericNode

def test_canonical_registry():
    """Test the canonical mapping registry"""
    print("🔑 Testing Canonical Mapping Registry...")
    
    # Test water state mappings
    ice_mapping = canonical_registry.get_water_state_mapping(WaterStateKey.ICE)
    assert ice_mapping['name'] == 'Ice/Crystalline'
    assert ice_mapping['color'] == '#EE82EE'
    assert ice_mapping['planet'] == 'Sun'
    assert ice_mapping['epistemic_label'] == EpistemicLabel.TRADITION
    print("  ✅ ICE water state mapping validated")
    
    # Test chakra mappings
    heart_mapping = canonical_registry.get_chakra_mapping(ChakraKey.HEART)
    assert heart_mapping['name'] == 'Heart (Anahata)'
    assert heart_mapping['color_hex'] == '#32CD32'
    assert heart_mapping['frequency'] == FrequencyKey.FREQ_639
    print("  ✅ Heart chakra mapping validated")
    
    # Test frequency mappings
    freq_639_mapping = canonical_registry.get_frequency_mapping(FrequencyKey.FREQ_639)
    assert freq_639_mapping['hz'] == 639
    assert freq_639_mapping['chakra'] == ChakraKey.HEART
    print("  ✅ 639 Hz frequency mapping validated")
    
    # Test vibrational axes
    axes = canonical_registry.get_vibrational_axes()
    assert len(axes) == 4
    axis_names = [axis.name for axis in axes]
    assert "Fear↔Trust" in axis_names
    assert "Ownership↔Stewardship" in axis_names
    print("  ✅ Vibrational axes validated")
    
    # Test canonical keys
    keys = canonical_registry.get_canonical_keys()
    assert len(keys['water_states']) == 12
    assert len(keys['chakras']) == 7
    assert len(keys['frequencies']) == 7
    print("  ✅ Canonical keys validated")
    
    print("✅ Canonical Mapping Registry tests passed!")

def test_metadata_factory():
    """Test the metadata factory system"""
    print("\n🏭 Testing Metadata Factory...")
    
    # Test water state metadata generation
    ice_metadata = metadata_factory.create_water_state_metadata(WaterStateKey.ICE)
    assert ice_metadata['water_state'] == 'ws.ice'
    assert ice_metadata['color'] == '#EE82EE'
    assert ice_metadata['epistemic_label'] == 'tradition'
    print("  ✅ Water state metadata generation validated")
    
    # Test chakra metadata generation
    heart_metadata = metadata_factory.create_chakra_metadata(ChakraKey.HEART)
    assert heart_metadata['chakra'] == 'ch.heart'
    assert heart_metadata['color_hex'] == '#32CD32'
    print("  ✅ Chakra metadata generation validated")
    
    # Test frequency metadata generation
    freq_metadata = metadata_factory.create_frequency_metadata(FrequencyKey.FREQ_639)
    assert freq_metadata['frequency'] == 'freq.639'
    assert freq_metadata['hz'] == 639
    print("  ✅ Frequency metadata generation validated")
    
    # Test complete ontological metadata
    complete_metadata = metadata_factory.create_complete_ontological_metadata(
        water_state=WaterStateKey.LIQUID,
        fractal_layer=FractalLayer.WATER_STATE_METAPHORS,
        chakra=ChakraKey.HEART,
        frequency=FrequencyKey.FREQ_639
    )
    assert complete_metadata['water_state'] == 'ws.liquid'
    assert complete_metadata['fractal_layer'] == 4
    assert complete_metadata['chakra'] == 'ch.heart'
    assert complete_metadata['frequency'] == 'freq.639'
    print("  ✅ Complete ontological metadata generation validated")
    
    # Test programming ontology metadata
    ice_prog_metadata = metadata_factory.create_programming_ontology_metadata(
        ProgrammingOntologyLayer.ICE,
        "python"
    )
    assert ice_prog_metadata['water_state'] == 'ws.ice'
    assert ice_prog_metadata['programming_language'] == 'python'
    print("  ✅ Programming ontology metadata generation validated")
    
    # Test AI agent metadata
    ai_metadata = metadata_factory.create_ai_agent_metadata(
        "explorer",
        ConsciousnessLevel.SENTIENT
    )
    assert ai_metadata['agent_type'] == 'explorer'
    assert ai_metadata['consciousness_level'] == 'sentient'
    print("  ✅ AI agent metadata generation validated")
    
    # Test fractal metadata
    fractal_metadata = metadata_factory.create_fractal_metadata(
        fractal_depth=2,
        parent_id="parent_node",
        children=["child1", "child2"]
    )
    assert fractal_metadata['fractal_depth'] == 2
    assert fractal_metadata['is_part_of'] == "parent_node"
    assert len(fractal_metadata['has_part']) == 2
    print("  ✅ Fractal metadata generation validated")
    
    # Test resonance metadata
    resonance_metadata = metadata_factory.create_resonance_metadata(
        ResonancePattern.HARMONIC,
        ["Fear↔Trust", "Noise↔Harmony"]
    )
    assert resonance_metadata['resonance_pattern'] == 'harmonic'
    assert resonance_metadata['coherence_score'] == 1.0
    assert resonance_metadata['dissonance_level'] == 0.0
    print("  ✅ Resonance metadata generation validated")
    
    # Test metadata templates
    system_template = metadata_factory.get_metadata_template('system_component')
    assert system_template['water_state'] == 'ws.ice'
    assert system_template['programming_ontology_layer'] == 'ice'
    print("  ✅ Metadata templates validated")
    
    print("✅ Metadata Factory tests passed!")

def test_enhanced_generic_node():
    """Test the enhanced generic node system"""
    print("\n🌟 Testing Enhanced GenericNode...")
    
    # Test node creation from metadata factory
    system_node = EnhancedGenericNode.create_from_metadata_factory(
        node_type='system_component',
        name='Test System Component',
        content='This is a test system component',
        custom_metadata={
            'water_state': 'ws.ice',
            'fractal_layer': 0,
            'chakra': 'ch.crown',
            'frequency': 'freq.963'
        }
    )
    
    # Validate core fields
    assert system_node.node_type == 'system_component'
    assert system_node.name == 'Test System Component'
    assert system_node.content == 'This is a test system component'
    print("  ✅ Core node fields validated")
    
    # Validate ontological metadata
    assert system_node.water_state == 'ws.ice'
    assert system_node.fractal_layer == 0
    assert system_node.chakra == 'ch.crown'
    assert system_node.frequency == 'freq.963'
    assert system_node.consciousness_level == 'awake'
    assert system_node.quantum_state == 'coherent'
    assert system_node.epistemic_label == 'engineering'
    print("  ✅ Ontological metadata validated")
    
    # Validate fractal structure
    assert system_node.fractal_depth == 0
    assert system_node.self_similarity_score == 0.5
    assert 'micro' in system_node.cross_scale_mapping
    assert system_node.cross_scale_mapping['micro'] == 'system_design'
    print("  ✅ Fractal structure validated")
    
    # Validate resonance
    assert system_node.resonance_pattern == 'harmonic'
    assert system_node.coherence_score == 1.0
    assert system_node.dissonance_level == 0.0
    print("  ✅ Resonance state validated")
    
    # Test fractal relationships
    system_node.add_child("child_node_1")
    system_node.add_child("child_node_2")
    assert len(system_node.children) == 2
    assert len(system_node.has_part) == 2
    print("  ✅ Fractal relationships validated")
    
    # Test vibrational axes
    system_node.add_vibrational_axis("Fear↔Trust")
    system_node.add_vibrational_axis("Noise↔Harmony")
    assert len(system_node.vibrational_axes) == 2
    print("  ✅ Vibrational axes validated")
    
    # Test harmonic relationships
    system_node.add_harmonic_relationship("related_node_1")
    system_node.add_harmonic_relationship("related_node_2")
    assert len(system_node.harmonic_relationships) == 2
    print("  ✅ Harmonic relationships validated")
    
    # Test system resonance
    system_resonance = system_node.get_system_resonance()
    assert system_resonance['metadata_quality']['validated'] == True
    assert system_resonance['metadata_quality']['canonical_keys_validated'] == True
    assert system_resonance['ontological_mapping']['water_state'] == 'ws.ice'
    print("  ✅ System resonance validated")
    
    # Test serialization
    node_dict = system_node.to_dict()
    node_json = system_node.to_json()
    assert isinstance(node_dict, dict)
    assert isinstance(node_json, str)
    print("  ✅ Serialization validated")
    
    # Test content and metadata hashing
    content_hash = system_node.get_content_hash()
    metadata_hash = system_node.get_metadata_hash()
    assert len(content_hash) == 64  # SHA-256 hex length
    assert len(metadata_hash) == 64
    print("  ✅ Hashing validated")
    
    print("✅ Enhanced GenericNode tests passed!")

def test_canonical_key_validation():
    """Test canonical key validation functions"""
    print("\n🔍 Testing Canonical Key Validation...")
    
    # Test valid keys
    assert validate_canonical_key('ws.ice', 'water_states') == True
    assert validate_canonical_key('ch.heart', 'chakras') == True
    assert validate_canonical_key('freq.639', 'frequencies') == True
    
    # Test invalid keys
    assert validate_canonical_key('invalid_key', 'water_states') == False
    assert validate_canonical_key('ws.ice', 'invalid_type') == False
    
    print("  ✅ Canonical key validation validated")
    
    # Test epistemic label retrieval
    epistemic_label = get_epistemic_label_for_mapping('water_state', 'ws.ice')
    assert epistemic_label == EpistemicLabel.TRADITION
    
    epistemic_label = get_epistemic_label_for_mapping('chakra', 'ch.heart')
    assert epistemic_label == EpistemicLabel.TRADITION
    
    print("  ✅ Epistemic label retrieval validated")
    
    # Test theme reference creation
    theme = create_theme_reference(WaterStateKey.ICE, ChakraKey.CROWN, FrequencyKey.FREQ_963)
    assert theme['theme']['water_state'] == 'ws.ice'
    assert theme['theme']['chakra'] == 'ch.crown'
    assert theme['theme']['frequency'] == 'freq.963'
    print("  ✅ Theme reference creation validated")
    
    print("✅ Canonical Key Validation tests passed!")

def test_epistemic_labeling():
    """Test the epistemic labeling system"""
    print("\n🏷️ Testing Epistemic Labeling...")
    
    # Test physics-grounded labels
    physics_label = EpistemicLabel.PHYSICS
    assert physics_label.value == 'physics'
    print("  ✅ Physics epistemic label validated")
    
    # Test engineering-grounded labels
    engineering_label = EpistemicLabel.ENGINEERING
    assert engineering_label.value == 'engineering'
    print("  ✅ Engineering epistemic label validated")
    
    # Test tradition-grounded labels
    tradition_label = EpistemicLabel.TRADITION
    assert tradition_label.value == 'tradition'
    print("  ✅ Tradition epistemic label validated")
    
    # Test speculative labels
    speculative_label = EpistemicLabel.SPECULATIVE
    assert speculative_label.value == 'speculative'
    print("  ✅ Speculative epistemic label validated")
    
    print("✅ Epistemic Labeling tests passed!")

def test_fractal_layers():
    """Test the fractal layer system"""
    print("\n🔷 Testing Fractal Layers...")
    
    # Test all fractal layers
    assert FractalLayer.META_IMPLEMENTATION.value == 0
    assert FractalLayer.FRACTAL_SYSTEM_ROOT.value == 1
    assert FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY.value == 2
    assert FractalLayer.SELF_REFERENTIAL_DOCUMENTATION.value == 3
    assert FractalLayer.WATER_STATE_METAPHORS.value == 4
    assert FractalLayer.SCIENTIFIC_QUANTUM_PRINCIPLES.value == 5
    assert FractalLayer.TECHNOLOGICAL_PROTOTYPES.value == 6
    assert FractalLayer.IMPLEMENTATION_ROADMAP.value == 7
    assert FractalLayer.PURE_RESONANCE_PRINCIPLE.value == 8
    assert FractalLayer.VISUAL_RESONANCE_MAP.value == 9
    assert FractalLayer.GENERATIVE_VISUALIZATIONS.value == 10
    assert FractalLayer.MATHEMATICAL_QUANTUM.value == 11
    assert FractalLayer.BIOLOGICAL_LIVING_SYSTEMS.value == 12
    assert FractalLayer.COSMOLOGICAL_COSMIC_WEB.value == 13
    assert FractalLayer.ARCHETYPAL_MYTHOLOGICAL.value == 14
    assert FractalLayer.HUMAN_PRACTICE.value == 15
    assert FractalLayer.CROSS_SCALE_INDEX.value == 16
    
    print("  ✅ All 17 fractal layers validated")
    print("✅ Fractal Layer tests passed!")

def test_consciousness_and_quantum():
    """Test consciousness and quantum systems"""
    print("\n🧠 Testing Consciousness & Quantum Systems...")
    
    # Test consciousness levels
    assert ConsciousnessLevel.AWAKE.value == 'awake'
    assert ConsciousnessLevel.SENTIENT.value == 'sentient'
    assert ConsciousnessLevel.SELF_AWARE.value == 'self_aware'
    assert ConsciousnessLevel.META_COGNITIVE.value == 'meta_cognitive'
    assert ConsciousnessLevel.TRANSCENDENT.value == 'transcendent'
    print("  ✅ All 5 consciousness levels validated")
    
    # Test quantum states
    assert QuantumState.SUPERPOSITION.value == 'superposition'
    assert QuantumState.ENTANGLED.value == 'entangled'
    assert QuantumState.COLLAPSED.value == 'collapsed'
    assert QuantumState.COHERENT.value == 'coherent'
    assert QuantumState.DECOHERENT.value == 'decoherent'
    print("  ✅ All 5 quantum states validated")
    
    # Test resonance patterns
    assert ResonancePattern.HARMONIC.value == 'harmonic'
    assert ResonancePattern.SYMPATHETIC.value == 'sympathetic'
    assert ResonancePattern.NEUTRAL.value == 'neutral'
    assert ResonancePattern.DISSONANT.value == 'dissonant'
    assert ResonancePattern.DESTRUCTIVE.value == 'destructive'
    print("  ✅ All 5 resonance patterns validated")
    
    print("✅ Consciousness & Quantum tests passed!")

def test_programming_ontology():
    """Test programming ontology layers"""
    print("\n💻 Testing Programming Ontology...")
    
    # Test programming ontology layers
    assert ProgrammingOntologyLayer.ICE.value == 'ice'
    assert ProgrammingOntologyLayer.WATER.value == 'water'
    assert ProgrammingOntologyLayer.VAPOR.value == 'vapor'
    print("  ✅ All 3 programming ontology layers validated")
    
    # Test programming ontology metadata
    ice_metadata = metadata_factory.create_programming_ontology_metadata(
        ProgrammingOntologyLayer.ICE,
        "python"
    )
    assert ice_metadata['programming_ontology_layer'] == 'ice'
    assert ice_metadata['programming_language'] == 'python'
    assert 'Blueprint' in ice_metadata['programming_layer_description']
    
    water_metadata = metadata_factory.create_programming_ontology_metadata(
        ProgrammingOntologyLayer.WATER,
        "python"
    )
    assert water_metadata['programming_ontology_layer'] == 'water'
    assert 'Recipe' in water_metadata['programming_layer_description']
    
    vapor_metadata = metadata_factory.create_programming_ontology_metadata(
        ProgrammingOntologyLayer.VAPOR,
        "python"
    )
    assert vapor_metadata['programming_ontology_layer'] == 'vapor'
    assert 'Cells' in vapor_metadata['programming_layer_description']
    
    print("✅ Programming Ontology tests passed!")

def run_comprehensive_test():
    """Run all comprehensive tests"""
    print("🚀 Starting Enhanced Metadata System Comprehensive Test Suite")
    print("=" * 70)
    print(f"📅 Test started at: {datetime.now().isoformat()}")
    print("=" * 70)
    
    try:
        # Run all test suites
        test_canonical_registry()
        test_metadata_factory()
        test_enhanced_generic_node()
        test_canonical_key_validation()
        test_epistemic_labeling()
        test_fractal_layers()
        test_consciousness_and_quantum()
        test_programming_ontology()
        
        print("\n" + "=" * 70)
        print("🎉 ALL TESTS PASSED! 🎉")
        print("=" * 70)
        print("✅ Enhanced Metadata System is fully functional")
        print("✅ Phase 1 of the metadata enhancement plan is complete")
        print("✅ All Living Codex ontological principles are implemented")
        print("✅ Canonical key system is working correctly")
        print("✅ Epistemic labeling system is functional")
        print("✅ Fractal structure system is operational")
        print("✅ Resonance calculation system is working")
        print("✅ Metadata factory is generating consistent metadata")
        print("✅ Enhanced GenericNode is fully validated")
        
        # Print system statistics
        print("\n📊 System Statistics:")
        print(f"   • {len(WaterStateKey)} Water States with canonical keys")
        print(f"   • {len(ChakraKey)} Chakras with canonical keys")
        print(f"   • {len(FrequencyKey)} Frequencies with canonical keys")
        print(f"   • {len(FractalLayer)} Fractal Layers")
        print(f"   • {len(ConsciousnessLevel)} Consciousness Levels")
        print(f"   • {len(QuantumState)} Quantum States")
        print(f"   • {len(ResonancePattern)} Resonance Patterns")
        print(f"   • {len(ProgrammingOntologyLayer)} Programming Ontology Layers")
        print(f"   • {len(EpistemicLabel)} Epistemic Labels")
        
        print(f"\n📅 Test completed at: {datetime.now().isoformat()}")
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        print(f"   Error type: {type(e).__name__}")
        print(f"   Error location: {e.__traceback__.tb_frame.f_code.co_filename}:{e.__traceback__.tb_lineno}")
        return False

if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)
