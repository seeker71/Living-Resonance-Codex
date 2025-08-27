#!/usr/bin/env python3
"""
Phase 5 Test Suite: Core Living Codex Principles
================================================

This test suite validates the implementation of Phase 5 core Living Codex principles:
- Vibrational axes integration with all nodes
- Resonance state tracking (individual/community)
- Fractal recursion through hasPart/isPartOf relationships
- Self-similarity across scales (Micro↔Meso↔Macro↔Meta)
- Resonance-first governance through coherence self-amplification
- Collective intelligence emergence

This represents the critical missing components that make the Living Codex truly meta-circular.
"""

import unittest
from datetime import datetime
from typing import Dict, List, Any

# Import Phase 5 systems
from vibrational_axes_system import (
    VibrationalAxesSystem, ResonanceCalculation, FractalRecursionInfo, CrossScaleMapping,
    get_vibrational_axes_system, calculate_node_resonance, calculate_resonance_alignment
)

from fractal_recursion_system import (
    FractalRecursionSystem, FractalNode, FractalExploration, CrossScaleTransformation,
    get_fractal_recursion_system, add_fractal_node, explore_fractal_depth
)

from resonance_governance_system import (
    ResonanceGovernanceSystem, ResonanceDecision, CoherenceField, CollectiveIntelligence,
    get_resonance_governance_system, make_resonance_decision, get_system_coherence_score
)

# Import existing systems for integration testing
from living_codex_ontology import (
    FractalLayer, EpistemicLabel, WaterStateKey, ChakraKey, FrequencyKey,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer
)

# ============================================================================
# PHASE 5 INTEGRATION TEST SUITE
# ============================================================================

