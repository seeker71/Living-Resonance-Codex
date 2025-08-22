#!/usr/bin/env python3
"""
Living Codex Platform - Test Runner
Comprehensive test execution with multiple modes and reporting
"""

import sys
import os
import subprocess
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import concurrent.futures
import signal
import tempfile
import shutil

class TestRunner:
    """Comprehensive test runner for the Living Codex Platform"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.tests_dir = project_root / "tests"
        self.scripts_dir = project_root / "scripts"
        self.reports_dir = project_root / "test_reports"
        self.reports_dir.mkdir(exist_ok=True)
        
        # Test configuration
        self.config = {
            'timeout': 300,  # 5 minutes per test
            'parallel': False,
            'max_workers': 4,
            'retry_failed': True,
            'max_retries': 2,
            'generate_reports': True,
            'stop_on_failure': False,
            'verbose': False
        }
        
        # Test results storage
        self.test_results: List[Dict[str, Any]] = []
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        
        # Signal handling for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        self._shutdown_requested = False
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print(f"\n⚠️  Received signal {signum}, shutting down gracefully...")
        self._shutdown_requested = True
    
    def discover_tests(self, test_pattern: str = None) -> List[str]:
        """Discover available tests based on pattern"""
        print("🔍 Discovering tests...")
        
        tests = []
        
        if test_pattern:
            # Use specific pattern
            patterns = [test_pattern]
        else:
            # Default patterns
            patterns = [
                "test_*.py",
                "*_test.py",
                "regression_test_suite.py",
                "demo_*.py",
                "*_demo.py"
            ]
        
        for pattern in patterns:
            if pattern.startswith("tests/"):
                # Look in tests directory
                for test_file in self.tests_dir.glob(pattern[6:]):
                    if test_file.is_file():
                        tests.append(str(test_file.relative_to(self.project_root)))
            else:
                # Look in project root
                for test_file in self.project_root.rglob(pattern):
                    if test_file.is_file() and test_file.parent.name != "scripts":
                        tests.append(str(test_file.relative_to(self.project_root)))
        
        # Remove duplicates while preserving order
        seen = set()
        unique_tests = []
        for test in tests:
            if test not in seen:
                seen.add(test)
                unique_tests.append(test)
        
        print(f"✅ Discovered {len(unique_tests)} tests:")
        for test in unique_tests:
            print(f"   📋 {test}")
        
        return unique_tests
    
    def run_single_test(self, test_path: str, retry_count: int = 0) -> Dict[str, Any]:
        """Run a single test and return detailed results"""
        if self._shutdown_requested:
            return {
                'test_path': test_path,
                'status': 'SKIPPED',
                'error': 'Shutdown requested',
                'duration': 0,
                'retry_count': retry_count
            }
        
        print(f"🧪 Running test: {test_path} (attempt {retry_count + 1})")
        
        start_time = time.time()
        test_file = self.project_root / test_path
        
        try:
            # Determine test execution strategy
            if test_path.startswith('tests/') and test_path.endswith('.py'):
                # Standard test file
                cmd = [sys.executable, str(test_file)]
                test_type = 'unittest'
            elif test_path in ['main.py', 'codex_cli.py']:
                # Main entry point - test basic functionality
                cmd = [sys.executable, str(test_file), '--test-mode']
                test_type = 'main'
            elif test_path.endswith('_demo.py'):
                # Demo file - test import and basic execution
                cmd = [sys.executable, '-c', f'import {test_path.replace("/", ".").replace(".py", "")}']
                test_type = 'demo'
            else:
                # Generic Python file
                cmd = [sys.executable, str(test_file)]
                test_type = 'generic'
            
            # Run the test
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.config['timeout'],
                cwd=self.project_root
            )
            
            duration = time.time() - start_time
            
            # Determine test status
            if result.returncode == 0:
                status = 'PASSED'
                error = None
            else:
                status = 'FAILED'
                error = result.stderr if result.stderr else "Unknown error"
            
            # Create test result
            test_result = {
                'test_path': test_path,
                'test_type': test_type,
                'status': status,
                'duration': duration,
                'timestamp': datetime.now().isoformat(),
                'return_code': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'command': ' '.join(cmd),
                'retry_count': retry_count,
                'error': error
            }
            
            # Display immediate result
            status_icon = "✅" if status == "PASSED" else "❌" if status == "FAILED" else "💥"
            print(f"   {status_icon} {test_path}: {status} ({duration:.2f}s)")
            
            if status != "PASSED" and self.config['verbose']:
                if error:
                    print(f"      Error: {error}")
                if result.stdout and len(result.stdout.strip()) > 0:
                    print(f"      Output: {result.stdout[:200]}...")
            
            return test_result
            
        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            return {
                'test_path': test_path,
                'test_type': test_type,
                'status': 'TIMEOUT',
                'duration': duration,
                'timestamp': datetime.now().isoformat(),
                'error': f"Test timed out after {self.config['timeout']} seconds",
                'retry_count': retry_count
            }
            
        except Exception as e:
            duration = time.time() - start_time
            return {
                'test_path': test_path,
                'test_type': 'unknown',
                'status': 'ERROR',
                'duration': duration,
                'timestamp': datetime.now().isoformat(),
                'error': str(e),
                'retry_count': retry_count
            }
    
    def run_tests_sequential(self, tests: List[str]) -> List[Dict[str, Any]]:
        """Run tests sequentially"""
        print("🔄 Running tests sequentially...")
        
        results = []
        for test_path in tests:
            if self._shutdown_requested:
                break
                
            result = self.run_single_test(test_path)
            results.append(result)
            
            # Stop on failure if configured
            if self.config['stop_on_failure'] and result['status'] not in ['PASSED', 'SKIPPED']:
                print(f"🚨 Stopping on test failure: {test_path}")
                break
        
        return results
    
    def run_tests_parallel(self, tests: List[str]) -> List[Dict[str, Any]]:
        """Run tests in parallel"""
        print(f"🔄 Running tests in parallel (max {self.config['max_workers']} workers)...")
        
        results = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.config['max_workers']) as executor:
            # Submit all tests
            future_to_test = {
                executor.submit(self.run_single_test, test_path): test_path 
                for test_path in tests
            }
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_test):
                if self._shutdown_requested:
                    # Cancel remaining futures
                    for f in future_to_test:
                        f.cancel()
                    break
                
                test_path = future_to_test[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    results.append({
                        'test_path': test_path,
                        'status': 'ERROR',
                        'error': f"Execution error: {e}",
                        'duration': 0,
                        'timestamp': datetime.now().isoformat()
                    })
        
        # Sort results by original test order
        test_order = {test: i for i, test in enumerate(tests)}
        results.sort(key=lambda r: test_order.get(r['test_path'], 999))
        
        return results
    
    def retry_failed_tests(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Retry failed tests if configured"""
        if not self.config['retry_failed'] or self.config['max_retries'] <= 0:
            return results
        
        failed_tests = [r for r in results if r['status'] not in ['PASSED', 'SKIPPED']]
        
        if not failed_tests:
            return results
        
        print(f"\n🔄 Retrying {len(failed_tests)} failed tests...")
        
        for retry_count in range(1, self.config['max_retries'] + 1):
            if self._shutdown_requested:
                break
                
            print(f"   📋 Retry attempt {retry_count}/{self.config['max_retries']}")
            
            retry_results = []
            for failed_test in failed_tests:
                if self._shutdown_requested:
                    break
                    
                retry_result = self.run_single_test(failed_test['test_path'], retry_count)
                retry_results.append(retry_result)
                
                # Update original result if retry succeeded
                if retry_result['status'] == 'PASSED':
                    failed_test.update(retry_result)
                    failed_test['retry_success'] = True
                    print(f"      ✅ {failed_test['test_path']} passed on retry!")
            
            # Check if all tests passed
            still_failing = [r for r in retry_results if r['status'] not in ['PASSED', 'SKIPPED']]
            if not still_failing:
                print("      🎉 All tests passed on retry!")
                break
        
        return results
    
    def generate_test_report(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive test report"""
        if not results:
            return {}
        
        # Calculate statistics
        total_tests = len(results)
        passed_tests = len([r for r in results if r['status'] == 'PASSED'])
        failed_tests = len([r for r in results if r['status'] == 'FAILED'])
        error_tests = len([r for r in results if r['status'] == 'ERROR'])
        timeout_tests = len([r for r in results if r['status'] == 'TIMEOUT'])
        skipped_tests = len([r for r in results if r['status'] == 'SKIPPED'])
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        # Calculate timing statistics
        durations = [r['duration'] for r in results if 'duration' in r and r['duration'] > 0]
        avg_duration = sum(durations) / len(durations) if durations else 0
        max_duration = max(durations) if durations else 0
        min_duration = min(durations) if durations else 0
        
        # Group by test type
        test_types = {}
        for result in results:
            test_type = result.get('test_type', 'unknown')
            if test_type not in test_types:
                test_types[test_type] = []
            test_types[test_type].append(result)
        
        # Generate report
        report = {
            'summary': {
                'total_tests': total_tests,
                'passed_tests': passed_tests,
                'failed_tests': failed_tests,
                'error_tests': error_tests,
                'timeout_tests': timeout_tests,
                'skipped_tests': skipped_tests,
                'success_rate': success_rate,
                'total_duration': sum(durations),
                'average_duration': avg_duration,
                'max_duration': max_duration,
                'min_duration': min_duration
            },
            'test_types': {
                test_type: {
                    'count': len(type_results),
                    'passed': len([r for r in type_results if r['status'] == 'PASSED']),
                    'failed': len([r for r in type_results if r['status'] != 'PASSED'])
                }
                for test_type, type_results in test_types.items()
            },
            'results': results,
            'timestamp': datetime.now().isoformat(),
            'configuration': self.config
        }
        
        return report
    
    def save_test_report(self, report: Dict[str, Any], filename: str = None) -> Path:
        """Save test report to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"test_report_{timestamp}.json"
        
        report_file = self.reports_dir / filename
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report_file
    
    def display_summary(self, report: Dict[str, Any]):
        """Display test summary"""
        if not report or 'summary' not in report:
            return
        
        summary = report['summary']
        
        print("\n" + "=" * 60)
        print("📊 TEST EXECUTION SUMMARY")
        print("=" * 60)
        
        print(f"📋 Test Results:")
        print(f"   Total Tests: {summary['total_tests']}")
        print(f"   ✅ Passed: {summary['passed_tests']}")
        print(f"   ❌ Failed: {summary['failed_tests']}")
        print(f"   💥 Errors: {summary['error_tests']}")
        print(f"   ⏰ Timeouts: {summary['timeout_tests']}")
        print(f"   ⏭️  Skipped: {summary['skipped_tests']}")
        print(f"   📊 Success Rate: {summary['success_rate']:.1f}%")
        
        print(f"\n⏱️  Timing:")
        print(f"   Total Duration: {summary['total_duration']:.2f}s")
        print(f"   Average Duration: {summary['average_duration']:.2f}s")
        print(f"   Fastest Test: {summary['min_duration']:.2f}s")
        print(f"   Slowest Test: {summary['max_duration']:.2f}s")
        
        if 'test_types' in report:
            print(f"\n🔍 Test Types:")
            for test_type, type_stats in report['test_types'].items():
                success_rate = (type_stats['passed'] / type_stats['count'] * 100) if type_stats['count'] > 0 else 0
                print(f"   {test_type}: {type_stats['passed']}/{type_stats['count']} ({success_rate:.1f}%)")
        
        # Show failed tests
        failed_tests = [r for r in report['results'] if r['status'] not in ['PASSED', 'SKIPPED']]
        if failed_tests:
            print(f"\n🚨 Failed Tests:")
            for test in failed_tests:
                print(f"   ❌ {test['test_path']}: {test.get('error', 'Unknown error')}")
        
        # Final status
        if summary['success_rate'] == 100:
            print(f"\n🎉 ALL TESTS PASSED!")
            print("✅ System integrity verified")
            print("✅ Ready for deployment")
        else:
            print(f"\n🚨 SOME TESTS FAILED!")
            print(f"❌ Success rate: {summary['success_rate']:.1f}%")
            print("🔧 Please investigate and fix failing tests")
    
    def run_test_suite(self, test_pattern: str = None, mode: str = 'auto') -> bool:
        """Run the complete test suite"""
        print("🚀 Living Codex Platform - Test Runner")
        print("=" * 60)
        
        self.start_time = datetime.now()
        
        try:
            # Discover tests
            tests = self.discover_tests(test_pattern)
            
            if not tests:
                print("❌ No tests found!")
                return False
            
            # Determine execution mode
            if mode == 'auto':
                mode = 'parallel' if self.config['parallel'] else 'sequential'
            
            print(f"\n🔧 Configuration:")
            print(f"   Execution Mode: {mode}")
            print(f"   Timeout: {self.config['timeout']}s")
            print(f"   Retry Failed: {self.config['retry_failed']}")
            print(f"   Max Retries: {self.config['max_retries']}")
            print(f"   Stop on Failure: {self.config['stop_on_failure']}")
            
            # Run tests
            if mode == 'parallel':
                results = self.run_tests_parallel(tests)
            else:
                results = self.run_tests_sequential(tests)
            
            # Retry failed tests if configured
            if self.config['retry_failed']:
                results = self.retry_failed_tests(results)
            
            # Generate report
            if self.config['generate_reports']:
                report = self.generate_test_report(results)
                self.display_summary(report)
                
                # Save report only if requested
                if len(sys.argv) > 1 and ('--save-report' in sys.argv or '--verbose' in sys.argv):
                    report_file = self.save_test_report(report)
                    print(f"\n📊 Test report saved to: {report_file}")
                else:
                    print(f"\n📊 Test report generation skipped (use --save-report to enable)")
                
                # Return success status
                summary = report['summary']
                return summary['success_rate'] == 100
            else:
                # Simple summary without detailed reporting
                passed = len([r for r in results if r['status'] == 'PASSED'])
                total = len(results)
                success_rate = (passed / total * 100) if total > 0 else 0
                
                print(f"\n📊 Simple Summary: {passed}/{total} tests passed ({success_rate:.1f}%)")
                return success_rate == 100
                
        except Exception as e:
            print(f"💥 Test suite execution failed: {e}")
            return False
        finally:
            self.end_time = datetime.now()
            if self.start_time and self.end_time:
                total_duration = (self.end_time - self.start_time).total_seconds()
                print(f"\n⏱️  Total execution time: {total_duration:.2f}s")

def main():
    """Main test runner execution"""
    parser = argparse.ArgumentParser(description="Living Codex Platform Test Runner")
    parser.add_argument('--pattern', '-p', help='Test pattern to match (e.g., "test_*.py")')
    parser.add_argument('--mode', '-m', choices=['auto', 'sequential', 'parallel'], 
                       default='auto', help='Execution mode')
    parser.add_argument('--timeout', '-t', type=int, default=300, 
                       help='Test timeout in seconds')
    parser.add_argument('--parallel', '-P', action='store_true', 
                       help='Enable parallel execution')
    parser.add_argument('--max-workers', type=int, default=4, 
                       help='Maximum parallel workers')
    parser.add_argument('--no-retry', action='store_true', 
                       help='Disable retry of failed tests')
    parser.add_argument('--max-retries', type=int, default=2, 
                       help='Maximum retry attempts')
    parser.add_argument('--stop-on-failure', action='store_true', 
                       help='Stop execution on first test failure')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Verbose output')
    parser.add_argument('--no-reports', action='store_true', 
                       help='Disable report generation')
    
    args = parser.parse_args()
    
    # Get project root
    project_root = Path(__file__).parent.parent
    
    if not project_root.exists():
        print("❌ Error: Project root not found!")
        sys.exit(1)
    
    # Initialize test runner
    runner = TestRunner(project_root)
    
    # Update configuration from command line arguments
    runner.config.update({
        'timeout': args.timeout,
        'parallel': args.parallel,
        'max_workers': args.max_workers,
        'retry_failed': not args.no_retry,
        'max_retries': args.max_retries,
        'stop_on_failure': args.stop_on_failure,
        'verbose': args.verbose,
        'generate_reports': not args.no_reports
    })
    
    try:
        # Run test suite
        success = runner.run_test_suite(args.pattern, args.mode)
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n⚠️  Test execution interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Test runner crashed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
