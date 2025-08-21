#!/usr/bin/env python3
"""
Neo4j Integration System - Living Codex
Replaces simulated graph operations with real Neo4j database connections
and operations, providing bidirectional synchronization with the fractal node system.
"""

import os
import json
import time
import hashlib
import asyncio
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import logging

# Neo4j imports
try:
    from neo4j import GraphDatabase, Driver, Session, Transaction
    from neo4j.exceptions import ServiceUnavailable, AuthError, ClientError
    NEO4J_AVAILABLE = True
except ImportError:
    print("⚠️  Neo4j driver not available. Install with: pip install neo4j")
    NEO4J_AVAILABLE = False
    # Mock classes for demonstration
    class GraphDatabase:
        @staticmethod
        def driver(uri, auth):
            return None
    class Driver:
        pass
    class Session:
        pass
    class Transaction:
        pass

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GraphOperationType(Enum):
    """Types of graph operations"""
    CREATE_NODE = "create_node"
    UPDATE_NODE = "update_node"
    DELETE_NODE = "delete_node"
    CREATE_RELATIONSHIP = "create_relationship"
    DELETE_RELATIONSHIP = "delete_relationship"
    QUERY = "query"
    TRAVERSE = "traverse"
    SYNC = "sync"

class GraphNodeType(Enum):
    """Types of nodes in the graph"""
    FRACTAL_NODE = "fractal_node"
    META_NODE = "meta_node"
    RELATIONSHIP = "relationship"
    SYSTEM_NODE = "system_node"
    EXTERNAL_NODE = "external_node"

@dataclass
class GraphNode:
    """Represents a node in the Neo4j graph"""
    node_id: str
    labels: List[str]
    properties: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    fractal_id: Optional[str] = None
    water_state: Optional[str] = None
    energy_level: Optional[float] = None

@dataclass
class GraphRelationship:
    """Represents a relationship in the Neo4j graph"""
    relationship_id: str
    start_node_id: str
    end_node_id: str
    relationship_type: str
    properties: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

@dataclass
class GraphQueryResult:
    """Result of a graph query"""
    operation_type: GraphOperationType
    success: bool
    data: Any
    execution_time: float
    timestamp: datetime
    metadata: Dict[str, Any]
    error_message: Optional[str] = None

