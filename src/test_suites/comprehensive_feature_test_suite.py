#!/usr/bin/env python3
"""
Comprehensive Feature Test Suite
- Tests all features and functionality in the fractal holographic architecture
- Validates that each component has proper higher-level descriptions and structure
- Ensures fractal self-similarity across all levels of the stack
"""

import unittest
import json
from datetime import datetime
from web_platform.unified_web_interface import app
from core.core_system import fractal_core_system


class FractalArchitectureTestSuite(unittest.TestCase):
    """Test suite for validating fractal holographic architecture"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        self.core_system = fractal_core_system
        
    def test_system_status_endpoint(self):
        """Test that system status endpoint returns comprehensive information"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        required_fields = [
            'system_overview', 'system_health', 'fractal_components',
            'node_types', 'fractal_layers', 'water_states', 'chakras', 'frequencies'
        ]
        
        for field in required_fields:
            self.assertIn(field, data)
            
        # Validate system health is 100%
        health = data['system_health']
        self.assertEqual(health['self_similarity'], 100.0)
        self.assertEqual(health['meta_circularity'], 100.0)
        self.assertEqual(health['holographic_nature'], 100.0)


class FeatureCoverageTestSuite(unittest.TestCase):
    """Test suite for validating complete feature coverage"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        
    def test_all_feature_categories_exist(self):
        """Test that all expected feature categories are present"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        node_types = data.get('node_types', {})
        
        # Expected feature categories based on Living Codex specification
        expected_categories = [
            'ai', 'api', 'architecture', 'asset', 'bootstrap', 'cli', 'code',
            'consciousness', 'data', 'database', 'digital', 'discovery', 'doc',
            'documentation', 'external', 'federation', 'frequency', 'grammar',
            'graph', 'ice', 'implementation', 'integration', 'language', 'meta',
            'node', 'ontology', 'principle', 'profile', 'programming', 'quantum',
            'resonance', 'sacred', 'seed', 'storage', 'structure', 'system',
            'template', 'testing', 'user', 'water', 'web'
        ]
        
        # Extract actual categories from node types
        actual_categories = set()
        for node_type in node_types.keys():
            if '_' in node_type:
                category = node_type.split('_')[0]
                actual_categories.add(category)
            else:
                actual_categories.add(node_type)
        
        # Check that all expected categories exist
        for category in expected_categories:
            self.assertIn(category, actual_categories, f"Missing category: {category}")
            
    def test_all_fractal_components_registered(self):
        """Test that all fractal components are properly registered"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        components = data['fractal_components']
        
        # Expected fractal components (matching actual component names)
        expected_components = [
            'ontology_system', 'water_state_system', 'programming_language_system', 'database_system',
            'graph_system', 'api_system', 'ice_bootstrap_system', 'web_platform_system', 'ai_agent_system',
            'cli_system', 'testing_system', 'integration_system', 'water_state_storage_system',
            'database_persistence_system', 'code_reflection_system', 'template_reflection_system',
            'documentation_reflection_system', 'data_model_reflection_system',
            'meta_system_reflection_system', 'sacred_geometry_system', 'consciousness_system',
            'digital_asset_system', 'user_management_system', 'federation_system',
            'programming_language_ontology_system'
        ]
        
        for component in expected_components:
            self.assertIn(component, components, f"Missing component: {component}")
            
    def test_water_states_complete(self):
        """Test that all 12 water states are present"""
        response = self.app.get('/api/search', query_string={'q': 'water_state', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        water_state_count = data.get('total_count', 0)
        
        # Should have at least 12 water states + system nodes
        self.assertGreaterEqual(water_state_count, 12)
        
    def test_fractal_layers_complete(self):
        """Test that all fractal layers are represented"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        fractal_layers = data.get('fractal_layers', {})
        
        # Should have multiple fractal layers
        self.assertGreater(len(fractal_layers), 0)
        
    def test_chakra_frequency_mapping(self):
        """Test that chakra-frequency mappings are complete"""
        response = self.app.get('/api/search', query_string={'q': 'frequency_mapping', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        frequency_count = data.get('total_count', 0)
        
        # Should have 7 frequency mappings (396Hz to 963Hz)
        self.assertGreaterEqual(frequency_count, 7)


class FractalSelfSimilarityTestSuite(unittest.TestCase):
    """Test suite for validating fractal self-similarity across all levels"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        
    def test_component_structure_consistency(self):
        """Test that all components have consistent fractal structure"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        components = data['fractal_components']
        
        # Test that each component has proper fractal metadata
        for component in components:
            # Search for the component system
            search_response = self.app.get('/api/search', 
                                         query_string={'q': component, 'type': 'all'})
            self.assertEqual(search_response.status_code, 200)
            
            search_data = search_response.get_json()
            results = search_data.get('results', [])
            
            # Should find at least one result for each component
            self.assertGreater(len(results), 0)
            
    def test_fractal_layer_consistency(self):
        """Test that fractal layers are consistent across components"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        fractal_layers = data.get('fractal_layers', {})
        
        # Each fractal layer should have consistent properties
        for layer_info in fractal_layers.values():
            if isinstance(layer_info, dict):
                # Should have fractal properties
                self.assertIn('water_states', layer_info)  # Fixed: water_states (plural)
                self.assertIn('frequencies', layer_info)   # Fixed: frequencies (plural)
                self.assertIn('chakras', layer_info)       # Fixed: chakras (plural)
                
    def test_water_state_consistency(self):
        """Test that water states are consistent across the system"""
        response = self.app.get('/api/search', query_string={'q': 'ice', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        results = data.get('results', [])
        
        # Should find ice-related nodes
        self.assertGreater(len(results), 0)
        
        # Check that ice nodes have consistent fractal properties
        for result in results[:3]:  # Check first 3 results
            metadata = result.get('metadata', {})
            if 'water_state' in metadata:
                self.assertEqual(metadata['water_state'], 'ice')


class FeatureFunctionalityTestSuite(unittest.TestCase):
    """Test suite for validating feature functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        
    def test_search_functionality(self):
        """Test that search functionality works across all node types"""
        # Test search for different feature types
        search_queries = [
            'sacred_geometry', 'consciousness_level', 'quantum_state',
            'asset_type', 'profile_component', 'federation_system',
            'resonance_pattern', 'language_layer', 'programming_language'
        ]
        
        for query in search_queries:
            response = self.app.get('/api/search', 
                                  query_string={'q': query, 'type': 'all'})
            self.assertEqual(response.status_code, 200)
            
            data = response.get_json()
            # Should return some results
            self.assertGreater(data.get('total_count', 0), 0)
            
    def test_fractal_component_functionality(self):
        """Test that fractal components are functional"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        components = data['fractal_components']
        
        # Test that each component can be searched
        for component in components:
            search_response = self.app.get('/api/search', 
                                         query_string={'q': component, 'type': 'all'})
            self.assertEqual(search_response.status_code, 200)
            
    def test_node_type_functionality(self):
        """Test that all node types are functional and searchable"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        node_types = data.get('node_types', {})
        
        # Test a sample of node types
        sample_types = list(node_types.keys())[:10]  # Test first 10
        
        for node_type in sample_types:
            search_response = self.app.get('/api/search', 
                                         query_string={'q': node_type, 'type': 'all'})
            self.assertEqual(search_response.status_code, 200)
            
            search_data = search_response.get_json()
            # Should return some results
            self.assertGreater(search_data.get('total_count', 0), 0)


class HigherLevelStructureTestSuite(unittest.TestCase):
    """Test suite for validating higher-level structure components"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        
    def test_meta_system_structure(self):
        """Test that meta-system has proper higher-level structure"""
        response = self.app.get('/api/search', 
                               query_string={'q': 'meta_architecture', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        results = data.get('results', [])
        
        # Should find meta-architecture nodes
        self.assertGreater(len(results), 0)
        
        # Check that meta nodes have proper structure
        for result in results:
            metadata = result.get('metadata', {})
            self.assertIn('fractal_layer', metadata)
            self.assertIn('water_state', metadata)
            self.assertIn('chakra', metadata)
            
    def test_system_definition_structure(self):
        """Test that system definitions have proper higher-level structure"""
        response = self.app.get('/api/search', 
                               query_string={'q': 'system_definition', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        results = data.get('results', [])
        
        # Should find system definition nodes
        self.assertGreater(len(results), 0)
        
        # Check that system definition nodes have proper structure
        for result in results:
            metadata = result.get('metadata', {})
            self.assertIn('fractal_layer', metadata)
            self.assertIn('water_state', metadata)
            
    def test_implementation_pattern_structure(self):
        """Test that implementation patterns have proper higher-level structure"""
        response = self.app.get('/api/search', 
                               query_string={'q': 'implementation_pattern', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        results = data.get('results', [])
        
        # Should find implementation pattern nodes
        self.assertGreater(len(results), 0)
        
        # Check that implementation pattern nodes have proper structure
        for result in results:
            metadata = result.get('metadata', {})
            self.assertIn('fractal_layer', metadata)
            self.assertIn('water_state', metadata)


class FractalHolographicArchitectureTestSuite(unittest.TestCase):
    """Test suite for validating fractal holographic architecture principles"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        
    def test_everything_is_nodes_principle(self):
        """Test that everything in the system is represented as nodes"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        
        # Everything should be countable as nodes
        self.assertGreater(data['system_overview']['total_nodes'], 0)
        self.assertGreater(data['system_overview']['node_types_count'], 0)
        
    def test_fractal_self_similarity_principle(self):
        """Test that fractal self-similarity is maintained across all levels"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        
        # System health should show 100% self-similarity
        health = data['system_health']
        self.assertEqual(health['self_similarity'], 100.0)
        
    def test_meta_circularity_principle(self):
        """Test that meta-circularity is maintained"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        
        # System health should show 100% meta-circularity
        health = data['system_health']
        self.assertEqual(health['meta_circularity'], 100.0)
        
    def test_holographic_nature_principle(self):
        """Test that holographic nature is maintained"""
        response = self.app.get('/api/system/status')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        
        # System health should show 100% holographic nature
        health = data['system_health']
        self.assertEqual(health['holographic_nature'], 100.0)
        
    def test_structure_as_content_principle(self):
        """Test that structure itself is represented as content"""
        # Search for structure-related nodes
        response = self.app.get('/api/search', 
                               query_string={'q': 'structure', 'type': 'all'})
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        results = data.get('results', [])
        
        # Should find structure nodes
        self.assertGreater(len(results), 0)
        
        # Check that structure nodes have proper content
        for result in results:
            self.assertIn('content', result)
            self.assertIn('metadata', result)
            # Check that metadata contains fractal structure information
            metadata = result.get('metadata', {})
            self.assertIn('fractal_layer', metadata)
            self.assertIn('water_state', metadata)


def run_comprehensive_test_suite():
    """Run the comprehensive test suite"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        FractalArchitectureTestSuite,
        FeatureCoverageTestSuite,
        FractalSelfSimilarityTestSuite,
        FeatureFunctionalityTestSuite,
        HigherLevelStructureTestSuite,
        FractalHolographicArchitectureTestSuite
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*60}")
    print("COMPREHENSIVE TEST SUITE RESULTS")
    print(f"{'='*60}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
            
    if result.errors:
        print(f"\nERRORS:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    return result


if __name__ == '__main__':
    run_comprehensive_test_suite()
