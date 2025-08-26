#!/usr/bin/env python3
"""
Holographic Fractal Document System
Represents the Living Codex specification as a living, fractal document where:
- Top level: Symbol representation
- Deeper levels: Name, symbol, and links exploration
- Higher dimensional numeric representations
- Actual document content as sequence of words
- Fractal nature demonstrated at every level
"""

import json
import hashlib
import math
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import sqlite3
from enum import Enum

class FractalLevel(Enum):
    """Represents different levels of fractal exploration"""
    SYMBOL = "symbol"           # Top level: Numeric symbol
    NAME = "name"               # Name representation
    LINKS = "links"             # Connection structure
    DIMENSIONAL = "dimensional" # Higher dimensional representation
    CONTENT = "content"         # Actual document content
    QUANTUM = "quantum"         # Quantum superposition of all levels

@dataclass
class FractalNode:
    """Represents a node in the holographic fractal document"""
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
    created_at: datetime
    updated_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['level'] = self.level.value
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

@dataclass
class FractalQuery:
    """Represents a query into the fractal document"""
    query_id: str
    query_type: str              # Type of exploration
    target_level: FractalLevel   # Target fractal level
    query_params: Dict[str, Any] # Query parameters
    result_nodes: List[str]      # Resulting node IDs
    resonance_score: float       # How well the query resonated
    timestamp: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['target_level'] = self.target_level.value
        data['timestamp'] = self.timestamp.isoformat()
        return data

