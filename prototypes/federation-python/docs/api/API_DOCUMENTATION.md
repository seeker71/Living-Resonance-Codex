# 🔌 **API Documentation - Living Codex System**

## 📅 **Last Updated**: December 2024

## 🎯 **Purpose**
This document provides comprehensive API documentation for the Living Codex system, including all available endpoints, request/response formats, authentication, and usage examples.

---

## 🏗️ **API Architecture Overview**

### **System APIs**
The Living Codex system provides multiple API layers:

1. **Core System APIs** - Direct Python interfaces for system components
2. **Graph Database APIs** - Neo4j graph operations and queries
3. **Database APIs** - SQLite/PostgreSQL CRUD operations
4. **External API Integrations** - Google Search, DuckDuckGo, Wikipedia, OpenAI
5. **Configuration APIs** - System configuration and management

### **API Design Principles**
- **Consistent Response Format** - All APIs return standardized response objects
- **Error Handling** - Comprehensive error reporting and status codes
- **Async Support** - Non-blocking operations for I/O-bound tasks
- **Resource Management** - Automatic cleanup and connection management
- **Rate Limiting** - Built-in rate limiting for external APIs

---

## 🔌 **Core System APIs**

### **Neo4j Integration System API**

#### **Class**: `Neo4jIntegrationSystem`

#### **Constructor**
```python
Neo4jIntegrationSystem(
    uri: str = None,
    username: str = None,
    password: str = None
)
```

**Parameters**:
- `uri` (str, optional): Neo4j connection URI (default: from environment)
- `username` (str, optional): Neo4j username (default: from environment)
- `password` (str, optional): Neo4j password (default: from environment)

#### **Methods**

##### **`is_connected() -> bool`**
Check if the system is connected to Neo4j.

**Returns**: `bool` - True if connected, False otherwise

**Example**:
```python
neo4j_system = Neo4jIntegrationSystem()
if neo4j_system.is_connected():
    print("✅ Connected to Neo4j")
else:
    print("❌ Not connected to Neo4j")
```

##### **`create_node(node_data: dict) -> GraphQueryResult`**
Create a new node in the graph database.

**Parameters**:
- `node_data` (dict): Node data including labels and properties

**Returns**: `GraphQueryResult` - Result object with success status and data

**Example**:
```python
node_data = {
    "node_id": "knowledge_node_001",
    "labels": ["Knowledge", "Concept"],
    "properties": {
        "name": "Living Codex",
        "water_state": "liquid",
        "energy_level": 100.0
    }
}

result = neo4j_system.create_node(node_data)
if result.success:
    print(f"Node created: {result.data}")
else:
    print(f"Error: {result.error}")
```

##### **`query_graph(query: str, parameters: dict = None) -> GraphQueryResult`**
Execute a Cypher query on the graph database.

**Parameters**:
- `query` (str): Cypher query string
- `parameters` (dict, optional): Query parameters

**Returns**: `GraphQueryResult` - Result object with success status and data

**Example**:
```python
# Simple query
query = "MATCH (n) WHERE n.water_state = 'liquid' RETURN n LIMIT 10"
result = neo4j_system.query_graph(query)

if result.success:
    for node in result.data:
        print(f"Found node: {node['n']['node_id']}")

# Parameterized query
query = "MATCH (n) WHERE n.energy_level > $min_energy RETURN n"
params = {"min_energy": 50.0}
result = neo4j_system.query_graph(query, params)

if result.success:
    print(f"Found {len(result.data)} high-energy nodes")
```

##### **`initialize_schema() -> bool`**
Initialize the database schema with required constraints and indexes.

**Returns**: `bool` - True if successful, False otherwise

**Example**:
```python
if neo4j_system.initialize_schema():
    print("✅ Schema initialized successfully")
else:
    print("❌ Schema initialization failed")
```

---

### **Database Persistence System API**

#### **Class**: `DatabasePersistenceSystem`

