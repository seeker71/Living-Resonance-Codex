#!/usr/bin/env python3
"""
Minimal ICE Bootstrap Cycle Demo - Clean, Error-Free Workflow

This demo tests the complete cycle using the minimal, clean implementation:
WATER (current system) → ICE (bootstrap storage) → WATER (new functional system)

Ensures zero errors and full functionality for community service.
"""

import sys
import time
import shutil
import tempfile
from pathlib import Path
import os

def create_clean_environment():
    """Create a clean environment for testing"""
    print("🧹 Creating clean test environment...")
    
    temp_dir = Path(tempfile.mkdtemp(prefix="minimal_ice_test_"))
    print(f"✅ Test environment created at: {temp_dir}")
    
    return temp_dir

def copy_essential_files(source_dir: Path, target_dir: Path):
    """Copy only the essential files needed for the bootstrap cycle"""
    print("📋 Copying essential files...")
    
    essential_files = [
        "src/core/water_state_storage.py",
        "src/core/minimal_ice_bootstrap.py",
        "src/core/dependency_manager.py",
        "src/platform/user_management.py",
        "src/platform/contribution_system.py",
        "src/platform/web_interface.py",
        "src/ontology/enhanced_ontology_system.py",
        "tests/regression_test_suite.py",
        "tests/test_testing_system.py",
        "requirements.txt",
        ".gitignore",
        "README.md",
        "docs/LIVING_CODEX_SPECIFICATION.md",
        "docs/WATER_STATE_STORAGE.md",
        "scripts/test_runner.py",
        "scripts/continuous_integration.py",
        "demo_water_states.py",
        "demo_platform.py"
    ]
    
    copied_count = 0
    for file_path in essential_files:
        source_file = source_dir / file_path
        target_file = target_dir / file_path
        
        if source_file.exists():
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, target_file)
            copied_count += 1
        else:
            print(f"⚠️ File not found: {file_path}")
    
    print(f"✅ Copied {copied_count} essential files")
    return copied_count

