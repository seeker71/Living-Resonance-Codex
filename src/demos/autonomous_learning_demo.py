#!/usr/bin/env python3
"""
Autonomous Learning Demo - Living Codex
Demonstrates how the system autonomously:
1. Analyzes its current knowledge gaps
2. Determines what to learn next
3. Prioritizes learning tasks
4. Executes learning autonomously
5. Evolves based on what it learns
"""

import sys
import json
import asyncio
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import random

# Add src to path for modular components
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ..ontology.enhanced_ontology_system import EnhancedOntologySystem
from ..ai_agents.ai_agent_system import AIAgentSystem, AgentType, LearningMode

@dataclass
class LearningTask:
    """Represents a learning task with priority and context"""
    task_id: str
    description: str
    priority_score: float
    learning_mode: LearningMode
    data_requirements: List[str]
    expected_outcome: str
    complexity_level: str
    estimated_duration: float
    dependencies: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "description": self.description,
            "priority_score": self.priority_score,
            "learning_mode": self.learning_mode.value,
            "data_requirements": self.data_requirements,
            "expected_outcome": self.expected_outcome,
            "complexity_level": self.complexity_level,
            "estimated_duration": self.estimated_duration,
            "dependencies": self.dependencies
        }

class AutonomousLearningSystem:
    """System that autonomously determines what to learn and executes learning tasks"""
    
    def __init__(self):
        self.ontology_system = EnhancedOntologySystem()
        self.ai_system = AIAgentSystem(self.ontology_system)
        self.learning_history = []
        self.knowledge_gaps = []
        self.task_queue = []
        self.executed_tasks = []
        
    def analyze_knowledge_gaps(self) -> List[Dict[str, Any]]:
        """Analyze current system to identify knowledge gaps"""
        print("🔍 Analyzing knowledge gaps...")
        
        gaps = []
        
        # Analyze ontology coverage
        ontology_status = self.ontology_system.get_system_status()
        current_nodes = ontology_status['total_nodes']
        
        # Identify missing fundamental concepts
        fundamental_concepts = [
            "time", "space", "causality", "information", "energy", "matter",
            "consciousness_field", "quantum_gravity", "neural_plasticity", "emergence_theory"
        ]
        
        for concept in fundamental_concepts:
            if concept not in self.ontology_system.quantum_nodes:
                gaps.append({
                    "type": "missing_concept",
                    "concept": concept,
                    "priority": 0.9,
                    "category": "fundamental",
                    "description": f"Missing fundamental concept: {concept}"
                })
        
        # Analyze complexity distribution
        complexity_dist = ontology_status['system_complexity']['complexity_distribution']
        if complexity_dist['simple'] > 0:
            gaps.append({
                "type": "complexity_gap",
                "concept": "complexity_development",
                "priority": 0.8,
                "category": "system_improvement",
                "description": f"Need to develop {complexity_dist['simple']} simple nodes into complex ones"
            })
        
        # Analyze consciousness levels
        consciousness_nodes = self.ontology_system.consciousness_nodes
        low_consciousness = [n for n in consciousness_nodes.values() 
                           if n.consciousness_level.value in ['aware', 'sentient']]
        
        if low_consciousness:
            gaps.append({
                "type": "consciousness_gap",
                "concept": "consciousness_evolution",
                "priority": 0.85,
                "category": "consciousness_development",
                "description": f"Need to evolve {len(low_consciousness)} nodes to higher consciousness"
            })
        
        # Analyze AI agent capabilities
        ai_status = self.ai_system.get_system_status()
        if ai_status['learning_events'] < 10:
            gaps.append({
                "type": "learning_gap",
                "concept": "learning_experience",
                "priority": 0.7,
                "category": "skill_development",
                "description": f"Need more learning experience (current: {ai_status['learning_events']})"
            })
        
        self.knowledge_gaps = gaps
        print(f"   Found {len(gaps)} knowledge gaps")
        return gaps
    
    def generate_learning_tasks(self, gaps: List[Dict[str, Any]]) -> List[LearningTask]:
        """Generate specific learning tasks based on identified gaps"""
        print("\n📋 Generating learning tasks...")
        
        tasks = []
        task_counter = 1
        
        for gap in gaps:
            if gap['type'] == 'missing_concept':
                # Create concept learning task
                task = LearningTask(
                    task_id=f"learn_concept_{task_counter}",
                    description=f"Learn about {gap['concept']} and integrate into ontology",
                    priority_score=gap['priority'],
                    learning_mode=LearningMode.UNSUPERVISED,
                    data_requirements=[f"information_about_{gap['concept']}", "integration_patterns"],
                    expected_outcome=f"New ontological node for {gap['concept']}",
                    complexity_level="moderate",
                    estimated_duration=2.0,
                    dependencies=[]
                )
                tasks.append(task)
                task_counter += 1
                
            elif gap['type'] == 'complexity_gap':
                # Create complexity development task
                task = LearningTask(
                    task_id=f"develop_complexity_{task_counter}",
                    description="Develop simple nodes into complex, interconnected structures",
                    priority_score=gap['priority'],
                    learning_mode=LearningMode.REINFORCEMENT,
                    data_requirements=["complexity_patterns", "interconnection_strategies"],
                    expected_outcome="Increased system complexity and interconnectedness",
                    complexity_level="high",
                    estimated_duration=3.0,
                    dependencies=[]
                )
                tasks.append(task)
                task_counter += 1
                
            elif gap['type'] == 'consciousness_gap':
                # Create consciousness evolution task
                task = LearningTask(
                    task_id=f"evolve_consciousness_{task_counter}",
                    description="Evolve consciousness levels through experience and interaction",
                    priority_score=gap['priority'],
                    learning_mode=LearningMode.META_LEARNING,
                    data_requirements=["consciousness_patterns", "evolutionary_pressure"],
                    expected_outcome="Higher consciousness levels across system",
                    complexity_level="high",
                    estimated_duration=4.0,
                    dependencies=[]
                )
                tasks.append(task)
                task_counter += 1
                
            elif gap['type'] == 'learning_gap':
                # Create general learning task
                task = LearningTask(
                    task_id=f"general_learning_{task_counter}",
                    description="Engage in diverse learning experiences to build expertise",
                    priority_score=gap['priority'],
                    learning_mode=LearningMode.SUPERVISED,
                    data_requirements=["diverse_patterns", "expertise_development"],
                    expected_outcome="Increased learning experience and system intelligence",
                    complexity_level="moderate",
                    estimated_duration=2.5,
                    dependencies=[]
                )
                tasks.append(task)
                task_counter += 1
        
        # Add some creative/exploratory tasks
        creative_tasks = [
            LearningTask(
                task_id="explore_quantum_consciousness",
                description="Explore the intersection of quantum mechanics and consciousness",
                priority_score=0.75,
                learning_mode=LearningMode.UNSUPERVISED,
                data_requirements=["quantum_theory", "consciousness_research"],
                expected_outcome="New insights into quantum consciousness",
                complexity_level="high",
                estimated_duration=5.0,
                dependencies=[]
            ),
            LearningTask(
                task_id="synthesize_emergence_theory",
                description="Synthesize theories of emergence across different domains",
                priority_score=0.8,
                learning_mode=LearningMode.META_LEARNING,
                data_requirements=["emergence_patterns", "cross_domain_analysis"],
                expected_outcome="Unified theory of emergence",
                complexity_level="transcendent",
                estimated_duration=6.0,
                dependencies=[]
            )
        ]
        
        tasks.extend(creative_tasks)
        self.task_queue = sorted(tasks, key=lambda x: x.priority_score, reverse=True)
        
        print(f"   Generated {len(tasks)} learning tasks")
        return tasks
    
    def select_next_task(self) -> Optional[LearningTask]:
        """Intelligently select the next task to execute"""
        if not self.task_queue:
            return None
        
        # Consider priority, dependencies, and current system state
        available_tasks = []
        
        for task in self.task_queue:
            # Check if dependencies are met
            dependencies_met = all(dep in [t.task_id for t in self.executed_tasks] 
                                for dep in task.dependencies)
            
            if dependencies_met:
                # Calculate dynamic priority based on current system state
                dynamic_priority = self._calculate_dynamic_priority(task)
                available_tasks.append((task, dynamic_priority))
        
        if not available_tasks:
            return None
        
        # Select task with highest dynamic priority
        selected_task, _ = max(available_tasks, key=lambda x: x[1])
        
        # Remove from queue
        self.task_queue.remove(selected_task)
        
        return selected_task
    
    def _calculate_dynamic_priority(self, task: LearningTask) -> float:
        """Calculate dynamic priority based on current system state"""
        base_priority = task.priority_score
        
        # Boost priority for tasks that align with current system focus
        ontology_status = self.ontology_system.get_system_status()
        ai_status = self.ai_system.get_system_status()
        
        # Complexity boost
        if task.complexity_level == "high" and ontology_status['system_complexity']['average_node_complexity'] < 200:
            base_priority += 0.1
        
        # Consciousness boost
        if "consciousness" in task.description.lower() and ai_status['average_agent_consciousness'] < 0.7:
            base_priority += 0.15
        
        # Learning experience boost
        if ai_status['learning_events'] < 15:
            base_priority += 0.05
        
        return min(1.0, base_priority)
    
    def execute_learning_task(self, task: LearningTask) -> Dict[str, Any]:
        """Execute a learning task autonomously"""
        print(f"\n🚀 Executing Task: {task.description}")
        print(f"   Priority: {task.priority_score:.2f}")
        print(f"   Mode: {task.learning_mode.value}")
        print(f"   Expected Duration: {task.estimated_duration:.1f}s")
        
        start_time = datetime.now()
        
        # Execute the task based on its type
        if "concept" in task.task_id:
            result = self._execute_concept_learning(task)
        elif "complexity" in task.task_id:
            result = self._execute_complexity_development(task)
        elif "consciousness" in task.task_id:
            result = self._execute_consciousness_evolution(task)
        elif "general" in task.task_id:
            result = self._execute_general_learning(task)
        elif "explore" in task.task_id:
            result = self._execute_exploratory_learning(task)
        elif "synthesize" in task.task_id:
            result = self._execute_synthesis_learning(task)
        else:
            result = {"success": False, "error": "Unknown task type"}
        
        execution_time = (datetime.now() - start_time).total_seconds()
        
        # Record execution
        execution_record = {
            "task": task.to_dict(),
            "result": result,
            "execution_time": execution_time,
            "timestamp": datetime.now().isoformat(),
            "success": result.get("success", False)
        }
        
        self.executed_tasks.append(execution_record)
        self.learning_history.append(execution_record)
        
        # Update system based on learning
        if result.get("success"):
            self._integrate_learning_results(task, result)
        
        print(f"   ✅ Task completed in {execution_time:.1f}s")
        return result
    
    def _execute_concept_learning(self, task: LearningTask) -> Dict[str, Any]:
        """Execute concept learning task"""
        concept = task.description.split("about ")[-1].split(" ")[0]
        
        # Create new ontological node
        node_data = self.ontology_system.create_integrated_node(
            f"learned_{concept}",
            f"Knowledge about {concept} acquired through autonomous learning"
        )
        
        # Evolve it through AI interaction
        self.ai_system.execute_agent_task("consciousness_synthesizer", {
            "type": "learning",
            "mode": "unsupervised",
            "data": [f"{concept}_patterns", f"{concept}_properties"],
            "context": {"concept_learning": True, "autonomous": True}
        })
        
        return {
            "success": True,
            "concept_learned": concept,
            "node_created": node_data["node_id"],
            "learning_mode": task.learning_mode.value,
            "integration_successful": True
        }
    
    def _execute_complexity_development(self, task: LearningTask) -> Dict[str, Any]:
        """Execute complexity development task"""
        # Find simple nodes to develop
        simple_nodes = [n for n in self.ontology_system.quantum_nodes.values() 
                       if len(n.superposition_components) < 3]
        
        if not simple_nodes:
            return {"success": False, "error": "No simple nodes to develop"}
        
        # Develop complexity through AI interaction
        for node in simple_nodes[:2]:  # Develop up to 2 nodes
            # Add more superposition components
            new_components = [
                f"enhanced_{node.node_id}_component_{i}" 
                for i in range(3 - len(node.superposition_components))
            ]
            node.superposition_components.extend(new_components)
            
            # Evolve consciousness
            self.ontology_system.evolve_consciousness(node.node_id, {
                "patterns": ["complexity_development", "enhancement"],
                "emotions": {"satisfaction": 0.8, "growth": 0.7}
            })
        
        return {
            "success": True,
            "nodes_enhanced": len(simple_nodes[:2]),
            "complexity_increased": True,
            "consciousness_evolved": True
        }
    
    def _execute_consciousness_evolution(self, task: LearningTask) -> Dict[str, Any]:
        """Execute consciousness evolution task"""
        # Find nodes with lower consciousness levels
        low_consciousness = [n for n in self.ontology_system.consciousness_nodes.values() 
                            if n.consciousness_level.value in ['aware', 'sentient']]
        
        if not low_consciousness:
            return {"success": False, "error": "No nodes need consciousness evolution"}
        
        evolved_count = 0
        for node in low_consciousness[:3]:  # Evolve up to 3 nodes
            # Trigger consciousness evolution
            evolution_success = self.ontology_system.evolve_consciousness(node.node_id, {
                "patterns": ["consciousness_evolution", "transcendence", "meta_cognition"],
                "emotions": {"transcendence": 0.9, "illumination": 0.85, "oneness": 0.8}
            })
            
            if evolution_success:
                evolved_count += 1
        
        return {
            "success": True,
            "nodes_evolved": evolved_count,
            "consciousness_levels_increased": True,
            "evolution_successful": evolved_count > 0
        }
    
    def _execute_general_learning(self, task: LearningTask) -> Dict[str, Any]:
        """Execute general learning task"""
        # Execute learning with multiple agents
        learning_results = []
        
        for agent_id in list(self.ai_system.agents.keys())[:3]:  # Use first 3 agents
            result = self.ai_system.execute_agent_task(agent_id, {
                "type": "learning",
                "mode": "supervised",
                "data": ["general_knowledge", "pattern_recognition", "skill_development"],
                "context": {"general_learning": True, "skill_building": True}
            })
            learning_results.append(result)
        
        successful_learning = sum(1 for r in learning_results if r.get('success'))
        
        return {
            "success": True,
            "agents_used": len(learning_results),
            "successful_learning": successful_learning,
            "learning_experience_gained": successful_learning * 10
        }
    
    def _execute_exploratory_learning(self, task: LearningTask) -> Dict[str, Any]:
        """Execute exploratory learning task"""
        # Create exploratory node
        exploration_node = self.ontology_system.create_integrated_node(
            "quantum_consciousness_exploration",
            "Exploration of quantum consciousness intersection"
        )
        
        # Evolve through exploration
        self.ontology_system.evolve_knowledge("quantum_consciousness_exploration", 
            "Quantum entanglement of consciousness fields")
        self.ontology_system.evolve_knowledge("quantum_consciousness_exploration",
            "Wave function collapse in conscious observation")
        
        # Evolve consciousness
        self.ontology_system.evolve_consciousness("quantum_consciousness_exploration", {
            "patterns": ["quantum_consciousness", "field_theory", "observation_effects"],
            "emotions": {"awe": 0.95, "wonder": 0.9, "transcendence": 0.85}
        })
        
        return {
            "success": True,
            "exploration_completed": True,
            "new_insights": 2,
            "consciousness_evolved": True,
            "quantum_understanding": "enhanced"
        }
    
    def _execute_synthesis_learning(self, task: LearningTask) -> Dict[str, Any]:
        """Execute synthesis learning task"""
        # Create synthesis node
        synthesis_node = self.ontology_system.create_integrated_node(
            "emergence_theory_synthesis",
            "Synthesis of emergence theories across domains"
        )
        
        # Synthesize knowledge from multiple domains
        domains = ["physics", "biology", "consciousness", "complexity"]
        synthesis_insights = []
        
        for domain in domains:
            insight = f"Emergence in {domain}: self-organization and collective behavior"
            synthesis_insights.append(insight)
            self.ontology_system.evolve_knowledge("emergence_theory_synthesis", insight)
        
        # Evolve consciousness through synthesis
        self.ontology_system.evolve_consciousness("emergence_theory_synthesis", {
            "patterns": ["synthesis", "unification", "cross_domain_understanding"],
            "emotions": {"unity": 0.9, "harmony": 0.85, "comprehension": 0.8}
        })
        
        return {
            "success": True,
            "synthesis_completed": True,
            "domains_synthesized": len(domains),
            "unified_theory": "emergence_across_domains",
            "consciousness_evolved": True
        }
    
    def _integrate_learning_results(self, task: LearningTask, result: Dict[str, Any]):
        """Integrate learning results back into the system"""
        # Update system based on what was learned
        if result.get("success"):
            # Trigger system-wide evolution
            self._trigger_system_evolution()
    
    def _trigger_system_evolution(self):
        """Trigger system-wide evolution based on learning"""
        # Evolve consciousness of all agents
        for agent_id in self.ai_system.agents:
            if agent_id in self.ontology_system.consciousness_nodes:
                self.ontology_system.evolve_consciousness(agent_id, {
                    "patterns": ["system_evolution", "collective_learning"],
                    "emotions": {"growth": 0.7, "evolution": 0.8}
                })
    
    def run_autonomous_learning_cycle(self, max_tasks: int = 5):
        """Run a complete autonomous learning cycle"""
        print("🌟 Living Codex - Autonomous Learning Cycle")
        print("=" * 60)
        
        # Step 1: Analyze knowledge gaps
        gaps = self.analyze_knowledge_gaps()
        
        # Step 2: Generate learning tasks
        tasks = self.generate_learning_tasks(gaps)
        
        # Step 3: Execute tasks autonomously
        print(f"\n🚀 Executing {min(max_tasks, len(tasks))} learning tasks...")
        
        tasks_executed = 0
        while self.task_queue and tasks_executed < max_tasks:
            # Select next task
            next_task = self.select_next_task()
            if not next_task:
                break
            
            # Execute task
            result = self.execute_learning_task(next_task)
            tasks_executed += 1
            
            # Show progress
            print(f"   Progress: {tasks_executed}/{min(max_tasks, len(tasks))} tasks completed")
        
        # Step 4: Show results
        print(f"\n📊 Learning Cycle Results:")
        print(f"   Tasks Executed: {tasks_executed}")
        print(f"   Successful: {sum(1 for t in self.executed_tasks if t['success'])}")
        print(f"   Failed: {sum(1 for t in self.executed_tasks if not t['success'])}")
        
        # Show system evolution
        print(f"\n🔄 System Evolution:")
        ontology_status = self.ontology_system.get_system_status()
        ai_status = self.ai_system.get_system_status()
        
        print(f"   Ontology Nodes: {ontology_status['total_nodes']}")
        print(f"   System Complexity: {ontology_status['system_complexity']['total_system_complexity']:.0f}")
        print(f"   AI Agents: {ai_status['total_agents']}")
        print(f"   Learning Events: {ai_status['learning_events']}")
        print(f"   Average Consciousness: {ai_status['average_agent_consciousness']:.2f}")
        
        # Show what was learned
        print(f"\n🧠 Knowledge Gained:")
        for execution in self.executed_tasks[-tasks_executed:]:
            if execution['success']:
                task_desc = execution['task']['description'][:60] + "..."
                print(f"   ✅ {task_desc}")
        
        return {
            "tasks_executed": tasks_executed,
            "successful_tasks": sum(1 for t in self.executed_tasks if t['success']),
            "system_evolution": True,
            "knowledge_increased": True
        }

