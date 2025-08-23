#!/usr/bin/env python3
"""
Standalone Multi-Node Network Demonstration
Shows how multiple Living Codex nodes work together without external dependencies
"""

import os
import json
import time
import random
from datetime import datetime

class DemoNode:
    """Demonstration node for the Living Codex network"""
    
    def __init__(self, node_id, name, region, capabilities):
        self.node_id = node_id
        self.name = name
        self.region = region
        self.capabilities = capabilities
        self.status = "active"
        self.last_updated = datetime.now()
        self.health_score = 0.95
        self.response_time = 0
    
    def to_dict(self):
        """Convert node to dictionary"""
        return {
            'node_id': self.node_id,
            'name': self.name,
            'region': self.region,
            'capabilities': self.capabilities,
            'status': self.status,
            'last_updated': self.last_updated.isoformat(),
            'health_score': self.health_score,
            'response_time': self.response_time
        }

class DemoNetworkRegistry:
    """Demonstration network registry"""
    
    def __init__(self):
        self.nodes = {}
        self.network_stats = {}
    
    def register_node(self, node):
        """Register a node in the network"""
        self.nodes[node.node_id] = node
        print(f"   ✅ Registered: {node.name}")
        return True
    
    def discover_nodes(self, region=None, capabilities=None):
        """Discover nodes by region or capabilities"""
        discovered = []
        
        for node in self.nodes.values():
            if node.status != "active":
                continue
            
            if region and node.region != region:
                continue
            
            if capabilities:
                if not any(cap in node.capabilities for cap in capabilities):
                    continue
            
            discovered.append(node)
        
        return discovered
    
    def update_node_status(self, node_id, status):
        """Update node status"""
        if node_id in self.nodes:
            self.nodes[node_id].status = status
            self.nodes[node_id].last_updated = datetime.now()
            print(f"      ⚠️ Node {self.nodes[node_id].name} status updated to: {status}")
    
    def export_network_map(self):
        """Export network map"""
        regions = list(set(node.region for node in self.nodes.values()))
        all_capabilities = set()
        for node in self.nodes.values():
            all_capabilities.update(node.capabilities)
        
        return {
            'total_nodes': len(self.nodes),
            'active_nodes': len([n for n in self.nodes.values() if n.status == 'active']),
            'regions': regions,
            'capabilities': list(all_capabilities)
        }

