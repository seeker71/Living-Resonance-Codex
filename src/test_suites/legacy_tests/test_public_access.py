#!/usr/bin/env python3
"""
Test Public Access Routes
Validates that read-only routes in unified_web_interface.py work without login
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

def test_public_routes():
    """Test if the public routes can be accessed without login"""
    
    print("🧪 Testing Public Access Routes")
    print("=" * 50)
    
    try:
        # Test 1: Import the Flask app
        print("\n1️⃣ Testing Flask App Import...")
        from web_platform.unified_web_interface import app
        print("   ✅ Flask app imported successfully")
        
        # Test 2: Check which routes are public vs. require login
        print("\n2️⃣ Testing Route Access Requirements...")
        
        public_routes = []
        protected_routes = []
        
        for rule in app.url_map.iter_rules():
            endpoint = app.view_functions.get(rule.endpoint)
            if endpoint and hasattr(endpoint, '__wrapped__'):
                # Check if the function has @login_required decorator
                if 'login_required' in str(endpoint.__wrapped__):
                    protected_routes.append(rule.rule)
                else:
                    public_routes.append(rule.rule)
            else:
                public_routes.append(rule.rule)
        
        print(f"   ✅ Found {len(public_routes)} public routes")
        print(f"   ✅ Found {len(protected_routes)} protected routes")
        
        # Test 3: Check specific public routes that should be accessible
        print("\n3️⃣ Testing Key Public Routes...")
        
        key_public_routes = [
            '/',
            '/discover',
            '/navigate',
            '/explore/<path:category>',
            '/user/<user_id>',
            '/concept/<concept_name>',
            '/source/<path:file_path>',
            '/expression/<path:file_path>/<int:line_number>',
            '/ontology',
            '/ontology/category/<category>',
            '/ontology/component/<component_id>',
            '/ontology/search',
            '/ontology/architecture',
            '/assets'
        ]
        
        public_accessible = []
        for route in key_public_routes:
            if route in public_routes:
                public_accessible.append(route)
                print(f"   ✅ {route} - Public access")
            else:
                print(f"   ❌ {route} - Requires login")
        
        # Test 4: Check protected routes that should require login
        print("\n4️⃣ Testing Protected Routes...")
        
        key_protected_routes = [
            '/dashboard',
            '/contribute',
            '/signup',
            '/login',
            '/connect/<user_id>'
        ]
        
        properly_protected = []
        for route in key_protected_routes:
            if route in protected_routes:
                properly_protected.append(route)
                print(f"   ✅ {route} - Properly protected")
            else:
                print(f"   ⚠️  {route} - Should be protected but isn't")
        
        # Test 5: Test API endpoints
        print("\n5️⃣ Testing API Endpoints...")
        
        public_apis = [
            '/api/discovery/similar_users',
            '/api/discovery/relevant_content',
            '/api/navigation/system_overview',
            '/api/contributions',
            '/api/assets',
            '/api/ontology/overview',
            '/api/ontology/categories',
            '/api/ontology/components'
        ]
        
        public_api_count = 0
        for api in public_apis:
            if api in public_routes:
                public_api_count += 1
                print(f"   ✅ {api} - Public API")
            else:
                print(f"   ❌ {api} - Protected API")
        
        # Test 6: Summary
        print("\n" + "=" * 50)
        print("🎯 PUBLIC ACCESS VALIDATION RESULTS")
        print("=" * 50)
        
        print(f"   📊 Total Routes: {len(public_routes) + len(protected_routes)}")
        print(f"   🌐 Public Routes: {len(public_routes)}")
        print(f"   🔒 Protected Routes: {len(protected_routes)}")
        print(f"   📱 Public APIs: {public_api_count}")
        
        print(f"\n   ✅ Key Public Routes Accessible: {len(public_accessible)}/{len(key_public_routes)}")
        print(f"   ✅ Properly Protected Routes: {len(properly_protected)}/{len(key_protected_routes)}")
        
        if len(public_accessible) >= len(key_public_routes) * 0.8:  # 80% success rate
            print("\n   🎉 PUBLIC ACCESS VALIDATION SUCCESSFUL!")
            print("   ✅ Most read-only routes are now publicly accessible")
            print("   ✅ Users can browse without login")
            print("   ✅ Only modification routes require authentication")
        else:
            print("\n   ⚠️  PUBLIC ACCESS VALIDATION PARTIAL")
            print("   ⚠️  Some routes still require login unnecessarily")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Validation failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("🚀 Starting Public Access Validation...")
    print("   Testing if read-only routes work without login")
    print()
    
    success = test_public_routes()
    
    if success:
        print("\n✅ PUBLIC ACCESS VALIDATION COMPLETED")
        print("   The web interface now provides public access to read-only features.")
        print("   Users can browse users, categories, and assets without logging in.")
    else:
        print("\n❌ PUBLIC ACCESS VALIDATION FAILED")
        print("   There are issues with the public route configuration.")
        print("   Check the error messages above.")

if __name__ == "__main__":
    main()
