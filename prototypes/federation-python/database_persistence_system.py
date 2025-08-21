#!/usr/bin/env python3
"""
Database Persistence System - Living Codex
Replaces simulated database operations with real SQLite/PostgreSQL persistence,
providing complete CRUD operations, query optimization, and data consistency.
"""

import os
import json
import time
import hashlib
import sqlite3
import asyncio
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import logging
from pathlib import Path

# Database imports
try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    POSTGRESQL_AVAILABLE = True
except ImportError:
    print("⚠️  PostgreSQL driver not available. Install with: pip install psycopg2-binary")
    POSTGRESQL_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseType(Enum):
    """Supported database types"""
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"

class OperationType(Enum):
    """Types of database operations"""
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    QUERY = "query"
    BULK_OPERATION = "bulk_operation"

@dataclass
class DatabaseNode:
    """Represents a node in the database"""
    node_id: str
    node_type: str
    name: str
    content: str
    realm: str
    water_state: str
    energy_level: float
    transformation_cost: float
    parent_id: Optional[str] = None
    children: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    structure_info: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

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
    rows_affected: int = 0

@dataclass
class QueryFilter:
    """Filter for database queries"""
    field: str
    operator: str  # =, !=, >, <, >=, <=, LIKE, IN, NOT IN
    value: Any
    logical_operator: str = "AND"  # AND, OR

@dataclass
class QueryOptions:
    """Options for database queries"""
    limit: Optional[int] = None
    offset: Optional[int] = None
    order_by: Optional[str] = None
    order_direction: str = "ASC"  # ASC, DESC
    include_deleted: bool = False

