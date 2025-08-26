#!/usr/bin/env python3
"""
Living Codex - Master Test Runner
================================

This script runs all test suites from the organized folder structure.
It serves as the main entry point for testing the entire Living Codex system.
"""

import sys
import os
import subprocess
from pathlib import Path

def main():
    """Run all test suites"""
    print("🌟 Living Codex - Master Test Runner")
    print("=" * 50)
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    test_suites_dir = script_dir / "src" / "test_suites"
    
    if not test_suites_dir.exists():
        print(f"❌ Test suites directory not found: {test_suites_dir}")
        return 1
    
    print(f"📁 Test suites directory: {test_suites_dir}")
    print()
    
    # Run the comprehensive test suite
    print("🚀 Running Comprehensive Test Suite...")
    try:
        result = subprocess.run([
            sys.executable, 
            str(test_suites_dir / "run_comprehensive_test_suite.py")
        ], cwd=script_dir, check=True, env={**os.environ, 'PYTHONPATH': str(script_dir / 'src')})
        
        if result.returncode == 0:
            print("✅ All tests completed successfully!")
            return 0
        else:
            print("❌ Some tests failed!")
            return 1
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Test execution failed: {e}")
        return 1
    except FileNotFoundError:
        print("❌ Test suite runner not found")
        return 1

if __name__ == "__main__":
    exit(main())
