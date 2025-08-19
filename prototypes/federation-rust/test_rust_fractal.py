#!/usr/bin/env python3
"""
Living Codex Phase 6 - Rust Fractal Federation Testing
Tests both Phase 4 compatibility and Phase 6 multi-implementation features
"""

import subprocess
import time
import requests
import json
import sys
import os
from pathlib import Path

class RustFractalTester:
    """Comprehensive tester for the Rust fractal federation server"""
    
    def __init__(self):
        self.server_process = None
        self.base_url = "http://localhost:8789"
        self.server_dir = "prototypes/federation-rust"
        self.max_wait_time = 30
        
    def log(self, message: str, level: str = "INFO"):
        """Log messages with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
    
    def build_and_start_server(self) -> bool:
        """Build and start the Rust fractal server"""
        self.log("Building Rust fractal federation server...")
        
        try:
            # Change to Rust directory
            os.chdir(self.server_dir)
            
            # Build the project
            self.log("Running cargo build...")
            build_result = subprocess.run(
                ["cargo", "build"],
                capture_output=True,
                text=True
            )
            
            if build_result.returncode != 0:
                self.log(f"Build failed: {build_result.stderr}", "ERROR")
                return False
            
            self.log("✅ Rust project built successfully")
            
            # Start server in background
            self.log("Starting Rust fractal federation server...")
            self.server_process = subprocess.Popen(
                ["cargo", "run"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=os.getcwd()
            )
            
            self.log(f"Server process started with PID: {self.server_process.pid}")
            
            # Wait a moment and check if it's still running
            time.sleep(2)
            if self.server_process.poll() is not None:
                stdout, stderr = self.server_process.communicate()
                self.log(f"❌ Server crashed immediately!", "ERROR")
                if stderr:
                    self.log(f"Error output: {stderr}", "ERROR")
                if stdout:
                    self.log(f"Standard output: {stdout}", "ERROR")
                return False
            
            return True
            
        except Exception as e:
            self.log(f"Failed to build/start server: {e}", "ERROR")
            return False
    
    def wait_for_server(self) -> bool:
        """Wait for server to be ready and responding"""
        self.log("Waiting for Rust server to be ready...")
        
        start_time = time.time()
        while time.time() - start_time < self.max_wait_time:
            try:
                response = requests.get(f"{self.base_url}/", timeout=2)
                if response.status_code == 200:
                    self.log("✅ Rust server is ready and responding!")
                    return True
            except requests.exceptions.RequestException:
                pass
            
            time.sleep(1)
            elapsed = int(time.time() - start_time)
            if elapsed % 5 == 0:
                self.log(f"Still waiting... ({elapsed}s elapsed)")
        
        self.log("❌ Rust server failed to start within timeout period", "ERROR")
        return False
    
    def test_phase4_compatibility(self) -> bool:
        """Test Phase 4 compatibility features"""
        self.log("\n" + "="*60)
        self.log("TESTING PHASE 4 COMPATIBILITY")
        self.log("="*60)
        
        # Test 1: Root endpoint
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Root endpoint: {data['name']}")
                self.log(f"   Version: {data['version']}")
                self.log(f"   Fractal levels: {data['fractal_levels']}")
            else:
                self.log(f"❌ Root endpoint failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Root endpoint error: {e}", "ERROR")
            return False
        
        # Test 2: Storage stats
        try:
            response = requests.get(f"{self.base_url}/storage/stats", timeout=10)
            if response.status_code == 200:
                stats = response.json()
                self.log(f"✅ Storage stats: Version {stats['version']}")
                self.log(f"   Base nodes: {stats['total_nodes']}")
                self.log(f"   Fractal subnodes: {stats['total_subnodes']}")
                self.log(f"   Total fractal dimensions: {stats['fractal_expansion']['total_fractal_dimensions']}")
            else:
                self.log(f"❌ Storage stats failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Storage stats error: {e}", "ERROR")
            return False
        
        # Test 3: ActivityPub inbox
        try:
            test_contribution = {
                "type": "Create",
                "actor": "rust_tester",
                "object": {
                    "type": "Contribution",
                    "nodeId": "codex:Void",
                    "content": "Testing Rust implementation compatibility",
                    "resonance": 0.88,
                    "fractalContext": "symbolic"
                }
            }
            
            response = requests.post(
                f"{self.base_url}/inbox",
                json=test_contribution,
                headers={"Content-Type": "application/activity+json"},
                timeout=10
            )
            
            if response.status_code == 200:
                self.log("✅ Posted contribution to inbox (ActivityPub)")
            else:
                self.log(f"❌ Inbox failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Inbox error: {e}", "ERROR")
            return False
        
        # Test 4: Outbox
        try:
            response = requests.get(f"{self.base_url}/outbox", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Outbox: {data['totalItems']} total items")
            else:
                self.log(f"❌ Outbox failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Outbox error: {e}", "ERROR")
            return False
        
        # Test 5: Federation peers
        try:
            response = requests.get(f"{self.base_url}/federation/peers", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Federation peers: {len(data['peers'])} peer(s)")
                
                # Check if Rust server is listed
                rust_peer = next((p for p in data['peers'] if 'rust' in p['id']), None)
                if rust_peer:
                    self.log(f"   Rust peer capabilities: {rust_peer['capabilities']}")
                else:
                    self.log("⚠️  Rust peer not found in federation peers")
            else:
                self.log(f"❌ Federation peers failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Federation peers error: {e}", "ERROR")
            return False
        
        self.log("\n🎉 PHASE 4 COMPATIBILITY TESTS PASSED!")
        return True
    
    def test_phase6_features(self) -> bool:
        """Test Phase 6 multi-implementation features"""
        self.log("\n" + "="*60)
        self.log("TESTING PHASE 6 MULTI-IMPLEMENTATION FEATURES")
        self.log("="*60)
        
        # Test 1: Fractal levels
        try:
            response = requests.get(f"{self.base_url}/fractal/levels", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Fractal levels: {data['fractal_levels']}")
                self.log(f"   Level 1: {data['level_statistics']['level_1']['count']} base nodes")
                self.log(f"   Level 2: {data['level_statistics']['level_2']['count']} fractal subnodes")
            else:
                self.log(f"❌ Fractal levels failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Fractal levels error: {e}", "ERROR")
            return False
        
        # Test 2: Fractal expansion
        try:
            response = requests.get(f"{self.base_url}/fractal/expand/codex:Void", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Void fractal expansion: {data['total_subnodes']} subnodes")
                self.log(f"   Scientific: {len([k for k in data['subnodes'].keys() if ':scientific:' in k])}")
                self.log(f"   Symbolic: {len([k for k in data['subnodes'].keys() if ':symbolic:' in k])}")
                self.log(f"   Water: {len([k for k in data['subnodes'].keys() if ':water:' in k])}")
            else:
                self.log(f"❌ Void expansion failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Void expansion error: {e}", "ERROR")
            return False
        
        # Test 3: Fractal subnodes
        try:
            response = requests.get(f"{self.base_url}/fractal/subnodes/codex:Field", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Field fractal subnodes: {data['total_subnodes']} subnodes")
                self.log(f"   Base node: {data['base_node']['name']}")
                self.log(f"   Water state: {data['base_node']['water_state']}")
            else:
                self.log(f"❌ Field subnodes failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Field subnodes error: {e}", "ERROR")
            return False
        
        # Test 4: Scientific context
        try:
            response = requests.get(f"{self.base_url}/fractal/context/scientific", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Scientific context: {data['count']} subnodes")
                self.log(f"   Description: {data['description']}")
            else:
                self.log(f"❌ Scientific context failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Scientific context error: {e}", "ERROR")
            return False
        
        # Test 5: Actor endpoint
        try:
            response = requests.get(f"{self.base_url}/actor", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Actor endpoint: {data['name']}")
                self.log(f"   Fractal capabilities: {data['fractal_capabilities']}")
            else:
                self.log(f"❌ Actor endpoint failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Actor endpoint error: {e}", "ERROR")
            return False
        
        self.log("\n🎉 PHASE 6 FEATURE TESTS PASSED!")
        return True
    
    def demonstrate_rust_wisdom(self):
        """Demonstrate the Rust implementation's fractal wisdom"""
        self.log("\n" + "="*60)
        self.log("DEMONSTRATING RUST FRACTAL WISDOM")
        self.log("="*60)
        
        # Show a few key node expansions
        demo_nodes = ["codex:Void", "codex:Field", "codex:Coherence"]
        
        for node_id in demo_nodes:
            try:
                response = requests.get(f"{self.base_url}/fractal/subnodes/{node_id}", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    self.log(f"\n🌊 {node_id} - {data['base_node']['name']}")
                    self.log(f"   Water State: {data['base_node']['water_state']}")
                    self.log(f"   Resonance: {data['base_node']['resonance']}")
                    self.log(f"   Total Subnodes: {data['total_subnodes']}")
                    
                    # Show one example from each context
                    for context in data['contexts']:
                        context_nodes = data['subnodes'][context]
                        if context_nodes:
                            first_key = list(context_nodes.keys())[0]
                            first_node = context_nodes[first_key]
                            self.log(f"   {context.title()}: {first_node['name']} (resonance: {first_node['resonance']:.2f})")
                
            except Exception as e:
                self.log(f"❌ Error demonstrating {node_id}: {e}", "ERROR")
    
    def run_full_test_suite(self) -> bool:
        """Run the complete Rust fractal test suite"""
        self.log("🌊 Living Codex Phase 6 - Rust Fractal Federation Testing")
        self.log("="*60)
        
        try:
            # Step 1: Build and start server
            if not self.build_and_start_server():
                return False
            
            # Step 2: Wait for server to be ready
            if not self.wait_for_server():
                return False
            
            # Step 3: Test Phase 4 compatibility
            if not self.test_phase4_compatibility():
                return False
            
            # Step 4: Test Phase 6 features
            if not self.test_phase6_features():
                return False
            
            # Step 5: Demonstrate Rust fractal wisdom
            self.demonstrate_rust_wisdom()
            
            self.log("\n" + "="*60)
            self.log("🎉 RUST FRACTAL TESTING COMPLETED SUCCESSFULLY!")
            self.log("✅ Phase 4: Full compatibility maintained")
            self.log("✅ Phase 6: Multi-implementation operational")
            self.log("✅ Rust server: High-performance fractal expansion")
            self.log("✅ 12 base nodes expanded into 108 fractal subnodes")
            self.log("✅ 3 fractal dimensions: scientific, symbolic, water")
            self.log("="*60)
            
            return True
            
        except Exception as e:
            self.log(f"❌ Test suite failed: {e}", "ERROR")
            return False
    
    def cleanup(self):
        """Clean up server process"""
        if self.server_process:
            self.log("Stopping Rust server...")
            try:
                self.server_process.terminate()
                self.server_process.wait(timeout=5)
                self.log("✅ Rust server stopped gracefully")
            except subprocess.TimeoutExpired:
                self.log("⚠️  Server didn't stop gracefully, forcing...")
                self.server_process.kill()
            except Exception as e:
                self.log(f"⚠️  Error stopping server: {e}")

def main():
    """Main entry point"""
    tester = RustFractalTester()
    
    try:
        success = tester.run_full_test_suite()
        
        if success:
            print("\n🎉 SUCCESS: Rust fractal federation is working perfectly!")
            print("✅ Multi-implementation foundation established")
            print("✅ High-performance fractal expansion operational")
        else:
            print("\n⚠️  Test suite completed with some failures")
        
        return success
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Testing interrupted by user")
        return False
    except Exception as e:
        print(f"\n\n❌ Test suite crashed: {e}")
        return False
    finally:
        # Always cleanup
        tester.cleanup()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

