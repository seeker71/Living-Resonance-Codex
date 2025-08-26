"""
SQLite Database Manager
Connection and schema management for SQLite databases
"""

import sqlite3
import logging
from pathlib import Path
from typing import Optional
from ..core.models import DatabaseType

logger = logging.getLogger(__name__)

class SQLiteManager:
    """Manages SQLite database connections and schema"""
    
    def __init__(self, db_path: str = "living_codex.db"):
        # Ensure db_path is never None
        if db_path is None:
            db_path = "living_codex.db"
        self.db_path = db_path
        self.connection = None
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
            self._create_schema()
            
            logger.info(f"✅ SQLite database initialized: {self.db_path}")
            
        except Exception as e:
            logger.error(f"❌ SQLite initialization failed: {e}")
            self.connection = None
    
    def _create_schema(self):
        """Create the database schema"""
        schema_sql = """
        CREATE TABLE IF NOT EXISTS nodes (
            node_id VARCHAR(255) PRIMARY KEY,
            node_type VARCHAR(100) NOT NULL,
            name VARCHAR(500) NOT NULL,
            content TEXT,
            realm VARCHAR(100),
            water_state VARCHAR(50),
            energy_level REAL,
            transformation_cost REAL,
            parent_id VARCHAR(255),
            children TEXT,  -- JSON array
            metadata TEXT,  -- JSON object
            structure_info TEXT,  -- JSON object
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_deleted BOOLEAN DEFAULT FALSE
        );
        
        CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(node_type);
        CREATE INDEX IF NOT EXISTS idx_nodes_realm ON nodes(realm);
        CREATE INDEX IF NOT EXISTS idx_nodes_water_state ON nodes(water_state);
        CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(parent_id);
        CREATE INDEX IF NOT EXISTS idx_nodes_energy ON nodes(energy_level);
        CREATE INDEX IF NOT EXISTS idx_nodes_deleted ON nodes(is_deleted);
        
        CREATE TABLE IF NOT EXISTS relationships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_node_id VARCHAR(255) NOT NULL,
            end_node_id VARCHAR(255) NOT NULL,
            relationship_type VARCHAR(100) NOT NULL,
            properties TEXT,  -- JSON object
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
            version VARCHAR(50) NOT NULL,
            description TEXT NOT NULL,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        try:
            # Split SQL into individual statements
            statements = [stmt.strip() for stmt in schema_sql.split(';') if stmt.strip()]
            
            cursor = self.connection.cursor()
            for statement in statements:
                cursor.execute(statement)
            
            self.connection.commit()
            logger.info("✅ Database schema created successfully")
            
        except Exception as e:
            logger.error(f"❌ Schema creation failed: {e}")
            if self.connection:
                self.connection.rollback()
    
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
    
    def execute_query(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query and return the cursor"""
        if not self.connection:
            raise RuntimeError("Database connection not available")
        
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor
    
    def execute_many(self, query: str, params_list: list) -> sqlite3.Cursor:
        """Execute a query with multiple parameter sets"""
        if not self.connection:
            raise RuntimeError("Database connection not available")
        
        cursor = self.connection.cursor()
        cursor.executemany(query, params_list)
        return cursor
    
    def commit(self):
        """Commit the current transaction"""
        if self.connection:
            self.connection.commit()
    
    def rollback(self):
        """Rollback the current transaction"""
        if self.connection:
            self.connection.rollback()
    
    def check_schema_version(self) -> str:
        """Check the current schema version"""
        try:
            cursor = self.execute_query(
                "SELECT version FROM schema_migrations ORDER BY applied_at DESC LIMIT 1"
            )
            result = cursor.fetchone()
            
            if result:
                return result[0]
            else:
                return "1.0.0"  # Default version for new databases
                
        except Exception as e:
            logger.error(f"❌ Schema version check failed: {e}")
            return "0.0.0"
