#!/usr/bin/env python3
"""
Living Codex Phase 5 - Fractal Level Testing
Tests both current level (Phase 4) and next fractal level (Phase 5)
"""

import requests
import json
import time
from typing import Dict, Any

class FractalLevelTester:
    """Test both current and next fractal levels"""
    
    def __init__(self):
        self.base_url = "http://localhost:8788"
        self.test_results = []
        
    def log(self, message: str, level: str = "INFO"):
        """Log messages with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
    
    def test_current_level(self) -> bool:
        """Test Phase 4 compatibility (current level)"""
        self.log("\n=== TESTING CURRENT LEVEL (Phase 4 Compatibility) ===")
        
        tests = []
        
        # Test 1: Basic connectivity
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                tests.append(("Root Endpoint", True, f"Server responding: {data['name']}"))
            else:
                tests.append(("Root Endpoint", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Root Endpoint", False, str(e)))
        
        # Test 2: Storage stats
        try:
            response = requests.get(f"{self.base_url}/storage/stats", timeout=10)
            if response.status_code == 200:
                stats = response.json()
                tests.append(("Storage Stats", True, f"Version {stats['version']}, {stats['total_nodes']} nodes"))
            else:
                tests.append(("Storage Stats", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Storage Stats", False, str(e)))
        
        # Test 3: Post contribution
        try:
            test_contribution = {
                "type": "Create",
                "actor": "fractal_tester",
                "object": {
                    "type": "Contribution",
                    "nodeId": "codex:Void",
                    "content": "Testing fractal expansion capabilities",
                    "resonance": 0.95
                }
            }
            
            response = requests.post(
                f"{self.base_url}/inbox",
                json=test_contribution,
                headers={"Content-Type": "application/activity+json"},
                timeout=10
            )
            
            if response.status_code == 202:
                tests.append(("Post Contribution", True, "Contribution accepted"))
            else:
                tests.append(("Post Contribution", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Post Contribution", False, str(e)))
        
        # Test 4: Retrieve contribution
        try:
            response = requests.get(f"{self.base_url}/contributions/node/codex:Void", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('count', 0) > 0:
                    tests.append(("Retrieve Contribution", True, f"Found {data['count']} contributions"))
                else:
                    tests.append(("Retrieve Contribution", False, "No contributions found"))
            else:
                tests.append(("Retrieve Contribution", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Retrieve Contribution", False, str(e)))
        
        # Test 5: ActivityPub compatibility
        try:
            response = requests.get(f"{self.base_url}/.well-known/webfinger", timeout=10)
            if response.status_code == 200:
                tests.append(("ActivityPub Compatibility", True, "WebFinger endpoint responding"))
            else:
                tests.append(("ActivityPub Compatibility", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("ActivityPub Compatibility", False, str(e)))
        
        # Display results
        all_passed = True
        for test_name, passed, details in tests:
            status = "✓" if passed else "✗"
            self.log(f"{status} {test_name}: {details}")
            if not passed:
                all_passed = False
        
        self.test_results.extend(tests)
        return all_passed
    
    def test_next_fractal_level(self) -> bool:
        """Test Phase 5 features (next fractal level)"""
        self.log("\n=== TESTING NEXT FRACTAL LEVEL (Phase 5 Features) ===")
        
        tests = []
        
        # Test 1: Fractal levels endpoint
        try:
            response = requests.get(f"{self.base_url}/fractal/levels", timeout=10)
            if response.status_code == 200:
                data = response.json()
                tests.append(("Fractal Levels", True, f"Levels {data['fractal_levels']}, {data['level_statistics']['level_2']['count']} subnodes"))
            else:
                tests.append(("Fractal Levels", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Fractal Levels", False, str(e)))
        
        # Test 2: Fractal expansion of a node
        try:
            response = requests.get(f"{self.base_url}/fractal/expand/codex:Void", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('total_subnodes', 0) > 0:
                    tests.append(("Fractal Expansion", True, f"Found {data['total_subnodes']} subnodes"))
                else:
                    tests.append(("Fractal Expansion", False, "No subnodes found"))
            else:
                tests.append(("Fractal Expansion", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Fractal Expansion", False, str(e)))
        
        # Test 3: Fractal subnodes
        try:
            response = requests.get(f"{self.base_url}/fractal/subnodes/codex:Void", timeout=10)
            if response.status_code == 200:
                data = response.json()
                contexts = data.get('contexts', [])
                if len(contexts) == 3:  # scientific, symbolic, water
                    tests.append(("Fractal Subnodes", True, f"Contexts: {', '.join(contexts)}"))
                else:
                    tests.append(("Fractal Subnodes", False, f"Expected 3 contexts, got {len(contexts)}"))
            else:
                tests.append(("Fractal Subnodes", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Fractal Subnodes", False, str(e)))
        
        # Test 4: Scientific context
        try:
            response = requests.get(f"{self.base_url}/fractal/context/scientific", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('count', 0) > 0:
                    tests.append(("Scientific Context", True, f"Found {data['count']} scientific subnodes"))
                else:
                    tests.append(("Scientific Context", False, "No scientific subnodes found"))
            else:
                tests.append(("Scientific Context", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Scientific Context", False, str(e)))
        
        # Test 5: Symbolic context
        try:
            response = requests.get(f"{self.base_url}/fractal/context/symbolic", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('count', 0) > 0:
                    tests.append(("Symbolic Context", True, f"Found {data['count']} symbolic subnodes"))
                else:
                    tests.append(("Symbolic Context", False, "No symbolic subnodes found"))
            else:
                tests.append(("Symbolic Context", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Symbolic Context", False, str(e)))
        
        # Test 6: Water context
        try:
            response = requests.get(f"{self.base_url}/fractal/context/water", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('count', 0) > 0:
                    tests.append(("Water Context", True, f"Found {data['count']} water subnodes"))
                else:
                    tests.append(("Water Context", False, "No water subnodes found"))
            else:
                tests.append(("Water Context", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Water Context", False, str(e)))
        
        # Test 7: Individual fractal node
        try:
            response = requests.get(f"{self.base_url}/fractal/nodes/codex:Void", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('fractal_context') == 'base_node':
                    tests.append(("Fractal Node Info", True, f"Base node with {data.get('subnode_count', 0)} subnodes"))
                else:
                    tests.append(("Fractal Node Info", False, "Not a base node"))
            else:
                tests.append(("Fractal Node Info", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Fractal Node Info", False, str(e)))
        
        # Display results
        all_passed = True
        for test_name, passed, details in tests:
            status = "✓" if passed else "✗"
            self.log(f"{status} {test_name}: {details}")
            if not passed:
                all_passed = False
        
        self.test_results.extend(tests)
        return all_passed
    
    def test_fractal_contribution(self) -> bool:
        """Test contributing to fractal subnodes"""
        self.log("\n=== TESTING FRACTAL CONTRIBUTIONS ===")
        
        tests = []
        
        # Test 1: Contribute to scientific subnode
        try:
            scientific_contribution = {
                "type": "Create",
                "actor": "fractal_explorer",
                "object": {
                    "type": "Contribution",
                    "nodeId": "codex:Void:scientific:empirical",
                    "content": "The Void's empirical nature shows in quantum vacuum fluctuations",
                    "resonance": 0.88,
                    "fractalContext": "scientific"
                }
            }
            
            response = requests.post(
                f"{self.base_url}/inbox",
                json=scientific_contribution,
                headers={"Content-Type": "application/activity+json"},
                timeout=10
            )
            
            if response.status_code == 202:
                tests.append(("Scientific Contribution", True, "Contribution to scientific subnode accepted"))
            else:
                tests.append(("Scientific Contribution", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Scientific Contribution", False, str(e)))
        
        # Test 2: Contribute to symbolic subnode
        try:
            symbolic_contribution = {
                "type": "Create",
                "actor": "archetypal_explorer",
                "object": {
                    "type": "Contribution",
                    "nodeId": "codex:Void:symbolic:archetypal",
                    "content": "The Void embodies the primordial chaos archetype",
                    "resonance": 0.92,
                    "fractalContext": "symbolic"
                }
            }
            
            response = requests.post(
                f"{self.base_url}/inbox",
                json=symbolic_contribution,
                headers={"Content-Type": "application/activity+json"},
                timeout=10
            )
            
            if response.status_code == 202:
                tests.append(("Symbolic Contribution", True, "Contribution to symbolic subnode accepted"))
            else:
                tests.append(("Symbolic Contribution", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Symbolic Contribution", False, str(e)))
        
        # Test 3: Contribute to water subnode
        try:
            water_contribution = {
                "type": "Create",
                "actor": "water_explorer",
                "object": {
                    "type": "Contribution",
                    "nodeId": "codex:Void:water:phase",
                    "content": "The Void exists in a plasma phase of infinite potential",
                    "resonance": 0.85,
                    "fractalContext": "water"
                }
            }
            
            response = requests.post(
                f"{self.base_url}/inbox",
                json=water_contribution,
                headers={"Content-Type": "application/activity+json"},
                timeout=10
            )
            
            if response.status_code == 202:
                tests.append(("Water Contribution", True, "Contribution to water subnode accepted"))
            else:
                tests.append(("Water Contribution", False, f"Status {response.status_code}"))
        except Exception as e:
            tests.append(("Water Contribution", False, str(e)))
        
        # Display results
        all_passed = True
        for test_name, passed, details in tests:
            status = "✓" if passed else "✗"
            self.log(f"{status} {test_name}: {details}")
            if not passed:
                all_passed = False
        
        self.test_results.extend(tests)
        return all_passed
    
    def generate_comprehensive_report(self):
        """Generate comprehensive test report for both levels"""
        self.log("\n" + "="*80)
        self.log("LIVING CODEX PHASE 5 - COMPREHENSIVE FRACTAL LEVEL TEST REPORT")
        self.log("="*80)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for _, passed, _ in self.test_results if passed)
        failed_tests = total_tests - passed_tests
        
        self.log(f"\nSUMMARY:")
        self.log(f"Total Tests: {total_tests}")
        self.log(f"Passed: {passed_tests}")
        self.log(f"Failed: {failed_tests}")
        self.log(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        # Categorize tests
        current_level_tests = [t for t in self.test_results if any(keyword in t[0] for keyword in 
            ["Root Endpoint", "Storage Stats", "Post Contribution", "Retrieve Contribution", "ActivityPub"])]
        fractal_level_tests = [t for t in self.test_results if any(keyword in t[0] for keyword in 
            ["Fractal", "Scientific", "Symbolic", "Water"])]
        
        current_passed = sum(1 for t in current_level_tests if t[1])
        fractal_passed = sum(1 for t in fractal_level_tests if t[1])
        
        self.log(f"\nLEVEL BREAKDOWN:")
        self.log(f"Current Level (Phase 4): {current_passed}/{len(current_level_tests)} tests passed")
        self.log(f"Next Fractal Level (Phase 5): {fractal_passed}/{len(fractal_level_tests)} tests passed")
        
        if failed_tests == 0:
            self.log("\n🎉 ALL TESTS PASSED! Both levels are working perfectly!")
            self.log("✅ Current Level: Full Phase 4 compatibility")
            self.log("✅ Next Fractal Level: Complete Phase 5 expansion")
        else:
            self.log(f"\n⚠️  {failed_tests} test(s) failed. Check the details above.")
            
        self.log("\nDETAILED RESULTS:")
        for i, (test_name, passed, details) in enumerate(self.test_results, 1):
            status = "PASS" if passed else "FAIL"
            level = "Phase 4" if any(keyword in test_name for keyword in 
                ["Root Endpoint", "Storage Stats", "Post Contribution", "Retrieve Contribution", "ActivityPub"]) else "Phase 5"
            self.log(f"{i:2d}. {status}: [{level}] {test_name} - {details}")
            
        self.log("\n" + "="*80)
        
        return failed_tests == 0
    
    def run_full_test_suite(self) -> bool:
        """Run the complete test suite for both levels"""
        self.log("🌊 Living Codex Phase 5 - Fractal Level Testing")
        self.log("="*60)
        self.log("Testing both current level (Phase 4) and next fractal level (Phase 5)")
        
        try:
            # Test current level (Phase 4 compatibility)
            current_success = self.test_current_level()
            
            # Test next fractal level (Phase 5 features)
            fractal_success = self.test_next_fractal_level()
            
            # Test fractal contributions
            contribution_success = self.test_fractal_contribution()
            
            # Generate comprehensive report
            overall_success = self.generate_comprehensive_report()
            
            return overall_success
            
        except Exception as e:
            self.log(f"Test suite failed: {e}", "ERROR")
            return False

def main():
    """Main entry point"""
    print("🌊 Living Codex Phase 5 - Fractal Level Testing")
    print("="*60)
    print("This will test BOTH levels:")
    print("• Current Level (Phase 4): Federation & Storage compatibility")
    print("• Next Fractal Level (Phase 5): Node expansion & multi-context")
    print("="*60)
    
    tester = FractalLevelTester()
    
    try:
        success = tester.run_full_test_suite()
        if success:
            print("\n🎉 SUCCESS: Both fractal levels are working perfectly!")
            print("✅ Phase 4: Full compatibility maintained")
            print("✅ Phase 5: Fractal expansion operational")
        else:
            print("\n⚠️  Some tests failed. Check the detailed report above.")
        
        return success
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Testing interrupted by user")
        return False
    except Exception as e:
        print(f"\n\n❌ Test suite crashed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
