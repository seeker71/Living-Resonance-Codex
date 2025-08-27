#!/usr/bin/env python3
"""
Digital Asset Manager - Living Codex

This module implements the Living Codex principle: "Everything is just nodes"
where the digital asset management system is represented as nodes that can:

1. Manage digital assets (images, documents, videos, audio) as nodes
2. Extract and store metadata as nodes
3. Handle content hashing and storage as nodes
4. Provide asset transformation and retrieval as nodes

This transformation demonstrates the Living Codex principles:
- Generic Node Structure (everything is nodes)
- Meta-Circular Architecture (system describes itself)
- API-First Evolution (use only API for operations)
- Fractal Self-Similarity (every level mirrors every other level)

The Digital Asset Manager represents the PLASMA layer (Dynamic Content) state in the programming language ontology.
"""

import os
import sys
import json
import hashlib
import mimetypes
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime
import logging

# Image processing
try:
    from PIL import Image, ExifTags
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False

# Audio processing
try:
    import mutagen
    MUTAGEN_AVAILABLE = True
except ImportError:
    MUTAGEN_AVAILABLE = False

# Video processing
try:
    import cv2
    OPENCV_AVAILABLE = True
except ImportError:
    OPENCV_AVAILABLE = False

# Document processing
try:
    import PyPDF2
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False

# Import the Shared Node System, GenericNode, and Database Persistence System
from .shared_node_system import SharedNodeSystem
from .generic_node_system import GenericNode
from .database_persistence_system import DatabasePersistenceSystem

logger = logging.getLogger(__name__)

