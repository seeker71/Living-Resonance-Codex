# Living Codex — Phase 1 Complete ✅

This is a **Phase 1 complete** implementation of the Living Codex - a federated, fractal knowledge system that integrates consciousness, archetypes, and resonance through water-state metaphors and harmonic principles.

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

## Phase 1 Implementation Status ✅

### **Core Components (Complete)**
- **`ontology/seed.json`** → Complete 12-node seed ontology with water-state mappings, archetypes, and harmonic representations
- **`ontology/schema.json`** → Full JSON-LD schema with all node types, relationships, and metadata
- **`prototypes/graph/loader.py`** → Enhanced Neo4j loader with all new properties and constraints
- **`prototypes/viz/`** → Enhanced Three.js visualization with proper geometry positioning and scaling
- **`prototypes/resonance/score.py`** → Advanced resonance analysis with harmonic and water-state themes
- **`prototypes/federation/server.js`** → ActivityPub-style federation endpoints

### **Enhanced Features**
- **Water-State Metaphors**: All 12 water states mapped to consciousness principles
- **Harmonic Representations**: Musical intervals and ratios for each node
- **Sacred Geometry**: Proper positioning in Flower of Life pattern
- **Archetypal Correspondences**: Cross-cultural deity and principle mappings
- **Vibrational Axes**: 5 primary axes with scale labels and metaphors
- **Validation**: Phase 1 validation script to ensure compliance

## Fractal Growth
- Each module can be **re-implemented** in parallel languages (see `impls/`).
- Use Cursor prompts (below) to expand nodes, add edges, generate shaders, or author appendices.

## Cursor Prompts
- *"Expand NODE into three subnodes across scientific, symbolic, and water-state lenses; add edges with justifications."*
- *"Generate a JSON-LD schema extension for Axis and ResonanceState; validate `ontology/seed.json`."*
- *"Add tone-reactive edge shaders to the viz; map Trust to a perfect fifth, Fear to a tritone."*
- *"Create ActivityPub endpoints for inbox/outbox with content-addressed attachments (IPFS placeholders)."*

---

## Phase 1 Validation

Run the validation script to ensure Phase 1 compliance:
```bash
python scripts/validate_phase1.py
```

## Next Steps (Phase 2)

The repository is now ready for Phase 2 enhancements:
- **Enhanced Visual Prototype**: Sacred geometry overlays, water-state animations
- **Resonance Contributions**: Interactive axis sliders, community overlays
- **AI Agent Integration**: Mirror-librarian prompts for node expansion
- **Multimodal Expression**: Sound engine, VR/AR exploration

## Cursor Prompts for Phase 2
- *"Add sacred geometry overlays to the visualization; implement Metatron's Cube and Icositetragon Wheel"*
- *"Create interactive axis sliders that affect node resonance and visualization"*
- *"Implement AI agent prompts for expanding nodes across scientific, symbolic, and water-state lenses"*
- *"Add sound engine mapping axes to musical intervals and water states to timbres"*