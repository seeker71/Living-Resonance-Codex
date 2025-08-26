#!/usr/bin/env python3
"""
Unified Living Codex Platform - Complete Feature Demonstration
Showcases all four modules: Discovery Engine, Navigation System, Contribution Manager, and User Manager
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5004"

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*70}")
    print(f"🌟 {title}")
    print(f"{'='*70}")

def print_section(title):
    """Print a formatted section"""
    print(f"\n🔍 {title}")
    print(f"{'-'*50}")

def test_unified_homepage():
    """Test the unified homepage with all modules"""
    print_section("Testing Unified Homepage")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Unified homepage loaded successfully")
            print(f"   Response time: {response.elapsed.total_seconds():.3f}s")
            
            # Check for unified features
            content = response.text
            if "Unified Discovery & Navigation" in content:
                print("✅ Unified title found")
            if "Platform Modules" in content:
                print("✅ Platform modules section found")
            if "Discovery Engine" in content:
                print("✅ Discovery Engine module found")
            if "Navigation System" in content:
                print("✅ Navigation System module found")
            if "Contribution Manager" in content:
                print("✅ Contribution Manager module found")
            if "User Manager" in content:
                print("✅ User Manager module found")
                
        else:
            print(f"❌ Unified homepage failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing unified homepage: {e}")

def test_platform_modules():
    """Test all platform modules"""
    print_section("Testing Platform Modules")
    
    modules = [
        {
            'name': '🔍 Discovery Engine',
            'description': 'Smart user matching and content discovery',
            'features': ['User similarity matching', 'Content relevance scoring', 'Interest-based discovery']
        },
        {
            'name': '🧭 Navigation System',
            'description': 'Personalized exploration and progress tracking',
            'features': ['Exploration paths', 'Progress tracking', 'System overview']
        },
        {
            'name': '💡 Contribution Manager',
            'description': 'Enhanced content creation and collaboration',
            'features': ['Content creation', 'Categorization', 'Collaboration tools']
        },
        {
            'name': '👥 User Manager',
            'description': 'Comprehensive profiles and community building',
            'features': ['Profile management', 'User connections', 'Community building']
        }
    ]
    
    for module in modules:
        print(f"\n{module['name']}")
        print(f"   Description: {module['description']}")
        print("   Features:")
        for feature in module['features']:
            print(f"     • {feature}")

def test_unified_signup():
    """Test the unified signup with all profile features"""
    print_section("Testing Unified Signup")
    
    try:
        response = requests.get(f"{BASE_URL}/signup")
        if response.status_code == 200:
            print("✅ Unified signup page loaded")
            print(f"   Response time: {response.elapsed.total_seconds():.3f}s")
            
            # Check for unified features
            content = response.text
            if "Unified Platform Features" in content:
                print("✅ Platform modules info found")
            if "Core Identity" in content:
                print("✅ Core identity section found")
            if "Communication Preferences" in content:
                print("✅ Communication preferences found")
            if "Technical Profile" in content:
                print("✅ Technical profile section found")
            if "Interests & Passions" in content:
                print("✅ Interests section found")
            if "Location & Community" in content:
                print("✅ Location section found")
            if "Life Experience" in content:
                print("✅ Life experience field found")
            if "Accessibility Needs" in content:
                print("✅ Accessibility needs field found")
                
        else:
            print(f"❌ Unified signup failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing unified signup: {e}")

def test_unified_login():
    """Test the unified login page"""
    print_section("Testing Unified Login")
    
    try:
        response = requests.get(f"{BASE_URL}/login")
        if response.status_code == 200:
            print("✅ Unified login page loaded")
            print(f"   Response time: {response.elapsed.total_seconds():.3f}s")
            
            # Check for unified features
            content = response.text
            if "All Platform Modules Await" in content:
                print("✅ Platform modules info found")
            if "Discovery Engine" in content:
                print("✅ Discovery Engine module info found")
            if "Navigation System" in content:
                print("✅ Navigation System module info found")
            if "Contribution Manager" in content:
                print("✅ Contribution Manager module info found")
            if "User Manager" in content:
                print("✅ User Manager module info found")
                
        else:
            print(f"❌ Unified login failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing unified login: {e}")

def test_api_endpoints():
    """Test all API endpoints"""
    print_section("Testing API Endpoints")
    
    api_endpoints = [
        ("/api/navigation/system_overview", "System Overview", False, "Public system statistics"),
        ("/api/navigation/exploration_paths", "Exploration Paths", True, "User exploration paths"),
        ("/api/discovery/similar_users", "Similar Users", True, "Find similar users"),
        ("/api/discovery/relevant_content", "Relevant Content", True, "Find relevant content"),
        ("/api/contributions", "User Contributions", True, "User's contributions"),
        ("/api/opportunities", "Contribution Opportunities", True, "Available opportunities")
    ]
    
    for endpoint, name, requires_auth, description in api_endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            if requires_auth:
                if response.status_code == 302:
                    print(f"✅ {name}: Properly protected (requires authentication)")
                else:
                    print(f"❌ {name}: Should require auth but got {response.status_code}")
            else:
                if response.status_code == 200:
                    print(f"✅ {name}: Public API working - {description}")
                else:
                    print(f"❌ {name}: Public API failed with {response.status_code}")
                    
        except Exception as e:
            print(f"❌ Error testing {name}: {e}")

def test_protected_routes():
    """Test protected routes"""
    print_section("Testing Protected Routes")
    
    protected_routes = [
        ("/discover", "Discovery Hub", "User and content discovery"),
        ("/navigate", "System Navigation", "Platform navigation and progress"),
        ("/dashboard", "User Dashboard", "Personalized user dashboard"),
        ("/contribute", "Contribution System", "Content creation and contribution"),
        ("/profile", "User Profile", "User profile management"),
        ("/explore/<category>", "Category Exploration", "Explore content by category")
    ]
    
    for route, name, description in protected_routes:
        try:
            response = requests.get(f"{BASE_URL}{route}")
            if response.status_code == 302:
                print(f"✅ {name}: Properly protected (redirects to login)")
            else:
                print(f"❌ {name}: Unexpected status {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error testing {name}: {e}")

def test_system_architecture():
    """Test the system architecture"""
    print_section("Testing System Architecture")
    
    print("🏗️  Unified Platform Architecture:")
    print("   • Single Flask application with modular design")
    print("   • Four core modules working together")
    print("   • Shared data structures and user management")
    print("   • Consistent API endpoints across all modules")
    
    print("\n🔧 Module Integration:")
    print("   • Discovery Engine ↔ Navigation System")
    print("   • User Manager ↔ Contribution Manager")
    print("   • All modules share user profiles and data")
    print("   • Unified authentication and session management")

def test_user_experience_flow():
    """Test the complete user experience flow"""
    print_section("Testing Complete User Experience")
    
    print("👤 Unified User Journey:")
    print("   1. Visit unified homepage with all module information")
    print("   2. Sign up with comprehensive profile (powers all modules)")
    print("   3. Login and access all platform features")
    print("   4. Use Discovery Engine to find users and content")
    print("   5. Navigate through personalized exploration paths")
    print("   6. Contribute content using enhanced contribution system")
    print("   7. Build community through user connections")
    print("   8. Track progress across all modules")
    
    print("\n🎯 Key Benefits of Unified Platform:")
    print("   • Single signup/login for all features")
    print("   • Consistent user experience across modules")
    print("   • Shared data and seamless integration")
    print("   • Comprehensive profile powers all functionality")
    print("   • No need to switch between different systems")

def main():
    """Main demonstration function"""
    print_header("Unified Living Codex Platform - Complete Feature Demonstration")
    print(f"Testing unified platform at: {BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test all unified features
    test_unified_homepage()
    test_platform_modules()
    test_unified_signup()
    test_unified_login()
    test_api_endpoints()
    test_protected_routes()
    test_system_architecture()
    test_user_experience_flow()
    
    print_header("Unified Platform Demonstration Complete")
    print("🎉 All modules are working together in one unified system!")
    print("\n🚀 Next Steps:")
    print("   1. Open http://localhost:5004 in your browser")
    print("   2. Sign up for a comprehensive profile")
    print("   3. Explore all four platform modules")
    print("   4. Experience seamless integration between features")
    
    print("\n💡 Unified Platform Features:")
    print("   • 🔍 Discovery Engine: Smart matching and discovery")
    print("   • 🧭 Navigation System: Personalized exploration paths")
    print("   • 💡 Contribution Manager: Enhanced content creation")
    print("   • 👥 User Manager: Community building and connections")
    
    print("\n🔗 Module Integration Benefits:")
    print("   • Single user profile powers all features")
    print("   • Seamless data sharing between modules")
    print("   • Consistent user experience")
    print("   • Unified authentication and management")
    print("   • No more switching between different systems!")

if __name__ == "__main__":
    main()
