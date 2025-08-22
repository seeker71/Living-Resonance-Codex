#!/usr/bin/env python3
"""
Enhanced Fractal API
Provides comprehensive navigation and modification capabilities for all knowledge 
and meta-knowledge in the unified fractal node system.
"""

from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel
import sqlite3
import json
import hashlib
from datetime import datetime

# Data Models
class NodeCreate(BaseModel):
    node_type: str
    name: str
    content: str
    parent_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = {}
    structure_info: Optional[Dict[str, Any]] = {}

class NodeUpdate(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    structure_info: Optional[Dict[str, Any]] = None

class QueryRequest(BaseModel):
    query: str
    node_type: Optional[str] = None
    max_results: Optional[int] = 100
    include_metadata: Optional[bool] = True

class NavigationRequest(BaseModel):
    node_id: str
    depth: Optional[int] = 3
    include_relationships: Optional[bool] = True

class EvolutionRequest(BaseModel):
    curiosity_question: str
    exploration_depth: Optional[int] = 5
    generate_nodes: Optional[bool] = True

class EnhancedFractalAPI:
    """Enhanced API for comprehensive fractal node system navigation and modification"""
    
    def __init__(self, db_path: str = "fractal_system.db"):
        self.db_path = db_path
        self.app = FastAPI(
            title="Enhanced Fractal API",
            description="Comprehensive API for navigating and modifying fractal knowledge system",
            version="1.0.0"
        )
        self._setup_routes()
        self._setup_middleware()
    
    def _setup_middleware(self):
        """Setup CORS and other middleware"""
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    def _setup_routes(self):
        """Setup all API routes"""
        
        # Core Node Operations
        @self.app.post("/nodes", response_model=Dict[str, Any])
        async def create_node(node: NodeCreate):
            """Create a new fractal node"""
            return await self._create_node(node)
        
        @self.app.get("/nodes/{node_id}", response_model=Dict[str, Any])
        async def get_node(node_id: str):
            """Get a specific node by ID"""
            return await self._get_node(node_id)
        
        @self.app.put("/nodes/{node_id}", response_model=Dict[str, Any])
        async def update_node(node_id: str, node_update: NodeUpdate):
            """Update an existing node"""
            return await self._update_node(node_id, node_update)
        
        @self.app.delete("/nodes/{node_id}")
        async def delete_node(node_id: str):
            """Delete a node and its children"""
            return await self._delete_node(node_id)
        
        # Knowledge Navigation
        @self.app.post("/navigate", response_model=Dict[str, Any])
        async def navigate_knowledge(nav_request: NavigationRequest):
            """Navigate through knowledge structure"""
            return await self._navigate_knowledge(nav_request)
        
        @self.app.post("/query", response_model=Dict[str, Any])
        async def query_knowledge(query_request: QueryRequest):
            """Query knowledge using natural language or structured queries"""
            return await self._query_knowledge(query_request)
        
        @self.app.get("/explore/{node_id}", response_model=Dict[str, Any])
        async def explore_node(node_id: str, depth: int = 3):
            """Explore a node and its fractal structure"""
            return await self._explore_node(node_id, depth)
        
        # Meta-Knowledge Operations
        @self.app.get("/meta-knowledge", response_model=Dict[str, Any])
        async def get_meta_knowledge():
            """Get overview of meta-knowledge structure"""
            return await self._get_meta_knowledge()
        
        @self.app.get("/meta-knowledge/{meta_type}", response_model=Dict[str, Any])
        async def get_meta_type(meta_type: str):
            """Get specific type of meta-knowledge"""
            return await self._get_meta_type(meta_type)
        
        @self.app.post("/meta-knowledge/evolve", response_model=Dict[str, Any])
        async def evolve_meta_knowledge(evolution_request: EvolutionRequest):
            """Evolve meta-knowledge through curiosity-driven exploration"""
            return await self._evolve_meta_knowledge(evolution_request)
        
        # System Operations
        @self.app.get("/system/overview", response_model=Dict[str, Any])
        async def get_system_overview():
            """Get comprehensive system overview"""
            return await self._get_system_overview()
        
        @self.app.get("/system/stats", response_model=Dict[str, Any])
        async def get_system_stats():
            """Get detailed system statistics"""
            return await self._get_system_stats()
        
        @self.app.post("/system/optimize")
        async def optimize_system():
            """Optimize system performance and structure"""
            return await self._optimize_system()
        
        # Graph Integration Operations
        @self.app.get("/graph/integration", response_model=Dict[str, Any])
        async def get_graph_integration():
            """Get graph integration status and capabilities"""
            return await self._get_graph_integration()
        
        @self.app.post("/graph/query", response_model=Dict[str, Any])
        async def execute_graph_query(query: str):
            """Execute graph queries and return results"""
            return await self._execute_graph_query(query)
        
        # Fractal Operations
        @self.app.get("/fractal/structure", response_model=Dict[str, Any])
        async def get_fractal_structure():
            """Get fractal structure overview"""
            return await self._get_fractal_structure()
        
        @self.app.post("/fractal/explore", response_model=Dict[str, Any])
        async def explore_fractal(exploration_request: Dict[str, Any]):
            """Explore fractal structure at multiple depths"""
            return await self._explore_fractal(exploration_request)
    
    # Implementation Methods
    async def _create_node(self, node: NodeCreate) -> Dict[str, Any]:
        """Create a new fractal node"""
        try:
            node_id = self._generate_node_id(node.content)
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT INTO nodes (node_id, node_type, name, content, parent_id, children, metadata, structure_info)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    node_id,
                    node.node_type,
                    node.name,
                    node.content,
                    node.parent_id or "fractal_system_root",
                    json.dumps([]),
                    json.dumps(node.metadata or {}),
                    json.dumps(node.structure_info or {})
                ))
                
                # Update parent's children list
                if node.parent_id:
                    self._add_child_to_parent(node.parent_id, node_id)
                
                return {"status": "success", "node_id": node_id, "message": "Node created successfully"}
                
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating node: {str(e)}")
    
    async def _get_node(self, node_id: str) -> Dict[str, Any]:
        """Get a specific node by ID"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                row = conn.execute("""
                    SELECT * FROM nodes WHERE node_id = ?
                """, (node_id,)).fetchone()
                
                if not row:
                    raise HTTPException(status_code=404, detail="Node not found")
                
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
                
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving node: {str(e)}")
    
    async def _update_node(self, node_id: str, node_update: NodeUpdate) -> Dict[str, Any]:
        """Update an existing node"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Build update query dynamically
                update_fields = []
                params = []
                
                if node_update.name is not None:
                    update_fields.append("name = ?")
                    params.append(node_update.name)
                
                if node_update.content is not None:
                    update_fields.append("content = ?")
                    params.append(node_update.content)
                
                if node_update.metadata is not None:
                    update_fields.append("metadata = ?")
                    params.append(json.dumps(node_update.metadata))
                
                if node_update.structure_info is not None:
                    update_fields.append("structure_info = ?")
                    params.append(json.dumps(node_update.structure_info))
                
                if not update_fields:
                    raise HTTPException(status_code=400, detail="No fields to update")
                
                params.append(node_id)
                query = f"UPDATE nodes SET {', '.join(update_fields)} WHERE node_id = ?"
                
                conn.execute(query, params)
                
                return {"status": "success", "message": "Node updated successfully"}
                
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating node: {str(e)}")
    
    async def _delete_node(self, node_id: str) -> Dict[str, Any]:
        """Delete a node and its children"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Get all children recursively
                children_to_delete = self._get_all_children(node_id)
                children_to_delete.append(node_id)
                
                # Delete all nodes
                for child_id in children_to_delete:
                    conn.execute("DELETE FROM nodes WHERE node_id = ?", (child_id,))
                
                return {"status": "success", "message": f"Deleted {len(children_to_delete)} nodes"}
                
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting node: {str(e)}")
    
    async def _navigate_knowledge(self, nav_request: NavigationRequest) -> Dict[str, Any]:
        """Navigate through knowledge structure"""
        try:
            navigation_result = {
                "current_node": await self._get_node(nav_request.node_id),
                "navigation_path": [],
                "related_nodes": [],
                "fractal_structure": {}
            }
            
            # Build navigation path
            current_id = nav_request.node_id
            path = []
            for _ in range(nav_request.depth):
                node = await self._get_node(current_id)
                path.append({
                    "node_id": node["node_id"],
                    "name": node["name"],
                    "node_type": node["node_type"]
                })
                
                if node["parent_id"] and node["parent_id"] != "fractal_system_root":
                    current_id = node["parent_id"]
                else:
                    break
            
            navigation_result["navigation_path"] = path
            
            # Get related nodes
            if nav_request.include_relationships:
                navigation_result["related_nodes"] = await self._get_related_nodes(nav_request.node_id)
            
            # Get fractal structure
            navigation_result["fractal_structure"] = await self._get_fractal_structure_for_node(nav_request.node_id)
            
            return navigation_result
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error navigating knowledge: {str(e)}")
    
    async def _query_knowledge(self, query_request: QueryRequest) -> Dict[str, Any]:
        """Query knowledge using natural language or structured queries"""
        try:
            query = query_request.query.lower()
            results = []
            
            with sqlite3.connect(self.db_path) as conn:
                # Search in names and content
                cursor = conn.execute("""
                    SELECT * FROM nodes 
                    WHERE (LOWER(name) LIKE ? OR LOWER(content) LIKE ?)
                    AND (? IS NULL OR node_type = ?)
                    LIMIT ?
                """, (f"%{query}%", f"%{query}%", query_request.node_type, query_request.node_type, query_request.max_results))
                
                for row in cursor.fetchall():
                    node_data = {
                        "node_id": row[0],
                        "node_type": row[1],
                        "name": row[2],
                        "content": row[3][:200] + "..." if len(row[3]) > 200 else row[3],
                        "parent_id": row[4]
                    }
                    
                    if query_request.include_metadata:
                        node_data["metadata"] = json.loads(row[6])
                        node_data["structure_info"] = json.loads(row[7])
                    
                    results.append(node_data)
            
            return {
                "query": query_request.query,
                "total_found": len(results),
                "results": results,
                "query_type": "text_search"
            }
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error querying knowledge: {str(e)}")
    
    async def _explore_node(self, node_id: str, depth: int) -> Dict[str, Any]:
        """Explore a node and its fractal structure"""
        try:
            exploration_result = {
                "root_node": await self._get_node(node_id),
                "fractal_layers": {},
                "total_nodes_explored": 0
            }
            
            # Explore fractal structure at different depths
            for current_depth in range(depth + 1):
                layer_nodes = await self._get_nodes_at_depth(node_id, current_depth)
                exploration_result["fractal_layers"][f"depth_{current_depth}"] = {
                    "node_count": len(layer_nodes),
                    "nodes": layer_nodes
                }
                exploration_result["total_nodes_explored"] += len(layer_nodes)
            
            return exploration_result
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error exploring node: {str(e)}")
    
    async def _get_meta_knowledge(self) -> Dict[str, Any]:
        """Get overview of meta-knowledge structure"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Get meta-knowledge nodes
                meta_nodes = conn.execute("""
                    SELECT node_type, COUNT(*) as count 
                    FROM nodes 
                    WHERE node_type LIKE 'meta_%' OR node_type LIKE 'graph_%'
                    GROUP BY node_type
                """).fetchall()
                
                # Get system overview
                total_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
                
                return {
                    "meta_knowledge_types": {row[0]: row[1] for row in meta_nodes},
                    "total_system_nodes": total_nodes,
                    "meta_knowledge_percentage": sum(row[1] for row in meta_nodes) / total_nodes * 100
                }
                
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting meta-knowledge: {str(e)}")
    
    async def _evolve_meta_knowledge(self, evolution_request: EvolutionRequest) -> Dict[str, Any]:
        """Evolve meta-knowledge through curiosity-driven exploration"""
        try:
            evolution_result = {
                "curiosity_question": evolution_request.curiosity_question,
                "exploration_depth": evolution_request.exploration_depth,
                "new_insights": [],
                "generated_nodes": [],
                "evolution_path": []
            }
            
            # Analyze the curiosity question
            question_analysis = self._analyze_curiosity_question(evolution_request.curiosity_question)
            
            # Explore related knowledge
            related_nodes = await self._find_related_knowledge(question_analysis)
            
            # Generate new insights
            new_insights = self._generate_insights_from_question(question_analysis, related_nodes)
            evolution_result["new_insights"] = new_insights
            
            # Generate new nodes if requested
            if evolution_request.generate_nodes:
                new_nodes = await self._generate_nodes_from_insights(new_insights)
                evolution_result["generated_nodes"] = new_nodes
            
            # Record evolution path
            evolution_result["evolution_path"] = {
                "question_analysis": question_analysis,
                "related_knowledge_count": len(related_nodes),
                "insights_generated": len(new_insights),
                "nodes_generated": len(evolution_result["generated_nodes"])
            }
            
            return evolution_result
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error evolving meta-knowledge: {str(e)}")
    
    # Helper Methods
    def _generate_node_id(self, content: str) -> str:
        """Generate a unique node ID from content"""
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def _add_child_to_parent(self, parent_id: str, child_id: str):
        """Add a child to a parent's children list"""
        with sqlite3.connect(self.db_path) as conn:
            parent = conn.execute("SELECT children FROM nodes WHERE node_id = ?", (parent_id,)).fetchone()
            if parent:
                children = json.loads(parent[0])
                if child_id not in children:
                    children.append(child_id)
                    conn.execute("UPDATE nodes SET children = ? WHERE node_id = ?", (json.dumps(children), parent_id))
    
    def _get_all_children(self, node_id: str) -> List[str]:
        """Get all children of a node recursively"""
        with sqlite3.connect(self.db_path) as conn:
            children = []
            stack = [node_id]
            
            while stack:
                current_id = stack.pop()
                current_children = conn.execute("SELECT children FROM nodes WHERE node_id = ?", (current_id,)).fetchone()
                
                if current_children:
                    current_children_list = json.loads(current_children[0])
                    children.extend(current_children_list)
                    stack.extend(current_children_list)
            
            return children
    
    async def _get_related_nodes(self, node_id: str) -> List[Dict[str, Any]]:
        """Get nodes related to a given node"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Get nodes with similar metadata or structure
                node = await self._get_node(node_id)
                node_metadata = node.get("metadata", {})
                
                # Find nodes with similar characteristics
                related = []
                cursor = conn.execute("SELECT * FROM nodes WHERE node_id != ?", (node_id,))
                
                for row in cursor.fetchall():
                    other_metadata = json.loads(row[6])
                    similarity_score = self._calculate_similarity(node_metadata, other_metadata)
                    
                    if similarity_score > 0.3:  # Threshold for relatedness
                        related.append({
                            "node_id": row[0],
                            "name": row[2],
                            "node_type": row[1],
                            "similarity_score": similarity_score
                        })
                
                # Sort by similarity
                related.sort(key=lambda x: x["similarity_score"], reverse=True)
                return related[:10]  # Return top 10 related nodes
                
        except Exception as e:
            return []
    
    def _calculate_similarity(self, metadata1: Dict, metadata2: Dict) -> float:
        """Calculate similarity between two metadata dictionaries"""
        if not metadata1 or not metadata2:
            return 0.0
        
        common_keys = set(metadata1.keys()) & set(metadata2.keys())
        if not common_keys:
            return 0.0
        
        total_similarity = 0.0
        for key in common_keys:
            if metadata1[key] == metadata2[key]:
                total_similarity += 1.0
            elif isinstance(metadata1[key], (int, float)) and isinstance(metadata2[key], (int, float)):
                # Numeric similarity
                diff = abs(metadata1[key] - metadata2[key])
                max_val = max(abs(metadata1[key]), abs(metadata2[key]))
                if max_val > 0:
                    total_similarity += 1.0 - (diff / max_val)
        
        return total_similarity / len(common_keys)
    
    def _analyze_curiosity_question(self, question: str) -> Dict[str, Any]:
        """Analyze a curiosity question to extract key concepts"""
        question_lower = question.lower()
        
        # Extract key concepts
        concepts = []
        if "water" in question_lower or "state" in question_lower:
            concepts.append("water_states")
        if "chakra" in question_lower or "frequency" in question_lower:
            concepts.append("chakra_frequencies")
        if "fractal" in question_lower or "structure" in question_lower:
            concepts.append("fractal_structure")
        if "meta" in question_lower or "knowledge" in question_lower:
            concepts.append("meta_knowledge")
        if "graph" in question_lower or "relationship" in question_lower:
            concepts.append("graph_relationships")
        
        return {
            "question": question,
            "extracted_concepts": concepts,
            "question_type": "curiosity_exploration",
            "complexity": len(concepts)
        }
    
    async def _find_related_knowledge(self, question_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Find knowledge related to a curiosity question"""
        related_nodes = []
        
        for concept in question_analysis["extracted_concepts"]:
            # Search for nodes related to each concept
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT * FROM nodes 
                    WHERE LOWER(content) LIKE ? OR LOWER(name) LIKE ?
                    LIMIT 5
                """, (f"%{concept}%", f"%{concept}%"))
                
                for row in cursor.fetchall():
                    related_nodes.append({
                        "node_id": row[0],
                        "name": row[2],
                        "node_type": row[1],
                        "concept": concept
                    })
        
        return related_nodes
    
    def _generate_insights_from_question(self, question_analysis: Dict[str, Any], related_nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate insights from a curiosity question and related knowledge"""
        insights = []
        
        # Generate insights based on question analysis
        if question_analysis["complexity"] > 2:
            insights.append({
                "type": "complex_relationship",
                "content": f"Question explores {question_analysis['complexity']} interconnected concepts",
                "confidence": 0.8
            })
        
        # Generate insights from related nodes
        concept_groups = {}
        for node in related_nodes:
            concept = node["concept"]
            if concept not in concept_groups:
                concept_groups[concept] = []
            concept_groups[concept].append(node)
        
        for concept, nodes in concept_groups.items():
            if len(nodes) > 1:
                insights.append({
                    "type": "concept_cluster",
                    "content": f"Found {len(nodes)} nodes related to {concept}",
                    "confidence": 0.7,
                    "concept": concept,
                    "node_count": len(nodes)
                })
        
        return insights
    
    async def _generate_nodes_from_insights(self, insights: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate new nodes from insights"""
        generated_nodes = []
        
        for insight in insights:
            # Create a new insight node
            node_data = NodeCreate(
                node_type="curiosity_insight",
                name=f"Insight: {insight['type']}",
                content=insight['content'],
                parent_id="fractal_system_root",
                metadata={
                    "insight_type": insight['type'],
                    "confidence": insight['confidence'],
                    "generated_at": datetime.now().isoformat()
                },
                structure_info={
                    "fractal_depth": 2,
                    "node_type": "curiosity_insight",
                    "parent_system": "fractal_system_root"
                }
            )
            
            # Create the node
            result = await self._create_node(node_data)
            if result["status"] == "success":
                generated_nodes.append({
                    "insight": insight,
                    "generated_node_id": result["node_id"]
                })
        
        return generated_nodes
    
    async def _get_nodes_at_depth(self, root_id: str, depth: int) -> List[Dict[str, Any]]:
        """Get nodes at a specific fractal depth from a root node"""
        if depth == 0:
            return [await self._get_node(root_id)]
        
        nodes_at_depth = []
        current_level = [root_id]
        
        for current_depth in range(depth):
            next_level = []
            for node_id in current_level:
                node = await self._get_node(node_id)
                next_level.extend(node.get("children", []))
            current_level = next_level
            if current_depth == depth - 1:
                # We're at the target depth
                for node_id in current_level:
                    nodes_at_depth.append(await self._get_node(node_id))
        
        return nodes_at_depth
    
    async def _get_fractal_structure_for_node(self, node_id: str) -> Dict[str, Any]:
        """Get fractal structure information for a specific node"""
        try:
            node = await self._get_node(node_id)
            structure_info = node.get("structure_info", {})
            
            return {
                "fractal_depth": structure_info.get("fractal_depth", 0),
                "node_type": structure_info.get("node_type", "unknown"),
                "parent_system": structure_info.get("parent_system", "unknown"),
                "abstraction_level": structure_info.get("abstraction_level", "unknown")
            }
        except Exception:
            return {"error": "Could not retrieve fractal structure"}
    
    async def _get_system_overview(self) -> Dict[str, Any]:
        """Get comprehensive system overview"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Basic counts
                total_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
                
                # Node type distribution
                type_distribution = {}
                cursor = conn.execute("SELECT node_type, COUNT(*) FROM nodes GROUP BY node_type")
                for row in cursor.fetchall():
                    type_distribution[row[0]] = row[1]
                
                # Fractal depth analysis
                max_depth = 0
                depth_distribution = {}
                cursor = conn.execute("SELECT structure_info FROM nodes")
                for row in cursor.fetchall():
                    try:
                        structure = json.loads(row[0])
                        depth = structure.get("fractal_depth", 0)
                        max_depth = max(max_depth, depth)
                        depth_distribution[depth] = depth_distribution.get(depth, 0) + 1
                    except:
                        pass
                
                return {
                    "total_nodes": total_nodes,
                    "node_type_distribution": type_distribution,
                    "max_fractal_depth": max_depth,
                    "depth_distribution": depth_distribution,
                    "system_status": "operational"
                }
                
        except Exception as e:
            return {"error": f"Could not retrieve system overview: {str(e)}"}
    
    async def _get_system_stats(self) -> Dict[str, Any]:
        """Get detailed system statistics"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Metadata analysis
                metadata_stats = {}
                cursor = conn.execute("SELECT metadata FROM nodes WHERE metadata != '{}'")
                for row in cursor.fetchall():
                    try:
                        metadata = json.loads(row[0])
                        for key, value in metadata.items():
                            if key not in metadata_stats:
                                metadata_stats[key] = {"count": 0, "values": set()}
                            metadata_stats[key]["count"] += 1
                            metadata_stats[key]["values"].add(str(value))
                    except:
                        pass
                
                # Convert sets to lists for JSON serialization
                for key in metadata_stats:
                    metadata_stats[key]["values"] = list(metadata_stats[key]["values"])
                
                return {
                    "metadata_analysis": metadata_stats,
                    "database_size": self._get_database_size(),
                    "last_updated": datetime.now().isoformat()
                }
                
        except Exception as e:
            return {"error": f"Could not retrieve system stats: {str(e)}"}
    
    def _get_database_size(self) -> str:
        """Get database file size"""
        try:
            import os
            size_bytes = os.path.getsize(self.db_path)
            if size_bytes < 1024:
                return f"{size_bytes} B"
            elif size_bytes < 1024 * 1024:
                return f"{size_bytes / 1024:.1f} KB"
            else:
                return f"{size_bytes / (1024 * 1024):.1f} MB"
        except:
            return "Unknown"
    
    async def _optimize_system(self) -> Dict[str, Any]:
        """Optimize system performance and structure"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Analyze database
                conn.execute("ANALYZE")
                
                # Optimize indexes
                conn.execute("REINDEX")
                
                # Vacuum database
                conn.execute("VACUUM")
                
                return {
                    "status": "success",
                    "message": "System optimization completed",
                    "operations": ["ANALYZE", "REINDEX", "VACUUM"]
                }
                
        except Exception as e:
            return {"error": f"System optimization failed: {str(e)}"}
    
    async def _get_graph_integration(self) -> Dict[str, Any]:
        """Get graph integration status and capabilities"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Count graph-related nodes
                graph_nodes = conn.execute("""
                    SELECT COUNT(*) FROM nodes WHERE node_type LIKE 'graph_%'
                """).fetchone()[0]
                
                # Get graph node types
                graph_types = {}
                cursor = conn.execute("""
                    SELECT node_type, COUNT(*) FROM nodes 
                    WHERE node_type LIKE 'graph_%' 
                    GROUP BY node_type
                """)
                for row in cursor.fetchall():
                    graph_types[row[0]] = row[1]
                
                return {
                    "integration_status": "active",
                    "total_graph_nodes": graph_nodes,
                    "graph_node_types": graph_types,
                    "capabilities": [
                        "graph_query_execution",
                        "relationship_discovery",
                        "pattern_recognition",
                        "fractal_node_generation"
                    ]
                }
                
        except Exception as e:
            return {"error": f"Could not retrieve graph integration: {str(e)}"}
    
    async def _execute_graph_query(self, query: str) -> Dict[str, Any]:
        """Execute graph queries and return results"""
        try:
            # This would integrate with the actual graph system
            # For now, return a mock response
            return {
                "query": query,
                "results": [],
                "message": "Graph query execution not yet fully implemented",
                "status": "mock_response"
            }
        except Exception as e:
            return {"error": f"Graph query execution failed: {str(e)}"}
    
    async def _get_fractal_structure(self) -> Dict[str, Any]:
        """Get fractal structure overview"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Analyze fractal structure
                fractal_layers = {}
                cursor = conn.execute("""
                    SELECT structure_info FROM nodes 
                    WHERE structure_info != '{}'
                """)
                
                for row in cursor.fetchall():
                    try:
                        structure = json.loads(row[0])
                        depth = structure.get("fractal_depth", 0)
                        layer_type = structure.get("layer_type", "unknown")
                        
                        if depth not in fractal_layers:
                            fractal_layers[depth] = {"count": 0, "types": set()}
                        
                        fractal_layers[depth]["count"] += 1
                        fractal_layers[depth]["types"].add(layer_type)
                    except:
                        pass
                
                # Convert sets to lists
                for depth in fractal_layers:
                    fractal_layers[depth]["types"] = list(fractal_layers[depth]["types"])
                
                return {
                    "fractal_layers": fractal_layers,
                    "total_layers": len(fractal_layers),
                    "structure_type": "hierarchical_fractal"
                }
                
        except Exception as e:
            return {"error": f"Could not retrieve fractal structure: {str(e)}"}
    
    async def _explore_fractal(self, exploration_request: Dict[str, Any]) -> Dict[str, Any]:
        """Explore fractal structure at multiple depths"""
        try:
            root_id = exploration_request.get("root_id", "fractal_system_root")
            max_depth = exploration_request.get("max_depth", 5)
            
            exploration_result = {
                "root_node": await self._get_node(root_id),
                "exploration_depth": max_depth,
                "fractal_layers": {},
                "total_nodes_explored": 0
            }
            
            # Explore each depth level
            for depth in range(max_depth + 1):
                nodes_at_depth = await self._get_nodes_at_depth(root_id, depth)
                exploration_result["fractal_layers"][f"depth_{depth}"] = {
                    "node_count": len(nodes_at_depth),
                    "nodes": [{"node_id": n["node_id"], "name": n["name"], "node_type": n["node_type"]} for n in nodes_at_depth]
                }
                exploration_result["total_nodes_explored"] += len(nodes_at_depth)
            
            return exploration_result
            
        except Exception as e:
            return {"error": f"Fractal exploration failed: {str(e)}"}

def main():
    """Main function to run the enhanced fractal API"""
    
    print("🌟 Enhanced Fractal API")
    print("=" * 50)
    
    # Initialize the API
    api = EnhancedFractalAPI()
    
    print("✅ Enhanced Fractal API initialized successfully!")
    print("\n🚀 Available Endpoints:")
    print("   • POST /nodes - Create new fractal nodes")
    print("   • GET /nodes/{node_id} - Get specific node")
    print("   • PUT /nodes/{node_id} - Update node")
    print("   • DELETE /nodes/{node_id} - Delete node")
    print("   • POST /navigate - Navigate knowledge structure")
    print("   • POST /query - Query knowledge")
    print("   • GET /explore/{node_id} - Explore fractal structure")
    print("   • GET /meta-knowledge - Get meta-knowledge overview")
    print("   • POST /meta-knowledge/evolve - Evolve through curiosity")
    print("   • GET /system/overview - Get system overview")
    print("   • GET /graph/integration - Get graph integration status")
    print("   • GET /fractal/structure - Get fractal structure")
    print("\n🌟 The API is ready to navigate and modify all knowledge and meta-knowledge!")
    print("   Start the server with: uvicorn enhanced_fractal_api:api.app --reload")

if __name__ == "__main__":
    main()
