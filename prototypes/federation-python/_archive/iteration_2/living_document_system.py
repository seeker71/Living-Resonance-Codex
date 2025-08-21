#!/usr/bin/env python3
"""
Living Document System for Meta-Circular Living Codex
Makes all documents, source code, and documentation self-evolving and explorable.
Every piece of content becomes a living node that can grow and evolve.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import hashlib
import time
import json
import sqlite3
import ast
import inspect
import os
from pathlib import Path
from datetime import datetime
import re
from dataclasses import dataclass

# Import our existing system
from complete_meta_codex import CompleteMetaNode, CompleteMetaCodexStorage

class LivingDocument(BaseModel):
    """A living document that can evolve and expand"""
    
    id: str
    title: str
    content: str
    content_type: str = Field(description="Type: markdown, python, json, text, code, documentation")
    source_path: Optional[str] = None
    version: str = "1.0.0"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    parent_document: Optional[str] = None
    child_documents: List[str] = Field(default_factory=list)
    references: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    evolution_history: List[Dict[str, Any]] = Field(default_factory=list)
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class CodeAnalysis(BaseModel):
    """Analysis of source code structure and relationships"""
    
    file_path: str
    functions: List[Dict[str, Any]]
    classes: List[Dict[str, Any]]
    imports: List[str]
    dependencies: List[str]
    complexity_score: float
    documentation_coverage: float
    test_coverage: float
    last_analyzed: datetime = Field(default_factory=datetime.utcnow)

class DocumentRelationship(BaseModel):
    """Relationship between documents"""
    
    source_doc: str
    target_doc: str
    relationship_type: str = Field(description="Type: references, extends, implements, documents, tests")
    strength: float = Field(default=1.0, ge=0.0, le=1.0)
    context: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class LivingDocumentStorage:
    """Persistent storage for living documents"""
    
    def __init__(self, db_path: str = "./living_documents.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the SQLite database for living documents"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Living documents
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS living_documents (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                content_type TEXT NOT NULL,
                source_path TEXT,
                version TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                parent_document TEXT,
                child_documents TEXT NOT NULL,
                doc_references TEXT NOT NULL,
                metadata TEXT NOT NULL,
                evolution_history TEXT NOT NULL
            )
        ''')
        
        # Code analysis
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS code_analysis (
                file_path TEXT PRIMARY KEY,
                functions TEXT NOT NULL,
                classes TEXT NOT NULL,
                imports TEXT NOT NULL,
                dependencies TEXT NOT NULL,
                complexity_score REAL NOT NULL,
                documentation_coverage REAL NOT NULL,
                test_coverage REAL NOT NULL,
                last_analyzed TEXT NOT NULL
            )
        ''')
        
        # Document relationships
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS document_relationships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_doc TEXT NOT NULL,
                target_doc TEXT NOT NULL,
                relationship_type TEXT NOT NULL,
                strength REAL NOT NULL,
                context TEXT,
                created_at TEXT NOT NULL
            )
        ''')
        
        # Evolution events
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evolution_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id TEXT NOT NULL,
                event_type TEXT NOT NULL,
                description TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                source TEXT NOT NULL,
                impact_score REAL NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def store_living_document(self, document: LivingDocument):
        """Store a living document in persistent storage"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO living_documents 
            (id, title, content, content_type, source_path, version, created_at, updated_at,
             parent_document, child_documents, doc_references, metadata, evolution_history)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            document.id,
            document.title,
            document.content,
            document.content_type,
            document.source_path,
            document.version,
            document.created_at.isoformat(),
            document.updated_at.isoformat(),
            document.parent_document,
            json.dumps(document.child_documents),
            json.dumps(document.references),
            json.dumps(document.metadata),
            json.dumps(document.evolution_history)
        ))
        
        conn.commit()
        conn.close()
    
    def get_living_document(self, document_id: str) -> Optional[LivingDocument]:
        """Retrieve a living document by ID"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM living_documents WHERE id = ?', (document_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return LivingDocument(
                id=row[0],
                title=row[1],
                content=row[2],
                content_type=row[3],
                source_path=row[4],
                version=row[5],
                created_at=datetime.fromisoformat(row[6]),
                updated_at=datetime.fromisoformat(row[7]),
                parent_document=row[8],
                child_documents=json.loads(row[9]),
                references=json.loads(row[10]),
                metadata=json.loads(row[11]),
                evolution_history=json.loads(row[12])
            )
        return None
    
    def get_all_living_documents(self) -> List[LivingDocument]:
        """Get all living documents"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM living_documents')
        rows = cursor.fetchall()
        conn.close()
        
        documents = []
        for row in rows:
            documents.append(LivingDocument(
                id=row[0],
                title=row[1],
                content=row[2],
                content_type=row[3],
                source_path=row[4],
                version=row[5],
                created_at=datetime.fromisoformat(row[6]),
                updated_at=datetime.fromisoformat(row[7]),
                parent_document=row[8],
                child_documents=json.loads(row[9]),
                references=json.loads(row[10]),
                metadata=json.loads(row[11]),
                evolution_history=json.loads(row[12])
            ))
        
        return documents
    
    def store_evolution_event(self, document_id: str, evolution_event: Dict[str, Any]):
        """Store an evolution event"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO evolution_events 
            (document_id, event_type, description, timestamp, source, impact_score)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            document_id,
            evolution_event["type"],
            evolution_event["description"],
            evolution_event["timestamp"],
            evolution_event["source"],
            evolution_event["impact_score"]
        ))
        
        conn.commit()
        conn.close()

class CodeAnalyzer:
    """Analyzes source code to understand structure and relationships"""
    
    def __init__(self, storage: LivingDocumentStorage):
        self.storage = storage
    
    def analyze_python_file(self, file_path: str) -> CodeAnalysis:
        """Analyze a Python file for structure and relationships"""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the AST
            tree = ast.parse(content)
            
            functions = []
            classes = []
            imports = []
            
            # Extract functions
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append({
                        "name": node.name,
                        "line_number": node.lineno,
                        "args": [arg.arg for arg in node.args.args],
                        "docstring": ast.get_docstring(node),
                        "decorators": [d.id for d in node.decorator_list if hasattr(d, 'id')]
                    })
                
                elif isinstance(node, ast.ClassDef):
                    classes.append({
                        "name": node.name,
                        "line_number": node.lineno,
                        "bases": [base.id for base in node.bases if hasattr(base, 'id')],
                        "docstring": ast.get_docstring(node),
                        "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                    })
                
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")
            
            # Calculate complexity score
            complexity_score = self._calculate_complexity(tree)
            
            # Calculate documentation coverage
            doc_coverage = self._calculate_documentation_coverage(functions, classes)
            
            # Calculate test coverage (simplified)
            test_coverage = self._estimate_test_coverage(file_path)
            
            analysis = CodeAnalysis(
                file_path=file_path,
                functions=functions,
                classes=classes,
                imports=imports,
                dependencies=self._extract_dependencies(content),
                complexity_score=complexity_score,
                documentation_coverage=doc_coverage,
                test_coverage=test_coverage
            )
            
            return analysis
            
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return None
    
    def _calculate_complexity(self, tree: ast.AST) -> float:
        """Calculate cyclomatic complexity of the code"""
        
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.With):
                complexity += 1
            elif isinstance(node, ast.Assert):
                complexity += 1
        
        return min(10.0, complexity / 10.0)  # Normalize to 0-1
    
    def _calculate_documentation_coverage(self, functions: List[Dict], classes: List[Dict]) -> float:
        """Calculate documentation coverage percentage"""
        
        total_items = len(functions) + len(classes)
        if total_items == 0:
            return 1.0
        
        documented_items = 0
        
        for func in functions:
            if func.get('docstring'):
                documented_items += 1
        
        for cls in classes:
            if cls.get('docstring'):
                documented_items += 1
        
        return documented_items / total_items
    
    def _estimate_test_coverage(self, file_path: str) -> float:
        """Estimate test coverage based on test file existence"""
        
        # Look for corresponding test file
        test_paths = [
            file_path.replace('.py', '_test.py'),
            file_path.replace('.py', 'test_'),
            file_path.replace('.py', '.test.py')
        ]
        
        for test_path in test_paths:
            if os.path.exists(test_path):
                return 0.8  # Assume good coverage if test file exists
        
        return 0.2  # Low coverage if no test file
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extract dependencies from import statements"""
        
        dependencies = []
        import_pattern = r'^(?:from\s+(\w+(?:\.\w+)*)\s+import|import\s+(\w+(?:\.\w+)*))'
        
        for line in content.split('\n'):
            match = re.match(import_pattern, line.strip())
            if match:
                dep = match.group(1) or match.group(2)
                if dep and not dep.startswith('.'):
                    dependencies.append(dep)
        
        return list(set(dependencies))

