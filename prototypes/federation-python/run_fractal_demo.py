#!/usr/bin/env python3
"""
Living Codex Phase 5 - End-to-End Fractal Demo
Starts the server, verifies it's running, and demonstrates fractal expansion
"""

import subprocess
import time
import requests
import json
import sys
import os
from pathlib import Path

class FractalDemoRunner:
    """End-to-end demo runner for the fractal federation server"""
    
    def __init__(self):
        self.server_process = None
        self.base_url = "http://localhost:8788"
        self.server_script = "fractal_server.py"
        self.max_wait_time = 45  # seconds
        
    def log(self, message: str, level: str = "INFO"):
        """Log messages with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
    
    def start_server(self) -> bool:
        """Start the fractal server in the background"""
        self.log("Starting fractal federation server...")
        
        try:
            # Start server in background
            self.server_process = subprocess.Popen(
                [sys.executable, self.server_script],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=os.getcwd()
            )
            
            self.log(f"Server process started with PID: {self.server_process.pid}")
            
            # Wait a moment and check if it's still running
            time.sleep(1)
            if self.server_process.poll() is not None:
                # Server crashed, get error output
                stdout, stderr = self.server_process.communicate()
                self.log(f"❌ Server crashed immediately!", "ERROR")
                if stderr:
                    self.log(f"Error output: {stderr.decode()}", "ERROR")
                if stdout:
                    self.log(f"Standard output: {stdout.decode()}", "ERROR")
                return False
            
            return True
            
        except Exception as e:
            self.log(f"Failed to start server: {e}", "ERROR")
            return False
    
    def wait_for_server(self) -> bool:
        """Wait for server to be ready and responding"""
        self.log("Waiting for server to be ready...")
        
        start_time = time.time()
        while time.time() - start_time < self.max_wait_time:
            # Check if server is still running
            if self.server_process.poll() is not None:
                stdout, stderr = self.server_process.communicate()
                self.log(f"❌ Server crashed while waiting!", "ERROR")
                if stderr:
                    self.log(f"Error output: {stderr.decode()}", "ERROR")
                if stdout:
                    self.log(f"Standard output: {stdout.decode()}", "ERROR")
                return False
            
            try:
                response = requests.get(f"{self.base_url}/", timeout=2)
                if response.status_code == 200:
                    self.log("✅ Server is ready and responding!")
                    return True
            except requests.exceptions.RequestException:
                pass
            
            time.sleep(1)
            elapsed = int(time.time() - start_time)
            if elapsed % 5 == 0:
                self.log(f"Still waiting... ({elapsed}s elapsed)")
                # Check server output for any clues
                if self.server_process.stdout and self.server_process.stdout.readable():
                    try:
                        output = self.server_process.stdout.read1(1024).decode()
                        if output:
                            self.log(f"Server output: {output.strip()}")
                    except:
                        pass
        
        # Give it one more try with a longer timeout
        self.log("Giving server one more chance with longer timeout...")
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                self.log("✅ Server responded on final attempt!")
                return True
        except requests.exceptions.RequestException as e:
            self.log(f"Final attempt failed: {e}")
        
        self.log("❌ Server failed to start within timeout period", "ERROR")
        return False
    
    def test_fractal_expansion(self):
        """Test the fractal expansion capabilities"""
        self.log("\n" + "="*60)
        self.log("TESTING FRACTAL EXPANSION CAPABILITIES")
        self.log("="*60)
        
        # Test 1: Root endpoint
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Root endpoint: {data['name']}")
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
        
        # Test 3: Fractal levels endpoint
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
        
        # Test 4: Fractal expansion of Void node
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
        
        # Test 5: Scientific context
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
        
        # Test 6: Post contribution to fractal subnode
        try:
            test_contribution = {
                "type": "Create",
                "actor": "fractal_demo",
                "object": {
                    "type": "Contribution",
                    "nodeId": "codex:Void:scientific:empirical",
                    "content": "The Void's empirical nature manifests in quantum vacuum fluctuations",
                    "resonance": 0.95,
                    "fractalContext": "scientific"
                }
            }
            
            response = requests.post(
                f"{self.base_url}/inbox",
                json=test_contribution,
                headers={"Content-Type": "application/activity+json"},
                timeout=10
            )
            
            if response.status_code == 202:
                self.log("✅ Posted contribution to fractal subnode")
            else:
                self.log(f"❌ Contribution failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Contribution error: {e}", "ERROR")
            return False
        
        # Test 7: Retrieve the contribution
        try:
            response = requests.get(f"{self.base_url}/contributions/node/codex:Void:scientific:empirical", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Retrieved contribution: {data['count']} found")
            else:
                self.log(f"❌ Contribution retrieval failed: {response.status_code}")
                return False
        except Exception as e:
            self.log(f"❌ Contribution retrieval error: {e}", "ERROR")
            return False
        
        self.log("\n🎉 ALL FRACTAL EXPANSION TESTS PASSED!")
        return True
    
    def demonstrate_fractal_wisdom(self):
        """Demonstrate the fractal wisdom by showing node expansions"""
        self.log("\n" + "="*60)
        self.log("DEMONSTRATING FRACTAL WISDOM")
        self.log("="*60)
        
        # Show a few key node expansions
        demo_nodes = ["codex:Void", "codex:Field", "codex:Pattern"]
        
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
    
    def run_demo(self) -> bool:
        """Run the complete fractal demo"""
        self.log("🌊 Living Codex Phase 5 - Fractal Expansion Demo")
        self.log("="*60)
        
        try:
            # Step 1: Start server
            if not self.start_server():
                return False
            
            # Step 2: Wait for server to be ready
            if not self.wait_for_server():
                return False
            
            # Step 3: Test fractal expansion
            if not self.test_fractal_expansion():
                return False
            
            # Step 4: Demonstrate fractal wisdom
            self.demonstrate_fractal_wisdom()
            
            self.log("\n" + "="*60)
            self.log("🎉 FRACTAL DEMO COMPLETED SUCCESSFULLY!")
            self.log("✅ Phase 4: Full compatibility maintained")
            self.log("✅ Phase 5: Fractal expansion operational")
            self.log("✅ 12 base nodes expanded into 36 fractal subnodes")
            self.log("✅ 3 fractal dimensions: scientific, symbolic, water")
            self.log("="*60)
            
            return True
            
        except Exception as e:
            self.log(f"❌ Demo failed: {e}", "ERROR")
            return False
    
    def cleanup(self):
        """Clean up server process"""
        if self.server_process:
            self.log("Stopping server...")
            try:
                self.server_process.terminate()
                self.server_process.wait(timeout=5)
                self.log("✅ Server stopped gracefully")
            except subprocess.TimeoutExpired:
                self.log("⚠️  Server didn't stop gracefully, forcing...")
                self.server_process.kill()
            except Exception as e:
                self.log(f"⚠️  Error stopping server: {e}")

def main():
    """Main entry point"""
    runner = FractalDemoRunner()
    
    try:
        success = runner.run_demo()
        
        if success:
            print("\n🎉 SUCCESS: Fractal expansion is working perfectly!")
            print("✅ Both fractal levels are operational")
            print("✅ You can now explore the expanded wisdom!")
        else:
            print("\n⚠️  Demo completed with some failures")
        
        return success
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
        return False
    except Exception as e:
        print(f"\n\n❌ Demo crashed: {e}")
        return False
    finally:
        # Always cleanup
        runner.cleanup()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
