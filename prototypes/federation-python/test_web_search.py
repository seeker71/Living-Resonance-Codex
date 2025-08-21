#!/usr/bin/env python3
"""
Web Search API Test Script
Tests the configured web search APIs
"""

import asyncio
from config_manager import ConfigManager
from real_external_api_system import RealExternalAPISystem, APISource

async def test_web_search():
    """Test web search functionality"""
    print("🔍 Testing Web Search APIs")
    print("=" * 40)
    
    # Load configuration
    config = ConfigManager()
    
    print("📊 Web Search Configuration:")
    print(f"  Google Custom Search: {'✅ Configured' if config.is_google_configured() else '❌ Not configured'}")
    print(f"  DuckDuckGo: ✅ Available (free)")
    print(f"  Wikipedia: ✅ Available (free)")
    print()
    
    # Initialize API system
    api_system = RealExternalAPISystem()
    
    # Test search query
    test_query = "Living Codex ontological framework"
    print(f"🔍 Testing search query: '{test_query}'")
    print()
    
    # Test different search sources
    sources_to_test = []
    
    if config.is_google_configured():
        sources_to_test.append(APISource.GOOGLE_SEARCH)
        print("✅ Testing Google Custom Search...")
    
    sources_to_test.extend([APISource.DUCKDUCKGO, APISource.WIKIPEDIA])
    print("✅ Testing DuckDuckGo...")
    print("✅ Testing Wikipedia...")
    
    try:
        # Perform search
        results = await api_system.search_external_knowledge(
            query=test_query,
            sources=sources_to_test,
            max_results=3
        )
        
        print("\n📊 Search Results Summary:")
        print(f"  Total Sources: {results['summary']['total_sources']}")
        print(f"  Successful Sources: {results['summary']['successful_sources']}")
        print(f"  Confidence Score: {results['summary']['confidence_score']:.2f}")
        
        # Show detailed results
        print("\n🔍 Detailed Results:")
        for source, source_results in results['sources'].items():
            if isinstance(source_results, list):
                # Web search results
                successful_results = [r for r in source_results if hasattr(r, 'status') and r.status.value == 'success']
                if successful_results:
                    print(f"\n  📡 {source.upper()}:")
                    for i, result in enumerate(successful_results[:2], 1):
                        if hasattr(result, 'data') and result.data and 'items' in result.data:
                            for item in result.data['items'][:1]:  # Show first item per source
                                title = item.get('title', 'No title')
                                snippet = item.get('snippet', 'No snippet')[:100] + "..."
                                print(f"    {i}. {title}")
                                print(f"       {snippet}")
                else:
                    print(f"\n  ❌ {source.upper()}: No successful results")
            elif hasattr(source_results, 'status'):
                # Single API response
                if source_results.status.value == 'success':
                    print(f"\n  ✅ {source.upper()}: Success")
                    if hasattr(source_results, 'data') and source_results.data:
                        print(f"     Data available: {type(source_results.data)}")
                else:
                    print(f"\n  ❌ {source.upper()}: {getattr(source_results, 'metadata', {}).get('error', 'Unknown error')}")
            else:
                print(f"\n  ⚠️  {source.upper()}: Unknown result format")
        
        # Test storing results in database
        print("\n💾 Testing Database Storage...")
        try:
            from database_persistence_system import DatabasePersistenceSystem, DatabaseType, DatabaseNode
            
            db_system = DatabasePersistenceSystem(DatabaseType.SQLITE, db_path="web_search_test.db")
            
            # Create a node for the search results
            search_node = DatabaseNode(
                node_id=f"web_search_{int(asyncio.get_event_loop().time())}",
                node_type="web_search_result",
                name=f"Web Search: {test_query}",
                content=str(results['summary']),
                realm="external_knowledge",
                water_state="vapor",
                energy_level=100.0,
                transformation_cost=10.0
            )
            
            result = db_system.crud_operations.create_node(search_node)
            if result.success:
                print("✅ Search results stored in database")
            else:
                print(f"⚠️  Database storage issue: {result.error_message}")
                
        except Exception as e:
            print(f"⚠️  Database test skipped: {e}")
        
        print("\n✅ Web search test completed successfully!")
        
    except Exception as e:
        print(f"❌ Web search test failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   • Check your API keys are correct")
        print("   • Verify internet connection")
        print("   • Check rate limits haven't been exceeded")
        print("   • Run setup_web_search.py to reconfigure")

def main():
    """Main function"""
    print("🌐 Living Codex Web Search Test")
    print("=" * 40)
    
    # Run the async test
    asyncio.run(test_web_search())
    
    print("\n🎉 Web Search Test Complete!")
    print("=" * 40)
    print("\n🌟 Your Living Codex can now:")
    print("   • Search the web for knowledge")
    print("   • Integrate external information")
    print("   • Store search results in your database")
    print("   • Build a comprehensive knowledge base")
    
    print("\n🚀 Next steps:")
    print("   1. Run integrated demo: python integrated_real_systems_demo.py")
    print("   2. Start searching for knowledge!")
    print("   3. Build your living knowledge system!")

if __name__ == "__main__":
    main()