#### **Constructor**
```python
DatabasePersistenceSystem(
    db_type: str = "sqlite",
    db_path: str = None
)
```

**Parameters**:
- `db_type` (str): Database type ("sqlite" or "postgresql")
- `db_path` (str, optional): Database file path (for SQLite) or connection string

#### **Methods**

##### **`create_node(node: DatabaseNode) -> DatabaseOperationResult`**
Create a new node in the database.

**Parameters**:
- `node` (DatabaseNode): Node object to create

**Returns**: `DatabaseOperationResult` - Result object with success status and data

**Example**:
```python
from src.database.core.models import DatabaseNode
from datetime import datetime

node = DatabaseNode(
    node_id="knowledge_node_001",
    node_type="concept",
    name="Living Codex",
    content="A fractal knowledge management system",
    realm="knowledge_systems",
    water_state="liquid",
    energy_level=100.0,
    transformation_cost=10.0,
    metadata={"category": "system", "complexity": "high"},
    created_at=datetime.now(),
    updated_at=datetime.now()
)

result = db_system.create_node(node)
if result.success:
    print(f"Node created: {result.data}")
else:
    print(f"Error: {result.error}")
```

##### **`read_node(node_id: str) -> DatabaseOperationResult`**
Retrieve a node from the database by ID.

**Parameters**:
- `node_id` (str): Unique identifier of the node

**Returns**: `DatabaseOperationResult` - Result object with success status and data

**Example**:
```python
result = db_system.read_node("knowledge_node_001")
if result.success:
    node = result.data
    print(f"Node: {node.name}")
    print(f"Content: {node.content}")
    print(f"Energy Level: {node.energy_level}")
else:
    print(f"Error: {result.error}")
```

##### **`update_node(node_id: str, updates: dict) -> DatabaseOperationResult`**
Update an existing node in the database.

**Parameters**:
- `node_id` (str): Unique identifier of the node
- `updates` (dict): Dictionary of fields to update

**Returns**: `DatabaseOperationResult` - Result object with success status and data

**Example**:
```python
updates = {
    "energy_level": 150.0,
    "water_state": "vapor",
    "updated_at": datetime.now()
}

result = db_system.update_node("knowledge_node_001", updates)
if result.success:
    print("✅ Node updated successfully")
else:
    print(f"Error: {result.error}")
```

##### **`delete_node(node_id: str) -> DatabaseOperationResult`**
Delete a node from the database.

**Parameters**:
- `node_id` (str): Unique identifier of the node

**Returns**: `DatabaseOperationResult` - Result object with success status and data

**Example**:
```python
result = db_system.delete_node("knowledge_node_001")
if result.success:
    print("✅ Node deleted successfully")
else:
    print(f"Error: {result.error}")
```

##### **`query_nodes(filters: List[QueryFilter], options: QueryOptions = None) -> DatabaseOperationResult`**
Query nodes using filters and options.

**Parameters**:
- `filters` (List[QueryFilter]): List of filter criteria
- `options` (QueryOptions, optional): Query options (limit, offset, ordering)

**Returns**: `DatabaseOperationResult` - Result object with success status and data

**Example**:
```python
from src.database.core.models import QueryFilter, QueryOptions

# Create filters
filters = [
    QueryFilter(field="water_state", operator="=", value="liquid"),
    QueryFilter(field="energy_level", operator=">", value=25.0)
]

# Create options
options = QueryOptions(
    limit=10,
    offset=0,
    order_by="energy_level",
    order_direction="desc"
)

# Execute query
result = db_system.query_nodes(filters, options)
if result.success:
    nodes = result.data
    print(f"Found {len(nodes)} nodes")
    for node in nodes:
        print(f"- {node.name}: {node.energy_level}")
else:
    print(f"Error: {result.error}")
```

---

### **External API System API**

#### **Class**: `RealExternalAPISystem`

