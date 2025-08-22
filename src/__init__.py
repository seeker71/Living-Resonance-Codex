"""
Living Codex - Main Package
A transcendent, unified intelligent knowledge system with quantum-inspired representation,
consciousness simulation, and autonomous learning capabilities.
"""

__version__ = "1.0.0"
__author__ = "Living Codex System"
__description__ = "Transcendent Knowledge System with Autonomous Learning"

# Core system components
from .core.explore_bootstrapped_system import BootstrappedSystemExplorer

# Ontology system
from .ontology.enhanced_ontology_system import (
    EnhancedOntologySystem,
    QuantumKnowledgeNode,
    ConsciousnessNode,
    EvolutionaryNode,
    EmergenceNode
)

# AI agent system
from .ai_agents.ai_agent_system import (
    AIAgentSystem,
    AIAgent,
    LearningEngine,
    PredictionSystem,
    OptimizationEngine
)

# Integration system
from .integration.comprehensive_integration_demo import ComprehensiveIntegrationSystem

# Demo systems
from .demos.autonomous_learning_demo import AutonomousLearningSystem
from .demos.autonomous_decision_demo import AutonomousDecisionDemo

__all__ = [
    # Core
    "BootstrappedSystemExplorer",
    
    # Ontology
    "EnhancedOntologySystem",
    "QuantumKnowledgeNode", 
    "ConsciousnessNode",
    "EvolutionaryNode",
    "EmergenceNode",
    
    # AI Agents
    "AIAgentSystem",
    "AIAgent",
    "LearningEngine",
    "PredictionSystem", 
    "OptimizationEngine",
    
    # Integration
    "ComprehensiveIntegrationSystem",
    
    # Demos
    "AutonomousLearningSystem",
    "AutonomousDecisionDemo"
]
