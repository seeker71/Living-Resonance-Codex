#!/usr/bin/env python3
"""
Ontological Validation System
============================

This implements the ontological validation system that ensures consistency
across all Living Codex mappings and validates ontological integrity.

This is part of Phase 2 of the metadata enhancement plan.
"""

from typing import Dict, List, Any, Optional, Set, Tuple, Union
from datetime import datetime
import json
from dataclasses import dataclass

from living_codex_ontology import (
    WaterStateKey, ChakraKey, FrequencyKey, FractalLayer,
    ConsciousnessLevel, QuantumState, ResonancePattern, ProgrammingOntologyLayer,
    EpistemicLabel, canonical_registry, validate_canonical_key
)

from enhanced_generic_node import EnhancedGenericNode

@dataclass
class ValidationResult:
    """Result of an ontological validation check"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    validation_timestamp: str
    validation_type: str
    details: Dict[str, Any]

@dataclass
class ConsistencyCheck:
    """Result of a consistency check between mappings"""
    mapping_a: str
    mapping_b: str
    relationship: str
    is_consistent: bool
    explanation: str
    severity: str  # "error", "warning", "info"

class OntologicalValidationSystem:
    """
    Ontological Validation System for ensuring consistency across all Living Codex mappings
    
    This system provides:
    - Canonical key validation
    - Mapping consistency validation
    - Epistemic label validation
    - Fractal structure validation
    - Resonance pattern validation
    - Cross-dimensional relationship validation
    """
    
    def __init__(self):
        """Initialize the ontological validation system"""
        self.registry = canonical_registry
        self.validation_history: List[ValidationResult] = []
        
        # Validation rules and constraints
        self._validation_rules = self._initialize_validation_rules()
        
        # Known valid combinations
        self._valid_combinations = self._initialize_valid_combinations()
        
        print("🔍 Ontological Validation System initialized")
        print("✨ Consistency checking enabled")
        print("✨ Cross-dimensional validation active")
    
    # ============================================================================
    # VALIDATION RULES INITIALIZATION
    # ============================================================================
    
    def _initialize_validation_rules(self) -> Dict[str, Any]:
        """Initialize validation rules and constraints"""
        return {
            'canonical_keys': {
                'water_states': [ws.value for ws in WaterStateKey],
                'chakras': [ch.value for ch in ChakraKey],
                'frequencies': [freq.value for freq in FrequencyKey],
                'fractal_layers': [layer.value for layer in FractalLayer],
                'consciousness_levels': [level.value for level in ConsciousnessLevel],
                'quantum_states': [state.value for state in QuantumState],
                'resonance_patterns': [pattern.value for pattern in ResonancePattern],
                'programming_ontology_layers': [layer.value for layer in ProgrammingOntologyLayer],
                'epistemic_labels': [label.value for label in EpistemicLabel],
            },
            'epistemic_constraints': {
                'physics_engineering_only': ['water_state', 'fractal_layer', 'consciousness_level'],
                'tradition_speculative_ok': ['chakra', 'frequency', 'resonance_pattern'],
                'mixed_allowed': ['quantum_state', 'programming_ontology_layer']
            },
            'fractal_constraints': {
                'max_depth': 16,
                'valid_parent_child_relationships': True,
                'cross_scale_mapping_required': True
            },
            'resonance_constraints': {
                'coherence_score_range': (0.0, 1.0),
                'dissonance_level_range': (0.0, 1.0),
                'vibrational_axes_max': 4
            }
        }
    
    def _initialize_valid_combinations(self) -> Dict[str, List[Dict[str, str]]]:
        """Initialize known valid combinations of ontological mappings"""
        return {
            'ice_theme': [
                {
                    'water_state': 'ws.ice',
                    'chakra': 'ch.crown',
                    'frequency': 'freq.963',
                    'fractal_layer': 0,
                    'consciousness_level': 'awake',
                    'quantum_state': 'coherent',
                    'resonance_pattern': 'harmonic',
                    'epistemic_label': 'engineering'
                }
            ],
            'liquid_theme': [
                {
                    'water_state': 'ws.liquid',
                    'chakra': 'ch.heart',
                    'frequency': 'freq.639',
                    'fractal_layer': 4,
                    'consciousness_level': 'awake',
                    'quantum_state': 'coherent',
                    'resonance_pattern': 'neutral',
                    'epistemic_label': 'engineering'
                }
            ],
            'vapor_theme': [
                {
                    'water_state': 'ws.vapor',
                    'chakra': 'ch.third_eye',
                    'frequency': 'freq.852',
                    'fractal_layer': 2,
                    'consciousness_level': 'sentient',
                    'quantum_state': 'superposition',
                    'resonance_pattern': 'sympathetic',
                    'epistemic_label': 'engineering'
                }
            ],
            'plasma_theme': [
                {
                    'water_state': 'ws.plasma',
                    'chakra': 'ch.root',
                    'frequency': 'freq.396',
                    'fractal_layer': 5,
                    'consciousness_level': 'awake',
                    'quantum_state': 'entangled',
                    'resonance_pattern': 'sympathetic',
                    'epistemic_label': 'engineering'
                }
            ]
        }
    
    # ============================================================================
    # CORE VALIDATION METHODS
    # ============================================================================
    
    def validate_canonical_keys(self, metadata: Dict[str, Any]) -> ValidationResult:
        """
        Validate that all canonical keys in metadata are valid
        
        Args:
            metadata: Metadata dictionary to validate
        
        Returns:
            ValidationResult with validation details
        """
        errors = []
        warnings = []
        details = {}
        
        # Check each canonical key field
        key_fields = {
            'water_state': 'water_states',
            'chakra': 'chakras',
            'frequency': 'frequencies',
            'fractal_layer': 'fractal_layers',
            'consciousness_level': 'consciousness_levels',
            'quantum_state': 'quantum_states',
            'resonance_pattern': 'resonance_patterns',
            'programming_ontology_layer': 'programming_layers',
            'epistemic_label': 'epistemic_labels'
        }
        
        for field, key_type in key_fields.items():
            if field in metadata:
                value = metadata[field]
                if not validate_canonical_key(value, key_type):
                    errors.append(f"Invalid {field}: '{value}' is not a valid {key_type} canonical key")
                else:
                    details[f"{field}_valid"] = True
        
        is_valid = len(errors) == 0
        
        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="canonical_key_validation",
            details=details
        )
        
        self.validation_history.append(result)
        return result
    
    def validate_epistemic_consistency(self, metadata: Dict[str, Any]) -> ValidationResult:
        """
        Validate epistemic consistency of ontological mappings
        
        Args:
            metadata: Metadata dictionary to validate
        
        Returns:
            ValidationResult with validation details
        """
        errors = []
        warnings = []
        details = {}
        
        # Check epistemic label consistency
        if 'epistemic_label' in metadata:
            epistemic_label = metadata['epistemic_label']
            
            # Check physics/engineering constraints
            if epistemic_label in ['physics', 'engineering']:
                for field in self._validation_rules['epistemic_constraints']['physics_engineering_only']:
                    if field in metadata:
                        # These fields should have physics/engineering grounding
                        details[f"{field}_epistemic_check"] = "passed"
            
            # Check tradition/speculative constraints
            elif epistemic_label in ['tradition', 'speculative']:
                for field in self._validation_rules['epistemic_constraints']['tradition_speculative_ok']:
                    if field in metadata:
                        # These fields are appropriate for tradition/speculative
                        details[f"{field}_epistemic_check"] = "passed"
                
                # Warn about mixing with physics/engineering
                for field in self._validation_rules['epistemic_constraints']['physics_engineering_only']:
                    if field in metadata:
                        warnings.append(f"Field '{field}' with epistemic label '{epistemic_label}' may need physics/engineering grounding")
        
        # Check for epistemic mixing issues
        if 'water_state' in metadata and 'epistemic_label' in metadata:
            water_state = metadata['water_state']
            epistemic_label = metadata['epistemic_label']
            
            # Water states are traditionally grounded
            if epistemic_label == 'physics' and water_state.startswith('ws.'):
                warnings.append("Water states are traditionally grounded; consider epistemic label 'tradition'")
        
        is_valid = len(errors) == 0
        
        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="epistemic_consistency_validation",
            details=details
        )
        
        self.validation_history.append(result)
        return result
    
    def validate_fractal_structure(self, metadata: Dict[str, Any]) -> ValidationResult:
        """
        Validate fractal structure consistency
        
        Args:
            metadata: Metadata dictionary to validate
        
        Returns:
            ValidationResult with validation details
        """
        errors = []
        warnings = []
        details = {}
        
        # Check fractal layer constraints
        if 'fractal_layer' in metadata:
            fractal_layer = metadata['fractal_layer']
            
            if not isinstance(fractal_layer, int):
                errors.append("Fractal layer must be an integer")
            elif fractal_layer < 0 or fractal_layer > self._validation_rules['fractal_constraints']['max_depth']:
                errors.append(f"Fractal layer {fractal_layer} is outside valid range [0, {self._validation_rules['fractal_constraints']['max_depth']}]")
            else:
                details['fractal_layer_valid'] = True
        
        # Check fractal depth constraints
        if 'fractal_depth' in metadata:
            fractal_depth = metadata['fractal_depth']
            
            if not isinstance(fractal_depth, int):
                errors.append("Fractal depth must be an integer")
            elif fractal_depth < 0:
                errors.append("Fractal depth cannot be negative")
            else:
                details['fractal_depth_valid'] = True
        
        # Check cross-scale mapping
        if 'cross_scale_mapping' in metadata:
            cross_scale = metadata['cross_scale_mapping']
            
            if not isinstance(cross_scale, dict):
                errors.append("Cross-scale mapping must be a dictionary")
            else:
                required_scales = ['micro', 'meso', 'macro', 'meta']
                for scale in required_scales:
                    if scale not in cross_scale:
                        warnings.append(f"Missing cross-scale mapping for '{scale}'")
                    else:
                        details[f'cross_scale_{scale}_valid'] = True
        
        is_valid = len(errors) == 0
        
        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="fractal_structure_validation",
            details=details
        )
        
        self.validation_history.append(result)
        return result
    
    def validate_resonance_patterns(self, metadata: Dict[str, Any]) -> ValidationResult:
        """
        Validate resonance pattern consistency
        
        Args:
            metadata: Metadata dictionary to validate
        
        Returns:
            ValidationResult with validation details
        """
        errors = []
        warnings = []
        details = {}
        
        # Check resonance pattern
        if 'resonance_pattern' in metadata:
            resonance_pattern = metadata['resonance_pattern']
            
            if resonance_pattern not in self._validation_rules['canonical_keys']['resonance_patterns']:
                errors.append(f"Invalid resonance pattern: {resonance_pattern}")
            else:
                details['resonance_pattern_valid'] = True
        
        # Check coherence score
        if 'coherence_score' in metadata:
            coherence_score = metadata['coherence_score']
            
            if not isinstance(coherence_score, (int, float)):
                errors.append("Coherence score must be a number")
            else:
                min_score, max_score = self._validation_rules['resonance_constraints']['coherence_score_range']
                if coherence_score < min_score or coherence_score > max_score:
                    errors.append(f"Coherence score {coherence_score} is outside valid range [{min_score}, {max_score}]")
                else:
                    details['coherence_score_valid'] = True
        
        # Check dissonance level
        if 'dissonance_level' in metadata:
            dissonance_level = metadata['dissonance_level']
            
            if not isinstance(dissonance_level, (int, float)):
                errors.append("Dissonance level must be a number")
            else:
                min_level, max_level = self._validation_rules['resonance_constraints']['dissonance_level_range']
                if dissonance_level < min_level or dissonance_level > max_level:
                    errors.append(f"Dissonance level {dissonance_level} is outside valid range [{min_level}, {max_level}]")
                else:
                    details['dissonance_level_valid'] = True
        
        # Check vibrational axes
        if 'vibrational_axes' in metadata:
            vibrational_axes = metadata['vibrational_axes']
            
            if not isinstance(vibrational_axes, list):
                errors.append("Vibrational axes must be a list")
            else:
                max_axes = self._validation_rules['resonance_constraints']['vibrational_axes_max']
                if len(vibrational_axes) > max_axes:
                    warnings.append(f"Number of vibrational axes ({len(vibrational_axes)}) exceeds recommended maximum ({max_axes})")
                
                details['vibrational_axes_count'] = len(vibrational_axes)
        
        is_valid = len(errors) == 0
        
        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="resonance_pattern_validation",
            details=details
        )
        
        self.validation_history.append(result)
        return result
    
    # ============================================================================
    # CROSS-DIMENSIONAL VALIDATION
    # ============================================================================
    
    def validate_ontological_signature(self, metadata: Dict[str, Any]) -> ValidationResult:
        """
        Validate complete ontological signature for consistency
        
        Args:
            metadata: Complete metadata dictionary to validate
        
        Returns:
            ValidationResult with validation details
        """
        # Run all individual validations
        canonical_result = self.validate_canonical_keys(metadata)
        epistemic_result = self.validate_epistemic_consistency(metadata)
        fractal_result = self.validate_fractal_structure(metadata)
        resonance_result = self.validate_resonance_patterns(metadata)
        
        # Combine results
        all_errors = []
        all_warnings = []
        all_details = {}
        
        all_errors.extend(canonical_result.errors)
        all_errors.extend(epistemic_result.errors)
        all_errors.extend(fractal_result.errors)
        all_errors.extend(resonance_result.errors)
        
        all_warnings.extend(canonical_result.warnings)
        all_warnings.extend(epistemic_result.warnings)
        all_warnings.extend(fractal_result.warnings)
        all_warnings.extend(resonance_result.warnings)
        
        all_details.update(canonical_result.details)
        all_details.update(epistemic_result.details)
        all_details.update(fractal_result.details)
        all_details.update(resonance_result.details)
        
        # Check for cross-dimensional consistency
        cross_dimensional_result = self._validate_cross_dimensional_consistency(metadata)
        all_errors.extend(cross_dimensional_result.errors)
        all_warnings.extend(cross_dimensional_result.warnings)
        all_details.update(cross_dimensional_result.details)
        
        is_valid = len(all_errors) == 0
        
        result = ValidationResult(
            is_valid=is_valid,
            errors=all_errors,
            warnings=all_warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="ontological_signature_validation",
            details=all_details
        )
        
        self.validation_history.append(result)
        return result
    
    def _validate_cross_dimensional_consistency(self, metadata: Dict[str, Any]) -> ValidationResult:
        """
        Validate consistency between different ontological dimensions
        
        Args:
            metadata: Metadata dictionary to validate
        
        Returns:
            ValidationResult with validation details
        """
        errors = []
        warnings = []
        details = {}
        
        # Check water state and chakra consistency
        if 'water_state' in metadata and 'chakra' in metadata:
            water_state = metadata['water_state']
            chakra = metadata['chakra']
            
            # Get expected chakra for water state (with error handling)
            try:
                water_mapping = self.registry.get_water_state_mapping(WaterStateKey(water_state))
                expected_chakra = water_mapping.get('chakra')
                
                if expected_chakra and chakra != expected_chakra.value:
                    warnings.append(f"Water state '{water_state}' typically maps to chakra '{expected_chakra.value}', not '{chakra}'")
                else:
                    details['water_chakra_consistency'] = True
            except ValueError:
                # Invalid water state - skip this consistency check
                pass
        
        # Check chakra and frequency consistency
        if 'chakra' in metadata and 'frequency' in metadata:
            chakra = metadata['chakra']
            frequency = metadata['frequency']
            
            # Get expected frequency for chakra (with error handling)
            try:
                chakra_mapping = self.registry.get_chakra_mapping(ChakraKey(chakra))
                expected_frequency = chakra_mapping.get('frequency')
                
                if expected_frequency and frequency != expected_frequency.value:
                    warnings.append(f"Chakra '{chakra}' typically maps to frequency '{expected_frequency.value}', not '{frequency}'")
                else:
                    details['chakra_frequency_consistency'] = True
            except ValueError:
                # Invalid chakra - skip this consistency check
                pass
        
        # Check fractal layer and consciousness level consistency
        if 'fractal_layer' in metadata and 'consciousness_level' in metadata:
            fractal_layer = metadata['fractal_layer']
            consciousness_level = metadata['consciousness_level']
            
            # Higher fractal layers should have higher consciousness levels
            if fractal_layer >= 10 and consciousness_level in ['awake', 'sentient']:
                warnings.append(f"High fractal layer {fractal_layer} with low consciousness level '{consciousness_level}' may indicate inconsistency")
            elif fractal_layer <= 2 and consciousness_level in ['meta_cognitive', 'transcendent']:
                warnings.append(f"Low fractal layer {fractal_layer} with high consciousness level '{consciousness_level}' may indicate inconsistency")
            else:
                details['fractal_consciousness_consistency'] = True
        
        # Check quantum state and resonance pattern consistency
        if 'quantum_state' in metadata and 'resonance_pattern' in metadata:
            quantum_state = metadata['quantum_state']
            resonance_pattern = metadata['resonance_pattern']
            
            # Entangled quantum states should have sympathetic/harmonic resonance
            if quantum_state == 'entangled' and resonance_pattern in ['dissonant', 'destructive']:
                warnings.append("Entangled quantum state with dissonant/destructive resonance may indicate inconsistency")
            elif quantum_state == 'decoherent' and resonance_pattern == 'harmonic':
                warnings.append("Decoherent quantum state with harmonic resonance may indicate inconsistency")
            else:
                details['quantum_resonance_consistency'] = True
        
        result = ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="cross_dimensional_consistency_validation",
            details=details
        )
        
        return result
    
    # ============================================================================
    # TEMPLATE VALIDATION
    # ============================================================================
    
    def validate_against_template(self, 
                                 metadata: Dict[str, Any],
                                 template_name: str) -> ValidationResult:
        """
        Validate metadata against a known template
        
        Args:
            metadata: Metadata to validate
            template_name: Name of the template to validate against
        
        Returns:
            ValidationResult with validation details
        """
        errors = []
        warnings = []
        details = {}
        
        if template_name not in self._valid_combinations:
            errors.append(f"Unknown template: {template_name}")
            return ValidationResult(
                is_valid=False,
                errors=errors,
                warnings=warnings,
                validation_timestamp=datetime.now().isoformat(),
                validation_type="template_validation",
                details=details
            )
        
        # Get template
        template = self._valid_combinations[template_name][0]
        
        # Check each field against template
        for field, expected_value in template.items():
            if field in metadata:
                actual_value = metadata[field]
                if actual_value != expected_value:
                    warnings.append(f"Field '{field}' value '{actual_value}' differs from template '{expected_value}'")
                else:
                    details[f"{field}_template_match"] = True
            else:
                warnings.append(f"Missing template field: {field}")
        
        # Check for extra fields not in template
        for field in metadata:
            if field not in template:
                warnings.append(f"Extra field not in template: {field}")
        
        is_valid = len(errors) == 0
        
        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            validation_timestamp=datetime.now().isoformat(),
            validation_type="template_validation",
            details=details
        )
        
        self.validation_history.append(result)
        return result
    
    # ============================================================================
    # BULK VALIDATION
    # ============================================================================
    
    def validate_node_batch(self, nodes: List[EnhancedGenericNode]) -> List[ValidationResult]:
        """
        Validate a batch of nodes
        
        Args:
            nodes: List of EnhancedGenericNode instances to validate
        
        Returns:
            List of ValidationResult for each node
        """
        results = []
        
        for node in nodes:
            # Convert node to metadata dictionary
            metadata = {
                'water_state': node.water_state,
                'chakra': node.chakra,
                'frequency': node.frequency,
                'fractal_layer': node.fractal_layer,
                'consciousness_level': node.consciousness_level,
                'quantum_state': node.quantum_state,
                'resonance_pattern': node.resonance_pattern,
                'programming_ontology_layer': node.programming_ontology_layer,
                'epistemic_label': node.epistemic_label,
                'fractal_depth': node.fractal_depth,
                'cross_scale_mapping': node.cross_scale_mapping,
                'coherence_score': node.coherence_score,
                'dissonance_level': node.dissonance_level,
                'vibrational_axes': node.vibrational_axes
            }
            
            # Validate the node
            result = self.validate_ontological_signature(metadata)
            results.append(result)
        
        return results
    
    def get_batch_validation_summary(self, results: List[ValidationResult]) -> Dict[str, Any]:
        """
        Get a summary of batch validation results
        
        Args:
            results: List of ValidationResult instances
        
        Returns:
            Summary dictionary
        """
        total_nodes = len(results)
        valid_nodes = sum(1 for r in results if r.is_valid)
        invalid_nodes = total_nodes - valid_nodes
        
        total_errors = sum(len(r.errors) for r in results)
        total_warnings = sum(len(r.warnings) for r in results)
        
        # Group errors by type
        error_types = {}
        for result in results:
            for error in result.errors:
                error_type = error.split(':')[0] if ':' in error else 'general'
                error_types[error_type] = error_types.get(error_type, 0) + 1
        
        return {
            'total_nodes': total_nodes,
            'valid_nodes': valid_nodes,
            'invalid_nodes': invalid_nodes,
            'validation_rate': round((valid_nodes / total_nodes) * 100, 2) if total_nodes > 0 else 0,
            'total_errors': total_errors,
            'total_warnings': total_warnings,
            'error_types': error_types,
            'validation_timestamp': datetime.now().isoformat()
        }
    
    # ============================================================================
    # VALIDATION HISTORY AND REPORTING
    # ============================================================================
    
    def get_validation_history(self, 
                              validation_type: Optional[str] = None,
                              limit: Optional[int] = None) -> List[ValidationResult]:
        """
        Get validation history with optional filtering
        
        Args:
            validation_type: Optional filter by validation type
            limit: Optional limit on number of results
        
        Returns:
            List of ValidationResult instances
        """
        if validation_type:
            filtered_results = [r for r in self.validation_history if r.validation_type == validation_type]
        else:
            filtered_results = self.validation_history
        
        if limit:
            filtered_results = filtered_results[-limit:]
        
        return filtered_results
    
    def get_validation_statistics(self) -> Dict[str, Any]:
        """Get comprehensive validation statistics"""
        if not self.validation_history:
            return {
                'total_validations': 0,
                'success_rate': 0.0,
                'validation_types': {},
                'error_summary': {},
                'warning_summary': {}
            }
        
        total_validations = len(self.validation_history)
        successful_validations = sum(1 for r in self.validation_history if r.is_valid)
        success_rate = (successful_validations / total_validations) * 100
        
        # Count by validation type
        validation_types = {}
        for result in self.validation_history:
            val_type = result.validation_type
            validation_types[val_type] = validation_types.get(val_type, 0) + 1
        
        # Count errors and warnings
        error_summary = {}
        warning_summary = {}
        
        for result in self.validation_history:
            for error in result.errors:
                error_type = error.split(':')[0] if ':' in error else 'general'
                error_summary[error_type] = error_summary.get(error_type, 0) + 1
            
            for warning in result.warnings:
                warning_type = warning.split(':')[0] if ':' in warning else 'general'
                warning_summary[warning_type] = warning_summary.get(warning_type, 0) + 1
        
        return {
            'total_validations': total_validations,
            'successful_validations': successful_validations,
            'failed_validations': total_validations - successful_validations,
            'success_rate': round(success_rate, 2),
            'validation_types': validation_types,
            'error_summary': error_summary,
            'warning_summary': warning_summary,
            'last_validation': self.validation_history[-1].validation_timestamp if self.validation_history else None
        }
    
    def export_validation_report(self, 
                                output_format: str = "json") -> Union[str, Dict[str, Any]]:
        """
        Export comprehensive validation report
        
        Args:
            output_format: "json" or "dict"
        
        Returns:
            Validation report in requested format
        """
        report = {
            'validation_system_info': {
                'name': 'Ontological Validation System',
                'version': '1.0.0',
                'description': 'Living Codex Ontological Validation System',
                'generated_at': datetime.now().isoformat()
            },
            'validation_rules': self._validation_rules,
            'valid_combinations': self._valid_combinations,
            'validation_statistics': self.get_validation_statistics(),
            'recent_validations': self.get_validation_history(limit=10)
        }
        
        if output_format.lower() == "json":
            return json.dumps(report, indent=2, default=str)
        else:
            return report
    
    # ============================================================================
    # UTILITY METHODS
    # ============================================================================
    
    def clear_validation_history(self):
        """Clear validation history (useful for testing)"""
        self.validation_history.clear()
        print("🔍 Validation history cleared")
    
    def add_custom_validation_rule(self, 
                                  rule_name: str,
                                  rule_definition: Dict[str, Any]):
        """
        Add a custom validation rule
        
        Args:
            rule_name: Name of the custom rule
            rule_definition: Rule definition dictionary
        """
        if rule_name not in self._validation_rules:
            self._validation_rules[rule_name] = {}
        
        self._validation_rules[rule_name].update(rule_definition)
        print(f"🔍 Custom validation rule '{rule_name}' added")

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

# Global ontological validation system instance
ontological_validation_system = OntologicalValidationSystem()

if __name__ == "__main__":
    # Test the ontological validation system
    print("🔍 Ontological Validation System Test")
    
    # Test basic functionality
    print(f"Validation rules: {len(ontological_validation_system._validation_rules)}")
    print(f"Valid combinations: {len(ontological_validation_system._valid_combinations)}")
    
    # Test validation
    test_metadata = {
        'water_state': 'ws.ice',
        'chakra': 'ch.crown',
        'frequency': 'freq.963',
        'fractal_layer': 0,
        'consciousness_level': 'awake',
        'quantum_state': 'coherent',
        'resonance_pattern': 'harmonic',
        'epistemic_label': 'engineering'
    }
    
    result = ontological_validation_system.validate_ontological_signature(test_metadata)
    print(f"Test validation result: {result.is_valid}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    
    print("\n✅ Ontological Validation System ready for use!")
