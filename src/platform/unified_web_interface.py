#!/usr/bin/env python3
"""
Living Codex Platform - Unified Web Interface
Combines original functionality with enhanced discovery, navigation, and collaboration features
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

from src.platform.user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle
)
from src.platform.contribution_system import (
    ContributionSystem, ContributionType, ContentCategory, ContributionStatus
)
from src.platform.ontology_navigator import ontology_navigator

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

# Digital asset store
assets_dir = Path(__file__).parent / 'assets_store'
assets_dir.mkdir(exist_ok=True)
assets_index_path = assets_dir / 'assets_index.json'
try:
    if assets_index_path.exists():
        with open(assets_index_path, 'r', encoding='utf-8') as f:
            assets_index = json.load(f)
    else:
        assets_index = []
except Exception:
    assets_index = []

def save_assets_index():
    try:
        with open(assets_index_path, 'w', encoding='utf-8') as f:
            json.dump(assets_index, f, ensure_ascii=False, indent=2, default=str)
    except Exception as e:
        print(f"Failed to save assets index: {e}")

def hash_file(path: Path) -> str:
    sha256 = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def detect_asset_type(path: Path) -> str:
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

def find_asset(asset_id: str) -> Optional[Dict[str, Any]]:
    for a in assets_index:
        if a['id'] == asset_id or a['checksum'].startswith(asset_id):
            return a
    return None

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
# MODULE 1: DISCOVERY ENGINE
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

# ============================================================================
# MODULE 2: NAVIGATION SYSTEM
# ============================================================================

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
# MODULE 3: CONTRIBUTION SYSTEM
# ============================================================================

class ContributionManager:
    """Enhanced contribution management system"""
    
    @staticmethod
    def create_contribution(user_id: str, data: Dict) -> Dict:
        """Create a new contribution"""
        contrib_id = f"contrib_{len(contributions) + 1}"
        
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
        
        contributions[contrib_id] = contribution_data
        
        # Update user exploration score
        if user_id in users:
            users[user_id].exploration_score += 10
        
        return contribution_data
    
    @staticmethod
    def get_user_contributions(user_id: str) -> List[Dict]:
        """Get all contributions by a user"""
        return [c for c in contributions.values() if c.get('user_id') == user_id]
    
    @staticmethod
    def get_contributions_by_category(category: str) -> List[Dict]:
        """Get all contributions in a specific category"""
        return [c for c in contributions.values() if c.get('category') == category]

# ============================================================================
# MODULE 4: USER MANAGEMENT
# ============================================================================

class UserManager:
    """Enhanced user management system"""
    
    @staticmethod
    def create_user_profile(user_data: Dict) -> UserProfile:
        """Create a comprehensive user profile"""
        try:
            # Create user profile using the existing system
            user_profile = user_system.create_user_profile(user_data)
            return user_profile
        except Exception as e:
            print(f"Error creating user profile: {e}")
            return None
    
    @staticmethod
    def connect_users(user1_id: str, user2_id: str) -> bool:
        """Connect two users"""
        if user1_id not in user_connections:
            user_connections[user1_id] = []
        
        if user2_id not in user_connections:
            user_connections[user2_id] = []
        
        if user2_id not in user_connections[user1_id]:
            user_connections[user1_id].append(user2_id)
            user_connections[user2_id].append(user1_id)
            
            # Update collaboration counts
            if user1_id in users:
                users[user1_id].collaboration_count += 1
            if user2_id in users:
                users[user2_id].collaboration_count += 1
            
            return True
        return False

# ============================================================================
# UNIFIED ROUTES
# ============================================================================

@app.route('/')
def index():
    """Unified home page with all features"""
    system_overview = NavigationSystem.get_system_overview()
    recent_contributions = list(contributions.values())[-5:] if contributions else []
    
    return render_template('unified_index.html', 
                         system_overview=system_overview,
                         recent_contributions=recent_contributions)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Unified user registration with all profile features"""
    if request.method == 'POST':
        try:
            # Get comprehensive form data
            user_data = {
                'identity': {
                    'name': request.form['name'],
                    'pronouns': request.form.get('pronouns'),
                    'cultural_background': request.form.get('cultural_background'),
                    'belief_system': request.form.get('belief_system'),
                    'life_experience': request.form.get('life_experience')
                },
                'communication': {
                    'primary_language': request.form['primary_language'],
                    'secondary_languages': request.form.get('secondary_languages', '').split(',') if request.form.get('secondary_languages') else [],
                    'communication_style': CommunicationStyle(request.form.get('communication_style', 'casual')),
                    'learning_style': LearningStyle(request.form.get('learning_style', 'reading')),
                    'accessibility_needs': request.form.get('accessibility_needs', '').split(',') if request.form.get('accessibility_needs') else []
                },
                'technical': {
                    'skill_levels': {
                        'programming': SkillLevel(request.form.get('programming_skill', 'beginner')),
                        'data_analysis': SkillLevel(request.form.get('data_skill', 'beginner')),
                        'design': SkillLevel(request.form.get('design_skill', 'beginner')),
                        'research': SkillLevel(request.form.get('research_skill', 'beginner'))
                    },
                    'learning_path': request.form.get('learning_path', '').split(',') if request.form.get('learning_path') else [],
                    'preferred_tools': request.form.get('preferred_tools', '').split(',') if request.form.get('preferred_tools') else [],
                    'contribution_areas': request.form.get('contribution_areas', '').split(',') if request.form.get('contribution_areas') else []
                },
                'interests': {
                    'primary_domains': request.form.get('primary_domains', '').split(',') if request.form.get('primary_domains') else [],
                    'specific_topics': request.form.get('specific_topics', '').split(',') if request.form.get('specific_topics') else [],
                    'expertise_levels': {},
                    'passion_areas': request.form.get('passion_areas', '').split(',') if request.form.get('passion_areas') else []
                },
                'location': {
                    'geographic_location': request.form['location'],
                    'timezone': request.form.get('timezone', 'UTC'),
                    'cultural_context': request.form.get('cultural_context'),
                    'local_challenges': request.form.get('local_challenges', '').split(',') if request.form.get('local_challenges') else [],
                    'local_resources': request.form.get('local_resources', '').split(',') if request.form.get('local_resources') else []
                }
            }
            
            # Create user profile
            user_profile = UserManager.create_user_profile(user_data)
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
    
    return render_template('unified_signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Unified login system"""
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
    
    return render_template('unified_login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Unified dashboard with all features"""
    user_profile = current_user.profile
    
    # Get personalized insights from discovery engine
    similar_users = DiscoveryEngine.find_similar_users(user_profile, limit=5)
    relevant_content = DiscoveryEngine.find_relevant_content(user_profile, limit=8)
    
    # Get user's contributions
    user_contributions = ContributionManager.get_user_contributions(current_user.id)
    
    # Get exploration paths
    exploration_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    return render_template('unified_dashboard.html',
                         user_profile=user_profile,
                         similar_users=similar_users,
                         relevant_content=relevant_content,
                         user_contributions=user_contributions,
                         exploration_paths=exploration_paths)

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
    
    return render_template('unified_discover.html',
                         similar_users=similar_users,
                         relevant_content=relevant_content,
                         exploration_paths=exploration_paths)

@app.route('/navigate')
@login_required
def navigate():
    """System navigation hub"""
    system_overview = NavigationSystem.get_system_overview()
    user_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    # Get user's current progress
    user_progress = {
        'contributions_made': len(ContributionManager.get_user_contributions(current_user.id)),
        'connections_made': len(user_connections.get(current_user.id, [])),
        'exploration_score': current_user.exploration_score,
        'collaboration_count': current_user.collaboration_count
    }
    
    return render_template('unified_navigate.html',
                         system_overview=system_overview,
                         user_paths=user_paths,
                         user_progress=user_progress)

@app.route('/contribute', methods=['GET', 'POST'])
@login_required
def contribute():
    """Unified contribution system"""
    if request.method == 'POST':
        try:
            contribution_data = {
                'title': request.form['title'],
                'description': request.form['description'],
                'category': request.form['category'],
                'contribution_type': request.form['contribution_type'],
                'skill_level': request.form.get('skill_level', 'all'),
                'language': request.form.get('code_language'),
                'tags': request.form.get('tags', '').split(',') if request.form.get('tags') else [],
                'visibility': request.form.get('visibility', 'public')
            }
            
            # Create contribution using the contribution manager
            contribution = ContributionManager.create_contribution(current_user.id, contribution_data)
            
            flash('Contribution created successfully!', 'success')
            return redirect(url_for('dashboard'))
            
        except Exception as e:
            flash(f'Error creating contribution: {str(e)}', 'error')
    
    return render_template('unified_contribute.html')

@app.route('/explore/<path:category>')
@login_required
def explore_category(category):
    """Explore content by category"""
    category_content = ContributionManager.get_contributions_by_category(category)
    
    if not category_content:
        abort(404)
    
    # Find users interested in this category
    interested_users = [u for u in users.values() 
                       if category in u.get('interests', {}).get('primary_domains', [])]
    
    return render_template('unified_explore_category.html',
                         category=category,
                         content=category_content,
                         interested_users=interested_users)

@app.route('/assets', methods=['GET', 'POST'])
@login_required
def assets_page():
    """Assets manager page with upload form and listing"""
    message = None
    if request.method == 'POST':
        try:
            if 'file' not in request.files or request.files['file'].filename == '':
                message = ('error', 'Please choose a file to upload')
            else:
                file = request.files['file']
                tmp_path = assets_dir / f"__upload_{datetime.now().timestamp()}"
                file.save(str(tmp_path))
                checksum = hash_file(tmp_path)
                ext = Path(file.filename).suffix.lstrip('.') or 'bin'
                stored_name = f"{checksum}.{ext}"
                dest = assets_dir / stored_name
                if not dest.exists():
                    tmp_path.rename(dest)
                else:
                    tmp_path.unlink(missing_ok=True)
                asset_type = request.form.get('type') or detect_asset_type(dest)
                tags = [t.strip() for t in request.form.get('tags', '').split(',') if t.strip()]
                meta = find_asset(checksum)
                if meta:
                    meta.update({
                        'original_name': file.filename,
                        'stored_name': stored_name,
                        'size': dest.stat().st_size,
                        'type': asset_type,
                        'tags': sorted(set(meta.get('tags', []) + tags)),
                        'updated_at': datetime.now().isoformat(),
                        'uploader': current_user.id
                    })
                else:
                    meta = {
                        'id': checksum,
                        'checksum': checksum,
                        'original_name': file.filename,
                        'stored_name': stored_name,
                        'size': dest.stat().st_size,
                        'type': asset_type,
                        'tags': tags,
                        'created_at': datetime.now().isoformat(),
                        'uploader': current_user.id
                    }
                    assets_index.append(meta)
                save_assets_index()
                message = ('success', f"Uploaded {file.filename}")
        except Exception as e:
            message = ('error', f"Upload failed: {e}")
    return render_template('unified_assets.html', assets=assets_index, message=message)

@app.route('/connect/<user_id>')
@login_required
def connect_with_user(user_id):
    """Connect with another user"""
    if user_id == current_user.id:
        flash('You cannot connect with yourself!', 'error')
        return redirect(url_for('discover'))
    
    if user_id not in users:
        abort(404)
    
    if UserManager.connect_users(current_user.id, user_id):
        flash(f'Connected with {users[user_id].get("name", "User")}!', 'success')
    else:
        flash('Already connected!', 'info')
    
    return redirect(url_for('discover'))

@app.route('/profile')
@login_required
def profile():
    """Unified user profile with all features"""
    user_profile = current_user.profile
    
    # Get user's network
    connections = user_connections.get(current_user.id, [])
    connected_users = [users.get(uid, {}) for uid in connections if uid in users]
    
    # Get user's exploration history
    user_exploration = exploration_paths.get(current_user.id, [])
    
    return render_template('unified_profile.html',
                         user_profile=user_profile,
                         connected_users=connected_users,
                         exploration_history=user_exploration)

# ============================================================================
# API ENDPOINTS
# ============================================================================

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

@app.route('/api/contributions')
@login_required
def api_contributions():
    """API endpoint for user contributions"""
    contributions = ContributionManager.get_user_contributions(current_user.id)
    return jsonify(contributions)

@app.route('/api/opportunities')
@login_required
def api_opportunities():
    """API endpoint for contribution opportunities"""
    # This would integrate with the existing contribution system
    opportunities = contribution_system.find_opportunities(current_user.profile)
    return jsonify(opportunities)

# ============================================================================
# ASSET API ENDPOINTS
# ============================================================================

@app.route('/api/assets', methods=['GET'])
@login_required
def api_assets_list():
    """List digital assets"""
    return jsonify(assets_index)

@app.route('/api/assets', methods=['POST'])
@login_required
def api_assets_upload():
    """Upload/add a digital asset (multipart form)"""
    if 'file' not in request.files:
        return jsonify({'error': 'file field required'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'empty filename'}), 400
    # Save to temp then hash
    tmp_path = assets_dir / f"__upload_{datetime.now().timestamp()}"
    file.save(str(tmp_path))
    checksum = hash_file(tmp_path)
    ext = Path(file.filename).suffix.lstrip('.') or 'bin'
    stored_name = f"{checksum}.{ext}"
    dest = assets_dir / stored_name
    if not dest.exists():
        tmp_path.rename(dest)
    else:
        tmp_path.unlink(missing_ok=True)
    asset_type = request.form.get('type') or detect_asset_type(dest)
    tags = [t.strip() for t in request.form.get('tags', '').split(',') if t.strip()]
    meta = find_asset(checksum)
    if meta:
        meta.update({
            'original_name': file.filename,
            'stored_name': stored_name,
            'size': dest.stat().st_size,
            'type': asset_type,
            'tags': sorted(set(meta.get('tags', []) + tags)),
            'updated_at': datetime.now().isoformat(),
            'uploader': current_user.id
        })
    else:
        meta = {
            'id': checksum,
            'checksum': checksum,
            'original_name': file.filename,
            'stored_name': stored_name,
            'size': dest.stat().st_size,
            'type': asset_type,
            'tags': tags,
            'created_at': datetime.now().isoformat(),
            'uploader': current_user.id
        }
        assets_index.append(meta)
    save_assets_index()
    return jsonify(meta), 201

@app.route('/api/assets/<asset_id>', methods=['GET'])
@login_required
def api_asset_info(asset_id):
    meta = find_asset(asset_id)
    if not meta:
        return jsonify({'error': 'not found'}), 404
    return jsonify(meta)

@app.route('/api/assets/download/<asset_id>', methods=['GET'])
@login_required
def api_asset_download(asset_id):
    meta = find_asset(asset_id)
    if not meta:
        abort(404)
    stored = assets_dir / meta['stored_name']
    if not stored.exists():
        abort(404)
    return send_from_directory(str(assets_dir), meta['stored_name'], as_attachment=True, download_name=meta['original_name'])

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

# ============================================================================
# ONTOLOGY NAVIGATION ROUTES
# ============================================================================

@app.route('/ontology')
def ontology():
    """Ontology overview and navigation"""
    overview = ontology_navigator.get_ontology_overview()
    architecture = ontology_navigator.get_system_architecture()
    
    return render_template('ontology_overview.html',
                         overview=overview,
                         architecture=architecture)

@app.route('/ontology/category/<category>')
def ontology_category(category):
    """View components in a specific category"""
    if category not in ontology_navigator.categories:
        abort(404)
    
    category_info = ontology_navigator.categories[category]
    components = ontology_navigator.get_nodes_by_category(category)
    
    return render_template('ontology_category.html',
                         category_info=category_info,
                         components=components)

@app.route('/ontology/component/<component_id>')
def ontology_component(component_id):
    """View detailed information about a specific component"""
    component = ontology_navigator.get_node_details(component_id)
    if not component:
        abort(404)
    
    relationships = ontology_navigator.get_node_relationships(component_id)
    
    return render_template('ontology_component.html',
                         component=component,
                         relationships=relationships)

@app.route('/ontology/search')
def ontology_search():
    """Search ontology components"""
    query = request.args.get('q', '')
    results = []
    
    if query:
        results = ontology_navigator.search_nodes(query)
    
    return render_template('ontology_search.html',
                         query=query,
                         results=results)

@app.route('/ontology/architecture')
def ontology_architecture():
    """View system architecture"""
    architecture = ontology_navigator.get_system_architecture()
    
    return render_template('ontology_architecture.html',
                         architecture=architecture)

# ============================================================================
# ONTOLOGY API ENDPOINTS
# ============================================================================

@app.route('/api/ontology/overview')
def api_ontology_overview():
    """API endpoint for ontology overview"""
    return jsonify(ontology_navigator.get_ontology_overview())

@app.route('/api/ontology/categories')
def api_ontology_categories():
    """API endpoint for ontology categories"""
    return jsonify(ontology_navigator.categories)

@app.route('/api/ontology/components')
def api_ontology_components():
    """API endpoint for all ontology components"""
    components = {}
    for node_id, node in ontology_navigator.nodes.items():
        components[node_id] = {
            'id': node.id,
            'name': node.name,
            'type': node.type,
            'description': node.description,
            'category': node.category,
            'metadata': node.metadata
        }
    return jsonify(components)

@app.route('/api/ontology/component/<component_id>')
def api_ontology_component(component_id):
    """API endpoint for specific component details"""
    component = ontology_navigator.get_node_details(component_id)
    if not component:
        abort(404)
    
    return jsonify({
        'id': component.id,
        'name': component.name,
        'type': component.type,
        'description': component.description,
        'category': component.category,
        'relationships': component.relationships,
        'metadata': component.metadata,
        'created_at': component.created_at.isoformat(),
        'updated_at': component.updated_at.isoformat()
    })

@app.route('/api/ontology/search')
def api_ontology_search():
    """API endpoint for ontology search"""
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    results = ontology_navigator.search_nodes(query)
    return jsonify([{
        'id': node.id,
        'name': node.name,
        'type': node.type,
        'description': node.description,
        'category': node.category
    } for node in results])

@app.route('/api/ontology/architecture')
def api_ontology_architecture():
    """API endpoint for system architecture"""
    return jsonify(ontology_navigator.get_system_architecture())

# ============================================================================
# TEMPLATE CREATION
# ============================================================================

def create_unified_templates():
    """Create unified HTML templates for the web interface"""
    
    # Create templates directory
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    # Unified index template
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Living Codex Platform - Unified Discovery & Navigation</title>
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
        
        .modules { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; margin: 40px 0; backdrop-filter: blur(10px); }
        .module-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .module-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; border-left: 4px solid #4CAF50; }
        .module-card h4 { color: #4CAF50; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>🌟 Living Codex Platform</h1>
            <p>Unified Discovery, Navigation, and Collaboration in a World of Knowledge</p>
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
        
        <div class="modules">
            <h2 style="text-align: center; color: #4CAF50; margin-bottom: 30px;">🔧 Platform Modules</h2>
            <div class="module-grid">
                <div class="module-card">
                    <h4>🔍 Discovery Engine</h4>
                    <p>Smart user matching, content relevance scoring, and interest-based discovery</p>
                </div>
                <div class="module-card">
                    <h4>🧭 Navigation System</h4>
                    <p>Personalized exploration paths, progress tracking, and system overview</p>
                </div>
                <div class="module-card">
                    <h4>💡 Contribution Manager</h4>
                    <p>Enhanced content creation, categorization, and collaboration tools</p>
                </div>
                <div class="module-card">
                    <h4>👥 User Manager</h4>
                    <p>Comprehensive profiles, connections, and community building</p>
                </div>
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
        
        <div class="ontology-section" style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; margin: 40px 0; backdrop-filter: blur(10px); text-align: center;">
            <h2 style="color: #4CAF50; margin-bottom: 20px;">🏗️ System Architecture & Ontology</h2>
            <p style="margin-bottom: 25px; font-size: 1.1em;">Explore the Living Codex system components, understand relationships, and navigate the knowledge structure</p>
            <a href="/ontology" class="btn btn-primary" style="display: inline-block; margin: 10px;">Explore Ontology</a>
            <a href="/ontology/architecture" class="btn btn-secondary" style="display: inline-block; margin: 10px;">View Architecture</a>
            <a href="/ontology/search" class="btn btn-secondary" style="display: inline-block; margin: 10px;">Search Components</a>
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
