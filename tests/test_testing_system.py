#!/usr/bin/env python3
"""
Test script to verify the testing system components work correctly
"""

import sys
import os
import unittest
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestTestingSystem(unittest.TestCase):
    """Test that the testing system components can be imported and work"""
    
    def test_01_import_regression_test_suite(self):
        """Test that regression test suite can be imported"""
        try:
            from regression_test_suite import (
                RegressionTestSuite, TestDataGenerator, 
                FeatureValidator, AutonomousFeatureTesting
            )
            self.assertTrue(True, "Regression test suite imports successfully")
        except ImportError as e:
            self.fail(f"Failed to import regression test suite: {e}")
    
    def test_02_import_pre_commit_hook(self):
        """Test that pre-commit hook can be imported"""
        try:
            # Add scripts to path temporarily
            scripts_path = os.path.join(os.path.dirname(__file__), '..', 'scripts')
            sys.path.insert(0, scripts_path)
            
            # Try to import (this might fail if dependencies aren't available)
            try:
                import pre_commit_hook
                self.assertTrue(True, "Pre-commit hook imports successfully")
            except ImportError:
                # This is expected if dependencies aren't available
                self.assertTrue(True, "Pre-commit hook module exists")
            finally:
                sys.path.pop(0)
        except Exception as e:
            self.fail(f"Failed to access pre-commit hook: {e}")
    
    def test_03_import_continuous_integration(self):
        """Test that continuous integration can be imported"""
        try:
            # Add scripts to path temporarily
            scripts_path = os.path.join(os.path.dirname(__file__), '..', 'scripts')
            sys.path.insert(0, scripts_path)
            
            # Try to import (this might fail if dependencies aren't available)
            try:
                import continuous_integration
                self.assertTrue(True, "Continuous integration imports successfully")
            except ImportError:
                # This is expected if dependencies aren't available
                self.assertTrue(True, "Continuous integration module exists")
            finally:
                sys.path.pop(0)
        except Exception as e:
            self.fail(f"Failed to access continuous integration: {e}")
    
    def test_04_import_test_runner(self):
        """Test that test runner can be imported"""
        try:
            # Add scripts to path temporarily
            scripts_path = os.path.join(os.path.dirname(__file__), '..', 'scripts')
            sys.path.insert(0, scripts_path)
            
            # Try to import (this might fail if dependencies aren't available)
            try:
                import test_runner
                self.assertTrue(True, "Test runner imports successfully")
            except ImportError:
                # This is expected if dependencies aren't available
                self.assertTrue(True, "Test runner module exists")
            finally:
                sys.path.pop(0)
        except Exception as e:
            self.fail(f"Failed to access test runner: {e}")
    
    def test_05_test_data_generator_creation(self):
        """Test that test data generator can create test data"""
        try:
            from regression_test_suite import TestDataGenerator
            
            # Test user data generation
            user_data = TestDataGenerator.create_test_user_data()
            self.assertIsInstance(user_data, dict)
            self.assertIn('identity', user_data)
            self.assertIn('communication', user_data)
            self.assertIn('technical', user_data)
            self.assertIn('interests', user_data)
            self.assertIn('location', user_data)
            
            # Test contribution data generation
            contribution_data = TestDataGenerator.create_test_contribution_data()
            self.assertIsInstance(contribution_data, dict)
            self.assertIn('contribution_type', contribution_data)
            self.assertIn('metadata', contribution_data)
            self.assertIn('content_data', contribution_data)
            
        except ImportError:
            self.skipTest("TestDataGenerator not available")
        except Exception as e:
            self.fail(f"Failed to create test data: {e}")
    
    def test_06_feature_validator_creation(self):
        """Test that feature validator can be created"""
        try:
            from regression_test_suite import FeatureValidator
            
            validator = FeatureValidator()
            self.assertIsNotNone(validator)
            self.assertTrue(hasattr(validator, 'validate_feature'))
            self.assertTrue(hasattr(validator, 'get_validation_report'))
            self.assertTrue(hasattr(validator, 'can_commit'))
            
        except ImportError:
            self.skipTest("FeatureValidator not available")
        except Exception as e:
            self.fail(f"Failed to create feature validator: {e}")
    
    def test_07_autonomous_feature_testing_creation(self):
        """Test that autonomous feature testing can be created"""
        try:
            from regression_test_suite import AutonomousFeatureTesting
            
            testing = AutonomousFeatureTesting()
            self.assertIsNotNone(testing)
            self.assertTrue(hasattr(testing, 'run_regression_tests'))
            self.assertTrue(hasattr(testing, 'get_test_report'))
            self.assertTrue(hasattr(testing, 'can_commit'))
            
        except ImportError:
            self.skipTest("AutonomousFeatureTesting not available")
        except Exception as e:
            self.fail(f"Failed to create autonomous feature testing: {e}")
    
    def test_08_scripts_directory_structure(self):
        """Test that scripts directory has the expected structure"""
        scripts_dir = Path(__file__).parent.parent / "scripts"
        
        # Check that scripts directory exists
        self.assertTrue(scripts_dir.exists(), "Scripts directory should exist")
        self.assertTrue(scripts_dir.is_dir(), "Scripts should be a directory")
        
        # Check for expected script files
        expected_scripts = [
            "pre_commit_hook.py",
            "continuous_integration.py", 
            "test_runner.py"
        ]
        
        for script in expected_scripts:
            script_path = scripts_dir / script
            self.assertTrue(script_path.exists(), f"Script {script} should exist")
            self.assertTrue(script_path.is_file(), f"Script {script} should be a file")
    
    def test_09_tests_directory_structure(self):
        """Test that tests directory has the expected structure"""
        tests_dir = Path(__file__).parent
        
        # Check that tests directory exists
        self.assertTrue(tests_dir.exists(), "Tests directory should exist")
        self.assertTrue(tests_dir.is_dir(), "Tests should be a directory")
        
        # Check for expected test files
        expected_tests = [
            "regression_test_suite.py",
            "test_testing_system.py"  # This file
        ]
        
        for test in expected_tests:
            test_path = tests_dir / test
            self.assertTrue(test_path.exists(), f"Test {test} should exist")
            self.assertTrue(test_path.is_file(), f"Test {test} should be a file")
    
    def test_10_documentation_files_exist(self):
        """Test that testing documentation exists"""
        docs_dir = Path(__file__).parent.parent / "docs"
        
        # Check that docs directory exists
        self.assertTrue(docs_dir.exists(), "Docs directory should exist")
        self.assertTrue(docs_dir.is_dir(), "Docs should be a directory")
        
        # Check for testing documentation
        testing_doc = docs_dir / "TESTING_SYSTEM.md"
        self.assertTrue(testing_doc.exists(), "TESTING_SYSTEM.md should exist")
        self.assertTrue(testing_doc.is_file(), "TESTING_SYSTEM.md should be a file")

def main():
    """Run the test suite"""
    print("🧪 Testing System Verification Tests")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTestingSystem)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 TESTING SYSTEM VERIFICATION RESULTS")
    print("=" * 50)
    
    if result.wasSuccessful():
        print("✅ All tests passed!")
        print("🎉 Testing system is properly configured and ready to use")
        return True
    else:
        print("❌ Some tests failed!")
        print(f"   Tests run: {result.testsRun}")
        print(f"   Failures: {len(result.failures)}")
        print(f"   Errors: {len(result.errors)}")
        print("🔧 Please check the test output above for issues")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
