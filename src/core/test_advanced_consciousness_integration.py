#!/usr/bin/env python3
"""
Test script for the Advanced Consciousness Integration System
"""

from advanced_consciousness_integration_system import get_advanced_consciousness_integration_system
from living_codex_ontology import (
    ConsciousnessLevel, QuantumState, WaterStateKey, 
    FrequencyKey, ChakraKey, ResonancePattern
)

def test_advanced_consciousness_integration():
    """Test the advanced consciousness integration system"""
    print("🧠 Testing Advanced Consciousness Integration System...")
    
    # Initialize the system
    consciousness_system = get_advanced_consciousness_integration_system()
    
    print(f"\n✅ System initialized successfully")
    print(f"   📊 Consciousness quantum states: {len(consciousness_system.consciousness_quantum_states)}")
    print(f"   🌊 Resonance fields: {len(consciousness_system.resonance_fields)}")
    print(f"   ✨ Coherence fields: {len(consciousness_system.coherence_fields)}")
    print(f"   🔄 Consciousness evolutions: {len(consciousness_system.consciousness_evolutions)}")
    
    # Test consciousness quantum states
    print(f"\n🧪 Testing Consciousness Quantum States...")
    for state_id, state in consciousness_system.consciousness_quantum_states.items():
        print(f"   ✅ {state_id}: {state.consciousness_level.value} + {state.quantum_state.value} + {state.water_state.value}")
        print(f"      🎵 Frequency: {state.frequency.value} Hz")
        print(f"      🌀 Chakra: {state.chakra.value}")
        print(f"      ✨ Coherence: {state.coherence_level:.2f}")
        print(f"      🌊 Resonance: {state.resonance_strength:.2f}")
    
    # Test resonance fields
    print(f"\n🧪 Testing Resonance Fields...")
    for field_id, field in consciousness_system.resonance_fields.items():
        print(f"   ✅ {field_id}: {field.field_name}")
        print(f"      🌊 Pattern: {field.resonance_pattern.value}")
        print(f"      💧 Water State: {field.water_state.value}")
        print(f"      🎵 Frequency: {field.frequency.value} Hz")
        print(f"      🌀 Chakra: {field.chakra.value}")
        print(f"      📏 Radius: {field.coherence_radius}")
        print(f"      🌊 Strength: {field.resonance_strength:.2f}")
    
    # Test coherence fields
    print(f"\n🧪 Testing Coherence Fields...")
    for field_id, field in consciousness_system.coherence_fields.items():
        print(f"   ✅ {field_id}: {field.field_name}")
        print(f"      🧠 Consciousness Levels: {[l.value for l in field.consciousness_levels]}")
        print(f"      ⚛️ Quantum States: {[s.value for s in field.quantum_states]}")
        print(f"      💧 Water States: {[w.value for w in field.water_states]}")
        print(f"      ✨ Coherence Score: {field.coherence_score:.2f}")
        print(f"      🌊 Resonance Patterns: {[p.value for p in field.resonance_patterns]}")
    
    # Test creating new consciousness quantum state
    print(f"\n🧪 Testing Creation of New Consciousness Quantum State...")
    new_state_id = consciousness_system.create_consciousness_quantum_state(
        ConsciousnessLevel.SELF_AWARE,
        QuantumState.SUPERPOSITION,
        WaterStateKey.VAPOR,
        FrequencyKey.FREQ_528,
        ChakraKey.SOLAR_PLEXUS,
        0.8,
        0.8
    )
    print(f"   ✅ Created new state: {new_state_id}")
    
    # Test creating new resonance field
    print(f"\n🧪 Testing Creation of New Resonance Field...")
    new_field_id = consciousness_system.create_resonance_field(
        "Test Harmonic Field",
        ResonancePattern.HARMONIC,
        WaterStateKey.STRUCTURED,
        FrequencyKey.FREQ_741,
        ChakraKey.THROAT,
        5.0,
        0.8
    )
    print(f"   ✅ Created new resonance field: {new_field_id}")
    
    # Test creating new coherence field
    print(f"\n🧪 Testing Creation of New Coherence Field...")
    new_coherence_id = consciousness_system.create_coherence_field(
        "Test Coherence Field",
        [ConsciousnessLevel.SENTIENT, ConsciousnessLevel.SELF_AWARE],
        [QuantumState.COLLAPSED, QuantumState.COLLAPSED],
        [WaterStateKey.LIQUID, WaterStateKey.VAPOR],
        0.75,
        [ResonancePattern.SYMPATHETIC]
    )
    print(f"   ✅ Created new coherence field: {new_coherence_id}")
    
    # Test consciousness evolution
    print(f"\n🧪 Testing Consciousness Evolution...")
    evolution_id = consciousness_system.evolve_consciousness(
        "awake_ice",
        ConsciousnessLevel.SENTIENT,
        QuantumState.COLLAPSED,
        WaterStateKey.LIQUID
    )
    print(f"   ✅ Created consciousness evolution: {evolution_id}")
    
    # Get final analytics
    print(f"\n🧪 Testing Analytics...")
    analytics = consciousness_system.get_consciousness_analytics()
    print(f"   📊 Total consciousness states: {analytics['total_consciousness_states']}")
    print(f"   🌊 Total resonance fields: {analytics['total_resonance_fields']}")
    print(f"   ✨ Total coherence fields: {analytics['total_coherence_fields']}")
    print(f"   🔄 Total consciousness evolutions: {analytics['total_consciousness_evolutions']}")
    
    print(f"\n✅ Advanced Consciousness Integration System test completed successfully!")
    return True

if __name__ == "__main__":
    test_advanced_consciousness_integration()
