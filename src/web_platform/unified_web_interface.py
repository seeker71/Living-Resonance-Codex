#!/usr/bin/env python3
"""
Living Codex Platform - Unified Web Interface

This module implements the Living Codex principle: "Everything is just nodes"
where the unified web interface and user experience system is represented as nodes that can:

1. Manage web interfaces and create interface nodes
2. Handle user experiences and create experience nodes
3. Coordinate discovery engines and create discovery nodes
4. Manage navigation systems and create navigation nodes
5. Handle contribution systems and create contribution nodes

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Unified Web Interface represents the CRYSTAL layer (User Interface) state in the programming language ontology.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
import random
from typing import List, Dict, Any, Optional
import hashlib
import mimetypes

# Import our platform components
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.web_platform.user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle
)
from src.web_platform.contribution_system import (
    ContributionSystem, ContributionType, ContentCategory, ContributionStatus
)
from src.web_platform.ontology_navigator import ontology_navigator
from src.core.generic_node_system import GenericNode
from src.core.shared_node_system import SharedNodeSystem

app = Flask(__name__)
app.secret_key = 'living-codex-secret-key-2024'  # In production, use environment variable

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize our systems
user_system = UserManagementSystem()
contribution_system = ContributionSystem()

class WebPlatformNodeSystem(SharedNodeSystem):
    """
    Web Platform System using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Web interfaces are nodes
    - User experiences are nodes
    - Discovery engines are nodes
    - Navigation systems are nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The Web Platform represents the CRYSTAL layer (User Interface) state in the programming language ontology:
    - User interface management, experience coordination, discovery engine operations
    - Navigation system management, contribution system coordination, web asset management
    - Interface templates, user interactions, platform analytics, system monitoring
    - Web platform evolution, interface optimization, user experience enhancement
    - Cross-platform integration, responsive design, accessibility management
    """
    
    def __init__(self):
        super().__init__("WebPlatformNodeSystem")
        
        # Enhanced user storage with discovery features
        self.users = {}
        self.contributions = {}
        self.user_connections = {}  # User-to-user connections
        self.content_tags = {}      # Content tagging system
        self.exploration_paths = {} # User exploration history
        
        # Digital asset store
        self.assets_dir = Path(__file__).parent / 'assets_store'
        self.assets_dir.mkdir(exist_ok=True)
        self.assets_index_path = self.assets_dir / 'assets_index.json'
        try:
            if self.assets_index_path.exists():
                with open(self.assets_index_path, 'r', encoding='utf-8') as f:
                    self.assets_index = json.load(f)
            else:
                self.assets_index = []
        except Exception:
            self.assets_index = []
        
        # Initialize the web platform system nodes
        self._initialize_web_platform_system_nodes()
        
        print(f"✅ WebPlatformNodeSystem initialized with {len(self.storage.get_all_nodes())} foundation nodes")
    
    def _initialize_web_platform_system_nodes(self):
        """
        Initialize web platform system nodes - the foundation of the user interface system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root web platform system node
        root_node = self.create_node(
            node_type='web_platform_system_root',
            name='Web Platform System Root',
            content='This is the root node of the Web Platform System. It represents the structured, reflective user interface layer for all Living Codex web platform and user experience operations.',
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,  # User Interface
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 1.0,
                'epistemic_label': 'user_interface',
                'system_principle': 'Everything is just nodes - web interfaces as crystalline nodes',
                'meta_circular': True,
                'programming_ontology_layer': 'crystal_user_interface',
                'description': 'Structured, reflective user interface layer for web platform and user experience'
            }
        )
        
        # Create the Web Interface node
        web_interface_node = self.create_node(
            node_type='web_interface',
            name='Web Interface - Interface Blueprint',
            content='Web Interface represents the interface blueprint - defines how web interfaces are created and managed',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 0.95,
                'epistemic_label': 'user_interface',
                'programming_ontology_layer': 'crystal_user_interface',
                'description': 'Interface blueprint for web interface creation and management'
            }
        )
        
        # Create the User Experience node
        user_experience_node = self.create_node(
            node_type='user_experience',
            name='User Experience - Experience Blueprint',
            content='User Experience represents the experience blueprint - defines how user experiences are coordinated',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 0.95,
                'epistemic_label': 'user_interface',
                'programming_ontology_layer': 'crystal_user_interface',
                'description': 'Experience blueprint for user experience coordination'
            }
        )
        
        # Create the Discovery Engine node
        discovery_engine_node = self.create_node(
            node_type='discovery_engine',
            name='Discovery Engine - Discovery Blueprint',
            content='Discovery Engine represents the discovery blueprint - defines how discovery engines operate',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 0.9,
                'epistemic_label': 'user_interface',
                'programming_ontology_layer': 'crystal_user_interface',
                'description': 'Discovery blueprint for discovery engine operations'
            }
        )
        
        # Create the Navigation System node
        navigation_system_node = self.create_node(
            node_type='navigation_system',
            name='Navigation System - Navigation Blueprint',
            content='Navigation System represents the navigation blueprint - defines how navigation systems are managed',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 0.9,
                'epistemic_label': 'user_interface',
                'programming_ontology_layer': 'crystal_user_interface',
                'description': 'Navigation blueprint for navigation system management'
            }
        )
        
        # Create the Contribution System node
        contribution_system_node = self.create_node(
            node_type='contribution_system',
            name='Contribution System - Contribution Blueprint',
            content='Contribution System represents the contribution blueprint - defines how contribution systems are coordinated',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 0.85,
                'epistemic_label': 'user_interface',
                'programming_ontology_layer': 'crystal_user_interface',
                'description': 'Contribution blueprint for contribution system coordination'
            }
        )
        
        print(f"🌟 Web Platform System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"🌐 Web Interface: {web_interface_node.name} (ID: {web_interface_node.node_id})")
        print(f"👤 User Experience: {user_experience_node.name} (ID: {user_experience_node.node_id})")
        print(f"🔍 Discovery Engine: {discovery_engine_node.name} (ID: {discovery_engine_node.node_id})")
        print(f"🧭 Navigation System: {navigation_system_node.name} (ID: {navigation_system_node.node_id})")
        print(f"📝 Contribution System: {contribution_system_node.name} (ID: {contribution_system_node.node_id})")
    
    def save_assets_index(self):
        """Save the assets index to file"""
        try:
            with open(self.assets_index_path, 'w', encoding='utf-8') as f:
                json.dump(self.assets_index, f, ensure_ascii=False, indent=2, default=str)
        except Exception as e:
            print(f"Failed to save assets index: {e}")
    
    def hash_file(self, path: Path) -> str:
        """Generate hash for a file"""
        sha256 = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def detect_asset_type(self, path: Path) -> str:
        """Detect the type of an asset file"""
        mime, _ = mimetypes.guess_type(str(path))
        if not mime:
            return 'other'
        if mime.startswith('image/'):
            return 'image'
        if mime.startswith('video/'):
            return 'video'
        if mime.startswith('audio/'):
            return 'audio'
        if mime in ('application/pdf', 'text/plain', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
            return 'document'
        if mime in ('application/zip', 'application/x-tar', 'application/x-7z-compressed', 'application/x-rar-compressed', 'application/gzip'):
            return 'archive'
        if mime in ('text/x-python', 'application/javascript', 'text/markdown', 'text/x-c', 'text/x-java-source'):
            return 'code'
        if mime in ('text/csv', 'application/json', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
            return 'data'
        return 'other'
    
    def find_asset(self, asset_id: str) -> Optional[Dict[str, Any]]:
        """Find an asset by ID or checksum"""
        for a in self.assets_index:
            if a['id'] == asset_id or a['checksum'].startswith(asset_id):
                return a
        return None
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        web_platform_nodes = [node for node in self.storage.get_all_nodes().values() if node.metadata.get('programming_ontology_layer') == 'crystal_user_interface']
        web_interfaces = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'web_interface']
        user_experiences = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'user_experience']
        discovery_engines = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'discovery_engine']
        navigation_systems = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'navigation_system']
        contribution_systems = [node for node in self.storage.get_all_nodes().values() if node.node_type == 'contribution_system']
        
        return {
            'total_nodes': len(self.storage.get_all_nodes()),
            'web_platform_nodes': len(web_platform_nodes),
            'web_interfaces': len(web_interfaces),
            'user_experiences': len(user_experiences),
            'discovery_engines': len(discovery_engines),
            'navigation_systems': len(navigation_systems),
            'contribution_systems': len(contribution_systems),
            'water_states': list(set(node.get_water_state() for node in self.storage.get_all_nodes().values())),
            'chakras': list(set(node.get_chakra() for node in self.storage.get_all_nodes().values())),
            'frequencies': list(set(node.get_frequency() for node in self.storage.get_all_nodes().values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.storage.get_all_nodes().values()) / max(len(self.storage.get_all_nodes()), 1),
            'system_principle': 'Everything is just nodes - web interfaces as crystalline nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'crystal_user_interface_layer'
        }

# Legacy compatibility - maintain the old interface for now
class WebPlatformSystem(WebPlatformNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self):
        super().__init__()
        print("🔄 WebPlatformSystem initialized with new node-based system")
        print("✨ This system now embodies Living Codex principles")
        print("🌟 Everything is just nodes - web interfaces as crystalline nodes")
        print("💎 Web platform system represents CRYSTAL (User Interface) state in programming language ontology")

# Initialize the web platform system
web_platform_system = WebPlatformSystem()

class WebUser(UserMixin):
    """Enhanced web user class for Flask-Login"""
    def __init__(self, user_id, profile):
        self.id = user_id
        self.profile = profile
        self.last_active = datetime.now()
        self.exploration_score = 0
        self.collaboration_count = 0

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    if user_id in web_platform_system.users:
        return WebUser(user_id, web_platform_system.users[user_id])
    return None

# ============================================================================
# MODULE 1: DISCOVERY ENGINE
# ============================================================================

class DiscoveryEngine:
    """Engine for discovering users, content, and opportunities"""
    
    @staticmethod
    def find_similar_users(user_profile: UserProfile, limit: int = 10) -> List[Dict]:
        """Find users with similar interests, skills, or location"""
        similar_users = []
        
        for user_id, profile in web_platform_system.users.items():
            if user_id == current_user.id:
                continue
                
            similarity_score = 0
            
            # Interest similarity
            if profile.interests and user_profile.interests:
                common_interests = set(profile.interests.primary_domains) & set(user_profile.interests.primary_domains)
                similarity_score += len(common_interests) * 10
            
            # Skill similarity
            if profile.technical and user_profile.technical:
                for skill in ['programming', 'data_analysis', 'design', 'research']:
                    if (skill in profile.technical.skill_levels and 
                        skill in user_profile.technical.skill_levels):
                        if profile.technical.skill_levels[skill] == user_profile.technical.skill_levels[skill]:
                            similarity_score += 5
            
            # Location similarity
            if profile.location and user_profile.location:
                if profile.location.geographic_location == user_profile.location.geographic_location:
                    similarity_score += 15
            
            if similarity_score > 0:
                similar_users.append({
                    'user_id': user_id,
                    'profile': profile,
                    'similarity_score': similarity_score,
                    'common_interests': list(common_interests) if 'common_interests' in locals() else []
                })
        
        # Sort by similarity and return top matches
        similar_users.sort(key=lambda x: x['similarity_score'], reverse=True)
        return similar_users[:limit]
    
    @staticmethod
    def find_relevant_content(user_profile: UserProfile, limit: int = 20) -> List[Dict]:
        """Find content relevant to user's interests and skills"""
        relevant_content = []
        
        for contrib_id, contribution in web_platform_system.contributions.items():
            relevance_score = 0
            
            # Category relevance
            if contribution.get('category') in user_profile.interests.primary_domains:
                relevance_score += 20
            
            # Skill level relevance
            if contribution.get('skill_level'):
                user_skill = user_profile.technical.skill_levels.get('programming', SkillLevel.BEGINNER)
                if contribution['skill_level'] == user_skill:
                    relevance_score += 15
            
            # Language relevance
            if contribution.get('language') in user_profile.technical.preferred_tools:
                relevance_score += 10
            
            if relevance_score > 0:
                relevant_content.append({
                    'contribution_id': contrib_id,
                    'contribution': contribution,
                    'relevance_score': relevance_score,
                    'author': web_platform_system.users.get(contribution.get('user_id', ''), {}).get('name', 'Unknown')
                })
        
        # Sort by relevance and return top matches
        relevant_content.sort(key=lambda x: x['relevance_score'], reverse=True)
        return relevant_content[:limit]

# ============================================================================
# MODULE 2: NAVIGATION SYSTEM
# ============================================================================

class NavigationSystem:
    """System for navigating the Living Codex platform"""
    
    @staticmethod
    def get_exploration_paths(user_id: str) -> List[Dict]:
        """Get personalized exploration paths for the user"""
        user_profile = web_platform_system.users.get(user_id, {})
        
        paths = [
            {
                'id': 'skill_growth',
                'title': '🚀 Skill Growth Path',
                'description': 'Follow a learning path based on your current skills',
                'steps': [
                    'Complete skill assessment',
                    'Choose learning modules',
                    'Practice with projects',
                    'Collaborate with peers',
                    'Share your knowledge'
                ],
                'difficulty': 'Beginner to Advanced',
                'estimated_time': '2-6 months'
            },
            {
                'id': 'community_building',
                'title': '🌍 Community Building',
                'description': 'Connect with like-minded individuals and build communities',
                'steps': [
                    'Find similar users',
                    'Join interest groups',
                    'Participate in discussions',
                    'Organize events',
                    'Mentor others'
                ],
                'difficulty': 'All Levels',
                'estimated_time': 'Ongoing'
            },
            {
                'id': 'local_impact',
                'title': '🏘️ Local Impact Projects',
                'description': 'Create solutions for your local community',
                'steps': [
                    'Identify local challenges',
                    'Research existing solutions',
                    'Design your approach',
                    'Implement and test',
                    'Share results globally'
                ],
                'difficulty': 'Intermediate to Advanced',
                'estimated_time': '3-12 months'
            }
        ]
        
        return paths
    
    @staticmethod
    def get_system_overview() -> Dict:
        """Get an overview of the Living Codex system"""
        return {
            'total_users': len(web_platform_system.users),
            'total_contributions': len(web_platform_system.contributions),
            'active_communities': len(set([c.get('category', '') for c in web_platform_system.contributions.values()])),
            'recent_activity': len([c for c in web_platform_system.contributions.values() 
                                  if datetime.now() - c.get('created_at', datetime.now()) < timedelta(days=7)]),
            'top_categories': sorted(
                [(cat, len([c for c in web_platform_system.contributions.values() if c.get('category') == cat])) 
                 for cat in set([c.get('category', '') for c in web_platform_system.contributions.values() if c.get('category')])],
                key=lambda x: x[1], reverse=True
            )[:5]
        }

# ============================================================================
# MODULE 3: CONTRIBUTION SYSTEM
# ============================================================================

class ContributionManager:
    """Enhanced contribution management system"""
    
    @staticmethod
    def create_contribution(user_id: str, data: Dict) -> Dict:
        """Create a new contribution"""
        contrib_id = f"contrib_{len(web_platform_system.contributions) + 1}"
        
        contribution_data = {
            'contribution_id': contrib_id,
            'user_id': user_id,
            'title': data.get('title', 'Untitled'),
            'description': data.get('description', ''),
            'category': data.get('category', 'General'),
            'contribution_type': data.get('contribution_type', 'knowledge'),
            'skill_level': data.get('skill_level', 'all'),
            'language': data.get('language', ''),
            'created_at': datetime.now(),
            'tags': data.get('tags', []),
            'visibility': data.get('visibility', 'public')
        }
        
        web_platform_system.contributions[contrib_id] = contribution_data
        
        # Create contribution node
        web_platform_system.create_node(
            node_type='contribution_instance',
            name=f"Contribution: {contribution_data['title']}",
            content=f'Contribution instance: {contribution_data["title"]} by user {user_id}',
            metadata={
                'water_state': 'crystal',
                'fractal_layer': 7,
                'chakra': 'crown',
                'frequency': 1185,
                'color': '#E6E6FA',
                'planet': 'Saturn',
                'consciousness_mode': 'Unity, Transcendence',
                'quantum_state': 'crystalline',
                'resonance_score': 0.9,
                'epistemic_label': 'user_interface',
                'programming_ontology_layer': 'crystal_user_interface',
                'contribution_data': contribution_data,
                'created_at': datetime.now().isoformat()
            }
        )
        
        return contribution_data

# ============================================================================
# FLASK ROUTES
# ============================================================================

@app.route('/')
def index():
    """Main page"""
    return render_template('unified_index.html')

@app.route('/api/assets/download/<asset_id>')
def download_asset(asset_id):
    """Download an asset"""
    asset = web_platform_system.find_asset(asset_id)
    if not asset:
        abort(404)
    
    asset_path = web_platform_system.assets_dir / asset['filename']
    if not asset_path.exists():
        abort(404)
    
    return send_from_directory(web_platform_system.assets_dir, asset['filename'])

@app.route('/api/system/resonance')
def get_system_resonance():
    """Get system resonance information"""
    return jsonify(web_platform_system.get_system_resonance())

# ============================================================================
# TEMPLATE CREATION
# ============================================================================

def create_unified_templates():
    """Create the unified HTML templates"""
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    # Unified index template
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Living Codex - Unified Platform</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        h1 { color: #4CAF50; text-align: center; font-size: 2.5em; margin-bottom: 30px; }
        .hero { text-align: center; margin: 40px 0; }
        .hero h2 { color: #81C784; font-size: 1.8em; margin-bottom: 20px; }
        .hero p { font-size: 1.2em; line-height: 1.6; margin-bottom: 30px; }
        .btn { 
            display: inline-block; 
            padding: 12px 24px; 
            margin: 10px; 
            background: linear-gradient(45deg, #4CAF50, #45a049); 
            color: white; 
            text-decoration: none; 
            border-radius: 25px; 
            font-weight: bold; 
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
        }
        .btn:hover { 
            transform: translateY(-2px); 
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
        }
        .btn-secondary { 
            background: linear-gradient(45deg, #2196F3, #1976D2);
            box-shadow: 0 4px 15px rgba(33, 150, 243, 0.3);
        }
        .btn-secondary:hover { 
            box-shadow: 0 6px 20px rgba(33, 150, 243, 0.4);
        }
        .features { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
            gap: 30px; 
            margin: 40px 0; 
        }
        .feature { 
            background: rgba(255,255,255,0.05); 
            padding: 30px; 
            border-radius: 15px; 
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            transition: transform 0.3s ease;
        }
        .feature:hover { transform: translateY(-5px); }
        .feature h3 { color: #4CAF50; margin-bottom: 15px; }
        .ontology-section { 
            background: rgba(255,255,255,0.1); 
            padding: 30px; 
            border-radius: 15px; 
            margin: 40px 0; 
            backdrop-filter: blur(10px); 
            text-align: center; 
        }
        .ontology-section h2 { color: #4CAF50; margin-bottom: 20px; }
        .ontology-section p { margin-bottom: 25px; font-size: 1.1em; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>🌟 Living Codex</h1>
            <h2>Unified Intelligent Platform</h2>
            <p>Experience the future of knowledge, collaboration, and intelligent systems in one unified platform.</p>
            <a href="/ontology" class="btn">Explore Ontology</a>
            <a href="/assets" class="btn btn-secondary">Digital Assets</a>
        </div>
        
        <div class="features">
            <div class="feature">
                <h3>🧠 Intelligent Discovery</h3>
                <p>AI-powered discovery engine that connects you with relevant knowledge, users, and opportunities.</p>
            </div>
            <div class="feature">
                <h3>🧭 Personalized Navigation</h3>
                <p>Intelligent navigation system that adapts to your learning style and goals.</p>
            </div>
            <div class="feature">
                <h3>🌍 Global Collaboration</h3>
                <p>Connect with like-minded individuals and build meaningful collaborations across the globe.</p>
            </div>
            <div class="feature">
                <h3>📊 Progress Tracking</h3>
                <p>Monitor your learning journey, contributions, and connections with detailed analytics.</p>
            </div>
        </div>
        
        <div class="ontology-section">
            <h2>🏗️ System Architecture & Ontology</h2>
            <p>Explore the Living Codex system components, understand relationships, and navigate the knowledge structure</p>
            <a href="/ontology" class="btn btn-primary">Explore Ontology</a>
            <a href="/ontology/architecture" class="btn btn-secondary">View Architecture</a>
            <a href="/ontology/search" class="btn btn-secondary">Search Components</a>
        </div>
    </div>
</body>
</html>"""
    
    # Save the template
    with open(templates_dir / 'unified_index.html', 'w') as f:
        f.write(index_html)
    
    # Unified assets template
    assets_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assets - Living Codex</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #111; color: #eee; }
        .container { max-width: 1000px; margin: 0 auto; }
        h1 { color: #4CAF50; }
        .card { background: #1b1b1b; padding: 20px; border-radius: 10px; margin: 15px 0; }
        input, select { padding: 8px; border-radius: 6px; border: 1px solid #333; background: #222; color: #eee; }
        .btn { padding: 10px 16px; border-radius: 6px; border: none; background: #4CAF50; color: white; cursor: pointer; }
        .btn:hover { opacity: 0.9; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border-bottom: 1px solid #333; padding: 8px; text-align: left; }
        small { color: #aaa; }
        .msg { padding: 10px; border-radius: 6px; margin-bottom: 15px; }
        .success { background: #124d2a; }
        .error { background: #4d1212; }
    </style>
    </head>
<body>
 <div class="container">
  <h1>📁 Digital Assets</h1>
  {% if message %}
    <div class="msg {{ message[0] }}">{{ message[1] }}</div>
  {% endif %}
  <div class="card">
    <h3>Upload Asset</h3>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file" required> 
      <select name="type">
        <option value="">auto-detect</option>
        <option>image</option><option>video</option><option>audio</option>
        <option>document</option><option>archive</option><option>code</option><option>data</option>
      </select>
      <input type="text" name="tags" placeholder="tags (comma separated)">
      <button class="btn" type="submit">Upload</button>
    </form>
  </div>
  <div class="card">
    <h3>Assets List</h3>
    <table>
      <thead><tr><th>ID</th><th>Name</th><th>Type</th><th>Size</th><th>Actions</th></tr></thead>
      <tbody>
      {% for a in assets %}
        <tr>
          <td><small>{{ a.id[:12] }}…</small></td>
          <td>{{ a.original_name }}</td>
          <td>{{ a.type }}</td>
          <td>{{ a.size }}</td>
          <td><a class="btn" href="/api/assets/download/{{ a.id }}">Download</a></td>
        </tr>
      {% endfor %}
      </tbody>
    </table>
  </div>
 </div>
</body>
</html>"""
    with open(templates_dir / 'unified_assets.html', 'w') as f:
        f.write(assets_html)
    
    print("✅ Unified templates created successfully!")

if __name__ == '__main__':
    print("🌐 Starting Unified Living Codex Platform...")
    print("   Open your browser to: http://localhost:5004")
    print("   All features combined in one modular system!")
    
    # Create templates
    create_unified_templates()
    
    app.run(debug=False, host='0.0.0.0', port=5004)
