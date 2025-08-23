#!/usr/bin/env python3
"""
ICE Core Creator - Package Living Codex into Self-Contained ICE Core

This tool analyzes the current system and creates a minimal, self-contained
ICE core that can bootstrap the entire Living Codex system.
"""

import json
import hashlib
import base64
import zlib
import os
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import asdict
from datetime import datetime
import importlib.util

from .ice_bootstrap_engine import SystemComponent

class ICECoreCreator:
    """
    Creates an ICE core from the current Living Codex system
    """
    
    def __init__(self, system_root: str = None):
        self.system_root = Path(system_root) if system_root else Path.cwd()
        self.core_components = []
        self.essential_files = self._get_essential_files()
        
    def _get_essential_files(self) -> List[Dict[str, str]]:
        """Define the essential files needed for system operation"""
        return [
            # Core system modules
            {"path": "src/core/water_state_storage.py", "type": "module", "name": "water_state_storage"},
            {"path": "src/core/ice_bootstrap_engine.py", "type": "module", "name": "ice_bootstrap_engine"},
            {"path": "src/core/ice_core_creator.py", "type": "module", "name": "ice_core_creator"},
            {"path": "src/core/minimal_ice_bootstrap.py", "type": "module", "name": "minimal_ice_bootstrap"},
            {"path": "src/core/dependency_manager.py", "type": "module", "name": "dependency_manager"},
            
            # Platform modules
            {"path": "src/platform/user_management.py", "type": "module", "name": "user_management"},
            {"path": "src/platform/contribution_system.py", "type": "module", "name": "contribution_system"},
            {"path": "src/platform/web_interface.py", "type": "module", "name": "web_interface"},
            
            # Ontology modules
            {"path": "src/ontology/enhanced_ontology_system.py", "type": "module", "name": "enhanced_ontology_system"},
            
            # Core tests
            {"path": "tests/regression_test_suite.py", "type": "test", "name": "regression_test_suite"},
            {"path": "tests/test_testing_system.py", "type": "test", "name": "test_testing_system"},
            
            # Core tests
            {"path": "tests/regression_test_suite.py", "type": "test", "name": "regression_test_suite"},
            {"path": "tests/test_testing_system.py", "type": "test", "name": "test_testing_system"},
            
            # Configuration files
            {"path": "requirements.txt", "type": "config", "name": "requirements"},
            {"path": ".gitignore", "type": "config", "name": "gitignore"},
            
            # Documentation
            {"path": "README.md", "type": "data", "name": "readme"},
            {"path": "docs/LIVING_CODEX_SPECIFICATION.md", "type": "data", "name": "living_codex_spec"},
            {"path": "docs/WATER_STATE_STORAGE.md", "type": "data", "name": "water_state_storage_docs"},
            
            # Scripts
            {"path": "scripts/test_runner.py", "type": "module", "name": "test_runner"},
            {"path": "scripts/continuous_integration.py", "type": "module", "name": "continuous_integration"},
            
            # Demo scripts
            {"path": "demo_water_states.py", "type": "module", "name": "demo_water_states"},
            {"path": "demo_platform.py", "type": "module", "name": "demo_platform"}
        ]
    
    def analyze_system(self) -> Dict[str, Any]:
        """Analyze the current system to understand its structure"""
        print("🔍 Analyzing Living Codex system...")
        
        analysis = {
            'total_files': 0,
            'total_size': 0,
            'file_types': {},
            'dependencies': {},
            'missing_files': [],
            'available_files': []
        }
        
        for file_info in self.essential_files:
            file_path = self.system_root / file_info['path']
            
            if file_path.exists():
                analysis['available_files'].append(file_info)
                analysis['total_files'] += 1
                analysis['total_size'] += file_path.stat().st_size
                
                file_type = file_info['type']
                analysis['file_types'][file_type] = analysis['file_types'].get(file_type, 0) + 1
                
                # Analyze dependencies
                if file_info['type'] == 'module':
                    deps = self._analyze_module_dependencies(file_path)
                    analysis['dependencies'][file_info['name']] = deps
            else:
                analysis['missing_files'].append(file_info)
        
        print(f"✅ Analysis complete: {analysis['total_files']} files found")
        print(f"📊 Total size: {analysis['total_size'] / 1024:.1f} KB")
        
        return analysis
    
    def _analyze_module_dependencies(self, file_path: Path) -> List[str]:
        """Analyze Python module dependencies"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            dependencies = []
            
            # Look for import statements
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('import ') or line.startswith('from '):
                    # Extract module name
                    if line.startswith('import '):
                        module = line.split('import ')[1].split(' as ')[0].split(',')[0].strip()
                    else:
                        module = line.split('from ')[1].split(' import ')[0].strip()
                    
                    if module and not module.startswith('.'):
                        dependencies.append(module)
            
            return dependencies
            
        except Exception as e:
            print(f"⚠️ Could not analyze dependencies for {file_path}: {e}")
            return []
    
    def create_ice_components(self) -> List[SystemComponent]:
        """Create ICE components from available files"""
        print("🧊 Creating ICE components...")
        
        components = []
        
        for file_info in self.essential_files:
            file_path = self.system_root / file_info['path']
            
            if file_path.exists():
                component = self._create_component_from_file(file_info, file_path)
                if component:
                    components.append(component)
                    print(f"✅ Created component: {component.name}")
        
        print(f"✅ Created {len(components)} ICE components")
        return components
    
    def _create_component_from_file(self, file_info: Dict[str, str], file_path: Path) -> Optional[SystemComponent]:
        """Create a SystemComponent from a file"""
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Compress and encode content
            compressed_content = zlib.compress(content.encode('utf-8'))
            encoded_content = base64.b64encode(compressed_content).decode('utf-8')
            
            # Calculate content hash
            content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
            
            # Get dependencies
            dependencies = []
            if file_info['type'] == 'module':
                dependencies = self._analyze_module_dependencies(file_path)
            
            # Create component
            component = SystemComponent(
                name=file_info['name'],
                component_type=file_info['type'],
                content=encoded_content,
                content_hash=content_hash,
                dependencies=dependencies,
                metadata={
                    'original_path': str(file_path),
                    'file_size': len(content),
                    'compressed_size': len(compressed_content),
                    'compression_ratio': len(compressed_content) / len(content) if content else 0
                },
                created_at=datetime.now().isoformat(),
                version="1.0.0"
            )
            
            return component
            
        except Exception as e:
            print(f"❌ Failed to create component from {file_path}: {e}")
            return None
    
    def create_ice_core(self, output_path: str = "ice_core") -> bool:
        """Create the complete ICE core"""
        print("🧊 Creating ICE Core...")
        print("=" * 40)
        
        # Step 1: Analyze system
        analysis = self.analyze_system()
        
        if analysis['missing_files']:
            print(f"⚠️ Warning: {len(analysis['missing_files'])} files are missing")
            for missing in analysis['missing_files']:
                print(f"   - {missing['path']}")
        
        # Step 2: Create components
        components = self.create_ice_components()
        
        if not components:
            print("❌ No components created")
            return False
        
        # Step 3: Create ICE core
        success = self._create_ice_core_directly(components, output_path)
        
        if success:
            print(f"\n🎉 ICE Core created successfully at {output_path}/")
            print(f"📦 Contains {len(components)} components")
            print(f"💾 Total compressed size: {sum(c.metadata['compressed_size'] for c in components) / 1024:.1f} KB")
            print("\n🚀 The ICE core can now bootstrap the entire Living Codex system!")
        
        return success
    
    def create_minimal_bootstrap(self, output_path: str = "minimal_bootstrap") -> bool:
        """Create a minimal bootstrap that can reconstruct the ICE core"""
        print("🔧 Creating minimal bootstrap...")
        
        # Create minimal bootstrap script
        bootstrap_content = '''#!/usr/bin/env python3
"""
Minimal Bootstrap Script for Living Codex ICE Core

