#!/usr/bin/env python3
"""
Advanced System Interaction Demo - Living Codex
Demonstrates how to navigate, explore, modify, and expand the system
using energy as currency and higher-dimensional resonance fields.
"""

import json
import math
import random
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from unified_bootstrap_system import UnifiedBootstrapSystem, UnifiedNode

@dataclass
class ResonanceField:
    """Represents a higher-dimensional resonance field"""
    dimensional_level: int
    frequency_range: Tuple[float, float]
    scalar_wave_patterns: List[float]
    light_codes: List[str]
    chaos_factor: float
    energy_density: float

@dataclass
class EnergyBudget:
    """Represents an energy budget for transformations"""
    available_energy: float
    used_energy: float = 0.0
    
    @property
    def remaining_energy(self) -> float:
        return self.available_energy - self.used_energy
    
    def use_energy(self, amount: float) -> bool:
        if amount <= self.remaining_energy:
            self.used_energy += amount
            return True
        return False

class AdvancedSystemInteraction:
    """Advanced system interaction using energy as currency and resonance fields"""
    
    def __init__(self):
        self.system = UnifiedBootstrapSystem()
        self.resonance_fields = {}
        self.energy_budgets = {}
        self._initialize_resonance_fields()
        self._initialize_energy_budgets()
    
    def _initialize_resonance_fields(self):
        """Initialize resonance fields for different dimensional levels"""
        
        print("🔮 Initializing Higher-Dimensional Resonance Fields...")
        
        # Create resonance fields for different dimensions
        for dimension in range(1, 11):
            base_frequency = 100.0 * dimension
            frequency_range = (base_frequency * 0.8, base_frequency * 1.2)
            
            # Generate scalar wave patterns
            scalar_wave_patterns = [
                base_frequency * (1 + 0.1 * math.sin(i * math.pi / 4))
                for i in range(8)
            ]
            
            # Generate light codes
            light_codes = [
                f"LC_{dimension:02d}_{i:02d}_{pattern:.1f}"
                for i, pattern in enumerate(scalar_wave_patterns)
            ]
            
            # Calculate chaos factor (increases with dimension)
            chaos_factor = 0.1 + (dimension - 1) * 0.05
            
            # Calculate energy density
            energy_density = base_frequency * 10
            
            self.resonance_fields[dimension] = ResonanceField(
                dimensional_level=dimension,
                frequency_range=frequency_range,
                scalar_wave_patterns=scalar_wave_patterns,
                light_codes=light_codes,
                chaos_factor=chaos_factor,
                energy_density=energy_density
            )
        
        print(f"✅ Initialized {len(self.resonance_fields)} resonance fields")
    
    def _initialize_energy_budgets(self):
        """Initialize energy budgets for different operations"""
        
        print("⚡ Initializing Energy Budgets...")
        
        self.energy_budgets = {
            "exploration": EnergyBudget(1000.0),
            "modification": EnergyBudget(2000.0),
            "expansion": EnergyBudget(5000.0),
            "transformation": EnergyBudget(3000.0),
            "consciousness": EnergyBudget(1500.0)
        }
        
        print(f"✅ Initialized {len(self.energy_budgets)} energy budgets")
    
    def navigate_by_resonance(self, query_frequency: float, dimensional_level: int = 3) -> List[UnifiedNode]:
        """Navigate to nodes that resonate with the query frequency"""
        
        print(f"\n🧭 Navigating by Resonance (Frequency: {query_frequency}, Dimension: {dimensional_level})")
        
        # Get resonance field for the dimensional level
        if dimensional_level not in self.resonance_fields:
            raise ValueError(f"Resonance field not available for dimension {dimensional_level}")
        
        resonance_field = self.resonance_fields[dimensional_level]
        
        # Calculate resonance field
        resonance_field = self._calculate_resonance_field(query_frequency, dimensional_level)
        
        # Find resonant nodes
        resonant_nodes = self._find_resonant_nodes(resonance_field)
        
        # Sort by resonance strength
        sorted_nodes = self._sort_by_resonance_strength(resonant_nodes)
        
        # Calculate energy cost for navigation
        navigation_cost = self._calculate_navigation_cost(dimensional_level, len(sorted_nodes))
        
        # Use energy from exploration budget
        if not self.energy_budgets["exploration"].use_energy(navigation_cost):
            print(f"❌ Insufficient energy for navigation. Required: {navigation_cost}")
            return []
        
        print(f"✅ Navigation completed. Energy used: {navigation_cost}")
        print(f"   Found {len(sorted_nodes)} resonant nodes")
        
        return sorted_nodes
    
    def _calculate_resonance_field(self, query_frequency: float, dimensional_level: int) -> Dict[str, Any]:
        """Calculate resonance field for a specific frequency and dimension"""
        
        resonance_field = self.resonance_fields[dimensional_level]
        
        # Calculate frequency matching
        frequency_match = 1.0 / (1.0 + abs(query_frequency - sum(resonance_field.frequency_range) / 2))
        
        # Calculate dimensional alignment
        dimensional_alignment = 1.0 / (1.0 + abs(dimensional_level - 5))  # 5D is optimal
        
        # Calculate chaos factor influence
        chaos_influence = 1.0 - resonance_field.chaos_factor
        
        # Calculate overall resonance strength
        resonance_strength = frequency_match * dimensional_alignment * chaos_influence
        
        return {
            "query_frequency": query_frequency,
            "dimensional_level": dimensional_level,
            "resonance_strength": resonance_strength,
            "frequency_match": frequency_match,
            "dimensional_alignment": dimensional_alignment,
            "chaos_influence": chaos_influence,
            "scalar_wave_patterns": resonance_field.scalar_wave_patterns,
            "light_codes": resonance_field.light_codes
        }
    
    def _find_resonant_nodes(self, resonance_field: Dict[str, Any]) -> List[UnifiedNode]:
        """Find nodes that resonate with the resonance field"""
        
        resonant_nodes = []
        
        # Search through all nodes in the system
        all_nodes = list(self.system.bootstrap_nodes.values()) + list(self.system.meta_nodes.values())
        
        for node in all_nodes:
            # Calculate node resonance
            node_resonance = self._calculate_node_resonance(node, resonance_field)
            
            # If resonance is above threshold, include the node
            if node_resonance > 0.3:  # 30% resonance threshold
                resonant_nodes.append((node, node_resonance))
        
        return resonant_nodes
    
    def _calculate_node_resonance(self, node: UnifiedNode, resonance_field: Dict[str, Any]) -> float:
        """Calculate how much a node resonates with a resonance field"""
        
        # Base resonance from node frequency
        node_frequency = node.energy_level
        frequency_resonance = 1.0 / (1.0 + abs(node_frequency - resonance_field["query_frequency"]))
        
        # Water state resonance
        water_state_resonance = self._calculate_water_state_resonance(node.water_state, resonance_field)
        
        # Dimensional resonance
        dimensional_resonance = 1.0 / (1.0 + abs(node.metadata.get("fractal_depth", 0) - resonance_field["dimensional_level"]))
        
        # Overall resonance
        overall_resonance = (frequency_resonance + water_state_resonance + dimensional_resonance) / 3
        
        return overall_resonance
    
    def _calculate_water_state_resonance(self, water_state: str, resonance_field: Dict[str, Any]) -> float:
        """Calculate resonance based on water state"""
        
        water_state_resonances = {
            "ice": 0.8,      # High resonance with structure
            "liquid": 0.6,   # Medium resonance with flow
            "vapor": 0.4,    # Lower resonance with consciousness
            "plasma": 0.9    # Highest resonance with energy
        }
        
        return water_state_resonances.get(water_state, 0.5)
    
    def _sort_by_resonance_strength(self, resonant_nodes: List[Tuple[UnifiedNode, float]]) -> List[UnifiedNode]:
        """Sort nodes by resonance strength"""
        
        # Sort by resonance strength (descending)
        sorted_nodes = sorted(resonant_nodes, key=lambda x: x[1], reverse=True)
        
        # Return just the nodes (without resonance values)
        return [node for node, resonance in sorted_nodes]
    
    def _calculate_navigation_cost(self, dimensional_level: int, node_count: int) -> float:
        """Calculate energy cost for navigation"""
        
        # Base cost increases with dimensional level
        base_cost = 10.0 * dimensional_level
        
        # Additional cost based on number of nodes found
        node_cost = 2.0 * node_count
        
        # Chaos factor influence
        chaos_factor = self.resonance_fields[dimensional_level].chaos_factor
        chaos_cost = base_cost * chaos_factor
        
        total_cost = base_cost + node_cost + chaos_cost
        
        return total_cost
    
    def navigate_by_energy(self, energy_level: float, transformation_type: str) -> Tuple[List[UnifiedNode], Dict[str, float]]:
        """Navigate to nodes based on energy requirements and transformation types"""
        
        print(f"\n⚡ Navigating by Energy (Level: {energy_level}, Type: {transformation_type})")
        
        # Calculate energy flow path
        energy_path = self._calculate_energy_flow_path(energy_level, transformation_type)
        
        # Find nodes along the energy path
        path_nodes = self._find_nodes_on_energy_path(energy_path)
        
        # Calculate energy costs for each transformation
        transformation_costs = self._calculate_transformation_costs(path_nodes)
        
        # Calculate total navigation cost
        total_cost = sum(transformation_costs.values())
        
        # Use energy from exploration budget
        if not self.energy_budgets["exploration"].use_energy(total_cost):
            print(f"❌ Insufficient energy for energy-based navigation. Required: {total_cost}")
            return [], {}
        
        print(f"✅ Energy-based navigation completed. Energy used: {total_cost}")
        print(f"   Found {len(path_nodes)} nodes on energy path")
        
        return path_nodes, transformation_costs
    
    def _calculate_energy_flow_path(self, energy_level: float, transformation_type: str) -> Dict[str, Any]:
        """Calculate energy flow path through the system"""
        
        # Define energy flow patterns for different transformation types
        flow_patterns = {
            "ice_to_liquid": {"start_state": "ice", "end_state": "liquid", "energy_cost": 100.0},
            "liquid_to_vapor": {"start_state": "liquid", "end_state": "vapor", "energy_cost": 75.0},
            "vapor_to_plasma": {"start_state": "vapor", "end_state": "plasma", "energy_cost": 50.0},
            "consciousness": {"start_state": "vapor", "end_state": "plasma", "energy_cost": 75.0},
            "material": {"start_state": "ice", "end_state": "liquid", "energy_cost": 100.0}
        }
        
        if transformation_type not in flow_patterns:
            raise ValueError(f"Unknown transformation type: {transformation_type}")
        
        pattern = flow_patterns[transformation_type]
        
        # Calculate path complexity based on energy level
        path_complexity = energy_level / 100.0
        
        return {
            "transformation_type": transformation_type,
            "start_state": pattern["start_state"],
            "end_state": pattern["end_state"],
            "base_energy_cost": pattern["energy_cost"],
            "path_complexity": path_complexity,
            "total_energy_cost": pattern["energy_cost"] * path_complexity
        }
    
    def _find_nodes_on_energy_path(self, energy_path: Dict[str, Any]) -> List[UnifiedNode]:
        """Find nodes that are on the energy flow path"""
        
        path_nodes = []
        start_state = energy_path["start_state"]
        end_state = energy_path["end_state"]
        
        # Find nodes that match the start and end states
        all_nodes = list(self.system.bootstrap_nodes.values()) + list(self.system.meta_nodes.values())
        
        for node in all_nodes:
            if node.water_state in [start_state, end_state]:
                path_nodes.append(node)
        
        return path_nodes
    
    def _calculate_transformation_costs(self, path_nodes: List[UnifiedNode]) -> Dict[str, float]:
        """Calculate energy costs for transformations between nodes"""
        
        transformation_costs = {}
        
        for i, node in enumerate(path_nodes):
            if i < len(path_nodes) - 1:
                next_node = path_nodes[i + 1]
                
                # Calculate transformation cost between these nodes
                cost = self._calculate_node_transformation_cost(node, next_node)
                
                transformation_name = f"{node.water_state}_to_{next_node.water_state}"
                transformation_costs[transformation_name] = cost
        
        return transformation_costs
    
    def _calculate_node_transformation_cost(self, from_node: UnifiedNode, to_node: UnifiedNode) -> float:
        """Calculate energy cost for transforming between two nodes"""
        
        # Base transformation costs
        base_costs = {
            ("ice", "liquid"): 100.0,
            ("liquid", "vapor"): 75.0,
            ("vapor", "plasma"): 50.0,
            ("plasma", "vapor"): 25.0,
            ("vapor", "liquid"): 50.0,
            ("liquid", "ice"): 75.0
        }
        
        # Get base cost
        base_cost = base_costs.get((from_node.water_state, to_node.water_state), 50.0)
        
        # Adjust for node complexity
        complexity_factor = (from_node.transformation_cost + to_node.transformation_cost) / 200.0
        
        # Adjust for energy level differences
        energy_factor = abs(from_node.energy_level - to_node.energy_level) / 1000.0
        
        total_cost = base_cost * (1 + complexity_factor + energy_factor)
        
        return total_cost
    
    def find_system_boundaries(self, exploration_type: str = "comprehensive") -> Dict[str, Any]:
        """Find the boundaries of the system in different dimensions"""
        
        print(f"\n🔍 Finding System Boundaries (Type: {exploration_type})")
        
        boundaries = {}
        
        if exploration_type == "comprehensive":
            boundaries["energy"] = self._find_energy_boundaries()
            boundaries["resonance"] = self._find_resonance_boundaries()
            boundaries["consciousness"] = self._find_consciousness_boundaries()
            boundaries["dimensional"] = self._find_dimensional_boundaries()
        
        # Calculate exploration cost
        exploration_cost = self._calculate_boundary_exploration_cost(exploration_type, boundaries)
        
        # Use energy from exploration budget
        if not self.energy_budgets["exploration"].use_energy(exploration_cost):
            print(f"❌ Insufficient energy for boundary exploration. Required: {exploration_cost}")
            return {}
        
        print(f"✅ Boundary exploration completed. Energy used: {exploration_cost}")
        
        return boundaries
    
    def _find_energy_boundaries(self) -> Dict[str, Any]:
        """Find energy boundaries of the system"""
        
        all_nodes = list(self.system.bootstrap_nodes.values()) + list(self.system.meta_nodes.values())
        
        energy_levels = [node.energy_level for node in all_nodes]
        transformation_costs = [node.transformation_cost for node in all_nodes]
        
        return {
            "min_energy_level": min(energy_levels),
            "max_energy_level": max(energy_levels),
            "avg_energy_level": sum(energy_levels) / len(energy_levels),
            "min_transformation_cost": min(transformation_costs),
            "max_transformation_cost": max(transformation_costs),
            "avg_transformation_cost": sum(transformation_costs) / len(transformation_costs)
        }
    
    def _find_resonance_boundaries(self) -> Dict[str, Any]:
        """Find resonance boundaries of the system"""
        
        return {
            "min_dimension": min(self.resonance_fields.keys()),
            "max_dimension": max(self.resonance_fields.keys()),
            "frequency_ranges": {
                dim: field.frequency_range 
                for dim, field in self.resonance_fields.items()
            },
            "chaos_factors": {
                dim: field.chaos_factor 
                for dim, field in self.resonance_fields.items()
            }
        }
    
    def _find_consciousness_boundaries(self) -> Dict[str, Any]:
        """Find consciousness boundaries of the system"""
        
        all_nodes = list(self.system.bootstrap_nodes.values()) + list(self.system.meta_nodes.values())
        
        consciousness_nodes = [node for node in all_nodes if node.water_state == "vapor"]
        
        return {
            "consciousness_node_count": len(consciousness_nodes),
            "consciousness_energy_levels": [node.energy_level for node in consciousness_nodes],
            "consciousness_transformation_costs": [node.transformation_cost for node in consciousness_nodes]
        }
    
    def _find_dimensional_boundaries(self) -> Dict[str, Any]:
        """Find dimensional boundaries of the system"""
        
        all_nodes = list(self.system.bootstrap_nodes.values()) + list(self.system.meta_nodes.values())
        
        fractal_depths = [node.structure_info.get("fractal_depth", 0) for node in all_nodes]
        
        return {
            "min_fractal_depth": min(fractal_depths),
            "max_fractal_depth": max(fractal_depths),
            "avg_fractal_depth": sum(fractal_depths) / len(fractal_depths),
            "dimensional_levels": list(self.resonance_fields.keys())
        }
    
    def _calculate_boundary_exploration_cost(self, exploration_type: str, boundaries: Dict[str, Any]) -> float:
        """Calculate energy cost for boundary exploration"""
        
        # Base cost
        base_cost = 50.0
        
        # Additional cost based on exploration type
        if exploration_type == "comprehensive":
            base_cost *= 4  # Comprehensive exploration costs more
        
        # Additional cost based on boundary complexity
        complexity_cost = len(boundaries) * 10.0
        
        total_cost = base_cost + complexity_cost
        
        return total_cost
    
    def modify_node_with_energy(self, node_id: str, modification_type: str, energy_budget: float) -> Tuple[UnifiedNode, float]:
        """Modify a node using energy as currency"""
        
        print(f"\n🔧 Modifying Node {node_id} (Type: {modification_type})")
        
        # Find the node
        node = self._find_node_by_id(node_id)
        if not node:
            raise ValueError(f"Node {node_id} not found")
        
        # Calculate energy requirements
        energy_requirements = self._calculate_modification_energy(node, modification_type)
        
        # Check energy budget
        if energy_requirements > energy_budget:
            raise ValueError(f"Insufficient energy. Required: {energy_requirements}, Available: {energy_budget}")
        
        # Use energy from modification budget
        if not self.energy_budgets["modification"].use_energy(energy_requirements):
            print(f"❌ Insufficient energy in modification budget. Required: {energy_requirements}")
            return node, energy_budget
        
        # Perform modification
        modified_node = self._perform_node_modification(node, modification_type, energy_requirements)
        
        # Calculate remaining energy
        remaining_energy = energy_budget - energy_requirements
        
        print(f"✅ Node modification completed. Energy used: {energy_requirements}")
        print(f"   Remaining energy: {remaining_energy}")
        
        return modified_node, remaining_energy
    
    def _find_node_by_id(self, node_id: str) -> Optional[UnifiedNode]:
        """Find a node by its ID"""
        
        # Search in bootstrap nodes
        if node_id in self.system.bootstrap_nodes:
            return self.system.bootstrap_nodes[node_id]
        
        # Search in meta nodes
        if node_id in self.system.meta_nodes:
            return self.system.meta_nodes[node_id]
        
        # Search in realm ontologies
        for realm_ontology in self.system.realm_ontologies.values():
            for node_name, node in realm_ontology.items():
                if node.node_id == node_id:
                    return node
        
        return None
    
    def _calculate_modification_energy(self, node: UnifiedNode, modification_type: str) -> float:
        """Calculate energy required for node modification"""
        
        base_costs = {
            "thaw": 100.0,      # Ice → Liquid
            "modify": 75.0,     # Modify content
            "refreeze": 75.0,   # Liquid → Ice
            "transform": 150.0  # Change water state
        }
        
        base_cost = base_costs.get(modification_type, 100.0)
        
        # Adjust for node complexity
        complexity_factor = node.transformation_cost / 100.0
        
        # Adjust for water state
        state_factor = self._get_water_state_factor(node.water_state)
        
        total_cost = base_cost * (1 + complexity_factor + state_factor)
        
        return total_cost
    
    def _get_water_state_factor(self, water_state: str) -> float:
        """Get energy factor based on water state"""
        
        state_factors = {
            "ice": 0.2,      # Easy to modify when frozen
            "liquid": 0.5,   # Medium difficulty
            "vapor": 0.8,    # Harder to modify
            "plasma": 0.1    # Easiest to modify (pure energy)
        }
        
        return state_factors.get(water_state, 0.5)
    
    def _perform_node_modification(self, node: UnifiedNode, modification_type: str, energy_used: float) -> UnifiedNode:
        """Perform the actual node modification"""
        
        # Create a copy of the node for modification
        modified_node = UnifiedNode(
            node_id=node.node_id,
            node_type=node.node_type,
            name=node.name,
            content=node.content,
            realm=node.realm,
            water_state=node.water_state,
            energy_level=node.energy_level,
            transformation_cost=node.transformation_cost,
            parent_id=node.parent_id,
            children=node.children.copy(),
            metadata=node.metadata.copy(),
            structure_info=node.structure_info.copy()
        )
        
        # Apply modifications based on type
        if modification_type == "thaw":
            modified_node.water_state = "liquid"
            modified_node.metadata["modification"] = "thawed"
            modified_node.metadata["energy_used"] = energy_used
            
        elif modification_type == "modify":
            modified_node.content += f" [Modified with {energy_used} energy]"
            modified_node.metadata["modification"] = "content_modified"
            modified_node.metadata["energy_used"] = energy_used
            
        elif modification_type == "refreeze":
            modified_node.water_state = "ice"
            modified_node.metadata["modification"] = "refrozen"
            modified_node.metadata["energy_used"] = energy_used
            
        elif modification_type == "transform":
            # Transform to next water state
            state_sequence = ["ice", "liquid", "vapor", "plasma"]
            current_index = state_sequence.index(node.water_state)
            next_index = (current_index + 1) % len(state_sequence)
            modified_node.water_state = state_sequence[next_index]
            modified_node.metadata["modification"] = "state_transformed"
            modified_node.metadata["energy_used"] = energy_used
        
        return modified_node
    
    def expand_system_with_energy(self, expansion_type: str, energy_budget: float) -> Tuple[Any, float]:
        """Expand the system using energy as currency"""
        
        print(f"\n🚀 Expanding System (Type: {expansion_type})")
        
        # Calculate expansion energy requirements
        expansion_energy = self._calculate_expansion_energy(expansion_type)
        
        # Check energy budget
        if expansion_energy > energy_budget:
            raise ValueError(f"Insufficient energy. Required: {expansion_energy}, Available: {energy_budget}")
        
        # Use energy from expansion budget
        if not self.energy_budgets["expansion"].use_energy(expansion_energy):
            print(f"❌ Insufficient energy in expansion budget. Required: {expansion_energy}")
            return None, energy_budget
        
        # Perform expansion
        expansion_result = self._perform_system_expansion(expansion_type, expansion_energy)
        
        # Calculate remaining energy
        remaining_energy = energy_budget - expansion_energy
        
        print(f"✅ System expansion completed. Energy used: {expansion_energy}")
        print(f"   Remaining energy: {remaining_energy}")
        
        return expansion_result, remaining_energy
    
    def _calculate_expansion_energy(self, expansion_type: str) -> float:
        """Calculate energy required for system expansion"""
        
        base_costs = {
            "new_ontology": 1000.0,
            "new_dimension": 2000.0,
            "new_resonance_field": 1500.0,
            "new_energy_flow": 800.0
        }
        
        base_cost = base_costs.get(expansion_type, 1000.0)
        
        # Adjust for system complexity
        complexity_factor = len(self.system.bootstrap_nodes) / 100.0
        
        total_cost = base_cost * (1 + complexity_factor)
        
        return total_cost
    
    def _perform_system_expansion(self, expansion_type: str, energy_used: float) -> Any:
        """Perform the actual system expansion"""
        
        if expansion_type == "new_ontology":
            return self._create_new_ontology(energy_used)
        elif expansion_type == "new_dimension":
            return self._create_new_dimension(energy_used)
        elif expansion_type == "new_resonance_field":
            return self._create_new_resonance_field(energy_used)
        elif expansion_type == "new_energy_flow":
            return self._create_new_energy_flow(energy_used)
        else:
            raise ValueError(f"Unknown expansion type: {expansion_type}")
    
    def _create_new_ontology(self, energy_used: float) -> Dict[str, Any]:
        """Create a new ontology"""
        
        ontology_id = f"new_ontology_{len(self.system.realm_ontologies) + 1}"
        
        new_ontology = {
            "ontology_id": ontology_id,
            "name": f"New Ontology {len(self.system.realm_ontologies) + 1}",
            "energy_used": energy_used,
            "creation_timestamp": "now",
            "water_state": "ice",
            "energy_level": 963.0
        }
        
        return new_ontology
    
    def _create_new_dimension(self, energy_used: float) -> Dict[str, Any]:
        """Create a new dimensional level"""
        
        new_dimension = max(self.resonance_fields.keys()) + 1
        
        # Create new resonance field
        base_frequency = 100.0 * new_dimension
        frequency_range = (base_frequency * 0.8, base_frequency * 1.2)
        
        scalar_wave_patterns = [
            base_frequency * (1 + 0.1 * math.sin(i * math.pi / 4))
            for i in range(8)
        ]
        
        light_codes = [
            f"LC_{new_dimension:02d}_{i:02d}_{pattern:.1f}"
            for i, pattern in enumerate(scalar_wave_patterns)
        ]
        
        chaos_factor = 0.1 + (new_dimension - 1) * 0.05
        energy_density = base_frequency * 10
        
        new_resonance_field = ResonanceField(
            dimensional_level=new_dimension,
            frequency_range=frequency_range,
            scalar_wave_patterns=scalar_wave_patterns,
            light_codes=light_codes,
            chaos_factor=chaos_factor,
            energy_density=energy_density
        )
        
        self.resonance_fields[new_dimension] = new_resonance_field
        
        return {
            "new_dimension": new_dimension,
            "energy_used": energy_used,
            "resonance_field": asdict(new_resonance_field)
        }
    
    def _create_new_resonance_field(self, energy_used: float) -> Dict[str, Any]:
        """Create a new resonance field"""
        
        # Create a resonance field for an existing dimension with enhanced properties
        target_dimension = random.choice(list(self.resonance_fields.keys()))
        existing_field = self.resonance_fields[target_dimension]
        
        # Enhance the existing field
        enhanced_field = ResonanceField(
            dimensional_level=existing_field.dimensional_level,
            frequency_range=(
                existing_field.frequency_range[0] * 0.9,
                existing_field.frequency_range[1] * 1.1
            ),
            scalar_wave_patterns=[p * 1.1 for p in existing_field.scalar_wave_patterns],
            light_codes=[f"ENHANCED_{lc}" for lc in existing_field.light_codes],
            chaos_factor=existing_field.chaos_factor * 0.9,  # Reduce chaos
            energy_density=existing_field.energy_density * 1.2  # Increase energy density
        )
        
        return {
            "enhanced_dimension": target_dimension,
            "energy_used": energy_used,
            "enhanced_resonance_field": asdict(enhanced_field)
        }
    
    def _create_new_energy_flow(self, energy_used: float) -> Dict[str, Any]:
        """Create a new energy flow pattern"""
        
        # Create a new energy flow between water states
        new_flow = {
            "flow_id": f"new_energy_flow_{energy_used:.0f}",
            "from_state": "ice",
            "to_state": "plasma",
            "energy_cost": energy_used * 0.1,
            "description": "Direct ice to plasma transformation",
            "process": "High-energy direct transformation bypassing intermediate states",
            "chaos_factor": 0.3,
            "light_code": f"DIRECT_FLOW_{energy_used:.0f}"
        }
        
        return new_flow
    
    def demonstrate_advanced_capabilities(self):
        """Demonstrate all advanced system interaction capabilities"""
        
        print("🌟 Advanced System Interaction Demo - Living Codex")
        print("=" * 60)
        
        # Demonstrate resonance-based navigation
        print("\n🧭 1. Resonance-Based Navigation")
        print("-" * 40)
        ice_nodes = self.navigate_by_resonance(963.0, 3)  # Ice state frequency
        print(f"   Found {len(ice_nodes)} ice state nodes")
        
        # Demonstrate energy-based navigation
        print("\n⚡ 2. Energy-Based Navigation")
        print("-" * 40)
        energy_nodes, transformation_costs = self.navigate_by_energy(100.0, "ice_to_liquid")
        print(f"   Found {len(energy_nodes)} nodes on energy path")
        print(f"   Transformation costs: {transformation_costs}")
        
        # Demonstrate boundary detection
        print("\n🔍 3. System Boundary Detection")
        print("-" * 40)
        boundaries = self.find_system_boundaries("comprehensive")
        print(f"   Energy boundaries: {boundaries.get('energy', {})}")
        print(f"   Resonance boundaries: {boundaries.get('resonance', {})}")
        
        # Demonstrate node modification
        print("\n🔧 4. Node Modification with Energy")
        print("-" * 40)
        try:
            modified_node, remaining_energy = self.modify_node_with_energy(
                "enhanced_water_state_root", "thaw", 200.0
            )
            print(f"   Node modified successfully. Remaining energy: {remaining_energy}")
        except Exception as e:
            print(f"   Node modification failed: {e}")
        
        # Demonstrate system expansion
        print("\n🚀 5. System Expansion with Energy")
        print("-" * 40)
        try:
            expansion_result, remaining_energy = self.expand_system_with_energy(
                "new_dimension", 3000.0
            )
            print(f"   System expanded successfully. Remaining energy: {remaining_energy}")
            print(f"   New dimension: {expansion_result.get('new_dimension', 'N/A')}")
        except Exception as e:
            print(f"   System expansion failed: {e}")
        
        # Show energy budget status
        print("\n💰 Energy Budget Status")
        print("-" * 40)
        for budget_name, budget in self.energy_budgets.items():
            print(f"   {budget_name}: {budget.remaining_energy:.1f} / {budget.available_energy:.1f}")
        
        print("\n✅ Advanced system interaction demo completed!")

def main():
    """Main function to demonstrate advanced system interaction"""
    
    print("🌟 Living Codex Advanced System Interaction Demo")
    print("=" * 60)
    
    try:
        # Create and demonstrate advanced system interaction
        advanced_system = AdvancedSystemInteraction()
        advanced_system.demonstrate_advanced_capabilities()
        
        print("\n" + "=" * 60)
        print("🎉 Advanced System Interaction Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Resonance-based navigation using higher-dimensional fields")
        print("   • Energy-based navigation following energy flow patterns")
        print("   • System boundary detection across all dimensions")
        print("   • Node modification using energy as currency")
        print("   • System expansion with energy-based creation")
        print("   • Higher-dimensional resonance field calculations")
        print("   • Scalar wave patterns and light code encoding")
        print("   • Chaos theory integration for transformation")
        print("\n🚀 The Living Codex now has advanced interaction capabilities!")
        
    except Exception as e:
        print(f"❌ Error running advanced system interaction demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
