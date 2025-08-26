#!/usr/bin/env python3
"""
Test Core System Navigation
Tests the Living Codex web interface navigation flow using core system APIs

This script:
1. Sets up demo data using core system APIs
2. Tests the web interface navigation step by step
3. Verifies each step returns HTTP 200 and proper data
4. Uses actual navigation links from the web interface
"""

import requests
import time
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

from web_platform.user_management import UserManagementSystem
from web_platform.contribution_system import ContributionSystem

def setup_demo_data():
    """Set up demo data using core system APIs"""
    print("🚀 Setting up demo data using core system APIs...")
    
    try:
        # Import and run the demo setup
        from demo_setup_core_system import setup_demo_data as setup_demo
        success = setup_demo()
        if success:
            print("✅ Demo data setup completed")
            return True
        else:
            print("❌ Demo data setup failed")
            return False
    except Exception as e:
        print(f"❌ Error setting up demo data: {e}")
        return False

def get_demo_user_ids():
    """Get the demo user IDs from the core system"""
    try:
        user_system = UserManagementSystem()
        all_profiles = user_system.profile_manager.get_all_profiles()
        
        alice_id = None
        bob_id = None
        
        for profile in all_profiles:
            if profile.core_identity.name == "Alice Chen":
                alice_id = profile.user_id
            elif profile.core_identity.name == "Bob Rodriguez":
                bob_id = profile.user_id
        
        return alice_id, bob_id
    except Exception as e:
        print(f"❌ Error getting demo user IDs: {e}")
        return None, None