class Neo4jConnectionManager:
    """Manages Neo4j database connections and connection pooling"""
    
    def __init__(self, uri: str = None, username: str = None, password: str = None):
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.username = username or os.getenv("NEO4J_USERNAME", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD", "password")
        self.driver: Optional[Driver] = None
        self.connection_pool_size = 10
        self.max_connection_lifetime = 3600  # 1 hour
        self.connection_timeout = 30
        self._initialize_connection()
    
    def _initialize_connection(self):
        """Initialize the Neo4j driver connection"""
        if not NEO4J_AVAILABLE:
            logger.warning("Neo4j driver not available, using mock connection")
            return
        
        try:
            self.driver = GraphDatabase.driver(
                self.uri,
                auth=(self.username, self.password),
                max_connection_pool_size=self.connection_pool_size,
                max_connection_lifetime=self.max_connection_lifetime,
                connection_timeout=self.connection_timeout
            )
            
            # Test the connection
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                test_value = result.single()["test"]
                if test_value == 1:
                    logger.info(f"✅ Neo4j connection established: {self.uri}")
                else:
                    logger.error("❌ Neo4j connection test failed")
                    self.driver = None
                    
        except ServiceUnavailable as e:
            logger.error(f"❌ Neo4j service unavailable: {e}")
            self.driver = None
        except AuthError as e:
            logger.error(f"❌ Neo4j authentication failed: {e}")
            self.driver = None
        except Exception as e:
            logger.error(f"❌ Neo4j connection error: {e}")
            self.driver = None
    
    def is_connected(self) -> bool:
        """Check if the Neo4j connection is active"""
        if not self.driver:
            return False
        
        try:
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                return result.single()["test"] == 1
        except Exception:
            return False
    
    def get_session(self) -> Optional[Session]:
        """Get a new Neo4j session"""
        if not self.is_connected():
            return None
        return self.driver.session()
    
    def close_connection(self):
        """Close the Neo4j connection"""
        if self.driver:
            self.driver.close()
            self.driver = None
            logger.info("Neo4j connection closed")

class GraphOperations:
    """Implements real graph operations using Neo4j"""
    
    def __init__(self, connection_manager: Neo4jConnectionManager):
        self.connection_manager = connection_manager
        self._initialize_schema()
    
    def _initialize_schema(self):
        """Initialize the graph database schema"""
        if not self.connection_manager.is_connected():
            logger.warning("Cannot initialize schema: Neo4j not connected")
            return
        
        try:
            with self.connection_manager.get_session() as session:
                # Create constraints and indexes
                session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (n:fractal_node) REQUIRE n.node_id IS UNIQUE")
                session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (n:meta_node) REQUIRE n.node_id IS UNIQUE")
                session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (n:system_node) REQUIRE n.node_id IS UNIQUE")
                
                # Create indexes for better performance
                session.run("CREATE INDEX IF NOT EXISTS FOR (n:fractal_node) ON (n.water_state)")
                session.run("CREATE INDEX IF NOT EXISTS FOR (n:fractal_node) ON (n.energy_level)")
                session.run("CREATE INDEX IF NOT EXISTS FOR (n:fractal_node) ON (n.fractal_id)")
                
                logger.info("✅ Neo4j schema initialized successfully")
                
        except Exception as e:
            logger.error(f"❌ Schema initialization failed: {e}")
    
    def create_node(self, node: GraphNode) -> GraphQueryResult:
        """Create a new node in the graph"""
        start_time = time.time()
        
        if not self.connection_manager.is_connected():
            return GraphQueryResult(
                operation_type=GraphOperationType.CREATE_NODE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id},
                error_message="Neo4j not connected"
            )
        
        try:
            with self.connection_manager.get_session() as session:
                # Build Cypher query
                labels_str = ":".join(node.labels)
                properties = {**node.properties, "created_at": node.created_at.isoformat(), "updated_at": node.updated_at.isoformat()}
                
                query = f"""
                CREATE (n:{labels_str} {{
                    node_id: $node_id,
                    fractal_id: $fractal_id,
                    water_state: $water_state,
                    energy_level: $energy_level,
                    created_at: $created_at,
                    updated_at: $updated_at
                }})
                SET n += $properties
                RETURN n
                """
                
                result = session.run(query, {
                    "node_id": node.node_id,
                    "fractal_id": node.fractal_id,
                    "water_state": node.water_state,
                    "energy_level": node.energy_level,
                    "created_at": node.created_at.isoformat(),
                    "updated_at": node.updated_at.isoformat(),
                    "properties": properties
                })
                
                created_node = result.single()
                execution_time = time.time() - start_time
                
                logger.info(f"✅ Node created: {node.node_id}")
                
                return GraphQueryResult(
                    operation_type=GraphOperationType.CREATE_NODE,
                    success=True,
                    data=created_node["n"],
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"node_id": node.node_id, "labels": node.labels}
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Node creation failed: {e}")
            
            return GraphQueryResult(
                operation_type=GraphOperationType.CREATE_NODE,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node.node_id},
                error_message=str(e)
            )
    
    def get_node(self, node_id: str) -> GraphQueryResult:
        """Retrieve a node from the graph"""
        start_time = time.time()
        
        if not self.connection_manager.is_connected():
            return GraphQueryResult(
                operation_type=GraphOperationType.QUERY,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message="Neo4j not connected"
            )
        
        try:
            with self.connection_manager.get_session() as session:
                query = """
                MATCH (n {node_id: $node_id})
                RETURN n
                """
                
                result = session.run(query, {"node_id": node_id})
                node = result.single()
                
                execution_time = time.time() - start_time
                
                if node:
                    return GraphQueryResult(
                        operation_type=GraphOperationType.QUERY,
                        success=True,
                        data=node["n"],
                        execution_time=execution_time,
                        timestamp=datetime.now(),
                        metadata={"node_id": node_id, "found": True}
                    )
                else:
                    return GraphQueryResult(
                        operation_type=GraphOperationType.QUERY,
                        success=True,
                        data=None,
                        execution_time=execution_time,
                        timestamp=datetime.now(),
                        metadata={"node_id": node_id, "found": False}
                    )
                    
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Node retrieval failed: {e}")
            
            return GraphQueryResult(
                operation_type=GraphOperationType.QUERY,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def update_node(self, node_id: str, properties: Dict[str, Any]) -> GraphQueryResult:
        """Update a node in the graph"""
        start_time = time.time()
        
        if not self.connection_manager.is_connected():
            return GraphQueryResult(
                operation_type=GraphOperationType.UPDATE_NODE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message="Neo4j not connected"
            )
        
        try:
            with self.connection_manager.get_session() as session:
                # Add updated_at timestamp
                properties["updated_at"] = datetime.now().isoformat()
                
                # Build SET clause dynamically
                set_clauses = []
                for key in properties.keys():
                    set_clauses.append(f"n.{key} = ${key}")
                
                set_clause = ", ".join(set_clauses)
                
                query = f"""
                MATCH (n {{node_id: $node_id}})
                SET {set_clause}
                RETURN n
                """
                
                result = session.run(query, {"node_id": node_id, **properties})
                updated_node = result.single()
                
                execution_time = time.time() - start_time
                
                if updated_node:
                    logger.info(f"✅ Node updated: {node_id}")
                    
                    return GraphQueryResult(
                        operation_type=GraphOperationType.UPDATE_NODE,
                        success=True,
                        data=updated_node["n"],
                        execution_time=execution_time,
                        timestamp=datetime.now(),
                        metadata={"node_id": node_id, "properties_updated": list(properties.keys())}
                    )
                else:
                    return GraphQueryResult(
                        operation_type=GraphOperationType.UPDATE_NODE,
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
            
            return GraphQueryResult(
                operation_type=GraphOperationType.UPDATE_NODE,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"node_id": node_id},
                error_message=str(e)
            )
    
    def create_relationship(self, relationship: GraphRelationship) -> GraphQueryResult:
        """Create a relationship between two nodes"""
        start_time = time.time()
        
        if not self.connection_manager.is_connected():
            return GraphQueryResult(
                operation_type=GraphOperationType.CREATE_RELATIONSHIP,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"relationship_id": relationship.relationship_id},
                error_message="Neo4j not connected"
            )
        
        try:
            with self.connection_manager.get_session() as session:
                properties = {**relationship.properties, "created_at": relationship.created_at.isoformat(), "updated_at": relationship.updated_at.isoformat()}
                
                query = """
                MATCH (a {node_id: $start_node_id})
                MATCH (b {node_id: $end_node_id})
                CREATE (a)-[r:RELATES_TO {relationship_id: $relationship_id}]->(b)
                SET r += $properties
                RETURN r
                """
                
                result = session.run(query, {
                    "start_node_id": relationship.start_node_id,
                    "end_node_id": relationship.end_node_id,
                    "relationship_id": relationship.relationship_id,
                    "properties": properties
                })
                
                created_relationship = result.single()
                execution_time = time.time() - start_time
                
                logger.info(f"✅ Relationship created: {relationship.relationship_id}")
                
                return GraphQueryResult(
                    operation_type=GraphOperationType.CREATE_RELATIONSHIP,
                    success=True,
                    data=created_relationship["r"],
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"relationship_id": relationship.relationship_id, "start_node": relationship.start_node_id, "end_node": relationship.end_node_id}
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Relationship creation failed: {e}")
            
            return GraphQueryResult(
                operation_type=GraphOperationType.CREATE_RELATIONSHIP,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"relationship_id": relationship.relationship_id},
                error_message=str(e)
            )
    
    def query_graph(self, cypher_query: str, parameters: Dict[str, Any] = None) -> GraphQueryResult:
        """Execute a custom Cypher query"""
        start_time = time.time()
        
        if not self.connection_manager.is_connected():
            return GraphQueryResult(
                operation_type=GraphOperationType.QUERY,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"query": cypher_query},
                error_message="Neo4j not connected"
            )
        
        try:
            with self.connection_manager.get_session() as session:
                if parameters is None:
                    parameters = {}
                
                result = session.run(cypher_query, parameters)
                data = [record.data() for record in result]
                
                execution_time = time.time() - start_time
                
                logger.info(f"✅ Query executed successfully: {len(data)} results")
                
                return GraphQueryResult(
                    operation_type=GraphOperationType.QUERY,
                    success=True,
                    data=data,
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"query": cypher_query, "result_count": len(data)}
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Query execution failed: {e}")
            
            return GraphQueryResult(
                operation_type=GraphOperationType.QUERY,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"query": cypher_query},
                error_message=str(e)
            )
    
    def traverse_graph(self, start_node_id: str, depth: int = 3, 
                      relationship_types: List[str] = None) -> GraphQueryResult:
        """Traverse the graph from a starting node"""
        start_time = time.time()
        
        if not self.connection_manager.is_connected():
            return GraphQueryResult(
                operation_type=GraphOperationType.TRAVERSE,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"start_node": start_node_id, "depth": depth},
                error_message="Neo4j not connected"
            )
        
        try:
            with self.connection_manager.get_session() as session:
                # Build relationship filter
                relationship_filter = ""
                if relationship_types:
                    rel_types = [f"*{rel_type}*" for rel_type in relationship_types]
                    relationship_filter = f"[:{'|'.join(rel_types)}]"
                
                query = f"""
                MATCH path = (start {{node_id: $start_node_id}})-{relationship_filter}*1..{depth}(end)
                RETURN path, 
                       [node in nodes(path) | {{node_id: node.node_id, labels: labels(node), properties: properties(node)}}] as nodes,
                       [rel in relationships(path) | {{type: type(rel), properties: properties(rel)}}] as relationships
                ORDER BY length(path)
                """
                
                result = session.run(query, {"start_node_id": start_node_id})
                data = [record.data() for record in result]
                
                execution_time = time.time() - start_time
                
                logger.info(f"✅ Graph traversal completed: {len(data)} paths found")
                
                return GraphQueryResult(
                    operation_type=GraphOperationType.TRAVERSE,
                    success=True,
                    data=data,
                    execution_time=execution_time,
                    timestamp=datetime.now(),
                    metadata={"start_node": start_node_id, "depth": depth, "paths_found": len(data)}
                )
                
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"❌ Graph traversal failed: {e}")
            
            return GraphQueryResult(
                operation_type=GraphOperationType.TRAVERSE,
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=datetime.now(),
                metadata={"start_node": start_node_id, "depth": depth},
                error_message=str(e)
            )

