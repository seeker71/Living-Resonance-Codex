#!/usr/bin/env python3
"""
Living Codex Platform - Regression Test Suite
Ensures all features stay functional while new features are tested autonomously
"""

import sys
import os
import unittest
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from web_platform.user_management import (
    UserManagementSystem, UserProfile, CoreIdentity, CommunicationPreferences,
    TechnicalProfile, Interests, LocationContext, SkillLevel, CommunicationStyle, LearningStyle,
    ProfileManager, PreferenceEngine, VaporState
)
from web_platform.contribution_system import (
    ContributionSystem, ContributionManager, ContributionMatcher,
    Contribution, ContributionType, ContributionStatus, ContentCategory,
    CodeContribution, ContentContribution, VisualContribution,
    TranslationContribution, LocalSolutionContribution, ContributionMetadata
)

class TestDataGenerator:
    """Generates test data for comprehensive testing"""
    
    @staticmethod
    def create_test_user_data() -> Dict[str, Any]:
        """Create comprehensive test user data"""
        return {
            'identity': {
                'name': 'Test User',
                'pronouns': 'they/them',
                'cultural_background': 'Test Culture',
                'belief_system': 'Test Beliefs',
                'life_experience': 'Test Experience'
            },
            'communication': {
                'primary_language': 'en',
                'secondary_languages': ['es', 'fr'],
                'communication_style': CommunicationStyle.CASUAL,
                'learning_style': LearningStyle.VISUAL,
                'accessibility_needs': ['High contrast']
            },
            'technical': {
                'skill_levels': {
                    'programming': SkillLevel.INTERMEDIATE,
                    'data_analysis': SkillLevel.BEGINNER,
                    'design': SkillLevel.ADVANCED,
                    'research': SkillLevel.EXPERT
                },
                'learning_path': ['Machine Learning', 'UI/UX'],
                'preferred_tools': ['Python', 'Figma'],
                'contribution_areas': ['Code', 'Design']
            },
            'interests': {
                'primary_domains': ['Technology', 'Art'],
                'specific_topics': ['AI Ethics', 'Digital Art'],
                'expertise_levels': {
                    'ai_ethics': SkillLevel.EXPERT,
                    'digital_art': SkillLevel.ADVANCED
                },
                'passion_areas': ['Ethical AI development']
            },
            'location': {
                'geographic_location': 'Test City, Test Country',
                'timezone': 'UTC',
                'cultural_context': 'Test cultural context',
                'community_connections': ['Test community'],
                'local_challenges': ['Test challenge'],
                'local_resources': ['Test resource']
            }
        }
    
    @staticmethod
    def create_test_contribution_data() -> Dict[str, Any]:
        """Create comprehensive test contribution data"""
        return {
            'contribution_type': 'content',
            'metadata': {
                'title': 'Test Contribution',
                'description': 'A test contribution for regression testing',
                'tags': ['test', 'regression', 'quality'],
                'language': 'en',
                'skill_level': 'intermediate',
                'target_audience': ['developers', 'testers']
            },
            'content_data': {
                'content': 'This is test content for regression testing.',
                'category': ContentCategory.ARTICLE.value,
                'citations': ['https://test.com']
            }
        }

