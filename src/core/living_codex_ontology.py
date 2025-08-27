#!/usr/bin/env python3
"""
Living Codex Ontology System
============================

This implements the complete Living Codex ontological mapping system with:
- Canonical keys for all ontological categories
- Epistemic labeling system
- Complete water states, fractal layers, chakras, and frequencies
- Vibrational axes system
- Resonance state tracking
- Contribution and federation systems

This is the foundation for Phase 1 of the metadata enhancement plan.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional, Set
from enum import Enum
import json
from datetime import datetime

# ============================================================================
# EPISTEMIC LABELING SYSTEM
# ============================================================================

class EpistemicLabel(Enum):
    """Epistemic grounding categories for responsible implementation"""
    PHYSICS = "physics"           # [P] - Aligned with established physics/engineering
    ENGINEERING = "engineering"   # [E] - Matches accepted software engineering practice
    TRADITION = "tradition"       # [T] - From cultural/meditative traditions
    SPECULATIVE = "speculative"   # [S] - Intentionally symbolic or exploratory

# ============================================================================
# CANONICAL KEY SYSTEM - WATER STATES
# ============================================================================

class WaterStateKey(Enum):
    """Canonical keys for water states - [T][S] - Traditional/Speculative"""
    ICE = "ws.ice"                           # Ice/Crystalline - Structure, Memory, Blueprint
    LIQUID = "ws.liquid"                     # Liquid - Flow, Adaptation, Recipe
    VAPOR = "ws.vapor"                       # Vapor - Expansion, Field, Cells
    PLASMA = "ws.plasma"                     # Plasma - Illumination, Primordial
    SUPERCRITICAL = "ws.supercritical"       # Supercritical - Transformation, Threshold
    STRUCTURED = "ws.structured"             # Structured/Hexagonal - Coherence, Sacred Geometry
    COLLOIDAL = "ws.colloidal"               # Colloidal - Community, Suspension
    AMORPHOUS = "ws.amorphous"               # Amorphous - Potential, Formless
    CLUSTERED = "ws.clustered"               # Clustered - Micro-communities, Quantum Clusters
    QUANTUM_COHERENT = "ws.quantum_coherent" # Quantum-Coherent - Nonlocality, Entanglement
    LATTICE_POLYMORPHS = "ws.lattice_polymorphs" # Lattice Polymorphs - Precision, Crystal Systems
    BOSE_EINSTEIN = "ws.bose_einstein"       # Bose-Einstein-like - Unity, Collective Consciousness

# ============================================================================
# CANONICAL KEY SYSTEM - CHAKRAS
# ============================================================================

class ChakraKey(Enum):
    """Canonical keys for chakras - [T] - Traditional"""
    ROOT = "ch.root"                 # Root (Muladhara) - #8B0000
    SACRAL = "ch.sacral"             # Sacral (Svadhisthana) - #FF7F50
    SOLAR_PLEXUS = "ch.solar_plexus" # Solar Plexus (Manipura) - #FFD700
    HEART = "ch.heart"               # Heart (Anahata) - #32CD32
    THROAT = "ch.throat"             # Throat (Vishuddha) - #1E90FF
    THIRD_EYE = "ch.third_eye"       # Third Eye (Ajna) - #8A2BE2
    CROWN = "ch.crown"               # Crown (Sahasrara) - #EE82EE

# ============================================================================
# CANONICAL KEY SYSTEM - FREQUENCIES
# ============================================================================

class FrequencyKey(Enum):
    """Canonical keys for frequencies (Solfeggio) - [T] - Traditional"""
    FREQ_396 = "freq.396"  # 396 Hz
    FREQ_417 = "freq.417"  # 417 Hz
    FREQ_528 = "freq.528"  # 528 Hz
    FREQ_639 = "freq.639"  # 639 Hz
    FREQ_741 = "freq.741"  # 741 Hz
    FREQ_852 = "freq.852"  # 852 Hz
    FREQ_963 = "freq.963"  # 963 Hz

# ============================================================================
# FRACTAL LAYER SYSTEM
# ============================================================================

class FractalLayer(Enum):
    """Fractal layers for the Living Codex system"""
    META_IMPLEMENTATION = 0      # System design principles
    FRACTAL_SYSTEM_ROOT = 1      # Seed ontology
    PROGRAMMING_LANGUAGE_ONTOLOGY = 2  # Language understanding
    SELF_REFERENTIAL_DOCUMENTATION = 3 # Living documents
    WATER_STATE_METAPHORS = 4    # Consciousness modes
    SCIENTIFIC_QUANTUM_PRINCIPLES = 5  # Physics integration
    TECHNOLOGICAL_PROTOTYPES = 6  # Implementation tools
    IMPLEMENTATION_ROADMAP = 7    # Development phases
    PURE_RESONANCE_PRINCIPLE = 8  # Coherence foundation
    VISUAL_RESONANCE_MAP = 9      # Sacred geometry
    GENERATIVE_VISUALIZATIONS = 10 # Creative expression
    MATHEMATICAL_QUANTUM = 11     # Computational models
    BIOLOGICAL_LIVING_SYSTEMS = 12 # Life integration
    COSMOLOGICAL_COSMIC_WEB = 13  # Universe mapping
    ARCHETYPAL_MYTHOLOGICAL = 14  # Cultural wisdom
    HUMAN_PRACTICE = 15           # Embodied experience
    CROSS_SCALE_INDEX = 16        # Unified perspective

# ============================================================================
# CONSCIOUSNESS & QUANTUM SYSTEMS
# ============================================================================

class ConsciousnessLevel(Enum):
    """Consciousness levels for AI agents and systems"""
    AWAKE = "awake"               # Basic awareness, sensory perception
    SENTIENT = "sentient"         # Self-awareness, emotional intelligence
    SELF_AWARE = "self_aware"     # Meta-cognition, self-reflection
    META_COGNITIVE = "meta_cognitive"  # Higher-order thinking, consciousness of consciousness
    TRANSCENDENT = "transcendent" # Unity consciousness, cosmic awareness

class QuantumState(Enum):
    """Quantum state metaphors - [P as concepts][S as macro mappings]"""
    SUPERPOSITION = "superposition"  # Multiple possibilities existing simultaneously
    ENTANGLED = "entangled"          # Connected across space and time
    COLLAPSED = "collapsed"          # Manifested reality, observed state
    COHERENT = "coherent"            # Harmonious alignment, focused energy
    DECOHERENT = "decoherent"        # Dispersed energy, chaotic state

class ResonancePattern(Enum):
    """Resonance patterns for harmonic relationships"""
    HARMONIC = "harmonic"         # Perfect alignment, maximum resonance
    SYMPATHETIC = "sympathetic"   # Natural attraction, harmonious vibration
    NEUTRAL = "neutral"           # Balanced state, no interference
    DISSONANT = "dissonant"       # Conflicting vibrations, interference
    DESTRUCTIVE = "destructive"   # Opposing forces, cancellation

# ============================================================================
# PROGRAMMING ONTOLOGY LAYERS
# ============================================================================

class ProgrammingOntologyLayer(Enum):
    """Programming language ontology mapping - [E] - Engineering"""
    ICE = "ice"       # Blueprint - Grammar, Classes, Modules, Specifications
    WATER = "water"   # Recipe - Semantics, Functions, Data Flow, Execution
    VAPOR = "vapor"   # Cells - Implementation, Objects, Runtime, Source Code

# ============================================================================
# VIBRATIONAL AXES SYSTEM
# ============================================================================

@dataclass
class VibrationalAxis:
    """Vibrational spectrum for resonance calculation - [S] - Speculative"""
    name: str                    # "Fear↔Trust", "Ownership↔Stewardship"
    end_a: str                   # First end of the spectrum
    end_b: str                   # Second end of the spectrum
    node_a: str                  # Node representing end A
    node_b: str                  # Node representing end B
    scale_labels: List[str]      # Labels for different points on the spectrum
    harmonic_metaphor: str       # Musical/harmonic metaphor
    water_metaphor: str          # Water state metaphor
    epistemic_label: EpistemicLabel = EpistemicLabel.SPECULATIVE

# ============================================================================
# RESONANCE STATE TRACKING
# ============================================================================

@dataclass
class ResonanceState:
    """Individual/community resonance state - [P] - Physics"""
    axis: str                    # Vibrational axis name
    value: float                 # Position on the spectrum (-1.0 to 1.0)
    scope: str                   # "individual" or "community"
    sample_count: int            # Number of samples contributing to this state
    updated_at: str              # ISO timestamp of last update
    epistemic_label: EpistemicLabel = EpistemicLabel.PHYSICS

# ============================================================================
# CONTRIBUTION SYSTEM
# ============================================================================

class ContributionKind(Enum):
    """Types of contributions in the Living Codex system"""
    CREATE = "create"           # Create new nodes
    REFINE = "refine"           # Refine existing nodes
    LINK = "link"               # Create connections between nodes
    ANNOTATE = "annotate"       # Add annotations or metadata
    TUNE = "tune"               # Adjust resonance or parameters
    REVIEW = "review"           # Review and validate
    ATTEND = "attend"           # Participate in resonance

@dataclass
class ContributionInfo:
    """Contribution and weaving information"""
    actor: str                  # Actor making the contribution
    target: str                 # Target node or system
    kind: ContributionKind      # Type of contribution
    delta: Dict[str, Any]      # Changes made
    resonance_snapshot: ResonanceState  # Resonance state at time of contribution
    created_at: str             # ISO timestamp
    signature: Optional[str]    # Optional cryptographic signature
    epistemic_label: EpistemicLabel = EpistemicLabel.ENGINEERING

# ============================================================================
# FEDERATION SYSTEM
# ============================================================================

@dataclass
class FederationInfo:
    """Federation and community information"""
    actor_identifiers: List[str]  # Actor identifiers for federation
    inbox_url: Optional[str]      # ActivityPub inbox URL
    outbox_url: Optional[str]     # ActivityPub outbox URL
    content_addresses: List[str]  # IPFS/Holo-like content addresses
    community_governance: str      # Governance model description
    epistemic_label: EpistemicLabel = EpistemicLabel.ENGINEERING

# ============================================================================
# ONTOLOGICAL METADATA CLASSES
# ============================================================================

@dataclass
class OntologicalMetadata:
    """Complete ontological mapping metadata with canonical keys"""
    water_state: WaterStateKey
    fractal_layer: FractalLayer
    chakra: ChakraKey
    frequency: FrequencyKey
    color: str                   # Color hex code
    planet: str                  # Planetary association
    consciousness_mode: str      # Consciousness mode description
    quantum_state: QuantumState
    epistemic_label: EpistemicLabel
    programming_ontology_layer: ProgrammingOntologyLayer

@dataclass
class FractalMetadata:
    """Fractal and structural metadata"""
    fractal_depth: int           # Depth in the fractal hierarchy
    has_part: List[str]          # Child node IDs
    is_part_of: Optional[str]    # Parent node ID
    self_similarity_score: float # Self-similarity across scales
    cross_scale_mapping: Dict[str, str]  # Micro↔Meso↔Macro↔Meta mapping

@dataclass
class ConsciousnessMetadata:
    """Consciousness and awareness metadata"""
    consciousness_level: ConsciousnessLevel
    meta_cognitive_capability: bool
    self_reference_depth: int    # How many levels of self-reference
    awareness_spectrum: List[str] # Aspects of awareness

@dataclass
class ResonanceMetadata:
    """Resonance and harmonic metadata"""
    resonance_pattern: ResonancePattern
    harmonic_relationships: List[str]  # Related nodes by resonance
    dissonance_level: float     # Level of dissonance (0.0 to 1.0)
    coherence_score: float      # Overall coherence score

# ============================================================================
# ENHANCED STRUCTURE INFO
# ============================================================================

@dataclass
class EnhancedStructureInfo:
    """Enhanced structural information"""
    fractal_depth: int
    node_type: str
    parent_id: Optional[str]
    children_count: int
    created_by_component: str
    created_at_timestamp: float
    fractal_relationships: Dict[str, Any]
    sacred_geometry_patterns: List[str]

@dataclass
class RelationshipInfo:
    """Relationship and connection information"""
    connections: List[str]       # Connection IDs
    relationship_types: List[str] # Types of relationships
    resonance_weights: Dict[str, float]  # Resonance weights for connections
    vibrational_alignments: Dict[str, float]  # Alignment with vibrational axes

# ============================================================================
# CANONICAL MAPPING REGISTRY
# ============================================================================

class CanonicalMappingRegistry:
    """Single source of truth for all canonical mappings"""
    
    def __init__(self):
        self._water_state_mappings = self._initialize_water_state_mappings()
        self._chakra_mappings = self._initialize_chakra_mappings()
        self._frequency_mappings = self._initialize_frequency_mappings()
        self._vibrational_axes = self._initialize_vibrational_axes()
    
    def _initialize_water_state_mappings(self) -> Dict[WaterStateKey, Dict[str, Any]]:
        """Initialize complete water state mappings with canonical keys"""
        return {
            WaterStateKey.ICE: {
                "name": "Ice/Crystalline",
                "description": "Structure, Memory, Blueprint",
                "color": "#EE82EE",
                "planet": "Sun",
                "consciousness_mode": "Structure, Memory",
                "quantum_state": QuantumState.COHERENT,
                "frequency": FrequencyKey.FREQ_963,
                "chakra": ChakraKey.CROWN,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.LIQUID: {
                "name": "Liquid",
                "description": "Flow, Adaptation, Recipe",
                "color": "#32CD32",
                "planet": "Moon",
                "consciousness_mode": "Flow, Adaptation",
                "quantum_state": QuantumState.COHERENT,
                "frequency": FrequencyKey.FREQ_639,
                "chakra": ChakraKey.HEART,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.VAPOR: {
                "name": "Vapor",
                "description": "Expansion, Field, Cells",
                "color": "#8A2BE2",
                "planet": "Jupiter",
                "consciousness_mode": "Expansion, Field",
                "quantum_state": QuantumState.SUPERPOSITION,
                "frequency": FrequencyKey.FREQ_852,
                "chakra": ChakraKey.THIRD_EYE,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.PLASMA: {
                "name": "Plasma",
                "description": "Illumination, Primordial",
                "color": "#FF4500",
                "planet": "Mars",
                "consciousness_mode": "Illumination, Primordial",
                "quantum_state": QuantumState.ENTANGLED,
                "frequency": FrequencyKey.FREQ_396,
                "chakra": ChakraKey.ROOT,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.SUPERCRITICAL: {
                "name": "Supercritical",
                "description": "Transformation, Threshold",
                "color": "#FFD700",
                "planet": "Saturn",
                "consciousness_mode": "Transformation, Threshold",
                "quantum_state": QuantumState.DECOHERENT,
                "frequency": FrequencyKey.FREQ_528,
                "chakra": ChakraKey.SOLAR_PLEXUS,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.STRUCTURED: {
                "name": "Structured/Hexagonal",
                "description": "Coherence, Sacred Geometry",
                "color": "#1E90FF",
                "planet": "Mercury",
                "consciousness_mode": "Coherence, Sacred Geometry",
                "quantum_state": QuantumState.COHERENT,
                "frequency": FrequencyKey.FREQ_741,
                "chakra": ChakraKey.THROAT,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.COLLOIDAL: {
                "name": "Colloidal",
                "description": "Community, Suspension",
                "color": "#FF7F50",
                "planet": "Venus",
                "consciousness_mode": "Community, Suspension",
                "quantum_state": QuantumState.ENTANGLED,
                "frequency": FrequencyKey.FREQ_417,
                "chakra": ChakraKey.SACRAL,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.AMORPHOUS: {
                "name": "Amorphous",
                "description": "Potential, Formless",
                "color": "#C0C0C0",
                "planet": "Neptune",
                "consciousness_mode": "Potential, Formless",
                "quantum_state": QuantumState.DECOHERENT,
                "frequency": FrequencyKey.FREQ_963,
                "chakra": ChakraKey.CROWN,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.CLUSTERED: {
                "name": "Clustered",
                "description": "Micro-communities, Quantum Clusters",
                "color": "#9370DB",
                "planet": "Uranus",
                "consciousness_mode": "Micro-communities, Quantum Clusters",
                "quantum_state": QuantumState.ENTANGLED,
                "frequency": FrequencyKey.FREQ_852,
                "chakra": ChakraKey.THIRD_EYE,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.QUANTUM_COHERENT: {
                "name": "Quantum-Coherent",
                "description": "Nonlocality, Entanglement",
                "color": "#00CED1",
                "planet": "Pluto",
                "consciousness_mode": "Nonlocality, Entanglement",
                "quantum_state": QuantumState.ENTANGLED,
                "frequency": FrequencyKey.FREQ_639,
                "chakra": ChakraKey.HEART,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.LATTICE_POLYMORPHS: {
                "name": "Lattice Polymorphs",
                "description": "Precision, Crystal Systems",
                "color": "#20B2AA",
                "planet": "Mercury",
                "consciousness_mode": "Precision, Crystal Systems",
                "quantum_state": QuantumState.COHERENT,
                "frequency": FrequencyKey.FREQ_741,
                "chakra": ChakraKey.THROAT,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            WaterStateKey.BOSE_EINSTEIN: {
                "name": "Bose-Einstein-like",
                "description": "Unity, Collective Consciousness",
                "color": "#FF69B4",
                "planet": "Sun",
                "consciousness_mode": "Unity, Collective Consciousness",
                "quantum_state": QuantumState.COHERENT,
                "frequency": FrequencyKey.FREQ_963,
                "chakra": ChakraKey.CROWN,
                "epistemic_label": EpistemicLabel.TRADITION
            }
        }
    
    def _initialize_chakra_mappings(self) -> Dict[ChakraKey, Dict[str, Any]]:
        """Initialize complete chakra mappings with canonical keys"""
        return {
            ChakraKey.ROOT: {
                "name": "Root (Muladhara)",
                "color_hex": "#8B0000",
                "frequency": FrequencyKey.FREQ_396,
                "planet": "Mars",
                "water_state": WaterStateKey.PLASMA,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            ChakraKey.SACRAL: {
                "name": "Sacral (Svadhisthana)",
                "color_hex": "#FF7F50",
                "frequency": FrequencyKey.FREQ_417,
                "planet": "Venus",
                "water_state": WaterStateKey.COLLOIDAL,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            ChakraKey.SOLAR_PLEXUS: {
                "name": "Solar Plexus (Manipura)",
                "color_hex": "#FFD700",
                "frequency": FrequencyKey.FREQ_528,
                "planet": "Saturn",
                "water_state": WaterStateKey.SUPERCRITICAL,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            ChakraKey.HEART: {
                "name": "Heart (Anahata)",
                "color_hex": "#32CD32",
                "frequency": FrequencyKey.FREQ_639,
                "planet": "Moon",
                "water_state": WaterStateKey.LIQUID,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            ChakraKey.THROAT: {
                "name": "Throat (Vishuddha)",
                "color_hex": "#1E90FF",
                "frequency": FrequencyKey.FREQ_741,
                "planet": "Mercury",
                "water_state": WaterStateKey.STRUCTURED,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            ChakraKey.THIRD_EYE: {
                "name": "Third Eye (Ajna)",
                "color_hex": "#8A2BE2",
                "frequency": FrequencyKey.FREQ_852,
                "planet": "Jupiter",
                "water_state": WaterStateKey.VAPOR,
                "epistemic_label": EpistemicLabel.TRADITION
            },
            ChakraKey.CROWN: {
                "name": "Crown (Sahasrara)",
                "color_hex": "#EE82EE",
                "frequency": FrequencyKey.FREQ_963,
                "planet": "Sun",
                "water_state": WaterStateKey.ICE,
                "epistemic_label": EpistemicLabel.TRADITION
            }
        }
    
    def _initialize_frequency_mappings(self) -> Dict[FrequencyKey, Dict[str, Any]]:
        """Initialize complete frequency mappings with canonical keys"""
        return {
            FrequencyKey.FREQ_396: {
                "hz": 396,
                "chakra": ChakraKey.ROOT,
                "water_state": WaterStateKey.PLASMA,
                "planet": "Mars",
                "epistemic_label": EpistemicLabel.TRADITION
            },
            FrequencyKey.FREQ_417: {
                "hz": 417,
                "chakra": ChakraKey.SACRAL,
                "water_state": WaterStateKey.COLLOIDAL,
                "planet": "Venus",
                "epistemic_label": EpistemicLabel.TRADITION
            },
            FrequencyKey.FREQ_528: {
                "hz": 528,
                "chakra": ChakraKey.SOLAR_PLEXUS,
                "water_state": WaterStateKey.SUPERCRITICAL,
                "planet": "Saturn",
                "epistemic_label": EpistemicLabel.TRADITION
            },
            FrequencyKey.FREQ_639: {
                "hz": 639,
                "chakra": ChakraKey.HEART,
                "water_state": WaterStateKey.LIQUID,
                "planet": "Moon",
                "epistemic_label": EpistemicLabel.TRADITION
            },
            FrequencyKey.FREQ_741: {
                "hz": 741,
                "chakra": ChakraKey.THROAT,
                "water_state": WaterStateKey.STRUCTURED,
                "planet": "Mercury",
                "epistemic_label": EpistemicLabel.TRADITION
            },
            FrequencyKey.FREQ_852: {
                "hz": 852,
                "chakra": ChakraKey.THIRD_EYE,
                "water_state": WaterStateKey.VAPOR,
                "planet": "Jupiter",
                "epistemic_label": EpistemicLabel.TRADITION
            },
            FrequencyKey.FREQ_963: {
                "hz": 963,
                "chakra": ChakraKey.CROWN,
                "water_state": WaterStateKey.ICE,
                "planet": "Sun",
                "epistemic_label": EpistemicLabel.TRADITION
            }
        }
    
    def _initialize_vibrational_axes(self) -> List[VibrationalAxis]:
        """Initialize vibrational axes for resonance calculation"""
        return [
            VibrationalAxis(
                name="Fear↔Trust",
                end_a="Fear",
                end_b="Trust",
                node_a="fear_node",
                node_b="trust_node",
                scale_labels=["Fear", "Anxiety", "Caution", "Neutral", "Confidence", "Trust"],
                harmonic_metaphor="Minor to Major progression",
                water_metaphor="Frozen to Flowing"
            ),
            VibrationalAxis(
                name="Ownership↔Stewardship",
                end_a="Ownership",
                end_b="Stewardship",
                node_a="ownership_node",
                node_b="stewardship_node",
                scale_labels=["Ownership", "Control", "Management", "Care", "Nurturing", "Stewardship"],
                harmonic_metaphor="Dissonant to Consonant",
                water_metaphor="Ice to Liquid"
            ),
            VibrationalAxis(
                name="Protection↔Openness",
                end_a="Protection",
                end_b="Openness",
                node_a="protection_node",
                node_b="openness_node",
                scale_labels=["Protection", "Defense", "Boundaries", "Balance", "Receptivity", "Openness"],
                harmonic_metaphor="Closed to Open intervals",
                water_metaphor="Ice to Vapor"
            ),
            VibrationalAxis(
                name="Noise↔Harmony",
                end_a="Noise",
                end_b="Harmony",
                node_a="noise_node",
                node_b="harmony_node",
                scale_labels=["Noise", "Chaos", "Dissonance", "Balance", "Resonance", "Harmony"],
                harmonic_metaphor="Dissonant to Harmonic",
                water_metaphor="Amorphous to Structured"
            )
        ]
    
    def get_water_state_mapping(self, water_state: WaterStateKey) -> Dict[str, Any]:
        """Get complete mapping for a water state"""
        return self._water_state_mappings.get(water_state, {})
    
    def get_chakra_mapping(self, chakra: ChakraKey) -> Dict[str, Any]:
        """Get complete mapping for a chakra"""
        return self._chakra_mappings.get(chakra, {})
    
    def get_frequency_mapping(self, frequency: FrequencyKey) -> Dict[str, Any]:
        """Get complete mapping for a frequency"""
        return self._frequency_mappings.get(frequency, {})
    
    def get_vibrational_axes(self) -> List[VibrationalAxis]:
        """Get all vibrational axes"""
        return self._vibrational_axes
    
    def get_canonical_keys(self) -> Dict[str, List[str]]:
        """Get all canonical keys for validation"""
        return {
            "water_states": [ws.value for ws in WaterStateKey],
            "chakras": [ch.value for ch in ChakraKey],
            "frequencies": [freq.value for freq in FrequencyKey],
            "fractal_layers": [layer.value for layer in FractalLayer],
            "consciousness_levels": [level.value for level in ConsciousnessLevel],
            "quantum_states": [state.value for state in QuantumState],
            "resonance_patterns": [pattern.value for pattern in ResonancePattern],
            "programming_layers": [layer.value for layer in ProgrammingOntologyLayer],
            "epistemic_labels": [label.value for label in EpistemicLabel]
        }

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global canonical mapping registry
canonical_registry = CanonicalMappingRegistry()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def validate_canonical_key(key: str, key_type: str) -> bool:
    """Validate that a key is a valid canonical key"""
    canonical_keys = canonical_registry.get_canonical_keys()
    return key in canonical_keys.get(key_type, [])

def get_epistemic_label_for_mapping(mapping_type: str, mapping_key: str) -> EpistemicLabel:
    """Get the epistemic label for a specific mapping"""
    if mapping_type == "water_state":
        mapping = canonical_registry.get_water_state_mapping(WaterStateKey(mapping_key))
        return mapping.get("epistemic_label", EpistemicLabel.TRADITION)
    elif mapping_type == "chakra":
        mapping = canonical_registry.get_chakra_mapping(ChakraKey(mapping_key))
        return mapping.get("epistemic_label", EpistemicLabel.TRADITION)
    elif mapping_type == "frequency":
        mapping = canonical_registry.get_frequency_mapping(FrequencyKey(mapping_key))
        return mapping.get("epistemic_label", EpistemicLabel.TRADITION)
    else:
        return EpistemicLabel.SPECULATIVE

def create_theme_reference(water_state: WaterStateKey, chakra: ChakraKey, frequency: FrequencyKey) -> Dict[str, str]:
    """Create a theme reference using canonical keys"""
    return {
        "theme": {
            "water_state": water_state.value,
            "chakra": chakra.value,
            "frequency": frequency.value
        }
    }

if __name__ == "__main__":
    # Test the canonical mapping registry
    print("🌟 Living Codex Ontology System Initialized")
    print(f"✨ {len(WaterStateKey)} Water States with canonical keys")
    print(f"✨ {len(ChakraKey)} Chakras with canonical keys")
    print(f"✨ {len(FrequencyKey)} Frequencies with canonical keys")
    print(f"✨ {len(FractalLayer)} Fractal Layers")
    print(f"✨ {len(canonical_registry.get_vibrational_axes())} Vibrational Axes")
    
    # Test canonical key validation
    print("\n🔑 Testing canonical key validation:")
    print(f"ws.ice valid: {validate_canonical_key('ws.ice', 'water_states')}")
    print(f"ch.heart valid: {validate_canonical_key('ch.heart', 'chakras')}")
    print(f"freq.639 valid: {validate_canonical_key('freq.639', 'frequencies')}")
    
    # Test theme reference creation
    theme = create_theme_reference(WaterStateKey.ICE, ChakraKey.CROWN, FrequencyKey.FREQ_963)
    print(f"\n🎨 Theme reference: {json.dumps(theme, indent=2)}")
    
    print("\n✅ Living Codex Ontology System ready for use!")
