# 🌐 **Web Search API Setup Guide for Living Codex**

## 🌟 **Overview**

This guide will help you set up web search APIs to enable your Living Codex to search the web for knowledge, integrate external information, and build a comprehensive knowledge base.

## 🔍 **Available Search Options**

### **1. Google Custom Search (Recommended)**
- **Quality**: High-quality, structured results
- **Rate Limit**: 100 queries/day (free tier)
- **Cost**: Free for basic usage
- **Setup**: Requires API key and search engine ID

### **2. DuckDuckGo (Free)**
- **Quality**: Good results, privacy-focused
- **Rate Limit**: No strict limits (be respectful)
- **Cost**: Completely free
- **Setup**: No API key required

### **3. Wikipedia API (Free)**
- **Quality**: Encyclopedic knowledge
- **Rate Limit**: No strict limits (be respectful)
- **Cost**: Completely free
- **Setup**: No API key required

## 🚀 **Quick Setup (Automated)**

### **Run the Setup Wizard**
```bash
python setup_web_search.py
```

This will guide you through setting up all web search APIs interactively.

## 🔧 **Manual Setup**

### **Step 1: Google Custom Search Setup**

#### **1.1 Get Google API Key**

1. **Go to Google Cloud Console**:
   - Visit: [https://console.cloud.google.com/](https://console.cloud.google.com/)
   - Sign in with your Google account

2. **Create a New Project**:
   - Click "Select a project" → "New Project"
   - Name: `Living Codex Search`
   - Click "Create"

3. **Enable Custom Search API**:
   - Go to "APIs & Services" → "Library"
   - Search for "Custom Search API"
   - Click "Enable"

4. **Create API Key**:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy the key (starts with `AIza...`)

#### **1.2 Create Custom Search Engine**

1. **Go to Custom Search Engine**:
   - Visit: [https://cse.google.com/cse/](https://cse.google.com/cse/)
   - Click "Add"

2. **Configure Search Engine**:
   - **Sites to search**: Leave blank for web-wide search
   - **Search engine name**: "Living Codex Web Search"
   - **Language**: Choose your preferred language
   - Click "Create"

3. **Get Search Engine ID**:
   - After creation, click on your search engine
   - Look for "Search engine ID" (format: `123456789:abcdefghijk`)
   - Copy this ID

#### **1.3 Set Environment Variables**

```bash
export GOOGLE_API_KEY="AIza-your-api-key-here"
export GOOGLE_CSE_ID="your-search-engine-id-here"
```

### **Step 2: DuckDuckGo Setup (Optional)**

DuckDuckGo doesn't require an API key, but you can set rate limits:

```bash
export DUCKDUCKGO_RATE_LIMIT="100"
```

### **Step 3: Wikipedia Setup (Optional)**

Wikipedia doesn't require an API key, but you can set rate limits:

```bash
export WIKIPEDIA_RATE_LIMIT="100"
```

## 📝 **Update Your .env File**

Add these lines to your `.env` file:

```bash
# Google Custom Search API
GOOGLE_API_KEY=AIza-your-api-key-here
GOOGLE_CSE_ID=your-search-engine-id-here

# Rate Limits (Optional)
DUCKDUCKGO_RATE_LIMIT=100
WIKIPEDIA_RATE_LIMIT=100
```

## 🧪 **Testing Your Setup**

### **Test Web Search Configuration**
```bash
python test_web_search.py
```

### **Test Individual Components**
```bash
python config_manager.py
```

### **Run Integrated Demo**
```bash
python integrated_real_systems_demo.py
```

## 🔍 **Expected Results**

### **Successful Setup**
```
📊 Web Search Configuration:
  Google Custom Search: ✅ Configured
  DuckDuckGo: ✅ Available (free)
  Wikipedia: ✅ Available (free)

🔍 Testing search query: 'Living Codex ontological framework'
📊 Search Results Summary:
  Total Sources: 3
  Successful Sources: 3
  Confidence Score: 1.00
```

### **Common Issues**

#### **API Key Format Error**
```
❌ Google Custom Search: Invalid API key format
```
**Solution**: Ensure your API key starts with `AIza` and is 39 characters long.

#### **Search Engine ID Error**
```
❌ Google Custom Search: Invalid Search Engine ID
```
**Solution**: Ensure your Search Engine ID follows the format `123456789:abcdefghijk`.

#### **Rate Limit Exceeded**
```
❌ Google Custom Search: Quota exceeded
```
**Solution**: Wait for quota reset (daily) or upgrade to paid tier.

## 🌟 **Advanced Configuration**

### **Custom Search Engine Settings**

1. **Go to your Custom Search Engine**:
   - Visit: [https://cse.google.com/cse/](https://cse.google.com/cse/)
   - Click on your search engine

2. **Configure Advanced Settings**:
   - **Search the entire web**: Enable for web-wide search
   - **Search only included sites**: For domain-specific search
   - **Image search**: Enable if you want image results
   - **SafeSearch**: Configure content filtering

### **Rate Limiting and Quotas**

#### **Google Custom Search**
- **Free Tier**: 100 queries/day
- **Paid Tier**: $5 per 1000 queries
- **Quota Reset**: Daily at midnight PST

#### **DuckDuckGo**
- **No strict limits**: Be respectful (recommend <1000 queries/hour)
- **Best practices**: Add delays between requests

#### **Wikipedia**
- **No strict limits**: Be respectful (recommend <1000 queries/hour)
- **Best practices**: Add delays between requests

## 🚀 **Usage Examples**

### **Basic Web Search**
```python
from real_external_api_system import RealExternalAPISystem, APISource

api_system = RealExternalAPISystem()

# Search using all available sources
results = await api_system.search_external_knowledge(
    query="Living Codex ontological framework",
    sources=[APISource.GOOGLE_SEARCH, APISource.DUCKDUCKGO, APISource.WIKIPEDIA],
    max_results=5
)
```

### **Source-Specific Search**
```python
# Google only (if configured)
if config.is_google_configured():
    results = await api_system.search_external_knowledge(
        query="your search query",
        sources=[APISource.GOOGLE_SEARCH],
        max_results=10
    )

# DuckDuckGo only (always available)
results = await api_system.search_external_knowledge(
    query="your search query",
    sources=[APISource.DUCKDUCKGO],
    max_results=10
)
```

## 🔧 **Troubleshooting**

### **Common Problems**

#### **1. API Key Not Working**
- Verify the key is correct and not truncated
- Check if the Custom Search API is enabled
- Ensure the project has billing enabled (if required)

#### **2. Search Engine Not Found**
- Verify the Search Engine ID is correct
- Check if the search engine is active
- Ensure the search engine is configured for web search

#### **3. Rate Limiting Issues**
- Check your current quota usage
- Implement delays between requests
- Consider upgrading to paid tier

#### **4. Network Issues**
- Check your internet connection
- Verify firewall settings
- Test with a simple curl command

### **Debug Commands**

#### **Test Google API Key**
```bash
curl "https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_SEARCH_ENGINE_ID&q=test"
```

#### **Test DuckDuckGo**
```bash
curl "https://api.duckduckgo.com/?q=test&format=json"
```

#### **Test Wikipedia**
```bash
curl "https://en.wikipedia.org/api/rest_v1/page/summary/test"
```

## 🎯 **Best Practices**

### **1. Rate Limiting**
- Implement delays between requests
- Monitor quota usage
- Handle rate limit errors gracefully

### **2. Error Handling**
- Always check for API errors
- Implement fallback to free sources
- Log errors for debugging

### **3. Caching**
- Cache search results when possible
- Implement TTL for cached data
- Store results in your database

### **4. Privacy**
- Be mindful of user privacy
- Don't log sensitive search queries
- Consider using DuckDuckGo for privacy-sensitive searches

## 🌟 **Benefits of Web Search Integration**

### **Knowledge Expansion**
- Access to current information
- Real-time knowledge updates
- Broader knowledge coverage

### **System Intelligence**
- AI-powered insights
- External knowledge validation
- Continuous learning capability

### **Research Capabilities**
- Academic research support
- News and current events
- Technical documentation access

## 🎉 **Next Steps**

Once your web search APIs are configured:

1. **Test the setup**: Run `python test_web_search.py`
2. **Explore capabilities**: Try different search queries
3. **Integrate with your system**: Use search results in your knowledge base
4. **Build applications**: Create knowledge discovery tools
5. **Scale up**: Consider additional search sources

## 🔗 **Useful Links**

- **Google Cloud Console**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
- **Custom Search Engine**: [https://cse.google.com/cse/](https://cse.google.com/cse/)
- **DuckDuckGo API**: [https://duckduckgo.com/api](https://duckduckgo.com/api)
- **Wikipedia API**: [https://en.wikipedia.org/api/](https://en.wikipedia.org/api/)

---

*This guide will get you up and running with web search APIs for your Living Codex. Once configured, your system will be able to search the web, integrate external knowledge, and continuously expand its knowledge base.*
