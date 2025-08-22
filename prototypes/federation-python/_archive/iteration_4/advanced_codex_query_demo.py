#!/usr/bin/env python3
"""
Advanced Codex Query Demo
Demonstrates advanced querying capabilities and fractal navigation through
the bootstrapped Living Codex specification system.
"""

import json
from typing import List, Dict, Any
from codex_bootstrap_demo import CodexBootstrapDemo

class AdvancedCodexQueryDemo:
    """Advanced demonstration of querying and fractal navigation capabilities"""
    
    def __init__(self):
        self.bootstrap_demo = CodexBootstrapDemo()
        self.fractal_system = self.bootstrap_demo.fractal_system
    
    def demonstrate_advanced_querying(self):
        """Demonstrate advanced querying capabilities"""
        
        print("🔍 Advanced Querying Demonstrations")
        print("=" * 60)
        
        # 1. Query for specific node types
        self._demonstrate_type_based_querying()
        
        # 2. Query for specific metadata values
        self._demonstrate_metadata_querying()
        
        # 3. Query for relationships
        self._demonstrate_relationship_querying()
        
        # 4. Query for frequency ranges
        self._demonstrate_frequency_querying()
        
        # 5. Query for water states
        self._demonstrate_water_state_querying()
    
    def _demonstrate_type_based_querying(self):
        """Demonstrate querying by node type"""
        
        print("\n📊 Type-Based Querying:")
        
        node_types = [
            "seed_ontology",
            "core_principle", 
            "ontological_relationship",
            "document_section"
        ]
        
        for node_type in node_types:
            result = self.fractal_system.query_system("", node_type=node_type)
            print(f"   • {node_type}: {result['total_found']} nodes")
            
            if result['results']:
                sample = result['results'][0]
                print(f"     Sample: {sample['name']} - {sample['content'][:60]}...")
    
    def _demonstrate_metadata_querying(self):
        """Demonstrate querying for specific metadata values"""
        
        print("\n🔍 Metadata-Based Querying:")
        
        # Query for specific chakras
        chakras = ["crown", "third_eye", "throat", "heart", "solar_plexus", "sacral", "root"]
        
        for chakra in chakras:
            # We'll search for content that mentions the chakra
            result = self.fractal_system.query_system(chakra)
            if result['total_found'] > 0:
                print(f"   • {chakra.title()} Chakra: {result['total_found']} related nodes")
                
                # Find the specific chakra node
                for res in result['results']:
                    if res['node_type'] == 'seed_ontology' and 'metadata' in res:
                        metadata = res['metadata']
                        if 'chakra' in metadata and metadata['chakra'] == chakra:
                            print(f"     {res['name']}: {metadata.get('water_state', 'N/A')} water state, "
                                  f"{metadata.get('frequency', 'N/A')} Hz, {metadata.get('planet', 'N/A')}")
    
    def _demonstrate_relationship_querying(self):
        """Demonstrate querying for relationships"""
        
        print("\n🔗 Relationship Querying:")
        
        # Get all ontological relationships
        relationships = self.fractal_system.query_system("", node_type="ontological_relationship")
        
        print(f"   📊 Total Relationships: {relationships['total_found']}")
        
        # Group relationships by source concept
        relationship_groups = {}
        for rel in relationships['results']:
            if 'metadata' in rel and 'source_concept' in rel['metadata']:
                source = rel['metadata']['source_concept']
                if source not in relationship_groups:
                    relationship_groups[source] = []
                relationship_groups[source].append(rel)
        
        print("\n   📈 Relationship Network:")
        for source, rels in relationship_groups.items():
            print(f"     • {source.title()} → {len(rels)} connections:")
            for rel in rels:
                target = rel['metadata'].get('target_concept', 'Unknown')
                rel_type = rel['metadata'].get('relationship_type', 'Unknown')
                print(f"       - {target.title()} ({rel_type})")
    
    def _demonstrate_frequency_querying(self):
        """Demonstrate querying for frequency ranges"""
        
        print("\n🎵 Frequency-Based Querying:")
        
        # Define frequency ranges (Solfeggio frequencies)
        frequency_ranges = [
            (396, 417, "Root Chakra Range"),
            (417, 528, "Sacral Chakra Range"),
            (528, 639, "Solar Plexus Range"),
            (639, 741, "Heart Chakra Range"),
            (741, 852, "Throat Chakra Range"),
            (852, 963, "Third Eye & Crown Range")
        ]
        
        for low, high, description in frequency_ranges:
            # Query for nodes in this frequency range
            nodes_in_range = []
            
            # Get all nodes with metadata
            all_nodes = self.fractal_system.query_system("")
            for node in all_nodes['results']:
                if 'metadata' in node and 'frequency' in node['metadata']:
                    freq = node['metadata']['frequency']
                    if low <= freq <= high:
                        nodes_in_range.append(node)
            
            if nodes_in_range:
                print(f"   • {description} ({low}-{high} Hz): {len(nodes_in_range)} nodes")
                for node in nodes_in_range[:2]:  # Show first 2
                    print(f"     - {node['name']}: {node['metadata']['frequency']} Hz")
    
    def _demonstrate_water_state_querying(self):
        """Demonstrate querying for water states"""
        
        print("\n💧 Water State Querying:")
        
        water_states = [
            "plasma", "vapor", "structured_hexagonal", "liquid", 
            "crystalline", "quantum_coherent", "supercritical"
        ]
        
        for water_state in water_states:
            # Find nodes with this water state
            nodes_with_state = []
            
            all_nodes = self.fractal_system.query_system("")
            for node in all_nodes['results']:
                if 'metadata' in node and 'water_state' in node['metadata']:
                    if node['metadata']['water_state'] == water_state:
                        nodes_with_state.append(node)
            
            if nodes_with_state:
                print(f"   • {water_state.replace('_', ' ').title()}: {len(nodes_with_state)} nodes")
                for node in nodes_with_state:
                    print(f"     - {node['name']} ({node['node_type']})")
                    if 'frequency' in node['metadata']:
                        print(f"       Frequency: {node['metadata']['frequency']} Hz")
    
    def demonstrate_fractal_navigation_deep(self):
        """Demonstrate deep fractal navigation"""
        
        print("\n🧭 Deep Fractal Navigation")
        print("=" * 60)
        
        # Get the complete fractal structure
        structure = self.fractal_system.explore_fractal_structure(max_depth=5)
        
        print(f"   🌳 Root: {structure['root_node']['name']}")
        print(f"   🧭 Max Depth: {structure['exploration_depth']}")
        
        # Navigate through the fractal levels
        if 'fractal_structure' in structure:
            self._navigate_fractal_levels(structure['fractal_structure'], 0)
    
    def _navigate_fractal_levels(self, level_data: Dict, current_depth: int):
        """Recursively navigate through fractal levels"""
        
        indent = "  " * (current_depth + 1)
        
        for node_id, node_info in level_data.items():
            if node_info and 'node' in node_info:
                node = node_info['node']
                
                # Show node information
                print(f"{indent}• {node['name']} ({node['node_type']})")
                
                # Show metadata if available
                if 'metadata' in node:
                    metadata = node['metadata']
                    if 'water_state' in metadata:
                        print(f"{indent}  💧 Water State: {metadata['water_state']}")
                    if 'frequency' in metadata:
                        print(f"{indent}  🎵 Frequency: {metadata['frequency']} Hz")
                    if 'chakra' in metadata:
                        print(f"{indent}  🌀 Chakra: {metadata['chakra']}")
                
                # Show children count
                if 'children' in node_info and node_info['children']:
                    print(f"{indent}  👥 Children: {len(node_info['children'])}")
                    
                    # Recursively navigate children
                    if current_depth < 3:  # Limit recursion depth for display
                        self._navigate_fractal_levels(node_info['children'], current_depth + 1)
    
    def demonstrate_concept_network_analysis(self):
        """Demonstrate analysis of the concept network"""
        
        print("\n🌐 Concept Network Analysis")
        print("=" * 60)
        
        # Get all seed ontology concepts
        ontology_concepts = self.fractal_system.query_system("", node_type="seed_ontology")
        
        print(f"   📊 Core Concepts: {ontology_concepts['total_found']}")
        
        # Analyze the network structure
        concept_network = {}
        
        for concept in ontology_concepts['results']:
            concept_id = concept['node_id']
            concept_network[concept_id] = {
                'name': concept['name'],
                'water_state': concept['metadata'].get('water_state', 'Unknown'),
                'frequency': concept['metadata'].get('frequency', 0),
                'chakra': concept['metadata'].get('chakra', 'Unknown'),
                'connections': []
            }
        
        # Find connections for each concept
        relationships = self.fractal_system.query_system("", node_type="ontological_relationship")
        
        for rel in relationships['results']:
            if 'metadata' in rel:
                source = rel['metadata'].get('source_concept')
                target = rel['metadata'].get('target_concept')
                rel_type = rel['metadata'].get('relationship_type', 'Unknown')
                
                if source in concept_network:
                    concept_network[source]['connections'].append({
                        'target': target,
                        'type': rel_type,
                        'description': rel['content']
                    })
        
        # Display the network
        print("\n   🔗 Concept Network:")
        for concept_id, concept_info in concept_network.items():
            print(f"\n     🌟 {concept_info['name']}")
            print(f"        💧 Water State: {concept_info['water_state']}")
            print(f"        🎵 Frequency: {concept_info['frequency']} Hz")
            print(f"        🌀 Chakra: {concept_info['chakra']}")
            print(f"        🔗 Connections: {len(concept_info['connections'])}")
            
            for conn in concept_info['connections']:
                print(f"          - → {conn['target'].title()} ({conn['type']})")
    
    def demonstrate_living_codex_as_final_node(self):
        """Demonstrate how the Living Codex specification is the final node"""
        
        print("\n📚 Living Codex as Final Node")
        print("=" * 60)
        
        # Get the Living Codex specification node
        codex_node = self.fractal_system.get_node_by_id("living_codex_specification")
        
        if codex_node:
            print(f"   🌟 Final Node: {codex_node['name']}")
            print(f"   📝 Content: {codex_node['content'][:100]}...")
            print(f"   🔗 Children: {len(codex_node['children'])}")
            
            # Show the children (document sections)
            print("\n   📖 Document Sections:")
            for child_id in codex_node['children']:
                child_node = self.fractal_system.get_node_by_id(child_id)
                if child_node:
                    print(f"     • {child_node['name']} ({child_node['node_type']})")
                    print(f"       Content: {child_node['content'][:80]}...")
                    
                    # Show metadata
                    if 'metadata' in child_node:
                        metadata = child_node['metadata']
                        if 'water_state' in metadata:
                            print(f"       💧 Water State: {metadata['water_state']}")
                        if 'frequency' in metadata:
                            print(f"       🎵 Frequency: {metadata['frequency']} Hz")
        
        # Show how this creates a living document
        print("\n   🌊 Living Document Properties:")
        print("     • The specification is represented as nodes")
        print("     • Each section is a fractal node")
        print("     • Concepts within sections are nodes")
        print("     • Relationships between concepts are nodes")
        print("     • The structure itself is represented as nodes")
        print("     • Everything can be queried and navigated")
    
    def run_advanced_demo(self):
        """Run the complete advanced demonstration"""
        
        print("🌟 Advanced Living Codex Query & Navigation Demo")
        print("=" * 70)
        
        # Show system overview
        overview = self.fractal_system.get_system_overview()
        print(f"\n📊 System Overview:")
        print(f"   📈 Total Nodes: {overview['total_nodes']}")
        print(f"   🧭 Max Fractal Depth: {overview['max_depth']}")
        print(f"   🌐 API Status: {overview['api_status']}")
        
        # Run all demonstrations
        self.demonstrate_advanced_querying()
        self.demonstrate_fractal_navigation_deep()
        self.demonstrate_concept_network_analysis()
        self.demonstrate_living_codex_as_final_node()
        
        print("\n" + "=" * 70)
        print("🎉 Advanced Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Advanced querying by node type, metadata, and relationships")
        print("   • Frequency-based and water state-based querying")
        print("   • Deep fractal navigation through the system")
        print("   • Concept network analysis and visualization")
        print("   • Living Codex specification as the final fractal node")
        print("   • How everything in the system is represented as nodes")
        print("   • Fractal relationships between concepts, principles, and ontology")

def main():
    """Main function to run the advanced demo"""
    
    try:
        demo = AdvancedCodexQueryDemo()
        demo.run_advanced_demo()
    except Exception as e:
        print(f"❌ Error running advanced demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
