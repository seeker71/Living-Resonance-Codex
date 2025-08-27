#!/usr/bin/env python3
"""
Phase 2 Metadata System Test Suite
==================================

This script tests the complete Phase 2 metadata enhancement system including:
- Ontological Validation System
- Enhanced Indexing System
- Integration between validation and indexing
- Advanced query capabilities
- Cross-dimensional validation

This validates Phase 2 of the metadata enhancement plan.
"""

import sys
import json
import time
from datetime import datetime

# Import our Phase 2 metadata system components
from living_codex_ontology import (
    canonical_registry, WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel
)

from metadata_factory import metadata_factory
from enhanced_generic_node import EnhancedGenericNode
from ontological_validation_system import (
    OntologicalValidationSystem, ValidationResult
)
from enhanced_indexing_system import (
    EnhancedIndexingSystem, IndexEntry, IndexQuery, IndexQueryResult
)

def test_ontological_validation_system():
    """Test the ontological validation system"""
    print("🔍 Testing Ontological Validation System...")
    
    # Initialize validation system
    validation_system = OntologicalValidationSystem()
    
    # Test 1: Valid metadata validation
    print("\n   Test 1: Valid metadata validation")
    valid_metadata = {
        'water_state': 'ws.ice',
        'chakra': 'ch.crown',
        'frequency': 'freq.963',
        'fractal_layer': 0,
        'consciousness_level': 'awake',
        'quantum_state': 'coherent',
        'resonance_pattern': 'harmonic',
        'epistemic_label': 'engineering',
        'fractal_depth': 0,
        'cross_scale_mapping': {'micro': 'system_design', 'meso': 'architecture', 'macro': 'ecosystem', 'meta': 'principles'},
        'coherence_score': 1.0,
        'dissonance_level': 0.0,
        'vibrational_axes': ['Fear↔Trust']
    }
    
    result = validation_system.validate_ontological_signature(valid_metadata)
    assert result.is_valid, f"Valid metadata should pass validation: {result.errors}"
    print(f"   ✅ Valid metadata validation passed")
    
    # Test 2: Invalid canonical keys
    print("\n   Test 2: Invalid canonical keys validation")
    invalid_metadata = valid_metadata.copy()
    invalid_metadata['water_state'] = 'invalid_water_state'
    
    result = validation_system.validate_ontological_signature(invalid_metadata)
    assert not result.is_valid, "Invalid canonical keys should fail validation"
    assert any('Invalid water_state' in error for error in result.errors), "Should have water state error"
    print(f"   ✅ Invalid canonical keys validation passed")
    
    # Test 3: Epistemic consistency validation
    print("\n   Test 3: Epistemic consistency validation")
    epistemic_metadata = valid_metadata.copy()
    epistemic_metadata['epistemic_label'] = 'tradition'
    
    result = validation_system.validate_epistemic_consistency(epistemic_metadata)
    assert result.is_valid, f"Epistemic consistency should pass: {result.errors}"
    print(f"   ✅ Epistemic consistency validation passed")
    
    # Test 4: Template validation
    print("\n   Test 4: Template validation")
    result = validation_system.validate_against_template(valid_metadata, 'ice_theme')
    assert result.is_valid, f"Template validation should pass: {result.errors}"
    print(f"   ✅ Template validation passed")
    
    # Test 5: Cross-dimensional consistency
    print("\n   Test 5: Cross-dimensional consistency validation")
    result = validation_system.validate_ontological_signature(valid_metadata)
    assert result.is_valid, f"Cross-dimensional validation should pass: {result.errors}"
    print(f"   ✅ Cross-dimensional consistency validation passed")
    
    # Test validation statistics
    stats = validation_system.get_validation_statistics()
    assert stats['total_validations'] > 0, "Should have validation history"
    print(f"   ✅ Validation statistics: {stats['total_validations']} validations")
    
    print("✅ Ontological Validation System tests passed!")

