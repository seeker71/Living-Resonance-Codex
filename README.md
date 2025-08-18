# Living Codex — Prototype Scaffold

This is a minimal, **federated, fractal** scaffold to start building the Living Codex prototype.

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

## Structure
- `ontology/seed.json` → JSON-LD/RDF-like seed nodes, axes.
- `prototypes/graph/loader.py` → loads seed into Neo4j.
- `prototypes/viz/` → simple Flower-of-Life canvas; renders nodes with water-state colorways.
- `prototypes/resonance/score.py` → toy coherence metric from axes.
- `prototypes/federation/server.js` → minimal ActivityPub-style inbox/outbox skeleton.

## Fractal Growth
- Each module can be **re-implemented** in parallel languages (see `impls/`).
- Use Cursor prompts (below) to expand nodes, add edges, generate shaders, or author appendices.

## Cursor Prompts
- *“Expand NODE into three subnodes across scientific, symbolic, and water-state lenses; add edges with justifications.”*
- *“Generate a JSON-LD schema extension for Axis and ResonanceState; validate `ontology/seed.json`.”*
- *“Add tone-reactive edge shaders to the viz; map Trust to a perfect fifth, Fear to a tritone.”*
- *“Create ActivityPub endpoints for inbox/outbox with content-addressed attachments (IPFS placeholders).”*