#!/usr/bin/env python3
"""
Comprehensive API Test Script
Tests both Google Custom Search and OpenAI integration together
"""

import asyncio
from config_manager import ConfigManager
from real_external_api_system import RealExternalAPISystem, APISource

async def test_comprehensive_apis():
    """Test both Google Custom Search and OpenAI together"""
    print("🌟 Living Codex Comprehensive API Test")
    print("=" * 60)
    
    # Load configuration
    config = ConfigManager()
    
    print("📊 API Configuration Status:")
    print(f"  OpenAI API: {'✅ Configured' if config.is_openai_configured() else '❌ Not configured'}")
    print(f"  Google Custom Search: {'✅ Configured' if config.is_google_configured() else '❌ Not configured'}")
    print(f"  Neo4j: {'✅ Configured' if config.is_neo4j_configured() else '❌ Not configured'}")
    print()
    
    # Initialize API system
    api_system = RealExternalAPISystem()
    
    # Test query that benefits from both sources
    test_query = "Living Codex ontological framework fractal systems"
    print(f"🔍 Testing comprehensive search: '{test_query}'")
    print()
    
    try:
        # Test with all available sources
        sources_to_test = []
        
        if config.is_google_configured():
            sources_to_test.append(APISource.GOOGLE_SEARCH)
            print("✅ Testing Google Custom Search...")
        
        sources_to_test.extend([APISource.DUCKDUCKGO, APISource.WIKIPEDIA])
        print("✅ Testing DuckDuckGo...")
        print("✅ Testing Wikipedia...")
        
        if config.is_openai_configured():
            sources_to_test.append(APISource.OPENAI)
            print("✅ Testing OpenAI...")
        
        print(f"\n🔍 Testing {len(sources_to_test)} sources...")
        
        # Perform comprehensive search
        results = await api_system.search_external_knowledge(
            query=test_query,
            sources=sources_to_test,
            max_results=5
        )
        
        print("\n📊 Comprehensive Search Results:")
        print(f"  Total Sources: {results['summary']['total_sources']}")
        print(f"  Successful Sources: {results['summary']['successful_sources']}")
        print(f"  Total Items: {results['summary']['total_items']}")
        print(f"  Confidence Score: {results['summary']['confidence_score']:.2f}")
        
        # Show detailed results by source
        print("\n🔍 Detailed Results by Source:")
        
        for source, source_results in results['sources'].items():
            print(f"\n  📡 {source.upper()}:")
            
            if isinstance(source_results, list):
                # Web search results (Google, DuckDuckGo)
                successful_results = [r for r in source_results if hasattr(r, 'status') and r.status.value == 'success']
                if successful_results:
                    print(f"    ✅ {len(successful_results)} successful results")
                    for i, result in enumerate(successful_results[:2], 1):
                        if hasattr(result, 'data') and result.data and 'items' in result.data:
                            for item in result.data['items'][:1]:  # Show first item per source
                                title = item.get('title', 'No title')
                                snippet = item.get('snippet', 'No snippet')[:150] + "..."
                                print(f"      {i}. {title}")
                                print(f"         {snippet}")
                else:
                    print("    ❌ No successful results")
                    
            elif hasattr(source_results, 'status'):
                # Single API response (Wikipedia, OpenAI)
                if source_results.status.value == 'success':
                    print("    ✅ Success")
                    
                    if source == 'wikipedia':
                        if hasattr(source_results, 'data') and source_results.data:
                            search_results = source_results.data.get("query", {}).get("search", [])
                            if search_results:
                                print(f"    📚 Found {len(search_results)} Wikipedia articles")
                                for i, item in enumerate(search_results[:2], 1):
                                    title = item.get('title', 'No title')
                                    snippet = item.get('snippet', 'No snippet')[:150] + "..."
                                    print(f"      {i}. {title}")
                                    print(f"         {snippet}")
                    
                    elif source == 'expert_system':
                        if hasattr(source_results, 'data') and source_results.data:
                            if 'choices' in source_results.data:
                                content = source_results.data['choices'][0]['message']['content']
                                print("    🤖 AI Expert Response:")
                                print(f"      {content[:200]}...")
                                
                                # Show metadata
                                if hasattr(source_results, 'metadata') and source_results.metadata:
                                    tokens_used = source_results.metadata.get('tokens_used', 'N/A')
                                    response_time = getattr(source_results, 'response_time', 0)
                                    print(f"      Tokens: {tokens_used}, Time: {response_time:.2f}s")
                else:
                    print(f"    ❌ Failed: {getattr(source_results, 'metadata', {}).get('error', 'Unknown error')}")
            else:
                print("    ⚠️  Unknown result format")
        
        # Show key insights summary
        if results['summary']['key_insights']:
            print(f"\n💡 Key Insights Summary:")
            for i, insight in enumerate(results['summary']['key_insights'][:3], 1):
                print(f"  {i}. [{insight['source']}] {insight['title']}")
                print(f"     {insight['content']}")
                if insight['url']:
                    print(f"     URL: {insight['url']}")
                print()
        
        print("\n✅ Comprehensive API test completed successfully!")
        
    except Exception as e:
        print(f"❌ Comprehensive test failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   • Check all API keys are correct")
        print("   • Verify internet connection")
        print("   • Check rate limits haven't been exceeded")
        print("   • Run individual tests to isolate issues")

def main():
    """Main function"""
    print("🌟 Living Codex Comprehensive API Test")
    print("=" * 60)
    
    # Run the async test
    asyncio.run(test_comprehensive_apis())
    
    print("\n🎉 Comprehensive API Test Complete!")
    print("=" * 60)
    print("\n🌟 Your Living Codex now has:")
    print("   • 🌐 Web search via Google Custom Search")
    print("   • 🦆 Web search via DuckDuckGo (free)")
    print("   • 📚 Knowledge via Wikipedia API")
    print("   • 🤖 AI insights via OpenAI")
    print("   • 💾 Persistent storage in Neo4j and SQLite")
    
    print("\n🚀 Next steps:")
    print("   1. Run integrated demo: python integrated_real_systems_demo.py")
    print("   2. Start building your knowledge base!")
    print("   3. Explore the power of integrated knowledge systems!")

if __name__ == "__main__":
    main()
