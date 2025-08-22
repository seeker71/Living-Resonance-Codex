#!/usr/bin/env python3
"""
Living Codex Platform - Pre-Commit Hook
Automatically runs regression tests before allowing commits
"""

import sys
import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

def run_regression_tests():
    """Run the regression test suite"""
    print("🔍 Pre-commit hook: Running regression tests...")
    
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    test_script = project_root / "tests" / "regression_test_suite.py"
    
    if not test_script.exists():
        print("❌ Error: Regression test suite not found!")
        print(f"   Expected location: {test_script}")
        return False
    
    try:
        # Run the regression test suite
        result = subprocess.run([
            sys.executable, str(test_script)
        ], capture_output=True, text=True, cwd=project_root)
        
        if result.returncode == 0:
            print("✅ All regression tests passed!")
            return True
        else:
            print("❌ Regression tests failed!")
            print("\n📋 Test Output:")
            print(result.stdout)
            if result.stderr:
                print("\n🚨 Test Errors:")
                print(result.stderr)
            return False
            
    except Exception as e:
        print(f"💥 Error running regression tests: {e}")
        return False

def run_code_quality_checks():
    """Run code quality checks"""
    print("🔍 Pre-commit hook: Running code quality checks...")
    
    project_root = Path(__file__).parent.parent
    
    # Check for basic Python syntax errors
    try:
        python_files = list(project_root.rglob("*.py"))
        syntax_errors = []
        
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    compile(f.read(), str(py_file), 'exec')
            except SyntaxError as e:
                syntax_errors.append(f"{py_file}: {e}")
        
        if syntax_errors:
            print("❌ Python syntax errors found:")
            for error in syntax_errors:
                print(f"   {error}")
            return False
        else:
            print("✅ No Python syntax errors found")
            return True
            
    except Exception as e:
        print(f"💥 Error during syntax check: {e}")
        return False

def check_file_sizes():
    """Check for unusually large files that shouldn't be committed"""
    print("🔍 Pre-commit hook: Checking file sizes...")
    
    project_root = Path(__file__).parent.parent
    max_file_size = 10 * 1024 * 1024  # 10MB
    
    large_files = []
    
    for file_path in project_root.rglob("*"):
        if file_path.is_file() and not file_path.name.startswith('.'):
            try:
                file_size = file_path.stat().st_size
                if file_size > max_file_size:
                    large_files.append((file_path, file_size))
            except (OSError, PermissionError):
                continue
    
    if large_files:
        print("⚠️  Large files detected (consider .gitignore):")
        for file_path, size in large_files:
            size_mb = size / (1024 * 1024)
            print(f"   {file_path} ({size_mb:.1f} MB)")
    
    print("✅ File size check completed")
    return True

def check_imports():
    """Check that all imports can be resolved"""
    print("🔍 Pre-commit hook: Checking import resolution...")
    
    project_root = Path(__file__).parent.parent
    src_dir = project_root / "src"
    
    if not src_dir.exists():
        print("⚠️  No src directory found, skipping import check")
        return True
    
    # Find all Python files in src
    python_files = list(src_dir.rglob("*.py"))
    import_errors = []
    
    for py_file in python_files:
        try:
            # Try to import the module
            module_name = str(py_file.relative_to(project_root)).replace('/', '.').replace('.py', '')
            if module_name.startswith('src.'):
                module_name = module_name[4:]  # Remove 'src.' prefix
            
            # Add src to path temporarily
            sys.path.insert(0, str(project_root / "src"))
            try:
                __import__(module_name)
            finally:
                sys.path.pop(0)
                
        except ImportError as e:
            import_errors.append(f"{py_file}: {e}")
        except Exception as e:
            import_errors.append(f"{py_file}: Unexpected error - {e}")
    
    if import_errors:
        print("❌ Import errors found:")
        for error in import_errors:
            print(f"   {error}")
        return False
    else:
        print("✅ All imports resolved successfully")
        return True

