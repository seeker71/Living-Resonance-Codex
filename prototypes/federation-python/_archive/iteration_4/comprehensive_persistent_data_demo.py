#!/usr/bin/env python3
"""
Comprehensive Persistent Data Demo
Demonstrates practical integration of the unified persistent data ontology
with real data examples, including JSON, self-referential formats, and seed data.
"""

import json
import hashlib
from typing import Dict, Any, List
from unified_persistent_data_ontology import UnifiedPersistentDataOntology, DataNode

class ComprehensivePersistentDataDemo:
    """Comprehensive demonstration of unified persistent data ontology capabilities"""
    
    def __init__(self):
        self.ontology = UnifiedPersistentDataOntology()
        print("🌟 Comprehensive Persistent Data Demo - Living Codex System")
        print("=" * 60)
    
    def run_comprehensive_demo(self):
        """Run the complete persistent data demonstration"""
        
        print("🚀 Starting Comprehensive Persistent Data Demo...")
        print()
        
        # Phase 1: Core Ontology Overview
        self._demonstrate_core_ontology()
        
        # Phase 2: JSON Data Handling
        self._demonstrate_json_handling()
        
        # Phase 3: Self-Referential Data Creation
        self._demonstrate_self_referential_data()
        
        # Phase 4: Seed Data Integration
        self._demonstrate_seed_data_integration()
        
        # Phase 5: Cross-Format Integration
        self._demonstrate_cross_format_integration()
        
        # Phase 6: Practical Applications
        self._demonstrate_practical_applications()
        
        print("\n" + "=" * 60)
        print("🎉 Comprehensive Persistent Data Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Complete persistent data ontology integration")
        print("   • JSON data handling and transformation")
        print("   • Self-referential data creation and evolution")
        print("   • Seed data integration with Codex ontology")
        print("   • Cross-format data harmony")
        print("   • Practical applications and use cases")
        print("\n🚀 The Living Codex now has comprehensive persistent data capabilities!")
    
    def _demonstrate_core_ontology(self):
        """Demonstrate the core persistent data ontology"""
        
        print("🔍 Phase 1: Core Persistent Data Ontology")
        print("-" * 40)
        
        # Show bootstrap nodes
        print("   🌱 Bootstrap Nodes:")
        for node_id, node in self.ontology.bootstrap_nodes.items():
            print(f"      • {node.name} ({node.node_type})")
            print(f"        🎯 Purpose: {node.content[:80]}...")
            print(f"        🌊 Water State: {node.metadata.get('water_state', 'unknown')}")
            print(f"        🎵 Frequency: {node.metadata.get('frequency', 'unknown')} Hz")
            print(f"        🔗 Children: {len(node.children)}")
        
        # Show meta-nodes
        print("\n   🔍 Meta-Nodes:")
        for node_id, node in self.ontology.meta_nodes.items():
            print(f"      • {node.name} ({node.node_type})")
            print(f"        🎯 Purpose: {node.content[:80]}...")
            print(f"        🌊 Water State: {node.metadata.get('water_state', 'unknown')}")
            print(f"        🧬 Meta Type: {node.metadata.get('meta_type', 'unknown')}")
        
        # Show data formats
        print("\n   📊 Data Format Ontologies:")
        for format_name, format_info in self.ontology.data_formats.items():
            print(f"      • {format_name.title()}: {format_info['root'].name}")
            print(f"        🧊 Ice Layer: {format_info['ice'].name}")
            print(f"        💧 Water Layer: {format_info['water'].name}")
            print(f"        🌫️ Vapor Layer: {format_info['vapor'].name}")
        
        print("   ✅ Core ontology demonstration complete!")
    
    def _demonstrate_json_handling(self):
        """Demonstrate JSON data handling capabilities"""
        
        print("\n🔍 Phase 2: JSON Data Handling")
        print("-" * 40)
        
        # Create sample JSON data
        sample_json = {
            "user": {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com",
                "preferences": {
                    "theme": "dark",
                    "language": "en"
                }
            },
            "settings": {
                "notifications": True,
                "auto_save": False
            }
        }
        
        print("   📝 Sample JSON Data:")
        print(f"      {json.dumps(sample_json, indent=6)}")
        
        # Create data instance nodes
        print("\n   🔧 Creating JSON Data Instance Nodes:")
        
        # Create root object node
        root_node = self.ontology.create_data_instance(sample_json, "json", "json_content_vapor")
        print(f"      • Root Object: {root_node.name} (ID: {root_node.node_id})")
        print(f"        🌊 Water State: {root_node.metadata['water_state']}")
        print(f"        📊 Data Type: {root_node.metadata['data_type']}")
        
        # Create nested object nodes
        user_node = self.ontology.create_data_instance(sample_json["user"], "json", root_node.node_id)
        print(f"      • User Object: {user_node.name} (ID: {user_node.node_id})")
        
        settings_node = self.ontology.create_data_instance(sample_json["settings"], "json", root_node.node_id)
        print(f"      • Settings Object: {settings_node.name} (ID: {settings_node.node_id})")
        
        # Create primitive nodes
        name_node = self.ontology.create_data_instance(sample_json["user"]["name"], "json", user_node.node_id)
        print(f"      • Name Primitive: {name_node.name} (ID: {name_node.node_id})")
        
        theme_node = self.ontology.create_data_instance(sample_json["user"]["preferences"]["theme"], "json", user_node.node_id)
        print(f"      • Theme Primitive: {theme_node.name} (ID: {theme_node.node_id})")
        
        print("   ✅ JSON data handling demonstration complete!")
    
    def _demonstrate_self_referential_data(self):
        """Demonstrate self-referential data creation"""
        
        print("\n🔍 Phase 3: Self-Referential Data Creation")
        print("-" * 40)
        
        # Create a self-referential data structure
        self_ref_data = {
            "metadata": {
                "description": "This data describes itself",
                "version": "1.0",
                "created": "2024-01-01",
                "schema": {
                    "type": "object",
                    "properties": {
                        "metadata": {"type": "object"},
                        "content": {"type": "object"},
                        "relationships": {"type": "array"}
                    }
                }
            },
            "content": {
                "title": "Self-Referential Document",
                "body": "This document contains metadata about itself",
                "tags": ["self-reference", "meta-data", "ontology"]
            },
            "relationships": [
                {
                    "type": "describes",
                    "target": "self",
                    "strength": "strong"
                },
                {
                    "type": "evolves_from",
                    "target": "previous_version",
                    "strength": "medium"
                }
            ]
        }
        
        print("   🔄 Self-Referential Data Structure:")
        print(f"      {json.dumps(self_ref_data, indent=6)}")
        
        # Create schema definition
        schema = {
            "type": "object",
            "properties": {
                "metadata": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "version": {"type": "string"},
                        "created": {"type": "string"},
                        "schema": {"type": "object"}
                    }
                },
                "content": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}}
                    }
                },
                "relationships": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string"},
                            "target": {"type": "string"},
                            "strength": {"type": "string"}
                        }
                    }
                }
            }
        }
        
        print("\n   📋 Schema Definition:")
        print(f"      {json.dumps(schema, indent=6)}")
        
        # Create self-referential data nodes
        print("\n   🔧 Creating Self-Referential Data Nodes:")
        self_ref_nodes = self.ontology.create_self_referential_data(self_ref_data, schema)
        
        print(f"      • Total Nodes Created: {len(self_ref_nodes)}")
        print("      • Node Types:")
        for path, node in self_ref_nodes.items():
            print(f"        - {path}: {node.name} ({node.node_type})")
            print(f"          🌊 Water State: {node.metadata.get('water_state', 'unknown')}")
            print(f"          📊 Data Type: {node.metadata.get('data_type', 'unknown')}")
        
        print("   ✅ Self-referential data creation demonstration complete!")
    
    def _demonstrate_seed_data_integration(self):
        """Demonstrate seed data integration with Codex ontology"""
        
        print("\n🔍 Phase 4: Seed Data Integration")
        print("-" * 40)
        
        # Create sample seed data (similar to ontology/seed.json)
        sample_seed_data = {
            "@context": "https://living-codex.org/ontology",
            "@graph": [
                {
                    "@id": "water_element",
                    "name": "Water Element",
                    "waterState": "liquid",
                    "chakra": "heart",
                    "baseFrequencyHz": 639.0,
                    "archetype": "flowing",
                    "hasPart": ["molecule", "flow", "transformation"],
                    "isPartOf": ["nature", "life", "cycle"]
                },
                {
                    "@id": "ice_element",
                    "name": "Ice Element",
                    "waterState": "ice",
                    "chakra": "crown",
                    "baseFrequencyHz": 963.0,
                    "archetype": "structured",
                    "hasPart": ["crystal", "form", "stability"],
                    "isPartOf": ["water_cycle", "winter", "preservation"]
                },
                {
                    "@id": "vapor_element",
                    "name": "Vapor Element",
                    "waterState": "vapor",
                    "chakra": "third_eye",
                    "baseFrequencyHz": 852.0,
                    "archetype": "evolving",
                    "hasPart": ["steam", "cloud", "change"],
                    "isPartOf": ["atmosphere", "evaporation", "transformation"]
                }
            ]
        }
        
        print("   🌱 Sample Seed Data:")
        print(f"      {json.dumps(sample_seed_data, indent=6)}")
        
        # Create seed data integration nodes
        print("\n   🔧 Creating Seed Data Integration Nodes:")
        seed_nodes = self.ontology.create_seed_data_integration(sample_seed_data)
        
        print(f"      • Total Seed Nodes Created: {len(seed_nodes)}")
        print("      • Seed Data Structure:")
        
        for node_id, node in seed_nodes.items():
            print(f"        - {node.name} ({node.node_type})")
            print(f"          🌊 Water State: {node.metadata.get('water_state_original', 'unknown')}")
            print(f"          🎵 Frequency: {node.metadata.get('frequency', 'unknown')} Hz")
            print(f"          🔮 Chakra: {node.metadata.get('chakra', 'unknown')}")
            print(f"          🧬 Archetype: {node.metadata.get('archetype', 'unknown')}")
            if hasattr(node, 'children') and node.children:
                print(f"          🔗 Children: {len(node.children)}")
        
        print("   ✅ Seed data integration demonstration complete!")
    
    def _demonstrate_cross_format_integration(self):
        """Demonstrate cross-format data integration"""
        
        print("\n🔍 Phase 5: Cross-Format Integration")
        print("-" * 40)
        
        # Create a complex data structure that combines multiple formats
        cross_format_data = {
            "document": {
                "type": "cross_format_integration",
                "format": "self_referential_json",
                "metadata": {
                    "created": "2024-01-01",
                    "version": "1.0",
                    "description": "Demonstrates cross-format data integration"
                }
            },
            "content": {
                "json_section": {
                    "type": "json_data",
                    "data": {"key": "value", "number": 42}
                },
                "self_ref_section": {
                    "type": "self_referential",
                    "describes": "itself",
                    "schema": {"type": "object"}
                },
                "seed_section": {
                    "type": "seed_data",
                    "element": "water",
                    "properties": {
                        "waterState": "liquid",
                        "frequency": 639.0,
                        "chakra": "heart"
                    }
                }
            },
            "relationships": {
                "json_to_self_ref": "JSON data can reference self-referential structures",
                "self_ref_to_seed": "Self-referential data can describe seed data",
                "seed_to_json": "Seed data can be represented in JSON format"
            }
        }
        
        print("   🔗 Cross-Format Data Structure:")
        print(f"      {json.dumps(cross_format_data, indent=6)}")
        
        # Create nodes for each format section
        print("\n   🔧 Creating Cross-Format Integration Nodes:")
        
        # JSON section
        json_section = self.ontology.create_data_instance(
            cross_format_data["content"]["json_section"], 
            "json", 
            "persistent_data_root"
        )
        print(f"      • JSON Section: {json_section.name} (ID: {json_section.node_id})")
        
        # Self-referential section
        self_ref_section = self.ontology.create_data_instance(
            cross_format_data["content"]["self_ref_section"], 
            "self_referential", 
            "persistent_data_root"
        )
        print(f"      • Self-Referential Section: {self_ref_section.name} (ID: {self_ref_section.node_id})")
        
        # Seed section
        seed_section = self.ontology.create_data_instance(
            cross_format_data["content"]["seed_section"], 
            "seed_data", 
            "persistent_data_root"
        )
        print(f"      • Seed Section: {seed_section.name} (ID: {seed_section.node_id})")
        
        # Relationships section
        relationships_section = self.ontology.create_data_instance(
            cross_format_data["relationships"], 
            "generic", 
            "persistent_data_root"
        )
        print(f"      • Relationships Section: {relationships_section.name} (ID: {relationships_section.node_id})")
        
        print("   ✅ Cross-format integration demonstration complete!")
    
    def _demonstrate_practical_applications(self):
        """Demonstrate practical applications of the unified persistent data ontology"""
        
        print("\n🔍 Phase 6: Practical Applications")
        print("-" * 40)
        
        # Application 1: Document Management System
        print("   📚 Application 1: Document Management System")
        doc_system = {
            "documents": [
                {
                    "id": "doc_001",
                    "title": "Living Codex Specification",
                    "format": "markdown",
                    "content_type": "specification",
                    "metadata": {
                        "author": "Living Codex System",
                        "created": "2024-01-01",
                        "version": "0.9R"
                    }
                },
                {
                    "id": "doc_002",
                    "title": "API Documentation",
                    "format": "json",
                    "content_type": "api_docs",
                    "metadata": {
                        "author": "System Generated",
                        "created": "2024-01-01",
                        "version": "1.0"
                    }
                }
            ]
        }
        
        doc_system_node = self.ontology.create_data_instance(doc_system, "generic", "persistent_data_root")
        print(f"      • Document System: {doc_system_node.name} (ID: {doc_system_node.node_id})")
        
        # Application 2: Knowledge Graph Integration
        print("\n   🧠 Application 2: Knowledge Graph Integration")
        knowledge_graph = {
            "nodes": [
                {
                    "id": "concept_001",
                    "type": "ontological_concept",
                    "name": "Water State Ontology",
                    "properties": {
                        "ice": "structured, frozen, blueprint",
                        "water": "flowing, dynamic, recipe",
                        "vapor": "evolving, living, cells"
                    }
                }
            ],
            "relationships": [
                {
                    "source": "concept_001",
                    "target": "concept_002",
                    "type": "evolves_into",
                    "properties": {
                        "ice_to_water": "melting",
                        "water_to_vapor": "evaporation",
                        "vapor_to_ice": "condensation"
                    }
                }
            ]
        }
        
        knowledge_graph_node = self.ontology.create_data_instance(knowledge_graph, "self_referential", "persistent_data_root")
        print(f"      • Knowledge Graph: {knowledge_graph_node.name} (ID: {knowledge_graph_node.node_id})")
        
        # Application 3: Configuration Management
        print("\n   ⚙️ Application 3: Configuration Management")
        config_system = {
            "system_config": {
                "database": {
                    "type": "sqlite",
                    "path": "fractal_system.db",
                    "backup_enabled": True
                },
                "api": {
                    "host": "localhost",
                    "port": 8000,
                    "cors_enabled": True
                },
                "ontology": {
                    "water_states": ["ice", "water", "vapor"],
                    "chakras": ["crown", "third_eye", "throat", "heart"],
                    "frequencies": [963.0, 852.0, 741.0, 639.0]
                }
            }
        }
        
        config_node = self.ontology.create_data_instance(config_system, "json", "persistent_data_root")
        print(f"      • Configuration System: {config_node.name} (ID: {config_node.node_id})")
        
        print("   ✅ Practical applications demonstration complete!")
    
    def show_integration_summary(self):
        """Show a summary of how the persistent data ontology integrates with the Living Codex"""
        
        print("\n🔗 Integration with Living Codex System")
        print("=" * 60)
        
        integration_points = {
            "Unified Language Ontology": {
                "connection": "Persistent data supports language representation",
                "benefit": "All language concepts can be stored and retrieved"
            },
            "Enhanced Fractal API": {
                "connection": "API can operate on persistent data nodes",
                "benefit": "Seamless data access and manipulation"
            },
            "Generic Fractal System": {
                "connection": "Data nodes become part of fractal structure",
                "benefit": "Infinite exploration and navigation"
            },
            "Self-Referential Capabilities": {
                "connection": "Data describes itself completely",
                "benefit": "Meta-circular understanding and evolution"
            }
        }
        
        for system, details in integration_points.items():
            print(f"\n   🔗 {system}:")
            print(f"      📖 Connection: {details['connection']}")
            print(f"      ✅ Benefit: {details['benefit']}")
        
        print("\n🌟 Complete System Integration:")
        print("   • **Language Understanding**: Python, Markdown, and other languages")
        print("   • **Data Representation**: JSON, self-referential, seed data, and generic formats")
        print("   • **Fractal Navigation**: Infinite exploration of knowledge structure")
        print("   • **Self-Reference**: Complete system self-awareness")
        print("   • **Cross-Domain Harmony**: All systems work together seamlessly")
        print("   • **Continuous Evolution**: System grows and improves over time")

def main():
    """Main function to run the comprehensive persistent data demo"""
    
    print("🌟 Comprehensive Persistent Data Demo - Living Codex System")
    print("=" * 60)
    
    try:
        # Create and run the demo
        demo = ComprehensivePersistentDataDemo()
        demo.run_comprehensive_demo()
        demo.show_integration_summary()
        
    except Exception as e:
        print(f"❌ Error running comprehensive persistent data demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
