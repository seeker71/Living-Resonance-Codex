"""
Neo4j Connection Manager
Manages Neo4j database connections and connection pooling
"""

import os
import logging
from typing import Optional
from neo4j import GraphDatabase, Driver, Session
from neo4j.exceptions import ServiceUnavailable, AuthError

logger = logging.getLogger(__name__)

class Neo4jConnectionManager:
    """Manages Neo4j database connections and connection pooling"""
    
    def __init__(self, uri: str = None, username: str = None, password: str = None):
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.username = username or os.getenv("NEO4J_USERNAME", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD", "password")
        self.driver: Optional[Driver] = None
        self.connection_pool_size = 10
        self.max_connection_lifetime = 3600  # 1 hour
        self.connection_timeout = 30
        self._initialize_connection()
    
    def _initialize_connection(self):
        """Initialize the Neo4j driver connection"""
        try:
            self.driver = GraphDatabase.driver(
                self.uri,
                auth=(self.username, self.password),
                max_connection_pool_size=self.connection_pool_size,
                max_connection_lifetime=self.max_connection_lifetime,
                connection_timeout=self.connection_timeout
            )
            
            # Test the connection
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                test_value = result.single()["test"]
                if test_value == 1:
                    logger.info(f"✅ Neo4j connection established: {self.uri}")
                else:
                    logger.error("❌ Neo4j connection test failed")
                    self.driver = None
                    
        except ServiceUnavailable as e:
            logger.error(f"❌ Neo4j service unavailable: {e}")
            self.driver = None
        except AuthError as e:
            logger.error(f"❌ Neo4j authentication failed: {e}")
            self.driver = None
        except Exception as e:
            logger.error(f"❌ Neo4j connection error: {e}")
            self.driver = None
    
    def is_connected(self) -> bool:
        """Check if the Neo4j connection is active"""
        if not self.driver:
            return False
        
        try:
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                return result.single()["test"] == 1
        except Exception:
            return False
    
    def get_session(self) -> Optional[Session]:
        """Get a new Neo4j session"""
        if not self.is_connected():
            return None
        return self.driver.session()
    
    def close_connection(self):
        """Close the Neo4j connection"""
        if self.driver:
            self.driver.close()
            self.driver = None
            logger.info("Neo4j connection closed")
    
    def get_connection_info(self) -> dict:
        """Get connection information"""
        return {
            "uri": self.uri,
            "username": self.username,
            "connected": self.is_connected(),
            "pool_size": self.connection_pool_size,
            "max_lifetime": self.max_connection_lifetime,
            "timeout": self.connection_timeout
        }