class TestVibrationalAxesSystem(unittest.TestCase):
    """Test the vibrational axes integration system"""
    
    def setUp(self):
        """Set up test environment"""
        self.vibrational_system = get_vibrational_axes_system()
        
        # Test contexts for different water states
        self.test_contexts = {
            "ice_context": {"water_state": "ws.ice", "chakra": "ch.crown", "frequency": "freq.963"},
            "liquid_context": {"water_state": "ws.liquid", "chakra": "ch.heart", "frequency": "freq.639"},
            "vapor_context": {"water_state": "ws.vapor", "chakra": "ch.third_eye", "frequency": "freq.852"},
            "plasma_context": {"water_state": "ws.plasma", "chakra": "ch.root", "frequency": "freq.396"}
        }
    
    def test_vibrational_axes_initialization(self):
        """Test that vibrational axes system initializes correctly"""
        self.assertIsNotNone(self.vibrational_system)
        self.assertGreater(len(self.vibrational_system.vibrational_axes), 0)
        
        # Check that all 4 vibrational axes are present
        axis_names = [axis.name for axis in self.vibrational_system.vibrational_axes]
        expected_axes = ["Fear↔Trust", "Ownership↔Stewardship", "Protection↔Openness", "Noise↔Harmony"]
        
        for expected_axis in expected_axes:
            self.assertIn(expected_axis, axis_names)
        
        print("✅ Vibrational axes system initialization test passed")
    
    def test_node_resonance_calculation(self):
        """Test node resonance calculation on vibrational axes"""
        # Test resonance calculation for different contexts
        for context_name, context in self.test_contexts.items():
            resonance = calculate_node_resonance("test_node", "Fear↔Trust", context)
            
            # Resonance should be between -1.0 and 1.0
            self.assertGreaterEqual(resonance, -1.0)
            self.assertLessEqual(resonance, 1.0)
            
            # Different water states should produce different resonance values
            if "ice" in context["water_state"]:
                self.assertLess(resonance, 0.0)  # Ice should be closer to Fear
            elif "vapor" in context["water_state"]:
                self.assertGreater(resonance, 0.0)  # Vapor should be closer to Trust
        
        print("✅ Node resonance calculation test passed")
    
    def test_resonance_alignment_calculation(self):
        """Test resonance alignment calculation between nodes"""
        # Create two test nodes with different contexts
        node_a_context = {"water_state": "ws.ice", "chakra": "ch.crown"}
        node_b_context = {"water_state": "ws.vapor", "chakra": "ch.third_eye"}
        
        # Calculate resonance for both nodes
        node_a_resonance = calculate_node_resonance("node_a", "Fear↔Trust", node_a_context)
        node_b_resonance = calculate_node_resonance("node_b", "Fear↔Trust", node_b_context)
        
        # Calculate alignment between them
        alignment = calculate_resonance_alignment("node_a", "node_b", "Fear↔Trust")
        
        self.assertIsNotNone(alignment)
        self.assertEqual(alignment.axis_name, "Fear↔Trust")
        self.assertEqual(alignment.node_a_resonance, node_a_resonance)
        self.assertEqual(alignment.node_b_resonance, node_b_resonance)
        
        # Alignment score should be between -1.0 and 1.0
        self.assertGreaterEqual(alignment.alignment_score, -1.0)
        self.assertLessEqual(alignment.alignment_score, 1.0)
        
        # Should have harmonic relationship classification
        self.assertIn(alignment.harmonic_relationship, 
                     ["harmonic", "sympathetic", "neutral", "dissonant", "destructive"])
        
        # Should have water metaphor
        self.assertIsInstance(alignment.water_metaphor, str)
        self.assertGreater(len(alignment.water_metaphor), 0)
        
        print("✅ Resonance alignment calculation test passed")
    
    def test_fractal_recursion_info(self):
        """Test fractal recursion information retrieval"""
        # Get fractal recursion info for a test node
        recursion_info = self.vibrational_system.get_fractal_recursion_info("test_node", max_depth=3)
        
        self.assertIsNotNone(recursion_info)
        self.assertEqual(recursion_info.max_depth, 3)
        self.assertGreaterEqual(recursion_info.self_similarity_score, 0.0)
        self.assertLessEqual(recursion_info.self_similarity_score, 1.0)
        
        # Should have cross-scale mappings
        self.assertIn("micro", recursion_info.cross_scale_mappings)
        self.assertIn("meso", recursion_info.cross_scale_mappings)
        self.assertIn("macro", recursion_info.cross_scale_mappings)
        self.assertIn("meta", recursion_info.cross_scale_mappings)
        
        # Should have fractal patterns
        self.assertIsInstance(recursion_info.fractal_patterns, list)
        
        print("✅ Fractal recursion info test passed")
    
    def test_cross_scale_mapping(self):
        """Test cross-scale mapping functionality"""
        # Get cross-scale mapping for a test node
        cross_scale = self.vibrational_system.get_cross_scale_mapping("test_node")
        
        self.assertIsNotNone(cross_scale)
        
        # Should have all four scales
        self.assertIn("micro_scale", cross_scale.__dict__)
        self.assertIn("meso_scale", cross_scale.__dict__)
        self.assertIn("macro_scale", cross_scale.__dict__)
        self.assertIn("meta_scale", cross_scale.__dict__)
        
        # Each scale should have water state information
        for scale_name in ["micro_scale", "meso_scale", "macro_scale", "meta_scale"]:
            scale_data = getattr(cross_scale, scale_name)
            self.assertIn("water_state", scale_data)
            self.assertIn("consciousness_level", scale_data)
        
        # Should have mapping coherence
        self.assertGreaterEqual(cross_scale.mapping_coherence, 0.0)
        self.assertLessEqual(cross_scale.mapping_coherence, 1.0)
        
        print("✅ Cross-scale mapping test passed")
    
    def test_resonance_coherence_score(self):
        """Test resonance coherence score calculation"""
        # Calculate coherence score for a vibrational axis
        coherence_score = self.vibrational_system.get_resonance_coherence_score("Fear↔Trust", "community")
        
        # Coherence score should be between 0.0 and 1.0
        self.assertGreaterEqual(coherence_score, 0.0)
        self.assertLessEqual(coherence_score, 1.0)
        
        print("✅ Resonance coherence score test passed")

