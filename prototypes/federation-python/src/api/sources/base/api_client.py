"""
Base API Client
Common functionality for all API integrations
"""

import time
import requests
import aiohttp
import asyncio
from typing import Optional, Dict, Any
from datetime import datetime
from .models import APIRequest, APIResponse, APIResponseStatus

class BaseAPIClient:
    """Base class for API clients with common functionality"""
    
    def __init__(self, base_url: str = None, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.cache = {}
        self.cache_ttl = 300  # 5 minutes default cache
    
    def make_request(self, request: APIRequest) -> APIResponse:
        """Make a synchronous HTTP request"""
        start_time = time.time()
        
        try:
            url = f"{self.base_url}{request.endpoint}" if self.base_url else request.endpoint
            
            response = self.session.request(
                method=request.method,
                url=url,
                headers=request.headers or {},
                params=request.params,
                json=request.data if request.method in ['POST', 'PUT', 'PATCH'] else None,
                timeout=request.timeout or self.timeout
            )
            
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                status = APIResponseStatus.SUCCESS
                try:
                    data = response.json()
                except ValueError:
                    data = response.text
            elif response.status_code == 429:
                status = APIResponseStatus.RATE_LIMITED
                data = None
            else:
                status = APIResponseStatus.ERROR
                data = None
            
            return APIResponse(
                source=request.source,
                status=status,
                data=data,
                headers=dict(response.headers),
                status_code=response.status_code,
                response_time=response_time,
                timestamp=datetime.now(),
                metadata={
                    "url": url,
                    "method": request.method,
                    "params": request.params
                }
            )
            
        except requests.exceptions.Timeout:
            return APIResponse(
                source=request.source,
                status=APIResponseStatus.TIMEOUT,
                data=None,
                headers={},
                status_code=408,
                response_time=time.time() - start_time,
                timestamp=datetime.now(),
                metadata={"error": "Request timeout"}
            )
            
        except Exception as e:
            return APIResponse(
                source=request.source,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=time.time() - start_time,
                timestamp=datetime.now(),
                metadata={"error": str(e)}
            )
    
    async def make_async_request(self, request: APIRequest) -> APIResponse:
        """Make an asynchronous HTTP request"""
        start_time = time.time()
        
        try:
            url = f"{self.base_url}{request.endpoint}" if self.base_url else request.endpoint
            
            async with aiohttp.ClientSession() as session:
                async with session.request(
                    method=request.method,
                    url=url,
                    headers=request.headers or {},
                    params=request.params,
                    json=request.data if request.method in ['POST', 'PUT', 'PATCH'] else None,
                    timeout=aiohttp.ClientTimeout(total=request.timeout or self.timeout)
                ) as response:
                    
                    response_time = time.time() - start_time
                    
                    if response.status == 200:
                        status = APIResponseStatus.SUCCESS
                        try:
                            data = await response.json()
                        except ValueError:
                            data = await response.text()
                    elif response.status == 429:
                        status = APIResponseStatus.RATE_LIMITED
                        data = None
                    else:
                        status = APIResponseStatus.ERROR
                        data = None
                    
                    return APIResponse(
                        source=request.source,
                        status=status,
                        data=data,
                        headers=dict(response.headers),
                        status_code=response.status,
                        response_time=response_time,
                        timestamp=datetime.now(),
                        metadata={
                            "url": url,
                            "method": request.method,
                            "params": request.params
                        }
                    )
                    
        except asyncio.TimeoutError:
            return APIResponse(
                source=request.source,
                status=APIResponseStatus.TIMEOUT,
                data=None,
                headers={},
                status_code=408,
                response_time=time.time() - start_time,
                timestamp=datetime.now(),
                metadata={"error": "Request timeout"}
            )
            
        except Exception as e:
            return APIResponse(
                source=request.source,
                status=APIResponseStatus.ERROR,
                data=None,
                headers={},
                status_code=500,
                response_time=time.time() - start_time,
                timestamp=datetime.now(),
                metadata={"error": str(e)}
            )
    
    def get_cached_response(self, cache_key: str) -> Optional[APIResponse]:
        """Get a cached response if still valid"""
        if cache_key not in self.cache:
            return None
        
        cached_response, cached_time = self.cache[cache_key]
        
        if time.time() - cached_time > self.cache_ttl:
            del self.cache[cache_key]
            return None
        
        return cached_response
    
    def cache_response(self, cache_key: str, response: APIResponse):
        """Cache a response"""
        self.cache[cache_key] = (response, time.time())
        
        # Limit cache size
        if len(self.cache) > 1000:
            # Remove oldest entries
            oldest_keys = sorted(self.cache.keys(), 
                               key=lambda k: self.cache[k][1])[:100]
            for key in oldest_keys:
                del self.cache[key]
