"""
Rate Limiter
Advanced rate limiting functionality for API requests
"""

import time
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass
class RateLimitInfo:
    """Rate limiting information"""
    requests_remaining: int
    reset_time: datetime
    window_size: int
    current_usage: int

class RateLimiter:
    """Advanced rate limiting with multiple window support"""
    
    def __init__(self):
        self.request_windows: Dict[str, List[datetime]] = {}
        self.rate_limits: Dict[str, Dict[str, int]] = {}
    
    def set_rate_limit(self, source: str, requests_per_minute: int, requests_per_hour: int = None):
        """Set rate limits for a source"""
        self.rate_limits[source] = {
            "requests_per_minute": requests_per_minute,
            "requests_per_hour": requests_per_hour or requests_per_minute * 60
        }
    
    def can_make_request(self, source: str) -> bool:
        """Check if a request can be made within rate limits"""
        if source not in self.rate_limits:
            return True
        
        now = datetime.now()
        
        # Check minute window
        if not self._check_window(source, now, timedelta(minutes=1), "requests_per_minute"):
            return False
        
        # Check hour window
        if not self._check_window(source, now, timedelta(hours=1), "requests_per_hour"):
            return False
        
        return True
    
    def record_request(self, source: str):
        """Record a request for rate limiting"""
        if source not in self.request_windows:
            self.request_windows[source] = []
        
        self.request_windows[source].append(datetime.now())
        self._cleanup_old_requests(source)
    
    def get_rate_limit_info(self, source: str) -> RateLimitInfo:
        """Get detailed rate limiting information"""
        if source not in self.rate_limits:
            return RateLimitInfo(
                requests_remaining=float('inf'),
                reset_time=datetime.now(),
                window_size=60,
                current_usage=0
            )
        
        now = datetime.now()
        window_start = now - timedelta(minutes=1)
        
        if source not in self.request_windows:
            requests_in_window = 0
        else:
            requests_in_window = len([
                req for req in self.request_windows[source]
                if req > window_start
            ])
        
        max_requests = self.rate_limits[source]["requests_per_minute"]
        
        return RateLimitInfo(
            requests_remaining=max(0, max_requests - requests_in_window),
            reset_time=now + timedelta(minutes=1),
            window_size=60,
            current_usage=requests_in_window
        )
    
    def _check_window(self, source: str, now: datetime, window: timedelta, limit_key: str) -> bool:
        """Check if request fits within a time window"""
        if source not in self.request_windows:
            return True
        
        window_start = now - window
        requests_in_window = [
            req for req in self.request_windows[source]
            if req > window_start
        ]
        
        max_requests = self.rate_limits[source][limit_key]
        return len(requests_in_window) < max_requests
    
    def _cleanup_old_requests(self, source: str):
        """Clean up old request records"""
        if source not in self.request_windows:
            return
        
        # Keep only requests from last 2 hours
        cutoff = datetime.now() - timedelta(hours=2)
        self.request_windows[source] = [
            req for req in self.request_windows[source]
            if req > cutoff
        ]
