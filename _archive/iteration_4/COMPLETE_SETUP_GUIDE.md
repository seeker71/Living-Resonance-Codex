# 🚀 **Complete Setup Guide for Living Codex**

## 🌟 **Overview**

This guide will walk you through setting up the Living Codex system with real API keys and Neo4j integration. By the end, you'll have a fully functional system that can:

- Connect to real external knowledge sources
- Store data in a real graph database
- Perform advanced graph operations
- Integrate with AI systems

## 📋 **Prerequisites**

- **Python 3.8+** installed
- **Git** for version control
- **macOS, Linux, or Windows** (setup instructions for all platforms)
- **Internet connection** for API access

## 🔑 **Step 1: API Key Setup**

### **OpenAI API Key (Required for AI Features)**

1. **Get Your API Key**:
   - Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Sign in or create an account
   - Click "Create new secret key"
   - Copy the key (starts with `sk-`)

2. **Set the Key**:
   ```bash
   export OPENAI_API_KEY="sk-your-key-here"
   ```

### **Google Custom Search (Optional)**

1. **Create Custom Search Engine**:
   - Go to [https://developers.google.com/custom-search](https://developers.google.com/custom-search)
   - Click "Get a Key"
   - Create a new project
   - Enable Custom Search API

2. **Create Search Engine**:
   - Go to [https://cse.google.com/cse/](https://cse.google.com/cse/)
   - Create a new search engine
   - Note your Search Engine ID

3. **Set the Keys**:
   ```bash
   export GOOGLE_API_KEY="your-google-api-key"
   export GOOGLE_CSE_ID="your-search-engine-id"
   ```

## 🗄️ **Step 2: Neo4j Setup**

### **Option A: macOS (Recommended)**

1. **Run the Setup Script**:
   ```bash
   ./setup_macos.sh
   ```

2. **Manual Installation** (if script fails):
   ```bash
   # Install Homebrew if not installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Neo4j
   brew install neo4j
   
   # Start Neo4j service
   brew services start neo4j
   
   # Set password (first time only)
   neo4j-admin set-initial-password your_password_here
   ```

### **Option B: Docker (Cross-platform)**

1. **Install Docker Desktop**:
   - Download from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
   - Install and start Docker

2. **Run Neo4j Container**:
   ```bash
   docker run \
     --name neo4j-living-codex \
     -p 7474:7474 -p 7687:7687 \
     -d \
     -e NEO4J_AUTH=neo4j/your_password_here \
     -e NEO4J_PLUGINS='["apoc"]' \
     neo4j:5.15
   ```

### **Option C: Linux (Ubuntu/Debian)**

```bash
# Add Neo4j repository
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable 5' | sudo tee /etc/apt/sources.list.d/neo4j.list

# Install Neo4j
sudo apt-get update
sudo apt-get install neo4j

# Start service
sudo systemctl start neo4j

# Set password
sudo neo4j-admin set-initial-password your_password_here
```

### **Option D: Windows**

1. **Download Neo4j Desktop**:
   - Go to [https://neo4j.com/download/](https://neo4j.com/download/)
   - Download Neo4j Desktop for Windows
   - Install the application

2. **Create Database**:
   - Open Neo4j Desktop
   - Click "Create" → "Create a Local Graph"
   - Choose "Neo4j 5.x"
   - Set name and password
   - Click "Create" then "Start"

## 🔧 **Step 3: Configuration Setup**

### **Automatic Setup (Recommended)**

1. **Run the Setup Wizard**:
   ```bash
   python setup_api_keys.py
   ```

2. **Follow the prompts**:
   - Enter your OpenAI API key
   - Enter your Google API key (optional)
   - Enter your Neo4j password
   - The wizard will create a `.env` file

### **Manual Setup**

1. **Create `.env` file**:
   ```bash
   cp env_example.txt .env
   ```

2. **Edit `.env` file**:
   ```bash
   # OpenAI API Configuration
   OPENAI_API_KEY=sk-your-openai-key-here
   OPENAI_MODEL=gpt-3.5-turbo
   
   # Google Custom Search API (Optional)
   GOOGLE_API_KEY=your-google-api-key-here
   GOOGLE_CSE_ID=your-custom-search-engine-id-here
   
   # Neo4j Database Configuration
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=your-neo4j-password-here
   
   # System Configuration
   SYSTEM_CACHE_TTL=3600
   SYSTEM_RATE_LIMIT=100
   SYSTEM_LOG_LEVEL=INFO
   ```

## 📦 **Step 4: Install Dependencies**

### **Install Python Packages**

```bash
# Install all required packages
pip install -r requirements_real_systems.txt

# Or install individually
pip install neo4j psycopg2-binary requests aiohttp pytest pytest-asyncio pytest-cov psutil
```

### **Verify Installation**

```bash
# Test Neo4j connection
python -c "
from neo4j_integration_system import Neo4jIntegrationSystem
neo4j = Neo4jIntegrationSystem()
print('Neo4j connected:', neo4j.connection_manager.is_connected())
"

# Test OpenAI connection
python -c "
from real_external_api_system import ExpertSystemIntegration
expert = ExpertSystemIntegration()
print('OpenAI ready')
"
```

## 🧪 **Step 5: Test the System**

### **Run Configuration Test**

```bash
# Test your configuration
python config_manager.py
```

### **Run Integrated Demo**

```bash
# Test the complete system
python integrated_real_systems_demo.py
```

### **Expected Output**

You should see:
- ✅ OpenAI integration ready
- ✅ Neo4j connection successful
- ✅ All systems working together
- ✅ Data flowing between components

## 🌐 **Step 6: Access Neo4j Browser**

### **Open Neo4j Browser**

1. **Open your web browser**
2. **Go to**: `http://localhost:7474`
3. **Login with**:
   - Username: `neo4j`
   - Password: Your password

### **Test Basic Operations**

```cypher
// Create a test node
CREATE (n:TestNode {name: 'Living Codex Test', created: datetime()})
RETURN n

// View all nodes
MATCH (n) RETURN n LIMIT 10

// View node labels
CALL db.labels() YIELD label RETURN label
```

## 🔍 **Troubleshooting**

### **Common Issues**

#### **Neo4j Connection Failed**

```bash
# Check if Neo4j is running
ps aux | grep neo4j

# Check port availability
netstat -an | grep 7687

# Restart Neo4j
brew services restart neo4j  # macOS
sudo systemctl restart neo4j  # Linux
```

#### **API Key Issues**

```bash
# Check environment variables
echo $OPENAI_API_KEY
echo $GOOGLE_API_KEY

# Reload .env file
source .env
```

#### **Python Import Errors**

```bash
# Reinstall dependencies
pip uninstall neo4j psycopg2-binary requests aiohttp
pip install -r requirements_real_systems.txt
```

### **Performance Issues**

#### **Neo4j Memory Settings**

Edit Neo4j configuration:
```bash
# macOS: /opt/homebrew/etc/neo4j/neo4j.conf
# Linux: /etc/neo4j/neo4j.conf

# Increase memory
dbms.memory.heap.initial_size=2G
dbms.memory.heap.max_size=4G
dbms.memory.pagecache.size=2G
```

#### **Create Indexes**

```cypher
// Create indexes for better performance
CREATE INDEX node_id_index FOR (n:UnifiedNode) ON (n.node_id);
CREATE INDEX node_type_index FOR (n:UnifiedNode) ON (n.node_type);
```

## 🚀 **Step 7: Advanced Configuration**

### **Enable APOC Procedures**

1. **Download APOC**:
   - Go to [https://github.com/neo4j/apoc/releases](https://github.com/neo4j/apoc/releases)
   - Download the latest JAR file

2. **Install APOC**:
   - Place JAR in Neo4j plugins directory
   - Restart Neo4j

3. **Test APOC**:
   ```cypher
   CALL apoc.help('apoc') YIELD * LIMIT 5;
   ```

### **Configure PostgreSQL (Optional)**

```bash
# Install PostgreSQL
brew install postgresql  # macOS
sudo apt-get install postgresql  # Ubuntu

# Start service
brew services start postgresql  # macOS
sudo systemctl start postgresql  # Ubuntu

# Create database
createdb living_codex

# Set environment variables
export POSTGRES_USERNAME=your_username
export POSTGRES_PASSWORD=your_password
```

## 📊 **Step 8: Monitor and Maintain**

### **System Status**

```bash
# Check Neo4j status
brew services list | grep neo4j  # macOS
sudo systemctl status neo4j  # Linux

# Check Python processes
ps aux | grep python

# Monitor system resources
htop  # or top
```

### **Database Maintenance**

```cypher
// Get database statistics
CALL apoc.monitor.kernel() YIELD *;

// Get node count by label
MATCH (n) RETURN labels(n) as Label, count(n) as Count;

// Get relationship count by type
MATCH ()-[r]->() RETURN type(r) as Type, count(r) as Count;
```

### **Backup and Restore**

```bash
# Create backup
neo4j-admin backup --database=neo4j --to=/path/to/backup

# Restore from backup
neo4j-admin restore --database=neo4j --from=/path/to/backup
```

## 🎯 **Next Steps**

Once everything is configured:

1. **Explore the System**:
   - Run various demos
   - Experiment with different queries
   - Explore the Neo4j Browser

2. **Extend Functionality**:
   - Add new knowledge sources
   - Create custom graph algorithms
   - Integrate with other systems

3. **Scale Up**:
   - Consider Neo4j clustering
   - Add load balancing
   - Implement monitoring and alerting

## 🌟 **Benefits of Full Setup**

With everything configured, you'll have:

- **Real External Knowledge**: Access to live web data
- **Advanced Graph Operations**: Complex relationship queries
- **AI Integration**: OpenAI-powered insights
- **Production Ready**: Enterprise-grade features
- **Scalable Architecture**: Ready for growth

## 🎉 **Congratulations!**

You now have a fully functional Living Codex system with:

- ✅ Real API integrations
- ✅ Graph database capabilities
- ✅ AI-powered features
- ✅ Production-ready architecture

**Happy exploring! 🌟**

---

*This guide covers all aspects of setting up the Living Codex system. If you encounter any issues, refer to the troubleshooting section or check the individual component guides.*
