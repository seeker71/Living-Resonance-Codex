#!/usr/bin/env python3
"""
Phase 1 Validation Script for Living Codex
Validates that the repository meets all Phase 1 requirements from the specification.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any

class Phase1Validator:
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.errors = []
        self.warnings = []
        self.passed = []
        
    def validate_file_exists(self, path: str, description: str) -> bool:
        """Check if a required file exists"""
        full_path = self.root / path
        if full_path.exists():
            self.passed.append(f"✓ {description}: {path}")
            return True
        else:
            self.errors.append(f"✗ {description}: {path} - FILE MISSING")
            return False
    
    def validate_json_structure(self, path: str, required_keys: List[str], description: str) -> bool:
        """Validate JSON structure has required keys"""
        full_path = self.root / path
        if not full_path.exists():
            self.errors.append(f"✗ {description}: {path} - FILE MISSING")
            return False
            
        try:
            with open(full_path, 'r') as f:
                data = json.load(f)
            
            missing_keys = [key for key in required_keys if key not in data]
            if missing_keys:
                self.errors.append(f"✗ {description}: {path} - Missing keys: {missing_keys}")
                return False
            else:
                self.passed.append(f"✓ {description}: {path} - Structure valid")
                return True
        except json.JSONDecodeError as e:
            self.errors.append(f"✗ {description}: {path} - Invalid JSON: {e}")
            return False
        except Exception as e:
            self.errors.append(f"✗ {description}: {path} - Error reading file: {e}")
            return False
    
    def validate_seed_ontology(self) -> bool:
        """Validate the seed ontology structure"""
        required_keys = ["@context", "@graph", "axes"]
        if not self.validate_json_structure("ontology/seed.json", required_keys, "Seed Ontology"):
            return False
        
        # Check specific node properties
        try:
            with open(self.root / "ontology/seed.json", 'r') as f:
                data = json.load(f)
            
            nodes = data.get("@graph", [])
            if len(nodes) != 12:
                self.errors.append(f"✗ Seed Ontology: Expected 12 nodes, found {len(nodes)}")
                return False
            
            # Check each node has required properties
            required_node_props = ["@id", "name", "type", "waterState", "essence", "correspondences", "geometry", "harmonicRepresentation"]
            for i, node in enumerate(nodes):
                missing_props = [prop for prop in required_node_props if prop not in node]
                if missing_props:
                    self.errors.append(f"✗ Node {i+1} ({node.get('name', 'Unknown')}): Missing properties: {missing_props}")
            
            # Check axes have required properties
            axes = data.get("axes", [])
            required_axis_props = ["name", "endA", "endB", "min", "max", "default", "scaleLabels", "harmonicMetaphor", "waterMetaphor"]
            for i, axis in enumerate(axes):
                missing_props = [prop for prop in required_axis_props if prop not in axis]
                if missing_props:
                    self.errors.append(f"✗ Axis {i+1} ({axis.get('name', 'Unknown')}): Missing properties: {missing_props}")
            
            if not self.errors:
                self.passed.append(f"✓ Seed Ontology: All {len(nodes)} nodes and {len(axes)} axes properly structured")
                return True
            return False
            
        except Exception as e:
            self.errors.append(f"✗ Seed Ontology: Error validating structure: {e}")
            return False
    
    def validate_schema(self) -> bool:
        """Validate the JSON-LD schema"""
        required_keys = ["@context", "@type", "name", "description", "nodeTypes", "relationshipTypes", "waterStates", "contributionKinds"]
        return self.validate_json_structure("ontology/schema.json", required_keys, "JSON-LD Schema")
    
    def validate_prototypes(self) -> bool:
        """Validate that all required prototypes exist and are functional"""
        prototypes = [
            ("prototypes/graph/loader.py", "Graph Database Loader"),
            ("prototypes/viz/package.json", "Visualization Package"),
            ("prototypes/viz/src/main.js", "Visualization Implementation"),
            ("prototypes/resonance/score.py", "Resonance Scoring"),
            ("prototypes/federation/server.js", "Federation Server")
        ]
        
        all_valid = True
        for path, description in prototypes:
            if not self.validate_file_exists(path, description):
                all_valid = False
        
        return all_valid
    
    def validate_requirements(self) -> bool:
        """Validate Python requirements file"""
        return self.validate_file_exists("prototypes/graph/requirements.txt", "Python Requirements")
    
    def validate_documentation(self) -> bool:
        """Validate documentation files"""
        docs = [
            ("docs/living_codex_specification.md", "Living Codex Specification"),
            ("docs/living_codex.md", "Living Codex Overview"),
            ("README.md", "Repository README")
        ]
        
        all_valid = True
        for path, description in docs:
            if not self.validate_file_exists(path, description):
                all_valid = False
        
        return all_valid
    
    def run_validation(self) -> Dict[str, Any]:
        """Run all Phase 1 validations"""
        print("🔍 Phase 1 Validation for Living Codex")
        print("=" * 50)
        
        # Run all validations
        self.validate_seed_ontology()
        self.validate_schema()
        self.validate_prototypes()
        self.validate_requirements()
        self.validate_documentation()
        
        # Print results
        print("\n📋 VALIDATION RESULTS:")
        print("=" * 50)
        
        for passed in self.passed:
            print(passed)
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(warning)
        
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(error)
        
        # Summary
        total_checks = len(self.passed) + len(self.warnings) + len(self.errors)
        print(f"\n📊 SUMMARY:")
        print(f"Passed: {len(self.passed)}")
        print(f"Warnings: {len(self.warnings)}")
        print(f"Errors: {len(self.errors)}")
        print(f"Total: {total_checks}")
        
        if self.errors:
            print(f"\n❌ Phase 1 validation FAILED with {len(self.errors)} errors")
            return False
        elif self.warnings:
            print(f"\n⚠️  Phase 1 validation PASSED with {len(self.warnings)} warnings")
            return True
        else:
            print(f"\n✅ Phase 1 validation PASSED completely!")
            return True

def main():
    validator = Phase1Validator()
    success = validator.run_validation()
    
    if success:
        print("\n🎉 Your repository is ready for Phase 1!")
        print("Next steps:")
        print("1. Test the enhanced graph loader")
        print("2. Run the enhanced resonance scoring")
        print("3. Test the enhanced visualization")
        print("4. Consider Phase 2: Visual Prototype enhancements")
    else:
        print("\n🔧 Please fix the errors above before proceeding to Phase 2")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
