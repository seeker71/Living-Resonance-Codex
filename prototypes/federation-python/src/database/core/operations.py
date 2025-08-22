"""
Database Core Operations
Base database operations and query functionality
"""

import time
import logging
from typing import List, Dict, Any, Optional, Tuple, Union
from datetime import datetime
from .models import (
    DatabaseNode, DatabaseOperationResult, QueryFilter, QueryOptions,
    OperationType, DatabaseType
)

logger = logging.getLogger(__name__)

class DatabaseOperations:
    """Base class for database operations"""
    
    def __init__(self, database_type: DatabaseType):
        self.database_type = database_type
        self.operation_history = []
    
    def create_node(self, node: DatabaseNode) -> DatabaseOperationResult:
        """Create a new node in the database (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement create_node")
    
    def read_node(self, node_id: str) -> DatabaseOperationResult:
        """Read a node from the database (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement read_node")
    
    def update_node(self, node: DatabaseNode) -> DatabaseOperationResult:
        """Update an existing node (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement update_node")
    
    def delete_node(self, node_id: str) -> DatabaseOperationResult:
        """Delete a node from the database (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement delete_node")
    
    def query_nodes(self, filters: List[Union[QueryFilter, Tuple[str, str, Any]]], 
                   options: Optional[QueryOptions] = None) -> DatabaseOperationResult:
        """Query nodes with filters and options (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement query_nodes")
    
    def _create_operation_result(self, operation_type: OperationType, success: bool,
                               data: Any, execution_time: float, 
                               error_message: Optional[str] = None,
                               rows_affected: int = 0) -> DatabaseOperationResult:
        """Create a standardized operation result"""
        result = DatabaseOperationResult(
            operation_type=operation_type,
            success=success,
            data=data,
            execution_time=execution_time,
            timestamp=datetime.now(),
            metadata={
                "database_type": self.database_type.value,
                "rows_affected": rows_affected
            },
            error_message=error_message,
            rows_affected=rows_affected
        )
        
        # Track operation history
        self.operation_history.append(result)
        
        # Limit history size
        if len(self.operation_history) > 1000:
            self.operation_history = self.operation_history[-500:]
        
        return result
    
    def _normalize_filters(self, filters: List[Union[QueryFilter, Tuple[str, str, Any]]]) -> List[QueryFilter]:
        """Normalize filter inputs to QueryFilter objects"""
        normalized_filters = []
        
        for filter_item in filters:
            if isinstance(filter_item, QueryFilter):
                normalized_filters.append(filter_item)
            elif isinstance(filter_item, tuple) and len(filter_item) >= 3:
                # Convert tuple to QueryFilter
                field, operator, value = filter_item[0], filter_item[1], filter_item[2]
                logical_op = filter_item[3] if len(filter_item) > 3 else "AND"
                
                normalized_filters.append(QueryFilter(
                    field=field,
                    operator=operator,
                    value=value,
                    logical_operator=logical_op
                ))
            else:
                raise ValueError(f"Invalid filter format: {filter_item}")
        
        return normalized_filters
    
    def _build_where_clause(self, filters: List[QueryFilter]) -> Tuple[str, List[Any]]:
        """Build SQL WHERE clause from filters"""
        if not filters:
            return "", []
        
        where_parts = []
        params = []
        
        for i, filter_obj in enumerate(filters):
            if i > 0:
                where_parts.append(filter_obj.logical_operator)
            
            # Handle different operators
            if filter_obj.operator in ["=", "!=", ">", "<", ">=", "<="]:
                where_parts.append(f"{filter_obj.field} {filter_obj.operator} ?")
                params.append(filter_obj.value)
            elif filter_obj.operator.upper() == "LIKE":
                where_parts.append(f"{filter_obj.field} LIKE ?")
                params.append(filter_obj.value)
            elif filter_obj.operator.upper() == "IN":
                if isinstance(filter_obj.value, (list, tuple)):
                    placeholders = ",".join(["?" for _ in filter_obj.value])
                    where_parts.append(f"{filter_obj.field} IN ({placeholders})")
                    params.extend(filter_obj.value)
                else:
                    where_parts.append(f"{filter_obj.field} = ?")
                    params.append(filter_obj.value)
            elif filter_obj.operator.upper() == "NOT IN":
                if isinstance(filter_obj.value, (list, tuple)):
                    placeholders = ",".join(["?" for _ in filter_obj.value])
                    where_parts.append(f"{filter_obj.field} NOT IN ({placeholders})")
                    params.extend(filter_obj.value)
                else:
                    where_parts.append(f"{filter_obj.field} != ?")
                    params.append(filter_obj.value)
        
        where_clause = "WHERE " + " ".join(where_parts) if where_parts else ""
        return where_clause, params
    
    def _build_order_clause(self, options: Optional[QueryOptions]) -> str:
        """Build SQL ORDER BY clause from options"""
        if not options or not options.order_by:
            return ""
        
        direction = options.order_direction.upper()
        if direction not in ["ASC", "DESC"]:
            direction = "ASC"
        
        return f"ORDER BY {options.order_by} {direction}"
    
    def _build_limit_clause(self, options: Optional[QueryOptions]) -> str:
        """Build SQL LIMIT/OFFSET clause from options"""
        if not options:
            return ""
        
        limit_parts = []
        
        if options.limit is not None:
            limit_parts.append(f"LIMIT {options.limit}")
        
        if options.offset is not None:
            limit_parts.append(f"OFFSET {options.offset}")
        
        return " ".join(limit_parts)
    
    def get_operation_stats(self) -> Dict[str, Any]:
        """Get statistics about database operations"""
        if not self.operation_history:
            return {
                "total_operations": 0,
                "success_rate": 0.0,
                "average_execution_time": 0.0,
                "operations_by_type": {}
            }
        
        total_ops = len(self.operation_history)
        successful_ops = len([op for op in self.operation_history if op.success])
        
        success_rate = successful_ops / total_ops if total_ops > 0 else 0.0
        
        total_time = sum(op.execution_time for op in self.operation_history)
        avg_time = total_time / total_ops if total_ops > 0 else 0.0
        
        ops_by_type = {}
        for op in self.operation_history:
            op_type = op.operation_type.value
            if op_type not in ops_by_type:
                ops_by_type[op_type] = {"count": 0, "success_count": 0}
            
            ops_by_type[op_type]["count"] += 1
            if op.success:
                ops_by_type[op_type]["success_count"] += 1
        
        return {
            "total_operations": total_ops,
            "success_rate": success_rate,
            "average_execution_time": avg_time,
            "operations_by_type": ops_by_type
        }
