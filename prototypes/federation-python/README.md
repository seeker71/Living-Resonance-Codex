# 🚀 Living Codex System

A **fractal, holographic knowledge management system** that represents all human knowledge through recursive, self-similar structures.

## 🌟 **Features**

- **Fractal Design**: Self-similar structures at all levels
- **Water State Metaphor**: Ice (structure), Water (flow), Vapor (content)
- **Energy as Currency**: Quantifiable costs for transformations
- **Modular Architecture**: Maintainable and extensible codebase
- **Multiple Storage Backends**: Neo4j, SQLite, PostgreSQL
- **External API Integration**: Google Search, DuckDuckGo, Wikipedia, OpenAI

## 🚀 **Quick Start**

### **Installation**
```bash
# Clone the repository
git clone <repository-url>
cd Living-Resonance-Codex/prototypes/federation-python

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp env_example.txt .env
# Edit .env with your API keys and database credentials
```

### **Basic Usage**
```python
from neo4j_integration_system import Neo4jIntegrationSystem
from database_persistence_system import DatabasePersistenceSystem
from real_external_api_system import RealExternalAPISystem

# Initialize systems
neo4j_system = Neo4jIntegrationSystem()
db_system = DatabasePersistenceSystem()
api_system = RealExternalAPISystem()

# Use the systems...
```

## 📚 **Documentation**

- **[Complete System Documentation](COMPLETE_SYSTEM_DOCUMENTATION.md)** - Comprehensive guide
- **[Setup and Testing Guide](COMPREHENSIVE_SETUP_AND_TESTING_GUIDE.md)** - Installation and testing

## 🧪 **Testing**

```bash
# Test system integration
python test_phase4_integration.py

# Test specific components
python -c "from src.config.manager import ConfigManager; print('✅ Config system working')"
```

## 🏗️ **Architecture**

The system uses a **hybrid architecture** that combines:
- **Modular Components** (`src/` directory) for core functionality
- **Legacy Systems** for backward compatibility
- **Seamless Integration** between old and new architectures

## 🔧 **Configuration**

Key environment variables:
- `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` - Neo4j database
- `OPENAI_API_KEY` - OpenAI API access
- `GOOGLE_API_KEY`, `GOOGLE_CSE_ID` - Google Custom Search
- `SQLITE_DB_PATH` - SQLite database path

## 🌟 **Core Principles**

1. **Fractal Nature**: Every part contains information about the whole
2. **Water States**: Knowledge exists in different states (ice, water, vapor)
3. **Energy Management**: Transformations have quantifiable costs
4. **Higher Dimensions**: Multi-dimensional knowledge representation

## 🚀 **Getting Help**

- Check the [troubleshooting section](COMPLETE_SYSTEM_DOCUMENTATION.md#-troubleshooting)
- Review the [source code](src/) and documentation
- Run the test suite to validate your environment

## 📄 **License**

This project is part of the Living Codex initiative.

---

*The Living Codex represents the future of knowledge management - a system that grows, evolves, and adapts while maintaining its core principles and functionality.*
