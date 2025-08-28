#!/usr/bin/env python3
"""
Living Codex REST API Server
============================

This server provides a REST API for the Living Codex that enables:
1. Querying all nodes and meta-nodes
2. Navigating from core principles to source files
3. Searching and filtering capabilities
4. Complete self-reflection of the system

The API is fully integrated with the persistence system and provides
real access to all stored nodes and meta-nodes.
"""

import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from flask import Flask, jsonify, request, render_template_string
import threading
import time

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Initialize Flask app
app = Flask(__name__)

# Global variables for the Living Codex systems
living_codex_systems = {}
file_system = None
discovered_files = {}
persistence_system = None

# HTML template for the API documentation
API_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Living Codex REST API</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .endpoint { margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
        .method { background: #007bff; color: white; padding: 5px 10px; border-radius: 3px; display: inline-block; }
        .url { background: #f8f9fa; padding: 10px; border-radius: 3px; font-family: monospace; }
        .example { background: #e9ecef; padding: 10px; border-radius: 3px; font-family: monospace; margin: 10px 0; }
        .description { margin: 10px 0; }
    </style>
</head>
<body>
    <h1>🌟 Living Codex REST API</h1>
    <p>This API provides access to the complete Living Codex system, enabling navigation from core principles to source files.</p>
    
    <h2>📚 API Endpoints</h2>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/status</div>
        <div class="description">Get system status and overview</div>
        <div class="example">curl http://localhost:5001/api/status</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/nodes</div>
        <div class="description">Get all nodes in the system</div>
        <div class="example">curl http://localhost:5001/api/nodes</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/nodes/{node_id}</div>
        <div class="description">Get a specific node by ID</div>
        <div class="example">curl http://localhost:5001/api/nodes/concept_be453fef</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/files</div>
        <div class="description">Get all discovered source files</div>
        <div class="example">curl http://localhost:5001/api/files</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/files/{file_path}</div>
        <div class="description">Get information about a specific file</div>
        <div class="example">curl http://localhost:5001/api/files/src/core/living_codex_ontology.py</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/search?q={query}</div>
        <div class="description">Search for nodes and files by query</div>
        <div class="example">curl "http://localhost:5001/api/search?q=System"</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/principles</div>
        <div class="description">Get all core principles</div>
        <div class="example">curl http://localhost:5001/api/principles</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/principles/{principle}/files</div>
        <div class="description">Get source files related to a specific principle</div>
        <div class="example">curl http://localhost:5000/api/principles/System/files</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/navigate?from={node_id}&to={target_type}</div>
        <div class="description">Navigate from one node to related nodes of a specific type</div>
        <div class="example">curl "http://localhost:5000/api/navigate?from=concept_be453fef&to=source_file"</div>
    </div>
    
    <div class="endpoint">
        <div class="method">GET</div>
        <div class="url">/api/analytics</div>
        <div class="description">Get comprehensive system analytics</div>
        <div class="example">curl http://localhost:5001/api/analytics</div>
    </div>
    
    <h2>🚀 Quick Start Examples</h2>
    
    <h3>1. Get System Status</h3>
    <div class="example">curl http://localhost:5001/api/status</div>
    
    <h3>2. Find Core Principles</h3>
    <div class="example">curl http://localhost:5001/api/principles</div>
    
    <h3>3. Navigate from Principle to Source Files</h3>
            <div class="example">curl "http://localhost:5001/api/principles/System/files"</div>
    
    <h3>4. Search for Specific Concepts</h3>
            <div class="example">curl "http://localhost:5001/api/search?q=meta-circular"</div>
    
    <h3>5. Get All Source Files</h3>
            <div class="example">curl http://localhost:5001/api/files</div>
    
    <h3>6. Get System Analytics</h3>
    <div class="example">curl http://localhost:5000/api/analytics</div>
    
    <h2>🔍 Navigation Examples</h2>
    
    <p><strong>From Core Principle to Source File:</strong></p>
    <ol>
        <li>Get all principles: <code>GET /api/principles</code></li>
        <li>Choose a principle (e.g., "System")</li>
        <li>Get related files: <code>GET /api/principles/System/files</code></li>
        <li>Examine specific file: <code>GET /api/files/{file_path}</code></li>
    </ol>
    
    <p><strong>Search and Discover:</strong></p>
    <ol>
        <li>Search for concepts: <code>GET /api/search?q={concept}</code></li>
        <li>Get node details: <code>GET /api/nodes/{node_id}</code></li>
        <li>Navigate to related nodes: <code>GET /api/navigate?from={node_id}&to={type}</code></li>
    </ol>
    
    <h2>📊 System Information</h2>
    <p>This API provides access to:</p>
    <ul>
        <li><strong>Foundational Nodes:</strong> Core system concepts and principles</li>
        <li><strong>Source Files:</strong> All discovered source code and documentation</li>
        <li><strong>Relationships:</strong> Connections between principles and implementations</li>
        <li><strong>Search:</strong> Find concepts, principles, and files</li>
        <li><strong>Navigation:</strong> Move from principles to source files</li>
        <li><strong>Analytics:</strong> Complete system statistics and insights</li>
    </ul>
</body>
</html>
"""

def initialize_living_codex():
    """Initialize the Living Codex systems and discover files"""
    global living_codex_systems, file_system, discovered_files, persistence_system
    
    print("🚀 Initializing Living Codex REST API...")
    
    try:
        # Import required systems
        from self_reflective_file_system import SelfReflectiveFileSystem
        from universal_knowledge_representation_system import get_universal_knowledge_representation_system
        from vibrational_axes_system import get_vibrational_axes_system
        from fractal_recursion_system import get_fractal_recursion_system
        from resonance_governance_system import get_resonance_governance_system
        from self_generating_system import get_self_generating_system
        from advanced_ai_integration_system import get_advanced_ai_integration_system
        from living_codex_persistence import LivingCodexPersistence
        
        print("✅ All systems imported successfully")
        
        # Initialize Living Codex systems
        living_codex_systems = {
            'universal': get_universal_knowledge_representation_system(),
            'vibrational': get_vibrational_axes_system(),
            'fractal': get_fractal_recursion_system(),
            'governance': get_resonance_governance_system(),
            'self_generating': get_self_generating_system(),
            'ai_integration': get_advanced_ai_integration_system()
        }
        
        print("✅ Living Codex systems initialized")
        
        # Initialize persistence system
        persistence_system = LivingCodexPersistence()
        
        # Try to load existing state
        print("🔄 Attempting to load existing system state...")
        # Always initialize the self-reflective file system
        file_system = SelfReflectiveFileSystem()
        
        if persistence_system.load_system_state(
            living_codex_systems['universal'],
            living_codex_systems['fractal'],
            living_codex_systems['ai_integration'],
            living_codex_systems['self_generating'],
            living_codex_systems['vibrational'],
            living_codex_systems['governance']
        ):
            print("✅ System state loaded from persistence")
            
            # Even when loading from persistence, discover files for API access
            discovered_files = file_system.discover_all_source_files()
            if discovered_files:
                print(f"✅ Rediscovered {len(discovered_files)} source files for API access")
            else:
                print("⚠️ No source files rediscovered")
        else:
            print("⚠️ No existing state found, initializing fresh system")
            
            # Discover and create file nodes
            discovered_files = file_system.discover_all_source_files()
            
            if discovered_files:
                print(f"✅ Discovered {len(discovered_files)} source files")
                
                # Create file nodes in Living Codex
                file_system.create_file_nodes_in_living_codex(living_codex_systems['universal'])
                
                # Save the new state
                persistence_system.save_system_state(
                    living_codex_systems['universal'],
                    living_codex_systems['fractal'],
                    living_codex_systems['ai_integration'],
                    living_codex_systems['self_generating'],
                    living_codex_systems['vibrational'],
                    living_codex_systems['governance']
                )
                
                # Generate self-description
                self_desc = file_system.generate_self_description()
                print(f"✅ Self-description generated: {self_desc['total_files']} files")
            else:
                print("❌ No source files discovered")
                return False
        
        print("✅ Living Codex REST API initialization complete")
        return True
        
    except Exception as e:
        print(f"❌ Initialization error: {e}")
        import traceback
        traceback.print_exc()
        return False

# API Routes

@app.route('/')
def index():
    """Main API documentation page"""
    return render_template_string(API_HTML_TEMPLATE)

@app.route('/api/status')
def api_status():
    """Get system status and overview"""
    try:
        # Get system analytics safely
        try:
            universal_analytics = living_codex_systems['universal'].get_universal_knowledge_analytics()
            total_concepts = universal_analytics.get('total_universal_concepts', 0)
            meta_circular = universal_analytics.get('total_meta_circular_architectures', 0)
            knowledge_expansions = universal_analytics.get('total_knowledge_expansions', 0)
        except:
            # Fallback to direct counting
            total_concepts = len(living_codex_systems['universal'].universal_concepts)
            meta_circular = 0
            knowledge_expansions = 0
        
        try:
            fractal_stats = living_codex_systems['fractal'].get_fractal_statistics()
            fractal_nodes = fractal_stats.get('total_nodes', 0)
        except:
            fractal_nodes = len(living_codex_systems['fractal'].fractal_nodes)
        
        # Ensure we have the correct count
        if total_concepts == 0:
            total_concepts = len(living_codex_systems['universal'].universal_concepts)
        if fractal_nodes == 0:
            fractal_nodes = len(living_codex_systems['fractal'].fractal_nodes)
        
        status = {
            'status': 'operational',
            'timestamp': datetime.now().isoformat(),
            'system_name': 'Living Codex REST API',
            'version': '2.0.0',
            'living_codex': {
                'total_concepts': total_concepts,
                'meta_circular_architectures': meta_circular,
                'knowledge_expansions': knowledge_expansions,
                'fractal_nodes': fractal_nodes
            },
            'file_system': {
                'total_files': len(discovered_files) if discovered_files else 0,
                'file_types': list(set([f['file_type'] for f in discovered_files.values()])) if discovered_files else [],
                'total_size_mb': sum(f['file_size_bytes'] for f in discovered_files.values()) / (1024 * 1024) if discovered_files else 0
            },
            'capabilities': [
                'self-reflection',
                'self-discovery',
                'self-analysis',
                'meta-circularity',
                'principle-to-file navigation',
                'complete source code access',
                'persistence',
                'real-time analytics'
            ]
        }
        
        return jsonify(status)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nodes')
def api_nodes():
    """Get all nodes in the system"""
    try:
        # Get all concepts safely
        try:
            all_concepts = living_codex_systems['universal'].get_universal_knowledge_analytics()
            total_concepts = all_concepts.get('total_universal_concepts', 0)
        except:
            total_concepts = len(living_codex_systems['universal'].universal_concepts)
        
        try:
            fractal_stats = living_codex_systems['fractal'].get_fractal_statistics()
            fractal_nodes = fractal_stats.get('total_nodes', 0)
        except:
            fractal_nodes = len(living_codex_systems['fractal'].fractal_nodes)
        
        # Get actual concept details
        concept_details = []
        for concept_id, concept in living_codex_systems['universal'].universal_concepts.items():
            if hasattr(concept, 'name'):
                concept_details.append({
                    'id': concept_id,
                    'name': concept.name,
                    'type': getattr(concept, 'concept_type', 'unknown'),
                    'description': getattr(concept, 'description', '')[:200] + '...' if getattr(concept, 'description', '') else ''
                })
            else:
                # Handle dictionary format from persistence
                concept_details.append({
                    'id': concept_id,
                    'name': concept.get('name', 'Unknown'),
                    'type': concept.get('concept_type', 'unknown'),
                    'description': concept.get('description', '')[:200] + '...' if concept.get('description', '') else ''
                })
        
        nodes = {
            'total_nodes': total_concepts,
            'fractal_nodes': fractal_nodes,
            'node_types': {
                'foundational': 9,  # Core system nodes
                'source_files': len(discovered_files) if discovered_files else 0,
                'generated': total_concepts - 9
            },
            'concepts': concept_details[:50]  # Limit to first 50 for performance
        }
        
        return jsonify(nodes)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nodes/<node_id>')
def api_node_detail(node_id):
    """Get a specific node by ID"""
    try:
        # Get concept from universal system
        if node_id in living_codex_systems['universal'].universal_concepts:
            concept = living_codex_systems['universal'].universal_concepts[node_id]
            
            if hasattr(concept, 'name'):
                # Object format
                node_detail = {
                    'id': node_id,
                    'name': concept.name,
                    'type': getattr(concept, 'concept_type', 'unknown'),
                    'description': getattr(concept, 'description', ''),
                    'properties': getattr(concept, 'ontological_properties', {}),
                    'vibrational_axes': getattr(concept, 'vibrational_axes', [])
                }
            else:
                # Dictionary format from persistence
                node_detail = {
                    'id': node_id,
                    'name': concept.get('name', 'Unknown'),
                    'type': concept.get('concept_type', 'unknown'),
                    'description': concept.get('description', ''),
                    'properties': concept.get('ontological_properties', {}),
                    'vibrational_axes': concept.get('vibrational_axes', [])
                }
            
            return jsonify(node_detail)
        else:
            return jsonify({'error': f'Node not found: {node_id}'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/files')
def api_files():
    """Get all discovered source files"""
    try:
        current_discovered_files = discovered_files
        if not current_discovered_files:
            # Try to get files from persistence
            try:
                file_system = SelfReflectiveFileSystem()
                current_discovered_files = file_system.discover_all_source_files()
            except:
                current_discovered_files = {}
        
        files_summary = {
            'total_files': len(current_discovered_files) if current_discovered_files else 0,
            'files': []
        }
        
        if current_discovered_files:
            for relative_path, file_info in current_discovered_files.items():
                files_summary['files'].append({
                    'path': relative_path,
                    'name': file_info['file_name'],
                    'type': file_info['file_type'],
                    'size_bytes': file_info['file_size_bytes'],
                    'size_mb': round(file_info['file_size_bytes'] / (1024 * 1024), 3),
                    'lines': file_info['line_count'],
                    'last_modified': file_info['last_modified'],
                    'key_concepts': file_info.get('key_concepts', []),
                    'principles': file_info.get('principles', [])
                })
        
        return jsonify(files_summary)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/files/<path:file_path>')
def api_file_detail(file_path):
    """Get information about a specific file"""
    try:
        current_discovered_files = discovered_files
        if not current_discovered_files:
            # Try to get files from persistence
            try:
                file_system = SelfReflectiveFileSystem()
                current_discovered_files = file_system.discover_all_source_files()
            except:
                current_discovered_files = {}
        
        if file_path in current_discovered_files:
            file_info = current_discovered_files[file_path]
            return jsonify({
                'file_path': file_path,
                'file_info': file_info
            })
        else:
            return jsonify({'error': f'File not found: {file_path}'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search')
def api_search():
    """Search for nodes and files by query"""
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify({'error': 'Query parameter "q" is required'}), 400
        
        # Search in files
        current_discovered_files = discovered_files
        if not current_discovered_files:
            try:
                file_system = SelfReflectiveFileSystem()
                current_discovered_files = file_system.discover_all_source_files()
            except:
                current_discovered_files = {}
        
        file_results = []
        if current_discovered_files:
            try:
                file_results = file_system.search_files_by_concept(query)
            except:
                file_results = []
        
        # Search in nodes
        node_results = []
        for concept_id, concept in living_codex_systems['universal'].universal_concepts.items():
            if hasattr(concept, 'name'):
                if query.lower() in concept.name.lower() or query.lower() in getattr(concept, 'description', '').lower():
                    node_results.append({
                        'id': concept_id,
                        'name': concept.name,
                        'type': getattr(concept, 'concept_type', 'unknown'),
                        'match_type': 'name' if query.lower() in concept.name.lower() else 'description'
                    })
            else:
                # Dictionary format
                if query.lower() in concept.get('name', '').lower() or query.lower() in concept.get('description', '').lower():
                    node_results.append({
                        'id': concept_id,
                        'name': concept.get('name', 'Unknown'),
                        'type': concept.get('concept_type', 'unknown'),
                        'match_type': 'name' if query.lower() in concept.get('name', '').lower() else 'description'
                    })
        
        search_results = {
            'query': query,
            'file_results': {
                'count': len(file_results),
                'results': file_results[:10]  # Limit to 10 results
            },
            'node_results': {
                'count': len(node_results),
                'results': node_results[:10]  # Limit to 10 results
            }
        }
        
        return jsonify(search_results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/principles')
def api_principles():
    """Get all core principles"""
    try:
        # Get principles from the foundational nodes
        principles = [
            {
                'id': 'core_principles',
                'name': 'Core Principles Documentation',
                'description': 'Complete documentation of Living Codex core principles and philosophy',
                'type': 'core_principles',
                'water_state': 'ws.structured',
                'fractal_layer': 1
            },
            {
                'id': 'system_boundaries',
                'name': 'System Boundaries Definition',
                'description': 'Complete definition of Living Codex system boundaries and principles',
                'type': 'system_boundaries',
                'water_state': 'ws.ice',
                'fractal_layer': 0
            },
            {
                'id': 'architecture_spec',
                'name': 'Architecture Specification',
                'description': 'Complete specification of Living Codex architecture and design',
                'type': 'architecture_spec',
                'water_state': 'ws.ice',
                'fractal_layer': 1
            }
        ]
        
        return jsonify({
            'total_principles': len(principles),
            'principles': principles
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/principles/<principle>/files')
def api_principle_files(principle):
    """Get source files related to a specific principle"""
    try:
        # Search for files related to this principle
        current_discovered_files = discovered_files
        if not current_discovered_files:
            try:
                file_system = SelfReflectiveFileSystem()
                current_discovered_files = file_system.discover_all_source_files()
            except:
                current_discovered_files = {}
        
        related_files = []
        if current_discovered_files:
            try:
                related_files = file_system.search_files_by_concept(principle)
            except:
                related_files = []
        
        return jsonify({
            'principle': principle,
            'related_files': {
                'count': len(related_files),
                'files': related_files
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/navigate')
def api_navigate():
    """Navigate from one node to related nodes of a specific type"""
    try:
        from_node = request.args.get('from', '')
        to_type = request.args.get('to', '')
        
        if not from_node or not to_type:
            return jsonify({'error': 'Both "from" and "to" parameters are required'}), 400
        
        # Get the source node
        if from_node not in living_codex_systems['universal'].universal_concepts:
            return jsonify({'error': f'Source node not found: {from_node}'}), 404
        
        source_concept = living_codex_systems['universal'].universal_concepts[from_node]
        
        # Find related nodes of the target type
        related_nodes = []
        for concept_id, concept in living_codex_systems['universal'].universal_concepts.items():
            if concept_id == from_node:
                continue
                
            if hasattr(concept, 'concept_type'):
                concept_type = concept.concept_type
            else:
                concept_type = concept.get('concept_type', '')
            
            if concept_type == to_type:
                if hasattr(concept, 'name'):
                    related_nodes.append({
                        'id': concept_id,
                        'name': concept.name,
                        'type': concept_type,
                        'description': getattr(concept, 'description', '')[:100] + '...'
                    })
                else:
                    related_nodes.append({
                        'id': concept_id,
                        'name': concept.get('name', 'Unknown'),
                        'type': concept_type,
                        'description': concept.get('description', '')[:100] + '...'
                    })
        
        return jsonify({
            'from_node': from_node,
            'to_type': to_type,
            'source_node': {
                'id': from_node,
                'name': source_concept.name if hasattr(source_concept, 'name') else source_concept.get('name', 'Unknown'),
                'type': source_concept.concept_type if hasattr(source_concept, 'concept_type') else source_concept.get('concept_type', 'unknown')
            },
            'related_nodes': {
                'count': len(related_nodes),
                'nodes': related_nodes[:20]  # Limit to 20 results
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analytics')
def api_analytics():
    """Get comprehensive system analytics"""
    try:
        # Get analytics from all systems safely
        try:
            universal_analytics = living_codex_systems['universal'].get_universal_knowledge_analytics()
            total_concepts = universal_analytics.get('total_universal_concepts', 0)
            meta_circular = universal_analytics.get('total_meta_circular_architectures', 0)
            knowledge_expansions = universal_analytics.get('total_knowledge_expansions', 0)
        except:
            total_concepts = len(living_codex_systems['universal'].universal_concepts)
            meta_circular = 0
            knowledge_expansions = 0
        
        try:
            fractal_stats = living_codex_systems['fractal'].get_fractal_statistics()
            fractal_nodes = fractal_stats.get('total_nodes', 0)
        except:
            fractal_nodes = len(living_codex_systems['fractal'].fractal_nodes)
        
        try:
            vibrational_stats = living_codex_systems['vibrational'].get_vibrational_analytics()
            vibrational_axes = len(vibrational_stats.get('vibrational_axes', []))
            resonance_states = len(vibrational_stats.get('resonance_states', {}))
        except:
            vibrational_axes = len(living_codex_systems['vibrational'].vibrational_axes)
            resonance_states = len(living_codex_systems['vibrational'].resonance_states)
        
        # Calculate file statistics
        current_discovered_files = discovered_files
        if not current_discovered_files:
            try:
                file_system = SelfReflectiveFileSystem()
                current_discovered_files = file_system.discover_all_source_files()
            except:
                current_discovered_files = {}
        
        file_stats = {
            'total_files': len(current_discovered_files) if current_discovered_files else 0,
            'file_types': {},
            'total_size_mb': 0,
            'total_lines': 0
        }
        
        if current_discovered_files:
            for file_info in current_discovered_files.values():
                file_type = file_info['file_type']
                file_stats['file_types'][file_type] = file_stats['file_types'].get(file_type, 0) + 1
                file_stats['total_size_mb'] += file_info['file_size_bytes'] / (1024 * 1024)
                file_stats['total_lines'] += file_info['line_count']
        
        analytics = {
            'timestamp': datetime.now().isoformat(),
            'system_overview': {
                'total_concepts': total_concepts,
                'meta_circular_architectures': meta_circular,
                'knowledge_expansions': knowledge_expansions,
                'fractal_nodes': fractal_nodes,
                'vibrational_axes': vibrational_axes,
                'resonance_states': resonance_states
            },
            'file_system': file_stats,
            'concept_distribution': {
                'by_type': {},
                'by_water_state': {},
                'by_fractal_layer': {}
            },
            'system_health': {
                'persistence_enabled': persistence_system is not None,
                'self_reflection_active': len(current_discovered_files) > 0 if current_discovered_files else False,
                'meta_circularity': meta_circular > 0
            }
        }
        
        # Analyze concept distribution
        for concept in living_codex_systems['universal'].universal_concepts.values():
            if hasattr(concept, 'concept_type'):
                concept_type = concept.concept_type
                water_state = getattr(concept, 'ontological_properties', {}).get('water_state', 'unknown')
                fractal_layer = getattr(concept, 'ontological_properties', {}).get('fractal_layer', 'unknown')
            else:
                concept_type = concept.get('concept_type', 'unknown')
                water_state = concept.get('ontological_properties', {}).get('water_state', 'unknown')
                fractal_layer = concept.get('ontological_properties', {}).get('fractal_layer', 'unknown')
            
            analytics['concept_distribution']['by_type'][concept_type] = analytics['concept_distribution']['by_type'].get(concept_type, 0) + 1
            analytics['concept_distribution']['by_water_state'][water_state] = analytics['concept_distribution']['by_water_state'].get(water_state, 0) + 1
            analytics['concept_distribution']['by_fractal_layer'][fractal_layer] = analytics['concept_distribution']['by_fractal_layer'].get(fractal_layer, 0) + 1
        
        return jsonify(analytics)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def start_api_server(host='0.0.0.0', port=5001):
    """Start the REST API server"""
    print(f"🚀 Starting Living Codex REST API server on {host}:{port}")
    print(f"📖 API documentation available at: http://{host}:{port}/")
    print(f"🔍 Test endpoints with curl commands")
    
    # Initialize the Living Codex system
    if not initialize_living_codex():
        print("❌ Failed to initialize Living Codex system")
        return False
    
    # Start the Flask server
    try:
        app.run(host=host, port=port, debug=False, threaded=True)
        return True
    except Exception as e:
        print(f"❌ Failed to start API server: {e}")
        return False

if __name__ == "__main__":
    start_api_server()
