"""
Living Codex Platform Package
Provides user management, contribution systems, and web interface
"""

from .user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle,
    ProfileManager, PreferenceEngine, VaporState
)

from .contribution_system import (
    ContributionSystem, ContributionManager, ContributionMatcher,
    Contribution, ContributionType, ContributionStatus, ContentCategory,
    CodeContribution, ContentContribution, VisualContribution,
    TranslationContribution, LocalSolutionContribution, ContributionMetadata
)

__all__ = [
    # User Management
    'UserManagementSystem', 'UserProfile', 'CoreIdentity', 'CommunicationPreferences',
    'TechnicalProfile', 'Interests', 'LocationContext', 'SkillLevel', 'CommunicationStyle', 'LearningStyle',
    'ProfileManager', 'PreferenceEngine', 'VaporState',
    
    # Contribution System
    'ContributionSystem', 'ContributionManager', 'ContributionMatcher',
    'Contribution', 'ContributionType', 'ContributionStatus', 'ContentCategory',
    'CodeContribution', 'ContentContribution', 'VisualContribution',
    'TranslationContribution', 'LocalSolutionContribution', 'ContributionMetadata'
]
