#!/usr/bin/env python3
"""
Test Digital Asset Management System
Creates sample files and demonstrates asset management capabilities
"""

import os
import tempfile
import shutil
from pathlib import Path

def create_sample_files():
    """Create sample files for testing"""
    # Create temporary directory for test files
    test_dir = Path("test_assets")
    test_dir.mkdir(exist_ok=True)
    
    sample_files = []
    
    # Create a simple text file
    text_file = test_dir / "sample_document.txt"
    with open(text_file, 'w') as f:
        f.write("This is a sample text document for testing the Living Codex digital asset management system.\n")
        f.write("It contains multiple lines of text to demonstrate document processing capabilities.\n")
        f.write("Tags: document, text, sample, test\n")
    sample_files.append(str(text_file))
    
    # Create a JSON data file
    json_file = test_dir / "sample_data.json"
    with open(json_file, 'w') as f:
        f.write('{\n')
        f.write('  "title": "Sample JSON Data",\n')
        f.write('  "description": "Test data for digital asset management",\n')
        f.write('  "type": "configuration",\n')
        f.write('  "tags": ["json", "data", "config", "sample"],\n')
        f.write('  "version": "1.0.0",\n')
        f.write('  "metadata": {\n')
        f.write('    "created": "2024-01-01",\n')
        f.write('    "author": "Living Codex System"\n')
        f.write('  }\n')
        f.write('}\n')
    sample_files.append(str(json_file))
    
    # Create a Python code file
    code_file = test_dir / "sample_code.py"
    with open(code_file, 'w') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('"""\n')
        f.write('Sample Python Code for Asset Management Testing\n')
        f.write('"""\n\n')
        f.write('def hello_world():\n')
        f.write('    """Simple function for demonstration"""\n')
        f.write('    print("Hello from the Living Codex!")\n\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    hello_world()\n')
    sample_files.append(str(code_file))
    
    # Create a CSV data file
    csv_file = test_dir / "sample_data.csv"
    with open(csv_file, 'w') as f:
        f.write('id,name,type,value,description\n')
        f.write('1,Node Alpha,concept,100,Primary knowledge node\n')
        f.write('2,Node Beta,relationship,75,Connection between concepts\n')
        f.write('3,Node Gamma,data,50,Information storage node\n')
        f.write('4,Node Delta,process,125,Computational process node\n')
    sample_files.append(str(csv_file))
    
    # Create an HTML file
    html_file = test_dir / "sample_page.html"
    with open(html_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('    <meta charset="UTF-8">\n')
        f.write('    <title>Living Codex Sample Page</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('    <h1>Living Codex Digital Asset Management</h1>\n')
        f.write('    <p>This is a sample HTML page for testing asset management.</p>\n')
        f.write('    <ul>\n')
        f.write('        <li>Asset Type: HTML Document</li>\n')
        f.write('        <li>Purpose: Testing web content storage</li>\n')
        f.write('        <li>Tags: html, web, sample, test</li>\n')
        f.write('    </ul>\n')
        f.write('</body>\n')
        f.write('</html>\n')
    sample_files.append(str(html_file))
    
    return sample_files

def test_asset_management():
    """Test the digital asset management system"""
    try:
        # Import the asset manager
        from ..core.database_persistence_system import DatabasePersistenceSystem
        from ..core.digital_asset_manager import DigitalAssetManager, AssetType
        
        print("🎨 Testing Digital Asset Management System")
        print("=" * 50)
        
        # Initialize systems
        database = DatabasePersistenceSystem(db_path="test_assets.db")
        asset_manager = DigitalAssetManager(database, storage_root="test_digital_assets")
        
        print("✅ Asset manager initialized")
        print(f"📁 Storage root: {asset_manager.storage_root}")
        
        # Create sample files
        print("\n📝 Creating sample files...")
        sample_files = create_sample_files()
        
        for file_path in sample_files:
            print(f"   📄 {file_path}")
        
        # Add assets to the system
        print("\n📤 Adding assets to the system...")
        added_assets = []
        
        for i, file_path in enumerate(sample_files):
            filename = os.path.basename(file_path)
            tags = [f"test_{i+1}", "sample", "demo"]
            
            print(f"\n   Adding: {filename}")
            asset = asset_manager.add_asset(file_path, tags=tags)
            
            if asset:
                print(f"   ✅ Added: {asset.asset_id}")
                print(f"      Type: {asset.asset_type.value}")
                print(f"      Size: {asset.metadata.file_size} bytes")
                print(f"      Hash: {asset.content_hash[:12]}...")
                added_assets.append(asset)
            else:
                print(f"   ❌ Failed to add {filename}")
        
        # Test search functionality
        print(f"\n🔍 Testing search functionality...")
        
        # Search by type
        print("\n   Searching for documents:")
        documents = asset_manager.search_assets(asset_type=AssetType.DOCUMENT)
        for doc in documents:
            print(f"      📄 {doc.original_filename}")
        
        # Search by query
        print("\n   Searching for 'sample':")
        sample_assets = asset_manager.search_assets(query="sample")
        for asset in sample_assets:
            print(f"      📁 {asset.original_filename} ({asset.asset_type.value})")
        
        # Test asset info
        if added_assets:
            print(f"\n📋 Testing asset info for: {added_assets[0].original_filename}")
            asset = asset_manager.get_asset(added_assets[0].asset_id)
            if asset:
                print(f"   ID: {asset.asset_id}")
                print(f"   Type: {asset.asset_type.value}")
                print(f"   Size: {asset.metadata.file_size:,} bytes")
                print(f"   MIME: {asset.metadata.mime_type}")
                print(f"   Tags: {', '.join(asset.metadata.tags)}")
        
        # Test metadata update
        print(f"\n🏷️  Testing metadata updates...")
        if added_assets:
            asset_id = added_assets[0].asset_id
            new_tags = ["updated", "metadata_test"]
            
            # Get current tags
            current_asset = asset_manager.get_asset(asset_id)
            if current_asset:
                all_tags = list(set(current_asset.metadata.tags + new_tags))
                success = asset_manager.update_asset_metadata(asset_id, {"tags": all_tags})
                
                if success:
                    print(f"   ✅ Updated tags for {current_asset.original_filename}")
                    updated_asset = asset_manager.get_asset(asset_id)
                    print(f"   🏷️  New tags: {', '.join(updated_asset.metadata.tags)}")
                else:
                    print(f"   ❌ Failed to update metadata")
        
        # Get statistics
        print(f"\n📊 Asset Statistics:")
        stats = asset_manager.get_asset_stats()
        print(f"   Total Assets: {stats.get('total_assets', 0)}")
        print(f"   Total Size: {stats.get('total_size_mb', 0):.2f} MB")
        print(f"   Storage Root: {stats.get('storage_root', 'Unknown')}")
        
        asset_types = stats.get('asset_types', {})
        if asset_types:
            print(f"   Asset Types:")
            for asset_type, count in asset_types.items():
                print(f"      {asset_type.title()}: {count}")
        
        print(f"\n✅ Digital Asset Management System Test Complete!")
        print(f"📁 Test files created in: test_assets/")
        print(f"🗄️  Asset storage in: test_digital_assets/")
        print(f"💾 Database: test_assets.db")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def cleanup_test_files():
    """Clean up test files"""
    try:
        # Remove test directories
        test_dirs = ["test_assets", "test_digital_assets"]
        for dir_name in test_dirs:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
                print(f"🗑️  Removed: {dir_name}/")
        
        # Remove test database
        test_db = "test_assets.db"
        if os.path.exists(test_db):
            os.remove(test_db)
            print(f"🗑️  Removed: {test_db}")
            
    except Exception as e:
        print(f"⚠️  Cleanup warning: {e}")

if __name__ == "__main__":
    print("🧪 Living Codex - Digital Asset Management Test")
    print("=" * 60)
    
    # Run the test
    success = test_asset_management()
    
    if success:
        print(f"\n🎉 All tests passed!")
        
        # Ask if user wants to clean up
        cleanup = input("\n🗑️  Clean up test files? (y/N): ").strip().lower()
        if cleanup == 'y':
            cleanup_test_files()
            print("✅ Cleanup complete")
        else:
            print("📁 Test files preserved for inspection")
    else:
        print(f"\n❌ Tests failed!")
        
    print(f"\n💡 To test with CLI: python codex_cli.py")
    print(f"   Then try: asset-add test_assets/sample_document.txt")
    print(f"            asset-list")
    print(f"            asset-stats")
