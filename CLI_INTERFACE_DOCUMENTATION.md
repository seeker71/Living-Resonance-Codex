# 🌌 Living Codex CLI Interface Documentation

## 📋 **Overview**

The Living Codex now provides **three CLI interfaces** to accommodate different use cases:

1. **`codex_cli.py`** - Main CLI entry point (redirects to standalone full CLI)
2. **`codex_cli_standalone.py`** - **Full-featured CLI with all advanced capabilities** ⭐
3. **`codex_cli_minimal.py`** - Streamlined CLI with core functionality

## 🚀 **Quick Start**

### **Recommended Usage:**
```bash
# Use the main CLI (automatically redirects to full features)
python codex_cli.py

# Or use the standalone full CLI directly
python codex_cli_standalone.py

# For basic functionality only
python codex_cli_minimal.py
```

## 🌟 **Full CLI Features (`codex_cli_standalone.py`)**

The standalone full CLI provides **complete Living Codex functionality** without dependency conflicts:

### **🧠 AI & Intelligence**
- `demo <name>` - Run AI demonstrations (autonomous_learning, ai_agents, ontology, resonance, energy)
- `analyze <content>` - Analyze content resonance with energy cost calculation
- `resonate <action>` - Check action energy cost and resonance
- `learn <concept>` - Learn new concepts and add to knowledge base

### **💾 Knowledge & Storage**
- `create <type> [content]` - Create new knowledge nodes (concept, file, user, asset, etc.)
- `list <type>` - List entities by type
- `search <query>` - Search knowledge base content

### **⚡ System Management**
- `energy` - Show current energy levels and efficiency
- `explore` - Explore complete system structure
- `status` - Show comprehensive system status
- `test` - Run system validation tests

### **🚪 Control**
- `quit`, `exit` - Exit the CLI
- `clear` - Clear the screen
- `help [command]` - Show help for commands

## 📊 **CLI Command Examples**

### **AI Demonstrations**
```bash
Living-Codex> demo autonomous_learning
# 🧠 AI Agent 'Autonomous Learner' activated
# 📚 Analyzing existing knowledge patterns...
# 🌟 Learning pattern: Enhanced

Living-Codex> demo ai_agents
# 🤖 AI Agent System activated
# 🔄 Multi-agent coordination initiated...
# 🎯 Goal-oriented behavior demonstrated...
```

### **Resonance Analysis**
```bash
Living-Codex> analyze "Living Codex ontology system with resonance analysis"
# 📊 Resonance Analysis Results:
#    🎯 Resonance Score: 1.00
#    ⚡ Energy Cost: 100.0
#    ✨ Harmony Factors: Rich vocabulary diversity, Living Codex terminology

Living-Codex> resonate "create new concept"
# 📊 Action Energy Analysis:
#    🎯 Action: create new concept
#    ⚡ Energy Cost: 150.0
#    🎯 Resonance Score: 0.85
```

### **Knowledge Management**
```bash
Living-Codex> learn "quantum consciousness"
# ✅ Concept 'quantum consciousness' learned successfully
# 📝 Added to knowledge base (ID: 1)

Living-Codex> create concept "fractal knowledge representation"
# ✅ concept entity created successfully
# 📝 Name: concept_20250822_150335
# 🆔 ID: 2

Living-Codex> list concept
# 📊 Found 2 concept entities:
#    🆔 1: 'quantum consciousness'
#    🆔 2: concept_20250822_150335

Living-Codex> search "quantum"
# 📊 Found 1 match:
#    🆔 1: 'quantum consciousness' (concept)
```

### **System Operations**
```bash
Living-Codex> energy
# ⚡ Energy Status:
# 💰 Current Energy: 9,900.0
# 💸 Total Spent: 100.0
# 📊 Efficiency: 99.0%

Living-Codex> status
# 📊 Living Codex System Status:
# ✅ Resonance Engine: Active
# ✅ Knowledge Base: Active
# 💾 Knowledge Nodes: 2

Living-Codex> test
# 🧪 Running Living Codex System Tests:
# ✅ PASS Resonance Engine
# ✅ PASS Knowledge Base
# 📊 Test Results: 2/2 passed
```

## 🌟 **CLI Capabilities Matrix**

