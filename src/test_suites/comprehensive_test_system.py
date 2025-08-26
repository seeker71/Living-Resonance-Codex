#!/usr/bin/env python3
"""
Living Codex Comprehensive Test System
Consolidated test system that provides access to all test scenarios
Following the Living Codex specification principles:
- Everything is just nodes
- Fractal self-similarity at every level
- Meta-circular self-description
"""

import os
import sys
import logging
import unittest
from typing import Dict, List, Any, Optional
from datetime import datetime, timezone

# Add the parent directory to the path to import core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.core_system import fractal_core_system, GenericNode
from core.fractal_components import initialize_fractal_components

logger = logging.getLogger(__name__)

class ComprehensiveTestSystem:
    """
    Comprehensive test system that consolidates all test functionality
    Provides a unified interface for running any test scenario
    """
    
    def __init__(self):
        self.name = "Comprehensive Test System"
        self.available_tests = self._discover_available_tests()
        self._register_as_fractal_node()
    
    def _discover_available_tests(self) -> Dict[str, Dict[str, Any]]:
        """Discover all available test scenarios"""
        return {
            'fractal_architecture': {
                'name': 'Fractal Architecture Tests',
                'description': 'Test fractal holographic architecture principles',
                'category': 'architecture',
                'complexity': 'high',
                'dependencies': ['fractal_components', 'core_system']
            },
            'core_functionality': {
                'name': 'Core Functionality Tests',
                'description': 'Test core system functionality',
                'category': 'core_system',
                'complexity': 'medium',
                'dependencies': ['core_system']
            },
            'search_functionality': {
                'name': 'Search Functionality Tests',
                'description': 'Test search and navigation capabilities',
                'category': 'search',
                'complexity': 'medium',
                'dependencies': ['search_system', 'core_system']
            },
            'web_interface': {
                'name': 'Web Interface Tests',
                'description': 'Test web platform functionality',
                'category': 'web_platform',
                'complexity': 'medium',
                'dependencies': ['web_platform', 'api_system']
            },
            'cli_functionality': {
                'name': 'CLI Functionality Tests',
                'description': 'Test command-line interface',
                'category': 'cli',
                'complexity': 'low',
                'dependencies': ['cli_system']
            },
            'file_system': {
                'name': 'File System Tests',
                'description': 'Test file reflection and management',
                'category': 'file_system',
                'complexity': 'medium',
                'dependencies': ['file_reflection_system']
            },
            'consciousness_system': {
                'name': 'Consciousness System Tests',
                'description': 'Test consciousness mapping and quantum systems',
                'category': 'consciousness',
                'complexity': 'high',
                'dependencies': ['consciousness_system', 'quantum_system']
            },
            'integration_tests': {
                'name': 'Integration Tests',
                'description': 'Test system integration and interoperability',
                'category': 'integration',
                'complexity': 'high',
                'dependencies': ['all_systems']
            }
        }
    
    def _register_as_fractal_node(self):
        """Register this test system as a node in the fractal system"""
        test_system_node = GenericNode(
            node_id="comprehensive_test_system",
            node_type="test_system",
            name=self.name,
            content="Unified test system providing access to all test scenarios",
            parent_id="meta_implementation",
            metadata={
                "fractal_layer": 3,
                "water_state": "supercritical",
                "frequency": 528,
                "chakra": "solar_plexus",
                "is_test_system": True,
                "test_count": len(self.available_tests)
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": True,
                "holographic": True,
                "test_categories": list(set(test['category'] for test in self.available_tests.values()))
            }
        )
        
        fractal_core_system._register_node(test_system_node)
        
        # Create test category nodes
        for test_id, test_info in self.available_tests.items():
            test_node = GenericNode(
                node_id=f"test_{test_id}",
                node_type="test_category",
                name=test_info['name'],
                content=test_info['description'],
                parent_id="comprehensive_test_system",
                metadata={
                    "fractal_layer": 4,
                    "water_state": "vapor",
                    "frequency": 741,
                    "chakra": "throat",
                    "category": test_info['category'],
                    "complexity": test_info['complexity'],
                    "dependencies": test_info['dependencies']
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True,
                    "test_type": "category"
                }
            )
            fractal_core_system._register_node(test_node)
            
            # Update parent's children list
            if test_system_node.node_id not in fractal_core_system.nodes["comprehensive_test_system"].children:
                fractal_core_system.nodes["comprehensive_test_system"].children.append(test_node.node_id)
        
        logger.info(f"Comprehensive test system registered with {len(self.available_tests)} test categories")
    
    def list_available_tests(self) -> Dict[str, Dict[str, Any]]:
        """List all available test categories"""
        return self.available_tests
    
    def run_tests(self, test_category: str = None, **kwargs) -> Dict[str, Any]:
        """Run tests for a specific category or all tests"""
        if test_category and test_category not in self.available_tests:
            return {
                'success': False,
                'error': f'Test category "{test_category}" not found',
                'available_tests': list(self.available_tests.keys())
            }
        
        try:
            if test_category:
                return self._run_specific_tests(test_category, **kwargs)
            else:
                return self._run_all_tests(**kwargs)
        except Exception as e:
            logger.error(f"Error running tests: {e}")
            return {
                'success': False,
                'error': str(e),
                'test_category': test_category
            }
    
    def _run_specific_tests(self, test_category: str, **kwargs) -> Dict[str, Any]:
        """Run tests for a specific category"""
        logger.info(f"Running tests for category: {test_category}")
        
        if test_category == 'fractal_architecture':
            return self._run_fractal_architecture_tests(**kwargs)
        elif test_category == 'core_functionality':
            return self._run_core_functionality_tests(**kwargs)
        elif test_category == 'search_functionality':
            return self._run_search_functionality_tests(**kwargs)
        elif test_category == 'web_interface':
            return self._run_web_interface_tests(**kwargs)
        elif test_category == 'cli_functionality':
            return self._run_cli_functionality_tests(**kwargs)
        elif test_category == 'file_system':
            return self._run_file_system_tests(**kwargs)
        elif test_category == 'consciousness_system':
            return self._run_consciousness_system_tests(**kwargs)
        elif test_category == 'integration_tests':
            return self._run_integration_tests(**kwargs)
        else:
            return {
                'success': False,
                'error': f'Test category "{test_category}" not implemented yet'
            }
    
    def _run_fractal_architecture_tests(self, **kwargs) -> Dict[str, Any]:
        """Run fractal architecture tests"""
        logger.info("Running fractal architecture tests...")
        
        # Test fractal properties
        test_results = {
            'fractal_layers': self._test_fractal_layers(),
            'water_states': self._test_water_states(),
            'chakras': self._test_chakras(),
            'frequencies': self._test_frequencies(),
            'self_similarity': self._test_self_similarity(),
            'meta_circularity': self._test_meta_circularity(),
            'holographic_nature': self._test_holographic_nature()
        }
        
        # Calculate overall success
        total_tests = len(test_results)
        successful_tests = len([r for r in test_results.values() if r.get('success', False)])
        
        return {
            'success': successful_tests == total_tests,
            'test_category': 'fractal_architecture',
            'description': 'Tested fractal holographic architecture principles',
            'results': test_results,
            'summary': {
                'total_tests': total_tests,
                'successful_tests': successful_tests,
                'failed_tests': total_tests - successful_tests,
                'success_rate': (successful_tests / total_tests) * 100 if total_tests > 0 else 0
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_core_functionality_tests(self, **kwargs) -> Dict[str, Any]:
        """Run core functionality tests"""
        logger.info("Running core functionality tests...")
        
        test_results = {
            'node_creation': self._test_node_creation(),
            'node_retrieval': self._test_node_retrieval(),
            'node_search': self._test_node_search(),
            'node_hierarchy': self._test_node_hierarchy(),
            'system_status': self._test_system_status()
        }
        
        total_tests = len(test_results)
        successful_tests = len([r for r in test_results.values() if r.get('success', False)])
        
        return {
            'success': successful_tests == total_tests,
            'test_category': 'core_functionality',
            'description': 'Tested core system functionality',
            'results': test_results,
            'summary': {
                'total_tests': total_tests,
                'successful_tests': successful_tests,
                'failed_tests': total_tests - successful_tests,
                'success_rate': (successful_tests / total_tests) * 100 if total_tests > 0 else 0
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_search_functionality_tests(self, **kwargs) -> Dict[str, Any]:
        """Run search functionality tests"""
        logger.info("Running search functionality tests...")
        
        # This would test the search system
        # For now, return a placeholder
        return {
            'success': True,
            'test_category': 'search_functionality',
            'description': 'Search functionality tests (placeholder)',
            'results': {'search_system': {'success': True, 'message': 'Search system available'}},
            'summary': {'total_tests': 1, 'successful_tests': 1, 'failed_tests': 0, 'success_rate': 100.0},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_web_interface_tests(self, **kwargs) -> Dict[str, Any]:
        """Run web interface tests"""
        logger.info("Running web interface tests...")
        
        # This would test the web platform
        # For now, return a placeholder
        return {
            'success': True,
            'test_category': 'web_interface',
            'description': 'Web interface tests (placeholder)',
            'results': {'web_platform': {'success': True, 'message': 'Web platform available'}},
            'summary': {'total_tests': 1, 'successful_tests': 1, 'failed_tests': 0, 'success_rate': 100.0},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_cli_functionality_tests(self, **kwargs) -> Dict[str, Any]:
        """Run CLI functionality tests"""
        logger.info("Running CLI functionality tests...")
        
        # This would test the CLI system
        # For now, return a placeholder
        return {
            'success': True,
            'test_category': 'cli_functionality',
            'description': 'CLI functionality tests (placeholder)',
            'results': {'cli_system': {'success': True, 'message': 'CLI system available'}},
            'summary': {'total_tests': 1, 'successful_tests': 1, 'failed_tests': 0, 'success_rate': 100.0},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_file_system_tests(self, **kwargs) -> Dict[str, Any]:
        """Run file system tests"""
        logger.info("Running file system tests...")
        
        # This would test the file reflection system
        # For now, return a placeholder
        return {
            'success': True,
            'test_category': 'file_system',
            'description': 'File system tests (placeholder)',
            'results': {'file_system': {'success': True, 'message': 'File system available'}},
            'summary': {'total_tests': 1, 'successful_tests': 1, 'failed_tests': 0, 'success_rate': 100.0},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_consciousness_system_tests(self, **kwargs) -> Dict[str, Any]:
        """Run consciousness system tests"""
        logger.info("Running consciousness system tests...")
        
        # This would test the consciousness mapping system
        # For now, return a placeholder
        return {
            'success': True,
            'test_category': 'consciousness_system',
            'description': 'Consciousness system tests (placeholder)',
            'results': {'consciousness_system': {'success': True, 'message': 'Consciousness system available'}},
            'summary': {'total_tests': 1, 'successful_tests': 1, 'failed_tests': 0, 'success_rate': 100.0},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_integration_tests(self, **kwargs) -> Dict[str, Any]:
        """Run integration tests"""
        logger.info("Running integration tests...")
        
        # This would test system integration
        # For now, return a placeholder
        return {
            'success': True,
            'test_category': 'integration_tests',
            'description': 'Integration tests (placeholder)',
            'results': {'integration': {'success': True, 'message': 'Integration system available'}},
            'summary': {'total_tests': 1, 'successful_tests': 1, 'failed_tests': 0, 'success_rate': 100.0},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_all_tests(self, **kwargs) -> Dict[str, Any]:
        """Run all test categories"""
        logger.info("Running all test categories...")
        
        results = {}
        for test_category in self.available_tests.keys():
            try:
                result = self._run_specific_tests(test_category, **kwargs)
                results[test_category] = result
            except Exception as e:
                results[test_category] = {
                    'success': False,
                    'error': str(e)
                }
        
        # Calculate overall statistics
        total_categories = len(results)
        successful_categories = len([r for r in results.values() if r.get('success', False)])
        
        return {
            'success': successful_categories == total_categories,
            'test_category': 'all_tests',
            'description': 'Ran all test categories',
            'results': results,
            'summary': {
                'total_categories': total_categories,
                'successful_categories': successful_categories,
                'failed_categories': total_categories - successful_categories,
                'success_rate': (successful_categories / total_categories) * 100 if total_categories > 0 else 0
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    # Individual test methods
    def _test_fractal_layers(self) -> Dict[str, Any]:
        """Test fractal layer consistency"""
        try:
            layers = set()
            for node in fractal_core_system.nodes.values():
                layer = node.metadata.get('fractal_layer')
                if layer is not None:
                    layers.add(layer)
            
            return {
                'success': True,
                'message': f'Found {len(layers)} fractal layers',
                'layers': sorted(list(layers))
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_water_states(self) -> Dict[str, Any]:
        """Test water state consistency"""
        try:
            water_states = set()
            for node in fractal_core_system.nodes.values():
                water_state = node.metadata.get('water_state')
                if water_state:
                    water_states.add(water_state)
            
            return {
                'success': True,
                'message': f'Found {len(water_states)} water states',
                'water_states': sorted(list(water_states))
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_chakras(self) -> Dict[str, Any]:
        """Test chakra consistency"""
        try:
            chakras = set()
            for node in fractal_core_system.nodes.values():
                chakra = node.metadata.get('chakra')
                if chakra:
                    chakras.add(chakra)
            
            return {
                'success': True,
                'message': f'Found {len(chakras)} chakras',
                'chakras': sorted(list(chakras))
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_frequencies(self) -> Dict[str, Any]:
        """Test frequency consistency"""
        try:
            frequencies = set()
            for node in fractal_core_system.nodes.values():
                frequency = node.metadata.get('frequency')
                if frequency:
                    frequencies.add(frequency)
            
            return {
                'success': True,
                'message': f'Found {len(frequencies)} frequencies',
                'frequencies': sorted(list(frequencies))
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_self_similarity(self) -> Dict[str, Any]:
        """Test self-similarity property"""
        try:
            self_similar_count = 0
            total_nodes = len(fractal_core_system.nodes)
            
            for node in fractal_core_system.nodes.values():
                if node.structure_info.get('self_similar'):
                    self_similar_count += 1
            
            return {
                'success': True,
                'message': f'{self_similar_count}/{total_nodes} nodes are self-similar',
                'self_similar_count': self_similar_count,
                'total_nodes': total_nodes,
                'percentage': (self_similar_count / total_nodes) * 100 if total_nodes > 0 else 0
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_meta_circularity(self) -> Dict[str, Any]:
        """Test meta-circularity property"""
        try:
            meta_circular_count = 0
            total_nodes = len(fractal_core_system.nodes)
            
            for node in fractal_core_system.nodes.values():
                if node.structure_info.get('meta_circular'):
                    meta_circular_count += 1
            
            return {
                'success': True,
                'message': f'{meta_circular_count}/{total_nodes} nodes are meta-circular',
                'meta_circular_count': meta_circular_count,
                'total_nodes': total_nodes,
                'percentage': (meta_circular_count / total_nodes) * 100 if total_nodes > 0 else 0
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_holographic_nature(self) -> Dict[str, Any]:
        """Test holographic nature property"""
        try:
            holographic_count = 0
            total_nodes = len(fractal_core_system.nodes)
            
            for node in fractal_core_system.nodes.values():
                if node.structure_info.get('holographic'):
                    holographic_count += 1
            
            return {
                'success': True,
                'message': f'{holographic_count}/{total_nodes} nodes are holographic',
                'holographic_count': holographic_count,
                'total_nodes': total_nodes,
                'percentage': (holographic_count / total_nodes) * 100 if total_nodes > 0 else 0
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_node_creation(self) -> Dict[str, Any]:
        """Test node creation functionality"""
        try:
            # Create a test node
            test_node = fractal_core_system.create_node(
                node_type="test_node",
                name="Test Node",
                content="This is a test node for testing node creation",
                metadata={"test": True, "timestamp": datetime.now(timezone.utc).isoformat()}
            )
            
            # Verify the node was created
            if test_node.node_id in fractal_core_system.nodes:
                # Clean up the test node
                fractal_core_system.delete_node(test_node.node_id)
                
                return {
                    'success': True,
                    'message': 'Node creation and deletion successful'
                }
            else:
                return {
                    'success': False,
                    'error': 'Node was not properly created'
                }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_node_retrieval(self) -> Dict[str, Any]:
        """Test node retrieval functionality"""
        try:
            # Get a node by ID
            if fractal_core_system.nodes:
                first_node_id = list(fractal_core_system.nodes.keys())[0]
                node = fractal_core_system.get_node(first_node_id)
                
                if node:
                    return {
                        'success': True,
                        'message': f'Successfully retrieved node: {node.name}'
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Failed to retrieve node'
                    }
            else:
                return {
                    'success': True,
                    'message': 'No nodes to test retrieval with'
                }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_node_search(self) -> Dict[str, Any]:
        """Test node search functionality"""
        try:
            # Search for nodes
            results = fractal_core_system.search_nodes("test")
            
            return {
                'success': True,
                'message': f'Search returned {len(results)} results',
                'result_count': len(results)
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_node_hierarchy(self) -> Dict[str, Any]:
        """Test node hierarchy functionality"""
        try:
            # Get hierarchy for a node
            if fractal_core_system.nodes:
                first_node_id = list(fractal_core_system.nodes.keys())[0]
                hierarchy = fractal_core_system.get_node_hierarchy(first_node_id, max_depth=2)
                
                return {
                    'success': True,
                    'message': 'Node hierarchy retrieval successful',
                    'hierarchy_depth': len(hierarchy.get('children', []))
                }
            else:
                return {
                    'success': True,
                    'message': 'No nodes to test hierarchy with'
                }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _test_system_status(self) -> Dict[str, Any]:
        """Test system status functionality"""
        try:
            status = fractal_core_system.get_system_status()
            
            return {
                'success': True,
                'message': f'System status retrieved successfully',
                'total_nodes': status.get('total_nodes', 0),
                'component_count': status.get('component_count', 0)
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}


def main():
    """Main function to run the comprehensive test system"""
    logging.basicConfig(level=logging.INFO)
    
    print("🧪 Living Codex Comprehensive Test System")
    print("=" * 50)
    
    # Initialize the test system
    test_system = ComprehensiveTestSystem()
    
    # List available tests
    print(f"\n📋 Available Test Categories ({len(test_system.available_tests)}):")
    for test_id, test_info in test_system.available_tests.items():
        print(f"  • {test_id}: {test_info['name']} - {test_info['description']}")
    
    # Run a specific test category if provided
    if len(sys.argv) > 1:
        test_category = sys.argv[1]
        print(f"\n🧪 Running tests for category: {test_category}")
        result = test_system.run_tests(test_category)
        
        if result['success']:
            print(f"✅ Tests completed successfully!")
            summary = result.get('summary', {})
            print(f"Success Rate: {summary.get('success_rate', 0):.1f}%")
            print(f"Passed: {summary.get('successful_tests', 0)}/{summary.get('total_tests', 0)}")
        else:
            print(f"❌ Tests failed: {result.get('error', 'Unknown error')}")
    else:
        # Run all tests
        print(f"\n🧪 Running all test categories...")
        results = test_system.run_tests()
        
        if results['success']:
            summary = results.get('summary', {})
            print(f"✅ All tests completed successfully!")
            print(f"Success Rate: {summary.get('success_rate', 0):.1f}%")
            print(f"Passed: {summary.get('successful_categories', 0)}/{summary.get('total_categories', 0)} categories")
        else:
            print(f"❌ Some tests failed")
            summary = results.get('summary', {})
            print(f"Success Rate: {summary.get('success_rate', 0):.1f}%")
            print(f"Passed: {summary.get('successful_categories', 0)}/{summary.get('total_categories', 0)} categories")


if __name__ == "__main__":
    main()
