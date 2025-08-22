#!/usr/bin/env python3
"""
Unified Living Codex System Test Script
Combines all individual test scripts into a single comprehensive testing tool
"""

import asyncio
import sys
import time
from typing import List, Dict, Any, Optional
from config_manager import ConfigManager
from real_external_api_system import RealExternalAPISystem, APISource

class UnifiedSystemTester:
    """Unified system tester that runs all tests"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.test_results = {}
        self.start_time = time.time()
        
    def print_header(self, title: str, char: str = "="):
        """Print a formatted header"""
        print(f"\n{char * 60}")
        print(f"  {title}")
        print(f"{char * 60}")
    
    def print_section(self, title: str, char: str = "-"):
        """Print a formatted section header"""
        print(f"\n{char * 40}")
        print(f"  {title}")
        print(f"{char * 40}")
    
    def print_result(self, test_name: str, success: bool, message: str = ""):
        """Print a test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if message:
            print(f"     {message}")
        
        # Store result
        self.test_results[test_name] = {"success": success, "message": message}
    
    def test_configuration(self) -> bool:
        """Test system configuration"""
        self.print_section("Testing System Configuration")
        
        try:
            # Test OpenAI
            openai_configured = self.config.is_openai_configured()
            self.print_result("OpenAI API", openai_configured, 
                            "Configured" if openai_configured else "Not configured")
            
            # Test Google Custom Search
            google_configured = self.config.is_google_configured()
            self.print_result("Google Custom Search", google_configured,
                            "Configured" if google_configured else "Not configured")
            
            # Test Neo4j
            neo4j_configured = self.config.is_neo4j_configured()
            self.print_result("Neo4j Database", neo4j_configured,
                            "Configured" if neo4j_configured else "Not configured")
            
            # Test PostgreSQL
            postgres_configured = self.config.is_postgres_configured()
            self.print_result("PostgreSQL Database", postgres_configured,
                            "Configured" if postgres_configured else "Optional")
            
            return True
            
        except Exception as e:
            self.print_result("Configuration Test", False, f"Error: {e}")
            return False
    
    async def test_neo4j_connection(self) -> bool:
        """Test Neo4j connection and basic operations"""
        self.print_section("Testing Neo4j Integration")
        
        try:
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
                self.print_result("Neo4j Connection", False, "Failed to connect")
                return False
            
            self.print_result("Neo4j Connection", True, "Successfully connected")
            
            # Test node creation
            test_node = GraphNode(
                node_id="unified_test_node",
                labels=["TestNode", "UnifiedTest"],
                properties={
                    "name": "Unified System Test",
                    "description": "Testing Neo4j integration",
                    "timestamp": datetime.now().isoformat(),
                    "status": "active"
                },
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            result = neo4j.graph_operations.create_node(test_node)
            if result.success:
                self.print_result("Neo4j Node Creation", True, "Test node created")
            else:
                self.print_result("Neo4j Node Creation", False, result.error_message)
            
            # Test querying
            query_result = neo4j.graph_operations.query_graph(
                "MATCH (n:TestNode) RETURN n.name as name, n.status as status"
            )
            if query_result.success:
                self.print_result("Neo4j Query", True, f"Found {len(query_result.data)} nodes")
            else:
                self.print_result("Neo4j Query", False, query_result.error_message)
            
            return True
            
        except Exception as e:
            self.print_result("Neo4j Integration", False, f"Error: {e}")
            return False
    
    async def test_database_persistence(self) -> bool:
        """Test database persistence system"""
        self.print_section("Testing Database Persistence")
        
        try:
            from database_persistence_system import DatabasePersistenceSystem, DatabaseType, DatabaseNode
            
            # Initialize database system
            db_system = DatabasePersistenceSystem(DatabaseType.SQLITE, db_path="unified_test.db")
            self.print_result("Database Initialization", True, "SQLite system ready")
            
            # Test node creation
            test_db_node = DatabaseNode(
                node_id="unified_test_db_node",
                node_type="test_node",
                name="Database Test Node",
                content="Testing database persistence",
                realm="test",
                water_state="liquid",
                energy_level=100.0,
                transformation_cost=10.0
            )
            
            result = db_system.crud_operations.create_node(test_db_node)
            if result.success:
                self.print_result("Database Node Creation", True, "Test node created")
            else:
                self.print_result("Database Node Creation", False, result.error_message)
            
            # Test querying
            query_result = db_system.crud_operations.query_nodes([
                ("node_type", "=", "test_node")
            ])
            if query_result.success:
                self.print_result("Database Query", True, f"Found {len(query_result.data)} nodes")
            else:
                self.print_result("Database Query", False, query_result.error_message)
            
            return True
            
        except Exception as e:
            self.print_result("Database Persistence", False, f"Error: {e}")
            return False
    
    async def test_web_search(self) -> bool:
        """Test web search APIs"""
        self.print_section("Testing Web Search APIs")
        
        try:
            # Initialize API system
            api_system = RealExternalAPISystem()
            
            # Test query
            test_query = "Living Codex ontological framework"
            print(f"🔍 Testing search: '{test_query}'")
            
            # Determine sources to test
            sources_to_test = []
            if self.config.is_google_configured():
                sources_to_test.append(APISource.GOOGLE_SEARCH)
                print("✅ Testing Google Custom Search...")
            
            sources_to_test.extend([APISource.DUCKDUCKGO, APISource.WIKIPEDIA])
            print("✅ Testing DuckDuckGo...")
            print("✅ Testing Wikipedia...")
            
            # Perform search
            results = await api_system.search_external_knowledge(
                query=test_query,
                sources=sources_to_test,
                max_results=3
            )
            
            # Analyze results
            total_sources = results['summary']['total_sources']
            successful_sources = results['summary']['successful_sources']
            confidence_score = results['summary']['confidence_score']
            
            print(f"\n📊 Search Results:")
            print(f"  Total Sources: {total_sources}")
            print(f"  Successful Sources: {successful_sources}")
            print(f"  Confidence Score: {confidence_score:.2f}")
            
            # Test individual sources
            for source, source_results in results['sources'].items():
                if isinstance(source_results, list):
                    # Web search results
                    successful_results = [r for r in source_results if hasattr(r, 'status') and r.status.value == 'success']
                    if successful_results:
                        self.print_result(f"Web Search ({source})", True, f"{len(successful_results)} results")
                    else:
                        self.print_result(f"Web Search ({source})", False, "No successful results")
                        
                elif hasattr(source_results, 'status'):
                    # Single API response
                    if source_results.status.value == 'success':
                        self.print_result(f"API ({source})", True, "Success")
                    else:
                        error = getattr(source_results, 'metadata', {}).get('error', 'Unknown error')
                        self.print_result(f"API ({source})", False, error)
            
            return successful_sources > 0
            
        except Exception as e:
            self.print_result("Web Search", False, f"Error: {e}")
            return False
    
    async def test_openai_integration(self) -> bool:
        """Test OpenAI integration"""
        self.print_section("Testing OpenAI Integration")
        
        try:
            if not self.config.is_openai_configured():
                self.print_result("OpenAI Test", False, "OpenAI not configured")
                return False
            
            # Initialize API system
            api_system = RealExternalAPISystem()
            
            # Test query
            test_query = "What are the key principles of ontological frameworks in knowledge systems?"
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
                    self.print_result("OpenAI Consultation", True, "AI response received")
                    
                    # Show response details
                    if hasattr(expert_response, 'data') and expert_response.data:
                        if 'choices' in expert_response.data:
                            content = expert_response.data['choices'][0]['message']['content']
                            print(f"💡 AI Response: {content[:200]}...")
                            
                            # Show metadata
                            if hasattr(expert_response, 'metadata') and expert_response.metadata:
                                tokens_used = expert_response.metadata.get('tokens_used', 'N/A')
                                response_time = getattr(expert_response, 'response_time', 0)
                                print(f"📊 Tokens: {tokens_used}, Time: {response_time:.2f}s")
                    
                    return True
                else:
                    error = getattr(expert_response, 'metadata', {}).get('error', 'Unknown error')
                    self.print_result("OpenAI Consultation", False, error)
                    return False
            else:
                self.print_result("OpenAI Integration", False, "No expert_system in results")
                return False
                
        except Exception as e:
            self.print_result("OpenAI Integration", False, f"Error: {e}")
            return False
    
    async def test_comprehensive_integration(self) -> bool:
        """Test all systems working together"""
        self.print_section("Testing Comprehensive Integration")
        
        try:
            # Initialize API system
            api_system = RealExternalAPISystem()
            
            # Test query that benefits from multiple sources
            test_query = "Living Codex ontological framework fractal systems"
            print(f"🔍 Testing comprehensive search: '{test_query}'")
            
            # Test with all available sources
            sources_to_test = []
            
            if self.config.is_google_configured():
                sources_to_test.append(APISource.GOOGLE_SEARCH)
            
            sources_to_test.extend([APISource.DUCKDUCKGO, APISource.WIKIPEDIA])
            
            if self.config.is_openai_configured():
                sources_to_test.append(APISource.OPENAI)
            
            print(f"✅ Testing {len(sources_to_test)} sources...")
            
            # Perform comprehensive search
            results = await api_system.search_external_knowledge(
                query=test_query,
                sources=sources_to_test,
                max_results=5
            )
            
            # Analyze comprehensive results
            total_sources = results['summary']['total_sources']
            successful_sources = results['summary']['successful_sources']
            total_items = results['summary']['total_items']
            confidence_score = results['summary']['confidence_score']
            
            print(f"\n📊 Comprehensive Results:")
            print(f"  Total Sources: {total_sources}")
            print(f"  Successful Sources: {successful_sources}")
            print(f"  Total Items: {total_items}")
            print(f"  Confidence Score: {confidence_score:.2f}")
            
            # Test data flow between systems
            if successful_sources > 0:
                self.print_result("Comprehensive Integration", True, 
                                f"{successful_sources}/{total_sources} sources working")
                
                # Show key insights
                if results['summary']['key_insights']:
                    print(f"\n💡 Key Insights Available:")
                    for i, insight in enumerate(results['summary']['key_insights'][:2], 1):
                        print(f"  {i}. [{insight['source']}] {insight['title']}")
                        print(f"     {insight['content']}")
                
                return True
            else:
                self.print_result("Comprehensive Integration", False, "No sources working")
                return False
                
        except Exception as e:
            self.print_result("Comprehensive Integration", False, f"Error: {e}")
            return False
    
    def print_summary(self):
        """Print test summary"""
        self.print_header("Test Summary")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results.values() if result['success'])
        failed_tests = total_tests - passed_tests
        
        print(f"📊 Test Results:")
        print(f"  Total Tests: {total_tests}")
        print(f"  Passed: {passed_tests} ✅")
        print(f"  Failed: {failed_tests} ❌")
        print(f"  Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        # Show failed tests
        if failed_tests > 0:
            print(f"\n❌ Failed Tests:")
            for test_name, result in self.test_results.items():
                if not result['success']:
                    print(f"  • {test_name}: {result['message']}")
        
        # Overall status
        if failed_tests == 0:
            print(f"\n🎉 All tests passed! Your Living Codex is fully operational!")
        else:
            print(f"\n⚠️  Some tests failed. Check the configuration and try again.")
        
        # Show test duration
        duration = time.time() - self.start_time
        print(f"\n⏱️  Total test duration: {duration:.2f} seconds")
    
    async def run_all_tests(self) -> bool:
        """Run all tests"""
        self.print_header("Living Codex Unified System Test")
        print("Running comprehensive system validation...")
        
        # Run all tests
        tests = [
            ("Configuration", self.test_configuration),
            ("Neo4j Integration", self.test_neo4j_connection),
            ("Database Persistence", self.test_database_persistence),
            ("Web Search APIs", self.test_web_search),
            ("OpenAI Integration", self.test_openai_integration),
            ("Comprehensive Integration", self.test_comprehensive_integration)
        ]
        
        for test_name, test_func in tests:
            try:
                if asyncio.iscoroutinefunction(test_func):
                    await test_func()
                else:
                    test_func()
            except Exception as e:
                self.print_result(test_name, False, f"Test error: {e}")
        
        # Print summary
        self.print_summary()
        
        # Return overall success
        return all(result['success'] for result in self.test_results.values())

async def main():
    """Main function"""
    print("🌟 Living Codex Unified System Test")
    print("=" * 60)
    
    # Create tester
    tester = UnifiedSystemTester()
    
    # Run all tests
    success = await tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    asyncio.run(main())
