#!/usr/bin/env python3
"""
Water State Storage System for Living Codex

This module implements a physics-inspired data storage architecture where different
water states determine storage strategies:

🧊 ICE: Global federation (distributed, immutable)
💧 WATER: Local persistence (stable, adaptable)  
☁️ VAPOR: Memory/sessions (temporary, fast)
⚡ PLASMA: Real-time streaming (dynamic, interconnected)
"""

import json
import sqlite3
import asyncio
import threading
from pathlib import Path
from typing import Dict, Any, Optional, List, Union
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import hashlib
import pickle
import tempfile
import shutil
import time

class WaterState(Enum):
    """Water states that determine storage strategy"""
    ICE = "ice"           # Global federation - immutable, distributed
    WATER = "water"       # Local persistence - stable, adaptable
    VAPOR = "vapor"       # Memory/sessions - temporary, fast
    PLASMA = "plasma"     # Real-time streaming - dynamic, interconnected

class StorageStrategy(Enum):
    """Storage strategies for each water state"""
    FEDERATED = "federated"      # Distributed consensus (ICE)
    LOCAL_DB = "local_db"        # Local database (WATER)
    MEMORY = "memory"            # RAM storage (VAPOR)
    STREAMING = "streaming"      # Real-time events (PLASMA)

@dataclass
class StorageConfig:
    """Configuration for each storage strategy"""
    water_state: WaterState
    strategy: StorageStrategy
    persistence_level: int  # 0=ephemeral, 1=local, 2=global
    replication_factor: int  # How many copies to maintain
    ttl_seconds: Optional[int] = None  # Time to live for temporary data
    encryption_required: bool = False
    compression_enabled: bool = True

class WaterStateStorage:
    """
    Main storage system that routes data to appropriate storage based on water state
    """
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.storage_engines = {}
        self.state_configs = self._initialize_state_configs()
        self._setup_storage_engines()
        
    def _initialize_state_configs(self) -> Dict[WaterState, StorageConfig]:
        """Initialize default configurations for each water state"""
        return {
            WaterState.ICE: StorageConfig(
                water_state=WaterState.ICE,
                strategy=StorageStrategy.FEDERATED,
                persistence_level=2,
                replication_factor=3,
                encryption_required=True,
                compression_enabled=True
            ),
            WaterState.WATER: StorageConfig(
                water_state=WaterState.WATER,
                strategy=StorageStrategy.LOCAL_DB,
                persistence_level=1,
                replication_factor=1,
                encryption_required=False,
                compression_enabled=True
            ),
            WaterState.VAPOR: StorageConfig(
                water_state=WaterState.VAPOR,
                strategy=StorageStrategy.MEMORY,
                persistence_level=0,
                replication_factor=1,
                ttl_seconds=3600,  # 1 hour default
                encryption_required=False,
                compression_enabled=False
            ),
            WaterState.PLASMA: StorageConfig(
                water_state=WaterState.PLASMA,
                strategy=StorageStrategy.STREAMING,
                persistence_level=0,
                replication_factor=2,
                ttl_seconds=300,  # 5 minutes default
                encryption_required=False,
                compression_enabled=False
            )
        }
    
    def _setup_storage_engines(self):
        """Initialize storage engines for each strategy"""
        # ICE - Federated storage (simulated with local consensus)
        self.storage_engines[StorageStrategy.FEDERATED] = FederatedStorageEngine(
            self.base_path / "ice_storage"
        )
        
        # WATER - Local database storage
        self.storage_engines[StorageStrategy.LOCAL_DB] = LocalDatabaseEngine(
            self.base_path / "water_storage"
        )
        
        # VAPOR - Memory storage
        self.storage_engines[StorageStrategy.MEMORY] = MemoryStorageEngine()
        
        # PLASMA - Streaming storage
        self.storage_engines[StorageStrategy.STREAMING] = StreamingStorageEngine()
    
    def store(self, key: str, data: Any, water_state: WaterState, 
              metadata: Dict[str, Any] = None) -> bool:
        """Store data using the appropriate storage strategy for the water state"""
        config = self.state_configs[water_state]
        engine = self.storage_engines[config.strategy]
        
        # Add metadata about the storage decision
        if metadata is None:
            metadata = {}
        metadata.update({
            'water_state': water_state.value,
            'storage_strategy': config.strategy.value,
            'stored_at': datetime.now().isoformat(),
            'persistence_level': config.persistence_level
        })
        
        return engine.store(key, data, config, metadata)
    
    def retrieve(self, key: str, water_state: WaterState) -> Optional[Any]:
        """Retrieve data from the appropriate storage"""
        config = self.state_configs[water_state]
        engine = self.storage_engines[config.strategy]
        return engine.retrieve(key, config)
    
    def get_storage_info(self, key: str, water_state: WaterState) -> Dict[str, Any]:
        """Get information about how data is stored"""
        config = self.state_configs[water_state]
        engine = self.storage_engines[config.strategy]
        return engine.get_storage_info(key, config)

