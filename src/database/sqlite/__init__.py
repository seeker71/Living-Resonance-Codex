"""
SQLite Database Package
SQLite-specific database implementation for the Living Codex system
"""

from .sqlite_manager import SQLiteManager

__all__ = [
    "SQLiteManager"
]

# Additional components will be added as they are implemented
# from .sqlite_operations import SQLiteOperations
