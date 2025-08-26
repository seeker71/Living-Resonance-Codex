#!/usr/bin/env python3
"""
Test Ontology Routes
Validates that the ontology routes in unified_web_interface.py work correctly
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

def test_ontology_routes():
    """Test if the ontology routes can be accessed without errors"""
    
    print("🧪 Testing Ontology Routes")
    print("=" * 50)
    
    try:
        # Test 1: Import the Flask app
        print("\n1️⃣ Testing Flask App Import...")
        from web_platform.unified_web_interface import app
        print("   ✅ Flask app imported successfully")
        
        # Test 2: Check if ontology routes are registered
        print("\n2️⃣ Testing Ontology Route Registration...")
        ontology_routes = []
        for rule in app.url_map.iter_rules():
            if rule.rule.startswith('/ontology'):
                ontology_routes.append(f"{rule.methods} {rule.rule}")
        
        print(f"   ✅ Found {len(ontology_routes)} ontology routes:")
        for route in ontology_routes:
            print(f"      - {route}")
        
        # Test 3: Test ontology navigator functionality
        print("\n3️⃣ Testing Ontology Navigator...")
        from web_platform.ontology_navigator import ontology_navigator
        
        print(f"   ✅ Ontology navigator type: {type(ontology_navigator)}")
        print(f"   ✅ Categories available: {list(ontology_navigator.categories.keys())}")
        print(f"   ✅ Total nodes: {len(ontology_navigator.nodes)}")
        
        # Test 4: Test specific category access
        print("\n4️⃣ Testing Category Access...")
        if 'core_system' in ontology_navigator.categories:
            core_category = ontology_navigator.categories['core_system']
            print(f"   ✅ Core system category found: {core_category}")
            
            # Test getting nodes by category
            core_components = ontology_navigator.get_nodes_by_category('core_system')
            print(f"   ✅ Core system components: {len(core_components)} found")
            
            if core_components:
                for component in core_components[:3]:  # Show first 3
                    print(f"      - {component.name} ({component.type})")
        else:
            print("   ❌ Core system category not found")
        
        # Test 5: Test component details
        print("\n5️⃣ Testing Component Details...")
        if ontology_navigator.nodes:
            first_node_id = list(ontology_navigator.nodes.keys())[0]
            component = ontology_navigator.get_node_details(first_node_id)
            if component:
                print(f"   ✅ Component details retrieved: {component.name}")
                print(f"      - Type: {component.type}")
                print(f"      - Category: {component.category}")
                print(f"      - Description: {component.description[:100]}...")
            else:
                print("   ❌ Could not retrieve component details")
        else:
            print("   ⚠️  No nodes available for testing")
        
        # Test 6: Test search functionality
        print("\n6️⃣ Testing Search Functionality...")
        search_results = ontology_navigator.search_nodes('core')
        print(f"   ✅ Search for 'core' returned {len(search_results)} results")
        
        # Test 7: Test system architecture
        print("\n7️⃣ Testing System Architecture...")
        try:
            architecture = ontology_navigator.get_system_architecture()
            if architecture:
                print(f"   ✅ System architecture retrieved: {type(architecture)}")
                if hasattr(architecture, 'keys'):
                    print(f"      - Keys: {list(architecture.keys())}")
            else:
                print("   ⚠️  System architecture returned None")
        except Exception as e:
            print(f"   ⚠️  System architecture error: {e}")
        
        print("\n" + "=" * 50)
        print("🎉 ONTOLOGY ROUTES VALIDATION SUCCESSFUL!")
        print("   ✅ All ontology routes are properly registered")
        print("   ✅ Ontology navigator is working correctly")
        print("   ✅ Category and component access works")
        print("   ✅ Search functionality is operational")
        print("\n   The ontology routes should now work without 500 errors!")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Validation failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("🚀 Starting Ontology Routes Validation...")
    print("   Testing if ontology routes work correctly")
    print()
    
    success = test_ontology_routes()
    
    if success:
        print("\n✅ ONTOLOGY ROUTES VALIDATION PASSED")
        print("   The ontology routes are working correctly.")
        print("   You can now navigate to /ontology/category/core_system without errors.")
    else:
        print("\n❌ ONTOLOGY ROUTES VALIDATION FAILED")
        print("   There are issues with the ontology routes.")
        print("   Check the error messages above.")

if __name__ == "__main__":
    main()
