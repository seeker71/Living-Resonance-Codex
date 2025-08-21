"""
Configuration Manager for Living Codex
Handles environment variables, API keys, and system configuration
"""

import os
from typing import Optional, Dict, Any
from dataclasses import dataclass
from pathlib import Path

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

class ConfigManager:
    """Manages all configuration for the Living Codex system"""
    
    def __init__(self, env_file: str = ".env"):
        self.env_file = env_file
        self.api_config = APIConfig()
        self.db_config = DatabaseConfig()
        self.system_config = SystemConfig()
        self._load_configuration()
    
    def _load_configuration(self):
        """Load configuration from environment variables and .env file"""
        # Try to load .env file if it exists
        self._load_env_file()
        
        # Load from environment variables (these override .env file)
        self._load_from_environment()
        
        # Validate configuration
        self._validate_configuration()
    
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
    
    def get_api_config(self) -> APIConfig:
        """Get API configuration"""
        return self.api_config
    
    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration"""
        return self.db_config
    
    def get_system_config(self) -> SystemConfig:
        """Get system configuration"""
        return self.system_config
    
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

def main():
    """Test the configuration manager"""
    print("🔧 Living Codex Configuration Manager")
    print("=" * 50)
    
    config = ConfigManager()
    
    print("\n📊 Current Configuration:")
    print(f"OpenAI Configured: {config.is_openai_configured()}")
    print(f"Google Configured: {config.is_google_configured()}")
    print(f"Neo4j Configured: {config.is_neo4j_configured()}")
    print(f"PostgreSQL Configured: {config.is_postgres_configured()}")
    
    print("\n💡 To configure your system:")
    print("1. Copy env_example.txt to .env")
    print("2. Fill in your API keys and passwords")
    print("3. Restart the system")
    
    # Offer to create .env file
    if not Path(".env").exists():
        create = input("\n❓ Create .env file now? (y/n): ").lower()
        if create == 'y':
            config.create_env_file()

if __name__ == "__main__":
    main()
