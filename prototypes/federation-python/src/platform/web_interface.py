#!/usr/bin/env python3
"""
Living Codex Platform - Web Interface
Simple Flask-based web interface for user registration and contribution
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
import json
from datetime import datetime
from pathlib import Path

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

# Simple user storage for demo (in production, use proper database)
users = {}

class WebUser(UserMixin):
    """Web user class for Flask-Login"""
    def __init__(self, user_id, profile):
        self.id = user_id
        self.profile = profile

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    if user_id in users:
        return WebUser(user_id, users[user_id])
    return None

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """User registration"""
    if request.method == 'POST':
        try:
            # Get form data
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
                    'community_connections': request.form.get('community_connections', '').split(',') if request.form.get('community_connections') else [],
                    'local_challenges': request.form.get('local_challenges', '').split(',') if request.form.get('local_challenges') else [],
                    'local_resources': request.form.get('local_resources', '').split(',') if request.form.get('local_resources') else []
                }
            }
            
            # Create user profile
            profile = user_system.create_user_profile(user_data)
            if profile:
                # Store in our simple user storage
                users[profile.user_id] = profile
                
                # Log user in
                user = WebUser(profile.user_id, profile)
                login_user(user)
                
                flash('Profile created successfully! Welcome to the Living Codex!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Failed to create profile. Please try again.', 'error')
                
        except Exception as e:
            flash(f'Error creating profile: {str(e)}', 'error')
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        # Simple demo login - in production, use proper authentication
        user_id = request.form.get('user_id')
        if user_id in users:
            user = WebUser(user_id, users[user_id])
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('User not found. Please sign up first.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard with personalized experience"""
    # Get personalized experience
    experience = user_system.get_personalized_experience(current_user.id)
    
    # Find contribution opportunities
    opportunities = contribution_system.find_opportunities(current_user.profile)
    
    # Get user contributions
    user_contributions = contribution_system.get_user_contributions(current_user.id)
    
    return render_template('dashboard.html', 
                         experience=experience, 
                         opportunities=opportunities,
                         contributions=user_contributions)

@app.route('/contribute', methods=['GET', 'POST'])
@login_required
def contribute():
    """Create new contribution"""
    if request.method == 'POST':
        try:
            contribution_type = request.form['contribution_type']
            
            # Prepare contribution data
            contribution_data = {
                'contribution_type': contribution_type,
                'metadata': {
                    'title': request.form['title'],
                    'description': request.form['description'],
                    'tags': request.form.get('tags', '').split(',') if request.form.get('tags') else [],
                    'language': request.form.get('language', 'en'),
                    'skill_level': request.form.get('skill_level', 'beginner'),
                    'target_audience': request.form.get('target_audience', '').split(',') if request.form.get('target_audience') else []
                }
            }
            
            # Add type-specific content
            if contribution_type == 'content':
                contribution_data['content_data'] = {
                    'content': request.form['content'],
                    'category': request.form.get('category', ContentCategory.ARTICLE.value),
                    'citations': request.form.get('citations', '').split(',') if request.form.get('citations') else []
                }
            elif contribution_type == 'code':
                contribution_data['code_content'] = {
                    'code_content': request.form['code_content'],
                    'language': request.form.get('code_language', 'python'),
                    'framework': request.form.get('framework'),
                    'dependencies': request.form.get('dependencies', '').split(',') if request.form.get('dependencies') else [],
                    'documentation': request.form.get('documentation')
                }
            elif contribution_type == 'local_solution':
                contribution_data['local_solution_data'] = {
                    'problem_description': request.form['problem_description'],
                    'solution_approach': request.form['solution_approach'],
                    'local_context': request.form['local_context'],
                    'community_involvement': request.form['community_involvement'],
                    'success_metrics': request.form.get('success_metrics', '').split(',') if request.form.get('success_metrics') else [],
                    'challenges_faced': request.form.get('challenges_faced', '').split(',') if request.form.get('challenges_faced') else [],
                    'lessons_learned': request.form.get('lessons_learned', '')
                }
            
            # Create contribution
            contribution = contribution_system.create_contribution(current_user.id, contribution_data)
            if contribution:
                flash('Contribution created successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Failed to create contribution. Please try again.', 'error')
                
        except Exception as e:
            flash(f'Error creating contribution: {str(e)}', 'error')
    
    return render_template('contribute.html')

@app.route('/profile')
@login_required
def profile():
    """View and edit user profile"""
    return render_template('profile.html', profile=current_user.profile)

@app.route('/api/opportunities')
@login_required
def api_opportunities():
    """API endpoint for contribution opportunities"""
    opportunities = contribution_system.find_opportunities(current_user.profile)
    return jsonify(opportunities)