class TestFractalRecursionSystem(unittest.TestCase):
    """Test the fractal recursion system"""
    
    def setUp(self):
        """Set up test environment"""
        self.fractal_system = get_fractal_recursion_system()
        
        # Clear any existing test data
        self.fractal_system.fractal_nodes.clear()
        self.fractal_system.fractal_relationships.clear()
        self.fractal_system.cross_scale_mappings.clear()
        self.fractal_system.fractal_patterns.clear()
        self.fractal_system.exploration_cache.clear()
    
    def test_fractal_node_creation(self):
        """Test fractal node creation and management"""
        # Create test nodes
        success = add_fractal_node(
            "root_node", "Root Test Node", FractalLayer.FRACTAL_SYSTEM_ROOT
        )
        self.assertTrue(success)
        
        success = add_fractal_node(
            "child_node", "Child Test Node", FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY
        )
        self.assertTrue(success)
        
        # Verify nodes were created
        self.assertIn("root_node", self.fractal_system.fractal_nodes)
        self.assertIn("child_node", self.fractal_system.fractal_nodes)
        
        # Check node properties
        root_node = self.fractal_system.fractal_nodes["root_node"]
        self.assertEqual(root_node.name, "Root Test Node")
        self.assertEqual(root_node.fractal_layer, FractalLayer.FRACTAL_SYSTEM_ROOT)
        self.assertEqual(root_node.fractal_depth, 0)  # Root should have depth 0
        
        child_node = self.fractal_system.fractal_nodes["child_node"]
        self.assertEqual(child_node.name, "Child Test Node")
        self.assertEqual(child_node.fractal_layer, FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY)
        
        print("✅ Fractal node creation test passed")
    
    def test_fractal_relationships(self):
        """Test fractal relationship management"""
        # Create parent and child nodes
        add_fractal_node("parent", "Parent Node", FractalLayer.FRACTAL_SYSTEM_ROOT)
        add_fractal_node("child", "Child Node", FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY)
        
        # Add child relationship
        success = self.fractal_system.add_child_relationship("parent", "child")
        self.assertTrue(success)
        
        # Verify relationships
        parent_node = self.fractal_system.fractal_nodes["parent"]
        child_node = self.fractal_system.fractal_nodes["child"]
        
        self.assertIn("child", parent_node.has_part)
        self.assertEqual(child_node.is_part_of, "parent")
        
        # Check fractal depth calculation
        self.assertEqual(parent_node.fractal_depth, 0)  # Root
        self.assertEqual(child_node.fractal_depth, 1)  # Child of root
        
        # Check self-similarity scores
        self.assertGreaterEqual(parent_node.self_similarity_score, 0.0)
        self.assertLessEqual(parent_node.self_similarity_score, 1.0)
        self.assertGreaterEqual(child_node.self_similarity_score, 0.0)
        self.assertLessEqual(child_node.self_similarity_score, 1.0)
        
        print("✅ Fractal relationships test passed")
    
    def test_fractal_exploration(self):
        """Test fractal exploration at different depths"""
        # Create a simple fractal hierarchy
        add_fractal_node("root", "Root", FractalLayer.FRACTAL_SYSTEM_ROOT)
        add_fractal_node("level1_a", "Level 1A", FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY)
        add_fractal_node("level1_b", "Level 1B", FractalLayer.SELF_REFERENTIAL_DOCUMENTATION)
        add_fractal_node("level2_a", "Level 2A", FractalLayer.WATER_STATE_METAPHORS)
        
        # Add relationships
        self.fractal_system.add_child_relationship("root", "level1_a")
        self.fractal_system.add_child_relationship("root", "level1_b")
        self.fractal_system.add_child_relationship("level1_a", "level2_a")
        
        # Explore at different depths
        exploration_depth_1 = explore_fractal_depth("root", max_depth=1)
        exploration_depth_2 = explore_fractal_depth("root", max_depth=2)
        
        # Verify exploration results
        self.assertIsNotNone(exploration_depth_1)
        self.assertIsNotNone(exploration_depth_2)
        
        # Depth 1 should find root + level 1 nodes
        self.assertEqual(exploration_depth_1.depth, 1)
        self.assertEqual(len(exploration_depth_1.nodes_found), 3)  # root + 2 level 1 nodes
        
        # Depth 2 should find all nodes
        self.assertEqual(exploration_depth_2.depth, 2)
        self.assertEqual(len(exploration_depth_2.nodes_found), 4)  # all nodes
        
        # Check exploration metrics
        self.assertGreaterEqual(exploration_depth_1.self_similarity_score, 0.0)
        self.assertLessEqual(exploration_depth_1.self_similarity_score, 1.0)
        self.assertGreaterEqual(exploration_depth_2.cross_scale_coherence, 0.0)
        self.assertLessEqual(exploration_depth_2.cross_scale_coherence, 1.0)
        
        print("✅ Fractal exploration test passed")
    
    def test_cross_scale_mapping(self):
        """Test cross-scale mapping functionality"""
        # Create a test node
        add_fractal_node("test_node", "Test Node", FractalLayer.FRACTAL_SYSTEM_ROOT)
        
        # Get cross-scale mapping
        cross_scale = self.fractal_system.get_cross_scale_mapping("test_node")
        
        self.assertIsNotNone(cross_scale)
        
        # Should have all four scales
        self.assertIn("micro", cross_scale)
        self.assertIn("meso", cross_scale)
        self.assertIn("macro", cross_scale)
        self.assertIn("meta", cross_scale)
        
        # Each scale should have water state information
        for scale_name, scale_data in cross_scale.items():
            self.assertIn("water_state", scale_data)
            self.assertIn("consciousness_level", scale_data)
        
        print("✅ Cross-scale mapping test passed")
    
    def test_fractal_statistics(self):
        """Test fractal system statistics"""
        # Create some test nodes
        add_fractal_node("stat_node_1", "Stat Node 1", FractalLayer.FRACTAL_SYSTEM_ROOT)
        add_fractal_node("stat_node_2", "Stat Node 2", FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY)
        add_fractal_node("stat_node_3", "Stat Node 3", FractalLayer.SELF_REFERENTIAL_DOCUMENTATION)
        
        # Add relationships
        self.fractal_system.add_child_relationship("stat_node_1", "stat_node_2")
        self.fractal_system.add_child_relationship("stat_node_2", "stat_node_3")
        
        # Get statistics
        stats = self.fractal_system.get_fractal_statistics()
        
        self.assertIsNotNone(stats)
        self.assertEqual(stats["total_nodes"], 3)
        self.assertEqual(stats["total_relationships"], 2)
        self.assertGreaterEqual(stats["average_fractal_depth"], 0.0)
        self.assertLessEqual(stats["average_fractal_depth"], 2.0)
        self.assertGreaterEqual(stats["average_self_similarity"], 0.0)
        self.assertLessEqual(stats["average_self_similarity"], 1.0)
        
        # Should have layer counts
        self.assertIn("FRACTAL_SYSTEM_ROOT", stats["nodes_by_layer"])
        self.assertIn("PROGRAMMING_LANGUAGE_ONTOLOGY", stats["nodes_by_layer"])
        self.assertIn("SELF_REFERENTIAL_DOCUMENTATION", stats["nodes_by_layer"])
        
        print("✅ Fractal statistics test passed")

