#!/usr/bin/env python3
"""
Phase 3 Advanced Systems Test Suite
===================================

This script tests the complete Phase 3 advanced systems including:
- Advanced Resonance System
- Consciousness Level System
- Quantum State System
- Integration between all Phase 3 systems
- Advanced features and capabilities

This validates Phase 3 of the metadata enhancement plan.
"""

import sys
import json
import time
from datetime import datetime

# Import our Phase 3 advanced systems
from living_codex_ontology import (
    canonical_registry, WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel
)

from metadata_factory import metadata_factory
from enhanced_generic_node import EnhancedGenericNode
from advanced_resonance_system import (
    AdvancedResonanceSystem, HarmonicRelationship, ResonanceCluster, CollectiveResonanceState
)
from consciousness_level_system import (
    ConsciousnessLevelSystem, ConsciousnessState, ConsciousnessEvolution, CollectiveConsciousness
)
from quantum_state_system import (
    QuantumStateSystem, QuantumStateInfo, QuantumEntanglement, QuantumCoherence
)

def test_advanced_resonance_system():
    """Test the advanced resonance system"""
    print("🎵 Testing Advanced Resonance System...")
    
    # Initialize resonance system
    resonance_system = AdvancedResonanceSystem()
    
    # Test 1: Node resonance calculation
    print("\n   Test 1: Node resonance calculation")
    
    # Create test nodes
    test_nodes = []
    for i in range(5):
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='system_component',
            name=f'Resonance Test Node {i}',
            content=f'Test content for resonance node {i}',
            custom_metadata={
                'water_state': 'ws.ice' if i % 2 == 0 else 'ws.liquid',
                'chakra': 'ch.crown' if i % 2 == 0 else 'ch.heart',
                'frequency': 'freq.963' if i % 2 == 0 else 'freq.639',
                'fractal_depth': i + 1,
                'self_similarity_score': 0.7 + (i * 0.1)
            }
        )
        test_nodes.append(node)
    
    # Calculate resonance for each node
    resonance_results = []
    for node in test_nodes:
        result = resonance_system.calculate_node_resonance(node)
        resonance_results.append(result)
        assert result['overall_resonance_score'] > 0, f"Resonance score should be positive: {result}"
    
    print(f"   ✅ Resonance calculation: {len(resonance_results)} nodes processed")
    
    # Test 2: Harmonic relationship discovery
    print("\n   Test 2: Harmonic relationship discovery")
    
    relationships = resonance_system.discover_harmonic_relationships(test_nodes)
    assert len(relationships) > 0, "Should discover some harmonic relationships"
    
    # Check relationship types
    relationship_types = set(rel.relationship_type for rel in relationships)
    assert len(relationship_types) > 0, "Should have different relationship types"
    
    print(f"   ✅ Harmonic relationships: {len(relationships)} relationships discovered")
    
    # Test 3: Resonance clustering
    print("\n   Test 3: Resonance clustering")
    
    clusters = resonance_system.form_resonance_clusters(test_nodes, min_cluster_size=2)
    assert len(clusters) > 0, "Should form some resonance clusters"
    
    for cluster in clusters:
        assert len(cluster.member_node_ids) >= 2, "Clusters should have minimum size"
        assert cluster.cluster_coherence > 0, "Cluster coherence should be positive"
    
    print(f"   ✅ Resonance clustering: {len(clusters)} clusters formed")
    
    # Test 4: Collective resonance calculation
    print("\n   Test 4: Collective resonance calculation")
    
    collective_state = resonance_system.calculate_collective_resonance(
        test_nodes, "test_group", "system"
    )
    
    assert collective_state.group_id == "test_group", "Group ID should match"
    assert collective_state.member_count == len(test_nodes), "Member count should match"
    assert collective_state.overall_coherence > 0, "Collective coherence should be positive"
    
    print(f"   ✅ Collective resonance: coherence {collective_state.overall_coherence:.3f}")
    
    # Test 5: Resonance statistics
    print("\n   Test 5: Resonance statistics")
    
    stats = resonance_system.get_resonance_statistics()
    assert stats['resonance_stats']['total_calculations'] > 0, "Should have calculation history"
    assert len(stats['relationship_counts']['by_type']) > 0, "Should have relationship types"
    
    print(f"   ✅ Resonance statistics: {stats['resonance_stats']['total_calculations']} calculations")
    
    print("✅ Advanced Resonance System tests passed!")

