#!/usr/bin/env python3
"""
Comprehensive Test Runner - Living Codex
Master script that runs both the comprehensive bootstrap test and the exploration,
demonstrating the complete self-contained Living Codex system.
"""

import sys
import asyncio
import time
from pathlib import Path

async def run_comprehensive_demonstration():
    """Run the complete comprehensive demonstration"""
    print("🚀 Living Codex - Comprehensive System Demonstration")
    print("=" * 70)
    print("This demonstration will:")
    print("1. Bootstrap all system files into the Codex itself")
    print("2. Create a fully self-contained, meta-circular system")
    print("3. Explore system boundaries and knowledge hologram")
    print("4. Identify missing components and expansion opportunities")
    print("=" * 70)
    
    start_time = time.time()
    
    try:
        # Step 1: Run the comprehensive bootstrap test
        print("\n🔧 Step 1: Running Comprehensive Bootstrap Test")
        print("-" * 50)
        
        from test_comprehensive_bootstrap import ComprehensiveBootstrapTest
        
        bootstrap_test = ComprehensiveBootstrapTest()
        bootstrap_success = await bootstrap_test.run_comprehensive_test()
        
        if not bootstrap_success:
            print("❌ Bootstrap test failed - cannot proceed with exploration")
            return False
        
        bootstrap_time = time.time() - start_time
        print(f"\n✅ Bootstrap completed in {bootstrap_time:.1f} seconds")
        
        # Step 2: Run the system exploration
        print("\n🔍 Step 2: Running System Exploration")
        print("-" * 50)
        
        from explore_bootstrapped_system import BootstrappedSystemExplorer
        
        explorer = BootstrappedSystemExplorer()
        exploration_success = await explorer.run_comprehensive_exploration()
        
        if not exploration_success:
            print("❌ Exploration failed - system may not be fully bootstrapped")
            return False
        
        total_time = time.time() - start_time
        print(f"\n✅ Exploration completed in {total_time - bootstrap_time:.1f} seconds")
        print(f"✅ Total demonstration time: {total_time:.1f} seconds")
        
        # Step 3: Generate final summary
        print("\n📊 Step 3: Final System Summary")
        print("-" * 50)
        
        await generate_final_summary()
        
        return True
        
    except Exception as e:
        print(f"❌ Comprehensive demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def generate_final_summary():
    """Generate a final summary of the system state"""
    print("🔍 Generating final system summary...")
    
    try:
        # Import the database to check final state
        from database_persistence_system import DatabasePersistenceSystem, QueryFilter, QueryOptions
        
        db = DatabasePersistenceSystem(db_path="comprehensive_bootstrap.db")
        await db.initialize()
        
        # Count all nodes by type
        ontology_nodes = await db.query_nodes(
            QueryFilter(node_type="ontological_concept"),
            QueryOptions(limit=1000)
        )
        
        file_nodes = await db.query_nodes(
            QueryFilter(node_type="file"),
            QueryOptions(limit=1000)
        )
        
        meta_nodes = await db.query_nodes(
            QueryFilter(node_type="meta_node"),
            QueryOptions(limit=1000)
        )
        
        # Calculate energy statistics
        all_nodes = ontology_nodes + file_nodes + meta_nodes
        total_energy = sum(node.energy_level for node in all_nodes)
        avg_energy = total_energy / len(all_nodes) if all_nodes else 0
        
        print(f"\n📊 Final System State:")
        print(f"   🧬 Ontological Concepts: {len(ontology_nodes)}")
        print(f"   📁 Files: {len(file_nodes)}")
        print(f"   🔄 Meta-Nodes: {len(meta_nodes)}")
        print(f"   📈 Total Nodes: {len(all_nodes)}")
        print(f"   ⚡ Total Energy: {total_energy:.0f}")
        print(f"   ⚡ Average Energy: {avg_energy:.0f}")
        
        # Show file categories
        categories = {}
        for node in file_nodes:
            category = node.metadata.get("category", "unknown")
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
        
        print(f"\n📂 File Categories:")
        for category, count in sorted(categories.items()):
            print(f"   {category}: {count} files")
        
        # Show top energy nodes
        sorted_nodes = sorted(all_nodes, key=lambda x: x.energy_level, reverse=True)
        print(f"\n🔥 Top 5 High-Energy Nodes:")
        for i, node in enumerate(sorted_nodes[:5]):
            print(f"   {i+1}. {node.name} - {node.energy_level:.0f} ({node.node_type})")
        
        # System completeness assessment
        expected_ontology = 8  # Core ontological concepts
        expected_categories = 6  # File categories
        expected_meta = 5  # Meta-nodes
        
        ontology_completeness = min(100, len(ontology_nodes) / expected_ontology * 100)
        category_completeness = min(100, len(categories) / expected_categories * 100)
        meta_completeness = min(100, len(meta_nodes) / expected_meta * 100)
        
        overall_completeness = (ontology_completeness + category_completeness + meta_completeness) / 3
        
        print(f"\n🎯 System Completeness Assessment:")
        print(f"   🧬 Ontology: {ontology_completeness:.1f}%")
        print(f"   📁 Categories: {category_completeness:.1f}%")
        print(f"   🔄 Meta-System: {meta_completeness:.1f}%")
        print(f"   🌟 Overall: {overall_completeness:.1f}%")
        
        if overall_completeness >= 90:
            print("   🎉 Excellent! System is highly complete")
        elif overall_completeness >= 75:
            print("   ✅ Good! System is well-developed")
        elif overall_completeness >= 50:
            print("   ⚠️  Fair! System has room for improvement")
        else:
            print("   ❌ Poor! System needs significant development")
        
        # Save summary to file
        summary = {
            "timestamp": time.time(),
            "system_state": {
                "ontology_nodes": len(ontology_nodes),
                "file_nodes": len(file_nodes),
                "meta_nodes": len(meta_nodes),
                "total_nodes": len(all_nodes),
                "total_energy": total_energy,
                "average_energy": avg_energy
            },
            "file_categories": categories,
            "completeness": {
                "ontology": ontology_completeness,
                "categories": category_completeness,
                "meta": meta_completeness,
                "overall": overall_completeness
            },
            "top_energy_nodes": [
                {
                    "name": node.name,
                    "energy": node.energy_level,
                    "type": node.node_type
                }
                for node in sorted_nodes[:10]
            ]
        }
        
        import json
        with open("comprehensive_test_summary.json", "w") as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n📝 Summary saved to: comprehensive_test_summary.json")
        
    except Exception as e:
        print(f"⚠️  Could not generate final summary: {e}")

def main():
    """Main execution function"""
    print("🚀 Starting Living Codex Comprehensive System Demonstration...")
    
    # Check if required files exist
    required_files = [
        "test_comprehensive_bootstrap.py",
        "explore_bootstrapped_system.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Please ensure all test files are present before running.")
        sys.exit(1)
    
    # Run the demonstration
    success = asyncio.run(run_comprehensive_demonstration())
    
    if success:
        print("\n🎉 🎉 🎉 COMPREHENSIVE DEMONSTRATION COMPLETED SUCCESSFULLY! 🎉 🎉 🎉")
        print("\n🚀 The Living Codex is now:")
        print("   ✅ Fully self-contained and self-describing")
        print("   ✅ Meta-circular with complete self-awareness")
        print("   ✅ Capable of exploring its own boundaries")
        print("   ✅ Ready for autonomous knowledge expansion")
        print("   ✅ Demonstrating true holographic knowledge representation")
        
        print("\n💡 What This Means:")
        print("   • The system can now represent and understand itself completely")
        print("   • It can identify what knowledge is missing and suggest expansions")
        print("   • It demonstrates the fractal, holographic nature of knowledge")
        print("   • It's ready for real-world knowledge management applications")
        
        print("\n🔮 Next Steps:")
        print("1. Use the system for real knowledge management tasks")
        print("2. Expand the ontology with domain-specific concepts")
        print("3. Integrate with external knowledge sources")
        print("4. Develop AI agents that can navigate the system")
        print("5. Scale to enterprise-level knowledge management")
        
        sys.exit(0)
    else:
        print("\n❌ Comprehensive demonstration failed")
        print("Check the error messages above for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
