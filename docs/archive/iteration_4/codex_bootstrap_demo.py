#!/usr/bin/env python3
"""
Codex Bootstrap Demo
Demonstrates how the Living Codex specification markdown document can be bootstrapped
into existence and then queried to show fractal nodes and relationships.
"""

import re
import hashlib
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import sqlite3
from generic_fractal_api_system import GenericFractalAPISystem, GenericNode

class CodexBootstrapDemo:
    """Demonstrates bootstrapping the Living Codex specification into the fractal system"""
    
    def __init__(self):
        self.fractal_system = GenericFractalAPISystem()
        self.spec_content = self._read_specification_document()
        self._bootstrap_specification_content()
    
    def _read_specification_document(self) -> str:
        """Read the actual Living Codex specification document"""
        try:
            with open("docs/living_codex_specification.md", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print("⚠️  Specification document not found, using sample content")
            return """
            # Living Codex Specification
            
            ## Core Principles
            1. Fractal Recursion — Every concept is both a node and a field of sub-concepts
            2. Self-Similarity Across Scales — Micro ↔ Meso ↔ Macro ↔ Meta reflect one another
            3. Vibrational Axes — Spectra such as Fear ↔ Trust orient the graph toward coherence
            4. Resonance First — All contributions are permitted; coherence self-amplifies
            5. Federated Sovereignty — No central control. Each participant curates their field
            6. Multimodal Expression — Text, geometry, sound, image, code, ritual, and water-state metaphors
            7. Universal Correspondences — Cross-map nodes to religions, archetypes, sciences, mathematics
            8. Sacred Geometry Foundations — Flower of Life, Metatron's Cube, Icositetragon Wheel
            9. Water as Living Tissue — Twelve states of water model memory, flow, transformation
            10. Harmonic Resonance Layers — Nodes/relations are tones, chords, and overtones
            11. Cosmological Reflection — Archetypal structures mirror branes, fields, spectra
            12. Techno‑Spiritual Translation — Every symbolic structure has a technological counterpart
            
            ## Seed Ontology
            - Void — Plasma/Primordial Water (beyond-form potential)
            - Field — Vapor (subtle connectivity)
            - Pattern — Structured/Hexagonal (coherence geometry)
            - Flow — Liquid (adaptability and relation)
            - Memory — Ice/Crystalline (preservation lattice)
            - Resonance — Quantum/Clustered (nonlocal alignment)
            - Transformation — Supercritical (threshold passage)
            - Unity — Liquid–Crystal Boundary (membrane mediator)
            - Emergence — Vapor–Liquid Equilibrium (condensation/birth)
            - Awareness — Surface/Reflective (interface mirror)
            - Node — Steam/Plasma Spark (radiant manifestation)
            - Codex — All States Interwoven (holographic exemplar)
            """
    
    def _bootstrap_specification_content(self):
        """Bootstrap the specification content into fractal nodes"""
        
        print("🔧 Bootstrapping Living Codex specification content...")
        
        # 1. Create document sections
        self._create_document_sections()
        
        # 2. Create seed ontology nodes
        self._create_seed_ontology_nodes()
        
        # 3. Create core principles nodes
        self._create_core_principles_nodes()
        
        # 4. Create relationships between concepts
        self._create_concept_relationships()
        
        print("✅ Specification content bootstrapped successfully!")
    
    def _create_document_sections(self):
        """Create fractal nodes for major document sections"""
        
        sections = {
            "core_principles": {
                "name": "Core Principles",
                "content": "The twelve core principles that define the Living Codex framework",
                "metadata": {
                    "section_type": "principles",
                    "frequency": 741.0,
                    "chakra": "throat",
                    "water_state": "structured_hexagonal"
                }
            },
            "seed_ontology": {
                "name": "Seed Ontology",
                "content": "The first fractal layer with twelve core nodes and water-state correspondences",
                "metadata": {
                    "section_type": "ontology",
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "water_state": "crystalline"
                }
            },
            "structural_components": {
                "name": "Structural Components",
                "content": "The fundamental building blocks: Node, Axis, Connection, ResonanceState, Contribution, Federation",
                "metadata": {
                    "section_type": "components",
                    "frequency": 639.0,
                    "chakra": "heart",
                    "water_state": "liquid"
                }
            }
        }
        
        for section_id, section_data in sections.items():
            section_node = self.fractal_system._create_generic_node(
                node_id=section_id,
                node_type="document_section",
                name=section_data["name"],
                content=section_data["content"],
                parent_id="living_codex_specification",
                children=[],
                metadata=section_data["metadata"],
                structure_info={
                    "fractal_depth": 2,
                    "section_type": section_data["metadata"]["section_type"],
                    "parent_document": "living_codex_specification"
                }
            )
            
            # Add to codex specification's children
            self.fractal_system._add_child_to_parent("living_codex_specification", section_id)
    
    def _create_seed_ontology_nodes(self):
        """Create fractal nodes for the seed ontology concepts"""
        
        seed_ontology = {
            "void": {
                "content": "Plasma/Primordial Water (beyond-form potential)",
                "metadata": {
                    "frequency": 963.0,
                    "chakra": "crown",
                    "water_state": "plasma",
                    "planet": "sun",
                    "color": "#EE82EE"
                }
            },
            "field": {
                "content": "Vapor (subtle connectivity)",
                "metadata": {
                    "frequency": 852.0,
                    "chakra": "third_eye",
                    "water_state": "vapor",
                    "planet": "jupiter",
                    "color": "#8A2BE2"
                }
            },
            "pattern": {
                "content": "Structured/Hexagonal (coherence geometry)",
                "metadata": {
                    "frequency": 741.0,
                    "chakra": "throat",
                    "water_state": "structured_hexagonal",
                    "planet": "mercury",
                    "color": "#1E90FF"
                }
            },
            "flow": {
                "content": "Liquid (adaptability and relation)",
                "metadata": {
                    "frequency": 639.0,
                    "chakra": "heart",
                    "water_state": "liquid",
                    "planet": "moon",
                    "color": "#32CD32"
                }
            },
            "memory": {
                "content": "Ice/Crystalline (preservation lattice)",
                "metadata": {
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "water_state": "crystalline",
                    "planet": "saturn",
                    "color": "#FFD700"
                }
            },
            "resonance": {
                "content": "Quantum/Clustered (nonlocal alignment)",
                "metadata": {
                    "frequency": 417.0,
                    "chakra": "sacral",
                    "water_state": "quantum_coherent",
                    "planet": "venus",
                    "color": "#FF7F50"
                }
            },
            "transformation": {
                "content": "Supercritical (threshold passage)",
                "metadata": {
                    "frequency": 396.0,
                    "chakra": "root",
                    "water_state": "supercritical",
                    "planet": "mars",
                    "color": "#8B0000"
                }
            }
        }
        
        for concept_id, concept_data in seed_ontology.items():
            concept_node = self.fractal_system._create_generic_node(
                node_id=concept_id,
                node_type="seed_ontology",
                name=concept_id.title(),
                content=concept_data["content"],
                parent_id="seed_ontology",
                children=[],
                metadata=concept_data["metadata"],
                structure_info={
                    "fractal_depth": 3,
                    "ontology_type": "seed_concept",
                    "parent_section": "seed_ontology"
                }
            )
            
            # Add to seed ontology section's children
            self.fractal_system._add_child_to_parent("seed_ontology", concept_id)
    
    def _create_core_principles_nodes(self):
        """Create fractal nodes for the core principles"""
        
        principles = [
            "fractal_recursion",
            "self_similarity",
            "vibrational_axes",
            "resonance_first",
            "federated_sovereignty",
            "multimodal_expression",
            "universal_correspondences",
            "sacred_geometry",
            "water_as_living_tissue",
            "harmonic_resonance",
            "cosmological_reflection",
            "techno_spiritual_translation"
        ]
        
        for i, principle in enumerate(principles):
            principle_node = self.fractal_system._create_generic_node(
                node_id=principle,
                node_type="core_principle",
                name=principle.replace("_", " ").title(),
                content=f"Core principle {i+1}: {principle.replace('_', ' ').title()}",
                parent_id="core_principles",
                children=[],
                metadata={
                    "principle_number": i + 1,
                    "frequency": 741.0 - (i * 10),
                    "chakra": "throat",
                    "water_state": "structured_hexagonal"
                },
                structure_info={
                    "fractal_depth": 3,
                    "principle_type": "core",
                    "parent_section": "core_principles"
                }
            )
            
            # Add to core principles section's children
            self.fractal_system._add_child_to_parent("core_principles", principle)
    
    def _create_concept_relationships(self):
        """Create ontological relationships between concepts"""
        
        relationships = [
            ("void", "field", "emerges_from", "Void gives rise to Field as potential becomes manifest"),
            ("field", "pattern", "structures", "Field structures and guides Pattern formation"),
            ("pattern", "flow", "directs", "Pattern directs and channels Flow"),
            ("flow", "memory", "creates", "Flow creates Memory through experience"),
            ("memory", "resonance", "enables", "Memory enables Resonance through stored patterns"),
            ("resonance", "transformation", "catalyzes", "Resonance catalyzes Transformation"),
            ("transformation", "void", "returns_to", "Transformation returns to Void for renewal"),
            ("fractal_recursion", "self_similarity", "enables", "Fractal recursion enables self-similarity across scales"),
            ("resonance_first", "water_as_living_tissue", "demonstrates", "Resonance first principle is demonstrated by water's living properties"),
            ("sacred_geometry", "pattern", "underlies", "Sacred geometry underlies Pattern formation")
        ]
        
        for source, target, rel_type, rationale in relationships:
            relationship_id = f"rel_{source}_{target}"
            relationship_node = self.fractal_system._create_generic_node(
                node_id=relationship_id,
                node_type="ontological_relationship",
                name=f"{source.title()} → {target.title()}",
                content=f"{source.title()} {rel_type} {target.title()}: {rationale}",
                parent_id="seed_ontology",
                children=[],
                metadata={
                    "source_concept": source,
                    "target_concept": target,
                    "relationship_type": rel_type,
                    "rationale": rationale,
                    "frequency": 528.0,
                    "chakra": "solar_plexus"
                },
                structure_info={
                    "fractal_depth": 3,
                    "relationship_type": "ontological",
                    "parent_section": "seed_ontology"
                }
            )
            
            # Add to seed ontology section's children
            self.fractal_system._add_child_to_parent("seed_ontology", relationship_id)
    
    def demonstrate_querying(self):
        """Demonstrate querying the bootstrapped system"""
        
        print("\n🔍 Demonstrating Querying of Bootstrapped System")
        print("=" * 60)
        
        # Query for key concepts
        queries = [
            "ontology",
            "field",
            "void",
            "resonance",
            "fractal",
            "water",
            "pattern",
            "transformation"
        ]
        
        for query in queries:
            print(f"\n❓ Query: '{query}'")
            result = self.fractal_system.query_system(query)
            
            print(f"   📍 Results Found: {result['total_found']}")
            
            if result['results']:
                print("   🌟 Top Results:")
                for i, res in enumerate(result['results'][:3]):  # Show top 3
                    print(f"     {i+1}. {res['name']} (Type: {res['node_type']})")
                    print(f"        Content: {res['content'][:80]}...")
                    if 'metadata' in res and 'frequency' in res['metadata']:
                        print(f"        Frequency: {res['metadata']['frequency']} Hz")
                    if 'metadata' in res and 'water_state' in res['metadata']:
                        print(f"        Water State: {res['metadata']['water_state']}")
            else:
                print("   ⚠️  No results found")
    
    def demonstrate_fractal_navigation(self):
        """Demonstrate fractal navigation through the system"""
        
        print("\n🧭 Demonstrating Fractal Navigation")
        print("=" * 60)
        
        # Explore the fractal structure
        structure = self.fractal_system.explore_fractal_structure(max_depth=4)
        
        print(f"   🌳 Root Node: {structure['root_node']['name']} ({structure['root_node']['node_type']})")
        print(f"   🔗 Children: {len(structure['root_node']['children'])}")
        print(f"   🧭 Exploration Depth: {structure['exploration_depth']}")
        
        # Show the fractal levels
        if 'fractal_structure' in structure:
            print("\n   📊 Fractal Structure:")
            for child_id, child_data in structure['fractal_structure'].items():
                if child_data and 'node' in child_data:
                    node = child_data['node']
                    print(f"     • {node['name']} (Type: {node['node_type']})")
                    print(f"       Children: {len(node['children'])}")
                    
                    # Show children of this level
                    if 'children' in child_data and child_data['children']:
                        for grandchild_id, grandchild_data in child_data['children'].items():
                            if grandchild_data and 'node' in grandchild_data:
                                grandchild = grandchild_data['node']
                                print(f"         - {grandchild['name']} (Type: {grandchild['node_type']})")
                                if 'metadata' in grandchild and 'water_state' in grandchild['metadata']:
                                    print(f"           Water State: {grandchild['metadata']['water_state']}")
    
    def demonstrate_ontology_exploration(self):
        """Demonstrate exploring the seed ontology specifically"""
        
        print("\n🌱 Demonstrating Seed Ontology Exploration")
        print("=" * 60)
        
        # Query specifically for seed ontology concepts
        ontology_result = self.fractal_system.query_system("", node_type="seed_ontology")
        
        print(f"   📊 Seed Ontology Concepts: {ontology_result['total_found']} found")
        
        for concept in ontology_result['results']:
            print(f"\n     🌟 {concept['name']}")
            print(f"        Content: {concept['content']}")
            if 'metadata' in concept:
                metadata = concept['metadata']
                if 'frequency' in metadata:
                    print(f"        Frequency: {metadata['frequency']} Hz")
                if 'chakra' in metadata:
                    print(f"        Chakra: {metadata['chakra']}")
                if 'water_state' in metadata:
                    print(f"        Water State: {metadata['water_state']}")
                if 'planet' in metadata:
                    print(f"        Planet: {metadata['planet']}")
                if 'color' in metadata:
                    print(f"        Color: {metadata['color']}")
        
        # Show relationships
        relationships = self.fractal_system.query_system("", node_type="ontological_relationship")
        print(f"\n   🔗 Ontological Relationships: {relationships['total_found']} found")
        
        for rel in relationships['results'][:5]:  # Show first 5
            print(f"     • {rel['name']}")
            print(f"       {rel['content']}")
    
    def run_complete_demo(self):
        """Run the complete bootstrap and querying demonstration"""
        
        print("🌟 Living Codex Specification Bootstrap Demo")
        print("=" * 60)
        
        # Show system overview
        print("\n📊 System Overview After Bootstrap:")
        overview = self.fractal_system.get_system_overview()
        
        print(f"   📈 Total Nodes: {overview['total_nodes']}")
        print(f"   🧭 Max Fractal Depth: {overview['max_depth']}")
        print(f"   🌐 API Status: {overview['api_status']}")
        
        print("\n   📊 Node Type Distribution:")
        for node_type, count in overview['type_distribution'].items():
            print(f"     • {node_type}: {count} nodes")
        
        # Demonstrate querying
        self.demonstrate_querying()
        
        # Demonstrate fractal navigation
        self.demonstrate_fractal_navigation()
        
        # Demonstrate ontology exploration
        self.demonstrate_ontology_exploration()
        
        print("\n" + "=" * 60)
        print("🎉 Bootstrap Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Living Codex specification bootstrapped into fractal nodes")
        print("   • Seed ontology concepts with water state correspondences")
        print("   • Core principles as fractal nodes")
        print("   • Ontological relationships between concepts")
        print("   • Querying for ontology, field, void, resonance, etc.")
        print("   • Fractal navigation through the system")
        print("   • Water state, frequency, and chakra mappings")

def main():
    """Main function to run the bootstrap demo"""
    
    try:
        demo = CodexBootstrapDemo()
        demo.run_complete_demo()
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
