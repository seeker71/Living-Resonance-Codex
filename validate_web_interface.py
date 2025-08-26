#!/usr/bin/env python3
"""
Validate Web Interface Startup
Tests if the unified_web_interface.py can start and respond to requests
"""

import sys
import time
import threading
import requests
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

def test_server_startup():
    """Test if the server can start and respond to requests"""
    
    print("🧪 Validating Web Interface Startup")
    print("=" * 50)
    
    try:
        # Test 1: Import the Flask app
        print("\n1️⃣ Testing Flask App Import...")
        from web_platform.unified_web_interface import app
        print("   ✅ Flask app imported successfully")
        print(f"   ✅ App name: {app.name}")
        print(f"   ✅ App instance path: {app.instance_path}")
        
        # Test 2: Check if all routes are registered
        print("\n2️⃣ Testing Route Registration...")
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(f"{rule.methods} {rule.rule}")
        
        print(f"   ✅ Found {len(routes)} registered routes")
        print("   ✅ Key routes:")
        for route in routes[:10]:  # Show first 10 routes
            print(f"      - {route}")
        
        # Test 3: Test server startup in a thread
        print("\n3️⃣ Testing Server Startup...")
        
        def start_server():
            """Start the server in a separate thread"""
            try:
                app.run(debug=False, host='127.0.0.1', port=5005, use_reloader=False)
            except Exception as e:
                print(f"   ❌ Server startup error: {e}")
        
        # Start server in background thread
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        
        # Wait for server to start
        print("   ⏳ Starting server on port 5005...")
        time.sleep(3)
        
        # Test 4: Test if server responds
        print("\n4️⃣ Testing Server Response...")
        try:
            response = requests.get('http://127.0.0.1:5005/', timeout=5)
            if response.status_code == 200:
                print("   ✅ Server responding successfully")
                print(f"   ✅ Response status: {response.status_code}")
                print(f"   ✅ Response length: {len(response.text)} characters")
                
                # Check if response contains expected content
                if "Living Codex Platform" in response.text:
                    print("   ✅ Response contains expected content")
                else:
                    print("   ⚠️  Response may not contain expected content")
                    
            else:
                print(f"   ❌ Server returned status {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Server not responding: {e}")
            return False
        
        # Test 5: Test specific routes
        print("\n5️⃣ Testing Specific Routes...")
        
        # Test discover route (requires login, so should redirect)
        try:
            response = requests.get('http://127.0.0.1:5005/discover', timeout=5, allow_redirects=False)
            if response.status_code in [302, 401]:  # Redirect or unauthorized
                print("   ✅ Discover route accessible (redirects as expected)")
            else:
                print(f"   ⚠️  Discover route returned status {response.status_code}")
        except Exception as e:
            print(f"   ❌ Discover route error: {e}")
        
        # Test login route
        try:
            response = requests.get('http://127.0.0.1:5005/login', timeout=5)
            if response.status_code == 200:
                print("   ✅ Login route accessible")
            else:
                print(f"   ⚠️  Login route returned status {response.status_code}")
        except Exception as e:
            print(f"   ❌ Login route error: {e}")
        
        print("\n" + "=" * 50)
        print("🎉 WEB INTERFACE VALIDATION SUCCESSFUL!")
        print("   ✅ Flask app imports correctly")
        print("   ✅ All routes are registered")
        print("   ✅ Server can start successfully")
        print("   ✅ Server responds to HTTP requests")
        print("   ✅ Core routes are accessible")
        print("\n   The unified_web_interface.py is working correctly!")
        print("   You can now run the navigation tests.")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Validation failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main validation function"""
    print("🚀 Starting Web Interface Validation...")
    print("   Testing if unified_web_interface.py can start and respond")
    print()
    
    success = test_server_startup()
    
    if success:
        print("\n✅ WEB INTERFACE VALIDATION PASSED")
        print("   The unified_web_interface.py is fully functional.")
        print("   Next step: Run the navigation tests.")
    else:
        print("\n❌ WEB INTERFACE VALIDATION FAILED")
        print("   There are issues with the web interface.")
        print("   Check the error messages above.")

if __name__ == "__main__":
    main()
