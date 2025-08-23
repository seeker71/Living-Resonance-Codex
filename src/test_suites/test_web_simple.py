#!/usr/bin/env python3
"""
Simplified Web Interface Test Suite
Checks file structure, syntax, and basic functionality without importing problematic modules
"""

import ast
import tempfile
import os
from pathlib import Path

def test_web_interface_file_structure():
    """Test that web interface files exist and have correct structure"""
    print("🧪 Testing Web Interface File Structure...")
    
    try:
        web_dir = Path(__file__).parent.parent / "web_platform"
        
        # Check if web_platform directory exists
        assert web_dir.exists(), "Web platform directory should exist"
        assert web_dir.is_dir(), "Web platform directory should be a directory"
        
        # Check for key web interface files
        key_files = [
            'unified_web_interface.py',
            'user_management.py',
            'contribution_system.py',
            'ontology_navigator.py'
        ]
        
        for file_name in key_files:
            file_path = web_dir / file_name
            assert file_path.exists(), f"File {file_name} should exist"
            assert file_path.is_file(), f"{file_name} should be a file"
        
        print("✅ Web Interface File Structure: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface File Structure: FAILED - {e}")
        return False

def test_web_interface_syntax():
    """Test that web interface Python files have valid syntax"""
    print("🧪 Testing Web Interface Syntax...")
    
    try:
        web_dir = Path(__file__).parent.parent / "web_platform"
        
        # Test main web interface file
        main_file = web_dir / "unified_web_interface.py"
        with open(main_file, 'r') as f:
            content = f.read()
            # Parse the Python code to check syntax
            ast.parse(content)
        
        # Test other key files
        key_files = ['user_management.py', 'contribution_system.py', 'ontology_navigator.py']
        for file_name in key_files:
            file_path = web_dir / file_name
            with open(file_path, 'r') as f:
                content = f.read()
                ast.parse(content)
        
        print("✅ Web Interface Syntax: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface Syntax: FAILED - {e}")
        return False

def test_web_interface_routes():
    """Test that web interface has expected route definitions"""
    print("🧪 Testing Web Interface Routes...")
    
    try:
        main_file = Path(__file__).parent.parent / "web_platform" / "unified_web_interface.py"
        
        with open(main_file, 'r') as f:
            content = f.read()
        
        # Check for expected route decorators
        expected_routes = [
            '@app.route(\'/\')',
            '@app.route(\'/signup\'',
            '@app.route(\'/login\'',
            '@app.route(\'/dashboard\'',
            '@app.route(\'/discover\'',
            '@app.route(\'/navigate\'',
            '@app.route(\'/contribute\'',
            '@app.route(\'/assets\'',
            '@app.route(\'/ontology\'',
            '@app.route(\'/api/assets\'',
            '@app.route(\'/api/ontology/overview\''
        ]
        
        for route in expected_routes:
            assert route in content, f"Route {route} should be defined"
        
        print("✅ Web Interface Routes: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface Routes: FAILED - {e}")
        return False

def test_web_interface_classes():
    """Test that web interface has expected class definitions"""
    print("🧪 Testing Web Interface Classes...")
    
    try:
        main_file = Path(__file__).parent.parent / "web_platform" / "unified_web_interface.py"
        
        with open(main_file, 'r') as f:
            content = f.read()
        
        # Check for expected class definitions
        expected_classes = [
            'class DiscoveryEngine:',
            'class NavigationSystem:',
            'class ContributionManager:',
            'class UserManager:',
            'class WebUser(',
            'def create_unified_templates():'
        ]
        
        for class_def in expected_classes:
            assert class_def in content, f"Class/function {class_def} should be defined"
        
        print("✅ Web Interface Classes: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface Classes: FAILED - {e}")
        return False

def test_web_interface_asset_management():
    """Test that web interface has asset management functionality"""
    print("🧪 Testing Web Interface Asset Management...")
    
    try:
        main_file = Path(__file__).parent.parent / "web_platform" / "unified_web_interface.py"
        
        with open(main_file, 'r') as f:
            content = f.read()
        
        # Check for asset management functions
        expected_asset_functions = [
            'def hash_file(',
            'def detect_asset_type(',
            'def find_asset(',
            'def save_assets_index(',
            'assets_dir =',
            'assets_index_path ='
        ]
        
        for func in expected_asset_functions:
            assert func in content, f"Asset function {func} should be defined"
        
        print("✅ Web Interface Asset Management: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface Asset Management: FAILED - {e}")
        return False

def test_web_interface_templates():
    """Test that web interface can create templates"""
    print("🧪 Testing Web Interface Template Creation...")
    
    try:
        main_file = Path(__file__).parent.parent / "web_platform" / "unified_web_interface.py"
        
        with open(main_file, 'r') as f:
            content = f.read()
        
        # Check for template creation
        assert 'create_unified_templates()' in content, "Template creation function should exist"
        assert 'unified_index.html' in content, "Should create index template"
        assert 'unified_assets.html' in content, "Should create assets template"
        
        print("✅ Web Interface Template Creation: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface Template Creation: FAILED - {e}")
        return False

def test_web_interface_api_endpoints():
    """Test that web interface has expected API endpoints"""
    print("🧪 Testing Web Interface API Endpoints...")
    
    try:
        main_file = Path(__file__).parent.parent / "web_platform" / "unified_web_interface.py"
        
        with open(main_file, 'r') as f:
            content = f.read()
        
        # Check for API endpoint definitions
        expected_apis = [
            '@app.route(\'/api/discovery/similar_users\')',
            '@app.route(\'/api/discovery/relevant_content\')',
            '@app.route(\'/api/navigation/system_overview\')',
            '@app.route(\'/api/contributions\')',
            '@app.route(\'/api/assets\'',
            '@app.route(\'/api/ontology/overview\')',
            '@app.route(\'/api/ontology/categories\')',
            '@app.route(\'/api/ontology/components\')'
        ]
        
        for api in expected_apis:
            assert api in content, f"API endpoint {api} should be defined"
        
        print("✅ Web Interface API Endpoints: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Web Interface API Endpoints: FAILED - {e}")
        return False

def run_simplified_web_test_suite():
    """Run all simplified web interface tests"""
    print("🌐 Living Codex Web Interface - Simplified Test Suite")
    print("=" * 60)
    
    test_functions = [
        test_web_interface_file_structure,
        test_web_interface_syntax,
        test_web_interface_routes,
        test_web_interface_classes,
        test_web_interface_asset_management,
        test_web_interface_templates,
        test_web_interface_api_endpoints
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
    print(f"📊 Simplified Web Test Results: {passed} PASSED, {failed} FAILED")
    
    if failed == 0:
        print("🎉 All simplified web tests passed!")
        return True
    else:
        print("⚠️  Some simplified web tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = run_simplified_web_test_suite()
    exit(0 if success else 1)
