#!/usr/bin/env python3
"""
Fractal Digital Asset Manager Component - Living Codex
Manages digital assets including images, documents, videos, audio, and other media files.
Provides storage, metadata extraction, content hashing, and retrieval capabilities.

Following fractal holographic principles:
- Everything is just nodes
- Self-registration with fractal system
- Fractal self-similarity at every level
"""

import os
import sys
import json
import hashlib
import mimetypes
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
import logging

from .fractal_components import FractalComponent

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

logger = logging.getLogger(__name__)

class AssetType(Enum):
    """Types of digital assets supported"""
    IMAGE = "image"
    DOCUMENT = "document"
    VIDEO = "video"
    AUDIO = "audio"
    ARCHIVE = "archive"
    CODE = "code"
    DATA = "data"
    UNKNOWN = "unknown"

class AssetStatus(Enum):
    """Asset processing status"""
    PENDING = "pending"
    PROCESSING = "processing"
    READY = "ready"
    ERROR = "error"

@dataclass
class AssetMetadata:
    """Metadata for digital assets"""
    file_size: int
    mime_type: str
    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None
    dimensions: Optional[Tuple[int, int]] = None  # width, height for images/videos
    duration: Optional[float] = None  # seconds for audio/video
    bitrate: Optional[int] = None  # for audio/video
    color_space: Optional[str] = None  # for images
    compression: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    tags: List[str] = None
    exif_data: Optional[Dict[str, Any]] = None
    custom_fields: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.custom_fields is None:
            self.custom_fields = {}

@dataclass
class DigitalAsset:
    """Represents a digital asset in the system"""
    asset_id: str
    original_filename: str
    asset_type: AssetType
    file_path: str
    content_hash: str
    metadata: AssetMetadata
    status: AssetStatus
    created_at: datetime
    updated_at: datetime
    tags: List[str] = None
    parent_id: Optional[str] = None
    children: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.children is None:
            self.children = []

