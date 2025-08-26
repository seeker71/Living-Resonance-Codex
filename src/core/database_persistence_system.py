#!/usr/bin/env python3
"""
Fractal Database Persistence System Component - Living Codex
Provides persistent storage for fractal nodes using SQLite and PostgreSQL,
with support for content-addressed storage and recursive data structures.

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level

UPDATED: Now uses modular components from src/database/ while maintaining backward compatibility
"""

import os
import json
import sqlite3
import hashlib
import asyncio
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import logging

from .fractal_components import FractalComponent

# Import new modular components
try:
    # Try relative imports first (when used as package)
    from ..database.core.models import (
        DatabaseNode, DatabaseOperationResult, QueryFilter, QueryOptions,
        DatabaseType, OperationType
    )
    from ..database.core.operations import DatabaseOperations
    from ..database.sqlite.sqlite_manager import SQLiteManager
    MODULAR_IMPORTS_AVAILABLE = True
    print("✅ Using new modular database components")
except ImportError:
    try:
        # Try absolute imports (when src is in path, e.g., CLI)
        from database.core.models import (
            DatabaseNode, DatabaseOperationResult, QueryFilter, QueryOptions,
            DatabaseType, OperationType
        )
        from database.core.operations import DatabaseOperations
        from database.sqlite.sqlite_manager import SQLiteManager
        MODULAR_IMPORTS_AVAILABLE = True
        print("✅ Using new modular database components")
    except ImportError:
        MODULAR_IMPORTS_AVAILABLE = False
        print("⚠️  Modular imports not available, using legacy components")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Legacy enums and models (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
    class DatabaseType(Enum):
        """Types of databases supported"""
        SQLITE = "sqlite"
        POSTGRESQL = "postgresql"
        MEMORY = "memory"

    class OperationType(Enum):
        """Types of database operations"""
        CREATE = "create"
        READ = "read"
        UPDATE = "update"
        DELETE = "delete"
        QUERY = "query"
        MIGRATE = "migrate"

    @dataclass
    class DatabaseNode:
        """Represents a node in the database"""
        node_id: str
        node_type: str
        content_hash: str
        content: Dict[str, Any]
        metadata: Dict[str, Any]
        created_at: datetime
        updated_at: datetime
        fractal_id: Optional[str] = None
        water_state: Optional[str] = None
        energy_level: Optional[float] = None

    @dataclass
    class DatabaseOperationResult:
        """Result of a database operation"""
        operation_type: OperationType
        success: bool
        data: Any
        execution_time: float
        timestamp: datetime
        metadata: Dict[str, Any]
        error_message: Optional[str] = None

    @dataclass
    class QueryFilter:
        """Filter for database queries"""
        field: str
        operator: str  # eq, ne, gt, lt, gte, lte, like, in
        value: Any
        logical_operator: str = "AND"  # AND, OR

    @dataclass
    class QueryOptions:
        """Options for database queries"""
        limit: Optional[int] = None
        offset: Optional[int] = None
        order_by: Optional[str] = None
        order_direction: str = "ASC"  # ASC, DESC

    class DatabaseOperations:
        """Legacy database operations class"""
        def __init__(self, db_manager):
            self.db_manager = db_manager
        
        def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
            """Legacy create method"""
            return self.db_manager.create_node(node)
        
        def read_node(self, node_id: str) -> DatabaseOperationResult:
            """Legacy read method"""
            return self.db_manager.read_node(node_id)
        
        def update_node(self, node: DatabaseNode) -> DatabaseOperationResult:
            """Legacy update method"""
            return self.db_manager.update_node(node)
        
        def delete_node(self, node_id: str) -> DatabaseOperationResult:
            """Legacy delete method"""
            return self.db_manager.delete_node(node_id)
        
        def query_nodes(self, filters: List[QueryFilter], options: QueryOptions = None) -> DatabaseOperationResult:
            """Legacy query method"""
            return self.db_manager.query_nodes(filters, options)

class FractalDatabasePersistenceComponent(FractalComponent):
    """
    Fractal component for database persistence functionality
    Provides persistent storage for fractal nodes using multiple database backends
    """
    
    def __init__(self):
        super().__init__(
            component_type="database_persistence_system",
            name="Fractal Database Persistence System",
            content="Database persistence system for storing fractal nodes",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        # Initialize database components
        self.db_operations = None
        self.sqlite_manager = None
        self.initialized = False
        
        # Create database capability nodes
        self._create_database_capability_nodes()
        
        # Initialize database connection
        self._initialize_database()
    
    def _create_database_capability_nodes(self):
        """Create fractal nodes for database capabilities"""
        capabilities = [
            {
                "name": "SQLite Storage",
                "content": "SQLite database backend for local storage",
                "metadata": {"backend": "sqlite", "type": "local", "scalability": "medium"}
            },
            {
                "name": "PostgreSQL Storage",
                "content": "PostgreSQL database backend for production storage",
                "metadata": {"backend": "postgresql", "type": "production", "scalability": "high"}
            },
            {
                "name": "Content-Addressed Storage",
                "content": "Store data using content hashes for deduplication",
                "metadata": {"feature": "content_addressing", "benefit": "deduplication"}
            },
            {
                "name": "Recursive Data Structures",
                "content": "Support for nested and recursive data structures",
                "metadata": {"feature": "recursive_structures", "complexity": "high"}
            },
            {
                "name": "Fractal Node Mapping",
                "content": "Map fractal nodes to database storage",
                "metadata": {"feature": "fractal_mapping", "integration": "core_system"}
            }
        ]
        
        for capability in capabilities:
            self.create_child_node(
                node_type="database_capability",
                name=capability["name"],
                content=capability["content"],
                metadata=capability["metadata"],
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _initialize_database(self):
        """Initialize database connection and operations"""
        try:
            if MODULAR_IMPORTS_AVAILABLE:
                # Use modular components
                self.sqlite_manager = SQLiteManager()
                self.db_operations = DatabaseOperations(self.sqlite_manager)
                self.initialized = True
                logger.info("✅ Database initialized with modular components")
            else:
                # Use legacy components
                self.initialized = False
                logger.warning("⚠️  Database not fully initialized - modular components unavailable")
        except Exception as e:
            logger.error(f"❌ Failed to initialize database: {e}")
            self.initialized = False
    
    def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
        """Create a new node in the database"""
        if not self.initialized:
            return DatabaseOperationResult(
                operation_type=OperationType.CREATE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={},
                error_message="Database not initialized"
            )
        
        try:
            result = self.db_operations.create_node(node)
            
            # Create fractal node for the database operation
            self._create_operation_node("create", node.node_id, result.success)
            
            return result
        except Exception as e:
            logger.error(f"Error creating node {node.node_id}: {e}")
            return DatabaseOperationResult(
                operation_type=OperationType.CREATE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id},
                error_message=str(e)
            )
    
    def read_node(self, node_id: str) -> DatabaseOperationResult:
        """Read a node from the database"""
        if not self.initialized:
            return DatabaseOperationResult(
                operation_type=OperationType.READ,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message="Database not initialized"
            )
        
        try:
            result = self.db_operations.read_node(node_id)
            
            # Create fractal node for the database operation
            self._create_operation_node("read", node_id, result.success)
            
            return result
        except Exception as e:
            logger.error(f"Error reading node {node_id}: {e}")
            return DatabaseOperationResult(
                operation_type=OperationType.READ,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def update_node(self, node: DatabaseNode) -> DatabaseOperationResult:
        """Update a node in the database"""
        if not self.initialized:
            return DatabaseOperationResult(
                operation_type=OperationType.UPDATE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id},
                error_message="Database not initialized"
            )
        
        try:
            result = self.db_operations.update_node(node)
            
            # Create fractal node for the database operation
            self._create_operation_node("update", node.node_id, result.success)
            
            return result
        except Exception as e:
            logger.error(f"Error updating node {node.node_id}: {e}")
            return DatabaseOperationResult(
                operation_type=OperationType.UPDATE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id},
                error_message=str(e)
            )
    
    def delete_node(self, node_id: str) -> DatabaseOperationResult:
        """Delete a node from the database"""
        if not self.initialized:
            return DatabaseOperationResult(
                operation_type=OperationType.DELETE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message="Database not initialized"
            )
        
        try:
            result = self.db_operations.delete_node(node_id)
            
            # Create fractal node for the database operation
            self._create_operation_node("delete", node_id, result.success)
            
            return result
        except Exception as e:
            logger.error(f"Error deleting node {node_id}: {e}")
            return DatabaseOperationResult(
                operation_type=OperationType.DELETE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def query_nodes(self, filters: List[QueryFilter], options: QueryOptions = None) -> DatabaseOperationResult:
        """Query nodes from the database"""
        if not self.initialized:
            return DatabaseOperationResult(
                operation_type=OperationType.QUERY,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"filters": str(filters)},
                error_message="Database not initialized"
            )
        
        try:
            result = self.db_operations.query_nodes(filters, options)
            
            # Create fractal node for the database operation
            self._create_operation_node("query", f"filters_{len(filters)}", result.success)
            
            return result
        except Exception as e:
            logger.error(f"Error querying nodes: {e}")
            return DatabaseOperationResult(
                operation_type=OperationType.QUERY,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"filters": str(filters)},
                error_message=str(e)
            )
    
    def _create_operation_node(self, operation_type: str, target_id: str, success: bool):
        """Create fractal node for database operation"""
        status_text = "✅ Success" if success else "❌ Failed"
        
        self.create_child_node(
            node_type="database_operation",
            name=f"{operation_type.title()} Operation - {status_text}",
            content=f"Database {operation_type} operation on {target_id}",
            metadata={
                "operation_type": operation_type,
                "target_id": target_id,
                "success": success,
                "timestamp": datetime.now().isoformat()
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
    
    def get_database_status(self) -> Dict[str, Any]:
        """Get current database status and capabilities"""
        return {
            "initialized": self.initialized,
            "modular_imports_available": MODULAR_IMPORTS_AVAILABLE,
            "database_type": "sqlite" if self.sqlite_manager else "none",
            "capabilities": [
                "sqlite_storage",
                "postgresql_storage", 
                "content_addressed_storage",
                "recursive_data_structures",
                "fractal_node_mapping"
            ],
            "operations_supported": [
                "create_node",
                "read_node", 
                "update_node",
                "delete_node",
                "query_nodes"
            ]
        }

# Create and register the fractal component
fractal_database_persistence = FractalDatabasePersistenceComponent()
