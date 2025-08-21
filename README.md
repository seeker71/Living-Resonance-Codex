# Living Codex — Phase 4 Complete ✅

This is a **Phase 4 complete** implementation of the Living Codex - a federated, fractal knowledge system that integrates consciousness, archetypes, and resonance through water-state metaphors and harmonic principles, now with interactive sacred geometry, resonance dynamics, **community resonance overlays**, **AI agent integration**, and **content-addressed storage with enhanced federation**.

## Quickstart

1. **Graph seed (Python + Neo4j):**
   - Ensure Neo4j is running locally (default bolt://localhost:7687).
   - Create a Python venv: `python3 -m venv .venv && source .venv/bin/activate` (Windows: `venv\Scripts\activate`).
   - Install deps (none required yet); run loader: `python prototypes/graph/loader.py`.

2. **Visualization (JS + Vite + Three.js):**
   - `cd prototypes/viz`
   - `npm install`
   - `npm run dev` → open the printed local URL.

3. **Resonance scoring (Python):**
   - `python prototypes/resonance/score.py`

4. **Federation stub (Node/Express):**
   - `node prototypes/federation/server.js`

## Phase 4 Implementation Status ✅

### **Core Components (Complete)**
- **`ontology/seed.json`** → Complete 12-node seed ontology with water-state mappings, archetypes, and harmonic representations
- **`ontology/schema.json`** → Full JSON-LD schema with all node types, relationships, and metadata
- **`prototypes/graph/loader.py`** → Enhanced Neo4j loader with all new properties and constraints
- **`prototypes/viz/`** → **Phase 2**: Interactive sacred geometry visualization with resonance dynamics
- **`prototypes/resonance/score.py`** → Advanced resonance analysis with harmonic and water-state themes
- **`prototypes/federation/server.js`** → ActivityPub-style federation endpoints

### **Phase 2 Enhanced Features**
- **🌊 Sacred Geometry Overlays**: Flower of Life, Icositetragon Wheel, Metatron's Cube
- **🎛️ Interactive Axis Sliders**: Real-time resonance control for all 5 vibrational axes
- **💫 Resonance Dynamics**: Node glow = resonance amplitude, edges ripple with coherence
- **🔍 Fractal Zoom**: Click nodes to reveal nested mandalas and deeper wisdom
- **🌊 Water Cycle Animation**: Animate through all water states with visual transitions
- **🎯 Attention-Based Interactions**: Mouse movement creates resonance waves and focus effects
- **🎵 Harmonic Mapping**: Real-time harmonic theme updates based on resonance state
- **📊 Live Resonance Feedback**: Coherence score, water state, and harmonic theme display

### **Phase 3 Community & AI Features**
- **🌊 Community Resonance Overlays**: Visual rings showing collective tuning across users
- **🤖 AI Mirror Librarian**: Intelligent agent providing archetypal guidance and node expansion prompts
- **👥 Multi-Layer Resonance**: Personal, community, AI, and historical resonance layers
- **📝 Contribution System**: Community members can contribute insights and resonance to nodes
- **🌊 Community Waves**: Visual feedback when contributions create collective resonance
- **🔮 Archetypal Prompts**: AI-generated guidance for expanding nodes across scientific, symbolic, and water-state lenses
- **📊 Community Statistics**: Real-time display of active users, total contributions, and collective coherence
- **🎨 Enhanced UI**: AI agent panel, community contributions panel, and contribution modal

### **Phase 4 Federation & Storage Features**
- **🔗 Content-Addressed Storage**: SHA-256 hashed contributions with IPFS-like addressing
- **🌐 Enhanced Federation**: ActivityPub-compliant endpoints for cross-instance communication
- **📊 Storage Manifest System**: Comprehensive metadata tracking for contributions, nodes, and users
- **🔄 Cross-Instance Sync**: Export/import capabilities for federation between Living Codex instances
- **📡 Federation Discovery**: Peer discovery and synchronization endpoints
- **💾 Persistent Storage**: Local file-based storage with JSON manifest management
- **🔍 Contribution Retrieval**: Hash-based lookup, node-based queries, and user-based queries

## Fractal Growth
- Each module can be **re-implemented** in parallel languages (see `impls/`).
- Use Cursor prompts (below) to expand nodes, add edges, generate shaders, or author appendices.

## Cursor Prompts
- *"Expand NODE into three subnodes across scientific, symbolic, and water-state lenses; add edges with justifications."*
- *"Generate a JSON-LD schema extension for Axis and ResonanceState; validate `ontology/seed.json`."*
- *"Add tone-reactive edge shaders to the viz; map Trust to a perfect fifth, Fear to a tritone."*
- *"Create ActivityPub endpoints for inbox/outbox with content-addressed attachments (IPFS placeholders)."*

---

## Phase 4 Validation

Run the validation script to ensure Phase 4 compliance:
```bash
python scripts/validate_phase4.py
```

## Next Steps (Phase 5)

The repository is now ready for Phase 5 enhancements:
- **Multi-Implementation**: Parallel implementations in different languages and frameworks
- **Immersive Experience**: VR/AR exploration, haptic feedback, spatial computing
- **Advanced AI Integration**: Machine learning resonance patterns, predictive insights
- **Quantum Resonance**: Quantum computing integration for advanced resonance calculations

## Cursor Prompts for Phase 5
- *"Implement multi-language parallel versions of the Living Codex (Python, Rust, Go)"*
- *"Create VR/AR immersive experience for spatial exploration of the Living Codex"*
- *"Add haptic feedback and spatial audio for multi-sensory resonance experience"*
- *"Integrate quantum computing for advanced resonance pattern analysis and quantum entanglement visualization"*

---

## Run Latest System (Integrated Iteration)

This repository now includes a fully integrated, living system implementation. To run the latest iteration:

```bash
cd prototypes/federation-python
python3 -m venv venv && source venv/bin/activate
pip install -r requirements_federated.txt

# Start the Federated API (port 8001)
python3 federated_meta_api.py

# In another terminal, validate end-to-end
python3 test_federated_system.py

# Create living documents from code/docs
python3 living_document_system.py

# Integrated overview (API + Living Docs + Codex)
python3 integrated_living_system.py
```

See:
- `prototypes/federation-python/HISTORY_SUMMARY.md` (collapsed history)
- `prototypes/federation-python/COMPLETE_LIVING_SYSTEM_SUMMARY.md` (final summary)