@app.route('/api/contributions')
@login_required
def api_contributions():
    """API endpoint for user contributions"""
    contributions = contribution_system.get_user_contributions(current_user.id)
    return jsonify([c.to_dict() for c in contributions])

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    # Create basic HTML templates
    create_basic_templates(templates_dir)
    
    print("🌐 Starting Living Codex Platform...")
    print("   Open your browser to: http://localhost:5000")
    print("   Sign up to create your profile and start contributing!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

def create_basic_templates(templates_dir):
    """Create basic HTML templates for the web interface"""
    
    # Index template
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Living Codex Platform</title>
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
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 60px; }
        .feature { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; backdrop-filter: blur(10px); }
        .feature h3 { color: #4CAF50; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>🌟 Living Codex Platform</h1>
            <p>A platform that honors human complexity and creates personalized experiences for every contributor</p>
            <div class="cta-buttons">
                <a href="/signup" class="btn btn-primary">Join the Platform</a>
                <a href="/login" class="btn btn-secondary">Sign In</a>
            </div>
        </div>
        
        <div class="features">
            <div class="feature">
                <h3>🎯 Personalized Experience</h3>
                <p>Every user sees a unique view tailored to their beliefs, skills, interests, and location.</p>
            </div>
            <div class="feature">
                <h3>🌍 Global Collaboration</h3>
                <p>Connect with people worldwide while maintaining your unique cultural and personal identity.</p>
            </div>
            <div class="feature">
                <h3>🚀 Skill-Based Growth</h3>
                <p>Learn and contribute at your own pace, with content that matches your current abilities.</p>
            </div>
            <div class="feature">
                <h3>💡 Local Solutions, Global Impact</h3>
                <p>Share solutions from your community that can help people around the world.</p>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    # Signup template
    signup_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Join Living Codex Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .container { max-width: 800px; margin: 0 auto; }
        .form-container { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 15px; backdrop-filter: blur(10px); }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select, textarea { width: 100%; padding: 10px; border: none; border-radius: 5px; font-size: 16px; }
        .btn { background: #4CAF50; color: white; padding: 15px 30px; border: none; border-radius: 25px; font-size: 16px; cursor: pointer; }
        .btn:hover { background: #45a049; }
        .section { margin-bottom: 30px; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 10px; }
        .section h3 { color: #4CAF50; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center; margin-bottom: 40px;">🌟 Join the Living Codex Platform</h1>
        
        <form method="POST" class="form-container">
            <div class="section">
                <h3>👤 Core Identity</h3>
                <div class="form-group">
                    <label for="name">Name *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="pronouns">Pronouns</label>
                    <input type="text" id="pronouns" name="pronouns" placeholder="e.g., they/them, she/her">
                </div>
                <div class="form-group">
                    <label for="cultural_background">Cultural Background</label>
                    <input type="text" id="cultural_background" name="cultural_background">
                </div>
                <div class="form-group">
                    <label for="belief_system">Belief System / Values</label>
                    <input type="text" id="belief_system" name="belief_system">
                </div>
            </div>
            
            <div class="section">
                <h3>🗣️ Communication Preferences</h3>
                <div class="form-group">
                    <label for="primary_language">Primary Language *</label>
                    <input type="text" id="primary_language" name="primary_language" required>
                </div>
                <div class="form-group">
                    <label for="secondary_languages">Secondary Languages</label>
                    <input type="text" id="secondary_languages" name="secondary_languages" placeholder="Comma-separated">
                </div>
                <div class="form-group">
                    <label for="communication_style">Communication Style</label>
                    <select id="communication_style" name="communication_style">
                        <option value="casual">Casual</option>
                        <option value="formal">Formal</option>
                        <option value="technical">Technical</option>
                        <option value="creative">Creative</option>
                    </select>
                </div>
            </div>
            
            <div class="section">
                <h3>💻 Technical Profile</h3>
                <div class="form-group">
                    <label for="programming_skill">Programming Skill</label>
                    <select id="programming_skill" name="programming_skill">
                        <option value="beginner">Beginner</option>
                        <option value="intermediate">Intermediate</option>
                        <option value="advanced">Advanced</option>
                        <option value="expert">Expert</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="learning_path">Learning Goals</label>
                    <input type="text" id="learning_path" name="learning_path" placeholder="Comma-separated skills you want to learn">
                </div>
            </div>
            
            <div class="section">
                <h3>🎯 Interests & Passions</h3>
                <div class="form-group">
                    <label for="specific_topics">Topics You Care About</label>
                    <input type="text" id="specific_topics" name="specific_topics" placeholder="e.g., Climate Change, AI Ethics, Community Building">
                </div>
                <div class="form-group">
                    <label for="passion_areas">What Are You Passionate About?</label>
                    <input type="text" id="passion_areas" name="passion_areas" placeholder="e.g., Making technology accessible to everyone">
                </div>
            </div>
            
            <div class="section">
                <h3>🌍 Location & Community</h3>
                <div class="form-group">
                    <label for="location">Where Are You Located? *</label>
                    <input type="text" id="location" name="location" required placeholder="City, Country">
                </div>
                <div class="form-group">
                    <label for="local_challenges">Local Challenges in Your Area</label>
                    <input type="text" id="local_challenges" name="local_challenges" placeholder="Comma-separated challenges">
                </div>
                <div class="form-group">
                    <label for="local_resources">Local Resources Available</label>
                    <input type="text" id="local_resources" name="local_resources" placeholder="Comma-separated resources">
                </div>
            </div>
            
            <button type="submit" class="btn">Create My Profile</button>
        </form>
        
        <p style="text-align: center; margin-top: 20px;">
            Already have a profile? <a href="/login" style="color: #4CAF50;">Sign In</a>
        </p>
    </div>
</body>
</html>"""
    
    # Dashboard template
    dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Living Codex Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .btn { background: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
        .section { background: rgba(255,255,255,0.1); padding: 20px; margin-bottom: 20px; border-radius: 10px; backdrop-filter: blur(10px); }
        .section h3 { color: #4CAF50; margin-bottom: 15px; }
        .opportunity { background: rgba(255,255,255,0.05); padding: 15px; margin-bottom: 10px; border-radius: 5px; }
        .contribution { background: rgba(255,255,255,0.05); padding: 15px; margin-bottom: 10px; border-radius: 5px; }
        .priority-high { border-left: 4px solid #f44336; }
        .priority-medium { border-left: 4px solid #ff9800; }
        .priority-low { border-left: 4px solid #4CAF50; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Welcome, {{ current_user.profile.core_identity.name }}!</h1>
            <div>
                <a href="/contribute" class="btn">Create Contribution</a>
                <a href="/profile" class="btn">View Profile</a>
                <a href="/logout" class="btn">Logout</a>
            </div>
        </div>
        
        <div class="section">
            <h3>🎯 Your Personalized Experience</h3>
            {% if experience %}
                <p><strong>Current Focus:</strong> {{ experience.learning_path.focus_area }}</p>
                <p><strong>Learning Style:</strong> {{ experience.learning_path.learning_style }}</p>
                <p><strong>Recommendations:</strong></p>
                <ul>
                {% for rec in experience.recommendations[:5] %}
                    <li>{{ rec }}</li>
                {% endfor %}
                </ul>
            {% else %}
                <p>Loading your personalized experience...</p>
            {% endif %}
        </div>
        
        <div class="section">
            <h3>🚀 Contribution Opportunities</h3>
            {% if opportunities %}
                {% for opp in opportunities %}
                <div class="opportunity priority-{{ opp.priority }}">
                    <h4>{{ opp.area }}</h4>
                    <p>{{ opp.description }}</p>
                    <p><strong>Type:</strong> {{ opp.contribution_type }}</strong></p>
                </div>
                {% endfor %}
            {% else %}
                <p>No opportunities found. Check back later!</p>
            {% endif %}
        </div>
        
        <div class="section">
            <h3>📚 Your Contributions</h3>
            {% if contributions %}
                {% for contrib in contributions %}
                <div class="contribution">
                    <h4>{{ contrib.metadata.title }}</h4>
                    <p>{{ contrib.metadata.description }}</p>
                    <p><strong>Type:</strong> {{ contrib.contribution_type.value }} | <strong>Status:</strong> {{ contrib.status.value }}</p>
                </div>
                {% endfor %}
            {% else %}
                <p>You haven't made any contributions yet. <a href="/contribute" style="color: #4CAF50;">Start contributing!</a></p>
            {% endif %}
        </div>
    </div>
</body>
</html>"""
    
    # Write templates to files
    (templates_dir / 'index.html').write_text(index_html)
    (templates_dir / 'signup.html').write_text(signup_html)
    (templates_dir / 'dashboard.html').write_text(dashboard_html)
    
    # Create simple templates for other pages
    (templates_dir / 'login.html').write_text("""<!DOCTYPE html>
<html><head><title>Login</title></head><body><h1>Login</h1><form method="POST"><input name="user_id" placeholder="User ID"><button type="submit">Login</button></form></body></html>""")
    
    (templates_dir / 'contribute.html').write_text("""<!DOCTYPE html>
<html><head><title>Create Contribution</title></head><body><h1>Create Contribution</h1><form method="POST"><select name="contribution_type"><option value="content">Content</option><option value="code">Code</option><option value="local_solution">Local Solution</option></select><input name="title" placeholder="Title"><textarea name="description" placeholder="Description"></textarea><button type="submit">Create</button></form></body></html>""")
    
    (templates_dir / 'profile.html').write_text("""<!DOCTYPE html>
<html><head><title>Profile</title></head><body><h1>Your Profile</h1><p>Name: {{ profile.core_identity.name }}</p><p>Location: {{ profile.location_context.geographic_location }}</p><a href="/dashboard">Back to Dashboard</a></body></html>""")
    
    print("✅ Created basic HTML templates")
