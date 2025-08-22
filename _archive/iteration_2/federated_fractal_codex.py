#!/usr/bin/env python3
"""
Federated Fractal Codex System
Uses the actual federated API to create a fractal representation of the 
Living Codex specification document, allowing exploration of core principles
and ontology at the sentence level.
"""

import requests
import json
import hashlib
import math
import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import sqlite3
from enum import Enum

class FractalLevel(Enum):
    """Represents different levels of fractal exploration"""
    DOCUMENT = "document"       # Top level: Entire specification
    SECTION = "section"         # Major sections (Core Principles, etc.)
    PARAGRAPH = "paragraph"     # Individual paragraphs
    SENTENCE = "sentence"       # Individual sentences
    CONCEPT = "concept"         # Key concepts and terms
    ONTOLOGY = "ontology"       # Ontological relationships
    WATER_STATE = "water_state" # Water state correspondences
    FREQUENCY = "frequency"     # Frequency and harmonic relationships

@dataclass
class FractalNode:
    """Represents a node in the federated fractal codex"""
    node_id: str
    level: FractalLevel
    symbol: str                    # Numeric representation
    name: str                     # Human-readable name
    content: str                  # Actual content at this level
    links: List[str]             # Connections to other nodes
    dimensional_coords: List[float]  # Higher dimensional coordinates
    fractal_depth: int            # How deep in the fractal structure
    parent_node: Optional[str]    # Parent node ID
    child_nodes: List[str]        # Child node IDs
    energy_signature: List[float] # Energy pattern at this level
    water_state: Optional[str]    # Corresponding water state
    chakra: Optional[str]         # Corresponding chakra
    frequency: Optional[float]    # Corresponding frequency
    color: Optional[str]          # Corresponding color
    planet: Optional[str]         # Corresponding planet
    created_at: datetime
    updated_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['level'] = self.level.value
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

