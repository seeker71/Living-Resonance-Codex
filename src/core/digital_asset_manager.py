#!/usr/bin/env python3
"""
Digital Asset Manager - Living Codex
Manages digital assets including images, documents, videos, audio, and other media files.
Provides storage, metadata extraction, content hashing, and retrieval capabilities.
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

from .database_persistence_system import DatabasePersistenceSystem, DatabaseNode, QueryFilter, QueryOptions

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
    content_hash: str
    storage_path: str
    metadata: AssetMetadata
    status: AssetStatus
    created_at: datetime
    updated_at: datetime
    access_count: int = 0
    last_accessed: Optional[datetime] = None
    thumbnail_path: Optional[str] = None
    preview_available: bool = False
    
    def to_database_node(self) -> DatabaseNode:
        """Convert to DatabaseNode for storage"""
        # Convert metadata to dict with proper datetime serialization
        metadata_dict = asdict(self.metadata)
        if metadata_dict.get('creation_date'):
            metadata_dict['creation_date'] = self.metadata.creation_date.isoformat()
        if metadata_dict.get('modification_date'):
            metadata_dict['modification_date'] = self.metadata.modification_date.isoformat()
        
        content = {
            "original_filename": self.original_filename,
            "asset_type": self.asset_type.value,
            "content_hash": self.content_hash,
            "storage_path": self.storage_path,
            "status": self.status.value,
            "access_count": self.access_count,
            "last_accessed": self.last_accessed.isoformat() if self.last_accessed else None,
            "thumbnail_path": self.thumbnail_path,
            "preview_available": self.preview_available,
            "metadata": metadata_dict
        }
        
        return DatabaseNode(
            node_id=self.asset_id,
            node_type="digital_asset",
            name=self.original_filename,
            content=json.dumps(content),
            realm="digital",
            water_state="solid",  # Digital assets are "solid" data
            energy_level=800,  # High energy for valuable digital content
            transformation_cost=200,  # Moderate cost to modify
            parent_id=None,
            children=None,
            metadata={
                "asset_type": self.asset_type.value,
                "mime_type": self.metadata.mime_type,
                "file_size": self.metadata.file_size,
                "content_hash": self.content_hash
            },
            structure_info=None,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

class AssetTypeDetector:
    """Detects asset types based on file extensions and MIME types"""
    
    TYPE_MAPPING = {
        # Images
        '.jpg': AssetType.IMAGE, '.jpeg': AssetType.IMAGE, '.png': AssetType.IMAGE,
        '.gif': AssetType.IMAGE, '.bmp': AssetType.IMAGE, '.tiff': AssetType.IMAGE,
        '.webp': AssetType.IMAGE, '.svg': AssetType.IMAGE, '.ico': AssetType.IMAGE,
        
        # Documents
        '.pdf': AssetType.DOCUMENT, '.doc': AssetType.DOCUMENT, '.docx': AssetType.DOCUMENT,
        '.txt': AssetType.DOCUMENT, '.rtf': AssetType.DOCUMENT, '.odt': AssetType.DOCUMENT,
        '.xls': AssetType.DOCUMENT, '.xlsx': AssetType.DOCUMENT, '.ppt': AssetType.DOCUMENT,
        '.pptx': AssetType.DOCUMENT, '.csv': AssetType.DOCUMENT,
        
        # Videos
        '.mp4': AssetType.VIDEO, '.avi': AssetType.VIDEO, '.mkv': AssetType.VIDEO,
        '.mov': AssetType.VIDEO, '.wmv': AssetType.VIDEO, '.flv': AssetType.VIDEO,
        '.webm': AssetType.VIDEO, '.m4v': AssetType.VIDEO,
        
        # Audio
        '.mp3': AssetType.AUDIO, '.wav': AssetType.AUDIO, '.flac': AssetType.AUDIO,
        '.aac': AssetType.AUDIO, '.ogg': AssetType.AUDIO, '.wma': AssetType.AUDIO,
        '.m4a': AssetType.AUDIO,
        
        # Archives
        '.zip': AssetType.ARCHIVE, '.rar': AssetType.ARCHIVE, '.7z': AssetType.ARCHIVE,
        '.tar': AssetType.ARCHIVE, '.gz': AssetType.ARCHIVE, '.bz2': AssetType.ARCHIVE,
        
        # Code
        '.py': AssetType.CODE, '.js': AssetType.CODE, '.html': AssetType.CODE,
        '.css': AssetType.CODE, '.java': AssetType.CODE, '.cpp': AssetType.CODE,
        '.c': AssetType.CODE, '.h': AssetType.CODE, '.php': AssetType.CODE,
        '.rb': AssetType.CODE, '.go': AssetType.CODE, '.rs': AssetType.CODE,
        
        # Data
        '.json': AssetType.DATA, '.xml': AssetType.DATA, '.yaml': AssetType.DATA,
        '.yml': AssetType.DATA, '.sql': AssetType.DATA, '.db': AssetType.DATA,
    }
    
    @classmethod
    def detect_type(cls, filename: str, mime_type: str = None) -> AssetType:
        """Detect asset type from filename and optional MIME type"""
        # Try extension first
        ext = Path(filename).suffix.lower()
        if ext in cls.TYPE_MAPPING:
            return cls.TYPE_MAPPING[ext]
        
        # Try MIME type
        if mime_type:
            if mime_type.startswith('image/'):
                return AssetType.IMAGE
            elif mime_type.startswith('video/'):
                return AssetType.VIDEO
            elif mime_type.startswith('audio/'):
                return AssetType.AUDIO
            elif mime_type in ['application/pdf', 'application/msword', 'text/plain']:
                return AssetType.DOCUMENT
            elif mime_type.startswith('application/') and 'zip' in mime_type:
                return AssetType.ARCHIVE
            elif mime_type.startswith('text/'):
                return AssetType.CODE
        
        return AssetType.UNKNOWN

class MetadataExtractor:
    """Extracts metadata from various file types"""
    
    @staticmethod
    def extract_image_metadata(file_path: str) -> Dict[str, Any]:
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
                    exif_dict = {}
                    for tag_id, value in img._getexif().items():
                        tag = ExifTags.TAGS.get(tag_id, tag_id)
                        exif_dict[tag] = value
                    metadata['exif'] = exif_dict
                
                return metadata
        except Exception as e:
            logger.warning(f"Failed to extract image metadata from {file_path}: {e}")
            return {}
    
    @staticmethod
    def extract_audio_metadata(file_path: str) -> Dict[str, Any]:
        """Extract metadata from audio files"""
        if not MUTAGEN_AVAILABLE:
            return {}
        
        try:
            audio_file = mutagen.File(file_path)
            if audio_file is None:
                return {}
            
            metadata = {
                'duration': getattr(audio_file.info, 'length', 0),
                'bitrate': getattr(audio_file.info, 'bitrate', 0),
                'channels': getattr(audio_file.info, 'channels', 0),
                'sample_rate': getattr(audio_file.info, 'sample_rate', 0)
            }
            
            # Extract tags
            if audio_file.tags:
                for key, value in audio_file.tags.items():
                    if isinstance(value, list) and value:
                        metadata[key] = str(value[0])
                    else:
                        metadata[key] = str(value)
            
            return metadata
        except Exception as e:
            logger.warning(f"Failed to extract audio metadata from {file_path}: {e}")
            return {}
    
    @staticmethod
    def extract_video_metadata(file_path: str) -> Dict[str, Any]:
        """Extract metadata from video files"""
        if not OPENCV_AVAILABLE:
            return {}
        
        try:
            cap = cv2.VideoCapture(file_path)
            if not cap.isOpened():
                return {}
            
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            metadata = {
                'dimensions': (width, height),
                'fps': fps,
                'frame_count': frame_count,
                'duration': frame_count / fps if fps > 0 else 0
            }
            
            cap.release()
            return metadata
        except Exception as e:
            logger.warning(f"Failed to extract video metadata from {file_path}: {e}")
            return {}
    
    @staticmethod
    def extract_document_metadata(file_path: str) -> Dict[str, Any]:
        """Extract metadata from document files"""
        metadata = {}
        
        if file_path.lower().endswith('.pdf') and PYPDF2_AVAILABLE:
            try:
                with open(file_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    metadata.update({
                        'page_count': len(pdf_reader.pages),
                        'title': pdf_reader.metadata.get('/Title', ''),
                        'author': pdf_reader.metadata.get('/Author', ''),
                        'subject': pdf_reader.metadata.get('/Subject', ''),
                        'creator': pdf_reader.metadata.get('/Creator', ''),
                        'producer': pdf_reader.metadata.get('/Producer', ''),
                        'creation_date': pdf_reader.metadata.get('/CreationDate', ''),
                        'modification_date': pdf_reader.metadata.get('/ModDate', '')
                    })
            except Exception as e:
                logger.warning(f"Failed to extract PDF metadata from {file_path}: {e}")
        
        return metadata

class DigitalAssetManager:
    """Main digital asset management system"""
    
    def __init__(self, database: DatabasePersistenceSystem, storage_root: str = "digital_assets"):
        self.database = database
        self.storage_root = Path(storage_root)
        self.storage_root.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different asset types
        for asset_type in AssetType:
            (self.storage_root / asset_type.value).mkdir(parents=True, exist_ok=True)
        
        # Create thumbnails directory
        (self.storage_root / "thumbnails").mkdir(parents=True, exist_ok=True)
        
        logger.info(f"✅ DigitalAssetManager initialized with storage: {self.storage_root}")
    
    def calculate_content_hash(self, file_path: str) -> str:
        """Calculate SHA-256 hash of file content"""
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except Exception as e:
            logger.error(f"Failed to calculate hash for {file_path}: {e}")
            return ""
    
    def extract_metadata(self, file_path: str, asset_type: AssetType) -> AssetMetadata:
        """Extract comprehensive metadata from file"""
        file_stat = os.stat(file_path)
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # Basic metadata
        metadata = AssetMetadata(
            file_size=file_stat.st_size,
            mime_type=mime_type or "application/octet-stream",
            creation_date=datetime.fromtimestamp(file_stat.st_ctime),
            modification_date=datetime.fromtimestamp(file_stat.st_mtime)
        )
        
        # Type-specific metadata extraction
        type_metadata = {}
        if asset_type == AssetType.IMAGE:
            type_metadata = MetadataExtractor.extract_image_metadata(file_path)
            if 'dimensions' in type_metadata:
                metadata.dimensions = type_metadata['dimensions']
            if 'exif' in type_metadata:
                metadata.exif_data = type_metadata['exif']
        
        elif asset_type == AssetType.AUDIO:
            type_metadata = MetadataExtractor.extract_audio_metadata(file_path)
            if 'duration' in type_metadata:
                metadata.duration = type_metadata['duration']
            if 'bitrate' in type_metadata:
                metadata.bitrate = type_metadata['bitrate']
        
        elif asset_type == AssetType.VIDEO:
            type_metadata = MetadataExtractor.extract_video_metadata(file_path)
            if 'dimensions' in type_metadata:
                metadata.dimensions = type_metadata['dimensions']
            if 'duration' in type_metadata:
                metadata.duration = type_metadata['duration']
        
        elif asset_type == AssetType.DOCUMENT:
            type_metadata = MetadataExtractor.extract_document_metadata(file_path)
        
        # Store additional metadata in custom_fields
        metadata.custom_fields.update(type_metadata)
        
        return metadata
    
    def generate_thumbnail(self, asset: DigitalAsset) -> Optional[str]:
        """Generate thumbnail for supported asset types"""
        if asset.asset_type == AssetType.IMAGE and PILLOW_AVAILABLE:
            try:
                thumbnail_path = self.storage_root / "thumbnails" / f"{asset.asset_id}_thumb.jpg"
                
                with Image.open(asset.storage_path) as img:
                    img.thumbnail((200, 200), Image.Resampling.LANCZOS)
                    img.convert('RGB').save(thumbnail_path, 'JPEG', quality=85)
                
                return str(thumbnail_path)
            except Exception as e:
                logger.warning(f"Failed to generate thumbnail for {asset.asset_id}: {e}")
        
        return None
    
    def add_asset(self, file_path: str, tags: List[str] = None, 
                  custom_metadata: Dict[str, Any] = None) -> Optional[DigitalAsset]:
        """Add a new digital asset to the system"""
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return None
        
        try:
            # Calculate content hash
            content_hash = self.calculate_content_hash(file_path)
            if not content_hash:
                return None
            
            # Check for duplicates
            existing = self.find_asset_by_hash(content_hash)
            if existing:
                logger.info(f"Asset already exists with hash {content_hash}: {existing.original_filename}")
                return existing
            
            # Detect asset type
            original_filename = os.path.basename(file_path)
            mime_type, _ = mimetypes.guess_type(file_path)
            asset_type = AssetTypeDetector.detect_type(original_filename, mime_type)
            
            # Generate unique asset ID
            asset_id = f"asset_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{content_hash[:8]}"
            
            # Determine storage path
            file_extension = Path(file_path).suffix
            storage_filename = f"{asset_id}{file_extension}"
            storage_path = self.storage_root / asset_type.value / storage_filename
            
            # Copy file to storage
            shutil.copy2(file_path, storage_path)
            
            # Extract metadata
            metadata = self.extract_metadata(str(storage_path), asset_type)
            
            # Add custom metadata and tags
            if tags:
                metadata.tags.extend(tags)
            if custom_metadata:
                metadata.custom_fields.update(custom_metadata)
            
            # Create digital asset
            asset = DigitalAsset(
                asset_id=asset_id,
                original_filename=original_filename,
                asset_type=asset_type,
                content_hash=content_hash,
                storage_path=str(storage_path),
                metadata=metadata,
                status=AssetStatus.PROCESSING,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            # Generate thumbnail if possible
            thumbnail_path = self.generate_thumbnail(asset)
            if thumbnail_path:
                asset.thumbnail_path = thumbnail_path
                asset.preview_available = True
            
            # Mark as ready
            asset.status = AssetStatus.READY
            asset.updated_at = datetime.now()
            
            # Store in database
            db_node = asset.to_database_node()
            result = self.database.operations.create_node(db_node)
            
            if result.success:
                logger.info(f"✅ Asset added successfully: {asset_id} ({original_filename})")
                return asset
            else:
                logger.error(f"Failed to store asset in database: {getattr(result, 'error_message', 'Unknown error')}")
                # Clean up storage
                if storage_path.exists():
                    storage_path.unlink()
                return None
                
        except Exception as e:
            logger.error(f"Failed to add asset {file_path}: {e}")
            return None
    
    def get_asset(self, asset_id: str) -> Optional[DigitalAsset]:
        """Retrieve an asset by ID"""
        try:
            result = self.database.operations.query_nodes(
                [QueryFilter("node_id", "=", asset_id)],
                QueryOptions(limit=1)
            )
            
            if result.success and result.data:
                return self._node_to_asset(result.data[0])
            
        except Exception as e:
            logger.error(f"Failed to get asset {asset_id}: {e}")
        
        return None
    
    def find_asset_by_hash(self, content_hash: str) -> Optional[DigitalAsset]:
        """Find asset by content hash"""
        try:
            # Search by content hash in the content JSON
            result = self.database.operations.query_nodes(
                [QueryFilter("content", "LIKE", f'%"content_hash": "{content_hash}"%')],
                QueryOptions(limit=1)
            )
            
            if result.success and result.data:
                return self._node_to_asset(result.data[0])
                
        except Exception as e:
            logger.error(f"Failed to find asset by hash {content_hash}: {e}")
        
        return None
    
    def search_assets(self, query: str = "", asset_type: AssetType = None, 
                     tags: List[str] = None, limit: int = 50) -> List[DigitalAsset]:
        """Search for assets based on various criteria"""
        filters = [QueryFilter("node_type", "=", "digital_asset")]
        
        if asset_type:
            filters.append(QueryFilter("content", "LIKE", f'%"asset_type": "{asset_type.value}"%'))
        
        if query:
            filters.append(QueryFilter("name", "LIKE", f"%{query}%"))
        
        try:
            result = self.database.operations.query_nodes(filters, QueryOptions(limit=limit))
            
            if result.success and result.data:
                assets = [self._node_to_asset(node) for node in result.data]
                
                # Filter by tags if specified
                if tags:
                    assets = [asset for asset in assets if asset and 
                             any(tag in asset.metadata.tags for tag in tags)]
                
                return [asset for asset in assets if asset is not None]
                
        except Exception as e:
            logger.error(f"Failed to search assets: {e}")
        
        return []
    
    def update_asset_metadata(self, asset_id: str, 
                            metadata_updates: Dict[str, Any]) -> bool:
        """Update asset metadata"""
        asset = self.get_asset(asset_id)
        if not asset:
            return False
        
        try:
            # Update metadata fields
            for key, value in metadata_updates.items():
                if hasattr(asset.metadata, key):
                    setattr(asset.metadata, key, value)
                else:
                    asset.metadata.custom_fields[key] = value
            
            asset.updated_at = datetime.now()
            
            # Update in database
            db_node = asset.to_database_node()
            result = self.database.operations.update_node(db_node)
            
            return result.success
            
        except Exception as e:
            logger.error(f"Failed to update asset metadata {asset_id}: {e}")
            return False
    
    def delete_asset(self, asset_id: str, remove_files: bool = True) -> bool:
        """Delete an asset from the system"""
        asset = self.get_asset(asset_id)
        if not asset:
            return False
        
        try:
            # Remove from database
            result = self.database.operations.delete_node(asset_id)
            
            if result.success and remove_files:
                # Remove storage files
                if os.path.exists(asset.storage_path):
                    os.remove(asset.storage_path)
                
                if asset.thumbnail_path and os.path.exists(asset.thumbnail_path):
                    os.remove(asset.thumbnail_path)
                
                logger.info(f"✅ Asset deleted: {asset_id}")
            
            return result.success
            
        except Exception as e:
            logger.error(f"Failed to delete asset {asset_id}: {e}")
            return False
    
    def get_asset_stats(self) -> Dict[str, Any]:
        """Get statistics about stored assets"""
        try:
            # Get all assets
            result = self.database.operations.query_nodes(
                [QueryFilter("node_type", "=", "digital_asset")],
                QueryOptions(limit=1000)
            )
            
            if not result.success:
                return {}
            
            assets = [self._node_to_asset(node) for node in result.data or []]
            assets = [asset for asset in assets if asset is not None]
            
            # Calculate statistics
            total_count = len(assets)
            total_size = sum(asset.metadata.file_size for asset in assets)
            
            type_counts = {}
            for asset in assets:
                asset_type = asset.asset_type.value
                type_counts[asset_type] = type_counts.get(asset_type, 0) + 1
            
            return {
                "total_assets": total_count,
                "total_size_bytes": total_size,
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "asset_types": type_counts,
                "storage_root": str(self.storage_root)
            }
            
        except Exception as e:
            logger.error(f"Failed to get asset stats: {e}")
            return {}
    
    def _node_to_asset(self, node: DatabaseNode) -> Optional[DigitalAsset]:
        """Convert DatabaseNode back to DigitalAsset"""
        try:
            content_data = json.loads(node.content) if node.content else {}
            metadata_data = content_data.get('metadata', {})
            
            # Reconstruct metadata with proper datetime handling
            creation_date = None
            if metadata_data.get('creation_date'):
                try:
                    creation_date = datetime.fromisoformat(metadata_data['creation_date'])
                except (ValueError, TypeError):
                    creation_date = None
            
            modification_date = None
            if metadata_data.get('modification_date'):
                try:
                    modification_date = datetime.fromisoformat(metadata_data['modification_date'])
                except (ValueError, TypeError):
                    modification_date = None
            
            metadata = AssetMetadata(
                file_size=metadata_data.get('file_size', 0),
                mime_type=metadata_data.get('mime_type', 'application/octet-stream'),
                creation_date=creation_date,
                modification_date=modification_date,
                dimensions=tuple(metadata_data['dimensions']) if metadata_data.get('dimensions') else None,
                duration=metadata_data.get('duration'),
                bitrate=metadata_data.get('bitrate'),
                color_space=metadata_data.get('color_space'),
                compression=metadata_data.get('compression'),
                author=metadata_data.get('author'),
                title=metadata_data.get('title'),
                description=metadata_data.get('description'),
                tags=metadata_data.get('tags', []),
                exif_data=metadata_data.get('exif_data'),
                custom_fields=metadata_data.get('custom_fields', {})
            )
            
            return DigitalAsset(
                asset_id=node.node_id,
                original_filename=content_data.get('original_filename', ''),
                asset_type=AssetType(content_data.get('asset_type', 'unknown')),
                content_hash=content_data.get('content_hash', ''),
                storage_path=content_data.get('storage_path', ''),
                metadata=metadata,
                status=AssetStatus(content_data.get('status', 'ready')),
                created_at=node.created_at,
                updated_at=node.updated_at,
                access_count=content_data.get('access_count', 0),
                last_accessed=datetime.fromisoformat(content_data['last_accessed']) if content_data.get('last_accessed') else None,
                thumbnail_path=content_data.get('thumbnail_path'),
                preview_available=content_data.get('preview_available', False)
            )
            
        except Exception as e:
            logger.error(f"Failed to convert node to asset: {e}")
            return None

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
    for asset_type in AssetType:
        print(f"   • {asset_type.value.title()}")
    
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