class DigitalAssetNodeSystem(SharedNodeSystem):
    """
    Digital Asset Management System using Shared Node Structure
    
    This implements the Living Codex principle: "Everything is just nodes"
    - Asset types are nodes
    - Asset statuses are nodes
    - Asset metadata are nodes
    - Digital assets are nodes
    - Everything emerges through the system's own operation
    - All nodes stored in centralized storage
    
    The Digital Asset Manager represents the PLASMA layer (Dynamic Content) state in the programming language ontology:
    - Dynamic content management, energetic transformation
    - Metadata extraction, content hashing, storage optimization
    - Asset processing, thumbnail generation, format conversion
    - Content discovery, tagging, categorization
    """
    
    def __init__(self, database: DatabasePersistenceSystem, storage_root: str = "digital_assets"):
        super().__init__("DigitalAssetNodeSystem")
        self.database = database
        self.storage_root = Path(storage_root)
        self.storage_root.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different asset types
        self._create_storage_structure()
        
        # Initialize the digital asset system nodes
        self._initialize_digital_asset_system_nodes()
        
        logger.info(f"✅ DigitalAssetNodeSystem initialized with storage: {self.storage_root}")
    
    def _create_storage_structure(self):
        """Create storage directory structure"""
        # Create subdirectories for different asset types
        asset_types = ['image', 'document', 'video', 'audio', 'archive', 'code', 'data', 'unknown']
        for asset_type in asset_types:
            (self.storage_root / asset_type).mkdir(parents=True, exist_ok=True)
        
        # Create thumbnails directory
        (self.storage_root / "thumbnails").mkdir(parents=True, exist_ok=True)
    
    def _initialize_digital_asset_system_nodes(self):
        """
        Initialize digital asset system nodes - the foundation of the asset management system
        
        This implements the "Bootstrap Paradox" principle:
        - Start with minimal, self-referential nodes
        - Use the system to describe itself
        - Create the specification as the final node
        - The system becomes what it describes
        """
        
        # Create the root digital asset system node
        root_node = self.create_node(
            node_type='digital_asset_system_root',
            name='Digital Asset Management System Root',
            content='This is the root node of the Digital Asset Management System. It represents the energetic, transformative content management layer for all Living Codex digital assets.',
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,  # Dynamic Content
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 1.0,
                'epistemic_label': 'content_management',
                'system_principle': 'Everything is just nodes - digital assets as content nodes',
                'meta_circular': True,
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Energetic, transformative content management layer for digital assets'
            }
        )
        
        # Create the Asset Type node
        asset_type_node = self.create_node(
            node_type='asset_type',
            name='Asset Type - Content Blueprint',
            content='Asset Type represents the content blueprint - defines different types of digital assets',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.95,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Content blueprint for different digital asset types'
            }
        )
        
        # Create the Asset Status node
        asset_status_node = self.create_node(
            node_type='asset_status',
            name='Asset Status - Processing Blueprint',
            content='Asset Status represents the processing blueprint - defines different processing states of digital assets',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.95,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Processing blueprint for different asset processing states'
            }
        )
        
        # Create the Asset Metadata node
        asset_metadata_node = self.create_node(
            node_type='asset_metadata',
            name='Asset Metadata - Information Blueprint',
            content='Asset Metadata represents the information blueprint - defines metadata structure for digital assets',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.9,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Information blueprint for digital asset metadata structure'
            }
        )
        
        # Create the Digital Asset node
        digital_asset_node = self.create_node(
            node_type='digital_asset',
            name='Digital Asset - Content Instance Blueprint',
            content='Digital Asset represents the content instance blueprint - defines how digital assets are stored and managed',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.9,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Content instance blueprint for digital asset storage and management'
            }
        )
        
        # Create the Content Hash node
        content_hash_node = self.create_node(
            node_type='content_hash',
            name='Content Hash - Integrity Blueprint',
            content='Content Hash represents the integrity blueprint - defines content hashing for digital assets',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.85,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Integrity blueprint for content hashing and verification'
            }
        )
        
        # Create the Thumbnail node
        thumbnail_node = self.create_node(
            node_type='thumbnail',
            name='Thumbnail - Preview Blueprint',
            content='Thumbnail represents the preview blueprint - defines thumbnail generation for digital assets',
            parent_id=root_node.node_id,
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.85,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'description': 'Preview blueprint for thumbnail generation and display'
            }
        )
        
        print(f"🌟 Digital Asset Management System initialized with {len(self.storage.get_all_nodes())} foundation nodes")
        print(f"🎨 Asset Type: {asset_type_node.name} (ID: {asset_type_node.node_id})")
        print(f"🔄 Asset Status: {asset_status_node.name} (ID: {asset_status_node.node_id})")
        print(f"📊 Asset Metadata: {asset_metadata_node.name} (ID: {asset_metadata_node.node_id})")
        print(f"💾 Digital Asset: {digital_asset_node.name} (ID: {digital_asset_node.node_id})")
        print(f"🔐 Content Hash: {content_hash_node.name} (ID: {content_hash_node.node_id})")
        print(f"🖼️ Thumbnail: {thumbnail_node.name} (ID: {thumbnail_node.node_id})")
    
    def create_asset_type_node(self, type_name: str, description: str = "") -> GenericNode:
        """Create an asset type node"""
        return self.create_node(
            node_type='asset_type_instance',
            name=f"Asset Type: {type_name}",
            content=f'Asset type instance: {type_name} - {description}',
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.9,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'type_name': type_name,
                'description': description,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def create_asset_status_node(self, status_name: str, description: str = "") -> GenericNode:
        """Create an asset status node"""
        return self.create_node(
            node_type='asset_status_instance',
            name=f"Asset Status: {status_name}",
            content=f'Asset status instance: {status_name} - {description}',
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.9,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'status_name': status_name,
                'description': description,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def create_asset_metadata_node(self, metadata_data: Dict[str, Any]) -> GenericNode:
        """Create an asset metadata node"""
        return self.create_node(
            node_type='asset_metadata_instance',
            name=f"Asset Metadata: {metadata_data.get('mime_type', 'Unknown')}",
            content=f'Asset metadata instance: {metadata_data.get("mime_type", "Unknown")}',
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.9,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'metadata_data': metadata_data,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def create_digital_asset_node(self, asset_data: Dict[str, Any]) -> GenericNode:
        """Create a digital asset node"""
        return self.create_node(
            node_type='digital_asset_instance',
            name=f"Digital Asset: {asset_data.get('original_filename', 'Unknown')}",
            content=f'Digital asset instance: {asset_data.get("original_filename", "Unknown")}',
            metadata={
                'water_state': 'plasma',
                'fractal_layer': 3,
                'chakra': 'solar_plexus',
                'frequency': 741,
                'color': '#FFD700',
                'planet': 'Sun',
                'consciousness_mode': 'Transformation, Energy',
                'quantum_state': 'excited',
                'resonance_score': 0.9,
                'epistemic_label': 'content_management',
                'programming_ontology_layer': 'plasma_dynamic_content',
                'asset_data': asset_data,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def get_system_resonance(self) -> Dict[str, Any]:
        """Get system resonance information - meta-circular self-description"""
        digital_asset_nodes = [node for node in self.nodes.values() if node.metadata.get('programming_ontology_layer') == 'plasma_dynamic_content']
        type_nodes = [node for node in self.nodes.values() if node.node_type == 'asset_type']
        status_nodes = [node for node in self.nodes.values() if node.node_type == 'asset_status']
        metadata_nodes = [node for node in self.nodes.values() if node.node_type == 'asset_metadata']
        asset_nodes = [node for node in self.nodes.values() if node.node_type == 'digital_asset']
        
        return {
            'total_nodes': len(self.nodes),
            'digital_asset_nodes': len(digital_asset_nodes),
            'type_nodes': len(type_nodes),
            'status_nodes': len(status_nodes),
            'metadata_nodes': len(metadata_nodes),
            'asset_nodes': len(asset_nodes),
            'water_states': list(set(node.get_water_state() for node in self.nodes.values())),
            'chakras': list(set(node.get_chakra() for node in self.nodes.values())),
            'frequencies': list(set(node.get_frequency() for node in self.nodes.values())),
            'average_resonance': sum(node.metadata.get('resonance_score', 0) for node in self.nodes.values()) / max(len(self.nodes), 1),
            'system_principle': 'Everything is just nodes - digital assets as content nodes',
            'meta_circular': True,
            'fractal_self_similar': True,
            'living_document': True,
            'programming_ontology': 'plasma_dynamic_content_layer'
        }
    
    def calculate_content_hash(self, file_path: str) -> str:
        """Calculate SHA-256 hash of file content - content integrity node creation"""
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            
            # Create content hash node
            hash_value = hash_sha256.hexdigest()
            self.create_node(
                node_type='content_hash_instance',
                name=f"Content Hash: {hash_value[:8]}...",
                content=f'Content hash instance: {hash_value} for file {file_path}',
                metadata={
                    'water_state': 'plasma',
                    'fractal_layer': 3,
                    'chakra': 'solar_plexus',
                    'frequency': 741,
                    'color': '#FFD700',
                    'planet': 'Sun',
                    'consciousness_mode': 'Transformation, Energy',
                    'quantum_state': 'excited',
                    'resonance_score': 0.9,
                    'epistemic_label': 'content_management',
                    'programming_ontology_layer': 'plasma_dynamic_content',
                    'hash_value': hash_value,
                    'file_path': file_path,
                    'hash_algorithm': 'SHA-256',
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return hash_value
        except Exception as e:
            logger.error(f"Failed to calculate hash for {file_path}: {e}")
            return ""
    
    def extract_metadata(self, file_path: str, asset_type: str) -> Dict[str, Any]:
        """Extract comprehensive metadata from file - metadata node creation"""
        try:
            file_stat = os.stat(file_path)
            mime_type, _ = mimetypes.guess_type(file_path)
            
            # Basic metadata
            metadata = {
                'file_size': file_stat.st_size,
                'mime_type': mime_type or "application/octet-stream",
                'creation_date': datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
                'modification_date': datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                'asset_type': asset_type
            }
            
            # Type-specific metadata extraction
            type_metadata = {}
            if asset_type == "image":
                type_metadata = self._extract_image_metadata(file_path)
            elif asset_type == "audio":
                type_metadata = self._extract_audio_metadata(file_path)
            elif asset_type == "video":
                type_metadata = self._extract_video_metadata(file_path)
            elif asset_type == "document":
                type_metadata = self._extract_document_metadata(file_path)
            
            # Store additional metadata in custom_fields
            metadata['custom_fields'] = type_metadata
            
            # Create metadata node
            self.create_asset_metadata_node(metadata)
            
            return metadata
            
        except Exception as e:
            logger.error(f"Failed to extract metadata from {file_path}: {e}")
            return {}
    
    def _extract_image_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from image files"""
        if not PILLOW_AVAILABLE:
            return {}
        
        try:
            with Image.open(file_path) as img:
                metadata = {
                    'dimensions': img.size,
                    'mode': img.mode,
                    'format': img.format
                }
                
                # Extract EXIF data
                if hasattr(img, '_getexif') and img._getexif():
                    exif = img._getexif()
                    if exif:
                        exif_data = {}
                        for tag_id, value in exif.items():
                            tag = ExifTags.TAGS.get(tag_id, tag_id)
                            exif_data[tag] = value
                        metadata['exif'] = exif_data
                
                return metadata
        except Exception as e:
            logger.warning(f"Failed to extract image metadata from {file_path}: {e}")
            return {}
    
    def _extract_audio_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from audio files"""
        if not MUTAGEN_AVAILABLE:
            return {}
        
        try:
            audio = mutagen.File(file_path)
            if audio:
                metadata = {}
                if hasattr(audio, 'info'):
                    if hasattr(audio.info, 'length'):
                        metadata['duration'] = audio.info.length
                    if hasattr(audio.info, 'bitrate'):
                        metadata['bitrate'] = audio.info.bitrate
                return metadata
        except Exception as e:
            logger.warning(f"Failed to extract audio metadata from {file_path}: {e}")
        
        return {}
    
    def _extract_video_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from video files"""
        if not OPENCV_AVAILABLE:
            return {}
        
        try:
            cap = cv2.VideoCapture(file_path)
            if cap.isOpened():
                metadata = {
                    'fps': cap.get(cv2.CAP_PROP_FPS),
                    'frame_count': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
                    'dimensions': (
                        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    )
                }
                cap.release()
                return metadata
        except Exception as e:
            logger.warning(f"Failed to extract video metadata from {file_path}: {e}")
        
        return {}
    
    def _extract_document_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from document files"""
        if not PYPDF2_AVAILABLE or not file_path.lower().endswith('.pdf'):
            return {}
        
        try:
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                metadata = {
                    'page_count': len(pdf_reader.pages),
                    'title': pdf_reader.metadata.get('/Title', ''),
                    'author': pdf_reader.metadata.get('/Author', ''),
                    'subject': pdf_reader.metadata.get('/Subject', ''),
                    'creator': pdf_reader.metadata.get('/Creator', '')
                }
                return metadata
        except Exception as e:
            logger.warning(f"Failed to extract PDF metadata from {file_path}: {e}")
        
        return {}
    
    def generate_thumbnail(self, asset_path: str, asset_id: str) -> Optional[str]:
        """Generate thumbnail for supported asset types - thumbnail node creation"""
        try:
            # Determine asset type from file extension
            file_ext = Path(asset_path).suffix.lower()
            asset_type = self._get_asset_type_from_extension(file_ext)
            
            if asset_type == "image" and PILLOW_AVAILABLE:
                thumbnail_path = self.storage_root / "thumbnails" / f"{asset_id}_thumb.jpg"
                
                with Image.open(asset_path) as img:
                    img.thumbnail((200, 200), Image.Resampling.LANCZOS)
                    img.convert('RGB').save(thumbnail_path, 'JPEG', quality=85)
                
                # Create thumbnail node
                self.create_node(
                    node_type='thumbnail_instance',
                    name=f"Thumbnail: {asset_id}",
                    content=f'Thumbnail instance: {asset_id} for asset {asset_path}',
                    metadata={
                        'water_state': 'plasma',
                        'fractal_layer': 3,
                        'chakra': 'solar_plexus',
                        'frequency': 741,
                        'color': '#FFD700',
                        'planet': 'Sun',
                        'consciousness_mode': 'Transformation, Energy',
                        'quantum_state': 'excited',
                        'resonance_score': 0.85,
                        'epistemic_label': 'content_management',
                        'programming_ontology_layer': 'plasma_dynamic_content',
                        'asset_id': asset_id,
                        'asset_path': asset_path,
                        'thumbnail_path': str(thumbnail_path),
                        'dimensions': (200, 200),
                        'format': 'JPEG',
                        'quality': 85,
                        'created_at': datetime.now().isoformat()
                    }
                )
                
                return str(thumbnail_path)
        except Exception as e:
            logger.warning(f"Failed to generate thumbnail for {asset_id}: {e}")
        
        return None
    
    def _get_asset_type_from_extension(self, file_ext: str) -> str:
        """Get asset type from file extension"""
        image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico'}
        audio_exts = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'}
        video_exts = {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'}
        document_exts = {'.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'}
        archive_exts = {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'}
        code_exts = {'.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go', '.rs'}
        data_exts = {'.json', '.xml', '.yaml', '.yml', '.sql', '.db'}
        
        if file_ext in image_exts:
            return "image"
        elif file_ext in audio_exts:
            return "audio"
        elif file_ext in video_exts:
            return "video"
        elif file_ext in document_exts:
            return "document"
        elif file_ext in archive_exts:
            return "archive"
        elif file_ext in code_exts:
            return "code"
        elif file_ext in data_exts:
            return "data"
        else:
            return "unknown"
    
    def add_asset(self, file_path: str, tags: List[str] = None, 
                  custom_metadata: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Add a new digital asset to the system - complete asset node creation"""
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return None
        
        try:
            # Calculate content hash
            content_hash = self.calculate_content_hash(file_path)
            if not content_hash:
                return None
            
            # Determine asset type
            file_ext = Path(file_path).suffix.lower()
            asset_type = self._get_asset_type_from_extension(file_ext)
            
            # Extract metadata
            metadata = self.extract_metadata(file_path, asset_type)
            
            # Generate asset ID
            asset_id = f"asset_{content_hash[:8]}"
            
            # Copy file to storage
            storage_path = self.storage_root / asset_type / f"{asset_id}{file_ext}"
            shutil.copy2(file_path, storage_path)
            
            # Generate thumbnail
            thumbnail_path = self.generate_thumbnail(str(storage_path), asset_id)
            
            # Prepare asset data
            asset_data = {
                'asset_id': asset_id,
                'original_filename': Path(file_path).name,
                'asset_type': asset_type,
                'content_hash': content_hash,
                'storage_path': str(storage_path),
                'metadata': metadata,
                'tags': tags or [],
                'custom_metadata': custom_metadata or {},
                'thumbnail_path': thumbnail_path,
                'preview_available': thumbnail_path is not None,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            
            # Create digital asset node
            self.create_digital_asset_node(asset_data)
            
            # Create asset type instance node if it doesn't exist
            self.create_asset_type_node(asset_type, f"Asset type for {asset_type} files")
            
            # Create asset status instance node
            self.create_asset_status_node("ready", f"Asset {asset_id} is ready for use")
            
            logger.info(f"✅ Asset added successfully: {asset_id}")
            return asset_data
            
        except Exception as e:
            logger.error(f"Failed to add asset {file_path}: {e}")
            return None
    
    def get_asset_stats(self) -> Dict[str, Any]:
        """Get statistics about stored assets - system resonance analysis"""
        try:
            # Count different types of nodes
            asset_instances = [node for node in self.nodes.values() if node.node_type == 'digital_asset_instance']
            type_instances = [node for node in self.nodes.values() if node.node_type == 'asset_type_instance']
            status_instances = [node for node in self.nodes.values() if node.node_type == 'asset_status_instance']
            metadata_instances = [node for node in self.nodes.values() if node.node_type == 'asset_metadata_instance']
            hash_instances = [node for node in self.nodes.values() if node.node_type == 'content_hash_instance']
            thumbnail_instances = [node for node in self.nodes.values() if node.node_type == 'thumbnail_instance']
            
            # Calculate total size
            total_size = 0
            for asset_node in asset_instances:
                metadata = asset_node.metadata.get('asset_data', {}).get('metadata', {})
                total_size += metadata.get('file_size', 0)
            
            # Group by asset type
            asset_types = {}
            for asset_node in asset_instances:
                asset_data = asset_node.metadata.get('asset_data', {})
                asset_type = asset_data.get('asset_type', 'unknown')
                if asset_type not in asset_types:
                    asset_types[asset_type] = 0
                asset_types[asset_type] += 1
            
            stats = {
                'total_assets': len(asset_instances),
                'total_size_mb': round(total_size / (1024 * 1024), 2),
                'asset_types': asset_types,
                'type_instances': len(type_instances),
                'status_instances': len(status_instances),
                'metadata_instances': len(metadata_instances),
                'hash_instances': len(hash_instances),
                'thumbnail_instances': len(thumbnail_instances),
                'system_resonance': self.get_system_resonance()
            }
            
            return stats
            
        except Exception as e:
            logger.error(f"Failed to get asset stats: {e}")
            return {}
    
    def search_assets(self, query: str = None, asset_type: str = None, tags: List[str] = None) -> List[Dict[str, Any]]:
        """Search for assets based on criteria - content discovery nodes"""
        try:
            results = []
            asset_instances = [node for node in self.nodes.values() if node.node_type == 'digital_asset_instance']
            
            for asset_node in asset_instances:
                asset_data = asset_node.metadata.get('asset_data', {})
                
                # Apply filters
                if asset_type and asset_data.get('asset_type') != asset_type:
                    continue
                
                if query:
                    filename = asset_data.get('original_filename', '').lower()
                    if query.lower() not in filename:
                        continue
                
                if tags:
                    asset_tags = asset_data.get('tags', [])
                    if not any(tag in asset_tags for tag in tags):
                        continue
                
                results.append(asset_data)
            
            # Create search result node
            self.create_node(
                node_type='search_result',
                name=f"Search Result: {len(results)} assets found",
                content=f'Search result: {len(results)} assets found for query "{query}"',
                metadata={
                    'water_state': 'plasma',
                    'fractal_layer': 3,
                    'chakra': 'solar_plexus',
                    'frequency': 741,
                    'color': '#FFD700',
                    'planet': 'Sun',
                    'consciousness_mode': 'Transformation, Energy',
                    'quantum_state': 'excited',
                    'resonance_score': 0.9,
                    'epistemic_label': 'content_management',
                    'programming_ontology_layer': 'plasma_dynamic_content',
                    'query': query,
                    'asset_type': asset_type,
                    'tags': tags,
                    'result_count': len(results),
                    'created_at': datetime.now().isoformat()
                }
            )
            
            return results
            
        except Exception as e:
            logger.error(f"Failed to search assets: {e}")
            return []

# Legacy compatibility - maintain the old interface for now
class DigitalAssetManager(DigitalAssetNodeSystem):
    """
    Legacy compatibility class that inherits from the new node-based system
    
    This demonstrates the Living Codex principle of graceful evolution:
    - New system embodies the principles
    - Old interface remains functional
    - System can describe its own transformation
    """
    
    def __init__(self, database: DatabasePersistenceSystem, storage_root: str = "digital_assets"):
        super().__init__(database, storage_root)
        logger.info("🔄 DigitalAssetManager initialized with new node-based system")
        logger.info("✨ This system now embodies Living Codex principles")
        logger.info("🌟 Everything is just nodes - digital assets as content nodes")
        logger.info("🔥 Digital asset system represents PLASMA (Dynamic Content) state in programming language ontology")

async def main():
    """Demo of digital asset management capabilities"""
    print("🎨 Digital Asset Manager - Living Codex")
    print("=" * 50)
    
    # Initialize systems
    from .database_persistence_system import DatabasePersistenceSystem
    database = DatabasePersistenceSystem(db_path="asset_demo.db")
    asset_manager = DigitalAssetManager(database)
    
    print(f"✅ Asset manager initialized")
    print(f"📁 Storage root: {asset_manager.storage_root}")
    
    # Show capabilities
    print("\n🎯 Supported Asset Types:")
    asset_types = ['image', 'document', 'video', 'audio', 'archive', 'code', 'data', 'unknown']
    for asset_type in asset_types:
        print(f"   • {asset_type.title()}")
    
    print("\n📊 Available Metadata Extractors:")
    print(f"   • Images: {'✅' if PILLOW_AVAILABLE else '❌'} (Pillow)")
    print(f"   • Audio: {'✅' if MUTAGEN_AVAILABLE else '❌'} (Mutagen)")
    print(f"   • Video: {'✅' if OPENCV_AVAILABLE else '❌'} (OpenCV)")
    print(f"   • Documents: {'✅' if PYPDF2_AVAILABLE else '❌'} (PyPDF2)")
    
    # Get current stats
    stats = asset_manager.get_asset_stats()
    print(f"\n📈 Current Asset Statistics:")
    print(f"   • Total Assets: {stats.get('total_assets', 0)}")
    print(f"   • Total Size: {stats.get('total_size_mb', 0)} MB")
    
    if stats.get('asset_types'):
        print("   • By Type:")
        for asset_type, count in stats['asset_types'].items():
            print(f"     - {asset_type.title()}: {count}")
    
    print("\n💡 Ready for asset management operations!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
