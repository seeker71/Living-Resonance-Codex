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
    from tree_sitter import Language, Parser
    from tree_sitter_languages import get_language, get_parser
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
                "Tree-sitter not available. Install 'tree_sitter' and 'tree_sitter_languages'."
            )

    def _detect_language(self, file_path: str, language_hint: Optional[str] = None):
        """Detect Tree-sitter language from file extension or hint."""
        if language_hint:
            return get_language(language_hint)

        ext = os.path.splitext(file_path)[1].lower().lstrip('.')
        # Common extension fallbacks
        fallback = {
            'py': 'python',
            'js': 'javascript',
            'ts': 'typescript',
            'jsx': 'tsx',
            'tsx': 'tsx',
            'go': 'go',
            'rs': 'rust',
            'rb': 'ruby',
            'java': 'java',
            'c': 'c',
            'h': 'c',
            'cpp': 'cpp',
            'hpp': 'cpp',
            'cc': 'cpp',
            'cs': 'c_sharp',
            'php': 'php',
            'html': 'html',
            'css': 'css',
            'json': 'json',
            'yaml': 'yaml',
            'yml': 'yaml',
            'md': 'markdown',
            'toml': 'toml',
            'sql': 'sql',
            'sh': 'bash',
            'bash': 'bash',
            'lua': 'lua'
        }
        lang = fallback.get(ext)
        if not lang:
            # default to plaintext-like parsing using markdown or json for structure
            lang = 'markdown'
        return get_language(lang)

    def parse(self, code: str, file_path: str = '', language_hint: Optional[str] = None) -> Any:
        """Parse code and return a Tree-sitter tree."""
        language = self._detect_language(file_path, language_hint)
        parser = Parser()
        parser.set_language(language)
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
        parser.set_language(language)
        tree = parser.parse(bytes(code, 'utf8'))

        # Build query
        from tree_sitter import Query
        ts_query = Query(language, query)
        cursor = tree.walk()

        # tree-sitter queries are run on nodes using QueryCursor
        from tree_sitter import QueryCursor
        qcur = QueryCursor()
        source_bytes = bytes(code, 'utf8')

        results: List[Dict[str, Any]] = []
        for match in qcur.exec(ts_query, tree.root_node):
            captures_info = []
            for capture in match.captures:
                node = capture[0]
                name = ts_query.captures[capture[1]]
                text = source_bytes[node.start_byte:node.end_byte].decode('utf8', errors='ignore')
                captures_info.append({
                    'name': name,
                    'type': node.type,
                    'start_byte': node.start_byte,
                    'end_byte': node.end_byte,
                    'start_point': node.start_point,
                    'end_point': node.end_point,
                    'text': text,
                })
            results.append({'captures': captures_info})
        return results


def main():
    import argparse, sys
    if not TREESITTER_AVAILABLE:
        print("❌ Tree-sitter not available. Please install 'tree_sitter' and 'tree_sitter_languages'.")
        return 1

    parser = argparse.ArgumentParser(description='Tree-sitter Code Parser')
    parser.add_argument('path', help='Path to source file')
    parser.add_argument('--query', help='Tree-sitter query string', default=None)
    parser.add_argument('--lang', help='Language hint (e.g., python, javascript)', default=None)
    args = parser.parse_args()

    with open(args.path, 'r', encoding='utf8', errors='ignore') as f:
        code = f.read()

    cp = CodeParser()
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


