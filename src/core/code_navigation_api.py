#!/usr/bin/env python3
"""
Code Navigation API - Living Codex Fractal Component
Integrates Tree-sitter code parsing with the Living Codex navigation system,
allowing users to explore code structure, syntax trees, and run queries
through the existing node exploration API.

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level
"""

import os
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import logging

from .fractal_components import FractalComponent
from .code_parser import CodeParser, SyntaxNode

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

class FractalCodeNavigationComponent(FractalComponent):
    """
    Fractal component for code navigation functionality
    Integrates Tree-sitter code parsing with the Living Codex navigation system
    """
    
    def __init__(self):
        super().__init__(
            component_type="code_navigation_system",
            name="Fractal Code Navigation System",
            content="Code navigation system that integrates Tree-sitter parsing with fractal node exploration",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        # Initialize code parser
        try:
            self.code_parser = CodeParser()
            self._create_code_parser_nodes()
        except Exception as e:
            logger.warning(f"Code parser not available: {e}")
            self.code_parser = None
        
        # Create child nodes for code navigation concepts
        self._create_navigation_concept_nodes()
    
    def _create_code_parser_nodes(self):
        """Create fractal nodes for code parser capabilities"""
        if not self.code_parser:
            return
        
        # Create nodes for available languages
        for lang_name in self.code_parser.languages.keys():
            self.create_child_node(
                node_type="programming_language",
                name=f"Tree-sitter {lang_name.title()}",
                content=f"Tree-sitter parser for {lang_name} programming language",
                metadata={
                    "language": lang_name,
                    "parser_type": "tree_sitter",
                    "available": True
                },
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _create_navigation_concept_nodes(self):
        """Create fractal nodes for code navigation concepts"""
        navigation_concepts = [
            {
                "name": "Syntax Tree Navigation",
                "content": "Navigate through abstract syntax trees of parsed code",
                "metadata": {"navigation_type": "syntax_tree", "complexity": "medium"}
            },
            {
                "name": "Code Query System",
                "content": "Query code structure using Tree-sitter query language",
                "metadata": {"query_type": "tree_sitter", "flexibility": "high"}
            },
            {
                "name": "File Structure Analysis",
                "content": "Analyze and navigate file structure and relationships",
                "metadata": {"analysis_type": "structural", "depth": "file_level"}
            },
            {
                "name": "Language-Specific Parsing",
                "content": "Parse and analyze code in multiple programming languages",
                "metadata": {"multi_language": True, "parser_framework": "tree_sitter"}
            }
        ]
        
        for concept in navigation_concepts:
            self.create_child_node(
                node_type="navigation_concept",
                name=concept["name"],
                content=concept["content"],
                metadata=concept["metadata"],
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def parse_and_store_code_file(self, file_path: str, store_syntax_tree: bool = True) -> Dict[str, Any]:
        """Parse a code file and store it in the fractal system"""
        if not self.code_parser:
            return {"success": False, "error": "Code parser not available"}
        
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return {"success": False, "error": f"File not found: {file_path}"}
            
            # Read file content
            with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
                content = f.read()
            
            # Generate content hash
            content_hash = hashlib.sha256(content.encode('utf8')).hexdigest()
            
            # Parse with Tree-sitter
            tree = self.code_parser.parse(content, str(file_path))
            if not tree:
                return {"success": False, "error": f"Failed to parse file: {file_path}"}
            
            # Create fractal node for the parsed file
            file_node = self.create_child_node(
                node_type="parsed_code_file",
                name=file_path.name,
                content=f"Parsed code file: {file_path}",
                metadata={
                    "file_path": str(file_path),
                    "language": self._detect_language(file_path),
                    "content_hash": content_hash,
                    "file_size": len(content),
                    "parse_time": datetime.now().isoformat(),
                    "syntax_tree_available": store_syntax_tree
                },
                structure_info={
                    "fractal_depth": 3,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
            
            # Create syntax tree nodes if requested
            if store_syntax_tree and tree:
                self._create_syntax_tree_nodes(tree, file_node.node_id)
            
            return {
                "success": True,
                "file_node_id": file_node.node_id,
                "language": self._detect_language(file_path),
                "parse_time": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error parsing file {file_path}: {e}")
            return {"success": False, "error": str(e)}
    
    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language from file extension"""
        ext = file_path.suffix.lower()
        language_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.html': 'html',
            '.css': 'css',
            '.json': 'json',
            '.yml': 'yaml',
            '.yaml': 'yaml',
            '.rs': 'rust',
            '.go': 'go',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.php': 'php',
            '.rb': 'ruby',
            '.sh': 'bash',
            '.sql': 'sql'
        }
        return language_map.get(ext, 'unknown')
    
    def _create_syntax_tree_nodes(self, tree: Any, file_node_id: str):
        """Create fractal nodes for syntax tree structure"""
        if not tree or not hasattr(tree, 'root_node'):
            return
        
        def create_node_recursive(node, parent_id=None):
            if not node:
                return
            
            # Create fractal node for this syntax node
            syntax_node = self.create_child_node(
                node_type="syntax_node",
                name=f"{node.type}",
                content=f"Syntax node: {node.type}",
                metadata={
                    "node_type": node.type,
                    "start_point": getattr(node, 'start_point', (0, 0)),
                    "end_point": getattr(node, 'end_point', (0, 0)),
                    "text": getattr(node, 'text', ''),
                    "parent_id": parent_id,
                    "file_node_id": file_node_id
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
            
            # Recursively create child nodes
            if hasattr(node, 'children'):
                for child in node.children:
                    create_node_recursive(child, syntax_node.node_id)
        
        # Start recursive creation from root
        create_node_recursive(tree.root_node, file_node_id)
    
    def query_code_structure(self, query: str, file_path: str = None) -> Dict[str, Any]:
        """Query code structure using Tree-sitter queries"""
        if not self.code_parser:
            return {"success": False, "error": "Code parser not available"}
        
        try:
            # This would implement Tree-sitter query functionality
            # For now, return a placeholder response
            return {
                "success": True,
                "query": query,
                "results": [],
                "message": "Code query functionality to be implemented"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_available_languages(self) -> List[str]:
        """Get list of available programming languages for parsing"""
        if not self.code_parser:
            return []
        return list(self.code_parser.languages.keys())
    
    def get_parsed_files(self) -> List[Dict[str, Any]]:
        """Get list of all parsed code files"""
        # This would query the fractal system for parsed code files
        return []

# Create and register the fractal component
fractal_code_navigation = FractalCodeNavigationComponent()
