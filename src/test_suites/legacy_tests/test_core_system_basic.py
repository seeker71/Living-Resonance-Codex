#!/usr/bin/env python3
"""
Basic Core System Test
Tests the core system APIs without needing the web server
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

def test_core_system_apis():
    """Test the core system APIs directly"""
    
    print("🧪 Testing Core System APIs Directly")
    print("=" * 50)
    
    try:
        # Test user management system
        print("\n1️⃣ Testing User Management System...")
        from web_platform.user_management import UserManagementSystem, UserProfile
        
        user_system = UserManagementSystem()
        print("   ✅ UserManagementSystem imported and instantiated")
        
        # Test contribution system
        print("\n2️⃣ Testing Contribution System...")
        from web_platform.contribution_system import ContributionSystem, ContributionType
        
        contribution_system = ContributionSystem()
        print("   ✅ ContributionSystem imported and instantiated")
        
        # Test creating a user profile
        print("\n3️⃣ Testing User Profile Creation...")
        test_user_data = {
            'identity': {
                'name': 'Test User',
                'pronouns': 'they/them',
                'cultural_background': 'Test',
                'belief_system': 'Test',
                'life_experience': 'Test'
            },
            'communication': {
                'primary_language': 'English',
                'secondary_languages': [],
                'communication_style': 'casual',
                'learning_style': 'visual'
            },
            'technical': {
                'skill_levels': {
                    'programming': 'beginner'
                },
                'preferred_tools': ['Python'],
                'contribution_areas': ['testing']
            },
            'interests': {
                'primary_domains': ['testing'],
                'specific_topics': ['Python Testing'],
                'expertise_levels': {
                    'Python': 'beginner'
                }
            },
            'location': {
                'geographic_location': 'Test',
                'timezone': 'UTC',
                'cultural_context': 'Test'
            }
        }
        
        # Fix the enum values
        from web_platform.user_management import CommunicationStyle, LearningStyle, SkillLevel
        
        test_user_data['communication']['communication_style'] = CommunicationStyle.CASUAL
        test_user_data['communication']['learning_style'] = LearningStyle.VISUAL
        test_user_data['technical']['skill_levels']['programming'] = SkillLevel.BEGINNER
        test_user_data['interests']['expertise_levels']['Python'] = SkillLevel.BEGINNER
        
        user_profile = user_system.create_user_profile(test_user_data)
        if user_profile:
            print(f"   ✅ Test user profile created with ID: {user_profile.user_id}")
        else:
            print("   ❌ Failed to create test user profile")
            return False
        
        # Test creating a contribution
        print("\n4️⃣ Testing Contribution Creation...")
        test_contribution_data = {
            'contribution_type': 'code',
            'metadata': {
                'title': 'Test Contribution',
                'description': 'A test contribution for testing purposes',
                'tags': ['test', 'python'],
                'language': 'en',
                'skill_level': 'beginner'
            },
            'code_content': {
                'code_content': 'print("Hello, World!")',
                'language': 'python',
                'dependencies': []
            }
        }
        
        contribution = contribution_system.create_contribution(user_profile.user_id, test_contribution_data)
        if contribution:
            print(f"   ✅ Test contribution created with ID: {contribution.contribution_id}")
        else:
            print("   ❌ Failed to create test contribution")
            return False
        
        # Test retrieving data
        print("\n5️⃣ Testing Data Retrieval...")
        
        # Get all profiles
        all_profiles = user_system.profile_manager.get_all_profiles()
        print(f"   ✅ Retrieved {len(all_profiles)} user profiles")
        
        # Get all contributions
        all_contributions = contribution_system.contribution_manager.get_all_contributions()
        print(f"   ✅ Retrieved {len(all_contributions)} contributions")
        
        # Get specific user profile
        retrieved_profile = user_system.profile_manager.get_profile(user_profile.user_id)
        if retrieved_profile:
            print(f"   ✅ Retrieved user profile: {retrieved_profile.core_identity.name}")
        else:
            print("   ❌ Failed to retrieve user profile")
            return False
        
        # Get user contributions
        user_contributions = contribution_system.get_user_contributions(user_profile.user_id)
        print(f"   ✅ Retrieved {len(user_contributions)} contributions for user")
        
        print("\n" + "=" * 50)
        print("🎉 ALL CORE SYSTEM API TESTS PASSED!")
        print("   The core system is working correctly.")
        print("   User profiles and contributions can be created and retrieved.")
        print("   The web interface should work with these APIs.")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("🚀 Starting Basic Core System Test...")
    print("   Testing core system APIs without web server")
    print()
    
    success = test_core_system_apis()
    
    if success:
        print("\n✅ BASIC CORE SYSTEM TEST PASSED")
        print("   The core system APIs are working correctly.")
        print("   Next step: Test the web interface navigation.")
    else:
        print("\n❌ BASIC CORE SYSTEM TEST FAILED")
        print("   There are issues with the core system APIs.")
        print("   Fix these before testing the web interface.")

if __name__ == "__main__":
    main()
