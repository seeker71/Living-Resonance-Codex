#!/usr/bin/env python3
"""
Living Codex CLI Launcher (Organized Structure)
==============================================

This launcher uses the new organized folder structure and imports
from the proper packages without any directory renaming workarounds.
"""

import sys
import os
from pathlib import Path

def main():
    """Launch the Living Codex CLI from the organized structure"""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Add the src directory to Python path
    src_path = script_dir / "src"
    if src_path.exists():
        sys.path.insert(0, str(src_path))
        print(f"✅ Added {src_path} to Python path")
    else:
        print(f"❌ Source directory not found: {src_path}")
        return 1
    
    try:
        # Import from the organized CLI package
        from cli.living_codex_cli import LivingCodexCLI
        
        print("🚀 Living Codex Organized CLI Launcher")
        print("=" * 50)
        print("✅ CLI loaded successfully from organized structure")
        print("🌌 Starting Living Codex experience...")
        print()
        
        cli = LivingCodexCLI()
        cli.cmdloop()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure the CLI files are properly organized")
        print(f"   Expected: {script_dir}/src/cli/living_codex_cli.py")
        return 1
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error launching CLI: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