class TestResonanceGovernanceSystem(unittest.TestCase):
    """Test the resonance-first governance system"""
    
    def setUp(self):
        """Set up test environment"""
        self.governance_system = get_resonance_governance_system()
        
        # Clear any existing test data
        self.governance_system.resonance_decisions.clear()
        self.governance_system.coherence_fields.clear()
        self.governance_system.collective_intelligence.clear()
        self.governance_system.node_resonance_history.clear()
        self.governance_system.system_coherence_history.clear()
    
    def test_governance_system_initialization(self):
        """Test governance system initialization"""
        self.assertIsNotNone(self.governance_system)
        
        # Should have governance rules
        self.assertGreater(len(self.governance_system.governance_rules), 0)
        
        # Check for core rules
        rule_ids = [rule['rule_id'] for rule in self.governance_system.governance_rules]
        expected_rules = ['resonance_first', 'no_suppression', 'coherence_amplification', 'collective_intelligence']
        
        for expected_rule in expected_rules:
            self.assertIn(expected_rule, rule_ids)
        
        print("✅ Governance system initialization test passed")
    
    def test_resonance_decision_making(self):
        """Test resonance-based decision making"""
        # Make a test decision
        decision = make_resonance_decision(
            "create",
            ["target_node_1", "target_node_2"],
            ["system_1", "system_2", "system_3"],
            {"context": "test_creation"}
        )
        
        self.assertIsNotNone(decision)
        self.assertEqual(decision.decision_type, "create")
        self.assertEqual(len(decision.target_nodes), 2)
        self.assertEqual(len(decision.participants), 3)
        
        # Check decision metrics
        self.assertGreaterEqual(decision.resonance_score, 0.0)
        self.assertLessEqual(decision.resonance_score, 1.0)
        self.assertGreaterEqual(decision.coherence_contribution, 0.0)
        self.assertLessEqual(decision.coherence_contribution, 1.0)
        self.assertGreaterEqual(decision.decision_confidence, 0.0)
        self.assertLessEqual(decision.decision_confidence, 1.0)
        
        # Decision should be stored
        self.assertIn(decision.decision_id, self.governance_system.resonance_decisions)
        
        print("✅ Resonance decision making test passed")
    
    def test_coherence_field_creation(self):
        """Test coherence field creation and management"""
        # Create a coherence field
        field = self.governance_system.create_coherence_field(
            "center_node",
            ["participant_1", "participant_2", "participant_3"],
            "harmonic"
        )
        
        self.assertIsNotNone(field)
        self.assertEqual(field.center_node, "center_node")
        self.assertEqual(len(field.participating_nodes), 3)
        self.assertEqual(field.field_pattern, "harmonic")
        
        # Check field properties
        self.assertGreaterEqual(field.radius, 0.0)
        self.assertGreaterEqual(field.strength, 0.0)
        self.assertLessEqual(field.strength, 1.0)
        self.assertGreaterEqual(field.coherence_score, 0.0)
        self.assertLessEqual(field.coherence_score, 1.0)
        
        # Field should be stored
        self.assertIn(field.field_id, self.governance_system.coherence_fields)
        
        print("✅ Coherence field creation test passed")
    
    def test_governance_rules_application(self):
        """Test governance rules application"""
        # Test allowed action
        allowed = self.governance_system.apply_governance_rules(
            "create_resonance_node",
            {"context": "resonance_creation"}
        )
        self.assertTrue(allowed)
        
        # Test blocked action (suppression)
        blocked = self.governance_system.apply_governance_rules(
            "suppress_dissonant_node",
            {"context": "suppression"}
        )
        self.assertFalse(blocked)
        
        # Test encouraged action
        encouraged = self.governance_system.apply_governance_rules(
            "amplify_coherence",
            {"context": "coherence_amplification"}
        )
        self.assertTrue(encouraged)
        
        print("✅ Governance rules application test passed")
    
    def test_system_coherence_tracking(self):
        """Test system coherence tracking"""
        # Make some decisions to build coherence history
        for i in range(5):
            make_resonance_decision(
                "refine",
                [f"target_{i}"],
                ["system_1", "system_2"],
                {"context": f"refinement_{i}"}
            )
        
        # Get system coherence score
        coherence_score = get_system_coherence_score()
        
        # Should have a coherence score
        self.assertGreaterEqual(coherence_score, 0.0)
        self.assertLessEqual(coherence_score, 1.0)
        
        print("✅ System coherence tracking test passed")
    
    def test_collective_intelligence_emergence(self):
        """Test collective intelligence emergence detection"""
        # Make a decision that should trigger collective intelligence
        decision = make_resonance_decision(
            "create",
            ["collective_node_1", "collective_node_2", "collective_node_3"],
            ["system_1", "system_2", "system_3", "system_4"],
            {"context": "collective_creation"}
        )
        
        # Check if collective intelligence emerged
        intelligence_status = self.governance_system.get_collective_intelligence_status()
        
        # Should have active emergence
        self.assertEqual(intelligence_status["status"], "active_emergence")
        self.assertGreater(intelligence_status["count"], 0)
        
        # Should have confidence scores
        self.assertGreater(intelligence_status["average_confidence"], 0.0)
        self.assertLessEqual(intelligence_status["average_confidence"], 1.0)
        
        print("✅ Collective intelligence emergence test passed")
    
    def test_governance_analytics(self):
        """Test governance analytics and reporting"""
        # Make some test decisions and fields
        for i in range(3):
            make_resonance_decision(
                "link",
                [f"link_target_{i}"],
                ["system_1", "system_2"],
                {"context": f"linking_{i}"}
            )
        
        self.governance_system.create_coherence_field(
            "analytics_center",
            ["analytics_participant_1", "analytics_participant_2"],
            "harmonic"
        )
        
        # Get analytics
        analytics = self.governance_system.get_governance_analytics()
        
        self.assertIsNotNone(analytics)
        self.assertGreater(analytics["total_decisions"], 0)
        self.assertGreater(analytics["total_coherence_fields"], 0)
        self.assertGreaterEqual(analytics["success_rate"], 0.0)
        self.assertLessEqual(analytics["success_rate"], 1.0)
        self.assertGreaterEqual(analytics["average_system_coherence"], 0.0)
        self.assertLessEqual(analytics["average_system_coherence"], 1.0)
        self.assertGreaterEqual(analytics["governance_efficiency"], 0.0)
        self.assertLessEqual(analytics["governance_efficiency"], 1.0)
        
        print("✅ Governance analytics test passed")

