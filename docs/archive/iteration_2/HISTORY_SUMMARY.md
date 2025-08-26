# Living Codex – Collapsed History (to Latest Iteration)

This document compresses the evolution into essentials required to understand and run the latest system.

## 1) Origins → Requirements
- Cross-platform setup (macOS installer); validated FastAPI services run (fractal + graph prototypes).
- Simplify data: “everything is a node”, links-as-nodes, water-state metaphor (frozen/meta, liquid/instance, vapor/link).
- Add symbols (numeric), names (words), meta-node, bag-of-links; chars/words/sentences also nodes.
- Minimal bootstrap set (16 nodes) to represent any concept/program/lang.
- Map Living Codex (water states, chakras, frequencies, planets) onto the node system.
- Make the system meta-circular/self-describing; introspective; able to evolve via questions.

## 2) Key Architecture Milestones
- Recursive node design → bootstrap nodes (16) → Codex mapping (water/chakra/frequency) → meta-circular system → complete meta-codex integration.
- Federation-ready API with persistence + curiosity engine (self-evolution).
- Frequency harmony and symbol resonance analyzers.
- Living Document System: source/docs become living, analyzed, versioned, and related.
- Integrated Living System: ties API + Living Documents + Living Codex together.

## 3) Final Artifacts (Latest Iteration)
- API: `federated_meta_api.py` (FastAPI, curiosity system, harmonies, resonances, persistence)
- Tests: `test_federated_system.py` (end-to-end API checks)
- Codex Core: `complete_meta_codex.py` (meta foundation + bootstrap + codex mapping)
- Living Docs: `living_document_system.py` (documents/code as living entities)
- Integration: `integrated_living_system.py` (API + Living Docs + Codex)
- Requirements: `requirements_federated.txt`
- DBs (runtime): `meta_codex.db`, `living_documents.db`

## 4) How to Run (Latest)
- Create venv, install deps: `pip install -r requirements_federated.txt`
- Start API: `python3 federated_meta_api.py` (default port 8001 in latest edits)
- Validate: `python3 test_federated_system.py`
- Make docs living: `python3 living_document_system.py`
- Integrated overview: `python3 integrated_living_system.py`

## 5) Core Concepts (Minimal Mental Model)
- Nodes are content-addressable; links are nodes; meta describes structure; symbols map to frequencies.
- Water states encode ontology states; chakras/frequencies provide harmonic structure.
- Curiosity engine asks/answers to evolve schema/knowledge.
- Living docs ensure source/docs evolve, relate, and self-document.

## 6) Fixes That Matter (Kept Only if Relevant)
- Python 3.13 compat (Pydantic v2, `.model_dump()`), venv usage, port conflicts handled.
- SQLite persistence schemas for nodes, curiosities, harmonies, symbol resonances, docs, relationships, evolution history.

## 7) What’s intentionally omitted now
- Earlier prototypes and intermediate drafts not needed to run or understand latest integrated system (see cleanup map).

— End of collapsed history —
