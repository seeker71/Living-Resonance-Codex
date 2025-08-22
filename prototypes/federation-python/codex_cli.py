#!/usr/bin/env python3
"""
Living Codex - Interactive CLI Interface
A resonance-aware command line interface for exploring and modifying the Living Codex system.
Changes cost energy based on how well they resonate with existing knowledge.
"""

import sys
import json
import asyncio
import cmd
import shlex
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import math
import re
from dataclasses import dataclass

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.core.database_persistence_system import DatabasePersistenceSystem, DatabaseNode, QueryFilter, QueryOptions
from src.ontology.enhanced_ontology_system import EnhancedOntologySystem
from src.ai_agents.ai_agent_system import AIAgentSystem

@dataclass
class ResonanceAnalysis:
    """Analysis of how well a change resonates with existing system"""
    resonance_score: float  # 0.0 to 1.0, higher = more resonant
    energy_cost: float      # Energy required for the change
    harmony_factors: List[str]  # What makes it harmonious
    discord_factors: List[str]  # What makes it discordant
    similar_nodes: List[str]    # Existing similar nodes
    
class ResonanceEngine:
    """Calculates energy costs based on resonance with existing knowledge"""
    
    def __init__(self, database: DatabasePersistenceSystem, ontology: EnhancedOntologySystem):
        self.database = database
        self.ontology = ontology
        self.base_energy_cost = 100
        self.max_energy_multiplier = 10.0
        
    def analyze_resonance(self, action: str, content: str, node_type: str = "concept", 
                         existing_node: Optional[DatabaseNode] = None) -> ResonanceAnalysis:
        """Analyze how well a change resonates with the existing system"""
        
        # Get all existing nodes for context
        result = self.database.operations.query_nodes([], QueryOptions())
        existing_nodes = result.data if result.success else []
        
        # Calculate various resonance factors
        semantic_resonance = self._calculate_semantic_resonance(content, existing_nodes)
        structural_resonance = self._calculate_structural_resonance(node_type, existing_nodes)
        energy_resonance = self._calculate_energy_resonance(content, existing_nodes)
        temporal_resonance = self._calculate_temporal_resonance(action, existing_node)
        
        # Combine resonance factors
        overall_resonance = (
            semantic_resonance * 0.4 +
            structural_resonance * 0.2 +
            energy_resonance * 0.3 +
            temporal_resonance * 0.1
        )
        
        # Calculate energy cost (inverse relationship with resonance)
        energy_multiplier = self.max_energy_multiplier * (1.0 - overall_resonance)
        energy_cost = self.base_energy_cost * (1.0 + energy_multiplier)
        
        # Find harmony and discord factors
        harmony_factors = self._find_harmony_factors(content, existing_nodes)
        discord_factors = self._find_discord_factors(content, existing_nodes)
        similar_nodes = self._find_similar_nodes(content, existing_nodes)
        
        return ResonanceAnalysis(
            resonance_score=overall_resonance,
            energy_cost=energy_cost,
            harmony_factors=harmony_factors,
            discord_factors=discord_factors,
            similar_nodes=similar_nodes
        )
    
    def _calculate_semantic_resonance(self, content: str, existing_nodes: List[DatabaseNode]) -> float:
        """Calculate semantic similarity with existing content"""
        if not existing_nodes:
            return 0.5  # Neutral for empty system
            
        content_words = set(re.findall(r'\w+', content.lower()))
        if not content_words:
            return 0.1
            
        max_similarity = 0.0
        for node in existing_nodes:
            if node.content:
                node_words = set(re.findall(r'\w+', node.content.lower()))
                if node_words:
                    intersection = len(content_words & node_words)
                    union = len(content_words | node_words)
                    similarity = intersection / union if union > 0 else 0
                    max_similarity = max(max_similarity, similarity)
        
        return min(1.0, max_similarity * 2.0)  # Scale up to make resonance more sensitive
    
    def _calculate_structural_resonance(self, node_type: str, existing_nodes: List[DatabaseNode]) -> float:
        """Calculate structural harmony with existing node types"""
        if not existing_nodes:
            return 0.5
            
        # Count existing node types
        type_counts = {}
        for node in existing_nodes:
            type_counts[node.node_type] = type_counts.get(node.node_type, 0) + 1
        
        total_nodes = len(existing_nodes)
        if node_type in type_counts:
            # More resonant if this type already exists
            type_frequency = type_counts[node_type] / total_nodes
            return min(1.0, type_frequency * 3.0)  # Scale to reward existing types
        else:
            # Less resonant if introducing new type
            return 0.3
    
    def _calculate_energy_resonance(self, content: str, existing_nodes: List[DatabaseNode]) -> float:
        """Calculate energy harmony based on complexity and depth"""
        content_complexity = len(content) + len(re.findall(r'[A-Z]', content)) * 2
        
        if not existing_nodes:
            return 0.5
            
        # Find average system complexity
        total_complexity = sum(len(node.content or "") for node in existing_nodes)
        avg_complexity = total_complexity / len(existing_nodes) if existing_nodes else 100
        
        # More resonant if complexity is similar to system average
        complexity_ratio = min(content_complexity, avg_complexity) / max(content_complexity, avg_complexity, 1)
        return complexity_ratio
    
    def _calculate_temporal_resonance(self, action: str, existing_node: Optional[DatabaseNode]) -> float:
        """Calculate temporal harmony based on action type and recency"""
        if action == "create":
            return 0.8  # Creating is generally harmonious
        elif action == "modify" and existing_node:
            # More resonant if node was recently active
            if existing_node.updated_at:
                time_diff = (datetime.now() - existing_node.updated_at).total_seconds()
                # More resonant for recently updated nodes
                recency_factor = max(0.1, 1.0 - (time_diff / 86400))  # Decay over 24 hours
                return recency_factor
            return 0.6
        elif action == "delete":
            return 0.2  # Deletion is generally less harmonious
        else:
            return 0.5
    
    def _find_harmony_factors(self, content: str, existing_nodes: List[DatabaseNode]) -> List[str]:
        """Identify what makes this change harmonious"""
        factors = []
        content_lower = content.lower()
        
        # Check for common concepts
        common_concepts = ["knowledge", "learning", "consciousness", "quantum", "evolution", "emergence"]
        for concept in common_concepts:
            if concept in content_lower:
                # Check if concept exists in system
                for node in existing_nodes:
                    if node.content and concept in node.content.lower():
                        factors.append(f"Resonates with existing {concept} concepts")
                        break
        
        # Check for structural patterns
        if any(char.isupper() for char in content):
            factors.append("Uses established naming conventions")
        
        if len(content) > 20 and len(content) < 200:
            factors.append("Appropriate content length for system")
            
        return factors
    
    def _find_discord_factors(self, content: str, existing_nodes: List[DatabaseNode]) -> List[str]:
        """Identify what makes this change discordant"""
        factors = []
        content_lower = content.lower()
        
        # Check for disruptive patterns
        disruptive_words = ["destroy", "delete", "remove", "chaos", "random", "break"]
        for word in disruptive_words:
            if word in content_lower:
                factors.append(f"Contains disruptive concept: {word}")
        
        # Check for extreme complexity
        if len(content) > 500:
            factors.append("Unusually complex for system")
        elif len(content) < 5:
            factors.append("Unusually simple for system")
        
        # Check for completely novel concepts
        content_words = set(re.findall(r'\w+', content_lower))
        system_words = set()
        for node in existing_nodes:
            if node.content:
                system_words.update(re.findall(r'\w+', node.content.lower()))
        
        if content_words and system_words:
            novelty_ratio = len(content_words - system_words) / len(content_words)
            if novelty_ratio > 0.8:
                factors.append("Introduces many novel concepts")
        
        return factors
    
    def _find_similar_nodes(self, content: str, existing_nodes: List[DatabaseNode]) -> List[str]:
        """Find nodes with similar content"""
        similar = []
        content_words = set(re.findall(r'\w+', content.lower()))
        
        for node in existing_nodes:
            if node.content:
                node_words = set(re.findall(r'\w+', node.content.lower()))
                if content_words and node_words:
                    intersection = len(content_words & node_words)
                    union = len(content_words | node_words)
                    similarity = intersection / union if union > 0 else 0
                    if similarity > 0.3:  # Threshold for similarity
                        similar.append(f"{node.name} (similarity: {similarity:.2f})")
        
        return similar[:5]  # Return top 5 similar nodes