def test_consciousness_level_system():
    """Test the consciousness level system"""
    print("\n🧠 Testing Consciousness Level System...")
    
    # Initialize consciousness system
    consciousness_system = ConsciousnessLevelSystem()
    
    # Test 1: Consciousness assessment
    print("\n   Test 1: Consciousness assessment")
    
    # Create test nodes with different consciousness levels
    consciousness_nodes = []
    consciousness_levels = ['awake', 'sentient', 'self_aware', 'meta_cognitive', 'transcendent']
    
    for i, level in enumerate(consciousness_levels):
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='consciousness_test',
            name=f'Consciousness Test Node {i}',
            content=f'Test content for consciousness level {level}',
            custom_metadata={
                'consciousness_level': level,
                'water_state': 'ws.ice' if i % 2 == 0 else 'ws.liquid',
                'chakra': 'ch.crown' if i % 2 == 0 else 'ch.heart',
                'frequency': 'freq.963' if i % 2 == 0 else 'freq.639',
                'fractal_depth': i + 2,
                'self_similarity_score': 0.6 + (i * 0.1)
            }
        )
        consciousness_nodes.append(node)
    
    # Assess consciousness for each node
    consciousness_states = []
    for node in consciousness_nodes:
        state = consciousness_system.assess_node_consciousness(node)
        consciousness_states.append(state)
        assert state.level == node.consciousness_level, "Consciousness level should match"
        assert state.awareness_score > 0, "Awareness score should be positive"
    
    print(f"   ✅ Consciousness assessment: {len(consciousness_states)} nodes assessed")
    
    # Test 2: Meta-cognitive capability assessment
    print("\n   Test 2: Meta-cognitive capability assessment")
    
    for state in consciousness_states:
        assert state.meta_cognitive_capability >= 0, "Meta-cognitive capability should be non-negative"
        assert state.meta_cognitive_capability <= 1, "Meta-cognitive capability should be <= 1"
        
        # Higher consciousness levels should have higher meta-cognitive capability
        if state.level in ['meta_cognitive', 'transcendent']:
            assert state.meta_cognitive_capability > 0.5, f"High consciousness should have high meta-cognitive capability: {state.level}"
    
    print("   ✅ Meta-cognitive capability assessment passed")
    
    # Test 3: Transcendent potential calculation
    print("\n   Test 3: Transcendent potential calculation")
    
    for state in consciousness_states:
        assert state.transcendent_potential >= 0, "Transcendent potential should be non-negative"
        assert state.transcendent_potential <= 1, "Transcendent potential should be <= 1"
    
    print("   ✅ Transcendent potential calculation passed")
    
    # Test 4: Evolution trajectory determination
    print("\n   Test 4: Evolution trajectory determination")
    
    for state in consciousness_states:
        assert state.evolution_trajectory in ['ascending', 'stable', 'descending'], f"Invalid evolution trajectory: {state.evolution_trajectory}"
    
    print("   ✅ Evolution trajectory determination passed")
    
    # Test 5: Collective consciousness calculation
    print("\n   Test 5: Collective consciousness calculation")
    
    collective_consciousness = consciousness_system.calculate_collective_consciousness(
        consciousness_nodes, "consciousness_test_group"
    )
    
    assert collective_consciousness.group_id == "consciousness_test_group", "Group ID should match"
    assert collective_consciousness.member_count == len(consciousness_nodes), "Member count should match"
    assert collective_consciousness.collective_awareness > 0, "Collective awareness should be positive"
    
    print(f"   ✅ Collective consciousness: awareness {collective_consciousness.collective_awareness:.3f}")
    
    # Test 6: Consciousness statistics
    print("\n   Test 6: Consciousness statistics")
    
    stats = consciousness_system.get_consciousness_statistics()
    assert stats['consciousness_stats']['total_nodes_tracked'] > 0, "Should have tracked nodes"
    assert len(stats['consciousness_distribution']) > 0, "Should have consciousness distribution"
    
    print(f"   ✅ Consciousness statistics: {stats['consciousness_stats']['total_nodes_tracked']} nodes tracked")
    
    print("✅ Consciousness Level System tests passed!")