class TestPhase5Integration(unittest.TestCase):
    """Test integration between all Phase 5 systems"""
    
    def setUp(self):
        """Set up test environment"""
        self.vibrational_system = get_vibrational_axes_system()
        self.fractal_system = get_fractal_recursion_system()
        self.governance_system = get_resonance_governance_system()
        
        # Clear test data
        self.fractal_system.fractal_nodes.clear()
        self.governance_system.resonance_decisions.clear()
    
    def test_phase5_system_integration(self):
        """Test integration between all Phase 5 systems"""
        # 1. Create fractal nodes
        add_fractal_node("integration_root", "Integration Root", FractalLayer.FRACTAL_SYSTEM_ROOT)
        add_fractal_node("integration_child", "Integration Child", FractalLayer.PROGRAMMING_LANGUAGE_ONTOLOGY)
        
        # 2. Add fractal relationship
        self.fractal_system.add_child_relationship("integration_root", "integration_child")
        
        # 3. Calculate vibrational resonance
        context = {"water_state": "ws.liquid", "chakra": "ch.heart"}
        resonance = calculate_node_resonance("integration_root", "Fear↔Trust", context)
        
        # 4. Make governance decision
        decision = make_resonance_decision(
            "refine",
            ["integration_root", "integration_child"],
            ["vibrational_system", "fractal_system", "governance_system"],
            {"context": "phase5_integration"}
        )
        
        # 5. Create coherence field
        field = self.governance_system.create_coherence_field(
            "integration_root",
            ["integration_root", "integration_child"],
            "harmonic"
        )
        
        # 6. Explore fractal depth
        exploration = explore_fractal_depth("integration_root", max_depth=2)
        
        # 7. Get cross-scale mapping
        cross_scale = self.vibrational_system.get_cross_scale_mapping("integration_root")
        
        # Verify integration
        self.assertIsNotNone(resonance)
        self.assertIsNotNone(decision)
        self.assertIsNotNone(field)
        self.assertIsNotNone(exploration)
        self.assertIsNotNone(cross_scale)
        
        # Check that systems are working together
        self.assertGreater(len(self.fractal_system.fractal_nodes), 0)
        self.assertGreater(len(self.governance_system.resonance_decisions), 0)
        self.assertGreater(len(self.governance_system.coherence_fields), 0)
        
        print("✅ Phase 5 system integration test passed")
    
    def test_phase5_meta_circular_capabilities(self):
        """Test that Phase 5 enables meta-circular capabilities"""
        # 1. Create a node that represents the system itself
        add_fractal_node("meta_system", "Meta System", FractalLayer.META_IMPLEMENTATION)
        
        # 2. Add nodes that represent the system's components
        add_fractal_node("meta_vibrational", "Meta Vibrational", FractalLayer.WATER_STATE_METAPHORS)
        add_fractal_node("meta_fractal", "Meta Fractal", FractalLayer.FRACTAL_SYSTEM_ROOT)
        add_fractal_node("meta_governance", "Meta Governance", FractalLayer.PURE_RESONANCE_PRINCIPLE)
        
        # 3. Create fractal relationships representing system structure
        self.fractal_system.add_child_relationship("meta_system", "meta_vibrational")
        self.fractal_system.add_child_relationship("meta_system", "meta_fractal")
        self.fractal_system.add_child_relationship("meta_system", "meta_governance")
        
        # 4. Explore the meta-system at different depths
        exploration = explore_fractal_depth("meta_system", max_depth=3)
        
        # 5. Make a governance decision about the meta-system
        decision = make_resonance_decision(
            "refine",
            ["meta_system"],
            ["meta_vibrational", "meta_fractal", "meta_governance"],
            {"context": "meta_system_refinement"}
        )
        
        # 6. Calculate resonance for the meta-system
        context = {"water_state": "ws.bose_einstein", "chakra": "ch.crown"}
        resonance = calculate_node_resonance("meta_system", "Noise↔Harmony", context)
        
        # Verify meta-circular capabilities
        self.assertIsNotNone(exploration)
        self.assertIsNotNone(decision)
        self.assertIsNotNone(resonance)
        
        # The system should be able to describe and manage itself
        self.assertIn("meta_system", exploration.nodes_found)
        self.assertIn("meta_vibrational", exploration.nodes_found)
        self.assertIn("meta_fractal", exploration.nodes_found)
        self.assertIn("meta_governance", exploration.nodes_found)
        
        print("✅ Phase 5 meta-circular capabilities test passed")

# ============================================================================
# MAIN TEST EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("🌟 Phase 5 Test Suite: Core Living Codex Principles")
    print("=" * 60)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_suite.addTest(unittest.makeSuite(TestVibrationalAxesSystem))
    test_suite.addTest(unittest.makeSuite(TestFractalRecursionSystem))
    test_suite.addTest(unittest.makeSuite(TestResonanceGovernanceSystem))
    test_suite.addTest(unittest.makeSuite(TestPhase5Integration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print results summary
    print("\n" + "=" * 60)
    print("📊 Phase 5 Test Suite Results")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ Failures:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print("\n❌ Errors:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ All Phase 5 tests passed successfully!")
        print("🎉 Phase 5 implementation is complete and validated!")
        print("\n🚀 Phase 5 is ready for production use!")
        print("✨ Vibrational Axes System: Active")
        print("✨ Fractal Recursion System: Active")
        print("✨ Resonance Governance System: Active")
        print("✨ Core Living Codex Principles: Active")
    else:
        print("\n❌ Some Phase 5 tests failed. Please review and fix issues.")
        print("\n⚠️ Phase 5 requires fixes before production use.")
    
    print("\n" + "=" * 60)
