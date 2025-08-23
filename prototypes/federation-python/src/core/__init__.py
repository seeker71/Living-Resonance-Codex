# Core system components (always available)
from .water_state_storage import WaterStateStorage
from .ice_bootstrap_engine import ICEBootstrapEngine
from .ice_core_creator import ICECoreCreator

# Legacy components (imported conditionally to avoid conflicts)
try:
    from .explore_bootstrapped_system import BootstrappedSystemExplorer
    from .database_persistence_system import DatabasePersistenceSystem
    from .digital_asset_manager import DigitalAssetManager
    from .code_parser import CodeParser
    from .code_navigation_api import CodeNavigationAPI
    from .real_external_api_system import RealExternalAPISystem
    from .neo4j_integration_system import Neo4jIntegrationSystem
except ImportError:
    # These components may not be available in all environments
    pass

__all__ = [
    # Core components
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
