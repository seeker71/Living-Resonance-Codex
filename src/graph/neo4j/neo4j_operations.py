"""
Neo4j Operations
Implements real graph operations using Neo4j
"""

import time
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from ..core.operations import GraphOperations
from ..core.models import (
    GraphNode, GraphRelationship, GraphQueryResult,
    GraphOperationType, GraphNodeType
)
from .connection_manager import Neo4jConnectionManager

logger = logging.getLogger(__name__)

class Neo4jOperations(GraphOperations):
    """Implements real graph operations using Neo4j"""
    
    def __init__(self, connection_manager: Neo4jConnectionManager):
        super().__init__()
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
        
        try:
            if not self.connection_manager.is_connected():
                return self._create_query_result(
                    GraphOperationType.CREATE_NODE,
                    False,
                    None,
                    time.time() - start_time,
                    "Neo4j not connected"
                )
            
            with self.connection_manager.get_session() as session:
                # Prepare properties for Neo4j
                properties = {
                    "node_id": node.node_id,
                    "fractal_id": node.fractal_id,
                    "water_state": node.water_state,
                    "energy_level": node.energy_level,
                    "created_at": node.created_at.isoformat(),
                    "updated_at": node.updated_at.isoformat()
                }
                
                # Add custom properties
                if node.properties:
                    properties.update(node.properties)
                
                # Create the node with labels
                labels_str = ":".join(node.labels)
                query = f"CREATE (n:{labels_str} $properties) RETURN n"
                
                result = session.run(query, properties=properties)
                created_node = result.single()
                
                if created_node:
                    logger.info(f"✅ Node created: {node.node_id}")
                    return self._create_query_result(
                        GraphOperationType.CREATE_NODE,
                        True,
                        created_node["n"],
                        time.time() - start_time,
                        metadata={"node_id": node.node_id, "labels": node.labels}
                    )
                else:
                    return self._create_query_result(
                        GraphOperationType.CREATE_NODE,
                        False,
                        None,
                        time.time() - start_time,
                        "Node creation failed - no result returned"
                    )
                    
        except Exception as e:
            logger.error(f"❌ Node creation failed: {e}")
            return self._create_query_result(
                GraphOperationType.CREATE_NODE,
                False,
                None,
                time.time() - start_time,
                str(e)
            )
    
    def update_node(self, node: GraphNode) -> GraphQueryResult:
        """Update an existing node"""
        start_time = time.time()
        
        try:
            if not self.connection_manager.is_connected():
                return self._create_query_result(
                    GraphOperationType.UPDATE_NODE,
                    False,
                    None,
                    time.time() - start_time,
                    "Neo4j not connected"
                )
            
            with self.connection_manager.get_session() as session:
                # Prepare properties for update
                properties = {
                    "node_id": node.node_id,
                    "fractal_id": node.fractal_id,
                    "water_state": node.water_state,
                    "energy_level": node.energy_level,
                    "updated_at": datetime.now().isoformat()
                }
                
                # Add custom properties
                if node.properties:
                    properties.update(node.properties)
                
                # Update the node
                query = """
                MATCH (n {node_id: $node_id})
                SET n += $properties
                RETURN n
                """
                
                result = session.run(query, properties=properties)
                updated_node = result.single()
                
                if updated_node:
                    logger.info(f"✅ Node updated: {node.node_id}")
                    return self._create_query_result(
                        GraphOperationType.UPDATE_NODE,
                        True,
                        updated_node["n"],
                        time.time() - start_time,
                        metadata={"node_id": node.node_id}
                    )
                else:
                    return self._create_query_result(
                        GraphOperationType.UPDATE_NODE,
                        False,
                        None,
                        time.time() - start_time,
                        "Node not found for update"
                    )
                    
        except Exception as e:
            logger.error(f"❌ Node update failed: {e}")
            return self._create_query_result(
                GraphOperationType.UPDATE_NODE,
                False,
                None,
                time.time() - start_time,
                str(e)
            )
    
    def delete_node(self, node_id: str) -> GraphQueryResult:
        """Delete a node from the graph"""
        start_time = time.time()
        
        try:
            if not self.connection_manager.is_connected():
                return self._create_query_result(
                    GraphOperationType.DELETE_NODE,
                    False,
                    None,
                    time.time() - start_time,
                    "Neo4j not connected"
                )
            
            with self.connection_manager.get_session() as session:
                # Delete the node and its relationships
                query = """
                MATCH (n {node_id: $node_id})
                OPTIONAL MATCH (n)-[r]-()
                DELETE r, n
                RETURN count(n) as deleted_count
                """
                
                result = session.run(query, node_id=node_id)
                deleted_count = result.single()["deleted_count"]
                
                if deleted_count > 0:
                    logger.info(f"✅ Node deleted: {node_id}")
                    return self._create_query_result(
                        GraphOperationType.DELETE_NODE,
                        True,
                        {"deleted_count": deleted_count},
                        time.time() - start_time,
                        metadata={"node_id": node_id}
                    )
                else:
                    return self._create_query_result(
                        GraphOperationType.DELETE_NODE,
                        False,
                        None,
                        time.time() - start_time,
                        "Node not found for deletion"
                    )
                    
        except Exception as e:
            logger.error(f"❌ Node deletion failed: {e}")
            return self._create_query_result(
                GraphOperationType.DELETE_NODE,
                False,
                None,
                time.time() - start_time,
                str(e)
            )
    
    def query_graph(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> GraphQueryResult:
        """Execute a graph query"""
        start_time = time.time()
        
        try:
            if not self.connection_manager.is_connected():
                return self._create_query_result(
                    GraphOperationType.QUERY,
                    False,
                    None,
                    time.time() - start_time,
                    "Neo4j not connected"
                )
            
            with self.connection_manager.get_session() as session:
                params = parameters or {}
                result = session.run(query, **params)
                
                # Collect all results
                data = [record.data() for record in result]
                
                logger.info(f"✅ Graph query executed: {len(data)} results")
                return self._create_query_result(
                    GraphOperationType.QUERY,
                    True,
                    data,
                    time.time() - start_time,
                    metadata={"query": query, "parameters": params, "result_count": len(data)}
                )
                
        except Exception as e:
            logger.error(f"❌ Graph query failed: {e}")
            return self._create_query_result(
                GraphOperationType.QUERY,
                False,
                None,
                time.time() - start_time,
                str(e)
            )
    
    def traverse_graph(self, start_node_id: str, max_depth: int = 3, 
                      relationship_types: Optional[List[str]] = None) -> GraphQueryResult:
        """Traverse the graph from a starting node"""
        start_time = time.time()
        
        try:
            if not self.connection_manager.is_connected():
                return self._create_query_result(
                    GraphOperationType.TRAVERSE,
                    False,
                    None,
                    time.time() - start_time,
                    "Neo4j not connected"
                )
            
            with self.connection_manager.get_session() as session:
                # Build relationship filter
                rel_filter = ""
                if relationship_types:
                    rel_types = [f"'{rt}'" for rt in relationship_types]
                    rel_filter = f"WHERE type(r) IN [{','.join(rel_types)}]"
                
                # Traverse query
                query = f"""
                MATCH path = (start {{node_id: $start_node_id}})-[r*1..{max_depth}]-(end)
                {rel_filter}
                RETURN path, length(path) as depth
                ORDER BY depth
                """
                
                result = session.run(query, start_node_id=start_node_id)
                paths = [record.data() for record in result]
                
                logger.info(f"✅ Graph traversal completed: {len(paths)} paths found")
                return self._create_query_result(
                    GraphOperationType.TRAVERSE,
                    True,
                    paths,
                    time.time() - start_time,
                    metadata={
                        "start_node_id": start_node_id,
                        "max_depth": max_depth,
                        "relationship_types": relationship_types,
                        "paths_found": len(paths)
                    }
                )
                
        except Exception as e:
            logger.error(f"❌ Graph traversal failed: {e}")
            return self._create_query_result(
                GraphOperationType.TRAVERSE,
                False,
                None,
                time.time() - start_time,
                str(e)
            )