class DocumentEvolutionEngine:
    """Engine that drives document evolution and growth"""
    
    def __init__(self, storage: LivingDocumentStorage, code_analyzer: CodeAnalyzer):
        self.storage = storage
        self.code_analyzer = code_analyzer
    
    def create_living_document(self, file_path: str, content_type: str = None) -> LivingDocument:
        """Create a living document from a file"""
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Determine content type
        if content_type is None:
            content_type = self._infer_content_type(file_path)
        
        # Read content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate document ID
        doc_id = self._generate_document_id(file_path, content)
        
        # Create living document
        document = LivingDocument(
            id=doc_id,
            title=os.path.basename(file_path),
            content=content,
            content_type=content_type,
            source_path=file_path,
            metadata=self._extract_metadata(file_path, content, content_type)
        )
        
        # Analyze code if it's a Python file
        if content_type == "python":
            analysis = self.code_analyzer.analyze_python_file(file_path)
            if analysis:
                # Convert datetime objects to strings for JSON serialization
                analysis_dict = analysis.model_dump()
                analysis_dict['last_analyzed'] = analysis_dict['last_analyzed'].isoformat()
                document.metadata["code_analysis"] = analysis_dict
        
        return document
    
    def _infer_content_type(self, file_path: str) -> str:
        """Infer the content type from file extension"""
        
        ext = Path(file_path).suffix.lower()
        
        if ext == '.py':
            return "python"
        elif ext == '.md':
            return "markdown"
        elif ext == '.json':
            return "json"
        elif ext == '.txt':
            return "text"
        elif ext == '.html' or ext == '.htm':
            return "html"
        else:
            return "text"
    
    def _generate_document_id(self, file_path: str, content: str) -> str:
        """Generate a unique document ID"""
        
        # Combine file path and content hash
        combined = f"{file_path}:{hashlib.sha256(content.encode()).hexdigest()[:16]}"
        return hashlib.sha256(combined.encode()).hexdigest()[:16]
    
    def _extract_metadata(self, file_path: str, content: str, content_type: str) -> Dict[str, Any]:
        """Extract metadata from the document"""
        
        metadata = {
            "file_size": len(content),
            "line_count": len(content.split('\n')),
            "word_count": len(content.split()),
            "character_count": len(content),
            "last_modified": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
        }
        
        if content_type == "python":
            metadata.update({
                "has_functions": "def " in content,
                "has_classes": "class " in content,
                "has_imports": any(keyword in content for keyword in ["import ", "from "]),
                "has_docstrings": '"""' in content or "'''" in content
            })
        elif content_type == "markdown":
            metadata.update({
                "has_headers": any(line.startswith('#') for line in content.split('\n')),
                "has_links": '[' in content and '](' in content,
                "has_code_blocks": '```' in content,
                "has_lists": any(line.strip().startswith(('-', '*', '1.')) for line in content.split('\n'))
            })
        
        return metadata
    
    def evolve_document(self, document_id: str, evolution_type: str, description: str, 
                       source: str = "system", impact_score: float = 0.5) -> bool:
        """Evolve a document through various mechanisms"""
        
        # Get the document
        document = self.storage.get_living_document(document_id)
        if not document:
            return False
        
        # Record evolution event
        evolution_event = {
            "type": evolution_type,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
            "source": source,
            "impact_score": impact_score
        }
        
        document.evolution_history.append(evolution_event)
        document.updated_at = datetime.utcnow()
        
        # Update version
        current_version = document.version.split('.')
        if evolution_type == "major_change":
            current_version[0] = str(int(current_version[0]) + 1)
            current_version[1] = "0"
            current_version[2] = "0"
        elif evolution_type == "minor_change":
            current_version[1] = str(int(current_version[1]) + 1)
            current_version[2] = "0"
        else:
            current_version[2] = str(int(current_version[2]) + 1)
        
        document.version = '.'.join(current_version)
        
        # Store updated document
        self.storage.store_living_document(document)
        
        # Store evolution event
        self.storage.store_evolution_event(document_id, evolution_event)
        
        return True
    
    def discover_relationships(self, document_id: str) -> List[DocumentRelationship]:
        """Discover relationships between documents"""
        
        document = self.storage.get_living_document(document_id)
        if not document:
            return []
        
        relationships = []
        
        # Find references to other documents
        if document.content_type == "python":
            # Look for import statements
            import_pattern = r'(?:from\s+(\w+(?:\.\w+)*)\s+import|import\s+(\w+(?:\.\w+)*))'
            for match in re.finditer(import_pattern, document.content):
                module = match.group(1) or match.group(2)
                # Look for corresponding document
                target_doc = self._find_document_by_module(module)
                if target_doc:
                    relationships.append(DocumentRelationship(
                        source_doc=document_id,
                        target_doc=target_doc.id,
                        relationship_type="imports",
                        strength=0.8
                    ))
        
        # Find documentation references
        if document.content_type == "markdown":
            # Look for links to other documents
            link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
            for match in re.finditer(link_pattern, document.content):
                link_text = match.group(1)
                link_target = match.group(2)
                # Look for corresponding document
                target_doc = self._find_document_by_path(link_target)
                if target_doc:
                    relationships.append(DocumentRelationship(
                        source_doc=document_id,
                        target_doc=target_doc.id,
                        relationship_type="references",
                        strength=0.6
                    ))
        
        return relationships
    
    def _find_document_by_module(self, module: str) -> Optional[LivingDocument]:
        """Find a document by module name"""
        
        # This is a simplified search - in practice, you'd want more sophisticated matching
        all_docs = self.storage.get_all_living_documents()
        
        for doc in all_docs:
            if doc.content_type == "python" and module in doc.content:
                return doc
        
        return None
    
    def _find_document_by_path(self, path: str) -> Optional[LivingDocument]:
        """Find a document by file path"""
        
        all_docs = self.storage.get_all_living_documents()
        
        for doc in all_docs:
            if doc.source_path and path in doc.source_path:
                return doc
        
        return None

