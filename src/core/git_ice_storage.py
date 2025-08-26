#!/usr/bin/env python3
"""
Git-Enabled ICE Storage System
Provides distributed, version-controlled access to the Living Codex bootstrap system
"""

import os
import json
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import subprocess
import hashlib

@dataclass
class PublicNode:
    """Represents a public node in the Living Codex network"""
    node_id: str
    name: str
    description: str
    location: str
    capabilities: List[str]
    ice_repository_url: str
    ice_commit_hash: str
    last_updated: datetime
    contact_info: Dict[str, str]
    network_region: str
    status: str  # 'active', 'maintenance', 'offline'

@dataclass
class ICEManifest:
    """Manifest for ICE core system"""
    version: str
    created_at: datetime
    components: List[str]
    dependencies: Dict[str, str]
    bootstrap_script: str
    validation_checksums: Dict[str, str]
    git_commit_hash: str
    git_branch: str
    git_remote_url: str

class GitICEstorage:
    """Git-enabled ICE storage system for distributed bootstrap access"""
    
    def __init__(self, ice_repo_path: str = None):
        self.ice_repo_path = ice_repo_path or os.path.join(os.getcwd(), 'ice_core_repo')
        self.public_nodes_file = 'public_nodes.json'
        self.ice_manifest_file = 'ice_manifest.json'
        self._ensure_ice_repo()
    
    def _ensure_ice_repo(self):
        """Ensure ICE repository exists and is initialized"""
        if not os.path.exists(self.ice_repo_path):
            os.makedirs(self.ice_repo_path)
            self._init_git_repo()
        elif not os.path.exists(os.path.join(self.ice_repo_path, '.git')):
            self._init_git_repo()
    
    def _init_git_repo(self):
        """Initialize Git repository for ICE core"""
        try:
            # Initialize Git repository
            subprocess.run(['git', 'init'], cwd=self.ice_repo_path, check=True)
            
            # Create initial commit
            self._create_initial_commit()
            
            print(f"✅ Initialized Git repository at {self.ice_repo_path}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to initialize Git repository: {e}")
        except FileNotFoundError:
            print("❌ Git not found. Please install Git to enable ICE storage features.")
    
    def _create_initial_commit(self):
        """Create initial commit with README"""
        readme_content = """# Living Codex ICE Core

This repository contains the immutable core (ICE) of the Living Codex system.

## Structure
- `src/core/` - Core system components
- `src/web_platform/` - Platform modules
- `bootstrap/` - Bootstrap scripts and manifests
- `public_nodes.json` - Network discovery information

## Usage
The ICE core provides self-bootstrapping capabilities for the Living Codex ecosystem.
"""
        
        readme_path = os.path.join(self.ice_repo_path, 'README.md')
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        # Add and commit
        subprocess.run(['git', 'add', '.'], cwd=self.ice_repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial ICE core commit'], cwd=self.ice_repo_path, check=True)
    
    def store_ice_core(self, ice_files: Dict[str, str], metadata: Dict[str, Any]) -> str:
        """Store ICE core files in Git repository"""
        try:
            # Create bootstrap directory
            bootstrap_dir = os.path.join(self.ice_repo_path, 'bootstrap')
            os.makedirs(bootstrap_dir, exist_ok=True)
            
            # Store ICE files
            for file_path, content in ice_files.items():
                full_path = os.path.join(self.ice_repo_path, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                with open(full_path, 'w') as f:
                    f.write(content)
            
            # Create ICE manifest
            manifest = ICEManifest(
                version=metadata.get('version', '1.0.0'),
                created_at=datetime.now(),
                components=list(ice_files.keys()),
                dependencies=metadata.get('dependencies', {}),
                bootstrap_script=metadata.get('bootstrap_script', 'bootstrap/ice_bootstrap.py'),
                validation_checksums=self._calculate_checksums(ice_files),
                git_commit_hash=self._get_current_commit_hash(),
                git_branch=self._get_current_branch(),
                git_remote_url=metadata.get('git_remote_url', '')
            )
            
            # Save manifest
            manifest_path = os.path.join(bootstrap_dir, self.ice_manifest_file)
            with open(manifest_path, 'w') as f:
                json.dump(asdict(manifest), f, indent=2, default=str)
            
            # Git operations
            subprocess.run(['git', 'add', '.'], cwd=self.ice_repo_path, check=True)
            commit_message = f"Update ICE core v{manifest.version} - {len(ice_files)} components"
            subprocess.run(['git', 'commit', '-m', commit_message], cwd=self.ice_repo_path, check=True)
            
            commit_hash = self._get_current_commit_hash()
            print(f"✅ Stored ICE core with commit hash: {commit_hash}")
            return commit_hash
            
        except Exception as e:
            print(f"❌ Failed to store ICE core: {e}")
            return None
    
    def retrieve_ice_core(self, commit_hash: str = None) -> Tuple[Dict[str, str], ICEManifest]:
        """Retrieve ICE core files from Git repository"""
        try:
            if commit_hash:
                # Checkout specific commit
                subprocess.run(['git', 'checkout', commit_hash], cwd=self.ice_repo_path, check=True)
            else:
                # Use latest commit
                subprocess.run(['git', 'checkout', 'main'], cwd=self.ice_repo_path, check=True)
            
            # Load manifest
            manifest_path = os.path.join(self.ice_repo_path, 'bootstrap', self.ice_manifest_file)
            with open(manifest_path, 'r') as f:
                manifest_data = json.load(f)
                manifest = ICEManifest(**manifest_data)
            
            # Retrieve files
            ice_files = {}
            for component_path in manifest.components:
                full_path = os.path.join(self.ice_repo_path, component_path)
                if os.path.exists(full_path):
                    with open(full_path, 'r') as f:
                        ice_files[component_path] = f.read()
            
            print(f"✅ Retrieved ICE core from commit: {manifest.git_commit_hash}")
            return ice_files, manifest
            
        except Exception as e:
            print(f"❌ Failed to retrieve ICE core: {e}")
            return {}, None
    
    def add_remote_origin(self, remote_url: str):
        """Add remote origin for distributed access"""
        try:
            # Check if remote already exists
            result = subprocess.run(['git', 'remote', '-v'], cwd=self.ice_repo_path, 
                                 capture_output=True, text=True, check=True)
            
            if 'origin' not in result.stdout:
                subprocess.run(['git', 'remote', 'add', 'origin', remote_url], 
                             cwd=self.ice_repo_path, check=True)
                print(f"✅ Added remote origin: {remote_url}")
            else:
                print("ℹ️ Remote origin already exists")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to add remote origin: {e}")
    
    def push_to_remote(self, branch: str = 'main'):
        """Push ICE core to remote repository"""
        try:
            subprocess.run(['git', 'push', '-u', 'origin', branch], 
                         cwd=self.ice_repo_path, check=True)
            print(f"✅ Pushed ICE core to remote branch: {branch}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to push to remote: {e}")
    
    def pull_from_remote(self, branch: str = 'main'):
        """Pull latest ICE core from remote repository"""
        try:
            subprocess.run(['git', 'pull', 'origin', branch], 
                         cwd=self.ice_repo_path, check=True)
            print(f"✅ Pulled latest ICE core from remote branch: {branch}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to pull from remote: {e}")
    
    def get_commit_history(self, limit: int = 10) -> List[Dict[str, str]]:
        """Get commit history for ICE core"""
        try:
            result = subprocess.run(['git', 'log', f'--max-count={limit}', '--oneline'], 
                                 cwd=self.ice_repo_path, capture_output=True, text=True, check=True)
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = line.split(' ', 1)
                    if len(parts) == 2:
                        commits.append({
                            'hash': parts[0],
                            'message': parts[1]
                        })
            
            return commits
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to get commit history: {e}")
            return []
    
    def _calculate_checksums(self, files: Dict[str, str]) -> Dict[str, str]:
        """Calculate SHA-256 checksums for files"""
        checksums = {}
        for file_path, content in files.items():
            checksums[file_path] = hashlib.sha256(content.encode()).hexdigest()
        return checksums
    
    def _get_current_commit_hash(self) -> str:
        """Get current Git commit hash"""
        try:
            result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                                 cwd=self.ice_repo_path, capture_output=True, text=True, check=True)
            return result.stdout.strip()[:8]  # Short hash
        except:
            return 'unknown'
    
    def _get_current_branch(self) -> str:
        """Get current Git branch"""
        try:
            result = subprocess.run(['git', 'branch', '--show-current'], 
                                 cwd=self.ice_repo_path, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except:
            return 'main'

class PublicNodeRegistry:
    """Registry for public Living Codex nodes"""
    
    def __init__(self, storage: GitICEstorage):
        self.storage = storage
        self.nodes_file_path = os.path.join(storage.ice_repo_path, self.storage.public_nodes_file)
        self.public_nodes = self._load_public_nodes()
    
    def _load_public_nodes(self) -> Dict[str, PublicNode]:
        """Load public nodes from file"""
        if os.path.exists(self.nodes_file_path):
            try:
                with open(self.nodes_file_path, 'r') as f:
                    nodes_data = json.load(f)
                    return {node_id: PublicNode(**node_data) for node_id, node_data in nodes_data.items()}
            except Exception as e:
                print(f"❌ Failed to load public nodes: {e}")
        return {}
    
    def _save_public_nodes(self):
        """Save public nodes to file"""
        try:
            nodes_data = {node_id: asdict(node) for node_id, node in self.public_nodes.items()}
            with open(self.nodes_file_path, 'w') as f:
                json.dump(nodes_data, f, indent=2, default=str)
        except Exception as e:
            print(f"❌ Failed to save public nodes: {e}")
    
    def register_node(self, node: PublicNode) -> bool:
        """Register a new public node"""
        try:
            self.public_nodes[node.node_id] = node
            self._save_public_nodes()
            
            # Commit to Git
            subprocess.run(['git', 'add', self.nodes_file_path], 
                         cwd=self.storage.ice_repo_path, check=True)
            subprocess.run(['git', 'commit', '-m', f'Register public node: {node.name}'], 
                         cwd=self.storage.ice_repo_path, check=True)
            
            print(f"✅ Registered public node: {node.name}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to register node: {e}")
            return False
    
    def discover_nodes(self, region: str = None, capabilities: List[str] = None) -> List[PublicNode]:
        """Discover public nodes by region or capabilities"""
        discovered = []
        
        for node in self.public_nodes.values():
            if node.status != 'active':
                continue
                
            if region and node.network_region != region:
                continue
                
            if capabilities:
                if not any(cap in node.capabilities for cap in capabilities):
                    continue
            
            discovered.append(node)
        
        return discovered
    
    def get_node_info(self, node_id: str) -> Optional[PublicNode]:
        """Get information about a specific node"""
        return self.public_nodes.get(node_id)
    
    def update_node_status(self, node_id: str, status: str):
        """Update node status"""
        if node_id in self.public_nodes:
            self.public_nodes[node_id].status = status
            self.public_nodes[node_id].last_updated = datetime.now()
            self._save_public_nodes()
            
            # Commit to Git
            subprocess.run(['git', 'add', self.nodes_file_path], 
                         cwd=self.storage.ice_repo_path, check=True)
            subprocess.run(['git', 'commit', '-m', f'Update node status: {node_id} -> {status}'], 
                         cwd=self.storage.ice_repo_path, check=True)
    
    def export_network_map(self) -> Dict[str, Any]:
        """Export network map for discovery"""
        return {
            'total_nodes': len(self.public_nodes),
            'active_nodes': len([n for n in self.public_nodes.values() if n.status == 'active']),
            'regions': list(set(n.network_region for n in self.public_nodes.values())),
            'capabilities': list(set(cap for node in self.public_nodes.values() for cap in node.capabilities)),
            'nodes': {node_id: asdict(node) for node_id, node in self.public_nodes.items()}
        }

# Global instances
git_ice_storage = GitICEstorage()
public_node_registry = PublicNodeRegistry(git_ice_storage)