def test_enhanced_indexing_system():
    """Test the enhanced indexing system"""
    print("\n🔍 Testing Enhanced Indexing System...")
    
    # Initialize indexing system
    indexing_system = EnhancedIndexingSystem()
    
    # Test 1: Node indexing
    print("\n   Test 1: Node indexing")
    
    # Create test nodes
    test_nodes = []
    for i in range(5):
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='system_component',
            name=f'Test Node {i}',
            content=f'Test content for node {i}',
            custom_metadata={
                'water_state': 'ws.ice' if i % 2 == 0 else 'ws.liquid',
                'chakra': 'ch.crown' if i % 2 == 0 else 'ch.heart',
                'frequency': 'freq.963' if i % 2 == 0 else 'freq.639'
            }
        )
        test_nodes.append(node)
    
    # Index nodes
    indexing_result = indexing_system.index_node_batch(test_nodes)
    assert indexing_result['successful'] == 5, f"All nodes should be indexed: {indexing_result}"
    assert indexing_system.total_indexed_nodes == 5, "Total indexed nodes should be 5"
    print(f"   ✅ Node indexing: {indexing_result['successful']} nodes indexed")
    
    # Test 2: Exact query
    print("\n   Test 2: Exact query")
    query = IndexQuery(
        query_type="exact",
        field="water_state",
        value="ws.ice"
    )
    
    result = indexing_system.query_index(query)
    assert result.total_count > 0, "Should find nodes with ws.ice water state"
    assert all(entry.metadata['water_state'] == 'ws.ice' for entry in result.results), "All results should have ws.ice"
    print(f"   ✅ Exact query: {result.total_count} results found")
    
    # Test 3: Range query
    print("\n   Test 3: Range query")
    query = IndexQuery(
        query_type="range",
        field="fractal_layer",
        value=0,
        operator="gte"
    )
    
    result = indexing_system.query_index(query)
    assert result.total_count > 0, "Should find nodes with fractal layer >= 0"
    print(f"   ✅ Range query: {result.total_count} results found")
    
    # Test 4: Composite query
    print("\n   Test 4: Composite query")
    query = IndexQuery(
        query_type="composite",
        field="water_state",
        value="ws.ice",
        secondary_field="chakra",
        secondary_value="ch.crown"
    )
    
    result = indexing_system.query_index(query)
    assert result.total_count > 0, "Should find nodes matching both criteria"
    print(f"   ✅ Composite query: {result.total_count} results found")
    
    # Test 5: Theme-based search
    print("\n   Test 5: Theme-based search")
    ice_theme_nodes = indexing_system.find_nodes_by_theme('ice')
    assert len(ice_theme_nodes) > 0, "Should find ice theme nodes"
    print(f"   ✅ Theme search: {len(ice_theme_nodes)} ice theme nodes found")
    
    # Test 6: Resonance pattern search
    print("\n   Test 6: Resonance pattern search")
    harmonic_nodes = indexing_system.find_nodes_by_resonance_pattern('harmonic', min_coherence=0.8)
    assert len(harmonic_nodes) > 0, "Should find harmonic nodes with high coherence"
    print(f"   ✅ Resonance search: {len(harmonic_nodes)} harmonic nodes found")
    
    # Test 7: Fractal depth range search
    print("\n   Test 7: Fractal depth range search")
    depth_nodes = indexing_system.find_nodes_by_fractal_depth_range(0, 1)
    assert len(depth_nodes) > 0, "Should find nodes in fractal depth range"
    print(f"   ✅ Fractal depth search: {len(depth_nodes)} nodes found")
    
    # Test 8: Epistemic alignment search
    print("\n   Test 8: Epistemic alignment search")
    engineering_nodes = indexing_system.find_nodes_by_epistemic_alignment('engineering')
    assert len(engineering_nodes) > 0, "Should find engineering nodes"
    print(f"   ✅ Epistemic search: {len(engineering_nodes)} engineering nodes found")
    
    # Test index statistics
    stats = indexing_system.get_index_statistics()
    assert stats['index_system_info']['total_indexed_nodes'] == 5, "Should have 5 indexed nodes"
    print(f"   ✅ Index statistics: {stats['index_system_info']['total_indexed_nodes']} nodes indexed")
    
    print("✅ Enhanced Indexing System tests passed!")

