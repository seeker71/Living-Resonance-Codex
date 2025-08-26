# Core system components (always available)
from .core_system import fractal_core_system, GenericNode
from .fractal_components import initialize_fractal_components

# Fractal components (imported conditionally to avoid conflicts)
try:
    from .code_parser import fractal_code_parser
    from .code_navigation_api import fractal_code_navigation
    from .code_reflector import fractal_code_reflector
    from .dependency_manager import DependencyManager
    from .neo4j_integration_system import Neo4jIntegrationSystem
    from .digital_asset_manager import DigitalAssetManager
    from .database_persistence_system import DatabasePersistenceSystem
    from .inventory_report_system import inventory_report_system, initialize_inventory_report_system
except ImportError:
    # These components may not be available in all environments
    pass

__all__ = [
    # Core system
    'fractal_core_system',
    'GenericNode',
    'initialize_fractal_components',
    
    # Fractal components (may be None if import failed)
    'fractal_code_parser',
    'fractal_code_navigation', 
    'fractal_code_reflector',
    'DependencyManager',
    'Neo4jIntegrationSystem',
    'DigitalAssetManager',
    'DatabasePersistenceSystem',
    'inventory_report_system',
    'initialize_inventory_report_system'
]