def test_quantum_state_system():
    """Test the quantum state system"""
    print("\n⚛️  Testing Quantum State System...")
    
    # Initialize quantum system
    quantum_system = QuantumStateSystem()
    
    # Test 1: Quantum state assessment
    print("\n   Test 1: Quantum state assessment")
    
    # Create test nodes with different quantum states
    quantum_nodes = []
    quantum_states = ['coherent', 'superposition', 'entangled', 'collapsed', 'decoherent']
    
    for i, state in enumerate(quantum_states):
        # Set specific metadata for decoherent state to ensure high decoherence rate
        if state == 'decoherent':
            custom_metadata = {
                'quantum_state': state,
                'water_state': 'ws.ice',
                'chakra': 'ch.crown',
                'frequency': 'freq.963',
                'fractal_depth': i + 1,
                'self_similarity_score': 0.5 + (i * 0.1),
                'vibrational_axes': ['Fear↔Trust'],
                'resonance_pattern': 'dissonant',
                'coherence_score': 0.2
            }
        else:
            custom_metadata = {
                'quantum_state': state,
                'water_state': 'ws.ice' if i % 2 == 0 else 'ws.liquid',
                'chakra': 'ch.crown' if i % 2 == 0 else 'ch.heart',
                'frequency': 'freq.963' if i % 2 == 0 else 'freq.639',
                'fractal_depth': i + 1,
                'self_similarity_score': 0.5 + (i * 0.1),
                'vibrational_axes': ['Fear↔Trust'] if i % 2 == 0 else ['Ownership↔Stewardship']
            }
        
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='quantum_test',
            name=f'Quantum Test Node {i}',
            content=f'Test content for quantum state {state}',
            custom_metadata=custom_metadata
        )
        quantum_nodes.append(node)
    
    # Assess quantum state for each node
    quantum_states_info = []
    for node in quantum_nodes:
        info = quantum_system.assess_node_quantum_state(node)
        quantum_states_info.append(info)
        assert info.current_state == node.quantum_state, "Quantum state should match"
        assert info.coherence_level >= 0, "Coherence level should be non-negative"
        assert info.coherence_level <= 1, "Coherence level should be <= 1"
    
    print(f"   ✅ Quantum state assessment: {len(quantum_states_info)} nodes assessed")
    
    # Test 2: Quantum coherence calculation
    print("\n   Test 2: Quantum coherence calculation")
    
    for info in quantum_states_info:
        assert info.coherence_level >= 0, "Coherence level should be non-negative"
        assert info.coherence_level <= 1, "Coherence level should be <= 1"
        
        # Coherent states should have high coherence
        if info.current_state == 'coherent':
            assert info.coherence_level > 0.7, "Coherent state should have high coherence"
    
    print("   ✅ Quantum coherence calculation passed")
    
    # Test 3: Entanglement strength calculation
    print("\n   Test 3: Entanglement strength calculation")
    
    for info in quantum_states_info:
        assert info.entanglement_strength >= 0, "Entanglement strength should be non-negative"
        assert info.entanglement_strength <= 1, "Entanglement strength should be <= 1"
        
        # Entangled states should have high entanglement strength
        if info.current_state == 'entangled':
            assert info.entanglement_strength > 0.5, "Entangled state should have high entanglement strength"
    
    print("   ✅ Entanglement strength calculation passed")
    
    # Test 4: Superposition factor calculation
    print("\n   Test 4: Superposition factor calculation")
    
    for info in quantum_states_info:
        assert info.superposition_factor >= 0, "Superposition factor should be non-negative"
        assert info.superposition_factor <= 1, "Superposition factor should be <= 1"
        
        # Superposition states should have high superposition factor
        if info.current_state == 'superposition':
            assert info.superposition_factor >= 0.6, "Superposition state should have high superposition factor"
    
    print("   ✅ Superposition factor calculation passed")
    
    # Test 5: Decoherence rate calculation
    print("\n   Test 5: Decoherence rate calculation")
    
    for info in quantum_states_info:
        assert info.decoherence_rate >= 0, "Decoherence rate should be non-negative"
        assert info.decoherence_rate <= 1, "Decoherence rate should be <= 1"
        
        # Decoherent states should have high decoherence rate
        if info.current_state == 'decoherent':
            assert info.decoherence_rate > 0.7, "Decoherent state should have high decoherence rate"
    
    print("   ✅ Decoherence rate calculation passed")
    
    # Test 6: Algorithmic entanglement detection
    print("\n   Test 6: Algorithmic entanglement detection")
    
    entanglements = quantum_system.detect_algorithmic_entanglements(quantum_nodes)
    assert len(entanglements) > 0, "Should detect some algorithmic entanglements"
    
    for ent in entanglements:
        assert ent.strength > 0.5, "Only significant entanglements should be detected"
        assert ent.entanglement_type in ['algorithmic', 'structural', 'resonance'], f"Invalid entanglement type: {ent.entanglement_type}"
    
    print(f"   ✅ Algorithmic entanglement detection: {len(entanglements)} entanglements detected")
    
    # Test 7: Quantum statistics
    print("\n   Test 7: Quantum statistics")
    
    stats = quantum_system.get_quantum_statistics()
    assert stats['quantum_stats']['total_nodes_tracked'] > 0, "Should have tracked nodes"
    assert len(stats['quantum_state_distribution']) > 0, "Should have quantum state distribution"
    
    print(f"   ✅ Quantum statistics: {stats['quantum_stats']['total_nodes_tracked']} nodes tracked")
    
    print("✅ Quantum State System tests passed!")

