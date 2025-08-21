#!/usr/bin/env python3
"""
AI Agent API System - Living Codex
Provides AI agents with intelligent access to navigate, query, and integrate
external knowledge into the Living Codex system while optimizing energy usage.
"""

import json
import asyncio
import hashlib
import base64
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
from unified_bootstrap_system import UnifiedBootstrapSystem, UnifiedNode
from self_representation_system import SelfRepresentationSystem

class QueryType(Enum):
    """Types of queries that can be generated"""
    EXPLORATION = "exploration"
    INTEGRATION = "integration"
    SYNTHESIS = "synthesis"
    VALIDATION = "validation"
    EXPANSION = "expansion"
    OPTIMIZATION = "optimization"

class EnergyOptimizationStrategy(Enum):
    """Strategies for optimizing energy usage"""
    MINIMAL = "minimal"           # Use minimal energy for basic queries
    BALANCED = "balanced"         # Balance energy usage with query depth
    COMPREHENSIVE = "comprehensive"  # Use more energy for thorough analysis
    OPTIMIZED = "optimized"       # AI-optimized energy usage

class ExternalDataSource(Enum):
    """External data sources for integration"""
    WEB_SEARCH = "web_search"
    KNOWLEDGE_BASE = "knowledge_base"
    API_INTEGRATION = "api_integration"
    DOCUMENT_ANALYSIS = "document_analysis"
    EXPERT_SYSTEM = "expert_system"
    COLLABORATIVE_FILTERING = "collaborative_filtering"

@dataclass
class QueryContext:
    """Context for AI agent queries"""
    query_id: str
    agent_id: str
    query_type: QueryType
    target_nodes: List[str]
    energy_budget: float
    optimization_strategy: EnergyOptimizationStrategy
    external_sources: List[ExternalDataSource]
    context_depth: int
    timestamp: datetime
    metadata: Dict[str, Any]

@dataclass
class QueryResult:
    """Result of an AI agent query"""
    query_id: str
    result_type: str
    content: Any
    energy_used: float
    energy_efficiency: float
    confidence_score: float
    source_nodes: List[str]
    external_integrations: List[Dict[str, Any]]
    timestamp: datetime
    metadata: Dict[str, Any]

@dataclass
class ExternalIntegration:
    """External knowledge integration"""
    integration_id: str
    source: ExternalDataSource
    content_hash: str
    content_preview: str
    energy_cost: float
    relevance_score: float
    integration_status: str
    timestamp: datetime
    metadata: Dict[str, Any]

