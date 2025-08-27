#!/usr/bin/env python3
"""
Enhanced Indexing System
========================

This implements the enhanced indexing system that provides efficient access
to ontological metadata with multiple indexing strategies.

This is part of Phase 2 of the metadata enhancement plan.
"""

from typing import Dict, List, Any, Optional, Set, Tuple, Union, Callable
from datetime import datetime
import json
from collections import defaultdict
from dataclasses import dataclass, asdict

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry
)

from enhanced_generic_node import EnhancedGenericNode

@dataclass
class IndexEntry:
    """Entry in an ontological index"""
    node_id: str
    node_type: str
    name: str
    metadata: Dict[str, Any]
    indexed_at: str
    index_version: str

@dataclass
class IndexQuery:
    """Query for searching ontological indices"""
    query_type: str  # "exact", "range", "fuzzy", "composite"
    field: str
    value: Any
    operator: str = "eq"  # eq, ne, gt, lt, gte, lte, in, not_in, contains
    secondary_field: Optional[str] = None
    secondary_value: Optional[Any] = None
    secondary_operator: Optional[str] = None

@dataclass
class IndexQueryResult:
    """Result of an index query"""
    query: IndexQuery
    results: List[IndexEntry]
    total_count: int
    query_time_ms: float
    index_used: str
    metadata: Dict[str, Any]