#### **Constructor**
```python
RealExternalAPISystem()
```

#### **Methods**

##### **`search_google(query: str, num_results: int = 10) -> APIResponse`**
Search Google Custom Search API.

**Parameters**:
- `query` (str): Search query string
- `num_results` (int, optional): Number of results to return (default: 10)

**Returns**: `APIResponse` - Response object with success status and data

**Example**:
```python
import asyncio

async def search_google_example():
    api_system = RealExternalAPISystem()
    
    try:
        result = await api_system.search_google("fractal systems", num_results=5)
        
        if result.status.value == "success":
            items = result.data.get("items", [])
            print(f"Found {len(items)} Google results:")
            
            for item in items:
                print(f"- {item.get('title', 'No title')}")
                print(f"  {item.get('link', 'No link')}")
                print(f"  {item.get('snippet', 'No snippet')}")
                print()
        else:
            print(f"Search failed: {result.error}")
            
    finally:
        await api_system.close()

# Run the search
asyncio.run(search_google_example())
```

##### **`search_duckduckgo(query: str) -> APIResponse`**
Search DuckDuckGo (free, no API key required).

**Parameters**:
- `query` (str): Search query string

**Returns**: `APIResponse` - Response object with success status and data

**Example**:
```python
import asyncio

async def search_duckduckgo_example():
    api_system = RealExternalAPISystem()
    
    try:
        result = await api_system.search_duckduckgo("Living Codex")
        
        if result.status.value == "success":
            print("DuckDuckGo search successful")
            # Process results as needed
        else:
            print(f"Search failed: {result.error}")
            
    finally:
        await api_system.close()

# Run the search
asyncio.run(search_duckduckgo_example())
```

##### **`search_wikipedia(query: str, num_results: int = 10) -> APIResponse`**
Search Wikipedia API.

**Parameters**:
- `query` (str): Search query string
- `num_results` (int, optional): Number of results to return (default: 10)

**Returns**: `APIResponse` - Response object with success status and data

**Example**:
```python
import asyncio

async def search_wikipedia_example():
    api_system = RealExternalAPISystem()
    
    try:
        result = await api_system.search_wikipedia("fractal", num_results=5)
        
        if result.status.value == "success":
            search_results = result.data.get("query", {}).get("search", [])
            print(f"Found {len(search_results)} Wikipedia results:")
            
            for result_item in search_results:
                print(f"- {result_item.get('title', 'No title')}")
                print(f"  {result_item.get('snippet', 'No snippet')}")
                print()
        else:
            print(f"Search failed: {result.error}")
            
    finally:
        await api_system.close()

# Run the search
asyncio.run(search_wikipedia_example())
```

##### **`query_openai(prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> APIResponse`**
Query OpenAI GPT model.

**Parameters**:
- `prompt` (str): Input prompt for the AI model
- `model` (str, optional): OpenAI model to use (default: "gpt-3.5-turbo")
- `max_tokens` (int, optional): Maximum tokens in response (default: 150)

**Returns**: `APIResponse` - Response object with success status and data

**Example**:
```python
import asyncio

async def query_openai_example():
    api_system = RealExternalAPISystem()
    
    try:
        result = await api_system.query_openai(
            "Explain the concept of fractal systems in simple terms",
            model="gpt-3.5-turbo",
            max_tokens=200
        )
        
        if result.status.value == "success":
            response_text = result.data.get("choices", [{}])[0].get("message", {}).get("content", "")
            print("OpenAI Response:")
            print(response_text)
        else:
            print(f"Query failed: {result.error}")
            
    finally:
        await api_system.close()

# Run the query
asyncio.run(query_openai_example())
```

##### **`get_api_status() -> dict`**
Get the status of all configured APIs.

**Returns**: `dict` - Dictionary containing API status information

