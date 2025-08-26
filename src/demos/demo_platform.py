#!/usr/bin/env python3
"""
Living Codex Platform Demo
Demonstrates the platform's user management and contribution systems
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from platform.user_management import (
    UserManagementSystem, SkillLevel, CommunicationStyle, LearningStyle
)
from platform.contribution_system import (
    ContributionSystem, ContributionType, ContentCategory
)

def demo_user_profiles():
    """Demonstrate user profile creation and management"""
    print("🌟 Living Codex Platform Demo")
    print("=" * 50)
    
    # Create user management system
    user_system = UserManagementSystem()
    
    # Example user 1: Technical expert
    print("\n👤 Creating User Profile: Alex Chen (Technical Expert)")
    alex_data = {
        'identity': {
            'name': 'Alex Chen',
            'pronouns': 'they/them',
            'cultural_background': 'Chinese-American',
            'belief_system': 'Humanist',
            'life_experience': 'Community organizer and software developer'
        },
        'communication': {
            'primary_language': 'English',
            'secondary_languages': ['Mandarin', 'Spanish'],
            'communication_style': CommunicationStyle.CASUAL,
            'learning_style': LearningStyle.VISUAL,
            'accessibility_needs': ['High contrast', 'Screen reader support']
        },
        'technical': {
            'skill_levels': {
                'programming': SkillLevel.EXPERT,
                'data_analysis': SkillLevel.ADVANCED,
                'design': SkillLevel.INTERMEDIATE,
                'research': SkillLevel.ADVANCED
            },
            'learning_path': ['UI/UX Design', 'Machine Learning'],
            'preferred_tools': ['Python', 'React', 'TensorFlow'],
            'contribution_areas': ['Code', 'Documentation', 'Community Building']
        },
        'interests': {
            'primary_domains': ['Technology', 'Social Justice', 'Community Building'],
            'specific_topics': ['AI Ethics', 'Climate Change', 'Digital Inclusion'],
            'expertise_levels': {
                'community_organizing': SkillLevel.EXPERT,
                'software_development': SkillLevel.EXPERT,
                'climate_science': SkillLevel.INTERMEDIATE
            },
            'passion_areas': ['Making technology accessible to everyone']
        },
        'location': {
            'geographic_location': 'San Francisco, CA, USA',
            'timezone': 'America/Los_Angeles',
            'cultural_context': 'Diverse urban community with strong tech culture',
            'community_connections': ['Local tech meetups', 'Climate action groups'],
            'local_challenges': ['Housing affordability', 'Digital divide'],
            'local_resources': ['Tech companies', 'Universities', 'Community centers']
        }
    }
    
    alex_profile = user_system.create_user_profile(alex_data)
    if alex_profile:
        print(f"✅ Created profile for {alex_profile.core_identity.name}")
        print(f"   User ID: {alex_profile.user_id}")
        print(f"   Location: {alex_profile.location_context.geographic_location}")
        print(f"   Skills: {list(alex_profile.technical_profile.skill_levels.keys())}")
        
        # Get personalized experience
        experience = user_system.get_personalized_experience(alex_profile.user_id)
        if experience:
            print(f"\n🎯 Personalized Experience for Alex:")
            print(f"   Focus Area: {experience['learning_path']['focus_area']}")
            print(f"   Learning Style: {experience['learning_path']['learning_style']}")
            print(f"   Recommendations: {experience['recommendations'][:3]}")
            print(f"   Collaboration Opportunities: {len(experience['collaboration_opportunities'])}")
    else:
        print("❌ Failed to create Alex's profile")
        return None
    
    # Example user 2: Community organizer
    print("\n👤 Creating User Profile: Maria Rodriguez (Community Organizer)")
    maria_data = {
        'identity': {
            'name': 'Maria Rodriguez',
            'pronouns': 'she/her',
            'cultural_background': 'Mexican-American',
            'belief_system': 'Community-focused',
            'life_experience': 'Community organizer and educator'
        },
        'communication': {
            'primary_language': 'Spanish',
            'secondary_languages': ['English'],
            'communication_style': CommunicationStyle.CREATIVE,
            'learning_style': LearningStyle.KINESTHETIC,
            'accessibility_needs': []
        },
        'technical': {
            'skill_levels': {
                'programming': SkillLevel.BEGINNER,
                'data_analysis': SkillLevel.BEGINNER,
                'design': SkillLevel.INTERMEDIATE,
                'research': SkillLevel.ADVANCED
            },
            'learning_path': ['Digital Tools', 'Data Visualization'],
            'preferred_tools': ['Canva', 'Google Workspace'],
            'contribution_areas': ['Community Solutions', 'Education', 'Local Knowledge']
        },
        'interests': {
            'primary_domains': ['Community Building', 'Education', 'Social Justice'],
            'specific_topics': ['Youth Empowerment', 'Food Security', 'Cultural Preservation'],
            'expertise_levels': {
                'community_organizing': SkillLevel.EXPERT,
                'youth_education': SkillLevel.EXPERT,
                'cultural_programs': SkillLevel.ADVANCED
            },
            'passion_areas': ['Building strong, resilient communities']
        },
        'location': {
            'geographic_location': 'Los Angeles, CA, USA',
            'timezone': 'America/Los_Angeles',
            'cultural_context': 'Large Latino community with rich cultural heritage',
            'community_connections': ['Local schools', 'Community centers', 'Cultural organizations'],
            'local_challenges': ['Food insecurity', 'Language barriers', 'Digital access'],
            'local_resources': ['Community gardens', 'Bilingual services', 'Cultural centers']
        }
    }
    
    maria_profile = user_system.create_user_profile(maria_data)
    if maria_profile:
        print(f"✅ Created profile for {maria_profile.core_identity.name}")
        print(f"   User ID: {maria_profile.user_id}")
        print(f"   Location: {maria_profile.location_context.geographic_location}")
        print(f"   Skills: {list(maria_profile.technical_profile.skill_levels.keys())}")
        
        # Get personalized experience
        experience = user_system.get_personalized_experience(maria_profile.user_id)
        if experience:
            print(f"\n🎯 Personalized Experience for Maria:")
            print(f"   Focus Area: {experience['learning_path']['focus_area']}")
            print(f"   Learning Style: {experience['learning_path']['learning_style']}")
            print(f"   Recommendations: {experience['recommendations'][:3]}")
            print(f"   Collaboration Opportunities: {len(experience['collaboration_opportunities'])}")
    else:
        print("❌ Failed to create Maria's profile")
        return None
    
    return alex_profile, maria_profile

def demo_contributions(alex_profile, maria_profile):
    """Demonstrate contribution creation and matching"""
    print("\n🚀 Contribution System Demo")
    print("=" * 50)
    
    # Create contribution system
    contribution_system = ContributionSystem()
    
    # Alex creates a technical contribution
    print("\n💻 Alex creates a code contribution:")
    alex_code_data = {
        'contribution_type': 'code',
        'metadata': {
            'title': 'Accessible Web Development Guide',
            'description': 'A comprehensive guide to making websites accessible to everyone',
            'tags': ['accessibility', 'web-development', 'inclusion'],
            'language': 'en',
            'skill_level': 'intermediate',
            'target_audience': ['developers', 'designers', 'accessibility advocates']
        },
        'code_content': {
            'code_content': 'function makeAccessible(element) {\n  // Add ARIA labels\n  element.setAttribute("aria-label", "Description");\n}',
            'language': 'javascript',
            'framework': 'Vanilla JS',
            'dependencies': [],
            'documentation': 'This function adds accessibility features to web elements'
        }
    }
    
    alex_code = contribution_system.create_contribution(alex_profile.user_id, alex_code_data)
    if alex_code:
        print(f"✅ Created: {alex_code.metadata.title}")
        print(f"   Type: {alex_code.contribution_type.value}")
        print(f"   Status: {alex_code.status.value}")
        print(f"   Tags: {', '.join(alex_code.metadata.tags)}")
    
    # Maria creates a local solution contribution
    print("\n🌍 Maria creates a local solution contribution:")
    maria_solution_data = {
        'contribution_type': 'local_solution',
        'metadata': {
            'title': 'Community Garden Food Security Program',
            'description': 'How we organized a community garden to address food insecurity in our neighborhood',
            'tags': ['food-security', 'community-gardens', 'local-solutions'],
            'language': 'en',
            'skill_level': 'beginner',
            'target_audience': ['community organizers', 'neighborhood groups', 'local government']
        },
        'local_solution_data': {
            'problem_description': 'Many families in our neighborhood struggle with food insecurity and lack access to fresh produce',
            'solution_approach': 'Organized a community garden program where residents can grow and share food',
            'local_context': 'Urban neighborhood with limited green space and high food insecurity rates',
            'community_involvement': '50+ families participate, rotating garden maintenance and harvest sharing',
            'success_metrics': ['Reduced food insecurity by 30%', 'Increased community engagement', 'Created 20 new garden plots'],
            'challenges_faced': ['Limited space', 'Water access', 'Coordinating schedules'],
            'lessons_learned': 'Start small, involve everyone, celebrate successes together'
        }
    }
    
    maria_solution = contribution_system.create_contribution(maria_profile.user_id, maria_solution_data)
    if maria_solution:
        print(f"✅ Created: {maria_solution.metadata.title}")
        print(f"   Type: {maria_solution.contribution_type.value}")
        print(f"   Status: {maria_solution.status.value}")
        print(f"   Tags: {', '.join(maria_solution.metadata.tags)}")
    
    # Find contribution opportunities for both users
    print("\n🔍 Finding contribution opportunities:")
    
    alex_opportunities = contribution_system.find_opportunities(alex_profile)
    print(f"\nAlex's opportunities ({len(alex_opportunities)}):")
    for opp in alex_opportunities[:3]:
        print(f"   • {opp['area']}: {opp['description']} (Priority: {opp['priority']})")
    
    maria_opportunities = contribution_system.find_opportunities(maria_profile)
    print(f"\nMaria's opportunities ({len(maria_opportunities)}):")
    for opp in maria_opportunities[:3]:
        print(f"   • {opp['area']}: {opp['description']} (Priority: {opp['priority']})")
    
    # Show all contributions
    print("\n📚 All contributions in the system:")
    all_contributions = contribution_system.get_contributions_by_type(ContributionType.CODE) + \
                       contribution_system.get_contributions_by_type(ContributionType.LOCAL_SOLUTION)
    
    for contrib in all_contributions:
        print(f"   • {contrib.metadata.title} by {contrib.user_id} ({contrib.contribution_type.value})")

def demo_personalization():
    """Demonstrate how the system personalizes experiences"""
    print("\n🎨 Personalization Demo")
    print("=" * 50)
    
    # This would show how different users see different content
    # based on their profiles, but we'll keep it simple for now
    print("The system automatically personalizes each user's experience based on:")
    print("   • Their technical skill level")
    print("   • Their interests and passions")
    print("   • Their geographic location")
    print("   • Their cultural context")
    print("   • Their learning style")
    print("   • Their current session focus")
    
    print("\nEach user sees:")
    print("   • Content filtered to their skill level")
    print("   • Recommendations based on their interests")
    print("   • Local solutions relevant to their area")
    print("   • Collaboration opportunities matching their expertise")
    print("   • Learning paths adapted to their style")

def main():
    """Run the complete platform demo"""
    try:
        # Demo user profiles
        profiles = demo_user_profiles()
        if not profiles:
            print("❌ Demo failed - could not create user profiles")
            return
        
        alex_profile, maria_profile = profiles
        
        # Demo contributions
        demo_contributions(alex_profile, maria_profile)
        
        # Demo personalization
        demo_personalization()
        
        print("\n🎉 Platform Demo Complete!")
        print("\nWhat you've seen:")
        print("   ✅ User profile creation with complex personal data")
        print("   ✅ Personalized experience generation")
        print("   ✅ Contribution creation and management")
        print("   ✅ Opportunity matching based on user profiles")
        print("   ✅ Water state metaphor in action (liquid preferences, vapor sessions)")
        
        print("\nNext steps:")
        print("   • Run the web interface: python src/web_platform/web_interface.py")
        print("   • Sign up users through the web interface")
        print("   • Create contributions and see personalization in action")
        print("   • Explore the API endpoints for integration")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
