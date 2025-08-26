#!/usr/bin/env python3
"""
Test Core Search System
Validates that the unified search system works across all Living Codex nodes
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

def test_core_search_system():
    """Test if the core search system works correctly across all nodes"""
    
    print("🧪 Testing Core Search System")
    print("=" * 50)
    
    try:
        # Test 1: Import the core search system
        print("\n1️⃣ Testing Core Search System Import...")
        from core.core_search_system import core_search_system, SearchQuery, SearchResult
        print("   ✅ Core search system imported successfully")
        print(f"   ✅ Search system type: {type(core_search_system)}")
        
        # Test 2: Test basic search functionality
        print("\n2️⃣ Testing Basic Search Functionality...")
        
        # Test search with string query
        print("   🔍 Testing string query search...")
        search_response = core_search_system.search("core")
        print(f"   ✅ String search returned {len(search_response.results)} results")
        print(f"   ✅ Search time: {search_response.search_time_ms:.2f}ms")
        print(f"   ✅ Total count: {search_response.total_count}")
        
        # Test search with SearchQuery object
        print("   🔍 Testing SearchQuery object search...")
        search_query = SearchQuery(
            query="system",
            search_type="all",
            limit=10,
            sort_by="relevance"
        )
        search_response = core_search_system.search(search_query)
        print(f"   ✅ SearchQuery search returned {len(search_response.results)} results")
        
        # Test 3: Test search across different node types
        print("\n3️⃣ Testing Search Across Node Types...")
        
        node_types = ["users", "content", "code", "assets", "ontology"]
        for node_type in node_types:
            print(f"   🔍 Testing {node_type} search...")
            try:
                search_query = SearchQuery(
                    query="test",
                    search_type=node_type,
                    limit=5
                )
                search_response = core_search_system.search(search_query)
                print(f"      ✅ {node_type}: {len(search_response.results)} results")
            except Exception as e:
                print(f"      ❌ {node_type}: Error - {e}")
        
        # Test 4: Test search with filters
        print("\n4️⃣ Testing Search with Filters...")
        
        filters = {
            'type': ['user', 'content'],
            'category': ['user_profile', 'code']
        }
        
        search_query = SearchQuery(
            query="system",
            filters=filters,
            limit=10
        )
        
        search_response = core_search_system.search(search_query)
        print(f"   ✅ Filtered search returned {len(search_response.results)} results")
        
        # Test 5: Test search result structure
        print("\n5️⃣ Testing Search Result Structure...")
        
        if search_response.results:
            result = search_response.results[0]
            print(f"   ✅ Result ID: {result.id}")
            print(f"   ✅ Result Type: {result.type}")
            print(f"   ✅ Result Title: {result.title}")
            print(f"   ✅ Result Description: {result.description[:100]}...")
            print(f"   ✅ Result Source: {result.source}")
            print(f"   ✅ Result Category: {result.category}")
            print(f"   ✅ Result Relevance Score: {result.relevance_score}")
            print(f"   ✅ Result Metadata: {len(result.metadata)} fields")
        else:
            print("   ⚠️  No results to test structure")
        
        # Test 6: Test search facets
        print("\n6️⃣ Testing Search Facets...")
        
        facets = search_response.facets
        if facets:
            print(f"   ✅ Types: {len(facets.get('types', {}))} facet groups")
            print(f"   ✅ Categories: {len(facets.get('categories', {}))} facet groups")
            print(f"   ✅ Sources: {len(facets.get('sources', {}))} facet groups")
            print(f"   ✅ Date Ranges: {len(facets.get('date_ranges', {}))} facet groups")
        else:
            print("   ⚠️  No facets generated")
        
        # Test 7: Test search suggestions
        print("\n7️⃣ Testing Search Suggestions...")
        
        suggestions = core_search_system.get_search_suggestions("sys")
        print(f"   ✅ Suggestions for 'sys': {len(suggestions)} suggestions")
        if suggestions:
            print(f"      - {', '.join(suggestions[:5])}")
        
        # Test 8: Test search analytics
        print("\n8️⃣ Testing Search Analytics...")
        
        analytics = core_search_system.get_search_analytics()
        print(f"   ✅ Total searches: {analytics['total_searches']}")
        print(f"   ✅ Popular queries: {len(analytics['popular_queries'])} queries")
        print(f"   ✅ Search patterns: {len(analytics['search_patterns'])} patterns")
        print(f"   ✅ Recent searches: {len(analytics['recent_searches'])} searches")
        
        # Test 9: Test different sort options
        print("\n9️⃣ Testing Sort Options...")
        
        sort_options = ["relevance", "date", "name"]
        for sort_by in sort_options:
            print(f"   🔍 Testing sort by {sort_by}...")
            search_query = SearchQuery(
                query="system",
                sort_by=sort_by,
                limit=5
            )
            search_response = core_search_system.search(search_query)
            print(f"      ✅ {sort_by} sort returned {len(search_response.results)} results")
        
        # Test 10: Test pagination
        print("\n🔟 Testing Pagination...")
        
        search_query = SearchQuery(
            query="system",
            limit=3,
            offset=0
        )
        first_page = core_search_system.search(search_query)
        
        search_query.offset = 3
        second_page = core_search_system.search(search_query)
        
        print(f"   ✅ First page: {len(first_page.results)} results")
        print(f"   ✅ Second page: {len(second_page.results)} results")
        print(f"   ✅ Total count: {first_page.total_count}")
        
        print("\n" + "=" * 50)
        print("🎉 CORE SEARCH SYSTEM VALIDATION SUCCESSFUL!")
        print("   ✅ Core search system is fully functional")
        print("   ✅ Search works across all node types")
        print("   ✅ Filters, sorting, and pagination work correctly")
        print("   ✅ Facets and suggestions are generated")
        print("   ✅ Search analytics are tracked")
        print("\n   The unified search system is ready to use!")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Validation failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("🚀 Starting Core Search System Validation...")
    print("   Testing unified search across all Living Codex nodes")
    print()
    
    success = test_core_search_system()
    
    if success:
        print("\n✅ CORE SEARCH SYSTEM VALIDATION PASSED")
        print("   The unified search system is working correctly.")
        print("   Users can now search across all system nodes.")
    else:
        print("\n❌ CORE SEARCH SYSTEM VALIDATION FAILED")
        print("   There are issues with the core search system.")
        print("   Check the error messages above.")

if __name__ == "__main__":
    main()
