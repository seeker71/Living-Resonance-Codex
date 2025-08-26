"""
Living Codex Inventory and Report System

This system provides comprehensive inventory management and reporting capabilities
for the fractal holographic architecture. It integrates with all fractal components
to generate detailed reports on system health, component status, and architectural integrity.
"""

import json
import os
import sys
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

# Add the src directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.fractal_components import FractalComponent
from core.core_system import fractal_core_system


@dataclass
class InventoryItem:
    """Represents an inventory item with fractal properties"""
    item_id: str
    item_type: str
    name: str
    description: str
    location: str
    fractal_layer: int
    water_state: str
    frequency: float
    chakra: str
    self_similar: bool
    meta_circular: bool
    holographic: bool
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
    health_score: float
    dependencies: List[str]
    relationships: List[str]


@dataclass
class ReportSection:
    """Represents a section of a comprehensive report"""
    title: str
    content: Dict[str, Any]
    summary: str
    recommendations: List[str]
    timestamp: str


@dataclass
class ComprehensiveReport:
    """Represents a comprehensive system report"""
    report_id: str
    title: str
    generated_at: str
    system_version: str
    sections: List[ReportSection]
    overall_health_score: float
    critical_issues: List[str]
    action_items: List[str]
    metadata: Dict[str, Any]


