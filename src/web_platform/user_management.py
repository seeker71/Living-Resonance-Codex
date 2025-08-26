#!/usr/bin/env python3
"""
Living Codex Platform - User Management System
Manages user profiles, preferences, and personalized experiences
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
from enum import Enum
from pathlib import Path

class UserState(Enum):
    """User states in the water metaphor"""
    ICE = "ice"           # Core system infrastructure
    WATER = "water"       # User preferences & identity (liquid state)
    VAPOR = "vapor"       # Temporary personal views (gas state)

class SkillLevel(Enum):
    """Skill level enumeration"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class CommunicationStyle(Enum):
    """Communication style preferences"""
    FORMAL = "formal"
    CASUAL = "casual"
    TECHNICAL = "technical"
    CREATIVE = "creative"

class LearningStyle(Enum):
    """Learning style preferences"""
    VISUAL = "visual"
    AUDITORY = "auditory"
    KINESTHETIC = "kinesthetic"
    READING = "reading"

@dataclass
class CoreIdentity:
    """Core user identity (liquid state - stable)"""
    name: str
    pronouns: Optional[str] = None
    cultural_background: Optional[str] = None
    belief_system: Optional[str] = None
    life_experience: Optional[str] = None
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        identity_dict = asdict(self)
        identity_dict['created_at'] = self.created_at.isoformat()
        return identity_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CoreIdentity':
        """Create from dictionary"""
        if 'created_at' in data:
            dt = datetime.fromisoformat(data['created_at'])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            data['created_at'] = dt
        return cls(**data)

@dataclass
class CommunicationPreferences:
    """Communication preferences (liquid state - adaptable)"""
    primary_language: str
    secondary_languages: List[str] = None
    communication_style: CommunicationStyle = CommunicationStyle.CASUAL
    learning_style: LearningStyle = LearningStyle.READING
    accessibility_needs: List[str] = None
    
    def __post_init__(self):
        if self.secondary_languages is None:
            self.secondary_languages = []
        if self.accessibility_needs is None:
            self.accessibility_needs = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        comm_dict = asdict(self)
        comm_dict['communication_style'] = self.communication_style.value
        comm_dict['learning_style'] = self.learning_style.value
        return comm_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CommunicationPreferences':
        """Create from dictionary"""
        data['communication_style'] = CommunicationStyle(data['communication_style'])
        data['learning_style'] = LearningStyle(data['learning_style'])
        return cls(**data)

@dataclass
class TechnicalProfile:
    """Technical skills and preferences (liquid state - growing)"""
    skill_levels: Dict[str, SkillLevel] = None
    learning_path: List[str] = None
    preferred_tools: List[str] = None
    contribution_areas: List[str] = None
    
    def __post_init__(self):
        if self.skill_levels is None:
            self.skill_levels = {}
        if self.learning_path is None:
            self.learning_path = []
        if self.preferred_tools is None:
            self.preferred_tools = []
        if self.contribution_areas is None:
            self.contribution_areas = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        tech_dict = asdict(self)
        # Convert SkillLevel enums to strings
        for skill, level in tech_dict['skill_levels'].items():
            tech_dict['skill_levels'][skill] = level.value
        return tech_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TechnicalProfile':
        """Create from dictionary"""
        # Convert string values back to SkillLevel enums
        for skill, level in data['skill_levels'].items():
            data['skill_levels'][skill] = SkillLevel(level)
        return cls(**data)

@dataclass
class Interests:
    """User interests and expertise (liquid state - evolving)"""
    primary_domains: List[str] = None
    specific_topics: List[str] = None
    expertise_levels: Dict[str, SkillLevel] = None
    passion_areas: List[str] = None
    
    def __post_init__(self):
        if self.primary_domains is None:
            self.primary_domains = []
        if self.specific_topics is None:
            self.specific_topics = []
        if self.expertise_levels is None:
            self.expertise_levels = {}
        if self.passion_areas is None:
            self.passion_areas = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        interests_dict = asdict(self)
        # Convert SkillLevel enums to strings
        for topic, level in interests_dict['expertise_levels'].items():
            interests_dict['expertise_levels'][topic] = level.value
        return interests_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Interests':
        """Create from dictionary"""
        # Convert string values back to SkillLevel enums
        for topic, level in data['expertise_levels'].items():
            data['expertise_levels'][topic] = SkillLevel(level)
        return cls(**data)