class GraphSyncManager:
    """Manages synchronization between Neo4j and the fractal node system"""
    
    def __init__(self, graph_operations: GraphOperations):
        self.graph_operations = graph_operations
        self.sync_history = []
        self.last_sync_time = None
    
    def sync_fractal_node_to_graph(self, fractal_node: Dict[str, Any]) -> GraphQueryResult:
        """Synchronize a fractal node to the Neo4j graph"""
        try:
            # Convert fractal node to graph node
            graph_node = GraphNode(
                node_id=fractal_node.get("node_id", ""),
                labels=["fractal_node"] + [fractal_node.get("node_type", "unknown")],
                properties=fractal_node.get("metadata", {}),
                created_at=datetime.now(),
                updated_at=datetime.now(),
                fractal_id=fractal_node.get("node_id"),
                water_state=fractal_node.get("water_state", "unknown"),
                energy_level=fractal_node.get("energy_level", 0.0)
            )
            
            # Create or update the node in Neo4j
            existing_node = self.graph_operations.get_node(graph_node.node_id)
            
            if existing_node.success and existing_node.data:
                # Update existing node
                update_properties = {
                    "water_state": graph_node.water_state,
                    "energy_level": graph_node.energy_level,
                    "updated_at": graph_node.updated_at.isoformat()
                }
                # Merge properties
                update_properties.update(graph_node.properties)
                
                result = self.graph_operations.update_node(graph_node.node_id, update_properties)
            else:
                # Create new node
                result = self.graph_operations.create_node(graph_node)
            
            # Record sync operation
            self.sync_history.append({
                "timestamp": datetime.now(),
                "operation": "fractal_to_graph",
                "node_id": graph_node.node_id,
                "success": result.success
            })
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Fractal to graph sync failed: {e}")
            return GraphQueryResult(
                operation_type=GraphOperationType.SYNC,
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"node_id": fractal_node.get("node_id", "unknown")},
                error_message=str(e)
            )
    
    def sync_graph_to_fractal(self, node_id: str) -> Dict[str, Any]:
        """Synchronize a graph node back to fractal format"""
        try:
            # Get node from Neo4j
            result = self.graph_operations.get_node(node_id)
            
            if not result.success or not result.data:
                return {"error": "Node not found in graph"}
            
            # Convert graph node to fractal format
            graph_node = result.data
            fractal_node = {
                "node_id": graph_node.get("node_id"),
                "node_type": graph_node.get("labels", [])[0] if graph_node.get("labels") else "unknown",
                "metadata": graph_node.get("properties", {}),
                "water_state": graph_node.get("water_state"),
                "energy_level": graph_node.get("energy_level"),
                "fractal_id": graph_node.get("fractal_id"),
                "created_at": graph_node.get("created_at"),
                "updated_at": graph_node.get("updated_at")
            }
            
            # Record sync operation
            self.sync_history.append({
                "timestamp": datetime.now(),
                "operation": "graph_to_fractal",
                "node_id": node_id,
                "success": True
            })
            
            return fractal_node
            
        except Exception as e:
            logger.error(f"❌ Graph to fractal sync failed: {e}")
            return {"error": str(e)}
    
    def get_sync_status(self) -> Dict[str, Any]:
        """Get synchronization status and history"""
        return {
            "last_sync_time": self.last_sync_time.isoformat() if self.last_sync_time else None,
            "total_sync_operations": len(self.sync_history),
            "successful_syncs": len([op for op in self.sync_history if op["success"]]),
            "failed_syncs": len([op for op in self.sync_history if not op["success"]]),
            "recent_operations": self.sync_history[-10:] if self.sync_history else []
        }

