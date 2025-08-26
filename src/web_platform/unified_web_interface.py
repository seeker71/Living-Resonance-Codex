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
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent))
# Also add project src (parent) and core dirs for cross-module imports
project_src = Path(__file__).parent.parent
if str(project_src) not in sys.path:
    sys.path.insert(0, str(project_src))
core_dir = project_src / 'core'
if str(core_dir) not in sys.path:
    sys.path.insert(0, str(core_dir))

from user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle
)
from contribution_system import (
    ContributionSystem, ContributionType, ContentCategory, ContributionStatus
)
try:
    from ontology_navigator import ontology_navigator
    print("✅ Ontology navigator imported successfully")
except ImportError as e:
    # Create a placeholder if ontology_navigator is not available
    print(f"Warning: ontology_navigator import failed: {e}")
    ontology_navigator = None

# Import core search system
try:
    from core.core_search_system import fractal_search_system, SearchQuery
    print("✅ Fractal search system imported successfully")
except ImportError as e:
    print(f"Warning: fractal search system import failed: {e}")
    fractal_search_system = None

app = Flask(__name__, template_folder=str(Path(__file__).parent / 'templates'))
app.secret_key = 'living-codex-secret-key-2024'  # In production, use environment variable

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize our systems
user_system = UserManagementSystem()
contribution_system = ContributionSystem()

# Enhanced user storage with discovery features
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

def calculate_similarity(user1: UserProfile, user2: UserProfile) -> int:
    """Calculate similarity score between two users"""
    similarity_score = 0
    
    # Interest similarity
    if user1.interests and user2.interests:
        common_interests = set(user1.interests.primary_domains) & set(user2.interests.primary_domains)
        similarity_score += len(common_interests) * 10
    
    # Skill similarity
    if user1.technical_profile and user2.technical_profile:
        for skill in ['programming', 'data_analysis', 'design', 'research']:
            if (skill in user1.technical_profile.skill_levels and 
                skill in user2.technical_profile.skill_levels):
                if user1.technical_profile.skill_levels[skill] == user2.technical_profile.skill_levels[skill]:
                    similarity_score += 5
    
    # Location similarity
    if user1.location_context and user2.location_context:
        if user1.location_context.geographic_location == user2.location_context.geographic_location:
            similarity_score += 15
    
    return similarity_score

def find_common_interests(user1: UserProfile, user2: UserProfile) -> List[str]:
    """Find common interests between two users"""
    if user1.interests and user2.interests:
        return list(set(user1.interests.primary_domains) & set(user2.interests.primary_domains))
    return []

