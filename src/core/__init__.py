#!/usr/bin/env python3
"""
Core System Module - Living Codex Foundation

This module implements the Living Codex principle: "Everything is just nodes"
where the core system is represented as nodes that can:

1. Import and manage all core components (as nodes)
2. Provide node-based access to system functionality
3. Maintain backward compatibility for legacy systems
4. Create a unified node-based core system

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Core System represents the Blueprint (Ice) state in the programming language ontology.
"""

from typing import Optional, List, Dict, Any

# Import the Shared Node System and GenericNode
from .shared_node_system import SharedNodeSystem
from .generic_node_system import GenericNode

class CoreSystemNodeManager(SharedNodeSystem):
    """
    Core System Node Manager using Generic Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Core components are nodes
    - System structure is nodes
    - Everything emerges through the system's own operation
    
    The Core System represents the Blueprint (Ice) state in the programming language ontology:
    - Grammar, syntax rules, language structure
    - Class definitions, inheritance
    - Module structure, imports
    - Type system, static analysis framework
    """
    
    def __init__(self):
        super().__init__("CoreSystemNodeManager")
        self._initialize_core_system_nodes()
        self._import_core_components()
        self._create_component_nodes()
    
    def _initialize_core_system_nodes(self):
        """
        Initialize core system nodes - the foundation of the entire system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root core system node
        root_node = self.create_node(
            node_type='core_system_root',
            name='Living Codex Core System Root',
            content='This is the root node of the Living Codex Core System. It represents the complete foundation that everything else builds upon.',
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,  # Fractal System Root
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Unity',
                'quantum_state': 'coherent',
                'resonance_score': 1.0,
                'epistemic_label': 'engineering',
                'system_principle': 'Everything is just nodes - core system as foundation',
                'meta_circular': True,
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Complete foundation for the Living Codex system'
            }
        )
        
        # Create the Core Foundation node
        core_foundation_node = self.create_node(
            node_type='core_foundation',
            name='Core Foundation - System Blueprint',
            content='Core Foundation represents the system blueprint - the immutable foundation that everything else builds upon',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.95,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Immutable foundation blueprint for the complete system'
            }
        )
        
        # Create the Component Management node
        component_management_node = self.create_node(
            node_type='component_management',
            name='Component Management - Integration Blueprint',
            content='Component Management represents the integration blueprint - manages all core components as nodes',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Integration blueprint for core component management'
            }
        )
        
        # Create the Legacy Compatibility node
        legacy_compatibility_node = self.create_node(
            node_type='legacy_compatibility',
            name='Legacy Compatibility - Evolution Blueprint',
            content='Legacy Compatibility represents the evolution blueprint - maintains backward compatibility while evolving to nodes',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.85,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Evolution blueprint for maintaining backward compatibility'
            }
        )
        
        print(f"🌟 Core System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"🧊 Core Foundation: {core_foundation_node.name} (ID: {core_foundation_node.node_id})")
        print(f"🔧 Component Management: {component_management_node.name} (ID: {component_management_node.node_id})")
        print(f"🔄 Legacy Compatibility: {legacy_compatibility_node.name} (ID: {legacy_compatibility_node.node_id})")
    
    def _import_core_components(self):
        """Import all core components"""
        try:
            # Import transformed components
            from .water_state_storage import WaterStateStorage
            from .ice_bootstrap_engine import ICEBootstrapEngine
            from .ice_core_creator import ICECoreCreator
            
            # Store imported components
            self.water_state_storage = WaterStateStorage
            self.ice_bootstrap_engine = ICEBootstrapEngine
            self.ice_core_creator = ICECoreCreator
            
            print("✅ Core components imported successfully")
            
        except ImportError as e:
            print(f"❌ Failed to import core components: {e}")
            self.water_state_storage = None
            self.ice_bootstrap_engine = None
            self.ice_core_creator = None
    
    def _create_component_nodes(self):
        """Create nodes for all core components"""
        
        # Create Water State Storage component node
        if self.water_state_storage:
            water_storage_node = self.create_node(
                node_type='core_component',
                name='Water State Storage Component',
                content='Water State Storage component - manages water states as nodes',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'water_state_storage',
                    'component_class': 'WaterStateStorage',
                    'status': 'transformed',
                    'description': 'Water state storage system using generic node structure'
                }
            )
        
        # Create ICE Bootstrap Engine component node
        if self.ice_bootstrap_engine:
            ice_bootstrap_node = self.create_node(
                node_type='core_component',
                name='ICE Bootstrap Engine Component',
                content='ICE Bootstrap Engine component - manages bootstrap system as nodes',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'ice_bootstrap_engine',
                    'component_class': 'ICEBootstrapEngine',
                    'status': 'transformed',
                    'description': 'ICE bootstrap engine using generic node structure'
                }
            )
        
        # Create ICE Core Creator component node
        if self.ice_core_creator:
            ice_creator_node = self.create_node(
                node_type='core_component',
                name='ICE Core Creator Component',
                content='ICE Core Creator component - manages core creation as nodes',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'ice_core_creator',
                    'component_class': 'ICECoreCreator',
                    'status': 'transformed',
                    'description': 'ICE core creator using generic node structure'
                }
            )
        
        # Try to import legacy components
        self._import_legacy_components()
    
    def _import_legacy_components(self):
        """Import legacy components conditionally"""
        try:
            from .explore_bootstrapped_system import BootstrappedSystemExplorer
            self.bootstrapped_system_explorer = BootstrappedSystemExplorer
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Bootstrapped System Explorer Component',
                content='Legacy component - Bootstrapped System Explorer',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'explore_bootstrapped_system',
                    'component_class': 'BootstrappedSystemExplorer',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.bootstrapped_system_explorer = None
        
        try:
            from .database_persistence_system import DatabasePersistenceSystem
            self.database_persistence_system = DatabasePersistenceSystem
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Database Persistence System Component',
                content='Legacy component - Database Persistence System',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'database_persistence_system',
                    'component_class': 'DatabasePersistenceSystem',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.database_persistence_system = None
        
        try:
            from .digital_asset_manager import DigitalAssetManager
            self.digital_asset_manager = DigitalAssetManager
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Digital Asset Manager Component',
                content='Legacy component - Digital Asset Manager',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'digital_asset_manager',
                    'component_class': 'DigitalAssetManager',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.digital_asset_manager = None
        
        try:
            from .code_parser import CodeParser
            self.code_parser = CodeParser
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Code Parser Component',
                content='Legacy component - Code Parser',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'code_parser',
                    'component_class': 'CodeParser',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.code_parser = None
        
        try:
            from .code_navigation_api import CodeNavigationAPI
            self.code_navigation_api = CodeNavigationAPI
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Code Navigation API Component',
                content='Legacy component - Code Navigation API',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'code_navigation_api',
                    'component_class': 'CodeNavigationAPI',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.code_navigation_api = None
        
        try:
            from .real_external_api_system import RealExternalAPISystem
            self.real_external_api_system = RealExternalAPISystem
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Real External API System Component',
                content='Legacy component - Real External API System',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'real_external_api_system',
                    'component_class': 'RealExternalAPISystem',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.real_external_api_system = None
        
        try:
            from .neo4j_integration_system import Neo4jIntegrationSystem
            self.neo4j_integration_system = Neo4jIntegrationSystem
            
            # Create legacy component node
            self.create_node(
                node_type='legacy_component',
                name='Neo4j Integration System Component',
                content='Legacy component - Neo4j Integration System',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.7,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_type': 'neo4j_integration_system',
                    'component_class': 'Neo4jIntegrationSystem',
                    'status': 'legacy',
                    'description': 'Legacy component - not yet transformed to nodes'
                }
            )
            
        except ImportError:
            self.neo4j_integration_system = None
    
    def get_component_node(self, component_name: str) -> Optional[GenericNode]:
        """Get a component node by name"""
        for node in self.nodes.values():
            if (node.node_type in ['core_component', 'legacy_component'] and 
                node.metadata.get('component_type') == component_name):
                return node
        return None
    
    def get_all_core_components(self) -> List[GenericNode]:
        """Get all core component nodes"""
        return [node for node in self.nodes.values() if node.node_type == 'core_component']
    
    def get_all_legacy_components(self) -> List[GenericNode]:
        """Get all legacy component nodes"""
        return [node for node in self.nodes.values() if node.node_type == 'legacy_component']
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        core_nodes = [node for node in self.nodes.values() if node.node_type == 'core_system_root']
        foundation_nodes = [node for node in self.nodes.values() if node.node_type == 'core_foundation']
        component_nodes = [node for node in self.nodes.values() if node.node_type == 'core_component']
        legacy_nodes = [node for node in self.nodes.values() if node.node_type == 'legacy_component']
        
        return {
            'total_nodes': len(self.nodes),
            'core_system_nodes': len(core_nodes),
            'foundation_nodes': len(foundation_nodes),
            'component_nodes': len(component_nodes),
            'legacy_nodes': len(legacy_nodes),
            'water_states': list(set(node.get_water_state() for node in self.nodes.values())),
            'chakras': list(set(node.get_chakra() for node in self.nodes.values())),
            'frequencies': list(set(node.get_frequency() for node in self.nodes.values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.nodes.values()) / max(len(self.nodes), 1),
            'system_principle': 'Everything is just nodes - core system as foundation nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'ice_blueprint_layer'
        }

# Create the core system instance
_core_system = CoreSystemNodeManager()

# Legacy compatibility - maintain the old interface for now
WaterStateStorage = _core_system.water_state_storage
ICEBootstrapEngine = _core_system.ice_bootstrap_engine
ICECoreCreator = _core_system.ice_core_creator

# Legacy components (may be None if import failed)
BootstrappedSystemExplorer = _core_system.bootstrapped_system_explorer
DatabasePersistenceSystem = _core_system.database_persistence_system
DigitalAssetManager = _core_system.digital_asset_manager
CodeParser = _core_system.code_parser
CodeNavigationAPI = _core_system.code_navigation_api
RealExternalAPISystem = _core_system.real_external_api_system
Neo4jIntegrationSystem = _core_system.neo4j_integration_system

__all__ = [
    # Core system
    '_core_system',
    
    # Core components (transformed to nodes)
    'WaterStateStorage',
    'ICEBootstrapEngine', 
    'ICECoreCreator',
    
    # Legacy components (may be None if import failed)
    'BootstrappedSystemExplorer',
    'DatabasePersistenceSystem',
    'DigitalAssetManager',
    'CodeParser',
    'CodeNavigationAPI',
    'RealExternalAPISystem',
    'Neo4jIntegrationSystem'
]

print("🌟 Living Codex Core System initialized with node-based architecture")
print("✨ Everything is just nodes - no predefined concepts, tables, or schemas")
print("🧊 Core system represents Blueprint (Ice) state in programming language ontology")