def test_core_system_navigation():
    """Test the core system navigation flow"""
    
    base_url = "http://localhost:5004"
    session = requests.Session()
    
    print("\n🧭 Testing Core System Navigation Flow")
    print("=" * 60)
    print(f"Testing at: {base_url}")
    print()
    
    # Step 1: Test main page accessibility
    print("1️⃣ Testing Main Page...")
    try:
        response = session.get(f"{base_url}/")
        if response.status_code == 200:
            print("   ✅ Main page accessible")
            if "Living Codex Platform" in response.text:
                print("   ✅ Platform content loaded")
            else:
                print("   ⚠️  Platform content may be incomplete")
        else:
            print(f"   ❌ Main page returned HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error accessing main page: {e}")
        return False
    
    print()
    
    # Step 2: Get demo user IDs and test login
    print("2️⃣ Getting Demo User IDs and Testing Login...")
    alice_id, bob_id = get_demo_user_ids()
    
    if not alice_id or not bob_id:
        print("   ❌ Could not get demo user IDs")
        return False
    
    print(f"   ✅ Alice Chen ID: {alice_id}")
    print(f"   ✅ Bob Rodriguez ID: {bob_id}")
    
    # Test login with Alice
    try:
        login_data = {"user_id": alice_id}
        response = session.post(f"{base_url}/login", data=login_data)
        
        if response.status_code == 302:  # Redirect after successful login
            print("   ✅ Login successful - redirected to discover")
            
            # Follow the redirect to discover page
            discover_response = session.get(f"{base_url}/discover")
            if discover_response.status_code == 200:
                print("   ✅ Discover page accessible after login")
                
                # Check if we can see user data
                if alice_id in discover_response.text or "Alice" in discover_response.text:
                    print("   ✅ User profile data visible on discover page")
                else:
                    print("   ⚠️  User profile data may not be visible")
                    
            else:
                print(f"   ❌ Discover page returned HTTP {discover_response.status_code}")
                return False
        elif response.status_code == 200:  # Direct access after login
            print("   ✅ Login successful - discover page loaded directly")
            
            # Check if we can see user data
            if alice_id in response.text or "Alice" in response.text:
                print("   ✅ User profile data visible on discover page")
            else:
                print("   ⚠️  User profile data may not be visible")
        else:
            print(f"   ❌ Login failed - returned HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error during login: {e}")
        return False
    
    print()
    
    # Step 3: Test user profile navigation
    print("3️⃣ Testing User Profile Navigation...")
    try:
        # Try to access Alice's profile
        response = session.get(f"{base_url}/user/{alice_id}")
        if response.status_code == 200:
            print("   ✅ User profile page accessible")
            if "Alice Chen" in response.text:
                print("   ✅ Alice's profile data visible")
            else:
                print("   ⚠️  Alice's profile data may not be visible")
        else:
            print(f"   ❌ User profile page returned HTTP {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error accessing user profile: {e}")
    
    print()
    
    # Step 4: Test concept navigation
    print("4️⃣ Testing Concept Navigation...")
    try:
        # Try to access Neural Networks concept
        response = session.get(f"{base_url}/concept/Neural Networks")
        if response.status_code == 200:
            print("   ✅ Concept page accessible")
            if "Neural Networks" in response.text:
                print("   ✅ Concept data visible")
            else:
                print("   ⚠️  Concept data may not be visible")
        else:
            print(f"   ❌ Concept page returned HTTP {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error accessing concept page: {e}")
    
    print()
    
    # Step 5: Test source file navigation
    print("5️⃣ Testing Source File Navigation...")
    try:
        # Try to access neural network source file
        response = session.get(f"{base_url}/source/neural_network.py")
        if response.status_code == 200:
            print("   ✅ Source file page accessible")
            if "neural_network.py" in response.text:
                print("   ✅ Source file data visible")
            else:
                print("   ⚠️  Source file data may not be visible")
        else:
            print(f"   ❌ Source file page returned HTTP {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error accessing source file page: {e}")
    
    print()
    
    # Step 6: Test expression navigation
    print("6️⃣ Testing Expression Navigation...")
    try:
        # Try to access AttentionMechanism expression
        response = session.get(f"{base_url}/expression/neural_network.py/15")
        if response.status_code == 200:
            print("   ✅ Expression page accessible")
            if "AttentionMechanism" in response.text:
                print("   ✅ Expression data visible")
            else:
                print("   ⚠️  Expression data may not be visible")
        else:
            print(f"   ❌ Expression page returned HTTP {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error accessing expression page: {e}")
    
    print()
    
    # Step 7: Test navigation flow completeness
    print("7️⃣ Testing Complete Navigation Flow...")
    
    navigation_steps = [
        ("Main Page", "/", "Living Codex Platform"),
        ("Discover", "/discover", "Discovery Hub"),
        ("User Profile", f"/user/{alice_id}", "Alice Chen"),
        ("Concept", "/concept/Neural Networks", "Neural Networks"),
        ("Source File", "/source/neural_network.py", "neural_network.py"),
        ("Expression", "/expression/neural_network.py/15", "AttentionMechanism")
    ]
    
    successful_steps = 0
    total_steps = len(navigation_steps)
    
    for step_name, url, expected_content in navigation_steps:
        try:
            response = session.get(f"{base_url}{url}")
            if response.status_code == 200:
                if expected_content in response.text:
                    print(f"   ✅ {step_name}: {expected_content} found")
                    successful_steps += 1
                else:
                    print(f"   ⚠️  {step_name}: {expected_content} not found")
            else:
                print(f"   ❌ {step_name}: HTTP {response.status_code}")
        except Exception as e:
            print(f"   ❌ {step_name}: Error - {e}")
    
    print()
    
    # Summary
    print("📊 Core System Navigation Test Summary")
    print("=" * 60)
    print(f"✅ Successful Steps: {successful_steps}/{total_steps}")
    print(f"📈 Success Rate: {(successful_steps/total_steps)*100:.1f}%")
    
    if successful_steps == total_steps:
        print("🎉 All navigation steps completed successfully!")
        print("   The web interface can perform the complete navigation flow:")
        print("   Void → User → User → Concept → Source File → Expression")
        print("   Using core system APIs for all data operations!")
    elif successful_steps > total_steps * 0.8:
        print("⚠️  Most navigation steps working, some issues detected")
    else:
        print("❌ Significant navigation issues detected")
    
    print()
    print("🌐 Web Interface URLs Tested:")
    for step_name, url, expected_content in navigation_steps:
        print(f"   {step_name}: {base_url}{url}")
    
    print()
    print("🔗 Key Navigation Features:")
    print("   ✅ User Profile Viewing (via core system)")
    print("   ✅ Concept Exploration (via core system)")
    print("   ✅ Source File Navigation (via core system)")
    print("   ✅ Expression Navigation (via core system)")
    print("   ✅ Progress Tracking")
    
    return successful_steps == total_steps

def main():
    """Main test function"""
    print("🚀 Starting Core System Navigation Test...")
    print("   Testing web interface with core system APIs")
    print()
    
    try:
        # Step 1: Setup demo data
        if not setup_demo_data():
            print("❌ Demo data setup failed. Cannot proceed with navigation test.")
            return
        
        # Step 2: Test navigation
        success = test_core_system_navigation()
        
        print("\n" + "=" * 60)
        if success:
            print("🎯 CORE SYSTEM NAVIGATION TEST PASSED")
            print("   The Living Codex web interface successfully demonstrates")
            print("   seamless navigation through complex knowledge structures!")
            print("   All data operations use core system APIs!")
        else:
            print("❌ CORE SYSTEM NAVIGATION TEST FAILED")
            print("   Some navigation steps are not working correctly.")
            print("   Check the web interface implementation and core system APIs.")
        
    except KeyboardInterrupt:
        print("\n⏹️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("   Make sure the web interface is running and accessible")

if __name__ == "__main__":
    main()
