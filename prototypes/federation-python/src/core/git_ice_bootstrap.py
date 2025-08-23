#!/usr/bin/env python3
"""
Enhanced ICE Bootstrap System with Git Integration
Provides distributed, version-controlled bootstrap capabilities
"""

import os
import sys
import json
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import subprocess
import hashlib

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core.git_ice_storage import (
    GitICEstorage, PublicNodeRegistry, PublicNode, ICEManifest
)
from src.core.dependency_manager import DependencyManager

@dataclass
class BootstrapConfig:
    """Configuration for ICE bootstrap process"""
    ice_repository_url: str
    ice_commit_hash: str = None
    auto_update: bool = True
    validate_checksums: bool = True
    network_discovery: bool = True
    bootstrap_timeout: int = 300  # seconds

class GitICEBootstrap:
    """Enhanced ICE bootstrap system with Git integration"""
    
    def __init__(self, config: BootstrapConfig):
        self.config = config
        self.storage = GitICEstorage()
        self.node_registry = PublicNodeRegistry(self.storage)
        self.dependency_manager = DependencyManager()
        self.bootstrap_status = {}
        
    def bootstrap_system(self) -> bool:
        """Main bootstrap process with Git integration"""
        try:
            print("🚀 Starting Enhanced ICE Bootstrap with Git Integration...")
            
            # Step 1: Validate dependencies
            if not self._validate_dependencies():
                print("❌ Dependency validation failed")
                return False
            
            # Step 2: Setup Git repository
            if not self._setup_git_repository():
                print("❌ Git repository setup failed")
                return False
            
            # Step 3: Retrieve ICE core
            if not self._retrieve_ice_core():
                print("❌ ICE core retrieval failed")
                return False
            
            # Step 4: Validate system integrity
            if not self._validate_system_integrity():
                print("❌ System integrity validation failed")
                return False
            
            # Step 5: Register as public node
            if self.config.network_discovery:
                self._register_public_node()
            
            # Step 6: Initialize system components
            if not self._initialize_system_components():
                print("❌ System component initialization failed")
                return False
            
            print("✅ Enhanced ICE Bootstrap completed successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Bootstrap failed with error: {e}")
            return False
    
    def _validate_dependencies(self) -> bool:
        """Validate system dependencies"""
        print("🔍 Validating system dependencies...")
        
        # Check Git availability
        try:
            subprocess.run(['git', '--version'], capture_output=True, check=True)
            print("✅ Git is available")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Git is not available. Please install Git for enhanced bootstrap features.")
            return False
        
        # Validate Python dependencies
        validation_result = self.dependency_manager.validate_system_readiness()
        if not validation_result.is_ready:
            print(f"❌ Python dependencies not ready: {validation_result.issues}")
            return False
        
        print("✅ All dependencies validated")
        return True
    
    def _setup_git_repository(self) -> bool:
        """Setup Git repository for ICE core"""
        print("🔧 Setting up Git repository...")
        
        try:
            # Add remote origin if specified
            if self.config.ice_repository_url:
                self.storage.add_remote_origin(self.config.ice_repository_url)
                
                # Pull latest changes
                if self.config.auto_update:
                    print("📥 Pulling latest ICE core from remote...")
                    self.storage.pull_from_remote()
            
            print("✅ Git repository setup completed")
            return True
            
        except Exception as e:
            print(f"❌ Git repository setup failed: {e}")
            return False
    
    def _retrieve_ice_core(self) -> bool:
        """Retrieve ICE core from Git repository"""
        print("📦 Retrieving ICE core...")
        
        try:
            # Retrieve ICE core files
            ice_files, manifest = self.storage.retrieve_ice_core(self.config.ice_commit_hash)
            
            if not ice_files or not manifest:
                print("❌ Failed to retrieve ICE core files")
                return False
            
            # Store manifest for validation
            self.current_manifest = manifest
            self.current_ice_files = ice_files
            
            print(f"✅ Retrieved ICE core v{manifest.version} with {len(ice_files)} components")
            print(f"   Commit: {manifest.git_commit_hash}")
            print(f"   Branch: {manifest.git_branch}")
            
            return True
            
        except Exception as e:
            print(f"❌ ICE core retrieval failed: {e}")
            return False
    
    def _validate_system_integrity(self) -> bool:
        """Validate system integrity using checksums"""
        if not self.config.validate_checksums:
            print("⚠️ Skipping checksum validation")
            return True
        
        print("🔒 Validating system integrity...")
        
        try:
            for file_path, expected_checksum in self.current_manifest.validation_checksums.items():
                if file_path in self.current_ice_files:
                    content = self.current_ice_files[file_path]
                    actual_checksum = hashlib.sha256(content.encode()).hexdigest()
                    
                    if actual_checksum != expected_checksum:
                        print(f"❌ Checksum mismatch for {file_path}")
                        return False
            
            print("✅ System integrity validated")
            return True
            
        except Exception as e:
            print(f"❌ Integrity validation failed: {e}")
            return False
    
    def _register_public_node(self):
        """Register this instance as a public node"""
        print("🌐 Registering as public node...")
        
        try:
            # Get local system information
            node_info = self._get_local_node_info()
            
            # Register with the registry
            success = self.node_registry.register_node(node_info)
            
            if success:
                print(f"✅ Registered as public node: {node_info.name}")
            else:
                print("⚠️ Failed to register as public node")
                
        except Exception as e:
            print(f"⚠️ Node registration failed: {e}")
    
    def _get_local_node_info(self) -> PublicNode:
        """Get local node information for registration"""
        # Generate unique node ID
        node_id = f"node_{hash(os.uname().nodename) % 10000:04d}"
        
        return PublicNode(
            node_id=node_id,
            name=f"Living Codex Node - {os.uname().nodename}",
            description="Local Living Codex instance with enhanced bootstrap capabilities",
            location="Local",
            capabilities=['bootstrap', 'ice_storage', 'network_discovery'],
            ice_repository_url=self.config.ice_repository_url or 'local',
            ice_commit_hash=self.current_manifest.git_commit_hash,
            last_updated=datetime.now(),
            contact_info={'type': 'local', 'host': os.uname().nodename},
            network_region='local',
            status='active'
        )
    
    def _initialize_system_components(self) -> bool:
        """Initialize system components from ICE core"""
        print("⚙️ Initializing system components...")
        
        try:
            # Create temporary directory for component initialization
            with tempfile.TemporaryDirectory() as temp_dir:
                # Write ICE files to temporary directory
                for file_path, content in self.current_ice_files.items():
                    full_path = os.path.join(temp_dir, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    
                    with open(full_path, 'w') as f:
                        f.write(content)
                
                # Initialize each component
                for component_path in self.current_manifest.components:
                    if self._is_initializable_component(component_path):
                        if not self._initialize_component(temp_dir, component_path):
                            print(f"⚠️ Failed to initialize component: {component_path}")
            
            print("✅ System components initialized")
            return True
            
        except Exception as e:
            print(f"❌ Component initialization failed: {e}")
            return False
    
    def _is_initializable_component(self, component_path: str) -> bool:
        """Check if a component can be initialized"""
        # Skip non-Python files
        if not component_path.endswith('.py'):
            return False
        
        # Skip test files
        if 'test' in component_path.lower():
            return False
        
        return True
    
    def _initialize_component(self, temp_dir: str, component_path: str) -> bool:
        """Initialize a specific component"""
        try:
            # Import and initialize component
            sys.path.insert(0, temp_dir)
            
            # Get module name from path
            module_name = component_path.replace('/', '.').replace('.py', '')
            
            # Try to import the module
            __import__(module_name)
            
            print(f"   ✅ Initialized: {component_path}")
            return True
            
        except Exception as e:
            print(f"   ⚠️ Failed to initialize {component_path}: {e}")
            return False
        finally:
            # Restore original path
            if temp_dir in sys.path:
                sys.path.remove(temp_dir)
    
    def get_bootstrap_status(self) -> Dict[str, Any]:
        """Get current bootstrap status"""
        return {
            'status': 'completed' if self.bootstrap_status else 'in_progress',
            'manifest': asdict(self.current_manifest) if hasattr(self, 'current_manifest') else None,
            'components_loaded': len(self.current_ice_files) if hasattr(self, 'current_ice_files') else 0,
            'git_commit': self.current_manifest.git_commit_hash if hasattr(self, 'current_manifest') else None,
            'bootstrap_time': datetime.now().isoformat()
        }
    
    def discover_network_nodes(self, region: str = None, capabilities: List[str] = None) -> List[PublicNode]:
        """Discover network nodes"""
        return self.node_registry.discover_nodes(region, capabilities)
    
    def get_network_map(self) -> Dict[str, Any]:
        """Get network map"""
        return self.node_registry.export_network_map()
    
    def update_ice_core(self) -> bool:
        """Update ICE core from remote repository"""
        print("🔄 Updating ICE core...")
        
        try:
            self.storage.pull_from_remote()
            
            # Re-run bootstrap with updated core
            return self.bootstrap_system()
            
        except Exception as e:
            print(f"❌ ICE core update failed: {e}")
            return False

def create_bootstrap_config(
    ice_repository_url: str = None,
    auto_update: bool = True,
    network_discovery: bool = True
) -> BootstrapConfig:
    """Create bootstrap configuration"""
    return BootstrapConfig(
        ice_repository_url=ice_repository_url,
        auto_update=auto_update,
        network_discovery=network_discovery
    )

def main():
    """Main bootstrap entry point"""
    # Create configuration
    config = create_bootstrap_config(
        ice_repository_url="https://github.com/your-org/living-codex-ice.git",
        auto_update=True,
        network_discovery=True
    )
    
    # Create bootstrap instance
    bootstrap = GitICEBootstrap(config)
    
    # Run bootstrap
    success = bootstrap.bootstrap_system()
    
    if success:
        # Show status
        status = bootstrap.get_bootstrap_status()
        print("\n📊 Bootstrap Status:")
        print(json.dumps(status, indent=2, default=str))
        
        # Show network map
        if config.network_discovery:
            network_map = bootstrap.get_network_map()
            print("\n🌐 Network Map:")
            print(json.dumps(network_map, indent=2, default=str))
    else:
        print("\n❌ Bootstrap failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
