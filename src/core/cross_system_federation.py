#!/usr/bin/env python3
"""
Cross-System Federation System
==============================

This implements the cross-system federation system that enables different
Living Codex systems to work together and share data for Phase 4 of the
metadata enhancement plan.

This system provides:
- System registration and discovery
- Inter-system communication protocols
- Data sharing and synchronization
- Federation governance and validation
- Cross-system metadata integration

The federation system enables the Living Codex to function as a unified
meta-circular system while maintaining system autonomy.
"""

from typing import Dict, List, Any, Optional, Set, Tuple, Union, Callable
from datetime import datetime
import json
import threading
import uuid
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry
)

from enhanced_generic_node import EnhancedGenericNode

class FederationProtocol(Enum):
    """Federation communication protocols"""
    REST = "rest"
    GRPC = "grpc"
    WEBSOCKET = "websocket"
    INTERNAL = "internal"
    EVENT_DRIVEN = "event_driven"

class FederationStatus(Enum):
    """Federation system status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    CONNECTING = "connecting"
    DISCONNECTED = "disconnected"
    ERROR = "error"
    MAINTENANCE = "maintenance"

@dataclass
class FederationNode:
    """A node in the federation network"""
    node_id: str
    system_name: str
    system_type: str
    protocol: FederationProtocol
    endpoint: str
    status: FederationStatus
    capabilities: List[str]
    metadata: Dict[str, Any]
    last_seen: str
    connection_quality: float  # 0.0 to 1.0
    trust_score: float  # 0.0 to 1.0
    created_at: str
    updated_at: str

@dataclass
class FederationMessage:
    """A message sent between federation nodes"""
    message_id: str
    sender_id: str
    receiver_id: str
    message_type: str
    payload: Dict[str, Any]
    timestamp: str
    priority: int  # 1-10, higher is more important
    requires_ack: bool
    ack_received: bool = False
    retry_count: int = 0
    max_retries: int = 3
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class FederationContract:
    """A contract defining data sharing between systems"""
    contract_id: str
    system_a: str
    system_b: str
    data_types: List[str]
    sharing_rules: Dict[str, Any]
    access_levels: Dict[str, str]  # "read", "write", "admin"
    validation_rules: List[str]
    created_at: str
    expires_at: Optional[str]
    status: str  # "active", "expired", "revoked"
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class FederationMetrics:
    """Metrics for federation performance and health"""
    total_nodes: int
    active_connections: int
    messages_sent: int
    messages_received: int
    data_transferred: int  # bytes
    average_response_time: float  # milliseconds
    error_rate: float  # 0.0 to 1.0
    trust_score_average: float
    last_updated: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class CrossSystemFederation:
    """
    Cross-System Federation System for enabling inter-system communication and data sharing
    
    This system implements:
    - System registration and discovery
    - Inter-system communication protocols
    - Data sharing and synchronization
    - Federation governance and validation
    - Cross-system metadata integration
    """
    
    def __init__(self):
        """Initialize the cross-system federation system"""
        self.registry = canonical_registry
        
        # Federation network
        self._federation_nodes: Dict[str, FederationNode] = {}
        self._federation_messages: Dict[str, FederationMessage] = {}
        self._federation_contracts: Dict[str, FederationContract] = {}
        
        # System capabilities registry
        self._system_capabilities: Dict[str, Dict[str, Any]] = {}
        
        # Communication protocols
        self._protocol_handlers: Dict[FederationProtocol, Callable] = {}
        
        # Federation governance
        self._governance_rules: List[Dict[str, Any]] = []
        self._validation_handlers: List[Callable] = []
        
        # Threading and synchronization
        self._lock = threading.RLock()
        self._message_queue: List[FederationMessage] = []
        self._processing_thread = None
        self._running = False
        
        # Federation metrics
        self._federation_metrics = FederationMetrics(
            total_nodes=0,
            active_connections=0,
            messages_sent=0,
            messages_received=0,
            data_transferred=0,
            average_response_time=0.0,
            error_rate=0.0,
            trust_score_average=0.0,
            last_updated=datetime.now().isoformat(),
            metadata={}
        )
        
        # Initialize default capabilities
        self._initialize_default_capabilities()
        
        # Initialize governance rules
        self._initialize_governance_rules()
        
        print("🌐 Cross-System Federation System initialized")
        print("✨ System registration and discovery active")
        print("✨ Inter-system communication enabled")
        print("✨ Data sharing and synchronization active")
        print("✨ Federation governance and validation enabled")
        print("✨ Cross-system metadata integration active")
    
    # ============================================================================
    # SYSTEM CAPABILITIES INITIALIZATION
    # ============================================================================
    
    def _initialize_default_capabilities(self):
        """Initialize default system capabilities"""
        self._system_capabilities = {
            'sacred_geometry_system': {
                'name': 'Sacred Geometry System',
                'version': '1.0.0',
                'capabilities': [
                    'sacred_geometry_pattern_recognition',
                    'universal_correspondences_mapping',
                    'geometric_resonance_calculation',
                    'epistemic_labeling'
                ],
                'data_types': [
                    'SacredGeometryPattern',
                    'UniversalCorrespondence',
                    'GeometricResonance'
                ],
                'epistemic_label': EpistemicLabel.TRADITION,
                'water_state': 'ws.ice',
                'chakra': 'ch.crown',
                'frequency': 'freq.963'
            },
            'advanced_resonance_system': {
                'name': 'Advanced Resonance System',
                'version': '1.0.0',
                'capabilities': [
                    'resonance_calculation',
                    'harmonic_relationship_discovery',
                    'resonance_clustering',
                    'collective_intelligence_emergence'
                ],
                'data_types': [
                    'HarmonicRelationship',
                    'ResonanceCluster',
                    'CollectiveResonanceState'
                ],
                'epistemic_label': EpistemicLabel.SPECULATIVE,
                'water_state': 'ws.liquid',
                'chakra': 'ch.heart',
                'frequency': 'freq.639'
            },
            'consciousness_level_system': {
                'name': 'Consciousness Level System',
                'version': '1.0.0',
                'capabilities': [
                    'consciousness_assessment',
                    'evolution_tracking',
                    'meta_cognitive_analysis',
                    'collective_consciousness_calculation'
                ],
                'data_types': [
                    'ConsciousnessState',
                    'ConsciousnessEvolution',
                    'CollectiveConsciousness'
                ],
                'epistemic_label': EpistemicLabel.SPECULATIVE,
                'water_state': 'ws.vapor',
                'chakra': 'ch.throat',
                'frequency': 'freq.741'
            },
            'quantum_state_system': {
                'name': 'Quantum State System',
                'version': '1.0.0',
                'capabilities': [
                    'quantum_state_tracking',
                    'entanglement_detection',
                    'superposition_management',
                    'coherence_calculation'
                ],
                'data_types': [
                    'QuantumStateInfo',
                    'QuantumEntanglement',
                    'QuantumCoherence'
                ],
                'epistemic_label': EpistemicLabel.SPECULATIVE,
                'water_state': 'ws.plasma',
                'chakra': 'ch.root',
                'frequency': 'freq.396'
            }
        }
    
    def _initialize_governance_rules(self):
        """Initialize federation governance rules"""
        self._governance_rules = [
            {
                'rule_id': 'epistemic_validation',
                'name': 'Epistemic Validation Rule',
                'description': 'All cross-system data must be validated for epistemic consistency',
                'validation_type': 'epistemic',
                'priority': 10,
                'enabled': True
            },
            {
                'rule_id': 'water_state_compatibility',
                'name': 'Water State Compatibility Rule',
                'description': 'Systems must have compatible water states for data sharing',
                'validation_type': 'ontological',
                'priority': 8,
                'enabled': True
            },
            {
                'rule_id': 'chakra_resonance',
                'name': 'Chakra Resonance Rule',
                'description': 'Systems should have harmonious chakra alignments',
                'validation_type': 'resonance',
                'priority': 6,
                'enabled': True
            },
            {
                'rule_id': 'frequency_harmony',
                'name': 'Frequency Harmony Rule',
                'description': 'Systems should operate on harmonious frequencies',
                'validation_type': 'resonance',
                'priority': 5,
                'enabled': True
            },
            {
                'rule_id': 'trust_score_threshold',
                'name': 'Trust Score Threshold Rule',
                'description': 'Minimum trust score required for data sharing',
                'validation_type': 'security',
                'priority': 9,
                'enabled': True,
                'threshold': 0.7
            }
        ]
    
    # ============================================================================
    # SYSTEM REGISTRATION AND DISCOVERY
    # ============================================================================
    
    def register_system(self, system_name: str, system_type: str, protocol: FederationProtocol,
                       endpoint: str, capabilities: List[str], metadata: Dict[str, Any] = None) -> str:
        """
        Register a system with the federation
        
        Args:
            system_name: Name of the system
            system_type: Type of the system
            protocol: Communication protocol
            endpoint: System endpoint
            capabilities: List of system capabilities
            metadata: Additional system metadata
        
        Returns:
            Federation node ID
        """
        with self._lock:
            try:
                # Generate unique node ID
                node_id = f"fed_{system_name}_{uuid.uuid4().hex[:8]}"
                
                # Create federation node
                federation_node = FederationNode(
                    node_id=node_id,
                    system_name=system_name,
                    system_type=system_type,
                    protocol=protocol,
                    endpoint=endpoint,
                    status=FederationStatus.ACTIVE,
                    capabilities=capabilities,
                    metadata=metadata or {},
                    last_seen=datetime.now().isoformat(),
                    connection_quality=1.0,
                    trust_score=0.8,  # Default trust score
                    created_at=datetime.now().isoformat(),
                    updated_at=datetime.now().isoformat()
                )
                
                # Register the node
                self._federation_nodes[node_id] = federation_node
                
                # Update system capabilities if not already registered
                if system_name not in self._system_capabilities:
                    self._system_capabilities[system_name] = {
                        'name': system_name,
                        'version': metadata.get('version', '1.0.0'),
                        'capabilities': capabilities,
                        'data_types': metadata.get('data_types', []),
                        'epistemic_label': metadata.get('epistemic_label', EpistemicLabel.SPECULATIVE),
                        'water_state': metadata.get('water_state', 'ws.liquid'),
                        'chakra': metadata.get('chakra', 'ch.heart'),
                        'frequency': metadata.get('frequency', 'freq.639')
                    }
                
                # Update metrics
                self._update_federation_metrics()
                
                print(f"✅ System '{system_name}' registered with federation (ID: {node_id})")
                return node_id
                
            except Exception as e:
                print(f"Error registering system '{system_name}': {e}")
                return None
    
    def discover_systems(self, capability_filter: Optional[str] = None, 
                        system_type_filter: Optional[str] = None) -> List[FederationNode]:
        """
        Discover systems in the federation
        
        Args:
            capability_filter: Filter by specific capability
            system_type_filter: Filter by system type
        
        Returns:
            List of matching federation nodes
        """
        with self._lock:
            discovered_nodes = []
            
            for node in self._federation_nodes.values():
                # Apply capability filter
                if capability_filter and capability_filter not in node.capabilities:
                    continue
                
                # Apply system type filter
                if system_type_filter and system_type_filter != node.system_type:
                    continue
                
                # Only return active nodes
                if node.status == FederationStatus.ACTIVE:
                    discovered_nodes.append(node)
            
            return discovered_nodes
    
    def get_system_capabilities(self, system_name: str) -> Optional[Dict[str, Any]]:
        """Get capabilities for a specific system"""
        return self._system_capabilities.get(system_name)
    
    def update_system_status(self, node_id: str, status: FederationStatus, 
                           connection_quality: Optional[float] = None) -> bool:
        """
        Update system status and connection quality
        
        Args:
            node_id: Federation node ID
            status: New status
            connection_quality: New connection quality (optional)
        
        Returns:
            True if update successful, False otherwise
        """
        with self._lock:
            if node_id not in self._federation_nodes:
                return False
            
            node = self._federation_nodes[node_id]
            node.status = status
            node.updated_at = datetime.now().isoformat()
            
            if connection_quality is not None:
                node.connection_quality = max(0.0, min(1.0, connection_quality))
            
            # Update last seen
            if status == FederationStatus.ACTIVE:
                node.last_seen = datetime.now().isoformat()
            
            # Update metrics
            self._update_federation_metrics()
            
            return True
    
    # ============================================================================
    # INTER-SYSTEM COMMUNICATION
    # ============================================================================
    
    def send_message(self, sender_id: str, receiver_id: str, message_type: str,
                    payload: Dict[str, Any], priority: int = 5, requires_ack: bool = True) -> str:
        """
        Send a message to another system in the federation
        
        Args:
            sender_id: Sender's federation node ID
            receiver_id: Receiver's federation node ID
            message_type: Type of message
            payload: Message payload
            priority: Message priority (1-10)
            requires_ack: Whether acknowledgment is required
        
        Returns:
            Message ID
        """
        with self._lock:
            try:
                # Validate sender and receiver
                if sender_id not in self._federation_nodes:
                    raise ValueError(f"Sender '{sender_id}' not found in federation")
                
                if receiver_id not in self._federation_nodes:
                    raise ValueError(f"Receiver '{receiver_id}' not found in federation")
                
                # Create message
                message = FederationMessage(
                    message_id=f"msg_{uuid.uuid4().hex[:8]}",
                    sender_id=sender_id,
                    receiver_id=receiver_id,
                    message_type=message_type,
                    payload=payload,
                    timestamp=datetime.now().isoformat(),
                    priority=priority,
                    requires_ack=requires_ack
                )
                
                # Store message
                self._federation_messages[message.message_id] = message
                
                # Add to processing queue
                self._message_queue.append(message)
                
                # Update metrics
                self._federation_metrics.messages_sent += 1
                self._update_federation_metrics()
                
                print(f"📤 Message sent from '{sender_id}' to '{receiver_id}' (ID: {message.message_id})")
                return message.message_id
                
            except Exception as e:
                print(f"Error sending message: {e}")
                return None
    
    def receive_message(self, receiver_id: str, message_type: Optional[str] = None) -> List[FederationMessage]:
        """
        Receive messages for a system
        
        Args:
            receiver_id: Receiver's federation node ID
            message_type: Filter by message type (optional)
        
        Returns:
            List of received messages
        """
        with self._lock:
            received_messages = []
            
            for message in self._federation_messages.values():
                if message.receiver_id == receiver_id:
                    if message_type is None or message.message_type == message_type:
                        received_messages.append(message)
            
            # Sort by priority and timestamp
            received_messages.sort(key=lambda m: (-m.priority, m.timestamp))
            
            return received_messages
    
    def acknowledge_message(self, message_id: str, ack_data: Optional[Dict[str, Any]] = None) -> bool:
        """
        Acknowledge receipt of a message
        
        Args:
            message_id: Message ID to acknowledge
            ack_data: Optional acknowledgment data
        
        Returns:
            True if acknowledgment successful, False otherwise
        """
        with self._lock:
            if message_id not in self._federation_messages:
                return False
            
            message = self._federation_messages[message_id]
            message.ack_received = True
            
            if ack_data:
                message.metadata['ack_data'] = ack_data
            
            print(f"✅ Message '{message_id}' acknowledged")
            return True
    
    # ============================================================================
    # DATA SHARING AND SYNCHRONIZATION
    # ============================================================================
    
    def create_federation_contract(self, system_a: str, system_b: str, data_types: List[str],
                                 sharing_rules: Dict[str, Any], access_levels: Dict[str, str],
                                 validation_rules: List[str], expires_at: Optional[str] = None) -> str:
        """
        Create a federation contract for data sharing
        
        Args:
            system_a: First system in the contract
            system_b: Second system in the contract
            data_types: Types of data to be shared
            sharing_rules: Rules for data sharing
            access_levels: Access levels for each system
            validation_rules: Validation rules for shared data
            expires_at: Contract expiration date (optional)
        
        Returns:
            Contract ID
        """
        with self._lock:
            try:
                # Validate systems exist
                if system_a not in self._system_capabilities:
                    raise ValueError(f"System '{system_a}' not found")
                
                if system_b not in self._system_capabilities:
                    raise ValueError(f"System '{system_b}' not found")
                
                # Create contract
                contract = FederationContract(
                    contract_id=f"contract_{uuid.uuid4().hex[:8]}",
                    system_a=system_a,
                    system_b=system_b,
                    data_types=data_types,
                    sharing_rules=sharing_rules,
                    access_levels=access_levels,
                    validation_rules=validation_rules,
                    created_at=datetime.now().isoformat(),
                    expires_at=expires_at,
                    status='active'
                )
                
                # Store contract
                self._federation_contracts[contract.contract_id] = contract
                
                print(f"📋 Federation contract created between '{system_a}' and '{system_b}' (ID: {contract.contract_id})")
                return contract.contract_id
                
            except Exception as e:
                print(f"Error creating federation contract: {e}")
                return None
    
    def validate_data_sharing(self, sender_system: str, receiver_system: str, 
                            data_type: str, data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate data sharing between systems
        
        Args:
            sender_system: Sending system name
            receiver_system: Receiving system name
            data_type: Type of data being shared
            data: Data to validate
        
        Returns:
            Tuple of (is_valid, validation_errors)
        """
        validation_errors = []
        
        try:
            # Check if contract exists
            contract = self._find_active_contract(sender_system, receiver_system)
            if not contract:
                validation_errors.append("No active federation contract found")
                return False, validation_errors
            
            # Check data type is allowed
            if data_type not in contract.data_types:
                validation_errors.append(f"Data type '{data_type}' not allowed in contract")
                return False, validation_errors
            
            # Apply governance rules
            for rule in self._governance_rules:
                if rule['enabled']:
                    rule_validation = self._apply_governance_rule(rule, sender_system, receiver_system, data)
                    if not rule_validation['valid']:
                        validation_errors.extend(rule_validation['errors'])
            
            # Apply contract validation rules
            for rule in contract.validation_rules:
                rule_validation = self._apply_contract_validation_rule(rule, data)
                if not rule_validation['valid']:
                    validation_errors.extend(rule_validation['errors'])
            
            is_valid = len(validation_errors) == 0
            
            if is_valid:
                print(f"✅ Data sharing validated between '{sender_system}' and '{receiver_system}'")
            else:
                print(f"❌ Data sharing validation failed: {validation_errors}")
            
            return is_valid, validation_errors
            
        except Exception as e:
            validation_errors.append(f"Validation error: {e}")
            return False, validation_errors
    
    def _find_active_contract(self, system_a: str, system_b: str) -> Optional[FederationContract]:
        """Find active contract between two systems"""
        for contract in self._federation_contracts.values():
            if contract.status == 'active':
                if ((contract.system_a == system_a and contract.system_b == system_b) or
                    (contract.system_a == system_b and contract.system_b == system_a)):
                    return contract
        return None
    
    def _apply_governance_rule(self, rule: Dict[str, Any], sender_system: str, 
                              receiver_system: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply a governance rule to data sharing validation"""
        result = {'valid': True, 'errors': []}
        
        try:
            if rule['rule_id'] == 'epistemic_validation':
                result = self._validate_epistemic_consistency(sender_system, receiver_system, data)
            elif rule['rule_id'] == 'water_state_compatibility':
                result = self._validate_water_state_compatibility(sender_system, receiver_system)
            elif rule['rule_id'] == 'chakra_resonance':
                result = self._validate_chakra_resonance(sender_system, receiver_system)
            elif rule['rule_id'] == 'frequency_harmony':
                result = self._validate_frequency_harmony(sender_system, receiver_system)
            elif rule['rule_id'] == 'trust_score_threshold':
                result = self._validate_trust_score_threshold(sender_system, receiver_system)
        
        except Exception as e:
            result['valid'] = False
            result['errors'].append(f"Rule application error: {e}")
        
        return result
    
    def _validate_epistemic_consistency(self, sender_system: str, receiver_system: str, 
                                      data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate epistemic consistency between systems"""
        result = {'valid': True, 'errors': []}
        
        sender_caps = self._system_capabilities.get(sender_system, {})
        receiver_caps = self._system_capabilities.get(receiver_system, {})
        
        # Check if systems have compatible epistemic labels
        if 'epistemic_label' in sender_caps and 'epistemic_label' in receiver_caps:
            sender_label = sender_caps['epistemic_label']
            receiver_label = receiver_caps['epistemic_label']
            
            # Physics and engineering systems should be compatible
            if (sender_label in [EpistemicLabel.PHYSICS, EpistemicLabel.ENGINEERING] and
                receiver_label in [EpistemicLabel.PHYSICS, EpistemicLabel.ENGINEERING]):
                result['valid'] = True
            # Traditional and speculative systems can interact
            elif (sender_label in [EpistemicLabel.TRADITION, EpistemicLabel.SPECULATIVE] and
                  receiver_label in [EpistemicLabel.TRADITION, EpistemicLabel.SPECULATIVE]):
                result['valid'] = True
            # Mixed epistemic labels require careful consideration
            else:
                result['valid'] = False
                result['errors'].append(f"Epistemic incompatibility: {sender_label.value} vs {receiver_label.value}")
        
        return result
    
    def _validate_water_state_compatibility(self, sender_system: str, receiver_system: str) -> Dict[str, Any]:
        """Validate water state compatibility between systems"""
        result = {'valid': True, 'errors': []}
        
        sender_caps = self._system_capabilities.get(sender_system, {})
        receiver_caps = self._system_capabilities.get(receiver_system, {})
        
        if 'water_state' in sender_caps and 'water_state' in receiver_caps:
            sender_state = sender_caps['water_state']
            receiver_state = receiver_caps['water_state']
            
            # Check for compatible water states
            compatible_states = {
                'ws.ice': ['ws.ice', 'ws.liquid'],
                'ws.liquid': ['ws.ice', 'ws.liquid', 'ws.vapor'],
                'ws.vapor': ['ws.liquid', 'ws.vapor', 'ws.plasma'],
                'ws.plasma': ['ws.vapor', 'ws.plasma', 'ws.supercritical'],
                'ws.supercritical': ['ws.plasma', 'ws.supercritical']
            }
            
            if sender_state in compatible_states and receiver_state in compatible_states[sender_state]:
                result['valid'] = True
            else:
                result['valid'] = False
                result['errors'].append(f"Incompatible water states: {sender_state} vs {receiver_state}")
        
        return result
    
    def _validate_chakra_resonance(self, sender_system: str, receiver_system: str) -> Dict[str, Any]:
        """Validate chakra resonance between systems"""
        result = {'valid': True, 'errors': []}
        
        sender_caps = self._system_capabilities.get(sender_system, {})
        receiver_caps = self._system_capabilities.get(receiver_system, {})
        
        if 'chakra' in sender_caps and 'chakra' in receiver_caps:
            sender_chakra = sender_caps['chakra']
            receiver_chakra = receiver_caps['chakra']
            
            # Self-harmony is always valid
            if sender_chakra == receiver_chakra:
                result['valid'] = True
                return result
            
            # Check for harmonious chakra alignments
            harmonious_pairs = [
                ('ch.root', 'ch.crown'),
                ('ch.sacral', 'ch.third_eye'),
                ('ch.solar_plexus', 'ch.throat'),
                ('ch.heart', 'ch.heart')
            ]
            
            is_harmonious = (sender_chakra, receiver_chakra) in harmonious_pairs or (receiver_chakra, sender_chakra) in harmonious_pairs
            
            if is_harmonious:
                result['valid'] = True
            else:
                result['valid'] = False
                result['errors'].append(f"Non-harmonious chakra alignment: {sender_chakra} vs {receiver_chakra}")
        
        return result
    
    def _validate_frequency_harmony(self, sender_system: str, receiver_system: str) -> Dict[str, Any]:
        """Validate frequency harmony between systems"""
        result = {'valid': True, 'errors': []}
        
        sender_caps = self._system_capabilities.get(sender_system, {})
        receiver_caps = self._system_capabilities.get(receiver_system, {})
        
        if 'frequency' in sender_caps and 'frequency' in receiver_caps:
            sender_freq = sender_caps['frequency']
            receiver_freq = receiver_caps['frequency']
            
            # Self-harmony is always valid
            if sender_freq == receiver_freq:
                result['valid'] = True
                return result
            
            # Check for harmonious frequencies
            harmonious_frequencies = [
                ('freq.396', 'freq.963'),  # Root to Crown
                ('freq.417', 'freq.852'),  # Sacral to Third Eye
                ('freq.528', 'freq.741'),  # Solar Plexus to Throat
                ('freq.639', 'freq.639')   # Heart to Heart
            ]
            
            is_harmonious = (sender_freq, receiver_freq) in harmonious_frequencies or (receiver_freq, sender_freq) in harmonious_frequencies
            
            if is_harmonious:
                result['valid'] = True
            else:
                result['valid'] = False
                result['errors'].append(f"Non-harmonious frequencies: {sender_freq} vs {receiver_freq}")
        
        return result
    
    def _validate_trust_score_threshold(self, sender_system: str, receiver_system: str) -> Dict[str, Any]:
        """Validate trust score threshold between systems"""
        result = {'valid': True, 'errors': []}
        
        # Find federation nodes
        sender_node = None
        receiver_node = None
        
        for node in self._federation_nodes.values():
            if node.system_name == sender_system:
                sender_node = node
            elif node.system_name == receiver_system:
                receiver_node = node
        
        if sender_node and receiver_node:
            threshold = 0.7  # Default threshold
            
            # Find threshold from governance rules
            for rule in self._governance_rules:
                if rule['rule_id'] == 'trust_score_threshold':
                    threshold = rule.get('threshold', 0.7)
                    break
            
            # Check if both systems meet threshold
            if sender_node.trust_score < threshold or receiver_node.trust_score < threshold:
                result['valid'] = False
                result['errors'].append(f"Trust score below threshold {threshold}: {sender_system}={sender_node.trust_score}, {receiver_system}={receiver_node.trust_score}")
        
        return result
    
    def _apply_contract_validation_rule(self, rule: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply a contract-specific validation rule"""
        result = {'valid': True, 'errors': []}
        
        try:
            # Simple rule evaluation (can be extended)
            if rule.startswith('required_field:'):
                field_name = rule.split(':', 1)[1]
                if field_name not in data:
                    result['valid'] = False
                    result['errors'].append(f"Required field '{field_name}' missing")
            
            elif rule.startswith('field_type:'):
                parts = rule.split(':', 2)
                if len(parts) == 3:
                    field_name, expected_type = parts[1], parts[2]
                    if field_name in data:
                        actual_type = type(data[field_name]).__name__
                        if actual_type != expected_type:
                            result['valid'] = False
                            result['errors'].append(f"Field '{field_name}' has type {actual_type}, expected {expected_type}")
        
        except Exception as e:
            result['valid'] = False
            result['errors'].append(f"Rule evaluation error: {e}")
        
        return result
    
    # ============================================================================
    # FEDERATION METRICS AND REPORTING
    # ============================================================================
    
    def get_federation_metrics(self) -> FederationMetrics:
        """Get current federation metrics"""
        return self._federation_metrics
    
    def _update_federation_metrics(self):
        """Update federation metrics"""
        with self._lock:
            # Count active nodes
            active_nodes = sum(1 for node in self._federation_nodes.values() 
                             if node.status == FederationStatus.ACTIVE)
            
            # Calculate average trust score
            trust_scores = [node.trust_score for node in self._federation_nodes.values()]
            avg_trust_score = sum(trust_scores) / len(trust_scores) if trust_scores else 0.0
            
            # Update metrics
            self._federation_metrics.total_nodes = len(self._federation_nodes)
            self._federation_metrics.active_connections = active_nodes
            self._federation_metrics.trust_score_average = avg_trust_score
            self._federation_metrics.last_updated = datetime.now().isoformat()
    
    def export_federation_report(self, output_format: str = "json") -> Union[str, Dict[str, Any]]:
        """
        Export comprehensive federation report
        
        Args:
            output_format: "json" or "dict"
        
        Returns:
            Federation report in requested format
        """
        report = {
            'federation_system_info': {
                'name': 'Cross-System Federation System',
                'version': '1.0.0',
                'exported_at': datetime.now().isoformat()
            },
            'metrics': {
                'total_nodes': self._federation_metrics.total_nodes,
                'active_connections': self._federation_metrics.active_connections,
                'messages_sent': self._federation_metrics.messages_sent,
                'messages_received': self._federation_metrics.messages_received,
                'trust_score_average': self._federation_metrics.trust_score_average
            },
            'registered_systems': [
                {
                    'name': caps['name'],
                    'version': caps['version'],
                    'capabilities': caps['capabilities'],
                    'epistemic_label': caps['epistemic_label'].value,
                    'water_state': caps['water_state'],
                    'chakra': caps['chakra'],
                    'frequency': caps['frequency']
                }
                for caps in self._system_capabilities.values()
            ],
            'federation_nodes': [
                {
                    'id': node.node_id,
                    'system_name': node.system_name,
                    'status': node.status.value,
                    'protocol': node.protocol.value,
                    'connection_quality': node.connection_quality,
                    'trust_score': node.trust_score
                }
                for node in self._federation_nodes.values()
            ],
            'active_contracts': [
                {
                    'id': contract.contract_id,
                    'system_a': contract.system_a,
                    'system_b': contract.system_b,
                    'data_types': contract.data_types,
                    'status': contract.status
                }
                for contract in self._federation_contracts.values()
                if contract.status == 'active'
            ]
        }
        
        if output_format.lower() == "json":
            return json.dumps(report, indent=2, default=str)
        else:
            return report

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global cross-system federation instance
cross_system_federation = CrossSystemFederation()

if __name__ == "__main__":
    # Test the cross-system federation system
    print("🌐 Cross-System Federation System Test")
    
    # Test basic functionality
    print(f"System initialized with {len(cross_system_federation._federation_nodes)} nodes")
    print(f"System capabilities: {len(cross_system_federation._system_capabilities)} systems")
    print(f"Governance rules: {len(cross_system_federation._governance_rules)} rules")
    
    # Test system registration
    test_node_id = cross_system_federation.register_system(
        system_name="test_system",
        system_type="test",
        protocol=FederationProtocol.INTERNAL,
        endpoint="internal://test",
        capabilities=["test_capability"],
        metadata={"version": "1.0.0"}
    )
    
    if test_node_id:
        print(f"✅ Test system registered with ID: {test_node_id}")
        
        # Test system discovery
        discovered = cross_system_federation.discover_systems()
        print(f"✅ Discovered {len(discovered)} systems")
        
        # Test metrics
        metrics = cross_system_federation.get_federation_metrics()
        print(f"✅ Federation metrics: {metrics.total_nodes} total nodes")
    
    print("\n✅ Cross-System Federation System ready for use!")
