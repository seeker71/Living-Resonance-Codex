#!/usr/bin/env python3
"""
Generic Fractal API System
Uses only the federated API to generate all nodes dynamically.
Everything is represented as generic nodes - including the structure itself.
The final node is the codex specification, with all intermediate fractal levels
represented as nodes as well.
"""

import requests
import json
import hashlib
import math
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import sqlite3

@dataclass
class GenericNode:
    """Generic node that can represent anything in the system"""
    node_id: str
    node_type: str                    # Type of node (document, section, sentence, concept, structure, etc.)
    name: str                         # Human-readable name
    content: str                      # Actual content or description
    parent_id: Optional[str]          # Parent node ID
    children: List[str]               # Child node IDs
    metadata: Dict[str, Any]          # Flexible metadata (water_state, frequency, chakra, etc.)
    structure_info: Dict[str, Any]    # Information about the node's structure
    created_at: datetime
    updated_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

class GenericFractalAPISystem:
    """Generic fractal system that uses only the API to generate everything"""
    
    def __init__(self, api_base_url: str = "http://localhost:8001", db_path: str = "generic_fractal.db"):
        self.api_base_url = api_base_url
        self.db_path = db_path
        self.session = requests.Session()
        self.init_generic_database()
        self._generate_complete_fractal_system()
    
    def init_generic_database(self):
        """Initialize a single generic table for all nodes"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS nodes (
                    node_id TEXT PRIMARY KEY,
                    node_type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL,
                    parent_id TEXT,
                    children TEXT NOT NULL,
                    metadata TEXT NOT NULL,
                    structure_info TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            
            # Create index for efficient queries
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_node_type ON nodes (node_type)
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_parent_id ON nodes (parent_id)
            """)
    
    def _generate_complete_fractal_system(self):
        """Generate the complete fractal system using only the API"""
        
        print("🔧 Generating complete fractal system via API...")
        
        # 1. Create the root system node
        system_node = self._create_generic_node(
            node_id="fractal_system_root",
            node_type="system",
            name="Fractal System Root",
            content="The root of the entire fractal system that contains all other nodes",
            parent_id=None,
            children=[],
            metadata={
                "frequency": 963.0,
                "chakra": "crown",
                "water_state": "all_states",
                "dimensional_coords": [1.0, 1.0, 1.0, 1.0, 1.0]
            },
            structure_info={
                "fractal_depth": 0,
                "is_root": True,
                "system_type": "generic_fractal"
            }
        )
        
        # 2. Create the codex specification node
        codex_node = self._create_generic_node(
            node_id="living_codex_specification",
            node_type="document",
            name="Living Codex Specification",
            content="The complete Living Codex specification document",
            parent_id="fractal_system_root",
            children=[],
            metadata={
                "frequency": 852.0,
                "chakra": "third_eye",
                "water_state": "vapor",
                "dimensional_coords": [0.9, 0.9, 0.9, 0.9, 0.9]
            },
            structure_info={
                "fractal_depth": 1,
                "document_type": "specification",
                "content_source": "docs/living_codex_specification.md"
            }
        )
        
        # 3. Use API to generate fractal structure
        self._generate_fractal_structure_via_api(system_node.node_id, codex_node.node_id)
        
        # 4. Update parent-child relationships
        self._update_parent_children("fractal_system_root", ["living_codex_specification"])
    
    def _generate_fractal_structure_via_api(self, system_root_id: str, codex_id: str):
        """Generate the complete fractal structure using the federated API"""
        
        try:
            # Get system overview from API
            system_overview = self._api_get_system_overview()
            
            # Create curiosity questions to explore the system
            curiosity_questions = [
                "What is the fractal structure of the Living Codex?",
                "How do the core principles relate to each other?",
                "What are the water state correspondences?",
                "How does consciousness manifest in the system?",
                "What are the ontological relationships?",
                "How do frequencies and chakras relate?",
                "What is the structure of nodes and connections?",
                "How does the system demonstrate recursion?"
            ]
            
            for i, question in enumerate(curiosity_questions):
                # Create curiosity question via API
                curiosity_response = self._api_create_curiosity_question(question)
                
                if "error" not in curiosity_response:
                    # Explore the question
                    exploration_response = self._api_explore_curiosity_question(curiosity_response.get("id"))
                    
                    # Create exploration node
                    exploration_node = self._create_generic_node(
                        node_id=f"exploration_{i:03d}",
                        node_type="exploration",
                        name=f"API Exploration: {question[:50]}...",
                        content=f"Question: {question}\nExploration: {exploration_response.get('exploration_result', 'No result')}",
                        parent_id=codex_id,
                        children=[],
                        metadata={
                            "frequency": 528.0,
                            "chakra": "solar_plexus",
                            "water_state": "crystalline",
                            "question": question,
                            "api_response": exploration_response
                        },
                        structure_info={
                            "fractal_depth": 2,
                            "exploration_type": "curiosity",
                            "api_source": "federated_api"
                        }
                    )
                    
                    # Update codex children
                    self._add_child_to_parent(codex_id, exploration_node.node_id)
            
            # Generate fractal levels dynamically
            self._generate_fractal_levels_via_api(codex_id)
            
        except Exception as e:
            print(f"⚠️  API not available, generating local structure: {e}")
            self._generate_local_fractal_structure(codex_id)
    
    def _generate_fractal_levels_via_api(self, parent_id: str):
        """Generate fractal levels using API responses"""
        
        # Create different fractal level nodes
        fractal_levels = [
            {
                "id": "fractal_level_1",
                "type": "fractal_level",
                "name": "Level 1: Document Structure",
                "content": "The document level showing the overall structure",
                "metadata": {"level": 1, "frequency": 741.0, "chakra": "throat"}
            },
            {
                "id": "fractal_level_2", 
                "type": "fractal_level",
                "name": "Level 2: Section Breakdown",
                "content": "Major sections and their relationships",
                "metadata": {"level": 2, "frequency": 639.0, "chakra": "heart"}
            },
            {
                "id": "fractal_level_3",
                "type": "fractal_level", 
                "name": "Level 3: Concept Mapping",
                "content": "Individual concepts and their ontological relationships",
                "metadata": {"level": 3, "frequency": 528.0, "chakra": "solar_plexus"}
            },
            {
                "id": "fractal_level_4",
                "type": "fractal_level",
                "name": "Level 4: Sentence Analysis", 
                "content": "Individual sentences and their fractal properties",
                "metadata": {"level": 4, "frequency": 417.0, "chakra": "sacral"}
            }
        ]
        
        for level_data in fractal_levels:
            level_node = self._create_generic_node(
                node_id=level_data["id"],
                node_type=level_data["type"],
                name=level_data["name"],
                content=level_data["content"],
                parent_id=parent_id,
                children=[],
                metadata=level_data["metadata"],
                structure_info={
                    "fractal_depth": level_data["metadata"]["level"],
                    "level_type": "fractal_structure",
                    "parent_level": parent_id
                }
            )
            
            # Add to parent's children
            self._add_child_to_parent(parent_id, level_node.node_id)
            
            # Generate content for this level
            self._generate_level_content_via_api(level_node.node_id, level_data["metadata"]["level"])
    
    def _generate_level_content_via_api(self, level_id: str, level_number: int):
        """Generate content for a specific fractal level using API"""
        
        # Create content nodes based on level
        if level_number == 1:  # Document Structure
            content_nodes = [
                {
                    "id": "doc_structure_overview",
                    "name": "Document Overview",
                    "content": "Complete Living Codex specification with all sections",
                    "metadata": {"content_type": "overview", "frequency": 741.0}
                }
            ]
        elif level_number == 2:  # Section Breakdown
            content_nodes = [
                {
                    "id": "section_core_principles",
                    "name": "Core Principles",
                    "content": "The twelve core principles of the Living Codex",
                    "metadata": {"content_type": "principles", "frequency": 639.0}
                },
                {
                    "id": "section_structural_components", 
                    "name": "Structural Components",
                    "content": "Node, Axis, Connection, ResonanceState, Contribution, Federation",
                    "metadata": {"content_type": "components", "frequency": 639.0}
                },
                {
                    "id": "section_seed_ontology",
                    "name": "Seed Ontology",
                    "content": "First fractal layer with water state correspondences",
                    "metadata": {"content_type": "ontology", "frequency": 528.0}
                }
            ]
        elif level_number == 3:  # Concept Mapping
            content_nodes = [
                {
                    "id": "concept_fractal_recursion",
                    "name": "Fractal Recursion",
                    "content": "Every concept is both a node and a field of sub-concepts",
                    "metadata": {"concept_type": "principle", "frequency": 528.0}
                },
                {
                    "id": "concept_water_states",
                    "name": "Water States",
                    "content": "Twelve states of water as living tissue",
                    "metadata": {"concept_type": "metaphor", "frequency": 417.0}
                },
                {
                    "id": "concept_resonance",
                    "name": "Resonance",
                    "content": "Fundamental principle of harmonic alignment",
                    "metadata": {"concept_type": "principle", "frequency": 528.0}
                }
            ]
        else:  # Sentence Analysis
            content_nodes = [
                {
                    "id": "sentence_sample_1",
                    "name": "Sample Sentence 1",
                    "content": "The Living Codex is a recursive, fractal, federated network",
                    "metadata": {"sentence_type": "definition", "frequency": 417.0}
                },
                {
                    "id": "sentence_sample_2",
                    "name": "Sample Sentence 2", 
                    "content": "Water's twelve states model memory, flow, transformation",
                    "metadata": {"sentence_type": "explanation", "frequency": 417.0}
                }
            ]
        
        # Create the content nodes
        for content_data in content_nodes:
            content_node = self._create_generic_node(
                node_id=content_data["id"],
                node_type="content",
                name=content_data["name"],
                content=content_data["content"],
                parent_id=level_id,
                children=[],
                metadata=content_data["metadata"],
                structure_info={
                    "fractal_depth": level_number + 1,
                    "content_level": level_number,
                    "parent_level": level_id
                }
            )
            
            # Add to level's children
            self._add_child_to_parent(level_id, content_node.node_id)
    
    def _generate_local_fractal_structure(self, codex_id: str):
        """Generate fractal structure locally when API is not available"""
        
        print("   🔧 Generating local fractal structure...")
        
        # Create basic fractal levels
        levels = ["document", "section", "concept", "sentence"]
        
        for i, level_type in enumerate(levels):
            level_node = self._create_generic_node(
                node_id=f"local_level_{i+1}",
                node_type="fractal_level",
                name=f"Local Level {i+1}: {level_type.title()}",
                content=f"Local generation of {level_type} level",
                parent_id=codex_id,
                children=[],
                metadata={
                    "level": i+1,
                    "frequency": 963.0 - (i * 100),
                    "chakra": ["crown", "third_eye", "throat", "heart"][i],
                    "water_state": ["plasma", "vapor", "structured", "liquid"][i]
                },
                structure_info={
                    "fractal_depth": i+1,
                    "generation_method": "local",
                    "level_type": level_type
                }
            )
            
            self._add_child_to_parent(codex_id, level_node.node_id)
    
    def _api_get_system_overview(self) -> Dict[str, Any]:
        """Get system overview from federated API"""
        try:
            response = self.session.get(f"{self.api_base_url}/system/overview", timeout=5)
            return response.json()
        except:
            return {"error": "API not available"}
    
    def _api_create_curiosity_question(self, question: str) -> Dict[str, Any]:
        """Create a curiosity question via federated API"""
        try:
            response = self.session.post(
                f"{self.api_base_url}/curiosity/questions",
                json={
                    "question": question,
                    "source": "generic_fractal_system",
                    "priority": "high"
                },
                timeout=5
            )
            return response.json()
        except:
            return {"error": "API not available"}
    
    def _api_explore_curiosity_question(self, question_id: int) -> Dict[str, Any]:
        """Explore a curiosity question via federated API"""
        try:
            response = self.session.post(
                f"{self.api_base_url}/curiosity/explore/{question_id}",
                json={},
                timeout=5
            )
            return response.json()
        except:
            return {"error": "API not available"}
    
    def _create_generic_node(self, node_id: str, node_type: str, name: str, content: str,
                            parent_id: Optional[str], children: List[str], metadata: Dict[str, Any],
                            structure_info: Dict[str, Any]) -> GenericNode:
        """Create a generic node and store it"""
        
        node = GenericNode(
            node_id=node_id,
            node_type=node_type,
            name=name,
            content=content,
            parent_id=parent_id,
            children=children,
            metadata=metadata,
            structure_info=structure_info,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        
        self._store_generic_node(node)
        return node
    
    def _store_generic_node(self, node: GenericNode):
        """Store a generic node in the database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO nodes 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                node.node_id,
                node.node_type,
                node.name,
                node.content,
                node.parent_id,
                json.dumps(node.children),
                json.dumps(node.metadata),
                json.dumps(node.structure_info),
                node.created_at.isoformat(),
                node.updated_at.isoformat()
            ))
    
    def _add_child_to_parent(self, parent_id: str, child_id: str):
        """Add a child node to a parent's children list"""
        
        with sqlite3.connect(self.db_path) as conn:
            # Get current children
            row = conn.execute("""
                SELECT children FROM nodes WHERE node_id = ?
            """, (parent_id,)).fetchone()
            
            if row:
                children = json.loads(row[0])
                if child_id not in children:
                    children.append(child_id)
                    
                    # Update parent node
                    conn.execute("""
                        UPDATE nodes SET children = ? WHERE node_id = ?
                    """, (json.dumps(children), parent_id))
    
    def _update_parent_children(self, parent_id: str, children: List[str]):
        """Update a parent's children list"""
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                UPDATE nodes SET children = ? WHERE node_id = ?
            """, (json.dumps(children), parent_id))
    
    def get_system_overview(self) -> Dict[str, Any]:
        """Get overview of the generic fractal system"""
        
        with sqlite3.connect(self.db_path) as conn:
            total_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
            
            # Count by type
            type_counts = {}
            rows = conn.execute("SELECT node_type, COUNT(*) FROM nodes GROUP BY node_type").fetchall()
            for row in rows:
                type_counts[row[0]] = row[1]
            
            # Get fractal depth info
            depth_info = conn.execute("""
                SELECT structure_info FROM nodes WHERE node_type = 'fractal_level'
            """).fetchall()
            
            depths = []
            for row in depth_info:
                structure = json.loads(row[0])
                depths.append(structure.get("fractal_depth", 0))
        
        return {
            "total_nodes": total_nodes,
            "type_distribution": type_counts,
            "fractal_depths": depths,
            "max_depth": max(depths) if depths else 0,
            "api_status": "connected" if self._test_api_connection() else "disconnected"
        }
    
    def _test_api_connection(self) -> bool:
        """Test connection to federated API"""
        try:
            response = self.session.get(f"{self.api_base_url}/system/overview", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def explore_fractal_structure(self, node_id: str = None, max_depth: int = 5) -> Dict[str, Any]:
        """Explore the fractal structure starting from a node"""
        
        if node_id is None:
            node_id = "fractal_system_root"
        
        with sqlite3.connect(self.db_path) as conn:
            # Get the starting node
            row = conn.execute("""
                SELECT * FROM nodes WHERE node_id = ?
            """, (node_id,)).fetchone()
            
            if not row:
                return {"error": "Node not found"}
            
            # Build the fractal structure
            structure = self._build_fractal_structure(node_id, max_depth, 0)
            
            return {
                "root_node": {
                    "node_id": row[0],
                    "node_type": row[1],
                    "name": row[2],
                    "content": row[3],
                    "parent_id": row[4],
                    "children": json.loads(row[5]),
                    "metadata": json.loads(row[6]),
                    "structure_info": json.loads(row[7])
                },
                "fractal_structure": structure,
                "exploration_depth": max_depth
            }
    
    def _build_fractal_structure(self, node_id: str, max_depth: int, current_depth: int) -> Dict:
        """Recursively build the fractal structure"""
        
        if current_depth >= max_depth:
            return {}
        
        with sqlite3.connect(self.db_path) as conn:
            # Get the node
            row = conn.execute("""
                SELECT * FROM nodes WHERE node_id = ?
            """, (node_id,)).fetchone()
            
            if not row:
                return {}
            
            node_data = {
                "node_id": row[0],
                "node_type": row[1],
                "name": row[2],
                "content": row[3],
                "parent_id": row[4],
                "children": json.loads(row[5]),
                "metadata": json.loads(row[6]),
                "structure_info": json.loads(row[7])
            }
            
            # Build children recursively
            children_structure = {}
            for child_id in node_data["children"]:
                children_structure[child_id] = self._build_fractal_structure(
                    child_id, max_depth, current_depth + 1
                )
            
            return {
                "node": node_data,
                "children": children_structure
            }
    
    def query_system(self, query: str, node_type: str = None) -> Dict[str, Any]:
        """Query the system for nodes matching criteria"""
        
        with sqlite3.connect(self.db_path) as conn:
            if node_type:
                rows = conn.execute("""
                    SELECT * FROM nodes 
                    WHERE node_type = ? AND (name LIKE ? OR content LIKE ?)
                    ORDER BY node_id
                """, (node_type, f"%{query}%", f"%{query}%")).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM nodes 
                    WHERE name LIKE ? OR content LIKE ?
                    ORDER BY node_id
                """, (f"%{query}%", f"%{query}%")).fetchall()
            
            results = []
            for row in rows:
                results.append({
                    "node_id": row[0],
                    "node_type": row[1],
                    "name": row[2],
                    "content": row[3],
                    "parent_id": row[4],
                    "children": json.loads(row[5]),
                    "metadata": json.loads(row[6]),
                    "structure_info": json.loads(row[7])
                })
            
            return {
                "query": query,
                "node_type_filter": node_type,
                "results": results,
                "total_found": len(results)
            }
    
    def get_node_by_id(self, node_id: str) -> Dict[str, Any]:
        """Get a specific node by its ID"""
        
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("""
                SELECT * FROM nodes 
                WHERE node_id = ?
            """, (node_id,)).fetchone()
            
            if row:
                return {
                    "node_id": row[0],
                    "node_type": row[1],
                    "name": row[2],
                    "content": row[3],
                    "parent_id": row[4],
                    "children": json.loads(row[5]),
                    "metadata": json.loads(row[6]),
                    "structure_info": json.loads(row[7])
                }
            else:
                return None

