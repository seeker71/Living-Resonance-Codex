#!/usr/bin/env python3
"""
Test script for the Living Codex Persistence System
Demonstrates saving and restoring complete system state
"""

from living_codex_persistence import LivingCodexPersistence
from self_reflective_file_system import SelfReflectiveFileSystem
from universal_knowledge_representation_system import get_universal_knowledge_representation_system
from fractal_recursion_system import get_fractal_recursion_system
from advanced_ai_integration_system import get_advanced_ai_integration_system
from self_generating_system import get_self_generating_system
from vibrational_axes_system import get_vibrational_axes_system
from resonance_governance_system import get_resonance_governance_system

def test_persistence_system():
    """Test the complete persistence system"""
    print("🧪 Testing Living Codex Persistence System")
    print("=" * 60)
    
    # Initialize all systems
    print("\n1. Initializing all Living Codex systems...")
    universal_system = get_universal_knowledge_representation_system()
    fractal_system = get_fractal_recursion_system()
    ai_system = get_advanced_ai_integration_system()
    self_gen_system = get_self_generating_system()
    vibrational_system = get_vibrational_axes_system()
    governance_system = get_resonance_governance_system()
    
    print("   ✅ All systems initialized")
    
    # Initialize persistence system
    print("\n2. Initializing persistence system...")
    persistence = LivingCodexPersistence()
    print("   ✅ Persistence system initialized")
    
    # Check initial state
    print(f"\n3. Initial system state:")
    print(f"   🧠 Universal concepts: {len(universal_system.universal_concepts)}")
    print(f"   🏗️ Fractal nodes: {len(fractal_system.fractal_nodes)}")
    print(f"   🤖 AI agents: {len(ai_system.ai_agents)}")
    
    # Discover and create file nodes
    print(f"\n4. Discovering and creating file nodes...")
    fs = SelfReflectiveFileSystem()
    fs.discover_all_source_files()
    fs.create_file_nodes_in_living_codex(universal_system)
    
    # Check state after file creation
    print(f"\n5. State after file node creation:")
    print(f"   🧠 Universal concepts: {len(universal_system.universal_concepts)}")
    print(f"   🏗️ Fractal nodes: {len(fractal_system.fractal_nodes)}")
    print(f"   🤖 AI agents: {len(ai_system.ai_agents)}")
    
    # Save system state
    print(f"\n6. Saving complete system state...")
    save_success = persistence.save_system_state(
        universal_system, fractal_system, ai_system,
        self_gen_system, vibrational_system, governance_system
    )
    
    if not save_success:
        print("   ❌ Failed to save system state")
        return False
    
    # Get persistence info
    print(f"\n7. Persistence system info:")
    info = persistence.get_system_info()
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # Clear system state (simulate restart)
    print(f"\n8. Clearing system state (simulating restart)...")
    universal_system.universal_concepts.clear()
    fractal_system.fractal_nodes.clear()
    ai_system.ai_agents.clear()
    self_gen_system.discovered_concepts.clear()
    
    print(f"   ✅ System state cleared")
    print(f"   🧠 Universal concepts: {len(universal_system.universal_concepts)}")
    print(f"   🏗️ Fractal nodes: {len(fractal_system.fractal_nodes)}")
    print(f"   🤖 AI agents: {len(ai_system.ai_agents)}")
    
    # Restore system state
    print(f"\n9. Restoring system state...")
    restore_success = persistence.load_system_state(
        universal_system, fractal_system, ai_system,
        self_gen_system, vibrational_system, governance_system
    )
    
    if not restore_success:
        print("   ❌ Failed to restore system state")
        return False
    
    # Verify restoration
    print(f"\n10. Verification after restoration:")
    print(f"    🧠 Universal concepts: {len(universal_system.universal_concepts)}")
    print(f"    🏗️ Fractal nodes: {len(fractal_system.fractal_nodes)}")
    print(f"    🤖 AI agents: {len(ai_system.ai_agents)}")
    
    # Test node accessibility
    print(f"\n11. Testing node accessibility...")
    if universal_system.universal_concepts:
        sample_concepts = list(universal_system.universal_concepts.values())[:3]
        print(f"    📄 Sample concepts restored:")
        for i, concept in enumerate(sample_concepts):
            print(f"      {i+1}. {concept.name} (ID: {concept.concept_id})")
    
    print(f"\n" + "=" * 60)
    print(f"🎉 Persistence system test completed successfully!")
    return True

if __name__ == "__main__":
    test_persistence_system()
