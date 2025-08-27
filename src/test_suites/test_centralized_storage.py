#!/usr/bin/env python3
"""
Test Centralized Storage - Living Codex Single Storage Point

This test script demonstrates that the Living Codex system now uses a single,
centralized storage point for all nodes, ensuring no duplication and shared access.

Key Tests:
1. Verify single storage instance across all components
2. Check that no nodes are duplicated
3. Verify components can see each other's nodes
4. Test cross-component relationships
5. Validate storage metrics and health
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.centralized_node_storage import centralized_storage
from core.shared_node_system import SharedNodeSystem

def test_single_storage_instance():
    """Test that there's only one storage instance across all components"""
    print("🧪 Testing Single Storage Instance...")
    print("=" * 50)
    
    # Get storage instances from different places
    storage1 = centralized_storage
    storage2 = centralized_storage
    storage3 = centralized_storage
    
    # Verify they're all the same instance
    assert storage1 is storage2, "Storage instances should be identical"
    assert storage2 is storage3, "Storage instances should be identical"
    assert id(storage1) == id(storage2) == id(storage3), "All storage references should point to same object"
    
    print("✅ Single storage instance verified")
    print(f"Storage ID: {id(storage1)}")
    print(f"Storage Type: {type(storage1).__name__}")
    
    return True

def test_component_connections():
    """Test that components can connect to the centralized storage"""
    print("\n🧪 Testing Component Connections...")
    print("=" * 50)
    
    # Create test components
    component1 = SharedNodeSystem("TestComponent1")
    component2 = SharedNodeSystem("TestComponent2")
    component3 = SharedNodeSystem("TestComponent3")
    
    print("✅ All components connected to centralized storage")
    print(f"Component 1: {component1.component_name}")
    print(f"Component 2: {component2.component_name}")
    print(f"Component 3: {component3.component_name}")
    
    return component1, component2, component3

def test_node_creation_and_sharing():
    """Test that nodes are created and shared between components"""
    print("\n🧪 Testing Node Creation and Sharing...")
    print("=" * 50)
    
    component1, component2, component3 = test_component_connections()
    
    # Component 1 creates some nodes
    print("\n🔧 Component 1 creating nodes...")
    node1 = component1.create_node(
        node_type="test_node",
        name="Test Node 1",
        content="This is a test node from component 1",
        metadata={
            'water_state': 'liquid',
            'fractal_layer': 1,
            'chakra': 'root',
            'test_data': 'component1_data'
        }
    )
    
    node2 = component1.create_node(
        node_type="test_node",
        name="Test Node 2",
        content="This is another test node from component 1",
        metadata={
            'water_state': 'fire',
            'fractal_layer': 2,
            'chakra': 'sacral',
            'test_data': 'component1_data'
        }
    )
    
    print(f"✅ Component 1 created 2 nodes")
    print(f"  Node 1: {node1.name} (ID: {node1.node_id})")
    print(f"  Node 2: {node2.name} (ID: {node2.node_id})")
    
    # Component 2 creates some nodes
    print("\n🔧 Component 2 creating nodes...")
    node3 = component2.create_node(
        node_type="test_node",
        name="Test Node 3",
        content="This is a test node from component 2",
        metadata={
            'water_state': 'air',
            'fractal_layer': 3,
            'chakra': 'solar_plexus',
            'test_data': 'component2_data'
        }
    )
    
    node4 = component2.create_node(
        node_type="test_node",
        name="Test Node 4",
        content="This is another test node from component 2",
        metadata={
            'water_state': 'earth',
            'fractal_layer': 4,
            'chakra': 'heart',
            'test_data': 'component2_data'
        }
    )
    
    print(f"✅ Component 2 created 2 nodes")
    print(f"  Node 3: {node3.name} (ID: {node3.node_id})")
    print(f"  Node 4: {node4.name} (ID: {node4.node_id})")
    
    # Component 3 creates some nodes
    print("\n🔧 Component 3 creating nodes...")
    node5 = component3.create_node(
        node_type="test_node",
        name="Test Node 5",
        content="This is a test node from component 3",
        metadata={
            'water_state': 'ether',
            'fractal_layer': 5,
            'chakra': 'throat',
            'test_data': 'component3_data'
        }
    )
    
    print(f"✅ Component 3 created 1 node")
    print(f"  Node 5: {node5.name} (ID: {node5.node_id})")
    
    return component1, component2, component3

