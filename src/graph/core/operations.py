"""
Graph Core Operations
Base graph operations and query functionality
"""

import time
import logging
from typing import List, Dict, Any, Optional, Union
from datetime import datetime
from .models import (
    GraphNode, GraphRelationship, GraphQueryResult,
    GraphOperationType, GraphNodeType
)

logger = logging.getLogger(__name__)

class GraphOperations:
    """Base class for graph operations"""
    
    def __init__(self):
        self.operation_history = []
    
    def create_node(self, node: GraphNode) -> GraphQueryResult:
        """Create a new node in the graph (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement create_node")
    
    def update_node(self, node: GraphNode) -> GraphQueryResult:
        """Update an existing node (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement update_node")
    
    def delete_node(self, node_id: str) -> GraphQueryResult:
        """Delete a node from the graph (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement delete_node")
    
    def create_relationship(self, relationship: GraphRelationship) -> GraphQueryResult:
        """Create a relationship between nodes (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement create_relationship")
    
    def delete_relationship(self, relationship_id: str) -> GraphQueryResult:
        """Delete a relationship (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement delete_relationship")
    
    def query_graph(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> GraphQueryResult:
        """Execute a graph query (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement query_graph")
    
    def traverse_graph(self, start_node_id: str, max_depth: int = 3, 
                      relationship_types: Optional[List[str]] = None) -> GraphQueryResult:
        """Traverse the graph from a starting node (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement traverse_graph")
    
    def _create_query_result(self, operation_type: GraphOperationType, success: bool,
                           data: Any, execution_time: float, 
                           error_message: Optional[str] = None,
                           metadata: Optional[Dict[str, Any]] = None) -> GraphQueryResult:
        """Create a standardized query result"""
        result = GraphQueryResult(
            operation_type=operation_type,
            success=success,
            data=data,
            execution_time=execution_time,
            timestamp=datetime.now(),
            metadata=metadata or {},
            error_message=error_message
        )
        
        # Track operation history
        self.operation_history.append(result)
        
        # Limit history size
        if len(self.operation_history) > 1000:
            self.operation_history = self.operation_history[-500:]
        
        return result
    
    def get_operation_stats(self) -> Dict[str, Any]:
        """Get statistics about graph operations"""
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
