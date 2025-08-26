#!/usr/bin/env python3
"""
API-Based Knowledge System with Memory Management
Uses the federated API for knowledge exploration with:
- Long-term memory: System structure and evolution history
- Short-term memory: Question-answer exchanges
- Memory summarization: Compress short-term exchanges into long-term structure
"""

import requests
import json
import time
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
import hashlib
import sqlite3
from dataclasses import dataclass, asdict

@dataclass
class KnowledgeExchange:
    """Represents a knowledge exchange (short-term memory)"""
    exchange_id: str
    question: str
    answer: str
    entities_involved: List[str]
    resonance_score: float
    energy_exchange: float
    timestamp: datetime
    context: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['timestamp'] = self.timestamp.isoformat()
        return data

@dataclass
class MemorySummary:
    """Represents a memory summary (long-term memory)"""
    summary_id: str
    exchange_ids: List[str]
    key_concepts: List[str]
    structural_changes: List[Dict[str, Any]]
    evolution_patterns: List[Dict[str, Any]]
    energy_signature: List[float]
    created_at: datetime
    updated_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

class MemoryManager:
    """Manages long-term and short-term memory with summarization"""
    
    def __init__(self, db_path: str = "knowledge_memory.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the memory database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS short_term_memory (
                    exchange_id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    entities_involved TEXT NOT NULL,
                    resonance_score REAL NOT NULL,
                    energy_exchange REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    context TEXT NOT NULL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS long_term_memory (
                    summary_id TEXT PRIMARY KEY,
                    exchange_ids TEXT NOT NULL,
                    key_concepts TEXT NOT NULL,
                    structural_changes TEXT NOT NULL,
                    evolution_patterns TEXT NOT NULL,
                    energy_signature TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS memory_index (
                    concept TEXT NOT NULL,
                    summary_id TEXT NOT NULL,
                    relevance_score REAL NOT NULL,
                    last_accessed TEXT NOT NULL,
                    PRIMARY KEY (concept, summary_id)
                )
            """)
    
    def store_exchange(self, exchange: KnowledgeExchange):
        """Store a knowledge exchange in short-term memory"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO short_term_memory 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                exchange.exchange_id,
                exchange.question,
                exchange.answer,
                json.dumps(exchange.entities_involved),
                exchange.resonance_score,
                exchange.energy_exchange,
                exchange.timestamp.isoformat(),
                json.dumps(exchange.context)
            ))
    
    def get_exchange(self, exchange_id: str) -> Optional[KnowledgeExchange]:
        """Retrieve a knowledge exchange from short-term memory"""
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("""
                SELECT * FROM short_term_memory WHERE exchange_id = ?
            """, (exchange_id,)).fetchone()
            
            if row:
                return KnowledgeExchange(
                    exchange_id=row[0],
                    question=row[1],
                    answer=row[2],
                    entities_involved=json.loads(row[3]),
                    resonance_score=row[4],
                    energy_exchange=row[5],
                    timestamp=datetime.fromisoformat(row[6]),
                    context=json.loads(row[7])
                )
        return None
    
    def store_summary(self, summary: MemorySummary):
        """Store a memory summary in long-term memory"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO long_term_memory 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                summary.summary_id,
                json.dumps(summary.exchange_ids),
                json.dumps(summary.key_concepts),
                json.dumps(summary.structural_changes),
                json.dumps(summary.evolution_patterns),
                json.dumps(summary.energy_signature),
                summary.created_at.isoformat(),
                summary.updated_at.isoformat()
            ))
            
            # Update memory index
            for concept in summary.key_concepts:
                conn.execute("""
                    INSERT OR REPLACE INTO memory_index 
                    VALUES (?, ?, ?, ?)
                """, (
                    concept,
                    summary.summary_id,
                    1.0,  # Default relevance score
                    datetime.now(timezone.utc).isoformat()
                ))
    
    def get_summary(self, summary_id: str) -> Optional[MemorySummary]:
        """Retrieve a memory summary from long-term memory"""
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("""
                SELECT * FROM long_term_memory WHERE summary_id = ?
            """, (summary_id,)).fetchone()
            
            if row:
                return MemorySummary(
                    summary_id=row[0],
                    exchange_ids=json.loads(row[1]),
                    key_concepts=json.loads(row[2]),
                    structural_changes=json.loads(row[3]),
                    evolution_patterns=json.loads(row[4]),
                    energy_signature=json.loads(row[5]),
                    created_at=datetime.fromisoformat(row[6]),
                    updated_at=datetime.fromisoformat(row[7])
                )
        return None
    
    def search_memory(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search both short-term and long-term memory"""
        results = []
        
        # Search short-term memory
        with sqlite3.connect(self.db_path) as conn:
            short_term_results = conn.execute("""
                SELECT * FROM short_term_memory 
                WHERE question LIKE ? OR answer LIKE ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (f"%{query}%", f"%{query}%", limit // 2)).fetchall()
            
            for row in short_term_results:
                results.append({
                    "type": "short_term",
                    "exchange_id": row[0],
                    "question": row[1],
                    "answer": row[2],
                    "resonance_score": row[4],
                    "timestamp": row[6]
                })
        
        # Search long-term memory
        with sqlite3.connect(self.db_path) as conn:
            long_term_results = conn.execute("""
                SELECT m.*, i.relevance_score 
                FROM long_term_memory m
                JOIN memory_index i ON m.summary_id = i.summary_id
                WHERE i.concept LIKE ?
                ORDER BY i.relevance_score DESC, m.updated_at DESC
                LIMIT ?
            """, (f"%{query}%", limit // 2)).fetchall()
            
            for row in long_term_results:
                results.append({
                    "type": "long_term",
                    "summary_id": row[0],
                    "key_concepts": json.loads(row[2]),
                    "relevance_score": row[7],
                    "updated_at": row[8]
                })
        
        return results

class KnowledgeExplorer:
    """Uses the federated API to explore knowledge and manage memory"""
    
    def __init__(self, api_base_url: str = "http://localhost:8001"):
        self.api_base_url = api_base_url
        self.memory_manager = MemoryManager()
        self.session = requests.Session()
    
    def explore_knowledge(self, question: str, entities: List[str] = None) -> Dict[str, Any]:
        """Explore knowledge using the federated API and store in memory"""
        
        # Generate exchange ID
        exchange_id = self._generate_exchange_id(question, entities)
        
        # Check if we already have this exchange
        existing_exchange = self.memory_manager.get_exchange(exchange_id)
        if existing_exchange:
            return {
                "type": "cached_exchange",
                "exchange": existing_exchange.to_dict(),
                "source": "short_term_memory"
            }
        
        # Use the federated API to explore
        try:
            # Create curiosity question
            curiosity_response = self._create_curiosity_question(question)
            
            # Explore the question
            exploration_response = self._explore_curiosity_question(curiosity_response.get("id"))
            
            # Get system overview for context
            system_overview = self._get_system_overview()
            
            # Create knowledge exchange
            exchange = KnowledgeExchange(
                exchange_id=exchange_id,
                question=question,
                answer=exploration_response.get("exploration_result", "Exploration completed"),
                entities_involved=entities or [],
                resonance_score=exploration_response.get("resonance_score", 0.5),
                energy_exchange=exploration_response.get("energy_impact", 0.0),
                timestamp=datetime.now(timezone.utc),
                context={
                    "curiosity_question": curiosity_response,
                    "exploration": exploration_response,
                    "system_overview": system_overview
                }
            )
            
            # Store in short-term memory
            self.memory_manager.store_exchange(exchange)
            
            # Check if we should create a memory summary
            self._check_memory_summarization()
            
            return {
                "type": "new_exchange",
                "exchange": exchange.to_dict(),
                "source": "federated_api"
            }
            
        except Exception as e:
            return {
                "type": "error",
                "error": str(e),
                "exchange_id": exchange_id
            }
    
    def _create_curiosity_question(self, question: str) -> Dict[str, Any]:
        """Create a curiosity question via the API"""
        response = self.session.post(
            f"{self.api_base_url}/curiosity/questions",
            json={
                "question": question,
                "source": "knowledge_explorer",
                "priority": "high"
            }
        )
        return response.json()
    
    def _explore_curiosity_question(self, question_id: int) -> Dict[str, Any]:
        """Explore a curiosity question via the API"""
        response = self.session.post(
            f"{self.api_base_url}/curiosity/explore/{question_id}",
            json={}
        )
        return response.json()
    
    def _get_system_overview(self) -> Dict[str, Any]:
        """Get system overview via the API"""
        response = self.session.get(f"{self.api_base_url}/system/overview")
        return response.json()
    
    def _generate_exchange_id(self, question: str, entities: List[str] = None) -> str:
        """Generate a unique exchange ID"""
        content = f"{question}:{':'.join(entities or [])}:{datetime.now(timezone.utc).isoformat()}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def _check_memory_summarization(self):
        """Check if we should create memory summaries from short-term exchanges"""
        # Get recent exchanges
        with sqlite3.connect(self.memory_manager.db_path) as conn:
            recent_exchanges = conn.execute("""
                SELECT * FROM short_term_memory 
                ORDER BY timestamp DESC 
                LIMIT 50
            """).fetchall()
        
        # If we have enough exchanges, create summaries
        if len(recent_exchanges) >= 10:
            self._create_memory_summaries(recent_exchanges)
    
    def _create_memory_summaries(self, exchanges: List[tuple]):
        """Create memory summaries from short-term exchanges"""
        
        # Group exchanges by concept similarity
        concept_groups = self._group_exchanges_by_concepts(exchanges)
        
        for concept, group_exchanges in concept_groups.items():
            if len(group_exchanges) >= 3:  # Only summarize if we have enough related exchanges
                
                # Extract key information
                exchange_ids = [ex[0] for ex in group_exchanges]
                key_concepts = [concept] + self._extract_additional_concepts(group_exchanges)
                
                # Analyze structural changes
                structural_changes = self._analyze_structural_changes(group_exchanges)
                
                # Identify evolution patterns
                evolution_patterns = self._identify_evolution_patterns(group_exchanges)
                
                # Calculate energy signature
                energy_signature = self._calculate_energy_signature(group_exchanges)
                
                # Create summary
                summary = MemorySummary(
                    summary_id=self._generate_summary_id(concept, exchange_ids),
                    exchange_ids=exchange_ids,
                    key_concepts=key_concepts,
                    structural_changes=structural_changes,
                    evolution_patterns=evolution_patterns,
                    energy_signature=energy_signature,
                    created_at=datetime.now(timezone.utc),
                    updated_at=datetime.now(timezone.utc)
                )
                
                # Store in long-term memory
                self.memory_manager.store_summary(summary)
    
    def _group_exchanges_by_concepts(self, exchanges: List[tuple]) -> Dict[str, List[tuple]]:
        """Group exchanges by concept similarity"""
        groups = {}
        
        for exchange in exchanges:
            question = exchange[1].lower()
            answer = exchange[2].lower()
            
            # Simple concept extraction (in practice, use more sophisticated NLP)
            concepts = self._extract_concepts_from_text(question + " " + answer)
            
            for concept in concepts:
                if concept not in groups:
                    groups[concept] = []
                groups[concept].append(exchange)
        
        return groups
    
    def _extract_concepts_from_text(self, text: str) -> List[str]:
        """Extract key concepts from text"""
        # Simple concept extraction - in practice, use NLP libraries
        concepts = []
        text_lower = text.lower()
        
        # Living Codex core concepts
        core_concepts = [
            "water", "consciousness", "chakra", "frequency", "resonance",
            "harmony", "void", "field", "pattern", "energy", "evolution"
        ]
        
        for concept in core_concepts:
            if concept in text_lower:
                concepts.append(concept)
        
        return concepts
    
    def _extract_additional_concepts(self, exchanges: List[tuple]) -> List[str]:
        """Extract additional concepts from a group of exchanges"""
        all_text = " ".join([ex[1] + " " + ex[2] for ex in exchanges])
        return self._extract_concepts_from_text(all_text)
    
    def _analyze_structural_changes(self, exchanges: List[tuple]) -> List[Dict[str, Any]]:
        """Analyze structural changes across exchanges"""
        changes = []
        
        # Analyze resonance score changes
        resonance_scores = [ex[4] for ex in exchanges]
        if len(resonance_scores) > 1:
            changes.append({
                "type": "resonance_trend",
                "description": f"Resonance scores range from {min(resonance_scores):.2f} to {max(resonance_scores):.2f}",
                "trend": "increasing" if resonance_scores[-1] > resonance_scores[0] else "decreasing"
            })
        
        # Analyze energy exchange patterns
        energy_exchanges = [ex[5] for ex in exchanges]
        if len(energy_exchanges) > 1:
            changes.append({
                "type": "energy_pattern",
                "description": f"Energy exchanges range from {min(energy_exchanges):.2f} to {max(energy_exchanges):.2f}",
                "pattern": "balanced" if abs(sum(energy_exchanges)) < 0.1 else "imbalanced"
            })
        
        return changes
    
    def _identify_evolution_patterns(self, exchanges: List[tuple]) -> List[Dict[str, Any]]:
        """Identify evolution patterns across exchanges"""
        patterns = []
        
        # Time-based patterns
        timestamps = [datetime.fromisoformat(ex[6]) for ex in exchanges]
        if len(timestamps) > 1:
            time_span = (max(timestamps) - min(timestamps)).total_seconds() / 3600  # hours
            patterns.append({
                "type": "temporal_evolution",
                "description": f"Evolution over {time_span:.1f} hours",
                "pace": "rapid" if time_span < 1 else "moderate" if time_span < 24 else "slow"
            })
        
        # Concept evolution
        all_concepts = set()
        for exchange in exchanges:
            concepts = self._extract_concepts_from_text(exchange[1] + " " + exchange[2])
            all_concepts.update(concepts)
        
        patterns.append({
            "type": "concept_expansion",
            "description": f"Explored {len(all_concepts)} distinct concepts",
            "breadth": "narrow" if len(all_concepts) <= 3 else "moderate" if len(all_concepts) <= 6 else "broad"
        })
        
        return patterns
    
    def _calculate_energy_signature(self, exchanges: List[tuple]) -> List[float]:
        """Calculate energy signature from exchanges"""
        # Simple energy signature calculation
        total_energy = sum(ex[5] for ex in exchanges)
        avg_resonance = sum(ex[4] for ex in exchanges) / len(exchanges)
        
        return [total_energy, avg_resonance, len(exchanges)]
    
    def _generate_summary_id(self, concept: str, exchange_ids: List[str]) -> str:
        """Generate a unique summary ID"""
        content = f"{concept}:{':'.join(exchange_ids)}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def get_memory_overview(self) -> Dict[str, Any]:
        """Get overview of memory usage"""
        with sqlite3.connect(self.memory_manager.db_path) as conn:
            short_term_count = conn.execute("SELECT COUNT(*) FROM short_term_memory").fetchone()[0]
            long_term_count = conn.execute("SELECT COUNT(*) FROM long_term_memory").fetchone()[0]
            index_count = conn.execute("SELECT COUNT(*) FROM memory_index").fetchone()[0]
        
        return {
            "short_term_memory": {
                "exchanges": short_term_count,
                "type": "Question-answer exchanges"
            },
            "long_term_memory": {
                "summaries": long_term_count,
                "type": "Structural evolution summaries"
            },
            "memory_index": {
                "concepts": index_count,
                "type": "Concept-based indexing"
            },
            "memory_efficiency": {
                "compression_ratio": long_term_count / max(short_term_count, 1),
                "description": "Long-term summaries per short-term exchange"
            }
        }

def run_api_based_demo():
    """Run a demo of the API-based knowledge system"""
    
    print("🌟 API-Based Knowledge System Demo")
    print("=" * 50)
    
    # Initialize the knowledge explorer
    print("\n🔧 Initializing Knowledge Explorer...")
    explorer = KnowledgeExplorer()
    
    print("✅ System initialized successfully!")
    
    # Example knowledge exploration queries
    exploration_queries = [
        "How do water states relate to consciousness?",
        "What frequencies resonate with chakra healing?",
        "How can patterns emerge from void and field?",
        "What is the relationship between resonance and harmony?"
    ]
    
    print("\n🔍 Exploring Knowledge via Federated API...")
    
    for i, query in enumerate(exploration_queries, 1):
        print(f"\n{i}. Exploring: '{query}'")
        
        # Explore knowledge
        result = explorer.explore_knowledge(query, entities=["human_explorer"])
        
        if result["type"] == "new_exchange":
            print(f"   ✅ New exchange created (ID: {result['exchange']['exchange_id'][:8]}...)")
            print(f"   📝 Answer: {result['exchange']['answer'][:100]}...")
            print(f"   🎵 Resonance: {result['exchange']['resonance_score']:.2f}")
        elif result["type"] == "cached_exchange":
            print(f"   💾 Retrieved from cache (ID: {result['exchange']['exchange_id'][:8]}...)")
        else:
            print(f"   ❌ Error: {result.get('error', 'Unknown error')}")
    
    # Show memory overview
    print("\n📊 Memory Overview:")
    memory_overview = explorer.get_memory_overview()
    
    for memory_type, info in memory_overview.items():
        if isinstance(info, dict) and 'type' in info:
            print(f"   {memory_type}: {info['type']} - {info.get('exchanges', info.get('summaries', info.get('concepts', 0)))} items")
        elif memory_type == "memory_efficiency":
            print(f"   {memory_type}: {info['description']} - {info['compression_ratio']:.2f}")
    
    # Search memory
    print("\n🔍 Searching Memory...")
    search_results = explorer.memory_manager.search_memory("consciousness", limit=5)
    
    print(f"   Found {len(search_results)} results:")
    for result in search_results:
        if result["type"] == "short_term":
            print(f"     📝 Short-term: {result['question'][:50]}...")
        else:
            print(f"     🧠 Long-term: {len(result['key_concepts'])} concepts")
    
    print("\n" + "=" * 50)
    print("🎉 API-Based Demo Completed!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Knowledge exploration via federated API")
    print("   • Short-term memory for question-answer exchanges")
    print("   • Long-term memory for structural evolution summaries")
    print("   • Memory compression and indexing")
    print("   • Efficient storage of only essential information")

def run_mock_demo():
    """Run a mock demo that works without the API"""
    
    print("🌟 Mock API-Based Knowledge System Demo")
    print("=" * 50)
    
    # Initialize the knowledge explorer
    print("\n🔧 Initializing Knowledge Explorer...")
    explorer = KnowledgeExplorer()
    
    print("✅ System initialized successfully!")
    
    # Create some mock exchanges to demonstrate memory management
    print("\n🔍 Creating Mock Knowledge Exchanges...")
    
    mock_exchanges = [
        {
            "question": "How do water states relate to consciousness?",
            "answer": "Water states (liquid, vapor, plasma) correspond to different levels of consciousness awareness and energy flow patterns.",
            "entities": ["human_explorer", "water_consciousness"],
            "resonance": 0.85,
            "energy": 0.2
        },
        {
            "question": "What frequencies resonate with chakra healing?",
            "answer": "Specific frequencies like 396Hz (root), 528Hz (heart), and 963Hz (crown) resonate with different chakra energy centers.",
            "entities": ["human_explorer", "chakra_healing"],
            "resonance": 0.92,
            "energy": 0.3
        },
        {
            "question": "How can patterns emerge from void and field?",
            "answer": "Patterns emerge through the interaction of void (potential) and field (manifestation), creating resonant structures.",
            "entities": ["human_explorer", "pattern_emergence"],
            "resonance": 0.78,
            "energy": 0.15
        }
    ]
    
    for i, mock in enumerate(mock_exchanges, 1):
        print(f"\n{i}. Creating exchange: '{mock['question'][:50]}...'")
        
        # Create a mock exchange
        exchange = KnowledgeExchange(
            exchange_id=f"mock_{i}_{hash(mock['question']) % 10000}",
            question=mock['question'],
            answer=mock['answer'],
            entities_involved=mock['entities'],
            resonance_score=mock['resonance'],
            energy_exchange=mock['energy'],
            timestamp=datetime.now(timezone.utc),
            context={
                "source": "mock_demo",
                "exploration_type": "consciousness_research",
                "domain": "spiritual_science"
            }
        )
        
        # Store in memory
        explorer.memory_manager.store_exchange(exchange)
        print(f"   ✅ Stored with ID: {exchange.exchange_id[:8]}...")
    
    # Show memory overview
    print("\n📊 Memory Overview:")
    memory_overview = explorer.get_memory_overview()
    
    for memory_type, info in memory_overview.items():
        if isinstance(info, dict) and 'type' in info:
            print(f"   {memory_type}: {info['type']} - {info.get('exchanges', info.get('summaries', info.get('concepts', 0)))} items")
        elif memory_type == "memory_efficiency":
            print(f"   {memory_type}: {info['description']} - {info['compression_ratio']:.2f}")
    
    # Search memory
    print("\n🔍 Searching Memory...")
    search_results = explorer.memory_manager.search_memory("consciousness", limit=5)
    
    print(f"   Found {len(search_results)} results:")
    for result in search_results:
        if result["type"] == "short_term":
            print(f"     📝 Short-term: {result['question'][:50]}...")
        else:
            print(f"     🧠 Long-term: {len(result['key_concepts'])} concepts")
    
    # Demonstrate memory summarization
    print("\n🧠 Testing Memory Summarization...")
    
    # Add more exchanges to trigger summarization
    additional_exchanges = [
        {
            "question": "What is the relationship between resonance and harmony?",
            "answer": "Resonance creates harmony when frequencies align, leading to coherent energy patterns and collective consciousness.",
            "entities": ["human_explorer", "resonance_harmony"],
            "resonance": 0.88,
            "energy": 0.25
        },
        {
            "question": "How does consciousness evolve through water states?",
            "answer": "Consciousness evolves from solid (crystallized) through liquid (flowing) to vapor (expanded) and plasma (unified).",
            "entities": ["human_explorer", "consciousness_evolution"],
            "resonance": 0.91,
            "energy": 0.35
        }
    ]
    
    for mock in additional_exchanges:
        exchange = KnowledgeExchange(
            exchange_id=f"mock_{hash(mock['question']) % 10000}",
            question=mock['question'],
            answer=mock['answer'],
            entities_involved=mock['entities'],
            resonance_score=mock['resonance'],
            energy_exchange=mock['energy'],
            timestamp=datetime.now(timezone.utc),
            context={
                "source": "mock_demo",
                "exploration_type": "consciousness_research",
                "domain": "spiritual_science"
            }
        )
        explorer.memory_manager.store_exchange(exchange)
    
    # Force summarization check
    explorer._check_memory_summarization()
    
    # Show updated memory overview
    print("\n📊 Updated Memory Overview:")
    memory_overview = explorer.get_memory_overview()
    
    for memory_type, info in memory_overview.items():
        if isinstance(info, dict) and 'type' in info:
            print(f"   {memory_type}: {info['type']} - {info.get('exchanges', info.get('summaries', info.get('concepts', 0)))} items")
        elif memory_type == "memory_efficiency":
            print(f"   {memory_type}: {info['description']} - {info['compression_ratio']:.2f}")
    
    print("\n" + "=" * 50)
    print("🎉 Mock Demo Completed!")
    print("\n🌟 What We've Demonstrated:")
    print("   • Memory management without API dependency")
    print("   • Short-term memory for question-answer exchanges")
    print("   • Automatic memory summarization")
    print("   • Memory compression and indexing")
    print("   • Efficient storage of only essential information")

if __name__ == "__main__":
    # Try to run the real demo, fall back to mock if API is not available
    try:
        run_api_based_demo()
    except Exception as e:
        print(f"\n⚠️  API not available, running mock demo instead...")
        print(f"   Error: {str(e)}")
        run_mock_demo()