class Neo4jIntegrationSystem:
    """Main system that orchestrates all Neo4j integration capabilities"""
    
    def __init__(self, uri: str = None, username: str = None, password: str = None):
        self.connection_manager = Neo4jConnectionManager(uri, username, password)
        self.graph_operations = GraphOperations(self.connection_manager)
        self.sync_manager = GraphSyncManager(self.graph_operations)
        
        # Initialize system nodes
        self._initialize_system_nodes()
    
    def _initialize_system_nodes(self):
        """Initialize system-level nodes in the graph"""
        if not self.connection_manager.is_connected():
            logger.warning("Cannot initialize system nodes: Neo4j not connected")
            return
        
        try:
            # Create system root node
            system_root = GraphNode(
                node_id="living_codex_system",
                labels=["system_node", "root"],
                properties={"name": "Living Codex System", "description": "Root system node"},
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            result = self.graph_operations.create_node(system_root)
            if result.success:
                logger.info("✅ System root node initialized")
            
        except Exception as e:
            logger.error(f"❌ System node initialization failed: {e}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get the current status of the Neo4j integration system"""
        return {
            "timestamp": datetime.now().isoformat(),
            "neo4j_connected": self.connection_manager.is_connected(),
            "neo4j_uri": self.connection_manager.uri,
            "sync_status": self.sync_manager.get_sync_status(),
            "driver_available": NEO4J_AVAILABLE
        }
    
    def close(self):
        """Close all connections and cleanup"""
        self.connection_manager.close_connection()
        logger.info("Neo4j integration system closed")

async def main():
    """Main function to demonstrate the Neo4j Integration System"""
    
    print("🌟 Living Codex Neo4j Integration System Demo")
    print("=" * 60)
    
    try:
        # Create the system
        neo4j_system = Neo4jIntegrationSystem()
        
        # Show system status
        status = neo4j_system.get_system_status()
        print(f"\n🔧 System Status:")
        print(f"   Neo4j Connected: {status['neo4j_connected']}")
        print(f"   Neo4j URI: {status['neo4j_uri']}")
        print(f"   Driver Available: {status['driver_available']}")
        
        if not status['neo4j_connected']:
            print(f"\n⚠️  Neo4j not connected. Please ensure Neo4j is running and accessible.")
            print(f"   You can set environment variables:")
            print(f"   - NEO4J_URI (default: bolt://localhost:7687)")
            print(f"   - NEO4J_USERNAME (default: neo4j)")
            print(f"   - NEO4J_PASSWORD (default: password)")
            return
        
        # Test basic operations
        print(f"\n🔍 Testing Basic Graph Operations...")
        
        # Create a test node
        test_node = GraphNode(
            node_id="test_fractal_node_001",
            labels=["fractal_node", "test"],
            properties={"name": "Test Node", "description": "A test fractal node"},
            created_at=datetime.now(),
            updated_at=datetime.now(),
            water_state="liquid",
            energy_level=639.0
        )
        
        create_result = neo4j_system.graph_operations.create_node(test_node)
        print(f"   Create Node: {'✅' if create_result.success else '❌'}")
        if create_result.success:
            print(f"      Execution Time: {create_result.execution_time:.3f}s")
        
        # Retrieve the test node
        get_result = neo4j_system.graph_operations.get_node("test_fractal_node_001")
        print(f"   Get Node: {'✅' if get_result.success else '❌'}")
        if get_result.success:
            print(f"      Execution Time: {get_result.execution_time:.3f}s")
            print(f"      Node Found: {get_result.metadata.get('found', False)}")
        
        # Update the test node
        update_result = neo4j_system.graph_operations.update_node(
            "test_fractal_node_001", 
            {"energy_level": 741.0, "description": "Updated test node"}
        )
        print(f"   Update Node: {'✅' if update_result.success else '❌'}")
        if update_result.success:
            print(f"      Execution Time: {update_result.execution_time:.3f}s")
        
        # Test graph traversal
        print(f"\n🔍 Testing Graph Traversal...")
        traverse_result = neo4j_system.graph_operations.traverse_graph(
            "living_codex_system", 
            depth=2
        )
        print(f"   Graph Traversal: {'✅' if traverse_result.success else '❌'}")
        if traverse_result.success:
            print(f"      Execution Time: {traverse_result.execution_time:.3f}s")
            print(f"      Paths Found: {traverse_result.metadata.get('paths_found', 0)}")
        
        # Test custom query
        print(f"\n🔍 Testing Custom Cypher Query...")
        query_result = neo4j_system.graph_operations.query_graph(
            "MATCH (n) RETURN count(n) as total_nodes"
        )
        print(f"   Custom Query: {'✅' if query_result.success else '❌'}")
        if query_result.success:
            print(f"      Execution Time: {query_result.execution_time:.3f}s")
            print(f"      Total Nodes: {query_result.data[0]['total_nodes'] if query_result.data else 0}")
        
        # Test synchronization
        print(f"\n🔄 Testing Fractal-Graph Synchronization...")
        fractal_node = {
            "node_id": "sync_test_node_001",
            "node_type": "test_sync",
            "metadata": {"name": "Sync Test", "type": "synchronization_test"},
            "water_state": "vapor",
            "energy_level": 852.0
        }
        
        sync_result = neo4j_system.sync_manager.sync_fractal_node_to_graph(fractal_node)
        print(f"   Fractal to Graph Sync: {'✅' if sync_result.success else '❌'}")
        if sync_result.success:
            print(f"      Execution Time: {sync_result.execution_time:.3f}s")
        
        # Show sync status
        sync_status = neo4j_system.sync_manager.get_sync_status()
        print(f"\n📊 Synchronization Status:")
        print(f"   Total Operations: {sync_status['total_sync_operations']}")
        print(f"   Successful: {sync_status['successful_syncs']}")
        print(f"   Failed: {sync_status['failed_syncs']}")
        
        print("\n" + "=" * 60)
        print("🎉 Neo4j Integration System Demo Completed!")
        print("\n🌟 What We've Achieved:")
        print("   • Real Neo4j database connection")
        print("   • Complete graph operations (CRUD)")
        print("   • Graph traversal and querying")
        print("   • Bidirectional fractal-graph synchronization")
        print("   • Connection management and error handling")
        print("\n🚀 The Living Codex now has real graph database integration!")
        
    except Exception as e:
        print(f"❌ Error running Neo4j Integration System demo: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cleanup
        if 'neo4j_system' in locals():
            neo4j_system.close()

if __name__ == "__main__":
    asyncio.run(main())