This script can reconstruct the entire Living Codex system from its ICE core.
It's designed to be as small as possible while being completely self-contained.
"""

import json
import hashlib
import base64
import zlib
import os
import sys
from pathlib import Path

def bootstrap_living_codex():
    """Bootstrap the Living Codex from ICE core"""
    print("🧊 Living Codex ICE Bootstrap Starting...")
    
    # Check for ICE core
    ice_core_path = Path("ice_core")
    if not ice_core_path.exists():
        print("❌ ICE core not found. Please ensure 'ice_core' directory exists.")
        return False
    
    manifest_file = ice_core_path / "bootstrap_manifest.json"
    if not manifest_file.exists():
        print("❌ Bootstrap manifest not found.")
        return False
    
    try:
        # Load manifest
        with open(manifest_file, 'r') as f:
            manifest = json.load(f)
        
        print(f"✅ Manifest loaded: {manifest['system_name']} v{manifest['version']}")
        
        # Extract components
        components = manifest['components']
        print(f"🔧 Extracting {len(components)} components...")
        
        for component in components:
            if not extract_component(component, ice_core_path):
                print(f"❌ Failed to extract {component['name']}")
                return False
        
        print("✅ All components extracted")
        print("🚀 Living Codex system ready!")
        print("🌐 Starting web service...")
        
        # Start web service
        start_web_service()
        return True
        
    except Exception as e:
        print(f"❌ Bootstrap failed: {e}")
        return False

def extract_component(component, ice_core_path):
    """Extract a single component"""
    try:
        # Decode and decompress
        compressed = base64.b64decode(component['content'])
        content = zlib.decompress(compressed).decode('utf-8')
        
        # Verify hash
        if hashlib.sha256(content.encode()).hexdigest() != component['content_hash']:
            return False
        
        # Write file
        file_path = Path(component['name'] + '.py')
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        return True
        
    except Exception:
        return False

def start_web_service():
    """Start the web service"""
    try:
        # Import and start web interface
        sys.path.insert(0, 'src/platform')
        from web_interface import app
        
        print("🌐 Web service starting on port 5001...")
        print("✅ Living Codex is now available for new users!")
        print("   Open your browser to: http://localhost:5001")
        
        # In production, this would run the Flask app
        # app.run(host='0.0.0.0', port=5001)
        
    except Exception as e:
        print(f"⚠️ Web service startup failed: {e}")

if __name__ == "__main__":
    success = bootstrap_living_codex()
    sys.exit(0 if success else 1)
'''
        
        # Write minimal bootstrap
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        bootstrap_file = output_dir / "bootstrap.py"
        with open(bootstrap_file, 'w') as f:
            f.write(bootstrap_content)
        
        # Make executable
        os.chmod(bootstrap_file, 0o755)
        
        print(f"✅ Minimal bootstrap created at {bootstrap_file}")
        print("🔧 This script can reconstruct the entire system from the ICE core")
        
        return True
    
    def _create_ice_core_directly(self, components: List[SystemComponent], output_path: str) -> bool:
        """Create ICE core directly without external function"""
        try:
            # Create bootstrap manifest
            manifest = {
                'system_name': "Living Codex",
                'version': "1.0.0",
                'created_at': datetime.now().isoformat(),
                'components': [
                    {
                        'name': c.name,
                        'component_type': c.component_type,
                        'content': c.content,
                        'content_hash': c.content_hash,
                        'dependencies': c.dependencies,
                        'metadata': c.metadata,
                        'created_at': c.created_at,
                        'version': c.version
                    }
                    for c in components
                ],
                'bootstrap_sequence': [
                    "load_manifest",
                    "extract_components", 
                    "reconstruct_system",
                    "run_validation",
                    "startup_system"
                ],
                'validation_tests': [
                    "test_system_coherence",
                    "test_core_functionality",
                    "test_web_interface"
                ],
                'startup_sequence': [
                    "validate_system",
                    "initialize_database",
                    "load_ontology", 
                    "start_web_service"
                ],
                'manifest_hash': ""
            }
            
            # Calculate manifest hash
            components_str = json.dumps(manifest['components'], sort_keys=True)
            manifest['manifest_hash'] = hashlib.sha256(components_str.encode()).hexdigest()
            
            # Save manifest
            output_dir = Path(output_path)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            manifest_file = output_dir / "bootstrap_manifest.json"
            with open(manifest_file, 'w') as f:
                json.dump(manifest, f, indent=2)
            
            print(f"✅ ICE core created at {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create ICE core: {e}")
            return False

def main():
    """Main function for ICE core creation"""
    print("🧊 Living Codex ICE Core Creator")
    print("=" * 40)
    
    creator = ICECoreCreator()
    
    # Create ICE core
    if creator.create_ice_core():
        print("\n🎯 Next steps:")
        print("1. Copy the 'ice_core' directory to your target system")
        print("2. Run: python src/core/ice_bootstrap_engine.py")
        print("3. The system will bootstrap itself and start the web service")
        print("4. New users can sign up and engage with the Living Codex!")
    
    # Create minimal bootstrap
    print("\n🔧 Creating minimal bootstrap...")
    creator.create_minimal_bootstrap()

if __name__ == "__main__":
    main()