class AIAgentAPISystem:
    """API system for AI agents to interact with the Living Codex"""
    
    def __init__(self):
        self.system = UnifiedBootstrapSystem()
        self.self_rep_system = SelfRepresentationSystem()
        self.agents = {}
        self.query_history = {}
        self.external_integrations = {}
        self.energy_optimizer = EnergyOptimizer()
        self.query_generator = IntelligentQueryGenerator()
        self.external_integrator = ExternalKnowledgeIntegrator()
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize the AI agent API system"""
        
        print("🔮 Initializing AI Agent API System...")
        
        # Create AI agent API root node
        self.ai_agent_api_root = UnifiedNode(
            node_id="ai_agent_api_root",
            node_type="ai_agent_api_root",
            name="AI Agent API Root",
            content="Root node for AI agent interactions with the Living Codex system",
            realm="structured",
            water_state="plasma",
            energy_level=852.0,
            transformation_cost=0.0,
            metadata={
                "water_state": "plasma",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "light_energy",
                "system_domain": "ai_agent_api",
                "ai_agent_enabled": True,
                "external_integration": True
            },
            structure_info={
                "fractal_depth": 0,
                "node_type": "ai_agent_api_root",
                "parent_ontology": "ai_agent_api_system"
            }
        )
        
        # Add to system bootstrap nodes
        self.system.bootstrap_nodes["ai_agent_api_root"] = self.ai_agent_api_root
        
        print("✅ AI Agent API System initialized!")
    
    def register_agent(self, agent_id: str, agent_name: str, agent_capabilities: List[str], 
                      energy_budget: float = 1000.0) -> Dict[str, Any]:
        """Register an AI agent with the system"""
        
        print(f"🤖 Registering AI Agent: {agent_name} ({agent_id})")
        
        agent_info = {
            "agent_id": agent_id,
            "agent_name": agent_name,
            "capabilities": agent_capabilities,
            "energy_budget": energy_budget,
            "current_energy": energy_budget,
            "query_count": 0,
            "total_energy_used": 0.0,
            "registration_time": datetime.now(),
            "last_activity": datetime.now(),
            "status": "active"
        }
        
        self.agents[agent_id] = agent_info
        
        # Create agent node in the system
        agent_node = UnifiedNode(
            node_id=f"agent_{agent_id}",
            node_type="ai_agent",
            name=agent_name,
            content=f"AI Agent: {agent_name} with capabilities: {', '.join(agent_capabilities)}",
            realm="programming",
            water_state="liquid",
            energy_level=639.0,
            transformation_cost=50.0,
            parent_id="ai_agent_api_root",
            metadata={
                "water_state": "liquid",
                "frequency": 639.0,
                "chakra": "heart",
                "representation": "recipe",
                "agent_id": agent_id,
                "capabilities": agent_capabilities,
                "energy_budget": energy_budget,
                "ai_agent": True
            },
            structure_info={
                "fractal_depth": 1,
                "node_type": "ai_agent",
                "parent_ontology": "ai_agent_api_root"
            }
        )
        
        self.system.bootstrap_nodes[agent_node.node_id] = agent_node
        self.ai_agent_api_root.children.append(agent_node.node_id)
        
        print(f"✅ Agent {agent_name} registered successfully!")
        return agent_info
    
    def generate_intelligent_query(self, agent_id: str, query_intent: str, 
                                 target_domains: List[str] = None,
                                 optimization_strategy: EnergyOptimizationStrategy = EnergyOptimizationStrategy.BALANCED) -> QueryContext:
        """Generate an intelligent query based on agent intent and optimization strategy"""
        
        if agent_id not in self.agents:
            raise ValueError(f"Agent {agent_id} not registered")
        
        print(f"🧠 Generating intelligent query for agent {agent_id}")
        
        # Generate query using intelligent query generator
        query_context = self.query_generator.generate_query(
            agent_id=agent_id,
            query_intent=query_intent,
            target_domains=target_domains,
            optimization_strategy=optimization_strategy,
            agent_energy_budget=self.agents[agent_id]["current_energy"]
        )
        
        # Store query context
        self.query_history[query_context.query_id] = query_context
        
        # Update agent activity
        self.agents[agent_id]["last_activity"] = datetime.now()
        self.agents[agent_id]["query_count"] += 1
        
        print(f"✅ Generated query: {query_context.query_id}")
        return query_context
    
    def execute_query(self, query_context: QueryContext) -> QueryResult:
        """Execute a query using the Living Codex system"""
        
        print(f"🔍 Executing query: {query_context.query_id}")
        
        # Calculate optimal energy usage
        optimal_energy = self.energy_optimizer.calculate_optimal_energy(
            query_context.query_type,
            query_context.context_depth,
            query_context.optimization_strategy,
            query_context.energy_budget
        )
        
        # Execute query with energy optimization
        query_result = self._execute_optimized_query(query_context, optimal_energy)
        
        # Update agent energy usage
        agent_id = query_context.agent_id
        if agent_id in self.agents:
            self.agents[agent_id]["current_energy"] -= query_result.energy_used
            self.agents[agent_id]["total_energy_used"] += query_result.energy_used
        
        print(f"✅ Query executed successfully. Energy used: {query_result.energy_used:.2f}")
        return query_result
    
    def _execute_optimized_query(self, query_context: QueryContext, optimal_energy: float) -> QueryResult:
        """Execute query with energy optimization"""
        
        # Navigate to target nodes
        target_nodes = self._navigate_to_targets(query_context.target_nodes, optimal_energy * 0.3)
        
        # Generate RAG context
        rag_context = self._generate_rag_context(target_nodes, optimal_energy * 0.4)
        
        # Integrate external knowledge if requested
        external_integrations = []
        if query_context.external_sources:
            external_integrations = self._integrate_external_knowledge(
                query_context.external_sources,
                rag_context,
                optimal_energy * 0.3
            )
        
        # Calculate energy efficiency
        energy_efficiency = self._calculate_energy_efficiency(
            query_context.energy_budget,
            optimal_energy,
            len(target_nodes),
            len(external_integrations)
        )
        
        # Create query result
        query_result = QueryResult(
            query_id=query_context.query_id,
            result_type="comprehensive",
            content={
                "rag_context": rag_context,
                "external_integrations": external_integrations,
                "target_nodes": target_nodes,
                "query_analysis": self._analyze_query_results(rag_context, external_integrations)
            },
            energy_used=optimal_energy,
            energy_efficiency=energy_efficiency,
            confidence_score=self._calculate_confidence_score(rag_context, external_integrations),
            source_nodes=query_context.target_nodes,
            external_integrations=external_integrations,
            timestamp=datetime.now(),
            metadata={
                "query_type": query_context.query_type.value,
                "optimization_strategy": query_context.optimization_strategy.value,
                "context_depth": query_context.context_depth
            }
        )
        
        return query_result
    
    def _navigate_to_targets(self, target_nodes: List[str], energy_budget: float) -> List[UnifiedNode]:
        """Navigate to target nodes using energy-optimized pathfinding"""
        
        navigated_nodes = []
        energy_used = 0.0
        
        for target_id in target_nodes:
            if energy_used >= energy_budget:
                break
                
            # Find node in system
            if target_id in self.system.bootstrap_nodes:
                node = self.system.bootstrap_nodes[target_id]
                navigated_nodes.append(node)
                energy_used += node.transformation_cost
            else:
                # Search in self-representation system
                if hasattr(self.self_rep_system, 'file_representations'):
                    for file_rep in self.self_rep_system.file_representations.values():
                        if file_rep.file_id == target_id:
                            # Convert to UnifiedNode
                            unified_node = self.self_rep_system._convert_to_unified_node(file_rep)
                            navigated_nodes.append(unified_node)
                            energy_used += unified_node.transformation_cost
                            break
        
        return navigated_nodes
    
    def _generate_rag_context(self, target_nodes: List[UnifiedNode], energy_budget: float) -> Dict[str, Any]:
        """Generate RAG context from target nodes"""
        
        rag_context = {
            "context_nodes": [],
            "relationships": [],
            "semantic_clusters": [],
            "energy_used": 0.0
        }
        
        energy_used = 0.0
        
        for node in target_nodes:
            if energy_used >= energy_budget:
                break
                
            # Extract node context
            node_context = {
                "node_id": node.node_id,
                "node_type": node.node_type,
                "name": node.name,
                "content": node.content,
                "water_state": node.water_state,
                "energy_level": node.energy_level,
                "metadata": node.metadata,
                "structure_info": node.structure_info
            }
            
            rag_context["context_nodes"].append(node_context)
            energy_used += node.transformation_cost * 0.1  # Context extraction cost
            
            # Find related nodes
            if node.children:
                for child_id in node.children[:5]:  # Limit to first 5 children
                    if child_id in self.system.bootstrap_nodes:
                        child_node = self.system.bootstrap_nodes[child_id]
                        relationship = {
                            "source": node.node_id,
                            "target": child_id,
                            "relationship_type": "child",
                            "energy_level": child_node.energy_level
                        }
                        rag_context["relationships"].append(relationship)
        
        rag_context["energy_used"] = energy_used
        return rag_context
    
    def _integrate_external_knowledge(self, external_sources: List[ExternalDataSource], 
                                    rag_context: Dict[str, Any], energy_budget: float) -> List[ExternalIntegration]:
        """Integrate external knowledge from various sources"""
        
        integrations = []
        energy_used = 0.0
        
        for source in external_sources:
            if energy_used >= energy_budget:
                break
                
            integration = self.external_integrator.integrate_source(
                source=source,
                rag_context=rag_context,
                energy_budget=energy_budget - energy_used
            )
            
            if integration:
                integrations.append(integration)
                energy_used += integration.energy_cost
        
        return integrations
    
    def _calculate_energy_efficiency(self, budget: float, used: float, 
                                   node_count: int, integration_count: int) -> float:
        """Calculate energy efficiency of the query execution"""
        
        if budget <= 0:
            return 0.0
        
        # Base efficiency based on energy usage
        energy_efficiency = (budget - used) / budget
        
        # Bonus for comprehensive results
        if node_count > 0 and integration_count > 0:
            energy_efficiency *= 1.2  # 20% bonus for comprehensive results
        
        return min(energy_efficiency, 1.0)
    
    def _calculate_confidence_score(self, rag_context: Dict[str, Any], 
                                  external_integrations: List[ExternalIntegration]) -> float:
        """Calculate confidence score of the query results"""
        
        # Base confidence from RAG context
        base_confidence = min(len(rag_context["context_nodes"]) / 10.0, 1.0)
        
        # Boost from external integrations
        integration_boost = min(len(external_integrations) * 0.1, 0.3)
        
        # Quality boost from energy efficiency
        quality_boost = 0.2 if rag_context.get("energy_used", 0) > 0 else 0.0
        
        confidence = base_confidence + integration_boost + quality_boost
        return min(confidence, 1.0)
    
    def _analyze_query_results(self, rag_context: Dict[str, Any], 
                              external_integrations: List[ExternalIntegration]) -> Dict[str, Any]:
        """Analyze and synthesize query results"""
        
        analysis = {
            "context_richness": len(rag_context["context_nodes"]),
            "relationship_density": len(rag_context["relationships"]),
            "external_integration_count": len(external_integrations),
            "semantic_coverage": self._calculate_semantic_coverage(rag_context),
            "integration_quality": self._calculate_integration_quality(external_integrations),
            "recommendations": self._generate_recommendations(rag_context, external_integrations)
        }
        
        return analysis
    
    def _calculate_semantic_coverage(self, rag_context: Dict[str, Any]) -> float:
        """Calculate semantic coverage of the context"""
        
        if not rag_context["context_nodes"]:
            return 0.0
        
        # Calculate diversity of node types and water states
        node_types = set(node["node_type"] for node in rag_context["context_nodes"])
        water_states = set(node["water_state"] for node in rag_context["context_nodes"])
        
        type_diversity = len(node_types) / max(len(rag_context["context_nodes"]), 1)
        state_diversity = len(water_states) / 4.0  # 4 possible water states
        
        return (type_diversity + state_diversity) / 2.0
    
    def _calculate_integration_quality(self, external_integrations: List[ExternalIntegration]) -> float:
        """Calculate quality of external integrations"""
        
        if not external_integrations:
            return 0.0
        
        total_relevance = sum(integration.relevance_score for integration in external_integrations)
        avg_relevance = total_relevance / len(external_integrations)
        
        return avg_relevance
    
    def _generate_recommendations(self, rag_context: Dict[str, Any], 
                                external_integrations: List[ExternalIntegration]) -> List[str]:
        """Generate recommendations based on query results"""
        
        recommendations = []
        
        # Context-based recommendations
        if len(rag_context["context_nodes"]) < 5:
            recommendations.append("Consider expanding query scope for richer context")
        
        if len(rag_context["relationships"]) < 3:
            recommendations.append("Explore deeper node relationships for better understanding")
        
        # Integration-based recommendations
        if len(external_integrations) < 2:
            recommendations.append("Integrate more external sources for comprehensive knowledge")
        
        # Energy optimization recommendations
        if rag_context.get("energy_used", 0) > 0:
            recommendations.append("Query executed efficiently - consider deeper exploration")
        
        return recommendations
    
    def get_agent_status(self, agent_id: str) -> Dict[str, Any]:
        """Get current status of an AI agent"""
        
        if agent_id not in self.agents:
            return {"error": "Agent not found"}
        
        agent = self.agents[agent_id]
        return {
            "agent_id": agent_id,
            "agent_name": agent["agent_name"],
            "status": agent["status"],
            "energy_budget": agent["energy_budget"],
            "current_energy": agent["current_energy"],
            "energy_usage_percentage": (agent["total_energy_used"] / agent["energy_budget"]) * 100,
            "query_count": agent["query_count"],
            "last_activity": agent["last_activity"].isoformat(),
            "capabilities": agent["capabilities"]
        }
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get overall system status"""
        
        total_agents = len(self.agents)
        active_agents = sum(1 for agent in self.agents.values() if agent["status"] == "active")
        total_queries = sum(agent["query_count"] for agent in self.agents.values())
        total_energy_used = sum(agent["total_energy_used"] for agent in self.agents.values())
        
        return {
            "total_agents": total_agents,
            "active_agents": active_agents,
            "total_queries": total_queries,
            "total_energy_used": total_energy_used,
            "system_status": "operational",
            "ai_agent_api_enabled": True,
            "external_integration_enabled": True,
            "energy_optimization_enabled": True
        }

