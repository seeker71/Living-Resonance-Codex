#!/usr/bin/env python3
"""
Modular Living Codex System Test Script
Uses the new testing framework for better organization and maintainability
"""

import asyncio
import sys
import argparse
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from testing.framework.test_runner import TestRunner
from testing.framework.test_reporter import TestReporter
from config.manager import ConfigManager

class ModularSystemTester:
    """Modular system tester using the new testing framework"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.test_runner = TestRunner()
        self.reporter = TestReporter()
        
    def setup_tests(self):
        """Setup all test functions"""
        # Configuration tests
        self.test_runner.add_test("configuration", self.test_configuration)
        
        # Database tests
        self.test_runner.add_test("neo4j_integration", self.test_neo4j_connection, async_func=True)
        self.test_runner.add_test("database_persistence", self.test_database_persistence, async_func=True)
        
        # API tests
        self.test_runner.add_test("web_search", self.test_web_search, async_func=True)
        self.test_runner.add_test("openai_integration", self.test_openai_integration, async_func=True)
        
        # Integration tests
        self.test_runner.add_test("comprehensive_integration", self.test_comprehensive_integration, async_func=True)
    
    def test_configuration(self) -> bool:
        """Test system configuration"""
        try:
            # Test OpenAI
            openai_configured = self.config.is_openai_configured()
            if not openai_configured:
                print("⚠️  OpenAI API key not configured")
            
            # Test Google Custom Search
            google_configured = self.config.is_google_configured()
            if not google_configured:
                print("ℹ️  Google Custom Search not configured (will use DuckDuckGo)")
            
            # Test Neo4j
            neo4j_configured = self.config.is_neo4j_configured()
            if not neo4j_configured:
                print("⚠️  Neo4j password not configured")
            
            # Test PostgreSQL
            postgres_configured = self.config.is_postgres_configured()
            if not postgres_configured:
                print("ℹ️  PostgreSQL not configured (will use SQLite)")
            
            # Return success if at least basic services are configured
            return openai_configured or neo4j_configured
            
        except Exception as e:
            print(f"❌ Configuration test error: {e}")
            return False
    
    async def test_neo4j_connection(self) -> bool:
        """Test Neo4j connection and basic operations"""
        try:
            if not self.config.is_neo4j_configured():
                print("⚠️  Neo4j not configured, skipping test")
                return True
            
            from neo4j_integration_system import Neo4jIntegrationSystem, GraphNode
            from datetime import datetime
            
            # Initialize Neo4j system
            neo4j = Neo4jIntegrationSystem(
                uri=self.config.db_config.neo4j_uri,
                username=self.config.db_config.neo4j_username,
                password=self.config.db_config.neo4j_password
            )
            
            # Test connection
            if not neo4j.connection_manager.is_connected():
                print("❌ Neo4j connection failed")
                return False
            
            print("✅ Neo4j connection successful")
            return True
            
        except Exception as e:
            print(f"❌ Neo4j test error: {e}")
            return False
    
    async def test_database_persistence(self) -> bool:
        """Test database persistence system"""
        try:
            from database_persistence_system import DatabasePersistenceSystem, DatabaseType, DatabaseNode
            
            # Initialize database system
            db_system = DatabasePersistenceSystem(DatabaseType.SQLITE, db_path="modular_test.db")
            print("✅ Database system initialized")
            
            # Test node creation
            test_db_node = DatabaseNode(
                node_id="modular_test_db_node",
                node_type="test_node",
                name="Modular Test Node",
                content="Testing modular database persistence",
                realm="test",
                water_state="liquid",
                energy_level=100.0,
                transformation_cost=10.0
            )
            
            result = db_system.crud_operations.create_node(test_db_node)
            if result.success:
                print("✅ Test node created in database")
                return True
            else:
                print(f"❌ Database node creation failed: {result.error_message}")
                return False
                
        except Exception as e:
            print(f"❌ Database test error: {e}")
            return False
    
    async def test_web_search(self) -> bool:
        """Test web search APIs"""
        try:
            from real_external_api_system import RealExternalAPISystem, APISource
            
            # Initialize API system
            api_system = RealExternalAPISystem()
            
            # Test query
            test_query = "Living Codex ontological framework"
            print(f"🔍 Testing web search: '{test_query}'")
            
            # Determine sources to test
            sources_to_test = []
            if self.config.is_google_configured():
                sources_to_test.append(APISource.GOOGLE_SEARCH)
            
            sources_to_test.extend([APISource.DUCKDUCKGO, APISource.WIKIPEDIA])
            
            # Perform search
            results = await api_system.search_external_knowledge(
                query=test_query,
                sources=sources_to_test,
                max_results=3
            )
            
            # Check results
            successful_sources = results['summary']['successful_sources']
            if successful_sources > 0:
                print(f"✅ Web search successful: {successful_sources} sources working")
                return True
            else:
                print("❌ Web search failed: no sources working")
                return False
                
        except Exception as e:
            print(f"❌ Web search test error: {e}")
            return False
    
    async def test_openai_integration(self) -> bool:
        """Test OpenAI integration"""
        try:
            if not self.config.is_openai_configured():
                print("⚠️  OpenAI not configured, skipping test")
                return True
            
            from real_external_api_system import RealExternalAPISystem, APISource
            
            # Initialize API system
            api_system = RealExternalAPISystem()
            
            # Test query
            test_query = "What are the key principles of ontological frameworks?"
            print(f"🤖 Testing OpenAI: '{test_query[:50]}...'")
            
            # Perform OpenAI consultation
            results = await api_system.search_external_knowledge(
                query=test_query,
                sources=[APISource.OPENAI],
                max_results=1
            )
            
            # Check results
            if 'expert_system' in results['sources']:
                expert_response = results['sources']['expert_system']
                if expert_response.status.value == 'success':
                    print("✅ OpenAI consultation successful")
                    return True
                else:
                    print(f"❌ OpenAI consultation failed: {expert_response.status.value}")
                    return False
            else:
                print("❌ No expert system response received")
                return False
                
        except Exception as e:
            print(f"❌ OpenAI test error: {e}")
            return False
    
    async def test_comprehensive_integration(self) -> bool:
        """Test all systems working together"""
        try:
            from real_external_api_system import RealExternalAPISystem, APISource
            
            # Initialize API system
            api_system = RealExternalAPISystem()
            
            # Test query
            test_query = "Living Codex ontological framework fractal systems"
            print(f"🔍 Testing comprehensive integration: '{test_query}'")
            
            # Test with all available sources
            sources_to_test = []
            
            if self.config.is_google_configured():
                sources_to_test.append(APISource.GOOGLE_SEARCH)
            
            sources_to_test.extend([APISource.DUCKDUCKGO, APISource.WIKIPEDIA])
            
            if self.config.is_openai_configured():
                sources_to_test.append(APISource.OPENAI)
            
            # Perform comprehensive search
            results = await api_system.search_external_knowledge(
                query=test_query,
                sources=sources_to_test,
                max_results=5
            )
            
            # Check results
            successful_sources = results['summary']['successful_sources']
            total_sources = results['summary']['total_sources']
            
            if successful_sources > 0:
                print(f"✅ Comprehensive integration successful: {successful_sources}/{total_sources} sources working")
                return True
            else:
                print("❌ Comprehensive integration failed: no sources working")
                return False
                
        except Exception as e:
            print(f"❌ Comprehensive integration test error: {e}")
            return False
    
    async def run_tests(self, component: str = None) -> bool:
        """Run tests with optional component filtering"""
        self.setup_tests()
        
        if component:
            # Run specific component test
            if component in self.test_runner._tests:
                self.reporter.print_header(f"Testing {component.title()}")
                result = await self.test_runner.run_test(component)
                self.reporter.print_test_result(component, result)
                return result.status.value == "passed"
            else:
                print(f"❌ Component '{component}' not found")
                print(f"Available components: {list(self.test_runner._tests.keys())}")
                return False
        else:
            # Run all tests
            self.reporter.print_header("Living Codex Modular System Test")
            print("Running comprehensive system validation...")
            
            await self.test_runner.run_all_tests()
            
            # Print results
            summary = self.test_runner.get_summary()
            self.reporter.print_performance_metrics(summary)
            self.reporter.print_failure_details(self.test_runner.test_results)
            self.reporter.print_success_message(summary)
            
            return summary.get('success_rate', 0) == 100.0

async def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Living Codex Modular System Test")
    parser.add_argument("--component", "-c", type=str, 
                       help="Test specific component only")
    parser.add_argument("--list", "-l", action="store_true",
                       help="List available test components")
    
    args = parser.parse_args()
    
    if args.list:
        print("Available test components:")
        print("  • configuration      - System configuration validation")
        print("  • neo4j_integration - Neo4j database integration")
        print("  • database_persistence - Database persistence system")
        print("  • web_search        - Web search API integration")
        print("  • openai_integration - OpenAI AI service integration")
        print("  • comprehensive_integration - All systems working together")
        return
    
    # Create tester
    tester = ModularSystemTester()
    
    # Run tests
    success = await tester.run_tests(args.component)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    asyncio.run(main())
