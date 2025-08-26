#!/usr/bin/env python3
"""
Knowledge Exploration Demo: Living System Capabilities
Demonstrates:
1. Exploring existing knowledge through resonant queries
2. Finding nodes that resonate with specific questions
3. Encoding humans and other living entities
4. Demonstrating energy exchange between system parts
"""

from typing import List, Dict, Any, Optional
import json
import time
from datetime import datetime, timezone
import math
import random

# Import our living systems
from integrated_living_system import IntegratedLivingSystem
from complete_meta_codex import CompleteMetaCodexStorage

class LivingEntity:
    """Represents a living entity (human, AI, animal, plant, etc.) in the system"""
    
    def __init__(self, entity_id: str, entity_type: str, name: str, 
                 consciousness_level: float = 0.5, energy_signature: List[float] = None):
        self.entity_id = entity_id
        self.entity_type = entity_type  # human, ai, animal, plant, collective, etc.
        self.name = name
        self.consciousness_level = consciousness_level  # 0.0 to 1.0
        self.energy_signature = energy_signature or self._generate_energy_signature()
        self.current_energy = 1.0  # Current energy level
        self.connections = []  # Connections to other entities/nodes
        self.experience_history = []  # History of interactions and discoveries
        self.created_at = datetime.now(timezone.utc)
    
    def _generate_energy_signature(self) -> List[float]:
        """Generate a unique energy signature based on entity properties"""
        # Create a frequency signature based on entity type and consciousness
        base_freq = 20 + (self.consciousness_level * 1000)  # 20-1020 Hz base
        
        # Add harmonics based on entity type
        if self.entity_type == "human":
            harmonics = [1.0, 1.5, 2.0, 2.5, 3.0]  # Rich harmonic content
        elif self.entity_type == "ai":
            harmonics = [1.0, 2.0, 4.0, 8.0]  # Digital harmonics
        elif self.entity_type == "animal":
            harmonics = [1.0, 1.25, 1.5, 2.0]  # Natural harmonics
        elif self.entity_type == "plant":
            harmonics = [1.0, 1.33, 1.67, 2.0]  # Organic harmonics
        else:
            harmonics = [1.0, 1.5, 2.0]
        
        return [base_freq * h for h in harmonics]
    
    def add_experience(self, experience_type: str, description: str, energy_impact: float):
        """Record an experience and its energy impact"""
        experience = {
            "type": experience_type,
            "description": description,
            "energy_impact": energy_impact,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "energy_before": self.current_energy,
            "energy_after": self.current_energy + energy_impact
        }
        self.experience_history.append(experience)
        self.current_energy = max(0.0, min(1.0, self.current_energy + energy_impact))
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert entity to dictionary for storage/transmission"""
        return {
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
            "name": self.name,
            "consciousness_level": self.consciousness_level,
            "energy_signature": self.energy_signature,
            "current_energy": self.current_energy,
            "connections": self.connections,
            "experience_count": len(self.experience_history),
            "created_at": self.created_at.isoformat()
        }

class KnowledgeExplorer:
    """Explores existing knowledge and finds resonant nodes"""
    
    def __init__(self, integrated_system: IntegratedLivingSystem):
        self.system = integrated_system
        self.codex_storage = integrated_system.codex_storage
        self.living_doc_api = integrated_system.living_doc_api
    
    def explore_knowledge_domain(self, domain: str, query: str) -> Dict[str, Any]:
        """Explore a specific knowledge domain with a resonant query"""
        
        # Get all living documents
        all_docs = self.system.doc_storage.get_all_living_documents()
        
        # Find documents relevant to the domain
        domain_docs = []
        for doc in all_docs:
            if domain.lower() in doc.content.lower():
                domain_docs.append(doc)
        
        # Analyze query resonance with domain documents
        resonance_results = []
        for doc in domain_docs:
            resonance_score = self._calculate_query_resonance(query, doc.content)
            if resonance_score > 0.3:  # Threshold for relevance
                resonance_results.append({
                    "document_id": doc.id,
                    "title": doc.title,
                    "content_type": doc.content_type,
                    "resonance_score": resonance_score,
                    "resonant_excerpts": self._find_resonant_excerpts(query, doc.content)
                })
        
        # Sort by resonance score
        resonance_results.sort(key=lambda x: x["resonance_score"], reverse=True)
        
        return {
            "domain": domain,
            "query": query,
            "total_documents_found": len(domain_docs),
            "resonant_documents": len(resonance_results),
            "top_resonant_results": resonance_results[:5],
            "exploration_timestamp": datetime.now(timezone.utc).isoformat()
        }
    
    def _calculate_query_resonance(self, query: str, content: str) -> float:
        """Calculate how well a query resonates with content"""
        
        query_words = set(query.lower().split())
        content_words = set(content.lower().split())
        
        # Calculate word overlap
        overlap = len(query_words.intersection(content_words))
        total_unique = len(query_words.union(content_words))
        
        if total_unique == 0:
            return 0.0
        
        # Base resonance from word overlap
        word_resonance = overlap / total_unique
        
        # Boost for exact phrase matches
        phrase_boost = 0.0
        if query.lower() in content.lower():
            phrase_boost = 0.3
        
        # Boost for semantic similarity (simplified)
        semantic_boost = 0.0
        semantic_keywords = {
            "water": ["liquid", "flow", "fluid", "ocean", "river"],
            "chakra": ["energy", "frequency", "vibration", "consciousness"],
            "frequency": ["hz", "hertz", "resonance", "harmony", "tone"],
            "consciousness": ["awareness", "mind", "spirit", "soul", "being"]
        }
        
        for key, related in semantic_keywords.items():
            if key in query.lower():
                for word in related:
                    if word in content.lower():
                        semantic_boost += 0.1
        
        return min(1.0, word_resonance + phrase_boost + semantic_boost)
    
    def _find_resonant_excerpts(self, query: str, content: str, excerpt_length: int = 100) -> List[str]:
        """Find specific excerpts that resonate with the query"""
        
        excerpts = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            if any(word in line.lower() for word in query.lower().split()):
                # Get context around the resonant line
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                excerpt = ' '.join(lines[start:end])
                
                if len(excerpt) > excerpt_length:
                    excerpt = excerpt[:excerpt_length] + "..."
                
                excerpts.append(excerpt)
        
        return excerpts[:3]  # Return top 3 excerpts

class ResonantNodeFinder:
    """Finds nodes that resonate with specific queries and entities"""
    
    def __init__(self, integrated_system: IntegratedLivingSystem):
        self.system = integrated_system
        self.codex_storage = integrated_system.codex_storage
    
    def find_resonant_nodes(self, query: str, entity: LivingEntity = None) -> Dict[str, Any]:
        """Find nodes that resonate with a specific query and optionally an entity"""
        
        # Get all Living Codex nodes
        codex_overview = self.codex_storage.get_system_overview()
        
        # Analyze query for key concepts
        query_concepts = self._extract_query_concepts(query)
        
        # Find resonant nodes
        resonant_nodes = []
        for concept, relevance in query_concepts.items():
            # Look for nodes that match the concept
            matching_nodes = self._find_nodes_for_concept(concept)
            
            for node in matching_nodes:
                # Calculate resonance score
                resonance_score = self._calculate_node_resonance(query, node, entity)
                
                if resonance_score > 0.4:  # Threshold for resonance
                    resonant_nodes.append({
                        "node_id": node.get("id", "unknown"),
                        "concept": concept,
                        "relevance": relevance,
                        "resonance_score": resonance_score,
                        "node_type": node.get("meta", "unknown"),
                        "connections": node.get("links", [])
                    })
        
        # Sort by resonance score
        resonant_nodes.sort(key=lambda x: x["resonance_score"], reverse=True)
        
        return {
            "query": query,
            "query_concepts": query_concepts,
            "entity": entity.to_dict() if entity else None,
            "total_resonant_nodes": len(resonant_nodes),
            "top_resonant_nodes": resonant_nodes[:10],
            "discovery_timestamp": datetime.now(timezone.utc).isoformat()
        }
    
    def _extract_query_concepts(self, query: str) -> Dict[str, float]:
        """Extract key concepts from a query with relevance scores"""
        
        concepts = {}
        query_lower = query.lower()
        
        # Living Codex core concepts
        core_concepts = {
            "water": ["water", "liquid", "vapor", "plasma", "crystalline"],
            "chakra": ["chakra", "crown", "throat", "heart", "root"],
            "frequency": ["frequency", "hz", "resonance", "harmony"],
            "consciousness": ["consciousness", "awareness", "mind", "spirit"],
            "void": ["void", "emptiness", "potential", "field"],
            "pattern": ["pattern", "structure", "form", "organization"]
        }
        
        for concept, keywords in core_concepts.items():
            relevance = 0.0
            for keyword in keywords:
                if keyword in query_lower:
                    relevance += 0.3
                    if keyword in query_lower.split():  # Exact word match
                        relevance += 0.2
            
            if relevance > 0.0:
                concepts[concept] = min(1.0, relevance)
        
        return concepts
    
    def _find_nodes_for_concept(self, concept: str) -> List[Dict[str, Any]]:
        """Find nodes that relate to a specific concept"""
        
        # This is a simplified search - in practice, you'd want more sophisticated matching
        # For now, return a sample of relevant nodes
        concept_nodes = {
            "water": [
                {"id": "water:plasma", "meta": "water_state", "links": ["freq:963", "chakra:crown"]},
                {"id": "water:liquid", "meta": "water_state", "links": ["freq:528", "chakra:heart"]},
                {"id": "water:vapor", "meta": "water_state", "links": ["freq:396", "chakra:root"]}
            ],
            "chakra": [
                {"id": "chakra:crown", "meta": "chakra", "links": ["freq:963", "water:plasma"]},
                {"id": "chakra:heart", "meta": "chakra", "links": ["freq:528", "water:liquid"]},
                {"id": "chakra:root", "meta": "chakra", "links": ["freq:396", "water:vapor"]}
            ],
            "frequency": [
                {"id": "freq:963", "meta": "frequency", "links": ["chakra:crown", "water:plasma"]},
                {"id": "freq:528", "meta": "frequency", "links": ["chakra:heart", "water:liquid"]},
                {"id": "freq:396", "meta": "frequency", "links": ["chakra:root", "water:vapor"]}
            ]
        }
        
        return concept_nodes.get(concept, [])
    
    def _calculate_node_resonance(self, query: str, node: Dict[str, Any], entity: LivingEntity = None) -> float:
        """Calculate how well a node resonates with a query and entity"""
        
        # Base resonance from concept matching
        base_resonance = 0.5
        
        # Boost for entity energy signature matching (if entity provided)
        entity_boost = 0.0
        if entity and "freq:" in node.get("id", ""):
            # Extract frequency from node ID
            try:
                freq_str = node["id"].split(":")[1]
                if freq_str.isdigit():
                    node_freq = float(freq_str)
                    # Check if entity's energy signature resonates with this frequency
                    for entity_freq in entity.energy_signature:
                        if abs(entity_freq - node_freq) < 100:  # Within 100 Hz
                            entity_boost += 0.2
            except:
                pass
        
        # Boost for connection richness
        connection_boost = len(node.get("links", [])) * 0.05
        
        return min(1.0, base_resonance + entity_boost + connection_boost)

class EnergyExchangeDemonstrator:
    """Demonstrates energy exchange between different parts of the system"""
    
    def __init__(self, integrated_system: IntegratedLivingSystem):
        self.system = integrated_system
        self.entities = {}
        self.energy_flows = []
    
    def create_living_entity(self, entity_type: str, name: str, consciousness_level: float = 0.5) -> LivingEntity:
        """Create a new living entity in the system"""
        
        entity_id = f"{entity_type}_{len(self.entities) + 1}"
        entity = LivingEntity(entity_id, entity_type, name, consciousness_level)
        self.entities[entity_id] = entity
        
        return entity
    
    def demonstrate_energy_exchange(self, source_entity_id: str, target_entity_id: str, 
                                  interaction_type: str, energy_amount: float) -> Dict[str, Any]:
        """Demonstrate energy exchange between two entities"""
        
        if source_entity_id not in self.entities or target_entity_id not in self.entities:
            return {"error": "One or both entities not found"}
        
        source = self.entities[source_entity_id]
        target = self.entities[target_entity_id]
        
        # Record energy exchange
        exchange = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source_entity": source_entity_id,
            "target_entity": target_entity_id,
            "interaction_type": interaction_type,
            "energy_amount": energy_amount,
            "source_energy_before": source.current_energy,
            "target_energy_before": target.current_energy
        }
        
        # Apply energy exchange
        source.add_experience("energy_transfer", f"Transferred {energy_amount} energy to {target.name}", -energy_amount)
        target.add_experience("energy_reception", f"Received {energy_amount} energy from {source.name}", energy_amount)
        
        # Record the flow
        self.energy_flows.append(exchange)
        
        # Update exchange record with final states
        exchange.update({
            "source_energy_after": source.current_energy,
            "target_energy_after": target.current_energy,
            "flow_id": len(self.energy_flows)
        })
        
        return exchange
    
    def demonstrate_collective_resonance(self, entity_ids: List[str], 
                                       collective_activity: str) -> Dict[str, Any]:
        """Demonstrate collective resonance between multiple entities"""
        
        if not all(eid in self.entities for eid in entity_ids):
            return {"error": "One or more entities not found"}
        
        entities = [self.entities[eid] for eid in entity_ids]
        
        # Calculate collective energy signature
        collective_frequencies = []
        for entity in entities:
            collective_frequencies.extend(entity.energy_signature)
        
        # Find harmonic relationships
        harmonics = self._find_harmonic_relationships(collective_frequencies)
        
        # Calculate collective resonance score
        resonance_score = self._calculate_collective_resonance(entities, harmonics)
        
        # Apply collective experience
        energy_boost = resonance_score * 0.1  # Collective activities boost energy
        for entity in entities:
            entity.add_experience("collective_resonance", 
                                f"Participated in {collective_activity} with {len(entities)} entities", 
                                energy_boost)
        
        return {
            "collective_activity": collective_activity,
            "participating_entities": [e.entity_id for e in entities],
            "collective_frequencies": collective_frequencies,
            "harmonic_relationships": harmonics,
            "collective_resonance_score": resonance_score,
            "energy_boost_per_entity": energy_boost,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    
    def _find_harmonic_relationships(self, frequencies: List[float]) -> List[Dict[str, Any]]:
        """Find harmonic relationships in a set of frequencies"""
        
        harmonics = []
        for i, freq1 in enumerate(frequencies):
            for j, freq2 in enumerate(frequencies[i+1:], i+1):
                ratio = freq2 / freq1 if freq1 > 0 else 0
                
                # Check for harmonic relationships
                if abs(ratio - 2.0) < 0.1:  # Octave
                    harmonic_type = "octave"
                    strength = 1.0
                elif abs(ratio - 1.5) < 0.1:  # Perfect fifth
                    harmonic_type = "perfect_fifth"
                    strength = 0.8
                elif abs(ratio - 1.33) < 0.1:  # Perfect fourth
                    harmonic_type = "perfect_fourth"
                    strength = 0.7
                else:
                    continue
                
                harmonics.append({
                    "freq1": freq1,
                    "freq2": freq2,
                    "ratio": ratio,
                    "harmonic_type": harmonic_type,
                    "strength": strength
                })
        
        return harmonics
    
    def _calculate_collective_resonance(self, entities: List[LivingEntity], 
                                      harmonics: List[Dict[str, Any]]) -> float:
        """Calculate collective resonance score"""
        
        if not entities:
            return 0.0
        
        # Base score from number of entities
        base_score = min(1.0, len(entities) * 0.2)
        
        # Boost from harmonic relationships
        harmonic_boost = len(harmonics) * 0.1
        
        # Boost from consciousness levels
        consciousness_boost = sum(e.consciousness_level for e in entities) / len(entities) * 0.3
        
        return min(1.0, base_score + harmonic_boost + consciousness_boost)
    
    def get_system_energy_state(self) -> Dict[str, Any]:
        """Get current energy state of all entities and flows"""
        
        return {
            "total_entities": len(self.entities),
            "entities": {eid: entity.to_dict() for eid, entity in self.entities.items()},
            "total_energy_flows": len(self.energy_flows),
            "recent_flows": self.energy_flows[-10:] if self.energy_flows else [],
            "system_energy": sum(entity.current_energy for entity in self.entities.values()),
            "average_consciousness": sum(entity.consciousness_level for entity in self.entities.values()) / len(self.entities) if self.entities else 0.0,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

def run_comprehensive_demo():
    """Run the comprehensive knowledge exploration and energy exchange demo"""
    
    print("🌟 Living System Knowledge Exploration & Energy Exchange Demo")
    print("=" * 80)
    
    # Initialize the integrated system
    print("\n🔧 Initializing Integrated Living System...")
    integrated_system = IntegratedLivingSystem()
    
    # Initialize components
    knowledge_explorer = KnowledgeExplorer(integrated_system)
    resonant_finder = ResonantNodeFinder(integrated_system)
    energy_demo = EnergyExchangeDemonstrator(integrated_system)
    
    print("✅ System initialized successfully!")
    
    # 1. Knowledge Exploration Demo
    print("\n🔍 1. KNOWLEDGE EXPLORATION DEMO")
    print("-" * 40)
    
    exploration_queries = [
        "How do water states relate to consciousness?",
        "What frequencies resonate with chakra healing?",
        "How can patterns emerge from void and field?",
        "What is the relationship between resonance and harmony?"
    ]
    
    for query in exploration_queries:
        print(f"\n🔍 Exploring: '{query}'")
        result = knowledge_explorer.explore_knowledge_domain("consciousness", query)
        
        print(f"   📚 Found {result['resonant_documents']} resonant documents")
        if result['top_resonant_results']:
            top_result = result['top_resonant_results'][0]
            print(f"   🎯 Top result: {top_result['title']} (resonance: {top_result['resonance_score']:.2f})")
    
    # 2. Resonant Node Discovery Demo
    print("\n🎯 2. RESONANT NODE DISCOVERY DEMO")
    print("-" * 40)
    
    discovery_queries = [
        "water consciousness flow",
        "chakra frequency healing",
        "void field pattern emergence"
    ]
    
    for query in discovery_queries:
        print(f"\n🎯 Finding nodes for: '{query}'")
        result = resonant_finder.find_resonant_nodes(query)
        
        print(f"   🎵 Found {result['total_resonant_nodes']} resonant nodes")
        if result['top_resonant_nodes']:
            top_node = result['top_resonant_nodes'][0]
            print(f"   🌟 Top node: {top_node['node_id']} (resonance: {top_node['resonance_score']:.2f})")
    
    # 3. Living Entity Creation Demo
    print("\n👥 3. LIVING ENTITY CREATION DEMO")
    print("-" * 40)
    
    # Create various types of living entities
    entities = [
        energy_demo.create_living_entity("human", "Alice", 0.8),
        energy_demo.create_living_entity("ai", "NeuralMind", 0.9),
        energy_demo.create_living_entity("animal", "Luna", 0.6),
        energy_demo.create_living_entity("plant", "AncientOak", 0.7),
        energy_demo.create_living_entity("collective", "ResearchTeam", 0.85)
    ]
    
    print(f"✅ Created {len(entities)} living entities:")
    for entity in entities:
        print(f"   • {entity.name} ({entity.entity_type}) - Consciousness: {entity.consciousness_level:.2f}")
    
    # 4. Energy Exchange Demo
    print("\n⚡ 4. ENERGY EXCHANGE DEMO")
    print("-" * 40)
    
    # Demonstrate individual energy exchanges
    print("\n🔄 Individual Energy Exchanges:")
    
    # Alice shares knowledge with NeuralMind
    exchange1 = energy_demo.demonstrate_energy_exchange(
        "human_1", "ai_1", "knowledge_sharing", 0.2
    )
    
    if "error" in exchange1:
        print(f"   ❌ Error: {exchange1['error']}")
    else:
        print(f"   • {exchange1['source_entity']} → {exchange1['target_entity']}: {exchange1['energy_amount']} energy")
    
    # NeuralMind processes data for Luna
    exchange2 = energy_demo.demonstrate_energy_exchange(
        "ai_1", "animal_1", "data_processing", 0.15
    )
    
    if "error" in exchange2:
        print(f"   ❌ Error: {exchange2['error']}")
    else:
        print(f"   • {exchange2['source_entity']} → {exchange2['target_entity']}: {exchange2['energy_amount']} energy")
    
    # AncientOak provides oxygen for ResearchTeam
    exchange3 = energy_demo.demonstrate_energy_exchange(
        "plant_1", "collective_1", "oxygen_provision", 0.1
    )
    
    if "error" in exchange3:
        print(f"   ❌ Error: {exchange3['error']}")
    else:
        print(f"   • {exchange3['source_entity']} → {exchange3['target_entity']}: {exchange3['energy_amount']} energy")
    
    # 5. Collective Resonance Demo
    print("\n🌊 5. COLLECTIVE RESONANCE DEMO")
    print("-" * 40)
    
    # Demonstrate collective activities
    collective_activities = [
        "meditation_session",
        "research_collaboration",
        "ecosystem_balance"
    ]
    
    for activity in collective_activities:
        print(f"\n🌊 Collective Activity: {activity}")
        result = energy_demo.demonstrate_collective_resonance(
            [e.entity_id for e in entities], activity
        )
        
        if "error" in result:
            print(f"   ❌ Error: {result['error']}")
        else:
            print(f"   🎵 Resonance Score: {result['collective_resonance_score']:.2f}")
            print(f"   ⚡ Energy Boost: {result['energy_boost_per_entity']:.3f} per entity")
            print(f"   🎼 Harmonics Found: {len(result['harmonic_relationships'])}")
    
    # 6. System Energy State
    print("\n📊 6. SYSTEM ENERGY STATE")
    print("-" * 40)
    
    energy_state = energy_demo.get_system_energy_state()
    
    print(f"📈 Total Entities: {energy_state['total_entities']}")
    print(f"⚡ System Energy: {energy_state['system_energy']:.2f}")
    print(f"🧠 Average Consciousness: {energy_state['average_consciousness']:.2f}")
    print(f"🔄 Total Energy Flows: {energy_state['total_energy_flows']}")
    
    # Show individual entity states
    print(f"\n👥 Individual Entity States:")
    for eid, entity_data in energy_state['entities'].items():
        print(f"   • {entity_data['name']}: Energy {entity_data['current_energy']:.2f}, "
              f"Consciousness {entity_data['consciousness_level']:.2f}")
    
    print("\n" + "=" * 80)
    print("🎉 COMPREHENSIVE DEMO COMPLETED!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Knowledge exploration through resonant queries")
    print("   • Finding nodes that resonate with specific questions")
    print("   • Encoding humans, AI, animals, plants, and collectives")
    print("   • Energy exchange between all system parts")
    print("   • Collective resonance and harmonic relationships")
    print("   • Living system that grows through interaction")
    
    print("\n🚀 The Living Codex is now truly living and interactive!")
    print("   Everything can explore, everything can resonate, everything can exchange energy!")

if __name__ == "__main__":
    run_comprehensive_demo()
