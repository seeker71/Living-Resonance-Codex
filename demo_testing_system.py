#!/usr/bin/env python3
"""
Living Codex Platform - Testing System Demo
Demonstrates the comprehensive testing system capabilities
"""

import sys
import os
import time
from pathlib import Path

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🌟 {title}")
    print("=" * 60)

def print_section(title):
    """Print a formatted section header"""
    print(f"\n📋 {title}")
    print("-" * 40)

def demo_regression_test_suite():
    """Demonstrate the regression test suite"""
    print_section("Regression Test Suite Demo")
    
    try:
        # Import the regression test suite
        from tests.regression_test_suite import (
            RegressionTestSuite, TestDataGenerator, 
            FeatureValidator, AutonomousFeatureTesting
        )
        
        print("✅ Successfully imported regression test suite components")
        
        # Create test data generator
        print("\n🔧 Creating test data generator...")
        data_generator = TestDataGenerator()
        
        # Generate sample test data
        user_data = TestDataGenerator.create_test_user_data()
        contribution_data = TestDataGenerator.create_test_contribution_data()
        
        print(f"✅ Generated test user data: {user_data['username']} ({user_data['email']})")
        print(f"✅ Generated test contribution: {contribution_data['title']}")
        
        # Create feature validator
        print("\n🔧 Creating feature validator...")
        validator = FeatureValidator()
        print("✅ Feature validator created successfully")
        
        # Create autonomous feature testing
        print("\n🔧 Creating autonomous feature testing...")
        testing = AutonomousFeatureTesting()
        print("✅ Autonomous feature testing created successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import regression test suite: {e}")
        return False
    except Exception as e:
        print(f"💥 Error during regression test suite demo: {e}")
        return False

def demo_pre_commit_hook():
    """Demonstrate the pre-commit hook"""
    print_section("Pre-Commit Hook Demo")
    
    try:
        # Check if scripts directory exists
        scripts_dir = Path(__file__).parent / "scripts"
        if not scripts_dir.exists():
            print("❌ Scripts directory not found")
            return False
        
        # Check for pre-commit hook
        pre_commit_script = scripts_dir / "pre_commit_hook.py"
        if not pre_commit_script.exists():
            print("❌ Pre-commit hook script not found")
            return False
        
        print("✅ Pre-commit hook script found")
        print(f"   Location: {pre_commit_script}")
        
        # Check if git hooks directory exists
        git_hooks_dir = Path(__file__).parent / ".git" / "hooks"
        if git_hooks_dir.exists():
            print("✅ Git repository found")
            print(f"   Hooks directory: {git_hooks_dir}")
            
            # Check for existing pre-commit hook
            existing_hook = git_hooks_dir / "pre-commit"
            if existing_hook.exists():
                print("✅ Pre-commit hook already installed")
            else:
                print("ℹ️  Pre-commit hook not yet installed")
                print("   Run: python scripts/pre_commit_hook.py --setup")
        else:
            print("ℹ️  Not in a git repository")
            print("   Initialize git to use pre-commit hooks")
        
        return True
        
    except Exception as e:
        print(f"💥 Error during pre-commit hook demo: {e}")
        return False

def demo_continuous_integration():
    """Demonstrate the continuous integration system"""
    print_section("Continuous Integration Demo")
    
    try:
        # Check if scripts directory exists
        scripts_dir = Path(__file__).parent / "scripts"
        if not scripts_dir.exists():
            print("❌ Scripts directory not found")
            return False
        
        # Check for CI script
        ci_script = scripts_dir / "continuous_integration.py"
        if not ci_script.exists():
            print("❌ Continuous integration script not found")
            return False
        
        print("✅ Continuous integration script found")
        print(f"   Location: {ci_script}")
        
        # Check for CI reports directory
        ci_reports_dir = Path(__file__).parent / "ci_reports"
        if ci_reports_dir.exists():
            print("✅ CI reports directory exists")
            
            # List existing reports
            report_files = list(ci_reports_dir.glob("*.json"))
            if report_files:
                print(f"   Found {len(report_files)} CI reports:")
                for report in report_files[-3:]:  # Show last 3 reports
                    print(f"     📊 {report.name}")
            else:
                print("   No CI reports found yet")
        else:
            print("ℹ️  CI reports directory will be created when CI runs")
        
        print("\n🚀 To run CI pipeline:")
        print("   python scripts/continuous_integration.py")
        
        return True
        
    except Exception as e:
        print(f"💥 Error during continuous integration demo: {e}")
        return False

def demo_test_runner():
    """Demonstrate the test runner"""
    print_section("Test Runner Demo")
    
    try:
        # Check if scripts directory exists
        scripts_dir = Path(__file__).parent / "scripts"
        if not scripts_dir.exists():
            print("❌ Scripts directory not found")
            return False
        
        # Check for test runner script
        test_runner_script = scripts_dir / "test_runner.py"
        if not test_runner_script.exists():
            print("❌ Test runner script not found")
            return False
        
        print("✅ Test runner script found")
        print(f"   Location: {test_runner_script}")
        
        # Check for test reports directory
        test_reports_dir = Path(__file__).parent / "test_reports"
        if test_reports_dir.exists():
            print("✅ Test reports directory exists")
            
            # List existing reports
            report_files = list(test_reports_dir.glob("*.json"))
            if report_files:
                print(f"   Found {len(report_files)} test reports:")
                for report in report_files[-3:]:  # Show last 3 reports
                    print(f"     📊 {report.name}")
            else:
                print("   No test reports found yet")
        else:
            print("ℹ️  Test reports directory will be created when tests run")
        
        print("\n🚀 To run test suite:")
        print("   python scripts/test_runner.py")
        print("\n🔧 Common options:")
        print("   --pattern 'test_*.py'     # Run specific test pattern")
        print("   --parallel                # Enable parallel execution")
        print("   --verbose                 # Verbose output")
        print("   --stop-on-failure        # Stop on first failure")
        
        return True
        
    except Exception as e:
        print(f"💥 Error during test runner demo: {e}")
        return False

