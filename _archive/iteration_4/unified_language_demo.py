#!/usr/bin/env python3
"""
Unified Language Demo
Comprehensive demonstration of Python and Markdown language support within the Living Codex system,
showing complete ontological mapping, self-referential capabilities, and cross-language integration.
"""

import asyncio
import json
from typing import List, Dict, Any, Optional
from enhanced_fractal_api import EnhancedFractalAPI, NodeCreate, NodeUpdate, QueryRequest, NavigationRequest

class UnifiedLanguageDemo:
    """Comprehensive demonstration of unified language ontology capabilities"""
    
    def __init__(self):
        self.api = EnhancedFractalAPI("fractal_system.db")
        print("🌟 Unified Language Demo - Living Codex System")
        print("=" * 60)
    
    async def run_comprehensive_demo(self):
        """Run the complete unified language demonstration"""
        
        print("🚀 Starting Comprehensive Unified Language Demo...")
        print()
        
        # Phase 1: System Overview
        await self._demonstrate_system_overview()
        
        # Phase 2: Core Language Ontology
        await self._demonstrate_language_ontology()
        
        # Phase 3: Self-Referential Capabilities
        await self._demonstrate_self_referential_capabilities()
        
        # Phase 4: Cross-Language Integration
        await self._demonstrate_cross_language_integration()
        
        # Phase 5: Advanced Querying and Navigation
        await self._demonstrate_advanced_capabilities()
        
        # Phase 6: System Evolution
        await self._demonstrate_system_evolution()
        
        print("\n" + "=" * 60)
        print("🎉 Comprehensive Unified Language Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Complete Python and Markdown language understanding")
        print("   • Three ontological layers: Ice (Blueprint), Water (Recipe), Vapor (Cells)")
        print("   • Self-referential documentation capabilities")
        print("   • Cross-language integration and harmony")
        print("   • Advanced querying and navigation")
        print("   • System evolution and growth")
        print("\n🚀 The Living Codex now has unified language support!")
    
    async def _demonstrate_system_overview(self):
        """Demonstrate the current system state and overview"""
        
        print("🔍 Phase 1: System Overview")
        print("-" * 40)
        
        try:
            # Get system overview
            system_overview = await self.api._get_system_overview()
            print(f"   📊 System Overview: {system_overview}")
            
            # Get system stats
            system_stats = await self.api._get_system_stats()
            print(f"   📈 System Stats: {system_stats}")
            
            # Count language-related nodes
            language_nodes = await self._count_language_nodes()
            print(f"   🌊 Language Nodes: {language_nodes}")
            
            print("   ✅ System overview demonstration complete!")
            
        except Exception as e:
            print(f"   ⚠️ System overview demonstration: {e}")
    
    async def _demonstrate_language_ontology(self):
        """Demonstrate the core language ontology structure"""
        
        print("\n🔍 Phase 2: Core Language Ontology")
        print("-" * 40)
        
        try:
            # Query for Python language ontology
            python_query = QueryRequest(
                query_type="type_based",
                query_params={"node_type": "python_language_ontology"}
            )
            python_results = await self.api._query_knowledge(python_query)
            print(f"   🐍 Python Ontology: {len(python_results.get('results', []))} nodes found")
            
            # Query for Markdown language ontology
            markdown_query = QueryRequest(
                query_type="type_based",
                query_params={"node_type": "markdown_language_ontology"}
            )
            markdown_results = await self.api._query_knowledge(markdown_query)
            print(f"   📝 Markdown Ontology: {len(markdown_results.get('results', []))} nodes found")
            
            # Query for unified language ontology
            unified_query = QueryRequest(
                query_type="type_based",
                query_params={"node_type": "unified_language_ontology"}
            )
            unified_results = await self.api._query_knowledge(unified_query)
            print(f"   🌊 Unified Ontology: {len(unified_results.get('results', []))} nodes found")
            
            # Show the three ontological layers
            await self._demonstrate_ontological_layers()
            
            print("   ✅ Language ontology demonstration complete!")
            
        except Exception as e:
            print(f"   ⚠️ Language ontology demonstration: {e}")
    
    async def _demonstrate_ontological_layers(self):
        """Demonstrate the three ontological layers (Ice, Water, Vapor)"""
        
        print("\n      🔍 Three Ontological Layers:")
        
        # Ice Layer (Blueprint)
        ice_query = QueryRequest(
            query_type="metadata_based",
            query_params={"metadata_key": "water_state", "metadata_value": "ice"}
        )
        ice_results = await self.api._query_knowledge(ice_query)
        print(f"         🧊 Ice Layer (Blueprint): {len(ice_results.get('results', []))} nodes")
        
        # Water Layer (Recipe)
        water_query = QueryRequest(
            query_type="metadata_based",
            query_params={"metadata_key": "water_state", "metadata_value": "liquid"}
        )
        water_results = await self.api._query_knowledge(water_query)
        print(f"         💧 Water Layer (Recipe): {len(water_results.get('results', []))} nodes")
        
        # Vapor Layer (Cells)
        vapor_query = QueryRequest(
            query_type="metadata_based",
            query_params={"metadata_key": "water_state", "metadata_value": "vapor"}
        )
        vapor_results = await self.api._query_knowledge(vapor_query)
        print(f"         🌫️ Vapor Layer (Cells): {len(vapor_results.get('results', []))} nodes")
    
    async def _demonstrate_self_referential_capabilities(self):
        """Demonstrate self-referential documentation capabilities"""
        
        print("\n🔍 Phase 3: Self-Referential Capabilities")
        print("-" * 40)
        
        try:
            # Query for self-referential capabilities
            self_ref_query = QueryRequest(
                query_type="type_based",
                query_params={"node_type": "self_referential_capabilities"}
            )
            self_ref_results = await self.api._query_knowledge(self_ref_query)
            print(f"   🔗 Self-Referential Capabilities: {len(self_ref_results.get('results', []))} nodes found")
            
            # Query for system self-description
            system_desc_query = QueryRequest(
                query_type="metadata_based",
                query_params={"metadata_key": "capability_type", "metadata_value": "self_documentation"}
            )
            system_desc_results = await self.api._query_knowledge(system_desc_query)
            print(f"   📚 System Self-Description: {len(system_desc_results.get('results', []))} nodes found")
            
            # Query for living documentation
            living_doc_query = QueryRequest(
                query_type="metadata_based",
                query_params={"metadata_key": "representation", "metadata_value": "cells"}
            )
            living_doc_results = await self.api._query_knowledge(living_doc_query)
            print(f"   🌱 Living Documentation: {len(living_doc_results.get('results', []))} nodes found")
            
            # Demonstrate how the system documents itself
            await self._demonstrate_system_self_documentation()
            
            print("   ✅ Self-referential capabilities demonstration complete!")
            
        except Exception as e:
            print(f"   ⚠️ Self-referential capabilities demonstration: {e}")
    
    async def _demonstrate_system_self_documentation(self):
        """Demonstrate how the system documents itself"""
        
        print("\n      🔍 System Self-Documentation:")
        
        # Find nodes that describe the system
        system_nodes_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "Living Codex System"}
        )
        system_nodes_results = await self.api._query_knowledge(system_nodes_query)
        print(f"         📖 System Description Nodes: {len(system_nodes_results.get('results', []))} found")
        
        # Find nodes that describe the ontology
        ontology_nodes_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "ontological"}
        )
        ontology_nodes_results = await self.api._query_knowledge(ontology_nodes_query)
        print(f"         🧬 Ontology Description Nodes: {len(ontology_nodes_results.get('results', []))} found")
        
        # Find nodes that describe the fractal structure
        fractal_nodes_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "fractal"}
        )
        fractal_nodes_results = await self.api._query_knowledge(fractal_nodes_query)
        print(f"         🌊 Fractal Description Nodes: {len(fractal_nodes_results.get('results', []))} found")
    
    async def _demonstrate_cross_language_integration(self):
        """Demonstrate cross-language integration capabilities"""
        
        print("\n🔍 Phase 4: Cross-Language Integration")
        print("-" * 40)
        
        try:
            # Query for cross-language integration
            cross_lang_query = QueryRequest(
                query_type="metadata_based",
                query_params={"metadata_key": "capability_type", "metadata_value": "cross_language"}
            )
            cross_lang_results = await self.api._query_knowledge(cross_lang_query)
            print(f"   🌐 Cross-Language Integration: {len(cross_lang_results.get('results', []))} nodes found")
            
            # Show how Python and Markdown work together
            await self._demonstrate_python_markdown_integration()
            
            # Show unified ontological framework
            await self._demonstrate_unified_framework()
            
            print("   ✅ Cross-language integration demonstration complete!")
            
        except Exception as e:
            print(f"   ⚠️ Cross-language integration demonstration: {e}")
    
    async def _demonstrate_python_markdown_integration(self):
        """Demonstrate how Python and Markdown work together"""
        
        print("\n      🔍 Python-Markdown Integration:")
        
        # Find nodes that reference both Python and Markdown
        python_markdown_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "Python.*Markdown|Markdown.*Python"}
        )
        python_markdown_results = await self.api._query_knowledge(python_markdown_query)
        print(f"         🔗 Python-Markdown References: {len(python_markdown_results.get('results', []))} found")
        
        # Find nodes that show language comparison
        comparison_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "three.*layer|ontological.*layers"}
        )
        comparison_results = await self.api._query_knowledge(comparison_query)
        print(f"         📊 Language Comparison Nodes: {len(comparison_results.get('results', []))} found")
        
        # Find nodes that demonstrate unified understanding
        unified_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "unified.*understanding|common.*framework"}
        )
        unified_results = await self.api._query_knowledge(unified_query)
        print(f"         🌊 Unified Understanding Nodes: {len(unified_results.get('results', []))} found")
    
    async def _demonstrate_unified_framework(self):
        """Demonstrate the unified ontological framework"""
        
        print("\n      🔍 Unified Ontological Framework:")
        
        # Find nodes that represent the unified framework
        framework_query = QueryRequest(
            query_type="type_based",
            query_params={"node_type": "unified_language_ontology"}
        )
        framework_results = await self.api._query_knowledge(framework_query)
        print(f"         🏗️ Framework Root Nodes: {len(framework_results.get('results', []))} found")
        
        # Find nodes that show the three-layer model
        three_layer_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "Ice.*Water.*Vapor|Blueprint.*Recipe.*Cells"}
        )
        three_layer_results = await self.api._query_knowledge(three_layer_query)
        print(f"         🌊 Three-Layer Model Nodes: {len(three_layer_results.get('results', []))} found")
        
        # Find nodes that demonstrate consistency
        consistency_query = QueryRequest(
            query_type="metadata_based",
            query_params={"metadata_key": "abstraction_level", "metadata_value": "meta_implementation"}
        )
        consistency_results = await self.api._query_knowledge(consistency_query)
        print(f"         🔄 Consistency Nodes: {len(consistency_results.get('results', []))} found")
    
    async def _demonstrate_advanced_capabilities(self):
        """Demonstrate advanced querying and navigation capabilities"""
        
        print("\n🔍 Phase 5: Advanced Capabilities")
        print("-" * 40)
        
        try:
            # Demonstrate fractal navigation
            await self._demonstrate_fractal_navigation()
            
            # Demonstrate metadata-based querying
            await self._demonstrate_metadata_querying()
            
            # Demonstrate relationship exploration
            await self._demonstrate_relationship_exploration()
            
            print("   ✅ Advanced capabilities demonstration complete!")
            
        except Exception as e:
            print(f"   ⚠️ Advanced capabilities demonstration: {e}")
    
    async def _demonstrate_fractal_navigation(self):
        """Demonstrate fractal navigation capabilities"""
        
        print("\n      🔍 Fractal Navigation:")
        
        # Navigate to different fractal depths
        for depth in [4, 5, 6, 7]:
            depth_query = QueryRequest(
                query_type="structure_based",
                query_params={"fractal_depth": depth}
            )
            depth_results = await self.api._query_knowledge(depth_query)
            print(f"         🌊 Depth {depth}: {len(depth_results.get('results', []))} nodes")
        
        # Show fractal structure exploration
        fractal_structure = await self.api._get_fractal_structure()
        print(f"         🏗️ Fractal Structure: {len(fractal_structure.get('layers', []))} layers")
    
    async def _demonstrate_metadata_querying(self):
        """Demonstrate metadata-based querying capabilities"""
        
        print("\n      🔍 Metadata Querying:")
        
        # Query by frequency ranges
        frequency_ranges = [
            (963.0, "Crown Chakra"),
            (852.0, "Third Eye Chakra"),
            (741.0, "Throat Chakra"),
            (639.0, "Heart Chakra")
        ]
        
        for freq, chakra in frequency_ranges:
            freq_query = QueryRequest(
                query_type="metadata_based",
                query_params={"metadata_key": "frequency", "metadata_value": freq}
            )
            freq_results = await self.api._query_knowledge(freq_query)
            print(f"         🎵 {chakra} ({freq}Hz): {len(freq_results.get('results', []))} nodes")
    
    async def _demonstrate_relationship_exploration(self):
        """Demonstrate relationship exploration capabilities"""
        
        print("\n      🔍 Relationship Exploration:")
        
        # Find parent-child relationships
        parent_child_query = QueryRequest(
            query_type="relationship_based",
            query_params={"relationship_type": "parent_child"}
        )
        parent_child_results = await self.api._query_knowledge(parent_child_query)
        print(f"         👥 Parent-Child Relationships: {len(parent_child_results.get('results', []))} found")
        
        # Find cross-references
        cross_ref_query = QueryRequest(
            query_type="relationship_based",
            query_params={"relationship_type": "cross_reference"}
        )
        cross_ref_results = await self.api._query_knowledge(cross_ref_query)
        print(f"         🔗 Cross-References: {len(cross_ref_results.get('results', []))} found")
    
    async def _demonstrate_system_evolution(self):
        """Demonstrate system evolution and growth capabilities"""
        
        print("\n🔍 Phase 6: System Evolution")
        print("-" * 40)
        
        try:
            # Show system growth
            await self._demonstrate_system_growth()
            
            # Show evolution patterns
            await self._demonstrate_evolution_patterns()
            
            # Show future pathways
            await self._demonstrate_future_pathways()
            
            print("   ✅ System evolution demonstration complete!")
            
        except Exception as e:
            print(f"   ⚠️ System evolution demonstration: {e}")
    
    async def _demonstrate_system_growth(self):
        """Demonstrate how the system grows and evolves"""
        
        print("\n      🔍 System Growth:")
        
        # Find nodes that represent growth
        growth_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "evolve|growth|expand|develop"}
        )
        growth_results = await self.api._query_knowledge(growth_query)
        print(f"         🌱 Growth-Related Nodes: {len(growth_results.get('results', []))} found")
        
        # Find nodes that represent evolution
        evolution_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "evolution|evolutionary|adapt"}
        )
        evolution_results = await self.api._query_knowledge(evolution_query)
        print(f"         🔄 Evolution-Related Nodes: {len(evolution_results.get('results', []))} found")
    
    async def _demonstrate_evolution_patterns(self):
        """Demonstrate evolution patterns in the system"""
        
        print("\n      🔍 Evolution Patterns:")
        
        # Find nodes that represent patterns
        patterns_query = QueryRequest(
            query_type="metadata_based",
            query_params={"metadata_key": "paradigm", "metadata_value": "evolution"}
        )
        patterns_results = await self.api._query_knowledge(patterns_query)
        print(f"         📊 Evolution Pattern Nodes: {len(patterns_results.get('results', []))} found")
        
        # Find nodes that represent future evolution
        future_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "future|pathway|next.*step"}
        )
        future_results = await self.api._query_knowledge(future_query)
        print(f"         🔮 Future Evolution Nodes: {len(future_results.get('results', []))} found")
    
    async def _demonstrate_future_pathways(self):
        """Demonstrate future evolution pathways"""
        
        print("\n      🔍 Future Evolution Pathways:")
        
        # Find nodes that represent extended language support
        extended_lang_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "extended.*language|more.*languages"}
        )
        extended_lang_results = await self.api._query_knowledge(extended_lang_query)
        print(f"         🌐 Extended Language Support: {len(extended_lang_results.get('results', []))} nodes")
        
        # Find nodes that represent enhanced self-reference
        enhanced_self_query = QueryRequest(
            query_type="content_based",
            query_params={"content_pattern": "enhanced.*self|automated.*documentation"}
        )
        enhanced_self_results = await self.api._query_knowledge(enhanced_self_query)
        print(f"         🔗 Enhanced Self-Reference: {len(enhanced_self_results.get('results', []))} nodes")
    
    async def _count_language_nodes(self):
        """Count the total number of language-related nodes"""
        
        try:
            # Count nodes by type
            language_types = [
                "python_language_ontology",
                "markdown_language_ontology", 
                "unified_language_ontology",
                "grammar_component",
                "semantics_component",
                "implementation_component",
                "syntax_component",
                "module_blueprint",
                "module_implementation",
                "document_blueprint",
                "document_implementation",
                "code_content",
                "document_content"
            ]
            
            total_count = 0
            for lang_type in language_types:
                query = QueryRequest(
                    query_type="type_based",
                    query_params={"node_type": lang_type}
                )
                results = await self.api._query_knowledge(query)
                count = len(results.get('results', []))
                total_count += count
            
            return total_count
            
        except Exception as e:
            print(f"   ⚠️ Error counting language nodes: {e}")
            return 0

def main():
    """Main function to run the unified language demo"""
    
    print("🌟 Unified Language Demo - Living Codex System")
    print("=" * 60)
    
    try:
        # Create and run the demo
        demo = UnifiedLanguageDemo()
        
        # Run the comprehensive demonstration
        asyncio.run(demo.run_comprehensive_demo())
        
    except Exception as e:
        print(f"❌ Error running unified language demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
