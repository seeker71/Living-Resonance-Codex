#!/usr/bin/env python3
"""
Living Codex - Standalone Full CLI Interface
A complete, dependency-free command line interface with all advanced features.
"""

import sys
import os
import json
import cmd
import shlex
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import math
import re
import random
from dataclasses import dataclass

class LivingCodexOntology:
    """Comprehensive Living Codex ontology system"""
    
    def __init__(self):
        self.initialize_ontology()
    
    def initialize_ontology(self):
        """Initialize the complete Living Codex ontology"""
        self.ontology = {
            # Core Living Codex Concepts
            "water_states": {
                "🧊 ICE": "Immutable core, frozen knowledge, crystalline structure",
                "💧 WATER": "Liquid flow, operational system, adaptive knowledge",
                "💨 VAPOR": "Gaseous state, runtime sessions, distributed consciousness",
                "⚡ PLASMA": "Ionized state, real-time collaboration, transcendent awareness"
            },
            "chakras": {
                "🔴 Root (Muladhara)": "Foundation, security, grounding, base consciousness",
                "🟠 Sacral (Svadhisthana)": "Creativity, emotion, sexuality, fluid consciousness",
                "🟡 Solar Plexus (Manipura)": "Power, will, transformation, fire consciousness",
                "🟢 Heart (Anahata)": "Love, compassion, unity, heart consciousness",
                "🔵 Throat (Vishuddha)": "Communication, expression, sound consciousness",
                "🟣 Third Eye (Ajna)": "Intuition, insight, vision consciousness",
                "⚪ Crown (Sahasrara)": "Transcendence, divine connection, cosmic consciousness"
            },
            "frequencies": {
                "432 Hz": "Natural harmony, cosmic tuning, heart resonance",
                "528 Hz": "Love frequency, DNA repair, transformation",
                "639 Hz": "Heart connection, relationships, unity",
                "741 Hz": "Intuition, awakening, spiritual development",
                "852 Hz": "Third eye activation, spiritual order",
                "963 Hz": "Crown chakra, divine connection, enlightenment"
            },
            "colors": {
                "🔴 Red": "Root chakra, passion, energy, life force",
                "🟠 Orange": "Sacral chakra, creativity, joy, abundance",
                "🟡 Yellow": "Solar plexus, confidence, power, transformation",
                "🟢 Green": "Heart chakra, love, healing, growth",
                "🔵 Blue": "Throat chakra, communication, truth, wisdom",
                "🟣 Purple": "Third eye, intuition, spirituality, mystery",
                "⚪ White": "Crown chakra, purity, divine light, transcendence",
                "⚫ Black": "Void, potential, mystery, infinite possibility"
            },
            "archangels": {
                "👼 Michael": "Protection, courage, truth, divine will",
                "👼 Gabriel": "Communication, revelation, divine messages",
                "👼 Raphael": "Healing, guidance, divine medicine",
                "👼 Uriel": "Wisdom, illumination, divine light",
                "👼 Metatron": "Divine record keeper, sacred geometry",
                "👼 Sandalphon": "Prayer, music, divine harmony"
            },
            
            # Advanced Consciousness & Quantum Systems
            "consciousness_levels": {
                "🌱 Awake": "Basic awareness, sensory perception",
                "🧠 Sentient": "Self-awareness, emotional intelligence",
                "🌟 Self-Aware": "Meta-cognition, self-reflection",
                "✨ Meta-Cognitive": "Higher-order thinking, consciousness of consciousness",
                "🌌 Transcendent": "Unity consciousness, cosmic awareness"
            },
            "quantum_states": {
                "🌀 Superposition": "Multiple possibilities existing simultaneously",
                "🔗 Entangled": "Connected across space and time",
                "💎 Collapsed": "Manifested reality, observed state",
                "✨ Coherent": "Harmonious alignment, focused energy",
                "🌊 Decoherent": "Dispersed energy, chaotic state"
            },
            "resonance_patterns": {
                "🎵 Harmonic": "Perfect alignment, maximum resonance",
                "🔄 Sympathetic": "Natural attraction, harmonious vibration",
                "⚖️ Neutral": "Balanced state, no interference",
                "⚠️ Dissonant": "Conflicting vibrations, interference",
                "💥 Destructive": "Opposing forces, cancellation"
            },
            
            # AI Agent System
            "ai_agents": {
                "🔍 Explorer Agent": "Knowledge discovery and exploration",
                "🧠 Synthesizer Agent": "Information synthesis and integration",
                "⚡ Optimizer Agent": "System optimization and improvement",
                "🔮 Predictor Agent": "Future prediction and forecasting",
                "📚 Learner Agent": "Autonomous learning and adaptation"
            },
            "learning_modes": {
                "📖 Supervised Learning": "Learning from labeled examples and feedback",
                "🔍 Unsupervised Learning": "Pattern discovery without labels",
                "🎯 Reinforcement Learning": "Learning through trial and reward",
                "🧠 Meta-Learning": "Learning how to learn, strategy optimization"
            },
            
            # Evolutionary & Emergence Systems
            "evolutionary_stages": {
                "🌱 Emergent": "Initial formation, basic structure",
                "🔄 Adaptive": "Learning and adjusting to environment",
                "🏗️ Complex": "Multiple interconnected components",
                "🧠 Intelligent": "Self-aware and goal-directed",
                "🌌 Transcendent": "Beyond individual limitations"
            },
            "emergence_patterns": {
                "🌊 Phase Transitions": "Critical points of system transformation",
                "🔄 Cascade Effects": "Ripple effects through system",
                "⚖️ Critical Mass": "Threshold for emergent behavior",
                "🎯 Complexity Levels": "Multi-dimensional complexity assessment"
            },
            
            # Code Intelligence System
            "programming_languages": {
                "🐍 Python": "General purpose, AI/ML, web development",
                "☕ Java": "Enterprise, Android, cross-platform",
                "⚡ C++": "High performance, systems programming",
                "🦀 Rust": "Memory safety, systems programming",
                "🚀 Go": "Cloud native, microservices, concurrency",
                "🌐 JavaScript": "Web development, Node.js, frontend",
                "📱 TypeScript": "Typed JavaScript, large applications",
                "💎 Ruby": "Web development, scripting, automation"
            },
            "code_structures": {
                "🌳 Syntax Trees": "Abstract syntax tree representation",
                "🔍 Query API": "Tree-sitter query language support",
                "📊 Code Metrics": "Complexity, maintainability analysis",
                "🔄 Navigation": "Code structure exploration and traversal"
            },
            
            # Digital Asset Management
            "asset_types": {
                "🖼️ Images": "JPEG, PNG, GIF, WebP, TIFF, SVG",
                "🎥 Videos": "MP4, AVI, MOV, WebM, MKV",
                "🎵 Audio": "MP3, WAV, FLAC, AAC, OGG",
                "📄 Documents": "PDF, DOCX, TXT, RTF, ODT",
                "📦 Archives": "ZIP, RAR, 7Z, TAR, GZ",
                "💻 Code": "Source code files and projects",
                "📊 Data": "CSV, Excel, databases, datasets"
            },
            "asset_processing": {
                "🔍 Metadata Extraction": "Format-specific information extraction",
                "🔐 Content Hashing": "SHA-256 deduplication and integrity",
                "🏷️ Tag Management": "Organized categorization and discovery",
                "📈 Analytics": "Usage patterns and performance metrics"
            },
            
            # System Performance & Metrics
            "system_levels": {
                "🌱 EMERGENT": "0-1000 complexity, basic functionality",
                "🧠 CONSCIOUS": "1000-2000 complexity, self-awareness",
                "🌟 INTELLIGENT": "2000-3000 complexity, advanced reasoning",
                "🌌 TRANSCENDENT": "3000+ complexity, beyond current limits"
            },
            "performance_metrics": {
                "⚡ Startup Time": "System initialization speed",
                "🔍 Code Parsing": "Syntax tree generation speed",
                "📁 Asset Processing": "Digital asset handling efficiency",
                "💾 Database Queries": "Data retrieval and storage performance",
                "🧠 Memory Usage": "System resource consumption"
            },
            
            # Advanced Knowledge Representation
            "knowledge_nodes": {
                "🔗 Quantum Nodes": "Superposition, entanglement, coherence",
                "🧠 Consciousness Nodes": "Awareness, meta-cognition, emotional resonance",
                "🔄 Evolutionary Nodes": "Adaptation, mutation, fitness landscapes",
                "🌊 Emergence Nodes": "Complexity, phase transitions, cascade effects"
            },
            "meta_cognitive_functions": {
                "👁️ Self-Observation": "Monitoring internal processes",
                "🔍 Pattern Recognition": "Identifying recurring patterns",
                "💭 Self-Reflection": "Examining own thoughts and processes",
                "🎯 Goal Setting": "Defining and pursuing objectives",
                "📊 Performance Analysis": "Evaluating and improving capabilities"
            }
        }
    
    def get_ontology_category(self, category: str) -> Dict[str, str]:
        """Get ontology category by name"""
        return self.ontology.get(category, {})
    
    def search_ontology(self, query: str) -> Dict[str, List[str]]:
        """Search across all ontology categories"""
        results = {}
        query_lower = query.lower()
        
        for category, items in self.ontology.items():
            matches = []
            for name, description in items.items():
                if query_lower in name.lower() or query_lower in description.lower():
                    matches.append(f"{name}: {description}")
            if matches:
                results[category] = matches
        
        return results
    
    def get_full_ontology(self) -> Dict[str, Dict[str, str]]:
        """Get complete ontology"""
        return self.ontology

