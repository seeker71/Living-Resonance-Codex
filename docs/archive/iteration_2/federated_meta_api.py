#!/usr/bin/env python3
"""
Federated Meta-Circular Living Codex API
Enables the system to self-evolve through curiosity questions and discover 
higher-dimensional frequency harmonies. Supports federation, persistence, and 
AI agent interactions.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import hashlib
import time
import json
import sqlite3
import asyncio
from pathlib import Path
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from datetime import datetime
import numpy as np
from scipy.fft import fft, fftfreq
import networkx as nx

# Import our meta-circular system
from complete_meta_codex import CompleteMetaNode, CompleteMetaCodexStorage

class CuriosityQuestion(BaseModel):
    """A curiosity question that can drive system evolution"""
    
    question: str
    question_type: str = Field(description="Type: ontology, symbol, frequency, harmony, evolution")
    context: Optional[str] = None
    source: str = Field(description="Source: human, ai_agent, system_curiosity")
    priority: int = Field(default=1, ge=1, le=10)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="pending", description="pending, exploring, answered, evolved")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class FrequencyHarmony(BaseModel):
    """Higher-dimensional frequency harmony discovered through exploration"""
    
    base_frequencies: List[float]
    harmonic_ratios: List[float]
    resonance_score: float
    dimensional_complexity: int
    discovered_at: datetime = Field(default_factory=datetime.utcnow)
    discovery_method: str
    related_concepts: List[str]
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class SymbolResonance(BaseModel):
    """Symbol resonance patterns discovered through frequency matching"""
    
    symbol_pattern: str
    frequency_signature: List[float]
    resonance_strength: float
    dimensional_mapping: Dict[str, Any]
    discovered_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class FederationNode(BaseModel):
    """A federated node in the distributed system"""
    
    node_id: str
    endpoint: str
    capabilities: List[str]
    last_seen: datetime = Field(default_factory=datetime.utcnow)
    trust_score: float = Field(default=1.0, ge=0.0, le=1.0)
    shared_knowledge: List[str] = Field(default_factory=list)

class PersistentMetaStorage:
    """Persistent storage for the meta-circular system with SQLite backend"""
    
    def __init__(self, db_path: str = "./meta_codex.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the SQLite database with all necessary tables"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Core meta-circular nodes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS meta_nodes (
                id TEXT PRIMARY KEY,
                symbol TEXT NOT NULL,
                name TEXT NOT NULL,
                meta TEXT NOT NULL,
                links TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')
        
        # Curiosity questions
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS curiosity_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                question_type TEXT NOT NULL,
                context TEXT,
                source TEXT NOT NULL,
                priority INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        
        # Frequency harmonies
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS frequency_harmonies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                base_frequencies TEXT NOT NULL,
                harmonic_ratios TEXT NOT NULL,
                resonance_score REAL NOT NULL,
                dimensional_complexity INTEGER NOT NULL,
                discovered_at TEXT NOT NULL,
                discovery_method TEXT NOT NULL,
                related_concepts TEXT NOT NULL
            )
        ''')
        
        # Symbol resonances
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS symbol_resonances (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_pattern TEXT NOT NULL,
                frequency_signature TEXT NOT NULL,
                resonance_strength REAL NOT NULL,
                dimensional_mapping TEXT NOT NULL,
                discovered_at TEXT NOT NULL
            )
        ''')
        
        # Federation nodes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS federation_nodes (
                node_id TEXT PRIMARY KEY,
                endpoint TEXT NOT NULL,
                capabilities TEXT NOT NULL,
                last_seen TEXT NOT NULL,
                trust_score REAL NOT NULL,
                shared_knowledge TEXT NOT NULL
            )
        ''')
        
        # Evolution history
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evolution_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                description TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                source TEXT NOT NULL,
                impact_score REAL NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def store_meta_node(self, node: CompleteMetaNode):
        """Store a meta-circular node in persistent storage"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO meta_nodes 
            (id, symbol, name, meta, links, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            node.id,
            node.symbol,
            node.name,
            node.meta,
            json.dumps(node.links),
            node.created_at,
            node.updated_at
        ))
        
        conn.commit()
        conn.close()
    
    def get_meta_node(self, node_id: str) -> Optional[CompleteMetaNode]:
        """Retrieve a meta-circular node from persistent storage"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM meta_nodes WHERE id = ?', (node_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return CompleteMetaNode(
                id=row[0],
                symbol=row[1],
                name=row[2],
                meta=row[3],
                links=json.loads(row[4]),
                created_at=row[5],
                updated_at=row[6]
            )
        return None
    
    def store_curiosity_question(self, question: CuriosityQuestion) -> int:
        """Store a curiosity question and return its ID"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO curiosity_questions 
            (question, question_type, context, source, priority, created_at, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            question.question,
            question.question_type,
            question.context,
            question.source,
            question.priority,
            question.created_at.isoformat(),
            question.status
        ))
        
        question_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return question_id
    
    def get_pending_curiosity_questions(self, limit: int = 10) -> List[CuriosityQuestion]:
        """Get pending curiosity questions for exploration"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM curiosity_questions 
            WHERE status = 'pending' 
            ORDER BY priority DESC, created_at ASC 
            LIMIT ?
        ''', (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        questions = []
        for row in rows:
            questions.append(CuriosityQuestion(
                question=row[1],
                question_type=row[2],
                context=row[3],
                source=row[4],
                priority=row[5],
                created_at=datetime.fromisoformat(row[6]),
                status=row[7]
            ))
        
        return questions
    
    def store_frequency_harmony(self, harmony: FrequencyHarmony) -> int:
        """Store a discovered frequency harmony"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO frequency_harmonies 
            (base_frequencies, harmonic_ratios, resonance_score, dimensional_complexity,
             discovered_at, discovery_method, related_concepts)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            json.dumps(harmony.base_frequencies),
            json.dumps(harmony.harmonic_ratios),
            harmony.resonance_score,
            harmony.dimensional_complexity,
            harmony.discovered_at.isoformat(),
            harmony.discovery_method,
            json.dumps(harmony.related_concepts)
        ))
        
        harmony_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return harmony_id
    
    def store_symbol_resonance(self, resonance: SymbolResonance) -> int:
        """Store a discovered symbol resonance pattern"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO symbol_resonances 
            (symbol_pattern, frequency_signature, resonance_strength, 
             dimensional_mapping, discovered_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            resonance.symbol_pattern,
            json.dumps(resonance.frequency_signature),
            resonance.resonance_strength,
            json.dumps(resonance.dimensional_mapping),
            resonance.discovered_at.isoformat()
        ))
        
        resonance_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return resonance_id

class FrequencyHarmonyExplorer:
    """Explores higher-dimensional frequency harmonies and symbol resonances"""
    
    def __init__(self, storage: PersistentMetaStorage):
        self.storage = storage
    
    def discover_harmonic_patterns(self, base_frequencies: List[float]) -> List[FrequencyHarmony]:
        """Discover harmonic patterns in frequency combinations"""
        
        harmonies = []
        
        # Analyze harmonic ratios
        for i, freq1 in enumerate(base_frequencies):
            for j, freq2 in enumerate(base_frequencies[i+1:], i+1):
                # Calculate harmonic ratios
                ratio = freq2 / freq1 if freq1 > 0 else 0
                
                # Check for harmonic relationships
                if self._is_harmonic_ratio(ratio):
                    # Calculate resonance score
                    resonance_score = self._calculate_resonance_score(freq1, freq2, ratio)
                    
                    # Determine dimensional complexity
                    dimensional_complexity = self._calculate_dimensional_complexity([freq1, freq2])
                    
                    harmony = FrequencyHarmony(
                        base_frequencies=[freq1, freq2],
                        harmonic_ratios=[ratio, 1/ratio],
                        resonance_score=resonance_score,
                        dimensional_complexity=dimensional_complexity,
                        discovery_method="harmonic_ratio_analysis",
                        related_concepts=[f"freq_{int(freq1)}", f"freq_{int(freq2)}"]
                    )
                    
                    harmonies.append(harmony)
                    self.storage.store_frequency_harmony(harmony)
        
        return harmonies
    
    def _is_harmonic_ratio(self, ratio: float) -> bool:
        """Check if a ratio represents a harmonic relationship"""
        
        # Common harmonic ratios (octave, perfect fifth, perfect fourth, etc.)
        harmonic_ratios = [2.0, 3/2, 4/3, 5/4, 6/5, 8/5, 9/8]
        
        for harmonic in harmonic_ratios:
            if abs(ratio - harmonic) < 0.01 or abs(ratio - 1/harmonic) < 0.01:
                return True
        
        return False
    
    def _calculate_resonance_score(self, freq1: float, freq2: float, ratio: float) -> float:
        """Calculate a resonance score based on frequency relationship"""
        
        # Base score from harmonic relationship
        base_score = 1.0 if self._is_harmonic_ratio(ratio) else 0.5
        
        # Frequency proximity bonus
        freq_diff = abs(freq1 - freq2)
        proximity_bonus = max(0, 1 - (freq_diff / max(freq1, freq2)))
        
        # Harmonic complexity bonus
        complexity_bonus = 0.1 * (1 / (1 + abs(ratio - 2.0)))  # Favor octave relationships
        
        return min(1.0, base_score + proximity_bonus + complexity_bonus)
    
    def _calculate_dimensional_complexity(self, frequencies: List[float]) -> int:
        """Calculate the dimensional complexity of frequency combinations"""
        
        if len(frequencies) <= 1:
            return 1
        
        # Use FFT to analyze frequency patterns
        freq_array = np.array(frequencies)
        fft_result = fft(freq_array)
        
        # Count significant frequency components
        significant_components = np.sum(np.abs(fft_result) > np.mean(np.abs(fft_result)))
        
        return min(10, significant_components)  # Cap at 10 dimensions
    
    def discover_symbol_resonances(self, symbols: List[str]) -> List[SymbolResonance]:
        """Discover resonance patterns in symbol combinations"""
        
        resonances = []
        
        for symbol in symbols:
            # Convert symbol to frequency signature
            freq_signature = self._symbol_to_frequency_signature(symbol)
            
            # Calculate resonance strength
            resonance_strength = self._calculate_symbol_resonance_strength(freq_signature)
            
            # Create dimensional mapping
            dimensional_mapping = self._create_dimensional_mapping(symbol, freq_signature)
            
            resonance = SymbolResonance(
                symbol_pattern=symbol,
                frequency_signature=freq_signature,
                resonance_strength=resonance_strength,
                dimensional_mapping=dimensional_mapping
            )
            
            resonances.append(resonance)
            self.storage.store_symbol_resonance(resonance)
        
        return resonances
    
    def _symbol_to_frequency_signature(self, symbol: str) -> List[float]:
        """Convert a symbol to its frequency signature"""
        
        # Convert ASCII values to frequencies
        frequencies = []
        for char in symbol:
            ascii_val = ord(char)
            # Map ASCII to frequency range (20 Hz - 20 kHz)
            freq = 20 + (ascii_val / 255) * 19980
            frequencies.append(freq)
        
        return frequencies
    
    def _calculate_symbol_resonance_strength(self, freq_signature: List[float]) -> float:
        """Calculate the resonance strength of a symbol's frequency signature"""
        
        if len(freq_signature) <= 1:
            return 1.0
        
        # Calculate harmonic relationships within the signature
        harmonic_count = 0
        total_relationships = 0
        
        for i, freq1 in enumerate(freq_signature):
            for j, freq2 in enumerate(freq_signature[i+1:], i+1):
                total_relationships += 1
                ratio = freq2 / freq1 if freq1 > 0 else 0
                if self._is_harmonic_ratio(ratio):
                    harmonic_count += 1
        
        if total_relationships == 0:
            return 1.0
        
        return harmonic_count / total_relationships
    
    def _create_dimensional_mapping(self, symbol: str, freq_signature: List[float]) -> Dict[str, Any]:
        """Create a dimensional mapping for a symbol"""
        
        return {
            "symbol_length": len(symbol),
            "frequency_range": {
                "min": min(freq_signature) if freq_signature else 0,
                "max": max(freq_signature) if freq_signature else 0,
                "mean": np.mean(freq_signature) if freq_signature else 0
            },
            "harmonic_components": len([f for f in freq_signature if f > 0]),
            "dimensional_vectors": self._calculate_dimensional_vectors(freq_signature)
        }
    
    def _calculate_dimensional_vectors(self, freq_signature: List[float]) -> List[float]:
        """Calculate dimensional vectors from frequency signature"""
        
        if not freq_signature:
            return [0.0]
        
        # Use FFT to extract dimensional components
        fft_result = fft(freq_signature)
        
        # Take the first few components as dimensional vectors
        vectors = np.abs(fft_result[:min(5, len(fft_result))])
        
        # Normalize
        if np.sum(vectors) > 0:
            vectors = vectors / np.sum(vectors)
        
        return vectors.tolist()

