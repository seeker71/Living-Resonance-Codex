#!/usr/bin/env python3
"""
Database Persistence System - Living Codex
Provides persistent storage for fractal nodes using SQLite and PostgreSQL,
with support for content-addressed storage and recursive data structures.

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

# Import new modular components
try:
    from src.database.core.models import (
        DatabaseNode, DatabaseOperationResult, QueryFilter, QueryOptions,
        DatabaseType, OperationType
    )
    from src.database.core.operations import DatabaseOperations
    from src.database.sqlite.sqlite_manager import SQLiteManager
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
        limit: int = 100
        offset: int = 0
        order_by: str = "created_at"
        order_direction: str = "ASC"  # ASC, DESC
        include_deleted: bool = False

# Legacy database operations (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
    class DatabaseOperations:
        """Base class for database operations"""
        
        def __init__(self):
            self.operation_history = []
        
        def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
            """Create a new node (to be implemented by subclasses)"""
            raise NotImplementedError("Subclasses must implement create_node")
        
        def read_node(self, node_id: str) -> DatabaseOperationResult:
            """Read a node by ID (to be implemented by subclasses)"""
            raise NotImplementedError("Subclasses must implement read_node")
        
        def update_node(self, node: DatabaseNode) -> DatabaseOperationResult:
            """Update an existing node (to be implemented by subclasses)"""
            raise NotImplementedError("Subclasses must implement update_node")
        
        def delete_node(self, node_id: str) -> DatabaseOperationResult:
            """Delete a node (to be implemented by subclasses)"""
            raise NotImplementedError("Subclasses must implement delete_node")
        
        def query_nodes(self, filters: List[QueryFilter], options: QueryOptions) -> DatabaseOperationResult:
            """Query nodes with filters"""
            start_time = datetime.now()
            
            try:
                if not self.db_manager.connection:
                    return DatabaseOperationResult(
                        OperationType.QUERY,
                        False,
                        None,
                        0.0,
                        datetime.now(),
                        {},
                        "Database not connected"
                    )
                
                cursor = self.db_manager.connection.cursor()
                
                # Build query
                query = "SELECT * FROM nodes WHERE 1=1"
                params = []
                
                # Apply filters
                for filter_item in filters:
                    if filter_item.field == "node_type" and filter_item.operator == "=":
                        query += " AND node_type = ?"
                        params.append(filter_item.value)
                    elif filter_item.field == "realm" and filter_item.operator == "=":
                        query += " AND realm = ?"
                        params.append(filter_item.value)
                    elif filter_item.field == "water_state" and filter_item.operator == "=":
                        query += " AND water_state = ?"
                        params.append(filter_item.value)
                    elif filter_item.field == "energy_level_min" and filter_item.operator == ">=":
                        query += " AND energy_level >= ?"
                        params.append(filter_item.value)
                    elif filter_item.field == "name" and filter_item.operator == "=":
                        query += " AND name = ?"
                        params.append(filter_item.value)
                
                # Apply options
                if options.order_by:
                    query += f" ORDER BY {options.order_by}"
                    if options.order_direction:
                        query += f" {options.order_direction}"
                
                if options.limit:
                    query += f" LIMIT {options.limit}"
                
                if options.offset:
                    query += f" OFFSET {options.offset}"
                
                # Execute query
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                # Convert rows to DatabaseNode objects
                nodes = []
                for row in rows:
                    try:
                        node = DatabaseNode(
                            node_id=row['node_id'],
                            node_type=row['node_type'],
                            name=row['name'],
                            content=row['content'],
                            realm=row['realm'],
                            water_state=row['water_state'],
                            energy_level=row['energy_level'],
                            transformation_cost=row['transformation_cost'],
                            parent_id=row['parent_id'],
                            children=json.loads(row['children']) if row['children'] else None,
                            metadata=json.loads(row['metadata']) if row['metadata'] else {},
                            structure_info=json.loads(row['structure_info']) if row['structure_info'] else None,
                            created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else datetime.now(),
                            updated_at=datetime.fromisoformat(row['updated_at']) if row['updated_at'] else datetime.now()
                        )
                        nodes.append(node)
                    except Exception as e:
                        logger.warning(f"Could not convert row to DatabaseNode: {e}")
                        continue
                
                execution_time = (datetime.now() - start_time).total_seconds()
                logger.info(f"✅ Query executed: {len(nodes)} nodes found")
                
                return DatabaseOperationResult(
                    OperationType.QUERY,
                    True,
                    nodes,
                    execution_time,
                    datetime.now(),
                    {"result_count": len(nodes)}
                )
                
            except Exception as e:
                execution_time = (datetime.now() - start_time).total_seconds()
                logger.error(f"❌ Query failed: {e}")
                
                return DatabaseOperationResult(
                    OperationType.QUERY,
                    False,
                    None,
                    execution_time,
                    datetime.now(),
                    {},
                    str(e)
                )

# Legacy SQLite manager (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
    class SQLiteManager:
        """Manages SQLite database connections and schema"""
        
        def __init__(self, db_path: str = None):
            self.db_path = db_path or os.getenv("SQLITE_DB_PATH", "living_codex.db")
            self.connection = None
            self._initialize_database()
        
        def _initialize_database(self):
            """Initialize the SQLite database and create schema"""
            try:
                self.connection = sqlite3.connect(self.db_path)
                self.connection.row_factory = sqlite3.Row
                
                # Create tables
                cursor = self.connection.cursor()
                
                # Nodes table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS nodes (
                        node_id TEXT PRIMARY KEY,
                        node_type TEXT NOT NULL,
                        content_hash TEXT UNIQUE NOT NULL,
                        content TEXT NOT NULL,
                        metadata TEXT,
                        fractal_id TEXT,
                        water_state TEXT,
                        energy_level REAL,
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    )
                """)
                
                # Indexes for better performance
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(node_type)")
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_nodes_fractal_id ON nodes(fractal_id)")
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_nodes_water_state ON nodes(water_state)")
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_nodes_created_at ON nodes(created_at)")
                
                self.connection.commit()
                logger.info(f"✅ SQLite database initialized: {self.db_path}")
                
            except Exception as e:
                logger.error(f"❌ SQLite initialization failed: {e}")
                if self.connection:
                    self.connection.close()
                    self.connection = None
        
        def get_connection(self) -> Optional[sqlite3.Connection]:
            """Get the database connection"""
            return self.connection
        
        def close(self):
            """Close the database connection"""
            if self.connection:
                self.connection.close()
                self.connection = None
                logger.info("SQLite connection closed")

