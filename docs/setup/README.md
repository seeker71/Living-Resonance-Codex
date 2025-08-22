# 🛠️ **Setup and Configuration - Living Codex**

This directory contains all setup and configuration files for the Living Codex system.

## 📁 **Files in this Directory**

### **Setup Scripts**
- **`setup_api_keys.py`** - Interactive API key configuration
- **`setup_web_search.py`** - Web search API setup
- **`setup_macos.sh`** - macOS-specific setup (Neo4j)

### **Configuration**
- **`env_example.txt`** - Template for environment variables

## 🚀 **Quick Setup**

### **1. Basic Setup**
```bash
# Copy environment template
cp docs/setup/env_example.txt .env

# Edit with your configuration
nano .env  # or your preferred editor
```

### **2. API Key Setup**
```bash
# Interactive setup
python docs/setup/setup_api_keys.py

# Web search specific setup
python docs/setup/setup_web_search.py
```

### **3. macOS Neo4j Setup**
```bash
# Run macOS setup script
bash docs/setup/setup_macos.sh
```

## 🔧 **Environment Variables**

Your `.env` file should contain:

```bash
# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password

# API Keys
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GOOGLE_CSE_ID=your_custom_search_engine_id

# Database Configuration
SQLITE_DB_PATH=living_codex.db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=living_codex
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
```

## 📚 **Additional Resources**

- **[Comprehensive Setup Guide](../guides/COMPREHENSIVE_SETUP_AND_TESTING_GUIDE.md)** - Detailed setup instructions
- **[Quick Start Guide](../development/QUICK_START.md)** - Get running in 5 minutes
- **[System Documentation](../overview/COMPLETE_SYSTEM_DOCUMENTATION.md)** - Complete system overview

## 🚨 **Troubleshooting**

### **Common Issues**
- **Permission errors**: Ensure write access to current directory
- **API key errors**: Check `.env` file format (no spaces around `=`)
- **Neo4j connection**: Verify Neo4j is running and credentials are correct

### **Getting Help**
- Check the [troubleshooting guide](../training/TRAINING_MATERIALS.md#-troubleshooting-guide)
- Review the [comprehensive setup guide](../guides/COMPREHENSIVE_SETUP_AND_TESTING_GUIDE.md)

---

*Setup files organized for the Living Codex system. Follow the guides for detailed instructions.*