class FractalDigitalAssetManagerComponent(FractalComponent):
    """
    Fractal component for digital asset management
    Manages digital assets with metadata extraction and content hashing
    """
    
    def __init__(self):
        super().__init__(
            component_type="digital_asset_management_system",
            name="Fractal Digital Asset Management System",
            content="Digital asset management system for images, documents, videos, and other media",
            fractal_layer=6,  # Technological Prototypes layer
            water_state="liquid",  # Flow, adaptability, relation
            frequency=741,  # Throat chakra - communication and expression
            chakra="throat"
        )
        
        # Initialize storage paths
        self.base_storage_path = Path("digital_assets")
        self.base_storage_path.mkdir(exist_ok=True)
        
        # Asset type storage paths
        self.asset_type_paths = {
            AssetType.IMAGE: self.base_storage_path / "images",
            AssetType.DOCUMENT: self.base_storage_path / "documents",
            AssetType.VIDEO: self.base_storage_path / "videos",
            AssetType.AUDIO: self.base_storage_path / "audio",
            AssetType.ARCHIVE: self.base_storage_path / "archives",
            AssetType.CODE: self.base_storage_path / "code",
            AssetType.DATA: self.base_storage_path / "data"
        }
        
        # Create storage directories
        for path in self.asset_type_paths.values():
            path.mkdir(exist_ok=True)
        
        # Create asset type capability nodes
        self._create_asset_type_capability_nodes()
        
        # Create processing capability nodes
        self._create_processing_capability_nodes()
    
    def _create_asset_type_capability_nodes(self):
        """Create fractal nodes for supported asset types"""
        for asset_type in AssetType:
            if asset_type == AssetType.UNKNOWN:
                continue
                
            self.create_child_node(
                node_type="asset_type_support",
                name=f"{asset_type.value.title()} Asset Support",
                content=f"Support for {asset_type.value} assets",
                metadata={
                    "asset_type": asset_type.value,
                    "storage_path": str(self.asset_type_paths[asset_type]),
                    "supported": True
                },
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def _create_processing_capability_nodes(self):
        """Create fractal nodes for processing capabilities"""
        capabilities = [
            {
                "name": "Image Processing",
                "content": "Image metadata extraction and processing",
                "metadata": {"available": PILLOW_AVAILABLE, "library": "Pillow"}
            },
            {
                "name": "Audio Processing",
                "content": "Audio metadata extraction and processing",
                "metadata": {"available": MUTAGEN_AVAILABLE, "library": "mutagen"}
            },
            {
                "name": "Video Processing",
                "content": "Video metadata extraction and processing",
                "metadata": {"available": OPENCV_AVAILABLE, "library": "OpenCV"}
            },
            {
                "name": "Document Processing",
                "content": "Document metadata extraction and processing",
                "metadata": {"available": PYPDF2_AVAILABLE, "library": "PyPDF2"}
            },
            {
                "name": "Content Hashing",
                "content": "SHA-256 content hashing for deduplication",
                "metadata": {"algorithm": "SHA-256", "purpose": "deduplication"}
            },
            {
                "name": "Metadata Extraction",
                "content": "Automatic metadata extraction from assets",
                "metadata": {"feature": "auto_extraction", "scope": "comprehensive"}
            }
        ]
        
        for capability in capabilities:
            self.create_child_node(
                node_type="processing_capability",
                name=capability["name"],
                content=capability["content"],
                metadata=capability["metadata"],
                structure_info={
                    "fractal_depth": 2,
                    "self_similar": True,
                    "meta_circular": False,
                    "holographic": True
                }
            )
    
    def add_asset(self, file_path: str, tags: List[str] = None, parent_id: Optional[str] = None) -> Dict[str, Any]:
        """Add a new digital asset to the system"""
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return {"success": False, "error": f"File not found: {file_path}"}
            
            # Determine asset type
            asset_type = self._detect_asset_type(file_path)
            
            # Generate content hash
            content_hash = self._generate_content_hash(file_path)
            
            # Extract metadata
            metadata = self._extract_metadata(file_path, asset_type)
            
            # Generate asset ID
            asset_id = f"{asset_type.value}_{content_hash[:8]}"
            
            # Copy file to appropriate storage location
            storage_path = self._store_asset_file(file_path, asset_type, content_hash)
            
            # Create asset object
            asset = DigitalAsset(
                asset_id=asset_id,
                original_filename=file_path.name,
                asset_type=asset_type,
                file_path=str(storage_path),
                content_hash=content_hash,
                metadata=metadata,
                status=AssetStatus.READY,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                tags=tags or [],
                parent_id=parent_id,
                children=[]
            )
            
            # Create fractal node for the asset
            self._create_asset_node(asset)
            
            return {
                "success": True,
                "asset_id": asset_id,
                "asset_type": asset_type.value,
                "content_hash": content_hash,
                "file_size": metadata.file_size
            }
            
        except Exception as e:
            logger.error(f"Error adding asset {file_path}: {e}")
            return {"success": False, "error": str(e)}
    
    def _detect_asset_type(self, file_path: Path) -> AssetType:
        """Detect the type of asset based on file extension and content"""
        mime_type, _ = mimetypes.guess_type(str(file_path))
        
        if mime_type:
            if mime_type.startswith('image/'):
                return AssetType.IMAGE
            elif mime_type.startswith('video/'):
                return AssetType.VIDEO
            elif mime_type.startswith('audio/'):
                return AssetType.AUDIO
            elif mime_type.startswith('application/pdf'):
                return AssetType.DOCUMENT
            elif mime_type.startswith('text/'):
                if file_path.suffix.lower() in ['.py', '.js', '.html', '.css', '.java', '.cpp']:
                    return AssetType.CODE
                else:
                    return AssetType.DOCUMENT
        
        # Fallback based on extension
        ext = file_path.suffix.lower()
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            return AssetType.IMAGE
        elif ext in ['.mp4', '.avi', '.mov', '.wmv', '.flv']:
            return AssetType.VIDEO
        elif ext in ['.mp3', '.wav', '.flac', '.aac']:
            return AssetType.AUDIO
        elif ext in ['.pdf', '.doc', '.docx', '.txt']:
            return AssetType.DOCUMENT
        elif ext in ['.zip', '.rar', '.7z', '.tar', '.gz']:
            return AssetType.ARCHIVE
        elif ext in ['.py', '.js', '.html', '.css', '.java', '.cpp']:
            return AssetType.CODE
        elif ext in ['.csv', '.json', '.xml', '.yaml', '.yml']:
            return AssetType.DATA
        
        return AssetType.UNKNOWN
    
    def _generate_content_hash(self, file_path: Path) -> str:
        """Generate SHA-256 hash of file content"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _extract_metadata(self, file_path: Path, asset_type: AssetType) -> AssetMetadata:
        """Extract metadata from the asset file"""
        file_size = file_path.stat().st_size
        mime_type, _ = mimetypes.guess_type(str(file_path))
        
        metadata = AssetMetadata(
            file_size=file_size,
            mime_type=mime_type or "application/octet-stream",
            creation_date=datetime.fromtimestamp(file_path.stat().st_ctime),
            modification_date=datetime.fromtimestamp(file_path.stat().st_mtime)
        )
        
        # Extract type-specific metadata
        if asset_type == AssetType.IMAGE and PILLOW_AVAILABLE:
            metadata = self._extract_image_metadata(file_path, metadata)
        elif asset_type == AssetType.AUDIO and MUTAGEN_AVAILABLE:
            metadata = self._extract_audio_metadata(file_path, metadata)
        elif asset_type == AssetType.VIDEO and OPENCV_AVAILABLE:
            metadata = self._extract_video_metadata(file_path, metadata)
        elif asset_type == AssetType.DOCUMENT and PYPDF2_AVAILABLE:
            metadata = self._extract_document_metadata(file_path, metadata)
        
        return metadata
    
    def _extract_image_metadata(self, file_path: Path, metadata: AssetMetadata) -> AssetMetadata:
        """Extract metadata from image files"""
        try:
            with Image.open(file_path) as img:
                metadata.dimensions = img.size
                metadata.color_space = img.mode
                
                # Extract EXIF data
                if hasattr(img, '_getexif') and img._getexif():
                    exif = img._getexif()
                    if exif:
                        metadata.exif_data = {}
                        for tag_id, value in exif.items():
                            tag = ExifTags.TAGS.get(tag_id, tag_id)
                            metadata.exif_data[tag] = value
        except Exception as e:
            logger.warning(f"Could not extract image metadata: {e}")
        
        return metadata
    
    def _extract_audio_metadata(self, file_path: Path, metadata: AssetMetadata) -> AssetMetadata:
        """Extract metadata from audio files"""
        try:
            audio = mutagen.File(str(file_path))
            if audio:
                if hasattr(audio, 'info'):
                    if hasattr(audio.info, 'length'):
                        metadata.duration = audio.info.length
                    if hasattr(audio.info, 'bitrate'):
                        metadata.bitrate = audio.info.bitrate
                
                # Extract tags
                if hasattr(audio, 'tags'):
                    for key, value in audio.tags.items():
                        if key.lower() in ['title', 'artist', 'album']:
                            if key.lower() == 'title':
                                metadata.title = str(value[0]) if value else None
                            elif key.lower() == 'artist':
                                metadata.author = str(value[0]) if value else None
        except Exception as e:
            logger.warning(f"Could not extract audio metadata: {e}")
        
        return metadata
    
    def _extract_video_metadata(self, file_path: Path, metadata: AssetMetadata) -> AssetMetadata:
        """Extract metadata from video files"""
        try:
            cap = cv2.VideoCapture(str(file_path))
            if cap.isOpened():
                metadata.dimensions = (
                    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                )
                metadata.duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
                cap.release()
        except Exception as e:
            logger.warning(f"Could not extract video metadata: {e}")
        
        return metadata
    
    def _extract_document_metadata(self, file_path: Path, metadata: AssetMetadata) -> AssetMetadata:
        """Extract metadata from document files"""
        try:
            if file_path.suffix.lower() == '.pdf':
                with open(file_path, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    metadata.author = pdf.metadata.get('/Author', None)
                    metadata.title = pdf.metadata.get('/Title', None)
                    metadata.description = pdf.metadata.get('/Subject', None)
        except Exception as e:
            logger.warning(f"Could not extract document metadata: {e}")
        
        return metadata
    
    def _store_asset_file(self, file_path: Path, asset_type: AssetType, content_hash: str) -> Path:
        """Store the asset file in the appropriate directory"""
        storage_dir = self.asset_type_paths[asset_type]
        extension = file_path.suffix
        new_filename = f"{content_hash}{extension}"
        storage_path = storage_dir / new_filename
        
        # Copy file if it doesn't exist
        if not storage_path.exists():
            shutil.copy2(file_path, storage_path)
        
        return storage_path
    
    def _create_asset_node(self, asset: DigitalAsset):
        """Create fractal node for the digital asset"""
        self.create_child_node(
            node_type="digital_asset",
            name=asset.original_filename,
            content=f"Digital asset: {asset.original_filename}",
            metadata={
                "asset_id": asset.asset_id,
                "asset_type": asset.asset_type.value,
                "file_size": asset.metadata.file_size,
                "mime_type": asset.metadata.mime_type,
                "content_hash": asset.content_hash,
                "status": asset.status.value,
                "tags": asset.tags,
                "parent_id": asset.parent_id
            },
            structure_info={
                "fractal_depth": 3,
                "self_similar": True,
                "meta_circular": False,
                "holographic": True
            }
        )
    
    def get_asset(self, asset_id: str) -> Optional[DigitalAsset]:
        """Get an asset by ID"""
        # This would query the fractal system for the asset
        # For now, return None as this is a simplified implementation
        return None
    
    def search_assets(self, query: str = None, asset_type: AssetType = None, tags: List[str] = None) -> List[DigitalAsset]:
        """Search for assets based on criteria"""
        # This would query the fractal system for assets
        # For now, return empty list as this is a simplified implementation
        return []
    
    def get_asset_manager_status(self) -> Dict[str, Any]:
        """Get current asset manager status and capabilities"""
        return {
            "base_storage_path": str(self.base_storage_path),
            "supported_asset_types": [t.value for t in AssetType if t != AssetType.UNKNOWN],
            "processing_capabilities": {
                "image_processing": PILLOW_AVAILABLE,
                "audio_processing": MUTAGEN_AVAILABLE,
                "video_processing": OPENCV_AVAILABLE,
                "document_processing": PYPDF2_AVAILABLE
            },
            "storage_paths": {t.value: str(p) for t, p in self.asset_type_paths.items()},
            "capabilities": [
                "asset_type_detection",
                "metadata_extraction",
                "content_hashing",
                "file_storage",
                "tag_management"
            ]
        }

# Create and register the fractal component
fractal_digital_asset_manager = FractalDigitalAssetManagerComponent()