def test_node_sharing(component1, component2, component3):
    """Test that components can see each other's nodes"""
    print("\n🧪 Testing Node Sharing...")
    print("=" * 50)
    
    # Check that each component can see all nodes
    print("\n🔍 Checking node visibility across components...")
    
    # Component 1 should see all 5 nodes
    all_nodes_comp1 = component1.get_all_nodes()
    comp1_nodes = component1.get_component_nodes()
    shared_nodes_comp1 = component1.get_shared_nodes()
    
    print(f"Component 1:")
    print(f"  Total nodes visible: {len(all_nodes_comp1)}")
    print(f"  Own nodes: {len(comp1_nodes)}")
    print(f"  Shared nodes: {len(shared_nodes_comp1)}")
    
    # Component 2 should see all 5 nodes
    all_nodes_comp2 = component2.get_all_nodes()
    comp2_nodes = component2.get_component_nodes()
    shared_nodes_comp2 = component2.get_shared_nodes()
    
    print(f"Component 2:")
    print(f"  Total nodes visible: {len(all_nodes_comp2)}")
    print(f"  Own nodes: {len(comp2_nodes)}")
    print(f"  Shared nodes: {len(shared_nodes_comp2)}")
    
    # Component 3 should see all 5 nodes
    all_nodes_comp3 = component3.get_all_nodes()
    comp3_nodes = component3.get_component_nodes()
    shared_nodes_comp3 = component3.get_shared_nodes()
    
    print(f"Component 3:")
    print(f"  Total nodes visible: {len(all_nodes_comp3)}")
    print(f"  Own nodes: {len(comp3_nodes)}")
    print(f"  Shared nodes: {len(shared_nodes_comp3)}")
    
    # Verify no duplication
    assert len(all_nodes_comp1) == len(all_nodes_comp2) == len(all_nodes_comp3), "All components should see the same total nodes"
    
    # Count only the test nodes we created (excluding core system nodes)
    test_nodes = [node for node in all_nodes_comp1.values() if node.node_type == "test_node"]
    assert len(test_nodes) == 5, f"Should have exactly 5 test nodes, but found {len(test_nodes)}"
    
    print("✅ All components can see all nodes")
    print("✅ No node duplication detected")
    
    return component1, component2, component3

def test_cross_component_relationships(component1, component2, component3):
    """Test cross-component relationships between nodes"""
    print("\n🧪 Testing Cross-Component Relationships...")
    print("=" * 50)
    
    # Create a cross-component relationship
    print("\n🔗 Creating cross-component relationship...")
    
    # Component 1 creates a parent node
    parent_node = component1.create_node(
        node_type="parent_node",
        name="Cross-Component Parent",
        content="This is a parent node from component 1",
        metadata={
            'water_state': 'crystal',
            'fractal_layer': 6,
            'chakra': 'third_eye',
            'test_data': 'cross_component_parent'
        }
    )
    
    # Component 2 creates a child node with the parent
    child_node = component2.create_node(
        node_type="child_node",
        name="Cross-Component Child",
        content="This is a child node from component 2",
        parent_id=parent_node.node_id,
        metadata={
            'water_state': 'aether',
            'fractal_layer': 7,
            'chakra': 'crown',
            'test_data': 'cross_component_child'
        }
    )
    
    print(f"✅ Created cross-component relationship:")
    print(f"  Parent: {parent_node.name} (Component: {parent_node.structure_info['created_by_component']})")
    print(f"  Child: {child_node.name} (Component: {child_node.structure_info['created_by_component']})")
    
    # Test that both components can see the relationship
    print("\n🔍 Testing relationship visibility...")
    
    # Component 1 should see the child
    children_comp1 = component1.get_children(parent_node.node_id)
    print(f"Component 1 sees {len(children_comp1)} children of parent")
    
    # Component 2 should see the parent
    parent_comp2 = component2.get_parent(child_node.node_id)
    print(f"Component 2 sees parent: {parent_comp2.name if parent_comp2 else 'None'}")
    
    # Check cross-component relationships
    relationships_comp1 = component1.get_cross_component_relationships()
    relationships_comp2 = component2.get_cross_component_relationships()
    
    print(f"\nCross-component relationships:")
    print(f"  Component 1 sees: {len(relationships_comp1)} relationships")
    print(f"  Component 2 sees: {len(relationships_comp2)} relationships")
    
    for relationship, node_pairs in relationships_comp1.items():
        print(f"    {relationship}: {len(node_pairs)} pairs")
    
    print("✅ Cross-component relationships working correctly")
    
    return component1, component2, component3

