#!/usr/bin/env python3
"""
Living Codex Unified API System
Consolidated API system that provides access to all system capabilities
Following the Living Codex specification principles:
- Everything is just nodes
- Fractal self-similarity at every level
- Meta-circular self-description
"""

import os
import sys
import logging
import json
import time
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, asdict

# Add the parent directory to the path to import core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.core_system import fractal_core_system, GenericNode
from core.fractal_components import initialize_fractal_components

logger = logging.getLogger(__name__)

@dataclass
class APIRequest:
    """API request structure"""
    endpoint: str
    method: str
    params: Dict[str, Any]
    headers: Dict[str, str]
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now(timezone.utc)

@dataclass
class APIResponse:
    """API response structure"""
    success: bool
    data: Any
    message: str
    timestamp: datetime
    request_id: str
    processing_time: float

@dataclass
class RateLimitInfo:
    """Rate limiting information"""
    requests_per_minute: int
    requests_per_hour: int
    current_minute_requests: int
    current_hour_requests: int
    reset_time: datetime

class UnifiedAPISystem:
    """
    Unified API system that consolidates all API functionality
    Provides a single interface for all system operations
    """
    
    def __init__(self):
        self.name = "Unified API System"
        self.version = "1.0.0"
        self.base_url = "/api/v1"
        
        # Rate limiting configuration
        self.rate_limits = {
            'requests_per_minute': 100,
            'requests_per_hour': 1000
        }
        
        # Request tracking
        self.request_history: List[APIRequest] = []
        self.rate_limit_tracker = {
            'minute': {'count': 0, 'reset_time': datetime.now(timezone.utc)},
            'hour': {'count': 0, 'reset_time': datetime.now(timezone.utc)}
        }
        
        # API endpoints registry
        self.endpoints = self._discover_endpoints()
        self._register_as_fractal_node()
    
    def _discover_endpoints(self) -> Dict[str, Dict[str, Any]]:
        """Discover all available API endpoints"""
        return {
            'system': {
                'name': 'System Management',
                'description': 'System status and management endpoints',
                'endpoints': {
                    'GET /system/status': 'Get comprehensive system status',
                    'GET /system/health': 'Get system health information',
                    'GET /system/nodes': 'Get all nodes in the system',
                    'GET /system/nodes/{node_id}': 'Get specific node by ID',
                    'POST /system/nodes': 'Create a new node',
                    'PUT /system/nodes/{node_id}': 'Update a node',
                    'DELETE /system/nodes/{node_id}': 'Delete a node'
                }
            },
            'search': {
                'name': 'Search and Navigation',
                'description': 'Search and navigation endpoints',
                'endpoints': {
                    'GET /search': 'Search nodes by query',
                    'GET /search/advanced': 'Advanced search with filters',
                    'GET /navigation/{node_id}': 'Get navigation context for a node',
                    'GET /navigation/path': 'Get navigation path between nodes'
                }
            },
            'fractal': {
                'name': 'Fractal Architecture',
                'description': 'Fractal architecture exploration endpoints',
                'endpoints': {
                    'GET /fractal/layers': 'Get fractal layer information',
                    'GET /fractal/layers/{layer}': 'Get nodes at specific fractal layer',
                    'GET /fractal/components': 'Get fractal component information',
                    'GET /fractal/properties': 'Get fractal property analysis'
                }
            },
            'consciousness': {
                'name': 'Consciousness Mapping',
                'description': 'Consciousness and quantum mapping endpoints',
                'endpoints': {
                    'GET /consciousness/water_states': 'Get water state mapping',
                    'GET /consciousness/chakras': 'Get chakra mapping',
                    'GET /consciousness/frequencies': 'Get frequency mapping',
                    'GET /consciousness/quantum': 'Get quantum consciousness mapping'
                }
            },
            'files': {
                'name': 'File System',
                'description': 'File reflection and management endpoints',
                'endpoints': {
                    'GET /files/types': 'Get file type information',
                    'GET /files/validation': 'Get file validation rules',
                    'GET /files/documentation': 'Get file documentation',
                    'GET /files/exploration': 'Get file exploration paths'
                }
            },
            'demos': {
                'name': 'Demo System',
                'description': 'Demo system endpoints',
                'endpoints': {
                    'GET /demos': 'List available demos',
                    'POST /demos/{demo_id}/run': 'Run a specific demo',
                    'POST /demos/run_all': 'Run all available demos'
                }
            },
            'tests': {
                'name': 'Testing System',
                'description': 'Testing system endpoints',
                'endpoints': {
                    'GET /tests': 'List available test categories',
                    'POST /tests/{category}/run': 'Run tests for a category',
                    'POST /tests/run_all': 'Run all test categories'
                }
            }
        }
    
    def _register_as_fractal_node(self):
        """Register this API system as a node in the fractal system"""
        api_system_node = GenericNode(
            node_id="unified_api_system",
            node_type="api_system",
            name=self.name,
            content="Unified API system providing access to all system capabilities",
            parent_id="meta_implementation",
            metadata={
                "fractal_layer": 3,
                "water_state": "vapor",
                "frequency": 741,
                "chakra": "throat",
                "is_api_system": True,
                "version": self.version,
                "endpoint_count": sum(len(ep['endpoints']) for ep in self.endpoints.values())
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": True,
                "holographic": True,
                "api_categories": list(self.endpoints.keys())
            }
        )
        
        fractal_core_system._register_node(api_system_node)
        
        # Create API category nodes
        for category_id, category_info in self.endpoints.items():
            category_node = GenericNode(
                node_id=f"api_category_{category_id}",
                node_type="api_category",
                name=category_info['name'],
                content=category_info['description'],
                parent_id="unified_api_system",
                metadata={
                    "fractal_layer": 4,
                    "water_state": "liquid",
                    "frequency": 639,
                    "chakra": "heart",
                    "category": category_id,
                    "endpoint_count": len(category_info['endpoints'])
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True,
                    "api_type": "category"
                }
            )
            fractal_core_system._register_node(category_node)
            
            # Update parent's children list
            if api_system_node.node_id not in fractal_core_system.nodes["unified_api_system"].children:
                fractal_core_system.nodes["unified_api_system"].children.append(category_node.node_id)
        
        logger.info(f"Unified API system registered with {len(self.endpoints)} API categories")
    
    def check_rate_limit(self, client_id: str = "default") -> bool:
        """Check if request is within rate limits"""
        now = datetime.now(timezone.utc)
        
        # Reset counters if needed
        if (now - self.rate_limit_tracker['minute']['reset_time']).seconds >= 60:
            self.rate_limit_tracker['minute'] = {'count': 0, 'reset_time': now}
        
        if (now - self.rate_limit_tracker['hour']['reset_time']).seconds >= 3600:
            self.rate_limit_tracker['hour'] = {'count': 0, 'reset_time': now}
        
        # Check limits
        if (self.rate_limit_tracker['minute']['count'] >= self.rate_limits['requests_per_minute'] or
            self.rate_limit_tracker['hour']['count'] >= self.rate_limits['requests_per_hour']):
            return False
        
        # Increment counters
        self.rate_limit_tracker['minute']['count'] += 1
        self.rate_limit_tracker['hour']['count'] += 1
        
        return True
    
    def get_rate_limit_info(self) -> RateLimitInfo:
        """Get current rate limit information"""
        now = datetime.now(timezone.utc)
        
        return RateLimitInfo(
            requests_per_minute=self.rate_limits['requests_per_minute'],
            requests_per_hour=self.rate_limits['requests_per_hour'],
            current_minute_requests=self.rate_limit_tracker['minute']['count'],
            current_hour_requests=self.rate_limit_tracker['hour']['count'],
            reset_time=now + timedelta(minutes=1)
        )
    
    def handle_request(self, endpoint: str, method: str, params: Dict[str, Any], 
                      headers: Dict[str, str] = None) -> APIResponse:
        """Handle an API request and return response"""
        start_time = time.time()
        request_id = f"req_{int(start_time * 1000)}"
        
        # Create request object
        request = APIRequest(
            endpoint=endpoint,
            method=method,
            params=params or {},
            headers=headers or {}
        )
        
        # Check rate limiting
        if not self.check_rate_limit():
            return APIResponse(
                success=False,
                data=None,
                message="Rate limit exceeded",
                timestamp=datetime.now(timezone.utc),
                request_id=request_id,
                processing_time=time.time() - start_time
            )
        
        # Add to request history
        self.request_history.append(request)
        
        try:
            # Route the request
            if endpoint.startswith('/system'):
                data = self._handle_system_endpoint(endpoint, method, params)
            elif endpoint.startswith('/search'):
                data = self._handle_search_endpoint(endpoint, method, params)
            elif endpoint.startswith('/fractal'):
                data = self._handle_fractal_endpoint(endpoint, method, params)
            elif endpoint.startswith('/consciousness'):
                data = self._handle_consciousness_endpoint(endpoint, method, params)
            elif endpoint.startswith('/files'):
                data = self._handle_files_endpoint(endpoint, method, params)
            elif endpoint.startswith('/demos'):
                data = self._handle_demos_endpoint(endpoint, method, params)
            elif endpoint.startswith('/tests'):
                data = self._handle_tests_endpoint(endpoint, method, params)
            else:
                data = None
                message = f"Unknown endpoint: {endpoint}"
                success = False
                return APIResponse(
                    success=success,
                    data=data,
                    message=message,
                    timestamp=datetime.now(timezone.utc),
                    request_id=request_id,
                    processing_time=time.time() - start_time
                )
            
            return APIResponse(
                success=True,
                data=data,
                message="Request processed successfully",
                timestamp=datetime.now(timezone.utc),
                request_id=request_id,
                processing_time=time.time() - start_time
            )
            
        except Exception as e:
            logger.error(f"Error handling request {request_id}: {e}")
            return APIResponse(
                success=False,
                data=None,
                message=f"Internal error: {str(e)}",
                timestamp=datetime.now(timezone.utc),
                request_id=request_id,
                processing_time=time.time() - start_time
            )
    
    def _handle_system_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle system-related endpoints"""
        if endpoint == '/system/status' and method == 'GET':
            return fractal_core_system.get_system_status()
        elif endpoint == '/system/health' and method == 'GET':
            return self._get_system_health()
        elif endpoint == '/system/nodes' and method == 'GET':
            return [node.to_dict() for node in fractal_core_system.nodes.values()]
        elif endpoint.startswith('/system/nodes/') and method == 'GET':
            node_id = endpoint.split('/')[-1]
            node = fractal_core_system.get_node(node_id)
            return node.to_dict() if node else None
        elif endpoint == '/system/nodes' and method == 'POST':
            return self._create_node_from_params(params)
        elif endpoint.startswith('/system/nodes/') and method == 'PUT':
            node_id = endpoint.split('/')[-1]
            return self._update_node_from_params(node_id, params)
        elif endpoint.startswith('/system/nodes/') and method == 'DELETE':
            node_id = endpoint.split('/')[-1]
            return fractal_core_system.delete_node(node_id)
        else:
            raise ValueError(f"Unsupported system endpoint: {endpoint} {method}")
    
    def _handle_search_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle search-related endpoints"""
        if endpoint == '/search' and method == 'GET':
            query = params.get('query', '')
            node_type = params.get('node_type')
            return fractal_core_system.search_nodes(query, node_type)
        elif endpoint == '/search/advanced' and method == 'GET':
            # Advanced search with filters
            query = params.get('query', '')
            filters = params.get('filters', {})
            return self._advanced_search(query, filters)
        elif endpoint.startswith('/navigation/') and method == 'GET':
            node_id = endpoint.split('/')[-1]
            max_depth = params.get('max_depth', 3)
            return fractal_core_system.get_node_hierarchy(node_id, max_depth)
        else:
            raise ValueError(f"Unsupported search endpoint: {endpoint} {method}")
    
    def _handle_fractal_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle fractal-related endpoints"""
        if endpoint == '/fractal/layers' and method == 'GET':
            return self._get_fractal_layers_info()
        elif endpoint.startswith('/fractal/layers/') and method == 'GET':
            layer = int(endpoint.split('/')[-1])
            return self._get_nodes_at_fractal_layer(layer)
        elif endpoint == '/fractal/components' and method == 'GET':
            return self._get_fractal_components_info()
        elif endpoint == '/fractal/properties' and method == 'GET':
            return self._get_fractal_properties_analysis()
        else:
            raise ValueError(f"Unsupported fractal endpoint: {endpoint} {method}")
    
    def _handle_consciousness_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle consciousness-related endpoints"""
        if endpoint == '/consciousness/water_states' and method == 'GET':
            return self._get_water_states_mapping()
        elif endpoint == '/consciousness/chakras' and method == 'GET':
            return self._get_chakras_mapping()
        elif endpoint == '/consciousness/frequencies' and method == 'GET':
            return self._get_frequencies_mapping()
        elif endpoint == '/consciousness/quantum' and method == 'GET':
            return self._get_quantum_consciousness_mapping()
        else:
            raise ValueError(f"Unsupported consciousness endpoint: {endpoint} {method}")
    
    def _handle_files_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle file-related endpoints"""
        if endpoint == '/files/types' and method == 'GET':
            return fractal_core_system.get_nodes_by_type('file_type')
        elif endpoint == '/files/validation' and method == 'GET':
            return fractal_core_system.get_nodes_by_type('validation_rule')
        elif endpoint == '/files/documentation' and method == 'GET':
            return fractal_core_system.get_nodes_by_type('documentation')
        elif endpoint == '/files/exploration' and method == 'GET':
            return fractal_core_system.get_nodes_by_type('exploration_path')
        else:
            raise ValueError(f"Unsupported files endpoint: {endpoint} {method}")
    
    def _handle_demos_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle demo-related endpoints"""
        if endpoint == '/demos' and method == 'GET':
            # Return available demos
            return {
                'available_demos': [
                    'ice_bootstrap', 'water_states', 'fractal_architecture',
                    'code_navigation', 'unified_platform', 'consciousness_mapping',
                    'file_reflection', 'testing_system'
                ]
            }
        elif endpoint.startswith('/demos/') and endpoint.endswith('/run') and method == 'POST':
            demo_id = endpoint.split('/')[1]
            # This would run the actual demo
            return {'demo_id': demo_id, 'status': 'demo_execution_placeholder'}
        elif endpoint == '/demos/run_all' and method == 'POST':
            # This would run all demos
            return {'status': 'all_demos_execution_placeholder'}
        else:
            raise ValueError(f"Unsupported demos endpoint: {endpoint} {method}")
    
    def _handle_tests_endpoint(self, endpoint: str, method: str, params: Dict[str, Any]) -> Any:
        """Handle test-related endpoints"""
        if endpoint == '/tests' and method == 'GET':
            # Return available test categories
            return {
                'available_test_categories': [
                    'fractal_architecture', 'core_functionality', 'search_functionality',
                    'web_interface', 'cli_functionality', 'file_system',
                    'consciousness_system', 'integration_tests'
                ]
            }
        elif endpoint.startswith('/tests/') and endpoint.endswith('/run') and method == 'POST':
            category = endpoint.split('/')[1]
            # This would run the actual tests
            return {'category': category, 'status': 'test_execution_placeholder'}
        elif endpoint == '/tests/run_all' and method == 'POST':
            # This would run all tests
            return {'status': 'all_tests_execution_placeholder'}
        else:
            raise ValueError(f"Unsupported tests endpoint: {endpoint} {method}")
    
    # Helper methods for endpoint handlers
    def _get_system_health(self) -> Dict[str, Any]:
        """Get system health information"""
        return {
            'status': 'healthy',
            'uptime': 'system_uptime_placeholder',
            'memory_usage': 'memory_usage_placeholder',
            'cpu_usage': 'cpu_usage_placeholder',
            'active_connections': len(self.request_history),
            'rate_limit_info': asdict(self.get_rate_limit_info())
        }
    
    def _create_node_from_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Create a node from request parameters"""
        node = fractal_core_system.create_node(
            node_type=params.get('node_type', 'generic'),
            name=params.get('name', 'Unnamed Node'),
            content=params.get('content', ''),
            parent_id=params.get('parent_id'),
            metadata=params.get('metadata', {}),
            structure_info=params.get('structure_info', {})
        )
        return node.to_dict()
    
    def _update_node_from_params(self, node_id: str, params: Dict[str, Any]) -> bool:
        """Update a node from request parameters"""
        updates = {}
        for key in ['name', 'content', 'metadata', 'structure_info']:
            if key in params:
                updates[key] = params[key]
        
        return fractal_core_system.update_node(node_id, updates)
    
    def _advanced_search(self, query: str, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Perform advanced search with filters"""
        results = fractal_core_system.search_nodes(query)
        
        # Apply filters
        if 'node_type' in filters:
            results = [r for r in results if r.node_type == filters['node_type']]
        
        if 'water_state' in filters:
            results = [r for r in results if r.metadata.get('water_state') == filters['water_state']]
        
        if 'chakra' in filters:
            results = [r for r in results if r.metadata.get('chakra') == filters['chakra']]
        
        return [r.to_dict() for r in results]
    
    def _get_fractal_layers_info(self) -> Dict[str, Any]:
        """Get information about fractal layers"""
        layers = {}
        for node in fractal_core_system.nodes.values():
            layer = node.metadata.get('fractal_layer', 0)
            if layer not in layers:
                layers[layer] = []
            layers[layer].append({
                'node_id': node.node_id,
                'name': node.name,
                'type': node.node_type
            })
        
        return {
            'fractal_layers': {str(layer): {'count': len(nodes), 'nodes': nodes} 
                              for layer, nodes in layers.items()}
        }
    
    def _get_nodes_at_fractal_layer(self, layer: int) -> List[Dict[str, Any]]:
        """Get nodes at a specific fractal layer"""
        nodes = [node for node in fractal_core_system.nodes.values() 
                if node.metadata.get('fractal_layer') == layer]
        return [node.to_dict() for node in nodes]
    
    def _get_fractal_components_info(self) -> Dict[str, Any]:
        """Get information about fractal components"""
        components = fractal_core_system.get_nodes_by_type('component')
        return {
            'total_components': len(components),
            'components': [comp.to_dict() for comp in components]
        }
    
    def _get_fractal_properties_analysis(self) -> Dict[str, Any]:
        """Get analysis of fractal properties"""
        total_nodes = len(fractal_core_system.nodes)
        
        self_similar_count = len([n for n in fractal_core_system.nodes.values() 
                                 if n.structure_info.get('self_similar')])
        meta_circular_count = len([n for n in fractal_core_system.nodes.values() 
                                  if n.structure_info.get('meta_circular')])
        holographic_count = len([n for n in fractal_core_system.nodes.values() 
                                if n.structure_info.get('holographic')])
        
        return {
            'total_nodes': total_nodes,
            'fractal_properties': {
                'self_similar': {
                    'count': self_similar_count,
                    'percentage': (self_similar_count / total_nodes) * 100 if total_nodes > 0 else 0
                },
                'meta_circular': {
                    'count': meta_circular_count,
                    'percentage': (meta_circular_count / total_nodes) * 100 if total_nodes > 0 else 0
                },
                'holographic': {
                    'count': holographic_count,
                    'percentage': (holographic_count / total_nodes) * 100 if total_nodes > 0 else 0
                }
            }
        }
    
    def _get_water_states_mapping(self) -> Dict[str, Any]:
        """Get water state consciousness mapping"""
        water_states = {}
        for node in fractal_core_system.nodes.values():
            water_state = node.metadata.get('water_state')
            if water_state:
                if water_state not in water_states:
                    water_states[water_state] = []
                water_states[water_state].append({
                    'node_id': node.node_id,
                    'name': node.name,
                    'type': node.node_type
                })
        
        return {
            'water_states': {state: {'count': len(nodes), 'nodes': nodes} 
                            for state, nodes in water_states.items()}
        }
    
    def _get_chakras_mapping(self) -> Dict[str, Any]:
        """Get chakra energy mapping"""
        chakras = {}
        for node in fractal_core_system.nodes.values():
            chakra = node.metadata.get('chakra')
            if chakra:
                if chakra not in chakras:
                    chakras[chakra] = []
                chakras[chakra].append({
                    'node_id': node.node_id,
                    'name': node.name,
                    'type': node.node_type
                })
        
        return {
            'chakras': {chakra: {'count': len(nodes), 'nodes': nodes} 
                       for chakra, nodes in chakras.items()}
        }
    
    def _get_frequencies_mapping(self) -> Dict[str, Any]:
        """Get frequency vibrational mapping"""
        frequencies = {}
        for node in fractal_core_system.nodes.values():
            frequency = node.metadata.get('frequency')
            if frequency:
                if frequency not in frequencies:
                    frequencies[frequency] = []
                frequencies[frequency].append({
                    'node_id': node.node_id,
                    'name': node.name,
                    'type': node.node_type
                })
        
        return {
            'frequencies': {str(freq): {'count': len(nodes), 'nodes': nodes} 
                           for freq, nodes in frequencies.items()}
        }
    
    def _get_quantum_consciousness_mapping(self) -> Dict[str, Any]:
        """Get quantum consciousness mapping"""
        quantum_nodes = [node for node in fractal_core_system.nodes.values() 
                        if node.metadata.get('category') == 'quantum' or 
                           node.metadata.get('category') == 'consciousness']
        
        return {
            'quantum_consciousness_nodes': len(quantum_nodes),
            'nodes': [node.to_dict() for node in quantum_nodes]
        }
    
    def get_api_documentation(self) -> Dict[str, Any]:
        """Get comprehensive API documentation"""
        return {
            'api_name': self.name,
            'version': self.version,
            'base_url': self.base_url,
            'endpoints': self.endpoints,
            'rate_limits': self.rate_limits,
            'authentication': 'Not required for read operations',
            'examples': self._get_api_examples()
        }
    
    def _get_api_examples(self) -> Dict[str, Any]:
        """Get API usage examples"""
        return {
            'get_system_status': {
                'endpoint': 'GET /system/status',
                'description': 'Get comprehensive system status',
                'response': 'System status information'
            },
            'search_nodes': {
                'endpoint': 'GET /search?query=fractal',
                'description': 'Search for nodes containing "fractal"',
                'response': 'List of matching nodes'
            },
            'get_fractal_layers': {
                'endpoint': 'GET /fractal/layers',
                'description': 'Get information about fractal layers',
                'response': 'Fractal layer analysis'
            }
        }


def main():
    """Main function to demonstrate the unified API system"""
    logging.basicConfig(level=logging.INFO)
    
    print("🔌 Living Codex Unified API System")
    print("=" * 50)
    
    # Initialize the API system
    api_system = UnifiedAPISystem()
    
    # Show API documentation
    print(f"\n📚 API Documentation:")
    print(f"Name: {api_system.name}")
    print(f"Version: {api_system.version}")
    print(f"Base URL: {api_system.base_url}")
    
    print(f"\n📋 Available Endpoint Categories ({len(api_system.endpoints)}):")
    for category_id, category_info in api_system.endpoints.items():
        print(f"  • {category_id}: {category_info['name']} - {category_info['description']}")
        print(f"    Endpoints: {len(category_info['endpoints'])}")
    
    # Test a simple API call
    print(f"\n🧪 Testing API call...")
    response = api_system.handle_request('/system/status', 'GET', {})
    
    if response.success:
        print(f"✅ API call successful!")
        print(f"Response time: {response.processing_time:.3f}s")
        print(f"Data keys: {list(response.data.keys()) if response.data else 'None'}")
    else:
        print(f"❌ API call failed: {response.message}")


if __name__ == "__main__":
    main()
