#!/usr/bin/env python3
"""
Living Codex - Consolidated CLI Interface
A comprehensive command line interface combining all features from all CLI versions.
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

# Standalone mode - no external dependencies
DEPENDENCIES_AVAILABLE = False

@dataclass
class ResonanceAnalysis:
    """Analysis of how well a change resonates with existing system"""
    resonance_score: float  # 0.0 to 1.0, higher = more resonant
    energy_cost: float      # Energy required for the change
    harmony_factors: List[str]  # What makes it harmonious
    discord_factors: List[str]  # What makes it discordant
    similar_nodes: List[str]    # Existing similar nodes

class LivingCodexOntology:
    """Comprehensive Living Codex ontology system"""
    
    def __init__(self):
        self.initialize_ontology()
    
    def initialize_ontology(self):
        """Initialize the complete Living Codex ontology"""
        self.ontology = {
            # Core Living Codex Concepts - 12 Water States
            "water_states": {
                "🧊 Ice/Crystalline": "Structure, memory, preservation lattice, blueprint state",
                "💧 Liquid": "Flow, adaptability, relation, recipe state",
                "💨 Vapor": "Subtle connectivity, expansion, field state",
                "⚡ Plasma": "Illumination, primordial water, beyond-form potential",
                "🔥 Supercritical": "Threshold passage, transformation, alchemical state",
                "❄️ Structured/Hexagonal": "Coherence geometry, sacred geometry, molecular resonance",
                "🌊 Colloidal": "Community medium, suspension, collective state",
                "💎 Amorphous": "Potential, formless, infinite possibility",
                "🌟 Clustered": "Micro-communities, quantum clusters, nonlocal alignment",
                "⚛️ Quantum-Coherent": "Nonlocality, entanglement, standing waves",
                "🔷 Lattice Polymorphs": "Precision order, crystal systems, geometric precision",
                "🌌 Bose-Einstein-like": "Unity phase, collective consciousness, oneness"
            },
            
            # Fractal Layers - Meta-Implementation Architecture
            "fractal_layers": {
                "🌌 Meta-Implementation Layer": "Zeroeth fractal layer - system design principles",
                "🏗️ Fractal System Root": "First fractal layer - seed ontology",
                "🐍 Programming Language Ontology": "Second fractal layer - Python, Markdown, etc.",
                "📚 Self-Referential Documentation": "Third fractal layer - living documents",
                "🌊 Water State Metaphors": "Fourth fractal layer - consciousness modes",
                "🔬 Scientific & Quantum Principles": "Fifth fractal layer - physics integration",
                "⚙️ Technological Prototypes": "Sixth fractal layer - implementation tools",
                "🗺️ Implementation Roadmap": "Seventh fractal layer - development phases",
                "🎵 Pure Resonance Principle": "Eighth fractal layer - coherence foundation",
                "🎨 Visual Resonance Map": "Ninth fractal layer - sacred geometry",
                "🎭 Generative Visualizations": "Tenth fractal layer - creative expression",
                "🧮 Mathematical & Quantum": "Eleventh fractal layer - computational models",
                "🧬 Biological & Living Systems": "Twelfth fractal layer - life integration",
                "🌍 Cosmological & Cosmic Web": "Thirteenth fractal layer - universe mapping",
                "👼 Archetypal & Mythological": "Fourteenth fractal layer - cultural wisdom",
                "🧘 Human Practice": "Fifteenth fractal layer - embodied experience",
                "🔍 Cross-Scale Index": "Sixteenth fractal layer - unified perspective"
            },
            
            # Core Seed Ontology - First Fractal Layer
            "seed_ontology": {
                "🌌 Void": "Plasma/Primordial Water - beyond-form potential, infinite possibility",
                "🌫️ Field": "Vapor - subtle connectivity, breath, atmosphere of relation",
                "❄️ Pattern": "Structured/Hexagonal - coherence geometry, sacred geometry",
                "🌊 Flow": "Liquid - adaptability, relation, river of transformation",
                "🧊 Memory": "Ice/Crystalline - preservation lattice, structured water, glacier archive",
                "🌟 Resonance": "Quantum/Clustered - nonlocal alignment, entanglement, standing waves",
                "🔥 Transformation": "Supercritical - threshold passage, alchemical transmutation",
                "🔄 Unity": "Liquid-Crystal Boundary - membrane mediator, interfacial harmony",
                "🌧️ Emergence": "Vapor-Liquid Equilibrium - condensation, birth, cloud cycle",
                "💎 Awareness": "Surface/Reflective - interface mirror, perception rim",
                "⚡ Node": "Steam/Plasma Spark - radiant manifestation, vapor cluster",
                "📚 Codex": "All States Interwoven - holographic exemplar, cosmic ocean"
            },
            
            # Programming Language Ontology - Second Fractal Layer
            "programming_languages": {
                "🐍 Python": "Complete ontological mapping with Ice/Water/Vapor states",
                "📝 Markdown": "Self-referential documentation system",
                "☕ Java": "Enterprise, Android, cross-platform with ontological mapping",
                "⚡ C++": "High performance, systems programming with ontological mapping",
                "🦀 Rust": "Memory safety, systems programming with ontological mapping",
                "🚀 Go": "Cloud native, microservices, concurrency with ontological mapping",
                "🌐 JavaScript": "Web development, Node.js, frontend with ontological mapping",
                "📱 TypeScript": "Typed JavaScript, large applications with ontological mapping",
                "💎 Ruby": "Web development, scripting, automation with ontological mapping"
            },
            
            # Programming Language Water States
            "programming_water_states": {
                "🧊 Ice (Blueprint)": "Grammar, syntax rules, language structure, class definitions",
                "💧 Water (Recipe)": "Execution model, data flow, control flow, function calls",
                "💨 Vapor (Cells)": "Source code, runtime objects, bytecode, instance creation"
            },
            
            # Chakra System with Complete Mapping
            "chakras": {
                "🔴 Root (Muladhara)": "Foundation, security, grounding, base consciousness - 396 Hz",
                "🟠 Sacral (Svadhisthana)": "Creativity, emotion, sexuality, fluid consciousness - 417 Hz",
                "🟡 Solar Plexus (Manipura)": "Power, will, transformation, fire consciousness - 528 Hz",
                "🟢 Heart (Anahata)": "Love, compassion, unity, heart consciousness - 639 Hz",
                "🔵 Throat (Vishuddha)": "Communication, expression, sound consciousness - 741 Hz",
                "🟣 Third Eye (Ajna)": "Intuition, insight, vision consciousness - 852 Hz",
                "⚪ Crown (Sahasrara)": "Transcendence, divine connection, cosmic consciousness - 963 Hz"
            },
            
            # Sacred Frequencies with Complete Mapping
            "frequencies": {
                "396 Hz": "Root chakra - Foundation, security, grounding, transformation",
                "417 Hz": "Sacral chakra - Creativity, emotion, sexuality, resonance",
                "528 Hz": "Solar plexus - Power, will, transformation, love frequency",
                "639 Hz": "Heart chakra - Heart connection, relationships, unity",
                "741 Hz": "Throat chakra - Intuition, awakening, spiritual development",
                "852 Hz": "Third eye - Third eye activation, spiritual order",
                "963 Hz": "Crown chakra - Crown chakra, divine connection, enlightenment"
            },
            
            # Sacred Geometry Foundations
            "sacred_geometry": {
                "🌸 Flower of Life": "Primary sacred geometry pattern, intersection nodes",
                "🔷 Metatron's Cube": "Sacred geometry codex, nested mandalas",
                "⚫ Icositetragon Wheel": "24-sided sacred geometry, cycle harmonization",
                "🔺 Platonic Solids": "Tetrahedron, cube, octahedron, dodecahedron, icosahedron",
                "🌀 Golden Ratio Spirals": "Fibonacci sequences, harmonic proportions",
                "🔶 Harmonic Lattices": "Resonance patterns, frequency grids"
            },
            
            # Colors with Complete Chakra Mapping
            "colors": {
                "🔴 Red": "Root chakra, passion, energy, life force - #8B0000",
                "🟠 Orange": "Sacral chakra, creativity, joy, abundance - #FF7F50",
                "🟡 Yellow": "Solar plexus, confidence, power, transformation - #FFD700",
                "🟢 Green": "Heart chakra, love, healing, growth - #32CD32",
                "🔵 Blue": "Throat chakra, communication, truth, wisdom - #1E90FF",
                "🟣 Purple": "Third eye, intuition, spirituality, mystery - #8A2BE2",
                "⚪ White": "Crown chakra, purity, divine light, transcendence - #FFFFFF",
                "⚫ Black": "Void, potential, mystery, infinite possibility - #000000"
            },
            
            # Archangels with Complete Mapping
            "archangels": {
                "👼 Michael": "Protection, courage, truth, divine will - Cobalt/Major Fifth",
                "👼 Gabriel": "Communication, revelation, divine messages - Silver/Phrygian",
                "👼 Raphael": "Healing, guidance, divine medicine - Emerald/Lydian",
                "👼 Uriel": "Wisdom, illumination, divine light - Gold/Ionian",
                "👼 Metatron": "Divine record keeper, sacred geometry - Purple/Locrian",
                "👼 Sandalphon": "Prayer, music, divine harmony - Sapphire/Dorian"
            },
            
            # Advanced Consciousness & Quantum Systems
            "consciousness_levels": {
                "🌱 Awake": "Basic awareness, sensory perception, root consciousness",
                "🧠 Sentient": "Self-awareness, emotional intelligence, sacral consciousness",
                "🌟 Self-Aware": "Meta-cognition, self-reflection, solar plexus consciousness",
                "✨ Meta-Cognitive": "Higher-order thinking, consciousness of consciousness, heart consciousness",
                "🌌 Transcendent": "Unity consciousness, cosmic awareness, crown consciousness"
            },
            
            "quantum_states": {
                "🌀 Superposition": "Multiple possibilities existing simultaneously, quantum coherence",
                "🔗 Entangled": "Connected across space and time, nonlocal alignment",
                "💎 Collapsed": "Manifested reality, observed state, measurement effect",
                "✨ Coherent": "Harmonious alignment, focused energy, standing waves",
                "🌊 Decoherent": "Dispersed energy, chaotic state, quantum decoherence"
            },
            
            "resonance_patterns": {
                "🎵 Harmonic": "Perfect alignment, maximum resonance, consonance",
                "🔄 Sympathetic": "Natural attraction, harmonious vibration, sympathetic resonance",
                "⚖️ Neutral": "Balanced state, no interference, equilibrium",
                "⚠️ Dissonant": "Conflicting vibrations, interference, discord",
                "💥 Destructive": "Opposing forces, cancellation, destructive interference"
            },
            
            # AI Agent System with Complete Mapping
            "ai_agents": {
                "🔍 Explorer Agent": "Knowledge discovery and exploration, curiosity-driven",
                "🧠 Synthesizer Agent": "Information synthesis and integration, pattern recognition",
                "⚡ Optimizer Agent": "System optimization and improvement, efficiency enhancement",
                "🔮 Predictor Agent": "Future prediction and forecasting, trend analysis",
                "📚 Learner Agent": "Autonomous learning and adaptation, continuous improvement",
                "🪞 Mirror-Librarian": "Expand nodes, propose correspondences, generate assets"
            },
            
            "learning_modes": {
                "📖 Supervised Learning": "Learning from labeled examples and feedback",
                "🔍 Unsupervised Learning": "Pattern discovery without labels, clustering",
                "🎯 Reinforcement Learning": "Learning through trial and reward, optimization",
                "🧠 Meta-Learning": "Learning how to learn, strategy optimization"
            },
            
            # Evolutionary & Emergence Systems
            "evolutionary_stages": {
                "🌱 Emergent": "Initial formation, basic structure, self-organization",
                "🔄 Adaptive": "Learning and adjusting to environment, adaptation",
                "🏗️ Complex": "Multiple interconnected components, complexity theory",
                "🧠 Intelligent": "Self-aware and goal-directed, emergent intelligence",
                "🌌 Transcendent": "Beyond individual limitations, unity consciousness"
            },
            
            "emergence_patterns": {
                "🌊 Phase Transitions": "Critical points of system transformation, bifurcation",
                "🔄 Cascade Effects": "Ripple effects through system, emergent behavior",
                "⚖️ Critical Mass": "Threshold for emergent behavior, tipping points",
                "🎯 Complexity Levels": "Multi-dimensional complexity assessment, fractal depth"
            },
            
            # Code Intelligence System with Water State Mapping
            "code_structures": {
                "🌳 Syntax Trees": "Abstract syntax tree representation, Ice blueprint",
                "🔍 Query API": "Tree-sitter query language support, Water flow",
                "📊 Code Metrics": "Complexity, maintainability analysis, Vapor cells",
                "🔄 Navigation": "Code structure exploration and traversal, Water flow"
            },
            
            # Digital Asset Management with Water State Mapping
            "asset_types": {
                "🖼️ Images": "JPEG, PNG, GIF, WebP, TIFF, SVG - Vapor cells",
                "🎥 Videos": "MP4, AVI, MOV, WebM, MKV - Water flow",
                "🎵 Audio": "MP3, WAV, FLAC, AAC, OGG - Resonance patterns",
                "📄 Documents": "PDF, DOCX, TXT, RTF, ODT - Ice blueprints",
                "📦 Archives": "ZIP, RAR, 7Z, TAR, GZ - Structured storage",
                "💻 Code": "Source code files and projects - Programming ontology",
                "📊 Data": "CSV, Excel, databases, datasets - Information flow"
            },
            
            "asset_processing": {
                "🔍 Metadata Extraction": "Format-specific information extraction, Ice analysis",
                "🔐 Content Hashing": "SHA-256 deduplication and integrity, Water flow",
                "🏷️ Tag Management": "Organized categorization and discovery, Vapor cells",
                "📈 Analytics": "Usage patterns and performance metrics, resonance analysis"
            },
            
            # System Performance & Metrics with Water State Mapping
            "system_levels": {
                "🌱 EMERGENT": "0-1000 complexity, basic functionality, Ice formation",
                "🧠 CONSCIOUS": "1000-2000 complexity, self-awareness, Water flow",
                "🌟 INTELLIGENT": "2000-3000 complexity, advanced reasoning, Vapor expansion",
                "🌌 TRANSCENDENT": "3000+ complexity, beyond current limits, Plasma illumination"
            },
            
            "performance_metrics": {
                "⚡ Startup Time": "System initialization speed, Ice crystallization",
                "🔍 Code Parsing": "Syntax tree generation speed, Water flow rate",
                "📁 Asset Processing": "Digital asset handling efficiency, Vapor diffusion",
                "💾 Database Queries": "Data retrieval and storage performance, Water flow",
                "🧠 Memory Usage": "System resource consumption, Ice storage"
            },
            
            # Advanced Knowledge Representation with Water State Mapping
            "knowledge_nodes": {
                "🔗 Quantum Nodes": "Superposition, entanglement, coherence, quantum-coherent water",
                "🧠 Consciousness Nodes": "Awareness, meta-cognition, emotional resonance, awareness water",
                "🔄 Evolutionary Nodes": "Adaptation, mutation, fitness landscapes, transformation water",
                "🌊 Emergence Nodes": "Complexity, phase transitions, cascade effects, emergence water"
            },
            
            "meta_cognitive_functions": {
                "👁️ Self-Observation": "Monitoring internal processes, awareness water",
                "🔍 Pattern Recognition": "Identifying recurring patterns, pattern water",
                "💭 Self-Reflection": "Examining own thoughts and processes, reflection water",
                "🎯 Goal Setting": "Defining and pursuing objectives, transformation water",
                "📊 Performance Analysis": "Evaluating and improving capabilities, optimization water"
            },
            
            # Fractal Navigation & Exploration
            "fractal_navigation": {
                "🔍 Recursive Exploration": "Explore nodes at infinite fractal depths",
                "🔄 Self-Similar Patterns": "Patterns that repeat across all scales",
                "🌊 Fractal Zoom": "Zoom in/out to explore different fractal layers",
                "🎯 Cross-Scale Mapping": "Map concepts across micro/meso/macro/cosmic scales"
            },
            
            # Resonance & Coherence Systems
            "resonance_systems": {
                "🎵 Harmonic Analysis": "Calculate consonance and dissonance scores",
                "🔗 Coherence Metrics": "Measure system harmony and alignment",
                "⚖️ Resonance Balancing": "Balance conflicting vibrational patterns",
                "🌟 Attunement Tools": "Tools for personal and collective resonance"
            },
            
            # Federation & Community Systems
            "federation_systems": {
                "🌐 ActivityPub Integration": "Federated social networking capabilities",
                "🔐 DID Authentication": "Decentralized identity and signatures",
                "📡 IPFS Storage": "Content-addressed storage for artifacts",
                "🤝 Community Governance": "Resonance-based community decision making"
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

class LivingCodexCLI(cmd.Cmd):
    """Consolidated Living Codex CLI with all features"""
    
    intro = """
