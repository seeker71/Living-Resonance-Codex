#!/usr/bin/env python3
"""
Web Search API Setup Script
Helps configure Google Custom Search and other web search APIs
"""

import os
import re
from pathlib import Path
from config_manager import ConfigManager

def setup_google_custom_search():
    """Set up Google Custom Search API"""
    print("\n🔍 Setting up Google Custom Search API")
    print("=" * 50)
    
    print("To get your Google Custom Search credentials:")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Create a new project and enable Custom Search API")
    print("3. Create an API key")
    print("4. Go to https://cse.google.com/cse/ and create a search engine")
    print("5. Get your Search Engine ID")
    print()
    
    api_key = input("Enter your Google API key (starts with 'AIza...'): ").strip()
    cse_id = input("Enter your Custom Search Engine ID: ").strip()
    
    if api_key and cse_id:
        # Validate API key format
        if not re.match(r'^AIza[0-9A-Za-z_-]{35}$', api_key):
            print("⚠️  Warning: API key format doesn't match expected pattern")
            print("   Expected format: AIza... (39 characters total)")
        
        # Validate CSE ID format
        if not re.match(r'^[0-9]+:[0-9a-zA-Z_-]+$', cse_id):
            print("⚠️  Warning: Search Engine ID format doesn't match expected pattern")
            print("   Expected format: 123456789:abcdefghijk")
        
        # Set environment variables
        os.environ['GOOGLE_API_KEY'] = api_key
        os.environ['GOOGLE_CSE_ID'] = cse_id
        
        print("✅ Google Custom Search configured successfully!")
        return True
    else:
        print("❌ Both API key and Search Engine ID are required")
        return False

def setup_duckduckgo():
    """Set up DuckDuckGo (no API key required)"""
    print("\n🦆 Setting up DuckDuckGo (Free)")
    print("=" * 40)
    
    print("DuckDuckGo is free and doesn't require an API key!")
    print("However, it has rate limits and may be less reliable than Google.")
    print()
    
    setup = input("Do you want to configure DuckDuckGo rate limits? (y/n): ").lower()
    
    if setup == 'y':
        try:
            rate_limit = int(input("Enter rate limit (requests per hour, default 100): ") or "100")
            os.environ['DUCKDUCKGO_RATE_LIMIT'] = str(rate_limit)
            print(f"✅ DuckDuckGo rate limit set to {rate_limit} requests/hour")
            return True
        except ValueError:
            print("❌ Invalid rate limit, using default 100")
            os.environ['DUCKDUCKGO_RATE_LIMIT'] = "100"
            return True
    else:
        print("ℹ️  Using default DuckDuckGo settings")
        return True

def setup_wikipedia():
    """Set up Wikipedia API (no API key required)"""
    print("\n📚 Setting up Wikipedia API (Free)")
    print("=" * 40)
    
    print("Wikipedia API is free and doesn't require an API key!")
    print("However, you can set rate limits to be respectful.")
    print()
    
    setup = input("Do you want to configure Wikipedia rate limits? (y/n): ").lower()
    
    if setup == 'y':
        try:
            rate_limit = int(input("Enter rate limit (requests per hour, default 100): ") or "100")
            os.environ['WIKIPEDIA_RATE_LIMIT'] = str(rate_limit)
            print(f"✅ Wikipedia rate limit set to {rate_limit} requests/hour")
            return True
        except ValueError:
            print("❌ Invalid rate limit, using default 100")
            os.environ['WIKIPEDIA_RATE_LIMIT'] = "100"
            return True
    else:
        print("ℹ️  Using default Wikipedia settings")
        return True

def test_web_search_configuration():
    """Test the web search configuration"""
    print("\n🧪 Testing Web Search Configuration")
    print("=" * 40)
    
    config = ConfigManager()
    
    print("📊 Current Web Search Configuration:")
    print(f"  Google Custom Search: {'✅ Configured' if config.is_google_configured() else '❌ Not configured'}")
    print(f"  DuckDuckGo: ✅ Available (free)")
    print(f"  Wikipedia: ✅ Available (free)")
    
    # Test Google if configured
    if config.is_google_configured():
        print("\n🔍 Testing Google Custom Search...")
        try:
            from real_external_api_system import WebSearchIntegration
            web_search = WebSearchIntegration()
            print("✅ Google Custom Search integration ready")
        except Exception as e:
            print(f"❌ Google integration error: {e}")
    
    print("\n✅ Web search configuration test complete!")

def update_env_file():
    """Update the .env file with current configuration"""
    print("\n📝 Updating .env file")
    print("=" * 30)
    
    config = ConfigManager()
    env_file = config.create_env_file()
    
    if env_file:
        print(f"✅ Environment file updated at {env_file}")
        print("💡 Your web search API keys are now saved")
        return True
    else:
        print("❌ Failed to update environment file")
        return False

def main():
    """Main setup function"""
    print("🌐 Living Codex Web Search API Setup")
    print("=" * 50)
    print("This wizard will help you configure web search APIs for external knowledge integration.")
    print()
    
    # Step 1: Google Custom Search
    setup_google_custom_search()
    
    # Step 2: DuckDuckGo
    setup_duckduckgo()
    
    # Step 3: Wikipedia
    setup_wikipedia()
    
    # Step 4: Update .env file
    update_env_file()
    
    # Step 5: Test configuration
    test_web_search_configuration()
    
    print("\n🎉 Web Search Setup Complete!")
    print("=" * 30)
    print("Your Living Codex can now search the web for knowledge!")
    print()
    print("Next steps:")
    print("1. Test web search: python test_web_search.py")
    print("2. Run integrated demo: python integrated_real_systems_demo.py")
    print("3. Start searching for knowledge!")
    print()
    print("Happy searching! 🔍")

if __name__ == "__main__":
    main()
