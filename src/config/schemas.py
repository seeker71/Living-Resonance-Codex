"""
Configuration Schemas
Data models for system configuration
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class APIConfig:
    """API configuration settings"""
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-3.5-turbo"
    google_api_key: Optional[str] = None
    google_cse_id: Optional[str] = None
    wikipedia_rate_limit: int = 100
    duckduckgo_rate_limit: int = 100

@dataclass
class DatabaseConfig:
    """Database configuration settings"""
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_username: str = "neo4j"
    neo4j_password: Optional[str] = None
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_database: str = "living_codex"
    postgres_username: Optional[str] = None
    postgres_password: Optional[str] = None

@dataclass
class SystemConfig:
    """System configuration settings"""
    cache_ttl: int = 3600
    rate_limit: int = 100
    log_level: str = "INFO"
