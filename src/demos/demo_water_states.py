#!/usr/bin/env python3
"""
Water State Storage Demo

This script demonstrates how the Living Codex uses different water states
to determine optimal storage strategies for different types of data.
"""

import sys
import time
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from core.water_state_storage import (
    WaterStateStorage, WaterState, 
    store_as_ice, store_as_water, store_as_vapor, store_as_plasma
)

def demo_ice_storage():
    """Demonstrate ICE state storage (Global Federation)"""
    print("\n🧊 ICE STORAGE - Global Federation & Consensus")
    print("=" * 50)
    
    storage = WaterStateStorage()
    
    # Store immutable, verified knowledge
    print("📚 Storing core knowledge in ICE state...")
    core_knowledge = {
        "principle": "The Living Codex is a living, evolving system",
        "verified_by": ["community_consensus", "scientific_validation"],
        "immutable": True,
        "federation_nodes": ["node_alpha", "node_beta", "node_gamma"]
    }
    
    success = store_as_ice(storage, "core_principle", core_knowledge, {
        "category": "philosophy",
        "verification_level": "consensus",
        "federation_required": True
    })
    
    if success:
        print("✅ Core knowledge stored with global consensus")
        
        # Retrieve and show storage info
        data = storage.retrieve("core_principle", WaterState.ICE)
        info = storage.get_storage_info("core_principle", WaterState.ICE)
        
        print(f"📖 Retrieved: {data['principle']}")
        print(f"🔒 Storage: {info['strategy']}")
        print(f"🌐 Consensus Hash: {info['consensus_hash']}")
    else:
        print("❌ Failed to store core knowledge")

def demo_water_storage():
    """Demonstrate WATER state storage (Local Persistence)"""
    print("\n💧 WATER STORAGE - Local Persistence & Adaptability")
    print("=" * 50)
    
    storage = WaterStateStorage()
    
    # Store user preferences and local knowledge
    print("👤 Storing user preferences in WATER state...")
    user_profile = {
        "user_id": "alice_123",
        "preferences": {
            "theme": "dark",
            "language": "en",
            "timezone": "UTC-8",
            "learning_style": "visual"
        },
        "local_knowledge": {
            "favorite_topics": ["AI", "philosophy", "art"],
            "recent_searches": ["consciousness", "emergence", "creativity"]
        }
    }
    
    success = store_as_water(storage, "user_profile_alice", user_profile, {
        "category": "user_data",
        "privacy_level": "personal",
        "backup_frequency": "daily"
    })
    
    if success:
        print("✅ User profile stored locally with persistence")
        
        # Retrieve and show storage info
        data = storage.retrieve("user_profile_alice", WaterState.WATER)
        info = storage.get_storage_info("user_profile_alice", WaterState.WATER)
        
        print(f"👤 User: {data['user_id']}")
        print(f"🎨 Theme: {data['preferences']['theme']}")
        print(f"💾 Storage: {info['strategy']}")
        print(f"📅 Created: {info['created_at']}")
        print(f"🗜️  Compressed: {info['compression_enabled']}")
    else:
        print("❌ Failed to store user profile")

def demo_vapor_storage():
    """Demonstrate VAPOR state storage (Memory & Sessions)"""
    print("\n☁️ VAPOR STORAGE - Memory & Temporary Sessions")
    print("=" * 50)
    
    storage = WaterStateStorage()
    
    # Store temporary session data
    print("🔄 Storing session data in VAPOR state...")
    session_data = {
        "session_id": "sess_abc123",
        "current_page": "dashboard",
        "active_tabs": ["knowledge_graph", "collaboration", "search"],
        "recent_actions": [
            {"action": "search", "query": "water states", "timestamp": time.time()},
            {"action": "navigate", "page": "dashboard", "timestamp": time.time()}
        ],
        "temporary_notes": [
            "Remember to check the new water state storage system",
            "Interesting connection between physics and data architecture"
        ]
    }
    
    success = store_as_vapor(storage, "session_abc123", session_data, {
        "category": "session",
        "ttl_hours": 1,
        "auto_cleanup": True
    })
    
    if success:
        print("✅ Session data stored in memory with TTL")
        
        # Retrieve and show storage info
        data = storage.retrieve("session_abc123", WaterState.VAPOR)
        info = storage.get_storage_info("session_abc123", WaterState.VAPOR)
        
        print(f"🆔 Session: {data['session_id']}")
        print(f"📱 Current Page: {data['current_page']}")
        print(f"💾 Storage: {info['strategy']}")
        print(f"⏰ TTL: {info['ttl_seconds']} seconds")
        print(f"🧠 In Memory: {info['in_memory']}")
        
        # Simulate time passing
        print("\n⏰ Simulating time passing...")
        time.sleep(2)
        
        # Check if still available
        data_after = storage.retrieve("session_abc123", WaterState.VAPOR)
        if data_after:
            print("✅ Session still active in memory")
        else:
            print("❌ Session expired and cleaned up")
    else:
        print("❌ Failed to store session data")

