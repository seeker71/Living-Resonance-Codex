#!/usr/bin/env python3
"""
OpenAI Integration Test Script
Tests OpenAI API functionality specifically
"""

import asyncio
from config_manager import ConfigManager
from real_external_api_system import RealExternalAPISystem, APISource

async def test_openai_integration():
    """Test OpenAI integration specifically"""
    print("🤖 Testing OpenAI Integration")
    print("=" * 40)
    
    # Load configuration
    config = ConfigManager()
    
    print("📊 OpenAI Configuration:")
    print(f"  OpenAI API Key: {'✅ Configured' if config.is_openai_configured() else '❌ Not configured'}")
    print(f"  OpenAI Model: {config.api_config.openai_model}")
    print()
    
    # Initialize API system
    api_system = RealExternalAPISystem()
    
    # Test OpenAI expert consultation
    test_query = "What are the key principles of ontological frameworks in knowledge systems?"
    print(f"🔍 Testing OpenAI with query: '{test_query}'")
    print()
    
    try:
        # Test OpenAI only
        results = await api_system.search_external_knowledge(
            query=test_query,
            sources=[APISource.OPENAI],
            max_results=1
        )
        
        print("📊 OpenAI Test Results:")
        print(f"  Total Sources: {results['summary']['total_sources']}")
        print(f"  Successful Sources: {results['summary']['successful_sources']}")
        print(f"  Confidence Score: {results['summary']['confidence_score']:.2f}")
        
        # Check OpenAI results specifically
        if 'expert_system' in results['sources']:
            expert_response = results['sources']['expert_system']
            print(f"\n🤖 Expert System Response:")
            print(f"  Status: {expert_response.status.value}")
            print(f"  Response Time: {expert_response.response_time:.2f}s")
            
            if expert_response.status.value == 'success':
                print("  ✅ OpenAI consultation successful!")
                
                # Extract and display the AI response
                if hasattr(expert_response, 'data') and expert_response.data:
                    if 'choices' in expert_response.data:
                        content = expert_response.data['choices'][0]['message']['content']
                        print(f"\n💡 AI Response:")
                        print(f"  {content[:500]}...")
                        
                        # Show metadata
                        if hasattr(expert_response, 'metadata') and expert_response.metadata:
                            tokens_used = expert_response.metadata.get('tokens_used', 'N/A')
                            print(f"\n📊 Metadata:")
                            print(f"  Tokens Used: {tokens_used}")
                    else:
                        print(f"  ⚠️  Unexpected data format: {type(expert_response.data)}")
                else:
                    print("  ⚠️  No data in response")
            else:
                print(f"  ❌ OpenAI consultation failed")
                if hasattr(expert_response, 'metadata') and expert_response.metadata:
                    error = expert_response.metadata.get('error', 'Unknown error')
                    print(f"  Error: {error}")
        else:
            print("  ❌ No expert_system in results")
            print(f"  Available sources: {list(results['sources'].keys())}")
        
        print("\n✅ OpenAI integration test completed!")
        
    except Exception as e:
        print(f"❌ OpenAI test failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   • Check your OpenAI API key is correct")
        print("   • Verify you have OpenAI API credits")
        print("   • Check internet connection")
        print("   • Verify API key permissions")

def main():
    """Main function"""
    print("🤖 Living Codex OpenAI Integration Test")
    print("=" * 50)
    
    # Run the async test
    asyncio.run(test_openai_integration())
    
    print("\n🎉 OpenAI Integration Test Complete!")
    print("=" * 50)
    print("\n🌟 Your Living Codex can now:")
    print("   • Consult OpenAI for AI-powered insights")
    print("   • Get expert knowledge on any topic")
    print("   • Integrate AI responses into your knowledge base")
    print("   • Build intelligent, evolving knowledge systems")
    
    print("\n🚀 Next steps:")
    print("   1. Test web search: python test_web_search.py")
    print("   2. Run integrated demo: python integrated_real_systems_demo.py")
    print("   3. Start building AI-powered knowledge systems!")

if __name__ == "__main__":
    main()
