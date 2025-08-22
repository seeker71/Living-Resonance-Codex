#!/usr/bin/env python3
"""
Code Navigation API - Living Codex
Integrates Tree-sitter code parsing with the Living Codex navigation system,
allowing users to explore code structure, syntax trees, and run queries
through the existing node exploration API.
"""

import os
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import logging

from .code_parser import CodeParser, SyntaxNode
from .database_persistence_system import DatabasePersistenceSystem, DatabaseNode, DatabaseOperationResult, QueryFilter, QueryOptions

logger = logging.getLogger(__name__)

@dataclass
class CodeFileNode:
    """Represents a parsed code file in the navigation system"""
    file_path: str
    file_name: str
    language: str
    content_hash: str
    file_size: int
    parse_time: datetime
    syntax_tree: Dict[str, Any]
    metadata: Dict[str, Any]

@dataclass
class SyntaxTreeNode:
    """Represents a syntax tree node for navigation"""
    node_id: str
    parent_id: Optional[str]
    node_type: str
    start_point: Tuple[int, int]
    end_point: Tuple[int, int]
    text: str
    children: List[str]  # List of child node IDs
    file_id: str  # Reference to the code file
    metadata: Dict[str, Any]

@dataclass
class CodeQueryResult:
    """Result of a code query operation"""
    query: str
    file_path: str
    matches: List[Dict[str, Any]]
    execution_time: float
    metadata: Dict[str, Any]