class LivingDocumentAPI:
    """API for interacting with living documents"""
    
    def __init__(self, storage: LivingDocumentStorage, evolution_engine: DocumentEvolutionEngine):
        self.storage = storage
        self.evolution_engine = evolution_engine
    
    def create_document_from_file(self, file_path: str) -> Dict[str, Any]:
        """Create a living document from a file"""
        
        try:
            document = self.evolution_engine.create_living_document(file_path)
            self.storage.store_living_document(document)
            
            return {
                "success": True,
                "document": document.model_dump(),
                "message": f"Created living document from {file_path}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_document(self, document_id: str) -> Dict[str, Any]:
        """Get a living document by ID"""
        
        document = self.storage.get_living_document(document_id)
        if document:
            return {
                "success": True,
                "document": document.model_dump()
            }
        else:
            return {
                "success": False,
                "error": "Document not found"
            }
    
    def evolve_document(self, document_id: str, evolution_type: str, 
                       description: str, source: str = "api", impact_score: float = 0.5) -> Dict[str, Any]:
        """Evolve a document"""
        
        success = self.evolution_engine.evolve_document(
            document_id, evolution_type, description, source, impact_score
        )
        
        if success:
            return {
                "success": True,
                "message": f"Document {document_id} evolved successfully"
            }
        else:
            return {
                "success": False,
                "error": "Failed to evolve document"
            }
    
    def discover_relationships(self, document_id: str) -> Dict[str, Any]:
        """Discover relationships for a document"""
        
        relationships = self.evolution_engine.discover_relationships(document_id)
        
        return {
            "success": True,
            "relationships": [rel.model_dump() for rel in relationships],
            "count": len(relationships)
        }
    
    def get_system_overview(self) -> Dict[str, Any]:
        """Get overview of the living document system"""
        
        all_docs = self.storage.get_all_living_documents()
        
        # Analyze document types
        type_counts = {}
        for doc in all_docs:
            doc_type = doc.content_type
            type_counts[doc_type] = type_counts.get(doc_type, 0) + 1
        
        # Calculate evolution statistics
        total_evolution_events = sum(len(doc.evolution_history) for doc in all_docs)
        
        return {
            "total_documents": len(all_docs),
            "document_types": type_counts,
            "total_evolution_events": total_evolution_events,
            "system_status": "operational",
            "capabilities": [
                "Document creation from files",
                "Automatic code analysis",
                "Relationship discovery",
                "Evolution tracking",
                "Version management",
                "Metadata extraction"
            ]
        }

# Test the living document system
if __name__ == "__main__":
    print("Living Document System for Meta-Circular Living Codex")
    print("=" * 60)
    
    # Initialize components
    storage = LivingDocumentStorage()
    code_analyzer = CodeAnalyzer(storage)
    evolution_engine = DocumentEvolutionEngine(storage, code_analyzer)
    api = LivingDocumentAPI(storage, evolution_engine)
    
    # Create living documents from existing files
    print("\nCreating living documents from existing files...")
    
    files_to_analyze = [
        "federated_meta_api.py",
        "complete_meta_codex.py",
        "FEDERATED_API_SYSTEM.md",
        "IMPLEMENTATION_SUMMARY.md"
    ]
    
    for file_path in files_to_analyze:
        if os.path.exists(file_path):
            result = api.create_document_from_file(file_path)
            if result["success"]:
                print(f"✅ Created living document: {file_path}")
            else:
                print(f"❌ Failed to create document: {file_path} - {result['error']}")
        else:
            print(f"⚠️  File not found: {file_path}")
    
    # Get system overview
    print("\nLiving Document System Overview:")
    overview = api.get_system_overview()
    print(json.dumps(overview, indent=2))
    
    print("\n" + "="*60)
    print("Living Document System Operational!")
    print("• All documents are now living and evolvable")
    print("• Source code is automatically analyzed")
    print("• Relationships are discovered automatically")
    print("• Evolution is tracked and versioned")
    print("• Everything becomes a living, breathing system")
