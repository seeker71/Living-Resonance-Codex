#!/usr/bin/env python3
"""
Living Codex Platform - Enhanced Web Interface
Advanced Flask-based web interface with discovery, navigation, and collaboration features
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
import random
from typing import List, Dict, Any, Optional

# Import our platform components
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.platform.user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle
)
from src.platform.contribution_system import (
    ContributionSystem, ContributionType, ContentCategory, ContributionStatus
)

app = Flask(__name__)
app.secret_key = 'living-codex-secret-key-2024'  # In production, use environment variable

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize our systems
user_system = UserManagementSystem()
contribution_system = ContributionSystem()

# Enhanced user storage with discovery features
users = {}
contributions = {}
user_connections = {}  # User-to-user connections
content_tags = {}      # Content tagging system
exploration_paths = {} # User exploration history

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
    if user_id in users:
        return WebUser(user_id, users[user_id])
    return None

# ============================================================================
# DISCOVERY & NAVIGATION FEATURES
# ============================================================================

class DiscoveryEngine:
    """Engine for discovering users, content, and opportunities"""
    
    @staticmethod
    def find_similar_users(user_profile: UserProfile, limit: int = 10) -> List[Dict]:
        """Find users with similar interests, skills, or location"""
        similar_users = []
        
        for user_id, profile in users.items():
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
        
        for contrib_id, contribution in contributions.items():
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
                    'author': users.get(contribution.get('user_id', ''), {}).get('name', 'Unknown')
                })
        
        # Sort by relevance and return top matches
        relevant_content.sort(key=lambda x: x['relevance_score'], reverse=True)
        return relevant_content[:limit]

class NavigationSystem:
    """System for navigating the Living Codex platform"""
    
    @staticmethod
    def get_exploration_paths(user_id: str) -> List[Dict]:
        """Get personalized exploration paths for the user"""
        user_profile = users.get(user_id, {})
        
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
            'total_users': len(users),
            'total_contributions': len(contributions),
            'active_communities': len(set([c.get('category', '') for c in contributions.values()])),
            'recent_activity': len([c for c in contributions.values() 
                                  if datetime.now() - c.get('created_at', datetime.now()) < timedelta(days=7)]),
            'top_categories': sorted(
                [(cat, len([c for c in contributions.values() if c.get('category') == cat])) 
                 for cat in set([c.get('category', '') for c in contributions.values() if c.get('category')])],
                key=lambda x: x[1], reverse=True
            )[:5]
        }

# ============================================================================
# ENHANCED ROUTES
# ============================================================================

@app.route('/')
def index():
    """Enhanced home page with discovery features"""
    system_overview = NavigationSystem.get_system_overview()
    recent_contributions = list(contributions.values())[-5:] if contributions else []
    
    return render_template('enhanced_index.html', 
                         system_overview=system_overview,
                         recent_contributions=recent_contributions)

@app.route('/discover')
@login_required
def discover():
    """Discovery hub for finding users and content"""
    user_profile = current_user.profile
    
    # Find similar users
    similar_users = DiscoveryEngine.find_similar_users(user_profile, limit=8)
    
    # Find relevant content
    relevant_content = DiscoveryEngine.find_relevant_content(user_profile, limit=12)
    
    # Get exploration paths
    exploration_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    return render_template('discover.html',
                         similar_users=similar_users,
                         relevant_content=relevant_content,
                         exploration_paths=exploration_paths)

@app.route('/explore/<path:category>')
@login_required
def explore_category(category):
    """Explore content by category"""
    category_content = [c for c in contributions.values() if c.get('category') == category]
    
    if not category_content:
        abort(404)
    
    # Find users interested in this category
    interested_users = [u for u in users.values() 
                       if category in u.get('interests', {}).get('primary_domains', [])]
    
    return render_template('explore_category.html',
                         category=category,
                         content=category_content,
                         interested_users=interested_users)

@app.route('/navigate')
@login_required
def navigate():
    """System navigation hub"""
    system_overview = NavigationSystem.get_system_overview()
    user_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    # Get user's current progress
    user_progress = {
        'contributions_made': len([c for c in contributions.values() if c.get('user_id') == current_user.id]),
        'connections_made': len(user_connections.get(current_user.id, [])),
        'exploration_score': current_user.exploration_score,
        'collaboration_count': current_user.collaboration_count
    }
    
    return render_template('navigate.html',
                         system_overview=system_overview,
                         user_paths=user_paths,
                         user_progress=user_progress)

@app.route('/connect/<user_id>')
@login_required
def connect_with_user(user_id):
    """Connect with another user"""
    if user_id == current_user.id:
        flash('You cannot connect with yourself!', 'error')
        return redirect(url_for('discover'))
    
    if user_id not in users:
        abort(404)
    
    # Initialize connections if not exists
    if current_user.id not in user_connections:
        user_connections[current_user.id] = []
    
    if user_id not in user_connections[current_user.id]:
        user_connections[current_user.id].append(user_id)
        current_user.collaboration_count += 1
        flash(f'Connected with {users[user_id].get("name", "User")}!', 'success')
    else:
        flash('Already connected!', 'info')
    
    return redirect(url_for('discover'))

@app.route('/api/discovery/similar_users')
@login_required
def api_similar_users():
    """API endpoint for finding similar users"""
    limit = request.args.get('limit', 10, type=int)
    similar_users = DiscoveryEngine.find_similar_users(current_user.profile, limit)
    
    # Format for API response
    formatted_users = []
    for user_data in similar_users:
        user = user_data['profile']
        formatted_users.append({
            'user_id': user_data['user_id'],
            'name': user.get('name', 'Unknown'),
            'similarity_score': user_data['similarity_score'],
            'common_interests': user_data['common_interests'],
            'skills': user.get('technical', {}).get('skill_levels', {}),
            'location': user.get('location', {}).get('geographic_location', 'Unknown')
        })
    
    return jsonify(formatted_users)

@app.route('/api/discovery/relevant_content')
@login_required
def api_relevant_content():
    """API endpoint for finding relevant content"""
    limit = request.args.get('limit', 20, type=int)
    relevant_content = DiscoveryEngine.find_relevant_content(current_user.profile, limit)
    
    # Format for API response
    formatted_content = []
    for content_data in relevant_content:
        content = content_data['contribution']
        formatted_content.append({
            'contribution_id': content_data['contribution_id'],
            'title': content.get('title', 'Untitled'),
            'category': content.get('category', 'General'),
            'relevance_score': content_data['relevance_score'],
            'author': content_data['author'],
            'created_at': content.get('created_at', '').isoformat() if content.get('created_at') else '',
            'skill_level': content.get('skill_level', 'All Levels')
        })
    
    return jsonify(formatted_content)

@app.route('/api/navigation/system_overview')
def api_system_overview():
    """API endpoint for system overview"""
    return jsonify(NavigationSystem.get_system_overview())

@app.route('/api/navigation/exploration_paths')
@login_required
def api_exploration_paths():
    """API endpoint for user exploration paths"""
    return jsonify(NavigationSystem.get_exploration_paths(current_user.id))

# ============================================================================
# EXISTING ROUTES (Enhanced)
# ============================================================================

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Enhanced user registration with discovery preferences"""
    if request.method == 'POST':
        try:
            # Get form data (existing logic)
            user_data = {
                'identity': {
                    'name': request.form['name'],
                    'pronouns': request.form.get('pronouns'),
                    'cultural_background': request.form.get('cultural_background'),
                    'belief_system': request.form.get('belief_system')
                },
                'communication': {
                    'primary_language': request.form['primary_language'],
                    'secondary_languages': request.form.get('secondary_languages', '').split(',') if request.form.get('secondary_languages') else [],
                    'communication_style': CommunicationStyle(request.form.get('communication_style', 'casual')),
                    'learning_style': LearningStyle(request.form.get('learning_style', 'reading'))
                },
                'technical': {
                    'skill_levels': {
                        'programming': SkillLevel(request.form.get('programming_skill', 'beginner')),
                        'data_analysis': SkillLevel(request.form.get('data_skill', 'beginner')),
                        'design': SkillLevel(request.form.get('design_skill', 'beginner')),
                        'research': SkillLevel(request.form.get('research_skill', 'beginner'))
                    },
                    'learning_path': request.form.get('learning_path', '').split(',') if request.form.get('learning_path') else [],
                    'preferred_tools': request.form.get('preferred_tools', '').split(',') if request.form.get('preferred_tools') else []
                },
                'interests': {
                    'primary_domains': request.form.get('primary_domains', '').split(',') if request.form.get('primary_domains') else [],
                    'specific_topics': request.form.get('specific_topics', '').split(',') if request.form.get('specific_topics') else [],
                    'passion_areas': request.form.get('passion_areas', '').split(',') if request.form.get('passion_areas') else []
                },
                'location': {
                    'geographic_location': request.form['location'],
                    'timezone': request.form.get('timezone', 'UTC'),
                    'cultural_context': request.form.get('cultural_context')
                }
            }
            
            # Create user profile
            user_profile = user_system.create_user_profile(user_data)
            if user_profile:
                user_id = f"user_{len(users) + 1}"
                users[user_id] = user_profile
                
                # Initialize user connections and exploration data
                user_connections[user_id] = []
                exploration_paths[user_id] = []
                
                flash('Profile created successfully! You can now sign in.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Failed to create profile. Please try again.', 'error')
                
        except Exception as e:
            flash(f'Error creating profile: {str(e)}', 'error')
    
    return render_template('enhanced_signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Enhanced login with discovery features"""
    if request.method == 'POST':
        user_id = request.form['user_id']
        
        if user_id in users:
            user = WebUser(user_id, users[user_id])
            login_user(user)
            
            # Update user activity
            user.last_active = datetime.now()
            
            flash('Welcome back! Explore the Living Codex platform.', 'success')
            return redirect(url_for('discover'))
        else:
            flash('User not found. Please check your ID or sign up.', 'error')
    
    return render_template('enhanced_login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Enhanced dashboard with discovery insights"""
    user_profile = current_user.profile
    
    # Get personalized insights
    similar_users = DiscoveryEngine.find_similar_users(user_profile, limit=5)
    relevant_content = DiscoveryEngine.find_relevant_content(user_profile, limit=8)
    
    # Get user's contributions
    user_contributions = [c for c in contributions.values() if c.get('user_id') == current_user.id]
    
    # Get exploration paths
    exploration_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    return render_template('enhanced_dashboard.html',
                         user_profile=user_profile,
                         similar_users=similar_users,
                         relevant_content=relevant_content,
                         user_contributions=user_contributions,
                         exploration_paths=exploration_paths)

@app.route('/contribute', methods=['GET', 'POST'])
@login_required
def contribute():
    """Enhanced contribution system with discovery features"""
    if request.method == 'POST':
        try:
            contribution_data = {
                'user_id': current_user.id,
                'title': request.form['title'],
                'description': request.form['description'],
                'category': request.form['category'],
                'contribution_type': request.form['contribution_type'],
                'skill_level': request.form.get('skill_level', 'all'),
                'language': request.form.get('code_language'),
                'created_at': datetime.now()
            }
            
            # Add to contributions
            contrib_id = f"contrib_{len(contributions) + 1}"
            contributions[contrib_id] = contribution_data
            
            # Update user exploration score
            current_user.exploration_score += 10
            
            flash('Contribution created successfully!', 'success')
            return redirect(url_for('dashboard'))
            
        except Exception as e:
            flash(f'Error creating contribution: {str(e)}', 'error')
    
    return render_template('enhanced_contribute.html')

@app.route('/profile')
@login_required
def profile():
    """Enhanced user profile with discovery insights"""
    user_profile = current_user.profile
    
    # Get user's network
    connections = user_connections.get(current_user.id, [])
    connected_users = [users.get(uid, {}) for uid in connections if uid in users]
    
    # Get user's exploration history
    user_exploration = exploration_paths.get(current_user.id, [])
    
    return render_template('enhanced_profile.html',
                         user_profile=user_profile,
                         connected_users=connected_users,
                         exploration_history=user_exploration)

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

# ============================================================================
# TEMPLATE CREATION
# ============================================================================

def create_enhanced_templates():
    """Create enhanced HTML templates for the web interface"""
    
    # Enhanced index template
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Living Codex Platform - Discovery & Navigation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .container { max-width: 1200px; margin: 0 auto; }
        .hero { text-align: center; padding: 60px 20px; }
        .hero h1 { font-size: 3em; margin-bottom: 20px; }
        .hero p { font-size: 1.2em; margin-bottom: 30px; }
        .cta-buttons { display: flex; gap: 20px; justify-content: center; }
        .btn { padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: bold; transition: all 0.3s; }
        .btn-primary { background: #4CAF50; color: white; }
        .btn-secondary { background: transparent; color: white; border: 2px solid white; }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
        
        .system-overview { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 40px 0; }
        .overview-card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; text-align: center; backdrop-filter: blur(10px); }
        .overview-card h3 { color: #4CAF50; margin-bottom: 10px; }
        .overview-card .number { font-size: 2em; font-weight: bold; color: #4CAF50; }
        
        .recent-content { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; margin: 40px 0; backdrop-filter: blur(10px); }
        .content-item { background: rgba(255,255,255,0.05); padding: 15px; margin: 10px 0; border-radius: 10px; }
        
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 60px; }
        .feature { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; backdrop-filter: blur(10px); }
        .feature h3 { color: #4CAF50; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>🌟 Living Codex Platform</h1>
            <p>Discover, Navigate, and Collaborate in a World of Knowledge</p>
            <div class="cta-buttons">
                <a href="/signup" class="btn btn-primary">Join the Platform</a>
                <a href="/login" class="btn btn-secondary">Sign In</a>
            </div>
        </div>
        
        <div class="system-overview">
            <div class="overview-card">
                <h3>👥 Active Users</h3>
                <div class="number">{{ system_overview.total_users }}</div>
            </div>
            <div class="overview-card">
                <h3>💡 Contributions</h3>
                <div class="number">{{ system_overview.total_contributions }}</div>
            </div>
            <div class="overview-card">
                <h3>🌍 Communities</h3>
                <div class="number">{{ system_overview.active_communities }}</div>
            </div>
            <div class="overview-card">
                <h3>🚀 Recent Activity</h3>
                <div class="number">{{ system_overview.recent_activity }}</div>
            </div>
        </div>
        
        <div class="recent-content">
            <h2>🔥 Recent Contributions</h2>
            {% for contribution in recent_contributions %}
            <div class="content-item">
                <h4>{{ contribution.title or 'Untitled' }}</h4>
                <p>{{ contribution.description or 'No description' }}</p>
                <small>Category: {{ contribution.category or 'General' }} | Author: {{ users.get(contribution.user_id, {}).get('name', 'Unknown') }}</small>
            </div>
            {% endfor %}
        </div>
        
        <div class="features">
            <div class="feature">
                <h3>🔍 Smart Discovery</h3>
                <p>Find users and content that match your interests, skills, and goals using AI-powered matching.</p>
            </div>
            <div class="feature">
                <h3>🧭 Intelligent Navigation</h3>
                <p>Follow personalized exploration paths and discover new opportunities in the Living Codex ecosystem.</p>
            </div>
            <div class="feature">
                <h3>🤝 Community Building</h3>
                <p>Connect with like-minded individuals and build meaningful collaborations across the globe.</p>
            </div>
            <div class="feature">
                <h3>📊 Progress Tracking</h3>
                <p>Monitor your learning journey, contributions, and connections with detailed analytics.</p>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    # Save the template
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    with open(templates_dir / 'enhanced_index.html', 'w') as f:
        f.write(index_html)
    
    print(f"✅ Template saved to: {templates_dir / 'enhanced_index.html'}")
    
    print("✅ Enhanced templates created successfully!")

if __name__ == '__main__':
    print("🌐 Starting Enhanced Living Codex Platform...")
    print("   Open your browser to: http://localhost:5003")
    print("   Discover, Navigate, and Collaborate!")
    
    # Create templates
    create_enhanced_templates()
    
    app.run(debug=False, host='0.0.0.0', port=5003)
