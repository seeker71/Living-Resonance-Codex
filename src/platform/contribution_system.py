#!/usr/bin/env python3
"""
Living Codex Platform - Contribution System
Allows users to contribute content based on their profiles and skills
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any, Union
from enum import Enum
from pathlib import Path

class ContributionType(Enum):
    """Types of contributions users can make"""
    CODE = "code"
    CONTENT = "content"
    VISUAL = "visual"
    TRANSLATION = "translation"
    LOCAL_SOLUTION = "local_solution"
    COMMUNITY_FEEDBACK = "community_feedback"
    FACT_CHECK = "fact_check"
    CURRICULUM = "curriculum"

class ContributionStatus(Enum):
    """Status of contributions"""
    DRAFT = "draft"
    SUBMITTED = "submitted"
    REVIEWING = "reviewing"
    APPROVED = "approved"
    REJECTED = "rejected"
    PUBLISHED = "published"

class ContentCategory(Enum):
    """Categories of content contributions"""
    TUTORIAL = "tutorial"
    ARTICLE = "article"
    RESEARCH = "research"
    STORY = "story"
    EXPLANATION = "explanation"
    CASE_STUDY = "case_study"

@dataclass
class ContributionMetadata:
    """Metadata for contributions"""
    title: str
    description: str
    tags: List[str] = None
    language: str = "en"
    cultural_context: Optional[str] = None
    skill_level: str = "beginner"
    target_audience: List[str] = None
    local_relevance: Optional[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.target_audience is None:
            self.target_audience = []

@dataclass
class CodeContribution:
    """Code-based contributions"""
    code_content: str
    language: str
    framework: Optional[str] = None
    dependencies: List[str] = None
    documentation: Optional[str] = None
    tests: Optional[str] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

@dataclass
class ContentContribution:
    """Text-based content contributions"""
    content: str
    category: ContentCategory
    word_count: int = 0
    reading_time: int = 0
    citations: List[str] = None
    
    def __post_init__(self):
        if self.citations is None:
            self.citations = []
        if self.word_count == 0:
            self.word_count = len(self.content.split())

@dataclass
class VisualContribution:
    """Visual content contributions"""
    visual_type: str  # image, diagram, infographic, video
    file_path: str
    alt_text: str
    description: str
    dimensions: Optional[Dict[str, int]] = None
    file_size: Optional[int] = None

@dataclass
class TranslationContribution:
    """Translation contributions"""
    original_language: str
    target_language: str
    original_content: str
    translated_content: str
    cultural_adaptations: List[str] = None
    notes: Optional[str] = None
    
    def __post_init__(self):
        if self.cultural_adaptations is None:
            self.cultural_adaptations = []

@dataclass
class LocalSolutionContribution:
    """Solutions specific to local communities"""
    problem_description: str
    solution_approach: str
    local_context: str
    community_involvement: str
    success_metrics: List[str] = None
    challenges_faced: List[str] = None
    lessons_learned: str = ""
    
    def __post_init__(self):
        if self.success_metrics is None:
            self.success_metrics = []
        if self.challenges_faced is None:
            self.challenges_faced = []

@dataclass
class Contribution:
    """Main contribution class that can contain any type of contribution"""
    contribution_id: str
    user_id: str
    contribution_type: ContributionType
    metadata: ContributionMetadata
    status: ContributionStatus = ContributionStatus.DRAFT
    created_at: datetime = None
    updated_at: datetime = None
    reviewed_by: Optional[str] = None
    review_notes: Optional[str] = None
    
    # Content based on type
    code_content: Optional[CodeContribution] = None
    content_data: Optional[ContentContribution] = None
    visual_data: Optional[VisualContribution] = None
    translation_data: Optional[TranslationContribution] = None
    local_solution_data: Optional[LocalSolutionContribution] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
        if self.updated_at is None:
            self.updated_at = datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert contribution to dictionary for storage"""
        contribution_dict = asdict(self)
        # Convert datetime objects to ISO strings
        contribution_dict['created_at'] = self.created_at.isoformat()
        contribution_dict['updated_at'] = self.updated_at.isoformat()
        
        # Convert enums to strings
        contribution_dict['contribution_type'] = self.contribution_type.value
        contribution_dict['status'] = self.status.value
        
        return contribution_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Contribution':
        """Create contribution from dictionary"""
        # Convert ISO strings back to datetime objects
        if 'created_at' in data:
            data['created_at'] = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = datetime.fromisoformat(data['updated_at'])
        
        # Convert string values back to enums
        data['contribution_type'] = ContributionType(data['contribution_type'])
        data['status'] = ContributionStatus(data['status'])
        
        # Reconstruct nested objects
        data['metadata'] = ContributionMetadata(**data['metadata'])
        
        if data.get('code_content'):
            data['code_content'] = CodeContribution(**data['code_content'])
        if data.get('content_data'):
            data['content_data'] = ContentContribution(**data['content_data'])
        if data.get('visual_data'):
            data['visual_data'] = VisualContribution(**data['visual_data'])
        if data.get('translation_data'):
            data['translation_data'] = TranslationContribution(**data['translation_data'])
        if data.get('local_solution_data'):
            data['local_solution_data'] = LocalSolutionContribution(**data['local_solution_data'])
        
        return cls(**data)

