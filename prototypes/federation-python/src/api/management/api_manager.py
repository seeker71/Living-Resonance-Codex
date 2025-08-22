"""
API Manager
Core API key management, rate limiting, and authentication
"""

import os
import logging
from typing import Optional, Dict, Any
from datetime import datetime, timedelta
from enum import Enum

# Configure logging
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
            APISource.GOOGLE_SEARCH: os.getenv("GOOGLE_API_KEY"),
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
    
    def get_rate_limit_info(self, source: APISource) -> Dict[str, Any]:
        """Get rate limiting information for a source"""
        if source not in self.request_history:
            return {
                "requests_in_last_minute": 0,
                "requests_remaining": self.rate_limits[source]["requests_per_minute"],
                "rate_limited": False
            }
        
        now = datetime.now()
        window_start = now - timedelta(minutes=1)
        
        recent_requests = [
            req_time for req_time in self.request_history[source]
            if req_time > window_start
        ]
        
        max_requests = self.rate_limits[source]["requests_per_minute"]
        requests_used = len(recent_requests)
        
        return {
            "requests_in_last_minute": requests_used,
            "requests_remaining": max(0, max_requests - requests_used),
            "rate_limited": requests_used >= max_requests
        }
    
    def is_api_available(self, source: APISource) -> bool:
        """Check if an API source is available and configured"""
        api_key = self.get_api_key(source)
        
        # Special handling for APIs that don't need keys
        if source in [APISource.DUCKDUCKGO, APISource.WIKIPEDIA]:
            return True
        
        # Google Search needs both API key and CSE ID
        if source == APISource.GOOGLE_SEARCH:
            return bool(api_key and self.get_google_cse_id())
        
        # Other APIs just need the API key
        return bool(api_key)