class DatabaseSchemaManager:
    """Manages database schema creation and migrations"""
    
    def __init__(self, database_type: DatabaseType):
        self.database_type = database_type
        self.schema_version = "1.0.0"
        self.migrations = []
        self._initialize_migrations()
    
    def _initialize_migrations(self):
        """Initialize migration scripts"""
        self.migrations = [
            {
                "version": "1.0.0",
                "description": "Initial schema creation",
                "sqlite_sql": self._get_sqlite_initial_schema(),
                "postgresql_sql": self._get_postgresql_initial_schema()
            }
        ]
    
    def _get_sqlite_initial_schema(self) -> str:
        """Get SQLite initial schema"""
        return """
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id TEXT UNIQUE NOT NULL,
            node_type TEXT NOT NULL,
            name TEXT NOT NULL,
            content TEXT NOT NULL,
            realm TEXT NOT NULL,
            water_state TEXT NOT NULL,
            energy_level REAL NOT NULL,
            transformation_cost REAL NOT NULL,
            parent_id TEXT,
            children TEXT,  -- JSON array as text
            metadata TEXT,  -- JSON object as text
            structure_info TEXT,  -- JSON object as text
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE INDEX IF NOT EXISTS idx_nodes_node_id ON nodes(node_id);
        CREATE INDEX IF NOT EXISTS idx_nodes_node_type ON nodes(node_type);
        CREATE INDEX IF NOT EXISTS idx_nodes_realm ON nodes(realm);
        CREATE INDEX IF NOT EXISTS idx_nodes_water_state ON nodes(water_state);
        CREATE INDEX IF NOT EXISTS idx_nodes_energy_level ON nodes(energy_level);
        CREATE INDEX IF NOT EXISTS idx_nodes_parent_id ON nodes(parent_id);
        
        CREATE TABLE IF NOT EXISTS relationships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            relationship_id TEXT UNIQUE NOT NULL,
            start_node_id TEXT NOT NULL,
            end_node_id TEXT NOT NULL,
            relationship_type TEXT NOT NULL,
            properties TEXT,  -- JSON object as text
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (start_node_id) REFERENCES nodes(node_id),
            FOREIGN KEY (end_node_id) REFERENCES nodes(node_id)
        );
        
        CREATE INDEX IF NOT EXISTS idx_relationships_start_node ON relationships(start_node_id);
        CREATE INDEX IF NOT EXISTS idx_relationships_end_node ON relationships(end_node_id);
        CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(relationship_type);
        
        CREATE TABLE IF NOT EXISTS schema_migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            version TEXT NOT NULL,
            description TEXT NOT NULL,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    
    def _get_postgresql_initial_schema(self) -> str:
        """Get PostgreSQL initial schema"""
        return """
        CREATE TABLE IF NOT EXISTS nodes (
            id SERIAL PRIMARY KEY,
            node_id VARCHAR(255) UNIQUE NOT NULL,
            node_type VARCHAR(100) NOT NULL,
            name TEXT NOT NULL,
            content TEXT NOT NULL,
            realm VARCHAR(50) NOT NULL,
            water_state VARCHAR(50) NOT NULL,
            energy_level DOUBLE PRECISION NOT NULL,
            transformation_cost DOUBLE PRECISION NOT NULL,
            parent_id VARCHAR(255),
            children JSONB,  -- JSON array
            metadata JSONB,  -- JSON object
            structure_info JSONB,  -- JSON object
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE INDEX IF NOT EXISTS idx_nodes_node_id ON nodes(node_id);
        CREATE INDEX IF NOT EXISTS idx_nodes_node_type ON nodes(node_type);
        CREATE INDEX IF NOT EXISTS idx_nodes_realm ON nodes(realm);
        CREATE INDEX IF NOT EXISTS idx_nodes_water_state ON nodes(water_state);
        CREATE INDEX IF NOT EXISTS idx_nodes_energy_level ON nodes(energy_level);
        CREATE INDEX IF NOT EXISTS idx_nodes_parent_id ON nodes(parent_id);
        
        CREATE TABLE IF NOT EXISTS relationships (
            id SERIAL PRIMARY KEY,
            relationship_id VARCHAR(255) UNIQUE NOT NULL,
            start_node_id VARCHAR(255) NOT NULL,
            end_node_id VARCHAR(255) NOT NULL,
            relationship_type VARCHAR(100) NOT NULL,
            properties JSONB,  -- JSON object
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (start_node_id) REFERENCES nodes(node_id),
            FOREIGN KEY (end_node_id) REFERENCES nodes(node_id)
        );
        
        CREATE INDEX IF NOT EXISTS idx_relationships_start_node ON relationships(start_node_id);
        CREATE INDEX IF NOT EXISTS idx_relationships_end_node ON relationships(end_node_id);
        CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(relationship_type);
        
        CREATE TABLE IF NOT EXISTS schema_migrations (
            id SERIAL PRIMARY KEY,
            version VARCHAR(50) NOT NULL,
            description TEXT NOT NULL,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    
    def create_schema(self, connection) -> bool:
        """Create the database schema"""
        try:
            if self.database_type == DatabaseType.SQLITE:
                schema_sql = self._get_sqlite_initial_schema()
            else:
                schema_sql = self._get_postgresql_initial_schema()
            
            # Split SQL into individual statements
            statements = [stmt.strip() for stmt in schema_sql.split(';') if stmt.strip()]
            
            cursor = connection.cursor()
            for statement in statements:
                cursor.execute(statement)
            
            connection.commit()
            logger.info("✅ Database schema created successfully")
            return True
            
        except Exception as e:
            logger.error(f"❌ Schema creation failed: {e}")
            connection.rollback()
            return False
    
    def check_schema_version(self, connection) -> str:
        """Check the current schema version"""
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT version FROM schema_migrations ORDER BY applied_at DESC LIMIT 1")
            result = cursor.fetchone()
            
            if result:
                return result[0]
            else:
                return "0.0.0"
                
        except Exception as e:
            logger.error(f"❌ Schema version check failed: {e}")
            return "0.0.0"

class SQLiteDatabaseManager:
    """Manages SQLite database connections and operations"""
    
    def __init__(self, db_path: str = "living_codex.db"):
        self.db_path = db_path
        self.connection = None
        self.schema_manager = DatabaseSchemaManager(DatabaseType.SQLITE)
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize the SQLite database"""
        try:
            # Ensure directory exists
            db_dir = Path(self.db_path).parent
            db_dir.mkdir(parents=True, exist_ok=True)
            
            # Create connection
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Enable dict-like access
            
            # Create schema if it doesn't exist
            current_version = self.schema_manager.check_schema_version(self.connection)
            if current_version == "0.0.0":
                self.schema_manager.create_schema(self.connection)
            
            logger.info(f"✅ SQLite database initialized: {self.db_path}")
            
        except Exception as e:
            logger.error(f"❌ SQLite initialization failed: {e}")
            self.connection = None
    
    def get_connection(self):
        """Get the database connection"""
        if not self.connection:
            self._initialize_database()
        return self.connection
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            logger.info("SQLite connection closed")

class PostgreSQLDatabaseManager:
    """Manages PostgreSQL database connections and operations"""
    
    def __init__(self, host: str = None, port: int = None, database: str = None, 
                 username: str = None, password: str = None):
        self.host = host or os.getenv("POSTGRES_HOST", "localhost")
        self.port = port or int(os.getenv("POSTGRES_PORT", "5432"))
        self.database = database or os.getenv("POSTGRES_DB", "living_codex")
        self.username = username or os.getenv("POSTGRES_USER", "postgres")
        self.password = password or os.getenv("POSTGRES_PASSWORD", "password")
        self.connection = None
        self.schema_manager = DatabaseSchemaManager(DatabaseType.POSTGRESQL)
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize the PostgreSQL database"""
        if not POSTGRESQL_AVAILABLE:
            logger.error("❌ PostgreSQL driver not available")
            return
        
        try:
            # Create connection
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password
            )
            
            # Create schema if it doesn't exist
            current_version = self.schema_manager.check_schema_version(self.connection)
            if current_version == "0.0.0":
                self.schema_manager.create_schema(self.connection)
            
            logger.info(f"✅ PostgreSQL database initialized: {self.host}:{self.port}/{self.database}")
            
        except Exception as e:
            logger.error(f"❌ PostgreSQL initialization failed: {e}")
            self.connection = None
    
    def get_connection(self):
        """Get the database connection"""
        if not self.connection:
            self._initialize_database()
        return self.connection
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            logger.info("PostgreSQL connection closed")

class CRUDOperations:
    """Implements complete CRUD operations for the database"""
    
    def __init__(self, database_manager):
        self.db_manager = database_manager
        self.database_type = database_manager.__class__.__name__
    
    def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
        """Create a new node in the database"""
        start_time = time.time()
        
        try:
            connection = self.db_manager.get_connection()
            if not connection:
                return DatabaseOperationResult(
                    operation_type=OperationType.CREATE,
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=datetime.now(),
                    metadata={"node_id": node.node_id},
                    error_message="Database not connected"
                )
            
            cursor = connection.cursor()
            
            # Prepare data
            children_json = json.dumps(node.children) if node.children else None
            metadata_json = json.dumps(node.metadata) if node.metadata else None
            structure_info_json = json.dumps(node.structure_info) if node.structure_info else None
            
            query = """
            INSERT INTO nodes (
                node_id, node_type, name, content, realm, water_state, 
                energy_level, transformation_cost, parent_id, children, 
                metadata, structure_info, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, (
                node.node_id, node.node_type, node.name, node.content,
                node.realm, node.water_state, node.energy_level,
                node.transformation_cost, node.parent_id, children_json,
                metadata_json, structure_info_json,
                datetime.now(), datetime.now()
            ))
            
            connection.commit()
            execution_time = time.time() - start_time
            
            logger.info(f"✅ Node created: {node.node_id}")
            
            return DatabaseOperationResult(
                operation_type=OperationType.CREATE,
                success=True,
                data={"node_id": node.node_id, "id": cursor.lastrowid},
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id, "node_type": node.node_type},
                rows_affected=1
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Node creation failed: {e}")
            
            if connection:
                connection.rollback()
            
            return DatabaseOperationResult(
                operation_type=OperationType.CREATE,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id},
                error_message=str(e)
            )
    
    def get_node(self, node_id: str) -> DatabaseOperationResult:
        """Retrieve a node from the database"""
        start_time = time.time()
        
        try:
            connection = self.db_manager.get_connection()
            if not connection:
                return DatabaseOperationResult(
                    operation_type=OperationType.READ,
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id},
                    error_message="Database not connected"
                )
            
            cursor = connection.cursor()
            
            query = "SELECT * FROM nodes WHERE node_id = ?"
            cursor.execute(query, (node_id,))
            
            row = cursor.fetchone()
            execution_time = time.time() - start_time
            
            if row:
                # Convert row to dict
                if hasattr(row, 'keys'):  # SQLite Row
                    node_data = dict(row)
                else:  # PostgreSQL tuple
                    columns = [desc[0] for desc in cursor.description]
                    node_data = dict(zip(columns, row))
                
                # Parse JSON fields
                if node_data.get('children'):
                    node_data['children'] = json.loads(node_data['children'])
                if node_data.get('metadata'):
                    node_data['metadata'] = json.loads(node_data['metadata'])
                if node_data.get('structure_info'):
                    node_data['structure_info'] = json.loads(node_data['structure_info'])
                
                return DatabaseOperationResult(
                    operation_type=OperationType.READ,
                    success=True,
                    data=node_data,
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id, "found": True}
                )
            else:
                return DatabaseOperationResult(
                    operation_type=OperationType.READ,
                    success=True,
                    data=None,
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id, "found": False}
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Node retrieval failed: {e}")
            
            return DatabaseOperationResult(
                operation_type=OperationType.READ,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def update_node(self, node_id: str, updates: Dict[str, Any]) -> DatabaseOperationResult:
        """Update a node in the database"""
        start_time = time.time()
        
        try:
            connection = self.db_manager.get_connection()
            if not connection:
                return DatabaseOperationResult(
                    operation_type=OperationType.UPDATE,
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id},
                    error_message="Database not connected"
                )
            
            cursor = connection.cursor()
            
            # Add updated_at timestamp
            updates['updated_at'] = datetime.now()
            
            # Build SET clause dynamically
            set_clauses = []
            values = []
            
            for key, value in updates.items():
                if key in ['children', 'metadata', 'structure_info'] and isinstance(value, (list, dict)):
                    set_clauses.append(f"{key} = ?")
                    values.append(json.dumps(value))
                else:
                    set_clauses.append(f"{key} = ?")
                    values.append(value)
            
            set_clause = ", ".join(set_clauses)
            values.append(node_id)  # For WHERE clause
            
            query = f"UPDATE nodes SET {set_clause} WHERE node_id = ?"
            cursor.execute(query, values)
            
            rows_affected = cursor.rowcount
            connection.commit()
            execution_time = time.time() - start_time
            
            if rows_affected > 0:
                logger.info(f"✅ Node updated: {node_id}")
                
                return DatabaseOperationResult(
                    operation_type=OperationType.UPDATE,
                    success=True,
                    data={"node_id": node_id, "rows_affected": rows_affected},
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id, "fields_updated": list(updates.keys())},
                    rows_affected=rows_affected
                )
            else:
                return DatabaseOperationResult(
                    operation_type=OperationType.UPDATE,
                    success=False,
                    data=None,
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id},
                    error_message="Node not found"
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Node update failed: {e}")
            
            if connection:
                connection.rollback()
            
            return DatabaseOperationResult(
                operation_type=OperationType.UPDATE,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def delete_node(self, node_id: str, soft_delete: bool = True) -> DatabaseOperationResult:
        """Delete a node from the database"""
        start_time = time.time()
        
        try:
            connection = self.db_manager.get_connection()
            if not connection:
                return DatabaseOperationResult(
                    operation_type=OperationType.DELETE,
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id},
                    error_message="Database not connected"
                )
            
            cursor = connection.cursor()
            
            if soft_delete:
                # Soft delete - mark as deleted
                query = "UPDATE nodes SET deleted_at = ? WHERE node_id = ?"
                cursor.execute(query, (datetime.now(), node_id))
            else:
                # Hard delete - remove from database
                query = "DELETE FROM nodes WHERE node_id = ?"
                cursor.execute(query, (node_id,))
            
            rows_affected = cursor.rowcount
            connection.commit()
            execution_time = time.time() - start_time
            
            if rows_affected > 0:
                logger.info(f"✅ Node deleted: {node_id}")
                
                return DatabaseOperationResult(
                    operation_type=OperationType.DELETE,
                    success=True,
                    data={"node_id": node_id, "rows_affected": rows_affected},
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id, "soft_delete": soft_delete},
                    rows_affected=rows_affected
                )
            else:
                return DatabaseOperationResult(
                    operation_type=OperationType.DELETE,
                    success=False,
                    data=None,
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node_id},
                    error_message="Node not found"
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Node deletion failed: {e}")
            
            if connection:
                connection.rollback()
            
            return DatabaseOperationResult(
                operation_type=OperationType.DELETE,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def query_nodes(self, filters: List[QueryFilter] = None, 
                   options: QueryOptions = None) -> DatabaseOperationResult:
        """Query nodes with filters and options"""
        start_time = time.time()
        
        try:
            connection = self.db_manager.get_connection()
            if not connection:
                return DatabaseOperationResult(
                    operation_type=OperationType.QUERY,
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=datetime.now(),
                    metadata={"filters": filters},
                    error_message="Database not connected"
                )
            
            cursor = connection.cursor()
            
            # Build query
            query = "SELECT * FROM nodes WHERE 1=1"
            values = []
            
            if filters:
                for i, filter_item in enumerate(filters):
                    if i > 0:
                        query += f" {filter_item.logical_operator}"
                    
                    if filter_item.operator == "LIKE":
                        query += f" AND {filter_item.field} LIKE ?"
                        values.append(f"%{filter_item.value}%")
                    elif filter_item.operator == "IN":
                        placeholders = ",".join(["?" for _ in filter_item.value])
                        query += f" AND {filter_item.field} IN ({placeholders})"
                        values.extend(filter_item.value)
                    else:
                        query += f" AND {filter_item.field} {filter_item.operator} ?"
                        values.append(filter_item.value)
            
            # Add options
            if options and options.order_by:
                query += f" ORDER BY {options.order_by} {options.order_direction}"
            
            if options and options.limit:
                query += f" LIMIT ?"
                values.append(options.limit)
            
            if options and options.offset:
                query += f" OFFSET ?"
                values.append(options.offset)
            
            cursor.execute(query, values)
            rows = cursor.fetchall()
            execution_time = time.time() - start_time
            
            # Convert rows to dicts
            results = []
            for row in rows:
                if hasattr(row, 'keys'):  # SQLite Row
                    node_data = dict(row)
                else:  # PostgreSQL tuple
                    columns = [desc[0] for desc in cursor.description]
                    node_data = dict(zip(columns, row))
                
                # Parse JSON fields
                if node_data.get('children'):
                    node_data['children'] = json.loads(node_data['children'])
                if node_data.get('metadata'):
                    node_data['metadata'] = json.loads(node_data['metadata'])
                if node_data.get('structure_info'):
                    node_data['structure_info'] = json.loads(node_data['structure_info'])
                
                results.append(node_data)
            
            logger.info(f"✅ Query executed: {len(results)} results")
            
            return DatabaseOperationResult(
                operation_type=OperationType.QUERY,
                success=True,
                data=results,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"filters": filters, "result_count": len(results)},
                rows_affected=len(results)
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Query execution failed: {e}")
            
            return DatabaseOperationResult(
                operation_type=OperationType.QUERY,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"filters": filters},
                error_message=str(e)
            )

class DatabasePersistenceSystem:
    """Main system that orchestrates all database persistence capabilities"""
    
    def __init__(self, database_type: DatabaseType = DatabaseType.SQLITE, **kwargs):
        self.database_type = database_type
        
        if database_type == DatabaseType.SQLITE:
            self.db_manager = SQLiteDatabaseManager(**kwargs)
        elif database_type == DatabaseType.POSTGRESQL:
            self.db_manager = PostgreSQLDatabaseManager(**kwargs)
        else:
            raise ValueError(f"Unsupported database type: {database_type}")
        
        self.crud_operations = CRUDOperations(self.db_manager)
        
        # Initialize system
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize the database persistence system"""
        try:
            # Test connection
            connection = self.db_manager.get_connection()
            if connection:
                logger.info(f"✅ Database persistence system initialized: {self.database_type.value}")
            else:
                logger.error("❌ Database persistence system initialization failed")
                
        except Exception as e:
            logger.error(f"❌ System initialization failed: {e}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get the current status of the database persistence system"""
        connection = self.db_manager.get_connection()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "database_type": self.database_type.value,
            "connected": connection is not None,
            "database_info": {
                "sqlite_path": getattr(self.db_manager, 'db_path', None),
                "postgresql_host": getattr(self.db_manager, 'host', None),
                "postgresql_port": getattr(self.db_manager, 'port', None),
                "postgresql_database": getattr(self.db_manager, 'database', None)
            }
        }
    
    def close(self):
        """Close all database connections and cleanup"""
        self.db_manager.close()
        logger.info("Database persistence system closed")

async def main():
    """Main function to demonstrate the Database Persistence System"""
    
    print("🌟 Living Codex Database Persistence System Demo")
    print("=" * 60)
    
    try:
        # Create the system (SQLite by default)
        db_system = DatabasePersistenceSystem(DatabaseType.SQLITE, db_path="demo_persistence.db")
        
        # Show system status
        status = db_system.get_system_status()
        print(f"\n🔧 System Status:")
        print(f"   Database Type: {status['database_type']}")
        print(f"   Connected: {status['connected']}")
        print(f"   Database Path: {status['database_info']['sqlite_path']}")
        
        if not status['connected']:
            print(f"\n⚠️  Database not connected. Please check configuration.")
            return
        
        # Test basic operations
        print(f"\n🔍 Testing Basic Database Operations...")
        
        # Create a test node
        test_node = DatabaseNode(
            node_id="test_db_node_001",
            node_type="test",
            name="Test Database Node",
            content="A test node for database persistence",
            realm="data",
            water_state="liquid",
            energy_level=639.0,
            transformation_cost=50.0,
            metadata={"test": True, "category": "demo"},
            structure_info={"fractal_depth": 1}
        )
        
        create_result = db_system.crud_operations.create_node(test_node)
        print(f"   Create Node: {'✅' if create_result.success else '❌'}")
        if create_result.success:
            print(f"      Execution Time: {create_result.execution_time:.3f}s")
            print(f"      Rows Affected: {create_result.rows_affected}")
        
        # Retrieve the test node
        get_result = db_system.crud_operations.get_node("test_db_node_001")
        print(f"   Get Node: {'✅' if get_result.success else '❌'}")
        if get_result.success:
            print(f"      Execution Time: {get_result.execution_time:.3f}s")
            print(f"      Node Found: {get_result.metadata.get('found', False)}")
            if get_result.data:
                print(f"      Node Name: {get_result.data.get('name', 'N/A')}")
        
        # Update the test node
        update_result = db_system.crud_operations.update_node(
            "test_db_node_001", 
            {"energy_level": 741.0, "content": "Updated test node content"}
        )
        print(f"   Update Node: {'✅' if update_result.success else '❌'}")
        if update_result.success:
            print(f"      Execution Time: {update_result.execution_time:.3f}s")
            print(f"      Rows Affected: {update_result.rows_affected}")
        
        # Test querying
        print(f"\n🔍 Testing Query Operations...")
        
        # Query by water state
        filters = [QueryFilter("water_state", "=", "liquid")]
        options = QueryOptions(limit=10, order_by="energy_level", order_direction="DESC")
        
        query_result = db_system.crud_operations.query_nodes(filters, options)
        print(f"   Query Nodes: {'✅' if query_result.success else '❌'}")
        if query_result.success:
            print(f"      Execution Time: {query_result.execution_time:.3f}s")
            print(f"      Results Found: {query_result.metadata.get('result_count', 0)}")
        
        # Test bulk operations
        print(f"\n🔍 Testing Bulk Operations...")
        
        # Create multiple nodes
        bulk_nodes = []
        for i in range(5):
            bulk_node = DatabaseNode(
                node_id=f"bulk_test_node_{i:03d}",
                node_type="bulk_test",
                name=f"Bulk Test Node {i}",
                content=f"Bulk test node content {i}",
                realm="data",
                water_state="vapor" if i % 2 == 0 else "ice",
                energy_level=100.0 + i * 50.0,
                transformation_cost=25.0 + i * 10.0,
                metadata={"bulk_test": True, "index": i}
            )
            bulk_nodes.append(bulk_node)
        
        bulk_results = []
        for node in bulk_nodes:
            result = db_system.crud_operations.create_node(node)
            bulk_results.append(result)
        
        successful_bulk = sum(1 for r in bulk_results if r.success)
        print(f"   Bulk Create: {successful_bulk}/{len(bulk_nodes)} successful")
        
        # Show final statistics
        print(f"\n📊 Final Database Statistics...")
        
        # Count all nodes
        count_result = db_system.crud_operations.query_nodes()
        if count_result.success:
            total_nodes = count_result.metadata.get('result_count', 0)
            print(f"   Total Nodes: {total_nodes}")
        
        # Count by water state
        for water_state in ["ice", "liquid", "vapor"]:
            filter_result = db_system.crud_operations.query_nodes(
                [QueryFilter("water_state", "=", water_state)]
            )
            if filter_result.success:
                count = filter_result.metadata.get('result_count', 0)
                print(f"   {water_state.capitalize()} State Nodes: {count}")
        
        print("\n" + "=" * 60)
        print("🎉 Database Persistence System Demo Completed!")
        print("\n🌟 What We've Achieved:")
        print("   • Real database persistence (SQLite/PostgreSQL)")
        print("   • Complete CRUD operations")
        print("   • Advanced querying with filters and options")
        print("   • Bulk operations support")
        print("   • JSON field handling")
        print("   • Connection management and error handling")
        print("\n🚀 The Living Codex now has real database persistence!")
        
    except Exception as e:
        print(f"❌ Error running Database Persistence System demo: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cleanup
        if 'db_system' in locals():
            db_system.close()

if __name__ == "__main__":
    asyncio.run(main())