class CuriosityEngine:
    """Engine that drives system evolution through curiosity questions"""
    
    def __init__(self, storage: PersistentMetaStorage, explorer: FrequencyHarmonyExplorer):
        self.storage = storage
        self.explorer = explorer
    
    def generate_system_curiosity(self) -> List[CuriosityQuestion]:
        """Generate curiosity questions about the system itself"""
        
        questions = [
            CuriosityQuestion(
                question="What is an ontology and how does it relate to our meta-circular structure?",
                question_type="ontology",
                source="system_curiosity",
                priority=10
            ),
            CuriosityQuestion(
                question="How can symbols be used to find similar resonant symbols through frequency matching?",
                question_type="symbol",
                source="system_curiosity",
                priority=9
            ),
            CuriosityQuestion(
                question="What higher-dimensional frequency harmonies exist in our chakra system?",
                question_type="frequency",
                source="system_curiosity",
                priority=8
            ),
            CuriosityQuestion(
                question="How does the water state metaphor relate to frequency resonance?",
                question_type="harmony",
                source="system_curiosity",
                priority=7
            ),
            CuriosityQuestion(
                question="What new meta-nodes could emerge from exploring our existing structure?",
                question_type="evolution",
                source="system_curiosity",
                priority=6
            )
        ]
        
        # Store questions
        for question in questions:
            self.storage.store_curiosity_question(question)
        
        return questions
    
    def explore_curiosity_question(self, question: CuriosityQuestion) -> Dict[str, Any]:
        """Explore a curiosity question and generate insights"""
        
        if question.question_type == "frequency":
            return self._explore_frequency_question(question)
        elif question.question_type == "symbol":
            return self._explore_symbol_question(question)
        elif question.question_type == "ontology":
            return self._explore_ontology_question(question)
        elif question.question_type == "harmony":
            return self._explore_harmony_question(question)
        elif question.question_type == "evolution":
            return self._explore_evolution_question(question)
        else:
            return {"error": "Unknown question type"}
    
    def _explore_frequency_question(self, question: CuriosityQuestion) -> Dict[str, Any]:
        """Explore frequency-related curiosity questions"""
        
        # Get all frequency nodes from storage
        chakra_frequencies = [396, 417, 528, 639, 741, 852, 963]
        
        # Discover harmonic patterns
        harmonies = self.explorer.discover_harmonic_patterns(chakra_frequencies)
        
        return {
            "question": question.question,
            "exploration_type": "frequency_harmony_discovery",
            "discovered_harmonies": len(harmonies),
            "chakra_frequencies": chakra_frequencies,
            "harmonic_insights": [
                {
                    "frequencies": harmony.base_frequencies,
                    "resonance_score": harmony.resonance_score,
                    "dimensional_complexity": harmony.dimensional_complexity
                }
                for harmony in harmonies
            ]
        }
    
    def _explore_symbol_question(self, question: CuriosityQuestion) -> Dict[str, Any]:
        """Explore symbol-related curiosity questions"""
        
        # Analyze symbols from our system
        symbols = ["void", "field", "pattern", "flow", "memory", "resonance"]
        
        # Discover symbol resonances
        resonances = self.explorer.discover_symbol_resonances(symbols)
        
        return {
            "question": question.question,
            "exploration_type": "symbol_resonance_discovery",
            "analyzed_symbols": symbols,
            "discovered_resonances": len(resonances),
            "resonance_insights": [
                {
                    "symbol": resonance.symbol_pattern,
                    "resonance_strength": resonance.resonance_strength,
                    "dimensional_mapping": resonance.dimensional_mapping
                }
                for resonance in resonances
            ]
        }
    
    def _explore_ontology_question(self, question: CuriosityQuestion) -> Dict[str, Any]:
        """Explore ontology-related curiosity questions"""
        
        return {
            "question": question.question,
            "exploration_type": "ontology_analysis",
            "insights": {
                "meta_circular_nature": "Our system is meta-circular - every concept describes itself",
                "bootstrap_foundation": "16 fundamental nodes provide universal building blocks",
                "living_codex_integration": "Water states, chakras, and frequencies are unified",
                "fractal_recursion": "Same patterns repeat at every level of abstraction",
                "self_evolution": "System can grow through curiosity and exploration"
            }
        }
    
    def _explore_harmony_question(self, question: CuriosityQuestion) -> Dict[str, Any]:
        """Explore harmony-related curiosity questions"""
        
        return {
            "question": question.question,
            "exploration_type": "harmony_analysis",
            "insights": {
                "water_frequency_correspondence": "Water states map to frequency ranges",
                "chakra_frequency_alignment": "Chakras have specific Solfeggio frequencies",
                "planetary_frequency_mapping": "Planets correspond to frequency archetypes",
                "symbolic_frequency_encoding": "Symbols encode frequency signatures",
                "harmonic_resonance_emergence": "Harmonies emerge from frequency relationships"
            }
        }
    
    def _explore_evolution_question(self, question: CuriosityQuestion) -> Dict[str, Any]:
        """Explore evolution-related curiosity questions"""
        
        return {
            "question": question.question,
            "exploration_type": "evolution_analysis",
            "insights": {
                "new_meta_nodes": "Could create meta-nodes for 'curiosity', 'exploration', 'discovery'",
                "frequency_meta_nodes": "Meta-nodes for 'harmonic_ratio', 'resonance_pattern'",
                "symbol_meta_nodes": "Meta-nodes for 'symbol_frequency', 'dimensional_mapping'",
                "evolution_meta_nodes": "Meta-nodes for 'system_growth', 'knowledge_expansion'",
                "federation_meta_nodes": "Meta-nodes for 'distributed_knowledge', 'shared_insights'"
            }
        }

