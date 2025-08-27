#!/usr/bin/env python3
"""
Database Persistence System - Living Codex

This module implements the Living Codex principle: "Everything is just nodes"
where the database persistence system is represented as nodes that can:

1. Store and manage all system nodes (as nodes)
2. Provide persistent storage for fractal nodes (as nodes)
3. Support content-addressed storage (as nodes)
4. Handle recursive data structures (as nodes)

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Database Persistence System represents the WATER layer (Local Persistence) state in the programming language ontology.
"""

import os
import json
import sqlite3
import hashlib
import asyncio
from typing import List, Dict, Any, Optional, Tuple, Union
from datetime import datetime, timedelta
import logging

# Import the Shared Node System and GenericNode
from .shared_node_system import SharedNodeSystem
from .generic_node_system import GenericNode

class DatabasePersistenceNodeSystem(SharedNodeSystem):
    """
    Database Persistence System using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Database types are nodes
    - Operation types are nodes
    - Database nodes are nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The Database Persistence System represents the WATER layer (Local Persistence) state in the programming language ontology:
    - Local database storage, stable persistence
    - Content-addressed storage, recursive structures
    - Query operations, filtering, indexing
    - Transaction management, data integrity
    """
    
    def __init__(self, db_type: str = "sqlite", db_path: str = None):
        super().__init__("DatabasePersistenceNodeSystem")
        self.db_type = db_type
        
        # Ensure db_path is never None and is a valid string
        if db_path is None:
            db_path = "living_codex.db"
        elif not isinstance(db_path, str):
            logging.warning(f"Invalid db_path type: {type(db_path)}, using default")
            db_path = "living_codex.db"
        
        self.db_path = db_path
        logging.info(f"🔧 Initializing DatabasePersistenceNodeSystem with path: {self.db_path}")
        
        self._initialize_database_system_nodes()
        self._setup_database_connection()
    
    def _initialize_database_system_nodes(self):
        """
        Initialize database system nodes - the foundation of the persistence system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root database system node
        root_node = self.create_node(
            node_type='database_system_root',
            name='Database Persistence System Root',
            content='This is the root node of the Database Persistence System. It represents the stable, adaptable storage layer for all Living Codex nodes.',
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,  # Local Persistence
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 1.0,
                'epistemic_label': 'engineering',
                'system_principle': 'Everything is just nodes - database as persistence nodes',
                'meta_circular': True,
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Stable, adaptable storage layer for all system nodes'
            }
        )
        
        # Create the Database Type node
        database_type_node = self.create_node(
            node_type='database_type',
            name='Database Type - Storage Blueprint',
            content='Database Type represents the storage blueprint - defines different types of database storage systems',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.95,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Storage blueprint for different database types'
            }
        )
        
        # Create the Operation Type node
        operation_type_node = self.create_node(
            node_type='operation_type',
            name='Operation Type - Action Blueprint',
            content='Operation Type represents the action blueprint - defines different types of database operations',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.95,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Action blueprint for different database operations'
            }
        )
        
        # Create the Database Node node
        database_node_node = self.create_node(
            node_type='database_node',
            name='Database Node - Data Blueprint',
            content='Database Node represents the data blueprint - defines how nodes are stored in the database',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Data blueprint for storing nodes in the database'
            }
        )
        
        # Create the Query Filter node
        query_filter_node = self.create_node(
            node_type='query_filter',
            name='Query Filter - Selection Blueprint',
            content='Query Filter represents the selection blueprint - defines how to filter database queries',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Selection blueprint for filtering database queries'
            }
        )
        
        # Create the Query Options node
        query_options_node = self.create_node(
            node_type='query_options',
            name='Query Options - Configuration Blueprint',
            content='Query Options represents the configuration blueprint - defines options for database queries',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Configuration blueprint for database query options'
            }
        )
        
        # Create the Database Schema node
        database_schema_node = self.create_node(
            node_type='database_schema',
            name='Database Schema - Structure Blueprint',
            content='Database Schema represents the structure blueprint - defines the database table structure',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.85,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'description': 'Structure blueprint for database table schema'
            }
        )
        
        print(f"🌟 Database Persistence System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"💧 Database Type: {database_type_node.name} (ID: {database_type_node.node_id})")
        print(f"🔧 Operation Type: {operation_type_node.name} (ID: {operation_type_node.node_id})")
        print(f"📊 Database Node: {database_node_node.name} (ID: {database_node_node.node_id})")
        print(f"🔍 Query Filter: {query_filter_node.name} (ID: {query_filter_node.node_id})")
        print(f"⚙️ Query Options: {query_options_node.name} (ID: {query_options_node.node_id})")
        print(f"🏗️ Database Schema: {database_schema_node.name} (ID: {database_schema_node.node_id})")
    
    def _setup_database_connection(self):
        """Setup database connection"""
        try:
            # Create database directory if it doesn't exist
            db_dir = os.path.dirname(self.db_path)
            if db_dir and not os.path.exists(db_dir):
                os.makedirs(db_dir)
            
            # Connect to SQLite database
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            
            # Create tables if they don't exist
            self._create_tables()
            
            logging.info(f"✅ Database connection established: {self.db_path}")
            
        except Exception as e:
            logging.error(f"❌ Failed to setup database connection: {e}")
            self.connection = None
    
    def _create_tables(self):
        """Create database tables"""
        try:
            cursor = self.connection.cursor()
            
            # Create nodes table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS nodes (
                    node_id TEXT PRIMARY KEY,
                    node_type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    content TEXT,
                    parent_id TEXT,
                    children TEXT,
                    metadata TEXT,
                    structure_info TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    water_state TEXT,
                    fractal_layer INTEGER,
                    chakra TEXT,
                    frequency INTEGER,
                    color TEXT,
                    planet TEXT,
                    consciousness_mode TEXT,
                    quantum_state TEXT,
                    resonance_score REAL,
                    epistemic_label TEXT
                )
            """)
            
            # Create database_types table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS database_types (
                    type_id TEXT PRIMARY KEY,
                    type_name TEXT NOT NULL,
                    description TEXT,
                    metadata TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            
            # Create operation_types table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS operation_types (
                    operation_id TEXT PRIMARY KEY,
                    operation_name TEXT NOT NULL,
                    description TEXT,
                    metadata TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            
            # Create database_schemas table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS database_schemas (
                    schema_id TEXT PRIMARY KEY,
                    table_name TEXT NOT NULL,
                    schema_definition TEXT NOT NULL,
                    metadata TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            
            self.connection.commit()
            logging.info("✅ Database tables created successfully")
            
        except Exception as e:
            logging.error(f"❌ Failed to create database tables: {e}")
    
    def create_database_type_node(self, type_name: str, description: str = "") -> GenericNode:
        """Create a database type node"""
        return self.create_node(
            node_type='database_type_instance',
            name=f"Database Type: {type_name}",
            content=f'Database type instance: {type_name} - {description}',
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'type_name': type_name,
                'description': description,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def create_operation_type_node(self, operation_name: str, description: str = "") -> GenericNode:
        """Create an operation type node"""
        return self.create_node(
            node_type='operation_type_instance',
            name=f"Operation Type: {operation_name}",
            content=f'Operation type instance: {operation_name} - {description}',
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'operation_name': operation_name,
                'description': description,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def create_database_node(self, node_data: Dict[str, Any]) -> GenericNode:
        """Create a database node"""
        return self.create_node(
            node_type='database_node_instance',
            name=f"Database Node: {node_data.get('name', 'Unknown')}",
            content=f'Database node instance: {node_data.get("name", "Unknown")}',
            metadata={
                'water_state': 'liquid',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'water_local_persistence',
                'node_data': node_data,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        database_nodes = [node for node in self.storage.get_all_nodes().values() if node.metadata.get('programming_ontology_layer') == 'water_local_persistence']
        type_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'database_type']
        operation_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'operation_type']
        schema_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'database_schema']
        
        return {
            'total_nodes': len(self.storage.get_all_nodes()),
            'database_persistence_nodes': len(database_nodes),
            'type_nodes': len(type_nodes),
            'operation_nodes': len(operation_nodes),
            'schema_nodes': len(schema_nodes),
            'water_states': list(set(node.get_water_state() for node in self.storage.get_all_nodes().values())),
            'chakras': list(set(node.get_chakra() for node in self.storage.get_all_nodes().values())),
            'frequencies': list(set(node.get_frequency() for node in self.storage.get_all_nodes().values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.storage.get_all_nodes().values()) / max(len(self.storage.get_all_nodes()), 1),
            'system_principle': 'Everything is just nodes - database as persistence nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'water_local_persistence_layer'
        }

# Legacy compatibility - maintain the old interface for now
class DatabasePersistenceSystem(DatabasePersistenceNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self, db_type: str = "sqlite", db_path: str = None):
        super().__init__(db_type, db_path)
        logging.info("🔄 DatabasePersistenceSystem initialized with new node-based system")
        logging.info("✨ This system now embodies Living Codex principles")
        logging.info("🌟 Everything is just nodes - database as persistence nodes")
        logging.info("💧 Database system represents WATER (Local Persistence) state in programming language ontology")