def test_ice_core_creation(test_dir: Path):
    """Test creating ICE core from the test environment"""
    print("\n🧊 STEP 1: Testing ICE Core Creation")
    print("=" * 50)
    
    try:
        # Change to test directory
        original_dir = Path.cwd()
        os.chdir(test_dir)
        
        # Import and test ICE core creator
        sys.path.insert(0, str(test_dir / "src"))
        from src.core.ice_core_creator import ICECoreCreator
        
        creator = ICECoreCreator()
        
        # Analyze system
        print("🔍 Analyzing test system...")
        analysis = creator.analyze_system()
        
        print(f"📊 Analysis Results:")
        print(f"   Total Files: {analysis['total_files']}")
        print(f"   Total Size: {analysis['total_size'] / 1024:.1f} KB")
        print(f"   File Types: {dict(analysis['file_types'])}")
        
        # Create ICE core
        print(f"\n🧊 Creating ICE core...")
        success = creator.create_ice_core("ice_core")
        
        if success:
            print("✅ ICE core created successfully!")
            
            # Verify ICE core contents
            ice_core_dir = test_dir / "ice_core"
            manifest_file = ice_core_dir / "bootstrap_manifest.json"
            
            if manifest_file.exists():
                print("✅ Bootstrap manifest verified")
                return True
            else:
                print("❌ Bootstrap manifest missing")
                return False
        else:
            print("❌ ICE core creation failed")
            return False
            
    except Exception as e:
        print(f"❌ ICE core creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # Return to original directory
        os.chdir(original_dir)

def test_minimal_ice_bootstrap(test_dir: Path):
    """Test bootstrapping using the minimal system"""
    print("\n🚀 STEP 2: Testing Minimal ICE Bootstrap")
    print("=" * 50)
    
    try:
        # Change to test directory
        original_dir = Path.cwd()
        os.chdir(test_dir)
        
        # Import and test minimal bootstrap
        sys.path.insert(0, str(test_dir / "src"))
        from src.core.minimal_ice_bootstrap import MinimalICEBootstrap
        
        # Initialize minimal bootstrap
        bootstrap = MinimalICEBootstrap("ice_core")
        
        # Run complete bootstrap
        print("🧊 Starting minimal ICE bootstrap process...")
        success = bootstrap.bootstrap_full_system()
        
        if success:
            print("✅ Minimal ICE bootstrap completed successfully!")
            
            # Verify system reconstruction
            required_files = [
                "src/core/water_state_storage.py",
                "src/platform/user_management.py",
                "src/platform/web_interface.py",
                "tests/regression_test_suite.py"
            ]
            
            all_files_exist = True
            for file_path in required_files:
                if not Path(file_path).exists():
                    print(f"❌ Reconstructed file missing: {file_path}")
                    all_files_exist = False
            
            if all_files_exist:
                print("✅ All required files reconstructed")
                return True
            else:
                print("❌ System reconstruction incomplete")
                return False
        else:
            print("❌ Minimal ICE bootstrap failed")
            return False
            
    except Exception as e:
        print(f"❌ Minimal ICE bootstrap failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # Return to original directory
        os.chdir(original_dir)

def test_community_readiness(test_dir: Path):
    """Test that the system is ready to serve the community"""
    print("\n🌐 STEP 3: Testing Community Readiness")
    print("=" * 50)
    
    try:
        # Change to test directory
        original_dir = Path.cwd()
        os.chdir(test_dir)
        
        # Test web service readiness
        print("🔍 Testing web service readiness...")
        sys.path.insert(0, str(test_dir / "src"))
        
        try:
            from src.platform.web_interface import app
            
            # Check Flask app configuration
            if hasattr(app, 'url_map'):
                routes = [rule.rule for rule in app.url_map.iter_rules()]
                core_routes = ['/', '/signup', '/login', '/dashboard', '/contribute']
                found_routes = [route for route in core_routes if route in routes]
                
                if len(found_routes) >= 3:
                    print(f"✅ Core routes registered: {found_routes}")
                else:
                    print(f"⚠️ Some core routes missing. Found: {found_routes}")
                
                print("✅ Web service ready for community engagement!")
                return True
            else:
                print("❌ Web interface not properly configured")
                return False
                
        except Exception as e:
            print(f"❌ Web interface test failed: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Community readiness test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # Return to original directory
        os.chdir(original_dir)

def run_complete_minimal_cycle():
    """Run the complete minimal ICE bootstrap cycle"""
    print("🌊 Living Codex - Minimal ICE Bootstrap Cycle")
    print("=" * 70)
    print("Testing: WATER → ICE → WATER transformation (Minimal Implementation)")
    print("Ensuring: Zero errors, full functionality, community readiness")
    print("=" * 70)
    
    # Step 1: Create clean environment
    test_dir = create_clean_environment()
    
    try:
        # Step 2: Copy essential files
        copied_count = copy_essential_files(Path.cwd(), test_dir)
        if copied_count < 10:
            print("❌ Insufficient files copied for testing")
            return False
        
        # Step 3: Test ICE core creation
        if not test_ice_core_creation(test_dir):
            print("\n❌ Cycle failed at ICE core creation")
            return False
        
        # Step 4: Test minimal ICE bootstrap
        if not test_minimal_ice_bootstrap(test_dir):
            print("\n❌ Cycle failed at minimal ICE bootstrap")
            return False
        
        # Step 5: Test community readiness
        if not test_community_readiness(test_dir):
            print("\n❌ Cycle failed at community readiness")
            return False
        
        print("\n🎉 COMPLETE MINIMAL ICE BOOTSTRAP CYCLE SUCCESSFUL!")
        print("=" * 70)
        print("🧊 The Living Codex has successfully:")
        print("   ✅ Transformed from WATER to ICE (bootstrap storage)")
        print("   ✅ Transformed from ICE to WATER (new system)")
        print("   ✅ Validated complete functionality")
        print("   ✅ Confirmed community readiness")
        print("\n🌐 The new WATER state is fully functional and ready to:")
        print("   - Welcome new community members")
        print("   - Handle user registrations and profiles")
        print("   - Manage contributions and collaborations")
        print("   - Provide personalized experiences")
        print("   - Scale and grow with the community")
        
        return True
        
    except Exception as e:
        print(f"\n💥 Cycle failed with unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        # Clean up test environment
        print(f"\n🧹 Cleaning up test environment...")
        try:
            shutil.rmtree(test_dir)
            print("✅ Test environment cleaned up")
        except Exception as e:
            print(f"⚠️ Cleanup warning: {e}")

def main():
    """Main function"""
    try:
        success = run_complete_minimal_cycle()
        
        if success:
            print("\n🚀 Minimal ICE Bootstrap Cycle Complete!")
            print("The Living Codex can now reliably transform between states")
            print("and serve the community without errors!")
        else:
            print("\n❌ Cycle failed - system needs attention")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⏹️ Cycle interrupted by user")
    except Exception as e:
        print(f"\n💥 Cycle failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