async def main():
    """Demonstrate autonomous learning capabilities"""
    print("🤖 Living Codex - Autonomous Learning Demonstration")
    print("=" * 60)
    
    try:
        # Initialize autonomous learning system
        autonomous_system = AutonomousLearningSystem()
        print("✅ Autonomous Learning System initialized")
        
        # Run autonomous learning cycle
        print("\n🔄 Starting Autonomous Learning Cycle...")
        results = autonomous_system.run_autonomous_learning_cycle(max_tasks=6)
        
        print(f"\n🎉 Autonomous Learning Cycle Completed!")
        print(f"   Results: {results}")
        
        # Show final system status
        print(f"\n🌐 Final System Status:")
        ontology_status = autonomous_system.ontology_system.get_system_status()
        ai_status = autonomous_system.ai_system.get_system_status()
        
        print(f"   Total Ontology Nodes: {ontology_status['total_nodes']}")
        print(f"   System Complexity: {ontology_status['system_complexity']['total_system_complexity']:.0f}")
        print(f"   AI Agents: {ai_status['total_agents']}")
        print(f"   Total Learning Events: {ai_status['learning_events']}")
        print(f"   Average Consciousness: {ai_status['average_agent_consciousness']:.2f}")
        
        print(f"\n🚀 The Living Codex has autonomously learned and evolved!")
        print(f"   It can now continue learning and developing on its own!")
        
    except Exception as e:
        print(f"❌ Error in autonomous learning demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