def test_integration_between_systems():
    """Test integration between validation and indexing systems"""
    print("\n🔗 Testing Integration Between Systems...")
    
    # Initialize both systems
    validation_system = OntologicalValidationSystem()
    indexing_system = EnhancedIndexingSystem()
    
    # Test 1: Validate then index workflow
    print("\n   Test 1: Validate then index workflow")
    
    # Create a node
    node = EnhancedGenericNode.create_from_metadata_factory(
        node_type='ai_agent',
        name='Integration Test Agent',
        content='Test agent for integration testing',
        custom_metadata={
            'water_state': 'ws.plasma',
            'chakra': 'ch.third_eye',
            'frequency': 'freq.852'
        }
    )
    
    # Validate the node's metadata
    metadata = {
        'water_state': node.water_state,
        'chakra': node.chakra,
        'frequency': node.frequency,
        'fractal_layer': node.fractal_layer,
        'consciousness_level': node.consciousness_level,
        'quantum_state': node.quantum_state,
        'resonance_pattern': node.resonance_pattern,
        'epistemic_label': node.epistemic_label,
        'programming_ontology_layer': node.programming_ontology_layer,
        'fractal_depth': node.fractal_depth,
        'cross_scale_mapping': node.cross_scale_mapping,
        'coherence_score': node.coherence_score,
        'dissonance_level': node.dissonance_level,
        'vibrational_axes': node.vibrational_axes
    }
    
    validation_result = validation_system.validate_ontological_signature(metadata)
    assert validation_result.is_valid, f"Node should pass validation: {validation_result.errors}"
    
    # Index the validated node
    indexing_success = indexing_system.index_node(node)
    assert indexing_success, "Validated node should be indexed successfully"
    
    # Query for the indexed node
    query = IndexQuery(
        query_type="exact",
        field="water_state",
        value="ws.plasma"
    )
    
    query_result = indexing_system.query_index(query)
    assert query_result.total_count > 0, "Should find the indexed node"
    assert any(entry.node_id == node.node_id for entry in query_result.results), "Should find our specific node"
    
    print("   ✅ Validate then index workflow passed")
    
    # Test 2: Batch validation and indexing
    print("\n   Test 2: Batch validation and indexing")
    
    # Create multiple nodes
    batch_nodes = []
    for i in range(3):
        batch_node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='data_node',
            name=f'Batch Node {i}',
            content=f'Batch content {i}',
            custom_metadata={
                'water_state': 'ws.liquid',
                'chakra': 'ch.heart',
                'frequency': 'freq.639'
            }
        )
        batch_nodes.append(batch_node)
    
    # Validate all nodes
    validation_results = []
    for batch_node in batch_nodes:
        batch_metadata = {
            'water_state': batch_node.water_state,
            'chakra': batch_node.chakra,
            'frequency': batch_node.frequency,
            'fractal_layer': batch_node.fractal_layer,
            'consciousness_level': batch_node.consciousness_level,
            'quantum_state': batch_node.quantum_state,
            'resonance_pattern': batch_node.resonance_pattern,
            'epistemic_label': batch_node.epistemic_label,
            'programming_ontology_layer': batch_node.programming_ontology_layer,
            'fractal_depth': batch_node.fractal_depth,
            'cross_scale_mapping': batch_node.cross_scale_mapping,
            'coherence_score': batch_node.coherence_score,
            'dissonance_level': batch_node.dissonance_level,
            'vibrational_axes': batch_node.vibrational_axes
        }
        
        batch_result = validation_system.validate_ontological_signature(batch_metadata)
        validation_results.append(batch_result)
    
    # All should be valid
    assert all(result.is_valid for result in validation_results), "All batch nodes should be valid"
    
    # Index all nodes
    batch_indexing_result = indexing_system.index_node_batch(batch_nodes)
    assert batch_indexing_result['successful'] == 3, "All batch nodes should be indexed"
    
    # Query for batch nodes
    batch_query = IndexQuery(
        query_type="exact",
        field="water_state",
        value="ws.liquid"
    )
    
    batch_query_result = indexing_system.query_index(batch_query)
    assert batch_query_result.total_count >= 3, "Should find all batch nodes"
    
    print("   ✅ Batch validation and indexing passed")
    
    # Test 3: Cross-system statistics
    print("\n   Test 3: Cross-system statistics")
    
    validation_stats = validation_system.get_validation_statistics()
    indexing_stats = indexing_system.get_index_statistics()
    
    assert validation_stats['total_validations'] > 0, "Should have validation history"
    assert indexing_stats['index_system_info']['total_indexed_nodes'] > 0, "Should have indexed nodes"
    
    print(f"   ✅ Cross-system statistics: {validation_stats['total_validations']} validations, {indexing_stats['index_system_info']['total_indexed_nodes']} indexed nodes")
    
    print("✅ Integration tests passed!")

def test_advanced_features():
    """Test advanced features of the metadata system"""
    print("\n🚀 Testing Advanced Features...")
    
    # Initialize systems
    validation_system = OntologicalValidationSystem()
    indexing_system = EnhancedIndexingSystem()
    
    # Test 1: Custom validation rules
    print("\n   Test 1: Custom validation rules")
    
    custom_rule = {
        'custom_field': 'custom_value',
        'custom_constraint': 'must_be_present'
    }
    
    validation_system.add_custom_validation_rule('custom_rules', custom_rule)
    print("   ✅ Custom validation rules added")
    
    # Test 2: Index optimization
    print("\n   Test 2: Index optimization")
    
    optimization_result = indexing_system.optimize_indexes()
    assert 'optimization_timestamp' in optimization_result, "Should have optimization timestamp"
    print("   ✅ Index optimization completed")
    
    # Test 3: Validation report export
    print("\n   Test 3: Validation report export")
    
    validation_report = validation_system.export_validation_report()
    assert 'validation_system_info' in validation_report, "Should have validation system info"
    print("   ✅ Validation report exported")
    
    # Test 4: Index data export
    print("\n   Test 4: Index data export")
    
    index_data = indexing_system.export_index_data()
    assert 'index_system_info' in index_data, "Should have index system info"
    print("   ✅ Index data exported")
    
    # Test 5: Query caching
    print("\n   Test 5: Query caching")
    
    # First query (cache miss)
    query = IndexQuery(
        query_type="exact",
        field="water_state",
        value="ws.ice"
    )
    
    first_result = indexing_system.query_index(query)
    
    # Second query (should be cache hit)
    second_result = indexing_system.query_index(query)
    
    # Both should have same results
    assert first_result.total_count == second_result.total_count, "Cached results should match"
    
    # Check cache statistics
    stats = indexing_system.get_index_statistics()
    assert stats['query_statistics']['cache_hits'] > 0, "Should have cache hits"
    
    print("   ✅ Query caching working")
    
    print("✅ Advanced features tests passed!")

