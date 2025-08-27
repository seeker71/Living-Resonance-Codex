#!/usr/bin/env python3
"""
ICE Core Creator - Package Living Codex into Self-Contained ICE Core

This tool implements the Living Codex principle: "Everything is just nodes"
where the ICE Core Creator system is represented as nodes that can:

1. Analyze the current system (as nodes)
2. Create ICE components (as nodes)
3. Package everything into a self-contained ICE core (as nodes)
4. Generate bootstrap scripts (as nodes)

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The ICE Core Creator represents the Blueprint (Ice) state in the programming language ontology.
"""

import json
import hashlib
import base64
import zlib
import os
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import importlib.util

# Import the Shared Node System and GenericNode
from .shared_node_system import SharedNodeSystem
from .generic_node_system import GenericNode

class ICECoreCreatorNodeSystem(SharedNodeSystem):
    """
    ICE Core Creator using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Essential files are nodes
    - System analysis is nodes
    - ICE components are nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The ICE Core Creator represents the Blueprint (Ice) state in the programming language ontology:
    - Grammar, syntax rules, language structure
    - Class definitions, inheritance
    - Module structure, imports
    - Type system, static analysis framework
    """
    
    def __init__(self, system_root: str = None):
        super().__init__("ICECoreCreatorNodeSystem")
        self.system_root = Path(system_root) if system_root else Path.cwd()
        self._initialize_ice_creator_nodes()
        self._create_essential_file_nodes()
    
    def _initialize_ice_creator_nodes(self):
        """
        Initialize ICE creator system nodes - the foundation of the creator system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root ICE creator system node
        root_node = self.create_node(
            node_type='ice_creator_system_root',
            name='ICE Core Creator System Root',
            content='This is the root node of the ICE Core Creator System. It represents the system that packages Living Codex into self-contained ICE cores.',
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,  # Fractal System Root
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 1.0,
                'epistemic_label': 'engineering',
                'system_principle': 'Everything is just nodes - ICE creator as blueprint',
                'meta_circular': True,
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'System that packages Living Codex into ICE cores'
            }
        )
        
        # Create the ICE Creator Blueprint node
        ice_creator_blueprint_node = self.create_node(
            node_type='ice_creator_blueprint',
            name='ICE Creator Blueprint - Packaging System',
            content='ICE Creator represents the packaging system blueprint - analyzes, compresses, encodes, and packages the complete Living Codex system',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.95,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Packaging system blueprint for ICE core creation'
            }
        )
        
        # Create the System Analysis node
        system_analysis_node = self.create_node(
            node_type='system_analysis',
            name='System Analysis - Understanding Blueprint',
            content='System analysis represents the understanding blueprint - analyzes file structure, dependencies, and system composition',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Understanding blueprint for system analysis'
            }
        )
        
        # Create the ICE Component node
        ice_component_node = self.create_node(
            node_type='ice_component',
            name='ICE Component - Packaging Blueprint',
            content='ICE components represent the packaging blueprint - individual files compressed, encoded, and packaged for ICE storage',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Packaging blueprint for individual ICE components'
            }
        )
        
        # Create the Bootstrap Generation node
        bootstrap_generation_node = self.create_node(
            node_type='bootstrap_generation',
            name='Bootstrap Generation - Execution Blueprint',
            content='Bootstrap generation represents the execution blueprint - creates scripts that can reconstruct the system from ICE storage',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.85,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'description': 'Execution blueprint for bootstrap script generation'
            }
        )
        
        print(f"🌟 ICE Core Creator System initialized with {len(self.nodes)} nodes")
        print(f"🧊 ICE Creator Blueprint: {ice_creator_blueprint_node.name} (ID: {ice_creator_blueprint_node.node_id})")
        print(f"🔍 System Analysis: {system_analysis_node.name} (ID: {system_analysis_node.node_id})")
        print(f"📦 ICE Component: {ice_component_node.name} (ID: {ice_component_node.node_id})")
        print(f"🔧 Bootstrap Generation: {bootstrap_generation_node.name} (ID: {bootstrap_generation_node.node_id})")
    
    def _create_essential_file_nodes(self):
        """Create nodes for all essential files"""
        
        essential_files_data = [
            # Core system modules
            {"path": "src/core/water_state_storage.py", "type": "module", "name": "water_state_storage"},
            {"path": "src/core/ice_bootstrap_engine.py", "type": "module", "name": "ice_bootstrap_engine"},
            {"path": "src/core/ice_core_creator.py", "type": "module", "name": "ice_core_creator"},
            {"path": "src/core/minimal_ice_bootstrap.py", "type": "module", "name": "minimal_ice_bootstrap"},
            {"path": "src/core/dependency_manager.py", "type": "module", "name": "dependency_manager"},
            
            # Platform modules
            {"path": "src/web_platform/user_management.py", "type": "module", "name": "user_management"},
            {"path": "src/web_platform/contribution_system.py", "type": "module", "name": "contribution_system"},
            {"path": "src/web_platform/web_interface.py", "type": "module", "name": "web_interface"},
            
            # Ontology modules
            {"path": "src/ontology/enhanced_ontology_system.py", "type": "module", "name": "enhanced_ontology_system"},
            
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
        
        for file_info in essential_files_data:
            self.create_node(
                node_type='essential_file',
                name=f"Essential File: {file_info['name']}",
                content=f"Essential file for system operation: {file_info['path']} of type {file_info['type']}",
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.8,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'file_path': file_info['path'],
                    'file_type': file_info['type'],
                    'file_name': file_info['name'],
                    'description': f'Essential {file_info["type"]} file for system operation'
                }
            )
    
    def analyze_system(self) -> Dict[str, Any]:
        """Analyze the current system to understand its structure"""
        print("🔍 Analyzing Living Codex system...")
        
        # Create system analysis node
        analysis_node = self.create_node(
            node_type='system_analysis_result',
            name='System Analysis Result',
            content='Result of analyzing the Living Codex system structure and dependencies',
            metadata={
                'water_state': 'ice',
                'fractal_layer': 1,
                'chakra': 'crown',
                'frequency': 963,
                'color': '#EE82EE',
                'planet': 'Sun',
                'consciousness_mode': 'Structure, Memory',
                'quantum_state': 'coherent',
                'resonance_score': 0.9,
                'epistemic_label': 'engineering',
                'programming_ontology_layer': 'ice_blueprint',
                'analysis_timestamp': datetime.now().isoformat(),
                'system_root': str(self.system_root)
            }
        )
        
        analysis = {
            'total_files': 0,
            'total_size': 0,
            'file_types': {},
            'dependencies': {},
            'missing_files': [],
            'available_files': [],
            'analysis_node_id': analysis_node.node_id
        }
        
        # Get all essential file nodes
        essential_file_nodes = [node for node in self.nodes.values() if node.node_type == 'essential_file']
        
        for file_node in essential_file_nodes:
            file_path = self.system_root / file_node.metadata['file_path']
            
            if file_path.exists():
                file_info = {
                    'path': file_node.metadata['file_path'],
                    'type': file_node.metadata['file_type'],
                    'name': file_node.metadata['file_name']
                }
                
                analysis['available_files'].append(file_info)
                analysis['total_files'] += 1
                analysis['total_size'] += file_path.stat().st_size
                
                file_type = file_node.metadata['file_type']
                analysis['file_types'][file_type] = analysis['file_types'].get(file_type, 0) + 1
                
                # Analyze dependencies
                if file_node.metadata['file_type'] == 'module':
                    deps = self._analyze_module_dependencies(file_path)
                    analysis['dependencies'][file_node.metadata['file_name']] = deps
            else:
                file_info = {
                    'path': file_node.metadata['file_path'],
                    'type': file_node.metadata['file_type'],
                    'name': file_node.metadata['file_name']
                }
                analysis['missing_files'].append(file_info)
        
        # Update analysis node with results
        analysis_node.metadata.update({
            'total_files': analysis['total_files'],
            'total_size': analysis['total_size'],
            'file_types': analysis['file_types'],
            'dependencies': analysis['dependencies'],
            'missing_files_count': len(analysis['missing_files']),
            'available_files_count': len(analysis['available_files'])
        })
        
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
    
    def create_ice_components(self) -> List[GenericNode]:
        """Create ICE components from available files"""
        print("🧊 Creating ICE components...")
        
        components = []
        
        # Get all essential file nodes
        essential_file_nodes = [node for node in self.nodes.values() if node.node_type == 'essential_file']
        
        for file_node in essential_file_nodes:
            file_path = self.system_root / file_node.metadata['file_path']
            
            if file_path.exists():
                component_node = self._create_component_node_from_file(file_node, file_path)
                if component_node:
                    components.append(component_node)
                    print(f"✅ Created component: {component_node.name}")
        
        print(f"✅ Created {len(components)} ICE components")
        return components
    
    def _create_component_node_from_file(self, file_node: GenericNode, file_path: Path) -> Optional[GenericNode]:
        """Create a component node from a file"""
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
            if file_node.metadata['file_type'] == 'module':
                dependencies = self._analyze_module_dependencies(file_path)
            
            # Create component node
            component_node = self.create_node(
                node_type='ice_component',
                name=f"ICE Component: {file_node.metadata['file_name']}",
                content=f'ICE component for {file_node.metadata["file_name"]} - compressed and encoded for storage',
                metadata={
                    'water_state': 'ice',
                    'fractal_layer': 1,
                    'chakra': 'crown',
                    'frequency': 963,
                    'color': '#EE82EE',
                    'planet': 'Sun',
                    'consciousness_mode': 'Structure, Memory',
                    'quantum_state': 'coherent',
                    'resonance_score': 0.9,
                    'epistemic_label': 'engineering',
                    'programming_ontology_layer': 'ice_blueprint',
                    'component_name': file_node.metadata['file_name'],
                    'component_type': file_node.metadata['file_type'],
                    'encoded_content': encoded_content,
                    'content_hash': content_hash,
                    'dependencies': dependencies,
                    'original_path': str(file_path),
                    'file_size': len(content),
                    'compressed_size': len(compressed_content),
                    'compression_ratio': len(compressed_content) / len(content) if content else 0,
                    'created_at': datetime.now().isoformat(),
                    'version': "1.0.0",
                    'description': f'{file_node.metadata["file_type"]} component for ICE storage'
                }
            )
            
            return component_node
            
        except Exception as e:
            print(f"❌ Failed to create component from {file_path}: {e}")
            return None
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        ice_nodes = [node for node in self.nodes.values() if node.metadata.get('programming_ontology_layer') == 'ice_blueprint']
        essential_file_nodes = [node for node in self.nodes.values() if node.node_type == 'essential_file']
        component_nodes = [node for node in self.nodes.values() if node.node_type == 'ice_component']
        analysis_nodes = [node for node in self.nodes.values() if node.node_type == 'system_analysis_result']
        
        return {
            'total_nodes': len(self.nodes),
            'ice_blueprint_nodes': len(ice_nodes),
            'essential_file_nodes': len(essential_file_nodes),
            'component_nodes': len(component_nodes),
            'analysis_nodes': len(analysis_nodes),
            'water_states': list(set(node.get_water_state() for node in self.nodes.values())),
            'chakras': list(set(node.get_chakra() for node in self.nodes.values())),
            'frequencies': list(set(node.get_frequency() for node in self.nodes.values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.nodes.values()) / max(len(self.nodes), 1),
            'system_principle': 'Everything is just nodes - ICE creator as blueprint nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'ice_blueprint_layer'
        }

# Legacy compatibility - maintain the old interface for now
class ICECoreCreator(ICECoreCreatorNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self, system_root: str = None):
        super().__init__(system_root)
        print("🔄 ICECoreCreator initialized with new node-based system")
        print("✨ This system now embodies Living Codex principles")
        print("🌟 Everything is just nodes - ICE creator as blueprint nodes")
        print("🧊 ICE Creator represents Blueprint (Ice) state in programming language ontology")