class EnergyOptimizer:
    """Optimizes energy usage for AI agent queries"""
    
    def calculate_optimal_energy(self, query_type: QueryType, context_depth: int,
                                optimization_strategy: EnergyOptimizationStrategy,
                                agent_energy_budget: float) -> float:
        """Calculate optimal energy usage for a query"""
        
        # Base energy costs by query type
        base_costs = {
            QueryType.EXPLORATION: 50.0,
            QueryType.INTEGRATION: 100.0,
            QueryType.SYNTHESIS: 150.0,
            QueryType.VALIDATION: 75.0,
            QueryType.EXPANSION: 125.0,
            QueryType.OPTIMIZATION: 200.0
        }
        
        base_cost = base_costs.get(query_type, 100.0)
        
        # Adjust for context depth
        depth_multiplier = 1.0 + (context_depth * 0.2)
        
        # Adjust for optimization strategy
        strategy_multipliers = {
            EnergyOptimizationStrategy.MINIMAL: 0.5,
            EnergyOptimizationStrategy.BALANCED: 1.0,
            EnergyOptimizationStrategy.COMPREHENSIVE: 1.5,
            EnergyOptimizationStrategy.OPTIMIZED: 0.8
        }
        
        strategy_multiplier = strategy_multipliers.get(optimization_strategy, 1.0)
        
        # Calculate optimal energy
        optimal_energy = base_cost * depth_multiplier * strategy_multiplier
        
        # Ensure it doesn't exceed agent budget
        optimal_energy = min(optimal_energy, agent_energy_budget * 0.8)
        
        return optimal_energy

