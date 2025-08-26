#!/usr/bin/env python3
"""
Demo Setup for Core System
Sets up demo data using the core system APIs for the Living Codex web interface
"""

import sys
import os
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

from web_platform.user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle
)
from web_platform.contribution_system import (
    ContributionSystem, ContributionType, ContentCategory, ContributionStatus,
    Contribution, ContributionMetadata, CodeContribution
)

def setup_demo_data():
    """Set up demo data using the core system APIs"""
    
    print("🚀 Setting up Living Codex Demo Data using Core System APIs")
    print("=" * 60)
    
    # Initialize the core systems
    user_system = UserManagementSystem()
    contribution_system = ContributionSystem()
    
    print("✅ Core systems initialized")
    
    # Create Alice Chen - Software Developer
    print("\n👩 Creating Alice Chen profile...")
    alice_data = {
        'identity': {
            'name': 'Alice Chen',
            'pronouns': 'she/her',
            'cultural_background': 'Asian American',
            'belief_system': 'Scientific',
            'life_experience': 'Tech industry professional'
        },
        'communication': {
            'primary_language': 'English',
            'secondary_languages': ['Mandarin'],
            'communication_style': CommunicationStyle.TECHNICAL,
            'learning_style': LearningStyle.VISUAL
        },
        'technical': {
            'skill_levels': {
                'programming': SkillLevel.EXPERT,
                'data_analysis': SkillLevel.INTERMEDIATE,
                'design': SkillLevel.BEGINNER,
                'research': SkillLevel.INTERMEDIATE
            },
            'preferred_tools': ['Python', 'JavaScript', 'Git', 'Docker'],
            'contribution_areas': ['software_development', 'web_development']
        },
        'interests': {
            'primary_domains': ['software_development', 'artificial_intelligence', 'web_development'],
            'specific_topics': ['Python', 'Flask', 'React', 'Neural Networks'],
            'expertise_levels': {
                'Python': SkillLevel.EXPERT,
                'JavaScript': SkillLevel.EXPERT,
                'Machine Learning': SkillLevel.INTERMEDIATE
            }
        },
        'location': {
            'geographic_location': 'San Francisco, CA',
            'timezone': 'PST',
            'cultural_context': 'Tech Hub'
        }
    }
    
    alice_profile = user_system.create_user_profile(alice_data)
    if alice_profile:
        print(f"   ✅ Alice Chen profile created with ID: {alice_profile.user_id}")
        # Store the ID for later use
        alice_id = alice_profile.user_id
    else:
        print("   ❌ Failed to create Alice Chen profile")
        return False
    
    # Create Bob Rodriguez - AI Researcher
    print("\n👨 Creating Bob Rodriguez profile...")
    bob_data = {
        'identity': {
            'name': 'Bob Rodriguez',
            'pronouns': 'he/him',
            'cultural_background': 'Latino American',
            'belief_system': 'Scientific',
            'life_experience': 'Academic researcher'
        },
        'communication': {
            'primary_language': 'English',
            'secondary_languages': ['Spanish'],
            'communication_style': CommunicationStyle.FORMAL,
            'learning_style': LearningStyle.READING
        },
        'technical': {
            'skill_levels': {
                'programming': SkillLevel.EXPERT,
                'data_analysis': SkillLevel.EXPERT,
                'research': SkillLevel.EXPERT,
                'mathematics': SkillLevel.EXPERT
            },
            'preferred_tools': ['Python', 'TensorFlow', 'PyTorch', 'Jupyter'],
            'contribution_areas': ['artificial_intelligence', 'machine_learning', 'research']
        },
        'interests': {
            'primary_domains': ['artificial_intelligence', 'machine_learning', 'research'],
            'specific_topics': ['Neural Networks', 'Deep Learning', 'Attention Mechanisms', 'Transformers'],
            'expertise_levels': {
                'Neural Networks': SkillLevel.EXPERT,
                'Deep Learning': SkillLevel.EXPERT,
                'Python': SkillLevel.EXPERT,
                'Mathematics': SkillLevel.EXPERT
            }
        },
        'location': {
            'geographic_location': 'Boston, MA',
            'timezone': 'EST',
            'cultural_context': 'Academic'
        }
    }
    
    bob_profile = user_system.create_user_profile(bob_data)
    if bob_profile:
        print(f"   ✅ Bob Rodriguez profile created with ID: {bob_profile.user_id}")
        bob_id = bob_profile.user_id
    else:
        print("   ❌ Failed to create Bob Rodriguez profile")
        return False
    
    # Create a neural network contribution
    print("\n💻 Creating Neural Network contribution...")
    contribution_data = {
        'contribution_type': 'code',
        'metadata': {
            'title': 'Advanced Neural Network Implementation',
            'description': 'Implementation of attention mechanisms and transformer architecture',
            'tags': ['neural_networks', 'attention_mechanisms', 'python', 'machine_learning'],
            'language': 'en',
            'skill_level': 'expert'
        },
        'code_content': {
            'code_content': 'import tensorflow as tf\nimport numpy as np\n\nclass AttentionMechanism:\n    def __init__(self):\n        pass\n\n    def forward(self, x):\n        return x',
            'language': 'python',
            'framework': 'tensorflow',
            'dependencies': ['tensorflow', 'numpy', 'matplotlib']
        }
    }
    
    # Create the contribution using Bob's ID
    contribution = contribution_system.create_contribution(bob_id, contribution_data)
    if contribution:
        print(f"   ✅ Neural Network contribution created with ID: {contribution.contribution_id}")
    else:
        print("   ❌ Failed to create Neural Network contribution")
    
    # Create a Flask web app contribution
    print("\n🌐 Creating Flask Web App contribution...")
    flask_contribution_data = {
        'contribution_type': 'code',
        'metadata': {
            'title': 'Flask Web Application Framework',
            'description': 'Modern web application framework with RESTful API support',
            'tags': ['flask', 'python', 'web_development', 'api'],
            'language': 'en',
            'skill_level': 'intermediate'
        },
        'code_content': {
            'code_content': 'from flask import Flask\n\napp = Flask(__name__)\n\n@app.route("/")\ndef hello():\n    return "Hello, World!"\n\nif __name__ == "__main__":\n    app.run()',
            'language': 'python',
            'framework': 'flask',
            'dependencies': ['flask', 'flask-restful', 'sqlalchemy']
        }
    }
    
    # Create the contribution using Alice's ID
    flask_contribution = contribution_system.create_contribution(alice_id, flask_contribution_data)
    if flask_contribution:
        print(f"   ✅ Flask Web App contribution created with ID: {flask_contribution.contribution_id}")
    else:
        print("   ❌ Failed to create Flask Web App contribution")
    
    print("\n" + "=" * 60)
    print("🎉 Demo data setup completed successfully!")
    print("\n📋 Created Demo Data:")
    print(f"   👩 Alice Chen (ID: {alice_id}) - Software Developer")
    print(f"   👨 Bob Rodriguez (ID: {bob_id}) - AI Researcher")
    print("   💻 Neural Network Implementation (Code)")
    print("   🌐 Flask Web Application Framework (Code)")
    
    print("\n🔑 Demo Login Credentials:")
    print(f"   Alice: {alice_id}")
    print(f"   Bob: {bob_id}")
    
    print("\n🧭 Navigation Flow:")
    print("   1. Login with Alice or Bob")
    print("   2. Navigate to Discover page")
    print("   3. View user profiles")
    print("   4. Explore concepts (Neural Networks, Flask)")
    print("   5. View source files")
    print("   6. Navigate to specific expressions")
    
    return True

def main():
    """Main function"""
    try:
        success = setup_demo_data()
        if success:
            print("\n✅ Demo setup completed successfully!")
            print("   You can now start the web interface and test the navigation flow.")
        else:
            print("\n❌ Demo setup failed!")
            print("   Check the error messages above.")
    except Exception as e:
        print(f"\n❌ Demo setup failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
