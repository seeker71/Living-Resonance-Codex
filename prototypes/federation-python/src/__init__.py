"""
Living Codex - Source Package
Modular, maintainable architecture for intelligent knowledge systems
"""

__version__ = "2.0.0"
__author__ = "Living Codex Team"
__description__ = "Modular Living Codex System"

# Import main components for easy access
from .config.manager import ConfigManager
from .api.integration.external_api_system import RealExternalAPISystem
from .database.persistence.database_system import DatabasePersistenceSystem
from .graph.integration.neo4j_system import Neo4jIntegrationSystem

__all__ = [
    "ConfigManager",
    "RealExternalAPISystem", 
    "DatabasePersistenceSystem",
    "Neo4jIntegrationSystem"
]
