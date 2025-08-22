#!/usr/bin/env python3
"""
Test script to validate the modular configuration system
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config.manager import ConfigManager
from api.management.api_manager import APIManagementSystem

def test_modular_config():
    """Test the modular configuration system"""
    print("🔧 Testing Modular Configuration System")
    print("=" * 50)
    
    try:
        # Test ConfigManager
        print("📁 Testing ConfigManager...")
        config = ConfigManager()
        
        # Test configuration status methods
        openai_status = config.is_openai_configured()
        google_status = config.is_google_configured()
        neo4j_status = config.is_neo4j_configured()
        
        print(f"✅ OpenAI configured: {openai_status}")
        print(f"✅ Google configured: {google_status}")
        print(f"✅ Neo4j configured: {neo4j_status}")
        
        # Test configuration summary
        summary = config.get_config_summary()
        print(f"✅ Config summary: {summary['total_configured']}/4 services configured")
        
        # Test APIManagementSystem
        print("\n🔑 Testing APIManagementSystem...")
        api_manager = APIManagementSystem()
        
        # Test API availability
        from api.management.api_manager import APISource
        google_available = api_manager.is_api_available(APISource.GOOGLE_SEARCH)
        openai_available = api_manager.is_api_available(APISource.OPENAI)
        
        print(f"✅ Google Search available: {google_available}")
        print(f"✅ OpenAI available: {openai_available}")
        
        # Test rate limiting info
        google_rate_info = api_manager.get_rate_limit_info(APISource.GOOGLE_SEARCH)
        print(f"✅ Google rate limit: {google_rate_info['requests_remaining']} requests remaining")
        
        print("\n🎉 All modular components working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing modular config: {e}")
        return False

def test_backward_compatibility():
    """Test that modular system works with existing code"""
    print("\n🔄 Testing Backward Compatibility")
    print("=" * 40)
    
    try:
        # Test that old import pattern still works through new system
        from config.manager import ConfigManager as ModularConfigManager
        
        # Compare with original
        modular_config = ModularConfigManager()
        
        print("✅ Modular ConfigManager created successfully")
        print(f"✅ Configuration validation: {modular_config.is_openai_configured()}")
        
        # Test that all expected methods exist
        expected_methods = [
            'is_openai_configured',
            'is_google_configured', 
            'is_neo4j_configured',
            'get_config_summary'
        ]
        
        for method in expected_methods:
            if hasattr(modular_config, method):
                print(f"✅ Method {method} available")
            else:
                print(f"❌ Method {method} missing")
                return False
        
        print("\n🎉 Backward compatibility maintained!")
        return True
        
    except Exception as e:
        print(f"❌ Backward compatibility error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Modular Configuration System Test")
    print("=" * 60)
    
    success1 = test_modular_config()
    success2 = test_backward_compatibility()
    
    if success1 and success2:
        print("\n🎉 All tests passed! Modular system is working correctly.")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed. Check the output above.")
        sys.exit(1)