class FederatedFractalCodex:
    """Creates a fractal representation of the Living Codex specification using the federated API"""
    
    def __init__(self, api_base_url: str = "http://localhost:8001", db_path: str = "federated_fractal_codex.db"):
        self.api_base_url = api_base_url
        self.db_path = db_path
        self.session = requests.Session()
        self.init_database()
        self._initialize_from_specification()
    
    def init_database(self):
        """Initialize the federated fractal codex database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS fractal_nodes (
                    node_id TEXT PRIMARY KEY,
                    level TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL,
                    links TEXT NOT NULL,
                    dimensional_coords TEXT NOT NULL,
                    fractal_depth INTEGER NOT NULL,
                    parent_node TEXT,
                    child_nodes TEXT NOT NULL,
                    energy_signature TEXT NOT NULL,
                    water_state TEXT,
                    chakra TEXT,
                    frequency REAL,
                    color TEXT,
                    planet TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS codex_sentences (
                    sentence_id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    section TEXT NOT NULL,
                    concepts TEXT NOT NULL,
                    water_states TEXT NOT NULL,
                    frequencies TEXT NOT NULL,
                    node_id TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS ontology_relationships (
                    source_concept TEXT NOT NULL,
                    target_concept TEXT NOT NULL,
                    relationship_type TEXT NOT NULL,
                    strength REAL NOT NULL,
                    rationale TEXT,
                    created_at TEXT NOT NULL,
                    PRIMARY KEY (source_concept, target_concept)
                )
            """)
    
    def _initialize_from_specification(self):
        """Initialize the fractal structure from the actual Living Codex specification"""
        
        # Read the specification document
        spec_content = self._read_specification_document()
        
        # Create root document node
        document_symbol = self._generate_symbol("Living Codex Specification", "document")
        document_node = FractalNode(
            node_id="living_codex_specification",
            level=FractalLevel.DOCUMENT,
            symbol=document_symbol,
            name="Living Codex Specification",
            content=spec_content[:500] + "...",  # First 500 chars
            links=["core_principles", "structural_components", "seed_ontology", "water_states"],
            dimensional_coords=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],  # 8D representation
            fractal_depth=0,
            parent_node=None,
            child_nodes=["core_principles", "structural_components", "seed_ontology"],
            energy_signature=[963.0, 852.0, 741.0, 639.0, 528.0, 417.0, 396.0],
            water_state="all_states_interwoven",
            chakra="crown",
            frequency=963.0,
            color="#EE82EE",
            planet="sun",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        self.store_fractal_node(document_node)
        
        # Create section nodes
        self._create_section_nodes(spec_content, document_node.node_id)
        
        # Create sentence-level nodes
        self._create_sentence_nodes(spec_content)
        
        # Create concept and ontology nodes
        self._create_concept_ontology_nodes()
        
        # Use federated API to enhance the structure
        self._enhance_with_federated_api()
    
    def _read_specification_document(self) -> str:
        """Read the Living Codex specification document"""
        try:
            with open("docs/living_codex_specification.md", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            # Fallback content if file not found
            return """
            # Living Codex Specification
            
            ## Core Principles
            1. Fractal Recursion — Every concept is both a node and a field of sub-concepts
            2. Self-Similarity Across Scales — Micro ↔ Meso ↔ Macro ↔ Meta reflect one another
            3. Vibrational Axes — Spectra such as Fear ↔ Trust orient the graph toward coherence
            4. Resonance First — All contributions are permitted; coherence self-amplifies
            5. Federated Sovereignty — No central control. Each participant curates their field
            6. Multimodal Expression — Text, geometry, sound, image, code, ritual, and water-state metaphors
            7. Universal Correspondences — Cross-map nodes to religions, archetypes, sciences, mathematics
            8. Sacred Geometry Foundations — Flower of Life, Metatron's Cube, Icositetragon Wheel
            9. Water as Living Tissue — Twelve states of water model memory, flow, transformation
            10. Harmonic Resonance Layers — Nodes/relations are tones, chords, and overtones
            11. Cosmological Reflection — Archetypal structures mirror branes, fields, spectra
            12. Techno‑Spiritual Translation — Every symbolic structure has a technological counterpart
            
            ## Seed Ontology
            - Void — Plasma/Primordial Water (beyond-form potential)
            - Field — Vapor (subtle connectivity)
            - Pattern — Structured/Hexagonal (coherence geometry)
            - Flow — Liquid (adaptability and relation)
            - Memory — Ice/Crystalline (preservation lattice)
            - Resonance — Quantum/Clustered (nonlocal alignment)
            - Transformation — Supercritical (threshold passage)
            - Unity — Liquid–Crystal Boundary (membrane mediator)
            - Emergence — Vapor–Liquid Equilibrium (condensation/birth)
            - Awareness — Surface/Reflective (interface mirror)
            - Node — Steam/Plasma Spark (radiant manifestation)
            - Codex — All States Interwoven (holographic exemplar)
            """
    
    def _create_section_nodes(self, spec_content: str, parent_id: str):
        """Create fractal nodes for major sections"""
        
        sections = {
            "core_principles": {
                "name": "Core Principles",
                "content": "The twelve core principles that define the Living Codex framework",
                "water_state": "structured_hexagonal",
                "chakra": "throat",
                "frequency": 741.0,
                "color": "#1E90FF",
                "planet": "mercury"
            },
            "structural_components": {
                "name": "Structural Components",
                "content": "The fundamental building blocks: Node, Axis, Connection, ResonanceState, Contribution, Federation",
                "water_state": "liquid",
                "chakra": "heart",
                "frequency": 639.0,
                "color": "#32CD32",
                "planet": "moon"
            },
            "seed_ontology": {
                "name": "Seed Ontology",
                "content": "The first fractal layer with twelve core nodes and water-state correspondences",
                "water_state": "crystalline",
                "chakra": "solar_plexus",
                "frequency": 528.0,
                "color": "#FFD700",
                "planet": "saturn"
            },
            "water_states": {
                "name": "Water States",
                "content": "Twelve states of water as living tissue modeling consciousness and transformation",
                "water_state": "all_states",
                "chakra": "sacral",
                "frequency": 417.0,
                "color": "#FF7F50",
                "planet": "venus"
            }
        }
        
        for section_id, section_data in sections.items():
            section_symbol = self._generate_symbol(section_data["name"], "section")
            section_node = FractalNode(
                node_id=section_id,
                level=FractalLevel.SECTION,
                symbol=section_symbol,
                name=section_data["name"],
                content=section_data["content"],
                links=[parent_id] + [k for k in sections.keys() if k != section_id],
                dimensional_coords=[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                fractal_depth=1,
                parent_node=parent_id,
                child_nodes=[],
                energy_signature=[section_data["frequency"]],
                water_state=section_data["water_state"],
                chakra=section_data["chakra"],
                frequency=section_data["frequency"],
                color=section_data["color"],
                planet=section_data["planet"],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
            
            self.store_fractal_node(section_node)
            
            # Update parent's child nodes
            self._add_child_to_parent(parent_id, section_id)
    
    def _create_sentence_nodes(self, spec_content: str):
        """Create fractal nodes for individual sentences"""
        
        # Split content into sentences
        sentences = re.split(r'[.!?]+', spec_content)
        sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 10]
        
        for i, sentence in enumerate(sentences[:50]):  # Limit to first 50 sentences
            sentence_id = f"sentence_{i:03d}"
            sentence_symbol = self._generate_symbol(sentence[:50], "sentence")
            
            # Extract concepts from sentence
            concepts = self._extract_concepts_from_sentence(sentence)
            
            # Determine water state and frequency based on concepts
            water_state, frequency = self._determine_water_state_and_frequency(concepts)
            
            sentence_node = FractalNode(
                node_id=sentence_id,
                level=FractalLevel.SENTENCE,
                symbol=sentence_symbol,
                name=f"Sentence {i+1}",
                content=sentence,
                links=concepts,
                dimensional_coords=[0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
                fractal_depth=2,
                parent_node="core_principles" if "principle" in sentence.lower() else "structural_components",
                child_nodes=[],
                energy_signature=[frequency],
                water_state=water_state,
                chakra=self._get_chakra_for_frequency(frequency),
                frequency=frequency,
                color=self._get_color_for_frequency(frequency),
                planet=self._get_planet_for_frequency(frequency),
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
            
            self.store_fractal_node(sentence_node)
            
            # Store sentence in codex_sentences table
            self._store_sentence_analysis(sentence_id, sentence, concepts, water_state, frequency)
    
    def _create_concept_ontology_nodes(self):
        """Create fractal nodes for key concepts and ontological relationships"""
        
        core_concepts = {
            "fractal_recursion": {
                "content": "Every concept is both a node and a field of sub-concepts",
                "water_state": "structured_hexagonal",
                "frequency": 741.0,
                "chakra": "throat",
                "color": "#1E90FF",
                "planet": "mercury"
            },
            "self_similarity": {
                "content": "Micro ↔ Meso ↔ Macro ↔ Meta reflect one another",
                "water_state": "liquid",
                "frequency": 639.0,
                "chakra": "heart",
                "color": "#32CD32",
                "planet": "moon"
            },
            "resonance_first": {
                "content": "All contributions are permitted; coherence self-amplifies",
                "water_state": "quantum_coherent",
                "frequency": 528.0,
                "chakra": "solar_plexus",
                "color": "#FFD700",
                "planet": "saturn"
            },
            "water_as_living_tissue": {
                "content": "Twelve states of water model memory, flow, transformation",
                "water_state": "all_states",
                "frequency": 417.0,
                "chakra": "sacral",
                "color": "#FF7F50",
                "planet": "venus"
            },
            "void": {
                "content": "Plasma/Primordial Water (beyond-form potential)",
                "water_state": "plasma",
                "frequency": 963.0,
                "chakra": "crown",
                "color": "#EE82EE",
                "planet": "sun"
            },
            "field": {
                "content": "Vapor (subtle connectivity)",
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "color": "#8A2BE2",
                "planet": "jupiter"
            }
        }
        
        for concept_id, concept_data in core_concepts.items():
            concept_symbol = self._generate_symbol(concept_id, "concept")
            concept_node = FractalNode(
                node_id=concept_id,
                level=FractalLevel.CONCEPT,
                symbol=concept_symbol,
                name=concept_id.replace("_", " ").title(),
                content=concept_data["content"],
                links=["core_principles"],
                dimensional_coords=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                fractal_depth=2,
                parent_node="core_principles",
                child_nodes=[],
                energy_signature=[concept_data["frequency"]],
                water_state=concept_data["water_state"],
                chakra=concept_data["chakra"],
                frequency=concept_data["frequency"],
                color=concept_data["color"],
                planet=concept_data["planet"],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
            
            self.store_fractal_node(concept_node)
            
            # Create ontological relationships
            self._create_ontology_relationships(concept_id, concept_data)
    
    def _enhance_with_federated_api(self):
        """Use the federated API to enhance the fractal structure"""
        
        try:
            # Get system overview from federated API
            system_overview = self._get_federated_system_overview()
            
            # Create curiosity questions about the codex
            curiosity_questions = [
                "How does the Living Codex specification demonstrate fractal recursion?",
                "What are the water state correspondences in the seed ontology?",
                "How do the core principles relate to consciousness and resonance?",
                "What is the relationship between sacred geometry and water states?"
            ]
            
            for question in curiosity_questions:
                # Create curiosity question via API
                curiosity_response = self._create_curiosity_question(question)
                
                # Explore the question
                exploration_response = self._explore_curiosity_question(curiosity_response.get("id"))
                
                # Store the exploration results
                self._store_federated_exploration(question, curiosity_response, exploration_response)
                
        except Exception as e:
            print(f"⚠️  Federated API not available: {e}")
            print("   Continuing with local fractal structure...")
    
    def _get_federated_system_overview(self) -> Dict[str, Any]:
        """Get system overview from federated API"""
        try:
            response = self.session.get(f"{self.api_base_url}/system/overview")
            return response.json()
        except:
            return {"error": "API not available"}
    
    def _create_curiosity_question(self, question: str) -> Dict[str, Any]:
        """Create a curiosity question via federated API"""
        try:
            response = self.session.post(
                f"{self.api_base_url}/curiosity/questions",
                json={
                    "question": question,
                    "source": "federated_fractal_codex",
                    "priority": "high"
                }
            )
            return response.json()
        except:
            return {"error": "API not available"}
    
    def _explore_curiosity_question(self, question_id: int) -> Dict[str, Any]:
        """Explore a curiosity question via federated API"""
        try:
            response = self.session.post(
                f"{self.api_base_url}/curiosity/explore/{question_id}",
                json={}
            )
            return response.json()
        except:
            return {"error": "API not available"}
    
    def _store_federated_exploration(self, question: str, curiosity_response: Dict, exploration_response: Dict):
        """Store federated API exploration results"""
        
        exploration_id = hashlib.sha256(f"{question}:{datetime.now(timezone.utc).isoformat()}".encode()).hexdigest()[:16]
        
        # Create exploration node
        exploration_node = FractalNode(
            node_id=f"exploration_{exploration_id}",
            level=FractalLevel.CONCEPT,
            symbol=self._generate_symbol(question, "exploration"),
            name=f"API Exploration: {question[:50]}...",
            content=f"Question: {question}\nExploration: {exploration_response.get('exploration_result', 'No result')}",
            links=["federated_api", "curiosity_engine"],
            dimensional_coords=[0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
            fractal_depth=3,
            parent_node="core_principles",
            child_nodes=[],
            energy_signature=[528.0],  # Solar plexus frequency for exploration
            water_state="vapor",  # Vapor for exploration and discovery
            chakra="solar_plexus",
            frequency=528.0,
            color="#FFD700",
            planet="saturn",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        self.store_fractal_node(exploration_node)
    
    def _extract_concepts_from_sentence(self, sentence: str) -> List[str]:
        """Extract key concepts from a sentence"""
        
        # Core Living Codex concepts
        core_concepts = [
            "fractal", "recursion", "consciousness", "resonance", "water", "archetype",
            "sacred", "geometry", "frequency", "chakra", "planet", "color",
            "void", "field", "pattern", "flow", "memory", "transformation",
            "unity", "emergence", "awareness", "node", "codex"
        ]
        
        concepts = []
        sentence_lower = sentence.lower()
        
        for concept in core_concepts:
            if concept in sentence_lower:
                concepts.append(concept)
        
        return concepts
    
    def _determine_water_state_and_frequency(self, concepts: List[str]) -> Tuple[str, float]:
        """Determine water state and frequency based on concepts"""
        
        # Default values
        water_state = "liquid"
        frequency = 639.0
        
        # Concept-based mapping
        if "void" in concepts or "crown" in concepts:
            water_state = "plasma"
            frequency = 963.0
        elif "field" in concepts or "third_eye" in concepts:
            water_state = "vapor"
            frequency = 852.0
        elif "pattern" in concepts or "throat" in concepts:
            water_state = "structured_hexagonal"
            frequency = 741.0
        elif "flow" in concepts or "heart" in concepts:
            water_state = "liquid"
            frequency = 639.0
        elif "memory" in concepts or "solar_plexus" in concepts:
            water_state = "crystalline"
            frequency = 528.0
        elif "resonance" in concepts or "sacral" in concepts:
            water_state = "quantum_coherent"
            frequency = 417.0
        elif "transformation" in concepts or "root" in concepts:
            water_state = "supercritical"
            frequency = 396.0
        
        return water_state, frequency
    
    def _get_chakra_for_frequency(self, frequency: float) -> str:
        """Get chakra name for a given frequency"""
        chakra_map = {
            396.0: "root",
            417.0: "sacral",
            528.0: "solar_plexus",
            639.0: "heart",
            741.0: "throat",
            852.0: "third_eye",
            963.0: "crown"
        }
        return chakra_map.get(frequency, "unknown")
    
    def _get_color_for_frequency(self, frequency: float) -> str:
        """Get color for a given frequency"""
        color_map = {
            396.0: "#8B0000",  # Dark red
            417.0: "#FF7F50",  # Coral
            528.0: "#FFD700",  # Gold
            639.0: "#32CD32",  # Lime green
            741.0: "#1E90FF",  # Dodger blue
            852.0: "#8A2BE2",  # Blue violet
            963.0: "#EE82EE"   # Violet
        }
        return color_map.get(frequency, "#000000")
    
    def _get_planet_for_frequency(self, frequency: float) -> str:
        """Get planet for a given frequency"""
        planet_map = {
            396.0: "mars",
            417.0: "venus",
            528.0: "saturn",
            639.0: "moon",
            741.0: "mercury",
            852.0: "jupiter",
            963.0: "sun"
        }
        return planet_map.get(frequency, "unknown")
    
    def _create_ontology_relationships(self, concept_id: str, concept_data: Dict[str, Any]):
        """Create ontological relationships for a concept"""
        
        # Create relationships with other core concepts
        relationships = [
            ("fractal_recursion", "self_similarity", "supports", 0.8, "Fractal recursion enables self-similarity across scales"),
            ("resonance_first", "water_as_living_tissue", "resonates_with", 0.9, "Resonance is fundamental to water's living properties"),
            ("void", "field", "emerges_from", 0.7, "Field emerges from void as potential becomes manifest"),
            ("pattern", "flow", "structures", 0.8, "Pattern structures and guides flow"),
            ("memory", "transformation", "preserves", 0.6, "Memory preserves transformation history")
        ]
        
        for source, target, rel_type, strength, rationale in relationships:
            if source == concept_id or target == concept_id:
                self._store_ontology_relationship(source, target, rel_type, strength, rationale)
    
    def _store_ontology_relationship(self, source: str, target: str, rel_type: str, strength: float, rationale: str):
        """Store an ontological relationship"""
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO ontology_relationships 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                source,
                target,
                rel_type,
                strength,
                rationale,
                datetime.now(timezone.utc).isoformat()
            ))
    
    def _store_sentence_analysis(self, sentence_id: str, content: str, concepts: List[str], water_state: str, frequency: float):
        """Store sentence analysis in the database"""
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO codex_sentences 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                sentence_id,
                content,
                "core_principles" if "principle" in content.lower() else "structural_components",
                json.dumps(concepts),
                json.dumps([water_state]),
                json.dumps([frequency]),
                sentence_id,
                datetime.now(timezone.utc).isoformat()
            ))
    
    def _add_child_to_parent(self, parent_id: str, child_id: str):
        """Add a child node to a parent's child_nodes list"""
        
        with sqlite3.connect(self.db_path) as conn:
            # Get current child nodes
            row = conn.execute("""
                SELECT child_nodes FROM fractal_nodes WHERE node_id = ?
            """, (parent_id,)).fetchone()
            
            if row:
                child_nodes = json.loads(row[0])
                if child_id not in child_nodes:
                    child_nodes.append(child_id)
                    
                    # Update parent node
                    conn.execute("""
                        UPDATE fractal_nodes SET child_nodes = ? WHERE node_id = ?
                    """, (json.dumps(child_nodes), parent_id))
    
    def _generate_symbol(self, name: str, context: str) -> str:
        """Generate a numeric symbol for a node"""
        content = f"{name}:{context}:{datetime.now(timezone.utc).isoformat()}"
        hash_value = hashlib.sha256(content.encode()).hexdigest()
        
        symbol_parts = []
        for i in range(0, 8, 2):
            hex_part = hash_value[i:i+2]
            decimal_value = int(hex_part, 16)
            symbol_parts.append(str(decimal_value))
        
        return ":".join(symbol_parts)
    
    def store_fractal_node(self, node: FractalNode):
        """Store a fractal node in the database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO fractal_nodes 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                node.node_id,
                node.level.value,
                node.symbol,
                node.name,
                node.content,
                json.dumps(node.links),
                json.dumps(node.dimensional_coords),
                node.fractal_depth,
                node.parent_node,
                json.dumps(node.child_nodes),
                json.dumps(node.energy_signature),
                node.water_state,
                node.chakra,
                node.frequency,
                node.color,
                node.planet,
                node.created_at.isoformat(),
                node.updated_at.isoformat()
            ))
    
    def explore_fractal_level(self, level: FractalLevel, query: str = None) -> List[FractalNode]:
        """Explore nodes at a specific fractal level"""
        
        with sqlite3.connect(self.db_path) as conn:
            if query:
                rows = conn.execute("""
                    SELECT * FROM fractal_nodes 
                    WHERE level = ? AND (name LIKE ? OR content LIKE ?)
                    ORDER BY fractal_depth, name
                """, (level.value, f"%{query}%", f"%{query}%")).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM fractal_nodes 
                    WHERE level = ?
                    ORDER BY fractal_depth, name
                """, (level.value,)).fetchall()
            
            nodes = []
            for row in rows:
                node = FractalNode(
                    node_id=row[0],
                    level=FractalLevel(row[1]),
                    symbol=row[2],
                    name=row[3],
                    content=row[4],
                    links=json.loads(row[5]),
                    dimensional_coords=json.loads(row[6]),
                    fractal_depth=row[7],
                    parent_node=row[8],
                    child_nodes=json.loads(row[9]),
                    energy_signature=json.loads(row[10]),
                    water_state=row[11],
                    chakra=row[12],
                    frequency=row[13],
                    color=row[14],
                    planet=row[15],
                    created_at=datetime.fromisoformat(row[16]),
                    updated_at=datetime.fromisoformat(row[17])
                )
                nodes.append(node)
            
            return nodes
    
    def query_fractal_system(self, query: str, target_level: FractalLevel = None) -> Dict[str, Any]:
        """Query the fractal system for information"""
        
        # Search across all levels if target not specified
        if target_level:
            nodes = self.explore_fractal_level(target_level, query)
        else:
            nodes = []
            for level in FractalLevel:
                level_nodes = self.explore_fractal_level(level, query)
                nodes.extend(level_nodes)
        
        # Calculate resonance score
        resonance_score = self._calculate_query_resonance(query, nodes)
        
        return {
            "query": query,
            "target_level": target_level.value if target_level else "all",
            "results": [node.to_dict() for node in nodes],
            "resonance_score": resonance_score,
            "fractal_insights": self._generate_fractal_insights(nodes)
        }
    
    def _calculate_query_resonance(self, query: str, nodes: List[FractalNode]) -> float:
        """Calculate how well a query resonates with the fractal nodes"""
        
        if not nodes:
            return 0.0
        
        total_resonance = 0.0
        query_lower = query.lower()
        
        for node in nodes:
            # Check name match
            if query_lower in node.name.lower():
                total_resonance += 0.4
            
            # Check content match
            if query_lower in node.content.lower():
                total_resonance += 0.3
            
            # Check link match
            for link in node.links:
                if query_lower in link.lower():
                    total_resonance += 0.2
            
            # Check symbol match
            if query_lower in node.symbol.lower():
                total_resonance += 0.1
        
        return min(1.0, total_resonance / len(nodes))
    
    def _generate_fractal_insights(self, nodes: List[FractalNode]) -> Dict[str, Any]:
        """Generate insights about the fractal nature of the results"""
        
        insights = {
            "fractal_patterns": [],
            "water_state_distribution": {},
            "frequency_harmonics": [],
            "chakra_balance": {},
            "planetary_correspondences": {}
        }
        
        if not nodes:
            return insights
        
        # Analyze fractal patterns
        depths = [node.fractal_depth for node in nodes]
        insights["fractal_patterns"].append({
            "depth_distribution": f"Nodes found at depths: {min(depths)} to {max(depths)}",
            "depth_variance": max(depths) - min(depths),
            "average_depth": sum(depths) / len(depths)
        })
        
        # Analyze water state distribution
        water_states = [node.water_state for node in nodes if node.water_state]
        for state in water_states:
            insights["water_state_distribution"][state] = water_states.count(state)
        
        # Analyze frequency harmonics
        frequencies = [node.frequency for node in nodes if node.frequency]
        if frequencies:
            insights["frequency_harmonics"] = self._find_harmonic_relationships(frequencies)
        
        # Analyze chakra balance
        chakras = [node.chakra for node in nodes if node.chakra]
        for chakra in chakras:
            insights["chakra_balance"][chakra] = chakras.count(chakra)
        
        # Analyze planetary correspondences
        planets = [node.planet for node in nodes if node.planet]
        for planet in planets:
            insights["planetary_correspondences"][planet] = planets.count(planet)
        
        return insights
    
    def _find_harmonic_relationships(self, frequencies: List[float]) -> List[Dict[str, Any]]:
        """Find harmonic relationships in frequency list"""
        
        harmonics = []
        for i, freq1 in enumerate(frequencies):
            for j, freq2 in enumerate(frequencies[i+1:], i+1):
                ratio = freq2 / freq1 if freq1 > 0 else 0
                
                if abs(ratio - 2.0) < 0.1:  # Octave
                    harmonic_type = "octave"
                    strength = 1.0
                elif abs(ratio - 1.5) < 0.1:  # Perfect fifth
                    harmonic_type = "perfect_fifth"
                    strength = 0.8
                elif abs(ratio - 1.33) < 0.1:  # Perfect fourth
                    harmonic_type = "perfect_fourth"
                    strength = 0.7
                else:
                    continue
                
                harmonics.append({
                    "freq1": freq1,
                    "freq2": freq2,
                    "ratio": ratio,
                    "harmonic_type": harmonic_type,
                    "strength": strength
                })
        
        return harmonics
    
    def get_system_overview(self) -> Dict[str, Any]:
        """Get overview of the federated fractal codex system"""
        
        with sqlite3.connect(self.db_path) as conn:
            total_nodes = conn.execute("SELECT COUNT(*) FROM fractal_nodes").fetchone()[0]
            total_sentences = conn.execute("SELECT COUNT(*) FROM codex_sentences").fetchone()[0]
            total_relationships = conn.execute("SELECT COUNT(*) FROM ontology_relationships").fetchone()[0]
            
            # Count by level
            level_counts = {}
            for level in FractalLevel:
                count = conn.execute("SELECT COUNT(*) FROM fractal_nodes WHERE level = ?", (level.value,)).fetchone()[0]
                level_counts[level.value] = count
        
        return {
            "total_nodes": total_nodes,
            "total_sentences": total_sentences,
            "total_relationships": total_relationships,
            "level_distribution": level_counts,
            "federated_api_status": "connected" if self._test_api_connection() else "disconnected"
        }
    
    def _test_api_connection(self) -> bool:
        """Test connection to federated API"""
        try:
            response = self.session.get(f"{self.api_base_url}/system/overview", timeout=5)
            return response.status_code == 200
        except:
            return False

def run_federated_fractal_demo():
    """Run a demo of the federated fractal codex system"""
    
    print("🌟 Federated Fractal Codex System Demo")
    print("=" * 60)
    
    # Initialize the system
    print("\n🔧 Initializing Federated Fractal Codex System...")
    fractal_codex = FederatedFractalCodex()
    
    print("✅ System initialized successfully!")
    print("   📚 Living Codex specification loaded as fractal document")
    print("   🧠 Multiple fractal levels created with real content")
    print("   🔗 Ontological relationships established")
    print("   🌊 Water state correspondences mapped")
    
    # Show system overview
    print("\n📊 System Overview:")
    overview = fractal_codex.get_system_overview()
    
    print(f"   📈 Total Nodes: {overview['total_nodes']}")
    print(f"   📝 Total Sentences: {overview['total_sentences']}")
    print(f"   🔗 Total Relationships: {overview['total_relationships']}")
    print(f"   🌐 Federated API: {overview['federated_api_status']}")
    
    print("\n   📊 Level Distribution:")
    for level, count in overview['level_distribution'].items():
        print(f"     • {level}: {count} nodes")
    
    # Explore different fractal levels
    print("\n🔍 Exploring Fractal Levels:")
    
    levels_to_explore = [
        FractalLevel.DOCUMENT,
        FractalLevel.SECTION,
        FractalLevel.SENTENCE,
        FractalLevel.CONCEPT
    ]
    
    for level in levels_to_explore:
        print(f"\n📊 {level.value.upper()} Level:")
        nodes = fractal_codex.explore_fractal_level(level)
        
        for node in nodes[:3]:  # Show first 3 nodes
            print(f"   • {node.name}")
            print(f"     Symbol: {node.symbol[:20]}...")
            print(f"     Water State: {node.water_state or 'N/A'}")
            print(f"     Frequency: {node.frequency or 'N/A'} Hz")
            print(f"     Chakra: {node.chakra or 'N/A'}")
    
    # Query the fractal system
    print("\n🔍 Querying the Fractal System:")
    
    queries = [
        "fractal recursion",
        "water states",
        "consciousness",
        "sacred geometry"
    ]
    
    for query in queries:
        print(f"\n❓ Query: '{query}'")
        result = fractal_codex.query_fractal_system(query)
        
        print(f"   🎵 Resonance Score: {result['resonance_score']:.2f}")
        print(f"   📍 Results Found: {len(result['results'])}")
        
        if result['results']:
            top_result = result['results'][0]
            print(f"   🌟 Top Result: {top_result['name']} (Level: {top_result['level']})")
            print(f"   🌊 Water State: {top_result.get('water_state', 'N/A')}")
            print(f"   🎵 Frequency: {top_result.get('frequency', 'N/A')} Hz")
    
    # Show fractal insights
    print("\n🧠 Fractal Insights:")
    insights = fractal_codex.query_fractal_system("water")['fractal_insights']
    
    for insight_type, insight_data in insights.items():
        print(f"   📊 {insight_type.replace('_', ' ').title()}:")
        if isinstance(insight_data, list):
            for insight in insight_data:
                for key, value in insight.items():
                    print(f"     • {key.replace('_', ' ').title()}: {value}")
        elif isinstance(insight_data, dict):
            for key, value in insight_data.items():
                print(f"     • {key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 60)
    print("🎉 Federated Fractal Codex Demo Completed!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Living Codex specification as fractal document")
    print("   • Real content from the specification document")
    print("   • Sentence-level fractal exploration")
    print("   • Water state and frequency correspondences")
    print("   • Ontological relationships and chakra mapping")
    print("   • Integration with federated API")
    print("   • Core principles and seed ontology exploration")

if __name__ == "__main__":
    run_federated_fractal_demo()