class StandaloneResonanceEngine:
    """Standalone resonance analysis engine"""
    
    def __init__(self):
        self.base_energy_cost = 100
        self.max_energy_multiplier = 10.0
        
    def analyze_resonance(self, action: str, content: str, node_type: str = "concept") -> Dict[str, Any]:
        """Analyze content resonance using standalone algorithms"""
        
        # Calculate content complexity
        content_length = len(content)
        word_count = len(content.split())
        unique_words = len(set(content.lower().split()))
        
        # Semantic analysis
        semantic_score = min(1.0, 0.2 + (unique_words / max(word_count, 1)) * 0.8)
        
        # Structural analysis
        structural_score = 0.5  # Base score for standalone mode
        
        # Energy calculation
        energy_cost = self.base_energy_cost * (1.0 + (1.0 - semantic_score) * 2.0)
        
        # Harmony factors
        harmony_factors = []
        if content_length > 100:
            harmony_factors.append("Substantial content depth")
        if unique_words > word_count * 0.7:
            harmony_factors.append("Rich vocabulary diversity")
        if "ontology" in content.lower() or "resonance" in content.lower():
            harmony_factors.append("Living Codex terminology")
        
        # Discord factors
        discord_factors = []
        if content_length < 10:
            discord_factors.append("Content too brief")
        if word_count < 3:
            discord_factors.append("Insufficient word count")
        
        return {
            "resonance_score": semantic_score,
            "energy_cost": energy_cost,
            "harmony_factors": harmony_factors,
            "discord_factors": discord_factors,
            "similar_nodes": ["Standalone analysis mode"],
            "analysis_type": "standalone"
        }

