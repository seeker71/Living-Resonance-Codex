#!/usr/bin/env python3
"""
Script to regenerate the persistence state with proper objects
"""

from living_codex_persistence import LivingCodexPersistence
from universal_knowledge_representation_system import get_universal_knowledge_representation_system
from fractal_recursion_system import get_fractal_recursion_system
from advanced_ai_integration_system import get_advanced_ai_integration_system
from self_generating_system import get_self_generating_system
from vibrational_axes_system import get_vibrational_axes_system
from resonance_governance_system import get_resonance_governance_system
from self_reflective_file_system import SelfReflectiveFileSystem

def main():
    print('=== REGENERATING PERSISTENCE STATE ===')
    
    # Initialize all systems
    p = LivingCodexPersistence()
    u = get_universal_knowledge_representation_system()
    f = get_fractal_recursion_system()
    a = get_advanced_ai_integration_system()
    s = get_self_generating_system()
    v = get_vibrational_axes_system()
    r = get_resonance_governance_system()
    
    print('=== DISCOVERING FILES ===')
    fs = SelfReflectiveFileSystem()
    discovered_files = fs.discover_all_source_files()
    print(f'Discovered {len(discovered_files)} files')
    
    print('=== CREATING FILE NODES ===')
    fs.create_file_nodes_in_living_codex(u)
    
    print('=== SAVING NEW STATE ===')
    success = p.save_system_state(u, f, a, s, v, r)
    print(f'Save success: {success}')
    
    print('=== VERIFYING NEW STATE ===')
    print(f'Universal concepts: {len(u.universal_concepts)}')
    print(f'Fractal nodes: {len(f.fractal_nodes)}')
    
    print('=== CHECKING OBJECT TYPES ===')
    if u.universal_concepts:
        sample_concept = next(iter(u.universal_concepts.values()))
        print(f'Sample concept type: {type(sample_concept)}')
        print(f'Has concept_type: {hasattr(sample_concept, "concept_type")}')
    
    if f.fractal_nodes:
        sample_node = next(iter(f.fractal_nodes.values()))
        print(f'Sample fractal node type: {type(sample_node)}')
        print(f'Has has_part: {hasattr(sample_node, "has_part")}')
    
    print('=== PERSISTENCE REGENERATION COMPLETE ===')

if __name__ == "__main__":
    main()
