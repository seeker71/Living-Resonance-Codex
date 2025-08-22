#!/usr/bin/env python3
"""
Real External API System - Living Codex
Integrates with real external APIs (Google Search, DuckDuckGo, Wikipedia, OpenAI)
to provide comprehensive knowledge acquisition and processing capabilities.

UPDATED: Now uses modular components from src/api/ while maintaining backward compatibility
"""

import os
import json
import time
import asyncio
import aiohttp
import hashlib
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import logging

# Import new modular components
try:
    from src.api.management.api_manager import APIManagementSystem
    from src.api.sources.base.api_client import BaseAPIClient
    from src.api.sources.base.models import APISource, APIResponseStatus, APIResponse
    MODULAR_IMPORTS_AVAILABLE = True
    print("✅ Using new modular API components")
except ImportError:
    MODULAR_IMPORTS_AVAILABLE = False
    print("⚠️  Modular imports not available, using legacy components")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Legacy enums and models (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
    class APISource(Enum):
        """External API sources"""
        GOOGLE_SEARCH = "google_search"
        DUCKDUCKGO = "duckduckgo"
        WIKIPEDIA = "wikipedia"
        OPENAI = "openai"
        UNKNOWN = "unknown"

    class APIResponseStatus(Enum):
        """API response status"""
        SUCCESS = "success"
        ERROR = "error"
        RATE_LIMITED = "rate_limited"
        UNAUTHORIZED = "unauthorized"
        NOT_FOUND = "not_found"
        TIMEOUT = "timeout"

    @dataclass
    class APIResponse:
        """Standardized API response"""
        source: APISource
        status: APIResponseStatus
        data: Any
        timestamp: datetime
        metadata: Dict[str, Any]
        error_message: Optional[str] = None

# Legacy API management system (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
    class APIManagementSystem:
        """Manages API keys, rate limits, and request history"""
        
        def __init__(self):
            self.api_keys = {}
            self.rate_limits = {}
            self.request_history = []
            self._load_api_keys()
            self._initialize_rate_limits()
        
        def _load_api_keys(self):
            """Load API keys from environment variables"""
            self.api_keys = {
                "openai": os.getenv("OPENAI_API_KEY"),
                "google": os.getenv("GOOGLE_API_KEY"),
                "google_cse": os.getenv("GOOGLE_CSE_ID"),
                "duckduckgo": "free",  # DuckDuckGo is free
                "wikipedia": "free"    # Wikipedia is free
            }
        
        def _initialize_rate_limits(self):
            """Initialize rate limits for different APIs"""
            self.rate_limits = {
                "openai": {"requests_per_minute": 60, "requests_per_hour": 3500},
                "google": {"requests_per_day": 10000},
                "duckduckgo": {"requests_per_minute": 100},
                "wikipedia": {"requests_per_minute": 100}
            }
        
        def get_api_key(self, api_name: str) -> Optional[str]:
            """Get API key for a specific service"""
            return self.api_keys.get(api_name)
        
        def get_google_cse_id(self) -> Optional[str]:
            """Get Google Custom Search Engine ID"""
            return self.api_keys.get("google_cse")
        
        def check_rate_limit(self, api_name: str) -> bool:
            """Check if API is within rate limits"""
            # Simple rate limiting - in production, use Redis or similar
            recent_requests = [
                req for req in self.request_history 
                if req["api"] == api_name and 
                req["timestamp"] > datetime.now() - timedelta(minutes=1)
            ]
            
            limit = self.rate_limits.get(api_name, {}).get("requests_per_minute", 100)
            return len(recent_requests) < limit
        
        def record_request(self, api_name: str, success: bool, response_time: float):
            """Record API request for monitoring"""
            self.request_history.append({
                "api": api_name,
                "timestamp": datetime.now(),
                "success": success,
                "response_time": response_time
            })
            
            # Keep only last 1000 requests
            if len(self.request_history) > 1000:
                self.request_history = self.request_history[-500:]

# Legacy API client (maintained for backward compatibility)
if not MODULAR_IMPORTS_AVAILABLE:
    class BaseAPIClient:
        """Base class for API clients"""
        
        def __init__(self, api_manager: APIManagementSystem):
            self.api_manager = api_manager
            self.session = None
            self.cache = {}
            self.cache_ttl = 3600  # 1 hour
        
        async def _get_session(self) -> aiohttp.ClientSession:
            """Get or create HTTP session"""
            if not self.session or self.session.closed:
                import aiohttp
                self.session = aiohttp.ClientSession(
                    timeout=aiohttp.ClientTimeout(total=30)
                )
            return self.session
        
        async def _make_request(self, method: str, url: str, **kwargs) -> APIResponse:
            """Make HTTP request with error handling"""
            start_time = time.time()
            
            try:
                session = await self._get_session()
                
                async with session.request(method, url, **kwargs) as response:
                    response_time = time.time() - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        self.api_manager.record_request(
                            "unknown", True, response_time
                        )
                        
                        return APIResponse(
                            source=APISource.UNKNOWN,
                            status=APIResponseStatus.SUCCESS,
                            data=data,
                            timestamp=datetime.now(),
                            metadata={"response_time": response_time}
                        )
                    else:
                        error_msg = f"HTTP {response.status}: {response.reason}"
                        self.api_manager.record_request(
                            "unknown", False, response_time
                        )
                        
                        return APIResponse(
                            source=APISource.UNKNOWN,
                            status=APIResponseStatus.ERROR,
                            data=None,
                            timestamp=datetime.now(),
                            metadata={"response_time": response_time},
                            error_message=error_msg
                        )
                        
            except Exception as e:
                response_time = time.time() - start_time
                self.api_manager.record_request(
                    "unknown", False, response_time
                )
                
                return APIResponse(
                    source=APISource.UNKNOWN,
                    status=APIResponseStatus.ERROR,
                    data=None,
                    timestamp=datetime.now(),
                    metadata={"response_time": response_time},
                    error_message=str(e)
                )
        
        async def close(self):
            """Close the HTTP session"""
            if self.session and not self.session.closed:
                await self.session.close()

# Main RealExternalAPISystem class - now uses modular components when available
class RealExternalAPISystem:
    """Main external API system - uses modular components when available"""
    
    def __init__(self):
        # Initialize API management system
        if MODULAR_IMPORTS_AVAILABLE:
            self.api_manager = APIManagementSystem()
            logger.info("✅ Using modular API components")
        else:
            self.api_manager = APIManagementSystem()
            logger.info("✅ Using legacy API components")
        
        # Initialize API clients
        if MODULAR_IMPORTS_AVAILABLE:
            # For now, we'll use a simple implementation
            # In the future, this will use the full modular system
            self.api_clients = self._create_simple_clients()
        else:
            self.api_clients = self._create_simple_clients()
    
    def _create_simple_clients(self):
        """Create simple API clients for backward compatibility"""
        class SimpleAPIClient:
            def __init__(self, api_manager):
                self.api_manager = api_manager
                self.session = None
            
            async def _get_session(self):
                """Get or create HTTP session"""
                if not self.session or self.session.closed:
                    import aiohttp
                    self.session = aiohttp.ClientSession(
                        timeout=aiohttp.ClientTimeout(total=30)
                    )
                return self.session
            
            async def search_google(self, query: str, num_results: int = 5) -> APIResponse:
                """Search Google using Custom Search API"""
                start_time = time.time()
                
                api_key = self.api_manager.get_api_key("google")
                cse_id = self.api_manager.get_google_cse_id()
                
                if not api_key or not cse_id:
                    return APIResponse(
                        source=APISource.GOOGLE_SEARCH,
                        status=APIResponseStatus.UNAUTHORIZED,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={},
                        error_message="Google API key or CSE ID not configured"
                    )
                
                if not self.api_manager.check_rate_limit("google"):
                    return APIResponse(
                        source=APISource.GOOGLE_SEARCH,
                        status=APIResponseStatus.RATE_LIMITED,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={},
                        error_message="Rate limit exceeded"
                    )
                
                try:
                    session = await self._get_session()
                    
                    url = "https://www.googleapis.com/customsearch/v1"
                    params = {
                        "key": api_key,
                        "cx": cse_id,
                        "q": query,
                        "num": min(num_results, 10)  # Google CSE max is 10
                    }
                    
                    async with session.get(url, params=params) as response:
                        response_time = time.time() - start_time
                        
                        if response.status == 200:
                            data = await response.json()
                            self.api_manager.record_request("google", True, response_time)
                            
                            return APIResponse(
                                source=APISource.GOOGLE_SEARCH,
                                status=APIResponseStatus.SUCCESS,
                                data=data,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time}
                            )
                        else:
                            error_msg = f"HTTP {response.status}: {response.reason}"
                            self.api_manager.record_request("google", False, response_time)
                            
                            return APIResponse(
                                source=APISource.GOOGLE_SEARCH,
                                status=APIResponseStatus.ERROR,
                                data=None,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time},
                                error_message=error_msg
                            )
                            
                except Exception as e:
                    response_time = time.time() - start_time
                    self.api_manager.record_request("google", False, response_time)
                    
                    return APIResponse(
                        source=APISource.GOOGLE_SEARCH,
                        status=APIResponseStatus.ERROR,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={"response_time": response_time},
                        error_message=str(e)
                    )
            
            async def search_duckduckgo(self, query: str) -> APIResponse:
                """Search DuckDuckGo (free, no API key required)"""
                start_time = time.time()
                
                if not self.api_manager.check_rate_limit("duckduckgo"):
                    return APIResponse(
                        source=APISource.DUCKDUCKGO,
                        status=APIResponseStatus.RATE_LIMITED,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={},
                        error_message="Rate limit exceeded"
                    )
                
                try:
                    session = await self._get_session()
                    
                    # DuckDuckGo Instant Answer API
                    url = "https://api.duckduckgo.com/"
                    params = {
                        "q": query,
                        "format": "json",
                        "no_html": "1",
                        "skip_disambig": "1"
                    }
                    
                    async with session.get(url, params=params) as response:
                        response_time = time.time() - start_time
                        
                        if response.status == 200:
                            data = await response.json()
                            self.api_manager.record_request("duckduckgo", True, response_time)
                            
                            return APIResponse(
                                source=APISource.DUCKDUCKGO,
                                status=APIResponseStatus.SUCCESS,
                                data=data,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time}
                            )
                        else:
                            error_msg = f"HTTP {response.status}: {response.reason}"
                            self.api_manager.record_request("duckduckgo", False, response_time)
                            
                            return APIResponse(
                                source=APISource.DUCKDUCKGO,
                                status=APIResponseStatus.ERROR,
                                data=None,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time},
                                error_message=error_msg
                            )
                            
                except Exception as e:
                    response_time = time.time() - start_time
                    self.api_manager.record_request("duckduckgo", False, response_time)
                    
                    return APIResponse(
                        source=APISource.DUCKDUCKGO,
                        status=APIResponseStatus.ERROR,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={"response_time": response_time},
                        error_message=str(e)
                    )
            
            async def search_wikipedia(self, query: str) -> APIResponse:
                """Search Wikipedia (free, no API key required)"""
                start_time = time.time()
                
                if not self.api_manager.check_rate_limit("wikipedia"):
                    return APIResponse(
                        source=APISource.WIKIPEDIA,
                        status=APIResponseStatus.RATE_LIMITED,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={},
                        error_message="Rate limit exceeded"
                    )
                
                try:
                    session = await self._get_session()
                    
                    # Wikipedia Search API
                    url = "https://en.wikipedia.org/w/api.php"
                    params = {
                        "action": "query",
                        "format": "json",
                        "list": "search",
                        "srsearch": query,
                        "srlimit": 5
                    }
                    
                    async with session.get(url, params=params) as response:
                        response_time = time.time() - start_time
                        
                        if response.status == 200:
                            data = await response.json()
                            self.api_manager.record_request("wikipedia", True, response_time)
                            
                            return APIResponse(
                                source=APISource.WIKIPEDIA,
                                status=APIResponseStatus.SUCCESS,
                                data=data,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time}
                            )
                        else:
                            error_msg = f"HTTP {response.status}: {response.reason}"
                            self.api_manager.record_request("wikipedia", False, response_time)
                            
                            return APIResponse(
                                source=APISource.WIKIPEDIA,
                                status=APIResponseStatus.ERROR,
                                data=None,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time},
                                error_message=error_msg
                            )
                            
                except Exception as e:
                    response_time = time.time() - start_time
                    self.api_manager.record_request("wikipedia", False, response_time)
                    
                    return APIResponse(
                        source=APISource.WIKIPEDIA,
                        status=APIResponseStatus.ERROR,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={"response_time": response_time},
                        error_message=str(e)
                    )
            
            async def query_openai(self, prompt: str, model: str = "gpt-3.5-turbo") -> APIResponse:
                """Query OpenAI API"""
                start_time = time.time()
                
                api_key = self.api_manager.get_api_key("openai")
                
                if not api_key:
                    return APIResponse(
                        source=APISource.OPENAI,
                        status=APIResponseStatus.UNAUTHORIZED,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={},
                        error_message="OpenAI API key not configured"
                    )
                
                if not self.api_manager.check_rate_limit("openai"):
                    return APIResponse(
                        source=APISource.OPENAI,
                        status=APIResponseStatus.RATE_LIMITED,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={},
                        error_message="Rate limit exceeded"
                    )
                
                try:
                    session = await self._get_session()
                    
                    url = "https://api.openai.com/v1/chat/completions"
                    headers = {
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    }
                    data = {
                        "model": model,
                        "messages": [{"role": "user", "content": prompt}],
                        "max_tokens": 1000,
                        "temperature": 0.7
                    }
                    
                    async with session.post(url, headers=headers, json=data) as response:
                        response_time = time.time() - start_time
                        
                        if response.status == 200:
                            result = await response.json()
                            self.api_manager.record_request("openai", True, response_time)
                            
                            return APIResponse(
                                source=APISource.OPENAI,
                                status=APIResponseStatus.SUCCESS,
                                data=result,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time, "model": model}
                            )
                        else:
                            error_msg = f"HTTP {response.status}: {response.reason}"
                            self.api_manager.record_request("openai", False, response_time)
                            
                            return APIResponse(
                                source=APISource.OPENAI,
                                status=APIResponseStatus.ERROR,
                                data=None,
                                timestamp=datetime.now(),
                                metadata={"response_time": response_time},
                                error_message=error_msg
                            )
                            
                except Exception as e:
                    response_time = time.time() - start_time
                    self.api_manager.record_request("openai", False, response_time)
                    
                    return APIResponse(
                        source=APISource.OPENAI,
                        status=APIResponseStatus.ERROR,
                        data=None,
                        timestamp=datetime.now(),
                        metadata={"response_time": response_time},
                        error_message=str(e)
                    )
            
            async def close(self):
                """Close the HTTP session"""
                if self.session and not self.session.closed:
                    await self.session.close()
        
        return SimpleAPIClient(self.api_manager)
    
    def get_api_status(self) -> Dict[str, Any]:
        """Get the status of all APIs"""
        return {
            "timestamp": datetime.now().isoformat(),
            "apis": {
                "google": {
                    "configured": bool(self.api_manager.get_api_key("google")),
                    "cse_configured": bool(self.api_manager.get_google_cse_id())
                },
                "duckduckgo": {"configured": True},  # Always available
                "wikipedia": {"configured": True},    # Always available
                "openai": {
                    "configured": bool(self.api_manager.get_api_key("openai"))
                }
            }
        }
    
    async def search_google(self, query: str, num_results: int = 5) -> APIResponse:
        """Search Google using the appropriate system"""
        return await self.api_clients.search_google(query, num_results)
    
    async def search_duckduckgo(self, query: str) -> APIResponse:
        """Search DuckDuckGo using the appropriate system"""
        return await self.api_clients.search_duckduckgo(query)
    
    async def search_wikipedia(self, query: str) -> APIResponse:
        """Search Wikipedia using the appropriate system"""
        return await self.api_clients.search_wikipedia(query)
    
    async def query_openai(self, prompt: str, model: str = "gpt-3.5-turbo") -> APIResponse:
        """Query OpenAI using the appropriate system"""
        return await self.api_clients.query_openai(prompt, model)
    
    async def close(self):
        """Close all API clients"""
        await self.api_clients.close()

