"""
Test Runner Framework
Core testing execution engine for the Living Codex system
"""

import asyncio
import time
import sys
from typing import List, Dict, Any, Callable, Optional, Union
from dataclasses import dataclass
from enum import Enum

class TestStatus(Enum):
    """Test execution status"""
    PENDING = "pending"
    RUNNING = "running"
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ERROR = "error"

@dataclass
class TestResult:
    """Result of a test execution"""
    name: str
    status: TestStatus
    duration: float
    message: str = ""
    error: Optional[Exception] = None
    metadata: Optional[Dict[str, Any]] = None

class TestRunner:
    """Main test execution engine"""
    
    def __init__(self):
        self.test_results: Dict[str, TestResult] = {}
        self.start_time = time.time()
        self.current_test: Optional[str] = None
        
    def add_test(self, name: str, test_func: Callable, 
                 async_func: bool = False, **kwargs) -> None:
        """Add a test to the test suite"""
        if not hasattr(self, '_tests'):
            self._tests = {}
        
        self._tests[name] = {
            'func': test_func,
            'async_func': async_func,
            'kwargs': kwargs
        }
    
    async def run_test(self, name: str) -> TestResult:
        """Run a single test"""
        if not hasattr(self, '_tests') or name not in self._tests:
            return TestResult(
                name=name,
                status=TestStatus.ERROR,
                duration=0.0,
                message=f"Test '{name}' not found",
                error=ValueError(f"Test '{name}' not found")
            )
        
        test_info = self._tests[name]
        test_func = test_info['func']
        async_func = test_info['async_func']
        kwargs = test_info['kwargs']
        
        self.current_test = name
        start_time = time.time()
        
        try:
            if async_func:
                result = await test_func(**kwargs)
            else:
                result = test_func(**kwargs)
            
            duration = time.time() - start_time
            
            if result:
                status = TestStatus.PASSED
                message = "Test passed successfully"
                error = None
            else:
                status = TestStatus.FAILED
                message = "Test failed"
                error = None
                
        except Exception as e:
            duration = time.time() - start_time
            status = TestStatus.ERROR
            message = f"Test error: {str(e)}"
            result = None
            error = e
        
        test_result = TestResult(
            name=name,
            status=status,
            duration=duration,
            message=message,
            error=error,
            metadata={'kwargs': kwargs}
        )
        
        self.test_results[name] = test_result
        return test_result
    
    async def run_all_tests(self) -> Dict[str, TestResult]:
        """Run all registered tests"""
        if not hasattr(self, '_tests'):
            return {}
        
        print(f"🚀 Running {len(self._tests)} tests...")
        
        for test_name in self._tests.keys():
            await self.run_test(test_name)
        
        return self.test_results
    
    def get_summary(self) -> Dict[str, Any]:
        """Get test execution summary"""
        if not self.test_results:
            return {}
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results.values() 
                          if r.status == TestStatus.PASSED)
        failed_tests = sum(1 for r in self.test_results.values() 
                          if r.status == TestStatus.FAILED)
        error_tests = sum(1 for r in self.test_results.values() 
                         if r.status == TestStatus.ERROR)
        
        total_duration = time.time() - self.start_time
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        return {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'error_tests': error_tests,
            'success_rate': success_rate,
            'total_duration': total_duration,
            'start_time': self.start_time
        }
    
    def print_summary(self) -> None:
        """Print test execution summary"""
        summary = self.get_summary()
        
        if not summary:
            print("No tests executed")
            return
        
        print("\n" + "=" * 60)
        print("  Test Execution Summary")
        print("=" * 60)
        
        print(f"📊 Test Results:")
        print(f"  Total Tests: {summary['total_tests']}")
        print(f"  Passed: {summary['passed_tests']} ✅")
        print(f"  Failed: {summary['failed_tests']} ❌")
        print(f"  Errors: {summary['error_tests']} ⚠️")
        print(f"  Success Rate: {summary['success_rate']:.1f}%")
        
        if summary['failed_tests'] > 0 or summary['error_tests'] > 0:
            print(f"\n❌ Failed/Error Tests:")
            for name, result in self.test_results.items():
                if result.status in [TestStatus.FAILED, TestStatus.ERROR]:
                    print(f"  • {name}: {result.message}")
        
        print(f"\n⏱️  Total execution time: {summary['total_duration']:.2f} seconds")
        
        if summary['success_rate'] == 100.0:
            print(f"\n🎉 All tests passed! Your system is fully operational!")
        else:
            print(f"\n⚠️  Some tests failed. Check the results above for details.")
    
    def exit_with_code(self) -> None:
        """Exit with appropriate exit code based on test results"""
        summary = self.get_summary()
        
        if summary.get('success_rate', 0) == 100.0:
            sys.exit(0)
        else:
            sys.exit(1)
