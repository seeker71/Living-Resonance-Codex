"""
Request Tracker
Track and analyze API request patterns and performance
"""

import time
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum

class RequestStatus(Enum):
    """Request execution status"""
    SUCCESS = "success"
    FAILED = "failed"
    RATE_LIMITED = "rate_limited"
    TIMEOUT = "timeout"
    ERROR = "error"

@dataclass
class RequestRecord:
    """Record of an API request"""
    source: str
    timestamp: datetime
    status: RequestStatus
    response_time: float
    status_code: Optional[int] = None
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class RequestTracker:
    """Track and analyze API request patterns"""
    
    def __init__(self, max_records: int = 10000):
        self.max_records = max_records
        self.records: List[RequestRecord] = []
        self.metrics_cache = {}
        self.cache_ttl = 60  # Cache metrics for 1 minute
    
    def record_request(self, source: str, status: RequestStatus, 
                      response_time: float, status_code: Optional[int] = None,
                      error_message: Optional[str] = None, 
                      metadata: Optional[Dict[str, Any]] = None):
        """Record a new API request"""
        record = RequestRecord(
            source=source,
            timestamp=datetime.now(),
            status=status,
            response_time=response_time,
            status_code=status_code,
            error_message=error_message,
            metadata=metadata
        )
        
        self.records.append(record)
        
        # Limit memory usage by keeping only recent records
        if len(self.records) > self.max_records:
            self.records = self.records[-self.max_records:]
        
        # Clear cache when new data arrives
        self.metrics_cache = {}
    
    def get_success_rate(self, source: str, hours: int = 24) -> float:
        """Get success rate for a source over the last N hours"""
        cutoff = datetime.now() - timedelta(hours=hours)
        recent_records = [
            r for r in self.records 
            if r.source == source and r.timestamp > cutoff
        ]
        
        if not recent_records:
            return 0.0
        
        successful = [r for r in recent_records if r.status == RequestStatus.SUCCESS]
        return len(successful) / len(recent_records)
    
    def get_average_response_time(self, source: str, hours: int = 24) -> float:
        """Get average response time for a source"""
        cutoff = datetime.now() - timedelta(hours=hours)
        recent_records = [
            r for r in self.records 
            if r.source == source and r.timestamp > cutoff and r.status == RequestStatus.SUCCESS
        ]
        
        if not recent_records:
            return 0.0
        
        total_time = sum(r.response_time for r in recent_records)
        return total_time / len(recent_records)
    
    def get_request_count(self, source: str, hours: int = 24) -> int:
        """Get total request count for a source"""
        cutoff = datetime.now() - timedelta(hours=hours)
        return len([
            r for r in self.records 
            if r.source == source and r.timestamp > cutoff
        ])
    
    def get_error_summary(self, source: str, hours: int = 24) -> Dict[str, int]:
        """Get error summary for a source"""
        cutoff = datetime.now() - timedelta(hours=hours)
        error_records = [
            r for r in self.records 
            if r.source == source and r.timestamp > cutoff and r.status != RequestStatus.SUCCESS
        ]
        
        error_counts = {}
        for record in error_records:
            error_type = record.status.value
            if record.error_message:
                error_key = f"{error_type}: {record.error_message}"
            else:
                error_key = error_type
            
            error_counts[error_key] = error_counts.get(error_key, 0) + 1
        
        return error_counts
    
    def get_performance_summary(self, source: str, hours: int = 24) -> Dict[str, Any]:
        """Get comprehensive performance summary"""
        cache_key = f"{source}_{hours}_{int(time.time() / self.cache_ttl)}"
        
        if cache_key in self.metrics_cache:
            return self.metrics_cache[cache_key]
        
        summary = {
            "source": source,
            "time_window_hours": hours,
            "total_requests": self.get_request_count(source, hours),
            "success_rate": self.get_success_rate(source, hours),
            "average_response_time": self.get_average_response_time(source, hours),
            "error_summary": self.get_error_summary(source, hours),
            "generated_at": datetime.now().isoformat()
        }
        
        self.metrics_cache[cache_key] = summary
        return summary
    
    def get_all_sources_summary(self, hours: int = 24) -> Dict[str, Dict[str, Any]]:
        """Get performance summary for all sources"""
        sources = set(r.source for r in self.records)
        return {
            source: self.get_performance_summary(source, hours)
            for source in sources
        }
    
    def cleanup_old_records(self, days: int = 7):
        """Remove records older than specified days"""
        cutoff = datetime.now() - timedelta(days=days)
        self.records = [r for r in self.records if r.timestamp > cutoff]
        self.metrics_cache = {}  # Clear cache after cleanup