class FeatureValidator:
    """Validates new features before they're committed to the system"""
    
    def __init__(self):
        self.validation_results = []
        self.critical_errors = []
    
    def validate_feature(self, feature_name: str, test_function, *args, **kwargs) -> bool:
        """Validate a new feature with comprehensive testing"""
        print(f"🔍 Validating feature: {feature_name}")
        
        try:
            # Run the feature test
            result = test_function(*args, **kwargs)
            
            if result:
                self.validation_results.append({
                    'feature': feature_name,
                    'status': 'PASSED',
                    'timestamp': datetime.now(timezone.utc).isoformat(),
                    'details': 'Feature validation successful'
                })
                print(f"✅ {feature_name}: PASSED")
                return True
            else:
                self.validation_results.append({
                    'feature': feature_name,
                    'status': 'FAILED',
                    'timestamp': datetime.now(timezone.utc).isoformat(),
                    'details': 'Feature validation failed'
                })
                print(f"❌ {feature_name}: FAILED")
                return False
                
        except Exception as e:
            error_msg = f"Feature validation error: {str(e)}"
            self.validation_results.append({
                'feature': feature_name,
                'status': 'ERROR',
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'details': error_msg
            })
            self.critical_errors.append(error_msg)
            print(f"💥 {feature_name}: ERROR - {error_msg}")
            return False
    
    def get_validation_report(self) -> Dict[str, Any]:
        """Get comprehensive validation report"""
        total_features = len(self.validation_results)
        passed_features = len([r for r in self.validation_results if r['status'] == 'PASSED'])
        failed_features = len([r for r in self.validation_results if r['status'] == 'FAILED'])
        error_features = len([r for r in self.validation_results if r['status'] == 'ERROR'])
        
        return {
            'summary': {
                'total_features': total_features,
                'passed': passed_features,
                'failed': failed_features,
                'errors': error_features,
                'success_rate': (passed_features / total_features * 100) if total_features > 0 else 0
            },
            'results': self.validation_results,
            'critical_errors': self.critical_errors,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def can_commit(self) -> bool:
        """Determine if code/data can be safely committed"""
        return len(self.critical_errors) == 0 and len([r for r in self.validation_results if r['status'] == 'FAILED']) == 0

class RegressionTestSuite(unittest.TestCase):
    """Comprehensive regression test suite for the Living Codex Platform"""
    
    def setUp(self):
        """Set up test environment before each test"""
        # Create temporary directories for testing
        self.test_dir = tempfile.mkdtemp()
        self.user_profiles_dir = os.path.join(self.test_dir, 'user_profiles')
        self.contributions_dir = os.path.join(self.test_dir, 'contributions')
        self.vapor_states_dir = os.path.join(self.test_dir, 'vapor_states')
        
        os.makedirs(self.user_profiles_dir, exist_ok=True)
        os.makedirs(self.contributions_dir, exist_ok=True)
        os.makedirs(self.vapor_states_dir, exist_ok=True)
        
        # Initialize systems with test directories
        self.user_system = UserManagementSystem(self.user_profiles_dir)
        self.contribution_system = ContributionSystem(self.contributions_dir)
        
        # Test data generator
        self.test_data = TestDataGenerator()
        
        # Feature validator
        self.validator = FeatureValidator()
    
    def tearDown(self):
        """Clean up test environment after each test"""
        shutil.rmtree(self.test_dir)
    
    def test_01_user_profile_creation(self):
        """Test user profile creation functionality"""
        print("\n🧪 Testing: User Profile Creation")
        
        # Create test user data
        user_data = self.test_data.create_test_user_data()
        
        # Create user profile
        profile = self.user_system.create_user_profile(user_data)
        
        # Validate profile creation
        self.assertIsNotNone(profile)
        self.assertEqual(profile.core_identity.name, 'Test User')
        self.assertEqual(profile.location_context.geographic_location, 'Test City, Test Country')
        self.assertEqual(len(profile.technical_profile.skill_levels), 4)
        
        # Test profile persistence
        retrieved_profile = self.user_system.profile_manager.get_profile(profile.user_id)
        self.assertIsNotNone(retrieved_profile)
        self.assertEqual(retrieved_profile.core_identity.name, 'Test User')
        
        print("✅ User Profile Creation: PASSED")
        return True
    
    def test_02_user_profile_serialization(self):
        """Test user profile serialization and deserialization"""
        print("\n🧪 Testing: User Profile Serialization")
        
        # Create test user
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # Test to_dict serialization
        profile_dict = profile.to_dict()
        self.assertIsInstance(profile_dict, dict)
        self.assertIn('user_id', profile_dict)
        self.assertIn('core_identity', profile_dict)
        self.assertIn('technical_profile', profile_dict)
        
        # Test from_dict deserialization
        reconstructed_profile = UserProfile.from_dict(profile_dict)
        self.assertEqual(reconstructed_profile.core_identity.name, profile.core_identity.name)
        self.assertEqual(reconstructed_profile.user_id, profile.user_id)
        
        print("✅ User Profile Serialization: PASSED")
        return True
    
    def test_03_personalized_experience_generation(self):
        """Test personalized experience generation"""
        print("\n🧪 Testing: Personalized Experience Generation")
        
        # Create test user
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # Generate personalized experience
        experience = self.user_system.get_personalized_experience(profile.user_id)
        
        # Validate experience structure
        self.assertIsNotNone(experience)
        self.assertIn('content_filters', experience)
        self.assertIn('recommendations', experience)
        self.assertIn('learning_path', experience)
        self.assertIn('collaboration_opportunities', experience)
        self.assertIn('local_relevance', experience)
        
        # Validate specific experience components
        self.assertIsInstance(experience['recommendations'], list)
        self.assertIsInstance(experience['learning_path'], dict)
        self.assertIn('focus_area', experience['learning_path'])
        
        print("✅ Personalized Experience Generation: PASSED")
        return True
    
    def test_04_contribution_creation(self):
        """Test contribution creation functionality"""
        print("\n🧪 Testing: Contribution Creation")
        
        # Create test user first
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # Create test contribution
        contribution_data = self.test_data.create_test_contribution_data()
        contribution = self.contribution_system.create_contribution(profile.user_id, contribution_data)
        
        # Validate contribution creation
        self.assertIsNotNone(contribution)
        self.assertEqual(contribution.metadata.title, 'Test Contribution')
        self.assertEqual(contribution.contribution_type, ContributionType.CONTENT)
        self.assertEqual(contribution.status, ContributionStatus.DRAFT)
        
        # Test contribution persistence
        retrieved_contribution = self.contribution_system.contribution_manager.get_contribution(contribution.contribution_id)
        self.assertIsNotNone(retrieved_contribution)
        self.assertEqual(retrieved_contribution.metadata.title, 'Test Contribution')
        
        print("✅ Contribution Creation: PASSED")
        return True
    
    def test_05_contribution_serialization(self):
        """Test contribution serialization and deserialization"""
        print("\n🧪 Testing: Contribution Serialization")
        
        # Create test user and contribution
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        contribution_data = self.test_data.create_test_contribution_data()
        contribution = self.contribution_system.create_contribution(profile.user_id, contribution_data)
        
        # Test to_dict serialization
        contribution_dict = contribution.to_dict()
        self.assertIsInstance(contribution_dict, dict)
        self.assertIn('contribution_id', contribution_dict)
        self.assertIn('metadata', contribution_dict)
        self.assertIn('contribution_type', contribution_dict)
        
        # Test from_dict deserialization
        reconstructed_contribution = Contribution.from_dict(contribution_dict)
        self.assertEqual(reconstructed_contribution.metadata.title, contribution.metadata.title)
        self.assertEqual(reconstructed_contribution.contribution_type, contribution.contribution_type)
        
        print("✅ Contribution Serialization: PASSED")
        return True
    
    def test_06_contribution_opportunity_matching(self):
        """Test contribution opportunity matching"""
        print("\n🧪 Testing: Contribution Opportunity Matching")
        
        # Create test user
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # Find contribution opportunities
        opportunities = self.contribution_system.find_opportunities(profile)
        
        # Validate opportunities
        self.assertIsInstance(opportunities, list)
        self.assertGreater(len(opportunities), 0)
        
        # Validate opportunity structure
        for opportunity in opportunities:
            self.assertIn('type', opportunity)
            self.assertIn('area', opportunity)
            self.assertIn('description', opportunity)
            self.assertIn('contribution_type', opportunity)
            self.assertIn('priority', opportunity)
        
        print("✅ Contribution Opportunity Matching: PASSED")
        return True
    
    def test_07_user_profile_updates(self):
        """Test user profile update functionality"""
        print("\n🧪 Testing: User Profile Updates")
        
        # Create test user
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # Update profile
        updates = {
            'identity': {'name': 'Updated Test User'},
            'interests': {'passion_areas': ['Updated passion area']}
        }
        
        success = self.user_system.update_user_preferences(profile.user_id, updates)
        self.assertTrue(success)
        
        # Verify updates
        updated_profile = self.user_system.profile_manager.get_profile(profile.user_id)
        self.assertEqual(updated_profile.core_identity.name, 'Updated Test User')
        self.assertIn('Updated passion area', updated_profile.interests.passion_areas)
        
        print("✅ User Profile Updates: PASSED")
        return True
    
    def test_08_session_state_management(self):
        """Test session state (vapor state) management"""
        print("\n🧪 Testing: Session State Management")
        
        # Create test user
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # First, get personalized experience to create the session
        experience = self.user_system.get_personalized_experience(profile.user_id)
        self.assertIsNotNone(experience)
        
        # Now update session state
        session_updates = {
            'current_focus': 'Test Focus',
            'temporary_interests': ['Temporary Interest 1', 'Temporary Interest 2']
        }
        
        success = self.user_system.update_session_state(profile.user_id, session_updates)
        self.assertTrue(success)
        
        # Verify session state was updated
        updated_experience = self.user_system.get_personalized_experience(profile.user_id)
        self.assertIsNotNone(updated_experience)
        
        print("✅ Session State Management: PASSED")
        return True
    
    def test_09_contribution_status_management(self):
        """Test contribution status management"""
        print("\n🧪 Testing: Contribution Status Management")
        
        # Create test user and contribution
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        contribution_data = self.test_data.create_test_contribution_data()
        contribution = self.contribution_system.create_contribution(profile.user_id, contribution_data)
        
        # Update contribution status
        success = self.contribution_system.update_contribution_status(
            contribution.contribution_id,
            ContributionStatus.APPROVED,
            reviewed_by='test_reviewer',
            review_notes='Test approval'
        )
        self.assertTrue(success)
        
        # Verify status update
        updated_contribution = self.contribution_system.contribution_manager.get_contribution(contribution.contribution_id)
        self.assertEqual(updated_contribution.status, ContributionStatus.APPROVED)
        self.assertEqual(updated_contribution.reviewed_by, 'test_reviewer')
        
        print("✅ Contribution Status Management: PASSED")
        return True
    
    def test_10_data_integrity_and_consistency(self):
        """Test data integrity and consistency across the system"""
        print("\n🧪 Testing: Data Integrity and Consistency")
        
        # Create test user
        user_data = self.test_data.create_test_user_data()
        profile = self.user_system.create_user_profile(user_data)
        
        # Create multiple contributions
        contributions = []
        for i in range(3):
            contribution_data = self.test_data.create_test_contribution_data()
            contribution_data['metadata']['title'] = f'Test Contribution {i+1}'
            contribution = self.contribution_system.create_contribution(profile.user_id, contribution_data)
            contributions.append(contribution)
        
        # Verify all contributions exist
        user_contributions = self.contribution_system.get_user_contributions(profile.user_id)
        self.assertEqual(len(user_contributions), 3)
        
        # Verify contribution IDs are unique
        contribution_ids = [c.contribution_id for c in user_contributions]
        self.assertEqual(len(contribution_ids), len(set(contribution_ids)))
        
        # Verify user profile consistency
        retrieved_profile = self.user_system.profile_manager.get_profile(profile.user_id)
        self.assertEqual(retrieved_profile.user_id, profile.user_id)
        self.assertEqual(retrieved_profile.core_identity.name, profile.core_identity.name)
        
        print("✅ Data Integrity and Consistency: PASSED")
        return True
    
    def test_11_error_handling_and_edge_cases(self):
        """Test error handling and edge cases"""
        print("\n🧪 Testing: Error Handling and Edge Cases")
        
        # Test with invalid user ID
        experience = self.user_system.get_personalized_experience('invalid_user_id')
        self.assertIsNone(experience)
        
        # Test with invalid contribution ID
        contribution = self.contribution_system.contribution_manager.get_contribution('invalid_contribution_id')
        self.assertIsNone(contribution)
        
        # Test profile update with invalid user ID
        success = self.user_system.update_user_preferences('invalid_user_id', {})
        self.assertFalse(success)
        
        # Test session state update with invalid user ID
        success = self.user_system.update_session_state('invalid_user_id', {})
        self.assertFalse(success)
        
        print("✅ Error Handling and Edge Cases: PASSED")
        return True
    
    def test_12_performance_and_scalability(self):
        """Test performance and scalability aspects"""
        print("\n🧪 Testing: Performance and Scalability")
        
        # Test creating multiple users
        start_time = datetime.now()
        user_ids = []
        
        for i in range(10):
            user_data = self.test_data.create_test_user_data()
            user_data['identity']['name'] = f'Test User {i+1}'
            profile = self.user_system.create_user_profile(user_data)
            user_ids.append(profile.user_id)
        
        creation_time = (datetime.now() - start_time).total_seconds()
        self.assertLess(creation_time, 5.0)  # Should create 10 users in under 5 seconds
        
        # Test retrieving multiple profiles
        start_time = datetime.now()
        for user_id in user_ids:
            profile = self.user_system.profile_manager.get_profile(user_id)
            self.assertIsNotNone(profile)
        
        retrieval_time = (datetime.now() - start_time).total_seconds()
        self.assertLess(retrieval_time, 2.0)  # Should retrieve 10 profiles in under 2 seconds
        
        print("✅ Performance and Scalability: PASSED")
        return True

class AutonomousFeatureTesting:
    """Autonomous feature testing system that runs before commits"""
    
    def __init__(self):
        self.test_suite = RegressionTestSuite()
        self.validator = FeatureValidator()
        self.test_results = []
    
    def run_regression_tests(self) -> Dict[str, Any]:
        """Run all regression tests"""
        print("🚀 Running Comprehensive Regression Test Suite...")
        print("=" * 60)
        
        # Get all test methods
        test_methods = [method for method in dir(self.test_suite) if method.startswith('test_')]
        
        # Run each test
        for test_method in sorted(test_methods):
            test_name = test_method.replace('test_', '').replace('_', ' ').title()
            print(f"\n🧪 Running: {test_name}")
            
            try:
                # Set up test environment
                self.test_suite.setUp()
                
                # Run the test
                test_result = getattr(self.test_suite, test_method)()
                
                # Record result
                self.test_results.append({
                    'test': test_name,
                    'method': test_method,
                    'status': 'PASSED' if test_result else 'FAILED',
                    'timestamp': datetime.now(timezone.utc).isoformat()
                })
                
                # Clean up
                self.test_suite.tearDown()
                
            except Exception as e:
                self.test_results.append({
                    'test': test_name,
                    'method': test_method,
                    'status': 'ERROR',
                    'timestamp': datetime.now(timezone.utc).isoformat(),
                    'error': str(e)
                })
                print(f"💥 {test_name}: ERROR - {str(e)}")
        
        return self.get_test_report()
    
    def get_test_report(self) -> Dict[str, Any]:
        """Get comprehensive test report"""
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if r['status'] == 'PASSED'])
        failed_tests = len([r for r in self.test_results if r['status'] == 'FAILED'])
        error_tests = len([r for r in self.test_results if r['status'] == 'ERROR'])
        
        return {
            'summary': {
                'total_tests': total_tests,
                'passed': passed_tests,
                'failed': failed_tests,
                'errors': error_tests,
                'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0
            },
            'results': self.test_results,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def can_commit(self) -> bool:
        """Determine if code can be safely committed"""
        return len([r for r in self.test_results if r['status'] in ['FAILED', 'ERROR']]) == 0
    
    def save_test_report(self, filename: str = None):
        """Save test report to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"regression_test_report_{timestamp}.json"
        
        report = self.get_test_report()
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Test report saved to: {filename}")

def main():
    """Run the regression test suite"""
    print("🌟 Living Codex Platform - Regression Test Suite")
    print("=" * 60)
    
    # Initialize autonomous testing
    autonomous_tester = AutonomousFeatureTesting()
    
    # Run regression tests
    test_report = autonomous_tester.run_regression_tests()
    
    # Display results
    print("\n" + "=" * 60)
    print("📊 REGRESSION TEST RESULTS")
    print("=" * 60)
    
    summary = test_report['summary']
    print(f"Total Tests: {summary['total_tests']}")
    print(f"Passed: {summary['passed']} ✅")
    print(f"Failed: {summary['failed']} ❌")
    print(f"Errors: {summary['errors']} 💥")
    print(f"Success Rate: {summary['success_rate']:.1f}%")
    
    # Display individual test results
    print("\n📋 DETAILED RESULTS:")
    for result in test_report['results']:
        status_icon = "✅" if result['status'] == 'PASSED' else "❌" if result['status'] == 'FAILED' else "💥"
        print(f"  {status_icon} {result['test']}: {result['status']}")
        if 'error' in result:
            print(f"     Error: {result['error']}")
    
    # Determine if commit is safe
    if autonomous_tester.can_commit():
        print("\n🎉 ALL TESTS PASSED - Safe to commit!")
        print("✅ Code quality maintained")
        print("✅ Features functional")
        print("✅ No regressions detected")
    else:
        print("\n🚨 TESTS FAILED - DO NOT COMMIT!")
        print("❌ Code quality compromised")
        print("❌ Features broken")
        print("❌ Regressions detected")
        print("\n🔧 Please fix all failing tests before committing.")
    
    # Save test report only when explicitly requested
    if len(sys.argv) > 1 and ('--save-report' in sys.argv or '--verbose' in sys.argv):
        autonomous_tester.save_test_report()
    # Skip saving test reports by default to avoid temporary files
    
    return autonomous_tester.can_commit()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