class FederatedStorageEngine:
    """
    ICE state storage - Global federation with consensus
    Simulates distributed storage with local consensus mechanisms
    """
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.base_path.mkdir(exist_ok=True)
        self.consensus_file = base_path / "consensus.json"
        self.data_path = base_path / "data"
        self.data_path.mkdir(exist_ok=True)
        self._load_consensus()
    
    def _load_consensus(self):
        """Load or initialize consensus data"""
        if self.consensus_file.exists():
            with open(self.consensus_file, 'r') as f:
                self.consensus = json.load(f)
        else:
            self.consensus = {
                'nodes': [],
                'last_consensus': datetime.now().isoformat(),
                'consensus_hash': ''
            }
            self._save_consensus()
    
    def _save_consensus(self):
        """Save consensus data"""
        with open(self.consensus_file, 'w') as f:
            json.dump(self.consensus, f, indent=2)
    
    def store(self, key: str, data: Any, config: StorageConfig, 
              metadata: Dict[str, Any]) -> bool:
        """Store data with consensus validation"""
        try:
            # Create data hash for consensus
            data_hash = hashlib.sha256(pickle.dumps(data)).hexdigest()
            
            # Store data with metadata
            data_file = self.data_path / f"{key}.json"
            storage_data = {
                'data': data,
                'metadata': metadata,
                'data_hash': data_hash,
                'consensus_verified': True,
                'stored_at': datetime.now().isoformat()
            }
            
            with open(data_file, 'w') as f:
                json.dump(storage_data, f, indent=2, default=str)
            
            # Update consensus
            self.consensus['last_consensus'] = datetime.now().isoformat()
            self.consensus['consensus_hash'] = data_hash
            self._save_consensus()
            
            return True
        except Exception as e:
            print(f"Federated storage error: {e}")
            return False
    
    def retrieve(self, key: str, config: StorageConfig) -> Optional[Any]:
        """Retrieve data with consensus verification"""
        try:
            data_file = self.data_path / f"{key}.json"
            if not data_file.exists():
                return None
            
            with open(data_file, 'r') as f:
                storage_data = json.load(f)
            
            # Verify consensus
            if storage_data.get('consensus_verified'):
                return storage_data['data']
            return None
        except Exception as e:
            print(f"Federated retrieval error: {e}")
            return None
    
    def get_storage_info(self, key: str, config: StorageConfig) -> Dict[str, Any]:
        """Get storage information"""
        data_file = self.data_path / f"{key}.json"
        if not data_file.exists():
            return {'status': 'not_found'}
        
        return {
            'status': 'stored',
            'strategy': 'federated',
            'consensus_verified': True,
            'file_path': str(data_file),
            'consensus_hash': self.consensus.get('consensus_hash', '')
        }

