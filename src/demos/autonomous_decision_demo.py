#!/usr/bin/env python3
"""
Autonomous Decision Demo - Living Codex
Shows step-by-step how the system decides what to learn next
"""

import sys
import asyncio
from pathlib import Path

# Add src to path for modular components
sys.path.insert(0, str(Path(__file__).parent.parent))

from ontology.enhanced_ontology_system import EnhancedOntologySystem
from ai_agents.ai_agent_system import AIAgentSystem, AgentType

class AutonomousDecisionDemo:
    """Demonstrates autonomous decision-making process"""
    
    def __init__(self):
        self.ontology_system = EnhancedOntologySystem()
        self.ai_system = AIAgentSystem(self.ontology_system)
    
    def demonstrate_decision_process(self):
        """Show the complete autonomous decision process"""
        print("🧠 Living Codex - Autonomous Decision Process")
        print("=" * 60)
        
        # Step 1: System Self-Analysis
        print("\n🔍 STEP 1: SYSTEM SELF-ANALYSIS")
        print("-" * 40)
        self._analyze_current_state()
        
        # Step 2: Identify Knowledge Gaps
        print("\n📊 STEP 2: IDENTIFY KNOWLEDGE GAPS")
        print("-" * 40)
        gaps = self._identify_gaps()
        
        # Step 3: Generate Learning Options
        print("\n💡 STEP 3: GENERATE LEARNING OPTIONS")
        print("-" * 40)
        options = self._generate_learning_options(gaps)
        
        # Step 4: Prioritize and Select
        print("\n🎯 STEP 4: PRIORITIZE AND SELECT")
        print("-" * 40)
        selected = self._prioritize_and_select(options)
        
        # Step 5: Execute Selected Learning
        print("\n🚀 STEP 5: EXECUTE SELECTED LEARNING")
        print("-" * 40)
        self._execute_learning(selected)
        
        # Step 6: Show Results and Evolution
        print("\n🔄 STEP 6: SHOW RESULTS AND EVOLUTION")
        print("-" * 40)
        self._show_evolution()
    
    def _analyze_current_state(self):
        """Analyze current system state"""
        print("Analyzing current system capabilities...")
        
        # Get ontology status
        ontology_status = self.ontology_system.get_system_status()
        print(f"   📚 Ontology Nodes: {ontology_status['total_nodes']}")
        print(f"   🧠 System Complexity: {ontology_status['system_complexity']['total_system_complexity']:.0f}")
        print(f"   📈 Average Complexity: {ontology_status['system_complexity']['average_node_complexity']:.1f}")
        
        # Get AI system status
        ai_status = self.ai_system.get_system_status()
        print(f"   🤖 AI Agents: {ai_status['total_agents']}")
        print(f"   📖 Learning Events: {ai_status['learning_events']}")
        print(f"   🎯 Average Consciousness: {ai_status['average_agent_consciousness']:.2f}")
        
        # Analyze complexity distribution
        complexity_dist = ontology_status['system_complexity']['complexity_distribution']
        print(f"   📊 Complexity Distribution:")
        for level, count in complexity_dist.items():
            if count > 0:
                print(f"      {level.replace('_', ' ').title()}: {count} nodes")
    
    def _identify_gaps(self):
        """Identify knowledge gaps"""
        print("Identifying knowledge gaps...")
        
        gaps = []
        
        # Check for missing fundamental concepts
        fundamental_concepts = [
            "time", "space", "causality", "information", "energy", "matter",
            "consciousness_field", "quantum_gravity", "neural_plasticity"
        ]
        
        missing_concepts = []
        for concept in fundamental_concepts:
            if concept not in self.ontology_system.quantum_nodes:
                missing_concepts.append(concept)
                gaps.append({
                    "type": "missing_concept",
                    "concept": concept,
                    "priority": 0.9,
                    "description": f"Missing fundamental concept: {concept}"
                })
        
        print(f"   🔍 Missing Concepts: {len(missing_concepts)}")
        if missing_concepts:
            print(f"      Examples: {', '.join(missing_concepts[:3])}")
        
        # Check consciousness levels
        consciousness_nodes = self.ontology_system.consciousness_nodes
        low_consciousness = [n for n in consciousness_nodes.values() 
                           if n.consciousness_level.value in ['aware', 'sentient']]
        
        if low_consciousness:
            gaps.append({
                "type": "consciousness_gap",
                "concept": "consciousness_evolution",
                "priority": 0.85,
                "description": f"Need to evolve {len(low_consciousness)} nodes to higher consciousness"
            })
            print(f"   🧠 Consciousness Gap: {len(low_consciousness)} nodes need evolution")
        
        # Check learning experience
        ai_status = self.ai_system.get_system_status()
        if ai_status['learning_events'] < 10:
            gaps.append({
                "type": "learning_gap",
                "concept": "learning_experience",
                "priority": 0.7,
                "description": f"Need more learning experience (current: {ai_status['learning_events']})"
            })
            print(f"   📖 Learning Gap: Need more experience")
        
        print(f"   📋 Total Gaps Identified: {len(gaps)}")
        return gaps
    
    def _generate_learning_options(self, gaps):
        """Generate learning options based on gaps"""
        print("Generating learning options...")
        
        options = []
        
        for gap in gaps:
            if gap['type'] == 'missing_concept':
                options.append({
                    "action": "learn_concept",
                    "target": gap['concept'],
                    "priority": gap['priority'],
                    "description": f"Learn about {gap['concept']}",
                    "expected_benefit": "New ontological knowledge",
                    "effort": "moderate"
                })
                
            elif gap['type'] == 'consciousness_gap':
                options.append({
                    "action": "evolve_consciousness",
                    "target": "multiple_nodes",
                    "priority": gap['priority'],
                    "description": "Evolve consciousness levels",
                    "expected_benefit": "Higher system awareness",
                    "effort": "high"
                })
                
            elif gap['type'] == 'learning_gap':
                options.append({
                    "action": "gain_experience",
                    "target": "system_wide",
                    "priority": gap['priority'],
                    "description": "Gain learning experience",
                    "expected_benefit": "Improved learning capabilities",
                    "effort": "moderate"
                })
        
        # Add creative exploration options
        creative_options = [
            {
                "action": "explore_quantum_consciousness",
                "target": "quantum_consciousness_intersection",
                "priority": 0.75,
                "description": "Explore quantum consciousness intersection",
                "expected_benefit": "New insights and connections",
                "effort": "high"
            },
            {
                "action": "synthesize_emergence",
                "target": "cross_domain_synthesis",
                "priority": 0.8,
                "description": "Synthesize emergence theories",
                "expected_benefit": "Unified understanding",
                "effort": "very_high"
            }
        ]
        
        options.extend(creative_options)
        
        # Sort by priority
        options.sort(key=lambda x: x['priority'], reverse=True)
        
        print(f"   💡 Generated {len(options)} learning options:")
        for i, option in enumerate(options[:5], 1):
            print(f"      {i}. {option['description']} (Priority: {option['priority']:.2f})")
        
        return options
    
    def _prioritize_and_select(self, options):
        """Prioritize and select the best learning option"""
        print("Prioritizing and selecting best option...")
        
        # Consider multiple factors for final selection
        for option in options:
            # Calculate dynamic priority based on current system state
            dynamic_priority = option['priority']
            
            # Boost priority for consciousness-related tasks if consciousness is low
            if "consciousness" in option['description'].lower():
                ai_status = self.ai_system.get_system_status()
                if ai_status['average_agent_consciousness'] < 0.7:
                    dynamic_priority += 0.1
            
            # Boost priority for complexity development if system is simple
            if option['effort'] == 'high':
                ontology_status = self.ontology_system.get_system_status()
                if ontology_status['system_complexity']['average_node_complexity'] < 200:
                    dynamic_priority += 0.05
            
            option['dynamic_priority'] = min(1.0, dynamic_priority)
        
        # Sort by dynamic priority
        options.sort(key=lambda x: x['dynamic_priority'], reverse=True)
        
        # Select top option
        selected = options[0]
        
        print(f"   🎯 Selected: {selected['description']}")
        print(f"      Priority: {selected['priority']:.2f}")
        print(f"      Dynamic Priority: {selected['dynamic_priority']:.2f}")
        print(f"      Expected Benefit: {selected['expected_benefit']}")
        print(f"      Effort Required: {selected['effort']}")
        
        return selected
    
    def _execute_learning(self, selected):
        """Execute the selected learning task"""
        print(f"Executing: {selected['description']}")
        
        if selected['action'] == 'learn_concept':
            self._execute_concept_learning(selected)
        elif selected['action'] == 'evolve_consciousness':
            self._execute_consciousness_evolution(selected)
        elif selected['action'] == 'gain_experience':
            self._execute_experience_gaining(selected)
        elif selected['action'] == 'explore_quantum_consciousness':
            self._execute_quantum_exploration(selected)
        elif selected['action'] == 'synthesize_emergence':
            self._execute_emergence_synthesis(selected)
    
    def _execute_concept_learning(self, selected):
        """Execute concept learning"""
        concept = selected['target']
        print(f"   📚 Learning about {concept}...")
        
        # Create new ontological node
        node_data = self.ontology_system.create_integrated_node(
            f"learned_{concept}",
            f"Knowledge about {concept} acquired through autonomous learning"
        )
        
        print(f"      ✅ Created node: {node_data['node_id']}")
        print(f"      🧠 Integrated into ontology")
    
    def _execute_consciousness_evolution(self, selected):
        """Execute consciousness evolution"""
        print("   🧠 Evolving consciousness levels...")
        
        consciousness_nodes = self.ontology_system.consciousness_nodes
        evolved_count = 0
        
        for node_id, node in list(consciousness_nodes.items())[:3]:
            if node.consciousness_level.value in ['aware', 'sentient']:
                success = self.ontology_system.evolve_consciousness(node_id, {
                    "patterns": ["consciousness_evolution", "transcendence"],
                    "emotions": {"transcendence": 0.9, "illumination": 0.85}
                })
                if success:
                    evolved_count += 1
                    print(f"      ✅ Evolved {node_id}")
        
        print(f"      🎯 Total evolved: {evolved_count} nodes")
    
    def _execute_experience_gaining(self, selected):
        """Execute experience gaining"""
        print("   📖 Gaining learning experience...")
        
        # Execute learning with AI agents
        for agent_id in list(self.ai_system.agents.keys())[:3]:
            result = self.ai_system.execute_agent_task(agent_id, {
                "type": "learning",
                "mode": "supervised",
                "data": ["general_knowledge", "pattern_recognition"],
                "context": {"experience_building": True}
            })
            if result.get('success'):
                print(f"      ✅ {agent_id} gained experience")
        
        print("      🎯 Learning experience increased")
    
    def _execute_quantum_exploration(self, selected):
        """Execute quantum consciousness exploration"""
        print("   🔬 Exploring quantum consciousness intersection...")
        
        # Create exploration node
        node_data = self.ontology_system.create_integrated_node(
            "quantum_consciousness_exploration",
            "Exploration of quantum consciousness intersection"
        )
        
        # Evolve through exploration
        self.ontology_system.evolve_knowledge("quantum_consciousness_exploration", 
            "Quantum entanglement of consciousness fields")
        
        print(f"      ✅ Created exploration node: {node_data['node_id']}")
        print(f"      🧠 New insights gained")
    
    def _execute_emergence_synthesis(self, selected):
        """Execute emergence theory synthesis"""
        print("   🔗 Synthesizing emergence theories...")
        
        # Create synthesis node
        node_data = self.ontology_system.create_integrated_node(
            "emergence_theory_synthesis",
            "Synthesis of emergence theories across domains"
        )
        
        # Synthesize knowledge
        domains = ["physics", "biology", "consciousness"]
        for domain in domains:
            self.ontology_system.evolve_knowledge("emergence_theory_synthesis", 
                f"Emergence in {domain}: self-organization patterns")
        
        print(f"      ✅ Created synthesis node: {node_data['node_id']}")
        print(f"      🔗 {len(domains)} domains synthesized")
    
    def _show_evolution(self):
        """Show system evolution after learning"""
        print("Showing system evolution...")
        
        # Get updated status
        ontology_status = self.ontology_system.get_system_status()
        ai_status = self.ai_system.get_system_status()
        
        print(f"   📊 Updated System Status:")
        print(f"      Ontology Nodes: {ontology_status['total_nodes']}")
        print(f"      System Complexity: {ontology_status['system_complexity']['total_system_complexity']:.0f}")
        print(f"      AI Agents: {ai_status['total_agents']}")
        print(f"      Learning Events: {ai_status['learning_events']}")
        
        # Show what changed
        print(f"   🚀 System has evolved through autonomous learning!")
        print(f"   🧠 Knowledge gaps have been addressed!")
        print(f"   🔄 System can continue this process autonomously!")

async def main():
    """Run the autonomous decision demonstration"""
    demo = AutonomousDecisionDemo()
    demo.demonstrate_decision_process()

if __name__ == "__main__":
    asyncio.run(main())