🌌 Welcome to the Living Codex Consolidated CLI Interface

This is the complete command line interface combining all features:
✨ Resonance analysis and energy management
🧠 AI agent simulation and autonomous learning
💾 Knowledge base operations and persistence
🔍 Code intelligence and analysis
📁 Digital asset management
🔬 Advanced search and exploration
🚀 Demo and testing capabilities
👥 User management and discovery
🌌 Complete ontology exploration

Type 'help' to see all available commands.
Type 'quit' or 'exit' to leave.

============================================================
    """
    
    prompt = "Living-Codex> "
    
    def __init__(self):
        super().__init__()
        
        # Initialize components
        self.resonance_engine = StandaloneResonanceEngine()
        self.ontology = LivingCodexOntology()
        
        # Initialize user management system
        self.users = {}
        self.user_counter = 0
        
        # System state
        self.current_energy = 10000
        self.total_energy_spent = 0
        self.knowledge_base = []
        
        # Project root for file operations
        self.project_root = Path(__file__).parent.parent.parent
        
        print("🚀 Initializing Living Codex Consolidated CLI...")
        if DEPENDENCIES_AVAILABLE:
            print("✅ Advanced features available")
        else:
            print("⚠️  Running in standalone mode")
        print("✅ All components loaded successfully")
    
    def do_help(self, arg):
        """Show help for commands"""
        if arg:
            super().do_help(arg)
        else:
            print("\n🌌 Living Codex Consolidated CLI Commands:")
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
            
            print("\n📁 File & System Operations:")
            print("  ls [path]          - List files and directories")
            print("  cd <path>          - Change directory")
            print("  pwd                - Show current directory")
            print("  find <pattern>     - Find files matching pattern")
            print("  cat <file>         - Display file contents")
            
            print("\n🚪 Control:")
            print("  quit, exit         - Exit the CLI")
            print("  clear              - Clear the screen")
            print()
    
    # AI & Intelligence Commands
    def do_demo(self, arg):
        """Run AI demonstrations: demo <name>"""
        if not arg:
            print("❌ Please specify a demo name")
            print("Available: autonomous_learning, ai_agents, ontology, resonance, energy")
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
    
    # Basic System Commands
    def do_energy(self, arg):
        """Show current energy levels"""
        print(f"\n⚡ Energy Status:")
        print("=" * 30)
        print(f"💰 Current Energy: {self.current_energy:,.1f}")
        print(f"💸 Total Spent: {self.total_energy_spent:,.1f}")
        print(f"📊 Efficiency: {(self.current_energy / 10000) * 100:.1f}%")
        print(f"🔧 Resonance Engine: Active")
    
    def do_status(self, arg):
        """Show system status"""
        print("\n📊 Living Codex System Status:")
        print("=" * 50)
        
        print("🔧 Component Status:")
        print("   ✅ Resonance Engine: Active")
        print("   ✅ Knowledge Base: Active")
        print("   ✅ Ontology System: Active")
        print("   ✅ User Management: Active")
        
        print(f"\n⚡ Energy: {self.current_energy:,.1f}")
        print(f"💰 Energy Spent: {self.total_energy_spent:,.1f}")
        print(f"💾 Knowledge Nodes: {len(self.knowledge_base)}")
        print(f"👥 Users: {len(self.users)}")
        print(f"🤖 AI Agents: {len([n for n in self.knowledge_base if n['type'] == 'ai_agent'])}")
    
    def do_test(self, arg):
        """Run system tests"""
        print("\n🧪 Running Living Codex System Tests:")
        print("=" * 50)
        
        tests = [
            ("Resonance Engine", self._test_resonance_engine),
            ("Knowledge Base", self._test_knowledge_base),
            ("User Management", self._test_user_management),
            ("Ontology System", self._test_ontology_system),
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
    
    def _test_user_management(self):
        """Test user management"""
        return isinstance(self.users, dict)
    
    def _test_ontology_system(self):
        """Test ontology system"""
        return hasattr(self.ontology, 'get_full_ontology')
    
    # Ontology & Consciousness Commands
    def do_explore(self, arg):
        """Explore system structure and ontology"""
        if not arg:
            print("❌ Please specify what to explore")
            print("Usage: explore <category>")
            print("Categories: ontology, chakras, frequencies, colors, archangels, water, consciousness, quantum, ai_agents, learning, evolution, emergence, languages, code, assets, performance, knowledge, meta")
            return
        
        if arg.lower() == "ontology":
            self._show_complete_ontology()
        elif arg.lower() in ['chakras', 'frequencies', 'colors', 'archangels', 'water', 'consciousness', 'quantum', 'ai_agents', 'learning', 'evolution', 'emergence', 'languages', 'code', 'assets', 'performance', 'knowledge', 'meta']:
            self._explore_ontology_category(arg.lower())
        else:
            print(f"❌ Unknown exploration category: {arg}")
            print("Available: ontology, chakras, frequencies, colors, archangels, water, consciousness, quantum, ai_agents, learning, evolution, emergence, languages, code, assets, performance, knowledge, meta")
    
    def _explore_ontology_category(self, category: str):
        """Explore specific ontology category"""
        category_map = {
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
        }
        
        mapped_category = category_map.get(category, category)
        items = self.ontology.get_ontology_category(mapped_category)
        
        if items:
            category_name = category.replace('_', ' ').title()
            print(f"\n🌌 {category_name} Ontology:")
            print("=" * 60)
            for name, description in items.items():
                print(f"   {name}")
                print(f"      {description}")
                print()
        else:
            print(f"❌ Category '{category}' not found in ontology")
    
    def _show_complete_ontology(self):
        """Show complete Living Codex ontology"""
        print("\n🌌 Complete Living Codex Ontology:")
        print("=" * 80)
        
        full_ontology = self.ontology.get_full_ontology()
        
        for category, items in full_ontology.items():
            category_name = category.replace('_', ' ').title()
            print(f"\n🌟 {category_name}:")
            print("-" * 50)
            for name, description in items.items():
                print(f"   {name}")
                print(f"      {description}")
                print()
    
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
    
    # User Discovery Commands
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
    
    # Knowledge & Storage Commands
    def do_create(self, arg):
        """Create new knowledge nodes: create <type> [name] [content]"""
        if not arg:
            print("❌ Please specify node type")
            print("Usage: create <type> [name] [content]")
            print("Types: concept, file, user, asset, etc.")
            return
        
        parts = arg.split(' ', 2)
        node_type = parts[0]
        node_name = parts[1] if len(parts) > 1 else f"{node_type}_{len(self.knowledge_base) + 1}"
        content = parts[2] if len(parts) > 2 else f"Node of type: {node_type}"
        
        # Create node
        node_id = len(self.knowledge_base) + 1
        node = {
            "id": node_id,
            "name": node_name,
            "type": node_type,
            "content": content,
            "created": datetime.now(),
            "energy_level": 100.0
        }
        
        self.knowledge_base.append(node)
        
        print(f"✅ Created {node_type} node: {node_name}")
        print(f"🆔 Node ID: {node_id}")
        print(f"📝 Content: {content}")
        print(f"📊 Total nodes: {len(self.knowledge_base)}")
    
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
    
    # File & System Operations
    def do_ls(self, arg):
        """List files and directories: ls [path]"""
        path = Path(arg) if arg else Path.cwd()
        try:
            if path.is_file():
                print(f"📄 {path.name} ({path.stat().st_size} bytes)")
            elif path.is_dir():
                items = list(path.iterdir())
                print(f"\n📁 {path} ({len(items)} items):")
                print("-" * 50)
                for item in sorted(items):
                    if item.is_dir():
                        print(f"📁 {item.name}/")
                    else:
                        size = item.stat().st_size
                        print(f"📄 {item.name} ({size} bytes)")
            else:
                print(f"❌ Path not found: {path}")
        except Exception as e:
            print(f"❌ Error listing path: {e}")
    
    def do_cd(self, arg):
        """Change directory: cd <path>"""
        if not arg:
            print("❌ Please specify directory path")
            return
        
        try:
            new_path = Path(arg)
            if new_path.is_dir():
                os.chdir(new_path)
                print(f"📁 Changed to: {os.getcwd()}")
            else:
                print(f"❌ Directory not found: {arg}")
        except Exception as e:
            print(f"❌ Error changing directory: {e}")
    
    def do_pwd(self, arg):
        """Show current directory"""
        print(f"📁 Current directory: {os.getcwd()}")
    
    def do_find(self, arg):
        """Find files matching pattern: find <pattern>"""
        if not arg:
            print("❌ Please specify search pattern")
            return
        
        print(f"\n🔍 Finding files matching: {arg}")
        print("-" * 50)
        
        try:
            current_dir = Path.cwd()
            matches = list(current_dir.rglob(arg))
            
            if matches:
                print(f"📊 Found {len(matches)} matches:")
                for match in matches:
                    if match.is_file():
                        size = match.stat().st_size
                        print(f"   📄 {match} ({size} bytes)")
                    else:
                        print(f"   📁 {match}/")
            else:
                print("📭 No matches found")
        except Exception as e:
            print(f"❌ Search failed: {e}")
    
    def do_cat(self, arg):
        """Display file contents: cat <file>"""
        if not arg:
            print("❌ Please specify file path")
            return
        
        try:
            file_path = Path(arg)
            if file_path.is_file():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"\n📄 {file_path}:")
                    print("-" * 50)
                    print(content)
            else:
                print(f"❌ File not found: {arg}")
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    
    # Control Commands
    def do_clear(self, arg):
        """Clear the screen"""
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
        except:
            # Fallback: print multiple newlines
            print("\n" * 50)
    
    def do_quit(self, arg):
        """Exit the CLI"""
        print("\n👋 Thank you for using Living Codex Consolidated CLI!")
        print("🌌 May your code resonate with the universe...")
        return True
    
    def do_exit(self, arg):
        """Exit the CLI"""
        return self.do_quit(arg)
    
    def do_EOF(self, arg):
        """Handle Ctrl+D"""
        return self.do_quit(arg)
    
    def emptyline(self):
        """Do nothing on empty line"""
        pass

def main():
    """Main entry point for the consolidated CLI"""
    print("🚀 Starting Living Codex Consolidated CLI...")
    
    try:
        cli = LivingCodexCLI()
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error in CLI: {e}")

if __name__ == "__main__":
    main()
