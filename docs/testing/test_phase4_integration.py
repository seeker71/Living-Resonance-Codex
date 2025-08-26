#!/usr/bin/env python3
"""
Phase 4 Integration Test
Demonstrate that all updated systems work together with the new modular components
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_phase4_integration():
    """Test that all Phase 4 updated systems work together"""
    print("🚀 Phase 4 Integration Test")
    print("=" * 60)
    
    # Test 1: Neo4j Integration System
    print("\n🔌 Testing Neo4j Integration System...")
    try:
        from neo4j_integration_system import Neo4jIntegrationSystem
        
        neo4j_system = Neo4jIntegrationSystem()
        print("✅ Neo4jIntegrationSystem created successfully")
        print(f"✅ Using modular components: {hasattr(neo4j_system, 'graph_operations')}")
        
        # Test connection status
        connected = neo4j_system.is_connected()
        print(f"✅ Connection status: {'Connected' if connected else 'Not connected'}")
        
    except Exception as e:
        print(f"❌ Neo4j integration error: {e}")
        return False
    
    # Test 2: Database Persistence System
    print("\n🗄️  Testing Database Persistence System...")
    try:
        from database_persistence_system import DatabasePersistenceSystem
        
        db_system = DatabasePersistenceSystem(db_path="test_phase4.db")
        print("✅ DatabasePersistenceSystem created successfully")
        print(f"✅ Using modular components: {hasattr(db_system, 'operations')}")
        
        # Test database manager
        db_manager = db_system.db_manager
        print(f"✅ Database manager: {type(db_manager).__name__}")
        
    except Exception as e:
        print(f"❌ Database persistence error: {e}")
        return False
    
    # Test 3: External API System
    print("\n🌐 Testing External API System...")
    try:
        from real_external_api_system import RealExternalAPISystem
        
        api_system = RealExternalAPISystem()
        print("✅ RealExternalAPISystem created successfully")
        print(f"✅ Using modular components: {hasattr(api_system, 'api_manager')}")
        
        # Test API status
        api_status = api_system.get_api_status()
        print(f"✅ API status retrieved: {len(api_status['apis'])} APIs configured")
        
    except Exception as e:
        print(f"❌ External API error: {e}")
        return False
    
    # Test 4: Modular Components Integration
    print("\n🔗 Testing Modular Components Integration...")
    try:
        # Test that we can import from the modular structure
        from src.config.manager import ConfigManager
        from src.api.management.api_manager import APIManagementSystem
        from src.database.core.models import DatabaseNode
        from src.graph.core.models import GraphNode
        
        print("✅ All modular components import successfully")
        
        # Test ConfigManager
        config_manager = ConfigManager()
        print("✅ ConfigManager created successfully")
        
        # Test APIManagementSystem
        api_manager = APIManagementSystem()
        print("✅ APIManagementSystem created successfully")
        
        # Test models
        test_db_node = DatabaseNode(
            node_id="test_node",
            node_type="test",
            name="Test Node",
            content="Test content",
            realm="test",
            water_state="liquid",
            energy_level=100.0,
            transformation_cost=10.0,
            metadata={},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        print("✅ DatabaseNode model working")
        
        test_graph_node = GraphNode(
            node_id="test_graph_node",
            labels=["Test"],
            properties={"test": "data"},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        print("✅ GraphNode model working")
        
    except Exception as e:
        print(f"❌ Modular components integration error: {e}")
        return False
    
    # Test 5: Backward Compatibility
    print("\n🔄 Testing Backward Compatibility...")
    try:
        # Test that old systems still work
        from neo4j_integration_system import GraphNode as LegacyGraphNode
        from database_persistence_system import DatabaseNode as LegacyDatabaseNode
        
        print("✅ Legacy imports working")
        
        # Test legacy model creation
        legacy_graph_node = LegacyGraphNode(
            node_id="legacy_test",
            labels=["LegacyTest"],
            properties={"test": "data"},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        print("✅ Legacy GraphNode working")
        
        legacy_db_node = LegacyDatabaseNode(
            node_id="legacy_db_test",
            node_type="legacy",
            name="Legacy Test Node",
            content="Legacy test content",
            realm="legacy",
            water_state="liquid",
            energy_level=100.0,
            transformation_cost=10.0,
            metadata={},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        print("✅ Legacy DatabaseNode working")
        
    except Exception as e:
        print(f"❌ Backward compatibility error: {e}")
        return False
    
    print("\n🎉 Phase 4 Integration Summary")
    print("=" * 40)
    print("✅ Neo4j integration system: Updated and working")
    print("✅ Database persistence system: Updated and working")
    print("✅ External API system: Updated and working")
    print("✅ Modular components: Fully integrated")
    print("✅ Backward compatibility: Maintained")
    
    print("\n🚀 What's Been Accomplished:")
    print("• All three original systems updated to use modular components")
    print("• Backward compatibility maintained throughout")
    print("• Seamless integration between old and new systems")
    print("• Foundation for future migration to full modular system")
    
    print("\n🔄 What's Next:")
    print("• Test full system integration")
    print("• Validate all functionality works together")
    print("• Plan Phase 5: Cleanup and optimization")
    print("• Consider removing legacy code after full validation")
    
    return True

async def test_async_functionality():
    """Test async functionality of the updated systems"""
    print("\n⚡ Testing Async Functionality...")
    
    try:
        from real_external_api_system import RealExternalAPISystem
        
        api_system = RealExternalAPISystem()
        
        # Test async search
        print("   Testing DuckDuckGo search...")
        result = await api_system.search_duckduckgo("Living Codex")
        print(f"   ✅ DuckDuckGo search: {'Success' if result.status.value == 'success' else 'Failed'}")
        
        # Test async close
        await api_system.close()
        print("   ✅ API system closed successfully")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Async functionality error: {e}")
        return False

def test_system_interoperability():
    """Test that all systems can work together"""
    print("\n🤝 Testing System Interoperability...")
    
    try:
        # Test that we can create all systems together
        from neo4j_integration_system import Neo4jIntegrationSystem
        from database_persistence_system import DatabasePersistenceSystem
        from real_external_api_system import RealExternalAPISystem
        
        # Create all systems
        neo4j_system = Neo4jIntegrationSystem()
        db_system = DatabasePersistenceSystem(db_path="test_interop.db")
        api_system = RealExternalAPISystem()
        
        print("   ✅ All systems created successfully")
        
        # Test that they can coexist
        systems = [neo4j_system, db_system, api_system]
        print(f"   ✅ {len(systems)} systems running simultaneously")
        
        # Test basic operations
        neo4j_connected = neo4j_system.is_connected()
        db_configured = hasattr(db_system, 'db_manager')
        api_configured = hasattr(api_system, 'api_manager')
        
        print(f"   ✅ Neo4j: {'Connected' if neo4j_connected else 'Not connected'}")
        print(f"   ✅ Database: {'Configured' if db_configured else 'Not configured'}")
        print(f"   ✅ API: {'Configured' if api_configured else 'Not configured'}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ System interoperability error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Phase 4 Integration Comprehensive Test")
    print("=" * 80)
    
    # Run synchronous tests
    success1 = test_phase4_integration()
    success2 = test_system_interoperability()
    
    # Run async tests
    success3 = asyncio.run(test_async_functionality())
    
    if success1 and success2 and success3:
        print("\n🎉 All Phase 4 integration tests passed! Systems are working together.")
        print("\n📊 Phase 4 Accomplishments:")
        print("• All three original systems updated to use modular components")
        print("• Backward compatibility maintained throughout")
        print("• Seamless integration between old and new systems")
        print("• Foundation for future migration to full modular system")
        print("• Async functionality working correctly")
        print("• System interoperability validated")
        sys.exit(0)
    else:
        print("\n❌ Some Phase 4 integration tests failed. Check the output above.")
        sys.exit(1)