class FractalInventoryReportComponent(FractalComponent):
    """
    Comprehensive inventory and report system for the Living Codex.
    
    This component provides:
    - System-wide inventory management
    - Comprehensive reporting capabilities
    - Health monitoring and diagnostics
    - Dependency analysis
    - Architectural integrity validation
    """
    
    def __init__(self):
        super().__init__(
            component_type="inventory_report_system",
            name="Fractal Inventory and Report System",
            content="Comprehensive inventory management and reporting for the fractal system",
            fractal_layer=8,
            water_state="PLASMA",
            frequency=432
        )
        
        self.inventory_items: Dict[str, InventoryItem] = {}
        self.reports: Dict[str, ComprehensiveReport] = {}
        self.health_monitors: Dict[str, Any] = {}
        
        # Create fractal nodes for capabilities
        self._create_inventory_capability_nodes()
        self._create_report_capability_nodes()
        self._create_health_monitor_nodes()
    
    def _create_inventory_capability_nodes(self):
        """Create fractal nodes for inventory capabilities"""
        capabilities = [
            ("system_inventory", "Complete system inventory management"),
            ("component_inventory", "Component-specific inventory tracking"),
            ("file_inventory", "File system inventory and analysis"),
            ("dependency_inventory", "Dependency tracking and analysis"),
            ("relationship_inventory", "Relationship mapping and analysis")
        ]
        
        for capability_id, description in capabilities:
            self.create_child_node(
                node_type="inventory_capability",
                name=capability_id.replace("_", " ").title(),
                content=description,
                metadata={
                    "fractal_layer": self.fractal_layer + 1,
                    "water_state": "VAPOR",
                    "frequency": int(self.frequency * 1.1),
                    "chakra": self.chakra
                },
                structure_info={
                    "fractal_depth": 1,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True
                }
            )
    
    def _create_report_capability_nodes(self):
        """Create fractal nodes for reporting capabilities"""
        capabilities = [
            ("system_health_report", "Comprehensive system health analysis"),
            ("component_status_report", "Detailed component status reporting"),
            ("architectural_integrity_report", "Architecture validation and analysis"),
            ("performance_report", "System performance metrics and analysis"),
            ("dependency_report", "Dependency health and conflict analysis")
        ]
        
        for capability_id, description in capabilities:
            self.create_child_node(
                node_type="report_capability",
                name=capability_id.replace("_", " ").title(),
                content=description,
                metadata={
                    "fractal_layer": self.fractal_layer + 1,
                    "water_state": "VAPOR",
                    "frequency": int(self.frequency * 1.1),
                    "chakra": self.chakra
                },
                structure_info={
                    "fractal_depth": 1,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True
                }
            )
    
    def _create_health_monitor_nodes(self):
        """Create fractal nodes for health monitoring capabilities"""
        monitors = [
            ("fractal_integrity", "Fractal architecture integrity monitoring"),
            ("component_health", "Component health and status monitoring"),
            ("system_performance", "System performance and resource monitoring"),
            ("dependency_health", "Dependency health and conflict monitoring"),
            ("architectural_coherence", "Architectural coherence and consistency monitoring")
        ]
        
        for monitor_id, description in monitors:
            self.create_child_node(
                node_type="health_monitor",
                name=monitor_id.replace("_", " ").title(),
                content=description,
                metadata={
                    "fractal_layer": self.fractal_layer + 1,
                    "water_state": "VAPOR",
                    "frequency": int(self.frequency * 1.1),
                    "chakra": self.chakra
                },
                structure_info={
                    "fractal_depth": 1,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True
                }
            )
    
    def scan_system_inventory(self) -> Dict[str, Any]:
        """Scan the entire system and create comprehensive inventory"""
        try:
            # Get system status
            system_status = fractal_core_system.get_system_status()
            
            # Scan all components
            components = system_status.get("components", [])
            component_inventory = {}
            
            for component_name in components:
                # Since components is a list of strings, we need to get the actual component data
                component_id = component_name
                component_inventory[component_id] = {
                    "type": "fractal_component",
                    "name": component_name,
                    "description": f"Fractal component: {component_name}",
                    "fractal_layer": 8,  # Default fractal layer for components
                    "water_state": "PLASMA",  # Default water state for components
                    "frequency": 432,  # Default frequency for components
                    "chakra": "CROWN",  # Default chakra for components
                    "health_score": 100.0,  # Default health score for registered components
                    "dependencies": [],
                    "relationships": []
                }
            
            # Scan all nodes
            all_nodes = list(fractal_core_system.nodes.values())
            node_inventory = {}
            
            for node in all_nodes:
                node_id = node.node_id
                node_inventory[node_id] = {
                    "type": "fractal_node",
                    "name": node.name,
                    "description": node.content,
                    "fractal_layer": node.metadata.get("fractal_layer", 0),
                    "water_state": node.metadata.get("water_state", "unknown"),
                    "frequency": node.metadata.get("frequency", 0),
                    "chakra": node.metadata.get("chakra", "unknown"),
                    "health_score": self._calculate_node_health(node),
                    "dependencies": node.metadata.get("dependencies", []),
                    "relationships": node.children
                }
            
            # Create comprehensive inventory
            inventory = {
                "scan_timestamp": datetime.now().isoformat(),
                "system_overview": {
                    "total_components": len(components),
                    "total_nodes": len(all_nodes),
                    "fractal_layers": system_status.get("fractal_layers", []),
                    "water_states": system_status.get("water_states", []),
                    "chakras": system_status.get("chakras", []),
                    "frequencies": system_status.get("frequencies", [])
                },
                "components": component_inventory,
                "nodes": node_inventory,
                "system_health": {
                    "overall_health": self._calculate_system_health(component_inventory, node_inventory),
                    "fractal_integrity": self._validate_fractal_integrity(),
                    "architectural_coherence": self._validate_architectural_coherence(),
                    "dependency_health": self._validate_dependency_health()
                }
            }
            
            # Store inventory
            self.inventory_items["system_inventory"] = InventoryItem(
                item_id="system_inventory",
                item_type="system_scan",
                name="System Inventory Scan",
                description="Comprehensive system inventory scan",
                location="system_memory",
                fractal_layer=0,
                water_state="PLASMA",
                frequency=432.0,
                chakra="CROWN",
                self_similar=True,
                meta_circular=True,
                holographic=True,
                metadata=inventory,
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                health_score=inventory["system_health"]["overall_health"],
                dependencies=[],
                relationships=list(component_inventory.keys())
            )
            
            return inventory
            
        except Exception as e:
            print(f"Error scanning system inventory: {e}")
            return {"error": str(e)}
    
    def _calculate_component_health(self, component: Dict[str, Any]) -> float:
        """Calculate health score for a component"""
        try:
            # Base health score
            health_score = 100.0
            
            # Check for required fields
            required_fields = ["node_id", "name", "content", "fractal_layer"]
            for field in required_fields:
                if not component.get(field):
                    health_score -= 20.0
            
            # Check fractal properties
            if not component.get("self_similar", False):
                health_score -= 10.0
            if not component.get("meta_circular", False):
                health_score -= 10.0
            if not component.get("holographic", False):
                health_score -= 10.0
            
            # Check water state validity
            valid_water_states = ["ICE", "WATER", "VAPOR", "PLASMA", "CRYSTAL", "STEAM", "LIQUID", "GAS", "SOLID", "PLASMA", "QUANTUM", "VOID"]
            if component.get("water_state") not in valid_water_states:
                health_score -= 15.0
            
            # Check chakra validity
            valid_chakras = ["ROOT", "SACRAL", "SOLAR_PLEXUS", "HEART", "THROAT", "THIRD_EYE", "CROWN"]
            if component.get("chakra") not in valid_chakras:
                health_score -= 15.0
            
            return max(0.0, health_score)
            
        except Exception as e:
            print(f"Error calculating component health: {e}")
            return 0.0
    
    def _calculate_node_health(self, node) -> float:
        """Calculate health score for a fractal node"""
        try:
            # Base health score
            health_score = 100.0
            
            # Check for required fields
            if not node.node_id or not node.name:
                health_score -= 30.0
            
            # Check fractal properties
            if not node.structure_info.get("self_similar", False):
                health_score -= 15.0
            if not node.structure_info.get("meta_circular", False):
                health_score -= 15.0
            if not node.structure_info.get("holographic", False):
                health_score -= 15.0
            
            # Check water state validity
            valid_water_states = ["ICE", "WATER", "VAPOR", "PLASMA", "CRYSTAL", "STEAM", "LIQUID", "GAS", "SOLID", "PLASMA", "QUANTUM", "VOID"]
            water_state = node.metadata.get("water_state", "unknown")
            if water_state not in valid_water_states:
                health_score -= 15.0
            
            # Check chakra validity
            valid_chakras = ["ROOT", "SACRAL", "SOLAR_PLEXUS", "HEART", "THROAT", "THIRD_EYE", "CROWN"]
            chakra = node.metadata.get("chakra", "unknown")
            if chakra not in valid_chakras:
                health_score -= 15.0
            
            return max(0.0, health_score)
            
        except Exception as e:
            print(f"Error calculating node health: {e}")
            return 0.0
    
    def _calculate_system_health(self, component_inventory: Dict, node_inventory: Dict) -> float:
        """Calculate overall system health score"""
        try:
            if not component_inventory and not node_inventory:
                return 0.0
            
            total_items = len(component_inventory) + len(node_inventory)
            if total_items == 0:
                return 0.0
            
            total_health = 0.0
            
            # Sum component health
            for component in component_inventory.values():
                total_health += component.get("health_score", 0.0)
            
            # Sum node health
            for node in node_inventory.values():
                total_health += node.get("health_score", 0.0)
            
            return total_health / total_items
            
        except Exception as e:
            print(f"Error calculating system health: {e}")
            return 0.0
    
    def _validate_fractal_integrity(self) -> Dict[str, Any]:
        """Validate fractal architecture integrity"""
        try:
            # Check self-similarity
            all_nodes = list(fractal_core_system.nodes.values())
            self_similar_count = sum(1 for node in all_nodes if node.structure_info.get("self_similar", False))
            self_similarity_ratio = self_similar_count / len(all_nodes) if all_nodes else 0.0
            
            # Check meta-circularity
            meta_circular_count = sum(1 for node in all_nodes if node.structure_info.get("meta_circular", False))
            meta_circularity_ratio = meta_circular_count / len(all_nodes) if all_nodes else 0.0
            
            # Check holographic nature
            holographic_count = sum(1 for node in all_nodes if node.structure_info.get("holographic", False))
            holographic_ratio = holographic_count / len(all_nodes) if all_nodes else 0.0
            
            return {
                "self_similarity": {
                    "ratio": self_similarity_ratio,
                    "score": self_similarity_ratio * 100.0,
                    "status": "HEALTHY" if self_similarity_ratio >= 0.9 else "WARNING" if self_similarity_ratio >= 0.7 else "CRITICAL"
                },
                "meta_circularity": {
                    "ratio": meta_circularity_ratio,
                    "score": meta_circularity_ratio * 100.0,
                    "status": "HEALTHY" if meta_circularity_ratio >= 0.9 else "WARNING" if meta_circularity_ratio >= 0.7 else "CRITICAL"
                },
                "holographic_nature": {
                    "ratio": holographic_ratio,
                    "score": holographic_ratio * 100.0,
                    "status": "HEALTHY" if holographic_ratio >= 0.9 else "WARNING" if holographic_ratio >= 0.7 else "CRITICAL"
                }
            }
            
        except Exception as e:
            print(f"Error validating fractal integrity: {e}")
            return {"error": str(e)}
    
    def _validate_architectural_coherence(self) -> Dict[str, Any]:
        """Validate architectural coherence and consistency"""
        try:
            # Check fractal layer distribution
            all_nodes = list(fractal_core_system.nodes.values())
            layer_distribution = {}
            
            for node in all_nodes:
                layer = node.metadata.get("fractal_layer", 0)
                layer_distribution[layer] = layer_distribution.get(layer, 0) + 1
            
            # Check for gaps in layers
            max_layer = max(layer_distribution.keys()) if layer_distribution else 0
            min_layer = min(layer_distribution.keys()) if layer_distribution else 0
            expected_layers = set(range(min_layer, max_layer + 1))
            actual_layers = set(layer_distribution.keys())
            missing_layers = expected_layers - actual_layers
            
            # Check water state distribution
            water_state_distribution = {}
            for node in all_nodes:
                water_state = node.metadata.get("water_state", "unknown")
                water_state_distribution[water_state] = water_state_distribution.get(water_state, 0) + 1
            
            # Check chakra distribution
            chakra_distribution = {}
            for node in all_nodes:
                chakra = node.metadata.get("chakra", "unknown")
                chakra_distribution[chakra] = chakra_distribution.get(chakra, 0) + 1
            
            return {
                "fractal_layers": {
                    "distribution": layer_distribution,
                    "missing_layers": list(missing_layers),
                    "coverage": len(actual_layers) / len(expected_layers) if expected_layers else 0.0,
                    "status": "HEALTHY" if not missing_layers else "WARNING"
                },
                "water_states": {
                    "distribution": water_state_distribution,
                    "coverage": len(water_state_distribution) / 12.0,  # 12 water states
                    "status": "HEALTHY" if len(water_state_distribution) >= 10 else "WARNING"
                },
                "chakras": {
                    "distribution": chakra_distribution,
                    "coverage": len(chakra_distribution) / 7.0,  # 7 chakras
                    "status": "HEALTHY" if len(chakra_distribution) >= 6 else "WARNING"
                }
            }
            
        except Exception as e:
            print(f"Error validating architectural coherence: {e}")
            return {"error": str(e)}
    
    def _validate_dependency_health(self) -> Dict[str, Any]:
        """Validate dependency health and identify conflicts"""
        try:
            all_nodes = list(fractal_core_system.nodes.values())
            dependency_map = {}
            circular_dependencies = []
            missing_dependencies = []
            
            # Build dependency map
            for node in all_nodes:
                dependencies = node.metadata.get("dependencies", [])
                dependency_map[node.node_id] = dependencies
                
                # Check for missing dependencies
                for dep in dependencies:
                    if not any(n.node_id == dep for n in all_nodes):
                        missing_dependencies.append({
                            "node": node.node_id,
                            "missing_dependency": dep
                        })
            
            # Check for circular dependencies (simplified check)
            for node_id, deps in dependency_map.items():
                for dep in deps:
                    if dep in dependency_map and node_id in dependency_map.get(dep, []):
                        circular_dependencies.append({
                            "node1": node_id,
                            "node2": dep
                        })
            
            return {
                "dependency_map": dependency_map,
                "circular_dependencies": circular_dependencies,
                "missing_dependencies": missing_dependencies,
                "health_score": max(0.0, 100.0 - len(circular_dependencies) * 20.0 - len(missing_dependencies) * 10.0),
                "status": "HEALTHY" if not circular_dependencies and not missing_dependencies else "WARNING" if len(circular_dependencies) <= 2 else "CRITICAL"
            }
            
        except Exception as e:
            print(f"Error validating dependency health: {e}")
            return {"error": str(e)}
    
    def generate_comprehensive_report(self, report_type: str = "system_health") -> ComprehensiveReport:
        """Generate a comprehensive system report"""
        try:
            # Scan system inventory
            inventory = self.scan_system_inventory()
            
            # Generate report sections based on type
            sections = []
            
            if report_type == "system_health":
                sections = self._generate_system_health_sections(inventory)
            elif report_type == "component_status":
                sections = self._generate_component_status_sections(inventory)
            elif report_type == "architectural_integrity":
                sections = self._generate_architectural_integrity_sections(inventory)
            elif report_type == "performance":
                sections = self._generate_performance_sections(inventory)
            elif report_type == "dependency":
                sections = self._generate_dependency_sections(inventory)
            else:
                # Generate all sections
                sections = self._generate_all_sections(inventory)
            
            # Calculate overall health score
            overall_health = inventory.get("system_health", {}).get("overall_health", 0.0)
            
            # Identify critical issues
            critical_issues = self._identify_critical_issues(inventory)
            
            # Generate action items
            action_items = self._generate_action_items(inventory, critical_issues)
            
            # Create comprehensive report
            report = ComprehensiveReport(
                report_id=f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                title=f"Living Codex {report_type.replace('_', ' ').title()} Report",
                generated_at=datetime.now().isoformat(),
                system_version="2.0.0",
                sections=sections,
                overall_health_score=overall_health,
                critical_issues=critical_issues,
                action_items=action_items,
                metadata=inventory
            )
            
            # Store report
            self.reports[report.report_id] = report
            
            # Create fractal node for report
            self.create_child_node(
                node_type="comprehensive_report",
                name=report.title,
                content=f"Generated at {report.generated_at}",
                metadata={
                    "fractal_layer": self.fractal_layer + 1,
                    "water_state": "CRYSTAL",
                    "frequency": int(self.frequency * 1.2),
                    "chakra": "THIRD_EYE",
                    "report_id": report.report_id,
                    "report_type": report_type,
                    "overall_health_score": overall_health,
                    "critical_issues_count": len(critical_issues),
                    "action_items_count": len(action_items)
                },
                structure_info={
                    "fractal_depth": 1,
                    "self_similar": True,
                    "meta_circular": True,
                    "holographic": True
                }
            )
            
            return report
            
        except Exception as e:
            print(f"Error generating comprehensive report: {e}")
            return None
    
    def _generate_system_health_sections(self, inventory: Dict[str, Any]) -> List[ReportSection]:
        """Generate system health report sections"""
        sections = []
        
        # System Overview Section
        system_overview = inventory.get("system_overview", {})
        sections.append(ReportSection(
            title="System Overview",
            content=system_overview,
            summary=f"Total components: {system_overview.get('total_components', 0)}, Total nodes: {system_overview.get('total_nodes', 0)}",
            recommendations=[
                "Monitor component and node growth patterns",
                "Ensure balanced distribution across fractal layers",
                "Maintain diversity in water states and chakras"
            ],
            timestamp=datetime.now().isoformat()
        ))
        
        # System Health Section
        system_health = inventory.get("system_health", {})
        sections.append(ReportSection(
            title="System Health",
            content=system_health,
            summary=f"Overall health score: {system_health.get('overall_health', 0.0):.1f}%",
            recommendations=[
                "Address any health scores below 80%",
                "Investigate components with low health scores",
                "Monitor health trends over time"
            ],
            timestamp=datetime.now().isoformat()
        ))
        
        return sections
    
    def _generate_component_status_sections(self, inventory: Dict[str, Any]) -> List[ReportSection]:
        """Generate component status report sections"""
        sections = []
        
        components = inventory.get("components", {})
        if components:
            # Component Health Distribution
            health_distribution = {}
            for component in components.values():
                health_score = component.get("health_score", 0.0)
                health_range = f"{(int(health_score) // 20) * 20}-{(int(health_score) // 20) * 20 + 19}"
                health_distribution[health_range] = health_distribution.get(health_range, 0) + 1
            
            sections.append(ReportSection(
                title="Component Health Distribution",
                content={"health_distribution": health_distribution, "components": components},
                summary=f"Component health distribution across {len(components)} components",
                recommendations=[
                    "Focus on components with health scores below 60%",
                    "Investigate root causes of low health scores",
                    "Implement health monitoring for critical components"
                ],
                timestamp=datetime.now().isoformat()
            ))
        
        return sections
    
    def _generate_architectural_integrity_sections(self, inventory: Dict[str, Any]) -> List[ReportSection]:
        """Generate architectural integrity report sections"""
        sections = []
        
        system_health = inventory.get("system_health", {})
        
        # Fractal Integrity Section
        fractal_integrity = system_health.get("fractal_integrity", {})
        if fractal_integrity:
            sections.append(ReportSection(
                title="Fractal Architecture Integrity",
                content=fractal_integrity,
                summary="Fractal architecture validation results",
                recommendations=[
                    "Maintain self-similarity above 90%",
                    "Ensure meta-circularity for system coherence",
                    "Preserve holographic nature for complete representation"
                ],
                timestamp=datetime.now().isoformat()
            ))
        
        # Architectural Coherence Section
        architectural_coherence = system_health.get("architectural_coherence", {})
        if architectural_coherence:
            sections.append(ReportSection(
                title="Architectural Coherence",
                content=architectural_coherence,
                summary="Architectural consistency and distribution analysis",
                recommendations=[
                    "Fill gaps in fractal layer distribution",
                    "Maintain balanced water state distribution",
                    "Ensure comprehensive chakra coverage"
                ],
                timestamp=datetime.now().isoformat()
            ))
        
        return sections
    
    def _generate_performance_sections(self, inventory: Dict[str, Any]) -> List[ReportSection]:
        """Generate performance report sections"""
        sections = []
        
        # Performance metrics would be collected here
        # For now, create a placeholder section
        sections.append(ReportSection(
            title="System Performance",
            content={"status": "Performance monitoring not yet implemented"},
            summary="Performance monitoring capabilities to be implemented",
            recommendations=[
                "Implement performance metrics collection",
                "Add response time monitoring",
                "Track resource utilization patterns"
            ],
            timestamp=datetime.now().isoformat()
        ))
        
        return sections
    
    def _generate_dependency_sections(self, inventory: Dict[str, Any]) -> List[ReportSection]:
        """Generate dependency report sections"""
        sections = []
        
        system_health = inventory.get("system_health", {})
        dependency_health = system_health.get("dependency_health", {})
        
        if dependency_health:
            sections.append(ReportSection(
                title="Dependency Health",
                content=dependency_health,
                summary=f"Dependency health score: {dependency_health.get('health_score', 0.0):.1f}%",
                recommendations=[
                    "Resolve circular dependencies immediately",
                    "Address missing dependencies",
                    "Implement dependency validation in CI/CD"
                ],
                timestamp=datetime.now().isoformat()
            ))
        
        return sections
    
    def _generate_all_sections(self, inventory: Dict[str, Any]) -> List[ReportSection]:
        """Generate all report sections"""
        sections = []
        sections.extend(self._generate_system_health_sections(inventory))
        sections.extend(self._generate_component_status_sections(inventory))
        sections.extend(self._generate_architectural_integrity_sections(inventory))
        sections.extend(self._generate_performance_sections(inventory))
        sections.extend(self._generate_dependency_sections(inventory))
        return sections
    
    def _identify_critical_issues(self, inventory: Dict[str, Any]) -> List[str]:
        """Identify critical issues from inventory data"""
        critical_issues = []
        
        system_health = inventory.get("system_health", {})
        
        # Check overall health
        overall_health = system_health.get("overall_health", 0.0)
        if overall_health < 70.0:
            critical_issues.append(f"Overall system health is critically low: {overall_health:.1f}%")
        
        # Check fractal integrity
        fractal_integrity = system_health.get("fractal_integrity", {})
        for aspect, data in fractal_integrity.items():
            if isinstance(data, dict) and data.get("status") == "CRITICAL":
                critical_issues.append(f"Critical {aspect} issue detected")
        
        # Check architectural coherence
        architectural_coherence = system_health.get("architectural_coherence", {})
        for aspect, data in architectural_coherence.items():
            if isinstance(data, dict) and data.get("status") == "CRITICAL":
                critical_issues.append(f"Critical {aspect} issue detected")
        
        # Check dependency health
        dependency_health = system_health.get("dependency_health", {})
        if dependency_health.get("status") == "CRITICAL":
            critical_issues.append("Critical dependency issues detected")
        
        return critical_issues
    
    def _generate_action_items(self, inventory: Dict[str, Any], critical_issues: List[str]) -> List[str]:
        """Generate actionable items based on inventory and critical issues"""
        action_items = []
        
        # Address critical issues
        for issue in critical_issues:
            if "health" in issue.lower():
                action_items.append("Investigate and resolve system health issues")
            elif "fractal" in issue.lower():
                action_items.append("Review and fix fractal architecture issues")
            elif "architectural" in issue.lower():
                action_items.append("Address architectural coherence problems")
            elif "dependency" in issue.lower():
                action_items.append("Resolve dependency conflicts and missing dependencies")
        
        # General maintenance items
        action_items.extend([
            "Schedule regular system health reviews",
            "Update component documentation",
            "Review and optimize fractal layer distribution",
            "Validate water state and chakra assignments"
        ])
        
        return action_items
    
    def export_report(self, report_id: str, format: str = "json") -> str:
        """Export a report in the specified format"""
        try:
            if report_id not in self.reports:
                return f"Report {report_id} not found"
            
            report = self.reports[report_id]
            
            if format.lower() == "json":
                return json.dumps(asdict(report), indent=2)
            elif format.lower() == "text":
                return self._format_report_as_text(report)
            else:
                return f"Unsupported format: {format}"
                
        except Exception as e:
            print(f"Error exporting report: {e}")
            return f"Error: {str(e)}"
    
    def _format_report_as_text(self, report: ComprehensiveReport) -> str:
        """Format a report as human-readable text"""
        try:
            text = []
            text.append("=" * 80)
            text.append(f"LIVING CODEX COMPREHENSIVE REPORT")
            text.append("=" * 80)
            text.append(f"Report ID: {report.report_id}")
            text.append(f"Title: {report.title}")
            text.append(f"Generated: {report.generated_at}")
            text.append(f"System Version: {report.system_version}")
            text.append(f"Overall Health Score: {report.overall_health_score:.1f}%")
            text.append("")
            
            if report.critical_issues:
                text.append("CRITICAL ISSUES:")
                text.append("-" * 40)
                for issue in report.critical_issues:
                    text.append(f"• {issue}")
                text.append("")
            
            if report.action_items:
                text.append("ACTION ITEMS:")
                text.append("-" * 40)
                for item in report.action_items:
                    text.append(f"• {item}")
                text.append("")
            
            text.append("REPORT SECTIONS:")
            text.append("-" * 40)
            for section in report.sections:
                text.append(f"\n{section.title.upper()}")
                text.append(f"Summary: {section.summary}")
                if section.recommendations:
                    text.append("Recommendations:")
                    for rec in section.recommendations:
                        text.append(f"  • {rec}")
            
            text.append("")
            text.append("=" * 80)
            
            return "\n".join(text)
            
        except Exception as e:
            print(f"Error formatting report as text: {e}")
            return f"Error formatting report: {str(e)}"
    
    def get_inventory_summary(self) -> Dict[str, Any]:
        """Get a summary of the current inventory"""
        try:
            return {
                "total_inventory_items": len(self.inventory_items),
                "total_reports": len(self.reports),
                "last_scan": max([item.updated_at for item in self.inventory_items.values()]) if self.inventory_items else None,
                "last_report": max([report.generated_at for report in self.reports.values()]) if self.reports else None,
                "inventory_types": list(set(item.item_type for item in self.inventory_items.values())),
                "report_types": list(set(report.title.split()[0] for report in self.reports.values()))
            }
        except Exception as e:
            print(f"Error getting inventory summary: {e}")
            return {"error": str(e)}


