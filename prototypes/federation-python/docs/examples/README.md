# 🌟 **Examples - Living Codex**

This directory contains practical examples and demonstrations of the Living Codex system.

## 📁 **Files in this Directory**

### **Complete System Examples**
- **`integrated_real_systems_demo.py`** - Comprehensive demonstration of all three systems working together

## 🚀 **Running Examples**

### **Integrated Systems Demo**
```bash
# Run the complete systems demonstration
python docs/examples/integrated_real_systems_demo.py
```

This demo showcases:
- ✅ External API integration (Google, Wikipedia, OpenAI)
- ✅ Database persistence operations
- ✅ Neo4j graph database integration
- ✅ Knowledge node creation and querying
- ✅ Energy management and transformation costs
- ✅ System interoperability

## 📚 **Example Categories**

### **1. Basic Operations**
```python
# Creating a knowledge node
from src.database.core.models import DatabaseNode
from datetime import datetime

node = DatabaseNode(
    node_id="example_node",
    node_type="example",
    name="Example Knowledge",
    content="This is an example of creating knowledge nodes",
    realm="examples",
    water_state="liquid",
    energy_level=100.0,
    transformation_cost=10.0,
    metadata={"category": "tutorial"},
    created_at=datetime.now(),
    updated_at=datetime.now()
)
```

### **2. System Integration**
```python
# Using all systems together
from neo4j_integration_system import Neo4jIntegrationSystem
from database_persistence_system import DatabasePersistenceSystem
from real_external_api_system import RealExternalAPISystem

# Initialize systems
neo4j = Neo4jIntegrationSystem()
database = DatabasePersistenceSystem()
api = RealExternalAPISystem()

# Create, store, and connect knowledge
# ... (see integrated_real_systems_demo.py for full example)
```

### **3. External Knowledge Integration**
```python
import asyncio

async def search_and_integrate():
    api_system = RealExternalAPISystem()
    
    try:
        # Search external sources
        wiki_result = await api_system.search_wikipedia("fractal systems")
        google_result = await api_system.search_google("knowledge management")
        
        # Process and integrate results
        # ... (see demo for processing logic)
        
    finally:
        await api_system.close()

asyncio.run(search_and_integrate())
```

## 🎯 **Learning Path**

### **For Beginners**
1. **Read the code** in `integrated_real_systems_demo.py`
2. **Run the demo** to see the system in action
3. **Modify parameters** to experiment with different configurations
4. **Create your own** simple examples based on the patterns

### **For Intermediate Users**
1. **Study the integration patterns** between systems
2. **Experiment with different** water states and energy levels
3. **Add new functionality** to the existing demo
4. **Create domain-specific** examples for your use case

### **For Advanced Users**
1. **Extend the demo** with new capabilities
2. **Integrate additional** external systems
3. **Optimize performance** and energy usage
4. **Create production-ready** applications

## 🔧 **Example Structure**

### **Typical Example File Structure**
```python
#!/usr/bin/env python3
"""
Example: Description of what this example demonstrates
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import required systems
from neo4j_integration_system import Neo4jIntegrationSystem
from database_persistence_system import DatabasePersistenceSystem
from real_external_api_system import RealExternalAPISystem

def demonstrate_feature():
    """Demonstrate a specific feature or capability"""
    print("🌟 Demonstrating Feature...")
    
    # Example implementation
    # ...
    
    print("✅ Demonstration complete!")

async def demonstrate_async_feature():
    """Demonstrate async capabilities"""
    print("⚡ Demonstrating Async Feature...")
    
    # Async example implementation
    # ...
    
    print("✅ Async demonstration complete!")

if __name__ == "__main__":
    # Run demonstrations
    demonstrate_feature()
    
    # Run async demonstrations
    import asyncio
    asyncio.run(demonstrate_async_feature())
```

## 🌟 **Featured Examples**

### **Integrated Real Systems Demo**
**File**: `integrated_real_systems_demo.py`

**What it demonstrates**:
- Complete system initialization and configuration
- Knowledge node creation with fractal properties
- External API integration and data retrieval
- Database persistence and querying
- Graph database operations and relationships
- Energy management and transformation costs
- Error handling and system resilience

**Key Features**:
- ✅ **Real API Integration** - Actually calls external services
- ✅ **Database Operations** - Creates and queries real data
- ✅ **Graph Relationships** - Builds knowledge graphs
- ✅ **Energy Tracking** - Monitors transformation costs
- ✅ **Comprehensive Logging** - Detailed operation reporting

## 🚨 **Running Examples Safely**

### **Prerequisites**
- Ensure your environment is set up (see [Setup Guide](../setup/README.md))
- Configure API keys for external services
- Have Neo4j running (optional but recommended)

### **Safety Notes**
- Examples may create test databases and files
- External API calls may count against your quotas
- Some examples require internet connectivity
- Neo4j examples require a running Neo4j instance

### **Cleanup**
Examples typically clean up after themselves, but you may want to:
```bash
# Remove test databases created by examples
rm -f *.db

# Check for any leftover files
ls -la
```

## 📊 **Example Outputs**

When you run the integrated demo, you should see output like:
```
🚀 Living Codex - Integrated Real Systems Demo
============================================================

🔧 System Initialization
✅ Using new modular API components
✅ Using new modular database components
✅ Using modular Neo4j components

📊 System Status Check
✅ External API System: 2 APIs configured
✅ Database System: SQLite configured
ℹ️  Neo4j System: Not connected (check configuration)

🧬 Knowledge Node Creation
✅ Created fractal knowledge node: fractal_knowledge_001
   Name: Fractal Systems Knowledge
   Energy Level: 100.0
   Water State: liquid
```

## 📚 **Additional Resources**

### **Documentation**
- **[API Documentation](../api/API_DOCUMENTATION.md)** - API reference for building examples
- **[Architecture Guide](../architecture/DEVELOPER_ARCHITECTURE_GUIDE.md)** - Understanding system structure
- **[Training Materials](../training/TRAINING_MATERIALS.md)** - Learning exercises and tutorials

### **Related Examples**
- **`src/examples/`** - Additional modular examples
- **`docs/training/TRAINING_MATERIALS.md`** - Tutorial examples
- **Test files** in `docs/testing/` for testing patterns

## 🎯 **Creating Your Own Examples**

### **Example Ideas**
1. **Personal Knowledge Base** - Organize your learning and interests
2. **Research Assistant** - Integrate external sources for research
3. **Decision Support System** - Model decision-making processes
4. **Learning Path Generator** - Create personalized learning sequences
5. **Knowledge Recommender** - Suggest related topics and resources

### **Best Practices**
1. **Start simple** and build complexity gradually
2. **Include error handling** for robust examples
3. **Clean up resources** when done
4. **Document your examples** clearly
5. **Share interesting patterns** with the community

---

*Practical examples for learning and using the Living Codex system. Start with the integrated demo and build from there!*