class ContributionManager:
    """Manages contribution storage and retrieval"""
    
    def __init__(self, storage_path: str = "contributions"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
    
    def store_contribution(self, contribution: Contribution) -> bool:
        """Store contribution to disk"""
        try:
            contribution_file = self.storage_path / f"{contribution.contribution_id}.json"
            with open(contribution_file, 'w', encoding='utf-8') as f:
                json.dump(contribution.to_dict(), f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error storing contribution: {e}")
            return False
    
    def get_contribution(self, contribution_id: str) -> Optional[Contribution]:
        """Retrieve contribution from disk"""
        try:
            contribution_file = self.storage_path / f"{contribution_id}.json"
            if not contribution_file.exists():
                return None
            
            with open(contribution_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return Contribution.from_dict(data)
        except Exception as e:
            print(f"Error retrieving contribution: {e}")
            return None
    
    def get_user_contributions(self, user_id: str) -> List[Contribution]:
        """Get all contributions by a specific user"""
        contributions = []
        for file_path in self.storage_path.glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                contribution = Contribution.from_dict(data)
                if contribution.user_id == user_id:
                    contributions.append(contribution)
            except Exception as e:
                print(f"Error reading contribution file {file_path}: {e}")
        
        return sorted(contributions, key=lambda x: x.created_at, reverse=True)
    
    def get_contributions_by_type(self, contribution_type: ContributionType) -> List[Contribution]:
        """Get all contributions of a specific type"""
        contributions = []
        for file_path in self.storage_path.glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                contribution = Contribution.from_dict(data)
                if contribution.contribution_type == contribution_type:
                    contributions.append(contribution)
            except Exception as e:
                print(f"Error reading contribution file {file_path}: {e}")
        
        return sorted(contributions, key=lambda x: x.created_at, reverse=True)
    
    def update_contribution(self, contribution: Contribution) -> bool:
        """Update existing contribution"""
        contribution.updated_at = datetime.now(timezone.utc)
        return self.store_contribution(contribution)
    
    def delete_contribution(self, contribution_id: str) -> bool:
        """Delete contribution"""
        try:
            contribution_file = self.storage_path / f"{contribution_id}.json"
            if contribution_file.exists():
                contribution_file.unlink()
            return True
        except Exception as e:
            print(f"Error deleting contribution: {e}")
            return False

class ContributionMatcher:
    """Finds contribution opportunities based on user profiles"""
    
    def __init__(self, contribution_manager: ContributionManager):
        self.contribution_manager = contribution_manager
    
    def find_contribution_opportunities(self, user_profile) -> List[Dict[str, Any]]:
        """Find where this user can best contribute"""
        opportunities = []
        
        # Match technical skills to technical needs
        if hasattr(user_profile, 'technical_profile') and user_profile.technical_profile.skill_levels:
            opportunities.extend(self._find_technical_contributions(user_profile))
        
        # Match interests to content needs
        if hasattr(user_profile, 'interests') and user_profile.interests.specific_topics:
            opportunities.extend(self._find_content_contributions(user_profile))
        
        # Match location to local needs
        if hasattr(user_profile, 'location_context') and user_profile.location_context.local_challenges:
            opportunities.extend(self._find_local_contributions(user_profile))
        
        # Match language skills to translation needs
        if hasattr(user_profile, 'communication') and user_profile.communication.secondary_languages:
            opportunities.extend(self._find_translation_contributions(user_profile))
        
        return opportunities
    
    def _find_technical_contributions(self, user_profile) -> List[Dict[str, Any]]:
        """Find technical contribution opportunities"""
        opportunities = []
        
        # Look for areas where the user has advanced skills
        for skill, level in user_profile.technical_profile.skill_levels.items():
            if level.value in ['advanced', 'expert']:
                opportunities.append({
                    'type': 'technical_contribution',
                    'area': skill,
                    'description': f"Share your {skill} expertise with the community",
                    'contribution_type': ContributionType.CODE,
                    'priority': 'high' if level.value == 'expert' else 'medium'
                })
        
        # Look for areas where the user wants to learn
        for learning_area in user_profile.technical_profile.learning_path:
            opportunities.append({
                'type': 'learning_contribution',
                'area': learning_area,
                'description': f"Document your learning journey in {learning_area}",
                'contribution_type': ContributionType.CONTENT,
                'priority': 'medium'
            })
        
        return opportunities
    
    def _find_content_contributions(self, user_profile) -> List[Dict[str, Any]]:
        """Find content contribution opportunities"""
        opportunities = []
        
        # Match specific topics to content needs
        for topic in user_profile.interests.specific_topics:
            opportunities.append({
                'type': 'topic_contribution',
                'area': topic,
                'description': f"Create content about {topic}",
                'contribution_type': ContributionType.CONTENT,
                'priority': 'high'
            })
        
        # Match passion areas to content needs
        for passion in user_profile.interests.passion_areas:
            opportunities.append({
                'type': 'passion_contribution',
                'area': passion,
                'description': f"Share your passion for {passion}",
                'contribution_type': ContributionType.CONTENT,
                'priority': 'high'
            })
        
        return opportunities
    
    def _find_local_contributions(self, user_profile) -> List[Dict[str, Any]]:
        """Find local contribution opportunities"""
        opportunities = []
        
        # Local challenges that need solutions
        for challenge in user_profile.location_context.local_challenges:
            opportunities.append({
                'type': 'local_solution',
                'area': challenge,
                'description': f"Share solutions for {challenge} in {user_profile.location_context.geographic_location}",
                'contribution_type': ContributionType.LOCAL_SOLUTION,
                'priority': 'high'
            })
        
        # Local resources that could help others
        for resource in user_profile.location_context.local_resources:
            opportunities.append({
                'type': 'local_resource',
                'area': resource,
                'description': f"Document how to access {resource} in your area",
                'contribution_type': ContributionType.CONTENT,
                'priority': 'medium'
            })
        
        return opportunities
    
    def _find_translation_contributions(self, user_profile) -> List[Dict[str, Any]]:
        """Find translation contribution opportunities"""
        opportunities = []
        
        # Match secondary languages to translation needs
        for language in user_profile.communication.secondary_languages:
            opportunities.append({
                'type': 'translation',
                'area': language,
                'description': f"Help translate content to {language}",
                'contribution_type': ContributionType.TRANSLATION,
                'priority': 'medium'
            })
        
        return opportunities

class ContributionSystem:
    """Main system for managing contributions"""
    
    def __init__(self, storage_path: str = "contributions"):
        self.contribution_manager = ContributionManager(storage_path)
        self.contribution_matcher = ContributionMatcher(self.contribution_manager)
    
    def create_contribution(self, user_id: str, contribution_data: Dict[str, Any]) -> Optional[Contribution]:
        """Create a new contribution"""
        try:
            # Generate unique contribution ID
            contribution_id = str(uuid.uuid4())
            
            # Create metadata
            metadata = ContributionMetadata(**contribution_data.get('metadata', {}))
            
            # Create contribution based on type
            contribution_type = ContributionType(contribution_data['contribution_type'])
            
            # Initialize content fields
            code_content = None
            content_data = None
            visual_data = None
            translation_data = None
            local_solution_data = None
            
            # Create specific content based on type
            if contribution_type == ContributionType.CODE:
                code_content = CodeContribution(**contribution_data.get('code_content', {}))
            elif contribution_type == ContributionType.CONTENT:
                content_data = ContentContribution(**contribution_data.get('content_data', {}))
            elif contribution_type == ContributionType.VISUAL:
                visual_data = VisualContribution(**contribution_data.get('visual_data', {}))
            elif contribution_type == ContributionType.TRANSLATION:
                translation_data = TranslationContribution(**contribution_data.get('translation_data', {}))
            elif contribution_type == ContributionType.LOCAL_SOLUTION:
                local_solution_data = LocalSolutionContribution(**contribution_data.get('local_solution_data', {}))
            
            # Create contribution
            contribution = Contribution(
                contribution_id=contribution_id,
                user_id=user_id,
                contribution_type=contribution_type,
                metadata=metadata,
                code_content=code_content,
                content_data=content_data,
                visual_data=visual_data,
                translation_data=translation_data,
                local_solution_data=local_solution_data
            )
            
            # Store contribution
            if self.contribution_manager.store_contribution(contribution):
                return contribution
            return None
            
        except Exception as e:
            print(f"Error creating contribution: {e}")
            return None
    
    def find_opportunities(self, user_profile) -> List[Dict[str, Any]]:
        """Find contribution opportunities for a user"""
        return self.contribution_matcher.find_contribution_opportunities(user_profile)
    
    def get_user_contributions(self, user_id: str) -> List[Contribution]:
        """Get all contributions by a user"""
        return self.contribution_manager.get_user_contributions(user_id)
    
    def get_contributions_by_type(self, contribution_type: ContributionType) -> List[Contribution]:
        """Get all contributions of a specific type"""
        return self.contribution_manager.get_contributions_by_type(contribution_type)
    
    def update_contribution_status(self, contribution_id: str, new_status: ContributionStatus, 
                                 reviewed_by: str = None, review_notes: str = None) -> bool:
        """Update contribution status (for moderation)"""
        contribution = self.contribution_manager.get_contribution(contribution_id)
        if not contribution:
            return False
        
        contribution.status = new_status
        contribution.reviewed_by = reviewed_by
        contribution.review_notes = review_notes
        
        return self.contribution_manager.update_contribution(contribution)

# Example usage and testing
if __name__ == "__main__":
    # Create contribution system
    contribution_system = ContributionSystem()
    
    # Example contribution data
    contribution_data = {
        'contribution_type': 'content',
        'metadata': {
            'title': 'Getting Started with Python for Beginners',
            'description': 'A friendly introduction to Python programming',
            'tags': ['python', 'programming', 'beginners', 'tutorial'],
            'language': 'en',
            'skill_level': 'beginner',
            'target_audience': ['students', 'beginners', 'self-learners']
        },
        'content_data': {
            'content': 'Python is a wonderful programming language...',
            'category': ContentCategory.TUTORIAL.value,
            'citations': ['https://python.org', 'https://docs.python.org']
        }
    }
    
    # Create contribution
    contribution = contribution_system.create_contribution("user123", contribution_data)
    if contribution:
        print(f"✅ Created contribution: {contribution.metadata.title}")
        print(f"   Type: {contribution.contribution_type.value}")
        print(f"   Status: {contribution.status.value}")
        print(f"   Tags: {', '.join(contribution.metadata.tags)}")
        
        # Get user contributions
        user_contributions = contribution_system.get_user_contributions("user123")
        print(f"\n📚 User has {len(user_contributions)} contributions")
        
        # Get contributions by type
        content_contributions = contribution_system.get_contributions_by_type(ContributionType.CONTENT)
        print(f"📝 Total content contributions: {len(content_contributions)}")
    else:
        print("❌ Failed to create contribution")
