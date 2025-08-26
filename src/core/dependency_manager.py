#!/usr/bin/env python3
"""
Fractal Dependency Manager Component - Ensures External Dependencies are Available and Functional

This module manages all external dependencies required by the Living Codex system,
ensuring they are properly installed, up-to-date, and functional before startup.

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level
"""

import subprocess
import sys
import importlib
import pkg_resources
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
import json
import time

from .fractal_components import FractalComponent

@dataclass
class DependencyInfo:
    """Information about a required dependency"""
    name: str
    min_version: str
    max_version: Optional[str] = None
    required: bool = True
    description: str = ""
    test_import: str = ""
    pip_package: Optional[str] = None
    conda_package: Optional[str] = None
    system_package: Optional[str] = None

@dataclass
class DependencyStatus:
    """Status of a dependency check"""
    name: str
    installed: bool
    version: Optional[str] = None
    meets_requirements: bool = False
    functional: bool = False
    error_message: Optional[str] = None
    install_method: Optional[str] = None

class FractalDependencyManagerComponent(FractalComponent):
    """
    Fractal component for managing external dependencies
    Ensures all required dependencies are available and functional
    """
    
    def __init__(self):
        super().__init__(
            component_type="dependency_management_system",
            name="Fractal Dependency Management System",
            content="Manages external dependencies for the Living Codex system",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        self.dependencies = self._get_required_dependencies()
        self.status_cache: Dict[str, DependencyStatus] = {}
        
        # Create dependency category nodes
        self._create_dependency_category_nodes()
        
    def _create_dependency_category_nodes(self):
        """Create fractal nodes for dependency categories"""
        categories = [
            {
                "name": "Core Python Packages",
                "content": "Essential Python packages for system operation",
                "metadata": {"category": "core", "priority": "high"}
            },
            {
                "name": "Database and Storage",
                "content": "Database and data storage dependencies",
                "metadata": {"category": "storage", "priority": "high"}
            },
            {
                "name": "Data Processing",
                "content": "Data manipulation and analysis libraries",
                "metadata": {"category": "data", "priority": "medium"}
            },
            {
                "name": "AI and Machine Learning",
                "content": "Artificial intelligence and ML libraries",
                "metadata": {"category": "ai", "priority": "medium"}
            },
            {
                "name": "Web and API",
                "content": "Web framework and API dependencies",
                "metadata": {"category": "web", "priority": "high"}
            },
            {
                "name": "Development Tools",
                "content": "Development and testing tools",
                "metadata": {"category": "dev", "priority": "low"}
            }
        ]
        
        for category in categories:
            self.create_child_node(
                node_type="dependency_category",
                name=category["name"],
                content=category["content"],
                metadata=category["metadata"],
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
        
    def _get_required_dependencies(self) -> List[DependencyInfo]:
        """Define all required external dependencies"""
        return [
            # Core Python packages
            DependencyInfo(
                name="flask",
                min_version="2.3.0",
                description="Web framework for the platform interface",
                test_import="flask",
                pip_package="Flask>=2.3.0"
            ),
            DependencyInfo(
                name="flask-login",
                min_version="0.6.0",
                description="User session management for Flask",
                test_import="flask_login",
                pip_package="Flask-Login>=0.6.0"
            ),
            
            # Database and storage
            DependencyInfo(
                name="sqlite3",
                min_version="2.6.0",
                description="SQLite database (built-in Python)",
                test_import="sqlite3",
                required=True
            ),
            
            # Data processing and utilities
            DependencyInfo(
                name="numpy",
                min_version="1.21.0",
                description="Numerical computing library",
                test_import="numpy",
                pip_package="numpy>=1.21.0"
            ),
            DependencyInfo(
                name="pandas",
                min_version="1.3.0",
                description="Data manipulation and analysis",
                test_import="pandas",
                pip_package="pandas>=1.3.0"
            ),
            
            # AI and machine learning
            DependencyInfo(
                name="scikit-learn",
                min_version="1.0.0",
                description="Machine learning library",
                test_import="sklearn",
                pip_package="scikit-learn>=1.0.0"
            ),
            
            # Web and API
            DependencyInfo(
                name="requests",
                min_version="2.25.0",
                description="HTTP library for API calls",
                test_import="requests",
                pip_package="requests>=2.25.0"
            ),
            
            # Development tools
            DependencyInfo(
                name="pytest",
                min_version="6.0.0",
                description="Testing framework",
                test_import="pytest",
                pip_package="pytest>=6.0.0",
                required=False
            )
        ]
    
    def check_dependency(self, dep: DependencyInfo) -> DependencyStatus:
        """Check the status of a specific dependency"""
        if dep.name in self.status_cache:
            return self.status_cache[dep.name]
        
        status = DependencyStatus(name=dep.name, installed=False)
        
        try:
            # Try to import the dependency
            module = importlib.import_module(dep.test_import)
            status.installed = True
            
            # Get version if available
            if hasattr(module, '__version__'):
                status.version = module.__version__
            elif hasattr(module, 'version'):
                status.version = module.version
            
            # Check version requirements
            if status.version:
                status.meets_requirements = self._check_version_requirements(
                    status.version, dep.min_version, dep.max_version
                )
            
            # Test functionality
            status.functional = self._test_dependency_functionality(dep)
            
        except ImportError:
            status.error_message = f"Module {dep.test_import} not found"
        except Exception as e:
            status.error_message = str(e)
        
        self.status_cache[dep.name] = status
        return status
    
    def _check_version_requirements(self, installed_version: str, min_version: str, 
                                  max_version: Optional[str]) -> bool:
        """Check if installed version meets requirements"""
        try:
            from packaging import version
            
            installed = version.parse(installed_version)
            min_ver = version.parse(min_version)
            
            if installed < min_ver:
                return False
            
            if max_version:
                max_ver = version.parse(max_version)
                if installed > max_ver:
                    return False
            
            return True
            
        except ImportError:
            # Fallback to string comparison if packaging not available
            return installed_version >= min_version
    
    def _test_dependency_functionality(self, dep: DependencyInfo) -> bool:
        """Test if a dependency is functionally working"""
        try:
            if dep.name == "flask":
                from flask import Flask
                app = Flask(__name__)
                return True
            elif dep.name == "numpy":
                import numpy as np
                arr = np.array([1, 2, 3])
                return len(arr) == 3
            elif dep.name == "pandas":
                import pandas as pd
                df = pd.DataFrame({'test': [1, 2, 3]})
                return len(df) == 3
            else:
                # Default test - just check if import works
                return True
        except Exception:
            return False
    
    def check_all_dependencies(self) -> Dict[str, DependencyStatus]:
        """Check all required dependencies"""
        results = {}
        
        for dep in self.dependencies:
            status = self.check_dependency(dep)
            results[dep.name] = status
            
            # Create fractal node for dependency status
            self._create_dependency_status_node(dep, status)
        
        return results
    
    def _create_dependency_status_node(self, dep: DependencyInfo, status: DependencyStatus):
        """Create fractal node for dependency status"""
        status_text = "✅ Available" if status.functional else "❌ Not Available"
        
        self.create_child_node(
            node_type="dependency_status",
            name=f"{dep.name} - {status_text}",
            content=f"Dependency: {dep.name} - {dep.description}",
            metadata={
                "dependency_name": dep.name,
                "installed": status.installed,
                "version": status.version,
                "meets_requirements": status.meets_requirements,
                "functional": status.functional,
                "error_message": status.error_message,
                "required": dep.required,
                "min_version": dep.min_version,
                "max_version": dep.max_version
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
    
    def get_system_readiness(self) -> Dict[str, Any]:
        """Get overall system readiness based on dependencies"""
        all_statuses = self.check_all_dependencies()
        
        total_deps = len(all_statuses)
        available_deps = sum(1 for s in all_statuses.values() if s.functional)
        required_deps = sum(1 for s in all_statuses.values() if s.required)
        available_required = sum(1 for s in all_statuses.values() 
                               if s.required and s.functional)
        
        readiness_score = available_required / required_deps if required_deps > 0 else 0
        
        return {
            "total_dependencies": total_deps,
            "available_dependencies": available_deps,
            "required_dependencies": required_deps,
            "available_required_dependencies": available_required,
            "readiness_score": readiness_score,
            "system_ready": readiness_score >= 0.8,  # 80% threshold
            "dependency_statuses": all_statuses
        }
    
    def install_dependency(self, dep_name: str, method: str = "pip") -> Dict[str, Any]:
        """Install a dependency using the specified method"""
        dep = next((d for d in self.dependencies if d.name == dep_name), None)
        if not dep:
            return {"success": False, "error": f"Dependency {dep_name} not found"}
        
        try:
            if method == "pip" and dep.pip_package:
                cmd = [sys.executable, "-m", "pip", "install", dep.pip_package]
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                return {"success": True, "output": result.stdout}
            elif method == "conda" and dep.conda_package:
                cmd = ["conda", "install", "-y", dep.conda_package]
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                return {"success": True, "output": result.stdout}
            else:
                return {"success": False, "error": f"Install method {method} not available for {dep_name}"}
        except subprocess.CalledProcessError as e:
            return {"success": False, "error": e.stderr}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_dependency_info(self) -> Dict[str, Any]:
        """Get comprehensive dependency information"""
        return {
            "total_dependencies": len(self.dependencies),
            "dependency_categories": [
                "Core Python Packages",
                "Database and Storage", 
                "Data Processing",
                "AI and Machine Learning",
                "Web and API",
                "Development Tools"
            ],
            "capabilities": [
                "dependency_checking",
                "version_validation",
                "functionality_testing",
                "automatic_installation",
                "system_readiness_assessment"
            ]
        }

# Create and register the fractal component
fractal_dependency_manager = FractalDependencyManagerComponent()