class LivingCodexCLI(cmd.Cmd):
    """Interactive CLI for the Living Codex system"""
    
    intro = """
🌟 Living Codex - Interactive CLI Interface
============================================================
Welcome to the resonance-aware Living Codex CLI!

Commands:
  explore <node_id>     - Explore a specific node
  list [type]          - List all nodes or nodes of specific type
  search <term>        - Search for nodes containing term
  create <name>        - Create a new node
  modify <node_id>     - Modify an existing node
  delete <node_id>     - Delete a node
  analyze <content>    - Analyze resonance of potential content
  energy               - Show current energy status
  resonate <node_id>   - Show resonance analysis for a node
  help                 - Show this help message
  demo                 - Run system exploration demo to populate database
  quit                 - Exit the CLI

Energy costs are based on resonance:
  🟢 High resonance = Low energy cost
  🟡 Medium resonance = Medium energy cost  
  🔴 Low resonance = High energy cost

Type 'help <command>' for detailed help on specific commands.
============================================================
    """
    
    prompt = "Living-Codex> "
    
    def __init__(self):
        super().__init__()
        # Initialize database with proper path
        db_path = str(Path(__file__).parent / "comprehensive_bootstrap.db")
        self.database = DatabasePersistenceSystem(db_type="sqlite", db_path=db_path)
        
        # Pass the existing database instance to avoid duplication
        self.ontology = EnhancedOntologySystem(database=self.database)
        self.ai_system = AIAgentSystem(self.ontology)
        self.resonance_engine = ResonanceEngine(self.database, self.ontology)
        self.current_energy = 10000  # Starting energy
        self.total_energy_spent = 0
        
    def preloop(self):
        """Initialize the CLI"""
        print("🚀 Initializing Living Codex CLI...")
        
        # Test database connection
        try:
            test_result = self.database.operations.query_nodes([], QueryOptions(limit=1))
            if test_result.success:
                print("✅ Database system ready")
            else:
                print("⚠️  Database system initialized (some operations may be limited)")
        except Exception as e:
            print(f"⚠️  Database system initialized with warnings: {e}")
        
        print("✅ Ontology system ready")
        print("✅ AI agent system ready")
        print("✅ Resonance engine ready")
        print(f"💫 Starting energy: {self.current_energy}")
        print()
    
    def do_explore(self, arg):
        """Explore a specific node by ID or name
        Usage: explore <node_id>
        """
        if not arg:
            print("❌ Please specify a node ID or name to explore")
            return
            
        # Try to find the node
        node = self._find_node(arg)
        if not node:
            print(f"❌ Node '{arg}' not found")
            return
        
        print(f"\n🔍 Exploring Node: {node.name}")
        print("=" * 50)
        print(f"ID: {node.node_id}")
        print(f"Type: {node.node_type}")
        print(f"Content: {node.content}")
        print(f"Realm: {node.realm}")
        print(f"Water State: {node.water_state}")
        print(f"Energy Level: {node.energy_level}")
        print(f"Created: {node.created_at}")
        print(f"Updated: {node.updated_at}")
        
        if node.metadata:
            print(f"Metadata: {json.dumps(node.metadata, indent=2)}")
        
        # Show resonance with system
        if node.content:
            resonance = self.resonance_engine.analyze_resonance("view", node.content, node.node_type, node)
            print(f"\n🎵 Resonance Analysis:")
            print(f"   Score: {resonance.resonance_score:.2f} {'🟢' if resonance.resonance_score > 0.7 else '🟡' if resonance.resonance_score > 0.4 else '🔴'}")
            if resonance.harmony_factors:
                print(f"   Harmony: {', '.join(resonance.harmony_factors[:2])}")
            if resonance.similar_nodes:
                print(f"   Similar: {', '.join(resonance.similar_nodes[:2])}")
    
    def do_list(self, arg):
        """List all nodes or nodes of a specific type
        Usage: list [type]
        """
        try:
            filters = []
            if arg:
                filters = [QueryFilter("node_type", "=", arg)]
            
            result = self.database.operations.query_nodes(filters, QueryOptions(limit=50))
            if not result.success:
                print(f"❌ Error listing nodes: {getattr(result, 'error_message', 'Unknown error')}")
                print("💡 Try running the system exploration demo first to populate the database")
                return
            
            nodes = result.data or []
            if not nodes:
                print("📭 No nodes found")
                print("💡 Try running the system exploration demo first to populate the database")
                return
            
            print(f"\n📋 Found {len(nodes)} nodes:")
            print("-" * 80)
            for node in nodes:
                energy_indicator = "🟢" if node.energy_level > 800 else "🟡" if node.energy_level > 400 else "🔴"
                content_preview = (node.content[:50] + "...") if node.content and len(node.content) > 50 else (node.content or "")
                print(f"{energy_indicator} {node.name:<20} {node.node_type:<15} {content_preview}")
        except Exception as e:
            print(f"❌ Database error: {e}")
            print("💡 Try running the system exploration demo first to populate the database")
    
    def do_search(self, arg):
        """Search for nodes containing specific terms
        Usage: search <term>
        """
        if not arg:
            print("❌ Please specify a search term")
            return
        
        # Get all nodes and search through them
        result = self.database.operations.query_nodes([], QueryOptions())
        if not result.success:
            print(f"❌ Error searching: {getattr(result, 'error_message', 'Unknown error')}")
            return
        
        nodes = result.data or []
        matching_nodes = []
        
        search_term = arg.lower()
        for node in nodes:
            if (search_term in node.name.lower() or 
                (node.content and search_term in node.content.lower()) or
                search_term in node.node_type.lower()):
                matching_nodes.append(node)
        
        if not matching_nodes:
            print(f"🔍 No nodes found containing '{arg}'")
            return
        
        print(f"\n🔍 Found {len(matching_nodes)} nodes containing '{arg}':")
        print("-" * 80)
        for node in matching_nodes:
            energy_indicator = "🟢" if node.energy_level > 800 else "🟡" if node.energy_level > 400 else "🔴"
            print(f"{energy_indicator} {node.name:<20} {node.node_type:<15}")
    
    def do_create(self, arg):
        """Create a new node
        Usage: create <name>
        """
        if not arg:
            print("❌ Please specify a name for the new node")
            return
        
        # Check if node already exists
        if self._find_node(arg):
            print(f"❌ Node '{arg}' already exists")
            return
        
        print(f"\n✨ Creating new node: {arg}")
        print("-" * 40)
        
        # Gather node information
        node_type = input("Node type [concept]: ").strip() or "concept"
        content = input("Content: ").strip()
        realm = input("Realm [physical]: ").strip() or "physical"
        water_state = input("Water state [liquid]: ").strip() or "liquid"
        
        if not content:
            print("❌ Content is required")
            return
        
        # Analyze resonance
        resonance = self.resonance_engine.analyze_resonance("create", content, node_type)
        
        print(f"\n🎵 Resonance Analysis:")
        print(f"   Score: {resonance.resonance_score:.2f} {'🟢' if resonance.resonance_score > 0.7 else '🟡' if resonance.resonance_score > 0.4 else '🔴'}")
        print(f"   Energy Cost: {resonance.energy_cost:.0f} ⚡")
        
        if resonance.harmony_factors:
            print(f"   ✅ Harmony: {', '.join(resonance.harmony_factors)}")
        if resonance.discord_factors:
            print(f"   ⚠️  Discord: {', '.join(resonance.discord_factors)}")
        if resonance.similar_nodes:
            print(f"   🔗 Similar: {', '.join(resonance.similar_nodes)}")
        
        # Check energy
        if resonance.energy_cost > self.current_energy:
            print(f"❌ Insufficient energy! Need {resonance.energy_cost:.0f}, have {self.current_energy}")
            return
        
        # Confirm creation
        confirm = input(f"\nConfirm creation? (y/N): ").strip().lower()
        if confirm != 'y':
            print("❌ Creation cancelled")
            return
        
        # Create the node
        try:
            new_node = DatabaseNode(
                node_id=f"node_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                node_type=node_type,
                name=arg,
                content=content,
                realm=realm,
                water_state=water_state,
                energy_level=1000,
                transformation_cost=resonance.energy_cost,
                parent_id=None,
                children=None,
                metadata={"created_via": "cli", "resonance_score": resonance.resonance_score},
                structure_info=None,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            create_result = self.database.operations.create_node(new_node)
            if create_result.success:
                self.current_energy -= resonance.energy_cost
                self.total_energy_spent += resonance.energy_cost
                print(f"✅ Node '{arg}' created successfully!")
                print(f"💫 Energy remaining: {self.current_energy}")
            else:
                print(f"❌ Failed to create node: {getattr(create_result, 'error_message', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Error creating node: {e}")
    
    def do_modify(self, arg):
        """Modify an existing node
        Usage: modify <node_id>
        """
        if not arg:
            print("❌ Please specify a node ID or name to modify")
            return
        
        node = self._find_node(arg)
        if not node:
            print(f"❌ Node '{arg}' not found")
            return
        
        print(f"\n✏️  Modifying node: {node.name}")
        print("-" * 40)
        print(f"Current content: {node.content}")
        
        new_content = input("New content (Enter to keep current): ").strip()
        if not new_content:
            print("❌ No changes made")
            return
        
        # Analyze resonance for modification
        resonance = self.resonance_engine.analyze_resonance("modify", new_content, node.node_type, node)
        
        print(f"\n🎵 Resonance Analysis:")
        print(f"   Score: {resonance.resonance_score:.2f} {'🟢' if resonance.resonance_score > 0.7 else '🟡' if resonance.resonance_score > 0.4 else '🔴'}")
        print(f"   Energy Cost: {resonance.energy_cost:.0f} ⚡")
        
        if resonance.harmony_factors:
            print(f"   ✅ Harmony: {', '.join(resonance.harmony_factors)}")
        if resonance.discord_factors:
            print(f"   ⚠️  Discord: {', '.join(resonance.discord_factors)}")
        
        # Check energy
        if resonance.energy_cost > self.current_energy:
            print(f"❌ Insufficient energy! Need {resonance.energy_cost:.0f}, have {self.current_energy}")
            return
        
        # Confirm modification
        confirm = input(f"\nConfirm modification? (y/N): ").strip().lower()
        if confirm != 'y':
            print("❌ Modification cancelled")
            return
        
        # Update the node
        try:
            node.content = new_content
            node.updated_at = datetime.now()
            node.metadata = node.metadata or {}
            node.metadata.update({
                "last_modified_via": "cli",
                "modification_resonance": resonance.resonance_score
            })
            
            update_result = self.database.operations.update_node(node)
            if update_result.success:
                self.current_energy -= resonance.energy_cost
                self.total_energy_spent += resonance.energy_cost
                print(f"✅ Node '{node.name}' modified successfully!")
                print(f"💫 Energy remaining: {self.current_energy}")
            else:
                print(f"❌ Failed to modify node: {getattr(update_result, 'error_message', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Error modifying node: {e}")
    
    def do_delete(self, arg):
        """Delete a node (high energy cost due to anti-resonance)
        Usage: delete <node_id>
        """
        if not arg:
            print("❌ Please specify a node ID or name to delete")
            return
        
        node = self._find_node(arg)
        if not node:
            print(f"❌ Node '{arg}' not found")
            return
        
        # Deletion has high energy cost (anti-resonant)
        base_cost = 500
        node_importance = node.energy_level / 100
        delete_cost = base_cost * (1 + node_importance)
        
        print(f"\n🗑️  Deleting node: {node.name}")
        print(f"⚠️  Deletion is anti-resonant and costly!")
        print(f"💥 Energy Cost: {delete_cost:.0f} ⚡")
        
        if delete_cost > self.current_energy:
            print(f"❌ Insufficient energy! Need {delete_cost:.0f}, have {self.current_energy}")
            return
        
        # Confirm deletion
        confirm = input(f"\nAre you sure you want to delete '{node.name}'? (y/N): ").strip().lower()
        if confirm != 'y':
            print("❌ Deletion cancelled")
            return
        
        try:
            delete_result = self.database.operations.delete_node(node.node_id)
            if delete_result.success:
                self.current_energy -= delete_cost
                self.total_energy_spent += delete_cost
                print(f"✅ Node '{node.name}' deleted")
                print(f"💫 Energy remaining: {self.current_energy}")
            else:
                print(f"❌ Failed to delete node: {getattr(delete_result, 'error_message', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Error deleting node: {e}")
    
    def do_analyze(self, arg):
        """Analyze the resonance of potential content without creating it
        Usage: analyze <content>
        """
        if not arg:
            print("❌ Please specify content to analyze")
            return
        
        resonance = self.resonance_engine.analyze_resonance("create", arg, "concept")
        
        print(f"\n🎵 Resonance Analysis for: '{arg[:50]}{'...' if len(arg) > 50 else ''}'")
        print("=" * 60)
        print(f"Resonance Score: {resonance.resonance_score:.2f} {'🟢' if resonance.resonance_score > 0.7 else '🟡' if resonance.resonance_score > 0.4 else '🔴'}")
        print(f"Energy Cost: {resonance.energy_cost:.0f} ⚡")
        print(f"Cost Efficiency: {(resonance.resonance_score / (resonance.energy_cost / 100)):.3f}")
        
        if resonance.harmony_factors:
            print(f"\n✅ Harmony Factors:")
            for factor in resonance.harmony_factors:
                print(f"   • {factor}")
        
        if resonance.discord_factors:
            print(f"\n⚠️  Discord Factors:")
            for factor in resonance.discord_factors:
                print(f"   • {factor}")
        
        if resonance.similar_nodes:
            print(f"\n🔗 Similar Existing Nodes:")
            for similar in resonance.similar_nodes:
                print(f"   • {similar}")
    
    def do_energy(self, arg):
        """Show current energy status
        Usage: energy
        """
        print(f"\n💫 Energy Status:")
        print(f"   Current Energy: {self.current_energy} ⚡")
        print(f"   Total Spent: {self.total_energy_spent} ⚡")
        print(f"   Efficiency Rating: {self._calculate_efficiency()}")
        
        # Energy level indicator
        if self.current_energy > 8000:
            print("   Status: 🟢 Abundant Energy")
        elif self.current_energy > 5000:
            print("   Status: 🟡 Moderate Energy") 
        elif self.current_energy > 2000:
            print("   Status: 🟠 Low Energy")
        else:
            print("   Status: 🔴 Critical Energy")
    
    def do_demo(self, arg):
        """Run system exploration demo to populate database
        Usage: demo
        """
        print("\n🚀 Running System Exploration Demo...")
        print("This will populate the database with initial nodes for exploration.")
        print("=" * 50)
        
        try:
            # Import and run the demo
            from src.core.explore_bootstrapped_system import main as explore_main
            import asyncio
            
            # Run the async demo
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(explore_main())
            loop.close()
            
            print("\n✅ Demo completed! Database should now be populated.")
            print("💡 Try 'list' or 'search <term>' to explore the new nodes.")
            
        except Exception as e:
            print(f"❌ Demo failed: {e}")
            print("💡 You can still use the CLI for analysis and planning.")
    
    def do_resonate(self, arg):
        """Show detailed resonance analysis for an existing node
        Usage: resonate <node_id>
        """
        if not arg:
            print("❌ Please specify a node ID or name")
            return
        
        node = self._find_node(arg)
        if not node:
            print(f"❌ Node '{arg}' not found")
            return
        
        if not node.content:
            print(f"❌ Node '{node.name}' has no content to analyze")
            return
        
        resonance = self.resonance_engine.analyze_resonance("view", node.content, node.node_type, node)
        
        print(f"\n🎵 Detailed Resonance Analysis: {node.name}")
        print("=" * 60)
        print(f"Content: {node.content}")
        print(f"Type: {node.node_type}")
        print(f"Resonance Score: {resonance.resonance_score:.3f}")
        print(f"Hypothetical Modification Cost: {resonance.energy_cost:.0f} ⚡")
        
        # Show resonance breakdown
        print(f"\n📊 Resonance Breakdown:")
        print(f"   Semantic Harmony: {'🟢' if resonance.resonance_score > 0.7 else '🟡' if resonance.resonance_score > 0.4 else '🔴'}")
        print(f"   Structural Fit: {'🟢' if node.node_type in ['concept', 'file'] else '🟡'}")
        print(f"   Energy Balance: {'🟢' if node.energy_level > 800 else '🟡' if node.energy_level > 400 else '🔴'}")
        
        if resonance.harmony_factors:
            print(f"\n✅ Harmony Factors:")
            for factor in resonance.harmony_factors:
                print(f"   • {factor}")
        
        if resonance.discord_factors:
            print(f"\n⚠️  Discord Factors:")
            for factor in resonance.discord_factors:
                print(f"   • {factor}")
        
        if resonance.similar_nodes:
            print(f"\n🔗 Similar Nodes:")
            for similar in resonance.similar_nodes:
                print(f"   • {similar}")
    
    def do_quit(self, arg):
        """Exit the CLI
        Usage: quit
        """
        print(f"\n👋 Thank you for using the Living Codex CLI!")
        print(f"💫 Final Energy: {self.current_energy} ⚡")
        print(f"📊 Total Energy Spent: {self.total_energy_spent} ⚡")
        print(f"🎯 Efficiency Rating: {self._calculate_efficiency()}")
        print("🌟 The Living Codex continues to evolve...")
        return True
    
    def do_exit(self, arg):
        """Exit the CLI (alias for quit)"""
        return self.do_quit(arg)
    
    def _find_node(self, identifier: str) -> Optional[DatabaseNode]:
        """Find a node by ID or name"""
        try:
            # Try by exact ID first
            result = self.database.operations.query_nodes(
                [QueryFilter("node_id", "=", identifier)], 
                QueryOptions(limit=1)
            )
            if result.success and result.data:
                return result.data[0]
            
            # Try by exact name
            result = self.database.operations.query_nodes(
                [QueryFilter("name", "=", identifier)], 
                QueryOptions(limit=1)
            )
            if result.success and result.data:
                return result.data[0]
            
            # Try partial name match
            all_result = self.database.operations.query_nodes([], QueryOptions())
            if all_result.success and all_result.data:
                for node in all_result.data:
                    if identifier.lower() in node.name.lower():
                        return node
        except Exception as e:
            print(f"⚠️  Database query error: {e}")
        
        return None
    
    def _calculate_efficiency(self) -> str:
        """Calculate energy efficiency rating"""
        if self.total_energy_spent == 0:
            return "Perfect (No energy spent)"
        
        efficiency_ratio = (10000 - self.current_energy) / self.total_energy_spent
        if efficiency_ratio < 0.5:
            return "🌟 Excellent"
        elif efficiency_ratio < 0.8:
            return "🟢 Good"
        elif efficiency_ratio < 1.2:
            return "🟡 Fair"
        else:
            return "🔴 Poor"
    
    def default(self, line):
        """Handle unknown commands"""
        if not line.strip():  # Handle empty lines
            return
        print(f"❌ Unknown command: {line}")
        print("Type 'help' for available commands")
    
    def emptyline(self):
        """Handle empty line"""
        pass
    
    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) gracefully"""
        print("\n👋 EOF detected. Exiting gracefully...")
        return self.do_quit(arg)
    
    def do_eof(self, arg):
        """Handle EOF (Ctrl+D) gracefully - lowercase alias"""
        return self.do_EOF(arg)

def main():
    """Main entry point for the CLI"""
    try:
        cli = LivingCodexCLI()
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\n\n👋 CLI interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ CLI Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
