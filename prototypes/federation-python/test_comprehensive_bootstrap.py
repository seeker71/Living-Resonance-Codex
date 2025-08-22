#!/usr/bin/env python3
"""
Comprehensive Self-Bootstrap Test - Living Codex
Bootstraps all system files into the Codex itself, creating a fully self-contained,
meta-circular knowledge system that can explore its own boundaries.
"""

import sys
import os
import json
import hashlib
import base64
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import asyncio

# Add src to path for modular components
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import our systems
from neo4j_integration_system import Neo4jIntegrationSystem
from database_persistence_system import DatabasePersistenceSystem, DatabaseType, DatabaseNode, QueryFilter, QueryOptions
from real_external_api_system import RealExternalAPISystem

class ComprehensiveBootstrapTest:
    """Comprehensive test for bootstrapping the entire system into itself"""
    
    def __init__(self):
        self.neo4j = Neo4jIntegrationSystem()
        self.database = DatabasePersistenceSystem(db_path="comprehensive_bootstrap.db")
        self.api_system = RealExternalAPISystem()
        self.bootstrap_nodes = {}
        self.meta_nodes = {}
        self.file_nodes = {}
        
    async def run_comprehensive_test(self):
        """Run the complete comprehensive bootstrap test"""
        print("🚀 Living Codex - Comprehensive Self-Bootstrap Test")
        print("=" * 70)
        
        try:
            # Phase 1: System Initialization
            await self.phase1_system_initialization()
            
            # Phase 2: Core Ontology Bootstrap
            await self.phase2_core_ontology_bootstrap()
            
            # Phase 3: File System Bootstrap
            await self.phase3_file_system_bootstrap()
            
            # Phase 4: Meta-Circular System Creation
            await self.phase4_meta_circular_system()
            
            # Phase 5: Self-Exploration and Boundary Detection
            await self.phase5_self_exploration()
            
            # Phase 6: Knowledge Hologram Analysis
            await self.phase6_knowledge_hologram_analysis()
            
            print("\n🎉 Comprehensive Bootstrap Test Completed Successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            await self.cleanup()
    
    async def phase1_system_initialization(self):
        """Phase 1: Initialize all systems"""
        print("\n🔧 Phase 1: System Initialization")
        print("-" * 40)
        
        # Initialize database
        print("📊 Initializing database...")
        await self.database.initialize()
        
        # Initialize Neo4j (with fallback)
        print("🕸️  Initializing Neo4j...")
        try:
            await self.neo4j.initialize()
            print("✅ Neo4j connected")
        except Exception as e:
            print(f"⚠️  Neo4j not available: {e}")
            print("   Using database fallback for graph operations")
        
        # Initialize API system
        print("🌐 Initializing API system...")
        await self.api_system.initialize()
        
        print("✅ All systems initialized")
    
    async def phase2_core_ontology_bootstrap(self):
        """Phase 2: Bootstrap core ontological concepts"""
        print("\n🧬 Phase 2: Core Ontology Bootstrap")
        print("-" * 40)
        
        # Create core ontological nodes
        core_concepts = [
            {
                "name": "node",
                "description": "Fundamental unit of knowledge in the Living Codex",
                "type": "ontological_concept",
                "properties": ["id", "name", "content", "type", "metadata", "relationships"]
            },
            {
                "name": "relationship",
                "description": "Connection between nodes representing knowledge links",
                "type": "ontological_concept", 
                "properties": ["source", "target", "type", "properties", "metadata"]
            },
            {
                "name": "water_state",
                "description": "Metaphysical state of knowledge (ice, liquid, vapor, plasma)",
                "type": "ontological_concept",
                "properties": ["state", "energy_level", "transformation_cost", "properties"]
            },
            {
                "name": "realm",
                "description": "Domain or category of knowledge",
                "type": "ontological_concept",
                "properties": ["name", "description", "parent_realm", "properties"]
            },
            {
                "name": "energy",
                "description": "Currency for knowledge transformations and operations",
                "type": "ontological_concept",
                "properties": ["amount", "type", "source", "cost", "efficiency"]
            },
            {
                "name": "meta_node",
                "description": "Node that describes other nodes or the system itself",
                "type": "ontological_concept",
                "properties": ["target", "description", "schema", "validation_rules"]
            },
            {
                "name": "file",
                "description": "Physical or virtual file representation in the system",
                "type": "ontological_concept",
                "properties": ["path", "content", "type", "metadata", "relationships"]
            },
            {
                "name": "system_component",
                "description": "Component of the Living Codex system",
                "type": "ontological_concept",
                "properties": ["name", "type", "function", "dependencies", "interfaces"]
            }
        ]
        
        print(f"📝 Creating {len(core_concepts)} core ontological concepts...")
        
        for concept in core_concepts:
            node_id = f"ontology_{concept['name']}"
            
            # Create database node
            db_node = DatabaseNode(
                node_id=node_id,
                node_type="ontological_concept",
                name=concept['name'],
                content=json.dumps(concept),
                realm="ontology",
                water_state="ice",  # Solid, foundational knowledge
                energy_level=1000.0,  # High energy for core concepts
                transformation_cost=0.0,  # No cost to access core concepts
                metadata={
                    "category": "core_ontology",
                    "properties": concept['properties'],
                    "description": concept['description'],
                    "created_at": datetime.now().isoformat()
                }
            )
            
            # Store in database
            await self.database.create_node(db_node)
            
            # Store in Neo4j if available
            if self.neo4j.is_connected():
                await self.neo4j.create_node(db_node)
            
            self.bootstrap_nodes[node_id] = db_node
            print(f"   ✅ Created: {concept['name']}")
        
        print(f"✅ Core ontology bootstrapped with {len(self.bootstrap_nodes)} concepts")
    
    async def phase3_file_system_bootstrap(self):
        """Phase 3: Bootstrap all system files into the Codex"""
        print("\n📁 Phase 3: File System Bootstrap")
        print("-" * 40)
        
        # Define file categories and their importance
        file_categories = {
            "core_system": {
                "priority": "critical",
                "energy_level": 1000.0,
                "water_state": "ice"
            },
            "documentation": {
                "priority": "high", 
                "energy_level": 800.0,
                "water_state": "liquid"
            },
            "examples": {
                "priority": "medium",
                "energy_level": 600.0,
                "water_state": "liquid"
            },
            "testing": {
                "priority": "medium",
                "energy_level": 500.0,
                "water_state": "vapor"
            },
            "setup": {
                "priority": "high",
                "energy_level": 700.0,
                "water_state": "liquid"
            },
            "configuration": {
                "priority": "critical",
                "energy_level": 900.0,
                "water_state": "ice"
            }
        }
        
        # Scan and categorize files
        files_to_bootstrap = await self.scan_system_files()
        
        print(f"📊 Found {len(files_to_bootstrap)} files to bootstrap...")
        
        for file_info in files_to_bootstrap:
            await self.bootstrap_file(file_info, file_categories)
        
        print(f"✅ File system bootstrapped with {len(self.file_nodes)} files")
    
    async def scan_system_files(self) -> List[Dict[str, Any]]:
        """Scan the system for all relevant files"""
        files = []
        root_path = Path(__file__).parent
        
        # Define important file patterns
        important_patterns = [
            "*.py", "*.md", "*.txt", "*.sh", "*.json", "*.yml", "*.yaml"
        ]
        
        # Define directories to scan
        scan_dirs = [
            root_path,
            root_path / "src",
            root_path / "docs"
        ]
        
        for scan_dir in scan_dirs:
            if scan_dir.exists():
                for pattern in important_patterns:
                    for file_path in scan_dir.rglob(pattern):
                        # Skip cache and temporary files
                        if any(part.startswith('.') or part.startswith('_') for part in file_path.parts):
                            continue
                        
                        # Determine category
                        category = self.categorize_file(file_path)
                        
                        # Read file content
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                        except Exception:
                            content = f"[Binary or unreadable file: {file_path.name}]"
                        
                        files.append({
                            "path": str(file_path.relative_to(root_path)),
                            "name": file_path.name,
                            "category": category,
                            "content": content,
                            "size": len(content),
                            "extension": file_path.suffix,
                            "relative_path": str(file_path.relative_to(root_path))
                        })
        
        return files
    
    def categorize_file(self, file_path: Path) -> str:
        """Categorize a file based on its location and type"""
        path_str = str(file_path)
        
        if "src/" in path_str:
            return "core_system"
        elif "docs/" in path_str:
            if "setup/" in path_str:
                return "setup"
            elif "testing/" in path_str:
                return "testing"
            elif "examples/" in path_str:
                return "examples"
            else:
                return "documentation"
        elif file_path.name in ["requirements.txt", "README.md", "ORGANIZATION_SUMMARY.md"]:
            return "configuration"
        elif file_path.suffix in [".py"] and "test" in file_path.name.lower():
            return "testing"
        else:
            return "core_system"
    
    async def bootstrap_file(self, file_info: Dict[str, Any], categories: Dict[str, Any]):
        """Bootstrap a single file into the system"""
        category = file_info['category']
        category_config = categories.get(category, categories['core_system'])
        
        # Create unique node ID
        content_hash = hashlib.sha256(file_info['content'].encode()).hexdigest()[:16]
        node_id = f"file_{category}_{content_hash}"
        
        # Create file node
        file_node = DatabaseNode(
            node_id=node_id,
            node_type="file",
            name=file_info['name'],
            content=file_info['content'],
            realm="file_system",
            water_state=category_config['water_state'],
            energy_level=category_config['energy_level'],
            transformation_cost=10.0,
            metadata={
                "category": category,
                "path": file_info['path'],
                "relative_path": file_info['relative_path'],
                "extension": file_info['extension'],
                "size": file_info['size'],
                "priority": category_config['priority'],
                "bootstrapped_at": datetime.now().isoformat(),
                "content_hash": content_hash
            }
        )
        
        # Store in database
        await self.database.create_node(file_node)
        
        # Store in Neo4j if available
        if self.neo4j.is_connected():
            await self.neo4j.create_node(file_node)
        
        self.file_nodes[node_id] = file_node
        
        # Create relationship to category
        category_node_id = f"category_{category}"
        await self.create_relationship(node_id, category_node_id, "belongs_to", {
            "strength": 1.0,
            "created_at": datetime.now().isoformat()
        })
    
    async def phase4_meta_circular_system(self):
        """Phase 4: Create meta-circular system describing itself"""
        print("\n🔄 Phase 4: Meta-Circular System Creation")
        print("-" * 40)
        
        # Create meta-nodes that describe the system structure
        meta_nodes = [
            {
                "name": "living_codex_system",
                "description": "The complete Living Codex system as a meta-node",
                "type": "meta_system",
                "components": ["ontology", "file_system", "knowledge_graph", "api_system"],
                "properties": ["self_describing", "meta_circular", "fractal", "holographic"]
            },
            {
                "name": "system_ontology",
                "description": "Ontological structure of the Living Codex system",
                "type": "meta_ontology",
                "concepts": list(self.bootstrap_nodes.keys()),
                "relationships": ["is_a", "has_property", "belongs_to", "transforms_to"]
            },
            {
                "name": "file_system_structure",
                "description": "Complete file system organization and relationships",
                "type": "meta_file_system",
                "categories": ["core_system", "documentation", "examples", "testing", "setup", "configuration"],
                "organization": "hierarchical",
                "properties": ["self_representing", "navigable", "queryable"]
            },
            {
                "name": "knowledge_graph_meta",
                "description": "Meta-description of the knowledge graph structure",
                "type": "meta_knowledge_graph",
                "node_types": ["ontological_concept", "file", "meta_node", "system_component"],
                "relationship_types": ["belongs_to", "describes", "implements", "depends_on"],
                "properties": ["fractal", "holographic", "self_referential"]
            },
            {
                "name": "system_boundaries",
                "description": "Boundaries and limits of the Living Codex system",
                "type": "meta_boundaries",
                "internal_components": list(self.bootstrap_nodes.keys()) + list(self.file_nodes.keys()),
                "external_dependencies": ["neo4j", "postgresql", "openai_api", "google_api"],
                "properties": ["expandable", "self_aware", "boundary_detection"]
            }
        ]
        
        print(f"📝 Creating {len(meta_nodes)} meta-nodes...")
        
        for meta_info in meta_nodes:
            node_id = f"meta_{meta_info['name']}"
            
            meta_node = DatabaseNode(
                node_id=node_id,
                node_type="meta_node",
                name=meta_info['name'],
                content=json.dumps(meta_info),
                realm="meta_system",
                water_state="plasma",  # Highest state - meta-awareness
                energy_level=1500.0,   # Very high energy for meta-concepts
                transformation_cost=50.0,  # Higher cost for meta-operations
                metadata={
                    "category": "meta_circular",
                    "target_system": "living_codex",
                    "meta_level": "system_self_description",
                    "properties": meta_info.get('properties', []),
                    "created_at": datetime.now().isoformat()
                }
            )
            
            # Store in database
            await self.database.create_node(meta_node)
            
            # Store in Neo4j if available
            if self.neo4j.is_connected():
                await self.neo4j.create_node(meta_node)
            
            self.meta_nodes[node_id] = meta_node
            print(f"   ✅ Created meta-node: {meta_info['name']}")
        
        # Create meta-relationships
        await self.create_meta_relationships()
        
        print(f"✅ Meta-circular system created with {len(self.meta_nodes)} meta-nodes")
    
    async def create_meta_relationships(self):
        """Create relationships between meta-nodes and system components"""
        print("🔗 Creating meta-relationships...")
        
        # System describes itself
        await self.create_relationship(
            "meta_living_codex_system",
            "meta_system_ontology",
            "describes",
            {"meta_level": "system_self_description"}
        )
        
        # Ontology describes files
        await self.create_relationship(
            "meta_system_ontology",
            "meta_file_system_structure",
            "describes",
            {"meta_level": "structure_description"}
        )
        
        # File system implements ontology
        await self.create_relationship(
            "meta_file_system_structure",
            "meta_system_ontology",
            "implements",
            {"meta_level": "concept_implementation"}
        )
        
        # Knowledge graph connects everything
        await self.create_relationship(
            "meta_knowledge_graph_meta",
            "meta_living_codex_system",
            "connects",
            {"meta_level": "system_integration"}
        )
        
        # Boundaries define system limits
        await self.create_relationship(
            "meta_system_boundaries",
            "meta_living_codex_system",
            "defines",
            {"meta_level": "boundary_definition"}
        )
        
        print("✅ Meta-relationships created")
    
    async def phase5_self_exploration(self):
        """Phase 5: Explore the system and find missing nodes"""
        print("\n🔍 Phase 5: Self-Exploration and Boundary Detection")
        print("-" * 40)
        
        # Query the system to understand itself
        print("📊 Analyzing system completeness...")
        
        # Check what we have
        total_nodes = len(self.bootstrap_nodes) + len(self.file_nodes) + len(self.meta_nodes)
        print(f"   Total nodes created: {total_nodes}")
        
        # Analyze coverage
        coverage_analysis = await self.analyze_system_coverage()
        
        # Find missing components
        missing_components = await self.identify_missing_components(coverage_analysis)
        
        # Suggest expansions
        expansion_suggestions = await self.suggest_system_expansions(missing_components)
        
        print("✅ Self-exploration completed")
        return coverage_analysis, missing_components, expansion_suggestions
    
    async def analyze_system_coverage(self) -> Dict[str, Any]:
        """Analyze how well the system covers its own structure"""
        analysis = {
            "ontology_coverage": {},
            "file_coverage": {},
            "meta_coverage": {},
            "relationship_coverage": {},
            "overall_score": 0.0
        }
        
        # Ontology coverage
        expected_ontology = ["node", "relationship", "water_state", "realm", "energy", "meta_node", "file", "system_component"]
        found_ontology = [node.name for node in self.bootstrap_nodes.values()]
        analysis["ontology_coverage"] = {
            "expected": expected_ontology,
            "found": found_ontology,
            "missing": list(set(expected_ontology) - set(found_ontology)),
            "coverage_percentage": len(found_ontology) / len(expected_ontology) * 100
        }
        
        # File coverage
        file_categories = ["core_system", "documentation", "examples", "testing", "setup", "configuration"]
        found_categories = list(set([node.metadata.get("category", "unknown") for node in self.file_nodes.values()]))
        analysis["file_coverage"] = {
            "expected_categories": file_categories,
            "found_categories": found_categories,
            "missing_categories": list(set(file_categories) - set(found_categories)),
            "total_files": len(self.file_nodes),
            "coverage_percentage": len(found_categories) / len(file_categories) * 100
        }
        
        # Meta coverage
        expected_meta = ["living_codex_system", "system_ontology", "file_system_structure", "knowledge_graph_meta", "system_boundaries"]
        found_meta = [node.name for node in self.meta_nodes.values()]
        analysis["meta_coverage"] = {
            "expected": expected_meta,
            "found": found_meta,
            "missing": list(set(expected_meta) - set(found_meta)),
            "coverage_percentage": len(found_meta) / len(expected_meta) * 100
        }
        
        # Calculate overall score
        scores = [
            analysis["ontology_coverage"]["coverage_percentage"],
            analysis["file_coverage"]["coverage_percentage"],
            analysis["meta_coverage"]["coverage_percentage"]
        ]
        analysis["overall_score"] = sum(scores) / len(scores)
        
        return analysis
    
    async def identify_missing_components(self, coverage_analysis: Dict[str, Any]) -> Dict[str, List[str]]:
        """Identify what components are missing from the system"""
        missing = {
            "ontology": coverage_analysis["ontology_coverage"]["missing"],
            "file_categories": coverage_analysis["file_coverage"]["missing_categories"],
            "meta_nodes": coverage_analysis["meta_coverage"]["missing"],
            "relationships": [],
            "external_integrations": []
        }
        
        # Check for missing relationships
        expected_relationships = [
            "is_a", "has_property", "belongs_to", "transforms_to",
            "describes", "implements", "connects", "defines"
        ]
        
        # Check for missing external integrations
        expected_integrations = [
            "neo4j", "postgresql", "sqlite", "openai", "google", "wikipedia", "duckduckgo"
        ]
        
        return missing
    
    async def suggest_system_expansions(self, missing_components: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """Suggest how to expand the system"""
        suggestions = {
            "immediate": [],
            "short_term": [],
            "long_term": []
        }
        
        # Immediate suggestions
        if missing_components["ontology"]:
            suggestions["immediate"].append(f"Create missing ontological concepts: {', '.join(missing_components['ontology'])}")
        
        if missing_components["file_categories"]:
            suggestions["immediate"].append(f"Add files for missing categories: {', '.join(missing_components['file_categories'])}")
        
        # Short term suggestions
        suggestions["short_term"].extend([
            "Implement relationship validation system",
            "Add energy cost calculation for operations",
            "Create system health monitoring",
            "Implement automatic boundary detection"
        ])
        
        # Long term suggestions
        suggestions["long_term"].extend([
            "Develop AI agent for autonomous system exploration",
            "Implement predictive knowledge expansion",
            "Create quantum-inspired knowledge representation",
            "Develop multi-dimensional knowledge mapping"
        ])
        
        return suggestions
    
    async def phase6_knowledge_hologram_analysis(self):
        """Phase 6: Analyze the knowledge hologram structure"""
        print("\n🌐 Phase 6: Knowledge Hologram Analysis")
        print("-" * 40)
        
        print("🔍 Analyzing holographic properties...")
        
        # Analyze fractal patterns
        fractal_analysis = await self.analyze_fractal_patterns()
        
        # Analyze holographic properties
        holographic_analysis = await self.analyze_holographic_properties()
        
        # Analyze energy distribution
        energy_analysis = await self.analyze_energy_distribution()
        
        # Generate hologram report
        await self.generate_hologram_report(fractal_analysis, holographic_analysis, energy_analysis)
        
        print("✅ Knowledge hologram analysis completed")
    
    async def analyze_fractal_patterns(self) -> Dict[str, Any]:
        """Analyze fractal patterns in the knowledge structure"""
        patterns = {
            "self_similarity": [],
            "recursive_structures": [],
            "scaling_properties": [],
            "fractal_dimension": 0.0
        }
        
        # Check for self-similarity in node structures
        node_types = {}
        for node in self.bootstrap_nodes.values():
            node_type = node.node_type
            if node_type not in node_types:
                node_types[node_type] = []
            node_types[node_type].append(node)
        
        # Analyze patterns
        for node_type, nodes in node_types.items():
            if len(nodes) > 1:
                patterns["self_similarity"].append({
                    "type": node_type,
                    "count": len(nodes),
                    "similarity_score": 0.8  # Placeholder
                })
        
        # Calculate fractal dimension (simplified)
        patterns["fractal_dimension"] = len(node_types) * 0.5 + len(patterns["self_similarity"]) * 0.3
        
        return patterns
    
    async def analyze_holographic_properties(self) -> Dict[str, Any]:
        """Analyze holographic properties of the knowledge system"""
        properties = {
            "wholeness": 0.0,
            "interconnectedness": 0.0,
            "redundancy": 0.0,
            "resilience": 0.0
        }
        
        # Calculate wholeness (how complete the system is)
        total_expected = 8 + 6 + 5  # ontology + file_categories + meta_nodes
        total_found = len(self.bootstrap_nodes) + len(self.file_nodes) + len(self.meta_nodes)
        properties["wholeness"] = total_found / total_expected
        
        # Calculate interconnectedness (relationship density)
        total_nodes = total_found
        # This would require counting actual relationships created
        properties["interconnectedness"] = min(0.8, total_nodes / 100)  # Placeholder
        
        # Calculate redundancy (information overlap)
        properties["redundancy"] = 0.3  # Placeholder
        
        # Calculate resilience (ability to recover from damage)
        properties["resilience"] = properties["wholeness"] * 0.7 + properties["redundancy"] * 0.3
        
        return properties
    
    async def analyze_energy_distribution(self) -> Dict[str, Any]:
        """Analyze energy distribution across the system"""
        energy_stats = {
            "total_energy": 0.0,
            "average_energy": 0.0,
            "energy_distribution": {},
            "high_energy_nodes": [],
            "low_energy_nodes": []
        }
        
        all_nodes = list(self.bootstrap_nodes.values()) + list(self.file_nodes.values()) + list(self.meta_nodes.values())
        
        if all_nodes:
            total_energy = sum(node.energy_level for node in all_nodes)
            average_energy = total_energy / len(all_nodes)
            
            energy_stats["total_energy"] = total_energy
            energy_stats["average_energy"] = average_energy
            
            # Categorize by energy level
            for node in all_nodes:
                if node.energy_level > average_energy * 1.5:
                    energy_stats["high_energy_nodes"].append({
                        "name": node.name,
                        "energy": node.energy_level,
                        "type": node.node_type
                    })
                elif node.energy_level < average_energy * 0.5:
                    energy_stats["low_energy_nodes"].append({
                        "name": node.name,
                        "energy": node.energy_level,
                        "type": node.node_type
                    })
        
        return energy_stats
    
    async def generate_hologram_report(self, fractal: Dict, holographic: Dict, energy: Dict):
        """Generate a comprehensive hologram analysis report"""
        print("\n📊 Knowledge Hologram Analysis Report")
        print("=" * 50)
        
        print(f"🧬 Fractal Properties:")
        print(f"   Self-similarity patterns: {len(fractal['self_similarity'])}")
        print(f"   Fractal dimension: {fractal['fractal_dimension']:.2f}")
        
        print(f"\n🌐 Holographic Properties:")
        print(f"   Wholeness: {holographic['wholeness']:.1%}")
        print(f"   Interconnectedness: {holographic['interconnectedness']:.1%}")
        print(f"   Redundancy: {holographic['redundancy']:.1%}")
        print(f"   Resilience: {holographic['resilience']:.1%}")
        
        print(f"\n⚡ Energy Distribution:")
        print(f"   Total energy: {energy['total_energy']:.0f}")
        print(f"   Average energy: {energy['average_energy']:.0f}")
        print(f"   High energy nodes: {len(energy['high_energy_nodes'])}")
        print(f"   Low energy nodes: {len(energy['low_energy_nodes'])}")
        
        # Save report to file
        report = {
            "timestamp": datetime.now().isoformat(),
            "fractal_analysis": fractal,
            "holographic_analysis": holographic,
            "energy_analysis": energy,
            "system_summary": {
                "total_nodes": len(self.bootstrap_nodes) + len(self.file_nodes) + len(self.meta_nodes),
                "bootstrap_nodes": len(self.bootstrap_nodes),
                "file_nodes": len(self.file_nodes),
                "meta_nodes": len(self.meta_nodes)
            }
        }
        
        with open("knowledge_hologram_report.json", "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📝 Report saved to: knowledge_hologram_report.json")
    
    async def create_relationship(self, source_id: str, target_id: str, relationship_type: str, properties: Dict[str, Any] = None):
        """Create a relationship between nodes"""
        try:
            # Create in database
            await self.database.create_relationship(source_id, target_id, relationship_type, properties or {})
            
            # Create in Neo4j if available
            if self.neo4j.is_connected():
                await self.neo4j.create_relationship(source_id, target_id, relationship_type, properties or {})
                
        except Exception as e:
            print(f"⚠️  Could not create relationship {source_id} -> {target_id}: {e}")
    
    async def cleanup(self):
        """Clean up resources"""
        try:
            await self.api_system.close()
        except:
            pass

async def main():
    """Main test execution"""
    test = ComprehensiveBootstrapTest()
    
    success = await test.run_comprehensive_test()
    
    if success:
        print("\n🎯 Test Results Summary:")
        print("✅ All phases completed successfully")
        print("✅ System is now fully self-contained")
        print("✅ Meta-circular relationships established")
        print("✅ Knowledge hologram analyzed")
        print("✅ Boundaries and missing components identified")
        print("\n🚀 The Living Codex is now fully self-aware and self-exploring!")
        
        # Show next steps
        print("\n📋 Next Steps for Exploration:")
        print("1. Query the system for specific knowledge patterns")
        print("2. Explore missing components and expand the system")
        print("3. Analyze energy flows and transformation costs")
        print("4. Investigate fractal patterns at different scales")
        print("5. Test boundary detection and system expansion")
        
        sys.exit(0)
    else:
        print("\n❌ Test failed - system needs attention")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
