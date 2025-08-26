#!/usr/bin/env python3
"""
Living Codex Comprehensive Demo System
Consolidated demo system that provides access to all demo scenarios
Following the Living Codex specification principles:
- Everything is just nodes
- Fractal self-similarity at every level
- Meta-circular self-description
"""

import os
import sys
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timezone

# Add the parent directory to the path to import core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.core_system import fractal_core_system, GenericNode
from core.fractal_components import initialize_fractal_components

logger = logging.getLogger(__name__)

class ComprehensiveDemoSystem:
    """
    Comprehensive demo system that consolidates all demo functionality
    Provides a unified interface for running any demo scenario
    """
    
    def __init__(self):
        self.name = "Comprehensive Demo System"
        self.available_demos = self._discover_available_demos()
        self._register_as_fractal_node()
    
    def _discover_available_demos(self) -> Dict[str, Dict[str, Any]]:
        """Discover all available demo scenarios"""
        return {
            'ice_bootstrap': {
                'name': 'ICE Bootstrap Demo',
                'description': 'Demonstrate the ICE bootstrap cycle',
                'category': 'core_system',
                'complexity': 'medium',
                'dependencies': ['core_system', 'fractal_components']
            },
            'water_states': {
                'name': 'Water States Demo',
                'description': 'Demonstrate water state consciousness mapping',
                'category': 'consciousness_system',
                'complexity': 'medium',
                'dependencies': ['water_state_system']
            },
            'fractal_architecture': {
                'name': 'Fractal Architecture Demo',
                'description': 'Demonstrate fractal holographic architecture',
                'category': 'architecture',
                'complexity': 'high',
                'dependencies': ['fractal_components']
            },
            'code_navigation': {
                'name': 'Code Navigation Demo',
                'description': 'Demonstrate code navigation and reflection',
                'category': 'development',
                'complexity': 'medium',
                'dependencies': ['code_reflection_system']
            },
            'unified_platform': {
                'name': 'Unified Platform Demo',
                'description': 'Demonstrate unified platform capabilities',
                'category': 'platform',
                'complexity': 'high',
                'dependencies': ['web_platform', 'api_system']
            },
            'consciousness_mapping': {
                'name': 'Consciousness Mapping Demo',
                'description': 'Demonstrate quantum consciousness mapping',
                'category': 'consciousness_system',
                'complexity': 'high',
                'dependencies': ['quantum_consciousness_system']
            },
            'file_reflection': {
                'name': 'File Reflection Demo',
                'description': 'Demonstrate comprehensive file reflection',
                'category': 'file_system',
                'complexity': 'medium',
                'dependencies': ['file_reflection_system']
            },
            'testing_system': {
                'name': 'Testing System Demo',
                'description': 'Demonstrate comprehensive testing capabilities',
                'category': 'testing',
                'complexity': 'medium',
                'dependencies': ['testing_system']
            }
        }
    
    def _register_as_fractal_node(self):
        """Register this demo system as a node in the fractal system"""
        demo_system_node = GenericNode(
            node_id="comprehensive_demo_system",
            node_type="demo_system",
            name=self.name,
            content="Unified demo system providing access to all demo scenarios",
            parent_id="meta_implementation",
            metadata={
                "fractal_layer": 3,
                "water_state": "liquid",
                "frequency": 639,
                "chakra": "heart",
                "is_demo_system": True,
                "demo_count": len(self.available_demos)
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": True,
                "holographic": True,
                "demo_categories": list(set(demo['category'] for demo in self.available_demos.values()))
            }
        )
        
        fractal_core_system._register_node(demo_system_node)
        
        # Create demo scenario nodes
        for demo_id, demo_info in self.available_demos.items():
            demo_node = GenericNode(
                node_id=f"demo_{demo_id}",
                node_type="demo_scenario",
                name=demo_info['name'],
                content=demo_info['description'],
                parent_id="comprehensive_demo_system",
                metadata={
                    "fractal_layer": 4,
                    "water_state": "vapor",
                    "frequency": 528,
                    "chakra": "solar_plexus",
                    "category": demo_info['category'],
                    "complexity": demo_info['complexity'],
                    "dependencies": demo_info['dependencies']
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True,
                    "demo_type": "scenario"
                }
            )
            fractal_core_system._register_node(demo_node)
            
            # Update parent's children list
            if demo_system_node.node_id not in fractal_core_system.nodes["comprehensive_demo_system"].children:
                fractal_core_system.nodes["comprehensive_demo_system"].children.append(demo_node.node_id)
        
        logger.info(f"Comprehensive demo system registered with {len(self.available_demos)} demo scenarios")
    
    def list_available_demos(self) -> Dict[str, Dict[str, Any]]:
        """List all available demo scenarios"""
        return self.available_demos
    
    def run_demo(self, demo_id: str, **kwargs) -> Dict[str, Any]:
        """Run a specific demo scenario"""
        if demo_id not in self.available_demos:
            return {
                'success': False,
                'error': f'Demo "{demo_id}" not found',
                'available_demos': list(self.available_demos.keys())
            }
        
        demo_info = self.available_demos[demo_id]
        logger.info(f"Running demo: {demo_info['name']}")
        
        try:
            if demo_id == 'ice_bootstrap':
                return self._run_ice_bootstrap_demo(**kwargs)
            elif demo_id == 'water_states':
                return self._run_water_states_demo(**kwargs)
            elif demo_id == 'fractal_architecture':
                return self._run_fractal_architecture_demo(**kwargs)
            elif demo_id == 'code_navigation':
                return self._run_code_navigation_demo(**kwargs)
            elif demo_id == 'unified_platform':
                return self._run_unified_platform_demo(**kwargs)
            elif demo_id == 'consciousness_mapping':
                return self._run_consciousness_mapping_demo(**kwargs)
            elif demo_id == 'file_reflection':
                return self._run_file_reflection_demo(**kwargs)
            elif demo_id == 'testing_system':
                return self._run_testing_system_demo(**kwargs)
            else:
                return {
                    'success': False,
                    'error': f'Demo "{demo_id}" not implemented yet'
                }
        except Exception as e:
            logger.error(f"Error running demo {demo_id}: {e}")
            return {
                'success': False,
                'error': str(e),
                'demo_id': demo_id
            }
    
    def _run_ice_bootstrap_demo(self, **kwargs) -> Dict[str, Any]:
        """Run ICE bootstrap demo"""
        logger.info("Running ICE bootstrap demo...")
        
        # Initialize fractal components if not already done
        try:
            components = initialize_fractal_components()
            logger.info(f"Initialized {len(components)} fractal components")
        except Exception as e:
            logger.warning(f"Could not initialize fractal components: {e}")
            components = []
        
        # Get system status
        system_status = fractal_core_system.get_system_status()
        
        return {
            'success': True,
            'demo_name': 'ICE Bootstrap Demo',
            'description': 'Demonstrated ICE bootstrap cycle with fractal components',
            'results': {
                'total_nodes': system_status['total_nodes'],
                'component_count': system_status['component_count'],
                'node_types': len(system_status['node_types']),
                'fractal_layers': len(system_status['fractal_layers']),
                'water_states': len(system_status['water_states']),
                'chakras': len(system_status['chakras'])
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_water_states_demo(self, **kwargs) -> Dict[str, Any]:
        """Run water states demo"""
        logger.info("Running water states demo...")
        
        # Get water state nodes
        water_state_nodes = fractal_core_system.get_nodes_by_metadata('water_state', 'liquid')
        ice_nodes = fractal_core_system.get_nodes_by_metadata('water_state', 'ice')
        vapor_nodes = fractal_core_system.get_nodes_by_metadata('water_state', 'vapor')
        
        return {
            'success': True,
            'demo_name': 'Water States Demo',
            'description': 'Demonstrated water state consciousness mapping',
            'results': {
                'liquid_nodes': len(water_state_nodes),
                'ice_nodes': len(ice_nodes),
                'vapor_nodes': len(vapor_nodes),
                'total_water_states': len(water_state_nodes) + len(ice_nodes) + len(vapor_nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_fractal_architecture_demo(self, **kwargs) -> Dict[str, Any]:
        """Run fractal architecture demo"""
        logger.info("Running fractal architecture demo...")
        
        # Get fractal layer information
        fractal_layers = {}
        for node in fractal_core_system.nodes.values():
            layer = node.metadata.get('fractal_layer', 0)
            if layer not in fractal_layers:
                fractal_layers[layer] = []
            fractal_layers[layer].append(node.node_id)
        
        # Analyze fractal properties
        self_similar_nodes = [n for n in fractal_core_system.nodes.values() 
                             if n.structure_info.get('self_similar')]
        meta_circular_nodes = [n for n in fractal_core_system.nodes.values() 
                              if n.structure_info.get('meta_circular')]
        holographic_nodes = [n for n in fractal_core_system.nodes.values() 
                            if n.structure_info.get('holographic')]
        
        return {
            'success': True,
            'demo_name': 'Fractal Architecture Demo',
            'description': 'Demonstrated fractal holographic architecture',
            'results': {
                'fractal_layers': {str(layer): len(nodes) for layer, nodes in fractal_layers.items()},
                'self_similar_nodes': len(self_similar_nodes),
                'meta_circular_nodes': len(meta_circular_nodes),
                'holographic_nodes': len(holographic_nodes),
                'total_nodes': len(fractal_core_system.nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_code_navigation_demo(self, **kwargs) -> Dict[str, Any]:
        """Run code navigation demo"""
        logger.info("Running code navigation demo...")
        
        # Get code-related nodes
        code_nodes = fractal_core_system.get_nodes_by_type('code')
        file_nodes = fractal_core_system.get_nodes_by_type('file')
        component_nodes = fractal_core_system.get_nodes_by_type('component')
        
        return {
            'success': True,
            'demo_name': 'Code Navigation Demo',
            'description': 'Demonstrated code navigation and reflection',
            'results': {
                'code_nodes': len(code_nodes),
                'file_nodes': len(file_nodes),
                'component_nodes': len(component_nodes),
                'total_code_related': len(code_nodes) + len(file_nodes) + len(component_nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_unified_platform_demo(self, **kwargs) -> Dict[str, Any]:
        """Run unified platform demo"""
        logger.info("Running unified platform demo...")
        
        # Get platform-related nodes
        web_nodes = fractal_core_system.get_nodes_by_type('web_platform')
        api_nodes = fractal_core_system.get_nodes_by_type('api')
        user_nodes = fractal_core_system.get_nodes_by_type('user')
        
        return {
            'success': True,
            'demo_name': 'Unified Platform Demo',
            'description': 'Demonstrated unified platform capabilities',
            'results': {
                'web_platform_nodes': len(web_nodes),
                'api_nodes': len(api_nodes),
                'user_nodes': len(user_nodes),
                'total_platform_nodes': len(web_nodes) + len(api_nodes) + len(user_nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_consciousness_mapping_demo(self, **kwargs) -> Dict[str, Any]:
        """Run consciousness mapping demo"""
        logger.info("Running consciousness mapping demo...")
        
        # Get consciousness-related nodes
        consciousness_nodes = fractal_core_system.get_nodes_by_metadata('category', 'consciousness')
        quantum_nodes = fractal_core_system.get_nodes_by_metadata('category', 'quantum')
        chakra_nodes = fractal_core_system.get_nodes_by_metadata('chakra', 'crown')
        
        return {
            'success': True,
            'demo_name': 'Consciousness Mapping Demo',
            'description': 'Demonstrated quantum consciousness mapping',
            'results': {
                'consciousness_nodes': len(consciousness_nodes),
                'quantum_nodes': len(quantum_nodes),
                'crown_chakra_nodes': len(chakra_nodes),
                'total_consciousness_nodes': len(consciousness_nodes) + len(quantum_nodes) + len(chakra_nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_file_reflection_demo(self, **kwargs) -> Dict[str, Any]:
        """Run file reflection demo"""
        logger.info("Running file reflection demo...")
        
        # Get file-related nodes
        file_type_nodes = fractal_core_system.get_nodes_by_type('file_type')
        validation_nodes = fractal_core_system.get_nodes_by_type('validation_rule')
        documentation_nodes = fractal_core_system.get_nodes_by_type('documentation')
        
        return {
            'success': True,
            'demo_name': 'File Reflection Demo',
            'description': 'Demonstrated comprehensive file reflection',
            'results': {
                'file_type_nodes': len(file_type_nodes),
                'validation_nodes': len(validation_nodes),
                'documentation_nodes': len(documentation_nodes),
                'total_file_nodes': len(file_type_nodes) + len(validation_nodes) + len(documentation_nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def _run_testing_system_demo(self, **kwargs) -> Dict[str, Any]:
        """Run testing system demo"""
        logger.info("Running testing system demo...")
        
        # Get testing-related nodes
        test_nodes = fractal_core_system.get_nodes_by_type('test')
        validation_nodes = fractal_core_system.get_nodes_by_type('validation')
        assertion_nodes = fractal_core_system.get_nodes_by_type('assertion')
        
        return {
            'success': True,
            'demo_name': 'Testing System Demo',
            'description': 'Demonstrated comprehensive testing capabilities',
            'results': {
                'test_nodes': len(test_nodes),
                'validation_nodes': len(validation_nodes),
                'assertion_nodes': len(assertion_nodes),
                'total_testing_nodes': len(test_nodes) + len(validation_nodes) + len(assertion_nodes)
            },
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def run_all_demos(self) -> Dict[str, Any]:
        """Run all available demo scenarios"""
        logger.info("Running all available demos...")
        
        results = {}
        for demo_id in self.available_demos.keys():
            try:
                result = self.run_demo(demo_id)
                results[demo_id] = result
            except Exception as e:
                results[demo_id] = {
                    'success': False,
                    'error': str(e)
                }
        
        return {
            'success': True,
            'total_demos': len(self.available_demos),
            'successful_demos': len([r for r in results.values() if r.get('success', False)]),
            'failed_demos': len([r for r in results.values() if not r.get('success', False)]),
            'results': results,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }


def main():
    """Main function to run the comprehensive demo system"""
    logging.basicConfig(level=logging.INFO)
    
    print("🌊 Living Codex Comprehensive Demo System")
    print("=" * 50)
    
    # Initialize the demo system
    demo_system = ComprehensiveDemoSystem()
    
    # List available demos
    print(f"\n📋 Available Demos ({len(demo_system.available_demos)}):")
    for demo_id, demo_info in demo_system.available_demos.items():
        print(f"  • {demo_id}: {demo_info['name']} - {demo_info['description']}")
    
    # Run a specific demo if provided
    if len(sys.argv) > 1:
        demo_id = sys.argv[1]
        print(f"\n🚀 Running demo: {demo_id}")
        result = demo_system.run_demo(demo_id)
        
        if result['success']:
            print(f"✅ Demo completed successfully!")
            print(f"Results: {result['results']}")
        else:
            print(f"❌ Demo failed: {result['error']}")
    else:
        # Run all demos
        print(f"\n🚀 Running all demos...")
        results = demo_system.run_all_demos()
        
        print(f"✅ Completed {results['successful_demos']}/{results['total_demos']} demos successfully")
        
        if results['failed_demos'] > 0:
            print(f"❌ {results['failed_demos']} demos failed")
            for demo_id, result in results['results'].items():
                if not result.get('success', False):
                    print(f"  • {demo_id}: {result.get('error', 'Unknown error')}")


if __name__ == "__main__":
    main()
