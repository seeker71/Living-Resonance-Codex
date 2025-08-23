#!/usr/bin/env python3
"""
User Management & Discovery Demo - Living Codex
Demonstrates comprehensive user management, interest tracking, and intelligent discovery
"""

import sys
import os
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

def demo_user_management():
    """Demonstrate comprehensive user management capabilities"""
    
    print("👥 Living Codex - User Management & Discovery Demo")
    print("=" * 60)
    print()
    
    print("🌟 This demo shows how to manage users and discover connections:")
    print("   • Create and manage user profiles")
    print("   • Track interests, skills, and locations")
    print("   • Discover users with similar interests")
    print("   • Location-based user discovery")
    print("   • Calculate user resonance and compatibility")
    print()
    
    print("🚀 Starting User Management Demo...")
    print()
    
    # Simulate CLI commands
    commands = [
        "user create Alice",
        "user create Bob", 
        "user create Carol",
        "user create David",
        "user create Eve",
        "user interests 1 add chakras",
        "user interests 1 add meditation",
        "user interests 1 add consciousness",
        "user location 1 San_Francisco",
        "user skills 1 meditation advanced",
        "user skills 1 chakras intermediate",
        "user interests 2 add chakras",
        "user interests 2 add yoga",
        "user interests 2 add energy_healing",
        "user location 2 San_Francisco",
        "user skills 2 yoga expert",
        "user skills 2 energy_healing advanced",
        "user interests 3 add meditation",
        "user interests 3 add mindfulness",
        "user interests 3 add psychology",
        "user location 3 New_York",
        "user skills 3 mindfulness intermediate",
        "user skills 3 psychology advanced",
        "user interests 4 add quantum_physics",
        "user interests 4 add consciousness",
        "user interests 4 add meditation",
        "user location 4 Berkeley",
        "user skills 4 quantum_physics expert",
        "user skills 4 consciousness advanced",
        "user interests 5 add chakras",
        "user interests 5 add energy_healing",
        "user interests 5 add spirituality",
        "user location 5 Los_Angeles",
        "user skills 5 spirituality expert",
        "user skills 5 energy_healing intermediate",
        "user list",
        "discover_users chakras",
        "discover_users meditation",
        "discover_users consciousness",
        "discover_users_location chakras San_Francisco",
        "discover_users_location meditation San_Francisco",
        "discover_users_location consciousness Berkeley",
        "resonance_match 1 2",
        "resonance_match 1 3",
        "resonance_match 2 5",
        "resonance_match 3 4",
        "user profile 1",
        "user profile 2",
        "user profile 3"
    ]
    
    print("📋 Commands to run in the CLI:")
    print("-" * 40)
    for i, cmd in enumerate(commands, 1):
        print(f"{i:2d}. {cmd}")
    
    print()
    print("🎯 How to use these commands:")
    print()
    
    print("1️⃣  **User Creation & Management:**")
    print("   user create <username>")
    print("   user profile <id>")
    print("   user update <id> <field> <value>")
    print("   user list")
    print()
    
    print("2️⃣  **Interest Management:**")
    print("   user interests <id> add <topic>")
    print("   user interests <id> remove <topic>")
    print("   Examples: chakras, meditation, consciousness, yoga, quantum_physics")
    print()
    
    print("3️⃣  **Location & Skills:**")
    print("   user location <id> <location>")
    print("   user skills <id> <skill> <level>")
    print("   Skill levels: beginner, intermediate, advanced, expert")
    print()
    
    print("4️⃣  **User Discovery:**")
    print("   discover_users <topic>")
    print("   discover_users_location <topic> <location>")
    print("   Examples: discover_users chakras")
    print("   Examples: discover_users_location meditation San_Francisco")
    print()
    
    print("5️⃣  **Resonance Analysis:**")
    print("   resonance_match <user1_id> <user2_id>")
    print("   Calculates compatibility across interests, location, consciousness, and skills")
    print()
    
    print("🔍 **Example Workflow:**")
    print()
    print("1. Start the CLI: python codex_cli.py")
    print("2. Create users: user create Alice")
    print("3. Add interests: user interests 1 add chakras")
    print("4. Set location: user location 1 San_Francisco")
    print("5. Add skills: user skills 1 meditation advanced")
    print("6. Discover connections: discover_users chakras")
    print("7. Analyze resonance: resonance_match 1 2")
    print()
    
    print("🌟 **Key Features:**")
    print("   • Comprehensive user profiles with multiple dimensions")
    print("   • Interest-based discovery with match scoring")
    print("   • Location-aware user discovery")
    print("   • Multi-factor resonance analysis")
    print("   • Skill level tracking and compatibility")
    print("   • Consciousness and quantum state integration")
    print()
    
    print("🎯 **Discovery Scenarios:**")
    print()
    print("🔍 **Topic-Based Discovery:**")
    print("   • Find users interested in 'chakras'")
    print("   • Discover 'meditation' practitioners")
    print("   • Locate 'consciousness' researchers")
    print()
    print("🌍 **Location-Based Discovery:**")
    print("   • Find 'chakras' experts in 'San_Francisco'")
    print("   • Locate 'meditation' teachers in 'New_York'")
    print("   • Discover 'consciousness' researchers in 'Berkeley'")
    print()
    print("⚡ **Resonance Analysis:**")
    print("   • Interest compatibility (40% weight)")
    print("   • Location compatibility (20% weight)")
    print("   • Consciousness compatibility (20% weight)")
    print("   • Technical compatibility (20% weight)")
    print()
    
    print("🚀 **Ready to explore user connections in the Living Codex!**")
    print()
    print("Run: python codex_cli.py")
    print("Then try the commands above to see user management in action!")

if __name__ == "__main__":
    demo_user_management()
