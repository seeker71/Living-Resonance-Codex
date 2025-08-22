"""
Test Reporter
Formatted test output and reporting for the Living Codex system
"""

from typing import Dict, Any, Optional
from .test_runner import TestResult, TestStatus

class TestReporter:
    """Formatted test output and reporting"""
    
    def __init__(self):
        self.section_count = 0
        
    def print_header(self, title: str, char: str = "=", width: int = 60) -> None:
        """Print a formatted header"""
        print(f"\n{char * width}")
        print(f"  {title}")
        print(f"{char * width}")
    
    def print_section(self, title: str, char: str = "-", width: int = 40) -> None:
        """Print a formatted section header"""
        self.section_count += 1
        print(f"\n{char * width}")
        print(f"  {self.section_count}. {title}")
        print(f"{char * width}")
    
    def print_test_result(self, test_name: str, result: TestResult) -> None:
        """Print a formatted test result"""
        status_icons = {
            TestStatus.PASSED: "✅ PASS",
            TestStatus.FAILED: "❌ FAIL", 
            TestStatus.ERROR: "⚠️  ERROR",
            TestStatus.SKIPPED: "⏭️  SKIP",
            TestStatus.PENDING: "⏳ PENDING",
            TestStatus.RUNNING: "🔄 RUNNING"
        }
        
        status_icon = status_icons.get(result.status, "❓ UNKNOWN")
        print(f"{status_icon} {test_name}")
        
        if result.message:
            print(f"     {result.message}")
        
        if result.duration > 0:
            print(f"     Duration: {result.duration:.2f}s")
        
        if result.error:
            print(f"     Error: {str(result.error)}")
    
    def print_test_section_header(self, section_name: str) -> None:
        """Print a test section header"""
        print(f"\n{'=' * 60}")
        print(f"  {section_name}")
        print(f"{'=' * 60}")
    
    def print_test_section(self, section_name: str) -> None:
        """Print a test section"""
        print(f"\n{'-' * 40}")
        print(f"  {section_name}")
        print(f"{'-' * 40}")
    
    def print_progress(self, current: int, total: int, test_name: str) -> None:
        """Print test progress"""
        percentage = (current / total * 100) if total > 0 else 0
        print(f"🔄 [{current}/{total}] ({percentage:.1f}%) Running: {test_name}")
    
    def print_summary_header(self) -> None:
        """Print test summary header"""
        print(f"\n{'=' * 60}")
        print(f"  Test Execution Summary")
        print(f"{'=' * 60}")
    
    def print_detailed_results(self, results: Dict[str, TestResult]) -> None:
        """Print detailed test results"""
        if not results:
            print("No test results to display")
            return
        
        print(f"\n📋 Detailed Test Results:")
        
        for test_name, result in results.items():
            self.print_test_result(test_name, result)
    
    def print_performance_metrics(self, summary: Dict[str, Any]) -> None:
        """Print performance metrics"""
        if not summary:
            return
        
        print(f"\n📊 Performance Metrics:")
        print(f"  Total Tests: {summary.get('total_tests', 0)}")
        print(f"  Passed: {summary.get('passed_tests', 0)} ✅")
        print(f"  Failed: {summary.get('failed_tests', 0)} ❌")
        print(f"  Errors: {summary.get('error_tests', 0)} ⚠️")
        print(f"  Success Rate: {summary.get('success_rate', 0):.1f}%")
        print(f"  Total Duration: {summary.get('total_duration', 0):.2f}s")
        
        if summary.get('total_tests', 0) > 0:
            avg_duration = summary.get('total_duration', 0) / summary.get('total_tests', 1)
            print(f"  Average Duration: {avg_duration:.2f}s per test")
    
    def print_failure_details(self, results: Dict[str, TestResult]) -> None:
        """Print detailed failure information"""
        failed_tests = {name: result for name, result in results.items() 
                       if result.status in [TestStatus.FAILED, TestStatus.ERROR]}
        
        if not failed_tests:
            return
        
        print(f"\n❌ Failure Details:")
        for test_name, result in failed_tests.items():
            print(f"\n  🔍 {test_name}:")
            print(f"     Status: {result.status.value}")
            print(f"     Message: {result.message}")
            print(f"     Duration: {result.duration:.2f}s")
            
            if result.error:
                print(f"     Error Type: {type(result.error).__name__}")
                print(f"     Error Details: {str(result.error)}")
            
            if result.metadata:
                print(f"     Metadata: {result.metadata}")
    
    def print_success_message(self, summary: Dict[str, Any]) -> None:
        """Print success or failure message"""
        if not summary:
            return
        
        success_rate = summary.get('success_rate', 0)
        
        if success_rate == 100.0:
            print(f"\n🎉 All tests passed! Your Living Codex is fully operational!")
        elif success_rate >= 80.0:
            print(f"\n✅ Most tests passed! Your system is mostly operational.")
        elif success_rate >= 50.0:
            print(f"\n⚠️  Some tests passed, but there are issues to address.")
        else:
            print(f"\n❌ Many tests failed. Please check your configuration and try again.")
        
        print(f"\n💡 Next Steps:")
        if success_rate == 100.0:
            print("   • Your system is ready to use!")
            print("   • Run the integrated demo to see all features working")
            print("   • Start building your knowledge base")
        else:
            print("   • Check the failure details above")
            print("   • Verify your configuration settings")
            print("   • Check the troubleshooting guide")
            print("   • Run individual component tests to isolate issues")
