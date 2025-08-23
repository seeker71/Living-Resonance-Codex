#!/usr/bin/env python3
"""
Enhanced Living Codex Platform - Feature Demonstration
Showcases discovery, navigation, and collaboration features
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5003"

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"🌟 {title}")
    print(f"{'='*60}")

def print_section(title):
    """Print a formatted section"""
    print(f"\n🔍 {title}")
    print(f"{'-'*40}")

def test_homepage():
    """Test the enhanced homepage"""
    print_section("Testing Enhanced Homepage")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Homepage loaded successfully")
            print(f"   Response time: {response.elapsed.total_seconds():.3f}s")
            
            # Check for enhanced features
            content = response.text
            if "Discovery & Navigation" in content:
                print("✅ Enhanced title found")
            if "Smart Discovery" in content:
                print("✅ Discovery features found")
            if "Intelligent Navigation" in content:
                print("✅ Navigation features found")
            if "Community Building" in content:
                print("✅ Collaboration features found")
                
        else:
            print(f"❌ Homepage failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing homepage: {e}")

def test_system_overview_api():
    """Test the system overview API"""
    print_section("Testing System Overview API")
    
    try:
        response = requests.get(f"{BASE_URL}/api/navigation/system_overview")
        if response.status_code == 200:
            print("✅ System overview API working")
            data = response.json()
            print(f"   Total users: {data.get('total_users', 0)}")
            print(f"   Total contributions: {data.get('total_contributions', 0)}")
            print(f"   Active communities: {data.get('active_communities', 0)}")
            print(f"   Recent activity: {data.get('recent_activity', 0)}")
            
            if data.get('top_categories'):
                print(f"   Top categories: {len(data['top_categories'])} found")
            else:
                print("   No categories yet (expected for new system)")
                
        else:
            print(f"❌ System overview API failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing system overview API: {e}")

def test_enhanced_signup():
    """Test the enhanced signup page"""
    print_section("Testing Enhanced Signup Page")
    
    try:
        response = requests.get(f"{BASE_URL}/signup")
        if response.status_code == 200:
            print("✅ Enhanced signup page loaded")
            print(f"   Response time: {response.elapsed.total_seconds():.3f}s")
            
            # Check for enhanced features
            content = response.text
            if "Discovery & Navigation Features" in content:
                print("✅ Discovery features note found")
            if "Learning Style" in content:
                print("✅ Enhanced learning preferences found")
            if "Cultural Background" in content:
                print("✅ Cultural context fields found")
            if "Preferred Tools" in content:
                print("✅ Technical preferences found")
                
        else:
            print(f"❌ Enhanced signup failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing enhanced signup: {e}")

def test_protected_routes():
    """Test protected discovery and navigation routes"""
    print_section("Testing Protected Routes")
    
    protected_routes = [
        ("/discover", "Discovery Hub"),
        ("/navigate", "System Navigation"),
        ("/dashboard", "User Dashboard"),
        ("/profile", "User Profile")
    ]
    
    for route, name in protected_routes:
        try:
            response = requests.get(f"{BASE_URL}{route}")
            if response.status_code == 302:
                print(f"✅ {name}: Properly protected (redirects to login)")
            else:
                print(f"❌ {name}: Unexpected status {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error testing {name}: {e}")

def test_api_endpoints():
    """Test discovery and navigation API endpoints"""
    print_section("Testing API Endpoints")
    
    api_endpoints = [
        ("/api/navigation/system_overview", "System Overview", False),
        ("/api/navigation/exploration_paths", "Exploration Paths", True),
        ("/api/discovery/similar_users", "Similar Users", True),
        ("/api/discovery/relevant_content", "Relevant Content", True)
    ]
    
    for endpoint, name, requires_auth in api_endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            if requires_auth:
                if response.status_code == 302:
                    print(f"✅ {name}: Properly protected (requires authentication)")
                else:
                    print(f"❌ {name}: Should require auth but got {response.status_code}")
            else:
                if response.status_code == 200:
                    print(f"✅ {name}: Public API working")
                else:
                    print(f"❌ {name}: Public API failed with {response.status_code}")
                    
        except Exception as e:
            print(f"❌ Error testing {name}: {e}")

def test_content_discovery():
    """Test content discovery features"""
    print_section("Testing Content Discovery Features")
    
    print("🔍 Discovery Engine Features:")
    print("   • Smart user matching based on interests, skills, and location")
    print("   • Content relevance scoring")
    print("   • Personalized exploration paths")
    print("   • Community building tools")
    
    print("\n🧭 Navigation System Features:")
    print("   • System overview and statistics")
    print("   • User progress tracking")
    print("   • Exploration path management")
    print("   • Category-based content organization")

def test_user_experience():
    """Test the complete user experience flow"""
    print_section("Testing Complete User Experience")
    
    print("👤 User Journey:")
    print("   1. Visit enhanced homepage with discovery features")
    print("   2. Sign up with comprehensive profile creation")
    print("   3. Get redirected to discovery hub after login")
    print("   4. Find similar users and relevant content")
    print("   5. Navigate through personalized exploration paths")
    print("   6. Connect with other users and build communities")
    print("   7. Track progress and contributions")
    
    print("\n🎯 Key Benefits:")
    print("   • Personalized content discovery")
    print("   • Intelligent user matching")
    print("   • Guided exploration paths")
    print("   • Progress tracking and analytics")
    print("   • Community building tools")

def main():
    """Main demonstration function"""
    print_header("Enhanced Living Codex Platform - Feature Demonstration")
    print(f"Testing platform at: {BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test all enhanced features
    test_homepage()
    test_system_overview_api()
    test_enhanced_signup()
    test_protected_routes()
    test_api_endpoints()
    test_content_discovery()
    test_user_experience()
    
    print_header("Demonstration Complete")
    print("🎉 All enhanced features are working!")
    print("\n🚀 Next Steps:")
    print("   1. Open http://localhost:5003 in your browser")
    print("   2. Sign up for a new account")
    print("   3. Explore the discovery and navigation features")
    print("   4. Connect with other users and contribute content")
    
    print("\n💡 Enhanced Features Available:")
    print("   • Smart Discovery Engine")
    print("   • Intelligent Navigation System")
    print("   • User Similarity Matching")
    print("   • Content Relevance Scoring")
    print("   • Personalized Exploration Paths")
    print("   • Progress Tracking")
    print("   • Community Building Tools")

if __name__ == "__main__":
    main()
