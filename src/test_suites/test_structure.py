#!/usr/bin/env python3
"""
Test the organized file structure of the Living Codex system
"""

import os
from pathlib import Path

def test_directory_structure():
    """Test that all required directories and files exist"""
    print("🧪 Testing Living Codex Directory Structure")
    print("=" * 50)
    
    # Fix the path calculation - we're in src/test_suites, so parent.parent gets us to the root
    base_path = Path(__file__).parent.parent.parent
    src_path = base_path / "src"
    
    # Check main directories
    required_dirs = [
        "src",
        "src/core",
        "src/ontology", 
        "src/ai_agents",
        "src/integration",
        "src/demos",
        "docs",
        "test_assets"
    ]
    
    # Check required files
    required_files = [
        "src/core/explore_bootstrapped_system.py",
        "src/ontology/enhanced_ontology_system.py",
        "src/ai_agents/ai_agent_system.py",
        "src/integration/comprehensive_integration_demo.py",
        "src/demos/autonomous_learning_demo.py",
        "src/demos/autonomous_decision_demo.py",
        "src/core/__init__.py",
        "src/ontology/__init__.py",
        "src/ai_agents/__init__.py",
        "src/integration/__init__.py",
        "src/demos/__init__.py",
        "src/__init__.py",
        "launch_cli.py",
        "README.md",
        "requirements.txt"
    ]
    
    print("Checking directories...")
    dir_results = []
    for dir_path in required_dirs:
        full_path = base_path / dir_path
        if full_path.exists() and full_path.is_dir():
            print(f"   ✅ {dir_path}")
            dir_results.append(True)
        else:
            print(f"   ❌ {dir_path}")
            dir_results.append(False)
    
    print("\nChecking files...")
    file_results = []
    for file_path in required_files:
        full_path = base_path / file_path
        if full_path.exists() and full_path.is_file():
            print(f"   ✅ {file_path}")
            file_results.append(True)
        else:
            print(f"   ❌ {file_path}")
            file_results.append(False)
    
    # Calculate results
    total_dirs = len(dir_results)
    total_files = len(file_results)
    passed_dirs = sum(dir_results)
    passed_files = sum(file_results)
    
    print(f"\n📊 Directory Results: {passed_dirs}/{total_dirs} passed")
    print(f"📊 File Results: {passed_files}/{total_files} passed")
    
    total_passed = passed_dirs + passed_files
    total_tests = total_dirs + total_files
    
    print(f"📊 Overall Results: {total_passed}/{total_tests} passed")
    
    if total_passed == total_tests:
        print("🎉 All structure tests passed! System is properly organized.")
        return True
    else:
        print("❌ Some structure tests failed. Check the organization.")
        return False

if __name__ == "__main__":
    success = test_directory_structure()
    exit(0 if success else 1)
