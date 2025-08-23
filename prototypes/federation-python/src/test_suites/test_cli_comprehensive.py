#!/usr/bin/env python3
"""
Comprehensive Test Suite for Living Codex CLI
Tests all major features: ontology, user management, asset management, knowledge operations, and system features
"""

import sys
import os
import tempfile
import shutil
import json
from pathlib import Path
from unittest.mock import patch, MagicMock
import io

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Temporarily rename web_platform directory to avoid conflicts
platform_dir = Path(__file__).parent / "src" / "web_platform"
platform_backup = Path(__file__).parent / "src" / "web_platform_backup"

if platform_dir.exists():
    print("🔄 Temporarily renaming platform directory to avoid conflicts...")
    platform_dir.rename(platform_backup)
    platform_renamed = True
else:
    platform_renamed = False

try:
    # Now import the CLI
    from core.living_codex_cli import LivingCodexCLI
finally:
    # Restore platform directory
    if platform_renamed and platform_backup.exists():
        print("🔄 Restoring platform directory...")
        platform_backup.rename(platform_dir)


def test_ontology_system():
    """Test ontology exploration and search capabilities"""
    print("🧪 Testing Ontology System...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test ontology initialization
        assert hasattr(cli, 'ontology'), "CLI should have ontology attribute"
        assert isinstance(cli.ontology, dict), "Ontology should be a dictionary"
        
        # Test water states
        assert 'water_states' in cli.ontology, "Should have water states"
        assert len(cli.ontology['water_states']) == 12, "Should have 12 water states"
        
        # Test fractal layers
        assert 'fractal_layers' in cli.ontology, "Should have fractal layers"
        assert len(cli.ontology['fractal_layers']) == 16, "Should have 16 fractal layers"
        
        # Test seed ontology
        assert 'seed_ontology' in cli.ontology, "Should have seed ontology"
        assert len(cli.ontology['seed_ontology']) == 12, "Should have 12 seed nodes"
        
        # Test programming languages
        assert 'programming_languages' in cli.ontology, "Should have programming languages"
        assert '🐍 Python' in cli.ontology['programming_languages'], "Should include Python"
        
        # Test chakras and frequencies
        assert 'chakras' in cli.ontology, "Should have chakra system"
        assert 'frequencies' in cli.ontology, "Should have frequency mapping"
        assert 'colors' in cli.ontology, "Should have color mapping"
        assert 'archangels' in cli.ontology, "Should have archangel mapping"
        
        print("✅ Ontology System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Ontology System: FAILED - {e}")
        return False

def test_user_management():
    """Test user creation, profile management, and discovery"""
    print("🧪 Testing User Management...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test user creation
        cli.do_user("create Alice")
        assert len(cli.users) == 1, "Should create user"
        assert 'Alice' in [u['core_identity']['name'] for u in cli.users.values()]
        
        # Test user profile
        user_id = list(cli.users.keys())[0]
        cli.do_user(f"profile {user_id}")
        
        # Test user update
        cli.do_user(f"update {user_id} location New York")
        assert cli.users[user_id]['location_context']['geographic_location'] == 'New York'
        
        # Test interests management
        cli.do_user(f"interests {user_id} add programming")
        assert 'programming' in cli.users[user_id]['interests']['primary_domains']
        
        # Test skills management
        cli.do_user(f"skills {user_id} python advanced")
        assert cli.users[user_id]['technical_profile']['skill_levels']['python'] == 'advanced'
        
        # Test user listing
        cli.do_user("list")
        
        print("✅ User Management: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ User Management: FAILED - {e}")
        return False

def test_asset_management():
    """Test digital asset management capabilities"""
    print("🧪 Testing Asset Management...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("Test content for asset management")
            test_file_path = f.name
        
        try:
            # Test asset addition
            cli.do_asset(f"add {test_file_path} --type document --tags test,cli")
            assert len(cli.assets_index) == 1, "Should add asset to index"
            
            # Test asset listing
            cli.do_asset("list")
            
            # Get asset ID for further tests
            asset_id = cli.assets_index[0]['id'][:12]  # First 12 chars
            
            # Test asset info
            cli.do_asset(f"info {asset_id}")
            
            # Test asset search
            cli.do_asset("search test")
            
            # Test asset retrieval
            test_dest = tempfile.mkdtemp()
            try:
                cli.do_asset(f"get {asset_id} {test_dest}")
                # Verify file was retrieved
                retrieved_files = list(Path(test_dest).glob("*"))
                assert len(retrieved_files) > 0, "Should retrieve asset file"
            finally:
                shutil.rmtree(test_dest)
            
            # Test asset removal (metadata only)
            cli.do_asset(f"remove {asset_id}")
            assert len(cli.assets_index) == 0, "Should remove asset metadata"
            
            print("✅ Asset Management: PASSED")
            return True
            
        finally:
            # Cleanup
            os.unlink(test_file_path)
            
    except Exception as e:
        print(f"❌ Asset Management: FAILED - {e}")
        return False

def test_knowledge_operations():
    """Test knowledge base operations"""
    print("🧪 Testing Knowledge Operations...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test knowledge creation
        cli.do_create("concept test_concept Test concept content")
        assert len(cli.knowledge_base) == 1, "Should create knowledge node"
        
        # Test knowledge listing
        cli.do_list("concept")
        
        # Test knowledge search
        cli.do_search("test_concept")
        
        print("✅ Knowledge Operations: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Knowledge Operations: FAILED - {e}")
        return False

def test_system_features():
    """Test system management and status features"""
    print("🧪 Testing System Features...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test energy system
        cli.do_energy("")
        assert cli.current_energy > 0, "Should have positive energy"
        
        # Test system status
        cli.do_status("")
        
        # Test system tests
        cli.do_test("")
        
        print("✅ System Features: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ System Features: FAILED - {e}")
        return False

def test_ai_agent_system():
    """Test AI agent and demo capabilities"""
    print("🧪 Testing AI Agent System...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test AI agent creation
        cli.do_agent("create Explorer")
        
        # Test AI agent listing
        cli.do_agent("list")
        
        # Test AI agent status
        cli.do_agent("status Explorer")
        
        # Test AI agent task execution
        cli.do_agent("task Explorer analyze")
        
        # Test demo system
        cli.do_demo("ontology")
        cli.do_demo("ai_agents")
        cli.do_demo("resonance")
        
        print("✅ AI Agent System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ AI Agent System: FAILED - {e}")
        return False

def test_file_operations():
    """Test file system operations"""
    print("🧪 Testing File Operations...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test current directory
        cli.do_pwd("")
        
        # Test directory listing
        cli.do_ls("")
        
        # Test file finding
        cli.do_find("*.py")
        
        # Test file content display (with a safe file)
        cli.do_cat(__file__)
        
        print("✅ File Operations: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ File Operations: FAILED - {e}")
        return False

def test_resonance_engine():
    """Test resonance analysis and energy management"""
    print("🧪 Testing Resonance Engine...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Test resonance analysis
        cli.do_analyze("Test content for resonance analysis")
        
        # Test energy resonance
        cli.do_resonate("create new concept")
        
        # Test learning
        cli.do_learn("new concept")
        
        print("✅ Resonance Engine: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Resonance Engine: FAILED - {e}")
        return False

def test_discovery_system():
    """Test user discovery and matching"""
    print("🧪 Testing Discovery System...")
    
    try:
        # Create a new CLI instance for this test
        cli = LivingCodexCLI()
        
        # Create multiple users for testing
        cli.do_user("create Bob")
        cli.do_user("create Carol")
        
        # Test interest-based discovery
        cli.do_discover_users("programming")
        
        # Test location-based discovery
        cli.do_discover_users_location("programming", "New York")
        
        # Test resonance matching
        user_ids = list(cli.users.keys())
        if len(user_ids) >= 2:
            cli.do_resonance_match(user_ids[0], user_ids[1])
        
        print("✅ Discovery System: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Discovery System: FAILED - {e}")
        return False

def run_comprehensive_test_suite():
    """Run all test categories"""
    print("🚀 Living Codex CLI - Comprehensive Test Suite")
    print("=" * 60)
    
    test_functions = [
        test_ontology_system,
        test_user_management,
        test_asset_management,
        test_knowledge_operations,
        test_system_features,
        test_ai_agent_system,
        test_file_operations,
        test_resonance_engine,
        test_discovery_system
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
    print(f"📊 Test Results: {passed} PASSED, {failed} FAILED")
    
    if failed == 0:
        print("🎉 All tests passed! CLI is fully functional.")
        return True
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = run_comprehensive_test_suite()
    sys.exit(0 if success else 1)
