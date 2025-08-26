"""
Configuration Manager
Centralized configuration management for the Living Codex system
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path
from .schemas import APIConfig, DatabaseConfig, SystemConfig

class ConfigManager:
    """Manages all configuration for the Living Codex system"""

    def __init__(self, env_file: str = ".env"):
        self.env_file = env_file
        self.api_config = APIConfig()
        self.db_config = DatabaseConfig()
        self.system_config = SystemConfig()
        self._load_configuration()

    def _load_env_file(self):
        """Load configuration from .env file"""
        env_path = Path(self.env_file)
        if env_path.exists():
            print(f"📁 Loading configuration from {env_path}")
            with open(env_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key] = value
        else:
            print(f"⚠️  No .env file found at {env_path}")
            print("   You can create one based on env_example.txt")

    def _load_from_environment(self):
        """Load configuration from environment variables"""
        # API Configuration
        self.api_config.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.api_config.openai_model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        self.api_config.google_api_key = os.getenv('GOOGLE_API_KEY')
        self.api_config.google_cse_id = os.getenv('GOOGLE_CSE_ID')
        self.api_config.wikipedia_rate_limit = int(os.getenv('WIKIPEDIA_RATE_LIMIT', '100'))
        self.api_config.duckduckgo_rate_limit = int(os.getenv('DUCKDUCKGO_RATE_LIMIT', '100'))

        # Database Configuration
        self.db_config.neo4j_uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
        self.db_config.neo4j_username = os.getenv('NEO4J_USERNAME', 'neo4j')
        self.db_config.neo4j_password = os.getenv('NEO4J_PASSWORD')
        self.db_config.postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
        self.db_config.postgres_port = int(os.getenv('POSTGRES_PORT', '5432'))
        self.db_config.postgres_database = os.getenv('POSTGRES_DATABASE', 'living_codex')
        self.db_config.postgres_username = os.getenv('POSTGRES_USERNAME')
        self.db_config.postgres_password = os.getenv('POSTGRES_PASSWORD')

        # System Configuration
        self.system_config.cache_ttl = int(os.getenv('SYSTEM_CACHE_TTL', '3600'))
        self.system_config.rate_limit = int(os.getenv('SYSTEM_RATE_LIMIT', '100'))
        self.system_config.log_level = os.getenv('SYSTEM_LOG_LEVEL', 'INFO')

    def _validate_configuration(self):
        """Validate the loaded configuration"""
        print("\n🔍 Configuration Validation:")

        # Check OpenAI
        if self.api_config.openai_api_key:
            print("✅ OpenAI API key configured")
        else:
            print("⚠️  OpenAI API key not configured (some features will be limited)")

        # Check Google (optional)
        if self.api_config.google_api_key and self.api_config.google_cse_id:
            print("✅ Google Custom Search configured")
        else:
            print("ℹ️  Google Custom Search not configured (will use DuckDuckGo)")

        # Check Neo4j
        if self.db_config.neo4j_password:
            print("✅ Neo4j password configured")
        else:
            print("⚠️  Neo4j password not configured (graph features will be limited)")

        # Check PostgreSQL (optional)
        if self.db_config.postgres_username and self.db_config.postgres_password:
            print("✅ PostgreSQL configured")
        else:
            print("ℹ️  PostgreSQL not configured (will use SQLite)")

        print()

    def _load_configuration(self):
        """Load and validate configuration"""
        self._load_env_file()
        self._load_from_environment()
        self._validate_configuration()

    # Configuration Access Methods
    def get_api_config(self) -> APIConfig:
        """Get API configuration"""
        return self.api_config

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration"""
        return self.db_config

    def get_system_config(self) -> SystemConfig:
        """Get system configuration"""
        return self.system_config

    # Configuration Status Methods
    def is_openai_configured(self) -> bool:
        """Check if OpenAI is properly configured"""
        return bool(self.api_config.openai_api_key)

    def is_google_configured(self) -> bool:
        """Check if Google Custom Search is properly configured"""
        return bool(self.api_config.google_api_key and self.api_config.google_cse_id)

    def is_neo4j_configured(self) -> bool:
        """Check if Neo4j is properly configured"""
        return bool(self.db_config.neo4j_password)

    def is_postgres_configured(self) -> bool:
        """Check if PostgreSQL is properly configured"""
        return bool(self.db_config.postgres_username and self.db_config.postgres_password)

    # Configuration Management Methods
    def create_env_file(self, output_file: str = ".env"):
        """Create a .env file with current configuration"""
        env_content = f"""# Living Codex Configuration
# Generated by ConfigManager

# OpenAI API Configuration
OPENAI_API_KEY={self.api_config.openai_api_key or 'your_openai_api_key_here'}
OPENAI_MODEL={self.api_config.openai_model}

# Google Custom Search API (Optional)
GOOGLE_API_KEY={self.api_config.google_api_key or 'your_google_api_key_here'}
GOOGLE_CSE_ID={self.api_config.google_cse_id or 'your_custom_search_engine_id_here'}

# Wikipedia API (No key required)
WIKIPEDIA_RATE_LIMIT={self.api_config.wikipedia_rate_limit}

# DuckDuckGo (No key required)
DUCKDUCKGO_RATE_LIMIT={self.api_config.duckduckgo_rate_limit}

# Neo4j Database Configuration
NEO4J_URI={self.db_config.neo4j_uri}
NEO4J_USERNAME={self.db_config.neo4j_username}
NEO4J_PASSWORD={self.db_config.neo4j_password or 'your_neo4j_password_here'}

# PostgreSQL Database Configuration (Optional)
POSTGRES_HOST={self.db_config.postgres_host}
POSTGRES_PORT={self.db_config.postgres_port}
POSTGRES_DATABASE={self.db_config.postgres_database}
POSTGRES_USERNAME={self.db_config.postgres_username or 'your_username'}
POSTGRES_PASSWORD={self.db_config.postgres_password or 'your_password'}

# System Configuration
SYSTEM_CACHE_TTL={self.system_config.cache_ttl}
SYSTEM_RATE_LIMIT={self.system_config.rate_limit}
SYSTEM_LOG_LEVEL={self.system_config.log_level}
"""

        with open(output_file, 'w') as f:
            f.write(env_content)

        print(f"📝 Created .env file at {output_file}")
        return output_file

    def get_config_summary(self) -> Dict[str, Any]:
        """Get a summary of current configuration status"""
        return {
            "openai_configured": self.is_openai_configured(),
            "google_configured": self.is_google_configured(),
            "neo4j_configured": self.is_neo4j_configured(),
            "postgres_configured": self.is_postgres_configured(),
            "total_configured": sum([
                self.is_openai_configured(),
                self.is_google_configured(),
                self.is_neo4j_configured(),
                self.is_postgres_configured()
            ])
        }
