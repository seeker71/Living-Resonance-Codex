#!/usr/bin/env python3
"""
Real Codex Bootstrap Demo
Demonstrates bootstrapping the actual Living Codex specification markdown document
into the fractal system and shows how it can be explored and queried.
"""

import os
import re
from typing import List, Dict, Any
from codex_bootstrap_demo import CodexBootstrapDemo

class RealCodexBootstrapDemo:
    """Demonstrates bootstrapping the real Living Codex specification document"""
    
    def __init__(self):
        self.bootstrap_demo = CodexBootstrapDemo()
        self.fractal_system = self.bootstrap_demo.fractal_system
        self.spec_path = "../../docs/living_codex_specification.md"
        self._bootstrap_real_specification()
    
    def _bootstrap_real_specification(self):
        """Bootstrap the actual Living Codex specification document"""
        
        if not os.path.exists(self.spec_path):
            print(f"⚠️  Specification document not found at {self.spec_path}")
            print("   Using the sample content that was already bootstrapped")
            return
        
        print(f"🔧 Reading real specification document: {self.spec_path}")
        
        try:
            with open(self.spec_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            print(f"   📄 Document size: {len(content)} characters")
            print(f"   📝 Content preview: {content[:100]}...")
            
            # Parse the document structure
            self._parse_and_bootstrap_document(content)
            
        except Exception as e:
            print(f"❌ Error reading specification: {e}")
            print("   Using the sample content that was already bootstrapped")
    
    def _parse_and_bootstrap_document(self, content: str):
        """Parse the markdown document and bootstrap it into fractal nodes"""
        
        print("\n🔍 Parsing document structure...")
        
        # Split into sections
        sections = self._extract_sections(content)
        print(f"   📖 Found {len(sections)} major sections")
        
        # Bootstrap each section
        for section_id, section_data in sections.items():
            self._bootstrap_section(section_id, section_data)
        
        # Extract and bootstrap key concepts
        concepts = self._extract_key_concepts(content)
        print(f"   🧠 Found {len(concepts)} key concepts")
        
        for concept_id, concept_data in concepts.items():
            self._bootstrap_concept(concept_id, concept_data)
        
        # Create relationships between concepts
        self._create_concept_relationships_from_content(content)
        
        print("✅ Real specification document bootstrapped successfully!")
    
    def _extract_sections(self, content: str) -> Dict[str, Dict]:
        """Extract major sections from the markdown document"""
        
        sections = {}
        
        # Find all headers (## and ###)
        header_pattern = r'^(#{2,3})\s+(.+)$'
        matches = re.finditer(header_pattern, content, re.MULTILINE)
        
        current_section = None
        current_content = ""
        
        for match in matches:
            level = len(match.group(1))
            title = match.group(2).strip()
            
            if level == 2:  # Major section
                if current_section:
                    sections[current_section['id']] = current_section
                
                section_id = title.lower().replace(' ', '_').replace('-', '_')
                current_section = {
                    'id': section_id,
                    'title': title,
                    'level': level,
                    'content': "",
                    'subsections': []
                }
                current_content = ""
            elif level == 3 and current_section:  # Subsection
                current_section['subsections'].append({
                    'title': title,
                    'content': current_content.strip()
                })
                current_content = ""
        
        # Add the last section
        if current_section:
            sections[current_section['id']] = current_section
        
        return sections
    
    def _extract_key_concepts(self, content: str) -> Dict[str, Dict]:
        """Extract key concepts mentioned in the document"""
        
        concepts = {}
        
        # Look for key terms that are mentioned multiple times
        key_terms = [
            "ontology", "fractal", "resonance", "water", "consciousness",
            "archetype", "field", "pattern", "flow", "memory", "transformation",
            "void", "unity", "emergence", "awareness", "node", "codex"
        ]
        
        for term in key_terms:
            if term.lower() in content.lower():
                # Count occurrences
                count = len(re.findall(rf'\b{term}\b', content, re.IGNORECASE))
                if count > 0:
                    concepts[term] = {
                        'name': term.title(),
                        'occurrences': count,
                        'content': f"Key concept '{term}' mentioned {count} times in the specification"
                    }
        
        return concepts
    
    def _bootstrap_section(self, section_id: str, section_data: Dict):
        """Bootstrap a document section into fractal nodes"""
        
        # Create the section node
        section_node = self.fractal_system._create_generic_node(
            node_id=f"real_section_{section_id}",
            node_type="real_document_section",
            name=section_data['title'],
            content=section_data['content'][:200] + "..." if len(section_data['content']) > 200 else section_data['content'],
            parent_id="living_codex_specification",
            children=[],
            metadata={
                "section_type": "real_specification",
                "level": section_data['level'],
                "subsections_count": len(section_data['subsections']),
                "frequency": 528.0,
                "chakra": "solar_plexus",
                "water_state": "crystalline"
            },
            structure_info={
                "fractal_depth": 2,
                "section_type": "real_specification",
                "parent_document": "living_codex_specification",
                "source_file": self.spec_path
            }
        )
        
        # Add to codex specification's children
        self.fractal_system._add_child_to_parent("living_codex_specification", f"real_section_{section_id}")
        
        # Create subsection nodes
        for i, subsection in enumerate(section_data['subsections']):
            subsection_id = f"real_subsection_{section_id}_{i}"
            subsection_node = self.fractal_system._create_generic_node(
                node_id=subsection_id,
                node_type="real_document_subsection",
                name=subsection['title'],
                content=subsection['content'][:150] + "..." if len(subsection['content']) > 150 else subsection['content'],
                parent_id=f"real_section_{section_id}",
                children=[],
                metadata={
                    "subsection_type": "real_specification",
                    "parent_section": section_id,
                    "frequency": 417.0,
                    "chakra": "sacral",
                    "water_state": "quantum_coherent"
                },
                structure_info={
                    "fractal_depth": 3,
                    "subsection_type": "real_specification",
                    "parent_section": f"real_section_{section_id}",
                    "source_file": self.spec_path
                }
            )
            
            # Add to section's children
            self.fractal_system._add_child_to_parent(f"real_section_{section_id}", subsection_id)
    
    def _bootstrap_concept(self, concept_id: str, concept_data: Dict):
        """Bootstrap a key concept into fractal nodes"""
        
        concept_node = self.fractal_system._create_generic_node(
            node_id=f"real_concept_{concept_id}",
            node_type="real_document_concept",
            name=concept_data['name'],
            content=concept_data['content'],
            parent_id="living_codex_specification",
            children=[],
            metadata={
                "concept_type": "real_specification",
                "occurrences": concept_data['occurrences'],
                "frequency": 639.0,
                "chakra": "heart",
                "water_state": "liquid"
            },
            structure_info={
                "fractal_depth": 3,
                "concept_type": "real_specification",
                "parent_document": "living_codex_specification",
                "source_file": self.spec_path
            }
        )
        
        # Add to codex specification's children
        self.fractal_system._add_child_to_parent("living_codex_specification", f"real_concept_{concept_id}")
    
    def _create_concept_relationships_from_content(self, content: str):
        """Create relationships between concepts based on content proximity"""
        
        # Look for concepts that appear near each other
        key_concepts = ["ontology", "fractal", "resonance", "water", "consciousness"]
        
        for i, concept1 in enumerate(key_concepts):
            for concept2 in key_concepts[i+1:]:
                # Check if concepts appear in the same paragraph
                paragraphs = content.split('\n\n')
                
                for paragraph in paragraphs:
                    if (concept1.lower() in paragraph.lower() and 
                        concept2.lower() in paragraph.lower()):
                        
                        # Create a relationship
                        relationship_id = f"real_rel_{concept1}_{concept2}"
                        relationship_node = self.fractal_system._create_generic_node(
                            node_id=relationship_id,
                            node_type="real_document_relationship",
                            name=f"{concept1.title()} ↔ {concept2.title()}",
                            content=f"Concepts '{concept1}' and '{concept2}' appear together in the specification",
                            parent_id="living_codex_specification",
                            children=[],
                            metadata={
                                "source_concept": concept1,
                                "target_concept": concept2,
                                "relationship_type": "content_proximity",
                                "frequency": 528.0,
                                "chakra": "solar_plexus"
                            },
                            structure_info={
                                "fractal_depth": 3,
                                "relationship_type": "real_document",
                                "parent_document": "living_codex_specification",
                                "source_file": self.spec_path
                            }
                        )
                        
                        # Add to codex specification's children
                        self.fractal_system._add_child_to_parent("living_codex_specification", relationship_id)
                        break
    
    def demonstrate_real_specification_querying(self):
        """Demonstrate querying the real specification content"""
        
        print("\n🔍 Querying Real Specification Content")
        print("=" * 60)
        
        # Query for real document sections
        real_sections = self.fractal_system.query_system("", node_type="real_document_section")
        print(f"   📖 Real Document Sections: {real_sections['total_found']} found")
        
        for section in real_sections['results']:
            print(f"\n     🌟 {section['name']}")
            print(f"        Content: {section['content'][:80]}...")
            if 'metadata' in section:
                metadata = section['metadata']
                print(f"        Subsections: {metadata.get('subsections_count', 0)}")
                print(f"        Water State: {metadata.get('water_state', 'N/A')}")
        
        # Query for real concepts
        real_concepts = self.fractal_system.query_system("", node_type="real_document_concept")
        print(f"\n   🧠 Real Document Concepts: {real_concepts['total_found']} found")
        
        for concept in real_concepts['results']:
            print(f"\n     🌟 {concept['name']}")
            print(f"        Content: {concept['content']}")
            if 'metadata' in concept:
                metadata = concept['metadata']
                print(f"        Occurrences: {metadata.get('occurrences', 0)}")
                print(f"        Water State: {metadata.get('water_state', 'N/A')}")
        
        # Query for real relationships
        real_relationships = self.fractal_system.query_system("", node_type="real_document_relationship")
        print(f"\n   🔗 Real Document Relationships: {real_relationships['total_found']} found")
        
        for rel in real_relationships['results']:
            print(f"\n     • {rel['name']}")
            print(f"       {rel['content']}")
    
    def demonstrate_complete_system_querying(self):
        """Demonstrate querying the complete system (both sample and real content)"""
        
        print("\n🔍 Complete System Querying")
        print("=" * 60)
        
        # Query for key terms across all content
        key_queries = [
            "ontology",
            "fractal", 
            "resonance",
            "water",
            "consciousness",
            "archetype"
        ]
        
        for query in key_queries:
            print(f"\n❓ Query: '{query}'")
            result = self.fractal_system.query_system(query)
            
            print(f"   📍 Total Results: {result['total_found']}")
            
            # Categorize results by type
            type_counts = {}
            for res in result['results']:
                node_type = res['node_type']
                type_counts[node_type] = type_counts.get(node_type, 0) + 1
            
            print("   📊 Results by Type:")
            for node_type, count in type_counts.items():
                print(f"     • {node_type}: {count}")
            
            # Show top results
            if result['results']:
                print("   🌟 Top Results:")
                for i, res in enumerate(result['results'][:3]):
                    print(f"     {i+1}. {res['name']} (Type: {res['node_type']})")
                    print(f"        Content: {res['content'][:60]}...")
    
    def run_real_codex_demo(self):
        """Run the complete real codex bootstrap demonstration"""
        
        print("🌟 Real Living Codex Specification Bootstrap Demo")
        print("=" * 70)
        
        # Show system overview
        overview = self.fractal_system.get_system_overview()
        print(f"\n📊 System Overview After Real Bootstrap:")
        print(f"   📈 Total Nodes: {overview['total_nodes']}")
        print(f"   🧭 Max Fractal Depth: {overview['max_depth']}")
        print(f"   🌐 API Status: {overview['api_status']}")
        
        print("\n   📊 Node Type Distribution:")
        for node_type, count in overview['type_distribution'].items():
            print(f"     • {node_type}: {count} nodes")
        
        # Demonstrate real specification querying
        self.demonstrate_real_specification_querying()
        
        # Demonstrate complete system querying
        self.demonstrate_complete_system_querying()
        
        print("\n" + "=" * 70)
        print("🎉 Real Codex Bootstrap Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Real Living Codex specification document read and parsed")
        print("   • Document sections bootstrapped into fractal nodes")
        print("   • Key concepts extracted and represented as nodes")
        print("   • Content-based relationships created between concepts")
        print("   • Querying across both sample and real content")
        print("   • How the specification becomes a living, fractal document")
        print("   • Everything in the document represented as explorable nodes")

def main():
    """Main function to run the real codex bootstrap demo"""
    
    try:
        demo = RealCodexBootstrapDemo()
        demo.run_real_codex_demo()
    except Exception as e:
        print(f"❌ Error running real codex demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
