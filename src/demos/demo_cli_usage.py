#!/usr/bin/env python3
"""
Living Codex CLI - Usage Demonstration
Shows how to use the resonance-aware CLI interface
"""

import subprocess
import time

def demo_cli_commands():
    """Demonstrate CLI commands with explanations"""
    
    print("🌟 Living Codex CLI - Usage Demonstration")
    print("=" * 60)
    print()
    
    commands = [
        ("energy", "Check current energy status"),
        ("analyze 'quantum consciousness field'", "Analyze resonance of potential content"),
        ("analyze 'destroy everything'", "Analyze anti-resonant content (high cost)"),
        ("analyze 'enhance knowledge representation'", "Analyze resonant content (low cost)"),
        ("list", "List all existing nodes"),
        ("search consciousness", "Search for nodes containing 'consciousness'"),
        ("help create", "Get help on the create command"),
        ("quit", "Exit the CLI")
    ]
    
    print("📋 CLI Commands to try:")
    print("-" * 40)
    
    for i, (command, description) in enumerate(commands, 1):
        print(f"{i:2d}. {command:<35} - {description}")
    
    print()
    print("🎯 Key Features:")
    print("• 🟢 High resonance changes cost less energy")
    print("• 🟡 Medium resonance changes cost moderate energy")
    print("• 🔴 Low resonance changes cost high energy")
    print("• Anti-resonant changes (like deletion) are very expensive")
    print("• Content similar to existing knowledge is more resonant")
    print("• Destructive or chaotic content is anti-resonant")
    print()
    
    print("🚀 To start the interactive CLI:")
    print("   python codex_cli.py")
    print()
    
    print("💡 Example Usage Scenarios:")
    print("-" * 30)
    
    scenarios = [
        {
            "title": "Creating Resonant Content",
            "commands": [
                "analyze 'machine learning algorithm'",
                "create 'ml_algorithm'",
                "# (then fill in: content='Advanced neural network for pattern recognition')"
            ],
            "note": "This would be highly resonant if ML concepts already exist"
        },
        {
            "title": "Creating Anti-Resonant Content", 
            "commands": [
                "analyze 'random chaos destruction'",
                "create 'chaos_node'",
                "# (then fill in: content='random chaos destruction')"
            ],
            "note": "This would cost much more energy due to anti-resonance"
        },
        {
            "title": "Exploring the System",
            "commands": [
                "list concept",
                "search quantum",
                "explore <node_id>",
                "resonate <node_id>"
            ],
            "note": "Understanding the system helps create more resonant content"
        }
    ]
    
    for scenario in scenarios:
        print(f"\n📖 {scenario['title']}:")
        for cmd in scenario['commands']:
            if cmd.startswith("#"):
                print(f"     {cmd}")
            else:
                print(f"   > {cmd}")
        print(f"   💡 {scenario['note']}")
    
    print()
    print("🎵 Resonance Principles:")
    print("• Content similar to existing knowledge = higher resonance = lower cost")
    print("• Content that builds on established patterns = harmonious")
    print("• Content that contradicts or destroys = anti-resonant = high cost")
    print("• The system learns what resonates and adapts accordingly")
    print()
    
    print("⚡ Energy Management:")
    print("• You start with 10,000 energy units")
    print("• High resonance changes: ~100-300 energy")
    print("• Medium resonance changes: ~300-600 energy") 
    print("• Low resonance changes: ~600-1000+ energy")
    print("• Deletions: 500+ energy (anti-resonant)")
    print()

if __name__ == "__main__":
    demo_cli_commands()
