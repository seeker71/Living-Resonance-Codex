# Living Codex — Phase 2 Complete ✅

This is a **Phase 2 complete** implementation of the Living Codex - a federated, fractal knowledge system that integrates consciousness, archetypes, and resonance through water-state metaphors and harmonic principles, now with interactive sacred geometry and resonance dynamics.

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

## Phase 2 Implementation Status ✅

### **Core Components (Complete)**
- **`ontology/seed.json`** → Complete 12-node seed ontology with water-state mappings, archetypes, and harmonic representations
- **`ontology/schema.json`** → Full JSON-LD schema with all node types, relationships, and metadata
- **`prototypes/graph/loader.py`** → Enhanced Neo4j loader with all new properties and constraints
- **`prototypes/viz/`** → **NEW**: Interactive sacred geometry visualization with resonance dynamics
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

## Fractal Growth
- Each module can be **re-implemented** in parallel languages (see `impls/`).
- Use Cursor prompts (below) to expand nodes, add edges, generate shaders, or author appendices.

## Cursor Prompts
- *"Expand NODE into three subnodes across scientific, symbolic, and water-state lenses; add edges with justifications."*
- *"Generate a JSON-LD schema extension for Axis and ResonanceState; validate `ontology/seed.json`."*
- *"Add tone-reactive edge shaders to the viz; map Trust to a perfect fifth, Fear to a tritone."*
- *"Create ActivityPub endpoints for inbox/outbox with content-addressed attachments (IPFS placeholders)."*

---

## Phase 2 Validation

Run the validation script to ensure Phase 2 compliance:
```bash
python scripts/validate_phase2.py
```

## Next Steps (Phase 3)

The repository is now ready for Phase 3 enhancements:
- **Resonance Contributions**: Community overlays, provenance of tuning acts
- **AI Agent Integration**: Mirror-librarian prompts for node expansion
- **Federation Features**: Enhanced ActivityPub endpoints and federated sync
- **Multimodal Expression**: Sound engine, VR/AR exploration

## Cursor Prompts for Phase 3
- *"Implement community resonance overlays showing collective tuning across users"*
- *"Create AI agent prompts for expanding nodes with scientific, symbolic, and water-state lenses"*
- *"Add sound engine mapping axes to musical intervals and water states to timbres"*
- *"Enhance federation with content-addressed storage and cross-instance synchronization"*