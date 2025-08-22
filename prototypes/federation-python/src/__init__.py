"""
Living Codex - Source Package
Modular, maintainable architecture for intelligent knowledge systems
"""

__version__ = "2.0.0"
__author__ = "Living Codex Team"
__description__ = "Modular Living Codex System"

# Import main components for easy access
from .config.manager import ConfigManager

# Core modules
from .core.database_persistence_system import DatabasePersistenceSystem
from .core.digital_asset_manager import DigitalAssetManager
from .core.code_parser import CodeParser
from .core.code_navigation_api import CodeNavigationAPI

# Demo modules
from .demos import (
    AutonomousLearningSystem,
    AutonomousDecisionDemo,
    demo_code_navigation,
    demo_parsing,
    demo_queries,
    demo_cli_integration,
    demo_cli_commands
)

__all__ = [
    "ConfigManager",
    "DatabasePersistenceSystem",
    "DigitalAssetManager", 
    "CodeParser",
    "CodeNavigationAPI",
    "AutonomousLearningSystem",
    "AutonomousDecisionDemo",
    "demo_code_navigation",
    "demo_parsing",
    "demo_queries",
    "demo_cli_integration",
    "demo_cli_commands"
]