def demo_testing_workflow():
    """Demonstrate the complete testing workflow"""
    print_section("Complete Testing Workflow Demo")
    
    print("🔄 The Living Codex Platform testing workflow:")
    print("\n1️⃣  Development Phase:")
    print("   • Developer writes code and tests")
    print("   • Local testing with test runner")
    print("   • Manual validation of features")
    
    print("\n2️⃣  Pre-Commit Phase:")
    print("   • Git pre-commit hook automatically runs")
    print("   • Code quality checks (syntax, imports)")
    print("   • File size validation")
    print("   • Regression test suite execution")
    print("   • Commit only proceeds if all checks pass")
    
    print("\n3️⃣  Continuous Integration Phase:")
    print("   • Automated CI pipeline runs")
    print("   • Comprehensive test execution")
    print("   • Performance benchmarking")
    print("   • Code coverage analysis")
    print("   • Detailed reporting and notifications")
    
    print("\n4️⃣  Autonomous Testing Phase:")
    print("   • New features automatically tested")
    print("   • System integrity validation")
    print("   • Regression detection")
    print("   • Safe deployment decisions")
    
    print("\n🎯 Benefits:")
    print("   ✅ Prevents regressions")
    print("   ✅ Maintains code quality")
    print("   ✅ Ensures system stability")
    print("   ✅ Provides confidence in changes")
    print("   ✅ Enables rapid development")
    
    return True

def run_quick_test():
    """Run a quick test to verify the testing system works"""
    print_section("Quick System Test")
    
    try:
        # Run the testing system verification test
        test_script = Path(__file__).parent / "tests" / "test_testing_system.py"
        
        if not test_script.exists():
            print("❌ Testing system verification test not found")
            return False
        
        print("🧪 Running testing system verification test...")
        
        # Import and run the test
        import subprocess
        result = subprocess.run([
            sys.executable, str(test_script)
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Testing system verification test passed!")
            print("🎉 All testing system components are working correctly")
            return True
        else:
            print("❌ Testing system verification test failed!")
            print("\n📋 Test Output:")
            print(result.stdout)
            if result.stderr:
                print("\n🚨 Test Errors:")
                print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Test timed out after 60 seconds")
        return False
    except Exception as e:
        print(f"💥 Error running quick test: {e}")
        return False

def main():
    """Main demonstration function"""
    print_header("Living Codex Platform - Testing System Demo")
    
    print("This demo showcases the comprehensive testing system that ensures")
    print("code quality, prevents regressions, and maintains system integrity.")
    
    demos = [
        ("Regression Test Suite", demo_regression_test_suite),
        ("Pre-Commit Hook", demo_pre_commit_hook),
        ("Continuous Integration", demo_continuous_integration),
        ("Test Runner", demo_test_runner),
        ("Testing Workflow", demo_testing_workflow),
        ("Quick System Test", run_quick_test)
    ]
    
    results = []
    
    for demo_name, demo_func in demos:
        try:
            print(f"\n{'='*20} {demo_name} {'='*20}")
            success = demo_func()
            results.append((demo_name, success))
            
            if success:
                print(f"✅ {demo_name} demo completed successfully")
            else:
                print(f"❌ {demo_name} demo failed")
                
        except Exception as e:
            print(f"💥 {demo_name} demo crashed: {e}")
            results.append((demo_name, False))
        
        # Small delay between demos
        time.sleep(1)
    
    # Display summary
    print_header("Demo Summary")
    
    successful_demos = [name for name, success in results if success]
    failed_demos = [name for name, success in results if not success]
    
    print(f"✅ Successful Demos ({len(successful_demos)}):")
    for demo in successful_demos:
        print(f"   • {demo}")
    
    if failed_demos:
        print(f"\n❌ Failed Demos ({len(failed_demos)}):")
        for demo in failed_demos:
            print(f"   • {demo}")
    
    print(f"\n📊 Overall Success Rate: {len(successful_demos)}/{len(results)} ({len(successful_demos)/len(results)*100:.1f}%)")
    
    if len(successful_demos) == len(results):
        print("\n🎉 All demos completed successfully!")
        print("🌟 The Living Codex Platform testing system is ready to use!")
    else:
        print(f"\n🔧 {len(failed_demos)} demo(s) need attention")
        print("Please check the output above for specific issues")
    
    print("\n📚 Next Steps:")
    print("   1. Review the testing system documentation")
    print("   2. Set up git pre-commit hooks")
    print("   3. Run the regression test suite")
    print("   4. Integrate testing into your development workflow")
    print("   5. Customize testing configuration as needed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Demo crashed: {e}")
        sys.exit(1)
