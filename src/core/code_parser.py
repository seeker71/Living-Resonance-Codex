#!/usr/bin/env python3
"""
Tree-sitter based generic code parser and query API for the Living Codex.
Supports parsing many programming languages and running Tree-sitter queries
to navigate syntax nodes.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

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


class CodeParser:
    """Generic parser over Tree-sitter with a simple query API."""

    def __init__(self):
        if not TREESITTER_AVAILABLE:
            raise RuntimeError(
                "Tree-sitter not available. Install 'tree_sitter' and language-specific packages."
            )
        
        # Initialize language parsers
        self.languages = {}
        self._load_languages()

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
            'css': 'css',
            'json': 'json',
            'yaml': 'yaml',
            'yml': 'yaml',
            'md': 'markdown',
            'toml': 'json',  # TOML fallback to JSON
            'sql': 'sql',
            'sh': 'bash',
            'bash': 'bash',
            'lua': 'lua'
        }
        
        lang = fallback.get(ext)
        if lang and lang in self.languages:
            return self.languages[lang]
        
        # Default to Python if available, otherwise first available language
        if 'python' in self.languages:
            return self.languages['python']
        elif self.languages:
            return list(self.languages.values())[0]
        else:
            raise RuntimeError("No Tree-sitter languages available")

    def parse(self, code: str, file_path: str = '', language_hint: Optional[str] = None) -> Any:
        """Parse code and return a Tree-sitter tree."""
        language = self._detect_language(file_path, language_hint)
        parser = Parser()
        parser.language = language
        tree = parser.parse(bytes(code, 'utf8'))
        return tree

    def to_syntax_tree(self, code: str, file_path: str = '', language_hint: Optional[str] = None) -> SyntaxNode:
        """Parse and convert to a SyntaxNode tree for easier consumption."""
        tree = self.parse(code, file_path, language_hint)
        root = tree.root_node
        source_bytes = bytes(code, 'utf8')

        def build(node) -> SyntaxNode:
            text = source_bytes[node.start_byte:node.end_byte].decode('utf8', errors='ignore')
            return SyntaxNode(
                type=node.type,
                start_byte=node.start_byte,
                end_byte=node.end_byte,
                start_point=node.start_point,
                end_point=node.end_point,
                text=text,
                children=[build(child) for child in node.children]
            )

        return build(root)

    def query(self, code: str, query: str, file_path: str = '', language_hint: Optional[str] = None) -> List[Dict[str, Any]]:
        """Run a Tree-sitter query against code and return captures with ranges and text."""
        language = self._detect_language(file_path, language_hint)
        parser = Parser()
        parser.language = language
        tree = parser.parse(bytes(code, 'utf8'))

        # Build query
        ts_query = Query(language, query)
        source_bytes = bytes(code, 'utf8')

        # Execute query using the matches method
        results: List[Dict[str, Any]] = []
        
        # Get matches from the root node
        matches = ts_query.matches(tree.root_node)
        
        for pattern_index, captures in matches:
            captures_info = []
            for capture_name, nodes in captures.items():
                # nodes is a list of Node objects
                for node in nodes:
                    text = source_bytes[node.start_byte:node.end_byte].decode('utf8', errors='ignore')
                    captures_info.append({
                        'name': capture_name,
                        'type': node.type,
                        'start_byte': node.start_byte,
                        'end_byte': node.end_byte,
                        'start_point': node.start_point,
                        'end_point': node.end_point,
                        'text': text,
                    })
            results.append({'captures': captures_info})
        return results

    def get_available_languages(self) -> List[str]:
        """Get list of available language parsers."""
        return list(self.languages.keys())
    
    def get_language_name(self, language_obj) -> str:
        """Get the language name from a Language object by finding the key in self.languages."""
        for name, lang_obj in self.languages.items():
            if lang_obj == language_obj:
                return name
        return "unknown"


def main():
    import argparse, sys
    if not TREESITTER_AVAILABLE:
        print("❌ Tree-sitter not available. Please install 'tree_sitter' and language-specific packages.")
        return 1

    parser = argparse.ArgumentParser(description='Tree-sitter Code Parser')
    parser.add_argument('path', help='Path to source file')
    parser.add_argument('--query', help='Tree-sitter query string', default=None)
    parser.add_argument('--lang', help='Language hint (e.g., python, javascript)', default=None)
    args = parser.parse_args()

    with open(args.path, 'r', encoding='utf8', errors='ignore') as f:
        code = f.read()

    cp = CodeParser()
    print(f"Available languages: {', '.join(cp.get_available_languages())}")
    
    if args.query:
        results = cp.query(code, args.query, file_path=args.path, language_hint=args.lang)
        for i, match in enumerate(results):
            print(f"Match {i+1}:")
            for cap in match['captures']:
                print(f"  [{cap['name']}] {cap['type']} {cap['start_point']}->{cap['end_point']}")
                snippet = cap['text'].strip().splitlines()
                if snippet:
                    print(f"    {snippet[0][:120]}")
    else:
        tree = cp.to_syntax_tree(code, file_path=args.path, language_hint=args.lang)
        print(f"Root: {tree.type}  children={len(tree.children)}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