# FastAPI application
app = FastAPI(title="Federated Meta-Circular Living Codex API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global storage and components
storage = PersistentMetaStorage()
explorer = FrequencyHarmonyExplorer(storage)
curiosity_engine = CuriosityEngine(storage, explorer)

# Lifespan approach for newer FastAPI versions
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    curiosity_engine.generate_system_curiosity()
    yield
    # Shutdown
    pass

app = FastAPI(
    title="Federated Meta-Circular Living Codex API", 
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    """Root endpoint with system information"""
    return {
        "system": "Federated Meta-Circular Living Codex API",
        "version": "1.0.0",
        "capabilities": [
            "Meta-circular node exploration",
            "Curiosity-driven evolution",
            "Frequency harmony discovery",
            "Symbol resonance analysis",
            "Federated knowledge sharing"
        ]
    }

@app.get("/nodes/{node_id}")
async def get_node(node_id: str):
    """Get a meta-circular node by ID"""
    node = storage.get_meta_node(node_id)
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    
    return {
        "node": node.model_dump(),
        "meta_description": "Node retrieved from persistent storage"
    }

@app.post("/curiosity/questions")
async def create_curiosity_question(question: CuriosityQuestion):
    """Create a new curiosity question"""
    question_id = storage.store_curiosity_question(question)
    
    return {
        "message": "Curiosity question created",
        "question_id": question_id,
        "question": question.model_dump()
    }

@app.get("/curiosity/questions")
async def get_curiosity_questions(status: str = "pending", limit: int = 10):
    """Get curiosity questions by status"""
    if status == "pending":
        questions = storage.get_pending_curiosity_questions(limit)
    else:
        # For now, just return pending questions
        questions = storage.get_pending_curiosity_questions(limit)
    
    return {
        "questions": [q.model_dump() for q in questions],
        "total": len(questions)
    }

@app.post("/curiosity/explore/{question_id}")
async def explore_curiosity_question(question_id: int):
    """Explore a specific curiosity question"""
    # For now, get a sample question to explore
    questions = storage.get_pending_curiosity_questions(1)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions available")
    
    question = questions[0]
    exploration_result = curiosity_engine.explore_curiosity_question(question)
    
    return {
        "question_id": question_id,
        "exploration_result": exploration_result
    }

@app.get("/harmonies/frequencies")
async def discover_frequency_harmonies(base_frequencies: str):
    """Discover harmonic patterns in frequency combinations"""
    try:
        frequencies = [float(f) for f in base_frequencies.split(",")]
        harmonies = explorer.discover_harmonic_patterns(frequencies)
        
        return {
            "base_frequencies": frequencies,
            "discovered_harmonies": len(harmonies),
            "harmonies": [h.model_dump() for h in harmonies]
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid frequency format")

@app.get("/resonances/symbols")
async def discover_symbol_resonances(symbols: str):
    """Discover resonance patterns in symbol combinations"""
    try:
        symbol_list = symbols.split(",")
        resonances = explorer.discover_symbol_resonances(symbol_list)
        
        return {
            "analyzed_symbols": symbol_list,
            "discovered_resonances": len(resonances),
            "resonances": [r.model_dump() for r in resonances]
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid symbol format")

@app.get("/system/curiosity/generate")
async def generate_system_curiosity():
    """Generate new system curiosity questions"""
    questions = curiosity_engine.generate_system_curiosity()
    
    return {
        "message": "System curiosity questions generated",
        "questions_generated": len(questions),
        "questions": [q.model_dump() for q in questions]
    }

@app.get("/system/overview")
async def get_system_overview():
    """Get comprehensive system overview"""
    return {
        "system": "Federated Meta-Circular Living Codex",
        "components": {
            "persistent_storage": "SQLite database with all system data",
            "frequency_explorer": "Discovers harmonic patterns and symbol resonances",
            "curiosity_engine": "Drives system evolution through questions",
            "federated_api": "Enables distributed knowledge sharing"
        },
        "capabilities": [
            "Store and retrieve meta-circular nodes",
            "Generate and explore curiosity questions",
            "Discover frequency harmonies",
            "Analyze symbol resonances",
            "Enable system self-evolution",
            "Support federation and distributed knowledge"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