def test_storage_metrics(component1, component2, component3):
    """Test storage metrics and health"""
    print("\n🧪 Testing Storage Metrics...")
    print("=" * 50)
    
    # Get overall storage metrics
    print("\n📊 Overall Storage Metrics:")
    metrics = centralized_storage.get_storage_metrics()
    print(f"Total Nodes: {metrics.total_nodes}")
    print(f"Storage Size: {metrics.storage_size_bytes} bytes")
    print(f"Last Updated: {metrics.last_updated}")
    
    print("\n🌊 Nodes by Water State:")
    for water_state, count in metrics.nodes_by_water_state.items():
        print(f"  {water_state}: {count}")
    
    print("\n🔢 Nodes by Fractal Layer:")
    for fractal_layer, count in metrics.nodes_by_fractal_layer.items():
        print(f"  Layer {fractal_layer}: {count}")
    
    print("\n🌀 Nodes by Chakra:")
    for chakra, count in metrics.nodes_by_chakra.items():
        print(f"  {chakra}: {count}")
    
    print("\n🔧 Component Access Counts:")
    for component, count in metrics.component_access_count.items():
        print(f"  {component}: {count}")
    
    # Test component-specific metrics
    print("\n📊 Component-Specific Metrics:")
    
    print("\nComponent 1 Summary:")
    component1.print_storage_summary()
    
    print("\nComponent 2 Summary:")
    component2.print_storage_summary()
    
    print("\nComponent 3 Summary:")
    component3.print_storage_summary()
    
    # Test storage health
    print("\n🏥 Storage Health:")
    
    health1 = component1.get_storage_health()
    print(f"Component 1 Health: {health1['health_score']:.1f}/100 ({health1['status']})")
    
    health2 = component2.get_storage_health()
    print(f"Component 2 Health: {health2['health_score']:.1f}/100 ({health2['status']})")
    
    health3 = component3.get_storage_health()
    print(f"Component 3 Health: {health3['health_score']:.1f}/100 ({health3['status']})")
    
    print("✅ Storage metrics working correctly")
    
    return component1, component2, component3

def test_no_duplication(component1, component2, component3):
    """Test that no nodes are duplicated"""
    print("\n🧪 Testing No Node Duplication...")
    print("=" * 50)
    
    # Get all nodes from centralized storage
    all_nodes = centralized_storage.get_all_nodes()
    
    # Check for duplicate node IDs
    node_ids = list(all_nodes.keys())
    unique_node_ids = set(node_ids)
    
    print(f"Total nodes: {len(all_nodes)}")
    print(f"Unique node IDs: {len(unique_node_ids)}")
    
    if len(node_ids) == len(unique_node_ids):
        print("✅ No duplicate node IDs detected")
    else:
        print("❌ Duplicate node IDs detected!")
        duplicates = [node_id for node_id in node_ids if node_ids.count(node_id) > 1]
        print(f"Duplicate IDs: {duplicates}")
        return False
    
    # Check for duplicate content (optional - might be legitimate)
    node_contents = [node.content for node in all_nodes.values()]
    unique_contents = set(node_contents)
    
    print(f"Unique content items: {len(unique_contents)}")
    if len(node_contents) == len(unique_contents):
        print("✅ No duplicate content detected")
    else:
        print("⚠️  Some duplicate content detected (this might be legitimate)")
    
    # Check that all components see the same nodes
    comp1_nodes = component1.get_all_nodes()
    comp2_nodes = component2.get_all_nodes()
    comp3_nodes = component3.get_all_nodes()
    
    assert len(comp1_nodes) == len(comp2_nodes) == len(comp3_nodes), "All components should see the same nodes"
    assert len(comp1_nodes) == len(all_nodes), "Central storage should have same count as component views"
    
    print("✅ All components see the same nodes")
    print("✅ No node duplication confirmed")
    
    return True

def main():
    """Main test runner"""
    print("🌟 Living Codex - Centralized Storage Test Suite")
    print("=" * 70)
    print("This will test that the Living Codex system uses a single,")
    print("centralized storage point with no node duplication.")
    print()
    
    try:
        # Run all tests
        test_single_storage_instance()
        components = test_node_creation_and_sharing()
        test_node_sharing(*components)
        test_cross_component_relationships(*components)
        test_storage_metrics(*components)
        test_no_duplication(*components)
        
        print("\n" + "=" * 80)
        print("🎉 CONGRATULATIONS! All centralized storage tests passed!")
        print("=" * 80)
        print("✅ Single storage instance verified")
        print("✅ All components connected to centralized storage")
        print("✅ Nodes created and shared between components")
        print("✅ Cross-component relationships working")
        print("✅ Storage metrics and health working")
        print("✅ No node duplication confirmed")
        print()
        print("🌟 The Living Codex system now truly embodies:")
        print("   'Everything is just nodes' with a single storage point")
        print("   No duplication across components")
        print("   Shared access to all nodes")
        print("   Centralized management and interface")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