**Example**:
```python
api_system = RealExternalAPISystem()
api_status = api_system.get_api_status()

print("API Status:")
for api_name, status in api_status['apis'].items():
    print(f"- {api_name}: {status['status']}")
    if 'rate_limit' in status:
        print(f"  Rate limit: {status['rate_limit']['remaining']}/{status['rate_limit']['limit']}")
```

##### **`close() -> None`**
Close all API connections and clean up resources.

**Example**:
```python
import asyncio

async def api_usage_example():
    api_system = RealExternalAPISystem()
    
    try:
        # Use the API system
        result = await api_system.search_google("test query")
        print("Search completed")
        
    finally:
        # Always close the system
        await api_system.close()
        print("API system closed")

# Run the example
asyncio.run(api_usage_example())
```

---

## 🔧 **Configuration Management API**

### **Class**: `ConfigManager`

#### **Constructor**
```python
ConfigManager(env_file: str = ".env")
```

**Parameters**:
- `env_file` (str): Path to environment file (default: ".env")

#### **Methods**

##### **`get(key: str, default: Any = None) -> Any`**
Get a configuration value.

**Parameters**:
- `key` (str): Configuration key name
- `default` (Any, optional): Default value if key not found

**Returns**: `Any` - Configuration value or default

**Example**:
```python
config_manager = ConfigManager()

# Get configuration values
neo4j_uri = config_manager.get("NEO4J_URI", "bolt://localhost:7687")
openai_key = config_manager.get("OPENAI_API_KEY")

print(f"Neo4j URI: {neo4j_uri}")
print(f"OpenAI Key: {'Configured' if openai_key else 'Not configured'}")
```

##### **`get_available_apis() -> List[str]`**
Get list of available APIs based on configured keys.

**Returns**: `List[str]` - List of available API names

**Example**:
```python
config_manager = ConfigManager()
available_apis = config_manager.get_available_apis()

print("Available APIs:")
for api in available_apis:
    print(f"- {api}")
```

##### **`validate_configuration() -> bool`**
Validate that all required configuration is present.

**Returns**: `bool` - True if configuration is valid, False otherwise

**Example**:
```python
config_manager = ConfigManager()

if config_manager.validate_configuration():
    print("✅ Configuration is valid")
else:
    print("❌ Configuration validation failed")
    print("Check your .env file for missing required values")
```

---

## 📊 **Response Format Standards**

### **GraphQueryResult**
```python
@dataclass
class GraphQueryResult:
    success: bool
    data: Any
    error: Optional[str] = None
    execution_time: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None
```

### **DatabaseOperationResult**
```python
@dataclass
class DatabaseOperationResult:
    success: bool
    data: Any
    error: Optional[str] = None
    operation_type: OperationType
    affected_rows: Optional[int] = None
    execution_time: Optional[float] = None
```

### **APIResponse**
```python
@dataclass
class APIResponse:
    status: APIResponseStatus
    data: Any
    error: Optional[str] = None
    rate_limit_info: Optional[RateLimitInfo] = None
    execution_time: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None
```

---

## 🚨 **Error Handling**

### **Common Error Scenarios**

#### **Neo4j Connection Errors**
```python
try:
    neo4j_system = Neo4jIntegrationSystem()
    if not neo4j_system.is_connected():
        print("❌ Neo4j connection failed")
        print("Check your NEO4J_URI, NEO4J_USERNAME, and NEO4J_PASSWORD")
        return
except Exception as e:
    print(f"❌ Neo4j initialization error: {e}")
```

#### **API Key Errors**
```python
config_manager = ConfigManager()
if not config_manager.get("OPENAI_API_KEY"):
    print("❌ OpenAI API key not configured")
    print("Set OPENAI_API_KEY in your .env file")
    return
```

#### **Database Errors**
```python
try:
    result = db_system.create_node(node)
    if not result.success:
        print(f"❌ Database operation failed: {result.error}")
        return
except Exception as e:
    print(f"❌ Database error: {e}")
```

---

