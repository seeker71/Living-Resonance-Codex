#!/usr/bin/env python3
"""
Code Navigation API - Living Codex

This module implements the Living Codex principle: "Everything is just nodes"
where the code navigation and structure exploration system is represented as nodes that can:

1. Navigate code structure and create navigation nodes
2. Store code files and create file nodes
3. Manage syntax trees and create tree nodes
4. Execute code queries and create query nodes
5. Provide code exploration and create exploration nodes

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Code Navigation API represents the WATER layer (Code Navigation) state in the programming language ontology.
"""

import os
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Union
from datetime import datetime
import logging

from .code_parser import CodeParser
from .database_persistence_system import DatabasePersistenceSystem
from .shared_node_system import SharedNodeSystem

logger = logging.getLogger(__name__)

class CodeNavigationNodeSystem(SharedNodeSystem):
    """
    Code Navigation System using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Code files are nodes
    - Syntax trees are nodes
    - Navigation paths are nodes
    - Query results are nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The Code Navigation API represents the WATER layer (Code Navigation) state in the programming language ontology:
    - Code navigation, structure exploration, file management
    - Syntax tree storage, node relationships, path finding
    - Query execution, result processing, exploration tracking
    - File indexing, language detection, metadata management
    """
    
    def __init__(self, database: DatabasePersistenceSystem, code_parser: CodeParser):
        super().__init__("CodeNavigationNodeSystem")
        self.database = database
        self.code_parser = code_parser
        self.storage_root = Path("code_assets")
        self.storage_root.mkdir(exist_ok=True)
        
        # Initialize the code navigation system nodes
        self._initialize_code_navigation_system_nodes()
        
        logger.info(f"✅ CodeNavigationNodeSystem initialized with {len(self.storage.get_all_nodes())} foundation nodes")
    
    def _initialize_code_navigation_system_nodes(self):
        """
        Initialize code navigation system nodes - the foundation of the code navigation system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root code navigation system node
        root_node = self.create_node(
            node_type='code_navigation_system_root',
            name='Code Navigation System Root',
            content='This is the root node of the Code Navigation System. It represents the liquid, flowing code navigation layer for all Living Codex code structure exploration and navigation operations.',
            metadata={
                'water_state': 'water',
                'fractal_layer': 2,  # Code Navigation
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 1.0,
                'epistemic_label': 'code_navigation',
                'system_principle': 'Everything is just nodes - code navigation as flow nodes',
                'meta_circular': True,
                'programming_ontology_layer': 'water_code_navigation',
                'description': 'Liquid, flowing code navigation layer for code structure exploration'
            }
        )
        
        # Create the Code File node
        code_file_node = self.create_node(
            node_type='code_file',
            name='Code File - Navigation Blueprint',
            content='Code File represents the navigation blueprint - defines how code files are stored and navigated',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'water',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.95,
                'epistemic_label': 'code_navigation',
                'programming_ontology_layer': 'water_code_navigation',
                'description': 'Navigation blueprint for code file storage and management'
            }
        )
        
        # Create the Syntax Tree node
        syntax_tree_node = self.create_node(
            node_type='syntax_tree',
            name='Syntax Tree - Structure Blueprint',
            content='Syntax Tree represents the structure blueprint - defines syntax tree navigation and relationships',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'water',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.95,
                'epistemic_label': 'code_navigation',
                'programming_ontology_layer': 'water_code_navigation',
                'description': 'Structure blueprint for syntax tree navigation and relationships'
            }
        )
        
        # Create the Navigation Path node
        navigation_path_node = self.create_node(
            node_type='navigation_path',
            name='Navigation Path - Flow Blueprint',
            content='Navigation Path represents the flow blueprint - defines navigation paths through code structure',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'water',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'code_navigation',
                'programming_ontology_layer': 'water_code_navigation',
                'description': 'Flow blueprint for navigation paths through code structure'
            }
        )
        
        # Create the Code Query node
        code_query_node = self.create_node(
            node_type='code_query',
            name='Code Query - Search Blueprint',
            content='Code Query represents the search blueprint - defines code query execution and navigation',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'water',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'code_navigation',
                'programming_ontology_layer': 'water_code_navigation',
                'description': 'Search blueprint for code query execution and navigation'
            }
        )
        
        # Create the Code Exploration node
        code_exploration_node = self.create_node(
            node_type='code_exploration',
            name='Code Exploration - Discovery Blueprint',
            content='Code Exploration represents the discovery blueprint - defines code exploration and discovery',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'water',
                'fractal_layer': 2,
                'chakra': 'heart',
                'frequency': 639,
                'color': '#32CD32',
                'planet': 'Moon',
                'consciousness_mode': 'Flow, Adaptation',
                'quantum_state': 'coherent',
                'resonance_score': 0.85,
                'epistemic_label': 'code_navigation',
                'programming_ontology_layer': 'water_code_navigation',
                'description': 'Discovery blueprint for code exploration and discovery'
            }
        )
        
        print(f"🌟 Code Navigation System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"📁 Code File: {code_file_node.name} (ID: {code_file_node.node_id})")
        print(f"🌳 Syntax Tree: {syntax_tree_node.name} (ID: {syntax_tree_node.node_id})")
        print(f"🛤️ Navigation Path: {navigation_path_node.name} (ID: {navigation_path_node.node_id})")
        print(f"🔍 Code Query: {code_query_node.name} (ID: {code_query_node.node_id})")
        print(f"🔍 Code Exploration: {code_exploration_node.name} (ID: {code_exploration_node.node_id})")
    
    def parse_and_store_code_file(self, file_path: str, store_syntax_tree: bool = True) -> Dict[str, Any]:
        """Parse a code file and store it in the navigation system - file navigation node creation"""
        start_time = datetime.now()
        
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return {
                    'operation_type': "CREATE",
                    'success': False,
                    'data': None,
                    'execution_time': 0.0,
                    'timestamp': start_time.isoformat(),
                    'metadata': {"file_path": str(file_path)},
                    'error_message': f"File not found: {file_path}"
                }
            
            # Read file content
            with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
                content = f.read()
            
            # Generate content hash
            content_hash = hashlib.sha256(content.encode('utf8')).hexdigest()
            
            # Parse with Tree-sitter
            tree = self.code_parser.parse(content, str(file_path))
            if not tree:
                return {
                    'operation_type': "CREATE",
                    'success': False,
                    'data': None,
                    'execution_time': 0.0,
                    'timestamp': start_time.isoformat(),
                    'metadata': {"file_path": str(file_path)},
                    'error_message': f"Failed to parse file: {file_path}"
                }
            
            # Create code file data
            code_file_data = {
                'file_path': str(file_path),
                'file_name': file_path.name,
                'language': self.code_parser.get_language_name(self.code_parser._detect_language(str(file_path))),
                'content_hash': content_hash,
                'file_size': len(content),
                'parse_time': start_time.isoformat(),
                'syntax_tree': self._tree_to_dict(tree.root_node) if store_syntax_tree else {},
                'metadata': {
                    "file_extension": file_path.suffix,
                    "line_count": len(content.splitlines()),
                    "character_count": len(content),
                    "parse_success": True
                }
            }
            
            # Create code file node
            self.create_node(
                node_type='code_file_instance',
                name=f"Code File: {file_path.name}",
                content=f'Code file instance: {file_path.name} - {code_file_data["language"]}',
                metadata={
                    'water_state': 'water',
                    'fractal_layer': 2,
                    'chakra': 'heart',
                    'frequency': 639,
                    'color': '#32CD32',
                    'planet': 'Moon',
                    'consciousness_mode': 'Flow, Adaptation',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'code_navigation',
                    'programming_ontology_layer': 'water_code_navigation',
                    'code_file_data': code_file_data,
                    'created_at': datetime.now().isoformat()
                }
            )
            
            if store_syntax_tree:
                # Store syntax tree nodes
                self._store_syntax_tree_nodes(tree.root_node, str(file_path), content_hash[:8])
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            return {
                'operation_type': "CREATE",
                'success': True,
                'data': code_file_data,
                'execution_time': execution_time,
                'timestamp': start_time.isoformat(),
                'metadata': {"file_path": str(file_path), "language": code_file_data["language"]}
            }
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            logger.error(f"Error parsing code file {file_path}: {e}")
            
            return {
                'operation_type': "CREATE",
                'success': False,
                'data': None,
                'execution_time': execution_time,
                'timestamp': start_time.isoformat(),
                'metadata': {"file_path": str(file_path)},
                'error_message': str(e)
            }
    
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
    
    def _store_syntax_tree_nodes(self, root_node, file_path: str, file_id: str):
        """Store syntax tree nodes in the navigation system"""
        def store_node(node, parent_id: Optional[str] = None):
            node_id = f"syntax_{file_id}_{node.start_byte}_{node.end_byte}"
            
            # Get node text
            if hasattr(node, 'text'):
                if hasattr(node.text, 'decode'):
                    text = node.text.decode()
                else:
                    text = str(node.text)
            else:
                text = ""
            
            # Create syntax tree node
            self.create_node(
                node_type='syntax_tree_instance',
                name=f"Syntax Tree: {node.type}",
                content=f'Syntax tree instance: {node.type} at {node.start_point}',
                parent_id=parent_id,
                metadata={
                    'water_state': 'water',
                    'fractal_layer': 2,
                    'chakra': 'heart',
                    'frequency': 639,
                    'color': '#32CD32',
                    'planet': 'Moon',
                    'consciousness_mode': 'Flow, Adaptation',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.85,
                    'epistemic_label': 'code_navigation',
                    'programming_ontology_layer': 'water_code_navigation',
                    'file_id': file_id,
                    'file_path': file_path,
                    'node_type': node.type,
                    'start_byte': node.start_byte,
                    'end_byte': node.end_byte,
                    'start_point': node.start_point,
                    'end_point': node.end_point,
                    'text': text,
                    'created_at': datetime.now().isoformat()
                }
            )
            
            # Store children and collect their IDs
            child_ids = []
            for child in node.children:
                child_id = store_node(child, node_id)
                if child_id:
                    child_ids.append(child_id)
            
            return node_id
        
        store_node(root_node)
    
    def search_code_files(self, query: str, language: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search for code files by content or metadata - search navigation node creation"""
        try:
            results = []
            code_file_instances = [node for node in self.nodes.values() if node.node_type == 'code_file_instance']
            
            for code_file_node in code_file_instances:
                code_file_data = code_file_node.metadata.get('code_file_data', {})
                
                # Apply filters
                if language and code_file_data.get('language') != language:
                    continue
                
                if query:
                    file_name = code_file_data.get('file_name', '').lower()
                    if query.lower() not in file_name:
                        continue
                
                results.append(code_file_data)
            
            # Create search result node
            self.create_node(
                node_type='search_result',
                name=f"Code Search Result: {len(results)} files found",
                content=f'Code search result: {len(results)} files found for query "{query}"',
                metadata={
                    'water_state': 'water',
                    'fractal_layer': 2,
                    'chakra': 'heart',
                    'frequency': 639,
                    'color': '#32CD32',
                    'planet': 'Moon',
                    'consciousness_mode': 'Flow, Adaptation',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'code_navigation',
                    'programming_ontology_layer': 'water_code_navigation',
                    'query': query,
                    'language': language,
                    'result_count': len(results),
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching code files: {e}")
            return []
    
    def get_code_file_structure(self, file_hash: str) -> Dict[str, Any]:
        """Get the structure of a code file including syntax tree - structure navigation node creation"""
        try:
            # Find the code file node
            code_file_nodes = [node for node in self.nodes.values() if node.node_type == 'code_file_instance']
            target_file = None
            
            for node in code_file_nodes:
                code_file_data = node.metadata.get('code_file_data', {})
                if code_file_data.get('content_hash', '').startswith(file_hash):
                    target_file = code_file_data
                    break
            
            if not target_file:
                return {
                    'operation_type': "READ",
                    'success': False,
                    'data': None,
                    'execution_time': 0.0,
                    'timestamp': datetime.now().isoformat(),
                    'metadata': {"file_hash": file_hash},
                    'error_message': f"File not found with hash: {file_hash}"
                }
            
            # Get syntax tree nodes
            syntax_nodes = [node for node in self.nodes.values() 
                          if node.node_type == 'syntax_tree_instance' 
                          and node.metadata.get('file_id') == file_hash[:8]]
            
            # Create structure navigation node
            self.create_node(
                node_type='structure_navigation',
                name=f"Structure Navigation: {target_file['file_name']}",
                content=f'Structure navigation: {target_file["file_name"]} with {len(syntax_nodes)} syntax nodes',
                metadata={
                    'water_state': 'water',
                    'fractal_layer': 2,
                    'chakra': 'heart',
                    'frequency': 639,
                    'color': '#32CD32',
                    'planet': 'Moon',
                    'consciousness_mode': 'Flow, Adaptation',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'code_navigation',
                    'programming_ontology_layer': 'water_code_navigation',
                    'file_hash': file_hash,
                    'file_name': target_file['file_name'],
                    'syntax_node_count': len(syntax_nodes),
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return {
                'operation_type': "READ",
                'success': True,
                'data': {
                    'code_file': target_file,
                    'syntax_nodes': syntax_nodes
                },
                'execution_time': 0.0,
                'timestamp': datetime.now().isoformat(),
                'metadata': {"file_hash": file_hash}
            }
            
        except Exception as e:
            logger.error(f"Error getting code file structure: {e}")
            return {
                'operation_type': "READ",
                'success': False,
                'data': None,
                'execution_time': 0.0,
                'timestamp': datetime.now().isoformat(),
                'metadata': {"file_hash": file_hash},
                'error_message': str(e)
            }
    
    def query_code_structure(self, file_path: str, query: str, language_hint: Optional[str] = None) -> Dict[str, Any]:
        """Run a Tree-sitter query on a code file - query navigation node creation"""
        start_time = datetime.now()
        
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
                content = f.read()
            
            # Run the query
            matches = self.code_parser.query(content, query, file_path, language_hint)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            query_result = {
                'query': query,
                'file_path': file_path,
                'matches': matches,
                'execution_time': execution_time,
                'metadata': {
                    "language": self.code_parser.get_language_name(self.code_parser._detect_language(file_path)),
                    "match_count": len(matches)
                }
            }
            
            # Create query navigation node
            self.create_node(
                node_type='query_navigation',
                name=f"Query Navigation: {file_path}",
                content=f'Query navigation: {query} on {file_path} with {len(matches)} matches',
                metadata={
                    'water_state': 'water',
                    'fractal_layer': 2,
                    'chakra': 'heart',
                    'frequency': 639,
                    'color': '#32CD32',
                    'planet': 'Moon',
                    'consciousness_mode': 'Flow, Adaptation',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'code_navigation',
                    'programming_ontology_layer': 'water_code_navigation',
                    'query_result': query_result,
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return query_result
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            logger.error(f"Error querying code structure: {e}")
            
            return {
                'query': query,
                'file_path': file_path,
                'matches': [],
                'execution_time': execution_time,
                'metadata': {"error": str(e)}
            }
    
    def get_available_languages(self) -> List[str]:
        """Get list of available programming languages"""
        return self.code_parser.get_available_languages()
    
    def get_code_file_stats(self) -> Dict[str, Any]:
        """Get statistics about stored code files - stats navigation node creation"""
        try:
            # Count different types of nodes
            code_file_instances = [node for node in self.nodes.values() if node.node_type == 'code_file_instance']
            syntax_tree_instances = [node for node in self.nodes.values() if node.node_type == 'syntax_tree_instance']
            search_results = [node for node in self.nodes.values() if node.node_type == 'search_result']
            structure_navigations = [node for node in self.nodes.values() if node.node_type == 'structure_navigation']
            query_navigations = [node for node in self.nodes.values() if node.node_type == 'query_navigation']
            
            stats = {
                "total_code_files": len(code_file_instances),
                "total_syntax_nodes": len(syntax_tree_instances),
                "search_operations": len(search_results),
                "structure_navigations": len(structure_navigations),
                "query_navigations": len(query_navigations),
                "available_languages": self.get_available_languages(),
                "storage_root": str(self.storage_root)
            }
            
            # Language breakdown
            language_counts = {}
            for node in code_file_instances:
                code_file_data = node.metadata.get('code_file_data', {})
                lang = code_file_data.get('language', 'unknown')
                language_counts[lang] = language_counts.get(lang, 0) + 1
            stats["language_breakdown"] = language_counts
            
            # Create stats navigation node
            self.create_node(
                node_type='stats_navigation',
                name=f"Stats Navigation: {stats['total_code_files']} files",
                content=f'Stats navigation: {stats["total_code_files"]} code files with {stats["total_syntax_nodes"]} syntax nodes',
                metadata={
                    'water_state': 'water',
                    'fractal_layer': 2,
                    'chakra': 'heart',
                    'frequency': 639,
                    'color': '#32CD32',
                    'planet': 'Moon',
                    'consciousness_mode': 'Flow, Adaptation',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.85,
                    'epistemic_label': 'code_navigation',
                    'programming_ontology_layer': 'water_code_navigation',
                    'stats_data': stats,
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting code file stats: {e}")
            return {"error": str(e)}
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        code_navigation_nodes = [node for node in self.nodes.values() if node.metadata.get('programming_ontology_layer') == 'water_code_navigation']
        code_file_nodes = [node for node in self.nodes.values() if node.node_type == 'code_file_instance']
        syntax_tree_nodes = [node for node in self.nodes.values() if node.node_type == 'syntax_tree_instance']
        search_nodes = [node for node in self.nodes.values() if node.node_type == 'search_result']
        structure_nodes = [node for node in self.nodes.values() if node.node_type == 'structure_navigation']
        query_nodes = [node for node in self.nodes.values() if node.node_type == 'query_navigation']
        stats_nodes = [node for node in self.nodes.values() if node.node_type == 'stats_navigation']
        
        return {
            'total_nodes': len(self.nodes),
            'code_navigation_nodes': len(code_navigation_nodes),
            'code_file_nodes': len(code_file_nodes),
            'syntax_tree_nodes': len(syntax_tree_nodes),
            'search_nodes': len(search_nodes),
            'structure_nodes': len(structure_nodes),
            'query_nodes': len(query_nodes),
            'stats_nodes': len(stats_nodes),
            'water_states': list(set(node.get_water_state() for node in self.nodes.values())),
            'chakras': list(set(node.get_chakra() for node in self.nodes.values())),
            'frequencies': list(set(node.get_frequency() for node in self.nodes.values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.nodes.values()) / max(len(self.nodes), 1),
            'system_principle': 'Everything is just nodes - code navigation as flow nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'water_code_navigation_layer'
        }

# Legacy compatibility - maintain the old interface for now
class CodeNavigationAPI(CodeNavigationNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self, database: DatabasePersistenceSystem, code_parser: CodeParser):
        super().__init__(database, code_parser)
        logger.info("🔄 CodeNavigationAPI initialized with new node-based system")
        logger.info("✨ This system now embodies Living Codex principles")
        logger.info("🌟 Everything is just nodes - code navigation as flow nodes")
        logger.info("💧 Code navigation system represents WATER (Code Navigation) state in programming language ontology")
