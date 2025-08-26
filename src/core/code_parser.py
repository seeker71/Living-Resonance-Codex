#!/usr/bin/env python3
"""
Tree-sitter based generic code parser and query API for the Living Codex.
Supports parsing many programming languages and running Tree-sitter queries
to navigate syntax nodes.

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from .fractal_components import FractalComponent

try:
    from tree_sitter import Language, Parser, Query
    TREESITTER_AVAILABLE = True
except Exception:
    TREESITTER_AVAILABLE = False


@dataclass
class SyntaxNode:
    """Lightweight representation of a syntax node."""
    type: str
    start_byte: int
    end_byte: int
    start_point: Tuple[int, int]
    end_point: Tuple[int, int]
    text: str
    children: List['SyntaxNode']


class FractalCodeParserComponent(FractalComponent):
    """
    Fractal component for Tree-sitter based code parsing
    Provides generic parsing capabilities for multiple programming languages
    """
    
    def __init__(self):
        super().__init__(
            component_type="code_parser_system",
            name="Fractal Code Parser System",
            content="Tree-sitter based code parser supporting multiple programming languages",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        # Initialize language parsers
        self.languages = {}
        self.parser = None
        
        if TREESITTER_AVAILABLE:
            self._load_languages()
            self._create_language_nodes()
            self._create_parser_capability_nodes()
        else:
            self._create_fallback_nodes()
    
    def _load_languages(self):
        """Load available language parsers."""
        language_packages = {
            'python': 'tree_sitter_python',
            'javascript': 'tree_sitter_javascript',
            'typescript': 'tree_sitter_typescript',
            'html': 'tree_sitter_html',
            'css': 'tree_sitter_css',
            'json': 'tree_sitter_json',
            'yaml': 'tree_sitter_yaml',
            'rust': 'tree_sitter_rust',
            'go': 'tree_sitter_go',
            'java': 'tree_sitter_java',
            'cpp': 'tree_sitter_cpp',
            'c': 'tree_sitter_c',
            'php': 'tree_sitter_php',
            'ruby': 'tree_sitter_ruby',
            'bash': 'tree_sitter_bash',
            'lua': 'tree_sitter_lua',
            'sql': 'tree_sitter_sql',
        }
        
        for lang_name, package_name in language_packages.items():
            try:
                package = __import__(package_name)
                if hasattr(package, 'language'):
                    # Wrap the PyCapsule in a Language object
                    from tree_sitter import Language
                    self.languages[lang_name] = Language(package.language())
            except ImportError:
                continue  # Skip unavailable languages
        
        # Initialize parser
        if self.languages:
            self.parser = Parser()
    
    def _create_language_nodes(self):
        """Create fractal nodes for each available programming language"""
        for lang_name, language_obj in self.languages.items():
            self.create_child_node(
                node_type="programming_language",
                name=f"Tree-sitter {lang_name.title()}",
                content=f"Tree-sitter parser for {lang_name} programming language",
                metadata={
                    "language": lang_name,
                    "parser_type": "tree_sitter",
                    "available": True,
                    "package_name": f"tree_sitter_{lang_name}"
                },
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _create_parser_capability_nodes(self):
        """Create fractal nodes for parser capabilities"""
        capabilities = [
            {
                "name": "Syntax Tree Generation",
                "content": "Generate abstract syntax trees from source code",
                "metadata": {"capability": "ast_generation", "complexity": "high"}
            },
            {
                "name": "Multi-Language Support",
                "content": "Parse code in multiple programming languages",
                "metadata": {"capability": "multi_language", "languages": list(self.languages.keys())}
            },
            {
                "name": "Query System",
                "content": "Query syntax trees using Tree-sitter query language",
                "metadata": {"capability": "query_system", "framework": "tree_sitter"}
            },
            {
                "name": "Error Recovery",
                "content": "Continue parsing even with syntax errors",
                "metadata": {"capability": "error_recovery", "robustness": "high"}
            }
        ]
        
        for capability in capabilities:
            self.create_child_node(
                node_type="parser_capability",
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
    
    def _create_fallback_nodes(self):
        """Create nodes when Tree-sitter is not available"""
        self.create_child_node(
            node_type="parser_status",
            name="Tree-sitter Not Available",
            content="Tree-sitter parser framework is not available",
            metadata={
                "status": "unavailable",
                "reason": "tree_sitter package not installed",
                "fallback": "basic text parsing only"
            },
            structure_info={
                "fractal_depth": 1,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
    
    def _detect_language(self, file_path: str, language_hint: Optional[str] = None):
        """Detect Tree-sitter language from file extension or hint."""
        if language_hint and language_hint in self.languages:
            return self.languages[language_hint]

        ext = os.path.splitext(file_path)[1].lower().lstrip('.')
        # Common extension fallbacks
        fallback = {
            'py': 'python',
            'js': 'javascript',
            'ts': 'typescript',
            'jsx': 'javascript',
            'tsx': 'typescript',
            'go': 'go',
            'rs': 'rust',
            'rb': 'ruby',
            'java': 'java',
            'c': 'c',
            'h': 'c',
            'cpp': 'cpp',
            'hpp': 'cpp',
            'cc': 'cpp',
            'cs': 'cpp',  # C# fallback to C++
            'php': 'php',
            'html': 'html',
            'htm': 'html',
            'css': 'css',
            'json': 'json',
            'yml': 'yaml',
            'yaml': 'yaml',
            'sql': 'sql',
            'sh': 'bash',
            'bash': 'bash',
            'zsh': 'bash',
            'lua': 'lua'
        }
        
        lang_name = fallback.get(ext, 'unknown')
        return self.languages.get(lang_name)
    
    def parse(self, code: str, file_path: str = None, language_hint: Optional[str] = None):
        """Parse code and return a syntax tree."""
        if not TREESITTER_AVAILABLE or not self.parser:
            return None
        
        language = self._detect_language(file_path or "unknown", language_hint)
        if not language:
            return None
        
        self.parser.set_language(language)
        return self.parser.parse(code.encode())
    
    def query(self, code: str, query_string: str, file_path: str = None, language_hint: Optional[str] = None):
        """Run a Tree-sitter query on code."""
        if not TREESITTER_AVAILABLE:
            return []
        
        tree = self.parse(code, file_path, language_hint)
        if not tree:
            return []
        
        language = self._detect_language(file_path or "unknown", language_hint)
        if not language:
            return []
        
        try:
            query = Query(language, query_string)
            captures = query.captures(tree.root_node)
            return [{"node": capture[0], "capture_name": capture[1]} for capture in captures]
        except Exception:
            return []
    
    def get_available_languages(self) -> List[str]:
        """Get list of available programming languages."""
        return list(self.languages.keys())
    
    def get_language_name(self, language_code: str) -> str:
        """Get human-readable language name from language code."""
        language_names = {
            'python': 'Python',
            'javascript': 'JavaScript',
            'typescript': 'TypeScript',
            'html': 'HTML',
            'css': 'CSS',
            'json': 'JSON',
            'yaml': 'YAML',
            'rust': 'Rust',
            'go': 'Go',
            'java': 'Java',
            'cpp': 'C++',
            'c': 'C',
            'php': 'PHP',
            'ruby': 'Ruby',
            'bash': 'Bash',
            'lua': 'Lua',
            'sql': 'SQL'
        }
        return language_names.get(language_code, language_code.title())
    
    def get_parser_status(self) -> Dict[str, Any]:
        """Get current parser status and capabilities."""
        return {
            "tree_sitter_available": TREESITTER_AVAILABLE,
            "available_languages": self.get_available_languages(),
            "total_languages": len(self.languages),
            "parser_initialized": self.parser is not None,
            "capabilities": [
                "syntax_tree_generation",
                "multi_language_support",
                "query_system",
                "error_recovery"
            ] if TREESITTER_AVAILABLE else ["basic_text_parsing"]
        }

# Create and register the fractal component
fractal_code_parser = FractalCodeParserComponent()