## 🔒 **Authentication and Security**

### **Environment Variables**
All sensitive configuration is stored in environment variables:

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

### **Security Best Practices**
1. **Never commit API keys** to version control
2. **Use environment variables** for all sensitive data
3. **Validate configuration** before system startup
4. **Implement rate limiting** for external APIs
5. **Monitor API usage** and implement alerts

---

## 📈 **Performance and Monitoring**

### **Performance Metrics**
All API responses include execution time:

```python
result = neo4j_system.query_graph("MATCH (n) RETURN n LIMIT 10")
if result.success:
    print(f"Query executed in {result.execution_time:.3f} seconds")
    print(f"Returned {len(result.data)} nodes")
```

### **Rate Limiting**
External APIs include rate limit information:

```python
result = await api_system.search_google("test query")
if result.rate_limit_info:
    print(f"Rate limit: {result.rate_limit_info.remaining}/{result.rate_limit_info.limit}")
    print(f"Reset time: {result.rate_limit_info.reset_time}")
```

### **Monitoring Best Practices**
1. **Track execution times** for performance optimization
2. **Monitor rate limits** to avoid API throttling
3. **Log errors** for debugging and monitoring
4. **Track API usage** for cost optimization

---

## 🧪 **Testing and Validation**

### **Running API Tests**
```bash
# Test all APIs
python test_phase4_integration.py

# Test specific components
python -c "
from src.config.manager import ConfigManager
config = ConfigManager()
print('✅ Config system working')
"
```

### **API Testing Best Practices**
1. **Test with real credentials** when possible
2. **Validate response formats** for all endpoints
3. **Test error conditions** and edge cases
4. **Monitor rate limits** during testing
5. **Clean up test data** after testing

---

## 🔮 **Future API Enhancements**

### **Planned Features**
1. **GraphQL Interface** - Modern query language for graph operations
2. **REST API Endpoints** - HTTP-based API for web integration
3. **WebSocket Support** - Real-time updates and notifications
4. **Batch Operations** - Efficient bulk data processing
5. **Advanced Queries** - Complex graph traversal and analysis

### **Extension Points**
The API architecture provides clear extension points for:
- **New API Sources** - Additional external services
- **Custom Response Formats** - Specialized data structures
- **Authentication Methods** - OAuth, JWT, etc.
- **Rate Limiting Strategies** - Custom throttling logic
- **Caching Layers** - Response caching and optimization

---

## 📚 **Additional Resources**

### **Related Documentation**
- `DEVELOPER_ARCHITECTURE_GUIDE.md` - Architecture and development guide
- `COMPLETE_SYSTEM_DOCUMENTATION.md` - Comprehensive system guide
- `COMPREHENSIVE_SETUP_AND_TESTING_GUIDE.md` - Setup and testing guide

### **Code Examples**
- `integrated_real_systems_demo.py` - Complete system integration examples
- `test_*.py` - Test files with usage examples
- `setup_*.py` - Configuration and setup examples

---

## 🎯 **Getting Help**

### **For API Issues**
1. Check the error handling section above
2. Review the response format standards
3. Run the test suite to validate your environment
4. Check the error logs for detailed information

### **For Integration Questions**
1. Review the code examples in this document
2. Examine the test files for usage patterns
3. Check the main system files for integration examples
4. Review the developer architecture guide

---

## 🌟 **Conclusion**

The Living Codex system provides a **comprehensive, well-documented API** that enables:

- **Easy Integration** with existing systems and applications
- **Flexible Data Access** through multiple storage and query interfaces
- **External Knowledge Integration** with leading search and AI services
- **Professional Development** with consistent patterns and error handling
- **Future Growth** through clear extension points and modular design

This API documentation provides the foundation for effective integration and development with the Living Codex system. Use it as a reference for all API operations, patterns, and best practices.

---

*This API documentation covers all available interfaces and provides comprehensive examples for effective system integration and development.*
