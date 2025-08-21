#!/usr/bin/env python3
"""
Enhanced API Demo
Demonstrates the comprehensive navigation and modification capabilities
for all knowledge and meta-knowledge in the fractal node system.
"""

import asyncio
import json
from enhanced_fractal_api import EnhancedFractalAPI, NodeCreate, NodeUpdate, QueryRequest, NavigationRequest, EvolutionRequest

class EnhancedAPIDemo:
    """Demonstrates the enhanced fractal API capabilities"""
    
    def __init__(self):
        self.api = EnhancedFractalAPI("fractal_system.db")
        print("🌟 Enhanced Fractal API Demo")
        print("=" * 60)
    
    async def run_comprehensive_demo(self):
        """Run the complete enhanced API demonstration"""
        
        print("\n🔧 Initializing Enhanced Fractal API...")
        
        # 1. System Overview
        await self._demonstrate_system_overview()
        
        # 2. Core Node Operations
        await self._demonstrate_core_node_operations()
        
        # 3. Knowledge Navigation
        await self._demonstrate_knowledge_navigation()
        
        # 4. Knowledge Querying
        await self._demonstrate_knowledge_querying()
        
        # 5. Meta-Knowledge Operations
        await self._demonstrate_meta_knowledge_operations()
        
        # 6. Fractal Exploration
        await self._demonstrate_fractal_exploration()
        
        # 7. Graph Integration
        await self._demonstrate_graph_integration()
        
        # 8. System Optimization
        await self._demonstrate_system_optimization()
        
        print("\n" + "=" * 60)
        print("🎉 Enhanced API Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Comprehensive system overview and statistics")
        print("   • Full CRUD operations on fractal nodes")
        print("   • Advanced knowledge navigation and exploration")
        print("   • Natural language querying capabilities")
        print("   • Meta-knowledge evolution through curiosity")
        print("   • Multi-depth fractal structure exploration")
        print("   • Graph integration status and capabilities")
        print("   • System optimization and performance tuning")
        print("\n🚀 The Enhanced Fractal API is ready for production use!")
    
    async def _demonstrate_system_overview(self):
        """Demonstrate system overview capabilities"""
        
        print("\n📊 System Overview Demonstration")
        print("-" * 40)
        
        # Get system overview
        overview = await self.api._get_system_overview()
        print(f"   📈 Total Nodes: {overview.get('total_nodes', 'N/A')}")
        print(f"   🧭 Max Fractal Depth: {overview.get('max_fractal_depth', 'N/A')}")
        print(f"   🌐 System Status: {overview.get('system_status', 'N/A')}")
        
        if 'node_type_distribution' in overview:
            print(f"\n   📊 Node Type Distribution:")
            for node_type, count in list(overview['node_type_distribution'].items())[:10]:
                print(f"      • {node_type}: {count} nodes")
        
        # Get system statistics
        stats = await self.api._get_system_stats()
        print(f"\n   💾 Database Size: {stats.get('database_size', 'N/A')}")
        print(f"   🕒 Last Updated: {stats.get('last_updated', 'N/A')}")
        
        if 'metadata_analysis' in stats:
            print(f"\n   🔍 Metadata Analysis:")
            for key, analysis in list(stats['metadata_analysis'].items())[:5]:
                print(f"      • {key}: {analysis['count']} occurrences")
    
    async def _demonstrate_core_node_operations(self):
        """Demonstrate core node CRUD operations"""
        
        print("\n🔧 Core Node Operations Demonstration")
        print("-" * 40)
        
        # Create a new node
        print("   🔧 Creating a new demonstration node...")
        new_node = NodeCreate(
            node_type="demo_node",
            name="Enhanced API Demo Node",
            content="This node demonstrates the enhanced API capabilities for comprehensive knowledge management",
            parent_id="fractal_system_root",
            metadata={
                "demo_type": "enhanced_api",
                "creation_method": "api_demo",
                "frequency": 528.0,
                "chakra": "solar_plexus",
                "water_state": "crystalline"
            },
            structure_info={
                "fractal_depth": 2,
                "node_type": "demo",
                "parent_system": "fractal_system_root"
            }
        )
        
        create_result = await self.api._create_node(new_node)
        if create_result["status"] == "success":
            demo_node_id = create_result["node_id"]
            print(f"      ✅ Node created with ID: {demo_node_id}")
            
            # Get the created node
            print("   📖 Retrieving the created node...")
            retrieved_node = await self.api._get_node(demo_node_id)
            print(f"      ✅ Retrieved: {retrieved_node['name']}")
            print(f"      📝 Content: {retrieved_node['content'][:80]}...")
            
            # Update the node
            print("   ✏️  Updating the node...")
            update_data = NodeUpdate(
                content="This node has been updated to demonstrate the enhanced API's modification capabilities",
                metadata={
                    "demo_type": "enhanced_api",
                    "creation_method": "api_demo",
                    "update_method": "api_demo",
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "water_state": "crystalline",
                    "updated_at": "demo_session"
                }
            )
            
            update_result = await self.api._update_node(demo_node_id, update_data)
            if update_result["status"] == "success":
                print("      ✅ Node updated successfully")
                
                # Verify the update
                updated_node = await self.api._get_node(demo_node_id)
                print(f"      📝 Updated content: {updated_node['content'][:80]}...")
            
            # Clean up - delete the demo node
            print("   🗑️  Cleaning up demo node...")
            delete_result = await self.api._delete_node(demo_node_id)
            if delete_result["status"] == "success":
                print("      ✅ Demo node deleted successfully")
        else:
            print("      ❌ Failed to create demo node")
    
    async def _demonstrate_knowledge_navigation(self):
        """Demonstrate knowledge navigation capabilities"""
        
        print("\n🧭 Knowledge Navigation Demonstration")
        print("-" * 40)
        
        # Navigate through the meta-implementation layer
        print("   🧭 Navigating through meta-implementation layer...")
        nav_request = NavigationRequest(
            node_id="meta_implementation_layer",
            depth=3,
            include_relationships=True
        )
        
        navigation_result = await self.api._navigate_knowledge(nav_request)
        
        if "current_node" in navigation_result:
            current = navigation_result["current_node"]
            print(f"      🎯 Current Node: {current['name']}")
            print(f"      📝 Content: {current['content'][:80]}...")
            
            if "navigation_path" in navigation_result:
                path = navigation_result["navigation_path"]
                print(f"      🛤️  Navigation Path: {len(path)} levels")
                for i, path_node in enumerate(path):
                    print(f"        {i+1}. {path_node['name']} ({path_node['node_type']})")
            
            if "related_nodes" in navigation_result:
                related = navigation_result["related_nodes"]
                print(f"      🔗 Related Nodes: {len(related)} found")
                for i, related_node in enumerate(related[:3]):
                    print(f"        {i+1}. {related_node['name']} (similarity: {related_node['similarity_score']:.2f})")
    
    async def _demonstrate_knowledge_querying(self):
        """Demonstrate knowledge querying capabilities"""
        
        print("\n🔍 Knowledge Querying Demonstration")
        print("-" * 40)
        
        # Query for meta-knowledge
        print("   🔍 Querying for meta-knowledge...")
        meta_query = QueryRequest(
            query="meta implementation",
            node_type=None,
            max_results=5,
            include_metadata=True
        )
        
        meta_results = await self.api._query_knowledge(meta_query)
        print(f"      📍 Meta-knowledge query results: {meta_results['total_found']} nodes found")
        
        if meta_results['results']:
            for i, result in enumerate(meta_results['results'][:3]):
                print(f"        {i+1}. {result['name']} ({result['node_type']})")
                print(f"           Content: {result['content'][:60]}...")
        
        # Query for graph-related knowledge
        print("\n   🔍 Querying for graph-related knowledge...")
        graph_query = QueryRequest(
            query="graph system",
            node_type=None,
            max_results=5,
            include_metadata=True
        )
        
        graph_results = await self.api._query_knowledge(graph_query)
        print(f"      📍 Graph knowledge query results: {graph_results['total_found']} nodes found")
        
        if graph_results['results']:
            for i, result in enumerate(graph_results['results'][:3]):
                print(f"        {i+1}. {result['name']} ({result['node_type']})")
                print(f"           Content: {result['content'][:60]}...")
    
    async def _demonstrate_meta_knowledge_operations(self):
        """Demonstrate meta-knowledge operations"""
        
        print("\n🧠 Meta-Knowledge Operations Demonstration")
        print("-" * 40)
        
        # Get meta-knowledge overview
        print("   📊 Getting meta-knowledge overview...")
        meta_overview = await self.api._get_meta_knowledge()
        
        if "meta_knowledge_types" in meta_overview:
            print(f"      📈 Total System Nodes: {meta_overview['total_system_nodes']}")
            print(f"      🧠 Meta-Knowledge Percentage: {meta_overview['meta_knowledge_percentage']:.1f}%")
            
            print(f"\n      📊 Meta-Knowledge Types:")
            for meta_type, count in meta_overview['meta_knowledge_types'].items():
                print(f"        • {meta_type}: {count} nodes")
        
        # Evolve meta-knowledge through curiosity
        print("\n   🚀 Evolving meta-knowledge through curiosity...")
        evolution_request = EvolutionRequest(
            curiosity_question="How do water states relate to fractal structure in the meta-implementation layer?",
            exploration_depth=3,
            generate_nodes=True
        )
        
        evolution_result = await self.api._evolve_meta_knowledge(evolution_request)
        
        if "new_insights" in evolution_result:
            insights = evolution_result["new_insights"]
            print(f"      💡 New Insights Generated: {len(insights)}")
            for i, insight in enumerate(insights):
                print(f"        {i+1}. {insight['type']}: {insight['content']}")
        
        if "generated_nodes" in evolution_result:
            generated = evolution_result["generated_nodes"]
            print(f"      🆕 New Nodes Generated: {len(generated)}")
            for i, node_info in enumerate(generated):
                print(f"        {i+1}. Node ID: {node_info['generated_node_id']}")
        
        if "evolution_path" in evolution_result:
            path = evolution_result["evolution_path"]
            print(f"      🛤️  Evolution Path:")
            print(f"        • Question Analysis: {path['question_analysis']['complexity']} concepts")
            print(f"        • Related Knowledge: {path['related_knowledge_count']} nodes")
            print(f"        • Insights Generated: {path['insights_generated']}")
            print(f"        • Nodes Generated: {path['nodes_generated']}")
    
    async def _demonstrate_fractal_exploration(self):
        """Demonstrate fractal exploration capabilities"""
        
        print("\n🌀 Fractal Exploration Demonstration")
        print("-" * 40)
        
        # Get fractal structure overview
        print("   🌀 Getting fractal structure overview...")
        fractal_structure = await self.api._get_fractal_structure()
        
        if "fractal_layers" in fractal_structure:
            print(f"      📊 Total Fractal Layers: {fractal_structure['total_layers']}")
            print(f"      🏗️  Structure Type: {fractal_structure['structure_type']}")
            
            print(f"\n      📊 Fractal Layer Analysis:")
            for depth, layer_info in fractal_structure['fractal_layers'].items():
                print(f"        • {depth}: {layer_info['count']} nodes, {len(layer_info['types'])} types")
        
        # Explore a specific node
        print("\n   🔍 Exploring meta-implementation layer...")
        exploration_result = await self.api._explore_node("meta_implementation_layer", 3)
        
        if "fractal_layers" in exploration_result:
            print(f"      📊 Exploration Results:")
            for depth, layer_info in exploration_result["fractal_layers"].items():
                print(f"        • {depth}: {layer_info['node_count']} nodes explored")
                if layer_info['nodes']:
                    for i, node in enumerate(layer_info['nodes'][:3]):
                        print(f"          {i+1}. {node['name']} ({node['node_type']})")
        
        # Explore fractal structure with custom request
        print("\n   🚀 Custom fractal exploration...")
        custom_exploration = {
            "root_id": "fractal_system_root",
            "max_depth": 4
        }
        
        custom_result = await self.api._explore_fractal(custom_exploration)
        
        if "fractal_layers" in custom_result:
            print(f"      📊 Custom Exploration Results:")
            for depth, layer_info in custom_result["fractal_layers"].items():
                print(f"        • {depth}: {layer_info['node_count']} nodes")
                print(f"          Total explored: {custom_result['total_nodes_explored']} nodes")
    
    async def _demonstrate_graph_integration(self):
        """Demonstrate graph integration capabilities"""
        
        print("\n🔗 Graph Integration Demonstration")
        print("-" * 40)
        
        # Get graph integration status
        print("   🔗 Getting graph integration status...")
        graph_status = await self.api._get_graph_integration()
        
        if "integration_status" in graph_status:
            print(f"      📊 Integration Status: {graph_status['integration_status']}")
            print(f"      📈 Total Graph Nodes: {graph_status['total_graph_nodes']}")
            
            if "graph_node_types" in graph_status:
                print(f"\n      📊 Graph Node Types:")
                for graph_type, count in graph_status['graph_node_types'].items():
                    print(f"        • {graph_type}: {count} nodes")
            
            if "capabilities" in graph_status:
                print(f"\n      🚀 Graph Capabilities:")
                for capability in graph_status['capabilities']:
                    print(f"        • {capability}")
        
        # Execute a graph query
        print("\n   🔍 Executing graph query...")
        graph_query = "MATCH (n:Node) WHERE n.waterState = 'Plasma' RETURN n"
        query_result = await self.api._execute_graph_query(graph_query)
        
        print(f"      📍 Query: {query_result['query']}")
        print(f"      📊 Status: {query_result['status']}")
        print(f"      💬 Message: {query_result['message']}")
    
    async def _demonstrate_system_optimization(self):
        """Demonstrate system optimization capabilities"""
        
        print("\n⚡ System Optimization Demonstration")
        print("-" * 40)
        
        # Optimize the system
        print("   ⚡ Optimizing system performance...")
        optimization_result = await self.api._optimize_system()
        
        if "status" in optimization_result:
            print(f"      📊 Status: {optimization_result['status']}")
            print(f"      💬 Message: {optimization_result['message']}")
            
            if "operations" in optimization_result:
                print(f"      🔧 Operations Performed:")
                for operation in optimization_result['operations']:
                    print(f"        • {operation}")
        else:
            print(f"      ❌ Optimization failed: {optimization_result.get('error', 'Unknown error')}")
        
        # Get updated system stats
        print("\n   📊 Getting updated system statistics...")
        updated_stats = await self.api._get_system_stats()
        
        if "database_size" in updated_stats:
            print(f"      💾 Database Size: {updated_stats['database_size']}")
        if "last_updated" in updated_stats:
            print(f"      🕒 Last Updated: {updated_stats['last_updated']}")

async def main():
    """Main function to run the enhanced API demo"""
    
    try:
        demo = EnhancedAPIDemo()
        await demo.run_comprehensive_demo()
    except Exception as e:
        print(f"❌ Error running enhanced API demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
