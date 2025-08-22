"""
Graph Core Models
Core data models for graph operations
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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
