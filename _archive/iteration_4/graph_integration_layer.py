#!/usr/bin/env python3
"""
Graph Integration Layer
Integrates the graph prototype with our meta-implementation fractal node system
to create a unified, living knowledge architecture.
"""

import os
import sys
import json
import requests
from typing import List, Dict, Any, Optional
from pathlib import Path

# Add the graph prototype to the path
sys.path.append(str(Path(__file__).parent.parent / "graph"))

try:
    from api import app as graph_app
except ImportError:
    print("⚠️  Graph prototype not found, using mock graph operations")
    graph_app = None

class GraphIntegrationLayer:
    """Integrates the graph prototype into the fractal node system"""
    
    def __init__(self, fractal_system):
        self.fractal_system = fractal_system
        self.graph_api_url = "http://localhost:8000"  # Graph API endpoint
        self.seed_data = self._load_seed_data()
        self._bootstrap_graph_system()
    
    def _load_seed_data(self) -> Dict[str, Any]:
        """Load seed data from the ontology directory"""
        try:
            seed_path = Path(__file__).parent.parent.parent / "ontology" / "seed.json"
            if seed_path.exists():
                with open(seed_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                print("⚠️  Seed data not found, using empty data")
                return {"@graph": [], "axes": []}
        except Exception as e:
            print(f"⚠️  Error loading seed data: {e}")
            return {"@graph": [], "axes": []}
    
    def _bootstrap_graph_system(self):
        """Bootstrap the graph system as fractal nodes"""
        
        print("🔧 Bootstrapping Graph Integration Layer...")
        
        # Create graph system node
        graph_system = self.fractal_system._create_generic_node(
            node_id="graph_system",
            node_type="graph_system",
            name="Living Codex Graph System",
            content="Neo4j-based graph database system for ontological exploration",
            parent_id="living_codex_specification",
            children=[],
            metadata={
                "system_type": "graph_database",
                "database": "neo4j",
                "api_framework": "fastapi",
                "frequency": 741.0,
                "chakra": "throat",
                "water_state": "structured_hexagonal",
                "seed_nodes_count": len(self.seed_data.get("@graph", [])),
                "axes_count": len(self.seed_data.get("axes", []))
            },
            structure_info={
                "fractal_depth": 3,
                "system_type": "graph_integration",
                "parent_document": "living_codex_specification"
            }
        )
        
        # Add to codex specification's children
        self.fractal_system._add_child_to_parent("living_codex_specification", "graph_system")
        
        # Create graph components as nodes
        self._create_graph_components()
        
        # Create graph operations as nodes
        self._create_graph_operations()
        
        # Bootstrap seed data as fractal nodes
        self._bootstrap_seed_data_as_nodes()
        
        print("✅ Graph Integration Layer bootstrapped successfully!")
    
    def _create_graph_components(self):
        """Create graph system components as fractal nodes"""
        
        components = {
            "neo4j_database": {
                "name": "Neo4j Graph Database",
                "content": "Native graph database for storing and querying ontological relationships",
                "metadata": {
                    "component_type": "database",
                    "technology": "neo4j",
                    "query_language": "cypher",
                    "frequency": 852.0,
                    "chakra": "third_eye",
                    "water_state": "vapor"
                }
            },
            "graph_api": {
                "name": "Graph API Server",
                "content": "FastAPI-based REST server for graph operations and exploration",
                "metadata": {
                    "component_type": "api_server",
                    "framework": "fastapi",
                    "protocol": "rest",
                    "frequency": 639.0,
                    "chakra": "heart",
                    "water_state": "liquid"
                }
            },
            "seed_data_loader": {
                "name": "Seed Data Loader",
                "content": "JSON-LD based ontology loader with fallback capabilities",
                "metadata": {
                    "component_type": "data_loader",
                    "format": "json_ld",
                    "fallback": "enabled",
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "water_state": "crystalline"
                }
            },
            "graph_schema": {
                "name": "Graph Schema",
                "content": "Ontological schema defining node types, relationships, and correspondences",
                "metadata": {
                    "component_type": "schema",
                    "schema_type": "ontology",
                    "extensible": "true",
                    "frequency": 741.0,
                    "chakra": "throat",
                    "water_state": "structured_hexagonal"
                }
            }
        }
        
        for comp_id, comp_data in components.items():
            component_node = self.fractal_system._create_generic_node(
                node_id=f"graph_comp_{comp_id}",
                node_type="graph_component",
                name=comp_data["name"],
                content=comp_data["content"],
                parent_id="graph_system",
                children=[],
                metadata=comp_data["metadata"],
                structure_info={
                    "fractal_depth": 4,
                    "component_type": "graph_integration",
                    "parent_system": "graph_system"
                }
            )
            
            # Add to graph system's children
            self.fractal_system._add_child_to_parent("graph_system", f"graph_comp_{comp_id}")
    
    def _create_graph_operations(self):
        """Create graph operations as fractal nodes"""
        
        operations = {
            "graph_query": {
                "name": "Graph Query Operations",
                "content": "Cypher queries and graph traversal operations for exploring ontological relationships",
                "metadata": {
                    "operation_type": "graph_query",
                    "query_language": "cypher",
                    "frequency": 639.0,
                    "chakra": "heart",
                    "water_state": "liquid"
                }
            },
            "relationship_discovery": {
                "name": "Relationship Discovery",
                "content": "Automatic discovery of graph relationships and ontological patterns",
                "metadata": {
                    "operation_type": "pattern_discovery",
                    "discovery_type": "automatic",
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "water_state": "crystalline"
                }
            },
            "graph_analytics": {
                "name": "Graph Analytics",
                "content": "Analysis of graph structure, patterns, and ontological insights",
                "metadata": {
                    "operation_type": "analytics",
                    "analysis_type": "structural",
                    "frequency": 417.0,
                    "chakra": "sacral",
                    "water_state": "quantum_coherent"
                }
            },
            "pattern_recognition": {
                "name": "Pattern Recognition",
                "content": "Recognition of recurring patterns and structures in the ontological graph",
                "metadata": {
                    "operation_type": "pattern_recognition",
                    "recognition_type": "structural",
                    "frequency": 396.0,
                    "chakra": "root",
                    "water_state": "supercritical"
                }
            }
        }
        
        for op_id, op_data in operations.items():
            operation_node = self.fractal_system._create_generic_node(
                node_id=f"graph_op_{op_id}",
                node_type="graph_operation",
                name=op_data["name"],
                content=op_data["content"],
                parent_id="graph_system",
                children=[],
                metadata=op_data["metadata"],
                structure_info={
                    "fractal_depth": 4,
                    "operation_type": "graph_integration",
                    "parent_system": "graph_system"
                }
            )
            
            # Add to graph system's children
            self.fractal_system._add_child_to_parent("graph_system", f"graph_op_{op_id}")
    
    def _bootstrap_seed_data_as_nodes(self):
        """Bootstrap seed data from the graph prototype as fractal nodes"""
        
        print("   🔧 Bootstrapping seed data as fractal nodes...")
        
        # Create seed ontology section if it doesn't exist
        seed_section_id = "seed_ontology_from_graph"
        seed_section = self.fractal_system._create_generic_node(
            node_id=seed_section_id,
            node_type="graph_seed_section",
            name="Seed Ontology from Graph Prototype",
            content="Ontological concepts loaded from the graph prototype seed data",
            parent_id="graph_system",
            children=[],
            metadata={
                "section_type": "seed_ontology",
                "source": "graph_prototype",
                "frequency": 528.0,
                "chakra": "solar_plexus",
                "water_state": "crystalline"
            },
            structure_info={
                "fractal_depth": 4,
                "section_type": "graph_integration",
                "parent_system": "graph_system"
            }
        )
        
        # Add to graph system's children
        self.fractal_system._add_child_to_parent("graph_system", seed_section_id)
        
        # Process each seed node
        seed_nodes = self.seed_data.get("@graph", [])
        for i, seed_node in enumerate(seed_nodes):
            node_id = seed_node.get("@id", f"seed_node_{i}")
            
            # Create fractal node from seed data
            fractal_node = self.fractal_system._create_generic_node(
                node_id=f"graph_seed_{node_id.replace(':', '_')}",
                node_type="graph_seed_node",
                name=seed_node.get("name", f"Seed Node {i}"),
                content=seed_node.get("essence", f"Seed ontology concept: {seed_node.get('name', 'Unknown')}"),
                parent_id=seed_section_id,
                children=[],
                metadata={
                    "seed_id": node_id,
                    "water_state": seed_node.get("waterState", "unknown"),
                    "chakra": seed_node.get("chakra", "unknown"),
                    "color_hex": seed_node.get("colorHex", "#000000"),
                    "base_frequency_hz": seed_node.get("baseFrequencyHz", 0),
                    "planet": seed_node.get("planet", "unknown"),
                    "archetype": seed_node.get("archetype", []),
                    "layer": seed_node.get("layer", "Seed"),
                    "frequency": seed_node.get("baseFrequencyHz", 528.0),
                    "chakra": seed_node.get("chakra", "solar_plexus"),
                    "water_state": seed_node.get("waterState", "crystalline")
                },
                structure_info={
                    "fractal_depth": 5,
                    "node_type": "graph_seed",
                    "parent_section": seed_section_id,
                    "source": "graph_prototype"
                }
            )
            
            # Add to seed section's children
            self.fractal_system._add_child_to_parent(seed_section_id, f"graph_seed_{node_id.replace(':', '_')}")
        
        print(f"   ✅ Bootstrapped {len(seed_nodes)} seed nodes as fractal nodes")
    
    def execute_graph_query(self, cypher_query: str) -> List[Dict[str, Any]]:
        """Execute a Cypher query against the graph system"""
        
        try:
            # Try to use the graph API if available
            if self._is_graph_api_available():
                response = requests.post(
                    f"{self.graph_api_url}/query",
                    json={"query": cypher_query},
                    timeout=10
                )
                if response.status_code == 200:
                    return response.json()
            
            # Fallback to seed data analysis
            return self._analyze_seed_data_for_query(cypher_query)
            
        except Exception as e:
            print(f"⚠️  Error executing graph query: {e}")
            return self._analyze_seed_data_for_query(cypher_query)
    
    def _is_graph_api_available(self) -> bool:
        """Check if the graph API is available"""
        try:
            response = requests.get(f"{self.graph_api_url}/nodes", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def _analyze_seed_data_for_query(self, query: str) -> List[Dict[str, Any]]:
        """Analyze seed data to simulate graph query results"""
        
        # Simple query analysis for demonstration
        results = []
        seed_nodes = self.seed_data.get("@graph", [])
        
        if "waterState" in query.lower():
            # Find nodes by water state
            for node in seed_nodes:
                if "waterState" in node:
                    results.append({
                        "node": {
                            "id": node.get("@id"),
                            "name": node.get("name"),
                            "waterState": node.get("waterState"),
                            "chakra": node.get("chakra"),
                            "baseFrequencyHz": node.get("baseFrequencyHz")
                        }
                    })
        
        elif "chakra" in query.lower():
            # Find nodes by chakra
            for node in seed_nodes:
                if "chakra" in node:
                    results.append({
                        "node": {
                            "id": node.get("@id"),
                            "name": node.get("name"),
                            "chakra": node.get("chakra"),
                            "waterState": node.get("waterState")
                        }
                    })
        
        elif "frequency" in query.lower():
            # Find nodes by frequency
            for node in seed_nodes:
                if "baseFrequencyHz" in node:
                    results.append({
                        "node": {
                            "id": node.get("@id"),
                            "name": node.get("name"),
                            "baseFrequencyHz": node.get("baseFrequencyHz"),
                            "chakra": node.get("chakra")
                        }
                    })
        
        else:
            # Return all nodes
            for node in seed_nodes:
                results.append({
                    "node": {
                        "id": node.get("@id"),
                        "name": node.get("name"),
                        "waterState": node.get("waterState"),
                        "chakra": node.get("chakra"),
                        "baseFrequencyHz": node.get("baseFrequencyHz")
                    }
                })
        
        return results
    
    def generate_nodes_from_graph_query(self, cypher_query: str) -> str:
        """Generate fractal nodes from graph queries"""
        
        try:
            # Execute graph query
            results = self.execute_graph_query(cypher_query)
            
            if not results:
                return "No results found from graph query"
            
            # Transform results into fractal nodes
            generated_count = 0
            for result in results:
                if "node" in result:
                    node_data = result["node"]
                    node_id = node_data.get("id", f"query_result_{generated_count}")
                    
                    # Create fractal node from query result
                    fractal_node = self.fractal_system._create_generic_node(
                        node_id=f"query_result_{node_id.replace(':', '_')}",
                        node_type="graph_query_result",
                        name=node_data.get("name", f"Query Result {generated_count}"),
                        content=f"Node generated from graph query: {cypher_query[:50]}...",
                        parent_id="graph_system",
                        children=[],
                        metadata={
                            "query_source": cypher_query,
                            "original_id": node_id,
                            "water_state": node_data.get("waterState", "unknown"),
                            "chakra": node_data.get("chakra", "unknown"),
                            "base_frequency_hz": node_data.get("baseFrequencyHz", 0),
                            "frequency": node_data.get("baseFrequencyHz", 528.0),
                            "chakra": node_data.get("chakra", "solar_plexus"),
                            "water_state": node_data.get("waterState", "crystalline")
                        },
                        structure_info={
                            "fractal_depth": 4,
                            "node_type": "query_result",
                            "parent_system": "graph_system",
                            "query_source": cypher_query
                        }
                    )
                    
                    # Store the node
                    self.fractal_system._store_generic_node(fractal_node)
                    generated_count += 1
            
            return f"Generated {generated_count} nodes from graph query"
            
        except Exception as e:
            return f"Error generating nodes from graph query: {e}"
    
    def get_graph_system_overview(self) -> Dict[str, Any]:
        """Get overview of the integrated graph system"""
        
        # Count nodes by type
        node_counts = {}
        import sqlite3
        with sqlite3.connect(self.fractal_system.db_path) as conn:
            cursor = conn.execute("""
                SELECT node_type, COUNT(*) as count 
                FROM nodes 
                WHERE node_type LIKE 'graph_%'
                GROUP BY node_type
            """)
            for row in cursor.fetchall():
                node_counts[row[0]] = row[1]
        
        return {
            "graph_system_status": "integrated",
            "total_graph_nodes": sum(node_counts.values()),
            "node_type_distribution": node_counts,
            "seed_data_nodes": len(self.seed_data.get("@graph", [])),
            "graph_api_available": self._is_graph_api_available(),
            "integration_layer": "complete"
        }
    
    def demonstrate_graph_integration(self):
        """Demonstrate the graph integration capabilities"""
        
        print("\n🔍 Demonstrating Graph Integration")
        print("=" * 60)
        
        # Show graph system overview
        overview = self.get_graph_system_overview()
        print(f"   📊 Graph System Overview:")
        print(f"      • Total Graph Nodes: {overview['total_graph_nodes']}")
        print(f"      • Graph API Available: {overview['graph_api_available']}")
        print(f"      • Seed Data Nodes: {overview['seed_data_nodes']}")
        
        print(f"\n   📊 Node Type Distribution:")
        for node_type, count in overview['node_type_distribution'].items():
            print(f"      • {node_type}: {count} nodes")
        
        # Demonstrate graph queries
        print(f"\n   🔍 Graph Query Demonstrations:")
        
        queries = [
            "MATCH (n:Node) WHERE n.waterState = 'Plasma' RETURN n",
            "MATCH (n:Node) WHERE n.chakra = 'Crown' RETURN n",
            "MATCH (n:Node) WHERE n.baseFrequencyHz > 800 RETURN n"
        ]
        
        for query in queries:
            print(f"\n     ❓ Query: {query}")
            results = self.execute_graph_query(query)
            print(f"        📍 Results: {len(results)} nodes found")
            
            if results:
                for i, result in enumerate(results[:2]):  # Show first 2
                    if "node" in result:
                        node = result["node"]
                        print(f"        {i+1}. {node.get('name', 'Unknown')}")
                        if "waterState" in node:
                            print(f"           Water State: {node['waterState']}")
                        if "chakra" in node:
                            print(f"           Chakra: {node['chakra']}")
        
        # Demonstrate node generation from queries
        print(f"\n   🚀 Node Generation from Queries:")
        
        for query in queries[:2]:  # Use first 2 queries
            print(f"\n     🔧 Generating nodes from: {query[:50]}...")
            result = self.generate_nodes_from_graph_query(query)
            print(f"        {result}")
        
        print(f"\n   ✅ Graph Integration Demonstration Complete!")

def main():
    """Main function to demonstrate graph integration"""
    
    print("🌟 Graph Integration Layer Demo")
    print("=" * 60)
    
    try:
        # Import the fractal system
        from meta_implementation_demo import MetaImplementationDemo
        
        # Initialize the meta-implementation demo
        demo = MetaImplementationDemo()
        fractal_system = demo.fractal_system
        
        # Create and demonstrate graph integration
        graph_integration = GraphIntegrationLayer(fractal_system)
        graph_integration.demonstrate_graph_integration()
        
        print("\n" + "=" * 60)
        print("🎉 Graph Integration Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Graph system integrated as fractal nodes")
        print("   • Graph operations as API-driven evolution")
        print("   • Seed data bootstrapped into fractal system")
        print("   • Graph queries generating fractal nodes")
        print("   • Unified graph-fractal architecture")
        
    except Exception as e:
        print(f"❌ Error running graph integration demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