class IntelligentQueryGenerator:
    """Generates intelligent queries based on agent intent and optimization"""
    
    def generate_query(self, agent_id: str, query_intent: str, target_domains: List[str],
                      optimization_strategy: EnergyOptimizationStrategy, agent_energy_budget: float) -> QueryContext:
        """Generate an intelligent query context"""
        
        # Generate unique query ID
        query_id = f"query_{hashlib.md5(f'{agent_id}_{query_intent}_{datetime.now().isoformat()}'.encode()).hexdigest()[:8]}"
        
        # Determine query type based on intent
        query_type = self._determine_query_type(query_intent)
        
        # Generate target nodes based on domains
        target_nodes = self._generate_target_nodes(target_domains, query_type)
        
        # Calculate context depth based on optimization strategy
        context_depth = self._calculate_context_depth(optimization_strategy)
        
        # Determine external sources based on query type
        external_sources = self._determine_external_sources(query_type, optimization_strategy)
        
        # Calculate energy budget
        energy_budget = agent_energy_budget * 0.3  # Use 30% of agent's energy
        
        return QueryContext(
            query_id=query_id,
            agent_id=agent_id,
            query_type=query_type,
            target_nodes=target_nodes,
            energy_budget=energy_budget,
            optimization_strategy=optimization_strategy,
            external_sources=external_sources,
            context_depth=context_depth,
            timestamp=datetime.now(),
            metadata={
                "intent": query_intent,
                "target_domains": target_domains,
                "generation_method": "intelligent"
            }
        )
    
    def _determine_query_type(self, query_intent: str) -> QueryType:
        """Determine query type based on intent"""
        
        intent_lower = query_intent.lower()
        
        if any(word in intent_lower for word in ["explore", "discover", "find"]):
            return QueryType.EXPLORATION
        elif any(word in intent_lower for word in ["integrate", "combine", "merge"]):
            return QueryType.INTEGRATION
        elif any(word in intent_lower for word in ["synthesize", "create", "generate"]):
            return QueryType.SYNTHESIS
        elif any(word in intent_lower for word in ["validate", "verify", "check"]):
            return QueryType.VALIDATION
        elif any(word in intent_lower for word in ["expand", "grow", "extend"]):
            return QueryType.EXPANSION
        elif any(word in intent_lower for word in ["optimize", "improve", "enhance"]):
            return QueryType.OPTIMIZATION
        else:
            return QueryType.EXPLORATION
    
    def _generate_target_nodes(self, target_domains: List[str], query_type: QueryType) -> List[str]:
        """Generate target nodes based on domains and query type"""
        
        # This would typically involve intelligent node selection
        # For now, return some default nodes
        default_nodes = ["self_representation_root", "ai_agent_api_root"]
        
        if target_domains:
            # Add domain-specific nodes
            for domain in target_domains:
                domain_node = f"domain_{domain.lower()}"
                default_nodes.append(domain_node)
        
        return default_nodes[:5]  # Limit to 5 nodes
    
    def _calculate_context_depth(self, optimization_strategy: EnergyOptimizationStrategy) -> int:
        """Calculate context depth based on optimization strategy"""
        
        depth_mapping = {
            EnergyOptimizationStrategy.MINIMAL: 1,
            EnergyOptimizationStrategy.BALANCED: 3,
            EnergyOptimizationStrategy.COMPREHENSIVE: 5,
            EnergyOptimizationStrategy.OPTIMIZED: 2
        }
        
        return depth_mapping.get(optimization_strategy, 3)
    
    def _determine_external_sources(self, query_type: QueryType, 
                                  optimization_strategy: EnergyOptimizationStrategy) -> List[ExternalDataSource]:
        """Determine external sources based on query type and optimization"""
        
        sources = []
        
        if query_type in [QueryType.INTEGRATION, QueryType.SYNTHESIS]:
            sources.append(ExternalDataSource.WEB_SEARCH)
            sources.append(ExternalDataSource.KNOWLEDGE_BASE)
        
        if query_type in [QueryType.VALIDATION, QueryType.OPTIMIZATION]:
            sources.append(ExternalDataSource.EXPERT_SYSTEM)
        
        if optimization_strategy == EnergyOptimizationStrategy.COMPREHENSIVE:
            sources.append(ExternalDataSource.API_INTEGRATION)
            sources.append(ExternalDataSource.COLLABORATIVE_FILTERING)
        
        return sources