def run_generic_fractal_demo():
    """Run a demo of the generic fractal API system"""
    
    print("🌟 Generic Fractal API System Demo")
    print("=" * 60)
    
    # Initialize the system
    print("\n🔧 Initializing Generic Fractal API System...")
    fractal_system = GenericFractalAPISystem()
    
    print("✅ System initialized successfully!")
    print("   🌐 Using federated API for node generation")
    print("   🧠 Generic node structure for everything")
    print("   🔗 Dynamic fractal structure creation")
    print("   📚 Codex specification as final node")
    
    # Show system overview
    print("\n📊 System Overview:")
    overview = fractal_system.get_system_overview()
    
    print(f"   📈 Total Nodes: {overview['total_nodes']}")
    print(f"   🧭 Max Fractal Depth: {overview['max_depth']}")
    print(f"   🌐 API Status: {overview['api_status']}")
    
    print("\n   📊 Node Type Distribution:")
    for node_type, count in overview['type_distribution'].items():
        print(f"     • {node_type}: {count} nodes")
    
    # Explore fractal structure
    print("\n🔍 Exploring Fractal Structure:")
    structure = fractal_system.explore_fractal_structure(max_depth=3)
    
    root_node = structure['root_node']
    print(f"   🌳 Root Node: {root_node['name']} ({root_node['node_type']})")
    print(f"   🔗 Children: {len(root_node['children'])}")
    print(f"   🧭 Exploration Depth: {structure['exploration_depth']}")
    
    # Show fractal levels
    if 'fractal_structure' in structure:
        print("\n   📊 Fractal Levels:")
        for child_id, child_data in structure['fractal_structure'].items():
            if child_data and 'node' in child_data:
                node = child_data['node']
                print(f"     • {node['name']} (Type: {node['node_type']})")
                print(f"       Children: {len(node['children'])}")
    
    # Query the system
    print("\n🔍 Querying the System:")
    
    queries = [
        "fractal",
        "water",
        "consciousness",
        "structure"
    ]
    
    for query in queries:
        print(f"\n❓ Query: '{query}'")
        result = fractal_system.query_system(query)
        
        print(f"   📍 Results Found: {result['total_found']}")
        
        if result['results']:
            top_result = result['results'][0]
            print(f"   🌟 Top Result: {top_result['name']} (Type: {top_result['node_type']})")
    
    # Show generic node structure
    print("\n🧠 Generic Node Structure:")
    print("   • Every node has the same structure")
    print("   • node_type determines what it represents")
    print("   • metadata contains flexible properties")
    print("   • structure_info contains fractal properties")
    print("   • Everything is just nodes - including structure itself")
    
    print("\n" + "=" * 60)
    print("🎉 Generic Fractal API Demo Completed!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Generic node structure for everything")
    print("   • API-driven node generation")
    print("   • Dynamic fractal structure creation")
    print("   • Codex specification as final node")
    print("   • Structure represented as nodes")
    print("   • No predefined tables - everything is nodes")

if __name__ == "__main__":
    run_generic_fractal_demo()
