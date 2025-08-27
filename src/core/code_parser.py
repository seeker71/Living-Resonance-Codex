#!/usr/bin/env python3
"""
Code Parser - Living Codex

This module implements the Living Codex principle: "Everything is just nodes"
where the code parsing and analysis system is represented as nodes that can:

1. Parse code files and create syntax tree nodes
2. Analyze code structure and create analysis nodes
3. Execute Tree-sitter queries and create query result nodes
4. Provide language detection and create language nodes
5. Support code navigation and create navigation nodes

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Code Parser represents the VAPOR layer (Code Analysis) state in the programming language ontology.
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import logging

try:
    from tree_sitter import Language, Parser, Query
    TREESITTER_AVAILABLE = True
except Exception:
    TREESITTER_AVAILABLE = False

# Import the Shared Node System
from .shared_node_system import SharedNodeSystem

logger = logging.getLogger(__name__)

class CodeParserNodeSystem(SharedNodeSystem):
    """
    Code Parser System using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Language parsers are nodes
    - Syntax trees are nodes
    - Code queries are nodes
    - Analysis results are nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The Code Parser represents the VAPOR layer (Code Analysis) state in the programming language ontology:
    - Code analysis, syntax tree generation, language detection
    - Tree-sitter integration, query execution, result processing
    - Code navigation, structure analysis, pattern recognition
    - Language support, parser management, syntax highlighting
    """
    
    def __init__(self):
        super().__init__("CodeParserNodeSystem")
        
        if not TREESITTER_AVAILABLE:
            raise RuntimeError(
                "Tree-sitter not available. Install 'tree_sitter' and language-specific packages."
            )
        
        # Initialize language parsers
        self.languages = {}
        self._load_languages()
        
        # Initialize the code parser system nodes
        self._initialize_code_parser_system_nodes()
        
        logger.info(f"✅ CodeParserNodeSystem initialized with {len(self.storage.get_all_nodes())} foundation nodes")
    
    def _initialize_code_parser_system_nodes(self):
        """
        Initialize code parser system nodes - the foundation of the code analysis system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root code parser system node
        root_node = self.create_node(
            node_type='code_parser_system_root',
            name='Code Parser System Root',
            content='This is the root node of the Code Parser System. It represents the evaporated, gaseous code analysis layer for all Living Codex code parsing and analysis operations.',
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,  # Code Analysis
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 1.0,
                'epistemic_label': 'code_analysis',
                'system_principle': 'Everything is just nodes - code parsing as analysis nodes',
                'meta_circular': True,
                'programming_ontology_layer': 'vapor_code_analysis',
                'description': 'Evaporated, gaseous code analysis layer for code parsing and analysis'
            }
        )
        
        # Create the Language Parser node
        language_parser_node = self.create_node(
            node_type='language_parser',
            name='Language Parser - Analysis Blueprint',
            content='Language Parser represents the analysis blueprint - defines different programming language parsers',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.95,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'description': 'Analysis blueprint for different programming language parsers'
            }
        )
        
        # Create the Syntax Tree node
        syntax_tree_node = self.create_node(
            node_type='syntax_tree',
            name='Syntax Tree - Structure Blueprint',
            content='Syntax Tree represents the structure blueprint - defines syntax tree structure for parsed code',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.95,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'description': 'Structure blueprint for syntax tree structure and navigation'
            }
        )
        
        # Create the Code Query node
        code_query_node = self.create_node(
            node_type='code_query',
            name='Code Query - Search Blueprint',
            content='Code Query represents the search blueprint - defines Tree-sitter query execution and results',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.9,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'description': 'Search blueprint for Tree-sitter query execution and result processing'
            }
        )
        
        # Create the Code Analysis node
        code_analysis_node = self.create_node(
            node_type='code_analysis',
            name='Code Analysis - Insight Blueprint',
            content='Code Analysis represents the insight blueprint - defines code analysis and pattern recognition',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.9,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'description': 'Insight blueprint for code analysis and pattern recognition'
            }
        )
        
        # Create the Language Support node
        language_support_node = self.create_node(
            node_type='language_support',
            name='Language Support - Compatibility Blueprint',
            content='Language Support represents the compatibility blueprint - defines supported programming languages',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.85,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'description': 'Compatibility blueprint for supported programming languages and parsers'
            }
        )
        
        print(f"🌟 Code Parser System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"🔤 Language Parser: {language_parser_node.name} (ID: {language_parser_node.node_id})")
        print(f"🌳 Syntax Tree: {syntax_tree_node.name} (ID: {syntax_tree_node.node_id})")
        print(f"🔍 Code Query: {code_query_node.name} (ID: {code_query_node.node_id})")
        print(f"📊 Code Analysis: {code_analysis_node.name} (ID: {code_analysis_node.node_id})")
        print(f"🌐 Language Support: {language_support_node.name} (ID: {language_support_node.node_id})")
    
    def _load_languages(self):
        """Load available language parsers and create language nodes."""
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
                    
                    # Create language support node
                    self.create_node(
                        node_type='language_support_instance',
                        name=f"Language Support: {lang_name}",
                        content=f'Language support instance: {lang_name} - {package_name}',
                        metadata={
                            'water_state': 'vapor',
                            'fractal_layer': 4,
                            'chakra': 'throat',
                            'frequency': 852,
                            'color': '#87CEEB',
                            'planet': 'Mercury',
                            'consciousness_mode': 'Communication, Expression',
                            'quantum_state': 'superposition',
                            'resonance_score': 0.9,
                            'epistemic_label': 'code_analysis',
                            'programming_ontology_layer': 'vapor_code_analysis',
                            'language_name': lang_name,
                            'package_name': package_name,
                            'status': 'available',
                            'created_at': datetime.now().isoformat()
                        }
                    )
            except ImportError:
                # Create unavailable language node
                self.create_node(
                    node_type='language_support_instance',
                    name=f"Language Support: {lang_name}",
                    content=f'Language support instance: {lang_name} - {package_name} (unavailable)',
                    metadata={
                        'water_state': 'vapor',
                        'fractal_layer': 4,
                        'chakra': 'throat',
                        'frequency': 852,
                        'color': '#87CEEB',
                        'planet': 'Mercury',
                        'consciousness_mode': 'Communication, Expression',
                        'quantum_state': 'superposition',
                        'resonance_score': 0.5,
                        'epistemic_label': 'code_analysis',
                        'programming_ontology_layer': 'vapor_code_analysis',
                        'language_name': lang_name,
                        'package_name': package_name,
                        'status': 'unavailable',
                        'created_at': datetime.now().isoformat()
                    }
                )
                continue

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
        
        # Create parse result node
        self.create_node(
            node_type='parse_result',
            name=f"Parse Result: {file_path or 'unknown'}",
            content=f'Parse result: {file_path or "unknown"} with {len(code)} characters',
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.9,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'file_path': file_path,
                'language_hint': language_hint,
                'code_length': len(code),
                'language_detected': self.get_language_name(language),
                'parse_success': True,
                'created_at': datetime.now().isoformat()
            }
        )
        
        return tree

    def to_syntax_tree(self, code: str, file_path: str = '', language_hint: Optional[str] = None) -> Dict[str, Any]:
        """Parse and convert to a syntax tree structure for easier consumption."""
        tree = self.parse(code, file_path, language_hint)
        root = tree.root_node
        source_bytes = bytes(code, 'utf8')

        def build(node) -> Dict[str, Any]:
            text = source_bytes[node.start_byte:node.end_byte].decode('utf8', errors='ignore')
            return {
                'type': node.type,
                'start_byte': node.start_byte,
                'end_byte': node.end_byte,
                'start_point': node.start_point,
                'end_point': node.end_point,
                'text': text,
                'children': [build(child) for child in node.children]
            }

        syntax_tree = build(root)
        
        # Create syntax tree node
        self.create_node(
            node_type='syntax_tree_instance',
            name=f"Syntax Tree: {file_path or 'unknown'}",
            content=f'Syntax tree instance: {file_path or "unknown"} with root type {syntax_tree["type"]}',
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.9,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'file_path': file_path,
                'language_hint': language_hint,
                'root_type': syntax_tree['type'],
                'node_count': self._count_nodes(syntax_tree),
                'tree_structure': syntax_tree,
                'created_at': datetime.now().isoformat()
            }
        )
        
        return syntax_tree
    
    def _count_nodes(self, tree_node: Dict[str, Any]) -> int:
        """Count total nodes in syntax tree."""
        count = 1  # Count current node
        for child in tree_node.get('children', []):
            count += self._count_nodes(child)
        return count

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
        
        # Create query result node
        self.create_node(
            node_type='query_result',
            name=f"Query Result: {file_path or 'unknown'}",
            content=f'Query result: {file_path or "unknown"} with {len(results)} matches',
            metadata={
                'water_state': 'vapor',
                'fractal_layer': 4,
                'chakra': 'throat',
                'frequency': 852,
                'color': '#87CEEB',
                'planet': 'Mercury',
                'consciousness_mode': 'Communication, Expression',
                'quantum_state': 'superposition',
                'resonance_score': 0.9,
                'epistemic_label': 'code_analysis',
                'programming_ontology_layer': 'vapor_code_analysis',
                'file_path': file_path,
                'language_hint': language_hint,
                'query_string': query,
                'match_count': len(results),
                'query_results': results,
                'created_at': datetime.now().isoformat()
            }
        )
        
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
    
    def analyze_code_structure(self, code: str, file_path: str = '', language_hint: Optional[str] = None) -> Dict[str, Any]:
        """Analyze code structure and create analysis nodes."""
        try:
            syntax_tree = self.to_syntax_tree(code, file_path, language_hint)
            
            # Analyze structure
            analysis = {
                'file_path': file_path,
                'language_hint': language_hint,
                'total_nodes': self._count_nodes(syntax_tree),
                'root_type': syntax_tree['type'],
                'max_depth': self._calculate_max_depth(syntax_tree),
                'node_types': self._analyze_node_types(syntax_tree),
                'function_count': self._count_functions(syntax_tree),
                'class_count': self._count_classes(syntax_tree),
                'import_count': self._count_imports(syntax_tree),
                'comment_count': self._count_comments(syntax_tree),
                'complexity_score': self._calculate_complexity(syntax_tree)
            }
            
            # Create code analysis node
            self.create_node(
                node_type='code_analysis_instance',
                name=f"Code Analysis: {file_path or 'unknown'}",
                content=f'Code analysis instance: {file_path or "unknown"} with complexity score {analysis["complexity_score"]}',
                metadata={
                    'water_state': 'vapor',
                    'fractal_layer': 4,
                    'chakra': 'throat',
                    'frequency': 852,
                    'color': '#87CEEB',
                    'planet': 'Mercury',
                    'consciousness_mode': 'Communication, Expression',
                    'quantum_state': 'superposition',
                    'resonance_score': 0.9,
                    'epistemic_label': 'code_analysis',
                    'programming_ontology_layer': 'vapor_code_analysis',
                    'analysis_data': analysis,
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return analysis
            
        except Exception as e:
            logger.error(f"Failed to analyze code structure: {e}")
            return {}
    
    def _calculate_max_depth(self, tree_node: Dict[str, Any], current_depth: int = 0) -> int:
        """Calculate maximum depth of syntax tree."""
        max_depth = current_depth
        for child in tree_node.get('children', []):
            child_depth = self._calculate_max_depth(child, current_depth + 1)
            max_depth = max(max_depth, child_depth)
        return max_depth
    
    def _analyze_node_types(self, tree_node: Dict[str, Any]) -> Dict[str, int]:
        """Analyze distribution of node types in syntax tree."""
        node_types = {}
        
        def count_types(node):
            node_type = node['type']
            node_types[node_type] = node_types.get(node_type, 0) + 1
            for child in node.get('children', []):
                count_types(child)
        
        count_types(tree_node)
        return node_types
    
    def _count_functions(self, tree_node: Dict[str, Any]) -> int:
        """Count function definitions in syntax tree."""
        count = 0
        
        def count_functions(node):
            nonlocal count
            if node['type'] in ['function_definition', 'function_declaration', 'method_definition']:
                count += 1
            for child in node.get('children', []):
                count_functions(child)
        
        count_functions(tree_node)
        return count
    
    def _count_classes(self, tree_node: Dict[str, Any]) -> int:
        """Count class definitions in syntax tree."""
        count = 0
        
        def count_classes(node):
            nonlocal count
            if node['type'] in ['class_definition', 'class_declaration']:
                count += 1
            for child in node.get('children', []):
                count_classes(child)
        
        count_classes(tree_node)
        return count
    
    def _count_imports(self, tree_node: Dict[str, Any]) -> int:
        """Count import statements in syntax tree."""
        count = 0
        
        def count_imports(node):
            nonlocal count
            if node['type'] in ['import_statement', 'import_declaration']:
                count += 1
            for child in node.get('children', []):
                count_imports(child)
        
        count_imports(tree_node)
        return count
    
    def _count_comments(self, tree_node: Dict[str, Any]) -> int:
        """Count comment nodes in syntax tree."""
        count = 0
        
        def count_comments(node):
            nonlocal count
            if node['type'] in ['comment', 'line_comment', 'block_comment']:
                count += 1
            for child in node.get('children', []):
                count_comments(child)
        
        count_comments(tree_node)
        return count
    
    def _calculate_complexity(self, tree_node: Dict[str, Any]) -> float:
        """Calculate complexity score based on various factors."""
        try:
            total_nodes = self._count_nodes(tree_node)
            max_depth = self._calculate_max_depth(tree_node)
            function_count = self._count_functions(tree_node)
            class_count = self._count_classes(tree_node)
            
            # Simple complexity formula
            complexity = (total_nodes * 0.1) + (max_depth * 0.5) + (function_count * 2) + (class_count * 3)
            return round(complexity, 2)
        except Exception:
            return 0.0
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        code_parser_nodes = [node for node in self.storage.get_all_nodes().values() if node.metadata.get('programming_ontology_layer') == 'vapor_code_analysis']
        language_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'language_support_instance']
        parse_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'parse_result']
        syntax_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'syntax_tree_instance']
        query_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'query_result']
        analysis_nodes = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'code_analysis_instance']
        
        return {
            'total_nodes': len(self.storage.get_all_nodes()),
            'code_parser_nodes': len(code_parser_nodes),
            'language_nodes': len(language_nodes),
            'parse_nodes': len(parse_nodes),
            'syntax_nodes': len(syntax_nodes),
            'query_nodes': len(query_nodes),
            'analysis_nodes': len(analysis_nodes),
            'water_states': list(set(node.get_water_state() for node in self.storage.get_all_nodes().values())),
            'chakras': list(set(node.get_chakra() for node in self.storage.get_all_nodes().values())),
            'frequencies': list(set(node.get_frequency() for node in self.storage.get_all_nodes().values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.storage.get_all_nodes().values()) / max(len(self.storage.get_all_nodes()), 1),
            'system_principle': 'Everything is just nodes - code parsing as analysis nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'vapor_code_analysis_layer'
        }

# Legacy compatibility - maintain the old interface for now
class CodeParser(CodeParserNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self):
        super().__init__()
        logger.info("🔄 CodeParser initialized with new node-based system")
        logger.info("✨ This system now embodies Living Codex principles")
        logger.info("🌟 Everything is just nodes - code parsing as analysis nodes")
        logger.info("💨 Code parser system represents VAPOR (Code Analysis) state in programming language ontology")

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
        print(f"Root: {tree['type']}  children={len(tree['children'])}")
        
        # Show analysis
        analysis = cp.analyze_code_structure(code, file_path=args.path, language_hint=args.lang)
        print(f"\nCode Analysis:")
        print(f"  Total nodes: {analysis.get('total_nodes', 0)}")
        print(f"  Max depth: {analysis.get('max_depth', 0)}")
        print(f"  Functions: {analysis.get('function_count', 0)}")
        print(f"  Classes: {analysis.get('class_count', 0)}")
        print(f"  Complexity: {analysis.get('complexity_score', 0)}")
    
    return 0

if __name__ == '__main__':
    raise SystemExit(main())


