# ⚡ **Quick Reference - Living Codex**

## 🏗️ **System Architecture**

### **Core Components**
- **Neo4j Integration**: Graph database operations
- **Database Persistence**: SQLite/PostgreSQL storage
- **External API**: Google, Wikipedia, OpenAI integration
- **Configuration**: Centralized environment management

### **Modular Structure**
```
src/
├── config/          # Configuration management
├── api/            # External API integrations
├── database/       # Database operations
├── graph/          # Graph database operations
├── testing/        # Testing framework
└── examples/       # Usage examples
```

---

## 🔌 **Quick API Reference**

### **Neo4j System**
```python
from neo4j_integration_system import Neo4jIntegrationSystem

neo4j = Neo4jIntegrationSystem()
connected = neo4j.is_connected()
result = neo4j.create_node(node_data)
query_result = neo4j.query_graph("MATCH (n) RETURN n LIMIT 10")
```

### **Database System**
```python
from database_persistence_system import DatabasePersistenceSystem
from src.database.core.models import DatabaseNode

db = DatabasePersistenceSystem(db_path="my_db.db")
result = db.create_node(node)
node = db.read_node("node_id")
```

### **External API System**
```python
import asyncio
from real_external_api_system import RealExternalAPISystem

async def search():
    api = RealExternalAPISystem()
    result = await api.search_google("query")
    await api.close()

asyncio.run(search())
```

---

## 💧 **Water States Quick Guide**

- **🧊 Ice (Structure)**: Frozen, stable, immutable (grammar, rules, schemas)
- **💧 Water (Flow)**: Dynamic, flowing, transforming (processes, pipelines)
- **🌫️ Vapor (Content)**: Living, evolving, breathing (instances, content)

---

## ⚡ **Energy System**

### **Transformation Costs**
- `ice_to_water`: 50 energy (melting)
- `water_to_vapor`: 100 energy (evaporation)
- `node_creation`: 10 energy
- `node_modification`: 5 energy
- `query_execution`: 1 energy

---

## 🔧 **Environment Variables**

```bash
# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password

# APIs
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GOOGLE_CSE_ID=your_cse_id

# Database
SQLITE_DB_PATH=living_codex.db
```

---

## 🧪 **Testing Commands**

```bash
# Run all tests
python test_phase5_cleanup.py

# Test components
python -c "from src.config.manager import ConfigManager; print('✅ Working')"

# Test integration
python test_phase4_integration.py
```

---

## 🚨 **Common Issues**

### **Import Errors**
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
```

### **Database Issues**
- Check file permissions
- Ensure directory exists
- Verify write access

### **API Key Issues**
- Check .env file format
- Verify environment variables
- No spaces around = sign

---

## 📚 **Key Documentation**

- **[Complete Overview](../overview/COMPLETE_SYSTEM_DOCUMENTATION.md)**
- **[Architecture Guide](../architecture/DEVELOPER_ARCHITECTURE_GUIDE.md)**
- **[API Documentation](../api/API_DOCUMENTATION.md)**
- **[Training Materials](../training/TRAINING_MATERIALS.md)**
- **[Setup Guide](../guides/COMPREHENSIVE_SETUP_AND_TESTING_GUIDE.md)**

---

*Quick reference for the Living Codex system. For detailed information, see the full documentation.*