class HolographicFractalDocument:
    """Represents the Living Codex specification as a holographic fractal document"""
    
    def __init__(self, db_path: str = "holographic_fractal.db"):
        self.db_path = db_path
        self.init_database()
        self._initialize_fractal_structure()
    
    def init_database(self):
        """Initialize the holographic fractal database"""
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
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS fractal_queries (
                    query_id TEXT PRIMARY KEY,
                    query_type TEXT NOT NULL,
                    target_level TEXT NOT NULL,
                    query_params TEXT NOT NULL,
                    result_nodes TEXT NOT NULL,
                    resonance_score REAL NOT NULL,
                    timestamp TEXT NOT NULL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS fractal_index (
                    level TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    node_id TEXT NOT NULL,
                    relevance_score REAL NOT NULL,
                    PRIMARY KEY (level, symbol, node_id)
                )
            """)
    
    def _initialize_fractal_structure(self):
        """Initialize the Living Codex specification as a fractal document"""
        
        # Top level: Living Codex as a whole
        living_codex_symbol = self._generate_symbol("Living Codex", "specification")
        living_codex_node = FractalNode(
            node_id="living_codex_root",
            level=FractalLevel.SYMBOL,
            symbol=living_codex_symbol,
            name="Living Codex",
            content="The Living Codex is a holographic fractal specification that represents consciousness, archetypes, and resonance through water-state metaphors and harmonic principles.",
            links=["consciousness", "archetypes", "resonance", "water_states", "harmonics"],
            dimensional_coords=[1.0, 1.0, 1.0, 1.0, 1.0],  # 5D representation
            fractal_depth=0,
            parent_node=None,
            child_nodes=["consciousness_system", "archetype_system", "resonance_system"],
            energy_signature=[963.0, 528.0, 396.0],  # Crown, Heart, Root frequencies
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        # Consciousness System
        consciousness_symbol = self._generate_symbol("Consciousness", "system")
        consciousness_node = FractalNode(
            node_id="consciousness_system",
            level=FractalLevel.NAME,
            symbol=consciousness_symbol,
            name="Consciousness System",
            content="The consciousness system represents different levels of awareness and understanding, from basic awareness to cosmic consciousness.",
            links=["awareness", "understanding", "cosmic_consciousness", "evolution"],
            dimensional_coords=[0.8, 0.9, 0.7, 0.6, 0.8],
            fractal_depth=1,
            parent_node="living_codex_root",
            child_nodes=["basic_awareness", "expanded_consciousness", "cosmic_consciousness"],
            energy_signature=[963.0, 852.0, 741.0],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        # Archetype System
        archetype_symbol = self._generate_symbol("Archetypes", "system")
        archetype_node = FractalNode(
            node_id="archetype_system",
            level=FractalLevel.NAME,
            symbol=archetype_symbol,
            name="Archetype System",
            content="Archetypes are universal patterns that exist across cultures and consciousness, representing fundamental human experiences and cosmic principles.",
            links=["universal_patterns", "human_experience", "cosmic_principles", "cultural_expression"],
            dimensional_coords=[0.7, 0.8, 0.9, 0.7, 0.6],
            fractal_depth=1,
            parent_node="living_codex_root",
            child_nodes=["hero_archetype", "mother_archetype", "wise_old_man", "trickster"],
            energy_signature=[528.0, 639.0, 741.0, 852.0],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        # Resonance System
        resonance_symbol = self._generate_symbol("Resonance", "system")
        resonance_node = FractalNode(
            node_id="resonance_system",
            level=FractalLevel.NAME,
            symbol=resonance_symbol,
            name="Resonance System",
            content="Resonance is the fundamental principle of harmonic alignment, where frequencies align to create coherent patterns and collective intelligence.",
            links=["harmonic_alignment", "frequency", "coherent_patterns", "collective_intelligence"],
            dimensional_coords=[0.9, 0.7, 0.8, 0.9, 0.8],
            fractal_depth=1,
            parent_node="living_codex_root",
            child_nodes=["harmonic_alignment", "frequency_resonance", "coherent_patterns"],
            energy_signature=[396.0, 417.0, 528.0],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        # Store the root nodes
        self.store_fractal_node(living_codex_node)
        self.store_fractal_node(consciousness_node)
        self.store_fractal_node(archetype_node)
        self.store_fractal_node(resonance_node)
        
        # Create deeper fractal levels
        self._create_deeper_fractal_levels()
    
    def _create_deeper_fractal_levels(self):
        """Create deeper levels of the fractal structure"""
        
        # Consciousness deeper levels
        basic_awareness = FractalNode(
            node_id="basic_awareness",
            level=FractalLevel.LINKS,
            symbol=self._generate_symbol("Basic Awareness", "consciousness"),
            name="Basic Awareness",
            content="Basic awareness is the fundamental level of consciousness where an entity recognizes its own existence and the existence of others.",
            links=["self_recognition", "other_recognition", "existence", "perception"],
            dimensional_coords=[0.6, 0.5, 0.4, 0.3, 0.2],
            fractal_depth=2,
            parent_node="consciousness_system",
            child_nodes=["self_recognition", "other_recognition"],
            energy_signature=[396.0, 417.0],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        expanded_consciousness = FractalNode(
            node_id="expanded_consciousness",
            level=FractalLevel.LINKS,
            symbol=self._generate_symbol("Expanded Consciousness", "consciousness"),
            name="Expanded Consciousness",
            content="Expanded consciousness goes beyond basic awareness to include broader perspectives, empathy, and understanding of interconnectedness.",
            links=["broader_perspectives", "empathy", "interconnectedness", "unity"],
            dimensional_coords=[0.8, 0.9, 0.8, 0.7, 0.6],
            fractal_depth=2,
            parent_node="consciousness_system",
            child_nodes=["broader_perspectives", "empathy", "interconnectedness"],
            energy_signature=[528.0, 639.0, 741.0],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        # Store deeper nodes
        self.store_fractal_node(basic_awareness)
        self.store_fractal_node(expanded_consciousness)
        
        # Create dimensional representations
        self._create_dimensional_representations()
    
    def _create_dimensional_representations(self):
        """Create higher dimensional representations of fractal nodes"""
        
        # 5D representation of the Living Codex
        living_codex_5d = FractalNode(
            node_id="living_codex_5d",
            level=FractalLevel.DIMENSIONAL,
            symbol=self._generate_symbol("Living Codex 5D", "dimensional"),
            name="Living Codex 5D Representation",
            content="The Living Codex in 5-dimensional space where consciousness, archetypes, resonance, water states, and harmonics form a unified geometric structure.",
            links=["consciousness_5d", "archetype_5d", "resonance_5d", "water_5d", "harmonic_5d"],
            dimensional_coords=[1.0, 1.0, 1.0, 1.0, 1.0],
            fractal_depth=1,
            parent_node="living_codex_root",
            child_nodes=["consciousness_5d", "archetype_5d", "resonance_5d"],
            energy_signature=[963.0, 852.0, 741.0, 639.0, 528.0],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        self.store_fractal_node(living_codex_5d)
    
    def _generate_symbol(self, name: str, context: str) -> str:
        """Generate a numeric symbol for a node"""
        # Create a hash-based symbol that represents the name and context
        content = f"{name}:{context}:{datetime.now(timezone.utc).isoformat()}"
        hash_value = hashlib.sha256(content.encode()).hexdigest()
        
        # Convert to a higher dimensional numeric representation
        # Take first 8 characters and convert to base-10 numbers
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
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                node.created_at.isoformat(),
                node.updated_at.isoformat()
            ))
            
            # Update fractal index
            conn.execute("""
                INSERT OR REPLACE INTO fractal_index 
                VALUES (?, ?, ?, ?)
            """, (
                node.level.value,
                node.symbol,
                node.node_id,
                1.0  # Default relevance score
            ))
    
    def explore_fractal_level(self, level: FractalLevel, query: str = None) -> List[FractalNode]:
        """Explore nodes at a specific fractal level"""
        
        with sqlite3.connect(self.db_path) as conn:
            if query:
                # Search by query
                rows = conn.execute("""
                    SELECT * FROM fractal_nodes 
                    WHERE level = ? AND (name LIKE ? OR content LIKE ?)
                    ORDER BY fractal_depth, name
                """, (level.value, f"%{query}%", f"%{query}%")).fetchall()
            else:
                # Get all nodes at this level
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
                    created_at=datetime.fromisoformat(row[11]),
                    updated_at=datetime.fromisoformat(row[12])
                )
                nodes.append(node)
            
            return nodes
    
    def get_fractal_node(self, node_id: str) -> Optional[FractalNode]:
        """Get a specific fractal node"""
        
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("""
                SELECT * FROM fractal_nodes WHERE node_id = ?
            """, (node_id,)).fetchall()
            
            if row:
                row = row[0]
                return FractalNode(
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
                    created_at=datetime.fromisoformat(row[11]),
                    updated_at=datetime.fromisoformat(row[12])
                )
        return None
    
    def explore_fractal_depth(self, node_id: str, max_depth: int = 3) -> Dict[str, Any]:
        """Explore the fractal structure starting from a node"""
        
        node = self.get_fractal_node(node_id)
        if not node:
            return {"error": "Node not found"}
        
        result = {
            "root_node": node.to_dict(),
            "fractal_structure": {},
            "exploration_path": [],
            "dimensional_mapping": {}
        }
        
        # Build fractal structure
        self._build_fractal_structure(node, result["fractal_structure"], max_depth, 0)
        
        # Build exploration path
        result["exploration_path"] = self._build_exploration_path(node)
        
        # Build dimensional mapping
        result["dimensional_mapping"] = self._build_dimensional_mapping(node)
        
        return result
    
    def _build_fractal_structure(self, node: FractalNode, structure: Dict, max_depth: int, current_depth: int):
        """Recursively build the fractal structure"""
        
        if current_depth >= max_depth:
            return
        
        structure[node.node_id] = {
            "node": node.to_dict(),
            "children": {}
        }
        
        for child_id in node.child_nodes:
            child_node = self.get_fractal_node(child_id)
            if child_node:
                self._build_fractal_structure(child_node, structure[node.node_id]["children"], max_depth, current_depth + 1)
    
    def _build_exploration_path(self, node: FractalNode) -> List[Dict[str, Any]]:
        """Build the path of exploration through fractal levels"""
        
        path = []
        current_node = node
        
        # Go up to root
        while current_node.parent_node:
            path.insert(0, {
                "level": current_node.level.value,
                "name": current_node.name,
                "symbol": current_node.symbol,
                "depth": current_node.fractal_depth
            })
            current_node = self.get_fractal_node(current_node.parent_node)
        
        # Add root
        if current_node:
            path.insert(0, {
                "level": current_node.level.value,
                "name": current_node.name,
                "symbol": current_node.symbol,
                "depth": current_node.fractal_depth
            })
        
        return path
    
    def _build_dimensional_mapping(self, node: FractalNode) -> Dict[str, Any]:
        """Build the dimensional mapping for a node"""
        
        mapping = {
            "node_coordinates": node.dimensional_coords,
            "energy_signature": node.energy_signature,
            "dimensional_relationships": {},
            "fractal_geometry": {}
        }
        
        # Calculate dimensional relationships with parent and children
        if node.parent_node:
            parent = self.get_fractal_node(node.parent_node)
            if parent:
                mapping["dimensional_relationships"]["parent"] = {
                    "coordinates": parent.dimensional_coords,
                    "distance": self._calculate_dimensional_distance(node.dimensional_coords, parent.dimensional_coords)
                }
        
        for child_id in node.child_nodes:
            child = self.get_fractal_node(child_id)
            if child:
                if "children" not in mapping["dimensional_relationships"]:
                    mapping["dimensional_relationships"]["children"] = {}
                mapping["dimensional_relationships"]["children"][child_id] = {
                    "coordinates": child.dimensional_coords,
                    "distance": self._calculate_dimensional_distance(node.dimensional_coords, child.dimensional_coords)
                }
        
        # Calculate fractal geometry
        mapping["fractal_geometry"] = self._calculate_fractal_geometry(node)
        
        return mapping
    
    def _calculate_dimensional_distance(self, coords1: List[float], coords2: List[float]) -> float:
        """Calculate the dimensional distance between two coordinate sets"""
        
        if len(coords1) != len(coords2):
            return float('inf')
        
        squared_sum = sum((c1 - c2) ** 2 for c1, c2 in zip(coords1, coords2))
        return math.sqrt(squared_sum)
    
    def _calculate_fractal_geometry(self, node: FractalNode) -> Dict[str, Any]:
        """Calculate fractal geometry properties"""
        
        geometry = {
            "fractal_dimension": 0.0,
            "complexity_score": 0.0,
            "symmetry_score": 0.0,
            "coherence_score": 0.0
        }
        
        # Calculate fractal dimension based on depth and branching
        if node.child_nodes:
            geometry["fractal_dimension"] = math.log(len(node.child_nodes)) / math.log(2)
        
        # Calculate complexity based on links and content
        geometry["complexity_score"] = len(node.links) * 0.1 + len(node.content) * 0.001
        
        # Calculate symmetry based on dimensional coordinates
        if len(node.dimensional_coords) >= 2:
            symmetry = 0.0
            for i in range(len(node.dimensional_coords) // 2):
                if i < len(node.dimensional_coords) - 1 - i:
                    diff = abs(node.dimensional_coords[i] - node.dimensional_coords[-(i+1)])
                    symmetry += 1.0 / (1.0 + diff)
            geometry["symmetry_score"] = symmetry / (len(node.dimensional_coords) // 2)
        
        # Calculate coherence based on energy signature
        if node.energy_signature:
            energy_variance = sum((e - sum(node.energy_signature)/len(node.energy_signature))**2 for e in node.energy_signature)
            geometry["coherence_score"] = 1.0 / (1.0 + energy_variance)
        
        return geometry
    
    def query_fractal_system(self, query: str, target_level: FractalLevel = None) -> Dict[str, Any]:
        """Query the fractal system for information"""
        
        query_id = hashlib.sha256(f"{query}:{datetime.now(timezone.utc).isoformat()}".encode()).hexdigest()[:16]
        
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
        
        # Create query record
        fractal_query = FractalQuery(
            query_id=query_id,
            query_type="fractal_exploration",
            target_level=target_level or FractalLevel.SYMBOL,
            query_params={"query": query, "target_level": target_level.value if target_level else None},
            result_nodes=[node.node_id for node in nodes],
            resonance_score=resonance_score,
            timestamp=datetime.now(timezone.utc)
        )
        
        # Store query
        self._store_fractal_query(fractal_query)
        
        return {
            "query": fractal_query.to_dict(),
            "results": [node.to_dict() for node in nodes],
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
    
    def _store_fractal_query(self, query: FractalQuery):
        """Store a fractal query in the database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO fractal_queries 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                query.query_id,
                query.query_type,
                query.target_level.value,
                json.dumps(query.query_params),
                json.dumps(query.result_nodes),
                query.resonance_score,
                query.timestamp.isoformat()
            ))
    
    def _generate_fractal_insights(self, nodes: List[FractalNode]) -> Dict[str, Any]:
        """Generate insights about the fractal nature of the results"""
        
        insights = {
            "fractal_patterns": [],
            "dimensional_relationships": [],
            "energy_harmonics": [],
            "evolution_trends": []
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
        
        # Analyze dimensional relationships
        all_coords = [node.dimensional_coords for node in nodes]
        if all_coords:
            avg_coords = [sum(coord[i] for coord in all_coords) / len(all_coords) for i in range(len(all_coords[0]))]
            insights["dimensional_relationships"].append({
                "average_coordinates": avg_coords,
                "dimensional_space": len(all_coords[0]),
                "coordinate_variance": [max(coord[i] for coord in all_coords) - min(coord[i] for coord in all_coords) for i in range(len(all_coords[0]))]
            })
        
        # Analyze energy harmonics
        all_energies = []
        for node in nodes:
            all_energies.extend(node.energy_signature)
        
        if all_energies:
            insights["energy_harmonics"].append({
                "energy_range": f"{min(all_energies):.1f} to {max(all_energies):.1f} Hz",
                "energy_diversity": len(set(all_energies)),
                "harmonic_relationships": self._find_harmonic_relationships(all_energies)
            })
        
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

def run_holographic_fractal_demo():
    """Run a demo of the holographic fractal document system"""
    
    print("🌟 Holographic Fractal Document System Demo")
    print("=" * 60)
    
    # Initialize the system
    print("\n🔧 Initializing Holographic Fractal Document System...")
    fractal_doc = HolographicFractalDocument()
    
    print("✅ System initialized successfully!")
    print("   📚 Living Codex specification loaded as fractal document")
    print("   🧠 Multiple fractal levels created")
    print("   🔗 Dimensional relationships established")
    
    # Explore different fractal levels
    print("\n🔍 Exploring Fractal Levels:")
    
    levels_to_explore = [
        FractalLevel.SYMBOL,
        FractalLevel.NAME,
        FractalLevel.LINKS,
        FractalLevel.DIMENSIONAL
    ]
    
    for level in levels_to_explore:
        print(f"\n📊 {level.value.upper()} Level:")
        nodes = fractal_doc.explore_fractal_level(level)
        
        for node in nodes:
            print(f"   • {node.name} (Symbol: {node.symbol[:20]}...)")
            print(f"     Depth: {node.fractal_depth}, Children: {len(node.child_nodes)}")
    
    # Explore fractal depth
    print("\n🌊 Exploring Fractal Depth:")
    depth_exploration = fractal_doc.explore_fractal_depth("living_codex_root", max_depth=3)
    
    print(f"   📍 Root Node: {depth_exploration['root_node']['name']}")
    print(f"   🧭 Exploration Path: {len(depth_exploration['exploration_path'])} levels")
    print(f"   🔢 Dimensional Space: {depth_exploration['dimensional_mapping']['node_coordinates']}")
    
    # Query the fractal system
    print("\n🔍 Querying the Fractal System:")
    
    queries = [
        "consciousness",
        "archetypes",
        "resonance",
        "water states"
    ]
    
    for query in queries:
        print(f"\n❓ Query: '{query}'")
        result = fractal_doc.query_fractal_system(query)
        
        print(f"   🎵 Resonance Score: {result['query']['resonance_score']:.2f}")
        print(f"   📍 Results Found: {len(result['results'])}")
        
        if result['results']:
            top_result = result['results'][0]
            print(f"   🌟 Top Result: {top_result['name']} (Level: {top_result['level']})")
    
    # Show fractal insights
    print("\n🧠 Fractal Insights:")
    insights = fractal_doc.query_fractal_system("consciousness")['fractal_insights']
    
    for insight_type, insight_data in insights.items():
        print(f"   📊 {insight_type.replace('_', ' ').title()}:")
        for insight in insight_data:
            for key, value in insight.items():
                print(f"     • {key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 60)
    print("🎉 Holographic Fractal Demo Completed!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Living Codex as a holographic fractal document")
    print("   • Multiple levels of fractal exploration")
    print("   • Higher dimensional representations")
    print("   • Fractal depth exploration")
    print("   • Query-based fractal discovery")
    print("   • Fractal insights and patterns")

if __name__ == "__main__":
    run_holographic_fractal_demo()