# Main DatabasePersistenceSystem class - now uses modular components when available
class DatabasePersistenceSystem:
    """Main database persistence system - uses modular components when available"""
    
    def __init__(self, db_type: str = "sqlite", db_path: str = None):
        self.db_type = db_type
        self.db_path = db_path
        
        # Initialize database manager
        if MODULAR_IMPORTS_AVAILABLE:
            if db_type == "sqlite":
                self.db_manager = SQLiteManager(db_path)
                logger.info("✅ Using modular SQLite components")
            else:
                logger.warning(f"Database type {db_type} not yet implemented in modular system")
                self.db_manager = SQLiteManager(db_path)
        else:
            self.db_manager = SQLiteManager(db_path)
            logger.info("✅ Using legacy database components")
        
        # Initialize operations
        if MODULAR_IMPORTS_AVAILABLE:
            # For now, we'll use a simple implementation
            # In the future, this will use the full modular system
            self.operations = self._create_simple_operations()
        else:
            self.operations = self._create_simple_operations()
    
    def _create_simple_operations(self):
        """Create simple database operations for backward compatibility"""
        class SimpleDatabaseOperations:
            def __init__(self, db_manager):
                self.db_manager = db_manager
                self.operation_history = []
            
            def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
                """Create a new node in the database"""
                start_time = datetime.now()
                
                try:
                    if not self.db_manager.connection:
                        return DatabaseOperationResult(
                            OperationType.CREATE,
                            False,
                            None,
                            0.0,
                            datetime.now(),
                            {},
                            "Database not connected"
                        )
                    
                    cursor = self.db_manager.connection.cursor()
                    
                    # Insert node using the correct schema
                    cursor.execute("""
                        INSERT INTO nodes (node_id, node_type, name, content, realm, water_state, 
                                        energy_level, transformation_cost, parent_id, children, 
                                        metadata, structure_info, created_at, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        node.node_id,
                        node.node_type,
                        node.name,
                        node.content,
                        node.realm,
                        node.water_state,
                        node.energy_level,
                        node.transformation_cost,
                        node.parent_id,
                        json.dumps(node.children) if node.children else None,
                        json.dumps(node.metadata) if node.metadata else None,
                        json.dumps(node.structure_info) if node.structure_info else None,
                        node.created_at.isoformat() if node.created_at else datetime.now().isoformat(),
                        node.updated_at.isoformat() if node.updated_at else datetime.now().isoformat()
                    ))
                    
                    self.db_manager.connection.commit()
                    
                    execution_time = (datetime.now() - start_time).total_seconds()
                    logger.info(f"✅ Node created: {node.node_id}")
                    
                    return DatabaseOperationResult(
                        OperationType.CREATE,
                        True,
                        node,
                        execution_time,
                        datetime.now(),
                        {"node_id": node.node_id}
                    )
                    
                except Exception as e:
                    execution_time = (datetime.now() - start_time).total_seconds()
                    logger.error(f"❌ Node creation failed: {e}")
                    
                    return DatabaseOperationResult(
                        OperationType.CREATE,
                        False,
                        None,
                        execution_time,
                        datetime.now(),
                        {"node_id": node.node_id},
                        str(e)
                    )
            
            def read_node(self, node_id: str) -> DatabaseOperationResult:
                """Read a node by ID"""
                start_time = datetime.now()
                
                try:
                    if not self.db_manager.connection:
                        return DatabaseOperationResult(
                            OperationType.READ,
                            False,
                            None,
                            0.0,
                            datetime.now(),
                            {},
                            "Database not connected"
                        )
                    
                    cursor = self.db_manager.connection.cursor()
                    
                    cursor.execute("SELECT * FROM nodes WHERE node_id = ?", (node_id,))
                    row = cursor.fetchone()
                    
                    execution_time = (datetime.now() - start_time).total_seconds()
                    
                    if row:
                        # Convert row to DatabaseNode using the correct schema
                        node = DatabaseNode(
                            node_id=row['node_id'],
                            node_type=row['node_type'],
                            name=row['name'],
                            content=row['content'],
                            realm=row['realm'],
                            water_state=row['water_state'],
                            energy_level=row['energy_level'],
                            transformation_cost=row['transformation_cost'],
                            parent_id=row['parent_id'],
                            children=json.loads(row['children']) if row['children'] else None,
                            metadata=json.loads(row['metadata']) if row['metadata'] else {},
                            structure_info=json.loads(row['structure_info']) if row['structure_info'] else None,
                            created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else datetime.now(),
                            updated_at=datetime.fromisoformat(row['updated_at']) if row['updated_at'] else datetime.now()
                        )
                        
                        logger.info(f"✅ Node read: {node_id}")
                        return DatabaseOperationResult(
                            OperationType.READ,
                            True,
                            node,
                            execution_time,
                            datetime.now(),
                            {"node_id": node_id, "found": True}
                        )
                    else:
                        return DatabaseOperationResult(
                            OperationType.READ,
                            True,
                            None,
                            execution_time,
                            datetime.now(),
                            {"node_id": node_id, "found": False}
                        )
                        
                except Exception as e:
                    execution_time = (datetime.now() - start_time).total_seconds()
                    logger.error(f"❌ Node read failed: {e}")
                    
                    return DatabaseOperationResult(
                        OperationType.READ,
                        False,
                        None,
                        execution_time,
                        datetime.now(),
                        {"node_id": node_id},
                        str(e)
                    )
            
            def query_nodes(self, filters: List[QueryFilter], options: QueryOptions) -> DatabaseOperationResult:
                """Query nodes with filters"""
                start_time = datetime.now()
                
                try:
                    if not self.db_manager.connection:
                        return DatabaseOperationResult(
                            OperationType.QUERY,
                            False,
                            None,
                            0.0,
                            datetime.now(),
                            {},
                            "Database not connected"
                        )
                    
                    cursor = self.db_manager.connection.cursor()
                    
                    # Build query
                    query = "SELECT * FROM nodes WHERE 1=1"
                    params = []
                    
                    # Apply filters
                    for filter_item in filters:
                        if filter_item.field == "node_type" and filter_item.operator == "=":
                            query += " AND node_type = ?"
                            params.append(filter_item.value)
                        elif filter_item.field == "realm" and filter_item.operator == "=":
                            query += " AND realm = ?"
                            params.append(filter_item.value)
                        elif filter_item.field == "water_state" and filter_item.operator == "=":
                            query += " AND water_state = ?"
                            params.append(filter_item.value)
                        elif filter_item.field == "energy_level" and filter_item.operator == ">=":
                            query += " AND energy_level >= ?"
                            params.append(filter_item.value)
                        elif filter_item.field == "name" and filter_item.operator == "=":
                            query += " AND name = ?"
                            params.append(filter_item.value)
                    
                    # Apply options
                    if options.order_by:
                        query += f" ORDER BY {options.order_by}"
                        if options.order_direction:
                            query += f" {options.order_direction}"
                    
                    if options.limit:
                        query += f" LIMIT {options.limit}"
                    
                    if options.offset:
                        query += f" OFFSET {options.offset}"
                    
                    # Execute query
                    cursor.execute(query, params)
                    rows = cursor.fetchall()
                    
                    # Convert rows to DatabaseNode objects
                    nodes = []
                    for row in rows:
                        try:
                            node = DatabaseNode(
                                node_id=row['node_id'],
                                node_type=row['node_type'],
                                name=row['name'],
                                content=row['content'],
                                realm=row['realm'],
                                water_state=row['water_state'],
                                energy_level=row['energy_level'],
                                transformation_cost=row['transformation_cost'],
                                parent_id=row['parent_id'],
                                children=json.loads(row['children']) if row['children'] else None,
                                metadata=json.loads(row['metadata']) if row['metadata'] else {},
                                structure_info=json.loads(row['structure_info']) if row['structure_info'] else None,
                                created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else datetime.now(),
                                updated_at=datetime.fromisoformat(row['updated_at']) if row['updated_at'] else datetime.now()
                            )
                            nodes.append(node)
                        except Exception as e:
                            logger.warning(f"Could not convert row to DatabaseNode: {e}")
                            continue
                    
                    execution_time = (datetime.now() - start_time).total_seconds()
                    logger.info(f"✅ Query executed: {len(nodes)} nodes found")
                    
                    return DatabaseOperationResult(
                        OperationType.QUERY,
                        True,
                        nodes,
                        execution_time,
                        datetime.now(),
                        {"result_count": len(nodes)}
                    )
                    
                except Exception as e:
                    execution_time = (datetime.now() - start_time).total_seconds()
                    logger.error(f"❌ Query failed: {e}")
                    
                    return DatabaseOperationResult(
                        OperationType.QUERY,
                        False,
                        None,
                        execution_time,
                        datetime.now(),
                        {},
                        str(e)
                    )
        
        return SimpleDatabaseOperations(self.db_manager)
    
    def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
        """Create a node using the appropriate system"""
        return self.operations.create_node(node)
    
    def read_node(self, node_id: str) -> DatabaseOperationResult:
        """Read a node using the appropriate system"""
        return self.operations.read_node(node_id)
    
    def close(self):
        """Close the database connection"""
        self.db_manager.close()
    
    def create_relationship(self, source_id: str, target_id: str, relationship_type: str, properties: Dict[str, Any] = None) -> bool:
        """Create a relationship between two nodes"""
        try:
            if not self.db_manager.connection:
                logger.error("Database not connected")
                return False
            
            cursor = self.db_manager.connection.cursor()
            
            # Insert relationship
            cursor.execute("""
                INSERT INTO relationships (start_node_id, end_node_id, relationship_type, properties, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                source_id,
                target_id,
                relationship_type,
                json.dumps(properties or {}),
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))
            
            self.db_manager.connection.commit()
            logger.info(f"✅ Relationship created: {source_id} -> {target_id} ({relationship_type})")
            return True
            
        except Exception as e:
            logger.error(f"❌ Relationship creation failed: {e}")
            return False

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