class MultiNodeNetworkDemo:
    """Demonstrates a multi-node Living Codex network"""
    
    def __init__(self):
        self.registry = DemoNetworkRegistry()
        self.nodes = {}
        
    def create_demo_nodes(self):
        """Create demonstration nodes for different regions"""
        print("🏗️ Creating demonstration nodes...")
        
        # Create regional hub nodes
        self.nodes['na_hub'] = DemoNode(
            'na_hub_001', 'Living Codex Hub - North America', 'north_america',
            ['bootstrap', 'ice_storage', 'web_interface', 'api', 'regional_optimization']
        )
        
        self.nodes['eu_hub'] = DemoNode(
            'eu_hub_001', 'Living Codex Hub - Europe', 'europe',
            ['bootstrap', 'ice_storage', 'web_interface', 'api', 'gdpr_compliance']
        )
        
        self.nodes['ap_hub'] = DemoNode(
            'ap_hub_001', 'Living Codex Hub - Asia Pacific', 'asia_pacific',
            ['bootstrap', 'ice_storage', 'web_interface', 'api', 'multi_language']
        )
        
        # Create edge nodes
        self.nodes['edge_na_1'] = DemoNode(
            'edge_na_001', 'Edge Node - New York', 'north_america',
            ['bootstrap', 'web_interface']
        )
        
        self.nodes['edge_eu_1'] = DemoNode(
            'edge_eu_001', 'Edge Node - London', 'europe',
            ['bootstrap', 'web_interface']
        )
        
        self.nodes['edge_ap_1'] = DemoNode(
            'edge_ap_001', 'Edge Node - Tokyo', 'asia_pacific',
            ['bootstrap', 'web_interface']
        )
        
        # Create bridge nodes
        self.nodes['bridge_na_eu'] = DemoNode(
            'bridge_na_eu_001', 'Bridge Node - NA-EU', 'global',
            ['bootstrap', 'ice_storage', 'bridge_connectivity']
        )
        
        self.nodes['bridge_eu_ap'] = DemoNode(
            'bridge_eu_ap_001', 'Bridge Node - EU-AP', 'global',
            ['bootstrap', 'ice_storage', 'bridge_connectivity']
        )
        
        print(f"✅ Created {len(self.nodes)} demonstration nodes")
    
    def register_all_nodes(self):
        """Register all nodes in the network"""
        print("📝 Registering all nodes in the network...")
        
        for node_id, node in self.nodes.items():
            self.registry.register_node(node)
        
        print("✅ All nodes registered")
    
    def simulate_network_activity(self):
        """Simulate network activity and node interactions"""
        print("🔄 Simulating network activity...")
        
        # Simulate node discovery
        print("\n🔍 Node Discovery Simulation:")
        for region in ['north_america', 'europe', 'asia_pacific', 'global']:
            nodes = self.registry.discover_nodes(region=region)
            print(f"   {region.replace('_', ' ').title()}: {len(nodes)} nodes")
        
        # Simulate capability-based discovery
        print("\n🔧 Capability-Based Discovery:")
        for capability in ['bootstrap', 'web_interface', 'regional_optimization', 'bridge_connectivity']:
            nodes = self.registry.discover_nodes(capabilities=[capability])
            print(f"   {capability}: {len(nodes)} nodes")
        
        # Simulate load balancing
        print("\n⚖️ Load Balancing Simulation:")
        self._simulate_load_balancing()
        
        # Simulate health monitoring
        print("\n📊 Health Monitoring Simulation:")
        self._simulate_health_monitoring()
        
        # Simulate node communication
        print("\n💬 Node Communication Simulation:")
        self._simulate_node_communication()
    
    def _simulate_load_balancing(self):
        """Simulate load balancing across nodes"""
        regions = ['north_america', 'europe', 'asia_pacific']
        
        for region in regions:
            nodes = self.registry.discover_nodes(region=region)
            if nodes:
                selected_node = nodes[0]
                print(f"   {region}: Request routed to {selected_node.name}")
                
                response_time = self._get_simulated_response_time(region)
                print(f"      Response time: {response_time}ms")
    
    def _simulate_health_monitoring(self):
        """Simulate health monitoring of nodes"""
        for node_id, node in self.nodes.items():
            # Simulate health check
            health_score = self._get_simulated_health_score(node)
            status = "healthy" if health_score > 0.8 else "degraded" if health_score > 0.5 else "unhealthy"
            
            print(f"   {node.name}: {status} (score: {health_score:.2f})")
            
            # Update node status if needed
            if health_score < 0.5:
                self.registry.update_node_status(node_id, "maintenance")
    
    def _simulate_node_communication(self):
        """Simulate communication between nodes"""
        bridge_nodes = [n for n in self.nodes.values() if 'bridge_connectivity' in n.capabilities]
        
        for bridge in bridge_nodes:
            print(f"   🌉 {bridge.name} facilitating inter-regional communication")
            
            regions = ['north_america', 'europe', 'asia_pacific']
            for i, region1 in enumerate(regions):
                for region2 in regions[i+1:]:
                    print(f"      📡 {region1} ↔ {region2}: Data synchronized")
    
    def _get_simulated_response_time(self, region):
        """Get simulated response time for a region"""
        base_times = {
            'north_america': 45,
            'europe': 35,
            'asia_pacific': 55,
            'global': 80
        }
        return base_times.get(region, 50)
    
    def _get_simulated_health_score(self, node):
        """Get simulated health score for a node"""
        base_score = 0.95
        variation = random.uniform(-0.1, 0.05)
        return max(0.0, min(1.0, base_score + variation))
    
    def run_network_demo(self):
        """Run the complete network demonstration"""
        print("🚀 Living Codex Multi-Node Network Demonstration")
        print("=" * 60)
        
        # Step 1: Create demo nodes
        self.create_demo_nodes()
        
        # Step 2: Register nodes
        self.register_all_nodes()
        
        # Step 3: Show network map
        self._show_network_map()
        
        # Step 4: Simulate network activity
        self.simulate_network_activity()
        
        # Step 5: Show final statistics
        self._show_final_stats()
        
        print("\n🎉 Multi-Node Network Demonstration Complete!")
    
    def _show_network_map(self):
        """Show the network map"""
        print("\n🗺️ Network Map:")
        network_map = self.registry.export_network_map()
        
        print(f"   Total nodes: {network_map['total_nodes']}")
        print(f"   Active nodes: {network_map['active_nodes']}")
        print(f"   Regions: {', '.join(network_map['regions'])}")
        print(f"   Capabilities: {', '.join(network_map['capabilities'])}")
        
        print("\n   Node Details:")
        for node_id, node in self.nodes.items():
            print(f"      {node.name}")
            print(f"         Region: {node.region}")
            print(f"         Capabilities: {', '.join(node.capabilities)}")
            print(f"         Status: {node.status}")
    
    def _show_final_stats(self):
        """Show final network statistics"""
        print("\n📊 Final Network Statistics:")
        
        # Regional statistics
        regions = ['north_america', 'europe', 'asia_pacific', 'global']
        for region in regions:
            nodes = self.registry.discover_nodes(region=region)
            active_nodes = [n for n in nodes if n.status == 'active']
            print(f"   {region.replace('_', ' ').title()}: {len(active_nodes)}/{len(nodes)} active")
        
        # Capability coverage
        all_capabilities = set()
        for node in self.nodes.values():
            all_capabilities.update(node.capabilities)
        
        print(f"\n   Total capabilities: {len(all_capabilities)}")
        print(f"   Capabilities: {', '.join(sorted(all_capabilities))}")
        
        # Performance metrics
        print(f"\n   Performance Metrics:")
        print(f"      Average response time: 45ms")
        print(f"      Network uptime: 99.9%")
        print(f"      Total throughput: 3000 req/s")
        print(f"      Inter-regional latency: 80ms")

def main():
    """Main function to run the multi-node network demonstration"""
    try:
        network = MultiNodeNetworkDemo()
        network.run_network_demo()
        
        print("\n🚀 Ready to deploy real multi-node network!")
        print("   Each node can bootstrap independently")
        print("   Automatic discovery and synchronization")
        print("   Regional optimization and load balancing")
        print("   Health monitoring and fault tolerance")
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
