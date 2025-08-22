#!/usr/bin/env python3
"""
Demonstration of Git-Enabled ICE Storage System
Shows how the Living Codex bootstrap system can be globally accessible via Git
"""

import os
import sys
import json
import tempfile
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.git_ice_storage import (
    GitICEstorage, PublicNodeRegistry, PublicNode, ICEManifest
)
from src.core.git_ice_bootstrap import GitICEBootstrap, create_bootstrap_config

def demo_git_ice_storage():
    """Demonstrate Git-enabled ICE storage capabilities"""
    
    print("🚀 Living Codex Git-Enabled ICE Storage Demonstration")
    print("=" * 60)
    
    # Step 1: Initialize Git ICE Storage
    print("\n1️⃣ Initializing Git ICE Storage...")
    storage = GitICEstorage()
    
    # Step 2: Create sample ICE core files
    print("\n2️⃣ Creating sample ICE core files...")
    ice_files = create_sample_ice_files()
    
    # Step 3: Store ICE core in Git repository
    print("\n3️⃣ Storing ICE core in Git repository...")
    metadata = {
        'version': '1.0.0',
        'dependencies': {
            'flask': '>=2.0.0',
            'flask-login': '>=0.6.0',
            'sqlite3': '>=2.6.0'
        },
        'bootstrap_script': 'bootstrap/ice_bootstrap.py',
        'git_remote_url': 'https://github.com/your-org/living-codex-ice.git'
    }
    
    commit_hash = storage.store_ice_core(ice_files, metadata)
    if commit_hash:
        print(f"✅ ICE core stored with commit: {commit_hash}")
    else:
        print("❌ Failed to store ICE core")
        return
    
    # Step 4: Show commit history
    print("\n4️⃣ Git commit history:")
    commits = storage.get_commit_history()
    for commit in commits:
        print(f"   {commit['hash']}: {commit['message']}")
    
    # Step 5: Demonstrate public node registry
    print("\n5️⃣ Setting up public node registry...")
    registry = PublicNodeRegistry(storage)
    
    # Register some sample nodes
    sample_nodes = create_sample_public_nodes()
    for node in sample_nodes:
        registry.register_node(node)
    
    # Step 6: Show network discovery
    print("\n6️⃣ Network discovery capabilities:")
    network_map = registry.export_network_map()
    print(f"   Total nodes: {network_map['total_nodes']}")
    print(f"   Active nodes: {network_map['active_nodes']}")
    print(f"   Regions: {', '.join(network_map['regions'])}")
    print(f"   Capabilities: {', '.join(network_map['capabilities'])}")
    
    # Step 7: Demonstrate node discovery
    print("\n7️⃣ Node discovery by capabilities:")
    discovery_nodes = registry.discover_nodes(capabilities=['bootstrap'])
    for node in discovery_nodes:
        print(f"   📡 {node.name} - {node.location} ({', '.join(node.capabilities)})")
    
    # Step 8: Show ICE core retrieval
    print("\n8️⃣ Retrieving ICE core from Git...")
    retrieved_files, manifest = storage.retrieve_ice_core()
    if retrieved_files and manifest:
        print(f"✅ Retrieved ICE core v{manifest.version}")
        print(f"   Components: {len(retrieved_files)}")
        print(f"   Git commit: {manifest.git_commit_hash}")
        print(f"   Git branch: {manifest.git_branch}")
    else:
        print("❌ Failed to retrieve ICE core")
    
    # Step 9: Demonstrate enhanced bootstrap
    print("\n9️⃣ Enhanced ICE Bootstrap with Git integration...")
    config = create_bootstrap_config(
        ice_repository_url="https://github.com/your-org/living-codex-ice.git",
        auto_update=True,
        network_discovery=True
    )
    
    bootstrap = GitICEBootstrap(config)
    
    # Get bootstrap status
    status = bootstrap.get_bootstrap_status()
    print(f"   Status: {status['status']}")
    print(f"   Components loaded: {status['components_loaded']}")
    
    # Step 10: Show network map
    print("\n🔟 Final network map:")
    final_network_map = bootstrap.get_network_map()
    print(json.dumps(final_network_map, indent=2, default=str))
    
    print("\n🎉 Git-Enabled ICE Storage Demonstration Complete!")
    print("\nKey Benefits:")
    print("✅ Global accessibility via Git repositories")
    print("✅ Version control for immutable core")
    print("✅ Distributed node discovery")
    print("✅ Automatic updates and synchronization")
    print("✅ Integrity validation via checksums")
    print("✅ Network topology mapping")

def create_sample_ice_files() -> dict:
    """Create sample ICE core files for demonstration"""
    return {
        'src/core/minimal_ice_bootstrap.py': '''#!/usr/bin/env python3
"""Minimal ICE Bootstrap System"""
print("ICE Core Bootstrap System - Ready")''',
        
        'src/core/dependency_manager.py': '''#!/usr/bin/env python3
"""Dependency Manager for ICE Core"""
print("Dependency Manager - Ready")''',
        
        'src/platform/web_interface.py': '''#!/usr/bin/env python3
"""Web Interface for Living Codex"""
print("Web Interface - Ready")''',
        
        'bootstrap/ice_bootstrap.py': '''#!/usr/bin/env python3
"""Main ICE Bootstrap Script"""
print("Main Bootstrap Script - Ready")''',
        
        'README.md': '''# Living Codex ICE Core

This is the immutable core of the Living Codex system.

## Features
- Self-bootstrapping capabilities
- Dependency management
- Web interface integration
- Git-based version control

## Usage
Run the bootstrap script to initialize the system.
'''
    }

def create_sample_public_nodes() -> list:
    """Create sample public nodes for demonstration"""
    from datetime import datetime
    
    return [
        PublicNode(
            node_id="node_001",
            name="Living Codex Hub - North America",
            description="Primary hub for North American region",
            location="North America",
            capabilities=['bootstrap', 'ice_storage', 'web_interface', 'api'],
            ice_repository_url="https://github.com/living-codex/ice-core.git",
            ice_commit_hash="abc12345",
            last_updated=datetime.now(),
            contact_info={'email': 'hub@living-codex.org', 'region': 'NA'},
            network_region="north_america",
            status="active"
        ),
        PublicNode(
            node_id="node_002",
            name="Living Codex Hub - Europe",
            description="Primary hub for European region",
            location="Europe",
            capabilities=['bootstrap', 'ice_storage', 'web_interface', 'api'],
            ice_repository_url="https://github.com/living-codex/ice-core.git",
            ice_commit_hash="def67890",
            last_updated=datetime.now(),
            contact_info={'email': 'hub-eu@living-codex.org', 'region': 'EU'},
            network_region="europe",
            status="active"
        ),
        PublicNode(
            node_id="node_003",
            name="Living Codex Hub - Asia Pacific",
            description="Primary hub for Asia Pacific region",
            location="Asia Pacific",
            capabilities=['bootstrap', 'ice_storage', 'web_interface', 'api'],
            ice_repository_url="https://github.com/living-codex/ice-core.git",
            ice_commit_hash="ghi11111",
            last_updated=datetime.now(),
            contact_info={'email': 'hub-ap@living-codex.org', 'region': 'AP'},
            network_region="asia_pacific",
            status="active"
        )
    ]

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

if __name__ == "__main__":
    try:
        demo_git_ice_storage()
        show_git_operations()
        show_network_topology()
        
        print("\n🚀 Ready to deploy globally accessible Living Codex nodes!")
        print("   Each node can bootstrap from the Git repository")
        print("   Automatic discovery and synchronization")
        print("   Version-controlled immutable core")
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        import traceback
        traceback.print_exc()