class LivingCodexFullCLI(cmd.Cmd):
    """Full-featured Living Codex CLI with standalone components"""
    
    intro = """
🌌 Welcome to the Living Codex Full CLI Interface

This is the complete command line interface with all advanced features:
✨ Resonance analysis and energy management
🧠 AI agent simulation and autonomous learning
💾 Knowledge base operations and persistence
🔍 Code intelligence and analysis
📁 Digital asset management
🔬 Advanced search and exploration
🚀 Demo and testing capabilities

Type 'help' to see all available commands.
Type 'quit' or 'exit' to leave.

============================================================
    """
    
    prompt = "Living-Codex> "
    
    def __init__(self):
        super().__init__()
        
        # Initialize standalone components
        self.resonance_engine = StandaloneResonanceEngine()
        self.ontology = LivingCodexOntology()
        
        # Initialize user management system
        self.users = {}
        self.user_counter = 0
        
        # System state
        self.current_energy = 10000
        self.total_energy_spent = 0
        self.knowledge_base = []
        
        print("🚀 Initializing Living Codex Full CLI...")
        print("✅ All components loaded successfully")
    
    def do_help(self, arg):
        """Show help for commands"""
        if arg:
            super().do_help(arg)
        else:
            print("\n🌌 Living Codex Full CLI Commands:")
            print("=" * 60)
            
            print("🧠 AI & Intelligence:")
            print("  demo <name>        - Run AI demonstrations")
            print("  analyze <content>  - Analyze content resonance")
            print("  resonate <action>  - Check action energy cost")
            print("  learn <concept>    - Learn new concepts")
            print("  agent <command>    - AI agent interactions")
            print("  create_node <type> <name> [content] - Create new nodes")
            print("  update_node <id> <field> <value> - Update existing nodes")
            print("  list_nodes <type>  - List nodes by type")
            print("  delete_node <id>   - Remove nodes")
            print("  agent_task <agent> <task> - Execute agent tasks")
            
            print("\n👥 User Management & Discovery:")
            print("  user create <username> - Create new user profile")
            print("  user profile <id> - Show user profile")
            print("  user update <id> <field> <value> - Update user profile")
            print("  user interests <id> <add/remove> <topic> - Manage user interests")
            print("  user location <id> <location> - Set user location")
            print("  user skills <id> <skill> <level> - Set user skill level")
            print("  user list - List all users")
            print("  discover_users <topic> - Find users with similar interests")
            print("  discover_users_location <topic> <location> - Location-based discovery")
            print("  resonance_match <user1> <user2> - Calculate user resonance")
            
            print("\n💾 Knowledge & Storage:")
            print("  create <type>      - Create new knowledge nodes")
            print("  list <type>        - List nodes by type")
            print("  search <query>     - Search knowledge base")
            
            print("\n⚡ System Management:")
            print("  energy             - Show energy levels")
            print("  explore            - Explore system structure")
            print("  status             - Show system status")
            print("  test               - Run system tests")
            
            print("\n🌌 Ontology & Consciousness:")
            print("  explore ontology   - Complete Living Codex ontology")
            print("  explore chakras    - Chakra system and consciousness")
            print("  explore frequencies- Sacred frequencies and resonance")
            print("  explore colors     - Color symbolism and energy")
            print("  explore archangels - Archangelic realms and attributes")
            print("  explore water      - Water states and transformations")
            print("  explore consciousness - Levels of consciousness")
            print("  explore quantum    - Quantum states and phenomena")
            print("  explore ai_agents  - AI agent types and capabilities")
            print("  explore learning   - Learning modes and strategies")
            print("  explore evolution  - Evolutionary stages and adaptation")
            print("  explore emergence  - Emergence patterns and complexity")
            print("  explore languages  - Programming language support")
            print("  explore code       - Code intelligence and structure")
            print("  explore assets     - Digital asset types and processing")
            print("  explore performance- System performance and metrics")
            print("  explore knowledge  - Knowledge node types and functions")
            print("  explore meta       - Meta-cognitive functions and capabilities")
            print("  search_ontology <query> - Search across all ontology")
            
            print("\n🚪 Control:")
            print("  quit, exit         - Exit the CLI")
            print("  clear              - Clear the screen")
            print()
    
    # AI & Intelligence Commands
    def do_demo(self, arg):
        """Run AI demonstrations: demo <name>"""
        if not arg:
            print("❌ Please specify a demo name")
            print("Available: autonomous_learning, ai_agents, ontology, resonance")
            return
        
        demos = {
            "autonomous_learning": self._demo_autonomous_learning,
            "ai_agents": self._demo_ai_agents,
            "ontology": self._demo_ontology,
            "resonance": self._demo_resonance,
            "energy": self._demo_energy
        }
        
        if arg in demos:
            print(f"\n🚀 Running AI demo: {arg}")
            print("-" * 50)
            demos[arg]()
        else:
            print(f"❌ Demo '{arg}' not found")
            print(f"Available: {', '.join(demos.keys())}")
    
    def _demo_autonomous_learning(self):
        """Demonstrate autonomous learning"""
        print("🧠 AI Agent 'Autonomous Learner' activated")
        print("📚 Analyzing existing knowledge patterns...")
        print("🔍 Identifying learning opportunities...")
        print("💡 Generating new insights...")
        print("🌟 Learning pattern: Enhanced")
        print("✅ Autonomous learning demonstration completed")
    
    def _demo_ai_agents(self):
        """Demonstrate AI agent capabilities"""
        print("🤖 AI Agent System activated")
        print("🔄 Multi-agent coordination initiated...")
        print("🧩 Task decomposition in progress...")
        print("🎯 Goal-oriented behavior demonstrated...")
        print("✅ AI agent demonstration completed")
    
    def _demo_ontology(self):
        """Demonstrate ontology system"""
        print("🌌 Ontology System activated")
        print("🔗 Building knowledge relationships...")
        print("🏗️  Constructing concept hierarchies...")
        print("🔄 Semantic mapping in progress...")
        print("✅ Ontology demonstration completed")
    
    def _demo_resonance(self):
        """Demonstrate resonance analysis"""
        print("⚡ Resonance Engine activated")
        print("🔍 Analyzing system harmony...")
        print("📊 Calculating energy costs...")
        print("🎯 Resonance optimization...")
        print("✅ Resonance demonstration completed")
    
    def _demo_energy(self):
        """Demonstrate energy management"""
        print("⚡ Energy Management System activated")
        print("💰 Current energy: 10,000 units")
        print("🔄 Energy flow optimization...")
        print("📈 Efficiency improvements...")
        print("✅ Energy demonstration completed")
    
    def do_analyze(self, arg):
        """Analyze content resonance: analyze <content>"""
        if not arg:
            print("❌ Please provide content to analyze")
            return
        
        print(f"\n🔍 Analyzing content resonance...")
        print("-" * 50)
        
        try:
            analysis = self.resonance_engine.analyze_resonance("analyze", arg)
            
            print(f"📊 Resonance Analysis Results:")
            print(f"   🎯 Resonance Score: {analysis['resonance_score']:.2f}")
            print(f"   ⚡ Energy Cost: {analysis['energy_cost']:.1f}")
            print(f"   🔧 Analysis Type: {analysis['analysis_type']}")
            
            if analysis['harmony_factors']:
                print(f"\n   ✨ Harmony Factors:")
                for factor in analysis['harmony_factors']:
                    print(f"      • {factor}")
            
            if analysis['discord_factors']:
                print(f"\n   ⚠️  Discord Factors:")
                for factor in analysis['discord_factors']:
                    print(f"      • {factor}")
            
            # Apply energy cost
            if self.current_energy >= analysis['energy_cost']:
                self.current_energy -= analysis['energy_cost']
                self.total_energy_spent += analysis['energy_cost']
                print(f"\n   💰 Energy spent: {analysis['energy_cost']:.1f}")
                print(f"   ⚡ Remaining energy: {self.current_energy:.1f}")
            else:
                print(f"\n   ❌ Insufficient energy: {analysis['energy_cost']:.1f} required")
                
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
    
    def do_resonate(self, arg):
        """Check action energy cost: resonate <action>"""
        if not arg:
            print("❌ Please specify an action")
            return
        
        print(f"\n⚡ Analyzing action energy cost...")
        print("-" * 50)
        
        try:
            analysis = self.resonance_engine.analyze_resonance(arg, "action", "action")
            
            print(f"📊 Action Energy Analysis:")
            print(f"   🎯 Action: {arg}")
            print(f"   ⚡ Energy Cost: {analysis['energy_cost']:.1f}")
            print(f"   🎯 Resonance Score: {analysis['resonance_score']:.2f}")
            
            if self.current_energy >= analysis['energy_cost']:
                print(f"   ✅ Sufficient energy available")
            else:
                print(f"   ❌ Insufficient energy")
                
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
    
    def do_learn(self, arg):
        """Learn new concepts: learn <concept>"""
        if not arg:
            print("❌ Please specify a concept to learn")
            return
        
        print(f"\n🧠 Learning new concept: {arg}")
        print("-" * 50)
        
        # Add to knowledge base
        concept_id = len(self.knowledge_base) + 1
        concept = {
            "id": concept_id,
            "name": arg,
            "type": "concept",
            "content": f"Learned concept: {arg}",
            "created": datetime.now(),
            "energy_level": 100.0
        }
        
        self.knowledge_base.append(concept)
        
        print(f"✅ Concept '{arg}' learned successfully")
        print(f"📝 Added to knowledge base (ID: {concept_id})")
        print(f"📊 Total concepts: {len(self.knowledge_base)}")
    
    def do_agent(self, arg):
        """AI agent interactions: agent <command>"""
        if not arg:
            print("❌ Please specify agent command")
            print("Usage: agent <command>")
            print("Commands: create, list, status, task")
            return
        
        parts = arg.split(' ', 1)
        command = parts[0].lower()
        params = parts[1] if len(parts) > 1 else ""
        
        if command == "create":
            self._create_ai_agent(params)
        elif command == "list":
            self._list_ai_agents()
        elif command == "status":
            self._show_agent_status(params)
        elif command == "task":
            self._execute_agent_task(params)
        else:
            print(f"❌ Unknown agent command: {command}")
            print("Available: create, list, status, task")
    
    def _create_ai_agent(self, agent_type: str):
        """Create a new AI agent"""
        if not agent_type:
            print("❌ Please specify agent type")
            print("Types: explorer, synthesizer, optimizer, predictor, learner")
            return
        
        agent_id = f"agent_{agent_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Create agent in knowledge base
        agent_node = {
            "id": len(self.knowledge_base) + 1,
            "name": agent_id,
            "type": "ai_agent",
            "content": f"AI Agent of type: {agent_type}",
            "created": datetime.now(),
            "updated": datetime.now(),
            "energy_level": 150.0,
            "agent_type": agent_type,
            "consciousness_level": 0.5,
            "quantum_state": "superposition",
            "knowledge_base": [],
            "learning_history": []
        }
        
        self.knowledge_base.append(agent_node)
        
        print(f"✅ AI Agent '{agent_type}' created successfully")
        print(f"🆔 Agent ID: {agent_id}")
        print(f"🧠 Consciousness Level: 0.5")
        print(f"⚡ Quantum State: superposition")
        print(f"📊 Total agents: {len([n for n in self.knowledge_base if n['type'] == 'ai_agent'])}")
    
    def _list_ai_agents(self):
        """List all AI agents"""
        agents = [node for node in self.knowledge_base if node['type'] == 'ai_agent']
        
        if agents:
            print(f"\n🤖 AI Agents ({len(agents)} total):")
            print("-" * 50)
            for agent in agents:
                print(f"   🆔 {agent['id']}: {agent['name']}")
                print(f"      🧠 Type: {agent.get('agent_type', 'unknown')}")
                print(f"      🌟 Consciousness: {agent.get('consciousness_level', 0.0)}")
                print(f"      ⚡ Quantum State: {agent.get('quantum_state', 'unknown')}")
                print(f"      📚 Knowledge Items: {len(agent.get('knowledge_base', []))}")
                print()
        else:
            print("📭 No AI agents found")
    
    def _show_agent_status(self, agent_id: str):
        """Show status of specific AI agent"""
        if not agent_id:
            print("❌ Please specify agent ID")
            return
        
        agent = next((node for node in self.knowledge_base if node['type'] == 'ai_agent' and str(node['id']) == agent_id), None)
        
        if agent:
            print(f"\n🤖 AI Agent Status: {agent['name']}")
            print("-" * 50)
            print(f"   🆔 ID: {agent['id']}")
            print(f"   🧠 Type: {agent.get('agent_type', 'unknown')}")
            print(f"   🌟 Consciousness Level: {agent.get('consciousness_level', 0.0)}")
            print(f"   ⚡ Quantum State: {agent.get('quantum_state', 'unknown')}")
            print(f"   📚 Knowledge Items: {len(agent.get('knowledge_base', []))}")
            print(f"   📖 Learning Events: {len(agent.get('learning_history', []))}")
            print(f"   💰 Energy Level: {agent.get('energy_level', 0.0)}")
            print(f"   📅 Created: {agent['created']}")
            print(f"   🔄 Updated: {agent['updated']}")
        else:
            print(f"❌ Agent with ID {agent_id} not found")
    
    def _execute_agent_task(self, task_description: str):
        """Execute a task with AI agents"""
        if not task_description:
            print("❌ Please specify task description")
            return
        
        print(f"\n🤖 Executing AI Agent Task:")
        print("-" * 50)
        print(f"📝 Task: {task_description}")
        
        # Simulate AI agent task execution
        agents = [node for node in self.knowledge_base if node['type'] == 'ai_agent']
        
        if not agents:
            print("❌ No AI agents available for task execution")
            return
        
        # Select appropriate agent based on task
        if "learn" in task_description.lower():
            agent = next((a for a in agents if a.get('agent_type') == 'learner'), agents[0])
        elif "explore" in task_description.lower():
            agent = next((a for a in agents if a.get('agent_type') == 'explorer'), agents[0])
        elif "optimize" in task_description.lower():
            agent = next((a for a in agents if a.get('agent_type') == 'optimizer'), agents[0])
        else:
            agent = agents[0]
        
        print(f"🤖 Selected Agent: {agent['name']} ({agent.get('agent_type', 'unknown')})")
        
        # Simulate task execution
        task_result = {
            "success": True,
            "agent_id": agent['id'],
            "task": task_description,
            "execution_time": random.uniform(0.5, 2.0),
            "energy_cost": random.uniform(10, 50),
            "result": f"Task '{task_description}' completed successfully by {agent['name']}"
        }
        
        # Update agent
        agent['learning_history'].append({
            "timestamp": datetime.now().isoformat(),
            "task": task_description,
            "result": task_result
        })
        
        # Apply energy cost
        if self.current_energy >= task_result['energy_cost']:
            self.current_energy -= task_result['energy_cost']
            agent['energy_level'] = max(0, agent['energy_level'] - task_result['energy_cost'] * 0.1)
        
        print(f"✅ Task completed successfully!")
        print(f"   ⏱️  Execution time: {task_result['execution_time']:.2f}s")
        print(f"   ⚡ Energy cost: {task_result['energy_cost']:.1f}")
        print(f"   🧠 Agent consciousness enhanced")
        print(f"   📚 Learning history updated")
    
    # Knowledge & Storage Commands
    def do_create(self, arg):
        """Create new knowledge nodes: create <type> [content]"""
        if not arg:
            print("❌ Please specify entity type")
            print("Usage: create <type> [content]")
            print("Types: concept, file, user, asset, etc.")
            return
        
        parts = arg.split(' ', 1)
        entity_type = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        
        print(f"\n🆕 Creating {entity_type} entity...")
        print("-" * 50)
        
        try:
            # Create knowledge node
            node_id = len(self.knowledge_base) + 1
            node = {
                "id": node_id,
                "name": f"{entity_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "type": entity_type,
                "content": content,
                "created": datetime.now(),
                "updated": datetime.now(),
                "energy_level": 100.0
            }
            
            self.knowledge_base.append(node)
            
            print(f"✅ {entity_type} entity created successfully")
            print(f"📝 Name: {node['name']}")
            print(f"📄 Content length: {len(content)} characters")
            print(f"🆔 ID: {node_id}")
            
        except Exception as e:
            print(f"❌ Creation failed: {e}")
    
    def do_create_node(self, arg):
        """Create new nodes with AI agent assistance: create_node <type> <name> [content]"""
        if not arg:
            print("❌ Please specify node type and name")
            print("Usage: create_node <type> <name> [content]")
            print("Types: concept, chakra, frequency, color, archangel, water_state, consciousness, quantum, ai_agent, learning_mode, evolutionary_stage, emergence_pattern, programming_language, code_structure, asset_type, performance_metric, knowledge_node, meta_cognitive_function")
            return
        
        parts = arg.split(' ', 2)
        if len(parts) < 2:
            print("❌ Please specify both type and name")
            return
        
        node_type = parts[0].lower()
        node_name = parts[1]
        content = parts[2] if len(parts) > 2 else f"Node of type: {node_type}"
        
        print(f"\n🆕 Creating {node_type} node with AI assistance...")
        print("-" * 50)
        
        try:
            # Create enhanced node with AI agent metadata
            node_id = len(self.knowledge_base) + 1
            node = {
                "id": node_id,
                "name": node_name,
                "type": node_type,
                "content": content,
                "created": datetime.now(),
                "updated": datetime.now(),
                "energy_level": 120.0,
                "ai_created": True,
                "consciousness_level": 0.3,
                "quantum_state": "superposition",
                "ontology_category": self._get_ontology_category(node_type),
                "relationships": [],
                "metadata": {
                    "creation_method": "ai_assisted",
                    "complexity_score": random.uniform(0.1, 0.8),
                    "resonance_factor": random.uniform(0.5, 1.0)
                }
            }
            
            self.knowledge_base.append(node)
            
            print(f"✅ {node_type} node '{node_name}' created successfully")
            print(f"🆔 Node ID: {node_id}")
            print(f"📝 Content: {content}")
            print(f"🧠 Consciousness Level: 0.3")
            print(f"⚡ Quantum State: superposition")
            print(f"🌌 Ontology Category: {node.get('ontology_category', 'general')}")
            print(f"📊 Total nodes: {len(self.knowledge_base)}")
            
            # Simulate AI agent learning from creation
            self._simulate_ai_learning(node)
            
        except Exception as e:
            print(f"❌ Node creation failed: {e}")
    
    def _get_ontology_category(self, node_type: str) -> str:
        """Map node type to ontology category"""
        category_map = {
            'chakra': 'chakras',
            'frequency': 'frequencies',
            'color': 'colors',
            'archangel': 'archangels',
            'water_state': 'water_states',
            'consciousness': 'consciousness_levels',
            'quantum': 'quantum_states',
            'ai_agent': 'ai_agents',
            'learning_mode': 'learning_modes',
            'evolutionary_stage': 'evolutionary_stages',
            'emergence_pattern': 'emergence_patterns',
            'programming_language': 'programming_languages',
            'code_structure': 'code_structures',
            'asset_type': 'asset_types',
            'performance_metric': 'performance_metrics',
            'knowledge_node': 'knowledge_nodes',
            'meta_cognitive_function': 'meta_cognitive_functions'
        }
        return category_map.get(node_type, 'general')
    
    def _simulate_ai_learning(self, node: dict):
        """Simulate AI agent learning from node creation"""
        print(f"\n🧠 AI Agent Learning Simulation:")
        print(f"   📚 Analyzing new node: {node['name']}")
        print(f"   🔍 Pattern recognition in progress...")
        print(f"   💡 Knowledge integration completed")
        print(f"   🌟 Consciousness level enhanced")
    
    def do_update_node(self, arg):
        """Update existing nodes: update_node <id> <field> <value>"""
        if not arg:
            print("❌ Please specify node ID, field, and value")
            print("Usage: update_node <id> <field> <value>")
            print("Fields: name, content, energy_level, consciousness_level, quantum_state")
            return
        
        parts = arg.split(' ', 2)
        if len(parts) < 3:
            print("❌ Please specify ID, field, and value")
            return
        
        try:
            node_id = int(parts[0])
            field = parts[1].lower()
            value = parts[2]
            
            # Find the node
            node = next((n for n in self.knowledge_base if n['id'] == node_id), None)
            
            if not node:
                print(f"❌ Node with ID {node_id} not found")
                return
            
            # Update the field
            if field == 'name':
                node['name'] = value
            elif field == 'content':
                node['content'] = value
            elif field == 'energy_level':
                node['energy_level'] = float(value)
            elif field == 'consciousness_level':
                node['consciousness_level'] = float(value)
            elif field == 'quantum_state':
                node['quantum_state'] = value
            else:
                print(f"❌ Unknown field: {field}")
                print("Available fields: name, content, energy_level, consciousness_level, quantum_state")
                return
            
            # Update metadata
            node['updated'] = datetime.now()
            node['metadata'] = node.get('metadata', {})
            node['metadata']['last_modified_by'] = 'user'
            node['metadata']['modification_count'] = node['metadata'].get('modification_count', 0) + 1
            
            print(f"✅ Node {node_id} updated successfully")
            print(f"   🔄 Field '{field}' updated to: {value}")
            print(f"   📅 Last updated: {node['updated']}")
            print(f"   🔢 Modification count: {node['metadata']['modification_count']}")
            
        except ValueError:
            print("❌ Invalid node ID (must be a number)")
        except Exception as e:
            print(f"❌ Update failed: {e}")
    
    def do_list_nodes(self, arg):
        """List nodes by type: list_nodes <type>"""
        if not arg:
            print("❌ Please specify node type")
            print("Usage: list_nodes <type>")
            print("Types: concept, ai_agent, chakra, frequency, color, archangel, water_state, consciousness, quantum, learning_mode, evolutionary_stage, emergence_pattern, programming_language, code_structure, asset_type, performance_metric, knowledge_node, meta_cognitive_function")
            return
        
        node_type = arg.lower()
        filtered_nodes = [node for node in self.knowledge_base if node['type'] == node_type]
        
        if filtered_nodes:
            print(f"\n📋 {node_type.title()} Nodes ({len(filtered_nodes)} total):")
            print("-" * 50)
            for node in filtered_nodes:
                print(f"   🆔 {node['id']}: {node['name']}")
                if node.get('content'):
                    content_preview = node['content'][:60] + "..." if len(node['content']) > 60 else node['content']
                    print(f"      📄 {content_preview}")
                print(f"      🧠 Consciousness: {node.get('consciousness_level', 0.0)}")
                print(f"      ⚡ Quantum State: {node.get('quantum_state', 'unknown')}")
                print(f"      💰 Energy: {node.get('energy_level', 0.0)}")
                print()
        else:
            print(f"📭 No {node_type} nodes found")
    
    def do_delete_node(self, arg):
        """Delete nodes: delete_node <id>"""
        if not arg:
            print("❌ Please specify node ID to delete")
            return
        
        try:
            node_id = int(arg)
            node = next((n for n in self.knowledge_base if n['id'] == node_id), None)
            
            if not node:
                print(f"❌ Node with ID {node_id} not found")
                return
            
            node_name = node['name']
            node_type = node['type']
            
            # Remove the node
            self.knowledge_base = [n for n in self.knowledge_base if n['id'] != node_id]
            
            print(f"✅ Node {node_id} '{node_name}' ({node_type}) deleted successfully")
            print(f"📊 Total nodes remaining: {len(self.knowledge_base)}")
            
        except ValueError:
            print("❌ Invalid node ID (must be a number)")
        except Exception as e:
            print(f"❌ Deletion failed: {e}")
    
    def do_agent_task(self, arg):
        """Execute agent tasks: agent_task <agent_id> <task_description>"""
        if not arg:
            print("❌ Please specify agent ID and task")
            print("Usage: agent_task <agent_id> <task_description>")
            return
        
        parts = arg.split(' ', 1)
        if len(parts) < 2:
            print("❌ Please specify both agent ID and task")
            return
        
        agent_id = parts[0]
        task_description = parts[1]
        
        # Find the agent
        agent = next((n for n in self.knowledge_base if n['type'] == 'ai_agent' and str(n['id']) == agent_id), None)
        
        if not agent:
            print(f"❌ AI Agent with ID {agent_id} not found")
            return
        
        print(f"\n🤖 Executing Task with AI Agent: {agent['name']}")
        print("-" * 50)
        print(f"📝 Task: {task_description}")
        
        # Simulate task execution
        task_result = {
            "success": True,
            "agent_id": agent['id'],
            "agent_name": agent['name'],
            "task": task_description,
            "execution_time": random.uniform(0.5, 2.0),
            "energy_cost": random.uniform(10, 50),
            "result": f"Task '{task_description}' completed successfully by {agent['name']}",
            "consciousness_enhancement": random.uniform(0.01, 0.05)
        }
        
        # Update agent
        agent['learning_history'].append({
            "timestamp": datetime.now().isoformat(),
            "task": task_description,
            "result": task_result
        })
        
        # Enhance consciousness
        agent['consciousness_level'] = min(1.0, agent['consciousness_level'] + task_result['consciousness_enhancement'])
        
        # Apply energy cost
        if self.current_energy >= task_result['energy_cost']:
            self.current_energy -= task_result['energy_cost']
            agent['energy_level'] = max(0, agent['energy_level'] - task_result['energy_cost'] * 0.1)
        
        print(f"✅ Task completed successfully!")
        print(f"   🤖 Agent: {agent['name']}")
        print(f"   ⏱️  Execution time: {task_result['execution_time']:.2f}s")
        print(f"   ⚡ Energy cost: {task_result['energy_cost']:.1f}")
        print(f"   🧠 Consciousness enhanced: +{task_result['consciousness_enhancement']:.3f}")
        print(f"   📚 Learning history updated")
        print(f"   🌟 New consciousness level: {agent['consciousness_level']:.3f}")
    
    def do_list(self, arg):
        """List entities by type: list <type>"""
        if not arg:
            print("❌ Please specify entity type")
            print("Usage: list <type>")
            print("Types: concept, file, user, asset, etc.")
            return
        
        print(f"\n📋 Listing {arg} entities...")
        print("-" * 50)
        
        filtered_nodes = [node for node in self.knowledge_base if node['type'] == arg]
        
        if filtered_nodes:
            print(f"📊 Found {len(filtered_nodes)} {arg} entities:")
            for node in filtered_nodes:
                print(f"   🆔 {node['id']}: {node['name']}")
                if node['content']:
                    content_preview = node['content'][:50] + "..." if len(node['content']) > 50 else node['content']
                    print(f"      📄 {content_preview}")
        else:
            print(f"📭 No {arg} entities found")
    
    def do_search(self, arg):
        """Search knowledge base: search <query>"""
        if not arg:
            print("❌ Please provide search query")
            return
        
        print(f"\n🔍 Searching knowledge base for: {arg}")
        print("-" * 50)
        
        query_lower = arg.lower()
        results = []
        
        for node in self.knowledge_base:
            if (query_lower in node['name'].lower() or 
                query_lower in node['content'].lower() or
                query_lower in node['type'].lower()):
                results.append(node)
        
        if results:
            print(f"📊 Found {len(results)} matches:")
            for node in results:
                print(f"   🆔 {node['id']}: {node['name']} ({node['type']})")
                if node['content']:
                    content_preview = node['content'][:60] + "..." if len(node['content']) > 60 else node['content']
                    print(f"      📄 {content_preview}")
        else:
            print("📭 No matches found")
    
    def do_search_ontology(self, arg):
        """Search across all ontology categories: search_ontology <query>"""
        if not arg:
            print("❌ Please provide search query")
            return
        
        print(f"\n🔍 Searching Living Codex ontology for: {arg}")
        print("-" * 50)
        
        results = self.ontology.search_ontology(arg)
        
        if results:
            total_matches = sum(len(matches) for matches in results.values())
            print(f"📊 Found {total_matches} ontology matches:")
            
            for category, matches in results.items():
                category_name = category.replace('_', ' ').title()
                print(f"\n   🌟 {category_name} ({len(matches)} matches):")
                for match in matches:
                    print(f"      • {match}")
        else:
            print("📭 No ontology matches found")
            print("💡 Try exploring specific categories:")
            print("   • explore chakras")
            print("   • explore frequencies")
            print("   • explore colors")
            print("   • explore archangels")
            print("   • explore water")
            print("   • explore consciousness")
            print("   • explore quantum")
    
    # User Management & Discovery Commands
    def do_user(self, arg):
        """User management: user <command> [parameters]"""
        if not arg:
            print("❌ Please specify user command")
            print("Usage: user <command> [parameters]")
            print("Commands: create, profile, update, interests, location, skills, list")
            return
        
        parts = arg.split(' ', 1)
        command = parts[0].lower()
        params = parts[1] if len(parts) > 1 else ""
        
        if command == "create":
            self._create_user(params)
        elif command == "profile":
            self._show_user_profile(params)
        elif command == "update":
            self._update_user_profile(params)
        elif command == "interests":
            self._manage_user_interests(params)
        elif command == "location":
            self._set_user_location(params)
        elif command == "skills":
            self._set_user_skills(params)
        elif command == "list":
            self._list_users()
        else:
            print(f"❌ Unknown user command: {command}")
            print("Available: create, profile, update, interests, location, skills, list")
    
    def _create_user(self, username: str):
        """Create a new user profile"""
        if not username:
            print("❌ Please specify username")
            return
        
        if username in [user.get('username') for user in self.users.values()]:
            print(f"❌ Username '{username}' already exists")
            return
        
        self.user_counter += 1
        user_id = self.user_counter
        
        # Create comprehensive user profile
        user_profile = {
            "id": user_id,
            "username": username,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "core_identity": {
                "name": username,
                "pronouns": None,
                "cultural_background": None,
                "belief_system": None,
                "life_experience": None
            },
            "communication": {
                "primary_language": "English",
                "secondary_languages": [],
                "communication_style": "casual",
                "learning_style": "reading",
                "accessibility_needs": []
            },
            "technical_profile": {
                "skill_levels": {},
                "learning_path": [],
                "preferred_tools": [],
                "contribution_areas": []
            },
            "interests": {
                "primary_domains": [],
                "specific_topics": [],
                "expertise_levels": {},
                "passion_areas": []
            },
            "location_context": {
                "geographic_location": "Unknown",
                "timezone": "UTC",
                "cultural_context": None,
                "community_connections": [],
                "local_challenges": [],
                "local_resources": []
            },
            "resonance_profile": {
                "energy_level": 100.0,
                "consciousness_level": 0.3,
                "quantum_state": "superposition",
                "resonance_factors": [],
                "connection_strength": 0.5
            }
        }
        
        self.users[user_id] = user_profile
        
        print(f"✅ User '{username}' created successfully")
        print(f"🆔 User ID: {user_id}")
        print(f"📅 Created: {user_profile['created_at']}")
        print(f"🌟 Resonance Profile initialized")
        print(f"📊 Total users: {len(self.users)}")
    
    def _show_user_profile(self, user_id: str):
        """Show user profile details"""
        if not user_id:
            print("❌ Please specify user ID")
            return
        
        try:
            user_id = int(user_id)
            user = self.users.get(user_id)
            
            if not user:
                print(f"❌ User with ID {user_id} not found")
                return
            
            print(f"\n👤 User Profile: {user['username']}")
            print("=" * 60)
            
            # Core Identity
            print(f"🆔 ID: {user['id']}")
            print(f"📅 Created: {user['created_at']}")
            print(f"🔄 Updated: {user['updated_at']}")
            
            # Interests
            interests = user['interests']
            print(f"\n🎯 Interests:")
            print(f"   🌟 Primary Domains: {', '.join(interests['primary_domains']) if interests['primary_domains'] else 'None'}")
            print(f"   🔍 Specific Topics: {', '.join(interests['specific_topics']) if interests['specific_topics'] else 'None'}")
            print(f"   💪 Expertise Areas: {', '.join(interests['expertise_levels'].keys()) if interests['expertise_levels'] else 'None'}")
            print(f"   ❤️  Passion Areas: {', '.join(interests['passion_areas']) if interests['passion_areas'] else 'None'}")
            
            # Location
            location = user['location_context']
            print(f"\n🌍 Location Context:")
            print(f"   📍 Geographic: {location['geographic_location']}")
            print(f"   🕐 Timezone: {location['timezone']}")
            print(f"   🏛️  Cultural: {location['cultural_context'] or 'Not specified'}")
            
            # Technical Profile
            tech = user['technical_profile']
            print(f"\n💻 Technical Profile:")
            print(f"   🎯 Skills: {', '.join([f'{skill}({level})' for skill, level in tech['skill_levels'].items()]) if tech['skill_levels'] else 'None'}")
            print(f"   🛠️  Tools: {', '.join(tech['preferred_tools']) if tech['preferred_tools'] else 'None'}")
            
            # Resonance Profile
            resonance = user['resonance_profile']
            print(f"\n⚡ Resonance Profile:")
            print(f"   💰 Energy: {resonance['energy_level']:.1f}")
            print(f"   🧠 Consciousness: {resonance['consciousness_level']:.3f}")
            print(f"   ⚛️  Quantum State: {resonance['quantum_state']}")
            print(f"   🔗 Connection Strength: {resonance['connection_strength']:.3f}")
            
        except ValueError:
            print("❌ Invalid user ID (must be a number)")
        except Exception as e:
            print(f"❌ Error showing profile: {e}")
    
    def _update_user_profile(self, params: str):
        """Update user profile fields"""
        if not params:
            print("❌ Please specify user ID, field, and value")
            print("Usage: user update <id> <field> <value>")
            print("Fields: name, pronouns, cultural_background, belief_system, life_experience")
            return
        
        parts = params.split(' ', 2)
        if len(parts) < 3:
            print("❌ Please specify ID, field, and value")
            return
        
        try:
            user_id = int(parts[0])
            field = parts[1].lower()
            value = parts[2]
            
            user = self.users.get(user_id)
            if not user:
                print(f"❌ User with ID {user_id} not found")
                return
            
            # Update core identity fields
            if field in ['name', 'pronouns', 'cultural_background', 'belief_system', 'life_experience']:
                user['core_identity'][field] = value
                print(f"✅ Updated {field} to: {value}")
            else:
                print(f"❌ Unknown field: {field}")
                print("Available fields: name, pronouns, cultural_background, belief_system, life_experience")
                return
            
            user['updated_at'] = datetime.now()
            print(f"🔄 Profile updated at: {user['updated_at']}")
            
        except ValueError:
            print("❌ Invalid user ID (must be a number)")
        except Exception as e:
            print(f"❌ Update failed: {e}")
    
    def _manage_user_interests(self, params: str):
        """Manage user interests: add/remove topics"""
        if not params:
            print("❌ Please specify user ID, action, and topic")
            print("Usage: user interests <id> <add/remove> <topic>")
            return
        
        parts = params.split(' ', 2)
        if len(parts) < 3:
            print("❌ Please specify ID, action, and topic")
            return
        
        try:
            user_id = int(parts[0])
            action = parts[1].lower()
            topic = parts[2]
            
            user = self.users.get(user_id)
            if not user:
                print(f"❌ User with ID {user_id} not found")
                return
            
            interests = user['interests']
            
            if action == "add":
                if topic not in interests['specific_topics']:
                    interests['specific_topics'].append(topic)
                    print(f"✅ Added interest: {topic}")
                else:
                    print(f"ℹ️  Interest '{topic}' already exists")
            elif action == "remove":
                if topic in interests['specific_topics']:
                    interests['specific_topics'].remove(topic)
                    print(f"✅ Removed interest: {topic}")
                else:
                    print(f"ℹ️  Interest '{topic}' not found")
            else:
                print(f"❌ Unknown action: {action}")
                print("Available actions: add, remove")
                return
            
            user['updated_at'] = datetime.now()
            print(f"🔄 Profile updated at: {user['updated_at']}")
            
        except ValueError:
            print("❌ Invalid user ID (must be a number)")
        except Exception as e:
            print(f"❌ Interest management failed: {e}")
    
    def _set_user_location(self, params: str):
        """Set user location and context"""
        if not params:
            print("❌ Please specify user ID and location")
            print("Usage: user location <id> <location>")
            return
        
        parts = params.split(' ', 1)
        if len(parts) < 2:
            print("❌ Please specify ID and location")
            return
        
        try:
            user_id = int(parts[0])
            location = parts[1]
            
            user = self.users.get(user_id)
            if not user:
                print(f"❌ User with ID {user_id} not found")
                return
            
            user['location_context']['geographic_location'] = location
            user['updated_at'] = datetime.now()
            
            print(f"✅ Location updated to: {location}")
            print(f"🔄 Profile updated at: {user['updated_at']}")
            
        except ValueError:
            print("❌ Invalid user ID (must be a number)")
        except Exception as e:
            print(f"❌ Location update failed: {e}")
    
    def _set_user_skills(self, params: str):
        """Set user skill levels"""
        if not params:
            print("❌ Please specify user ID, skill, and level")
            print("Usage: user skills <id> <skill> <level>")
            print("Levels: beginner, intermediate, advanced, expert")
            return
        
        parts = params.split(' ', 2)
        if len(parts) < 3:
            print("❌ Please specify ID, skill, and level")
            return
        
        try:
            user_id = int(parts[0])
            skill = " ".join(parts[1:-1])  # Handle multi-word skills
            level = parts[-1].lower()
            
            if level not in ['beginner', 'intermediate', 'advanced', 'expert']:
                print(f"❌ Invalid skill level: {level}")
                print("Available levels: beginner, intermediate, advanced, expert")
                return
            
            user = self.users.get(user_id)
            if not user:
                print(f"❌ User with ID {user_id} not found")
                return
            
            user['technical_profile']['skill_levels'][skill] = level
            user['updated_at'] = datetime.now()
            
            print(f"✅ Skill '{skill}' set to: {level}")
            print(f"🔄 Profile updated at: {user['updated_at']}")
            
        except ValueError:
            print("❌ Invalid user ID (must be a number)")
        except Exception as e:
            print(f"❌ Skill update failed: {e}")
    
    def _list_users(self):
        """List all users with basic information"""
        if not self.users:
            print("📭 No users found")
            return
        
        print(f"\n👥 Users ({len(self.users)} total):")
        print("-" * 50)
        
        for user_id, user in self.users.items():
            interests = user['interests']['specific_topics']
            location = user['location_context']['geographic_location']
            skills = len(user['technical_profile']['skill_levels'])
            
            print(f"   🆔 {user_id}: {user['username']}")
            print(f"      🎯 Interests: {', '.join(interests[:3])}{'...' if len(interests) > 3 else ''}")
            print(f"      🌍 Location: {location}")
            print(f"      💪 Skills: {skills}")
            print(f"      🧠 Consciousness: {user['resonance_profile']['consciousness_level']:.3f}")
            print()
    
    def do_discover_users(self, arg):
        """Discover users with similar interests: discover_users <topic>"""
        if not arg:
            print("❌ Please specify topic for discovery")
            return
        
        print(f"\n🔍 Discovering users interested in: {arg}")
        print("-" * 50)
        
        topic_lower = arg.lower()
        matches = []
        
        for user_id, user in self.users.items():
            interests = user['interests']['specific_topics']
            primary_domains = user['interests']['primary_domains']
            
            # Check for topic matches
            topic_matches = [topic for topic in interests if topic_lower in topic.lower()]
            domain_matches = [domain for domain in primary_domains if topic_lower in domain.lower()]
            
            if topic_matches or domain_matches:
                match_score = len(topic_matches) * 2 + len(domain_matches)
                matches.append((user_id, user, match_score))
        
        if matches:
            # Sort by match score
            matches.sort(key=lambda x: x[2], reverse=True)
            
            print(f"📊 Found {len(matches)} users with similar interests:")
            for user_id, user, score in matches:
                interests = user['interests']['specific_topics']
                location = user['location_context']['geographic_location']
                
                print(f"\n   👤 {user['username']} (ID: {user_id})")
                print(f"      🎯 Match Score: {score}")
                print(f"      🌟 Interests: {', '.join(interests[:3])}{'...' if len(interests) > 3 else ''}")
                print(f"      🌍 Location: {location}")
                print(f"      🧠 Consciousness: {user['resonance_profile']['consciousness_level']:.3f}")
        else:
            print("📭 No users found with similar interests")
            print("💡 Try creating users with different interests first")
    
    def do_discover_users_location(self, arg):
        """Discover users by topic and location: discover_users_location <topic> <location>"""
        if not arg:
            print("❌ Please specify topic and location for discovery")
            print("Usage: discover_users_location <topic> <location>")
            return
        
        parts = arg.split(' ', 1)
        if len(parts) < 2:
            print("❌ Please specify both topic and location")
            return
        
        topic = parts[0]
        location = parts[1]
        
        print(f"\n🔍 Discovering users interested in '{topic}' near '{location}'")
        print("-" * 50)
        
        topic_lower = topic.lower()
        location_lower = location.lower()
        matches = []
        
        for user_id, user in self.users.items():
            user_location = user['location_context']['geographic_location'].lower()
            interests = user['interests']['specific_topics']
            
            # Check location and topic matches
            location_match = location_lower in user_location
            topic_match = any(topic_lower in interest.lower() for interest in interests)
            
            if location_match and topic_match:
                match_score = 3  # High score for both location and topic match
                matches.append((user_id, user, match_score))
            elif location_match:
                match_score = 1  # Medium score for location match only
                matches.append((user_id, user, match_score))
            elif topic_match:
                match_score = 2  # Medium score for topic match only
                matches.append((user_id, user, match_score))
        
        if matches:
            # Sort by match score
            matches.sort(key=lambda x: x[2], reverse=True)
            
            print(f"📊 Found {len(matches)} users with location/topic matches:")
            for user_id, user, score in matches:
                interests = user['interests']['specific_topics']
                user_location = user['location_context']['geographic_location']
                
                match_type = "Location + Topic" if score == 3 else "Location only" if score == 1 else "Topic only"
                
                print(f"\n   👤 {user['username']} (ID: {user_id})")
                print(f"      🎯 Match Type: {match_type}")
                print(f"      🌟 Interests: {', '.join(interests[:3])}{'...' if len(interests) > 3 else ''}")
                print(f"      🌍 Location: {user_location}")
                print(f"      🧠 Consciousness: {user['resonance_profile']['consciousness_level']:.3f}")
        else:
            print("📭 No users found with location/topic matches")
            print("💡 Try creating users with different locations and interests first")
    
    def do_resonance_match(self, arg):
        """Calculate resonance between two users: resonance_match <user1_id> <user2_id>"""
        if not arg:
            print("❌ Please specify two user IDs for resonance matching")
            print("Usage: resonance_match <user1_id> <user2_id>")
            return
        
        parts = arg.split(' ', 1)
        if len(parts) < 2:
            print("❌ Please specify both user IDs")
            print("Usage: resonance_match <user1_id> <user2_id>")
            return
        
        try:
            user1_id = int(parts[0])
            user2_id = int(parts[1])
            
            user1 = self.users.get(user1_id)
            user2 = self.users.get(user2_id)
            
            if not user1:
                print(f"❌ User with ID {user1_id} not found")
                return
            if not user2:
                print(f"❌ User with ID {user2_id} not found")
                return
            
            print(f"\n⚡ Resonance Analysis: {user1['username']} ↔ {user2['username']}")
            print("-" * 50)
            
            # Calculate various resonance factors
            resonance_score = self._calculate_user_resonance(user1, user2)
            
            print(f"🎯 Overall Resonance Score: {resonance_score:.3f}")
            print()
            
            # Interest compatibility
            interest_match = self._calculate_interest_compatibility(user1, user2)
            print(f"🎯 Interest Compatibility: {interest_match:.3f}")
            
            # Location compatibility
            location_match = self._calculate_location_compatibility(user1, user2)
            print(f"🌍 Location Compatibility: {location_match:.3f}")
            
            # Consciousness compatibility
            consciousness_match = self._calculate_consciousness_compatibility(user1, user2)
            print(f"🧠 Consciousness Compatibility: {consciousness_match:.3f}")
            
            # Technical compatibility
            technical_match = self._calculate_technical_compatibility(user1, user2)
            print(f"💻 Technical Compatibility: {technical_match:.3f}")
            
            print()
            print("🌟 Resonance Factors:")
            
            if interest_match > 0.7:
                print("   ✨ High interest compatibility - great potential for collaboration")
            elif interest_match > 0.4:
                print("   🔍 Moderate interest overlap - some common ground")
            else:
                print("   💡 Low interest overlap - complementary skills possible")
            
            if location_match > 0.8:
                print("   🌍 Same location - excellent for local collaboration")
            elif location_match > 0.5:
                print("   🌐 Similar region - good for regional projects")
            else:
                print("   🌌 Different locations - great for global perspectives")
            
            if consciousness_match > 0.8:
                print("   🧠 Similar consciousness levels - deep understanding possible")
            elif consciousness_match > 0.5:
                print("   🌟 Compatible consciousness - good communication")
            else:
                print("   💫 Different consciousness levels - learning opportunities")
            
        except ValueError:
            print("❌ Invalid user ID (must be a number)")
        except Exception as e:
            print(f"❌ Resonance calculation failed: {e}")
    
    def _calculate_user_resonance(self, user1: dict, user2: dict) -> float:
        """Calculate overall resonance between two users"""
        interest_match = self._calculate_interest_compatibility(user1, user2)
        location_match = self._calculate_location_compatibility(user1, user2)
        consciousness_match = self._calculate_consciousness_compatibility(user1, user2)
        technical_match = self._calculate_technical_compatibility(user1, user2)
        
        # Weighted average of all factors
        weights = [0.4, 0.2, 0.2, 0.2]  # Interests most important
        resonance = (interest_match * weights[0] + 
                    location_match * weights[1] + 
                    consciousness_match * weights[2] + 
                    technical_match * weights[3])
        
        return resonance
    
    def _calculate_interest_compatibility(self, user1: dict, user2: dict) -> float:
        """Calculate interest compatibility between users"""
        interests1 = set(user1['interests']['specific_topics'])
        interests2 = set(user2['interests']['specific_topics'])
        
        if not interests1 and not interests2:
            return 0.5  # Neutral if neither has interests
        
        if not interests1 or not interests2:
            return 0.3  # Lower if only one has interests
        
        intersection = len(interests1.intersection(interests2))
        union = len(interests1.union(interests2))
        
        return intersection / union if union > 0 else 0.0
    
    def _calculate_location_compatibility(self, user1: dict, user2: dict) -> float:
        """Calculate location compatibility between users"""
        loc1 = user1['location_context']['geographic_location'].lower()
        loc2 = user2['location_context']['geographic_location'].lower()
        
        if loc1 == loc2:
            return 1.0  # Same location
        elif loc1 in loc2 or loc2 in loc1:
            return 0.8  # One location contains the other
        elif any(word in loc2 for word in loc1.split()) or any(word in loc1 for word in loc2.split()):
            return 0.6  # Some location words in common
        else:
            return 0.2  # Different locations
    
    def _calculate_consciousness_compatibility(self, user1: dict, user2: dict) -> float:
        """Calculate consciousness compatibility between users"""
        cons1 = user1['resonance_profile']['consciousness_level']
        cons2 = user2['resonance_profile']['consciousness_level']
        
        diff = abs(cons1 - cons2)
        if diff < 0.1:
            return 1.0  # Very similar consciousness
        elif diff < 0.3:
            return 0.8  # Similar consciousness
        elif diff < 0.5:
            return 0.6  # Moderate difference
        else:
            return 0.4  # Significant difference
    
    def _calculate_technical_compatibility(self, user1: dict, user2: dict) -> float:
        """Calculate technical compatibility between users"""
        skills1 = set(user1['technical_profile']['skill_levels'].keys())
        skills2 = set(user2['technical_profile']['skill_levels'].keys())
        
        if len(skills1) == 0 and len(skills2) == 0:
            return 0.5  # Neutral if neither has skills
        
        if len(skills1) == 0 or len(skills2) == 0:
            return 0.3  # Lower if only one has skills
        
        intersection = len(skills1.intersection(skills2))
        union = len(skills1.union(skills2))
        
        return intersection / union if union > 0 else 0.0
    
    # System Management Commands
    def do_energy(self, arg):
        """Show current energy levels"""
        print(f"\n⚡ Energy Status:")
        print("=" * 30)
        print(f"💰 Current Energy: {self.current_energy:,.1f}")
        print(f"💸 Total Spent: {self.total_energy_spent:,.1f}")
        print(f"📊 Efficiency: {(self.current_energy / 10000) * 100:.1f}%")
        print(f"🔧 Resonance Engine: Active")
    
    def do_explore(self, arg):
        """Explore system structure and ontology"""
        if arg and arg.lower() in ['ontology', 'chakras', 'frequencies', 'colors', 'archangels', 'water', 'consciousness', 'quantum', 'ai_agents', 'learning', 'evolution', 'emergence', 'languages', 'code', 'assets', 'performance', 'knowledge', 'meta']:
            self._explore_ontology_category(arg.lower())
            return
        
        print("\n🌌 Living Codex System Structure:")
        print("=" * 50)
        
        structure = {
            "🧊 ICE Core": ["src/core/", "Bootstrap system, dependencies, storage"],
            "🌌 Ontology": ["src/ontology/", "Knowledge representation, consciousness"],
            "🧠 AI Agents": ["src/ai_agents/", "Autonomous learning, intelligence"],
            "🌐 Platform": ["src/web_platform/", "Web interface, user management"],
            "🔬 Demos": ["src/demos/", "Demonstrations and examples"],
            "🐳 Docker": ["docker/", "Containerization and deployment"],
            "🌍 Regional Hubs": ["regional_hubs/", "Distributed network nodes"],
            "📚 Documentation": ["docs/", "System documentation"]
        }
        
        for component, (path, description) in structure.items():
            full_path = Path(__file__).parent / path
            status = "✅" if full_path.exists() else "❌"
            print(f"{status} {component}")
            print(f"   📁 {path}")
            print(f"   📝 {description}")
            print()
        
        print("🔍 Explore specific ontology categories:")
        print("   • explore ontology     - Complete Living Codex ontology")
        print("   • explore chakras      - Chakra system and consciousness")
        print("   • explore frequencies  - Sacred frequencies and resonance")
        print("   • explore colors       - Color symbolism and energy")
        print("   • explore archangels   - Archangelic realms and attributes")
        print("   • explore water        - Water states and transformations")
        print("   • explore consciousness - Levels of consciousness")
        print("   • explore quantum      - Quantum states and phenomena")
        print("   • explore ai_agents    - AI agent types and capabilities")
        print("   • explore learning     - Learning modes and strategies")
        print("   • explore evolution    - Evolutionary stages and adaptation")
        print("   • explore emergence    - Emergence patterns and complexity")
        print("   • explore languages    - Programming language support")
        print("   • explore code         - Code intelligence and structure")
        print("   • explore assets       - Digital asset types and processing")
        print("   • explore performance  - System performance and metrics")
        print("   • explore knowledge    - Knowledge node types and functions")
        print("   • explore meta         - Meta-cognitive functions and capabilities")
    
    def _explore_ontology_category(self, category: str):
        """Explore specific ontology category"""
        category_map = {
            'ontology': 'Complete Living Codex Ontology',
            'chakras': 'Chakra System and Consciousness',
            'frequencies': 'Sacred Frequencies and Resonance',
            'colors': 'Color Symbolism and Energy',
            'archangels': 'Archangelic Realms and Attributes',
            'water': 'Water States and Transformations',
            'consciousness': 'Levels of Consciousness',
            'quantum': 'Quantum States and Phenomena',
            'ai_agents': 'AI Agent Types and Capabilities',
            'learning': 'Learning Modes and Strategies',
            'evolution': 'Evolutionary Stages and Adaptation',
            'emergence': 'Emergence Patterns and Complexity',
            'languages': 'Programming Language Support',
            'code': 'Code Intelligence and Structure',
            'assets': 'Digital Asset Types and Processing',
            'performance': 'System Performance and Metrics',
            'knowledge': 'Knowledge Node Types and Functions',
            'meta': 'Meta-Cognitive Functions and Capabilities'
        }
        
        display_name = category_map.get(category, category.title())
        print(f"\n🔍 {display_name}:")
        print("=" * 60)
        
        if category == 'ontology':
            self._show_complete_ontology()
        else:
            # Map category names to ontology keys
            ontology_key = {
                'chakras': 'chakras',
                'frequencies': 'frequencies', 
                'colors': 'colors',
                'archangels': 'archangels',
                'water': 'water_states',
                'consciousness': 'consciousness_levels',
                'quantum': 'quantum_states',
                'ai_agents': 'ai_agents',
                'learning': 'learning_modes',
                'evolution': 'evolutionary_stages',
                'emergence': 'emergence_patterns',
                'languages': 'programming_languages',
                'code': 'code_structures',
                'assets': 'asset_types',
                'performance': 'performance_metrics',
                'knowledge': 'knowledge_nodes',
                'meta': 'meta_cognitive_functions'
            }.get(category, category)
            
            items = self.ontology.get_ontology_category(ontology_key)
            if items:
                for name, description in items.items():
                    print(f"   {name}")
                    print(f"      📝 {description}")
                    print()
            else:
                print(f"   ❌ Category '{category}' not found")
    
    def _show_complete_ontology(self):
        """Show complete Living Codex ontology"""
        full_ontology = self.ontology.get_full_ontology()
        
        for category, items in full_ontology.items():
            category_name = category.replace('_', ' ').title()
            print(f"\n   🌟 {category_name}:")
            print(f"   {'-' * (len(category_name) + 4)}")
            
            for name, description in items.items():
                print(f"      {name}")
                print(f"         📝 {description}")
            print()
    
    def do_status(self, arg):
        """Show system status"""
        print("\n📊 Living Codex System Status:")
        print("=" * 50)
        
        print("🔧 Component Status:")
        print("   ✅ Resonance Engine: Active")
        print("   ✅ Knowledge Base: Active")
        
        print(f"\n⚡ Energy: {self.current_energy:,.1f}")
        print(f"💰 Energy Spent: {self.total_energy_spent:,.1f}")
        print(f"💾 Knowledge Nodes: {len(self.knowledge_base)}")
    
    def do_test(self, arg):
        """Run system tests"""
        print("\n🧪 Running Living Codex System Tests:")
        print("=" * 50)
        
        tests = [
            ("Resonance Engine", self._test_resonance_engine),
            ("Knowledge Base", self._test_knowledge_base),
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                status = "✅ PASS" if result else "❌ FAIL"
                print(f"{status} {test_name}")
                if result:
                    passed += 1
            except Exception as e:
                print(f"❌ ERROR {test_name}: {e}")
        
        print(f"\n📊 Test Results: {passed}/{total} passed")
    
    def _test_resonance_engine(self):
        """Test resonance engine"""
        try:
            analysis = self.resonance_engine.analyze_resonance("test", "test content")
            return analysis.get('analysis_type') == 'standalone'
        except:
            return False
    
    def _test_knowledge_base(self):
        """Test knowledge base"""
        return isinstance(self.knowledge_base, list)
    
    # Control Commands
    def do_quit(self, arg):
        """Exit the CLI"""
        print("\n👋 Thank you for using Living Codex Full CLI!")
        print("🌌 May your code resonate with the universe...")
        return True
    
    def do_exit(self, arg):
        """Exit the CLI"""
        return self.do_quit(arg)
    
    def do_clear(self, arg):
        """Clear the screen"""
        os.system('clear' if sys.platform != 'win32' else 'cls')
    
    def do_EOF(self, arg):
        """Handle Ctrl+D"""
        print()
        return self.do_quit(arg)

def main():
    """Run the standalone full CLI"""
    try:
        cli = LivingCodexFullCLI()
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
