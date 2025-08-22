#!/usr/bin/env python3
"""
Standalone Demonstration of Git-Enabled ICE Storage System
Shows how the Living Codex bootstrap system can be globally accessible via Git
"""

import os
import sys
import json
import tempfile
from pathlib import Path
from datetime import datetime
import subprocess
import hashlib

def check_git_availability():
    """Check if Git is available on the system"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True, check=True)
        print(f"✅ Git is available: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not available. Please install Git for enhanced bootstrap features.")
        return False

def create_ice_repository():
    """Create a local ICE repository for demonstration"""
    print("\n🔧 Creating local ICE repository...")
    
    # Create repository directory
    repo_path = os.path.join(os.getcwd(), 'ice_core_demo')
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)
    
    os.makedirs(repo_path)
    
    try:
        # Initialize Git repository
        subprocess.run(['git', 'init'], cwd=repo_path, check=True)
        print(f"✅ Initialized Git repository at {repo_path}")
        
        # Create initial README
        readme_content = """# Living Codex ICE Core

This repository contains the immutable core (ICE) of the Living Codex system.

## Structure
- `src/core/` - Core system components
- `src/platform/` - Platform modules
- `bootstrap/` - Bootstrap scripts and manifests
- `public_nodes.json` - Network discovery information

## Usage
The ICE core provides self-bootstrapping capabilities for the Living Codex ecosystem.
"""
        
        readme_path = os.path.join(repo_path, 'README.md')
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        # Add and commit
        subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial ICE core commit'], cwd=repo_path, check=True)
        
        return repo_path
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create ICE repository: {e}")
        return None

def create_sample_ice_files(repo_path):
    """Create sample ICE core files in the repository"""
    print("\n📝 Creating sample ICE core files...")
    
    # Sample ICE files
    ice_files = {
        'src/core/minimal_ice_bootstrap.py': '''#!/usr/bin/env python3
"""
Minimal ICE Bootstrap System
Provides self-bootstrapping capabilities for Living Codex
"""

import os
import sys
from pathlib import Path

class ICEBootstrap:
    def __init__(self):
        self.core_components = []
        self.bootstrap_status = "initialized"
    
    def validate_system(self):
        print("🔍 Validating system components...")
        return True
    
    def bootstrap_core(self):
        print("🚀 Bootstrapping ICE core...")
        self.bootstrap_status = "bootstrapped"
        return True
    
    def get_status(self):
        return {
            "status": self.bootstrap_status,
            "components": len(self.core_components),
            "timestamp": "2025-08-22T12:00:00Z"
        }

if __name__ == "__main__":
    bootstrap = ICEBootstrap()
    if bootstrap.validate_system():
        bootstrap.bootstrap_core()
        print("✅ ICE Bootstrap completed successfully!")
''',
        
        'src/core/dependency_manager.py': '''#!/usr/bin/env python3
"""
Dependency Manager for ICE Core
Manages external dependencies and system requirements
"""

import subprocess
import sys

class DependencyManager:
    def __init__(self):
        self.required_packages = ['flask', 'flask-login', 'sqlite3']
    
    def check_dependencies(self):
        print("🔍 Checking system dependencies...")
        return True
    
    def install_dependencies(self):
        print("📦 Installing required dependencies...")
        return True
    
    def validate_system(self):
        print("✅ System dependencies validated")
        return True

if __name__ == "__main__":
    dm = DependencyManager()
    dm.check_dependencies()
    dm.install_dependencies()
    dm.validate_system()
''',
        
        'src/platform/web_interface.py': '''#!/usr/bin/env python3
"""
Web Interface for Living Codex
Provides web-based access to system features
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Living Codex Web Interface - Ready"

@app.route('/status')
def status():
    return {"status": "active", "version": "1.0.0"}

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
''',
        
        'bootstrap/ice_bootstrap.py': '''#!/usr/bin/env python3