def calculate_content_relevance(user_profile: UserProfile, contribution) -> int:
    """Calculate relevance score between user and contribution"""
    relevance_score = 0
    
    # Category relevance
    if hasattr(contribution, 'metadata') and contribution.metadata:
        if contribution.metadata.tags:
            for tag in contribution.metadata.tags:
                if tag.lower() in [domain.lower() for domain in user_profile.interests.primary_domains]:
                    relevance_score += 20
                    break
    
    # Skill level relevance
    if hasattr(contribution, 'metadata') and contribution.metadata:
        if contribution.metadata.skill_level:
            user_skill = user_profile.technical_profile.skill_levels.get('programming', SkillLevel.BEGINNER)
            if contribution.metadata.skill_level.lower() == user_skill.value.lower():
                relevance_score += 15
    
    # Language relevance
    if hasattr(contribution, 'metadata') and contribution.metadata:
        if contribution.metadata.language:
            if contribution.metadata.language in user_profile.technical_profile.preferred_tools:
                relevance_score += 10
    
    return relevance_score

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
    try:
        profile = user_system.profile_manager.get_profile(user_id)
        if profile:
            return WebUser(user_id, profile)
    except Exception as e:
        print(f"Error loading user {user_id}: {e}")
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
            if profile.technical_profile and user_profile.technical_profile:
                for skill in ['programming', 'data_analysis', 'design', 'research']:
                    if (skill in profile.technical_profile.skill_levels and 
                        skill in user_profile.technical_profile.skill_levels):
                        if profile.technical_profile.skill_levels[skill] == user_profile.technical_profile.skill_levels[skill]:
                            similarity_score += 5
            
            # Location similarity
            if profile.location_context and user_profile.location_context:
                if profile.location_context.geographic_location == user_profile.location_context.geographic_location:
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
                user_skill = user_profile.technical_profile.skill_levels.get('programming', SkillLevel.BEGINNER)
                if contribution['skill_level'] == user_skill:
                    relevance_score += 15
            
            # Language relevance
            if contribution.get('language') in user_profile.technical_profile.preferred_tools:
                relevance_score += 10
            
            if relevance_score > 0:
                relevant_content.append({
                    'contribution_id': contrib_id,
                    'contribution': contribution,
                    'relevance_score': relevance_score,
                    'author': users.get(contribution.get('user_id', '')).core_identity.name if users.get(contribution.get('user_id', '')) else 'Unknown'
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
        try:
            # Get data from core systems
            user_system = UserManagementSystem()
            contribution_system = ContributionSystem()
            
            all_users = user_system.profile_manager.get_all_profiles()
            all_contributions = contribution_system.contribution_manager.get_all_contributions()
            
            # Calculate categories from contributions
            categories = set()
            for contrib in all_contributions:
                if contrib.metadata and contrib.metadata.category:
                    categories.add(contrib.metadata.category)
            
            # Count recent activity (contributions from last 7 days)
            recent_activity = 0
            for contrib in all_contributions:
                if contrib.created_at:
                    time_diff = datetime.now(contrib.created_at.tzinfo) - contrib.created_at
                    if time_diff.days < 7:
                        recent_activity += 1
            
            # Count contributions by category
            category_counts = {}
            for contrib in all_contributions:
                if contrib.metadata and contrib.metadata.category:
                    cat = contrib.metadata.category
                    category_counts[cat] = category_counts.get(cat, 0) + 1
            
            # Sort categories by count
            top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            
            return {
                'total_users': len(all_users),
                'total_contributions': len(all_contributions),
                'active_communities': len(categories),
                'recent_activity': recent_activity,
                'top_categories': top_categories
            }
        except Exception as e:
            print(f"Error getting system overview: {e}")
            # Return fallback data
            return {
                'total_users': 0,
                'total_contributions': 0,
                'active_communities': 0,
                'recent_activity': 0,
                'top_categories': []
            }

# ============================================================================
# MODULE 3: CONTRIBUTION SYSTEM
# ============================================================================

# Old ContributionManager and UserManager classes removed - now using core system APIs directly

# ============================================================================
# UNIFIED ROUTES
# ============================================================================

@app.route('/')
def index():
    """Unified home page with all features"""
    system_overview = NavigationSystem.get_system_overview()
    
    # Get recent contributions from the core system
    all_contributions = contribution_system.contribution_manager.get_all_contributions()
    recent_contributions = all_contributions[-5:] if all_contributions else []
    
    # Transform contributions to match template expectations
    transformed_contributions = []
    for contrib in recent_contributions:
        transformed_contrib = {
            'title': contrib.metadata.title if contrib.metadata else 'Untitled',
            'description': contrib.metadata.description if contrib.metadata else 'No description',
            'category': contrib.metadata.category if contrib.metadata else 'General',
            'user_id': contrib.user_id
        }
        transformed_contributions.append(transformed_contrib)
    
    # Get user profiles for display
    user_profiles = {}
    for contrib in recent_contributions:
        if contrib.user_id not in user_profiles:
            profile = user_system.profile_manager.get_profile(contrib.user_id)
            if profile:
                user_profiles[contrib.user_id] = profile
    
    return render_template('unified_index.html', 
                         system_overview=system_overview,
                         recent_contributions=transformed_contributions,
                         users=user_profiles)

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
            
            # Create user profile using core system
            user_profile = user_system.create_user_profile(user_data)
            if user_profile:
                user_id = user_profile.user_id
                
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
        
        try:
            profile = user_system.profile_manager.get_profile(user_id)
            if profile:
                user = WebUser(user_id, profile)
                login_user(user)
                
                # Update user activity
                user.last_active = datetime.now()
                
                flash('Welcome back! Explore the Living Codex platform.', 'success')
                return redirect(url_for('discover'))
            else:
                flash('User not found. Please check your ID or sign up.', 'error')
        except Exception as e:
            flash(f'Error during login: {str(e)}', 'error')
    
    return render_template('unified_login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Unified dashboard with all features"""
    user_profile = current_user.profile
    
    # Find similar users using core system
    similar_users = []
    all_profiles = user_system.profile_manager.get_all_profiles()
    for profile in all_profiles:
        if profile.user_id != current_user.id:
            # Calculate similarity score
            similarity_score = calculate_similarity(user_profile, profile)
            if similarity_score > 0:
                similar_users.append({
                    'user_id': profile.user_id,
                    'profile': profile,
                    'similarity_score': similarity_score,
                    'common_interests': find_common_interests(user_profile, profile)
                })
    
    # Sort by similarity and limit
    similar_users.sort(key=lambda x: x['similarity_score'], reverse=True)
    similar_users = similar_users[:5]
    
    # Find relevant content from core system
    relevant_content = []
    all_contributions = contribution_system.contribution_manager.get_all_contributions()
    for contrib in all_contributions:
        relevance_score = calculate_content_relevance(user_profile, contrib)
        if relevance_score > 0:
            author_profile = user_system.profile_manager.get_profile(contrib.user_id)
            author_name = author_profile.core_identity.name if author_profile else 'Unknown'
            relevant_content.append({
                'contribution_id': contrib.contribution_id,
                'contribution': contrib,
                'relevance_score': relevance_score,
                'author': author_name
            })
    
    # Sort by relevance and limit
    relevant_content.sort(key=lambda x: x['relevance_score'], reverse=True)
    relevant_content = relevant_content[:8]
    
    # Get user's contributions from core system
    user_contributions = contribution_system.get_user_contributions(current_user.id)
    
    # Get exploration paths
    exploration_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    return render_template('unified_dashboard.html',
                         user_profile=user_profile,
                         similar_users=similar_users,
                         relevant_content=relevant_content,
                         user_contributions=user_contributions,
                         exploration_paths=exploration_paths)

@app.route('/discover')
def discover():
    """Discovery hub for finding users and content"""
    # For public access, we'll show general discovery without user-specific filtering
    user_profile = None
    
    # Find users for public discovery
    similar_users = []
    all_profiles = user_system.profile_manager.get_all_profiles()
    for profile in all_profiles:
        # For public access, show all users with basic info
        similar_users.append({
            'user_id': profile.user_id,
            'profile': profile,
            'similarity_score': 0,  # No personalization for public access
            'common_interests': []  # No personalization for public access
        })
    
    # Sort by user ID and limit
    similar_users.sort(key=lambda x: x['user_id'])
    similar_users = similar_users[:8]
    
    # Find content for public discovery
    relevant_content = []
    all_contributions = contribution_system.contribution_manager.get_all_contributions()
    for contrib in all_contributions:
        author_profile = user_system.profile_manager.get_profile(contrib.user_id)
        author_name = author_profile.core_identity.name if author_profile else 'Unknown'
        relevant_content.append({
            'contribution_id': contrib.contribution_id,
            'contribution': contrib,
            'relevance_score': 0,  # No personalization for public access
            'author': author_name
        })
    
    # Sort by relevance and limit
    relevant_content.sort(key=lambda x: x['relevance_score'], reverse=True)
    relevant_content = relevant_content[:12]
    
    # Get exploration paths
    exploration_paths = NavigationSystem.get_exploration_paths(current_user.id)
    
    return render_template('discover.html',
                         similar_users=similar_users,
                         relevant_content=relevant_content,
                         exploration_paths=exploration_paths)

@app.route('/navigate')
def navigate():
    """System navigation hub"""
    system_overview = NavigationSystem.get_system_overview()
    
    # For public access, show general navigation without user-specific data
    if current_user.is_authenticated:
        user_paths = NavigationSystem.get_exploration_paths(current_user.id)
        user_progress = {
            'contributions_made': len(contribution_system.get_user_contributions(current_user.id)),
            'connections_made': len(user_connections.get(current_user.id, [])),
            'exploration_score': current_user.exploration_score,
            'collaboration_count': current_user.collaboration_count
        }
    else:
        user_paths = []
        user_progress = {
            'contributions_made': 0,
            'connections_made': 0,
            'exploration_score': 0,
            'collaboration_count': 0
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
            contribution = contribution_system.create_contribution(current_user.id, contribution_data)
            
            flash('Contribution created successfully!', 'success')
            return redirect(url_for('dashboard'))
            
        except Exception as e:
            flash(f'Error creating contribution: {str(e)}', 'error')
    
    return render_template('unified_contribute.html')

@app.route('/explore/<path:category>')
def explore_category(category):
    """Explore content by category"""
    category_content = contribution_system.contribution_manager.get_contributions_by_type(ContributionType.CONTENT)
    
    if not category_content:
        abort(404)
    
    # Find users interested in this category from core system
    interested_users = []
    all_profiles = user_system.profile_manager.get_all_profiles()
    for profile in all_profiles:
        if profile.interests and profile.interests.primary_domains:
            if category in profile.interests.primary_domains:
                interested_users.append(profile)
    
    return render_template('unified_explore_category.html',
                         category=category,
                         content=category_content,
                         interested_users=interested_users)

@app.route('/assets', methods=['GET', 'POST'])
def assets_page():
    """Assets manager page with upload form and listing"""
    message = None
    # Only allow uploads for logged-in users
    if request.method == 'POST' and not current_user.is_authenticated:
        message = ('error', 'Please login to upload files')
        return render_template('unified_assets.html', assets=assets_index, message=message)
    
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
    
    try:
        profile = user_system.profile_manager.get_profile(user_id)
        if not profile:
            abort(404)
        
        # Simple connection logic
        if user_id not in user_connections:
            user_connections[user_id] = []
        if current_user.id not in user_connections:
            user_connections[current_user.id] = []
        
        if current_user.id not in user_connections[user_id]:
            user_connections[user_id].append(current_user.id)
            user_connections[current_user.id].append(user_id)
            flash(f'Connected with {profile.core_identity.name}!', 'success')
        else:
            flash('Already connected!', 'info')
    except Exception as e:
        flash(f'Error connecting with user: {str(e)}', 'error')
    
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

@app.route('/user/<user_id>')
def view_user_profile(user_id):
    """View another user's profile"""
    # Get target user profile from core system
    target_user = user_system.profile_manager.get_profile(user_id)
    if not target_user:
        abort(404, description="User not found")
    
    current_user_profile = current_user.profile
    
    # Find common interests
    common_interests = []
    if (target_user.interests and target_user.interests.primary_domains and 
        current_user_profile.interests and current_user_profile.interests.primary_domains):
        common_interests = list(set(target_user.interests.primary_domains) & 
                              set(current_user_profile.interests.primary_domains))
    
    # Get user's contributions from core system
    user_contributions = contribution_system.get_user_contributions(user_id)
    
    # Get concepts the user is interested in
    user_concepts = []
    if target_user.interests and target_user.interests.specific_topics:
        user_concepts = target_user.interests.specific_topics
    
    return render_template('unified_user_profile.html',
                         target_user=target_user,
                         current_user=current_user_profile,
                         common_interests=common_interests,
                         user_contributions=user_contributions,
                         user_concepts=user_concepts)

@app.route('/concept/<concept_name>')
def explore_concept(concept_name):
    """Explore a specific concept and find related content"""
    # Find contributions related to this concept from core system
    concept_contributions = []
    all_contributions = contribution_system.contribution_manager.get_all_contributions()
    for contribution in all_contributions:
        if (hasattr(contribution, 'metadata') and contribution.metadata and
            (concept_name.lower() in contribution.metadata.title.lower() or
             concept_name.lower() in contribution.metadata.description.lower() or
             concept_name.lower() in [tag.lower() for tag in contribution.metadata.tags])):
            concept_contributions.append(contribution)
    
    # Find users interested in this concept from core system
    interested_users = []
    all_profiles = user_system.profile_manager.get_all_profiles()
    for user in all_profiles:
        if (user.interests and user.interests.specific_topics and
            concept_name.lower() in [topic.lower() for topic in user.interests.specific_topics]):
            interested_users.append(user)
    
    # Find source files related to this concept
    source_files = []
    for contribution in concept_contributions:
        if (hasattr(contribution, 'metadata') and contribution.metadata and
            contribution.metadata.contribution_type == 'code'):
            author_profile = user_system.profile_manager.get_profile(contribution.user_id)
            author_name = author_profile.core_identity.name if author_profile else 'Unknown'
            source_files.append({
                'name': contribution.metadata.title or 'Untitled',
                'path': f"contributions/{contribution.contribution_id}",
                'description': contribution.metadata.description or '',
                'complexity': contribution.metadata.skill_level or 'Unknown',
                'author': author_name
            })
    
    return render_template('unified_concept_explorer.html',
                         concept_name=concept_name,
                         concept_contributions=concept_contributions,
                         interested_users=interested_users,
                         source_files=source_files)

@app.route('/source/<path:file_path>')
def view_source_file(file_path):
    """View a source file and its contents"""
    # Find the contribution that matches this file path from core system
    matching_contribution = None
    all_contributions = contribution_system.contribution_manager.get_all_contributions()
    for contribution in all_contributions:
        if (hasattr(contribution, 'metadata') and contribution.metadata and
            contribution.metadata.title and file_path in contribution.metadata.title):
            matching_contribution = contribution
            break
    
    if not matching_contribution:
        abort(404, description="Source file not found")
    
    # Try to read the actual file content
    file_content = ""
    try:
        # Check if the file exists in test files
        test_file_path = Path("test_navigation_files") / Path(file_path).name
        if test_file_path.exists():
            with open(test_file_path, 'r') as f:
                file_content = f.read()
        else:
            file_content = f"# {matching_contribution.metadata.title or 'Source File'}\n\nFile path: {file_path}\n\nContent not available in demo mode."
    except Exception as e:
        file_content = f"Error reading file: {str(e)}"
    
    # Extract key expressions from the file (simplified for demo)
    expressions = []
    if file_content:
        lines = file_content.split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('class ') or line.strip().startswith('def '):
                expressions.append({
                    'type': 'Class' if line.strip().startswith('class ') else 'Function',
                    'name': line.strip().split('(')[0].split(':')[0].split()[-1],
                    'line_number': i,
                    'code': line.strip()
                })
    
    return render_template('unified_source_viewer.html',
                         file_path=file_path,
                         contribution=matching_contribution,
                         file_content=file_content,
                         expressions=expressions)

@app.route('/expression/<path:file_path>/<int:line_number>')
def view_expression(file_path, line_number):
    """View a specific expression within a source file"""
    # Find the contribution that matches this file path
    matching_contribution = None
    for contrib_id, contribution in contributions.items():
        if contribution.get('file_path') == file_path:
            matching_contribution = contribution
            break
    
    if not matching_contribution:
        abort(404)
    
    # Try to read the file content around the specified line
    file_content = ""
    context_lines = []
    try:
        test_file_path = Path("test_navigation_files") / Path(file_path).name
        if test_file_path.exists():
            with open(test_file_path, 'r') as f:
                lines = f.readlines()
                # Get context around the line (5 lines before and after)
                start_line = max(0, line_number - 6)
                end_line = min(len(lines), line_number + 5)
                context_lines = lines[start_line:end_line]
                file_content = ''.join(context_lines)
        else:
            file_content = f"# Expression at line {line_number}\n\nFile: {file_path}\n\nContent not available in demo mode."
    except Exception as e:
        file_content = f"Error reading file: {str(e)}"
    
    # Find the specific expression
    target_expression = None
    if context_lines:
        for i, line in enumerate(context_lines, start_line + 1):
            if i == line_number:
                if line.strip().startswith('class '):
                    target_expression = {
                        'type': 'Class',
                        'name': line.strip().split('(')[0].split(':')[0].split()[-1],
                        'line_number': i,
                        'code': line.strip()
                    }
                elif line.strip().startswith('def '):
                    target_expression = {
                        'type': 'Function',
                        'name': line.strip().split('(')[0].split(':')[0].split()[-1],
                        'line_number': i,
                        'code': line.strip()
                    }
                break
    
    return render_template('unified_expression_viewer.html',
                         file_path=file_path,
                         line_number=line_number,
                         contribution=matching_contribution,
                         file_content=file_content,
                         target_expression=target_expression)

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/discovery/similar_users')
def api_similar_users():
    """API endpoint for finding similar users"""
    limit = request.args.get('limit', 10, type=int)
    
    # For public access, show all users
    if current_user.is_authenticated:
        user_profile = current_user.profile
        # Find similar users using core system
        similar_users = []
        all_profiles = user_system.profile_manager.get_all_profiles()
        for profile in all_profiles:
            if profile.user_id != current_user.id:
                # Calculate similarity score
                similarity_score = calculate_similarity(user_profile, profile)
                if similarity_score > 0:
                    similar_users.append({
                        'user_id': profile.user_id,
                        'profile': profile,
                        'similarity_score': similarity_score,
                        'common_interests': find_common_interests(user_profile, profile)
                    })
        
        # Sort by similarity and limit
        similar_users.sort(key=lambda x: x['similarity_score'], reverse=True)
        similar_users = similar_users[:limit]
    else:
        # Show all users for public access
        all_profiles = user_system.profile_manager.get_all_profiles()
        similar_users = []
        for profile in all_profiles:
            similar_users.append({
                'user_id': profile.user_id,
                'profile': profile,
                'similarity_score': 0,
                'common_interests': []
            })
        similar_users = similar_users[:limit]
    
    # Format for API response
    formatted_users = []
    for user_data in similar_users:
        user = user_data['profile']
        formatted_users.append({
            'user_id': user_data['user_id'],
            'name': user.core_identity.name if user.core_identity else 'Unknown',
            'similarity_score': user_data['similarity_score'],
            'common_interests': user_data['common_interests'],
            'skills': user.technical_profile.skill_levels if user.technical_profile else {},
            'location': user.location_context.geographic_location if user.location_context else 'Unknown'
        })
    
    return jsonify(formatted_users)

@app.route('/api/discovery/relevant_content')
def api_relevant_content():
    """API endpoint for finding relevant content"""
    limit = request.args.get('limit', 20, type=int)
    
    # For public access, show all content
    if current_user.is_authenticated:
        user_profile = current_user.profile
        # Find relevant content from core system
        relevant_content = []
        all_contributions = contribution_system.contribution_manager.get_all_contributions()
        for contrib in all_contributions:
            relevance_score = calculate_content_relevance(user_profile, contrib)
            if relevance_score > 0:
                author_profile = user_system.profile_manager.get_profile(contrib.user_id)
                author_name = author_profile.core_identity.name if author_profile else 'Unknown'
                relevant_content.append({
                    'contribution_id': contrib.contribution_id,
                    'contribution': contrib,
                    'relevance_score': relevance_score,
                    'author': author_name
                })
        
        # Sort by relevance and limit
        relevant_content.sort(key=lambda x: x['relevance_score'], reverse=True)
        relevant_content = relevant_content[:limit]
    else:
        # Show all content for public access
        all_contributions = contribution_system.contribution_manager.get_all_contributions()
        relevant_content = []
        for contrib in all_contributions:
            author_profile = user_system.profile_manager.get_profile(contrib.user_id)
            author_name = author_profile.core_identity.name if author_profile else 'Unknown'
            relevant_content.append({
                'contribution_id': contrib.contribution_id,
                'contribution': contrib,
                'relevance_score': 0,
                'author': author_name
            })
        
        # Sort by creation date and limit
        relevant_content.sort(key=lambda x: x['contribution'].created_at if x['contribution'].created_at else '', reverse=True)
        relevant_content = relevant_content[:limit]
    
    # Format for API response
    formatted_content = []
    for content_data in relevant_content:
        content = content_data['contribution']
        formatted_content.append({
            'contribution_id': content_data['contribution_id'],
            'title': content.metadata.title if content.metadata else 'Untitled',
            'category': content.metadata.category if content.metadata else 'General',
            'relevance_score': content_data['relevance_score'],
            'author': content_data['author'],
            'created_at': content.created_at.isoformat() if content.created_at else '',
            'skill_level': content.metadata.skill_level if content.metadata else 'All Levels'
        })
    
    return jsonify(formatted_content)

@app.route('/api/navigation/system_overview')
def api_system_overview():
    """API endpoint for system overview"""
    return jsonify(NavigationSystem.get_system_overview())

@app.route('/api/navigation/exploration_paths')
def api_exploration_paths():
    """API endpoint for user exploration paths"""
    if current_user.is_authenticated:
        return jsonify(NavigationSystem.get_exploration_paths(current_user.id))
    else:
        return jsonify([])  # Return empty paths for public access

@app.route('/api/contributions')
def api_contributions():
    """API endpoint for user contributions"""
    if current_user.is_authenticated:
        # Return user's own contributions
        contributions = contribution_system.get_user_contributions(current_user.id)
    else:
        # Return all contributions for public access
        contributions = contribution_system.contribution_manager.get_all_contributions()
    
    return jsonify(contributions)

@app.route('/api/opportunities')
def api_opportunities():
    """API endpoint for contribution opportunities"""
    if not current_user.is_authenticated:
        return jsonify([])  # No opportunities for public access
    
    # This would integrate with the existing contribution system
    opportunities = contribution_system.find_opportunities(current_user.profile)
    return jsonify(opportunities)

# ============================================================================
# ASSET API ENDPOINTS
# ============================================================================

@app.route('/api/assets', methods=['GET'])
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
# UNIFIED SEARCH ROUTES
# ============================================================================

@app.route('/search')
def unified_search():
    """Unified search across all system nodes"""
    query = request.args.get('q', '')
    search_type = request.args.get('type', 'all')
    filters = {}
    
    # Parse filters from query parameters
    for key in ['type', 'category', 'source', 'date_from', 'date_to']:
        if request.args.get(key):
            filters[key] = request.args.get(key)
    
    results = []
    total_count = 0
    facets = {}
    suggestions = []
    
    if query and fractal_search_system:
        try:
            # Create search query
            search_query = SearchQuery(
                query=query,
                search_type=search_type,
                filters=filters,
                limit=50,
                offset=0,
                sort_by='relevance'
            )
            
            # Perform search
            search_response = fractal_search_system.search(search_query)
            results = search_response.results
            total_count = search_response.total_count
            facets = search_response.facets
            suggestions = search_response.suggestions
            
        except Exception as e:
            flash(f'Search error: {str(e)}', 'error')
    
    return render_template('unified_search.html',
                         query=query,
                         search_type=search_type,
                         results=results,
                         total_count=total_count,
                         facets=facets,
                         suggestions=suggestions)

@app.route('/api/search')
def api_unified_search():
    """API endpoint for unified search"""
    query = request.args.get('q', '')
    search_type = request.args.get('type', 'all')
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    sort_by = request.args.get('sort_by', 'relevance')
    
    # Parse filters
    filters = {}
    for key in ['type', 'category', 'source', 'date_from', 'date_to']:
        if request.args.get(key):
            filters[key] = request.args.get(key)
    
    # Fallback: if core search unavailable, serve ontology-only search
    if query and (fractal_search_system is None) and ontology_navigator is not None:
        if search_type in ('all', 'ontology'):
            try:
                nodes = ontology_navigator.search_nodes(query)
                total = len(nodes)
                sliced = nodes[offset:offset+limit]
                formatted_results = []
                for n in sliced:
                    formatted_results.append({
                        'id': n.id,
                        'type': 'ontology',
                        'title': n.name,
                        'description': n.description,
                        'content': f"Category: {n.category}, Type: {n.type}",
                        'source': 'ontology_navigator',
                        'category': n.category,
                        'relevance_score': 0.0,
                        'metadata': {'node_type': n.type, 'relationships': n.relationships},
                        'created_at': n.created_at.isoformat() if n.created_at else None,
                        'updated_at': n.updated_at.isoformat() if n.updated_at else None
                    })
                return jsonify({
                    'query': query,
                    'search_type': search_type,
                    'results': formatted_results,
                    'total_count': total,
                    'search_time_ms': 0.0,
                    'facets': {'types': {'ontology': total}, 'categories': {}},
                    'suggestions': []
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'results': [], 'total_count': 0, 'facets': {}, 'suggestions': []})
    
    if not query or not fractal_search_system:
        return jsonify({
            'results': [],
            'total_count': 0,
            'facets': {},
            'suggestions': []
        })
    
    try:
        # Create search query
        search_query = SearchQuery(
            query=query,
            search_type=search_type,
            filters=filters,
            limit=limit,
            offset=offset,
            sort_by=sort_by
        )
        
        # Perform search
        search_response = fractal_search_system.search(search_query)
        
        # Format results for API
        formatted_results = []
        for result in search_response.results:
            content_preview = result.content[:200] + '...' if isinstance(result.content, str) and len(result.content) > 200 else result.content
            formatted_results.append({
                'id': result.id,
                'type': result.type,
                'title': result.title,
                'description': result.description,
                'content': content_preview,
                'source': result.source,
                'category': result.category,
                'relevance_score': result.relevance_score,
                'metadata': result.metadata,
                'created_at': result.created_at.isoformat() if result.created_at else None,
                'updated_at': result.updated_at.isoformat() if result.updated_at else None
            })
        
        return jsonify({
            'query': query,
            'search_type': search_type,
            'results': formatted_results,
            'total_count': search_response.total_count,
            'search_time_ms': search_response.search_time_ms,
            'facets': search_response.facets,
            'suggestions': search_response.suggestions
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search/suggestions')
def api_search_suggestions():
    """API endpoint for search suggestions/autocomplete"""
    partial_query = request.args.get('q', '')
    
    if not partial_query or not fractal_search_system:
        return jsonify([])
    
    try:
        suggestions = fractal_search_system.get_search_suggestions(partial_query)
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search/analytics')
def api_search_analytics():
    """API endpoint for search analytics"""
    if not fractal_search_system:
        return jsonify({'error': 'Search system not available'}), 500
    
    try:
        analytics = fractal_search_system.get_search_analytics()
        return jsonify(analytics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
# NAVIGATION DEMO ROUTES
# ============================================================================



@app.route('/api/navigation/<flow_type>')
def api_navigation_flow(flow_type):
    """API endpoint for navigation flow data"""
    navigation_flows = {
        "void_to_user": {
            "description": "Navigate from system void to user profile",
            "steps": [
                "System entry point (Void)",
                "User discovery",
                "Profile access",
                "User information display"
            ],
            "example_data": {
                "start_point": "System Void",
                "target_user": "Alice Chen",
                "user_type": "Software Developer",
                "interests": ["Python", "Flask", "React", "Neural Networks"]
            }
        },
        "user_to_user": {
            "description": "Navigate from one user to another user",
            "steps": [
                "Current user profile",
                "Related users discovery",
                "User selection",
                "Target user profile"
            ],
            "example_data": {
                "current_user": "Alice Chen",
                "target_user": "Bob Rodriguez",
                "connection_type": "Shared Interest",
                "common_interests": ["Artificial Intelligence", "Python"]
            }
        },
        "user_to_concept": {
            "description": "Navigate from user to concept of interest",
            "steps": [
                "User profile",
                "Interests exploration",
                "Concept selection",
                "Concept details"
            ],
            "example_data": {
                "user": "Bob Rodriguez",
                "concept": "Neural Networks",
                "concept_type": "Technical Domain",
                "relevance_score": 0.95
            }
        },
        "concept_to_source": {
            "description": "Navigate from concept to source file",
            "steps": [
                "Concept information",
                "Related content discovery",
                "Source file selection",
                "File content display"
            ],
            "example_data": {
                "concept": "Neural Networks",
                "source_file": "neural_network.py",
                "file_type": "Python Implementation",
                "complexity": "Advanced"
            }
        },
        "source_to_expression": {
            "description": "Navigate from source file to specific expression",
            "steps": [
                "Source file content",
                "Code structure analysis",
                "Expression identification",
                "Expression details"
            ],
            "example_data": {
                "source_file": "neural_network.py",
                "expression": "AttentionMechanism class",
                "expression_type": "Class Definition",
                "line_numbers": "15-25"
            }
        }
    }
    
    if flow_type not in navigation_flows:
        abort(404)
    
    return jsonify(navigation_flows[flow_type])

@app.route('/api/navigation/complete')
def api_complete_navigation():
    """API endpoint for complete navigation data"""
    return jsonify({
        "title": "Complete Navigation Flow Demonstration",
        "description": "Demonstrates the full navigation path from Void to Expression",
        "flows": ["void_to_user", "user_to_user", "user_to_concept", "concept_to_source", "source_to_expression"],
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
    })

# Navigation demo route removed - using actual web interface navigation instead

@app.route('/api/system/status', methods=['GET'])
def api_system_status():
    """API endpoint for comprehensive fractal system status"""
    try:
        from core.core_system import fractal_core_system
        from core.fractal_components import initialize_fractal_components
        
        # Initialize fractal components if not already done
        initialize_fractal_components()
        
        # Get basic system status
        status = fractal_core_system.get_system_status()
        
        # Enhance with comprehensive information
        comprehensive_status = {
            "system_overview": {
                "name": "Living Codex Fractal System",
                "version": "2.0.0",
                "description": "Fractal holographic architecture with everything as nodes",
                "timestamp": datetime.now().isoformat(),
                "total_nodes": status.get("total_nodes", 0),
                "node_types_count": len(status.get("node_types", [])),
                "component_count": status.get("component_count", 0)
            },
            "system_health": {
                "self_similarity": 100.0,
                "meta_circularity": 100.0,
                "holographic_nature": 100.0,
                "fractal_integrity": 100.0
            },
            "fractal_components": status.get("components", []),
            "node_types": {node_type: {"name": node_type, "count": 1} for node_type in status.get("node_types", [])},
            "fractal_layers": {str(layer): {"layer": layer, "count": 1} for layer in status.get("fractal_layers", [])},
            "water_states": {state: {"name": state, "count": 1} for state in status.get("water_states", [])},
            "chakras": {chakra: {"name": chakra, "count": 1} for chakra in status.get("chakras", [])},
            "frequencies": {str(freq): {"frequency": freq, "count": 1} for freq in status.get("frequencies", [])},
            "total_nodes": status.get("total_nodes", 0),
            "component_count": status.get("component_count", 0)
        }
        
        return jsonify(comprehensive_status)
    except Exception as e:
        print(f"Error getting system status: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("🌐 Starting Unified Living Codex Platform...")
    print("   Open your browser to: http://localhost:5004")
    print("   All features combined in one modular system!")
    
    app.run(debug=False, host='0.0.0.0', port=5004)
