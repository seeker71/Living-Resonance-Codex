#!/usr/bin/env python3
"""
Comprehensive Test Suite for Living Codex Web Interface
Tests all major features: user management, discovery, navigation, contributions, ontology, and asset management
"""

import sys
import os
import tempfile
import shutil
import json
import requests
import time
from pathlib import Path
from unittest.mock import patch, MagicMock
import io

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the web interface components
from web_platform.unified_web_interface import (
    app, UserManager, UserManagementSystem, WebUser, DiscoveryEngine, 
    NavigationSystem, ContributionManager, ontology_navigator,
    assets_dir, assets_index_path, save_assets_index, hash_file, 
    detect_asset_type, find_asset, create_unified_templates
)

def test_web_server_startup():
    """Test web server startup and basic functionality"""
    print("🧪 Testing Web Server Startup...")
    
    try:
        # Test app configuration
        assert app.name == 'unified_web_interface', "App should have correct name"
        assert hasattr(app, 'route'), "App should have route decorator"
        
        # Test basic routes exist
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        expected_routes = ['/', '/signup', '/login', '/dashboard', '/discover', '/navigate', '/contribute', '/assets']
        for route in expected_routes:
            assert route in routes, f"Route {route} should exist"
        
        print("✅ Web Server Startup: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Server Startup: FAILED - {e}")
        return False

def test_user_management_system():
    """Test user management components"""
    print("🧪 Testing User Management System...")
    
    try:
        # Test user management system initialization
        user_system = UserManagementSystem()
        assert user_system is not None, "User management system should initialize"
        
        # Test user profile creation
        user_data = {
            'identity': {
                'name': 'Test User',
                'pronouns': 'they/them',
                'cultural_background': 'Global',
                'belief_system': 'Open',
                'life_experience': 'Diverse'
            },
            'communication': {
                'primary_language': 'English',
                'secondary_languages': ['Spanish'],
                'communication_style': 'casual',
                'learning_style': 'reading',
                'accessibility_needs': []
            },
            'technical': {
                'skill_levels': {
                    'programming': 'intermediate',
                    'data_analysis': 'beginner',
                    'design': 'beginner',
                    'research': 'intermediate'
                },
                'learning_path': ['AI', 'ML'],
                'preferred_tools': ['Python', 'Jupyter'],
                'contribution_areas': ['Documentation', 'Testing']
            },
            'interests': {
                'primary_domains': ['Technology', 'Science'],
                'specific_topics': ['Artificial Intelligence', 'Machine Learning'],
                'expertise_levels': {},
                'passion_areas': ['Education', 'Innovation']
            },
            'location': {
                'geographic_location': 'San Francisco',
                'timezone': 'PST',
                'cultural_context': 'Tech Hub',
                'local_challenges': ['Housing', 'Traffic'],
                'local_resources': ['Universities', 'Tech Companies']
            }
        }
        
        user_profile = UserManager.create_user_profile(user_data)
        assert user_profile is not None, "Should create user profile"
        assert user_profile.identity.name == 'Test User', "Profile should have correct name"
        
        # Test WebUser class
        web_user = WebUser("test_id", user_profile)
        assert web_user.id == "test_id", "WebUser should have correct ID"
        assert web_user.profile == user_profile, "WebUser should have correct profile"
        
        print("✅ User Management System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ User Management System: FAILED - {e}")
        return False

def test_discovery_engine():
    """Test discovery engine functionality"""
    print("🧪 Testing Discovery Engine...")
    
    try:
        # Create test user profiles
        user1_data = {
            'identity': CoreIdentity('Alice', 'she/her'),
            'communication': CommunicationPreferences('English', ['Spanish']),
            'technical': TechnicalProfile(),
            'interests': Interests(['Technology', 'Programming']),
            'location': LocationContext('San Francisco', 'PST')
        }
        user1 = UserProfile(user1_data)
        
        user2_data = {
            'identity': CoreIdentity('Bob', 'he/him'),
            'communication': CommunicationPreferences('English', ['French']),
            'technical': TechnicalProfile(),
            'interests': Interests(['Technology', 'AI']),
            'location': LocationContext('San Francisco', 'PST')
        }
        user2 = UserProfile(user2_data)
        
        # Test similar user discovery
        similar_users = DiscoveryEngine.find_similar_users(user1, limit=5)
        assert isinstance(similar_users, list), "Should return list of similar users"
        
        # Test relevant content discovery
        relevant_content = DiscoveryEngine.find_relevant_content(user1, limit=10)
        assert isinstance(relevant_content, list), "Should return list of relevant content"
        
        print("✅ Discovery Engine: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Discovery Engine: FAILED - {e}")
        return False