def create_git_hook():
    """Create the git pre-commit hook"""
    print("🔧 Setting up git pre-commit hook...")
    
    git_hooks_dir = Path(__file__).parent.parent / ".git" / "hooks"
    pre_commit_hook = git_hooks_dir / "pre-commit"
    
    if not git_hooks_dir.exists():
        print("❌ Error: .git/hooks directory not found!")
        print("   Make sure you're in a git repository")
        return False
    
    # Create the pre-commit hook script
    hook_content = f"""#!/bin/sh
# Living Codex Platform - Pre-commit Hook
# This hook runs automatically before each commit

echo "🔍 Running pre-commit checks..."

# Run the Python pre-commit hook
python "{Path(__file__).absolute()}"

if [ $? -ne 0 ]; then
    echo "❌ Pre-commit checks failed. Commit aborted."
    exit 1
fi

echo "✅ Pre-commit checks passed. Proceeding with commit."
exit 0
"""
    
    try:
        with open(pre_commit_hook, 'w') as f:
            f.write(hook_content)
        
        # Make the hook executable
        os.chmod(pre_commit_hook, 0o755)
        
        print("✅ Git pre-commit hook created successfully!")
        print(f"   Location: {pre_commit_hook}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating git hook: {e}")
        return False

def main():
    """Main pre-commit hook execution"""
    print("🌟 Living Codex Platform - Pre-Commit Hook")
    print("=" * 50)
    
    # Check if this is being run as a git hook or manually
    is_git_hook = len(sys.argv) > 1 and sys.argv[1] == "--git-hook"
    
    if not is_git_hook:
        print("🔧 Manual pre-commit check mode")
        print("   Use --git-hook to run as git pre-commit hook")
        print("   Use --setup to install git pre-commit hook")
        
        if len(sys.argv) > 1 and sys.argv[1] == "--setup":
            return create_git_hook()
    
    # Run all pre-commit checks
    checks = [
        ("Code Quality", run_code_quality_checks),
        ("File Sizes", check_file_sizes),
        ("Import Resolution", check_imports),
        ("Regression Tests", run_regression_tests)
    ]
    
    all_passed = True
    check_results = []
    
    for check_name, check_function in checks:
        print(f"\n{'='*20} {check_name} {'='*20}")
        try:
            result = check_function()
            check_results.append({
                'check': check_name,
                'status': 'PASSED' if result else 'FAILED',
                'timestamp': datetime.now().isoformat()
            })
            
            if not result:
                all_passed = False
                
        except Exception as e:
            print(f"💥 Error during {check_name}: {e}")
            check_results.append({
                'check': check_name,
                'status': 'ERROR',
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            })
            all_passed = False
    
    # Display summary
    print("\n" + "=" * 50)
    print("📊 PRE-COMMIT CHECK SUMMARY")
    print("=" * 50)
    
    for result in check_results:
        status_icon = "✅" if result['status'] == 'PASSED' else "❌" if result['status'] == 'FAILED' else "💥"
        print(f"{status_icon} {result['check']}: {result['status']}")
        if 'error' in result:
            print(f"     Error: {result['error']}")
    
    # Save check report
    report = {
        'summary': {
            'total_checks': len(check_results),
            'passed': len([r for r in check_results if r['status'] == 'PASSED']),
            'failed': len([r for r in check_results if r['status'] == 'FAILED']),
            'errors': len([r for r in check_results if r['status'] == 'ERROR']),
            'success_rate': len([r for r in check_results if r['status'] == 'PASSED']) / len(check_results) * 100 if check_results else 0
        },
        'results': check_results,
        'timestamp': datetime.now().isoformat()
    }
    
    # Save report to file
    report_file = Path(__file__).parent.parent / "pre_commit_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 Check report saved to: {report_file}")
    
    # Final result
    if all_passed:
        print("\n🎉 ALL CHECKS PASSED - Safe to commit!")
        print("✅ Code quality maintained")
        print("✅ No regressions detected")
        print("✅ System integrity preserved")
        return True
    else:
        print("\n🚨 CHECKS FAILED - DO NOT COMMIT!")
        print("❌ Code quality compromised")
        print("❌ Potential regressions detected")
        print("❌ System integrity at risk")
        print("\n🔧 Please fix all failing checks before committing.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
