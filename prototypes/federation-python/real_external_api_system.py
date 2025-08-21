#!/usr/bin/env python3
"""
Real External API Integration System - Living Codex
Replaces simulated external integrations with real HTTP-based API connections
to external knowledge sources including web search, knowledge bases, and expert systems.
"""

import os
import json
import time
import hashlib
import asyncio
import aiohttp
import requests
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import logging
from urllib.parse import quote_plus, urlencode

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APISource(Enum):
    """External API sources"""
    GOOGLE_SEARCH = "google_search"
    DUCKDUCKGO = "duckduckgo"
    WIKIPEDIA = "wikipedia"
    WIKIDATA = "wikidata"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    CUSTOM_KNOWLEDGE_BASE = "custom_kb"

class APIResponseStatus(Enum):
    """API response status"""
    SUCCESS = "success"
    RATE_LIMITED = "rate_limited"
    ERROR = "error"
    TIMEOUT = "timeout"
    INVALID_RESPONSE = "invalid_response"

@dataclass
class APIRequest:
    """API request configuration"""
    source: APISource
    endpoint: str
    method: str = "GET"
    headers: Optional[Dict[str, str]] = None
    params: Optional[Dict[str, Any]] = None
    data: Optional[Dict[str, Any]] = None
    timeout: int = 30
    retry_count: int = 3

@dataclass
class APIResponse:
    """API response data"""
    source: APISource
    status: APIResponseStatus
    data: Any
    headers: Dict[str, str]
    status_code: int
    response_time: float
    timestamp: datetime
    metadata: Dict[str, Any]

@dataclass
class RateLimitInfo:
    """Rate limiting information"""
    requests_remaining: int
    reset_time: datetime
    window_size: int
    current_usage: int

class APIManagementSystem:
    """Manages API keys, rate limiting, and authentication"""
    
    def __init__(self):
        self.api_keys = {}
        self.rate_limits = {}
        self.request_history = {}
        self._load_api_keys()
        self._initialize_rate_limits()
    
    def _load_api_keys(self):
        """Load API keys from environment variables"""
        self.api_keys = {
            APISource.GOOGLE_SEARCH: os.getenv("GOOGLE_API_KEY"),  # Use GOOGLE_API_KEY
            APISource.OPENAI: os.getenv("OPENAI_API_KEY"),
            APISource.ANTHROPIC: os.getenv("ANTHROPIC_API_KEY"),
            APISource.CUSTOM_KNOWLEDGE_BASE: os.getenv("CUSTOM_KB_API_KEY"),
        }
        
        # Store CSE ID separately
        self.google_cse_id = os.getenv("GOOGLE_CSE_ID")
        
        # Log which APIs are available
        available_apis = [source.value for source, key in self.api_keys.items() if key]
        logger.info(f"Available API keys: {available_apis}")
    
    def _initialize_rate_limits(self):
        """Initialize rate limiting for different APIs"""
        self.rate_limits = {
            APISource.GOOGLE_SEARCH: {"requests_per_minute": 100, "requests_per_day": 10000},
            APISource.DUCKDUCKGO: {"requests_per_minute": 1000, "requests_per_day": 100000},
            APISource.WIKIPEDIA: {"requests_per_minute": 500, "requests_per_day": 50000},
            APISource.WIKIDATA: {"requests_per_minute": 500, "requests_per_day": 50000},
            APISource.OPENAI: {"requests_per_minute": 60, "requests_per_day": 5000},
            APISource.ANTHROPIC: {"requests_per_minute": 60, "requests_per_day": 5000},
            APISource.CUSTOM_KNOWLEDGE_BASE: {"requests_per_minute": 200, "requests_per_day": 20000},
        }
    
    def get_api_key(self, source: APISource) -> Optional[str]:
        """Get API key for a specific source"""
        return self.api_keys.get(source)
    
    def get_google_cse_id(self) -> Optional[str]:
        """Get Google Custom Search Engine ID"""
        return getattr(self, 'google_cse_id', None)
    
    def check_rate_limit(self, source: APISource) -> bool:
        """Check if we can make a request to the API"""
        if source not in self.request_history:
            return True
        
        now = datetime.now()
        window_start = now - timedelta(minutes=1)
        
        # Count requests in the last minute
        recent_requests = [
            req_time for req_time in self.request_history[source]
            if req_time > window_start
        ]
        
        max_requests = self.rate_limits[source]["requests_per_minute"]
        return len(recent_requests) < max_requests
    
    def record_request(self, source: APISource):
        """Record a request to track rate limiting"""
        if source not in self.request_history:
            self.request_history[source] = []
        
        self.request_history[source].append(datetime.now())
        
        # Clean up old requests (keep only last hour)
        cutoff = datetime.now() - timedelta(hours=1)
        self.request_history[source] = [
            req_time for req_time in self.request_history[source]
            if req_time > cutoff
        ]

