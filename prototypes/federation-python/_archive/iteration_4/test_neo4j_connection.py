#!/usr/bin/env python3
"""
Test Neo4j Connection using Config Manager
"""

from config_manager import ConfigManager
from neo4j_integration_system import Neo4jIntegrationSystem

def test_neo4j_connection():
    """Test Neo4j connection using config manager"""
    print("🔧 Testing Neo4j Connection")
    print("=" * 40)
    
    # Load configuration
    config = ConfigManager()
    
    print(f"Neo4j URI: {config.db_config.neo4j_uri}")
    print(f"Neo4j Username: {config.db_config.neo4j_username}")
    print(f"Neo4j Password: {config.db_config.neo4j_password[:10]}..." if config.db_config.neo4j_password else "None")
    
    # Test connection with explicit credentials
    try:
        neo4j = Neo4jIntegrationSystem(
            uri=config.db_config.neo4j_uri,
            username=config.db_config.neo4j_username,
            password=config.db_config.neo4j_password
        )
        
        if neo4j.connection_manager.is_connected():
            print("✅ Neo4j connection successful!")
            
            # Test basic operations
            print("\n🧪 Testing basic operations...")
            
            # Test creating a test node
            from neo4j_integration_system import GraphNode
            from datetime import datetime
            
            test_node = GraphNode(
                node_id="test_node_001",
                labels=["TestNode"],
                properties={"name": "Living Codex Test", "created": datetime.now().isoformat()},
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            result = neo4j.graph_operations.create_node(test_node)
            if result.success:
                print("✅ Test node created successfully")
            else:
                print(f"❌ Failed to create test node: {result.error_message}")
            
            # Test querying the test node
            query_result = neo4j.graph_operations.query_graph("MATCH (n:TestNode) RETURN n LIMIT 5")
            if query_result.success:
                print("✅ Test query successful")
                print(f"   Found {len(query_result.data)} test nodes")
            else:
                print(f"❌ Test query failed: {query_result.error_message}")
            
        else:
            print("❌ Neo4j connection failed")
            
    except Exception as e:
        print(f"❌ Error testing Neo4j: {e}")

if __name__ == "__main__":
    test_neo4j_connection()
