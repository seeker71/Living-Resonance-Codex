#!/usr/bin/env python3
"""
Living Codex Core Search System - Fractal Holographic Architecture
Following the Living Codex specification principles:
- Everything is just nodes
- Fractal self-similarity at every level
- Meta-circular self-description
- Generic search across all node types
"""

import logging
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json

logger = logging.getLogger(__name__)

@dataclass
class SearchResult:
    """Search result from any system node - following fractal principles"""
    id: str
    type: str
    title: str
    description: str
    content: str
    source: str
    category: str
    relevance_score: float
    metadata: Dict[str, Any]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class SearchQuery:
    """Search query parameters - generic across all node types"""
    query: str
    search_type: str = 'all'
    filters: Dict[str, Any] = field(default_factory=dict)
    limit: int = 50
    offset: int = 0
    sort_by: str = 'relevance'

@dataclass
class SearchResponse:
    """Search response with results and metadata - fractal structure"""
    query: str
    results: List[SearchResult]
    total_count: int
    search_time_ms: float
    facets: Dict[str, Any] = field(default_factory=dict)
    suggestions: List[str] = field(default_factory=list)

class FractalSearchSystem:
    """
    Unified search system that works across all Living Codex nodes
    Following fractal holographic principles from the specification
    """
    
    def __init__(self):
        self.search_index = {}
        self.search_history = []
        self.search_analytics = {
            'total_searches': 0,
            'popular_queries': {},
            'search_patterns': {}
        }
    
    def search(self, query: SearchQuery) -> SearchResponse:
        """Perform unified search through the fractal core system"""
        start_time = datetime.now(timezone.utc)
        
        # Log the search query
        self._log_search(query)
        
        # Search through the fractal core system
        from .core_system import fractal_core_system
        found_nodes = fractal_core_system.search_nodes(query.query)
        
        # Convert GenericNodes to SearchResults
        results = []
        for node in found_nodes:
            search_result = self._convert_node_to_search_result(node, query.query)
            results.append(search_result)
        
        # Apply filters
        if query.filters:
            results = self._apply_filters(results, query.filters)
        
        # Calculate relevance scores
        for result in results:
            if result.relevance_score == 0.0:
                result.relevance_score = self._calculate_relevance(query.query, result)
        
        # Sort results
        results = self._sort_results(results, query.sort_by)
        
        # Apply pagination
        total_count = len(results)
        start_idx = query.offset
        end_idx = start_idx + query.limit
        paginated_results = results[start_idx:end_idx]
        
        # Generate facets and suggestions
        facets = self._generate_fractal_facets(results)
        suggestions = self._generate_suggestions(query.query)
        
        # Calculate search time
        search_time = (datetime.now(timezone.utc) - start_time).total_seconds() * 1000
        
        return SearchResponse(
            query=query.query,
            results=paginated_results,
            total_count=total_count,
            search_time_ms=search_time,
            facets=facets,
            suggestions=suggestions
        )
    
    def _convert_node_to_search_result(self, node, query: str) -> SearchResult:
        """Convert a GenericNode to a SearchResult following fractal principles"""
        # Extract water state and frequency information
        water_state = node.metadata.get('water_state', 'unknown')
        frequency = node.metadata.get('frequency', 0)
        chakra = node.metadata.get('chakra', 'unknown')
        
        # Create category based on fractal layer and water state
        fractal_layer = node.metadata.get('fractal_layer', 0)
        # Ensure fractal_layer is an integer
        try:
            fractal_layer = int(fractal_layer) if fractal_layer is not None else 0
        except (ValueError, TypeError):
            fractal_layer = 0
            
        # Ensure frequency is an integer
        try:
            frequency = int(frequency) if frequency is not None else 0
        except (ValueError, TypeError):
            frequency = 0
            
        category = f"fractal_layer_{fractal_layer}_{water_state}"
        
        # Create source based on node type and structure
        source = f"{node.node_type}_system"
        
        # Calculate initial relevance based on fractal properties
        relevance = 0.0
        if query.lower() in node.name.lower():
            relevance += 1.0
        if query.lower() in node.content.lower():
            relevance += 0.6
        if query.lower() in node.node_type.lower():
            relevance += 0.4
        
        return SearchResult(
            id=node.node_id,
            type=node.node_type,
            title=node.name,
            description=f"Fractal layer {fractal_layer}, {water_state} state, {chakra} chakra",
            content=node.content,
            source=source,
            category=category,
            relevance_score=min(relevance, 1.0),
            metadata={
                'fractal_layer': fractal_layer,
                'water_state': water_state,
                'frequency': frequency,
                'chakra': chakra,
                'self_similar': node.structure_info.get('self_similar', False),
                'meta_circular': node.structure_info.get('meta_circular', False),
                'holographic': node.structure_info.get('holographic', False),
                'parent_id': node.parent_id,
                'children_count': len(node.children)
            },
            created_at=node.created_at,
            updated_at=node.updated_at
        )
    
    def _calculate_relevance(self, query: str, result: SearchResult) -> float:
        """Calculate relevance scores following fractal principles"""
        query_terms = query.lower().split()
        
        score = 0.0
        
        # Title match (highest weight)
        title_lower = result.title.lower()
        for term in query_terms:
            if term in title_lower:
                score += 10.0
        
        # Description match (medium weight)
        desc_lower = result.description.lower()
        for term in query_terms:
            if term in desc_lower:
                score += 5.0
        
        # Content match (lower weight)
        content_lower = result.content.lower()
        for term in query_terms:
            if term in content_lower:
                score += 2.0
        
        # Fractal properties bonus
        if result.metadata.get('self_similar'):
            score += 1.0
        if result.metadata.get('meta_circular'):
            score += 1.0
        if result.metadata.get('holographic'):
            score += 1.0
        
        # Exact phrase match bonus
        if query.lower() in title_lower:
            score += 15.0
        elif query.lower() in desc_lower:
            score += 8.0
        
        return score
    
    def _apply_filters(self, results: List[SearchResult], filters: Dict[str, Any]) -> List[SearchResult]:
        """Apply filters following fractal principles"""
        filtered_results = results
        
        for filter_key, filter_value in filters.items():
            if filter_value and filter_value != 'all':
                if filter_key == 'type':
                    filtered_results = [r for r in filtered_results if r.type == filter_value]
                elif filter_key == 'category':
                    filtered_results = [r for r in filtered_results if r.category == filter_value]
                elif filter_key == 'source':
                    filtered_results = [r for r in filtered_results if r.source == filter_value]
                elif filter_key == 'fractal_layer':
                    filtered_results = [r for r in filtered_results 
                                     if r.metadata.get('fractal_layer') == filter_value]
                elif filter_key == 'water_state':
                    filtered_results = [r for r in filtered_results 
                                     if r.metadata.get('water_state') == filter_value]
                elif filter_key == 'chakra':
                    filtered_results = [r for r in filtered_results 
                                     if r.metadata.get('chakra') == filter_value]
        
        return filtered_results
    
    def _sort_results(self, results: List[SearchResult], sort_by: str) -> List[SearchResult]:
        """Sort search results following fractal principles"""
        if sort_by == 'relevance':
            return sorted(results, key=lambda x: x.relevance_score, reverse=True)
        elif sort_by == 'title':
            return sorted(results, key=lambda x: x.title.lower())
        elif sort_by == 'fractal_layer':
            return sorted(results, key=lambda x: self._safe_int(x.metadata.get('fractal_layer', 0)))
        elif sort_by == 'frequency':
            return sorted(results, key=lambda x: self._safe_int(x.metadata.get('frequency', 0)), reverse=True)
        elif sort_by == 'created_at':
            return sorted(results, key=lambda x: x.created_at or datetime.min, reverse=True)
        elif sort_by == 'updated_at':
            return sorted(results, key=lambda x: x.updated_at or datetime.min, reverse=True)
        else:
            return results
    
    def _safe_int(self, value) -> int:
        """Safely convert value to integer for sorting"""
        try:
            if isinstance(value, str):
                return int(value)
            elif isinstance(value, (int, float)):
                return int(value)
            else:
                return 0
        except (ValueError, TypeError):
            return 0
    
    def _generate_fractal_facets(self, results: List[SearchResult]) -> Dict[str, Any]:
        """Generate search facets following fractal principles"""
        facets = {
            'types': {},
            'categories': {},
            'sources': {},
            'fractal_layers': {},
            'water_states': {},
            'chakras': {},
            'frequencies': {}
        }
        
        for result in results:
            # Type facets
            result_type = result.type
            if result_type not in facets['types']:
                facets['types'][result_type] = 0
            facets['types'][result_type] += 1
            
            # Category facets
            result_category = result.category
            if result_category not in facets['categories']:
                facets['categories'][result_category] = 0
            facets['categories'][result_category] += 1
            
            # Source facets
            result_source = result.source
            if result_source not in facets['sources']:
                facets['sources'][result_source] = 0
            facets['sources'][result_source] += 1
            
            # Fractal layer facets
            fractal_layer = result.metadata.get('fractal_layer', 0)
            if fractal_layer not in facets['fractal_layers']:
                facets['fractal_layers'][fractal_layer] = 0
            facets['fractal_layers'][fractal_layer] += 1
            
            # Water state facets
            water_state = result.metadata.get('water_state')
            if water_state:
                if water_state not in facets['water_states']:
                    facets['water_states'][water_state] = 0
                facets['water_states'][water_state] += 1
            
            # Chakra facets
            chakra = result.metadata.get('chakra')
            if chakra:
                if chakra not in facets['chakras']:
                    facets['chakras'][chakra] = 0
                facets['chakras'][chakra] += 1
            
            # Frequency facets
            frequency = result.metadata.get('frequency')
            if frequency:
                if frequency not in facets['frequencies']:
                    facets['frequencies'][frequency] = 0
                facets['frequencies'][frequency] += 1
        
        return facets
    
    def _generate_suggestions(self, query: str) -> List[str]:
        """Generate search suggestions following fractal principles"""
        suggestions = []
        
        # Add query variations
        if len(query) > 3:
            suggestions.append(query + " fractal")
            suggestions.append(query + " holographic")
            suggestions.append(query + " meta-circular")
            suggestions.append(query + " water state")
            suggestions.append(query + " chakra")
        
        # Add from search history
        for search_data in self.search_history[-5:]:
            if isinstance(search_data, dict) and 'query' in search_data:
                suggestions.append(search_data['query'])
        
        # Return top suggestions
        return suggestions[:10]
    
    def _log_search(self, query: SearchQuery):
        """Log search for analytics following fractal principles"""
        self.search_analytics['total_searches'] += 1
        
        # Track popular queries
        query_str = query.query.lower()
        if query_str not in self.search_analytics['popular_queries']:
            self.search_analytics['popular_queries'][query_str] = 0
        self.search_analytics['popular_queries'][query_str] += 1
        
        # Store in search history
        self.search_history.append({
            'query': query.query,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'filters': query.filters
        })
        
        # Keep history manageable
        if len(self.search_history) > 100:
            self.search_history = self.search_history[-50:]

# Global instance following fractal principles
fractal_search_system = FractalSearchSystem()
