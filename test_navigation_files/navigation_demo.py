#!/usr/bin/env python3
"""
Web Interface Navigation Demo
Demonstrates the Living Codex web interface navigation capabilities
"""

from flask import Flask, render_template, request, jsonify
from typing import Dict, List, Any
import json

class NavigationDemo:
    """Demonstrates navigation flow through the Living Codex system"""
    
    def __init__(self):
        self.navigation_paths = {
            "void_to_user": {
                "description": "Navigate from system void to user profile",
                "steps": [
                    "System entry point (Void)",
                    "User discovery",
                    "Profile access",
                    "User information display"
                ]
            },
            "user_to_user": {
                "description": "Navigate from one user to another user",
                "steps": [
                    "Current user profile",
                    "Related users discovery",
                    "User selection",
                    "Target user profile"
                ]
            },
            "user_to_concept": {
                "description": "Navigate from user to concept of interest",
                "steps": [
                    "User profile",
                    "Interests exploration",
                    "Concept selection",
                    "Concept details"
                ]
            },
            "concept_to_source": {
                "description": "Navigate from concept to source file",
                "steps": [
                    "Concept information",
                    "Related content discovery",
                    "Source file selection",
                    "File content display"
                ]
            },
            "source_to_expression": {
                "description": "Navigate from source file to specific expression",
                "steps": [
                    "Source file content",
                    "Code structure analysis",
                    "Expression identification",
                    "Expression details"
                ]
            }
        }
    
    def get_navigation_flow(self, flow_type: str) -> Dict[str, Any]:
        """Get complete navigation flow for a specific type"""
        if flow_type not in self.navigation_paths:
            return {"error": "Unknown navigation flow type"}
        
        flow = self.navigation_paths[flow_type]
        
        # Add example data for the flow
        if flow_type == "void_to_user":
            flow["example_data"] = {
                "start_point": "System Void",
                "target_user": "Alice Chen",
                "user_type": "Software Developer",
                "interests": ["Python", "Flask", "React", "Neural Networks"]
            }
        elif flow_type == "user_to_user":
            flow["example_data"] = {
                "current_user": "Alice Chen",
                "target_user": "Bob Rodriguez",
                "connection_type": "Shared Interest",
                "common_interests": ["Artificial Intelligence", "Python"]
            }
        elif flow_type == "user_to_concept":
            flow["example_data"] = {
                "user": "Bob Rodriguez",
                "concept": "Neural Networks",
                "concept_type": "Technical Domain",
                "relevance_score": 0.95
            }
        elif flow_type == "concept_to_source":
            flow["example_data"] = {
                "concept": "Neural Networks",
                "source_file": "neural_network.py",
                "file_type": "Python Implementation",
                "complexity": "Advanced"
            }
        elif flow_type == "source_to_expression":
            flow["example_data"] = {
                "source_file": "neural_network.py",
                "expression": "AttentionMechanism class",
                "expression_type": "Class Definition",
                "line_numbers": "15-25"
            }
        
        return flow
    
    def get_complete_navigation_demo(self) -> Dict[str, Any]:
        """Get complete navigation demonstration data"""
        return {
            "title": "Complete Navigation Flow Demonstration",
            "description": "Demonstrates the full navigation path from Void to Expression",
            "flows": list(self.navigation_paths.keys()),
            "complete_path": {
                "void": "System entry point",
                "user1": "Alice Chen - Software Developer",
                "user2": "Bob Rodriguez - AI Researcher",
                "concept": "Neural Networks",
                "source_file": "neural_network.py",
                "expression": "AttentionMechanism class implementation"
            },
            "navigation_metadata": {
                "total_steps": 6,
                "estimated_time": "2-3 minutes",
                "complexity": "Intermediate",
                "prerequisites": ["Basic understanding of web interfaces"]
            }
        }

# Flask application for the demo
app = Flask(__name__)
demo = NavigationDemo()

@app.route('/')
def index():
    """Main demo page"""
    return render_template('navigation_demo.html', demo=demo.get_complete_navigation_demo())

@app.route('/api/navigation/<flow_type>')
def get_navigation_flow(flow_type):
    """API endpoint for navigation flow data"""
    return jsonify(demo.get_navigation_flow(flow_type))

@app.route('/api/navigation/complete')
def get_complete_navigation():
    """API endpoint for complete navigation data"""
    return jsonify(demo.get_complete_navigation_demo())

if __name__ == '__main__':
    print("🧭 Starting Navigation Demo...")
    print("   Open your browser to: http://localhost:5005")
    print("   Navigate through the Living Codex system!")
    
    app.run(debug=True, host='0.0.0.0', port=5005)