def test_integration_between_phase3_systems():
    """Test integration between all Phase 3 systems"""
    print("\n🔗 Testing Integration Between Phase 3 Systems...")
    
    # Initialize all Phase 3 systems
    resonance_system = AdvancedResonanceSystem()
    consciousness_system = ConsciousnessLevelSystem()
    quantum_system = QuantumStateSystem()
    
    # Test 1: Integrated node processing workflow
    print("\n   Test 1: Integrated node processing workflow")
    
    # Create a comprehensive test node
    integrated_node = EnhancedGenericNode.create_from_metadata_factory(
        node_type='integrated_test',
        name='Phase 3 Integration Test Node',
        content='Test node for Phase 3 system integration',
        custom_metadata={
            'water_state': 'ws.ice',
            'chakra': 'ch.crown',
            'frequency': 'freq.963',
            'consciousness_level': 'meta_cognitive',
            'quantum_state': 'coherent',
            'fractal_depth': 8,
            'self_similarity_score': 0.8,
            'vibrational_axes': ['Fear↔Trust', 'Ownership↔Stewardship']
        }
    )
    
    # Process through all systems
    resonance_result = resonance_system.calculate_node_resonance(integrated_node)
    consciousness_state = consciousness_system.assess_node_consciousness(integrated_node)
    quantum_info = quantum_system.assess_node_quantum_state(integrated_node)
    
    # Verify all systems processed the node
    assert resonance_result['overall_resonance_score'] > 0, "Resonance should be calculated"
    assert consciousness_state.awareness_score > 0, "Consciousness should be assessed"
    assert quantum_info.coherence_level > 0, "Quantum state should be assessed"
    
    print("   ✅ Integrated node processing workflow passed")
    
    # Test 2: Cross-system resonance and consciousness
    print("\n   Test 2: Cross-system resonance and consciousness")
    
    # Check if high resonance correlates with high consciousness
    if resonance_result['overall_resonance_score'] > 0.7:
        assert consciousness_state.awareness_score > 0.5, "High resonance should correlate with high consciousness"
    
    # Check if high consciousness correlates with high quantum coherence
    if consciousness_state.awareness_score > 0.7:
        assert quantum_info.coherence_level > 0.6, "High consciousness should correlate with high quantum coherence"
    
    print("   ✅ Cross-system resonance and consciousness correlation passed")
    
    # Test 3: Collective system processing
    print("\n   Test 3: Collective system processing")
    
    # Create multiple nodes for collective processing
    collective_nodes = [integrated_node]
    for i in range(3):
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='collective_test',
            name=f'Collective Test Node {i}',
            content=f'Collective test content {i}',
            custom_metadata={
                'water_state': 'ws.liquid',
                'chakra': 'ch.heart',
                'frequency': 'freq.639',
                'consciousness_level': 'self_aware',
                'quantum_state': 'superposition'
            }
        )
        collective_nodes.append(node)
    
    # Process through all systems collectively
    resonance_clusters = resonance_system.form_resonance_clusters(collective_nodes)
    collective_resonance = resonance_system.calculate_collective_resonance(collective_nodes, "collective_test", "system")
    collective_consciousness = consciousness_system.calculate_collective_consciousness(collective_nodes, "collective_test")
    
    # Verify collective processing
    assert len(resonance_clusters) > 0, "Should form resonance clusters"
    assert collective_resonance.member_count == len(collective_nodes), "Collective resonance should include all nodes"
    assert collective_consciousness.member_count == len(collective_nodes), "Collective consciousness should include all nodes"
    
    print("   ✅ Collective system processing passed")
    
    # Test 4: Cross-system statistics
    print("\n   Test 4: Cross-system statistics")
    
    resonance_stats = resonance_system.get_resonance_statistics()
    consciousness_stats = consciousness_system.get_consciousness_statistics()
    quantum_stats = quantum_system.get_quantum_statistics()
    
    # Verify all systems have statistics
    assert resonance_stats['resonance_stats']['total_calculations'] > 0, "Resonance system should have statistics"
    assert consciousness_stats['consciousness_stats']['total_nodes_tracked'] > 0, "Consciousness system should have statistics"
    assert quantum_stats['quantum_stats']['total_nodes_tracked'] > 0, "Quantum system should have statistics"
    
    print("   ✅ Cross-system statistics verification passed")
    
    print("✅ Phase 3 system integration tests passed!")