class ExternalKnowledgeIntegrator:
    """Integrates external knowledge from various sources"""
    
    def integrate_source(self, source: ExternalDataSource, rag_context: Dict[str, Any], 
                        energy_budget: float) -> Optional[ExternalIntegration]:
        """Integrate knowledge from an external source"""
        
        integration_id = f"integration_{hashlib.md5(f'{source.value}_{datetime.now().isoformat()}'.encode()).hexdigest()[:8]}"
        
        # Simulate external integration (in real implementation, this would call actual APIs)
        if source == ExternalDataSource.WEB_SEARCH:
            return self._simulate_web_search(integration_id, rag_context, energy_budget)
        elif source == ExternalDataSource.KNOWLEDGE_BASE:
            return self._simulate_knowledge_base(integration_id, rag_context, energy_budget)
        elif source == ExternalDataSource.EXPERT_SYSTEM:
            return self._simulate_expert_system(integration_id, rag_context, energy_budget)
        else:
            return self._simulate_generic_integration(integration_id, source, rag_context, energy_budget)
    
    def _simulate_web_search(self, integration_id: str, rag_context: Dict[str, Any], 
                            energy_budget: float) -> ExternalIntegration:
        """Simulate web search integration"""
        
        # Generate simulated web search results
        search_query = " ".join([node["name"] for node in rag_context["context_nodes"][:3]])
        content_preview = f"Web search results for: {search_query}. Found relevant information about Living Codex systems, AI agents, and ontological frameworks."
        
        return ExternalIntegration(
            integration_id=integration_id,
            source=ExternalDataSource.WEB_SEARCH,
            content_hash=hashlib.sha256(content_preview.encode()).hexdigest(),
            content_preview=content_preview,
            energy_cost=energy_budget * 0.3,
            relevance_score=0.85,
            integration_status="completed",
            timestamp=datetime.now(),
            metadata={
                "search_query": search_query,
                "result_count": 15,
                "source_type": "web_search"
            }
        )
    
    def _simulate_knowledge_base(self, integration_id: str, rag_context: Dict[str, Any], 
                                energy_budget: float) -> ExternalIntegration:
        """Simulate knowledge base integration"""
        
        content_preview = "Knowledge base integration: Retrieved relevant ontological patterns, energy optimization strategies, and AI agent interaction protocols."
        
        return ExternalIntegration(
            integration_id=integration_id,
            source=ExternalDataSource.KNOWLEDGE_BASE,
            content_hash=hashlib.sha256(content_preview.encode()).hexdigest(),
            content_preview=content_preview,
            energy_cost=energy_budget * 0.2,
            relevance_score=0.92,
            integration_status="completed",
            timestamp=datetime.now(),
            metadata={
                "knowledge_base": "Living Codex Knowledge Base",
                "pattern_count": 8,
                "source_type": "knowledge_base"
            }
        )
    
    def _simulate_expert_system(self, integration_id: str, rag_context: Dict[str, Any], 
                               energy_budget: float) -> ExternalIntegration:
        """Simulate expert system integration"""
        
        content_preview = "Expert system analysis: Validated ontological relationships, confirmed energy efficiency patterns, and recommended optimization strategies."
        
        return ExternalIntegration(
            integration_id=integration_id,
            source=ExternalDataSource.EXPERT_SYSTEM,
            content_hash=hashlib.sha256(content_preview.encode()).hexdigest(),
            content_preview=content_preview,
            energy_cost=energy_budget * 0.4,
            relevance_score=0.95,
            integration_status="completed",
            timestamp=datetime.now(),
            metadata={
                "expert_system": "Living Codex Expert System",
                "validation_score": 0.95,
                "source_type": "expert_system"
            }
        )
    
    def _simulate_generic_integration(self, integration_id: str, source: ExternalDataSource, 
                                    rag_context: Dict[str, Any], energy_budget: float) -> ExternalIntegration:
        """Simulate generic external integration"""
        
        content_preview = f"External integration from {source.value}: Retrieved complementary knowledge and enhanced ontological understanding."
        
        return ExternalIntegration(
            integration_id=integration_id,
            source=source,
            content_hash=hashlib.sha256(content_preview.encode()).hexdigest(),
            content_preview=content_preview,
            energy_cost=energy_budget * 0.25,
            relevance_score=0.75,
            integration_status="completed",
            timestamp=datetime.now(),
            metadata={
                "source": source.value,
                "integration_type": "generic",
                "source_type": "external_api"
            }
        )