@dataclass
class LocationContext:
    """Geographic and cultural context (liquid state - local)"""
    geographic_location: str
    timezone: str
    cultural_context: Optional[str] = None
    community_connections: List[str] = None
    local_challenges: List[str] = None
    local_resources: List[str] = None
    
    def __post_init__(self):
        if self.community_connections is None:
            self.community_connections = []
        if self.local_challenges is None:
            self.local_challenges = []
        if self.local_resources is None:
            self.local_resources = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LocationContext':
        """Create from dictionary"""
        return cls(**data)

@dataclass
class UserProfile:
    """Complete user profile combining all aspects"""
    user_id: str
    core_identity: CoreIdentity
    communication: CommunicationPreferences
    technical_profile: TechnicalProfile
    interests: Interests
    location_context: LocationContext
    created_at: datetime = None
    updated_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
        if self.updated_at is None:
            self.updated_at = datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert profile to dictionary for storage"""
        profile_dict = asdict(self)
        # Convert datetime objects to ISO strings
        profile_dict['created_at'] = self.created_at.isoformat()
        profile_dict['updated_at'] = self.updated_at.isoformat()
        
        # Use nested objects' to_dict methods
        profile_dict['core_identity'] = self.core_identity.to_dict()
        profile_dict['communication'] = self.communication.to_dict()
        profile_dict['technical_profile'] = self.technical_profile.to_dict()
        profile_dict['interests'] = self.interests.to_dict()
        profile_dict['location_context'] = self.location_context.to_dict()
        
        return profile_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserProfile':
        """Create profile from dictionary"""
        # Convert ISO strings back to datetime objects
        if 'created_at' in data:
            dt = datetime.fromisoformat(data['created_at'])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            data['created_at'] = dt
        if 'updated_at' in data:
            dt = datetime.fromisoformat(data['updated_at'])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            data['updated_at'] = dt
        
        # Reconstruct nested objects using their from_dict methods
        data['core_identity'] = CoreIdentity.from_dict(data['core_identity'])
        data['communication'] = CommunicationPreferences.from_dict(data['communication'])
        data['technical_profile'] = TechnicalProfile.from_dict(data['technical_profile'])
        data['interests'] = Interests.from_dict(data['interests'])
        data['location_context'] = LocationContext.from_dict(data['location_context'])
        
        return cls(**data)

@dataclass
class VaporState:
    """Temporary user state (vapor state - session-specific)"""
    session_id: str
    current_focus: Optional[str] = None
    temporary_interests: List[str] = None
    session_goals: List[str] = None
    current_collaborations: List[str] = None
    created_at: datetime = None
    
    def __post_init__(self):
        if self.temporary_interests is None:
            self.temporary_interests = []
        if self.session_goals is None:
            self.session_goals = []
        if self.current_collaborations is None:
            self.current_collaborations = []
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage"""
        vapor_dict = asdict(self)
        vapor_dict['created_at'] = self.created_at.isoformat()
        return vapor_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'VaporState':
        """Create from dictionary"""
        if 'created_at' in data:
            dt = datetime.fromisoformat(data['created_at'])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            data['created_at'] = dt
        return cls(**data)