def test_advanced_features():
    """Test advanced features of the Phase 3 systems"""
    print("\n🚀 Testing Advanced Features...")
    
    # Initialize systems
    resonance_system = AdvancedResonanceSystem()
    consciousness_system = ConsciousnessLevelSystem()
    quantum_system = QuantumStateSystem()
    
    # Test 1: Resonance report export
    print("\n   Test 1: Resonance report export")
    
    resonance_report = resonance_system.export_resonance_report()
    assert 'resonance_system_info' in resonance_report, "Should have resonance system info"
    assert 'harmonic_relationships' in resonance_report, "Should have harmonic relationships"
    
    print("   ✅ Resonance report export passed")
    
    # Test 2: Consciousness report export
    print("\n   Test 2: Consciousness report export")
    
    consciousness_report = consciousness_system.export_consciousness_report()
    assert 'consciousness_system_info' in consciousness_report, "Should have consciousness system info"
    assert 'consciousness_states' in consciousness_report, "Should have consciousness states"
    
    print("   ✅ Consciousness report export passed")
    
    # Test 3: Quantum report export
    print("\n   Test 3: Quantum report export")
    
    quantum_report = quantum_system.export_quantum_report()
    assert 'quantum_system_info' in quantum_report, "Should have quantum system info"
    assert 'quantum_states' in quantum_report, "Should have quantum states"
    
    print("   ✅ Quantum report export passed")
    
    # Test 4: System optimization
    print("\n   Test 4: System optimization")
    
    # Clear caches
    resonance_system.clear_cache()
    quantum_system.clear_cache()
    
    print("   ✅ System optimization completed")
    
    print("✅ Advanced features tests passed!")