def test_navigation_system():
    """Test navigation system functionality"""
    print("🧪 Testing Navigation System...")
    
    try:
        # Test exploration paths
        paths = NavigationSystem.get_exploration_paths("test_user")
        assert isinstance(paths, list), "Should return list of exploration paths"
        assert len(paths) > 0, "Should have exploration paths"
        
        # Test system overview
        overview = NavigationSystem.get_system_overview()
        assert isinstance(overview, dict), "Should return system overview dict"
        assert 'total_users' in overview, "Overview should have total_users"
        assert 'total_contributions' in overview, "Overview should have total_contributions"
        
        print("✅ Navigation System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Navigation System: FAILED - {e}")
        return False

def test_contribution_system():
    """Test contribution management"""
    print("🧪 Testing Contribution System...")
    
    try:
        # Test contribution creation
        contrib_data = {
            'title': 'Test Contribution',
            'description': 'A test contribution for testing',
            'category': 'Technology',
            'contribution_type': 'knowledge',
            'skill_level': 'intermediate',
            'language': 'Python',
            'tags': ['test', 'documentation'],
            'visibility': 'public'
        }
        
        contribution = ContributionManager.create_contribution("test_user", contrib_data)
        assert contribution is not None, "Should create contribution"
        assert contribution['title'] == 'Test Contribution', "Contribution should have correct title"
        
        # Test getting user contributions
        user_contributions = ContributionManager.get_user_contributions("test_user")
        assert isinstance(user_contributions, list), "Should return list of user contributions"
        
        # Test getting contributions by category
        category_contributions = ContributionManager.get_contributions_by_category("Technology")
        assert isinstance(category_contributions, list), "Should return list of category contributions"
        
        print("✅ Contribution System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Contribution System: FAILED - {e}")
        return False

def test_ontology_navigation():
    """Test ontology navigation system"""
    print("🧪 Testing Ontology Navigation...")
    
    try:
        # Test ontology overview
        overview = ontology_navigator.get_ontology_overview()
        assert isinstance(overview, dict), "Should return ontology overview"
        
        # Test system architecture
        architecture = ontology_navigator.get_system_architecture()
        assert isinstance(architecture, dict), "Should return system architecture"
        
        # Test categories
        assert hasattr(ontology_navigator, 'categories'), "Should have categories attribute"
        
        # Test node operations
        nodes = ontology_navigator.get_nodes_by_category('core_system')
        assert isinstance(nodes, list), "Should return nodes by category"
        
        print("✅ Ontology Navigation: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Ontology Navigation: FAILED - {e}")
        return False

def test_asset_management():
    """Test asset management functionality"""
    print("🧪 Testing Asset Management...")
    
    try:
        # Test asset store initialization
        assert assets_dir.exists(), "Assets directory should exist"
        assert assets_dir.is_dir(), "Assets directory should be a directory"
        
        # Test asset type detection
        test_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        test_file.write(b"Test content")
        test_file.close()
        
        try:
            asset_type = detect_asset_type(Path(test_file.name))
            assert asset_type == 'document', "Should detect text file as document type"
            
            # Test file hashing
            file_hash = hash_file(Path(test_file.name))
            assert len(file_hash) == 64, "SHA-256 hash should be 64 characters"
            assert file_hash.isalnum(), "Hash should be alphanumeric"
            
            # Test asset finding
            asset = find_asset(file_hash)
            assert asset is None, "New file should not be in index"
            
        finally:
            os.unlink(test_file.name)
        
        print("✅ Asset Management: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Asset Management: FAILED - {e}")
        return False