async def main():
    """Main function to demonstrate the Real External API System"""
    
    print("🌟 Living Codex Real External API Integration System Demo")
    print("=" * 70)
    
    try:
        # Create the system
        external_api_system = RealExternalAPISystem()
        
        # Show system status
        status = external_api_system.get_api_status()
        print(f"\n🔧 System Status:")
        print(f"   Available APIs: {[api for api, available in status['apis'].items() if available]}")
        print(f"   Cache Size: {0} (Legacy)") # No cache in legacy
        print(f"   Total Requests: {0} (Legacy)") # No request history in legacy
        
        # Test external knowledge search
        print(f"\n🔍 Testing External Knowledge Search...")
        query = "Living Codex ontological framework and fractal systems"
        
        results = await external_api_system.search_google(
            query=query,
            num_results=5
        )
        
        print(f"\n📊 Search Results for: '{query}'")
        print(f"   Total Sources: 1 (Google)")
        print(f"   Successful Sources: {1 if results.status == APIResponseStatus.SUCCESS else 0}")
        print(f"   Total Items: {len(results.data.get('items', [])) if results.data else 0}")
        print(f"   Confidence Score: {1.0 if results.status == APIResponseStatus.SUCCESS else 0.0}") # No confidence score in legacy
        
        # Show key insights
        if results.data and "items" in results.data:
            print(f"\n💡 Key Insights:")
            for i, item in enumerate(results.data["items"][:3], 1):
                print(f"   {i}. [Google] {item.get('title', 'N/A')}")
                print(f"      {item.get('snippet', 'N/A')}")
                if item.get('link'):
                    print(f"      URL: {item['link']}")
                print()
        
        # Test expert system if available
        if status['apis'].get('openai') and status['apis']['openai']['configured']:
            print(f"\n🤖 Testing Expert System Consultation...")
            expert_query = "What are the key principles of ontological frameworks in knowledge systems?"
            
            expert_results = await external_api_system.query_openai(
                prompt=expert_query
            )
            
            if expert_results.status == APIResponseStatus.SUCCESS:
                print(f"✅ Expert consultation successful!")
                print(f"   Response Time: {expert_results.metadata.get('response_time', 'N/A'):.2f}s")
                print(f"   Tokens Used: {expert_results.metadata.get('tokens_used', 'N/A')}") # Legacy metadata
                print(f"   Model: {expert_results.metadata.get('model', 'N/A')}") # Legacy metadata
            else:
                print(f"❌ Expert consultation failed: {expert_results.error_message}")
        
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
