#!/usr/bin/env python3
"""
Living Codex - Minimal CLI Interface
A streamlined command line interface for the Living Codex system.
"""

import sys
import os
import json
import cmd
import shlex
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import re

class MinimalCodexCLI(cmd.Cmd):
    """Minimal CLI for the Living Codex system"""
    
    intro = """
🌌 Welcome to the Living Codex CLI (Minimal Version)

This is a streamlined interface to the Living Codex system.
Type 'help' to see available commands or 'help <command>' for detailed help.
Type 'quit' or 'exit' to leave.

✨ Available subsystems:
   - System navigation and exploration
   - Basic content management
   - Demo and testing capabilities
   - File and directory operations

============================================================
    """
    
    prompt = "Living-Codex> "
    
    def __init__(self):
        super().__init__()
        self.project_root = Path(__file__).parent
        self.current_energy = 10000
        self.total_energy_spent = 0
        
    def preloop(self):
        """Initialize the CLI"""
        print("🚀 Initializing Living Codex Minimal CLI...")
        print("✅ CLI ready")
        
    def do_help(self, arg):
        """Show help for commands"""
        if arg:
            super().do_help(arg)
        else:
            print("\n🌌 Living Codex CLI Commands:")
            print("=" * 50)
            print("📁 File & System Operations:")
            print("  ls [path]          - List files and directories")
            print("  cd <path>          - Change directory")
            print("  pwd                - Show current directory")
            print("  find <pattern>     - Find files matching pattern")
            print("  cat <file>         - Display file contents")
            print("")
            print("🔍 Exploration & Discovery:")
            print("  explore            - Explore system structure")
            print("  search <term>      - Search for content")
            print("  status             - Show system status")
            print("")
            print("🚀 Demo & Testing:")
            print("  demo <name>        - Run a demonstration")
            print("  list_demos         - List available demos")
            print("  test               - Run basic system tests")
            print("")
            print("⚡ System Management:")
            print("  energy             - Show current energy levels")
            print("  info               - Show system information")
            print("  components         - List system components")
            print("")
            print("🚪 Control:")
            print("  quit, exit         - Exit the CLI")
            print("  clear              - Clear the screen")
            print("")
    
    # File & System Operations
    def do_ls(self, arg):
        """List files and directories: ls [path]"""
        path = Path(arg) if arg else Path.cwd()
        try:
            if path.is_file():
                print(f"📄 {path.name} ({path.stat().st_size} bytes)")
            elif path.is_dir():
                items = list(path.iterdir())
                print(f"\n📁 {path} ({len(items)} items):")
                print("-" * 50)
                for item in sorted(items):
                    if item.is_dir():
                        print(f"📁 {item.name}/")
                    else:
                        size = item.stat().st_size
                        print(f"📄 {item.name} ({size} bytes)")
            else:
                print(f"❌ Path not found: {path}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def do_cd(self, arg):
        """Change directory: cd <path>"""
        if not arg:
            arg = str(self.project_root)
        try:
            new_path = Path(arg).resolve()
            if new_path.is_dir():
                os.chdir(new_path)
                print(f"📁 Changed to: {new_path}")
            else:
                print(f"❌ Directory not found: {arg}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def do_pwd(self, arg):
        """Show current directory"""
        print(f"📁 Current directory: {Path.cwd()}")
    
    def do_find(self, arg):
        """Find files matching pattern: find <pattern>"""
        if not arg:
            print("❌ Please provide a search pattern")
            return
        
        try:
            root = Path.cwd()
            pattern = f"*{arg}*"
            matches = list(root.rglob(pattern))
            
            print(f"\n🔍 Found {len(matches)} matches for '{arg}':")
            print("-" * 50)
            for match in sorted(matches)[:20]:  # Limit to 20 results
                rel_path = match.relative_to(root)
                if match.is_dir():
                    print(f"📁 {rel_path}/")
                else:
                    print(f"📄 {rel_path}")
            
            if len(matches) > 20:
                print(f"... and {len(matches) - 20} more matches")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def do_cat(self, arg):
        """Display file contents: cat <file>"""
        if not arg:
            print("❌ Please provide a file path")
            return
        
        try:
            file_path = Path(arg)
            if file_path.is_file():
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                print(f"\n📄 {file_path} ({len(content)} chars):")
                print("=" * 50)
                print(content[:2000])  # Limit to first 2000 chars
                if len(content) > 2000:
                    print(f"\n... ({len(content) - 2000} more characters)")
            else:
                print(f"❌ File not found: {arg}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Exploration & Discovery
    def do_explore(self, arg):
        """Explore system structure"""
        print("\n🌌 Living Codex System Structure:")
        print("=" * 50)
        
        structure = {
            "🧊 ICE Core": ["src/core/", "Bootstrap system, dependencies, storage"],
            "🌌 Ontology": ["src/ontology/", "Knowledge representation, consciousness"],
            "🧠 AI Agents": ["src/ai_agents/", "Autonomous learning, intelligence"],
            "🌐 Platform": ["src/platform/", "Web interface, user management"],
            "🔬 Demos": ["src/demos/", "Demonstrations and examples"],
            "🐳 Docker": ["docker/", "Containerization and deployment"],
            "🌍 Regional Hubs": ["regional_hubs/", "Distributed network nodes"],
            "📚 Documentation": ["docs/", "System documentation"]
        }
        
        for component, (path, description) in structure.items():
            full_path = self.project_root / path
            status = "✅" if full_path.exists() else "❌"
            print(f"{status} {component}")
            print(f"   📁 {path}")
            print(f"   📝 {description}")
            print()
    
    def do_search(self, arg):
        """Search for content: search <term>"""
        if not arg:
            print("❌ Please provide a search term")
            return
        
        print(f"\n🔍 Searching for '{arg}'...")
        matches = []
        
        try:
            # Search in Python files
            for py_file in self.project_root.rglob("*.py"):
                try:
                    content = py_file.read_text(encoding='utf-8', errors='ignore')
                    if arg.lower() in content.lower():
                        matches.append(("Python", py_file))
                except:
                    continue
            
            # Search in markdown files
            for md_file in self.project_root.rglob("*.md"):
                try:
                    content = md_file.read_text(encoding='utf-8', errors='ignore')
                    if arg.lower() in content.lower():
                        matches.append(("Markdown", md_file))
                except:
                    continue
            
            print(f"Found {len(matches)} matches:")
            print("-" * 50)
            for file_type, file_path in matches[:15]:  # Limit to 15 results
                rel_path = file_path.relative_to(self.project_root)
                print(f"📄 {file_type}: {rel_path}")
            
            if len(matches) > 15:
                print(f"... and {len(matches) - 15} more matches")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def do_status(self, arg):
        """Show system status"""
        print("\n📊 Living Codex System Status:")
        print("=" * 50)
        
        # Check key directories
        components = [
            ("🧊 ICE Core", "src/core/"),
            ("🌌 Ontology", "src/ontology/"),
            ("🧠 AI Agents", "src/ai_agents/"),
            ("🌐 Platform", "src/platform/"),
            ("🔬 Demos", "src/demos/"),
            ("🐳 Docker", "docker/"),
        ]
        
        for name, path in components:
            full_path = self.project_root / path
            if full_path.exists():
                file_count = len(list(full_path.rglob("*.py")))
                print(f"✅ {name}: {file_count} Python files")
            else:
                print(f"❌ {name}: Not found")
        
        print(f"\n⚡ Energy: {self.current_energy:,}")
        print(f"💰 Energy Spent: {self.total_energy_spent:,}")
    
    # Demo & Testing
    def do_demo(self, arg):
        """Run a demonstration: demo <name>"""
        if not arg:
            print("❌ Please specify a demo name. Use 'list_demos' to see available demos.")
            return
        
        demos_dir = self.project_root / "src" / "demos"
        demo_file = demos_dir / f"{arg}.py"
        
        if not demo_file.exists():
            demo_file = demos_dir / f"demo_{arg}.py"
        
        if demo_file.exists():
            print(f"\n🚀 Running demo: {arg}")
            print("-" * 50)
            try:
                # Execute the demo file
                os.system(f"cd {self.project_root} && python {demo_file}")
            except Exception as e:
                print(f"❌ Error running demo: {e}")
        else:
            print(f"❌ Demo not found: {arg}")
            print("Use 'list_demos' to see available demos.")
    
    def do_list_demos(self, arg):
        """List available demonstrations"""
        demos_dir = self.project_root / "src" / "demos"
        
        if not demos_dir.exists():
            print("❌ Demos directory not found")
            return
        
        print("\n🚀 Available Demonstrations:")
        print("=" * 50)
        
        demo_files = list(demos_dir.glob("*.py"))
        demo_files = [f for f in demo_files if f.name != "__init__.py"]
        
        for demo_file in sorted(demo_files):
            name = demo_file.stem
            if name.startswith("demo_"):
                name = name[5:]  # Remove "demo_" prefix
            
            # Try to read the docstring
            try:
                content = demo_file.read_text(encoding='utf-8', errors='ignore')
                lines = content.split('\n')
                description = "No description"
                for line in lines:
                    if '"""' in line or "'''" in line:
                        desc_line = lines[lines.index(line) + 1] if lines.index(line) + 1 < len(lines) else ""
                        if desc_line.strip():
                            description = desc_line.strip()
                        break
            except:
                description = "No description"
            
            print(f"🔬 {name}")
            print(f"   📝 {description}")
            print()
    
    def do_test(self, arg):
        """Run basic system tests"""
        print("\n🧪 Running Living Codex System Tests:")
        print("=" * 50)
        
        tests = [
            ("Directory Structure", self._test_directory_structure),
            ("Python Files", self._test_python_files),
            ("Core Components", self._test_core_components),
            ("Documentation", self._test_documentation),
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                status = "✅ PASS" if result else "❌ FAIL"
                print(f"{status} {test_name}")
                if result:
                    passed += 1
            except Exception as e:
                print(f"❌ ERROR {test_name}: {e}")
        
        print(f"\n📊 Test Results: {passed}/{total} passed")
    
    def _test_directory_structure(self):
        """Test if key directories exist"""
        required_dirs = ["src", "src/core", "src/platform", "docs"]
        return all((self.project_root / d).exists() for d in required_dirs)
    
    def _test_python_files(self):
        """Test if Python files can be parsed"""
        py_files = list(self.project_root.rglob("*.py"))
        return len(py_files) > 10  # Should have at least 10 Python files
    
    def _test_core_components(self):
        """Test if core components exist"""
        core_files = ["src/core/minimal_ice_bootstrap.py", "src/core/dependency_manager.py"]
        return all((self.project_root / f).exists() for f in core_files)
    
    def _test_documentation(self):
        """Test if documentation exists"""
        docs = list(self.project_root.glob("*.md"))
        return len(docs) > 0
    
    # System Management
    def do_energy(self, arg):
        """Show current energy levels"""
        print(f"\n⚡ Energy Status:")
        print("=" * 30)
        print(f"💰 Current Energy: {self.current_energy:,}")
        print(f"💸 Total Spent: {self.total_energy_spent:,}")
        print(f"📊 Efficiency: {(self.current_energy / 10000) * 100:.1f}%")
    
    def do_info(self, arg):
        """Show system information"""
        print("\n🌌 Living Codex System Information:")
        print("=" * 50)
        print(f"📁 Project Root: {self.project_root}")
        print(f"🐍 Python Version: {sys.version.split()[0]}")
        print(f"💻 Platform: {sys.platform}")
        print(f"📊 Working Directory: {Path.cwd()}")
        
        # Count files
        py_files = len(list(self.project_root.rglob("*.py")))
        md_files = len(list(self.project_root.rglob("*.md")))
        total_files = len(list(self.project_root.rglob("*")))
        
        print(f"📄 Python Files: {py_files}")
        print(f"📝 Markdown Files: {md_files}")
        print(f"📂 Total Files: {total_files}")
    
    def do_components(self, arg):
        """List system components"""
        print("\n🔧 Living Codex Components:")
        print("=" * 50)
        
        components_map = {
            "src/core/": "🧊 ICE Core Components",
            "src/ontology/": "🌌 Ontology Components", 
            "src/ai_agents/": "🧠 AI Agent Components",
            "src/platform/": "🌐 Platform Components",
            "src/demos/": "🔬 Demo Components",
        }
        
        for path, title in components_map.items():
            full_path = self.project_root / path
            if full_path.exists():
                py_files = [f for f in full_path.rglob("*.py") if f.name != "__init__.py"]
                print(f"\n{title} ({len(py_files)} files):")
                for py_file in sorted(py_files)[:10]:  # Limit to 10 per category
                    rel_path = py_file.relative_to(full_path)
                    print(f"  📄 {rel_path}")
                if len(py_files) > 10:
                    print(f"  ... and {len(py_files) - 10} more")
    
    # Control
    def do_quit(self, arg):
        """Exit the CLI"""
        print("\n👋 Thank you for using Living Codex CLI!")
        print("🌌 May your code resonate with the universe...")
        return True
    
    def do_exit(self, arg):
        """Exit the CLI"""
        return self.do_quit(arg)
    
    def do_clear(self, arg):
        """Clear the screen"""
        os.system('clear' if sys.platform != 'win32' else 'cls')
    
    def do_EOF(self, arg):
        """Handle Ctrl+D"""
        print()
        return self.do_quit(arg)

def main():
    """Run the CLI"""
    try:
        cli = MinimalCodexCLI()
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
