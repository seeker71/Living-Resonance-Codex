#!/usr/bin/env python3
"""
Living Codex Ontology Navigator
Provides structured navigation through system components, relationships, and knowledge structures
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timezone
import json

@dataclass
class OntologyNode:
    """Represents a node in the Living Codex ontology"""
    id: str
    name: str
    type: str
    description: str
    category: str
    relationships: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

@dataclass
class OntologyRelationship:
    """Represents a relationship between ontology nodes"""
    id: str
    source_id: str
    target_id: str
    relationship_type: str
    description: str
    strength: float  # 0.0 to 1.0
    metadata: Dict[str, Any]

class OntologyNavigator:
    """Navigates through the Living Codex ontology"""
    
    def __init__(self):
        self.nodes = {}
        self.relationships = {}
        self.categories = {}
        self._initialize_ontology()
    
    def _initialize_ontology(self):
        """Initialize the Living Codex ontology with system components"""
        
        # Core System Components
        core_components = [
            {
                'id': 'ice_core',
                'name': 'ICE Core Bootstrap System',
                'type': 'system_component',
                'description': 'Immutable core system that provides self-bootstrapping capabilities',
                'category': 'core_system',
                'relationships': ['water_state', 'bootstrap_engine', 'dependency_manager'],
                'metadata': {
                    'file_path': 'src/core/minimal_ice_bootstrap.py',
                    'complexity': 'high',
                    'dependencies': ['dependency_manager', 'user_management', 'contribution_system'],
                    'status': 'active'
                }
            },
            {
                'id': 'water_state',
                'name': 'WATER State System',
                'type': 'system_component',
                'description': 'Operational system state that handles dynamic operations',
                'category': 'operational_system',
                'relationships': ['ice_core', 'vapor_state', 'plasma_state'],
                'metadata': {
                    'file_path': 'src/core/water_state_storage.py',
                    'complexity': 'medium',
                    'dependencies': ['ice_core', 'user_management'],
                    'status': 'active'
                }
            },
            {
                'id': 'vapor_state',
                'name': 'VAPOR State System',
                'type': 'system_component',
                'description': 'Temporary interaction state for user sessions and collaborations',
                'category': 'interaction_system',
                'relationships': ['water_state', 'plasma_state'],
                'metadata': {
                    'file_path': 'src/core/vapor_state_manager.py',
                    'complexity': 'medium',
                    'dependencies': ['water_state', 'user_management'],
                    'status': 'active'
                }
            },
            {
                'id': 'plasma_state',
                'name': 'PLASMA State System',
                'type': 'system_component',
                'description': 'Real-time streaming and collaboration state',
                'category': 'collaboration_system',
                'relationships': ['vapor_state', 'water_state'],
                'metadata': {
                    'file_path': 'src/core/plasma_state_manager.py',
                    'complexity': 'high',
                    'dependencies': ['vapor_state', 'real_time_engine'],
                    'status': 'active'
                }
            },
            {
                'id': 'bootstrap_engine',
                'name': 'Bootstrap Engine',
                'type': 'system_component',
                'description': 'Engine that handles system initialization and validation',
                'category': 'core_system',
                'relationships': ['ice_core', 'dependency_manager'],
                'metadata': {
                    'file_path': 'src/core/ice_bootstrap_engine.py',
                    'complexity': 'high',
                    'dependencies': ['dependency_manager'],
                    'status': 'active'
                }
            },
            {
                'id': 'dependency_manager',
                'name': 'Dependency Manager',
                'type': 'system_component',
                'description': 'Manages external dependencies and system requirements',
                'category': 'core_system',
                'relationships': ['ice_core', 'bootstrap_engine'],
                'metadata': {
                    'file_path': 'src/core/dependency_manager.py',
                    'complexity': 'medium',
                    'dependencies': ['pkg_resources', 'subprocess'],
                    'status': 'active'
                }
            },
            {
                'id': 'user_management',
                'name': 'User Management System',
                'type': 'platform_component',
                'description': 'Handles user profiles, authentication, and management',
                'category': 'platform_system',
                'relationships': ['ice_core', 'contribution_system', 'web_interface'],
                'metadata': {
                    'file_path': 'src/web_platform/user_management.py',
                    'complexity': 'medium',
                    'dependencies': ['flask_login', 'dataclasses'],
                    'status': 'active'
                }
            },
            {
                'id': 'contribution_system',
                'name': 'Contribution System',
                'type': 'platform_component',
                'description': 'Manages content contributions and collaboration',
                'category': 'platform_system',
                'relationships': ['user_management', 'web_interface'],
                'metadata': {
                    'file_path': 'src/web_platform/contribution_system.py',
                    'complexity': 'medium',
                    'dependencies': ['user_management', 'enums'],
                    'status': 'active'
                }
            },
            {
                'id': 'web_interface',
                'name': 'Unified Web Interface',
                'type': 'platform_component',
                'description': 'Main web interface that integrates all platform modules',
                'category': 'platform_system',
                'relationships': ['user_management', 'contribution_system', 'discovery_engine'],
                'metadata': {
                    'file_path': 'src/web_platform/unified_web_interface.py',
                    'complexity': 'high',
                    'dependencies': ['flask', 'flask_login', 'all_modules'],
                    'status': 'active'
                }
            },
            {
                'id': 'discovery_engine',
                'name': 'Discovery Engine',
                'type': 'platform_module',
                'description': 'Smart user matching and content discovery system',
                'category': 'discovery_system',
                'relationships': ['web_interface', 'user_management'],
                'metadata': {
                    'file_path': 'src/web_platform/unified_web_interface.py',
                    'complexity': 'medium',
                    'dependencies': ['user_management'],
                    'status': 'active'
                }
            },
            {
                'id': 'navigation_system',
                'name': 'Navigation System',
                'type': 'platform_module',
                'description': 'Personalized exploration paths and progress tracking',
                'category': 'navigation_system',
                'relationships': ['web_interface', 'user_management'],
                'metadata': {
                    'file_path': 'src/web_platform/unified_web_interface.py',
                    'complexity': 'medium',
                    'dependencies': ['user_management'],
                    'status': 'active'
                }
            }
        ]
        
        # Create ontology nodes
        for component in core_components:
            self.nodes[component['id']] = OntologyNode(
                id=component['id'],
                name=component['name'],
                type=component['type'],
                description=component['description'],
                category=component['category'],
                relationships=component['relationships'],
                metadata=component['metadata'],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
        
        # Create relationships
        self._create_relationships()
        
        # Create categories
        self._create_categories()
    
    def _create_relationships(self):
        """Create relationships between ontology nodes"""
        relationship_data = [
            ('ice_core', 'water_state', 'creates', 'ICE core creates WATER state'),
            ('water_state', 'vapor_state', 'transforms_to', 'WATER transforms to VAPOR'),
            ('vapor_state', 'plasma_state', 'transforms_to', 'VAPOR transforms to PLASMA'),
            ('plasma_state', 'water_state', 'condenses_to', 'PLASMA condenses to WATER'),
            ('ice_core', 'bootstrap_engine', 'uses', 'ICE core uses bootstrap engine'),
            ('bootstrap_engine', 'dependency_manager', 'requires', 'Bootstrap requires dependencies'),
            ('user_management', 'contribution_system', 'enables', 'Users enable contributions'),
            ('web_interface', 'discovery_engine', 'integrates', 'Web interface integrates discovery'),
            ('web_interface', 'navigation_system', 'integrates', 'Web interface integrates navigation'),
            ('discovery_engine', 'user_management', 'uses', 'Discovery uses user data'),
            ('navigation_system', 'user_management', 'uses', 'Navigation uses user data')
        ]
        
        for i, (source, target, rel_type, description) in enumerate(relationship_data):
            rel_id = f"rel_{i+1}"
            self.relationships[rel_id] = OntologyRelationship(
                id=rel_id,
                source_id=source,
                target_id=target,
                relationship_type=rel_type,
                description=description,
                strength=0.8,
                metadata={'bidirectional': False}
            )
    
    def _create_categories(self):
        """Create category groupings"""
        self.categories = {
            'core_system': {
                'name': 'Core System Components',
                'description': 'Fundamental system components that provide core functionality',
                'color': '#4CAF50',
                'icon': '🔧'
            },
            'operational_system': {
                'name': 'Operational Systems',
                'description': 'Systems that handle day-to-day operations',
                'color': '#2196F3',
                'icon': '⚙️'
            },
            'interaction_system': {
                'name': 'Interaction Systems',
                'description': 'Systems that handle user interactions and sessions',
                'color': '#FF9800',
                'icon': '🤝'
            },
            'collaboration_system': {
                'name': 'Collaboration Systems',
                'description': 'Systems that enable real-time collaboration',
                'color': '#9C27B0',
                'icon': '🚀'
            },
            'platform_system': {
                'name': 'Platform Systems',
                'description': 'Core platform functionality and management',
                'color': '#607D8B',
                'icon': '🏗️'
            },
            'discovery_system': {
                'name': 'Discovery Systems',
                'description': 'Systems that enable content and user discovery',
                'color': '#E91E63',
                'icon': '🔍'
            },
            'navigation_system': {
                'name': 'Navigation Systems',
                'description': 'Systems that provide navigation and guidance',
                'color': '#795548',
                'icon': '🧭'
            }
        }
    
    def get_ontology_overview(self) -> Dict[str, Any]:
        """Get an overview of the ontology"""
        return {
            'total_nodes': len(self.nodes),
            'total_relationships': len(self.relationships),
            'total_categories': len(self.categories),
            'categories': self.categories,
            'node_types': list(set(node.type for node in self.nodes.values())),
            'recent_updates': sorted(
                [{'id': node.id, 'name': node.name, 'updated': node.updated_at} 
                 for node in self.nodes.values()],
                key=lambda x: x['updated'],
                reverse=True
            )[:5]
        }
    
    def get_nodes_by_category(self, category: str) -> List[OntologyNode]:
        """Get all nodes in a specific category"""
        return [node for node in self.nodes.values() if node.category == category]
    
    def get_node_details(self, node_id: str) -> Optional[OntologyNode]:
        """Get detailed information about a specific node"""
        return self.nodes.get(node_id)
    
    def get_node_relationships(self, node_id: str) -> List[Dict[str, Any]]:
        """Get all relationships for a specific node"""
        relationships = []
        for rel in self.relationships.values():
            if rel.source_id == node_id or rel.target_id == node_id:
                target_id = rel.target_id if rel.source_id == node_id else rel.source_id
                target_node = self.nodes.get(target_id)
                relationships.append({
                    'relationship': rel,
                    'target_node': target_node,
                    'direction': 'outgoing' if rel.source_id == node_id else 'incoming'
                })
        return relationships
    
    def search_nodes(self, query: str) -> List[OntologyNode]:
        """Search for nodes by name, description, or category"""
        query = query.lower()
        results = []
        for node in self.nodes.values():
            if (query in node.name.lower() or 
                query in node.description.lower() or 
                query in node.category.lower() or
                query in node.type.lower()):
                results.append(node)
        return results
    
    def get_system_architecture(self) -> Dict[str, Any]:
        """Get the system architecture overview"""
        architecture = {
            'layers': {
                'ice_layer': {
                    'name': 'ICE Layer (Immutable Core)',
                    'components': self.get_nodes_by_category('core_system'),
                    'description': 'Foundation layer providing self-bootstrapping capabilities'
                },
                'water_layer': {
                    'name': 'WATER Layer (Operational)',
                    'components': self.get_nodes_by_category('operational_system'),
                    'description': 'Operational layer handling day-to-day system operations'
                },
                'vapor_layer': {
                    'name': 'VAPOR Layer (Interaction)',
                    'components': self.get_nodes_by_category('interaction_system'),
                    'description': 'Interaction layer managing user sessions and interactions'
                },
                'plasma_layer': {
                    'name': 'PLASMA Layer (Collaboration)',
                    'components': self.get_nodes_by_category('collaboration_system'),
                    'description': 'Collaboration layer enabling real-time teamwork'
                },
                'platform_layer': {
                    'name': 'Platform Layer (Integration)',
                    'components': self.get_nodes_by_category('platform_system'),
                    'description': 'Platform layer integrating all systems and modules'
                }
            },
            'flows': [
                {
                    'name': 'ICE → WATER → VAPOR → PLASMA',
                    'description': 'Primary transformation flow through system states',
                    'components': ['ice_core', 'water_state', 'vapor_state', 'plasma_state']
                },
                {
                    'name': 'User → Discovery → Navigation → Contribution',
                    'description': 'User experience flow through platform modules',
                    'components': ['user_management', 'discovery_engine', 'navigation_system', 'contribution_system']
                }
            ]
        }
        return architecture

# Global instance
ontology_navigator = OntologyNavigator()
