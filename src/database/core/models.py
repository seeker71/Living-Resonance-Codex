"""
Database Core Models
Core data models for database operations
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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
