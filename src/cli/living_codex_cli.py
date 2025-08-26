#!/usr/bin/env python3
"""
Living Codex CLI - Functional Command Line Interface
A comprehensive CLI that integrates with the web API to expose all system features.

Usage:
    python living_codex_cli.py [command] [options]
    
Commands:
    status          - Show system status
    search <query>  - Search the system
    components      - List all components
    nodes           - List all nodes
    inventory       - Generate system inventory
    report          - Generate comprehensive report
    test            - Run test suites
    help            - Show this help
"""

import sys
import os
import json
import argparse
import requests
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from core.fractal_components import FractalComponent
    from core.core_system import fractal_core_system
    FRACTAL_AVAILABLE = True
except ImportError:
    FRACTAL_AVAILABLE = False

class LivingCodexCLI:
    """
    Functional Living Codex CLI that integrates with the web API
    """
    
    def __init__(self, api_base_url: str = "http://localhost:5004"):
        self.api_base_url = api_base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'LivingCodexCLI/1.0',
            'Accept': 'application/json'
        })
    
    def _make_api_request(self, endpoint: str, method: str = "GET", data: Dict = None) -> Dict[str, Any]:
        """Make a request to the API"""
        try:
            url = f"{self.api_base_url}{endpoint}"
            if method.upper() == "GET":
                response = self.session.get(url)
            elif method.upper() == "POST":
                response = self.session.post(url, json=data)
            else:
                return {"error": f"Unsupported method: {method}"}
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API request failed: {response.status_code}", "details": response.text}
                
        except requests.exceptions.ConnectionError:
            return {"error": f"Cannot connect to API at {self.api_base_url}. Is the web server running?"}
        except Exception as e:
            return {"error": f"API request failed: {str(e)}"}
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return self._make_api_request("/api/system/status")
    
    def search_system(self, query: str, search_type: str = "all") -> Dict[str, Any]:
        """Search the system"""
        params = {"q": query, "type": search_type}
        return self._make_api_request("/api/search", data=params)
    
    def get_components(self) -> Dict[str, Any]:
        """Get all system components"""
        status = self.get_system_status()
        if "error" in status:
            return status
        
        components = status.get("fractal_components", [])
        return {
            "total_components": len(components),
            "components": components
        }
    
    def get_nodes(self) -> Dict[str, Any]:
        """Get all system nodes"""
        status = self.get_system_status()
        if "error" in status:
            return status
        
        return {
            "total_nodes": status.get("total_nodes", 0),
            "node_types": status.get("node_types", {}),
            "fractal_layers": status.get("fractal_layers", {}),
            "water_states": status.get("water_states", {}),
            "chakras": status.get("chakras", {}),
            "frequencies": status.get("frequencies", {})
        }
    
    def generate_inventory(self) -> Dict[str, Any]:
        """Generate system inventory using the inventory report system"""
        try:
            if FRACTAL_AVAILABLE:
                from core.inventory_report_system import inventory_report_system
                return inventory_report_system.scan_system_inventory()
            else:
                return {"error": "Fractal system not available for inventory generation"}
        except Exception as e:
            return {"error": f"Inventory generation failed: {str(e)}"}
    
    def generate_report(self, report_type: str = "system_health") -> Dict[str, Any]:
        """Generate comprehensive system report"""
        try:
            if FRACTAL_AVAILABLE:
                from core.inventory_report_system import inventory_report_system
                report = inventory_report_system.generate_comprehensive_report(report_type)
                if report:
                    return {
                        "success": True,
                        "report_id": report.report_id,
                        "title": report.title,
                        "overall_health_score": report.overall_health_score,
                        "critical_issues_count": len(report.critical_issues),
                        "action_items_count": len(report.action_items),
                        "sections_count": len(report.sections)
                    }
                else:
                    return {"error": "Failed to generate report"}
            else:
                return {"error": "Fractal system not available for report generation"}
        except Exception as e:
            return {"error": f"Report generation failed: {str(e)}"}
    
    def run_tests(self, test_category: str = "all") -> Dict[str, Any]:
        """Run test suites"""
        try:
            if FRACTAL_AVAILABLE:
                from test_suites.comprehensive_test_system import ComprehensiveTestSystem
                test_system = ComprehensiveTestSystem()
                return test_system.run_tests(test_category)
            else:
                return {"error": "Fractal system not available for testing"}
        except Exception as e:
            return {"error": f"Test execution failed: {str(e)}"}
    
    def display_status(self):
        """Display system status in a formatted way"""
        print("🔍 Living Codex System Status")
        print("=" * 50)
        
        status = self.get_system_status()
        if "error" in status:
            print(f"❌ Error: {status['error']}")
            return
        
        # System overview
        overview = status.get("system_overview", {})
        print(f"📊 System Overview:")
        print(f"   Name: {overview.get('name', 'Unknown')}")
        print(f"   Version: {overview.get('version', 'Unknown')}")
        print(f"   Total Nodes: {overview.get('total_nodes', 0):,}")
        print(f"   Component Count: {overview.get('component_count', 0)}")
        print(f"   Node Types: {overview.get('node_types_count', 0)}")
        print()
        
        # System health
        health = status.get("system_health", {})
        print(f"🏥 System Health:")
        print(f"   Self-Similarity: {health.get('self_similarity', 0):.1f}%")
        print(f"   Meta-Circularity: {health.get('meta_circularity', 0):.1f}%")
        print(f"   Holographic Nature: {health.get('holographic_nature', 0):.1f}%")
        print(f"   Fractal Integrity: {health.get('fractal_integrity', 0):.1f}%")
        print()
        
        # Fractal architecture
        print(f"🌌 Fractal Architecture:")
        print(f"   Fractal Layers: {len(status.get('fractal_layers', {}))}")
        print(f"   Water States: {len(status.get('water_states', {}))}")
        print(f"   Chakras: {len(status.get('chakras', {}))}")
        print(f"   Frequencies: {len(status.get('frequencies', {}))}")
    
    def display_components(self):
        """Display system components"""
        print("🔧 System Components")
        print("=" * 50)
        
        components = self.get_components()
        if "error" in components:
            print(f"❌ Error: {components['error']}")
            return
        
        print(f"Total Components: {components['total_components']}")
        print()
        
        for i, component in enumerate(components['components'], 1):
            print(f"{i:2d}. {component}")
    
    def display_nodes(self):
        """Display system nodes summary"""
        print("🌳 System Nodes")
        print("=" * 50)
        
        nodes = self.get_nodes()
        if "error" in nodes:
            print(f"❌ Error: {nodes['error']}")
            return
        
        print(f"Total Nodes: {nodes['total_nodes']:,}")
        print()
        
        # Node types
        node_types = nodes.get('node_types', {})
        print(f"Node Types ({len(node_types)}):")
        for node_type, info in list(node_types.items())[:10]:  # Show first 10
            print(f"  • {node_type}")
        if len(node_types) > 10:
            print(f"  ... and {len(node_types) - 10} more")
        print()
        
        # Fractal layers
        fractal_layers = nodes.get('fractal_layers', {})
        print(f"Fractal Layers ({len(fractal_layers)}):")
        for layer, info in fractal_layers.items():
            print(f"  • Layer {info.get('layer', layer)}: {info.get('count', 1)} nodes")
    
    def display_search_results(self, query: str):
        """Display search results"""
        print(f"🔍 Search Results for: '{query}'")
        print("=" * 50)
        
        results = self.search_system(query)
        if "error" in results:
            print(f"❌ Error: {results['error']}")
            return
        
        total_count = results.get('total_count', 0)
        print(f"Total Results: {total_count}")
        print()
        
        if total_count == 0:
            print("No results found.")
            return
        
        # Display first few results
        search_results = results.get('results', [])
        for i, result in enumerate(search_results[:5], 1):  # Show first 5
            print(f"{i}. {result.get('name', 'Unknown')}")
            print(f"   Type: {result.get('node_type', 'Unknown')}")
            print(f"   Content: {result.get('content', 'No content')[:100]}...")
            print()
        
        if total_count > 5:
            print(f"... and {total_count - 5} more results")
    
    def display_inventory(self):
        """Display system inventory"""
        print("📋 System Inventory")
        print("=" * 50)
        
        inventory = self.generate_inventory()
        if "error" in inventory:
            print(f"❌ Error: {inventory['error']}")
            return
        
        print(f"Scan Timestamp: {inventory.get('scan_timestamp', 'Unknown')}")
        print()
        
        # System overview
        overview = inventory.get('system_overview', {})
        print(f"📊 Overview:")
        print(f"   Total Components: {overview.get('total_components', 0)}")
        print(f"   Total Nodes: {overview.get('total_nodes', 0):,}")
        print()
        
        # System health
        health = inventory.get('system_health', {})
        print(f"🏥 Health Score: {health.get('overall_health', 0):.1f}%")
        
        # Fractal integrity
        fractal_integrity = health.get('fractal_integrity', {})
        if fractal_integrity:
            print(f"🌌 Fractal Integrity:")
            for aspect, data in fractal_integrity.items():
                if isinstance(data, dict):
                    status = data.get('status', 'UNKNOWN')
                    score = data.get('score', 0)
                    print(f"   {aspect.replace('_', ' ').title()}: {score:.1f}% ({status})")
    
    def display_report(self, report_type: str = "system_health"):
        """Display system report"""
        print(f"📊 System Report: {report_type.replace('_', ' ').title()}")
        print("=" * 50)
        
        report = self.generate_report(report_type)
        if "error" in report:
            print(f"❌ Error: {report['error']}")
            return
        
        print(f"Report ID: {report['report_id']}")
        print(f"Title: {report['title']}")
        print(f"Overall Health: {report['overall_health_score']:.1f}%")
        print(f"Critical Issues: {report['critical_issues_count']}")
        print(f"Action Items: {report['action_items_count']}")
        print(f"Sections: {report['sections_count']}")
    
    def display_tests(self, test_category: str = "all"):
        """Display test results"""
        print(f"🧪 Test Results: {test_category.replace('_', ' ').title()}")
        print("=" * 50)
        
        test_results = self.run_tests(test_category)
        if "error" in test_results:
            print(f"❌ Error: {test_results['error']}")
            return
        
        print(f"Test Category: {test_results.get('test_category', 'Unknown')}")
        print(f"Description: {test_results.get('description', 'No description')}")
        print()
        
        results = test_results.get('results', {})
        for test_name, test_result in results.items():
            status = "✅ PASS" if test_result.get('success', False) else "❌ FAIL"
            print(f"{status} {test_name}")
            if 'message' in test_result:
                print(f"   {test_result['message']}")
    
    def run_interactive_mode(self):
        """Run interactive CLI mode"""
        print("🌌 Living Codex CLI - Interactive Mode")
        print("Type 'help' for commands, 'quit' to exit")
        print("=" * 50)
        
        while True:
            try:
                command = input("\n🔮 > ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                elif command in ['help', 'h', '?']:
                    self.show_help()
                elif command in ['status', 's']:
                    self.display_status()
                elif command in ['components', 'c']:
                    self.display_components()
                elif command in ['nodes', 'n']:
                    self.display_nodes()
                elif command in ['inventory', 'i']:
                    self.display_inventory()
                elif command.startswith('search '):
                    query = command[7:].strip()
                    if query:
                        self.display_search_results(query)
                    else:
                        print("❌ Please provide a search query")
                elif command.startswith('report '):
                    report_type = command[7:].strip()
                    if report_type:
                        self.display_report(report_type)
                    else:
                        self.display_report()
                elif command.startswith('test '):
                    test_category = command[5:].strip()
                    if test_category:
                        self.display_tests(test_category)
                    else:
                        self.display_tests()
                elif command == 'test':
                    self.display_tests()
                elif command == '':
                    continue
                else:
                    print(f"❌ Unknown command: {command}")
                    print("Type 'help' for available commands")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")
    
    def show_help(self):
        """Show help information"""
        print("🌌 Living Codex CLI - Available Commands")
        print("=" * 50)
        print("Commands:")
        print("  status, s           - Show system status")
        print("  components, c       - List all components")
        print("  nodes, n            - List all nodes")
        print("  inventory, i        - Generate system inventory")
        print("  search <query>      - Search the system")
        print("  report [type]       - Generate system report")
        print("  test [category]     - Run test suites")
        print("  help, h, ?          - Show this help")
        print("  quit, exit, q       - Exit the CLI")
        print()
        print("Report Types: system_health, component_status, architectural_integrity")
        print("Test Categories: all, fractal_architecture, core_functionality, search_functionality")
        print()
        print("Examples:")
        print("  search water        - Search for water-related nodes")
        print("  report system_health - Generate system health report")
        print("  test fractal_architecture - Run fractal architecture tests")

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Living Codex CLI - Access all system features via command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s status                    # Show system status
  %(prog)s search water              # Search for water nodes
  %(prog)s inventory                 # Generate system inventory
  %(prog)s report system_health      # Generate health report
  %(prog)s test fractal_architecture # Run specific tests
  %(prog)s --interactive             # Run interactive mode
        """
    )
    
    parser.add_argument('command', nargs='?', help='Command to execute')
    parser.add_argument('args', nargs='*', help='Command arguments')
    parser.add_argument('--api-url', default='http://localhost:5004', 
                       help='API base URL (default: http://localhost:5004)')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run in interactive mode')
    
    args = parser.parse_args()
    
    # Create CLI instance
    cli = LivingCodexCLI(args.api_url)
    
    # Check if web server is accessible
    status = cli.get_system_status()
    if "error" in status and "Cannot connect" in status["error"]:
        print("❌ Cannot connect to Living Codex web server")
        print(f"   Expected URL: {args.api_url}")
        print("   Please ensure the web server is running")
        print("   You can start it with: python web_platform/unified_web_interface.py")
        return 1
    
    # Run interactive mode if requested
    if args.interactive or not args.command:
        cli.run_interactive_mode()
        return 0
    
    # Execute single command
    try:
        if args.command == 'status':
            cli.display_status()
        elif args.command == 'components':
            cli.display_components()
        elif args.command == 'nodes':
            cli.display_nodes()
        elif args.command == 'inventory':
            cli.display_inventory()
        elif args.command == 'search':
            if args.args:
                cli.display_search_results(' '.join(args.args))
            else:
                print("❌ Please provide a search query")
                return 1
        elif args.command == 'report':
            report_type = args.args[0] if args.args else 'system_health'
            cli.display_report(report_type)
        elif args.command == 'test':
            test_category = args.args[0] if args.args else 'all'
            cli.display_tests(test_category)
        elif args.command == 'help':
            cli.show_help()
        else:
            print(f"❌ Unknown command: {args.command}")
            cli.show_help()
            return 1
            
    except Exception as e:
        print(f"❌ Error executing command: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
