#!/usr/bin/env python3
"""
Test imports for the organized Living Codex system
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_core_imports():
    """Test core system imports"""
    try:
        from src.core import BootstrappedSystemExplorer
        print("✅ Core imports successful")
        return True
    except ImportError as e:
        print(f"❌ Core import failed: {e}")
        return False

def test_ontology_imports():
    """Test ontology system imports"""
    try:
        from src.ontology import (
            EnhancedOntologySystem,
            QuantumKnowledgeNode,
            ConsciousnessNode,
            EvolutionaryNode,
            EmergenceNode
        )
        print("✅ Ontology imports successful")
        return True
    except ImportError as e:
        print(f"❌ Ontology import failed: {e}")
        return False

def test_ai_agent_imports():
    """Test AI agent system imports"""
    try:
        from src.ai_agents import (
            AIAgentSystem,
            AIAgent,
            LearningEngine,
            PredictionSystem,
            OptimizationEngine
        )
        print("✅ AI Agent imports successful")
        return True
    except ImportError as e:
        print(f"❌ AI Agent import failed: {e}")
        return False

def test_integration_imports():
    """Test integration system imports"""
    try:
        from src.integration import ComprehensiveIntegrationSystem
        print("✅ Integration imports successful")
        return True
    except ImportError as e:
        print(f"❌ Integration import failed: {e}")
        return False

def test_demo_imports():
    """Test demo system imports"""
    try:
        from src.demos import (
            AutonomousLearningSystem,
            AutonomousDecisionDemo
        )
        print("✅ Demo imports successful")
        return True
    except ImportError as e:
        print(f"❌ Demo import failed: {e}")
        return False

def test_main_package_imports():
    """Test main package imports"""
    try:
        from src import (
            BootstrappedSystemExplorer,
            EnhancedOntologySystem,
            AIAgentSystem,
            ComprehensiveIntegrationSystem,
            AutonomousLearningSystem,
            AutonomousDecisionDemo
        )
        print("✅ Main package imports successful")
        return True
    except ImportError as e:
        print(f"❌ Main package import failed: {e}")
        return False

def run_all_tests():
    """Run all import tests"""
    print("🧪 Testing Living Codex System Imports")
    print("=" * 50)
    
    tests = [
        test_core_imports,
        test_ontology_imports,
        test_ai_agent_imports,
        test_integration_imports,
        test_demo_imports,
        test_main_package_imports
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All imports successful! System is properly organized.")
        return True
    else:
        print("❌ Some imports failed. Check the organization.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
