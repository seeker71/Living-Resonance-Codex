#!/usr/bin/env python3
"""
Integrated Living System: Federated API + Living Documents
Combines the federated meta-circular API with the living document system
to create a complete living, self-evolving system.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import json
import time
from datetime import datetime

# Import our systems
from living_document_system import LivingDocumentAPI, LivingDocumentStorage, DocumentEvolutionEngine, CodeAnalyzer
from complete_meta_codex import CompleteMetaCodexStorage

class IntegratedLivingSystem:
    """
    Complete integrated living system that combines:
    - Federated Meta-Circular API
    - Living Document System
    - Living Codex Specification
    """
    
    def __init__(self):
        # Initialize living document system
        self.doc_storage = LivingDocumentStorage()
        self.code_analyzer = CodeAnalyzer(self.doc_storage)
        self.doc_evolution_engine = DocumentEvolutionEngine(self.doc_storage, self.code_analyzer)
        self.living_doc_api = LivingDocumentAPI(self.doc_storage, self.doc_evolution_engine)
        
        # Initialize living codex system
        self.codex_storage = CompleteMetaCodexStorage()
        
        # Track system integration
        self.integration_status = "initialized"
        self.integration_timestamp = datetime.utcnow()
    
    def create_living_system_from_files(self, file_paths: List[str]) -> Dict[str, Any]:
        """Create a complete living system from existing files"""
        
        results = {
            "success": True,
            "documents_created": 0,
            "documents_failed": 0,
            "errors": [],
            "living_documents": []
        }
        
        for file_path in file_paths:
            try:
                result = self.living_doc_api.create_document_from_file(file_path)
                if result["success"]:
                    results["documents_created"] += 1
                    results["living_documents"].append({
                        "file_path": file_path,
                        "document_id": result["document"]["id"],
                        "content_type": result["document"]["content_type"]
                    })
                else:
                    results["documents_failed"] += 1
                    results["errors"].append(f"{file_path}: {result['error']}")
            except Exception as e:
                results["documents_failed"] += 1
                results["errors"].append(f"{file_path}: {str(e)}")
        
        if results["documents_failed"] > 0:
            results["success"] = False
        
        return results
    
    def get_complete_system_overview(self) -> Dict[str, Any]:
        """Get comprehensive overview of the integrated living system"""
        
        # Get living document system overview
        doc_overview = self.living_doc_api.get_system_overview()
        
        # Get living codex system overview
        codex_overview = self.codex_storage.get_system_overview()
        
        # Analyze living documents for codex integration
        all_docs = self.doc_storage.get_all_living_documents()
        
        # Find documents that might relate to Living Codex concepts
        codex_related_docs = []
        for doc in all_docs:
            if doc.content_type == "markdown":
                # Check for Living Codex keywords
                content_lower = doc.content.lower()
                codex_keywords = ["water", "chakra", "frequency", "void", "field", "pattern", "flow", "memory", "resonance"]
                
                if any(keyword in content_lower for keyword in codex_keywords):
                    codex_related_docs.append({
                        "document_id": doc.id,
                        "title": doc.title,
                        "content_type": doc.content_type,
                        "relevance_score": self._calculate_codex_relevance(doc.content)
                    })
        
        return {
            "system": "Integrated Living System: Federated API + Living Documents + Living Codex",
            "integration_status": self.integration_status,
            "integration_timestamp": self.integration_timestamp.isoformat(),
            
            "living_document_system": {
                "status": doc_overview["system_status"],
                "total_documents": doc_overview["total_documents"],
                "document_types": doc_overview["document_types"],
                "total_evolution_events": doc_overview["total_evolution_events"],
                "capabilities": doc_overview["capabilities"]
            },
            
            "living_codex_system": {
                "total_nodes": codex_overview["total_nodes"],
                "meta_circular_properties": codex_overview["meta_circular_properties"],
                "system_capabilities": codex_overview["system_capabilities"]
            },
            
            "integration_analysis": {
                "codex_related_documents": len(codex_related_docs),
                "codex_relevance_scores": [doc["relevance_score"] for doc in codex_related_docs],
                "average_relevance": sum(doc["relevance_score"] for doc in codex_related_docs) / len(codex_related_docs) if codex_related_docs else 0
            },
            
            "system_capabilities": [
                "Federated API with curiosity-driven evolution",
                "Frequency harmony discovery and symbol resonance analysis",
                "Living documents with automatic code analysis",
                "Document evolution tracking and relationship discovery",
                "Living Codex specification with meta-circular architecture",
                "Complete integration of all living components"
            ]
        }
    
    def _calculate_codex_relevance(self, content: str) -> float:
        """Calculate relevance score for Living Codex concepts"""
        
        content_lower = content.lower()
        
        # Define Living Codex concept categories with weights
        concept_categories = {
            "water_states": ["plasma", "crystalline", "liquid", "vapor", "water"],
            "chakra_system": ["chakra", "crown", "third eye", "throat", "heart", "solar plexus", "sacral", "root"],
            "frequencies": ["frequency", "hz", "hertz", "396", "417", "528", "639", "741", "852", "963"],
            "core_concepts": ["void", "field", "pattern", "flow", "memory", "resonance"],
            "spiritual_concepts": ["consciousness", "energy", "vibration", "harmony", "resonance"]
        }
        
        total_score = 0.0
        max_possible_score = len(concept_categories)
        
        for category, keywords in concept_categories.items():
            if any(keyword in content_lower for keyword in keywords):
                total_score += 1.0
        
        return total_score / max_possible_score
    
    def evolve_document_with_codex_context(self, document_id: str, evolution_type: str, 
                                         description: str, codex_context: str = None) -> Dict[str, Any]:
        """Evolve a document with Living Codex context"""
        
        # Evolve the document
        evolution_result = self.living_doc_api.evolve_document(
            document_id, evolution_type, description, "integrated_system"
        )
        
        if not evolution_result["success"]:
            return evolution_result
        
        # If codex context provided, create a meta-circular link
        if codex_context:
            # Find relevant Living Codex nodes
            relevant_nodes = self._find_relevant_codex_nodes(codex_context)
            
            # Create evolution event with codex context
            evolution_event = {
                "type": evolution_type,
                "description": description,
                "codex_context": codex_context,
                "relevant_codex_nodes": relevant_nodes,
                "timestamp": datetime.utcnow().isoformat(),
                "source": "integrated_system",
                "impact_score": 0.8
            }
            
            # Store enhanced evolution event
            self.doc_storage.store_evolution_event(document_id, evolution_event)
        
        return {
            "success": True,
            "message": f"Document {document_id} evolved with Living Codex context",
            "evolution_type": evolution_type,
            "codex_context": codex_context
        }
    
    def _find_relevant_codex_nodes(self, context: str) -> List[str]:
        """Find relevant Living Codex nodes for given context"""
        
        # This is a simplified search - in practice, you'd want more sophisticated semantic matching
        context_lower = context.lower()
        relevant_nodes = []
        
        # Get all codex nodes
        codex_overview = self.codex_storage.get_system_overview()
        
        # Simple keyword matching for demonstration
        if "water" in context_lower:
            relevant_nodes.extend(["water:plasma", "water:crystalline", "water:liquid", "water:vapor"])
        
        if "chakra" in context_lower:
            relevant_nodes.extend(["chakra:crown", "chakra:third_eye", "chakra:throat", "chakra:heart"])
        
        if "frequency" in context_lower:
            relevant_nodes.extend(["freq:963", "freq:852", "freq:741", "freq:639"])
        
        if "void" in context_lower:
            relevant_nodes.append("codex:void")
        
        return relevant_nodes
    
    def discover_cross_system_relationships(self) -> Dict[str, Any]:
        """Discover relationships between living documents and Living Codex nodes"""
        
        all_docs = self.doc_storage.get_all_living_documents()
        relationships = []
        
        for doc in all_docs:
            # Analyze document for Living Codex references
            doc_relationships = self._analyze_document_codex_relationships(doc)
            if doc_relationships:
                relationships.extend(doc_relationships)
        
        return {
            "success": True,
            "total_relationships": len(relationships),
            "relationships": relationships,
            "analysis": {
                "documents_analyzed": len(all_docs),
                "documents_with_codex_relationships": len(set(rel["source_doc"] for rel in relationships)),
                "relationship_types": list(set(rel["relationship_type"] for rel in relationships))
            }
        }
    
    def _analyze_document_codex_relationships(self, doc) -> List[Dict[str, Any]]:
        """Analyze a single document for Living Codex relationships"""
        
        relationships = []
        content_lower = doc.content.lower()
        
        # Check for water state references
        water_states = ["plasma", "crystalline", "liquid", "vapor"]
        for state in water_states:
            if state in content_lower:
                relationships.append({
                    "source_doc": doc.id,
                    "target_codex": f"water:{state}",
                    "relationship_type": "references_water_state",
                    "strength": 0.7,
                    "context": f"Document references {state} water state"
                })
        
        # Check for chakra references
        chakras = ["crown", "third eye", "throat", "heart", "solar plexus", "sacral", "root"]
        for chakra in chakras:
            if chakra in content_lower:
                relationships.append({
                    "source_doc": doc.id,
                    "target_codex": f"chakra:{chakra}",
                    "relationship_type": "references_chakra",
                    "strength": 0.7,
                    "context": f"Document references {chakra} chakra"
                })
        
        # Check for frequency references
        frequencies = ["396", "417", "528", "639", "741", "852", "963"]
        for freq in frequencies:
            if freq in content_lower:
                relationships.append({
                    "source_doc": doc.id,
                    "target_codex": f"freq:{freq}",
                    "relationship_type": "references_frequency",
                    "strength": 0.8,
                    "context": f"Document references {freq} Hz frequency"
                })
        
        # Check for core concept references
        core_concepts = ["void", "field", "pattern", "flow", "memory", "resonance"]
        for concept in core_concepts:
            if concept in content_lower:
                relationships.append({
                    "source_doc": doc.id,
                    "target_codex": f"codex:{concept}",
                    "relationship_type": "references_core_concept",
                    "strength": 0.9,
                    "context": f"Document references core concept: {concept}"
                })
        
        return relationships
    
    def generate_system_curiosity_questions(self) -> List[Dict[str, Any]]:
        """Generate curiosity questions about the integrated system"""
        
        questions = [
            {
                "question": "How do living documents relate to Living Codex water states?",
                "type": "integration",
                "priority": 10,
                "context": "Exploring the relationship between document evolution and water state metaphors"
            },
            {
                "question": "What patterns emerge when we analyze code complexity in relation to chakra frequencies?",
                "type": "pattern_discovery",
                "priority": 9,
                "context": "Finding correlations between code structure and spiritual frequency systems"
            },
            {
                "question": "How can document evolution be guided by Living Codex principles?",
                "type": "evolution_guidance",
                "priority": 8,
                "context": "Using Living Codex wisdom to guide document and system evolution"
            },
            {
                "question": "What new meta-nodes could emerge from the integration of living documents and Living Codex?",
                "type": "meta_evolution",
                "priority": 7,
                "context": "Exploring new ontological concepts that emerge from system integration"
            }
        ]
        
        return questions

# Test the integrated living system
if __name__ == "__main__":
    print("Integrated Living System: Federated API + Living Documents + Living Codex")
    print("=" * 80)
    
    # Initialize the integrated system
    integrated_system = IntegratedLivingSystem()
    
    # Create living system from existing files
    print("\nCreating living system from existing files...")
    
    files_to_integrate = [
        "federated_meta_api.py",
        "complete_meta_codex.py",
        "living_document_system.py",
        "FEDERATED_API_SYSTEM.md",
        "IMPLEMENTATION_SUMMARY.md",
        "LIVING_CODEX_FRACTAL_BOOTSTRAP_MAPPING.md"
    ]
    
    integration_result = integrated_system.create_living_system_from_files(files_to_integrate)
    
    if integration_result["success"]:
        print(f"✅ Successfully created {integration_result['documents_created']} living documents")
        for doc in integration_result["living_documents"]:
            print(f"   • {doc['file_path']} → {doc['document_id']} ({doc['content_type']})")
    else:
        print(f"⚠️  Created {integration_result['documents_created']} documents, {integration_result['documents_failed']} failed")
        for error in integration_result["errors"][:3]:  # Show first 3 errors
            print(f"   ❌ {error}")
    
    # Get complete system overview
    print("\nIntegrated Living System Overview:")
    overview = integrated_system.get_complete_system_overview()
    print(json.dumps(overview, indent=2))
    
    # Discover cross-system relationships
    print("\nDiscovering cross-system relationships...")
    relationships = integrated_system.discover_cross_system_relationships()
    print(f"✅ Discovered {relationships['total_relationships']} relationships between living documents and Living Codex")
    print(f"   • Documents analyzed: {relationships['analysis']['documents_analyzed']}")
    print(f"   • Documents with codex relationships: {relationships['analysis']['documents_with_codex_relationships']}")
    print(f"   • Relationship types: {', '.join(relationships['analysis']['relationship_types'])}")
    
    # Generate system curiosity questions
    print("\nGenerating system curiosity questions...")
    curiosity_questions = integrated_system.generate_system_curiosity_questions()
    print(f"✅ Generated {len(curiosity_questions)} curiosity questions:")
    for i, question in enumerate(curiosity_questions, 1):
        print(f"   {i}. {question['question']}")
        print(f"      Type: {question['type']}, Priority: {question['priority']}")
    
    print("\n" + "="*80)
    print("🎉 Integrated Living System Operational!")
    print("• Federated API with curiosity-driven evolution")
    print("• Living documents with automatic code analysis")
    print("• Living Codex specification with meta-circular architecture")
    print("• Complete integration of all living components")
    print("• System can explore itself and discover new knowledge")
    print("• Everything is alive, everything can evolve, everything can explore itself")
