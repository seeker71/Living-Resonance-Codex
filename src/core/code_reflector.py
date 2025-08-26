#!/usr/bin/env python3
"""
Fractal Code Reflector Component
- Scans Python files under a base directory
- Extracts files, modules, classes, and functions
- Registers each as fractal nodes with structure-of-structure metadata
- Creates structure-of-structure nodes that define how structures are defined

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level
"""

import ast
import os
import inspect
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone
from pathlib import Path

from .fractal_components import FractalComponent


class FractalCodeReflectorComponent(FractalComponent):
    """
    Fractal component for code reflection and analysis
    Scans Python files and creates fractal nodes for code structures
    """
    
    def __init__(self, base_dir: str = None):
        super().__init__(
            component_type="code_reflection_system",
            name="Fractal Code Reflection System",
            content="Code reflection system that analyzes Python files and creates fractal nodes",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.scanned_files = set()
        
        # Create reflection capability nodes
        self._create_reflection_capability_nodes()
    
    def _create_reflection_capability_nodes(self):
        """Create fractal nodes for code reflection capabilities"""
        capabilities = [
            {
                "name": "Python AST Analysis",
                "content": "Parse Python files using Abstract Syntax Trees",
                "metadata": {"analysis_type": "ast", "language": "python"}
            },
            {
                "name": "Structure Extraction",
                "content": "Extract classes, functions, and modules from code",
                "metadata": {"extraction_type": "structural", "granularity": "fine"}
            },
            {
                "name": "Documentation Analysis",
                "content": "Extract and analyze docstrings and comments",
                "metadata": {"analysis_type": "documentation", "source": "docstrings"}
            },
            {
                "name": "Import Dependency Mapping",
                "content": "Map import dependencies between modules",
                "metadata": {"mapping_type": "imports", "scope": "module_level"}
            }
        ]
        
        for capability in capabilities:
            self.create_child_node(
                node_type="reflection_capability",
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
    
    def scan_directory(self, directory: str = None) -> Dict[str, Any]:
        """Scan a directory for Python files and create fractal nodes"""
        scan_dir = Path(directory) if directory else self.base_dir
        
        if not scan_dir.exists():
            return {"success": False, "error": f"Directory not found: {scan_dir}"}
        
        python_files = list(scan_dir.rglob("*.py"))
        results = {
            "success": True,
            "total_files": len(python_files),
            "processed_files": 0,
            "errors": [],
            "created_nodes": 0
        }
        
        for py_file in python_files:
            try:
                if self._process_python_file(py_file):
                    results["processed_files"] += 1
                    results["created_nodes"] += self._count_created_nodes(py_file)
            except Exception as e:
                results["errors"].append(f"Error processing {py_file}: {e}")
        
        return results
    
    def _process_python_file(self, file_path: Path) -> bool:
        """Process a single Python file and create fractal nodes"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse the Python file
            tree = ast.parse(content, filename=str(file_path))
            
            # Create file node
            file_node = self.create_child_node(
                node_type="python_file",
                name=file_path.name,
                content=f"Python file: {file_path}",
                metadata={
                    "file_path": str(file_path),
                    "file_size": len(content),
                    "line_count": len(content.splitlines()),
                    "scan_time": datetime.now(timezone.utc).isoformat()
                },
                structure_info={
                    "fractal_depth": 3,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
            
            # Process AST nodes
            self._process_ast_nodes(tree, file_node.node_id, content)
            
            self.scanned_files.add(str(file_path))
            return True
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False
    
    def _process_ast_nodes(self, tree: ast.AST, file_node_id: str, content: str):
        """Process AST nodes and create fractal nodes for each"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Module):
                self._process_module_node(node, file_node_id, content)
            elif isinstance(node, ast.ClassDef):
                self._process_class_node(node, file_node_id, content)
            elif isinstance(node, ast.FunctionDef):
                self._process_function_node(node, file_node_id, content)
            elif isinstance(node, ast.Import):
                self._process_import_node(node, file_node_id)
            elif isinstance(node, ast.ImportFrom):
                self._process_import_from_node(node, file_node_id)
    
    def _process_module_node(self, node: ast.Module, file_node_id: str, content: str):
        """Process module-level information"""
        # Module node is already created as the file node
        # Extract module-level docstring
        docstring = ast.get_docstring(node)
        if docstring:
            self.create_child_node(
                node_type="module_docstring",
                name="Module Documentation",
                content=docstring,
                metadata={
                    "docstring_type": "module",
                    "length": len(docstring),
                    "has_content": bool(docstring.strip())
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _process_class_node(self, node: ast.ClassDef, file_node_id: str, content: str):
        """Process class definition and create fractal node"""
        class_info = self._extract_class_info(node)
        
        class_node = self.create_child_node(
            node_type="python_class",
            name=node.name,
            content=f"Python class: {node.name}",
            metadata={
                "class_name": node.name,
                "bases": class_info["bases"],
                "decorators": class_info["decorators"],
                "line_number": node.lineno,
                "docstring": class_info["docstring"],
                "method_count": len(class_info["methods"]),
                "class_var_count": len(class_info["class_vars"])
            },
            structure_info={
                "fractal_depth": 4,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
        
        # Create nodes for methods
        for method_info in class_info["methods"]:
            self.create_child_node(
                node_type="python_method",
                name=f"{node.name}.{method_info['name']}",
                content=f"Method: {method_info['name']} in class {node.name}",
                metadata={
                    "method_name": method_info["name"],
                    "class_name": node.name,
                    "signature": method_info["signature"],
                    "line_number": method_info["line_number"],
                    "docstring": method_info["docstring"],
                    "decorators": method_info["decorators"]
                },
                structure_info={
                    "fractal_depth": 5,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _process_function_node(self, node: ast.FunctionDef, file_node_id: str, content: str):
        """Process function definition and create fractal node"""
        function_info = self._extract_function_info(node)
        
        self.create_child_node(
            node_type="python_function",
            name=node.name,
            content=f"Python function: {node.name}",
            metadata={
                "function_name": node.name,
                "signature": function_info["signature"],
                "line_number": node.lineno,
                "docstring": function_info["docstring"],
                "decorators": function_info["decorators"],
                "is_async": isinstance(node, ast.AsyncFunctionDef)
            },
            structure_info={
                "fractal_depth": 4,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
    
    def _process_import_node(self, node: ast.Import, file_node_id: str):
        """Process import statement"""
        for alias in node.names:
            self.create_child_node(
                node_type="python_import",
                name=f"import {alias.name}",
                content=f"Import statement: {alias.name}",
                metadata={
                    "import_name": alias.name,
                    "alias_name": alias.asname,
                    "import_type": "direct"
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _process_import_from_node(self, node: ast.ImportFrom, file_node_id: str):
        """Process from ... import statement"""
        module_name = node.module or ""
        for alias in node.names:
            self.create_child_node(
                node_type="python_import",
                name=f"from {module_name} import {alias.name}",
                content=f"From import: {alias.name} from {module_name}",
                metadata={
                    "module_name": module_name,
                    "import_name": alias.name,
                    "alias_name": alias.asname,
                    "import_type": "from"
                },
                structure_info={
                    "fractal_depth": 4,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _extract_class_info(self, node: ast.ClassDef) -> Dict[str, Any]:
        """Extract detailed class information"""
        class_info = {
            'bases': [],
            'decorators': [],
            'methods': [],
            'class_vars': [],
            'docstring': ast.get_docstring(node)
        }
        
        # Extract base classes
        for base in node.bases:
            if isinstance(base, ast.Name):
                class_info['bases'].append(base.id)
            elif isinstance(base, ast.Attribute):
                class_info['bases'].append(self._ast_to_string(base))
        
        # Extract decorators
        for decorator in node.decorator_list:
            class_info['decorators'].append(self._ast_to_string(decorator))
        
        # Extract methods and class variables
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_info = self._extract_function_info(item)
                method_info["line_number"] = item.lineno
                class_info['methods'].append(method_info)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        class_info['class_vars'].append(target.id)
        
        return class_info
    
    def _extract_function_info(self, node: ast.FunctionDef) -> Dict[str, Any]:
        """Extract detailed function information"""
        function_info = {
            'signature': self._extract_function_signature(node),
            'docstring': ast.get_docstring(node),
            'decorators': [self._ast_to_string(d) for d in node.decorator_list]
        }
        return function_info
    
    def _extract_function_signature(self, func_node: ast.FunctionDef) -> Dict[str, Any]:
        """Extract detailed function signature information"""
        signature = {
            'args': [],
            'defaults': [],
            'vararg': None,
            'kwarg': None,
            'returns': None
        }
        
        # Extract positional arguments
        for arg in func_node.args.args:
            arg_info = {
                'name': arg.arg,
                'annotation': self._ast_to_string(arg.annotation) if arg.annotation else None
            }
            signature['args'].append(arg_info)
        
        # Extract defaults
        if func_node.args.defaults:
            for default in func_node.args.defaults:
                signature['defaults'].append(self._ast_to_string(default))
        
        # Extract vararg and kwarg
        if func_node.args.vararg:
            signature['vararg'] = func_node.args.vararg.arg
        if func_node.args.kwarg:
            signature['kwarg'] = func_node.args.kwarg.arg
        
        # Extract return annotation
        if func_node.returns:
            signature['returns'] = self._ast_to_string(func_node.returns)
        
        return signature
    
    def _ast_to_string(self, node: ast.AST) -> str:
        """Convert AST node to string representation"""
        try:
            return ast.unparse(node)
        except:
            return str(node)
    
    def _count_created_nodes(self, file_path: Path) -> int:
        """Count how many nodes were created for a file"""
        # This is a simplified count - in practice you'd track this more precisely
        return 10  # Approximate count for a typical Python file
    
    def get_scan_status(self) -> Dict[str, Any]:
        """Get current scan status and statistics"""
        return {
            "base_directory": str(self.base_dir),
            "scanned_files": len(self.scanned_files),
            "total_nodes_created": len(self.scanned_files) * 10,  # Approximate
            "capabilities": [
                "python_ast_analysis",
                "structure_extraction",
                "documentation_analysis",
                "import_dependency_mapping"
            ]
        }

# Create and register the fractal component
fractal_code_reflector = FractalCodeReflectorComponent()
