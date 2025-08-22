"""
Setup Script for Living Codex API Keys and Configuration
Helps you configure and test your API keys
"""

import os
import sys
from pathlib import Path
from config_manager import ConfigManager

def setup_openai_key():
    """Set up OpenAI API key"""
    print("\n🔑 Setting up OpenAI API Key")
    print("=" * 40)
    
    # Check if already set
    if os.getenv('OPENAI_API_KEY'):
        print("✅ OpenAI API key already configured")
        return True
    
    print("To get an OpenAI API key:")
    print("1. Go to https://platform.openai.com/api-keys")
    print("2. Sign in or create an account")
    print("3. Click 'Create new secret key'")
    print("4. Copy the key (it starts with 'sk-')")
    print()
    
    api_key = input("Enter your OpenAI API key (or press Enter to skip): ").strip()
    
    if api_key:
        if api_key.startswith('sk-'):
            # Set environment variable
            os.environ['OPENAI_API_KEY'] = api_key
            print("✅ OpenAI API key configured successfully!")
            return True
        else:
            print("❌ Invalid OpenAI API key format. Should start with 'sk-'")
            return False
    else:
        print("ℹ️  Skipping OpenAI configuration")
        return False

def setup_google_search():
    """Set up Google Custom Search (optional)"""
    print("\n🔍 Setting up Google Custom Search (Optional)")
    print("=" * 50)
    
    print("Google Custom Search is optional. You can use DuckDuckGo instead.")
    print("To set up Google Custom Search:")
    print("1. Go to https://developers.google.com/custom-search")
    print("2. Create a new search engine")
    print("3. Get your API key and Search Engine ID")
    print()
    
    setup = input("Do you want to set up Google Custom Search? (y/n): ").lower()
    
    if setup == 'y':
        api_key = input("Enter your Google API key: ").strip()
        cse_id = input("Enter your Custom Search Engine ID: ").strip()
        
        if api_key and cse_id:
            os.environ['GOOGLE_API_KEY'] = api_key
            os.environ['GOOGLE_CSE_ID'] = cse_id
            print("✅ Google Custom Search configured successfully!")
            return True
        else:
            print("❌ Both API key and Search Engine ID are required")
            return False
    else:
        print("ℹ️  Skipping Google Custom Search configuration")
        return False

def setup_neo4j():
    """Set up Neo4j configuration"""
    print("\n🗄️  Setting up Neo4j Configuration")
    print("=" * 40)
    
    print("Neo4j is a graph database that enhances the Living Codex.")
    print("You can install it locally or use Neo4j Desktop.")
    print()
    
    # Check if Neo4j is running
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 7687))
        sock.close()
        
        if result == 0:
            print("✅ Neo4j appears to be running on localhost:7687")
        else:
            print("⚠️  Neo4j is not running on localhost:7687")
            print("   You'll need to start Neo4j first")
    except Exception as e:
        print(f"⚠️  Could not check Neo4j status: {e}")
    
    print("\nTo install Neo4j:")
    print("1. Download from https://neo4j.com/download/")
    print("2. Install and start the service")
    print("3. Set a password during first startup")
    print()
    
    password = input("Enter your Neo4j password (or press Enter to skip): ").strip()
    
    if password:
        os.environ['NEO4J_PASSWORD'] = password
        print("✅ Neo4j password configured!")
        return True
    else:
        print("ℹ️  Skipping Neo4j configuration")
        return False

def create_env_file():
    """Create .env file with current configuration"""
    print("\n📝 Creating .env file")
    print("=" * 30)
    
    config = ConfigManager()
    env_file = config.create_env_file()
    
    if env_file:
        print(f"✅ Environment file created at {env_file}")
        print("💡 You can edit this file to modify settings later")
        return True
    else:
        print("❌ Failed to create environment file")
        return False

def test_configuration():
    """Test the current configuration"""
    print("\n🧪 Testing Configuration")
    print("=" * 30)
    
    config = ConfigManager()
    
    print("📊 Configuration Status:")
    print(f"  OpenAI: {'✅ Configured' if config.is_openai_configured() else '❌ Not configured'}")
    print(f"  Google: {'✅ Configured' if config.is_google_configured() else '❌ Not configured'}")
    print(f"  Neo4j: {'✅ Configured' if config.is_neo4j_configured() else '❌ Not configured'}")
    print(f"  PostgreSQL: {'✅ Configured' if config.is_postgres_configured() else '❌ Not configured'}")
    
    # Test OpenAI if configured
    if config.is_openai_configured():
        print("\n🔍 Testing OpenAI connection...")
        try:
            from real_external_api_system import ExpertSystemIntegration
            expert = ExpertSystemIntegration()
            print("✅ OpenAI integration ready")
        except Exception as e:
            print(f"❌ OpenAI integration error: {e}")
    
    # Test Neo4j if configured
    if config.is_neo4j_configured():
        print("\n🗄️  Testing Neo4j connection...")
        try:
            from neo4j_integration_system import Neo4jIntegrationSystem
            neo4j = Neo4jIntegrationSystem()
            if neo4j.connection_manager.is_connected():
                print("✅ Neo4j connection successful")
            else:
                print("❌ Neo4j connection failed")
        except Exception as e:
            print(f"❌ Neo4j integration error: {e}")
    
    print("\n✅ Configuration test complete!")

def main():
    """Main setup function"""
    print("🚀 Living Codex Setup Wizard")
    print("=" * 40)
    print("This wizard will help you configure your API keys and database connections.")
    print()
    
    # Step 1: OpenAI
    setup_openai_key()
    
    # Step 2: Google (optional)
    setup_google_search()
    
    # Step 3: Neo4j
    setup_neo4j()
    
    # Step 4: Create .env file
    create_env_file()
    
    # Step 5: Test configuration
    test_configuration()
    
    print("\n🎉 Setup Complete!")
    print("=" * 20)
    print("Your Living Codex is now configured and ready to use!")
    print()
    print("Next steps:")
    print("1. Start Neo4j if you configured it")
    print("2. Run the integrated demo: python integrated_real_systems_demo.py")
    print("3. Explore the system capabilities")
    print()
    print("Happy exploring! 🌟")

if __name__ == "__main__":
    main()
