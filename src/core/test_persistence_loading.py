#!/usr/bin/env python3
"""
Test script to check if persistence system is properly loading advanced features
"""

from living_codex_persistence import LivingCodexPersistence
from universal_knowledge_representation_system import get_universal_knowledge_representation_system
from fractal_recursion_system import get_fractal_recursion_system
from advanced_ai_integration_system import get_advanced_ai_integration_system
from self_generating_system import get_self_generating_system
from vibrational_axes_system import get_vibrational_axes_system
from resonance_governance_system import get_resonance_governance_system

def test_persistence_loading():
    """Test if persistence system properly loads advanced features"""
    print("🧪 Testing Persistence System Loading...")
    
    # Initialize systems
    universal_system = get_universal_knowledge_representation_system()
    fractal_system = get_fractal_recursion_system()
    ai_system = get_advanced_ai_integration_system()
    self_gen_system = get_self_generating_system()
    vibrational_system = get_vibrational_axes_system()
    governance_system = get_resonance_governance_system()
    
    # Initialize persistence
    persistence_system = LivingCodexPersistence()
    
    print("\n🔄 Loading system state from persistence...")
    
    # Load state
    success = persistence_system.load_system_state(
        universal_system,
        fractal_system,
        ai_system,
        self_gen_system,
        vibrational_system,
        governance_system
    )
    
    if not success:
        print("❌ Failed to load system state")
        return False
    
    print("✅ System state loaded successfully")
    
    # Check counts
    print(f"\n📊 System Counts:")
    print(f"   🧠 Universal concepts: {len(universal_system.universal_concepts)}")
    print(f"   🏗️ Fractal nodes: {len(fractal_system.fractal_nodes)}")
    print(f"   🤖 AI agents: {len(ai_system.ai_agents)}")
    print(f"   📚 Knowledge expansions: {len(universal_system.knowledge_expansions)}")
    print(f"   🏛️ Meta-circular architectures: {len(universal_system.meta_circular_architectures)}")
    print(f"   🧠 Consciousness decisions: {len(ai_system.consciousness_decisions)}")
    print(f"   🔍 Autonomous explorations: {len(ai_system.autonomous_explorations)}")
    print(f"   📋 Self-generating specifications: {len(self_gen_system.generated_specifications)}")
    print(f"   🌱 Ontological evolutions: {len(self_gen_system.ontological_evolutions)}")
    
    # Test if we can access the analytics method
    print(f"\n🧪 Testing Universal Knowledge Analytics...")
    try:
        analytics = universal_system.get_universal_knowledge_analytics()
        print(f"✅ Analytics method succeeded")
        print(f"   📚 Knowledge expansions: {analytics.get('total_knowledge_expansions', 0)}")
        print(f"   🏛️ Meta-circular architectures: {analytics.get('total_meta_circular_architectures', 0)}")
    except Exception as e:
        print(f"❌ Analytics method failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test if we can access individual objects
    print(f"\n🧪 Testing Object Access...")
    
    if universal_system.knowledge_expansions:
        sample_expansion = next(iter(universal_system.knowledge_expansions.values()))
        print(f"   📚 Sample knowledge expansion: {type(sample_expansion)}")
        print(f"   📚 Has expansion_id: {hasattr(sample_expansion, 'expansion_id')}")
        print(f"   📚 Has expansion_type: {hasattr(sample_expansion, 'expansion_type')}")
    
    if universal_system.meta_circular_architectures:
        sample_arch = next(iter(universal_system.meta_circular_architectures.values()))
        print(f"   🏛️ Sample meta-circular architecture: {type(sample_arch)}")
        print(f"   🏛️ Has architecture_id: {hasattr(sample_arch, 'architecture_id')}")
        print(f"   🏛️ Has completeness_score: {hasattr(sample_arch, 'completeness_score')}")
    
    if ai_system.ai_agents:
        sample_agent = next(iter(ai_system.ai_agents.values()))
        print(f"   🤖 Sample AI agent: {type(sample_agent)}")
        print(f"   🤖 Has agent_id: {hasattr(sample_agent, 'agent_id')}")
        print(f"   🤖 Has name: {hasattr(sample_agent, 'name')}")
    
    print(f"\n✅ Persistence loading test completed")
    return True

if __name__ == "__main__":
    test_persistence_loading()