# Global instance
inventory_report_system = FractalInventoryReportComponent()


def initialize_inventory_report_system():
    """Initialize the inventory and report system"""
    try:
        # The system is already initialized when the class is instantiated
        return inventory_report_system
    except Exception as e:
        print(f"Error initializing inventory report system: {e}")
        return None


if __name__ == "__main__":
    # Test the inventory and report system
    print("Testing Living Codex Inventory and Report System...")
    
    # Initialize system
    system = initialize_inventory_report_system()
    if system:
        print("✓ Inventory and Report System initialized")
        
        # Scan system inventory
        print("\nScanning system inventory...")
        inventory = system.scan_system_inventory()
        if "error" not in inventory:
            print("✓ System inventory scanned successfully")
            print(f"  Total components: {inventory.get('system_overview', {}).get('total_components', 0)}")
            print(f"  Total nodes: {inventory.get('system_overview', {}).get('total_nodes', 0)}")
            print(f"  Overall health: {inventory.get('system_health', {}).get('overall_health', 0.0):.1f}%")
        else:
            print(f"✗ Error scanning inventory: {inventory['error']}")
        
        # Generate comprehensive report
        print("\nGenerating comprehensive report...")
        report = system.generate_comprehensive_report("system_health")
        if report:
            print("✓ Comprehensive report generated")
            print(f"  Report ID: {report.report_id}")
            print(f"  Overall health: {report.overall_health_score:.1f}%")
            print(f"  Critical issues: {len(report.critical_issues)}")
            print(f"  Action items: {len(report.action_items)}")
            
            # Export report
            print("\nExporting report as text...")
            text_report = system.export_report(report.report_id, "text")
            print("✓ Report exported successfully")
            
            # Save report to file
            report_file = f"inventory_report_{report.report_id}.txt"
            with open(report_file, "w") as f:
                f.write(text_report)
            print(f"✓ Report saved to {report_file}")
        else:
            print("✗ Error generating report")
        
        # Get inventory summary
        print("\nGetting inventory summary...")
        summary = system.get_inventory_summary()
        if "error" not in summary:
            print("✓ Inventory summary retrieved")
            print(f"  Total inventory items: {summary['total_inventory_items']}")
            print(f"  Total reports: {summary['total_reports']}")
        else:
            print(f"✗ Error getting summary: {summary['error']}")
        
        print("\n✓ Inventory and Report System test completed")
    else:
        print("✗ Failed to initialize Inventory and Report System")