class WebSearchIntegration:
    """Real web search integration using multiple search engines"""
    
    def __init__(self, api_manager: APIManagementSystem):
        self.api_manager = api_manager
        self.session = requests.Session()
        self.cache = {}
        self.cache_ttl = 3600  # 1 hour cache
    
    async def search_google(self, query: str, max_results: int = 10) -> APIResponse:
        """Search using Google Custom Search API"""
        if not self.api_manager.check_rate_limit(APISource.GOOGLE_SEARCH):
            return APIResponse(
                source=APISource.GOOGLE_SEARCH,
                status=APIResponseStatus.RATE_LIMITED,
                data=None,
                headers={},
                status_code=429,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Rate limited"}
            )
        
        api_key = self.api_manager.get_api_key(APISource.GOOGLE_SEARCH)
        cse_id = self.api_manager.get_google_cse_id()
        
        if not api_key or not cse_id:
            return APIResponse(
                source=APISource.GOOGLE_SEARCH,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=400,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Missing API key or CSE ID"}
            )
        
        start_time = time.time()
        
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": api_key,
                "cx": cse_id,
                "q": query,
                "num": min(max_results, 10)  # Google CSE max is 10
            }
            
            response = self.session.get(url, params=params, timeout=30)
            response_time = time.time() - start_time
            
            self.api_manager.record_request(APISource.GOOGLE_SEARCH)
            
            if response.status_code == 200:
                data = response.json()
                return APIResponse(
                    source=APISource.GOOGLE_SEARCH,
                    status=APIResponseStatus.SUCCESS,
                    data=data,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={
                        "query": query,
                        "results_count": len(data.get("items", [])),
                        "total_results": data.get("searchInformation", {}).get("totalResults", 0)
                    }
                )
            else:
                return APIResponse(
                    source=APISource.GOOGLE_SEARCH,
                    status=APIResponseStatus.ERROR,
                    data=None,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={"error": f"HTTP {response.status_code}", "query": query}
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            logger.error(f"Google search error: {e}")
            return APIResponse(
                source=APISource.GOOGLE_SEARCH,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=response_time,
                timestamp=datetime.now(),
                metadata={"error": str(e), "query": query}
            )
    
    async def search_duckduckgo(self, query: str, max_results: int = 10) -> APIResponse:
        """Search using DuckDuckGo Instant Answer API"""
        if not self.api_manager.check_rate_limit(APISource.DUCKDUCKGO):
            return APIResponse(
                source=APISource.DUCKDUCKGO,
                status=APIResponseStatus.RATE_LIMITED,
                data=None,
                headers={},
                status_code=429,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Rate limited"}
            )
        
        start_time = time.time()
        
        try:
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json",
                "no_html": "1",
                "skip_disambig": "1"
            }
            
            response = self.session.get(url, params=params, timeout=30)
            response_time = time.time() - start_time
            
            self.api_manager.record_request(APISource.DUCKDUCKGO)
            
            if response.status_code == 200:
                data = response.json()
                return APIResponse(
                    source=APISource.DUCKDUCKGO,
                    status=APIResponseStatus.SUCCESS,
                    data=data,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={
                        "query": query,
                        "abstract": data.get("Abstract", ""),
                        "related_topics": len(data.get("RelatedTopics", [])),
                        "answer_type": data.get("AnswerType", "")
                    }
                )
            else:
                return APIResponse(
                    source=APISource.DUCKDUCKGO,
                    status=APIResponseStatus.ERROR,
                    data=None,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={"error": f"HTTP {response.status_code}", "query": query}
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            logger.error(f"DuckDuckGo search error: {e}")
            return APIResponse(
                source=APISource.DUCKDUCKGO,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=response_time,
                timestamp=datetime.now(),
                metadata={"error": str(e), "query": query}
            )
    
    async def search_web(self, query: str, max_results: int = 10, 
                         sources: List[APISource] = None) -> List[APIResponse]:
        """Search multiple web sources"""
        if sources is None:
            sources = [APISource.GOOGLE_SEARCH, APISource.DUCKDUCKGO]
        
        results = []
        
        for source in sources:
            if source == APISource.GOOGLE_SEARCH:
                result = await self.search_google(query, max_results)
            elif source == APISource.DUCKDUCKGO:
                result = await self.search_duckduckgo(query, max_results)
            else:
                continue
            
            results.append(result)
        
        return results

class KnowledgeBaseIntegration:
    """Integration with knowledge bases like Wikipedia and Wikidata"""
    
    def __init__(self, api_manager: APIManagementSystem):
        self.api_manager = api_manager
        self.session = requests.Session()
    
    async def search_wikipedia(self, query: str, max_results: int = 5) -> APIResponse:
        """Search Wikipedia using the MediaWiki API"""
        if not self.api_manager.check_rate_limit(APISource.WIKIPEDIA):
            return APIResponse(
                source=APISource.WIKIPEDIA,
                status=APIResponseStatus.RATE_LIMITED,
                data=None,
                headers={},
                status_code=429,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Rate limited"}
            )
        
        start_time = time.time()
        
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "format": "json",
                "list": "search",
                "srsearch": query,
                "srlimit": max_results,
                "srnamespace": 0
            }
            
            response = self.session.get(url, params=params, timeout=30)
            response_time = time.time() - start_time
            
            self.api_manager.record_request(APISource.WIKIPEDIA)
            
            if response.status_code == 200:
                data = response.json()
                return APIResponse(
                    source=APISource.WIKIPEDIA,
                    status=APIResponseStatus.SUCCESS,
                    data=data,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={
                        "query": query,
                        "results_count": len(data.get("query", {}).get("search", [])),
                        "total_results": data.get("query", {}).get("searchinfo", {}).get("totalhits", 0)
                    }
                )
            else:
                return APIResponse(
                    source=APISource.WIKIPEDIA,
                    status=APIResponseStatus.ERROR,
                    data=None,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={"error": f"HTTP {response.status_code}", "query": query}
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            logger.error(f"Wikipedia search error: {e}")
            return APIResponse(
                source=APISource.WIKIPEDIA,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=response_time,
                timestamp=datetime.now(),
                metadata={"error": str(e), "query": query}
            )
    
    async def get_wikipedia_article(self, title: str) -> APIResponse:
        """Get full Wikipedia article content"""
        if not self.api_manager.check_rate_limit(APISource.WIKIPEDIA):
            return APIResponse(
                source=APISource.WIKIPEDIA,
                status=APIResponseStatus.RATE_LIMITED,
                data=None,
                headers={},
                status_code=429,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Rate limited"}
            )
        
        start_time = time.time()
        
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "format": "json",
                "titles": title,
                "prop": "extracts|info",
                "exintro": 1,
                "explaintext": 1,
                "inprop": "url"
            }
            
            response = self.session.get(url, params=params, timeout=30)
            response_time = time.time() - start_time
            
            self.api_manager.record_request(APISource.WIKIPEDIA)
            
            if response.status_code == 200:
                data = response.json()
                return APIResponse(
                    source=APISource.WIKIPEDIA,
                    status=APIResponseStatus.SUCCESS,
                    data=data,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={
                        "title": title,
                        "has_content": "extract" in str(data),
                        "url": data.get("query", {}).get("pages", {}).get("1", {}).get("fullurl", "")
                    }
                )
            else:
                return APIResponse(
                    source=APISource.WIKIPEDIA,
                    status=APIResponseStatus.ERROR,
                    data=None,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={"error": f"HTTP {response.status_code}", "title": title}
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            logger.error(f"Wikipedia article error: {e}")
            return APIResponse(
                source=APISource.WIKIPEDIA,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=response_time,
                timestamp=datetime.now(),
                metadata={"error": str(e), "title": title}
            )

class ExpertSystemIntegration:
    """Integration with AI expert systems like OpenAI and Anthropic"""
    
    def __init__(self, api_manager: APIManagementSystem):
        self.api_manager = api_manager
        self.session = requests.Session()
    
    async def consult_openai(self, question: str, context: str = "", 
                           model: str = "gpt-3.5-turbo") -> APIResponse:
        """Consult OpenAI for expert knowledge"""
        if not self.api_manager.check_rate_limit(APISource.OPENAI):
            return APIResponse(
                source=APISource.OPENAI,
                status=APIResponseStatus.RATE_LIMITED,
                data=None,
                headers={},
                status_code=429,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Rate limited"}
            )
        
        api_key = self.api_manager.get_api_key(APISource.OPENAI)
        if not api_key:
            return APIResponse(
                source=APISource.OPENAI,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=400,
                response_time=0.0,
                timestamp=datetime.now(),
                metadata={"error": "Missing OpenAI API key"}
            )
        
        start_time = time.time()
        
        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            messages = []
            if context:
                messages.append({"role": "system", "content": context})
            messages.append({"role": "user", "content": question})
            
            data = {
                "model": model,
                "messages": messages,
                "max_tokens": 1000,
                "temperature": 0.7
            }
            
            response = self.session.post(url, headers=headers, json=data, timeout=60)
            response_time = time.time() - start_time
            
            self.api_manager.record_request(APISource.OPENAI)
            
            if response.status_code == 200:
                result_data = response.json()
                return APIResponse(
                    source=APISource.OPENAI,
                    status=APIResponseStatus.SUCCESS,
                    data=result_data,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={
                        "question": question,
                        "model": model,
                        "tokens_used": result_data.get("usage", {}).get("total_tokens", 0),
                        "response_length": len(result_data.get("choices", [{}])[0].get("message", {}).get("content", ""))
                    }
                )
            else:
                return APIResponse(
                    source=APISource.OPENAI,
                    status=APIResponseStatus.ERROR,
                    data=None,
                    headers=dict(response.headers),
                    status_code=response.status_code,
                    response_time=response_time,
                    timestamp=datetime.now(),
                    metadata={"error": f"HTTP {response.status_code}", "question": question}
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            logger.error(f"OpenAI consultation error: {e}")
            return APIResponse(
                source=APISource.OPENAI,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=response_time,
                timestamp=datetime.now(),
                metadata={"error": str(e), "question": question}
            )

class RealExternalAPISystem:
    """Main system that orchestrates all external API integrations"""
    
    def __init__(self):
        self.api_manager = APIManagementSystem()
        self.web_search = WebSearchIntegration(self.api_manager)
        self.knowledge_base = KnowledgeBaseIntegration(self.api_manager)
        self.expert_system = ExpertSystemIntegration(self.api_manager)
        self.cache = {}
        self.cache_ttl = 3600  # 1 hour
    
    async def search_external_knowledge(self, query: str, 
                                      sources: List[APISource] = None,
                                      max_results: int = 10) -> Dict[str, Any]:
        """Search external knowledge sources"""
        
        # Check cache first
        cache_key = hashlib.sha256(f"{query}_{sources}_{max_results}".encode()).hexdigest()
        if cache_key in self.cache:
            cache_entry = self.cache[cache_key]
            if (datetime.now() - cache_entry["timestamp"]).seconds < self.cache_ttl:
                logger.info(f"Returning cached result for query: {query}")
                return cache_entry["data"]
        
        results = {
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "sources": {},
            "summary": {},
            "total_results": 0
        }
        
        # Web search
        if sources is None or any(s in sources for s in [APISource.GOOGLE_SEARCH, APISource.DUCKDUCKGO]):
            web_results = await self.web_search.search_web(query, max_results)
            results["sources"]["web_search"] = web_results
            results["total_results"] += len(web_results)
        
        # Knowledge base search
        if sources is None or APISource.WIKIPEDIA in sources:
            wiki_result = await self.knowledge_base.search_wikipedia(query, max_results)
            results["sources"]["wikipedia"] = wiki_result
            if wiki_result.status == APIResponseStatus.SUCCESS:
                results["total_results"] += 1
        
        # Expert system consultation
        if sources is None or APISource.OPENAI in sources:
            expert_result = await self.expert_system.consult_openai(query)
            results["sources"]["expert_system"] = expert_result
            if expert_result.status == APIResponseStatus.SUCCESS:
                results["total_results"] += 1
        
        # Generate summary
        results["summary"] = self._generate_summary(results["sources"])
        
        # Cache the result
        self.cache[cache_key] = {
            "data": results,
            "timestamp": datetime.now()
        }
        
        return results
    
    def _generate_summary(self, sources: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a summary of all source results"""
        summary = {
            "total_sources": len(sources),
            "successful_sources": 0,
            "total_items": 0,
            "key_insights": [],
            "confidence_score": 0.0
        }
        
        for source_name, source_results in sources.items():
            if isinstance(source_results, list):
                # Web search results
                successful_results = [r for r in source_results if r.status == APIResponseStatus.SUCCESS]
                summary["successful_sources"] += 1 if successful_results else 0
                summary["total_items"] += len(successful_results)
                
                # Extract key insights from web search
                for result in successful_results:
                    if result.data and "items" in result.data:
                        for item in result.data["items"][:3]:  # Top 3 results
                            if "snippet" in item:
                                summary["key_insights"].append({
                                    "source": source_name,
                                    "content": item["snippet"][:200] + "...",
                                    "title": item.get("title", ""),
                                    "url": item.get("link", "")
                                })
            
            elif isinstance(source_results, APIResponse):
                # Single API response
                if source_results.status == APIResponseStatus.SUCCESS:
                    summary["successful_sources"] += 1
                    summary["total_items"] += 1
                    
                    # Extract insights from different source types
                    if source_name == "wikipedia" and source_results.data:
                        search_results = source_results.data.get("query", {}).get("search", [])
                        for item in search_results[:3]:
                            summary["key_insights"].append({
                                "source": source_name,
                                "content": item.get("snippet", "")[:200] + "...",
                                "title": item.get("title", ""),
                                "url": f"https://en.wikipedia.org/wiki/{item.get('title', '').replace(' ', '_')}"
                            })
                    
                    elif source_name == "expert_system" and source_results.data:
                        content = source_results.data.get("choices", [{}])[0].get("message", {}).get("content", "")
                        if content:
                            summary["key_insights"].append({
                                "source": source_name,
                                "content": content[:300] + "...",
                                "title": "AI Expert Consultation",
                                "url": ""
                            })
        
        # Calculate confidence score
        if summary["total_sources"] > 0:
            summary["confidence_score"] = summary["successful_sources"] / summary["total_sources"]
        
        return summary
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get the current status of the external API system"""
        return {
            "timestamp": datetime.now().isoformat(),
            "api_keys_available": {
                source.value: bool(key) for source, key in self.api_manager.api_keys.items()
            },
            "rate_limits": self.api_manager.rate_limits,
            "cache_size": len(self.cache),
            "cache_ttl": self.cache_ttl,
            "total_requests": sum(len(requests) for requests in self.api_manager.request_history.values())
        }

async def main():
    """Main function to demonstrate the Real External API System"""
    
    print("🌟 Living Codex Real External API Integration System Demo")
    print("=" * 70)
    
    try:
        # Create the system
        external_api_system = RealExternalAPISystem()
        
        # Show system status
        status = external_api_system.get_system_status()
        print(f"\n🔧 System Status:")
        print(f"   Available APIs: {[api for api, available in status['api_keys_available'].items() if available]}")
        print(f"   Cache Size: {status['cache_size']}")
        print(f"   Total Requests: {status['total_requests']}")
        
        # Test external knowledge search
        print(f"\n🔍 Testing External Knowledge Search...")
        query = "Living Codex ontological framework and fractal systems"
        
        results = await external_api_system.search_external_knowledge(
            query=query,
            sources=[APISource.DUCKDUCKGO, APISource.WIKIPEDIA],
            max_results=5
        )
        
        print(f"\n📊 Search Results for: '{query}'")
        print(f"   Total Sources: {results['summary']['total_sources']}")
        print(f"   Successful Sources: {results['summary']['successful_sources']}")
        print(f"   Total Items: {results['summary']['total_items']}")
        print(f"   Confidence Score: {results['summary']['confidence_score']:.2f}")
        
        # Show key insights
        if results['summary']['key_insights']:
            print(f"\n💡 Key Insights:")
            for i, insight in enumerate(results['summary']['key_insights'][:3], 1):
                print(f"   {i}. [{insight['source']}] {insight['title']}")
                print(f"      {insight['content']}")
                if insight['url']:
                    print(f"      URL: {insight['url']}")
                print()
        
        # Test expert system if available
        if status['api_keys_available'].get('openai'):
            print(f"\n🤖 Testing Expert System Consultation...")
            expert_query = "What are the key principles of ontological frameworks in knowledge systems?"
            
            expert_results = await external_api_system.search_external_knowledge(
                query=expert_query,
                sources=[APISource.OPENAI],
                max_results=1
            )
            
            if expert_results['sources'].get('expert_system'):
                expert_response = expert_results['sources']['expert_system']
                if expert_response.status == APIResponseStatus.SUCCESS:
                    print(f"✅ Expert consultation successful!")
                    print(f"   Response Time: {expert_response.response_time:.2f}s")
                    print(f"   Tokens Used: {expert_response.metadata.get('tokens_used', 'N/A')}")
                else:
                    print(f"❌ Expert consultation failed: {expert_response.metadata.get('error', 'Unknown error')}")
        
        print("\n" + "=" * 70)
        print("🎉 Real External API Integration System Demo Completed!")
        print("\n🌟 What We've Achieved:")
        print("   • Real HTTP-based API integrations")
        print("   • Rate limiting and API key management")
        print("   • Multiple search engine support")
        print("   • Wikipedia and knowledge base integration")
        print("   • AI expert system consultation")
        print("   • Intelligent result caching and summarization")
        print("\n🚀 The Living Codex now has real external knowledge integration!")
        
    except Exception as e:
        print(f"❌ Error running Real External API System demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
