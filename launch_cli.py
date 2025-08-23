#!/usr/bin/env python3
"""
Living Codex CLI Launcher
Simple launcher script that can be run from anywhere to start the consolidated CLI.
"""

import sys
import os
from pathlib import Path

def main():
    """Launch the Living Codex CLI from any location"""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Temporarily rename platform directory to avoid conflicts
    platform_dir = script_dir / "src" / "platform"
    platform_backup = script_dir / "src" / "platform_backup"
    
    if platform_dir.exists():
        print("🔄 Temporarily renaming platform directory to avoid conflicts...")
        platform_dir.rename(platform_backup)
        platform_renamed = True
    else:
        platform_renamed = False
    
    try:
        # Add the src directory to Python path
        src_path = script_dir / "src"
        if src_path.exists():
            sys.path.insert(0, str(src_path))
            print(f"✅ Added {src_path} to Python path")
        else:
            print(f"❌ Source directory not found: {src_path}")
            return 1
        
        # Import and run the consolidated CLI
        from core.living_codex_cli import LivingCodexCLI
        
        print("🚀 Living Codex Consolidated CLI Launcher")
        print("=" * 50)
        print("✅ CLI loaded successfully")
        print("🌌 Starting Living Codex experience...")
        print()
        
        cli = LivingCodexCLI()
        cli.cmdloop()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure the CLI files are properly installed")
        print(f"   Expected: {script_dir}/src/core/living_codex_cli.py")
        return 1
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error launching CLI: {e}")
        return 1
    finally:
        # Restore platform directory
        if platform_renamed and platform_backup.exists():
            print("🔄 Restoring platform directory...")
            platform_backup.rename(platform_dir)
    
    return 0

if __name__ == "__main__":
    exit(main())