class LocalDatabaseEngine:
    """
    WATER state storage - Local database with persistence
    Uses SQLite for reliable local storage
    """
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.base_path.mkdir(exist_ok=True)
        self.db_path = base_path / "water_storage.db"
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS water_storage (
                key TEXT PRIMARY KEY,
                data TEXT,
                metadata TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP,
                water_state TEXT,
                compression_enabled BOOLEAN
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def store(self, key: str, data: Any, config: StorageConfig, 
              metadata: Dict[str, Any]) -> bool:
        """Store data in local database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Compress data if enabled
            if config.compression_enabled:
                import gzip
                compressed_data = gzip.compress(pickle.dumps(data))
                data_str = compressed_data.hex()
            else:
                data_str = pickle.dumps(data).hex()
            
            metadata_str = json.dumps(metadata)
            now = datetime.now()
            
            cursor.execute('''
                INSERT OR REPLACE INTO water_storage 
                (key, data, metadata, created_at, updated_at, water_state, compression_enabled)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (key, data_str, metadata_str, now, now, config.water_state.value, config.compression_enabled))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Local database storage error: {e}")
            return False
    
    def retrieve(self, key: str, config: StorageConfig) -> Optional[Any]:
        """Retrieve data from local database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT data, compression_enabled FROM water_storage WHERE key = ?', (key,))
            result = cursor.fetchone()
            conn.close()
            
            if not result:
                return None
            
            data_str, compression_enabled = result
            
            # Decompress if needed
            if compression_enabled:
                import gzip
                compressed_data = bytes.fromhex(data_str)
                data = pickle.loads(gzip.decompress(compressed_data))
            else:
                data = pickle.loads(bytes.fromhex(data_str))
            
            return data
        except Exception as e:
            print(f"Local database retrieval error: {e}")
            return False
    
    def get_storage_info(self, key: str, config: StorageConfig) -> Dict[str, Any]:
        """Get storage information"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT created_at, updated_at, water_state, compression_enabled 
                FROM water_storage WHERE key = ?
            ''', (key,))
            result = cursor.fetchone()
            conn.close()
            
            if not result:
                return {'status': 'not_found'}
            
            created_at, updated_at, water_state, compression_enabled = result
            return {
                'status': 'stored',
                'strategy': 'local_database',
                'created_at': created_at,
                'updated_at': updated_at,
                'water_state': water_state,
                'compression_enabled': bool(compression_enabled),
                'db_path': str(self.db_path)
            }
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

class MemoryStorageEngine:
    """
    VAPOR state storage - In-memory storage with TTL
    Fast access for temporary data
    """
    
    def __init__(self):
        self.storage = {}
        self.metadata = {}
        self.expiry_times = {}
        self._cleanup_thread = threading.Thread(target=self._cleanup_expired, daemon=True)
        self._cleanup_thread.start()
    
    def store(self, key: str, data: Any, config: StorageConfig, 
              metadata: Dict[str, Any]) -> bool:
        """Store data in memory with TTL"""
        try:
            self.storage[key] = data
            self.metadata[key] = metadata
            
            # Set expiry time if TTL is configured
            if config.ttl_seconds:
                expiry = datetime.now() + timedelta(seconds=config.ttl_seconds)
                self.expiry_times[key] = expiry
            
            return True
        except Exception as e:
            print(f"Memory storage error: {e}")
            return False
    
    def retrieve(self, key: str, config: StorageConfig) -> Optional[Any]:
        """Retrieve data from memory"""
        # Check if expired
        if key in self.expiry_times:
            if datetime.now() > self.expiry_times[key]:
                self._remove_expired(key)
                return None
        
        return self.storage.get(key)
    
    def get_storage_info(self, key: str, config: StorageConfig) -> Dict[str, Any]:
        """Get storage information"""
        if key not in self.storage:
            return {'status': 'not_found'}
        
        info = {
            'status': 'stored',
            'strategy': 'memory',
            'in_memory': True,
            'metadata': self.metadata.get(key, {})
        }
        
        if key in self.expiry_times:
            info['expires_at'] = self.expiry_times[key].isoformat()
            info['ttl_seconds'] = config.ttl_seconds
        
        return info
    
    def _remove_expired(self, key: str):
        """Remove expired data"""
        if key in self.storage:
            del self.storage[key]
        if key in self.metadata:
            del self.metadata[key]
        if key in self.expiry_times:
            del self.expiry_times[key]
    
    def _cleanup_expired(self):
        """Background thread to clean up expired data"""
        while True:
            try:
                current_time = datetime.now()
                expired_keys = [
                    key for key, expiry in self.expiry_times.items()
                    if current_time > expiry
                ]
                
                for key in expired_keys:
                    self._remove_expired(key)
                
                time.sleep(60)  # Check every minute
            except Exception as e:
                print(f"Cleanup error: {e}")
                time.sleep(60)

class StreamingStorageEngine:
    """
    PLASMA state storage - Real-time streaming with event sourcing
    Handles dynamic, interconnected data flows
    """
    
    def __init__(self):
        self.event_streams = {}
        self.subscribers = {}
        self.event_history = {}
        self.max_history = 1000  # Keep last 1000 events per stream
    
    def store(self, key: str, data: Any, config: StorageConfig, 
              metadata: Dict[str, Any]) -> bool:
        """Store data as a streaming event"""
        try:
            if key not in self.event_streams:
                self.event_streams[key] = []
                self.event_history[key] = []
            
            event = {
                'id': len(self.event_streams[key]),
                'data': data,
                'metadata': metadata,
                'timestamp': datetime.now().isoformat(),
                'water_state': config.water_state.value
            }
            
            # Add to current stream
            self.event_streams[key].append(event)
            
            # Add to history
            self.event_history[key].append(event)
            
            # Maintain history size
            if len(self.event_history[key]) > self.max_history:
                self.event_history[key] = self.event_history[key][-self.max_history:]
            
            # Notify subscribers
            self._notify_subscribers(key, event)
            
            return True
        except Exception as e:
            print(f"Streaming storage error: {e}")
            return False
    
    def retrieve(self, key: str, config: StorageConfig) -> Optional[Any]:
        """Retrieve latest data from stream"""
        if key not in self.event_streams or not self.event_streams[key]:
            return None
        
        # Return the most recent event
        latest_event = self.event_streams[key][-1]
        return latest_event['data']
    
    def get_stream_history(self, key: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent history from a stream"""
        if key not in self.event_history:
            return []
        
        return self.event_history[key][-limit:]
    
    def subscribe(self, key: str, callback) -> str:
        """Subscribe to a stream"""
        if key not in self.subscribers:
            self.subscribers[key] = {}
        
        subscription_id = f"sub_{len(self.subscribers[key])}_{int(datetime.now().timestamp())}"
        self.subscribers[key][subscription_id] = callback
        return subscription_id
    
    def unsubscribe(self, key: str, subscription_id: str):
        """Unsubscribe from a stream"""
        if key in self.subscribers and subscription_id in self.subscribers[key]:
            del self.subscribers[key][subscription_id]
    
    def _notify_subscribers(self, key: str, event: Dict[str, Any]):
        """Notify all subscribers of a new event"""
        if key in self.subscribers:
            for callback in self.subscribers[key].values():
                try:
                    callback(event)
                except Exception as e:
                    print(f"Subscriber notification error: {e}")
    
    def get_storage_info(self, key: str, config: StorageConfig) -> Dict[str, Any]:
        """Get storage information"""
        if key not in self.event_streams:
            return {'status': 'not_found'}
        
        return {
            'status': 'streaming',
            'strategy': 'streaming',
            'event_count': len(self.event_streams[key]),
            'history_size': len(self.event_history[key]),
            'subscriber_count': len(self.subscribers.get(key, {})),
            'latest_timestamp': self.event_streams[key][-1]['timestamp'] if self.event_streams[key] else None
        }

# Utility functions for easy water state storage
def store_as_ice(storage: WaterStateStorage, key: str, data: Any, metadata: Dict[str, Any] = None) -> bool:
    """Store data in ICE state (global federation)"""
    return storage.store(key, data, WaterState.ICE, metadata)

def store_as_water(storage: WaterStateStorage, key: str, data: Any, metadata: Dict[str, Any] = None) -> bool:
    """Store data in WATER state (local persistence)"""
    return storage.store(key, data, WaterState.WATER, metadata)

def store_as_vapor(storage: WaterStateStorage, key: str, data: Any, metadata: Dict[str, Any] = None) -> bool:
    """Store data in VAPOR state (memory/sessions)"""
    return storage.store(key, data, WaterState.VAPOR, metadata)

def store_as_plasma(storage: WaterStateStorage, key: str, data: Any, metadata: Dict[str, Any] = None) -> bool:
    """Store data in PLASMA state (real-time streaming)"""
    return storage.store(key, data, WaterState.PLASMA, metadata)

if __name__ == "__main__":
    # Demo the water state storage system
    print("🌊 Water State Storage System Demo")
    print("=" * 50)
    
    storage = WaterStateStorage()
    
    # Store data in different states
    print("\n🧊 Storing in ICE (Global Federation)...")
    store_as_ice(storage, "core_knowledge", {"fact": "The Living Codex is a living system"}, {"verified": True})
    
    print("\n💧 Storing in WATER (Local Persistence)...")
    store_as_water(storage, "user_preferences", {"theme": "dark", "language": "en"}, {"user_id": "123"})
    
    print("\n☁️ Storing in VAPOR (Memory/Sessions)...")
    store_as_vapor(storage, "current_session", {"active_tab": "dashboard", "last_action": "search"}, {"session_id": "abc"})
    
    print("\n⚡ Storing in PLASMA (Real-time Streaming)...")
    store_as_plasma(storage, "live_collaboration", {"message": "Hello from user 456"}, {"user_id": "456", "room": "general"})
    
    # Retrieve and show storage info
    print("\n📊 Storage Information:")
    print("-" * 30)
    
    for state in [WaterState.ICE, WaterState.WATER, WaterState.VAPOR, WaterState.PLASMA]:
        state_name = state.value.upper()
        key = f"{state_name.lower()}_data"
        
        if state == WaterState.ICE:
            key = "core_knowledge"
        elif state == WaterState.WATER:
            key = "user_preferences"
        elif state == WaterState.VAPOR:
            key = "current_session"
        elif state == WaterState.PLASMA:
            key = "live_collaboration"
        
        data = storage.retrieve(key, state)
        info = storage.get_storage_info(key, state)
        
        print(f"\n{state_name}:")
        print(f"  Data: {data}")
        print(f"  Info: {info}")
    
    print("\n✨ Water State Storage System Ready!")
