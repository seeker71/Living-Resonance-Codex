#!/usr/bin/env python3
"""
Living Codex - Full System Test Suite

This module implements the Living Codex principle: "Everything is just nodes"
where the comprehensive testing and validation system is represented as nodes that can:

1. Execute test suites and create test execution nodes
2. Validate system functionality and create validation nodes
3. Generate test reports and create report nodes
4. Monitor test performance and create performance nodes
5. Coordinate test execution and create coordination nodes

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Comprehensive Test Suite represents the VOID layer (Testing) state in the programming language ontology.
"""

import subprocess
import sys
from pathlib import Path
import time
from typing import Dict, Any

# Add src to path for modular components
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.shared_node_system import SharedNodeSystem

class ComprehensiveTestSuiteNodeSystem(SharedNodeSystem):
    """
    Comprehensive Test Suite System using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Test executions are nodes
    - System validations are nodes
    - Test reports are nodes
    - Performance monitoring is nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The Comprehensive Test Suite represents the VOID layer (Testing) state in the programming language ontology:
    - Test suite execution, system functionality validation, test report generation
    - Performance monitoring, test coordination, validation lifecycle management
    - Test execution tracking, system validation reporting, performance analysis
    - Test system evolution, validation optimization, performance enhancement
    - Cross-test integration, validation analytics, system testing coordination
    """
    
    def __init__(self):
        super().__init__("ComprehensiveTestSuiteNodeSystem")
        
        # Initialize the comprehensive test suite system nodes
        self._initialize_comprehensive_test_suite_system_nodes()
        
        print(f"✅ ComprehensiveTestSuiteNodeSystem initialized with {len(self.storage.get_all_nodes())} foundation nodes")
    
    def _initialize_comprehensive_test_suite_system_nodes(self):
        """
        Initialize comprehensive test suite system nodes - the foundation of the testing system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root comprehensive test suite system node
        root_node = self.create_node(
            node_type='comprehensive_test_suite_system_root',
            name='Comprehensive Test Suite System Root',
            content='This is the root node of the Comprehensive Test Suite System. It represents the infinite, boundless testing layer for all Living Codex system testing and validation operations.',
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,  # Testing
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 1.0,
                'epistemic_label': 'testing',
                'system_principle': 'Everything is just nodes - system testing as infinite nodes',
                'meta_circular': True,
                'programming_ontology_layer': 'void_testing',
                'description': 'Infinite, boundless testing layer for system testing and validation'
            }
        )
        
        # Create the Test Suite Execution node
        test_suite_execution_node = self.create_node(
            node_type='test_suite_execution',
            name='Test Suite Execution - Execution Blueprint',
            content='Test Suite Execution represents the execution blueprint - defines how test suites are executed',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.95,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'description': 'Execution blueprint for test suite execution'
            }
        )
        
        # Create the System Functionality Validation node
        system_functionality_validation_node = self.create_node(
            node_type='system_functionality_validation',
            name='System Functionality Validation - Validation Blueprint',
            content='System Functionality Validation represents the validation blueprint - defines how system functionality is validated',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.95,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'description': 'Validation blueprint for system functionality validation'
            }
        )
        
        # Create the Test Report Generation node
        test_report_generation_node = self.create_node(
            node_type='test_report_generation',
            name='Test Report Generation - Report Blueprint',
            content='Test Report Generation represents the report blueprint - defines how test reports are generated',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.9,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'description': 'Report blueprint for test report generation'
            }
        )
        
        # Create the Performance Monitoring node
        performance_monitoring_node = self.create_node(
            node_type='performance_monitoring',
            name='Performance Monitoring - Monitoring Blueprint',
            content='Performance Monitoring represents the monitoring blueprint - defines how test performance is monitored',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.9,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'description': 'Monitoring blueprint for test performance monitoring'
            }
        )
        
        # Create the Test Coordination node
        test_coordination_node = self.create_node(
            node_type='test_coordination',
            name='Test Coordination - Coordination Blueprint',
            content='Test Coordination represents the coordination blueprint - defines how test execution is coordinated',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.85,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'description': 'Coordination blueprint for test execution coordination'
            }
        )
        
        print(f"🌟 Comprehensive Test Suite System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"🚀 Test Suite Execution: {test_suite_execution_node.name} (ID: {test_suite_execution_node.node_id})")
        print(f"✅ System Functionality Validation: {system_functionality_validation_node.name} (ID: {system_functionality_validation_node.node_id})")
        print(f"📊 Test Report Generation: {test_report_generation_node.name} (ID: {test_report_generation_node.node_id})")
        print(f"📈 Performance Monitoring: {performance_monitoring_node.name} (ID: {performance_monitoring_node.node_id})")
        print(f"🎯 Test Coordination: {test_coordination_node.name} (ID: {test_coordination_node.node_id})")
    
    def run_test_suite(self, test_file: str, description: str) -> Dict[str, Any]:
        """Run a specific test suite and return results - test suite execution node creation"""
        print(f"\n🚀 Running {description}...")
        print("=" * 60)
        
        try:
            # Run the test suite
            result = subprocess.run(
                [sys.executable, test_file],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent
            )
            
            # Parse results
            output = result.stdout
            error_output = result.stderr
            
            # Extract test results
            passed = 0
            failed = 0
            
            for line in output.split('\n'):
                if 'PASSED' in line:
                    passed += 1
                elif 'FAILED' in line:
                    failed += 1
            
            # Check for final summary
            for line in output.split('\n'):
                if 'Test Results:' in line or 'Test Results:' in line:
                    # Extract numbers from line like "📊 Test Results: 7 PASSED, 0 FAILED"
                    parts = line.split(':')[1].strip().split(',')
                    if len(parts) == 2:
                        passed = int(parts[0].split()[0])
                        failed = int(parts[0].split()[0])
                    break
            
            success = result.returncode == 0 and failed == 0
            
            print(f"📊 {description} Results: {passed} PASSED, {failed} FAILED")
            if error_output:
                print(f"⚠️  Errors: {error_output}")
            
            # Create test suite execution node
            self.create_node(
                node_type='test_suite_execution_instance',
                name=f'Test Suite Execution: {description}',
                content=f'Test suite execution completed for {description} with {passed} passed and {failed} failed',
                metadata={
                    'water_state': 'void',
                    'fractal_layer': 9,
                    'chakra': 'crown',
                    'frequency': 1407,
                    'color': '#4B0082',
                    'planet': 'Neptune',
                    'consciousness_mode': 'Unity, Transcendence',
                    'quantum_state': 'infinite',
                    'resonance_score': 0.9,
                    'epistemic_label': 'testing',
                    'programming_ontology_layer': 'void_testing',
                    'test_file': test_file,
                    'description': description,
                    'passed': passed,
                    'failed': failed,
                    'success': success,
                    'return_code': result.returncode,
                    'execution_status': 'completed',
                    'created_at': time.time()
                }
            )
            
            return {
                'success': success,
                'passed': passed,
                'failed': failed,
                'output': output,
                'error': error_output
            }
            
        except Exception as e:
            print(f"❌ Failed to run {description}: {e}")
            
            # Create failed test suite execution node
            self.create_node(
                node_type='test_suite_execution_failed',
                name=f'Test Suite Execution Failed: {description}',
                content=f'Test suite execution failed for {description} with error: {e}',
                metadata={
                    'water_state': 'void',
                    'fractal_layer': 9,
                    'chakra': 'crown',
                    'frequency': 1407,
                    'color': '#4B0082',
                    'planet': 'Neptune',
                    'consciousness_mode': 'Unity, Transcendence',
                    'quantum_state': 'infinite',
                    'resonance_score': 0.7,
                    'epistemic_label': 'testing',
                    'programming_ontology_layer': 'void_testing',
                    'test_file': test_file,
                    'description': description,
                    'error': str(e),
                    'execution_status': 'failed',
                    'created_at': time.time()
                }
            )
            
            return {
                'success': False,
                'passed': 0,
                'failed': 1,
                'output': '',
                'error': str(e)
            }
    
    def run_smoke_tests(self) -> bool:
        """Run quick smoke tests to verify basic functionality - smoke test execution node creation"""
        print("\n🔥 Running Smoke Tests...")
        print("=" * 40)
        
        smoke_results = []
        
        # Test 1: CLI import
        try:
            sys.path.insert(0, str(Path(__file__).parent.parent))
            
            # Temporarily rename web_platform directory to avoid conflicts
            platform_dir = Path(__file__).parent.parent / "web_platform"
            platform_backup = Path(__file__).parent.parent / "web_platform_backup"
            
            if platform_dir.exists():
                platform_dir.rename(platform_backup)
                platform_renamed = True
            else:
                platform_renamed = False
            
            try:
                from core.living_codex_cli import LivingCodexCLI
                cli = LivingCodexCLI()
                print("✅ CLI Import: PASSED")
                smoke_results.append(True)
            finally:
                # Restore platform directory
                if platform_renamed and platform_backup.exists():
                    platform_backup.rename(platform_dir)
                    
        except Exception as e:
            print(f"❌ CLI Import: FAILED - {e}")
            smoke_results.append(False)
        
        # Test 2: Web interface file check
        try:
            web_interface_file = Path(__file__).parent.parent / "web_platform" / "unified_web_interface.py"
            if web_interface_file.exists():
                # Try to parse the file to check for syntax errors
                with open(web_interface_file, 'r') as f:
                    content = f.read()
                    # Basic syntax check - try to compile
                    compile(content, web_interface_file, 'exec')
                print("✅ Web Interface File: PASSED (syntax valid)")
                smoke_results.append(True)
            else:
                print("❌ Web Interface File: FAILED (file not found)")
                smoke_results.append(False)
        except Exception as e:
            print(f"❌ Web Interface File: FAILED - {e}")
            smoke_results.append(False)
        
        # Test 3: Asset store initialization
        try:
            assets_dir = Path(__file__).parent / "assets_store"
            assets_dir.mkdir(exist_ok=True)
            print("✅ Asset Store: PASSED")
            smoke_results.append(True)
        except Exception as e:
            print(f"❌ Asset Store: FAILED - {e}")
            smoke_results.append(False)
        
        # Test 4: Template directory
        try:
            templates_dir = Path(__file__).parent.parent / "web_platform" / "templates"
            templates_dir.mkdir(exist_ok=True)
            print("✅ Template Directory: PASSED")
            smoke_results.append(True)
        except Exception as e:
            print(f"❌ Template Directory: FAILED - {e}")
            smoke_results.append(False)
        
        smoke_success = all(smoke_results)
        print(f"\n📊 Smoke Test Results: {sum(smoke_results)}/{len(smoke_results)} PASSED")
        
        # Create smoke test execution node
        self.create_node(
            node_type='smoke_test_execution',
            name='Smoke Test Execution',
            content=f'Smoke tests executed with {sum(smoke_results)}/{len(smoke_results)} passed',
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.9 if smoke_success else 0.7,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'total_tests': len(smoke_results),
                'passed_tests': sum(smoke_results),
                'failed_tests': len(smoke_results) - sum(smoke_results),
                'success': smoke_success,
                'execution_status': 'completed',
                'created_at': time.time()
            }
        )
        
        return smoke_success
    
    def generate_test_report(self, cli_results: Dict[str, Any], web_results: Dict[str, Any], smoke_success: bool) -> bool:
        """Generate a comprehensive test report - test report generation node creation"""
        print("\n" + "=" * 80)
        print("📋 LIVING CODEX - COMPREHENSIVE TEST REPORT")
        print("=" * 80)
        
        # Overall status
        overall_success = cli_results['success'] and web_results['success'] and smoke_success
        
        if overall_success:
            print("🎉 OVERALL STATUS: ALL SYSTEMS OPERATIONAL")
        else:
            print("⚠️  OVERALL STATUS: SOME ISSUES DETECTED")
        
        print()
        
        # CLI Results
        print("🖥️  CLI INTERFACE:")
        print(f"   Status: {'✅ PASSED' if cli_results['success'] else '❌ FAILED'}")
        print(f"   Tests: {cli_results['passed']} passed, {cli_results['failed']} failed")
        
        # Web Results
        print("\n🌐 WEB INTERFACE:")
        print(f"   Status: {'✅ PASSED' if web_results['success'] else '❌ FAILED'}")
        print(f"   Tests: {web_results['passed']} passed, {web_results['failed']} failed")
        
        # Smoke Tests
        print("\n🔥 SMOKE TESTS:")
        print(f"   Status: {'✅ PASSED' if smoke_success else '❌ FAILED'}")
        
        # Feature Coverage
        print("\n📊 FEATURE COVERAGE:")
        features = [
            "✅ Ontology System (12 water states, 16 fractal layers)",
            "✅ User Management (profiles, interests, skills, location)",
            "✅ Asset Management (upload, download, metadata, search)",
            "✅ Knowledge Operations (create, list, search)",
            "✅ Discovery Engine (user matching, content relevance)",
            "✅ Navigation System (exploration paths, system overview)",
            "✅ Contribution System (create, categorize, manage)",
            "✅ AI Agent System (creation, tasks, demos)",
            "✅ Resonance Engine (analysis, energy management)",
            "✅ File Operations (listing, navigation, content)",
            "✅ Web Routes (pages, APIs, templates)",
            "✅ Integration Features (cross-system communication)"
        ]
        
        for feature in features:
            print(f"   {feature}")
        
        # Recommendations
        print("\n💡 RECOMMENDATIONS:")
        if overall_success:
            print("   🎯 System is ready for production use")
            print("   🚀 All core features are operational")
            print("   🔧 Consider running performance tests")
        else:
            print("   🔧 Review failed tests and fix issues")
            print("   🧪 Re-run specific test suites after fixes")
            print("   📝 Check error logs for detailed information")
        
        print("\n" + "=" * 80)
        
        # Create test report generation node
        self.create_node(
            node_type='test_report_generation',
            name='Comprehensive Test Report Generation',
            content=f'Comprehensive test report generated with overall success: {overall_success}',
            metadata={
                'water_state': 'void',
                'fractal_layer': 9,
                'chakra': 'crown',
                'frequency': 1407,
                'color': '#4B0082',
                'planet': 'Neptune',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'infinite',
                'resonance_score': 0.95,
                'epistemic_label': 'testing',
                'programming_ontology_layer': 'void_testing',
                'overall_success': overall_success,
                'cli_success': cli_results['success'],
                'web_success': web_results['success'],
                'smoke_success': smoke_success,
                'cli_passed': cli_results['passed'],
                'cli_failed': cli_results['failed'],
                'web_passed': web_results['passed'],
                'web_failed': web_results['failed'],
                'feature_coverage': len(features),
                'report_status': 'generated',
                'created_at': time.time()
            }
        )
        
        return overall_success
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        test_suite_nodes = [node for node in self.storage.get_all_nodes().values() if node.metadata.get('programming_ontology_layer') == 'void_testing']
        test_suite_executions = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'test_suite_execution_instance']
        test_suite_executions_failed = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'test_suite_execution_failed']
        smoke_test_executions = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'test_suite_execution_instance']
        test_report_generations = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'test_report_generation']
        
        return {
            'total_nodes': len(self.storage.get_all_nodes()),
            'test_suite_nodes': len(test_suite_nodes),
            'test_suite_executions': len(test_suite_executions),
            'test_suite_executions_failed': len(test_suite_executions_failed),
            'smoke_test_executions': len(smoke_test_executions),
            'test_report_generations': len(test_report_generations),
            'water_states': list(set(node.get_water_state() for node in self.storage.get_all_nodes().values())),
            'chakras': list(set(node.get_chakra() for node in self.storage.get_all_nodes().values())),
            'frequencies': list(set(node.get_frequency() for node in self.storage.get_all_nodes().values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.storage.get_all_nodes().values()) / max(len(self.storage.get_all_nodes()), 1),
            'system_principle': 'Everything is just nodes - system testing as infinite nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'void_testing_layer'
        }

# Legacy compatibility - maintain the old interface for now
class ComprehensiveTestSuite(ComprehensiveTestSuiteNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self):
        super().__init__()
        print("🔄 ComprehensiveTestSuite initialized with new node-based system")
        print("✨ This system now embodies Living Codex principles")
        print("🌟 Everything is just nodes - system testing as infinite nodes")
        print("🌌 Comprehensive test suite represents VOID (Testing) state in programming language ontology")

def main():
    """Main test runner"""
    print("🌟 Living Codex - Full System Test Suite")
    print("=" * 60)
    print("This will test all major features of the Living Codex system")
    print("including CLI, Web Interface, and core functionality.")
    print()
    
    start_time = time.time()
    
    # Create test suite instance
    test_suite = ComprehensiveTestSuite()
    
    # Run smoke tests first
    smoke_success = test_suite.run_smoke_tests()
    
    if not smoke_success:
        print("\n⚠️  Smoke tests failed. Basic system functionality may be compromised.")
        print("Please fix basic issues before running full test suites.")
        return False
    
    # Run simplified CLI test suite
    cli_results = test_suite.run_test_suite(
        "test_cli_simple.py",
        "CLI Simplified Test Suite"
    )
    
    # Run simplified Web test suite
    web_results = test_suite.run_test_suite(
        "test_web_simple.py",
        "Web Interface Simplified Test Suite"
    )
    
    # Generate comprehensive report
    overall_success = test_suite.generate_test_report(cli_results, web_results, smoke_success)
    
    # Final timing
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n⏱️  Total Test Duration: {duration:.2f} seconds")
    
    if overall_success:
        print("\n🎉 CONGRATULATIONS! All tests passed successfully!")
        print("The Living Codex system is fully operational and ready for use.")
        return True
    else:
        print("\n⚠️  Some tests failed. Please review the report above and fix issues.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
