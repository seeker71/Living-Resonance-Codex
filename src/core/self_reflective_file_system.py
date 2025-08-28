#!/usr/bin/env python3
"""
Self-Reflective File System - Living Codex
==========================================

This system implements the missing self-reflection capability that the Living Codex
specification requires. It automatically:

1. Discovers all source files in the system
2. Analyzes their content and relationships
3. Registers them as living nodes
4. Creates a complete self-description of the codebase
5. Enables navigation from principles to source files

This is the core of the Living Codex's self-containment and self-analysis.
"""

import os
import sys
import hashlib
import mimetypes
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from datetime import datetime
import ast
import re

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

class SelfReflectiveFileSystem:
    """
    Self-Reflective File System that discovers and registers all source files
    as living nodes in the Living Codex
    """
    
    def __init__(self, root_path: str = None):
        """Initialize the self-reflective file system"""
        if root_path is None:
            # Default to the project root (two levels up from core)
            self.root_path = Path(__file__).parent.parent.parent
        else:
            self.root_path = Path(root_path)
        
        self.discovered_files = {}
        self.file_relationships = {}
        self.code_analysis = {}
        self.self_description = {}
        
        print(f"🌟 Self-Reflective File System initialized")
        print(f"   Root path: {self.root_path}")
        print(f"   System will discover and register all source files")
    
    def discover_all_source_files(self) -> Dict[str, Any]:
        """Discover all source files in the system"""
        print(f"\n🔍 Discovering all source files in {self.root_path}...")
        
        source_extensions = {
            '.py': 'python',
            '.md': 'markdown',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.txt': 'text',
            '.rst': 'restructured_text',
            '.html': 'html',
            '.css': 'css',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.h': 'header',
            '.hpp': 'header',
            '.sh': 'shell',
            '.bash': 'shell',
            '.zsh': 'shell',
            '.fish': 'shell',
            '.sql': 'sql',
            '.xml': 'xml',
            '.toml': 'toml',
            '.ini': 'ini',
            '.cfg': 'config',
            '.conf': 'config'
        }
        
        discovered_files = {}
        
        for file_path in self.root_path.rglob('*'):
            if file_path.is_file() and file_path.suffix in source_extensions:
                # Skip certain directories
                if any(part.startswith('.') or part in ['__pycache__', 'node_modules', '.git', 'venv', 'env'] 
                       for part in file_path.parts):
                    continue
                
                file_info = self._analyze_file(file_path, source_extensions[file_path.suffix])
                if file_info:
                    relative_path = str(file_path.relative_to(self.root_path))
                    discovered_files[relative_path] = file_info
                    print(f"   ✅ {relative_path} ({file_info['file_type']})")
        
        self.discovered_files = discovered_files
        print(f"✅ Discovered {len(discovered_files)} source files")
        
        return discovered_files
    
    def _analyze_file(self, file_path: Path, file_type: str) -> Optional[Dict[str, Any]]:
        """Analyze a single file and extract metadata"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Basic file info
            file_info = {
                'file_path': str(file_path),
                'file_name': file_path.name,
                'file_type': file_type,
                'file_size': len(content),
                'file_size_bytes': file_path.stat().st_size,
                'last_modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                'content_hash': hashlib.sha256(content.encode()).hexdigest(),
                'content_preview': content[:500] + "..." if len(content) > 500 else content,
                'line_count': len(content.splitlines()),
                'character_count': len(content),
                'word_count': len(content.split())
            }
            
            # Language-specific analysis
            if file_type == 'python':
                file_info.update(self._analyze_python_file(content, file_path))
            elif file_type == 'markdown':
                file_info.update(self._analyze_markdown_file(content, file_path))
            elif file_type == 'json':
                file_info.update(self._analyze_json_file(content, file_path))
            
            # Extract imports and dependencies
            file_info['imports'] = self._extract_imports(content, file_type)
            file_info['dependencies'] = self._extract_dependencies(content, file_type)
            
            # Extract key concepts and principles
            file_info['key_concepts'] = self._extract_key_concepts(content, file_type)
            file_info['principles'] = self._extract_principles(content, file_type)
            
            return file_info
            
        except Exception as e:
            print(f"   ⚠️ Error analyzing {file_path}: {e}")
            return None
    
    def _analyze_python_file(self, content: str, file_path: Path) -> Dict[str, Any]:
        """Analyze Python file content"""
        analysis = {
            'python_analysis': {},
            'classes': [],
            'functions': [],
            'imports': [],
            'docstrings': []
        }
        
        try:
            tree = ast.parse(content)
            
            # Extract classes
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_info = {
                        'name': node.name,
                        'line': node.lineno,
                        'docstring': ast.get_docstring(node),
                        'methods': [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                    }
                    analysis['classes'].append(class_info)
                
                elif isinstance(node, ast.FunctionDef):
                    func_info = {
                        'name': node.name,
                        'line': node.lineno,
                        'docstring': ast.get_docstring(node),
                        'args': [arg.arg for arg in node.args.args]
                    }
                    analysis['functions'].append(func_info)
                
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        analysis['imports'].append(alias.name)
                
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ''
                    for alias in node.names:
                        analysis['imports'].append(f"{module}.{alias.name}")
            
            # Extract docstrings
            docstring_pattern = r'"""(.*?)"""'
            analysis['docstrings'] = re.findall(docstring_pattern, content, re.DOTALL)
            
        except Exception as e:
            analysis['python_analysis']['error'] = str(e)
        
        return analysis
    
    def _analyze_markdown_file(self, content: str, file_path: Path) -> Dict[str, Any]:
        """Analyze Markdown file content"""
        analysis = {
            'markdown_analysis': {},
            'headings': [],
            'links': [],
            'code_blocks': [],
            'lists': []
        }
        
        lines = content.splitlines()
        
        for line in lines:
            # Extract headings
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                heading = line.lstrip('#').strip()
                analysis['headings'].append({'level': level, 'text': heading})
            
            # Extract links
            link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
            links = re.findall(link_pattern, line)
            analysis['links'].extend([{'text': text, 'url': url} for text, url in links])
            
            # Extract code blocks
            if line.startswith('```'):
                analysis['code_blocks'].append(line)
        
        return analysis
    
    def _analyze_json_file(self, content: str, file_path: Path) -> Dict[str, Any]:
        """Analyze JSON file content"""
        analysis = {
            'json_analysis': {},
            'is_valid': False,
            'structure': {}
        }
        
        try:
            import json
            data = json.loads(content)
            analysis['is_valid'] = True
            analysis['structure'] = self._analyze_json_structure(data)
        except Exception as e:
            analysis['json_analysis']['error'] = str(e)
        
        return analysis
    
    def _analyze_json_structure(self, data: Any, max_depth: int = 3, current_depth: int = 0) -> Dict[str, Any]:
        """Recursively analyze JSON structure"""
        if current_depth >= max_depth:
            return {'type': type(data).__name__, 'truncated': True}
        
        if isinstance(data, dict):
            return {
                'type': 'dict',
                'keys': list(data.keys()),
                'key_count': len(data),
                'sample_values': {k: type(v).__name__ for k, v in list(data.items())[:5]}
            }
        elif isinstance(data, list):
            return {
                'type': 'list',
                'length': len(data),
                'sample_types': [type(item).__name__ for item in data[:5]]
            }
        else:
            return {'type': type(data).__name__, 'value': str(data)[:100]}
    
    def _extract_imports(self, content: str, file_type: str) -> List[str]:
        """Extract imports and dependencies from file content"""
        imports = []
        
        if file_type == 'python':
            # Python imports
            import_patterns = [
                r'^import\s+(\w+)',
                r'^from\s+(\w+)\s+import',
                r'^import\s+(\w+\.\w+)',
                r'^from\s+(\w+\.\w+)\s+import'
            ]
            
            for pattern in import_patterns:
                matches = re.findall(pattern, content, re.MULTILINE)
                imports.extend(matches)
        
        elif file_type == 'markdown':
            # Markdown links and references
            link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
            links = re.findall(link_pattern, content)
            imports.extend([url for _, url in links if not url.startswith('http')])
        
        return list(set(imports))  # Remove duplicates
    
    def _extract_dependencies(self, content: str, file_type: str) -> List[str]:
        """Extract dependencies from file content"""
        dependencies = []
        
        if file_type == 'python':
            # Look for requirements.txt patterns, setup.py, etc.
            req_patterns = [
                r'requirements?\.txt',
                r'setup\.py',
                r'Pipfile',
                r'pyproject\.toml'
            ]
            
            for pattern in req_patterns:
                if re.search(pattern, content):
                    dependencies.append(pattern)
        
        return dependencies
    
    def _extract_key_concepts(self, content: str, file_type: str) -> List[str]:
        """Extract key concepts from file content"""
        concepts = []
        
        # Look for capitalized terms, technical terms, etc.
        concept_patterns = [
            r'\b[A-Z][a-zA-Z]*(?:[A-Z][a-zA-Z]*)*\b',  # CamelCase
            r'\b\w+System\b',  # System names
            r'\b\w+Manager\b',  # Manager names
            r'\b\w+Controller\b',  # Controller names
            r'\b\w+Service\b',  # Service names
        ]
        
        for pattern in concept_patterns:
            matches = re.findall(pattern, content)
            concepts.extend(matches)
        
        return list(set(concepts))[:10]  # Limit to 10 concepts
    
    def _extract_principles(self, content: str, file_type: str) -> List[str]:
        """Extract principles and philosophical concepts from file content"""
        principles = []
        
        # Look for principle-related terms
        principle_patterns = [
            r'\b\w+Principle\b',
            r'\b\w+Philosophy\b',
            r'\b\w+Concept\b',
            r'\b\w+Theory\b',
            r'\b\w+Framework\b',
            r'\b\w+Architecture\b',
            r'\b\w+Pattern\b',
            r'\b\w+Design\b'
        ]
        
        for pattern in principle_patterns:
            matches = re.findall(pattern, content)
            principles.extend(matches)
        
        return list(set(principles))[:5]  # Limit to 5 principles
    
    def create_file_nodes_in_living_codex(self, universal_system) -> bool:
        """Create living nodes for all discovered files in the Living Codex"""
        print(f"\n🌟 Creating living nodes for all discovered files...")
        
        if not self.discovered_files:
            print("   ❌ No files discovered yet. Run discover_all_source_files() first.")
            return False
        
        created_nodes = []
        
        for relative_path, file_info in self.discovered_files.items():
            try:
                # Create a living node for this file
                file_concept = universal_system.represent_concept_as_living_node(
                    f"Source File: {file_info['file_name']}",
                    f"Source file: {relative_path}\n\n{file_info.get('content_preview', 'No preview available')}",
                    "source_file",
                    {
                        "file_path": relative_path,
                        "file_type": file_info['file_type'],
                        "file_size_bytes": file_info['file_size_bytes'],
                        "line_count": file_info['line_count'],
                        "character_count": file_info['character_count'],
                        "word_count": file_info['word_count'],
                        "last_modified": file_info['last_modified'],
                        "content_hash": file_info['content_hash'],
                        "imports": file_info.get('imports', []),
                        "dependencies": file_info.get('dependencies', []),
                        "key_concepts": file_info.get('key_concepts', []),
                        "principles": file_info.get('principles', []),
                        "water_state": "ws.liquid",
                        "fractal_layer": 2,
                        "chakra": "ch.throat",
                        "frequency": "freq.741",
                        "consciousness_mode": "Communication, Expression",
                        "quantum_state": "coherent",
                        "resonance_score": 0.8,
                        "epistemic_label": "engineering",
                        "system_principle": "Source file as living node",
                        "meta_circular": True
                    },
                    ["Fear↔Trust", "Protection↔Openness"]
                )
                
                created_nodes.append(file_concept)
                print(f"   ✅ Created node for {relative_path}")
                
            except Exception as e:
                print(f"   ❌ Failed to create node for {relative_path}: {e}")
        
        print(f"✅ Created {len(created_nodes)} file nodes in Living Codex")
        return True
    
    def generate_self_description(self) -> Dict[str, Any]:
        """Generate a complete self-description of the discovered codebase"""
        print(f"\n📝 Generating complete self-description...")
        
        if not self.discovered_files:
            print("   ❌ No files discovered yet.")
            return {}
        
        # Analyze file types and statistics
        file_types = {}
        total_size = 0
        total_lines = 0
        total_files = len(self.discovered_files)
        
        for file_info in self.discovered_files.values():
            file_type = file_info['file_type']
            if file_type not in file_types:
                file_types[file_type] = {'count': 0, 'size': 0, 'lines': 0}
            
            file_types[file_type]['count'] += 1
            file_types[file_type]['size'] += file_info['file_size_bytes']
            file_types[file_type]['lines'] += file_info['line_count']
            
            total_size += file_info['file_size_bytes']
            total_lines += file_info['line_count']
        
        # Generate self-description
        self_description = {
            'system_name': 'Living Codex Self-Reflective File System',
            'discovery_timestamp': datetime.now().isoformat(),
            'root_path': str(self.root_path),
            'total_files': total_files,
            'total_size_bytes': total_size,
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'total_lines': total_lines,
            'file_types': file_types,
            'file_paths': list(self.discovered_files.keys()),
            'system_analysis': {
                'self_contained': True,
                'self_reflective': True,
                'self_analyzing': True,
                'meta_circular': True
            }
        }
        
        self.self_description = self_description
        print(f"✅ Self-description generated: {total_files} files, {total_lines} lines")
        
        return self_description
    
    def get_file_by_path(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Get file information by path"""
        return self.discovered_files.get(file_path)
    
    def search_files_by_concept(self, concept: str) -> List[Dict[str, Any]]:
        """Search files by concept or principle"""
        matching_files = []
        
        for relative_path, file_info in self.discovered_files.items():
            # Check in key concepts
            if concept.lower() in [c.lower() for c in file_info.get('key_concepts', [])]:
                matching_files.append({
                    'path': relative_path,
                    'match_type': 'key_concept',
                    'file_info': file_info
                })
            
            # Check in principles
            if concept.lower() in [p.lower() for p in file_info.get('principles', [])]:
                matching_files.append({
                    'path': relative_path,
                    'match_type': 'principle',
                    'file_info': file_info
                })
            
            # Check in content
            if concept.lower() in file_info.get('content_preview', '').lower():
                matching_files.append({
                    'path': relative_path,
                    'match_type': 'content',
                    'file_info': file_info
                })
        
        return matching_files
    
    def get_file_relationships(self) -> Dict[str, List[str]]:
        """Get relationships between files based on imports and references"""
        relationships = {}
        
        for relative_path, file_info in self.discovered_files.items():
            imports = file_info.get('imports', [])
            related_files = []
            
            if isinstance(imports, list):
                for imp in imports:
                    if isinstance(imp, str):
                        # Find files that might be related to this import
                        for other_path, other_info in self.discovered_files.items():
                            if other_path != relative_path:
                                # Check if import relates to this file
                                if (imp.lower() in other_path.lower() or 
                                    imp.lower() in other_info.get('file_name', '').lower()):
                                    related_files.append(other_path)
            
            if related_files:
                relationships[relative_path] = list(set(related_files))
        
        return relationships

def main():
    """Test the self-reflective file system"""
    print("🌟 Testing Self-Reflective File System")
    print("=" * 50)
    
    # Initialize the system
    file_system = SelfReflectiveFileSystem()
    
    # Discover all files
    discovered_files = file_system.discover_all_source_files()
    
    if discovered_files:
        # Generate self-description
        self_desc = file_system.generate_self_description()
        
        print(f"\n📊 Self-Description Summary:")
        print(f"   Total files: {self_desc['total_files']}")
        print(f"   Total size: {self_desc['total_size_mb']} MB")
        print(f"   Total lines: {self_desc['total_lines']}")
        print(f"   File types: {list(self_desc['file_types'].keys())}")
        
        # Test search functionality
        print(f"\n🔍 Testing search functionality...")
        search_results = file_system.search_files_by_concept("System")
        print(f"   Files containing 'System': {len(search_results)}")
        
        for result in search_results[:3]:  # Show first 3
            print(f"     - {result['path']} ({result['match_type']})")
        
        print(f"\n✅ Self-Reflective File System test complete!")
    else:
        print(f"❌ No files discovered")

if __name__ == "__main__":
    main()