def test_web_routes():
    """Test web route definitions and handlers"""
    print("🧪 Testing Web Routes...")
    
    try:
        # Test route handlers exist
        routes = app.url_map.iter_rules()
        route_handlers = {}
        
        for rule in routes:
            if rule.endpoint != 'static':
                route_handlers[rule.rule] = rule.endpoint
        
        # Test key routes have handlers
        key_routes = ['/', '/signup', '/login', '/dashboard', '/discover', '/navigate', '/contribute', '/assets']
        for route in key_routes:
            assert route in route_handlers, f"Route {route} should have a handler"
        
        # Test API routes
        api_routes = ['/api/discovery/similar_users', '/api/discovery/relevant_content', 
                     '/api/navigation/system_overview', '/api/contributions', 
                     '/api/assets', '/api/ontology/overview']
        
        for route in api_routes:
            assert route in route_handlers, f"API route {route} should have a handler"
        
        print("✅ Web Routes: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Routes: FAILED - {e}")
        return False

def test_template_creation():
    """Test template creation functionality"""
    print("🧪 Testing Template Creation...")
    
    try:
        # Test template creation
        create_unified_templates()
        
        # Check if templates directory exists
        templates_dir = Path(__file__).parent / "src" / "platform" / "templates"
        assert templates_dir.exists(), "Templates directory should be created"
        
        # Check if key templates exist
        key_templates = [
            'unified_index.html',
            'unified_signup.html', 
            'unified_login.html',
            'unified_dashboard.html',
            'unified_discover.html',
            'unified_navigate.html',
            'unified_contribute.html',
            'unified_assets.html'
        ]
        
        for template in key_templates:
            template_path = templates_dir / template
            assert template_path.exists(), f"Template {template} should be created"
        
        print("✅ Template Creation: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Template Creation: FAILED - {e}")
        return False

def test_integration_features():
    """Test integration between different systems"""
    print("🧪 Testing Integration Features...")
    
    try:
        # Test user creation and contribution integration
        user_data = {
            'identity': {'name': 'Integration Test User'},
            'communication': {'primary_language': 'English'},
            'technical': {'skill_levels': {}},
            'interests': {'primary_domains': ['Technology']},
            'location': {'geographic_location': 'Test City'}
        }
        
        user_profile = UserManager.create_user_profile(user_data)
        assert user_profile is not None, "Should create user profile"
        
        # Test contribution with user
        contrib_data = {
            'title': 'Integration Test',
            'description': 'Testing system integration',
            'category': 'Technology',
            'contribution_type': 'knowledge'
        }
        
        contribution = ContributionManager.create_contribution("test_user_id", contrib_data)
        assert contribution is not None, "Should create contribution"
        
        # Test discovery with user
        similar_users = DiscoveryEngine.find_similar_users(user_profile, limit=5)
        assert isinstance(similar_users, list), "Should find similar users"
        
        # Test navigation with user
        paths = NavigationSystem.get_exploration_paths("test_user_id")
        assert isinstance(paths, list), "Should get exploration paths"
        
        print("✅ Integration Features: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Integration Features: FAILED - {e}")
        return False

def run_comprehensive_web_test_suite():
    """Run all web interface test categories"""
    print("🌐 Living Codex Web Interface - Comprehensive Test Suite")
    print("=" * 60)
    
    test_functions = [
        test_web_server_startup,
        test_user_management_system,
        test_discovery_engine,
        test_navigation_system,
        test_contribution_system,
        test_ontology_navigation,
        test_asset_management,
        test_web_routes,
        test_template_creation,
        test_integration_features
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ {test_func.__name__}: CRASHED - {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"📊 Web Test Results: {passed} PASSED, {failed} FAILED")
    
    if failed == 0:
        print("🎉 All web tests passed! Web interface is fully functional.")
        return True
    else:
        print("⚠️  Some web tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = run_comprehensive_web_test_suite()
    sys.exit(0 if success else 1)
