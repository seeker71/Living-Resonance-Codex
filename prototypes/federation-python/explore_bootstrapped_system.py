#!/usr/bin/env python3
"""
Explore Bootstrapped System - Living Codex
Demonstrates how to explore, query, and navigate the fully bootstrapped
self-contained Living Codex system.
"""

import sys
import json
import asyncio
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add src to path for modular components
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import our systems
from neo4j_integration_system import Neo4jIntegrationSystem
from database_persistence_system import DatabasePersistenceSystem, DatabaseType, DatabaseNode, QueryFilter, QueryOptions
from real_external_api_system import RealExternalAPISystem

class BootstrappedSystemExplorer:
    """Explorer for the fully bootstrapped Living Codex system"""
    
    def __init__(self):
        self.neo4j = Neo4jIntegrationSystem()
        self.database = DatabasePersistenceSystem(db_path="comprehensive_bootstrap.db")
        self.api_system = RealExternalAPISystem()
        
    async def initialize(self):
        """Initialize the explorer"""
        print("🔍 Living Codex - Bootstrapped System Explorer")
        print("=" * 60)
        
        # Initialize systems
        await self.database.initialize()
        
        try:
            await self.neo4j.initialize()
            print("✅ Neo4j connected")
        except Exception as e:
            print(f"⚠️  Neo4j not available: {e}")
            print("   Using database fallback")
        
        await self.api_system.initialize()
        print("✅ Explorer initialized")
    
    async def explore_system_boundaries(self):
        """Explore the boundaries of the knowledge hologram"""
        print("\n🌐 Exploring System Boundaries")
        print("-" * 40)
        
        # Query for meta-nodes that define boundaries
        boundary_nodes = await self.database.query_nodes(
            QueryFilter(node_type="meta_node", realm="meta_system"),
            QueryOptions(limit=100)
        )
        
        print(f"📊 Found {len(boundary_nodes)} boundary-defining meta-nodes")
        
        for node in boundary_nodes:
            print(f"\n🔍 {node.name}:")
            try:
                content = json.loads(node.content)
                if "properties" in content:
                    print(f"   Properties: {', '.join(content['properties'])}")
                if "external_dependencies" in content:
                    print(f"   External Dependencies: {', '.join(content['external_dependencies'])}")
            except:
                print(f"   Content: {node.content[:100]}...")
        
        return boundary_nodes
    
    async def analyze_knowledge_coverage(self):
        """Analyze what knowledge is covered and what's missing"""
        print("\n📊 Knowledge Coverage Analysis")
        print("-" * 40)
        
        # Get all nodes by type
        ontology_nodes = await self.database.query_nodes(
            QueryFilter(node_type="ontological_concept"),
            QueryOptions(limit=100)
        )
        
        file_nodes = await self.database.query_nodes(
            QueryFilter(node_type="file"),
            QueryOptions(limit=100)
        )
        
        meta_nodes = await self.database.query_nodes(
            QueryFilter(node_type="meta_node"),
            QueryOptions(limit=100)
        )
        
        print(f"🧬 Ontological Concepts: {len(ontology_nodes)}")
        print(f"📁 Files: {len(file_nodes)}")
        print(f"🔄 Meta-Nodes: {len(meta_nodes)}")
        
        # Analyze file categories
        categories = {}
        for node in file_nodes:
            category = node.metadata.get("category", "unknown")
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
        
        print(f"\n📂 File Categories:")
        for category, count in categories.items():
            print(f"   {category}: {count} files")
        
        # Analyze energy distribution
        total_energy = sum(node.energy_level for node in ontology_nodes + file_nodes + meta_nodes)
        avg_energy = total_energy / (len(ontology_nodes) + len(file_nodes) + len(meta_nodes)) if (len(ontology_nodes) + len(file_nodes) + len(meta_nodes)) > 0 else 0
        
        print(f"\n⚡ Energy Analysis:")
        print(f"   Total Energy: {total_energy:.0f}")
        print(f"   Average Energy: {avg_energy:.0f}")
        
        return {
            "ontology": ontology_nodes,
            "files": file_nodes,
            "meta": meta_nodes,
            "categories": categories,
            "total_energy": total_energy,
            "avg_energy": avg_energy
        }
    
    async def query_knowledge_patterns(self, pattern_type: str = "all"):
        """Query for specific knowledge patterns"""
        print(f"\n🔍 Querying Knowledge Patterns: {pattern_type}")
        print("-" * 40)
        
        patterns = {
            "fractal": "self_similar",
            "holographic": "interconnected",
            "meta_circular": "self_describing",
            "energy_flow": "high_energy"
        }
        
        if pattern_type == "all":
            for pattern_name, pattern_desc in patterns.items():
                await self.query_specific_pattern(pattern_name, pattern_desc)
        else:
            await self.query_specific_pattern(pattern_type, patterns.get(pattern_type, pattern_type))
    
    async def query_specific_pattern(self, pattern_name: str, pattern_desc: str):
        """Query for a specific knowledge pattern"""
        print(f"\n🔍 Pattern: {pattern_name} ({pattern_desc})")
        
        if pattern_name == "fractal":
            # Look for self-similar structures
            nodes = await self.database.query_nodes(
                QueryFilter(realm="ontology"),
                QueryOptions(limit=50)
            )
            
            # Group by type to find patterns
            type_groups = {}
            for node in nodes:
                node_type = node.node_type
                if node_type not in type_groups:
                    type_groups[node_type] = []
                type_groups[node_type].append(node)
            
            print(f"   Found {len(type_groups)} node types with self-similar patterns:")
            for node_type, group in type_groups.items():
                print(f"     {node_type}: {len(group)} instances")
        
        elif pattern_name == "holographic":
            # Look for highly interconnected nodes
            high_energy_nodes = await self.database.query_nodes(
                QueryFilter(energy_level_min=800.0),
                QueryOptions(limit=20)
            )
            
            print(f"   Found {len(high_energy_nodes)} high-energy interconnected nodes:")
            for node in high_energy_nodes[:5]:  # Show top 5
                print(f"     {node.name} (Energy: {node.energy_level:.0f})")
        
        elif pattern_name == "meta_circular":
            # Look for self-describing nodes
            meta_nodes = await self.database.query_nodes(
                QueryFilter(node_type="meta_node"),
                QueryOptions(limit=20)
            )
            
            print(f"   Found {len(meta_nodes)} meta-circular nodes:")
            for node in meta_nodes:
                print(f"     {node.name} - {node.metadata.get('meta_level', 'unknown')}")
        
        elif pattern_name == "energy_flow":
            # Analyze energy flow patterns
            all_nodes = await self.database.query_nodes(
                QueryFilter(),
                QueryOptions(limit=100)
            )
            
            # Sort by energy level
            sorted_nodes = sorted(all_nodes, key=lambda x: x.energy_level, reverse=True)
            
            print(f"   Top 10 high-energy nodes:")
            for i, node in enumerate(sorted_nodes[:10]):
                print(f"     {i+1}. {node.name} - {node.energy_level:.0f} ({node.node_type})")
    
    async def explore_missing_components(self):
        """Explore what components might be missing from the system"""
        print("\n🔍 Exploring Missing Components")
        print("-" * 40)
        
        # Check for expected but missing components
        expected_components = {
            "ontological_concepts": [
                "quantum_state", "consciousness", "evolution", "emergence", "complexity"
            ],
            "system_components": [
                "ai_agent", "learning_engine", "prediction_system", "optimization_engine"
            ],
            "external_integrations": [
                "quantum_computer", "blockchain", "iot_devices", "satellite_data"
            ]
        }
        
        missing_components = {}
        
        for category, components in expected_components.items():
            missing = []
            for component in components:
                # Check if component exists
                existing = await self.database.query_nodes(
                    QueryFilter(name=component),
                    QueryOptions(limit=1)
                )
                if not existing:
                    missing.append(component)
            
            if missing:
                missing_components[category] = missing
        
        if missing_components:
            print("❌ Missing components detected:")
            for category, missing in missing_components.items():
                print(f"   {category}: {', '.join(missing)}")
        else:
            print("✅ All expected components are present")
        
        return missing_components
    
    async def suggest_system_expansions(self, missing_components: Dict[str, List[str]]):
        """Suggest how to expand the system"""
        print("\n💡 System Expansion Suggestions")
        print("-" * 40)
        
        suggestions = {
            "immediate": [],
            "short_term": [],
            "long_term": []
        }
        
        # Immediate suggestions based on missing components
        for category, missing in missing_components.items():
            if category == "ontological_concepts":
                suggestions["immediate"].extend([
                    f"Create ontological concept: {concept}" for concept in missing
                ])
            elif category == "system_components":
                suggestions["immediate"].extend([
                    f"Implement system component: {component}" for component in missing
                ])
            elif category == "external_integrations":
                suggestions["short_term"].extend([
                    f"Integrate external system: {integration}" for integration in missing
                ])
        
        # General expansion suggestions
        suggestions["short_term"].extend([
            "Implement quantum-inspired knowledge representation",
            "Add consciousness simulation capabilities",
            "Create evolutionary learning algorithms",
            "Develop complexity analysis tools"
        ])
        
        suggestions["long_term"].extend([
            "Build quantum-classical hybrid system",
            "Implement multi-dimensional consciousness mapping",
            "Create universal knowledge synthesis engine",
            "Develop reality-simulation capabilities"
        ])
        
        # Display suggestions
        for timeframe, items in suggestions.items():
            if items:
                print(f"\n{timeframe.title()} ({len(items)} suggestions):")
                for item in items:
                    print(f"   • {item}")
        
        return suggestions
    
    async def demonstrate_boundary_navigation(self):
        """Demonstrate how to navigate the system boundaries"""
        print("\n🧭 Boundary Navigation Demonstration")
        print("-" * 40)
        
        # Show how to navigate from any node to system boundaries
        print("🔍 Navigation Patterns:")
        
        # Pattern 1: From specific concept to meta-description
        print("\n1. Concept → Meta-Description:")
        ontology_nodes = await self.database.query_nodes(
            QueryFilter(node_type="ontological_concept"),
            QueryOptions(limit=3)
        )
        
        for node in ontology_nodes:
            print(f"   {node.name} → meta_system_ontology (describes)")
        
        # Pattern 2: From file to category to system structure
        print("\n2. File → Category → System Structure:")
        file_nodes = await self.database.query_nodes(
            QueryFilter(node_type="file"),
            QueryOptions(limit=3)
        )
        
        for node in file_nodes:
            category = node.metadata.get("category", "unknown")
            print(f"   {node.name} → category_{category} → meta_file_system_structure")
        
        # Pattern 3: From meta-node to system boundaries
        print("\n3. Meta-Node → System Boundaries:")
        meta_nodes = await self.database.query_nodes(
            QueryFilter(node_type="meta_node"),
            QueryOptions(limit=3)
        )
        
        for node in meta_nodes:
            print(f"   {node.name} → meta_system_boundaries (defines limits)")
        
        print("\n✅ Boundary navigation patterns demonstrated")
    
    async def run_comprehensive_exploration(self):
        """Run the complete exploration"""
        try:
            await self.initialize()
            
            # Explore system boundaries
            boundaries = await self.explore_system_boundaries()
            
            # Analyze knowledge coverage
            coverage = await self.analyze_knowledge_coverage()
            
            # Query knowledge patterns
            await self.query_knowledge_patterns("all")
            
            # Explore missing components
            missing = await self.explore_missing_components()
            
            # Suggest expansions
            suggestions = await self.suggest_system_expansions(missing)
            
            # Demonstrate boundary navigation
            await self.demonstrate_boundary_navigation()
            
            print("\n🎉 Comprehensive Exploration Completed!")
            print("\n📋 Key Findings:")
            print(f"   • System has {coverage['total_energy']:.0f} total energy")
            print(f"   • {len(missing)} component categories have missing elements")
            print(f"   • {len(suggestions['immediate'])} immediate expansion opportunities")
            
            return True
            
        except Exception as e:
            print(f"❌ Exploration failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            await self.cleanup()
    
    async def cleanup(self):
        """Clean up resources"""
        try:
            await self.api_system.close()
        except:
            pass

async def main():
    """Main exploration execution"""
    explorer = BootstrappedSystemExplorer()
    
    success = await explorer.run_comprehensive_exploration()
    
    if success:
        print("\n🚀 The Living Codex system is fully explorable!")
        print("\n💡 Next Steps:")
        print("1. Run specific pattern queries")
        print("2. Explore missing components in detail")
        print("3. Implement suggested expansions")
        print("4. Test boundary navigation with custom queries")
        print("5. Analyze energy flows and transformation costs")
        
        sys.exit(0)
    else:
        print("\n❌ Exploration failed - check system status")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
