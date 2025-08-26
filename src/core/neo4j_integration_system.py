#!/usr/bin/env python3
"""
Fractal Neo4j Integration System Component - Living Codex
Replaces simulated graph operations with real Neo4j database connections
and operations, providing bidirectional synchronization with the fractal node system.

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level

UPDATED: Now uses modular components from src/graph/ while maintaining backward compatibility
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

from .fractal_components import FractalComponent

# Import new modular components
try:
    # Try relative imports first (when used as package)
    from ..graph.core.models import (
        GraphNode, GraphRelationship, GraphQueryResult,
        GraphOperationType, GraphNodeType
    )
    from ..graph.neo4j.connection_manager import Neo4jConnectionManager
    from ..graph.neo4j.neo4j_operations import Neo4jOperations
    MODULAR_IMPORTS_AVAILABLE = True
    print("✅ Using new modular graph components")
except ImportError:
    try:
        # Try absolute imports (when src is in path, e.g., CLI)
        from graph.core.models import (
            GraphNode, GraphRelationship, GraphQueryResult,
            GraphOperationType, GraphNodeType
        )
        from graph.neo4j.connection_manager import Neo4jConnectionManager
        from graph.neo4j.neo4j_operations import Neo4jOperations
        MODULAR_IMPORTS_AVAILABLE = True
        print("✅ Using new modular graph components")
    except ImportError:
        MODULAR_IMPORTS_AVAILABLE = False
        print("⚠️  Modular imports not available, using legacy components")

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

# Legacy enums and models (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
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

    @dataclass
    class GraphRelationship:
        """Represents a relationship in the Neo4j graph"""
        relationship_id: str
        start_node_id: str
        end_node_id: str
        relationship_type: str
        properties: Dict[str, Any]
        created_at: datetime

    @dataclass
    class GraphQueryResult:
        """Result of a graph query operation"""
        success: bool
        data: Any
        execution_time: float
        timestamp: datetime
        metadata: Dict[str, Any]
        error_message: Optional[str] = None

class FractalNeo4jIntegrationComponent(FractalComponent):
    """
    Fractal component for Neo4j graph database integration
    Provides bidirectional synchronization with the fractal node system
    """
    
    def __init__(self):
        super().__init__(
            component_type="neo4j_integration_system",
            name="Fractal Neo4j Integration System",
            content="Neo4j graph database integration for fractal node synchronization",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        # Initialize Neo4j components
        self.connection_manager = None
        self.neo4j_operations = None
        self.connected = False
        
        # Create graph capability nodes
        self._create_graph_capability_nodes()
        
        # Initialize Neo4j connection
        self._initialize_neo4j()
    
    def _create_graph_capability_nodes(self):
        """Create fractal nodes for graph capabilities"""
        capabilities = [
            {
                "name": "Graph Database Integration",
                "content": "Neo4j graph database integration",
                "metadata": {"database": "neo4j", "type": "graph", "scalability": "high"}
            },
            {
                "name": "Bidirectional Synchronization",
                "content": "Sync fractal nodes with graph database",
                "metadata": {"sync_type": "bidirectional", "direction": "both_ways"}
            },
            {
                "name": "Graph Query Language",
                "content": "Cypher query language support",
                "metadata": {"query_language": "cypher", "power": "high"}
            },
            {
                "name": "Relationship Management",
                "content": "Manage complex node relationships",
                "metadata": {"feature": "relationships", "complexity": "high"}
            },
            {
                "name": "Graph Traversal",
                "content": "Navigate graph structure efficiently",
                "metadata": {"feature": "traversal", "efficiency": "high"}
            },
            {
                "name": "Real-time Updates",
                "content": "Real-time graph database updates",
                "metadata": {"feature": "real_time", "latency": "low"}
            }
        ]
        
        for capability in capabilities:
            self.create_child_node(
                node_type="graph_capability",
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
    
    def _initialize_neo4j(self):
        """Initialize Neo4j connection and operations"""
        try:
            if MODULAR_IMPORTS_AVAILABLE and NEO4J_AVAILABLE:
                # Use modular components
                self.connection_manager = Neo4jConnectionManager()
                self.neo4j_operations = Neo4jOperations(self.connection_manager)
                self.connected = self.connection_manager.test_connection()
                logger.info("✅ Neo4j initialized with modular components")
            else:
                # Use legacy components or fallback
                self.connected = False
                logger.warning("⚠️  Neo4j not fully initialized - modular components or driver unavailable")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Neo4j: {e}")
            self.connected = False
    
    def create_graph_node(self, fractal_node_id: str, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a node in the Neo4j graph from fractal node data"""
        if not self.connected:
            return {"success": False, "error": "Neo4j not connected"}
        
        try:
            # Create graph node
            graph_node = GraphNode(
                node_id=f"graph_{fractal_node_id}",
                labels=["FractalNode", node_data.get("node_type", "Unknown")],
                properties={
                    "fractal_id": fractal_node_id,
                    "name": node_data.get("name", ""),
                    "content": node_data.get("content", ""),
                    "fractal_layer": node_data.get("fractal_layer", 0),
                    "water_state": node_data.get("water_state", "unknown"),
                    "frequency": node_data.get("frequency", 0),
                    "chakra": node_data.get("chakra", "unknown")
                },
                created_at=datetime.now(),
                updated_at=datetime.now(),
                fractal_id=fractal_node_id
            )
            
            # Store in Neo4j
            result = self.neo4j_operations.create_node(graph_node)
            
            # Create fractal node for the graph operation
            self._create_graph_operation_node("create_node", fractal_node_id, result.success)
            
            return {
                "success": result.success,
                "graph_node_id": graph_node.node_id,
                "fractal_node_id": fractal_node_id
            }
            
        except Exception as e:
            logger.error(f"Error creating graph node for {fractal_node_id}: {e}")
            return {"success": False, "error": str(e)}
    
    def create_graph_relationship(self, source_id: str, target_id: str, 
                                relationship_type: str, properties: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create a relationship between two nodes in the graph"""
        if not self.connected:
            return {"success": False, "error": "Neo4j not connected"}
        
        try:
            # Create graph relationship
            relationship = GraphRelationship(
                relationship_id=f"rel_{source_id}_{target_id}_{int(time.time())}",
                start_node_id=f"graph_{source_id}",
                end_node_id=f"graph_{target_id}",
                relationship_type=relationship_type,
                properties=properties or {},
                created_at=datetime.now()
            )
            
            # Store in Neo4j
            result = self.neo4j_operations.create_relationship(relationship)
            
            # Create fractal node for the graph operation
            self._create_graph_operation_node("create_relationship", f"{source_id}->{target_id}", result.success)
            
            return {
                "success": result.success,
                "relationship_id": relationship.relationship_id,
                "relationship_type": relationship_type
            }
            
        except Exception as e:
            logger.error(f"Error creating graph relationship: {e}")
            return {"success": False, "error": str(e)}
    
    def query_graph(self, cypher_query: str, parameters: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a Cypher query on the graph database"""
        if not self.connected:
            return {"success": False, "error": "Neo4j not connected"}
        
        try:
            # Execute query
            result = self.neo4j_operations.execute_query(cypher_query, parameters or {})
            
            # Create fractal node for the graph operation
            self._create_graph_operation_node("query", f"cypher_{len(cypher_query)}", result.success)
            
            return {
                "success": result.success,
                "data": result.data,
                "execution_time": result.execution_time,
                "result_count": len(result.data) if result.data else 0
            }
            
        except Exception as e:
            logger.error(f"Error executing graph query: {e}")
            return {"success": False, "error": str(e)}
    
    def sync_fractal_to_graph(self, fractal_nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Synchronize multiple fractal nodes to the graph database"""
        if not self.connected:
            return {"success": False, "error": "Neo4j not connected"}
        
        try:
            results = {
                "total_nodes": len(fractal_nodes),
                "created_nodes": 0,
                "failed_nodes": 0,
                "errors": []
            }
            
            for node_data in fractal_nodes:
                result = self.create_graph_node(
                    node_data.get("node_id", ""),
                    node_data
                )
                
                if result["success"]:
                    results["created_nodes"] += 1
                else:
                    results["failed_nodes"] += 1
                    results["errors"].append(result.get("error", "Unknown error"))
            
            # Create fractal node for the sync operation
            self._create_graph_operation_node("sync", f"batch_{len(fractal_nodes)}", results["failed_nodes"] == 0)
            
            return {
                "success": results["failed_nodes"] == 0,
                "results": results
            }
            
        except Exception as e:
            logger.error(f"Error syncing fractal nodes to graph: {e}")
            return {"success": False, "error": str(e)}
    
    def _create_graph_operation_node(self, operation_type: str, target_id: str, success: bool):
        """Create fractal node for graph operation"""
        status_text = "✅ Success" if success else "❌ Failed"
        
        self.create_child_node(
            node_type="graph_operation",
            name=f"{operation_type.title()} Operation - {status_text}",
            content=f"Graph {operation_type} operation on {target_id}",
            metadata={
                "operation_type": operation_type,
                "target_id": target_id,
                "success": success,
                "timestamp": datetime.now().isoformat(),
                "neo4j_connected": self.connected
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
    
    def get_graph_status(self) -> Dict[str, Any]:
        """Get current graph database status and capabilities"""
        return {
            "neo4j_connected": self.connected,
            "modular_imports_available": MODULAR_IMPORTS_AVAILABLE,
            "neo4j_driver_available": NEO4J_AVAILABLE,
            "capabilities": [
                "graph_database_integration",
                "bidirectional_synchronization",
                "graph_query_language",
                "relationship_management",
                "graph_traversal",
                "real_time_updates"
            ],
            "operations_supported": [
                "create_graph_node",
                "create_graph_relationship",
                "query_graph",
                "sync_fractal_to_graph"
            ],
            "connection_info": {
                "status": "connected" if self.connected else "disconnected",
                "driver": "neo4j" if NEO4J_AVAILABLE else "unavailable"
            }
        }

# Create and register the fractal component
fractal_neo4j_integration = FractalNeo4jIntegrationComponent()
