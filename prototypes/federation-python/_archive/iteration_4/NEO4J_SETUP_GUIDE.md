# 🗄️ **Neo4j Setup Guide for Living Codex**

## 🌟 **Overview**

Neo4j is a powerful graph database that enhances the Living Codex with advanced graph operations, relationship mapping, and complex querying capabilities. This guide will help you install and configure Neo4j locally.

## 🚀 **Installation Options**

### **Option 1: Neo4j Desktop (Recommended for Development)**

#### **Step 1: Download Neo4j Desktop**
1. Go to [https://neo4j.com/download/](https://neo4j.com/download/)
2. Click "Download Neo4j Desktop"
3. Choose your operating system (Windows, macOS, or Linux)
4. Download and install the application

#### **Step 2: Create a New Database**
1. Open Neo4j Desktop
2. Click "Create" → "Create a Local Graph"
3. Choose "Neo4j 5.x" (latest stable version)
4. Set a name (e.g., "Living Codex")
5. Set a password (remember this!)
6. Click "Create"

#### **Step 3: Start the Database**
1. Click the "Start" button on your database
2. Wait for the database to start (green status)
3. Note the connection details:
   - **URI**: `bolt://localhost:7687`
   - **Username**: `neo4j`
   - **Password**: The password you set

### **Option 2: Docker Installation**

#### **Step 1: Install Docker**
1. Download Docker Desktop from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Install and start Docker Desktop

#### **Step 2: Run Neo4j Container**
```bash
docker run \
  --name neo4j-living-codex \
  -p 7474:7474 -p 7687:7687 \
  -d \
  -e NEO4J_AUTH=neo4j/your_password_here \
  -e NEO4J_PLUGINS='["apoc"]' \
  neo4j:5.15
```

#### **Step 3: Verify Installation**
```bash
# Check if container is running
docker ps

# Check logs
docker logs neo4j-living-codex

# Access Neo4j Browser
# Open http://localhost:7474 in your browser
```

### **Option 3: Package Manager Installation**

#### **macOS (using Homebrew)**
```bash
# Install Neo4j
brew install neo4j

# Start Neo4j service
brew services start neo4j

# Set password (first time only)
neo4j-admin set-initial-password your_password_here
```

#### **Ubuntu/Debian**
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

## 🔧 **Configuration**

### **Environment Variables**
Add these to your `.env` file:
```bash
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password_here
```

### **Connection Testing**
Test your Neo4j connection:
```bash
python -c "
from neo4j_integration_system import Neo4jIntegrationSystem
neo4j = Neo4jIntegrationSystem()
print('Connected:', neo4j.connection_manager.is_connected())
"
```

## 🌐 **Neo4j Browser Access**

### **Access the Browser**
1. Open your web browser
2. Go to `http://localhost:7474`
3. Login with:
   - **Username**: `neo4j`
   - **Password**: Your password

### **Test Basic Operations**
In the Neo4j Browser, try these Cypher queries:

#### **Create a Test Node**
```cypher
CREATE (n:TestNode {name: 'Living Codex Test', created: datetime()})
RETURN n
```

#### **View All Nodes**
```cypher
MATCH (n) RETURN n LIMIT 10
```

#### **View Node Labels**
```cypher
CALL db.labels() YIELD label RETURN label
```

## 🧪 **Integration Testing**

### **Test with Living Codex**
Run the integrated demo to test Neo4j integration:
```bash
python integrated_real_systems_demo.py
```

### **Expected Output**
You should see:
- ✅ Neo4j connection successful
- ✅ Graph operations working
- ✅ Real-time data synchronization

## 🔍 **Troubleshooting**

### **Common Issues**

#### **Connection Refused**
```bash
# Check if Neo4j is running
# On macOS/Linux:
ps aux | grep neo4j

# Check port availability
netstat -an | grep 7687
```

#### **Authentication Failed**
1. Reset password:
   ```bash
   # Stop Neo4j first
   sudo systemctl stop neo4j  # Linux
   brew services stop neo4j   # macOS
   
   # Reset password
   neo4j-admin set-initial-password new_password
   
   # Start Neo4j
   sudo systemctl start neo4j  # Linux
   brew services start neo4j   # macOS
   ```

#### **Port Already in Use**
```bash
# Find process using port 7687
lsof -i :7687

# Kill the process
kill -9 <PID>
```

### **Performance Optimization**

#### **Memory Settings**
Edit `neo4j.conf`:
```bash
# Increase memory for better performance
dbms.memory.heap.initial_size=2G
dbms.memory.heap.max_size=4G
dbms.memory.pagecache.size=2G
```

#### **Indexing**
Create indexes for better query performance:
```cypher
// Create index on node_id
CREATE INDEX node_id_index FOR (n:UnifiedNode) ON (n.node_id);

// Create index on node_type
CREATE INDEX node_type_index FOR (n:UnifiedNode) ON (n.node_type);
```

## 🚀 **Advanced Features**

### **APOC Procedures**
APOC provides additional graph algorithms and utilities:

#### **Install APOC**
1. Download APOC from [https://github.com/neo4j/apoc/releases](https://github.com/neo4j/apoc/releases)
2. Place the JAR file in Neo4j's plugins directory
3. Restart Neo4j

#### **Useful APOC Procedures**
```cypher
// Get database statistics
CALL apoc.monitor.kernel() YIELD *;

// Export graph to various formats
CALL apoc.export.json.all("export.json", {});

// Community detection
CALL apoc.algo.community("louvain", null, "weight");
```

## 📊 **Monitoring and Maintenance**

### **Database Statistics**
```cypher
// Get node count by label
MATCH (n) RETURN labels(n) as Label, count(n) as Count;

// Get relationship count by type
MATCH ()-[r]->() RETURN type(r) as Type, count(r) as Count;

// Get database size
CALL dbms.database.size() YIELD *;
```

### **Backup and Restore**
```bash
# Create backup
neo4j-admin backup --database=neo4j --to=/path/to/backup

# Restore from backup
neo4j-admin restore --database=neo4j --from=/path/to/backup
```

## 🎯 **Next Steps**

Once Neo4j is running:

1. **Test Integration**: Run the integrated demo
2. **Explore Graph**: Use Neo4j Browser to explore your data
3. **Optimize Queries**: Create indexes for better performance
4. **Scale Up**: Consider clustering for production use

## 🌟 **Benefits of Neo4j Integration**

- **Graph Operations**: Complex relationship queries
- **Real-time Sync**: Live data synchronization
- **Advanced Analytics**: Graph algorithms and analytics
- **Scalability**: Handle large-scale graph data
- **Visualization**: Built-in graph visualization tools

---

*This guide will get you up and running with Neo4j for the Living Codex system. Once configured, you'll have access to powerful graph database capabilities that enhance the system's knowledge representation and querying abilities.*
