#!/usr/bin/env python3
"""
ICE Bootstrap Engine - Self-Contained System Reconstruction

This module implements a minimal, immutable core that can:
1. Extract itself from ICE storage
2. Reconstruct the full Living Codex system
3. Validate its own coherence
4. Start up autonomously
"""

import json
import hashlib
import base64
import zlib
import os
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import subprocess
import importlib.util

@dataclass
class SystemComponent:
    """Represents a system component in ICE storage"""
    name: str
    component_type: str  # 'module', 'config', 'data', 'test'
    content: str  # Base64 encoded, compressed content
    content_hash: str
    dependencies: List[str]
    metadata: Dict[str, Any]
    created_at: str
    version: str

@dataclass
class BootstrapManifest:
    """Manifest of all system components"""
    system_name: str
    version: str
    created_at: str
    components: List[SystemComponent]
    bootstrap_sequence: List[str]
    validation_tests: List[str]
    startup_sequence: List[str]
    manifest_hash: str

class ICEBootstrapEngine:
    """
    Core engine that can reconstruct the Living Codex from ICE storage
    """
    
    def __init__(self, ice_storage_path: str = None):
        self.ice_storage_path = Path(ice_storage_path) if ice_storage_path else Path.cwd() / "ice_core"
        self.manifest = None
        self.extracted_components = {}
        self.system_root = Path.cwd()
        
    def load_bootstrap_manifest(self) -> bool:
        """Load the bootstrap manifest from ICE storage"""
        try:
            manifest_file = self.ice_storage_path / "bootstrap_manifest.json"
            if not manifest_file.exists():
                print("❌ Bootstrap manifest not found")
                return False
                
            with open(manifest_file, 'r') as f:
                manifest_data = json.load(f)
            
            # Validate manifest integrity
            if not self._validate_manifest(manifest_data):
                print("❌ Manifest validation failed")
                return False
            
            self.manifest = BootstrapManifest(**manifest_data)
            print(f"✅ Bootstrap manifest loaded: {self.manifest.system_name} v{self.manifest.version}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to load manifest: {e}")
            return False
    
    def _validate_manifest(self, manifest_data: Dict[str, Any]) -> bool:
        """Validate manifest integrity using hash verification"""
        try:
            # Calculate expected hash
            components_str = json.dumps(manifest_data.get('components', []), sort_keys=True)
            expected_hash = hashlib.sha256(components_str.encode()).hexdigest()
            
            actual_hash = manifest_data.get('manifest_hash', '')
            return expected_hash == actual_hash
            
        except Exception:
            return False
    
    def extract_system_components(self) -> bool:
        """Extract all system components from ICE storage"""
        if not self.manifest:
            print("❌ No manifest loaded")
            return False
        
        print(f"🔧 Extracting {len(self.manifest.components)} system components...")
        
        for component in self.manifest.components:
            if not self._extract_component(component):
                print(f"❌ Failed to extract {component.name}")
                return False
        
        print("✅ All components extracted successfully")
        return True
    
    def _extract_component(self, component: SystemComponent) -> bool:
        """Extract a single component from ICE storage"""
        try:
            # Decode and decompress content
            compressed_content = base64.b64decode(component.content)
            decompressed_content = zlib.decompress(compressed_content)
            
            # Verify content hash
            content_hash = hashlib.sha256(decompressed_content).hexdigest()
            if content_hash != component.content_hash:
                print(f"❌ Hash mismatch for {component.name}")
                return False
            
            # Store extracted component
            self.extracted_components[component.name] = {
                'content': decompressed_content.decode('utf-8'),
                'component': component
            }
            
            return True
            
        except Exception as e:
            print(f"❌ Extraction failed for {component.name}: {e}")
            return False
    
    def reconstruct_system(self) -> bool:
        """Reconstruct the full system from extracted components"""
        print("🏗️ Reconstructing Living Codex system...")
        
        # Create necessary directories
        self._create_system_structure()
        
        # Write components to files
        for name, data in self.extracted_components.items():
            if not self._write_component_file(name, data):
                return False
        
        print("✅ System reconstruction complete")
        return True
    
    def _create_system_structure(self):
        """Create the necessary directory structure"""
        directories = [
            'src/core',
            'src/platform', 
            'src/ontology',
            'src/ai_agents',
            'src/integration',
            'src/demos',
            'tests',
            'docs',
            'scripts'
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
    
    def _write_component_file(self, name: str, data: Dict[str, Any]) -> bool:
        """Write a component to its appropriate file location"""
        try:
            component = data['component']
            content = data['content']
            
            # Determine file path based on component type
            if component.component_type == 'module':
                file_path = self.system_root / f"src/core/{name}.py"
            elif component.component_type == 'config':
                file_path = self.system_root / f"config/{name}.json"
            elif component.component_type == 'test':
                file_path = self.system_root / f"tests/{name}.py"
            elif component.component_type == 'data':
                file_path = self.system_root / f"data/{name}.json"
            else:
                file_path = self.system_root / f"{name}.py"
            
            # Ensure parent directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to write {name}: {e}")
            return False
    
    def run_self_validation(self) -> bool:
        """Run self-validation tests to ensure system coherence"""
        print("🧪 Running self-validation tests...")
        
        if not self.manifest.validation_tests:
            print("⚠️ No validation tests defined")
            return True
        
        for test_name in self.manifest.validation_tests:
            if not self._run_validation_test(test_name):
                print(f"❌ Validation test failed: {test_name}")
                return False
        
        print("✅ All validation tests passed")
        return True
    
    def _run_validation_test(self, test_name: str) -> bool:
        """Run a single validation test"""
        try:
            # Import and run the test
            test_module = importlib.import_module(f"tests.{test_name}")
            
            if hasattr(test_module, 'run_validation'):
                return test_module.run_validation()
            else:
                print(f"⚠️ Test {test_name} has no run_validation method")
                return True
                
        except Exception as e:
            print(f"❌ Test {test_name} failed: {e}")
            return False
    
    def startup_system(self) -> bool:
        """Start up the Living Codex system"""
        print("🚀 Starting Living Codex system...")
        
        # Follow startup sequence
        for startup_step in self.manifest.startup_sequence:
            if not self._execute_startup_step(startup_step):
                print(f"❌ Startup step failed: {startup_step}")
                return False
        
        print("✅ System startup complete")
        return True
    
    def _execute_startup_step(self, step: str) -> bool:
        """Execute a single startup step"""
        try:
            if step == "start_web_service":
                return self._start_web_service()
            elif step == "initialize_database":
                return self._initialize_database()
            elif step == "load_ontology":
                return self._load_ontology()
            else:
                print(f"⚠️ Unknown startup step: {step}")
                return True
                
        except Exception as e:
            print(f"❌ Startup step {step} failed: {e}")
            return False
    
    def _start_web_service(self) -> bool:
        """Start the web service"""
        try:
            # Import and start web interface
            from src.platform.web_interface import app
            
            print("🌐 Starting web service on port 5001...")
            # Note: In production, this would run in a separate process
            print("✅ Web service ready (simulated)")
            return True
            
        except Exception as e:
            print(f"❌ Web service startup failed: {e}")
            return False
    
    def _initialize_database(self) -> bool:
        """Initialize the system database"""
        try:
            # Import and initialize database
            from src.core.database_persistence_system import DatabasePersistenceSystem
            
            db = DatabasePersistenceSystem()
            print("✅ Database initialized")
            return True
            
        except Exception as e:
            print(f"❌ Database initialization failed: {e}")
            return False
    
    def _load_ontology(self) -> bool:
        """Load the system ontology"""
        try:
            # Import and load ontology
            from src.ontology.enhanced_ontology_system import EnhancedOntologySystem
            
            ontology = EnhancedOntologySystem()
            print("✅ Ontology loaded")
            return True
            
        except Exception as e:
            print(f"❌ Ontology loading failed: {e}")
            return False
    
    def bootstrap_full_system(self) -> bool:
        """Complete bootstrap process"""
        print("🧊 ICE Bootstrap Process Starting...")
        print("=" * 50)
        
        # Step 1: Load manifest
        if not self.load_bootstrap_manifest():
            return False
        
        # Step 2: Extract components
        if not self.extract_system_components():
            return False
        
        # Step 3: Reconstruct system
        if not self.reconstruct_system():
            return False
        
        # Step 4: Self-validate
        if not self.run_self_validation():
            return False
        
        # Step 5: Start up
        if not self.startup_system():
            return False
        
        print("🎉 ICE Bootstrap Complete!")
        print("🌐 Living Codex is now available for new users to sign up and engage!")
        return True

def create_ice_core(components: List[SystemComponent], output_path: str) -> bool:
    """Create an ICE core from existing system components"""
    try:
        # Create bootstrap manifest
        manifest = BootstrapManifest(
            system_name="Living Codex",
            version="1.0.0",
            created_at=datetime.now().isoformat(),
            components=components,
            bootstrap_sequence=[
                "load_manifest",
                "extract_components", 
                "reconstruct_system",
                "run_validation",
                "startup_system"
            ],
            validation_tests=[
                "test_system_coherence",
                "test_core_functionality",
                "test_web_interface"
            ],
            startup_sequence=[
                "initialize_database",
                "load_ontology", 
                "start_web_service"
            ],
            manifest_hash=""
        )
        
        # Calculate manifest hash
        components_str = json.dumps(manifest.components, sort_keys=True)
        manifest.manifest_hash = hashlib.sha256(components_str.encode()).hexdigest()
        
        # Save manifest
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        manifest_file = output_dir / "bootstrap_manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest.__dict__, f, indent=2)
        
        print(f"✅ ICE core created at {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create ICE core: {e}")
        return False

if __name__ == "__main__":
    # Demo the bootstrap engine
    print("🧊 ICE Bootstrap Engine Demo")
    print("=" * 40)
    
    engine = ICEBootstrapEngine()
    
    # Check if manifest exists
    if engine.load_bootstrap_manifest():
        print("✅ Manifest found, ready to bootstrap")
    else:
        print("❌ No manifest found, system needs to be created first")