def test_performance_and_scalability():
    """Test performance and scalability aspects"""
    print("\n⚡ Testing Performance and Scalability...")
    
    # Initialize systems
    validation_system = OntologicalValidationSystem()
    indexing_system = EnhancedIndexingSystem()
    
    # Test 1: Large batch processing
    print("\n   Test 1: Large batch processing")
    
    # Create a larger batch of nodes
    large_batch = []
    start_time = time.time()
    
    for i in range(50):
        node = EnhancedGenericNode.create_from_metadata_factory(
            node_type='system_component',
            name=f'Performance Node {i}',
            content=f'Performance test content {i}',
            custom_metadata={
                'water_state': 'ws.ice' if i % 3 == 0 else 'ws.liquid' if i % 3 == 1 else 'ws.vapor',
                'chakra': 'ch.crown' if i % 3 == 0 else 'ch.heart' if i % 3 == 1 else 'ch.third_eye',
                'frequency': 'freq.963' if i % 3 == 0 else 'freq.639' if i % 3 == 1 else 'freq.852'
            }
        )
        large_batch.append(node)
    
    creation_time = time.time() - start_time
    print(f"   ⏱️  Created {len(large_batch)} nodes in {creation_time:.3f}s")
    
    # Index large batch
    start_time = time.time()
    indexing_result = indexing_system.index_node_batch(large_batch)
    indexing_time = time.time() - start_time
    
    assert indexing_result['successful'] == 50, "All nodes should be indexed"
    print(f"   ⏱️  Indexed {len(large_batch)} nodes in {indexing_time:.3f}s")
    
    # Test 2: Query performance
    print("\n   Test 2: Query performance")
    
    # Test different query types
    query_types = [
        ("exact", "water_state", "ws.ice"),
        ("range", "fractal_layer", 0, "gte"),
        ("composite", "water_state", "ws.ice", "chakra", "ch.crown")
    ]
    
    for query_type, field, value, *extra in query_types:
        start_time = time.time()
        
        if query_type == "exact":
            query = IndexQuery(query_type=query_type, field=field, value=value)
        elif query_type == "range":
            query = IndexQuery(query_type=query_type, field=field, value=value, operator=extra[0])
        elif query_type == "composite":
            query = IndexQuery(
                query_type=query_type, 
                field=field, 
                value=value, 
                secondary_field=extra[0], 
                secondary_value=extra[1]
            )
        
        result = indexing_system.query_index(query)
        query_time = time.time() - start_time
        
        print(f"   ⏱️  {query_type} query: {result.total_count} results in {query_time:.3f}s")
    
    # Test 3: Memory usage and cleanup
    print("\n   Test 3: Memory usage and cleanup")
    
    # Clear validation history
    validation_system.clear_validation_history()
    
    # Rebuild indexes
    rebuild_result = indexing_system.rebuild_indexes()
    assert rebuild_result['rebuild_completed'], "Indexes should be rebuilt"
    
    print("   ✅ Memory cleanup completed")
    
    print("✅ Performance and scalability tests passed!")

def main():
    """Run all Phase 2 metadata system tests"""
    print("🌟 Phase 2 Metadata Enhancement System Test Suite")
    print("=" * 60)
    
    try:
        # Test ontological validation system
        test_ontological_validation_system()
        
        # Test enhanced indexing system
        test_enhanced_indexing_system()
        
        # Test integration between systems
        test_integration_between_systems()
        
        # Test advanced features
        test_advanced_features()
        
        # Test performance and scalability
        test_performance_and_scalability()
        
        print("\n" + "=" * 60)
        print("🎉 ALL PHASE 2 TESTS PASSED!")
        print("✅ Ontological Validation System: Working")
        print("✅ Enhanced Indexing System: Working")
        print("✅ System Integration: Working")
        print("✅ Advanced Features: Working")
        print("✅ Performance & Scalability: Working")
        print("\n🚀 Phase 2 Metadata Enhancement System is ready for production!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