def demo_plasma_storage():
    """Demonstrate PLASMA state storage (Real-time Streaming)"""
    print("\n⚡ PLASMA STORAGE - Real-time Streaming & Collaboration")
    print("=" * 50)
    
    storage = WaterStateStorage()
    
    # Store real-time collaboration events
    print("🤝 Storing collaboration events in PLASMA state...")
    
    # Simulate multiple users collaborating
    collaboration_events = [
        {
            "user_id": "alice",
            "action": "join_room",
            "room": "water_states_discussion",
            "timestamp": time.time()
        },
        {
            "user_id": "bob",
            "action": "share_idea",
            "content": "What if we use quantum entanglement for ICE storage?",
            "room": "water_states_discussion",
            "timestamp": time.time()
        },
        {
            "user_id": "charlie",
            "action": "react",
            "reaction": "🧠",
            "target": "bob's idea",
            "room": "water_states_discussion",
            "timestamp": time.time()
        }
    ]
    
    # Store each event
    for i, event in enumerate(collaboration_events):
        key = f"collab_event_{i}"
        success = store_as_plasma(storage, key, event, {
            "category": "collaboration",
            "room": event.get("room", "general"),
            "priority": "high"
        })
        
        if success:
            print(f"✅ Event {i+1} stored: {event['action']} by {event['user_id']}")
        else:
            print(f"❌ Failed to store event {i+1}")
    
    # Show streaming information
    print("\n📊 Streaming Information:")
    for i in range(len(collaboration_events)):
        key = f"collab_event_{i}"
        info = storage.get_storage_info(key, WaterState.PLASMA)
        
        print(f"  Event {i+1}: {info['event_count']} events, {info['subscriber_count']} subscribers")
    
    # Get stream history
    engine = storage.storage_engines[storage.storage_engines.keys().__iter__().__next__()]
    if hasattr(engine, 'get_stream_history'):
        print("\n📜 Recent Collaboration History:")
        for i in range(len(collaboration_events)):
            key = f"collab_event_{i}"
            history = engine.get_stream_history(key, limit=3)
            if history:
                latest = history[-1]
                print(f"  {latest['metadata']['user_id']}: {latest['data']['action']}")

def demo_water_state_transitions():
    """Demonstrate how data can transition between water states"""
    print("\n🔄 WATER STATE TRANSITIONS")
    print("=" * 50)
    
    storage = WaterStateStorage()
    
    # Start with an idea in VAPOR (temporary)
    print("💡 Starting with an idea in VAPOR state...")
    idea = {
        "concept": "Water state-based data architecture",
        "description": "Using physics metaphors for data storage decisions",
        "status": "exploration",
        "confidence": 0.7
    }
    
    store_as_vapor(storage, "new_idea", idea, {"category": "exploration"})
    print("✅ Idea stored in VAPOR (memory)")
    
    # As the idea develops, move to WATER (local persistence)
    print("\n💧 Idea developing - moving to WATER state...")
    developed_idea = {
        **idea,
        "status": "development",
        "confidence": 0.85,
        "implementation_notes": [
            "ICE: Global federation with consensus",
            "WATER: Local database persistence",
            "VAPOR: Memory with TTL",
            "PLASMA: Real-time streaming"
        ],
        "created_date": time.time()
    }
    
    store_as_water(storage, "developed_idea", developed_idea, {
        "category": "development",
        "version": "1.0"
    })
    print("✅ Idea moved to WATER (local persistence)")
    
    # When fully validated, move to ICE (global consensus)
    print("\n🧊 Idea validated - moving to ICE state...")
    validated_idea = {
        **developed_idea,
        "status": "validated",
        "confidence": 0.95,
        "validation_method": "community_consensus",
        "federation_nodes": ["node_alpha", "node_beta", "node_gamma"],
        "immutable": True
    }
    
    store_as_ice(storage, "validated_idea", validated_idea, {
        "category": "validated_knowledge",
        "consensus_required": True
    })
    print("✅ Idea moved to ICE (global consensus)")
    
    # Show the progression
    print("\n📈 Idea Evolution Through Water States:")
    vapor_data = storage.retrieve("new_idea", WaterState.VAPOR)
    water_data = storage.retrieve("developed_idea", WaterState.WATER)
    ice_data = storage.retrieve("validated_idea", WaterState.ICE)
    
    print(f"  VAPOR: {vapor_data['status']} (confidence: {vapor_data['confidence']})")
    print(f"  WATER: {water_data['status']} (confidence: {water_data['confidence']})")
    print(f"  ICE: {ice_data['status']} (confidence: {ice_data['confidence']})")

def main():
    """Run the complete water state storage demo"""
    print("🌊 Living Codex - Water State Storage System Demo")
    print("=" * 60)
    print("This demo shows how different water states determine")
    print("optimal storage strategies for different types of data.")
    print("=" * 60)
    
    try:
        # Run all demos
        demo_ice_storage()
        demo_water_storage()
        demo_vapor_storage()
        demo_plasma_storage()
        demo_water_state_transitions()
        
        print("\n🎉 Water State Storage Demo Complete!")
        print("\n💡 Key Insights:")
        print("  🧊 ICE: For immutable, globally-verified knowledge")
        print("  💧 WATER: For stable, locally-persistent data")
        print("  ☁️ VAPOR: For temporary, fast-access sessions")
        print("  ⚡ PLASMA: For real-time, collaborative interactions")
        print("  🔄 Data can transition between states as it evolves")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
