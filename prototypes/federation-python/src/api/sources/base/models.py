"""
Base API Models
Common data models for API responses and requests
"""

from typing import Any, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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
    source: str
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
    source: str
    status: APIResponseStatus
    data: Any
    headers: Dict[str, str]
    status_code: int
    response_time: float
    timestamp: datetime
    metadata: Dict[str, Any]
