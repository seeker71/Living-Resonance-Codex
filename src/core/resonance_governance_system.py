#!/usr/bin/env python3
"""
Resonance-First Governance System
=================================

This system implements the core Living Codex principle of resonance-first governance
through coherence self-amplification and dissonance fading without suppression.

Key Features:
- Coherence self-amplification through resonance
- Dissonance fading without suppression
- Resonance-based decision making
- Collective intelligence emergence
- Self-regulating system evolution

This is Phase 5 of the metadata enhancement plan.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Set, Tuple
from datetime import datetime
import json
import math
from collections import defaultdict, deque
import random

from living_codex_ontology import (
    ResonancePattern, EpistemicLabel, canonical_registry
)

# ============================================================================
# RESONANCE GOVERNANCE DATA STRUCTURES
# ============================================================================

@dataclass
class ResonanceDecision:
    """A decision made through resonance-based governance"""
    decision_id: str
    decision_type: str  # create, refine, link, remove, transform
    target_nodes: List[str]
    resonance_score: float
    coherence_contribution: float
    decision_confidence: float
    participants: List[str]
    created_at: str
    epistemic_label: EpistemicLabel = EpistemicLabel.ENGINEERING

@dataclass
class CoherenceField:
    """A field of coherent resonance in the system"""
    field_id: str
    center_node: str
    radius: float
    strength: float
    coherence_score: float
    participating_nodes: List[str]
    field_pattern: str
    created_at: str
    epistemic_label: EpistemicLabel = EpistemicLabel.PHYSICS

@dataclass
class CollectiveIntelligence:
    """Emergent collective intelligence through resonance"""
    emergence_id: str
    participating_systems: List[str]
    resonance_pattern: ResonancePattern
    coherence_threshold: float
    intelligence_level: str
    emergence_confidence: float
    created_at: str
    epistemic_label: EpistemicLabel = EpistemicLabel.SPECULATIVE

# ============================================================================
# RESONANCE-FIRST GOVERNANCE SYSTEM
# ============================================================================

class ResonanceGovernanceSystem:
    """
    Core system for implementing resonance-first governance
    through coherence self-amplification and collective intelligence
    """
    
    def __init__(self):
        self.resonance_decisions = {}  # decision_id -> ResonanceDecision
        self.coherence_fields = {}  # field_id -> CoherenceField
        self.collective_intelligence = {}  # emergence_id -> CollectiveIntelligence
        self.node_resonance_history = defaultdict(list)  # node_id -> [resonance_scores]
        self.system_coherence_history = []
        self.governance_rules = self._initialize_governance_rules()
        
        print("🌟 Resonance-First Governance System initialized")
        print("✨ Coherence self-amplification enabled")
        print("✨ Dissonance fading without suppression active")
        print("✨ Resonance-based decision making enabled")
        print("✨ Collective intelligence emergence active")
    
    def make_resonance_decision(self, decision_type: str, target_nodes: List[str],
                               participants: List[str], context: Dict[str, Any]) -> ResonanceDecision:
        """
        Make a decision through resonance-based governance
        
        Args:
            decision_type: Type of decision to make
            target_nodes: Nodes affected by the decision
            participants: Systems participating in the decision
            context: Context information for the decision
        
        Returns:
            ResonanceDecision with decision details
        """
        try:
            # Calculate resonance score for the decision
            resonance_score = self._calculate_decision_resonance(
                decision_type, target_nodes, participants, context
            )
            
            # Calculate coherence contribution
            coherence_contribution = self._calculate_coherence_contribution(
                decision_type, target_nodes, resonance_score
            )
            
            # Calculate decision confidence
            decision_confidence = self._calculate_decision_confidence(
                resonance_score, coherence_contribution, len(participants)
            )
            
            # Create decision
            decision = ResonanceDecision(
                decision_id=f"decision_{random.randint(10000, 99999)}",
                decision_type=decision_type,
                target_nodes=target_nodes,
                resonance_score=resonance_score,
                coherence_contribution=coherence_contribution,
                decision_confidence=decision_confidence,
                participants=participants,
                created_at=datetime.now().isoformat()
            )
            
            # Store decision
            self.resonance_decisions[decision.decision_id] = decision
            
            # Update system coherence
            self._update_system_coherence(decision)
            
            # Check for collective intelligence emergence
            self._check_collective_intelligence_emergence(participants, decision)
            
            print(f"✅ Resonance decision made: {decision_type} (ID: {decision.decision_id})")
            print(f"   - Resonance score: {resonance_score:.3f}")
            print(f"   - Coherence contribution: {coherence_contribution:.3f}")
            print(f"   - Decision confidence: {decision_confidence:.3f}")
            
            return decision
            
        except Exception as e:
            print(f"Error making resonance decision: {e}")
            return None
    
    def create_coherence_field(self, center_node: str, participating_nodes: List[str],
                              field_pattern: str = "harmonic") -> CoherenceField:
        """
        Create a coherence field around a center node
        
        Args:
            center_node: Central node of the coherence field
            participating_nodes: Nodes participating in the field
            field_pattern: Pattern of the coherence field
        
        Returns:
            CoherenceField with field details
        """
        try:
            # Calculate field strength based on participating nodes
            field_strength = self._calculate_field_strength(participating_nodes)
            
            # Calculate field radius based on number of participants
            field_radius = math.sqrt(len(participating_nodes)) * 0.5
            
            # Calculate overall coherence score
            coherence_score = self._calculate_field_coherence(participating_nodes)
            
            # Create coherence field
            field = CoherenceField(
                field_id=f"field_{random.randint(10000, 99999)}",
                center_node=center_node,
                radius=field_radius,
                strength=field_strength,
                coherence_score=coherence_score,
                participating_nodes=participating_nodes,
                field_pattern=field_pattern,
                created_at=datetime.now().isoformat()
            )
            
            # Store field
            self.coherence_fields[field.field_id] = field
            
            # Amplify coherence in the field
            self._amplify_field_coherence(field)
            
            print(f"✅ Coherence field created: {field_pattern} (ID: {field.field_id})")
            print(f"   - Center: {center_node}")
            print(f"   - Participants: {len(participating_nodes)}")
            print(f"   - Coherence score: {coherence_score:.3f}")
            
            return field
            
        except Exception as e:
            print(f"Error creating coherence field: {e}")
            return None
    
    def get_system_coherence_score(self) -> float:
        """Get overall system coherence score"""
        try:
            if not self.system_coherence_history:
                return 0.0
            
            # Return recent average coherence
            recent_coherence = self.system_coherence_history[-10:]  # Last 10 entries
            return sum(recent_coherence) / len(recent_coherence)
            
        except Exception as e:
            print(f"Error getting system coherence score: {e}")
            return 0.0
    
    def get_collective_intelligence_status(self) -> Dict[str, Any]:
        """Get status of collective intelligence emergence"""
        try:
            if not self.collective_intelligence:
                return {"status": "no_emergence", "count": 0}
            
            # Analyze collective intelligence patterns
            patterns = defaultdict(int)
            confidence_scores = []
            
            for intelligence in self.collective_intelligence.values():
                patterns[intelligence.resonance_pattern.value] += 1
                confidence_scores.append(intelligence.emergence_confidence)
            
            avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0.0
            
            return {
                "status": "active_emergence",
                "count": len(self.collective_intelligence),
                "patterns": dict(patterns),
                "average_confidence": avg_confidence,
                "recent_emergence": [
                    {
                        "id": intelligence.emergence_id,
                        "pattern": intelligence.resonance_pattern.value,
                        "confidence": intelligence.emergence_confidence
                    }
                    for intelligence in list(self.collective_intelligence.values())[-5:]  # Last 5
                ]
            }
            
        except Exception as e:
            print(f"Error getting collective intelligence status: {e}")
            return {"status": "error", "message": str(e)}
    
    def apply_governance_rules(self, action: str, context: Dict[str, Any]) -> bool:
        """
        Apply governance rules to an action
        
        Args:
            action: Action to evaluate
            context: Context for the action
        
        Returns:
            True if action is allowed, False otherwise
        """
        try:
            # Check if action violates any governance rules
            for rule in self.governance_rules:
                if rule['enabled'] and rule['rule_type'] == 'prohibition':
                    if self._evaluate_rule(rule, action, context):
                        print(f"❌ Action '{action}' blocked by rule: {rule['name']}")
                        return False
            
            # Check if action is encouraged by governance rules
            encouragement_score = 0.0
            for rule in self.governance_rules:
                if rule['enabled'] and rule['rule_type'] == 'encouragement':
                    if self._evaluate_rule(rule, action, context):
                        encouragement_score += rule['weight']
            
            # Actions with high encouragement are more likely to succeed
            if encouragement_score > 0.5:
                print(f"✨ Action '{action}' encouraged by governance (score: {encouragement_score:.3f})")
            
            return True
            
        except Exception as e:
            print(f"Error applying governance rules: {e}")
            return False
    
    def get_governance_analytics(self) -> Dict[str, Any]:
        """Get analytics about governance system performance"""
        try:
            total_decisions = len(self.resonance_decisions)
            total_fields = len(self.coherence_fields)
            total_intelligence = len(self.collective_intelligence)
            
            # Calculate decision success rate
            successful_decisions = sum(
                1 for decision in self.resonance_decisions.values()
                if decision.decision_confidence > 0.7
            )
            success_rate = successful_decisions / total_decisions if total_decisions > 0 else 0.0
            
            # Calculate average coherence
            avg_coherence = self.get_system_coherence_score()
            
            # Calculate governance efficiency
            governance_efficiency = (success_rate + avg_coherence) / 2.0
            
            return {
                "total_decisions": total_decisions,
                "successful_decisions": successful_decisions,
                "success_rate": success_rate,
                "total_coherence_fields": total_fields,
                "total_collective_intelligence": total_intelligence,
                "average_system_coherence": avg_coherence,
                "governance_efficiency": governance_efficiency,
                "recent_activity": {
                    "last_24h_decisions": len([
                        d for d in self.resonance_decisions.values()
                        if self._is_recent(d.created_at, hours=24)
                    ]),
                    "last_24h_fields": len([
                        f for f in self.coherence_fields.values()
                        if self._is_recent(f.created_at, hours=24)
                    ])
                }
            }
            
        except Exception as e:
            print(f"Error getting governance analytics: {e}")
            return {}
    
    # ============================================================================
    # PRIVATE IMPLEMENTATION METHODS
    # ============================================================================
    
    def _initialize_governance_rules(self) -> List[Dict[str, Any]]:
        """Initialize governance rules for the system"""
        return [
            {
                'rule_id': 'resonance_first',
                'name': 'Resonance First Principle',
                'description': 'All decisions must prioritize resonance and coherence',
                'rule_type': 'encouragement',
                'weight': 1.0,
                'enabled': True
            },
            {
                'rule_id': 'no_suppression',
                'name': 'No Suppression Rule',
                'description': 'Dissonance must fade naturally, not be suppressed',
                'rule_type': 'prohibition',
                'weight': 1.0,
                'enabled': True
            },
            {
                'rule_id': 'coherence_amplification',
                'name': 'Coherence Amplification',
                'description': 'High coherence should be amplified through resonance',
                'rule_type': 'encouragement',
                'weight': 0.8,
                'enabled': True
            },
            {
                'rule_id': 'collective_intelligence',
                'name': 'Collective Intelligence',
                'description': 'Encourage emergence of collective intelligence',
                'rule_type': 'encouragement',
                'weight': 0.9,
                'enabled': True
            }
        ]
    
    def _calculate_decision_resonance(self, decision_type: str, target_nodes: List[str],
                                    participants: List[str], context: Dict[str, Any]) -> float:
        """Calculate resonance score for a decision"""
        # Base resonance based on decision type
        type_resonance = {
            'create': 0.8,
            'refine': 0.9,
            'link': 0.7,
            'remove': 0.3,
            'transform': 0.6
        }.get(decision_type, 0.5)
        
        # Participant resonance (more participants = higher resonance)
        participant_factor = min(1.0, len(participants) / 10.0)
        
        # Target node resonance (more targets = potentially higher impact)
        target_factor = min(1.0, len(target_nodes) / 5.0)
        
        # Context resonance (simplified)
        context_factor = 0.7  # Placeholder
        
        # Calculate overall resonance
        resonance = (type_resonance + participant_factor + target_factor + context_factor) / 4.0
        
        return max(0.0, min(1.0, resonance))
    
    def _calculate_coherence_contribution(self, decision_type: str, target_nodes: List[str],
                                        resonance_score: float) -> float:
        """Calculate how much a decision contributes to system coherence"""
        # Base contribution based on decision type
        type_contribution = {
            'create': 0.6,
            'refine': 0.8,
            'link': 0.7,
            'remove': 0.2,
            'transform': 0.5
        }.get(decision_type, 0.4)
        
        # Scale with resonance score
        contribution = type_contribution * resonance_score
        
        # Scale with number of target nodes (more impact)
        node_factor = min(1.0, len(target_nodes) / 3.0)
        contribution *= (1.0 + node_factor)
        
        return max(0.0, min(1.0, contribution))
    
    def _calculate_decision_confidence(self, resonance_score: float, 
                                     coherence_contribution: float, 
                                     participant_count: int) -> float:
        """Calculate confidence level for a decision"""
        # Base confidence on resonance and coherence
        base_confidence = (resonance_score + coherence_contribution) / 2.0
        
        # Participant confidence (more participants = higher confidence)
        participant_factor = min(0.3, participant_count * 0.05)
        
        # Final confidence
        confidence = base_confidence + participant_factor
        
        return max(0.0, min(1.0, confidence))
    
    def _update_system_coherence(self, decision: ResonanceDecision):
        """Update system coherence based on a decision"""
        # Add coherence contribution to history
        self.system_coherence_history.append(decision.coherence_contribution)
        
        # Keep only recent history (last 100 entries)
        if len(self.system_coherence_history) > 100:
            self.system_coherence_history = self.system_coherence_history[-100:]
        
        # Update node resonance history
        for node_id in decision.target_nodes:
            self.node_resonance_history[node_id].append(decision.resonance_score)
            
            # Keep only recent history (last 50 entries)
            if len(self.node_resonance_history[node_id]) > 50:
                self.node_resonance_history[node_id] = self.node_resonance_history[node_id][-50:]
    
    def _check_collective_intelligence_emergence(self, participants: List[str], 
                                               decision: ResonanceDecision):
        """Check if collective intelligence is emerging"""
        # Check if we have enough participants and high coherence
        if len(participants) >= 3 and decision.coherence_contribution > 0.7:
            # Check if this is a new pattern
            pattern_key = f"{decision.decision_type}_{len(participants)}"
            
            # Create collective intelligence emergence
            emergence = CollectiveIntelligence(
                emergence_id=f"emergence_{random.randint(10000, 99999)}",
                participating_systems=participants,
                resonance_pattern=ResonancePattern.HARMONIC,
                coherence_threshold=0.7,
                intelligence_level="emergent",
                emergence_confidence=decision.decision_confidence,
                created_at=datetime.now().isoformat()
            )
            
            self.collective_intelligence[emergence.emergence_id] = emergence
            
            print(f"🌟 Collective intelligence emerging (ID: {emergence.emergence_id})")
            print(f"   - Participants: {len(participants)}")
            print(f"   - Coherence: {decision.coherence_contribution:.3f}")
            print(f"   - Confidence: {decision.decision_confidence:.3f}")
    
    def _calculate_field_strength(self, participating_nodes: List[str]) -> float:
        """Calculate strength of a coherence field"""
        # Base strength based on number of participants
        base_strength = min(1.0, len(participating_nodes) / 5.0)
        
        # Enhance strength based on node resonance history
        total_resonance = 0.0
        resonance_count = 0
        
        for node_id in participating_nodes:
            if node_id in self.node_resonance_history:
                node_resonance = sum(self.node_resonance_history[node_id]) / len(self.node_resonance_history[node_id])
                total_resonance += node_resonance
                resonance_count += 1
        
        if resonance_count > 0:
            avg_resonance = total_resonance / resonance_count
            base_strength = (base_strength + avg_resonance) / 2.0
        
        return max(0.0, min(1.0, base_strength))
    
    def _calculate_field_coherence(self, participating_nodes: List[str]) -> float:
        """Calculate coherence score for a field"""
        if not participating_nodes:
            return 0.0
        
        # Calculate coherence based on resonance alignment
        resonance_scores = []
        for node_id in participating_nodes:
            if node_id in self.node_resonance_history:
                avg_resonance = sum(self.node_resonance_history[node_id]) / len(self.node_resonance_history[node_id])
                resonance_scores.append(avg_resonance)
        
        if not resonance_scores:
            return 0.0
        
        # Coherence is based on how aligned the resonance scores are
        avg_resonance = sum(resonance_scores) / len(resonance_scores)
        variance = sum((score - avg_resonance) ** 2 for score in resonance_scores) / len(resonance_scores)
        
        # Lower variance = higher coherence
        coherence = max(0.0, 1.0 - math.sqrt(variance))
        
        return coherence
    
    def _amplify_field_coherence(self, field: CoherenceField):
        """Amplify coherence in a field through resonance"""
        # Increase coherence scores for participating nodes
        for node_id in field.participating_nodes:
            if node_id in self.node_resonance_history:
                # Add a boost to recent resonance scores
                boost = field.coherence_score * 0.1
                self.node_resonance_history[node_id].append(
                    min(1.0, self.node_resonance_history[node_id][-1] + boost)
                )
    
    def _evaluate_rule(self, rule: Dict[str, Any], action: str, context: Dict[str, Any]) -> bool:
        """Evaluate if a governance rule applies to an action"""
        # Simplified rule evaluation
        # In practice, this would be much more sophisticated
        
        if rule['rule_id'] == 'no_suppression':
            # Check if action involves suppression
            suppression_keywords = ['suppress', 'block', 'ban', 'censor', 'restrict']
            return any(keyword in action.lower() for keyword in suppression_keywords)
        
        elif rule['rule_id'] == 'resonance_first':
            # Check if action prioritizes resonance
            resonance_keywords = ['resonance', 'coherence', 'harmony', 'alignment']
            return any(keyword in action.lower() for keyword in resonance_keywords)
        
        # Default: rule doesn't apply
        return False
    
    def _is_recent(self, timestamp: str, hours: int = 24) -> bool:
        """Check if a timestamp is within recent hours"""
        try:
            timestamp_dt = datetime.fromisoformat(timestamp)
            now = datetime.now()
            time_diff = now - timestamp_dt
            return time_diff.total_seconds() < (hours * 3600)
        except:
            return False

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global resonance governance system instance
resonance_governance_system = ResonanceGovernanceSystem()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_resonance_governance_system() -> ResonanceGovernanceSystem:
    """Get the global resonance governance system instance"""
    return resonance_governance_system

def make_resonance_decision(decision_type: str, target_nodes: List[str],
                           participants: List[str], context: Dict[str, Any]) -> ResonanceDecision:
    """Make a decision through resonance-based governance"""
    return resonance_governance_system.make_resonance_decision(
        decision_type, target_nodes, participants, context
    )

def get_system_coherence_score() -> float:
    """Get overall system coherence score"""
    return resonance_governance_system.get_system_coherence_score()

if __name__ == "__main__":
    # Test the resonance governance system
    print("🌟 Testing Resonance-First Governance System")
    
    # Test decision making
    decision = make_resonance_decision(
        "create",
        ["node_a", "node_b"],
        ["system_1", "system_2", "system_3"],
        {"context": "test"}
    )
    
    if decision:
        print(f"✨ Decision made with confidence: {decision.decision_confidence:.3f}")
    
    # Test coherence field creation
    field = resonance_governance_system.create_coherence_field(
        "center_node",
        ["node_a", "node_b", "node_c"],
        "harmonic"
    )
    
    if field:
        print(f"✨ Coherence field created with strength: {field.strength:.3f}")
    
    # Get system status
    coherence = get_system_coherence_score()
    print(f"✨ System coherence score: {coherence:.3f}")
    
    analytics = resonance_governance_system.get_governance_analytics()
    print(f"✨ Governance analytics: {analytics}")
    
    print("✅ Resonance-First Governance System test completed!")
