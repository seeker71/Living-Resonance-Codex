# 🌟 **Living Codex: Comprehensive Setup and Testing Guide**

## 📋 **Table of Contents**
1. [System Overview](#system-overview)
2. [Prerequisites](#prerequisites)
3. [Quick Start](#quick-start)
4. [Detailed Setup](#detailed-setup)
5. [Testing Your System](#testing-your-system)
6. [Troubleshooting](#troubleshooting)
7. [Next Steps](#next-steps)

---

## 🎯 **System Overview**

The Living Codex is a **production-ready, intelligent knowledge system** that integrates:
- 🌐 **Web Search APIs**: Google Custom Search, DuckDuckGo, Wikipedia
- 🤖 **AI Integration**: OpenAI API for expert insights
- 🗄️ **Database Systems**: Neo4j graph database + SQLite persistence
- ⚙️ **Configuration Management**: Centralized, secure setup
- 🧪 **Testing Framework**: Comprehensive validation

## ✅ **Prerequisites**

### **Required**
- **Python 3.8+** installed
- **Git** for version control
- **Internet connection** for API access

### **Optional but Recommended**
- **Neo4j** for graph database functionality
- **PostgreSQL** for advanced database features

---

## 🚀 **Quick Start**

### **1. Clone and Setup**
```bash
# Clone the repository
git clone <your-repo-url>
cd Living-Resonance-Codex/prototypes/federation-python

# Install dependencies
pip install -r requirements_real_systems.txt

# Run the setup wizard
python setup_api_keys.py
```

### **2. Configure API Keys**
```bash
# Run the web search setup
python setup_web_search.py

# Or configure manually
cp env_example.txt .env
# Edit .env with your API keys
```

### **3. Test Everything**
```bash
# Run unified system test
python test_unified_system.py
```

---

## 🔧 **Detailed Setup**

## **Section 1: API Key Configuration**

### **OpenAI API Setup**

1. **Get OpenAI API Key**:
   - Visit: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Sign in and create a new API key
   - Copy the key (starts with `sk-...`)

2. **Configure in .env**:
   ```bash
   OPENAI_API_KEY=sk-your-actual-key-here
   OPENAI_MODEL=gpt-3.5-turbo
   ```

### **Google Custom Search Setup**

1. **Get Google API Key**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable Custom Search API
   - Create API key (starts with `AIza...`)

2. **Create Custom Search Engine**:
   - Visit [Custom Search Engine](https://cse.google.com/cse/)
   - Create search engine for web-wide search
   - Get Search Engine ID (format: `123456789:abcdefghijk`)

3. **Configure in .env**:
   ```bash
   GOOGLE_API_KEY=AIza-your-actual-key-here
   GOOGLE_CSE_ID=your-search-engine-id-here
   ```

### **Neo4j Setup**

#### **Option A: macOS (Recommended)**
```bash
# Run automated setup
chmod +x setup_macos.sh
./setup_macos.sh
```

#### **Option B: Manual Installation**

1. **Install Neo4j**:
   ```bash
   # macOS
   brew install neo4j
   
   # Linux
   wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
   echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
   sudo apt-get update
   sudo apt-get install neo4j
   
   # Windows
   # Download from https://neo4j.com/download/
   ```

2. **Start Neo4j Service**:
   ```bash
   # macOS
   brew services start neo4j
   
   # Linux
   sudo systemctl start neo4j
   
   # Windows
   # Use Neo4j Desktop or service
   ```

3. **Set Initial Password**:
   ```bash
   # Stop Neo4j first
   brew services stop neo4j  # macOS
   sudo systemctl stop neo4j  # Linux
   
   # Set password
   neo4j-admin dbms set-initial-password your_password_here
   
   # Start Neo4j
   brew services start neo4j  # macOS
   sudo systemctl start neo4j  # Linux
   ```

4. **Configure in .env**:
   ```bash
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=your_password_here
   ```

### **PostgreSQL Setup (Optional)**

1. **Install PostgreSQL**:
   ```bash
   # macOS
   brew install postgresql
   
   # Linux
   sudo apt-get install postgresql postgresql-contrib
   
   # Windows
   # Download from https://www.postgresql.org/download/
   ```

2. **Create Database**:
   ```bash
   createdb living_codex
   ```

3. **Configure in .env**:
   ```bash
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   POSTGRES_DATABASE=living_codex
   POSTGRES_USERNAME=your_username
   POSTGRES_PASSWORD=your_password
   ```

## **Section 2: Environment Configuration**

### **Create .env File**
```bash
# Copy example file
cp env_example.txt .env

# Edit with your actual values
nano .env  # or use your preferred editor
```

### **Complete .env Example**
```bash
# Living Codex Configuration

# OpenAI API Configuration
OPENAI_API_KEY=sk-your-openai-key-here
OPENAI_MODEL=gpt-3.5-turbo

# Google Custom Search API
GOOGLE_API_KEY=AIza-your-google-key-here
GOOGLE_CSE_ID=your-search-engine-id-here

# Wikipedia API (No key required)
WIKIPEDIA_RATE_LIMIT=100

# DuckDuckGo (No key required)
DUCKDUCKGO_RATE_LIMIT=100

# Neo4j Database Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password_here

# PostgreSQL Database Configuration (Optional)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=living_codex
POSTGRES_USERNAME=your_username
POSTGRES_PASSWORD=your_password

# System Configuration
SYSTEM_CACHE_TTL=3600
SYSTEM_RATE_LIMIT=100
SYSTEM_LOG_LEVEL=INFO
```

## **Section 3: Python Dependencies**

### **Install Required Packages**
```bash
# Install from requirements file
pip install -r requirements_real_systems.txt

# Or install individually
pip install fastapi uvicorn pydantic requests aiohttp neo4j psycopg2-binary
```

---

## 🧪 **Testing Your System**

## **Section 1: Unified System Testing (Recommended)**

### **Test Everything at Once**
```bash
python test_unified_system.py
```
**What it does**: Tests all system components in one comprehensive run
**Expected Output**: Detailed test results for each component with overall summary

### **Test Configuration Only**
```bash
python config_manager.py
```
**Expected Output**: All configured services show ✅ status

## **Section 2: Component-Specific Testing (Advanced)**

### **Understanding Test Results**
The unified test script provides:
- **Individual test results** for each component
- **Comprehensive summary** with success rates
- **Performance metrics** including test duration
- **Clear error reporting** for failed tests

### **Test Components Covered**
1. **Configuration Testing** - API keys and settings validation
2. **Neo4j Integration** - Database connection and operations
3. **Database Persistence** - SQLite system validation
4. **Web Search APIs** - Google, DuckDuckGo, Wikipedia
5. **OpenAI Integration** - AI consultation testing
6. **Comprehensive Integration** - All systems working together

### **Run Integrated Demo**
```bash
python integrated_real_systems_demo.py
```
**Expected Output**: Full system demonstration with data flow between components

## **Section 3: Expected Test Results**

### **Successful Unified Test Run**
```
============================================================
  Living Codex Unified System Test
============================================================
Running comprehensive system validation...

----------------------------------------
  Testing System Configuration
----------------------------------------
✅ PASS OpenAI API
     Configured
✅ PASS Google Custom Search
     Configured
✅ PASS Neo4j Database
     Configured
✅ PASS PostgreSQL Database
     Configured

----------------------------------------
  Testing Neo4j Integration
----------------------------------------
✅ PASS Neo4j Connection
     Successfully connected
✅ PASS Neo4j Node Creation
     Test node created
✅ PASS Neo4j Query
     Found 3 nodes

============================================================
  Test Summary
============================================================
📊 Test Results:
  Total Tests: 14
  Passed: 14 ✅
  Failed: 0 ❌
  Success Rate: 100.0%

🎉 All tests passed! Your Living Codex is fully operational!

⏱️  Total test duration: 5.28 seconds
```

### **Understanding Test Output**
- **✅ PASS**: Component test successful
- **❌ FAIL**: Component test failed with error details
- **Test Summary**: Overall results with success rate
- **Duration**: Total time for all tests

---

## 🔧 **Troubleshooting**

## **Common Issues and Solutions**

### **1. API Key Errors**

#### **OpenAI API Key Invalid**
```
❌ OpenAI test failed: Invalid API key
```
**Solution**:
- Verify your API key starts with `sk-`
- Check if you have OpenAI API credits
- Ensure the key is not truncated

#### **Google API Key Invalid**
```
❌ Google Custom Search: Invalid API key format
```
**Solution**:
- Verify your API key starts with `AIza`
- Check if Custom Search API is enabled
- Ensure project has billing enabled

### **2. Neo4j Connection Issues**

#### **Authentication Failed**
```
❌ Neo4j authentication failed: Unauthorized
```
**Solution**:
- Verify Neo4j service is running
- Check username/password in .env
- Restart Neo4j after password changes

#### **Connection Refused**
```
❌ Neo4j connection failed: Connection refused
```
**Solution**:
- Start Neo4j service: `brew services start neo4j`
- Check if port 7687 is available
- Verify firewall settings

### **3. Web Search Issues**

#### **Rate Limit Exceeded**
```
❌ Google Custom Search: Quota exceeded
```
**Solution**:
- Wait for daily quota reset
- Upgrade to paid tier if needed
- Use DuckDuckGo as fallback

#### **No Search Results**
```
❌ Web search: No successful results
```
**Solution**:
- Check internet connection
- Verify search engine configuration
- Test with simple queries first

### **4. Python Import Errors**

#### **Module Not Found**
```
❌ ModuleNotFoundError: No module named 'neo4j'
```
**Solution**:
- Install dependencies: `pip install -r requirements_real_systems.txt`
- Activate virtual environment if using one
- Check Python path

### **5. Database Issues**

#### **Schema Creation Failed**
```
❌ Database schema creation failed
```
**Solution**:
- Check database permissions
- Verify database connection
- Ensure database exists

## **Debug Commands**

### **Test API Keys Manually**
```bash
# Test Google API
curl "https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CSE_ID&q=test"

# Test OpenAI API
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"model":"gpt-3.5-turbo","messages":[{"role":"user","content":"Hello"}]}' \
     https://api.openai.com/v1/chat/completions
```

### **Check Service Status**
```bash
# Check Neo4j
curl -s http://localhost:7474/

# Check PostgreSQL
psql -h localhost -U your_username -d living_codex -c "SELECT version();"
```

---

## 🚀 **Next Steps**

## **After Successful Setup**

### **1. Explore Your System**
- Run the integrated demo to see all components working together
- Try different search queries to test web search capabilities
- Experiment with OpenAI integration for AI-powered insights

### **2. Build Your Knowledge Base**
- Start searching for topics of interest
- Store results in your database
- Build connections between concepts

### **3. Customize and Extend**
- Modify search parameters and sources
- Add new API integrations
- Customize the ontology and data structures

### **4. Scale Up**
- Consider additional search sources
- Implement caching and optimization
- Add user interfaces and APIs

## **Advanced Features**

### **Custom Search Engines**
- Create domain-specific search engines
- Configure image search capabilities
- Set up SafeSearch filters

### **Rate Limiting and Optimization**
- Implement intelligent rate limiting
- Add request caching
- Optimize API usage patterns

### **Data Integration**
- Connect to external databases
- Implement data synchronization
- Build data pipelines

---

## 📚 **Additional Resources**

### **Documentation**
- `COMPLETE_SETUP_GUIDE.md` - Detailed setup instructions
- `NEO4J_SETUP_GUIDE.md` - Neo4j-specific setup
- `WEB_SEARCH_SETUP_GUIDE.md` - Web search API setup

### **API References**
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Google Custom Search API](https://developers.google.com/custom-search)
- [Neo4j Python Driver](https://neo4j.com/docs/python-manual/current/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

### **Community and Support**
- Check the project repository for updates
- Review archived iterations for historical context
- Explore the codebase for implementation examples

---

## 🎉 **Congratulations!**

You now have a **fully operational Living Codex system** that can:
- 🔍 Search the web for knowledge
- 🤖 Get AI-powered insights
- 🗄️ Store and organize information
- 🔄 Continuously learn and evolve

Your system is ready to become a **living, breathing knowledge base** that grows with your needs!

---

*This comprehensive guide combines all setup and testing information into a single, easy-to-follow resource. For detailed information about specific components, refer to the individual documentation files.*