class CodeNavigationAPI:
    """API for navigating code structure through the Living Codex system"""
    
    def __init__(self, database: DatabasePersistenceSystem, code_parser: CodeParser):
        self.database = database
        self.code_parser = code_parser
        self.storage_root = Path("code_assets")
        self.storage_root.mkdir(exist_ok=True)
    
    def parse_and_store_code_file(self, file_path: str, store_syntax_tree: bool = True) -> DatabaseOperationResult:
        """Parse a code file and store it in the navigation system"""
        start_time = datetime.now()
        
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return DatabaseOperationResult(
                    operation_type="CREATE",
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=start_time,
                    metadata={"file_path": str(file_path)},
                    error_message=f"File not found: {file_path}"
                )
            
            # Read file content
            with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
                content = f.read()
            
            # Generate content hash
            content_hash = hashlib.sha256(content.encode('utf8')).hexdigest()
            
            # Parse with Tree-sitter
            tree = self.code_parser.parse(content, str(file_path))
            if not tree:
                return DatabaseOperationResult(
                    operation_type="CREATE",
                    success=False,
                    data=None,
                    execution_time=0.0,
                    timestamp=start_time,
                    metadata={"file_path": str(file_path)},
                    error_message=f"Failed to parse file: {file_path}"
                )
            
            # Create code file node
            code_file_node = CodeFileNode(
                file_path=str(file_path),
                file_name=file_path.name,
                language=self.code_parser.get_language_name(self.code_parser._detect_language(str(file_path))),
                content_hash=content_hash,
                file_size=len(content),
                parse_time=start_time,
                syntax_tree=self._tree_to_dict(tree.root_node) if store_syntax_tree else {},
                metadata={
                    "file_extension": file_path.suffix,
                    "line_count": len(content.splitlines()),
                    "character_count": len(content),
                    "parse_success": True
                }
            )
            
            # Store in database
            db_node = self._code_file_to_db_node(code_file_node)
            result = self.database.operations.create_node(db_node)
            
            if result.success and store_syntax_tree:
                # Store syntax tree nodes
                self._store_syntax_tree_nodes(tree.root_node, str(file_path), result.data.node_id)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return DatabaseOperationResult(
                operation_type="CREATE",
                success=True,
                data=code_file_node,
                execution_time=execution_time,
                timestamp=start_time,
                metadata={"file_path": str(file_path), "language": code_file_node.language}
            )
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            logger.error(f"Error parsing code file {file_path}: {e}")
            
            return DatabaseOperationResult(
                operation_type="CREATE",
                success=False,
                data=None,
                execution_time=execution_time,
                timestamp=start_time,
                metadata={"file_path": str(file_path)},
                error_message=str(e)
            )
    
    def _tree_to_dict(self, node) -> Dict[str, Any]:
        """Convert Tree-sitter node to dictionary for storage"""
        return {
            "type": node.type,
            "start_byte": node.start_byte,
            "end_byte": node.end_byte,
            "start_point": node.start_point,
            "end_point": node.end_point,
            "children": [self._tree_to_dict(child) for child in node.children]
        }
    
    def _code_file_to_db_node(self, code_file: CodeFileNode) -> DatabaseNode:
        """Convert CodeFileNode to DatabaseNode for storage"""
        # Convert to dict and handle datetime serialization
        code_file_dict = asdict(code_file)
        if code_file_dict.get('parse_time'):
            code_file_dict['parse_time'] = code_file.parse_time.isoformat()
        
        return DatabaseNode(
            node_id=f"code_file_{code_file.content_hash[:8]}",
            node_type="code_file",
            name=code_file.file_name,
            content=json.dumps(code_file_dict),
            realm="code_analysis",
            water_state="crystalline",
            energy_level=100.0,
            transformation_cost=10.0,
            metadata={
                "file_path": code_file.file_path,
                "language": code_file.language,
                "file_size": code_file.file_size,
                "parse_time": code_file.parse_time.isoformat(),
                "content_hash": code_file.content_hash
            },
            created_at=code_file.parse_time,
            updated_at=code_file.parse_time
        )
    
    def _store_syntax_tree_nodes(self, root_node, file_path: str, file_id: str):
        """Store syntax tree nodes in the database"""
        def store_node(node, parent_id: Optional[str] = None):
            node_id = f"syntax_{file_id}_{node.start_byte}_{node.end_byte}"
            
            syntax_node = SyntaxTreeNode(
                node_id=node_id,
                parent_id=parent_id,
                node_type=node.type,
                start_point=node.start_point,
                end_point=node.end_point,
                text=node.text.decode() if hasattr(node.text, 'decode') else str(node.text),
                children=[],
                file_id=file_id,
                metadata={
                    "start_byte": node.start_byte,
                    "end_byte": node.end_byte,
                    "depth": 0  # Will be calculated
                }
            )
            
            # Store the node
            db_node = DatabaseNode(
                node_id=node_id,
                node_type="syntax_node",
                name=f"syntax_{node.type}",
                content=json.dumps(asdict(syntax_node)),
                realm="code_analysis",
                water_state="crystalline",
                energy_level=50.0,
                transformation_cost=5.0,
                parent_id=parent_id,
                metadata={
                    "file_id": file_id,
                    "file_path": file_path,
                    "start_byte": node.start_byte,
                    "end_byte": node.end_byte,
                    "start_point": node.start_point,
                    "end_point": node.end_point,
                    "depth": 0  # Will be calculated
                },
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            self.database.operations.create_node(db_node)
            
            # Store children and collect their IDs
            child_ids = []
            for child in node.children:
                child_id = store_node(child, node_id)
                if child_id:
                    child_ids.append(child_id)
            
            # Update children list
            syntax_node.children = child_ids
            
            return node_id
        
        store_node(root_node)
    
    def search_code_files(self, query: str, language: Optional[str] = None) -> DatabaseOperationResult:
        """Search for code files by content or metadata"""
        try:
            filters = [QueryFilter("node_type", "=", "code_file")]
            
            if language:
                filters.append(QueryFilter("content", "LIKE", f'%"language": "{language}"%'))
            
            if query:
                filters.append(QueryFilter("content", "LIKE", f"%{query}%"))
            
            result = self.database.operations.query_nodes(filters, QueryOptions(limit=50))
            return result
            
        except Exception as e:
            logger.error(f"Error searching code files: {e}")
            return DatabaseOperationResult(
                operation_type="QUERY",
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"query": query, "language": language},
                error_message=str(e)
            )
    
    def get_code_file_structure(self, file_id: str) -> DatabaseOperationResult:
        """Get the structure of a code file including syntax tree"""
        try:
            # Get the code file node
            result = self.database.operations.read_node(file_id)
            if not result.success:
                return result
            
            # Get syntax tree nodes
            syntax_result = self.database.operations.query_nodes(
                [QueryFilter("node_type", "=", "syntax_node"), 
                 QueryFilter("metadata", "LIKE", f'%"file_id": "{file_id}"%')],
                QueryOptions()
            )
            
            if syntax_result.success:
                result.data.syntax_nodes = syntax_result.data
            else:
                result.data.syntax_nodes = []
            
            return result
            
        except Exception as e:
            logger.error(f"Error getting code file structure: {e}")
            return DatabaseOperationResult(
                operation_type="READ",
                success=False,
                data=None,
                execution_time=0.0,
                timestamp=datetime.now(),
                metadata={"file_id": file_id},
                error_message=str(e)
            )
    
    def query_code_structure(self, file_path: str, query: str, language_hint: Optional[str] = None) -> CodeQueryResult:
        """Run a Tree-sitter query on a code file"""
        start_time = datetime.now()
        
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
                content = f.read()
            
            # Run the query
            matches = self.code_parser.query(content, query, file_path, language_hint)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return CodeQueryResult(
                query=query,
                file_path=file_path,
                matches=matches,
                execution_time=execution_time,
                metadata={
                    "language": self.code_parser.get_language_name(self.code_parser._detect_language(file_path)),
                    "match_count": len(matches)
                }
            )
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            logger.error(f"Error querying code structure: {e}")
            
            return CodeQueryResult(
                query=query,
                file_path=file_path,
                matches=[],
                execution_time=execution_time,
                metadata={"error": str(e)}
            )
    
    def get_available_languages(self) -> List[str]:
        """Get list of available programming languages"""
        return self.code_parser.get_available_languages()
    
    def get_code_file_stats(self) -> Dict[str, Any]:
        """Get statistics about stored code files"""
        try:
            # Count code files
            code_files_result = self.database.operations.query_nodes(
                [QueryFilter("node_type", "=", "code_file")],
                QueryOptions()
            )
            
            # Count syntax nodes
            syntax_nodes_result = self.database.operations.query_nodes(
                [QueryFilter("node_type", "=", "syntax_node")],
                QueryOptions()
            )
            
            stats = {
                "total_code_files": len(code_files_result.data) if code_files_result.success else 0,
                "total_syntax_nodes": len(syntax_nodes_result.data) if syntax_nodes_result.success else 0,
                "available_languages": self.get_available_languages(),
                "storage_root": str(self.storage_root)
            }
            
            # Language breakdown
            if code_files_result.success:
                language_counts = {}
                for node in code_files_result.data:
                    content = node.content
                    if isinstance(content, dict) and 'language' in content:
                        lang = content['language']
                        language_counts[lang] = language_counts.get(lang, 0) + 1
                stats["language_breakdown"] = language_counts
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting code file stats: {e}")
            return {"error": str(e)}
