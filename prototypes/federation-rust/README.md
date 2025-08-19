# Living Codex Phase 6 - Rust Fractal Federation Server

## Overview

This is the Rust implementation of the Living Codex fractal federation server, representing **Phase 6: Multi-Implementation & Advanced AI Integration**. It provides high-performance, memory-safe fractal expansion capabilities while maintaining full compatibility with Phase 4 federation standards.

## Features

### 🌊 **Phase 4 Compatibility**
- **Content-Addressed Storage**: SHA-256 hashing for contributions
- **ActivityPub Compliance**: Full inbox/outbox support with Create activities
- **Federation Endpoints**: Peers, sync, webfinger, actor
- **Storage Management**: Manifest system with statistics

### 🚀 **Phase 6 Multi-Implementation**
- **High Performance**: Rust's zero-cost abstractions and async/await
- **Memory Safety**: Guaranteed thread safety with Arc<RwLock<>>
- **Fractal Expansion**: 12 base nodes → 108 fractal subnodes
- **Multi-Dimensional Contexts**: scientific, symbolic, water-state

## Architecture

```
src/
├── main.rs          # Server entry point and routing
├── models.rs        # Data structures (FractalNode, Contribution, etc.)
└── storage.rs       # Fractal storage implementation
```

### Key Components

- **FractalNode**: Hierarchical structure with subnodes
- **Contribution**: Community input with fractal context
- **FractalStorage**: Async storage with content addressing
- **Axum Router**: High-performance HTTP routing

## Quick Start

### Prerequisites
- Rust 1.70+ with Cargo
- Network access for dependencies

### Build & Run
```bash
# Build the project
cargo build

# Run the server
cargo run
```

The server will start on `http://localhost:8789`

### Testing
```bash
# Run the comprehensive test suite
python test_rust_fractal.py
```

## API Endpoints

### Core Federation (Phase 4)
- `GET /` - Server information
- `GET /storage/stats` - Storage statistics
- `GET /contributions/{hash}` - Get contribution by hash
- `GET /contributions/node/{node_id}` - Node contributions
- `GET /contributions/user/{user_id}` - User contributions
- `POST /inbox` - ActivityPub inbox
- `GET /outbox` - ActivityPub outbox
- `GET /federation/peers` - Federation peers
- `GET /federation/sync` - Federation sync

### Fractal Expansion (Phase 6)
- `GET /fractal/expand/{node_id}` - Complete node expansion
- `GET /fractal/nodes/{node_id}` - Detailed node information
- `GET /fractal/subnodes/{node_id}` - All subnodes of a base node
- `GET /fractal/context/{context}` - Nodes by fractal context
- `GET /fractal/levels` - Fractal level information

### ActivityPub Compliance
- `GET /.well-known/webfinger` - WebFinger discovery
- `GET /actor` - Actor information

## Fractal Structure

### Base Nodes (Level 1)
12 core ontological concepts:
- **Void** (Plasma) - Infinite potential
- **Field** (Vapor) - Information connectivity
- **Pattern** (Structured) - Form and rhythm
- **Flow** (Liquid) - Movement and change
- **Coherence** (Crystalline) - Alignment and unity
- **Resonance** (Wave) - Vibration and harmony
- **Transformation** (Phase) - Evolution and metamorphosis
- **Integration** (Colloidal) - Unity and synthesis
- **Emergence** (Complex) - Novelty and creation
- **Wisdom** (Living) - Knowledge and insight
- **Consciousness** (Aware) - Awareness and presence
- **Breath** (Vapor) - Life and energy

### Fractal Subnodes (Level 2)
Each base node expands into 9 subnodes across 3 contexts:

#### Scientific Context
- **Empirical**: Direct observation and measurement
- **Theoretical**: Conceptual frameworks and models
- **Experimental**: Systematic investigation and testing

#### Symbolic Context
- **Archetypal**: Universal patterns and meanings
- **Cultural**: Shared beliefs and practices
- **Personal**: Individual experience and interpretation

#### Water-State Context
- **Phase**: State transitions and transformations
- **Flow**: Dynamic movement and change
- **Coherence**: Pattern formation and stability

## Performance Characteristics

- **Startup Time**: <2 seconds
- **Memory Usage**: Efficient with Arc<RwLock<>>
- **Concurrency**: Async/await with Tokio runtime
- **Storage**: In-memory with optional persistence
- **API Response**: Sub-100ms for most endpoints

## Federation Integration

The Rust server integrates with the existing federation network:

- **Node.js Server** (Port 8787): Phase 4 compatibility
- **Python Server** (Port 8788): Phase 5 fractal expansion
- **Rust Server** (Port 8789): Phase 6 multi-implementation

All servers maintain full interoperability through shared ActivityPub standards.

## Development

### Adding New Fractal Contexts
1. Extend the `contexts` vector in `storage.rs`
2. Add context-specific logic in `expand_node_fractally()`
3. Update the fractal expansion response handling

### Extending Node Types
1. Add new fields to `FractalNode` in `models.rs`
2. Update the initialization logic in `storage.rs`
3. Modify the API response formatting

### Performance Optimization
- Use `Arc<Mutex<>>` for single-writer scenarios
- Implement connection pooling for external services
- Add metrics collection with Prometheus integration

## Testing

The test suite validates:
- ✅ Phase 4 compatibility (federation, storage, ActivityPub)
- ✅ Phase 6 features (fractal expansion, multi-implementation)
- ✅ Performance characteristics (startup time, response latency)
- ✅ Error handling and edge cases
- ✅ Federation peer integration

## Next Steps

This Rust implementation establishes the foundation for:
- **Go Implementation**: Additional language support
- **Advanced AI Integration**: Neural network integration
- **Quantum Resonance**: Quantum computing interfaces
- **Immersive Experiences**: VR/AR and haptic feedback

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement with Rust best practices
4. Add comprehensive tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

---

**Living Codex Phase 6** - Expanding consciousness through multi-implementation fractal wisdom.