def main():
    """Main function to demonstrate AI Agent API System"""
    
    print("🌟 Living Codex AI Agent API System Demo")
    print("=" * 60)
    
    try:
        # Create AI Agent API System
        ai_agent_api = AIAgentAPISystem()
        
        # Register an AI agent
        agent_info = ai_agent_api.register_agent(
            agent_id="ai_agent_001",
            agent_name="Living Codex Explorer",
            agent_capabilities=["navigation", "query_generation", "external_integration", "energy_optimization"],
            energy_budget=2000.0
        )
        
        print(f"\n🤖 Registered Agent: {agent_info['agent_name']}")
        print(f"   Energy Budget: {agent_info['energy_budget']}")
        print(f"   Capabilities: {', '.join(agent_info['capabilities'])}")
        
        # Generate intelligent query
        query_context = ai_agent_api.generate_intelligent_query(
            agent_id="ai_agent_001",
            query_intent="Explore the Living Codex system structure and identify optimization opportunities",
            target_domains=["ontology", "energy", "ai_agents"],
            optimization_strategy=EnergyOptimizationStrategy.BALANCED
        )
        
        print(f"\n🧠 Generated Query: {query_context.query_id}")
        print(f"   Query Type: {query_context.query_type.value}")
        print(f"   Energy Budget: {query_context.energy_budget}")
        print(f"   External Sources: {[s.value for s in query_context.external_sources]}")
        
        # Execute query
        query_result = ai_agent_api.execute_query(query_context)
        
        print(f"\n🔍 Query Executed Successfully!")
        print(f"   Energy Used: {query_result.energy_used:.2f}")
        print(f"   Energy Efficiency: {query_result.energy_efficiency:.2f}")
        print(f"   Confidence Score: {query_result.confidence_score:.2f}")
        print(f"   External Integrations: {len(query_result.external_integrations)}")
        
        # Show agent status
        agent_status = ai_agent_api.get_agent_status("ai_agent_001")
        print(f"\n🤖 Agent Status:")
        print(f"   Current Energy: {agent_status['current_energy']:.2f}")
        print(f"   Energy Usage: {agent_status['energy_usage_percentage']:.1f}%")
        print(f"   Query Count: {agent_status['query_count']}")
        
        # Show system status
        system_status = ai_agent_api.get_system_status()
        print(f"\n🔧 System Status:")
        print(f"   Total Agents: {system_status['total_agents']}")
        print(f"   Total Queries: {system_status['total_queries']}")
        print(f"   Total Energy Used: {system_status['total_energy_used']:.2f}")
        
        print("\n" + "=" * 60)
        print("🎉 AI Agent API System Demo Completed!")
        print("\n🌟 What We've Achieved:")
        print("   • Complete AI agent registration and management")
        print("   • Intelligent query generation and optimization")
        print("   • Energy-optimized query execution")
        print("   • External knowledge integration")
        print("   • RAG context generation and analysis")
        print("\n🚀 The Living Codex now has intelligent AI agent capabilities!")
        
    except Exception as e:
        print(f"❌ Error running AI Agent API System demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