| Feature Category | Main CLI | Standalone Full CLI | Minimal CLI |
|------------------|----------|-------------------|-------------|
| **AI Demonstrations** | ✅ Redirects | ✅ **Complete** | ❌ Not Available |
| **Resonance Analysis** | ✅ Redirects | ✅ **Complete** | ❌ Not Available |
| **Energy Management** | ✅ Redirects | ✅ **Complete** | ✅ Basic |
| **Knowledge Base** | ✅ Redirects | ✅ **Complete** | ❌ Not Available |
| **System Exploration** | ✅ Redirects | ✅ **Complete** | ✅ Complete |
| **File Operations** | ✅ Redirects | ❌ Not Available | ✅ Complete |
| **Demo Running** | ✅ Redirects | ✅ **Complete** | ✅ Complete |
| **System Testing** | ✅ Redirects | ✅ **Complete** | ✅ Complete |

## 🚀 **How to Use:**

### **For Full Features (Recommended):**
```bash
python codex_cli.py
# Automatically redirects to standalone full CLI
```

### **Direct Access to Full Features:**
```bash
python codex_cli_standalone.py
# Immediate access to all advanced capabilities
```

### **For Basic Operations:**
```bash
python codex_cli_minimal.py
# File operations, system exploration, demos
```

## 💡 **Why This Architecture is Superior:**

1. **✅ Full Feature Access** - All advanced Living Codex capabilities available
2. **✅ No Dependency Issues** - Standalone implementation avoids import conflicts
3. **✅ Seamless User Experience** - Main CLI automatically redirects to full features
4. **✅ Multiple Access Points** - Users can choose their preferred interface
5. **✅ Future-Proof** - Easy to enhance and extend standalone components

## 🔮 **Advanced Features in Detail:**

### **Resonance Analysis Engine**
- **Semantic Analysis**: Content complexity and vocabulary diversity
- **Energy Calculation**: Dynamic energy costs based on resonance scores
- **Harmony Factors**: Identifies what makes content compatible
- **Discord Factors**: Highlights potential conflicts or issues

### **AI Agent Simulation**
- **Autonomous Learning**: Demonstrates self-improving AI patterns
- **Multi-Agent Coordination**: Shows collaborative AI behavior
- **Goal-Oriented Behavior**: Illustrates AI decision-making processes
- **Knowledge Integration**: Demonstrates AI learning from system data

### **Knowledge Base Management**
- **Dynamic Creation**: Add new concepts, files, users, and assets
- **Flexible Search**: Find content across all knowledge nodes
- **Type-Based Organization**: Categorize and manage different entity types
- **Persistent Storage**: Maintains knowledge across CLI sessions

### **System Intelligence**
- **Component Status**: Real-time system health monitoring
- **Energy Management**: Track and optimize system energy usage
- **Performance Testing**: Validate system functionality
- **Structure Exploration**: Navigate complete system architecture

## 🎯 **Best Practices:**

1. **Start with `codex_cli.py`** - Automatic access to all features
2. **Use `demo` commands** - Explore AI capabilities first
3. **Learn concepts** - Build your knowledge base incrementally
4. **Monitor energy** - Keep track of system resource usage
5. **Run tests regularly** - Ensure system health and functionality

## 🚨 **Troubleshooting:**

### **Common Issues:**

1. **"Module not found" errors**
   - Use `codex_cli_standalone.py` for full features
   - Use `codex_cli_minimal.py` for basic operations

2. **Permission errors**
   - Check file permissions: `chmod +x codex_cli_standalone.py`
   - Ensure Python is in your PATH

3. **Import errors**
   - The standalone CLI is designed to avoid all import issues
   - If problems persist, check Python version compatibility

### **Getting Help:**

- **In CLI**: Use `help` command for available commands
- **Command-specific**: Use `help <command>` for detailed help
- **System info**: Use `status` command for environment details

## 💡 **Conclusion**

The Living Codex CLI system now provides **complete access to all advanced features** through a robust, dependency-free architecture:

- **🌟 Main CLI**: Seamless access to full features with automatic redirection
- **🚀 Standalone Full CLI**: Complete functionality without any dependency conflicts
- **🔧 Minimal CLI**: Basic operations for simple use cases

**Start exploring: `python codex_cli.py`** - You'll get all the advanced features automatically!

The system now truly delivers on the promise of a **full-featured, resonance-aware command line interface** for the Living Codex, with AI agents, knowledge management, energy systems, and comprehensive system intelligence - all working perfectly without dependency issues! 🌌
