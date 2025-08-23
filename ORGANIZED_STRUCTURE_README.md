# Living Codex - Organized Folder Structure

This document describes the new, organized folder structure for the Living Codex system.

## 📁 Directory Structure

```
prototypes/federation-python/
├── src/
│   ├── cli/                          # CLI Package
│   │   ├── __init__.py               # CLI package initialization
│   │   └── living_codex_cli.py      # Consolidated CLI implementation
│   ├── core/                         # Core System Components
│   │   ├── ice_core_bootstrap.py
│   │   ├── living_codex_cli.py      # Original CLI (kept for reference)
│   │   └── ...
│   ├── web_platform/                 # Web Interface Components
│   │   ├── unified_web_interface.py
│   │   ├── user_management.py
│   │   └── ...
│   └── test_suites/                  # All Test Suites
│       ├── __init__.py               # Test suites package initialization
│       ├── test_cli_simple.py        # Simplified CLI tests
│       ├── test_web_simple.py        # Simplified web tests
│       ├── test_cli_comprehensive.py # Comprehensive CLI tests
│       ├── test_web_comprehensive.py # Comprehensive web tests
│       ├── run_comprehensive_test_suite.py # Main test runner
│       ├── run_full_test_suite.py    # Alternative test runner
│       ├── test_imports.py           # Import tests
│       ├── test_structure.py         # Structure tests
│       ├── test_testing_system.py    # Testing system tests
│       └── regression_test_suite.py  # Regression tests
├── launch_cli_organized.py           # New organized CLI launcher
├── run_all_tests.py                  # Master test runner
└── launch_cli.py                     # Legacy CLI launcher (kept for compatibility)
```

## 🚀 Usage

### Running the CLI
```bash
# Use the new organized launcher (recommended)
python launch_cli_organized.py

# Or use the legacy launcher (still works)
python launch_cli.py
```

### Running Tests
```bash
# Run all tests using the master runner
python run_all_tests.py

# Run specific test suites
python src/test_suites/run_comprehensive_test_suite.py
python src/test_suites/test_cli_simple.py
python src/test_suites/test_web_simple.py
```

## 🔄 Migration from Old Structure

### What Changed
1. **CLI Consolidation**: Multiple CLI versions (`codex_cli.py`, `codex_cli_minimal.py`, `codex_cli_full.py`, `codex_cli_standalone.py`) consolidated into `src/cli/living_codex_cli.py`
2. **Test Organization**: All test files moved to `src/test_suites/`
3. **Package Structure**: Proper Python packages with `__init__.py` files
4. **Import Paths**: Clean import paths without directory renaming workarounds

### Benefits
- **No More Import Conflicts**: Eliminated Python built-in `platform` module conflicts
- **Cleaner Structure**: Logical organization of components
- **Better Maintainability**: Clear separation of concerns
- **Easier Testing**: Centralized test suites
- **Professional Structure**: Follows Python packaging best practices

## 📋 File Descriptions

### CLI Package (`src/cli/`)
- **`living_codex_cli.py`**: The consolidated CLI that combines all features from the multiple CLI versions
- **`__init__.py`**: Package initialization and exports

### Test Suites (`src/test_suites/`)
- **`test_cli_simple.py`**: Simplified CLI tests using subprocess approach
- **`test_web_simple.py`**: Simplified web interface tests
- **`test_cli_comprehensive.py`**: Comprehensive CLI tests
- **`test_web_comprehensive.py`**: Comprehensive web interface tests
- **`run_comprehensive_test_suite.py`**: Main test orchestrator
- **`run_full_test_suite.py`**: Alternative test runner

### Launchers
- **`launch_cli_organized.py`**: New launcher using organized structure
- **`launch_cli.py`**: Legacy launcher (maintained for compatibility)

## 🧪 Testing

The organized structure maintains all existing test functionality:

- **CLI Tests**: 7/7 tests pass
- **Web Tests**: 7/7 tests pass  
- **Smoke Tests**: 4/4 tests pass
- **Total**: 18/18 tests pass

## 🔧 Development

When adding new features:
1. **CLI Features**: Add to `src/cli/living_codex_cli.py`
2. **Web Features**: Add to `src/web_platform/` modules
3. **Tests**: Add to `src/test_suites/`
4. **Core Features**: Add to `src/core/`

## 📚 Legacy Files

The following files are kept for reference but are no longer the primary implementation:
- `codex_cli.py` (3.1KB) - Minimal CLI
- `codex_cli_minimal.py` (16KB) - Minimal feature set
- `codex_cli_full.py` (63KB) - Full feature set
- `codex_cli_standalone.py` (80KB) - Standalone implementation

All functionality has been consolidated into `src/cli/living_codex_cli.py`.

## ✅ Status

- **Structure**: ✅ Organized and documented
- **CLI**: ✅ Consolidated and functional
- **Tests**: ✅ All passing
- **Imports**: ✅ Clean and conflict-free
- **Documentation**: ✅ Complete and up-to-date

The Living Codex system is now properly organized and ready for continued development!