class ProfileManager:
    """Manages user profile storage and retrieval"""
    
    def __init__(self, storage_path: str = "user_profiles"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
    
    def store_profile(self, profile: UserProfile) -> bool:
        """Store user profile to disk"""
        try:
            profile_file = self.storage_path / f"{profile.user_id}.json"
            profile_dict = profile.to_dict()

            with open(profile_file, 'w', encoding='utf-8') as f:
                json.dump(profile_dict, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error storing profile: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """Retrieve user profile from disk"""
        try:
            profile_file = self.storage_path / f"{user_id}.json"
            if not profile_file.exists():
                return None
            
            with open(profile_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return UserProfile.from_dict(data)
        except Exception as e:
            print(f"Error retrieving profile: {e}")
            return None
    
    def get_all_profiles(self) -> List[UserProfile]:
        """Get all user profiles from storage"""
        profiles = []
        for file_path in self.storage_path.glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                profile = UserProfile.from_dict(data)
                profiles.append(profile)
            except Exception as e:
                print(f"Error reading profile file {file_path}: {e}")
        
        return profiles
    
    def update_profile(self, profile: UserProfile) -> bool:
        """Update existing user profile"""
        profile.updated_at = datetime.now(timezone.utc)
        return self.store_profile(profile)
    
    def delete_profile(self, user_id: str) -> bool:
        """Delete user profile"""
        try:
            profile_file = self.storage_path / f"{user_id}.json"
            if profile_file.exists():
                profile_file.unlink()
            return True
        except Exception as e:
            print(f"Error deleting profile: {e}")
            return False

class PreferenceEngine:
    """Creates personalized experiences based on user profiles"""
    
    def create_experience(self, liquid_state: UserProfile, vapor_state: VaporState) -> Dict[str, Any]:
        """Combine stable preferences with current context"""
        experience = {
            'content_filters': self._get_content_filters(liquid_state, vapor_state),
            'recommendations': self._get_recommendations(liquid_state, vapor_state),
            'learning_path': self._get_learning_path(liquid_state, vapor_state),
            'collaboration_opportunities': self._find_collaborations(liquid_state, vapor_state),
            'local_relevance': self._get_local_content(liquid_state, vapor_state)
        }
        return experience
    
    def _get_content_filters(self, liquid_state: UserProfile, vapor_state: VaporState) -> Dict[str, Any]:
        """Generate content filters based on user preferences"""
        return {
            'languages': [liquid_state.communication.primary_language] + liquid_state.communication.secondary_languages,
            'skill_level': self._get_appropriate_skill_level(liquid_state),
            'interests': liquid_state.interests.primary_domains + vapor_state.temporary_interests,
            'cultural_context': liquid_state.location_context.cultural_context,
            'accessibility': liquid_state.communication.accessibility_needs
        }
    
    def _get_recommendations(self, liquid_state: UserProfile, vapor_state: VaporState) -> List[str]:
        """Generate personalized recommendations"""
        recommendations = []
        
        # Add recommendations based on interests
        for topic in liquid_state.interests.specific_topics:
            recommendations.append(f"Learn more about {topic}")
        
        # Add recommendations based on skill gaps
        for skill, level in liquid_state.technical_profile.skill_levels.items():
            if level == SkillLevel.BEGINNER:
                recommendations.append(f"Develop {skill} skills")
        
        # Add recommendations based on current focus
        if vapor_state.current_focus:
            recommendations.append(f"Deep dive into {vapor_state.current_focus}")
        
        return recommendations
    
    def _get_learning_path(self, liquid_state: UserProfile, vapor_state: VaporState) -> Dict[str, Any]:
        """Generate personalized learning path"""
        return {
            'current_level': self._get_appropriate_skill_level(liquid_state),
            'next_steps': liquid_state.technical_profile.learning_path,
            'focus_area': vapor_state.current_focus or liquid_state.interests.primary_domains[0] if liquid_state.interests.primary_domains else "General",
            'learning_style': liquid_state.communication.learning_style.value
        }
    
    def _find_collaborations(self, liquid_state: UserProfile, vapor_state: VaporState) -> List[Dict[str, Any]]:
        """Find collaboration opportunities"""
        collaborations = []
        
        # Find people with similar interests
        for topic in liquid_state.interests.specific_topics:
            collaborations.append({
                'type': 'interest_match',
                'topic': topic,
                'description': f"Connect with others interested in {topic}"
            })
        
        # Find local collaboration opportunities
        if liquid_state.location_context.local_challenges:
            collaborations.append({
                'type': 'local_challenge',
                'topic': 'Local Community',
                'description': f"Work on local challenges in {liquid_state.location_context.geographic_location}"
            })
        
        return collaborations
    
    def _get_local_content(self, liquid_state: UserProfile, vapor_state: VaporState) -> Dict[str, Any]:
        """Get locally relevant content"""
        return {
            'location': liquid_state.location_context.geographic_location,
            'timezone': liquid_state.location_context.timezone,
            'local_challenges': liquid_state.location_context.local_challenges,
            'local_resources': liquid_state.location_context.local_resources,
            'cultural_context': liquid_state.location_context.cultural_context
        }
    
    def _get_appropriate_skill_level(self, liquid_state: UserProfile) -> str:
        """Determine appropriate skill level for content"""
        if not liquid_state.technical_profile.skill_levels:
            return "beginner"
        
        # Find the most common skill level
        levels = list(liquid_state.technical_profile.skill_levels.values())
        if not levels:
            return "beginner"
        
        # Return the most frequent level, or beginner if no clear pattern
        from collections import Counter
        level_counts = Counter(levels)
        most_common = level_counts.most_common(1)[0][0]
        return most_common.value

class UserManagementSystem:
    """Main system for managing users and their experiences"""
    
    def __init__(self, storage_path: str = "user_profiles"):
        self.profile_manager = ProfileManager(storage_path)
        self.preference_engine = PreferenceEngine()
        self.active_sessions: Dict[str, VaporState] = {}
    
    def create_user_profile(self, user_data: Dict[str, Any]) -> Optional[UserProfile]:
        """Create a new user profile with all their complexity"""
        try:
            # Generate unique user ID
            user_id = str(uuid.uuid4())
            
            # Create profile components
            core_identity = CoreIdentity(**user_data.get('identity', {}))
            communication = CommunicationPreferences(**user_data.get('communication', {}))
            technical_profile = TechnicalProfile(**user_data.get('technical', {}))
            interests = Interests(**user_data.get('interests', {}))
            location_context = LocationContext(**user_data.get('location', {}))
            
            # Create complete profile
            profile = UserProfile(
                user_id=user_id,
                core_identity=core_identity,
                communication=communication,
                technical_profile=technical_profile,
                interests=interests,
                location_context=location_context
            )
            
            # Store profile
            if self.profile_manager.store_profile(profile):
                return profile
            return None
            
        except Exception as e:
            print(f"Error creating user profile: {e}")
            return None
    
    def get_personalized_experience(self, user_id: str, current_context: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Generate personalized experience based on liquid and vapor states"""
        # Get liquid state (stable preferences)
        liquid_state = self.profile_manager.get_profile(user_id)
        if not liquid_state:
            return None
        
        # Get or create vapor state (current session)
        vapor_state = self.active_sessions.get(user_id)
        if not vapor_state:
            vapor_state = VaporState(
                session_id=str(uuid.uuid4()),
                current_focus=current_context.get('focus') if current_context else None
            )
            self.active_sessions[user_id] = vapor_state
        
        # Create personalized experience
        return self.preference_engine.create_experience(liquid_state, vapor_state)
    
    def _store_vapor_state(self, user_id: str, vapor_state: VaporState) -> bool:
        """Store vapor state to disk"""
        try:
            vapor_file = Path("vapor_states") / f"{user_id}.json"
            vapor_file.parent.mkdir(exist_ok=True)
            with open(vapor_file, 'w', encoding='utf-8') as f:
                json.dump(vapor_state.to_dict(), f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error storing vapor state: {e}")
            return False
    
    def _load_vapor_state(self, user_id: str) -> Optional[VaporState]:
        """Load vapor state from disk"""
        try:
            vapor_file = Path("vapor_states") / f"{user_id}.json"
            if not vapor_file.exists():
                return None
            
            with open(vapor_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return VaporState.from_dict(data)
        except Exception as e:
            print(f"Error loading vapor state: {e}")
            return None
    
    def update_user_preferences(self, user_id: str, updates: Dict[str, Any]) -> bool:
        """Update user preferences in liquid state"""
        profile = self.profile_manager.get_profile(user_id)
        if not profile:
            return False
        
        # Update specific sections
        if 'identity' in updates:
            for key, value in updates['identity'].items():
                if hasattr(profile.core_identity, key):
                    setattr(profile.core_identity, key, value)
        
        if 'communication' in updates:
            for key, value in updates['communication'].items():
                if hasattr(profile.communication, key):
                    setattr(profile.communication, key, value)
        
        if 'technical' in updates:
            for key, value in updates['technical'].items():
                if hasattr(profile.technical_profile, key):
                    setattr(profile.technical_profile, key, value)
        
        if 'interests' in updates:
            for key, value in updates['interests'].items():
                if hasattr(profile.interests, key):
                    setattr(profile.interests, key, value)
        
        if 'location' in updates:
            for key, value in updates['location'].items():
                if hasattr(profile.location_context, key):
                    setattr(profile.location_context, key, value)
        
        # Update timestamp and save
        profile.updated_at = datetime.now(timezone.utc)
        return self.profile_manager.update_profile(profile)
    
    def update_session_state(self, user_id: str, session_updates: Dict[str, Any]) -> bool:
        """Update current session state (vapor state)"""
        if user_id not in self.active_sessions:
            return False
        
        vapor_state = self.active_sessions[user_id]
        
        # Update session-specific information
        if 'current_focus' in session_updates:
            vapor_state.current_focus = session_updates['current_focus']
        
        if 'temporary_interests' in session_updates:
            vapor_state.temporary_interests = session_updates['temporary_interests']
        
        if 'session_goals' in session_updates:
            vapor_state.session_goals = session_updates['session_goals']
        
        if 'current_collaborations' in session_updates:
            vapor_state.current_collaborations = session_updates['current_collaborations']
        
        return True
    
    def end_session(self, user_id: str) -> bool:
        """End user session and clear vapor state"""
        if user_id in self.active_sessions:
            del self.active_sessions[user_id]
            return True
        return False

# Example usage and testing
if __name__ == "__main__":
    # Create user management system
    user_system = UserManagementSystem()
    
    # Example user data
    user_data = {
        'identity': {
            'name': 'Alex Chen',
            'pronouns': 'they/them',
            'cultural_background': 'Chinese-American',
            'belief_system': 'Humanist',
            'life_experience': 'Community organizer and software developer'
        },
        'communication': {
            'primary_language': 'English',
            'secondary_languages': ['Mandarin', 'Spanish'],
            'communication_style': CommunicationStyle.CASUAL,
            'learning_style': LearningStyle.VISUAL,
            'accessibility_needs': ['High contrast', 'Screen reader support']
        },
        'technical': {
            'skill_levels': {
                'programming': SkillLevel.ADVANCED,
                'data_analysis': SkillLevel.INTERMEDIATE,
                'design': SkillLevel.BEGINNER
            },
            'learning_path': ['UI/UX Design', 'Data Visualization'],
            'preferred_tools': ['Python', 'React', 'Figma'],
            'contribution_areas': ['Code', 'Documentation', 'Community Building']
        },
        'interests': {
            'primary_domains': ['Technology', 'Social Justice', 'Community Building'],
            'specific_topics': ['AI Ethics', 'Climate Change', 'Digital Inclusion'],
            'expertise_levels': {
                'community_organizing': SkillLevel.EXPERT,
                'software_development': SkillLevel.ADVANCED,
                'climate_science': SkillLevel.BEGINNER
            },
            'passion_areas': ['Making technology accessible to everyone']
        },
        'location': {
            'geographic_location': 'San Francisco, CA, USA',
            'timezone': 'America/Los_Angeles',
            'cultural_context': 'Diverse urban community with strong tech culture',
            'community_connections': ['Local tech meetups', 'Climate action groups'],
            'local_challenges': ['Housing affordability', 'Digital divide'],
            'local_resources': ['Tech companies', 'Universities', 'Community centers']
        }
    }
    
    # Create user profile
    profile = user_system.create_user_profile(user_data)
    if profile:
        print(f"✅ Created profile for {profile.core_identity.name}")
        print(f"   User ID: {profile.user_id}")
        print(f"   Location: {profile.location_context.geographic_location}")
        print(f"   Skills: {list(profile.technical_profile.skill_levels.keys())}")
        
        # Get personalized experience
        experience = user_system.get_personalized_experience(profile.user_id)
        if experience:
            print(f"\n🎯 Personalized Experience:")
            print(f"   Recommendations: {experience['recommendations'][:3]}")
            print(f"   Learning Path: {experience['learning_path']['focus_area']}")
            print(f"   Collaborations: {len(experience['collaboration_opportunities'])} opportunities")
    else:
        print("❌ Failed to create user profile")
