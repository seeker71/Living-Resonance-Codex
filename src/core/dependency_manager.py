#!/usr/bin/env python3
"""
Dependency Manager - Ensures External Dependencies are Available and Functional

This module manages all external dependencies required by the Living Codex system,
ensuring they are properly installed, up-to-date, and functional before startup.
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

class DependencyManager:
    """
    Manages external dependencies for the Living Codex system
    """
    
    def __init__(self):
        self.dependencies = self._get_required_dependencies()
        self.status_cache: Dict[str, DependencyStatus] = {}
        
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
            
            # Development and testing
            DependencyInfo(
                name="pytest",
                min_version="6.0.0",
                description="Testing framework",
                test_import="pytest",
                pip_package="pytest>=6.0.0"
            ),
            
            # Code parsing and analysis
            DependencyInfo(
                name="tree-sitter",
                min_version="0.20.0",
                description="Parser generator for code analysis",
                test_import="tree_sitter",
                pip_package="tree-sitter>=0.20.0"
            ),
            
            # Graph and network
            DependencyInfo(
                name="networkx",
                min_version="2.6.0",
                description="Graph theory and network analysis",
                test_import="networkx",
                pip_package="networkx>=2.6.0"
            ),
            
            # Visualization
            DependencyInfo(
                name="matplotlib",
                min_version="3.4.0",
                description="Plotting and visualization",
                test_import="matplotlib",
                pip_package="matplotlib>=3.4.0"
            ),
            
            # Configuration and environment
            DependencyInfo(
                name="python-dotenv",
                min_version="0.19.0",
                description="Environment variable management",
                test_import="dotenv",
                pip_package="python-dotenv>=0.19.0"
            ),
            
            # Async and concurrency
            DependencyInfo(
                name="asyncio",
                min_version="3.7.0",
                description="Asynchronous I/O (built-in Python)",
                test_import="asyncio",
                required=True
            ),
            
            # Security and cryptography
            DependencyInfo(
                name="cryptography",
                min_version="3.4.0",
                description="Cryptographic recipes and primitives",
                test_import="cryptography",
                pip_package="cryptography>=3.4.0"
            ),
            
            # Logging and monitoring
            DependencyInfo(
                name="loguru",
                min_version="0.6.0",
                description="Advanced logging library",
                test_import="loguru",
                pip_package="loguru>=0.6.0"
            )
        ]
    
    def check_dependency(self, dep: DependencyInfo) -> DependencyStatus:
        """Check the status of a single dependency"""
        try:
            # Check if package is importable
            module = importlib.import_module(dep.test_import)
            
            # Get version information
            version = self._get_package_version(dep.name, module)
            
            # Check version requirements
            meets_requirements = self._check_version_requirements(
                version, dep.min_version, dep.max_version
            )
            
            # Test functionality
            functional = self._test_dependency_functionality(dep, module)
            
            return DependencyStatus(
                name=dep.name,
                installed=True,
                version=version,
                meets_requirements=meets_requirements,
                functional=functional,
                install_method="pip" if dep.pip_package else "built-in"
            )
            
        except ImportError as e:
            return DependencyStatus(
                name=dep.name,
                installed=False,
                error_message=str(e),
                install_method="pip" if dep.pip_package else "system"
            )
        except Exception as e:
            return DependencyStatus(
                name=dep.name,
                installed=True,
                error_message=str(e),
                functional=False
            )
    
    def _get_package_version(self, name: str, module: Any) -> Optional[str]:
        """Get the version of an imported package"""
        try:
            # Try common version attributes
            if hasattr(module, '__version__'):
                return module.__version__
            elif hasattr(module, 'version'):
                return module.version
            elif hasattr(module, 'VERSION'):
                return module.VERSION
            
            # Try pkg_resources for pip-installed packages
            try:
                return pkg_resources.get_distribution(name).version
            except:
                pass
            
            # For built-in modules, try to get Python version
            if name in ['sqlite3', 'asyncio']:
                return sys.version.split()[0]
            
            return "unknown"
            
        except Exception:
            return "unknown"
    
    def _check_version_requirements(self, version: str, min_version: str, max_version: Optional[str] = None) -> bool:
        """Check if version meets requirements"""
        try:
            from packaging import version as pkg_version
            
            current = pkg_version.parse(version)
            min_ver = pkg_version.parse(min_version)
            
            if not current >= min_ver:
                return False
            
            if max_version:
                max_ver = pkg_version.parse(max_version)
                if not current <= max_ver:
                    return False
            
            return True
            
        except ImportError:
            # Fallback to string comparison if packaging not available
            try:
                return version >= min_version
            except:
                return False
    
    def _test_dependency_functionality(self, dep: DependencyInfo, module: Any) -> bool:
        """Test if a dependency is functionally working"""
        try:
            if dep.name == "flask":
                # Test Flask app creation
                app = module.Flask("test_app")
                return hasattr(app, 'route')
            
            elif dep.name == "numpy":
                # Test numpy array creation
                arr = module.array([1, 2, 3])
                return len(arr) == 3
            
            elif dep.name == "pandas":
                # Test pandas DataFrame creation
                df = module.DataFrame({'test': [1, 2, 3]})
                return len(df) == 3
            
            elif dep.name == "requests":
                # Test requests session creation
                session = module.Session()
                return hasattr(session, 'get')
            
            elif dep.name == "sqlite3":
                # Test SQLite connection
                conn = module.connect(':memory:')
                conn.close()
                return True
            
            elif dep.name == "asyncio":
                # Test asyncio event loop
                loop = module.new_event_loop()
                loop.close()
                return True
            
            # Default test - just check if module has some attributes
            return hasattr(module, '__name__')
            
        except Exception:
            return False
    
    def check_all_dependencies(self) -> Dict[str, DependencyStatus]:
        """Check the status of all dependencies"""
        print("🔍 Checking external dependencies...")
        
        for dep in self.dependencies:
            status = self.check_dependency(dep)
            self.status_cache[dep.name] = status
            
            # Display status
            if status.installed and status.meets_requirements and status.functional:
                print(f"✅ {dep.name} {status.version} - {dep.description}")
            elif status.installed and not status.meets_requirements:
                print(f"⚠️ {dep.name} {status.version} - Version mismatch (need {dep.min_version}+)")
            elif status.installed and not status.functional:
                print(f"❌ {dep.name} {status.version} - Not functional: {status.error_message}")
            else:
                print(f"❌ {dep.name} - Not installed: {status.error_message}")
        
        return self.status_cache
    
    def install_missing_dependencies(self) -> bool:
        """Install missing or outdated dependencies"""
        print("\n🔧 Installing missing dependencies...")
        
        success_count = 0
        total_count = 0
        
        for dep in self.dependencies:
            if not dep.required:
                continue
                
            status = self.status_cache.get(dep.name)
            if not status or not status.installed or not status.meets_requirements or not status.functional:
                total_count += 1
                
                if self._install_dependency(dep):
                    success_count += 1
                    # Recheck the dependency
                    new_status = self.check_dependency(dep)
                    self.status_cache[dep.name] = new_status
                    
                    if new_status.functional:
                        print(f"✅ {dep.name} installed and functional")
                    else:
                        print(f"⚠️ {dep.name} installed but not functional")
                else:
                    print(f"❌ Failed to install {dep.name}")
        
        print(f"\n📊 Installation Summary: {success_count}/{total_count} dependencies installed")
        return success_count == total_count
    
    def _install_dependency(self, dep: DependencyInfo) -> bool:
        """Install a single dependency"""
        try:
            if dep.pip_package:
                print(f"📦 Installing {dep.name} via pip...")
                result = subprocess.run([
                    sys.executable, "-m", "pip", "install", dep.pip_package
                ], capture_output=True, text=True, timeout=300)
                
                if result.returncode == 0:
                    return True
                else:
                    print(f"   Error: {result.stderr}")
                    return False
            
            elif dep.conda_package:
                print(f"📦 Installing {dep.name} via conda...")
                result = subprocess.run([
                    "conda", "install", "-y", dep.conda_package
                ], capture_output=True, text=True, timeout=300)
                
                if result.returncode == 0:
                    return True
                else:
                    print(f"   Error: {result.stderr}")
                    return False
            
            elif dep.system_package:
                print(f"📦 Installing {dep.name} via system package manager...")
                # This would need to be adapted for different systems
                print(f"   Please install {dep.system_package} manually")
                return False
            
            else:
                print(f"⚠️ No installation method specified for {dep.name}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"   Timeout installing {dep.name}")
            return False
        except Exception as e:
            print(f"   Error installing {dep.name}: {e}")
            return False
    
    def validate_system_readiness(self) -> bool:
        """Validate that the system is ready for startup"""
        print("\n🧪 Validating system readiness...")
        
        # Check all dependencies
        self.check_all_dependencies()
        
        # Install missing ones
        if not self.install_missing_dependencies():
            print("❌ Some dependencies could not be installed")
            return False
        
        # Final validation - focus on critical dependencies
        all_ready = True
        critical_deps = ['flask', 'flask-login', 'sqlite3']
        
        print(f"\n🔍 Validating critical dependencies...")
        for dep_name in critical_deps:
            status = self.status_cache.get(dep_name)
            if not status or not status.functional:
                print(f"❌ Critical dependency {dep_name} not functional")
                all_ready = False
            else:
                print(f"✅ Critical dependency {dep_name} is functional")
        
        if all_ready:
            print("✅ All critical dependencies are functional")
            print("🚀 System ready for startup!")
        else:
            print("❌ System not ready for startup")
        
        return all_ready
    
    def get_dependency_report(self) -> Dict[str, Any]:
        """Generate a comprehensive dependency report"""
        report = {
            'timestamp': time.time(),
            'python_version': sys.version,
            'dependencies': {},
            'summary': {
                'total': len(self.dependencies),
                'installed': 0,
                'functional': 0,
                'missing': 0,
                'outdated': 0
            }
        }
        
        for dep in self.dependencies:
            status = self.status_cache.get(dep.name, DependencyStatus(
                name=dep.name, installed=False, functional=False
            ))
            
            report['dependencies'][dep.name] = {
                'required': dep.required,
                'description': dep.description,
                'min_version': dep.min_version,
                'max_version': dep.max_version,
                'installed': status.installed,
                'version': status.version,
                'meets_requirements': status.meets_requirements,
                'functional': status.functional,
                'error_message': status.error_message,
                'install_method': status.install_method
            }
            
            if status.installed:
                report['summary']['installed'] += 1
                if status.functional:
                    report['summary']['functional'] += 1
                if not status.meets_requirements:
                    report['summary']['outdated'] += 1
            else:
                report['summary']['missing'] += 1
        
        return report

def main():
    """Main function for testing dependency management"""
    print("🔍 Living Codex Dependency Manager")
    print("=" * 40)
    
    manager = DependencyManager()
    
    # Check and install dependencies
    if manager.validate_system_readiness():
        print("\n🎉 All dependencies are ready!")
        
        # Generate report
        report = manager.get_dependency_report()
        print(f"\n📊 Dependency Report:")
        print(f"   Total: {report['summary']['total']}")
        print(f"   Installed: {report['summary']['installed']}")
        print(f"   Functional: {report['summary']['functional']}")
        print(f"   Missing: {report['summary']['missing']}")
        print(f"   Outdated: {report['summary']['outdated']}")
    else:
        print("\n❌ System dependencies not ready")
        sys.exit(1)

if __name__ == "__main__":
    main()