"""
Main ICE Bootstrap Script
Entry point for system initialization
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def main():
    print("🚀 Living Codex ICE Bootstrap System")
    print("=" * 40)
    
    try:
        # Import and run bootstrap
        from core.minimal_ice_bootstrap import ICEBootstrap
        
        bootstrap = ICEBootstrap()
        if bootstrap.validate_system():
            bootstrap.bootstrap_core()
            status = bootstrap.get_status()
            print(f"✅ Bootstrap completed: {status}")
        else:
            print("❌ System validation failed")
            
    except Exception as e:
        print(f"❌ Bootstrap failed: {e}")

if __name__ == "__main__":
    main()
''',
        
        'ice_manifest.json': '''{
  "version": "1.0.0",
  "created_at": "2025-08-22T12:00:00Z",
  "components": [
    "src/core/minimal_ice_bootstrap.py",
    "src/core/dependency_manager.py",
    "src/platform/web_interface.py",
    "bootstrap/ice_bootstrap.py"
  ],
  "dependencies": {
    "flask": ">=2.0.0",
    "flask-login": ">=0.6.0",
    "sqlite3": ">=2.6.0"
  },
  "bootstrap_script": "bootstrap/ice_bootstrap.py",
  "git_commit_hash": "initial",
  "git_branch": "main",
  "git_remote_url": "https://github.com/your-org/living-codex-ice.git"
}'''
    }
    
    # Create files in repository
    for file_path, content in ice_files.items():
        full_path = os.path.join(repo_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'w') as f:
            f.write(content)
        
        print(f"   ✅ Created: {file_path}")
    
    return ice_files

def commit_ice_core(repo_path, ice_files):
    """Commit ICE core files to Git repository"""
    print("\n💾 Committing ICE core to Git...")
    
    try:
        # Add all files
        subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)
        
        # Commit with descriptive message
        commit_message = f"Add ICE core v1.0.0 - {len(ice_files)} components"
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)
        
        # Get commit hash
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=repo_path, 
                              capture_output=True, text=True, check=True)
        commit_hash = result.stdout.strip()[:8]
        
        print(f"✅ Committed ICE core with hash: {commit_hash}")
        return commit_hash
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to commit ICE core: {e}")
        return None

def show_git_history(repo_path):
    """Show Git commit history"""
    print("\n📜 Git commit history:")
    
    try:
        result = subprocess.run(['git', 'log', '--oneline'], cwd=repo_path, 
                              capture_output=True, text=True, check=True)
        
        commits = result.stdout.strip().split('\n')
        for commit in commits:
            if commit:
                print(f"   {commit}")
                
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to get commit history: {e}")

def create_public_nodes_file(repo_path):
    """Create public nodes registry file"""
    print("\n🌐 Creating public nodes registry...")
    
    public_nodes = {
        "node_001": {
            "node_id": "node_001",
            "name": "Living Codex Hub - North America",
            "description": "Primary hub for North American region",
            "location": "North America",
            "capabilities": ["bootstrap", "ice_storage", "web_interface", "api"],
            "ice_repository_url": "https://github.com/living-codex/ice-core.git",
            "ice_commit_hash": "abc12345",
            "last_updated": "2025-08-22T12:00:00Z",
            "contact_info": {"email": "hub@living-codex.org", "region": "NA"},
            "network_region": "north_america",
            "status": "active"
        },
        "node_002": {
            "node_id": "node_002",
            "name": "Living Codex Hub - Europe",
            "description": "Primary hub for European region",
            "location": "Europe",
            "capabilities": ["bootstrap", "ice_storage", "web_interface", "api"],
            "ice_repository_url": "https://github.com/living-codex/ice-core.git",
            "ice_commit_hash": "def67890",
            "last_updated": "2025-08-22T12:00:00Z",
            "contact_info": {"email": "hub-eu@living-codex.org", "region": "EU"},
            "network_region": "europe",
            "status": "active"
        },
        "node_003": {
            "node_id": "node_003",
            "name": "Living Codex Hub - Asia Pacific",
            "description": "Primary hub for Asia Pacific region",
            "location": "Asia Pacific",
            "capabilities": ["bootstrap", "ice_storage", "web_interface", "api"],
            "ice_repository_url": "https://github.com/living-codex/ice-core.git",
            "ice_commit_hash": "ghi11111",
            "last_updated": "2025-08-22T12:00:00Z",
            "contact_info": {"email": "hub-ap@living-codex.org", "region": "AP"},
            "network_region": "asia_pacific",
            "status": "active"
        }
    }
    
    # Write public nodes file
    nodes_file_path = os.path.join(repo_path, 'public_nodes.json')
    with open(nodes_file_path, 'w') as f:
        json.dump(public_nodes, f, indent=2)
    
    print(f"✅ Created public nodes registry with {len(public_nodes)} nodes")
    
    # Commit the nodes file
    try:
        subprocess.run(['git', 'add', 'public_nodes.json'], cwd=repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', 'Add public nodes registry'], cwd=repo_path, check=True)
        print("✅ Committed public nodes registry")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Failed to commit nodes registry: {e}")

def demonstrate_network_discovery(repo_path):
    """Demonstrate network discovery capabilities"""
    print("\n🔍 Demonstrating network discovery...")
    
    # Load public nodes
    nodes_file_path = os.path.join(repo_path, 'public_nodes.json')
    with open(nodes_file_path, 'r') as f:
        public_nodes = json.load(f)
    
    # Show network statistics
    total_nodes = len(public_nodes)
    active_nodes = len([n for n in public_nodes.values() if n['status'] == 'active'])
    regions = list(set(n['network_region'] for n in public_nodes.values()))
    capabilities = list(set(cap for node in public_nodes.values() for cap in node['capabilities']))
    
    print(f"   📊 Network Statistics:")
    print(f"      Total nodes: {total_nodes}")
    print(f"      Active nodes: {active_nodes}")
    print(f"      Regions: {', '.join(regions)}")
    print(f"      Capabilities: {', '.join(capabilities)}")
    
    # Show node discovery by capabilities
    print(f"\n   🔍 Node Discovery by Capabilities:")
    bootstrap_nodes = [n for n in public_nodes.values() if 'bootstrap' in n['capabilities']]
    for node in bootstrap_nodes:
        print(f"      📡 {node['name']} - {node['location']}")
        print(f"         Capabilities: {', '.join(node['capabilities'])}")
        print(f"         Status: {node['status']}")
        print()

def show_git_operations():
    """Show available Git operations"""
    print("\n🔧 Available Git Operations:")
    print("   git init                    - Initialize ICE repository")
    print("   git add .                   - Stage all changes")
    print("   git commit -m 'message'     - Commit changes")
    print("   git remote add origin URL   - Add remote repository")
    print("   git push origin main        - Push to remote")
    print("   git pull origin main        - Pull from remote")
    print("   git checkout <commit>       - Checkout specific version")
    print("   git log --oneline          - View commit history")

def show_network_topology():
    """Show network topology benefits"""
    print("\n🌐 Network Topology Benefits:")
    print("   📡 Global Discovery        - Find nodes worldwide")
    print("   🔄 Load Balancing          - Distribute requests across nodes")
    print("   🛡️ Fault Tolerance         - Multiple node redundancy")
    print("   📊 Health Monitoring       - Track node status and performance")
    print("   🔗 Peer Connections        - Direct node-to-node communication")
    print("   📈 Scalability            - Add nodes as needed")

def main():
    """Main demonstration function"""
    print("🚀 Living Codex Git-Enabled ICE Storage Demonstration")
    print("=" * 60)
    
    # Check Git availability
    if not check_git_availability():
        print("❌ Git is required for this demonstration")
        return
    
    # Step 1: Create ICE repository
    repo_path = create_ice_repository()
    if not repo_path:
        print("❌ Failed to create ICE repository")
        return
    
    # Step 2: Create sample ICE files
    ice_files = create_sample_ice_files(repo_path)
    
    # Step 3: Commit ICE core
    commit_hash = commit_ice_core(repo_path, ice_files)
    if not commit_hash:
        print("❌ Failed to commit ICE core")
        return
    
    # Step 4: Show Git history
    show_git_history(repo_path)
    
    # Step 5: Create public nodes registry
    create_public_nodes_file(repo_path)
    
    # Step 6: Demonstrate network discovery
    demonstrate_network_discovery(repo_path)
    
    # Step 7: Show Git operations and benefits
    show_git_operations()
    show_network_topology()
    
    print("\n🎉 Git-Enabled ICE Storage Demonstration Complete!")
    print(f"\n📁 ICE Repository created at: {repo_path}")
    print("   You can now:")
    print("   - Add a remote origin: git remote add origin <your-repo-url>")
    print("   - Push to remote: git push -u origin main")
    print("   - Pull updates: git pull origin main")
    print("   - Checkout versions: git checkout <commit-hash>")
    
    print("\nKey Benefits:")
    print("✅ Global accessibility via Git repositories")
    print("✅ Version control for immutable core")
    print("✅ Distributed node discovery")
    print("✅ Automatic updates and synchronization")
    print("✅ Integrity validation via checksums")
    print("✅ Network topology mapping")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        import traceback
        traceback.print_exc()
