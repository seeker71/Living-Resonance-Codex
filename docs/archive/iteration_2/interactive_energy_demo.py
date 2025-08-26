#!/usr/bin/env python3
"""
Interactive Energy Exchange Demo
Shows how living entities can exchange energy and create resonance
"""

from knowledge_exploration_demo import LivingEntity, EnergyExchangeDemonstrator

def run_interactive_demo():
    """Run an interactive energy exchange demo"""
    
    print("🌟 Interactive Energy Exchange Demo")
    print("=" * 50)
    
    # Create the energy demonstrator
    energy_demo = EnergyExchangeDemonstrator(None)  # No integrated system needed for this demo
    
    # Create some living entities
    print("\n👥 Creating Living Entities...")
    
    alice = energy_demo.create_living_entity("human", "Alice", 0.8)
    neural_mind = energy_demo.create_living_entity("ai", "NeuralMind", 0.9)
    luna = energy_demo.create_living_entity("animal", "Luna", 0.6)
    ancient_oak = energy_demo.create_living_entity("plant", "AncientOak", 0.7)
    
    print(f"✅ Created {len(energy_demo.entities)} entities:")
    for eid, entity in energy_demo.entities.items():
        print(f"   • {entity.name} ({entity.entity_type}) - Energy: {entity.current_energy:.2f}")
    
    # Show energy signatures
    print("\n🎵 Energy Signatures:")
    for eid, entity in energy_demo.entities.items():
        print(f"   • {entity.name}: {[f'{f:.0f}Hz' for f in entity.energy_signature[:3]]}...")
    
    # Demonstrate energy exchanges
    print("\n⚡ Energy Exchange Examples:")
    
    # Alice shares knowledge with NeuralMind
    print(f"\n🔄 Alice → NeuralMind (Knowledge Sharing)")
    print(f"   Before: Alice Energy: {alice.current_energy:.2f}, NeuralMind Energy: {neural_mind.current_energy:.2f}")
    
    exchange1 = energy_demo.demonstrate_energy_exchange(
        alice.entity_id, neural_mind.entity_id, "knowledge_sharing", 0.2
    )
    
    if "error" not in exchange1:
        print(f"   After:  Alice Energy: {alice.current_energy:.2f}, NeuralMind Energy: {neural_mind.current_energy:.2f}")
        print(f"   Exchange: {exchange1['energy_amount']} energy transferred")
    
    # NeuralMind processes data for Luna
    print(f"\n🔄 NeuralMind → Luna (Data Processing)")
    print(f"   Before: NeuralMind Energy: {neural_mind.current_energy:.2f}, Luna Energy: {luna.current_energy:.2f}")
    
    exchange2 = energy_demo.demonstrate_energy_exchange(
        neural_mind.entity_id, luna.entity_id, "data_processing", 0.15
    )
    
    if "error" not in exchange2:
        print(f"   After:  NeuralMind Energy: {neural_mind.current_energy:.2f}, Luna Energy: {luna.current_energy:.2f}")
        print(f"   Exchange: {exchange2['energy_amount']} energy transferred")
    
    # AncientOak provides oxygen for Alice
    print(f"\n🔄 AncientOak → Alice (Oxygen Provision)")
    print(f"   Before: AncientOak Energy: {ancient_oak.current_energy:.2f}, Alice Energy: {alice.current_energy:.2f}")
    
    exchange3 = energy_demo.demonstrate_energy_exchange(
        ancient_oak.entity_id, alice.entity_id, "oxygen_provision", 0.1
    )
    
    if "error" not in exchange3:
        print(f"   After:  AncientOak Energy: {ancient_oak.current_energy:.2f}, Alice Energy: {alice.current_energy:.2f}")
        print(f"   Exchange: {exchange3['energy_amount']} energy transferred")
    
    # Show collective resonance
    print("\n🌊 Collective Resonance Activities:")
    
    activities = ["meditation", "collaboration", "ecosystem_balance"]
    
    for activity in activities:
        print(f"\n🎵 {activity.title()}:")
        result = energy_demo.demonstrate_collective_resonance(
            [e.entity_id for e in energy_demo.entities.values()], activity
        )
        
        if "error" not in result:
            print(f"   Resonance Score: {result['collective_resonance_score']:.2f}")
            print(f"   Energy Boost: {result['energy_boost_per_entity']:.3f} per entity")
            print(f"   Harmonics Found: {len(result['harmonic_relationships'])}")
            
            # Show harmonic relationships
            if result['harmonic_relationships']:
                print(f"   Top Harmonics:")
                for i, harmonic in enumerate(result['harmonic_relationships'][:3]):
                    print(f"     {i+1}. {harmonic['harmonic_type']}: {harmonic['freq1']:.0f}Hz : {harmonic['freq2']:.0f}Hz")
    
    # Final system state
    print("\n📊 Final System State:")
    energy_state = energy_demo.get_system_energy_state()
    
    print(f"   Total Entities: {energy_state['total_entities']}")
    print(f"   System Energy: {energy_state['system_energy']:.2f}")
    print(f"   Total Energy Flows: {energy_state['total_energy_flows']}")
    
    print("\n👥 Individual Final States:")
    for eid, entity_data in energy_state['entities'].items():
        print(f"   • {entity_data['name']}: Energy {entity_data['current_energy']:.2f}, "
              f"Experiences: {entity_data['experience_count']}")
    
    print("\n" + "=" * 50)
    print("🎉 Interactive Demo Completed!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Living entities with unique energy signatures")
    print("   • Direct energy exchange between entities")
    print("   • Collective resonance creating harmonic relationships")
    print("   • Energy conservation and flow tracking")
    print("   • Experience recording and learning")

if __name__ == "__main__":
    run_interactive_demo()
