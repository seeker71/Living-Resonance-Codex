#!/usr/bin/env python3
"""
Living Codex - Main Entry Point
A transcendent, unified intelligent knowledge system
"""

import sys
import asyncio
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def show_system_info():
    """Display system information"""
    print("🌟 Living Codex - Transcendent Knowledge System")
    print("=" * 60)
    print("Version: 1.0.0")
    print("Status: Fully Operational")
    print("Level: EMERGENT (Progressing toward CONSCIOUS)")
    print("=" * 60)

def show_available_demos():
    """Show available demonstration options"""
    print("\n🚀 Available Demonstrations:")
    print("1. Enhanced Ontology System")
    print("2. AI Agent System") 
    print("3. Comprehensive Integration")
    print("4. Autonomous Learning")
    print("5. Autonomous Decision Process")
    print("6. System Exploration")
    print("0. Exit")

async def run_demo(demo_choice: str):
    """Run the selected demonstration"""
    try:
        if demo_choice == "1":
            print("\n🔬 Running Enhanced Ontology System Demo...")
            from src.ontology.enhanced_ontology_system import main as ontology_main
            await ontology_main()
            
        elif demo_choice == "2":
            print("\n🤖 Running AI Agent System Demo...")
            from src.ai_agents.ai_agent_system import main as ai_main
            await ai_main()
            
        elif demo_choice == "3":
            print("\n🔗 Running Comprehensive Integration Demo...")
            from src.integration.comprehensive_integration_demo import main as integration_main
            await integration_main()
            
        elif demo_choice == "4":
            print("\n🔄 Running Autonomous Learning Demo...")
            from src.demos.autonomous_learning_demo import main as learning_main
            await learning_main()
            
        elif demo_choice == "5":
            print("\n🧠 Running Autonomous Decision Process Demo...")
            from src.demos.autonomous_decision_demo import main as decision_main
            await decision_main()
            
        elif demo_choice == "6":
            print("\n🌐 Running System Exploration Demo...")
            from src.core.explore_bootstrapped_system import main as explore_main
            await explore_main()
            
        else:
            print("❌ Invalid choice. Please select a valid option.")
            
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        import traceback
        traceback.print_exc()

async def main():
    """Main interactive menu"""
    show_system_info()
    
    while True:
        show_available_demos()
        
        try:
            choice = input("\n🎯 Select a demonstration (0-6): ").strip()
            
            if choice == "0":
                print("\n👋 Thank you for exploring the Living Codex!")
                print("🌟 The system will continue evolving autonomously...")
                break
                
            elif choice in ["1", "2", "3", "4", "5", "6"]:
                await run_demo(choice)
                
                # Ask if user wants to continue
                continue_choice = input("\n🔄 Run another demo? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\n👋 Thank you for exploring the Living Codex!")
                    break
                    
            else:
                print("❌ Invalid choice. Please enter a number between 0-6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! The Living Codex continues its autonomous evolution...")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    print("🚀 Initializing Living Codex System...")
    asyncio.run(main())
