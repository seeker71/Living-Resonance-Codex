#!/usr/bin/env python3
"""
Simplified CLI Test Suite
Uses subprocess to test CLI functionality through launch_cli.py
"""

import subprocess
import tempfile
import os
from pathlib import Path

def test_cli_basic_functionality():
    """Test basic CLI functionality through subprocess"""
    print("🧪 Testing CLI Basic Functionality...")
    
    try:
        # Test help command
        result = subprocess.run(
            ['python', 'launch_cli.py'],
            input='help\nquit\n',
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        output = result.stdout
        
        # Check for expected help content
        assert '🌌 Living Codex Consolidated CLI Commands:' in output, "Help should show CLI commands"
        assert '🧠 AI & Intelligence:' in output, "Help should show AI section"
        assert '👥 User Management & Discovery:' in output, "Help should show user management section"
        assert '📁 Digital asset management' in output, "Help should show asset management"
        
        print("✅ CLI Basic Functionality: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ CLI Basic Functionality: FAILED - {e}")
        return False

def test_cli_ontology_exploration():
    """Test ontology exploration commands"""
    print("🧪 Testing CLI Ontology Exploration...")
    
    try:
        # Test ontology exploration
        result = subprocess.run(
            ['python', 'launch_cli.py'],
            input='explore ontology\nquit\n',
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        output = result.stdout
        
        # Check for ontology content - look for the actual output patterns
        assert '🌟 Fractal Navigation:' in output, "Should show fractal navigation"
        assert '🌟 Resonance Systems:' in output, "Should show resonance systems"
        assert '🌟 Federation Systems:' in output, "Should show federation systems"
        
        print("✅ CLI Ontology Exploration: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ CLI Ontology Exploration: FAILED - {e}")
        return False

def test_cli_user_management():
    """Test user management commands"""
    print("🧪 Testing CLI User Management...")
    
    try:
        # Test user creation
        result = subprocess.run(
            ['python', 'launch_cli.py'],
            input='user create TestUser\nuser list\nquit\n',
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        output = result.stdout
        
        # Check for user creation - look for the actual output pattern
        assert '✅ User \'TestUser\' created successfully' in output, "Should create user successfully"
        
        print("✅ CLI User Management: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ CLI User Management: FAILED - {e}")
        return False

def test_cli_asset_management():
    """Test asset management commands"""
    print("🧪 Testing CLI Asset Management...")
    
    try:
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("Test content for asset management")
            test_file_path = f.name
        
        try:
            # Test asset addition
            result = subprocess.run(
                ['python', 'launch_cli.py'],
                input=f'asset add {test_file_path} --type document --tags test,cli\nasset list\nquit\n',
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent
            )
            
            output = result.stdout
            
            # Check for asset storage
            assert '✅ Asset stored:' in output, "Should store asset successfully"
            assert '📁 Assets in store' in output, "Should list assets"
            
            print("✅ CLI Asset Management: PASSED")
            return True
            
        finally:
            # Cleanup
            os.unlink(test_file_path)
            
    except Exception as e:
        print(f"❌ CLI Asset Management: FAILED - {e}")
        return False

def test_cli_knowledge_operations():
    """Test knowledge base operations"""
    print("🧪 Testing CLI Knowledge Operations...")
    
    try:
        # Test knowledge creation
        result = subprocess.run(
            ['python', 'launch_cli.py'],
            input='create concept test_concept Test concept content\nlist concept\nquit\n',
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        output = result.stdout
        
        # Check for knowledge operations
        assert '✅ Created concept node:' in output, "Should create concept successfully"
        assert '📋 Listing concept entities' in output, "Should list concepts"
        
        print("✅ CLI Knowledge Operations: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ CLI Knowledge Operations: FAILED - {e}")
        return False

def test_cli_system_features():
    """Test system management features"""
    print("🧪 Testing CLI System Features...")
    
    try:
        # Test system status
        result = subprocess.run(
            ['python', 'launch_cli.py'],
            input='status\nenergy\nquit\n',
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        output = result.stdout
        
        # Check for system features
        assert '📊 Living Codex System Status:' in output, "Should show system status"
        assert '⚡ Energy Status:' in output, "Should show energy status"
        
        print("✅ CLI System Features: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ CLI System Features: FAILED - {e}")
        return False

def test_cli_ai_agent_system():
    """Test AI agent system"""
    print("🧪 Testing CLI AI Agent System...")
    
    try:
        # Test AI agent creation
        result = subprocess.run(
            ['python', 'launch_cli.py'],
            input='agent create Explorer\nagent list\nquit\n',
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        output = result.stdout
        
        # Check for AI agent operations - look for the actual output pattern
        assert '✅ AI Agent \'Explorer\' created successfully' in output, "Should create AI agent"
        assert '🆔 Agent ID:' in output, "Should show agent ID"
        
        print("✅ CLI AI Agent System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ CLI AI Agent System: FAILED - {e}")
        return False

def run_simplified_cli_test_suite():
    """Run all simplified CLI tests"""
    print("🚀 Living Codex CLI - Simplified Test Suite")
    print("=" * 60)
    
    test_functions = [
        test_cli_basic_functionality,
        test_cli_ontology_exploration,
        test_cli_user_management,
        test_cli_asset_management,
        test_cli_knowledge_operations,
        test_cli_system_features,
        test_cli_ai_agent_system
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
    print(f"📊 Simplified CLI Test Results: {passed} PASSED, {failed} FAILED")
    
    if failed == 0:
        print("🎉 All simplified CLI tests passed!")
        return True
    else:
        print("⚠️  Some simplified CLI tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = run_simplified_cli_test_suite()
    exit(0 if success else 1)