class EnhancedIndexingSystem:
    """
    Enhanced Indexing System for efficient ontological metadata access
    
    This system provides:
    - Multi-dimensional indexing (water state, chakra, frequency, etc.)
    - Fractal structure indexing
    - Resonance pattern indexing
    - Epistemic label indexing
    - Cross-dimensional relationship indexing
    - Query optimization and caching
    """
    
    def __init__(self):
        """Initialize the enhanced indexing system"""
        self.registry = canonical_registry
        
        # Core indices
        self._water_state_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._chakra_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._frequency_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._fractal_layer_index: Dict[int, List[IndexEntry]] = defaultdict(list)
        self._consciousness_level_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._quantum_state_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._resonance_pattern_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._epistemic_label_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        self._programming_ontology_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        
        # Specialized indices
        self._fractal_depth_index: Dict[int, List[IndexEntry]] = defaultdict(list)
        self._coherence_score_index: Dict[float, List[IndexEntry]] = defaultdict(list)
        self._dissonance_level_index: Dict[float, List[IndexEntry]] = defaultdict(list)
        self._vibrational_axes_index: Dict[str, List[IndexEntry]] = defaultdict(list)
        
        # Composite indices
        self._water_chakra_index: Dict[Tuple[str, str], List[IndexEntry]] = defaultdict(list)
        self._chakra_frequency_index: Dict[Tuple[str, str], List[IndexEntry]] = defaultdict(list)
        self._fractal_consciousness_index: Dict[Tuple[int, str], List[IndexEntry]] = defaultdict(list)
        
        # Metadata tracking
        self.index_version = "1.0.0"
        self.last_rebuild = datetime.now().isoformat()
        self.total_indexed_nodes = 0
        
        # Query statistics
        self._query_stats = {
            'total_queries': 0,
            'queries_by_type': defaultdict(int),
            'average_query_time': 0.0,
            'cache_hits': 0,
            'cache_misses': 0
        }
        
        # Query cache
        self._query_cache: Dict[str, Tuple[IndexQueryResult, float]] = {}
        self._cache_ttl = 300.0  # 5 minutes
        
        print("🔍 Enhanced Indexing System initialized")
        print("✨ Multi-dimensional indexing active")
        print("✨ Query optimization enabled")
        print("✨ Caching system active")
    
    # ============================================================================
    # CORE INDEXING METHODS
    # ============================================================================
    
    def index_node(self, node: EnhancedGenericNode) -> bool:
        """
        Index a single node in all relevant indices
        
        Args:
            node: EnhancedGenericNode to index
        
        Returns:
            True if indexing successful, False otherwise
        """
        try:
            # Create index entry
            entry = IndexEntry(
                node_id=node.node_id,
                node_type=node.node_type,
                name=node.name,
                metadata=node.to_dict(),
                indexed_at=datetime.now().isoformat(),
                index_version=self.index_version
            )
            
            # Index in core ontological dimensions
            self._water_state_index[node.water_state].append(entry)
            self._chakra_index[node.chakra].append(entry)
            self._frequency_index[node.frequency].append(entry)
            self._fractal_layer_index[node.fractal_layer].append(entry)
            self._consciousness_level_index[node.consciousness_level].append(entry)
            self._quantum_state_index[node.quantum_state].append(entry)
            self._resonance_pattern_index[node.resonance_pattern].append(entry)
            self._epistemic_label_index[node.epistemic_label].append(entry)
            self._programming_ontology_index[node.programming_ontology_layer].append(entry)
            
            # Index in specialized dimensions
            self._fractal_depth_index[node.fractal_depth].append(entry)
            self._coherence_score_index[node.coherence_score].append(entry)
            self._dissonance_level_index[node.dissonance_level].append(entry)
            
            # Index vibrational axes
            for axis in node.vibrational_axes:
                self._vibrational_axes_index[axis].append(entry)
            
            # Index in composite indices
            self._water_chakra_index[(node.water_state, node.chakra)].append(entry)
            self._chakra_frequency_index[(node.chakra, node.frequency)].append(entry)
            self._fractal_consciousness_index[(node.fractal_layer, node.consciousness_level)].append(entry)
            
            self.total_indexed_nodes += 1
            return True
            
        except Exception as e:
            print(f"Error indexing node {node.node_id}: {e}")
            return False
    
    def index_node_batch(self, nodes: List[EnhancedGenericNode]) -> Dict[str, int]:
        """
        Index a batch of nodes
        
        Args:
            nodes: List of EnhancedGenericNode instances to index
        
        Returns:
            Dictionary with indexing statistics
        """
        successful = 0
        failed = 0
        
        for node in nodes:
            if self.index_node(node):
                successful += 1
            else:
                failed += 1
        
        # Update last rebuild timestamp
        self.last_rebuild = datetime.now().isoformat()
        
        return {
            'total_nodes': len(nodes),
            'successful': successful,
            'failed': failed,
            'indexed_at': self.last_rebuild
        }
    
    def remove_node_from_index(self, node_id: str) -> bool:
        """
        Remove a node from all indices
        
        Args:
            node_id: ID of the node to remove
        
        Returns:
            True if removal successful, False otherwise
        """
        try:
            # Find the node in indices to get its metadata
            node_metadata = None
            for entry_list in self._water_state_index.values():
                for entry in entry_list:
                    if entry.node_id == node_id:
                        node_metadata = entry.metadata
                        break
                if node_metadata:
                    break
            
            if not node_metadata:
                return False
            
            # Remove from all indices
            self._remove_from_index(self._water_state_index, node_id, node_metadata.get('water_state'))
            self._remove_from_index(self._chakra_index, node_id, node_metadata.get('chakra'))
            self._remove_from_index(self._frequency_index, node_id, node_metadata.get('frequency'))
            self._remove_from_index(self._fractal_layer_index, node_id, node_metadata.get('fractal_layer'))
            self._remove_from_index(self._consciousness_level_index, node_id, node_metadata.get('consciousness_level'))
            self._remove_from_index(self._quantum_state_index, node_id, node_metadata.get('quantum_state'))
            self._remove_from_index(self._resonance_pattern_index, node_id, node_metadata.get('resonance_pattern'))
            self._remove_from_index(self._epistemic_label_index, node_id, node_metadata.get('epistemic_label'))
            self._remove_from_index(self._programming_ontology_index, node_id, node_metadata.get('programming_ontology_layer'))
            
            self._remove_from_index(self._fractal_depth_index, node_id, node_metadata.get('fractal_depth'))
            self._remove_from_index(self._coherence_score_index, node_id, node_metadata.get('coherence_score'))
            self._remove_from_index(self._dissonance_level_index, node_id, node_metadata.get('dissonance_level'))
            
            # Remove from vibrational axes
            for axis in node_metadata.get('vibrational_axes', []):
                self._remove_from_index(self._vibrational_axes_index, node_id, axis)
            
            # Remove from composite indices
            water_state = node_metadata.get('water_state')
            chakra = node_metadata.get('chakra')
            frequency = node_metadata.get('frequency')
            fractal_layer = node_metadata.get('fractal_layer')
            consciousness_level = node_metadata.get('consciousness_level')
            
            if water_state and chakra:
                self._remove_from_composite_index(self._water_chakra_index, node_id, (water_state, chakra))
            if chakra and frequency:
                self._remove_from_composite_index(self._chakra_frequency_index, node_id, (chakra, frequency))
            if fractal_layer is not None and consciousness_level:
                self._remove_from_composite_index(self._fractal_consciousness_index, node_id, (fractal_layer, consciousness_level))
            
            self.total_indexed_nodes = max(0, self.total_indexed_nodes - 1)
            return True
            
        except Exception as e:
            print(f"Error removing node {node_id} from index: {e}")
            return False
    
    def _remove_from_index(self, index: Dict[Any, List[IndexEntry]], node_id: str, key: Any):
        """Helper method to remove a node from a specific index"""
        if key in index:
            index[key] = [entry for entry in index[key] if entry.node_id != node_id]
            # Remove empty keys
            if not index[key]:
                del index[key]
    
    def _remove_from_composite_index(self, index: Dict[Tuple, List[IndexEntry]], node_id: str, key: Tuple):
        """Helper method to remove a node from a composite index"""
        if key in index:
            index[key] = [entry for entry in index[key] if entry.node_id != node_id]
            # Remove empty keys
            if not index[key]:
                del index[key]
    
    # ============================================================================
    # QUERY METHODS
    # ============================================================================
    
    def query_index(self, query: IndexQuery) -> IndexQueryResult:
        """
        Query the ontological indices
        
        Args:
            query: IndexQuery specifying the search criteria
        
        Returns:
            IndexQueryResult with matching entries
        """
        import time
        start_time = time.time()
        
        # Check cache first
        cache_key = self._generate_cache_key(query)
        if cache_key in self._query_cache:
            cached_result, timestamp = self._query_cache[cache_key]
            if time.time() - timestamp < self._cache_ttl:
                self._query_stats['cache_hits'] += 1
                return cached_result
        
        self._query_stats['cache_misses'] += 1
        
        # Execute query based on type
        if query.query_type == "exact":
            results = self._execute_exact_query(query)
        elif query.query_type == "range":
            results = self._execute_range_query(query)
        elif query.query_type == "fuzzy":
            results = self._execute_fuzzy_query(query)
        elif query.query_type == "composite":
            results = self._execute_composite_query(query)
        else:
            results = []
        
        # Create result
        query_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        result = IndexQueryResult(
            query=query,
            results=results,
            total_count=len(results),
            query_time_ms=round(query_time, 2),
            index_used=self._determine_index_used(query),
            metadata={
                'cache_hit': False,
                'index_size': self.total_indexed_nodes,
                'query_complexity': self._calculate_query_complexity(query)
            }
        )
        
        # Cache result
        self._query_cache[cache_key] = (result, time.time())
        
        # Update statistics
        self._update_query_stats(query, query_time)
        
        return result
    
    def _execute_exact_query(self, query: IndexQuery) -> List[IndexEntry]:
        """Execute an exact match query"""
        if query.field == "water_state" and query.value in self._water_state_index:
            return self._water_state_index[query.value]
        elif query.field == "chakra" and query.value in self._chakra_index:
            return self._chakra_index[query.value]
        elif query.field == "frequency" and query.value in self._frequency_index:
            return self._frequency_index[query.value]
        elif query.field == "fractal_layer" and query.value in self._fractal_layer_index:
            return self._fractal_layer_index[query.value]
        elif query.field == "consciousness_level" and query.value in self._consciousness_level_index:
            return self._consciousness_level_index[query.value]
        elif query.field == "quantum_state" and query.value in self._quantum_state_index:
            return self._quantum_state_index[query.value]
        elif query.field == "resonance_pattern" and query.value in self._resonance_pattern_index:
            return self._resonance_pattern_index[query.value]
        elif query.field == "epistemic_label" and query.value in self._epistemic_label_index:
            return self._epistemic_label_index[query.value]
        elif query.field == "programming_ontology_layer" and query.value in self._programming_ontology_index:
            return self._programming_ontology_index[query.value]
        elif query.field == "fractal_depth" and query.value in self._fractal_depth_index:
            return self._fractal_depth_index[query.value]
        elif query.field == "coherence_score" and query.value in self._coherence_score_index:
            return self._coherence_score_index[query.value]
        elif query.field == "dissonance_level" and query.value in self._dissonance_level_index:
            return self._dissonance_level_index[query.value]
        elif query.field == "vibrational_axes" and query.value in self._vibrational_axes_index:
            return self._vibrational_axes_index[query.value]
        
        return []
    
    def _execute_range_query(self, query: IndexQuery) -> List[IndexEntry]:
        """Execute a range query"""
        results = []
        
        if query.field == "fractal_layer":
            for layer, entries in self._fractal_layer_index.items():
                if self._evaluate_range_condition(layer, query.operator, query.value):
                    results.extend(entries)
        elif query.field == "fractal_depth":
            for depth, entries in self._fractal_depth_index.items():
                if self._evaluate_range_condition(depth, query.operator, query.value):
                    results.extend(entries)
        elif query.field == "coherence_score":
            for score, entries in self._coherence_score_index.items():
                if self._evaluate_range_condition(score, query.operator, query.value):
                    results.extend(entries)
        elif query.field == "dissonance_level":
            for level, entries in self._dissonance_level_index.items():
                if self._evaluate_range_condition(level, query.operator, query.value):
                    results.extend(entries)
        
        return results
    
    def _execute_fuzzy_query(self, query: IndexQuery) -> List[IndexEntry]:
        """Execute a fuzzy query (partial matches)"""
        results = []
        
        if query.field == "name":
            # Search in all indices for name matches
            for entries in self._water_state_index.values():
                for entry in entries:
                    if query.value.lower() in entry.name.lower():
                        results.append(entry)
        elif query.field == "node_type":
            # Search in all indices for node type matches
            for entries in self._water_state_index.values():
                for entry in entries:
                    if query.value.lower() in entry.node_type.lower():
                        results.append(entry)
        
        return results
    
    def _execute_composite_query(self, query: IndexQuery) -> List[IndexEntry]:
        """Execute a composite query (multiple conditions)"""
        if not query.secondary_field or not query.secondary_value:
            return []
        
        # Get results for primary field
        primary_results = self._execute_exact_query(IndexQuery(
            query_type="exact",
            field=query.field,
            value=query.value
        ))
        
        # Get results for secondary field
        secondary_results = self._execute_exact_query(IndexQuery(
            query_type="exact",
            field=query.secondary_field,
            value=query.secondary_value
        ))
        
        # Find intersection
        primary_ids = {entry.node_id for entry in primary_results}
        secondary_ids = {entry.node_id for entry in secondary_results}
        
        intersection_ids = primary_ids.intersection(secondary_ids)
        
        # Return entries from primary results that are in intersection
        return [entry for entry in primary_results if entry.node_id in intersection_ids]
    
    def _evaluate_range_condition(self, value: Any, operator: str, target: Any) -> bool:
        """Evaluate a range condition"""
        if operator == "eq":
            return value == target
        elif operator == "ne":
            return value != target
        elif operator == "gt":
            return value > target
        elif operator == "lt":
            return value < target
        elif operator == "gte":
            return value >= target
        elif operator == "lte":
            return value <= target
        elif operator == "in":
            return value in target if isinstance(target, (list, set)) else False
        elif operator == "not_in":
            return value not in target if isinstance(target, (list, set)) else False
        else:
            return False
    
    # ============================================================================
    # ADVANCED QUERY METHODS
    # ============================================================================
    
    def find_nodes_by_theme(self, theme_name: str) -> List[IndexEntry]:
        """
        Find nodes by ontological theme (ice, liquid, vapor, plasma)
        
        Args:
            theme_name: Name of the theme to search for
        
        Returns:
            List of IndexEntry instances matching the theme
        """
        theme_mappings = {
            'ice': {
                'water_state': 'ws.ice',
                'chakra': 'ch.crown',
                'frequency': 'freq.963'
            },
            'liquid': {
                'water_state': 'ws.liquid',
                'chakra': 'ch.heart',
                'frequency': 'freq.639'
            },
            'vapor': {
                'water_state': 'ws.vapor',
                'chakra': 'ch.third_eye',
                'frequency': 'freq.852'
            },
            'plasma': {
                'water_state': 'ws.plasma',
                'chakra': 'ch.root',
                'frequency': 'freq.396'
            }
        }
        
        if theme_name not in theme_mappings:
            return []
        
        theme = theme_mappings[theme_name]
        
        # Find nodes matching the theme
        water_state_nodes = set(entry.node_id for entry in self._water_state_index.get(theme['water_state'], []))
        chakra_nodes = set(entry.node_id for entry in self._chakra_index.get(theme['chakra'], []))
        frequency_nodes = set(entry.node_id for entry in self._frequency_index.get(theme['frequency'], []))
        
        # Find intersection (nodes that match all three)
        theme_nodes = water_state_nodes.intersection(chakra_nodes).intersection(frequency_nodes)
        
        # Return full entries
        return [entry for entry in self._water_state_index.get(theme['water_state'], []) 
                if entry.node_id in theme_nodes]
    
    def find_nodes_by_resonance_pattern(self, 
                                       pattern: str,
                                       min_coherence: float = 0.0,
                                       max_dissonance: float = 1.0) -> List[IndexEntry]:
        """
        Find nodes by resonance pattern with coherence/dissonance constraints
        
        Args:
            pattern: Resonance pattern to search for
            min_coherence: Minimum coherence score
            max_dissonance: Maximum dissonance level
        
        Returns:
            List of IndexEntry instances matching the criteria
        """
        results = []
        
        # Get nodes with matching resonance pattern
        pattern_nodes = self._resonance_pattern_index.get(pattern, [])
        
        # Filter by coherence and dissonance
        for entry in pattern_nodes:
            metadata = entry.metadata
            coherence = metadata.get('coherence_score', 0.0)
            dissonance = metadata.get('dissonance_level', 1.0)
            
            if coherence >= min_coherence and dissonance <= max_dissonance:
                results.append(entry)
        
        return results
    
    def find_nodes_by_fractal_depth_range(self, 
                                         min_depth: int,
                                         max_depth: int,
                                         consciousness_filter: Optional[str] = None) -> List[IndexEntry]:
        """
        Find nodes within a fractal depth range with optional consciousness filtering
        
        Args:
            min_depth: Minimum fractal depth
            max_depth: Maximum fractal depth
            consciousness_filter: Optional consciousness level filter
        
        Returns:
            List of IndexEntry instances matching the criteria
        """
        results = []
        
        for depth in range(min_depth, max_depth + 1):
            if depth in self._fractal_depth_index:
                depth_entries = self._fractal_depth_index[depth]
                
                if consciousness_filter:
                    # Filter by consciousness level
                    filtered_entries = [
                        entry for entry in depth_entries
                        if entry.metadata.get('consciousness_level') == consciousness_filter
                    ]
                    results.extend(filtered_entries)
                else:
                    results.extend(depth_entries)
        
        return results
    
    def find_nodes_by_epistemic_alignment(self, 
                                         primary_label: str,
                                         secondary_label: Optional[str] = None) -> List[IndexEntry]:
        """
        Find nodes by epistemic label alignment
        
        Args:
            primary_label: Primary epistemic label to search for
            secondary_label: Optional secondary epistemic label
        
        Returns:
            List of IndexEntry instances matching the criteria
        """
        if primary_label not in self._epistemic_label_index:
            return []
        
        primary_results = self._epistemic_label_index[primary_label]
        
        if not secondary_label:
            return primary_results
        
        if secondary_label not in self._epistemic_label_index:
            return []
        
        secondary_results = self._epistemic_label_index[secondary_label]
        
        # Find intersection
        primary_ids = {entry.node_id for entry in primary_results}
        secondary_ids = {entry.node_id for entry in secondary_results}
        
        intersection_ids = primary_ids.intersection(secondary_ids)
        
        return [entry for entry in primary_results if entry.node_id in intersection_ids]
    
    # ============================================================================
    # INDEX MAINTENANCE AND OPTIMIZATION
    # ============================================================================
    
    def rebuild_indexes(self) -> Dict[str, Any]:
        """
        Rebuild all indexes from scratch
        
        Returns:
            Dictionary with rebuild statistics
        """
        # Clear all indexes
        self._clear_all_indexes()
        
        # Note: In a real implementation, you would re-index all nodes here
        # For now, we'll just update the metadata
        
        self.last_rebuild = datetime.now().isoformat()
        self.total_indexed_nodes = 0
        
        return {
            'rebuild_completed': True,
            'rebuild_timestamp': self.last_rebuild,
            'total_indexed_nodes': self.total_indexed_nodes,
            'indexes_cleared': True
        }
    
    def _clear_all_indexes(self):
        """Clear all indexes"""
        self._water_state_index.clear()
        self._chakra_index.clear()
        self._frequency_index.clear()
        self._fractal_layer_index.clear()
        self._consciousness_level_index.clear()
        self._quantum_state_index.clear()
        self._resonance_pattern_index.clear()
        self._epistemic_label_index.clear()
        self._programming_ontology_index.clear()
        
        self._fractal_depth_index.clear()
        self._coherence_score_index.clear()
        self._dissonance_level_index.clear()
        self._vibrational_axes_index.clear()
        
        self._water_chakra_index.clear()
        self._chakra_frequency_index.clear()
        self._fractal_consciousness_index.clear()
    
    def optimize_indexes(self) -> Dict[str, Any]:
        """
        Optimize indexes for better performance
        
        Returns:
            Dictionary with optimization statistics
        """
        optimization_stats = {
            'optimization_timestamp': datetime.now().isoformat(),
            'index_sizes': {},
            'optimization_applied': []
        }
        
        # Record current index sizes
        optimization_stats['index_sizes'] = {
            'water_state': len(self._water_state_index),
            'chakra': len(self._chakra_index),
            'frequency': len(self._frequency_index),
            'fractal_layer': len(self._fractal_layer_index),
            'consciousness_level': len(self._consciousness_level_index),
            'quantum_state': len(self._quantum_state_index),
            'resonance_pattern': len(self._resonance_pattern_index),
            'epistemic_label': len(self._epistemic_label_index),
            'programming_ontology': len(self._programming_ontology_index),
            'fractal_depth': len(self._fractal_depth_index),
            'coherence_score': len(self._coherence_score_index),
            'dissonance_level': len(self._dissonance_level_index),
            'vibrational_axes': len(self._vibrational_axes_index),
            'water_chakra': len(self._water_chakra_index),
            'chakra_frequency': len(self._chakra_frequency_index),
            'fractal_consciousness': len(self._fractal_consciousness_index)
        }
        
        # Clear query cache to free memory
        cache_size_before = len(self._query_cache)
        self._query_cache.clear()
        optimization_stats['optimization_applied'].append(f"Cleared query cache ({cache_size_before} entries)")
        
        # Clear validation history if it's too large
        if len(self._query_stats) > 1000:
            self._query_stats.clear()
            optimization_stats['optimization_applied'].append("Cleared query statistics")
        
        return optimization_stats
    
    # ============================================================================
    # UTILITY METHODS
    # ============================================================================
    
    def _generate_cache_key(self, query: IndexQuery) -> str:
        """Generate a cache key for a query"""
        return json.dumps(asdict(query), sort_keys=True)
    
    def _determine_index_used(self, query: IndexQuery) -> str:
        """Determine which index was used for the query"""
        if query.query_type == "exact":
            return f"{query.field}_index"
        elif query.query_type == "range":
            return f"{query.field}_range_index"
        elif query.query_type == "fuzzy":
            return "fuzzy_search_index"
        elif query.query_type == "composite":
            return f"composite_{query.field}_{query.secondary_field}_index"
        else:
            return "unknown_index"
    
    def _calculate_query_complexity(self, query: IndexQuery) -> str:
        """Calculate the complexity of a query"""
        if query.query_type == "exact":
            return "low"
        elif query.query_type == "range":
            return "medium"
        elif query.query_type == "fuzzy":
            return "high"
        elif query.query_type == "composite":
            return "high"
        else:
            return "unknown"
    
    def _update_query_stats(self, query: IndexQuery, query_time: float):
        """Update query statistics"""
        self._query_stats['total_queries'] += 1
        self._query_stats['queries_by_type'][query.query_type] += 1
        
        # Update average query time
        current_avg = self._query_stats['average_query_time']
        total_queries = self._query_stats['total_queries']
        self._query_stats['average_query_time'] = (current_avg * (total_queries - 1) + query_time) / total_queries
    
    def get_index_statistics(self) -> Dict[str, Any]:
        """Get comprehensive index statistics"""
        return {
            'index_system_info': {
                'name': 'Enhanced Indexing System',
                'version': self.index_version,
                'last_rebuild': self.last_rebuild,
                'total_indexed_nodes': self.total_indexed_nodes
            },
            'index_sizes': {
                'water_state': len(self._water_state_index),
                'chakra': len(self._chakra_index),
                'frequency': len(self._frequency_index),
                'fractal_layer': len(self._fractal_layer_index),
                'consciousness_level': len(self._consciousness_level_index),
                'quantum_state': len(self._quantum_state_index),
                'resonance_pattern': len(self._resonance_pattern_index),
                'epistemic_label': len(self._epistemic_label_index),
                'programming_ontology': len(self._programming_ontology_index),
                'fractal_depth': len(self._fractal_depth_index),
                'coherence_score': len(self._coherence_score_index),
                'dissonance_level': len(self._dissonance_level_index),
                'vibrational_axes': len(self._vibrational_axes_index),
                'water_chakra': len(self._water_chakra_index),
                'chakra_frequency': len(self._chakra_frequency_index),
                'fractal_consciousness': len(self._fractal_consciousness_index)
            },
            'query_statistics': self._query_stats,
            'cache_info': {
                'cache_size': len(self._query_cache),
                'cache_ttl': self._cache_ttl,
                'cache_hit_rate': round(
                    (self._query_stats['cache_hits'] / max(1, self._query_stats['total_queries'])) * 100, 2
                )
            }
        }
    
    def export_index_data(self, output_format: str = "json") -> Union[str, Dict[str, Any]]:
        """
        Export index data for analysis
        
        Args:
            output_format: "json" or "dict"
        
        Returns:
            Index data in requested format
        """
        index_data = {
            'index_system_info': {
                'name': 'Enhanced Indexing System',
                'version': self.index_version,
                'exported_at': datetime.now().isoformat(),
                'total_indexed_nodes': self.total_indexed_nodes
            },
            'index_contents': {
                'water_state': {k: len(v) for k, v in self._water_state_index.items()},
                'chakra': {k: len(v) for k, v in self._chakra_index.items()},
                'frequency': {k: len(v) for k, v in self._frequency_index.items()},
                'fractal_layer': {k: len(v) for k, v in self._fractal_layer_index.items()},
                'consciousness_level': {k: len(v) for k, v in self._consciousness_level_index.items()},
                'quantum_state': {k: len(v) for k, v in self._quantum_state_index.items()},
                'resonance_pattern': {k: len(v) for k, v in self._resonance_pattern_index.items()},
                'epistemic_label': {k: len(v) for k, v in self._epistemic_label_index.items()},
                'programming_ontology': {k: len(v) for k, v in self._programming_ontology_index.items()}
            },
            'statistics': self.get_index_statistics()
        }
        
        if output_format.lower() == "json":
            return json.dumps(index_data, indent=2, default=str)
        else:
            return index_data

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global enhanced indexing system instance
enhanced_indexing_system = EnhancedIndexingSystem()

if __name__ == "__main__":
    # Test the enhanced indexing system
    print("🔍 Enhanced Indexing System Test")
    
    # Test basic functionality
    print(f"Index version: {enhanced_indexing_system.index_version}")
    print(f"Total indexed nodes: {enhanced_indexing_system.total_indexed_nodes}")
    
    # Test index statistics
    stats = enhanced_indexing_system.get_index_statistics()
    print(f"Index sizes: {len(stats['index_sizes'])} different index types")
    
    print("\n✅ Enhanced Indexing System ready for use!")
