#!/usr/bin/env python3
"""
Living Codex - Consolidated CLI Interface
Main entry point for the comprehensive Living Codex CLI system.

🌟 This CLI combines all features from all previous versions:
✨ Resonance analysis and energy management
🧠 AI agent simulation and autonomous learning  
💾 Knowledge base operations and persistence
🔍 Code intelligence and analysis
📁 Digital asset management
🔬 Advanced search and exploration
🚀 Demo and testing capabilities
👥 User management and discovery
🌌 Complete ontology exploration
📁 File and system operations

The consolidated CLI provides complete functionality with proper import handling.
"""

import sys
from pathlib import Path

def main():
    """Launch the consolidated Living Codex CLI"""
    print("🌌 Living Codex Consolidated CLI Interface")
    print("=" * 60)
    print()
    print("🌟 This CLI combines ALL features from all previous versions:")
    print("   • Resonance analysis and energy management")
    print("   • AI agent simulation and autonomous learning")
    print("   • Knowledge base operations and persistence")
    print("   • Code intelligence and analysis")
    print("   • Digital asset management")
    print("   • Advanced search and exploration")
    print("   • Demo and testing capabilities")
    print("   • User management and discovery")
    print("   • Complete ontology exploration")
    print("   • File and system operations")
    print()
    print("🚀 Launching consolidated CLI...")
    print()
    
    try:
        # Import the consolidated CLI from the proper location
        from src.core.living_codex_cli import LivingCodexCLI
        
        print("✅ Consolidated CLI loaded successfully")
        print("🌌 Starting Living Codex experience...")
        print()
        
        cli = LivingCodexCLI()
        cli.cmdloop()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're running from the project root directory")
        print("   Current directory:", Path.cwd())
        print("   Expected structure: src/core/living_codex_cli.py")
        print()
        print("🔄 Trying alternative import path...")
        
        try:
            # Try alternative import path
            sys.path.insert(0, str(Path(__file__).parent / "src" / "core"))
            from living_codex_cli import LivingCodexCLI
            
            print("✅ Alternative import successful")
            cli = LivingCodexCLI()
            cli.cmdloop()
            
        except ImportError as e2:
            print(f"❌ Alternative import also failed: {e2}")
            print("💡 Please ensure the consolidated CLI is properly installed")
            print("   Run: python -m src.core.living_codex_cli")
            return 1
            
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error launching consolidated CLI: {e}")
        print("💡 Please check the installation and try again")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())