def test_performance_and_scalability():
    """Test performance and scalability aspects"""
    print("\n⚡ Testing Performance and Scalability...")
    
    # Initialize systems
    resonance_system = AdvancedResonanceSystem()
    consciousness_system = ConsciousnessLevelSystem()
    quantum_system = QuantumStateSystem()
    
    # Test 1: Large batch processing
    print("\n   Test 1: Large batch processing")
    
    # Create a larger batch of nodes
    large_batch = []
    start_time = time.time()
    
    for i in range(50):
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='performance_test',
            name=f'Performance Node {i}',
            content=f'Performance test content {i}',
            custom_metadata={
                'water_state': 'ws.ice' if i % 3 == 0 else 'ws.liquid' if i % 3 == 1 else 'ws.vapor',
                'chakra': 'ch.crown' if i % 3 == 0 else 'ch.heart' if i % 3 == 1 else 'ch.third_eye',
                'frequency': 'freq.963' if i % 3 == 0 else 'freq.639' if i % 3 == 1 else 'freq.852',
                'consciousness_level': 'awake' if i % 4 == 0 else 'sentient' if i % 4 == 1 else 'self_aware' if i % 4 == 2 else 'meta_cognitive',
                'quantum_state': 'coherent' if i % 3 == 0 else 'superposition' if i % 3 == 1 else 'entangled'
            }
        )
        large_batch.append(node)
    
    creation_time = time.time() - start_time
    print(f"   ⏱️  Created {len(large_batch)} nodes in {creation_time:.3f}s")
    
    # Process through resonance system
    start_time = time.time()
    for node in large_batch:
        resonance_system.calculate_node_resonance(node)
    resonance_time = time.time() - start_time
    
    print(f"   ⏱️  Resonance calculation: {len(large_batch)} nodes in {resonance_time:.3f}s")
    
    # Process through consciousness system
    start_time = time.time()
    for node in large_batch:
        consciousness_system.assess_node_consciousness(node)
    consciousness_time = time.time() - start_time
    
    print(f"   ⏱️  Consciousness assessment: {len(large_batch)} nodes in {consciousness_time:.3f}s")
    
    # Process through quantum system
    start_time = time.time()
    for node in large_batch:
        quantum_system.assess_node_quantum_state(node)
    quantum_time = time.time() - start_time
    
    print(f"   ⏱️  Quantum state assessment: {len(large_batch)} nodes in {quantum_time:.3f}s")
    
    # Test 2: Advanced operations
    print("\n   Test 2: Advanced operations")
    
    # Test harmonic relationship discovery
    start_time = time.time()
    relationships = resonance_system.discover_harmonic_relationships(large_batch)
    relationship_time = time.time() - start_time
    
    print(f"   ⏱️  Harmonic relationship discovery: {len(relationships)} relationships in {relationship_time:.3f}s")
    
    # Test resonance clustering
    start_time = time.time()
    clusters = resonance_system.form_resonance_clusters(large_batch)
    clustering_time = time.time() - start_time
    
    print(f"   ⏱️  Resonance clustering: {len(clusters)} clusters in {clustering_time:.3f}s")
    
    # Test algorithmic entanglement detection
    start_time = time.time()
    entanglements = quantum_system.detect_algorithmic_entanglements(large_batch)
    entanglement_time = time.time() - start_time
    
    print(f"   ⏱️  Algorithmic entanglement detection: {len(entanglements)} entanglements in {entanglement_time:.3f}s")
    
    print("   ✅ Performance and scalability tests completed")
    
    print("✅ Performance and scalability tests passed!")

def main():
    """Run all Phase 3 advanced systems tests"""
    print("🌟 Phase 3 Advanced Systems Test Suite")
    print("=" * 60)
    
    try:
        # Test advanced resonance system
        test_advanced_resonance_system()
        
        # Test consciousness level system
        test_consciousness_level_system()
        
        # Test quantum state system
        test_quantum_state_system()
        
        # Test integration between Phase 3 systems
        test_integration_between_phase3_systems()
        
        # Test advanced features
        test_advanced_features()
        
        # Test performance and scalability
        test_performance_and_scalability()
        
        print("\n" + "=" * 60)
        print("🎉 ALL PHASE 3 TESTS PASSED!")
        print("✅ Advanced Resonance System: Working")
        print("✅ Consciousness Level System: Working")
        print("✅ Quantum State System: Working")
        print("✅ System Integration: Working")
        print("✅ Advanced Features: Working")
        print("✅ Performance & Scalability: Working")
        print("\n🚀 Phase 3 Advanced Systems are ready for production!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
