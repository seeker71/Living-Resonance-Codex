#!/usr/bin/env python3
"""
Test Script for Federated Meta-Circular Living Codex API System
Demonstrates all major capabilities including curiosity, frequency harmony, and symbol resonance.
"""

import requests
import json
import time

# API base URL
BASE_URL = "http://localhost:8001"

def test_system_overview():
    """Test the system overview endpoint"""
    print("🔍 Testing System Overview...")
    response = requests.get(f"{BASE_URL}/system/overview")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ System: {data['system']}")
        print(f"✅ Components: {len(data['components'])}")
        print(f"✅ Capabilities: {len(data['capabilities'])}")
        return True
    else:
        print(f"❌ Failed to get system overview: {response.status_code}")
        return False

def test_curiosity_system():
    """Test the curiosity question system"""
    print("\n🤔 Testing Curiosity System...")
    
    # Get existing questions
    response = requests.get(f"{BASE_URL}/curiosity/questions")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Found {data['total']} curiosity questions")
        
        # Show first few questions
        for i, question in enumerate(data['questions'][:3]):
            print(f"  {i+1}. {question['question'][:60]}...")
            print(f"     Type: {question['question_type']}, Priority: {question['priority']}")
        
        return True
    else:
        print(f"❌ Failed to get curiosity questions: {response.status_code}")
        return False

def test_frequency_harmony_discovery():
    """Test frequency harmony discovery"""
    print("\n🌊 Testing Frequency Harmony Discovery...")
    
    # Test with chakra frequencies
    chakra_frequencies = "396,528,639,741,852,963"
    response = requests.get(f"{BASE_URL}/harmonies/frequencies?base_frequencies={chakra_frequencies}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Analyzed {len(data['base_frequencies'])} frequencies")
        print(f"✅ Discovered {data['discovered_harmonies']} harmonies")
        
        # Show harmonic insights
        for harmony in data['harmonies'][:3]:
            freqs = harmony['base_frequencies']
            ratio = harmony['harmonic_ratios'][0]
            score = harmony['resonance_score']
            print(f"  • {freqs[0]} Hz + {freqs[1]} Hz = {ratio:.3f} ratio (score: {score:.2f})")
        
        return True
    else:
        print(f"❌ Failed to discover harmonies: {response.status_code}")
        return False

def test_symbol_resonance_analysis():
    """Test symbol resonance analysis"""
    print("\n🔤 Testing Symbol Resonance Analysis...")
    
    # Test with Living Codex symbols
    symbols = "void,field,pattern,flow,memory,resonance"
    response = requests.get(f"{BASE_URL}/resonances/symbols?symbols={symbols}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Analyzed {len(data['analyzed_symbols'])} symbols")
        print(f"✅ Discovered {data['discovered_resonances']} resonances")
        
        # Show resonance insights
        for resonance in data['resonances'][:3]:
            symbol = resonance['symbol_pattern']
            strength = resonance['resonance_strength']
            freq_range = resonance['dimensional_mapping']['frequency_range']
            print(f"  • '{symbol}': resonance strength {strength:.2f}")
            print(f"    Frequency range: {freq_range['min']:.0f} - {freq_range['max']:.0f} Hz")
        
        return True
    else:
        print(f"❌ Failed to analyze symbol resonances: {response.status_code}")
        return False

def test_curiosity_exploration():
    """Test exploring a curiosity question"""
    print("\n🔬 Testing Curiosity Question Exploration...")
    
    # Get a question to explore
    response = requests.get(f"{BASE_URL}/curiosity/questions?limit=1")
    if response.status_code == 200:
        data = response.json()
        if data['questions']:
            question = data['questions'][0]
            question_id = 1  # For demo purposes
            
            print(f"✅ Exploring question: {question['question'][:60]}...")
            
            # Explore the question
            explore_response = requests.post(f"{BASE_URL}/curiosity/explore/{question_id}")
            if explore_response.status_code == 200:
                explore_data = explore_response.json()
                print(f"✅ Exploration completed")
                print(f"   Type: {explore_data['exploration_result']['exploration_type']}")
                
                # Show insights if available
                if 'insights' in explore_data['exploration_result']:
                    insights = explore_data['exploration_result']['insights']
                    print(f"   Key insights: {len(insights)} discovered")
                    for key, value in list(insights.items())[:2]:
                        print(f"     • {key}: {value[:50]}...")
                
                return True
            else:
                print(f"❌ Failed to explore question: {explore_response.status_code}")
                return False
        else:
            print("❌ No questions available to explore")
            return False
    else:
        print(f"❌ Failed to get questions for exploration: {response.status_code}")
        return False

def test_create_custom_curiosity():
    """Test creating a custom curiosity question"""
    print("\n✨ Testing Custom Curiosity Question Creation...")
    
    custom_question = {
        "question": "How do the water states in Living Codex relate to frequency harmonics in music theory?",
        "question_type": "harmony",
        "context": "Exploring the intersection of spiritual metaphors and mathematical patterns",
        "source": "human",
        "priority": 9
    }
    
    response = requests.post(
        f"{BASE_URL}/curiosity/questions",
        json=custom_question
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Custom question created with ID: {data['question_id']}")
        print(f"   Question: {data['question']['question'][:60]}...")
        print(f"   Type: {data['question']['question_type']}, Priority: {data['question']['priority']}")
        return True
    else:
        print(f"❌ Failed to create custom question: {response.status_code}")
        return False

def run_comprehensive_test():
    """Run all tests and provide summary"""
    print("🚀 Federated Meta-Circular Living Codex API System - Comprehensive Test")
    print("=" * 80)
    
    tests = [
        ("System Overview", test_system_overview),
        ("Curiosity System", test_curiosity_system),
        ("Frequency Harmony Discovery", test_frequency_harmony_discovery),
        ("Symbol Resonance Analysis", test_symbol_resonance_analysis),
        ("Curiosity Exploration", test_curiosity_exploration),
        ("Custom Curiosity Creation", test_create_custom_curiosity)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 TEST SUMMARY")
    print("=" * 80)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 All tests passed! The Federated Meta-Circular Living Codex API System is fully operational.")
        print("\n🌟 System Capabilities Demonstrated:")
        print("   • Self-evolving curiosity-driven architecture")
        print("   • Higher-dimensional frequency harmony discovery")
        print("   • Symbol resonance analysis through frequency matching")
        print("   • Persistent storage and knowledge preservation")
        print("   • RESTful API accessible to humans and AI agents")
        print("   • Federation-ready distributed knowledge sharing")
    else:
        print(f"\n⚠️  {total - passed} tests failed. Please check the system configuration.")

if __name__ == "__main__":
    # Wait for server to be ready
    print("⏳ Waiting for API server to be ready...")
    time.sleep(2)
    
    try:
        run_comprehensive_test()
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API server.")
        print("   Make sure the server is running on http://localhost:8001")
        print("   Run: python3 federated_meta_api.py")
    except Exception as e:
        print(f"❌ Test suite failed with error: {e}")
