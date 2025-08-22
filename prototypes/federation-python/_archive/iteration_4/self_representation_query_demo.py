#!/usr/bin/env python3
"""
Self-Representation Query Demo - Living Codex
Demonstrates how the system can query and understand its own files
through the self-representation system.
"""

import json
import re
from typing import List, Dict, Any, Optional
from self_representation_system import SelfRepresentationSystem

class SelfRepresentationQueryDemo:
    """Demonstrates querying capabilities of the self-representation system"""
    
    def __init__(self):
        self.self_rep_system = SelfRepresentationSystem()
        self.file_representations = {}
        self._load_self_representation_data()
    
    def _load_self_representation_data(self):
        """Load self-representation data from the system"""
        
        print("🔮 Loading Self-Representation Data...")
        
        # Upload files to system
        self.file_representations = self.self_rep_system.upload_files_to_system()
        
        # Create file category ontology
        self.self_rep_system.file_categories = self.self_rep_system.create_file_category_ontology()
        
        print(f"✅ Loaded {len(self.file_representations)} file representations")
    
    def query_files_by_type(self, file_type: str) -> List[Dict[str, Any]]:
        """Query files by file type"""
        
        results = []
        for file_id, file_rep in self.file_representations.items():
            if file_rep.file_type == file_type:
                results.append({
                    "file_id": file_rep.file_id,
                    "file_name": file_rep.file_name,
                    "file_path": file_rep.file_path,
                    "file_size": file_rep.file_size,
                    "water_state": file_rep.water_state,
                    "energy_level": file_rep.energy_level,
                    "content_hash": file_rep.content_hash[:16] + "..."
                })
        
        return results
    
    def query_files_by_water_state(self, water_state: str) -> List[Dict[str, Any]]:
        """Query files by water state"""
        
        results = []
        for file_id, file_rep in self.file_representations.items():
            if file_rep.water_state == water_state:
                results.append({
                    "file_id": file_rep.file_id,
                    "file_name": file_rep.file_name,
                    "file_path": file_rep.file_path,
                    "file_type": file_rep.file_type,
                    "file_size": file_rep.file_size,
                    "energy_level": file_rep.energy_level,
                    "representation": self.self_rep_system._get_representation_for_water_state(water_state)
                })
        
        return results
    
    def query_files_by_content(self, search_term: str, case_sensitive: bool = False) -> List[Dict[str, Any]]:
        """Query files by content search"""
        
        results = []
        search_term_lower = search_term.lower() if not case_sensitive else search_term
        
        for file_id, file_rep in self.file_representations.items():
            # Decode base64 content for search
            try:
                import base64
                content = base64.b64decode(file_rep.content_base64).decode('utf-8')
                
                if case_sensitive:
                    if search_term in content:
                        results.append({
                            "file_id": file_rep.file_id,
                            "file_name": file_rep.file_name,
                            "file_path": file_rep.file_path,
                            "file_type": file_rep.file_type,
                            "water_state": file_rep.water_state,
                            "match_count": content.count(search_term),
                            "content_preview": content[:200] + "..." if len(content) > 200 else content
                        })
                else:
                    if search_term_lower in content.lower():
                        results.append({
                            "file_id": file_rep.file_id,
                            "file_name": file_rep.file_name,
                            "file_path": file_rep.file_path,
                            "file_type": file_rep.file_type,
                            "water_state": file_rep.water_state,
                            "match_count": content.lower().count(search_term_lower),
                            "content_preview": content[:200] + "..." if len(content) > 200 else content
                        })
                        
            except Exception as e:
                # Skip files that can't be decoded
                continue
        
        return results
    
    def query_files_by_metadata(self, metadata_key: str, metadata_value: Any) -> List[Dict[str, Any]]:
        """Query files by metadata"""
        
        results = []
        for file_id, file_rep in self.file_representations.items():
            if metadata_key in file_rep.metadata:
                if file_rep.metadata[metadata_key] == metadata_value:
                    results.append({
                        "file_id": file_rep.file_id,
                        "file_name": file_rep.file_name,
                        "file_path": file_rep.file_path,
                        "file_type": file_rep.file_type,
                        "water_state": file_rep.water_state,
                        "metadata_value": file_rep.metadata[metadata_key]
                    })
        
        return results
    
    def query_files_by_size_range(self, min_size: int, max_size: int) -> List[Dict[str, Any]]:
        """Query files by size range"""
        
        results = []
        for file_id, file_rep in self.file_representations.items():
            if min_size <= file_rep.file_size <= max_size:
                results.append({
                    "file_id": file_rep.file_id,
                    "file_name": file_rep.file_name,
                    "file_path": file_rep.file_path,
                    "file_type": file_rep.file_type,
                    "file_size": file_rep.file_size,
                    "water_state": file_rep.water_state,
                    "energy_level": file_rep.energy_level
                })
        
        return results
    
    def query_meta_circular_files(self) -> List[Dict[str, Any]]:
        """Query files that are meta-circular"""
        
        results = []
        for file_id, file_rep in self.file_representations.items():
            if file_rep.metadata.get("meta_circular", False):
                results.append({
                    "file_id": file_rep.file_id,
                    "file_name": file_rep.file_name,
                    "file_path": file_rep.file_path,
                    "file_type": file_rep.file_type,
                    "water_state": file_rep.water_state,
                    "meta_circular": True,
                    "self_contained": file_rep.metadata.get("self_contained", False)
                })
        
        return results
    
    def query_files_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Query files by category"""
        
        results = []
        for file_id, file_rep in self.file_representations.items():
            if file_rep.structure_info.get("file_category") == category:
                results.append({
                    "file_id": file_rep.file_id,
                    "file_name": file_rep.file_name,
                    "file_path": file_rep.file_path,
                    "file_type": file_rep.file_type,
                    "water_state": file_rep.water_state,
                    "category": category,
                    "energy_level": file_rep.energy_level
                })
        
        return results
    
    def get_system_statistics(self) -> Dict[str, Any]:
        """Get comprehensive system statistics"""
        
        stats = {
            "total_files": len(self.file_representations),
            "file_types": {},
            "water_states": {},
            "categories": {},
            "size_distribution": {
                "small": 0,      # < 1KB
                "medium": 0,     # 1KB - 100KB
                "large": 0,      # 100KB - 1MB
                "very_large": 0  # > 1MB
            },
            "meta_circular_count": 0,
            "self_contained_count": 0
        }
        
        for file_id, file_rep in self.file_representations.items():
            # File type distribution
            file_type = file_rep.file_type
            stats["file_types"][file_type] = stats["file_types"].get(file_type, 0) + 1
            
            # Water state distribution
            water_state = file_rep.water_state
            stats["water_states"][water_state] = stats["water_states"].get(water_state, 0) + 1
            
            # Category distribution
            category = file_rep.structure_info.get("file_category", "unknown")
            stats["categories"][category] = stats["categories"].get(category, 0) + 1
            
            # Size distribution
            size_kb = file_rep.file_size / 1024
            if size_kb < 1:
                stats["size_distribution"]["small"] += 1
            elif size_kb < 100:
                stats["size_distribution"]["medium"] += 1
            elif size_kb < 1024:
                stats["size_distribution"]["large"] += 1
            else:
                stats["size_distribution"]["very_large"] += 1
            
            # Meta-circular and self-contained counts
            if file_rep.metadata.get("meta_circular", False):
                stats["meta_circular_count"] += 1
            if file_rep.metadata.get("self_contained", False):
                stats["self_contained_count"] += 1
        
        return stats
    
    def demonstrate_query_capabilities(self):
        """Demonstrate all query capabilities"""
        
        print("🌟 Living Codex Self-Representation Query Demo")
        print("=" * 70)
        
        # 1. System Statistics
        print("\n📊 1. System Statistics")
        print("-" * 40)
        stats = self.get_system_statistics()
        
        print(f"   📁 Total Files: {stats['total_files']}")
        print(f"   🔮 Meta-Circular Files: {stats['meta_circular_count']}")
        print(f"   🎯 Self-Contained Files: {stats['self_contained_count']}")
        
        print("\n   📁 File Type Distribution:")
        for file_type, count in stats["file_types"].items():
            print(f"      • {file_type}: {count}")
        
        print("\n   🌊 Water State Distribution:")
        for water_state, count in stats["water_states"].items():
            print(f"      • {water_state}: {count}")
        
        print("\n   📏 Size Distribution:")
        for size_cat, count in stats["size_distribution"].items():
            print(f"      • {size_cat}: {count}")
        
        # 2. Query by File Type
        print("\n🔍 2. Query by File Type (Python files)")
        print("-" * 40)
        python_files = self.query_files_by_type("py")
        print(f"   Found {len(python_files)} Python files:")
        for file_info in python_files[:5]:  # Show first 5
            print(f"      • {file_info['file_name']} ({file_info['file_path']}) - {file_info['water_state']}")
        if len(python_files) > 5:
            print(f"      ... and {len(python_files) - 5} more")
        
        # 3. Query by Water State
        print("\n🌊 3. Query by Water State (Liquid files)")
        print("-" * 40)
        liquid_files = self.query_files_by_water_state("liquid")
        print(f"   Found {len(liquid_files)} Liquid state files:")
        for file_info in liquid_files[:5]:  # Show first 5
            print(f"      • {file_info['file_name']} ({file_info['file_type']}) - {file_info['representation']}")
        if len(liquid_files) > 5:
            print(f"      ... and {len(liquid_files) - 5} more")
        
        # 4. Query by Content
        print("\n🔍 4. Query by Content (search for 'ontology')")
        print("-" * 40)
        ontology_files = self.query_files_by_content("ontology")
        print(f"   Found {len(ontology_files)} files containing 'ontology':")
        for file_info in ontology_files[:3]:  # Show first 3
            print(f"      • {file_info['file_name']} - {file_info['match_count']} matches")
            print(f"        Preview: {file_info['content_preview'][:100]}...")
        if len(ontology_files) > 3:
            print(f"      ... and {len(ontology_files) - 3} more")
        
        # 5. Query Meta-Circular Files
        print("\n🔮 5. Query Meta-Circular Files")
        print("-" * 40)
        meta_circular_files = self.query_meta_circular_files()
        print(f"   Found {len(meta_circular_files)} meta-circular files:")
        for file_info in meta_circular_files:
            print(f"      • {file_info['file_name']} ({file_info['file_path']}) - {file_info['water_state']}")
        
        # 6. Query by Category
        print("\n📚 6. Query by Category (markdown_documentation)")
        print("-" * 40)
        markdown_files = self.query_files_by_category("markdown_documentation")
        print(f"   Found {len(markdown_files)} markdown documentation files:")
        for file_info in markdown_files[:5]:  # Show first 5
            print(f"      • {file_info['file_name']} - {file_info['energy_level']} Hz")
        if len(markdown_files) > 5:
            print(f"      ... and {len(markdown_files) - 5} more")
        
        # 7. Query by Size Range
        print("\n📏 7. Query by Size Range (1KB - 100KB)")
        print("-" * 40)
        medium_files = self.query_files_by_size_range(1024, 102400)
        print(f"   Found {len(medium_files)} medium-sized files:")
        for file_info in medium_files[:5]:  # Show first 5
            size_kb = file_info['file_size'] / 1024
            print(f"      • {file_info['file_name']} - {size_kb:.1f} KB - {file_info['water_state']}")
        if len(medium_files) > 5:
            print(f"      ... and {len(medium_files) - 5} more")
        
        print("\n" + "=" * 70)
        print("🎉 Self-Representation Query Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Complete file system understanding and querying")
        print("   • Water state-based file categorization")
        print("   • Content-based search and analysis")
        print("   • Meta-circular file identification")
        print("   • Comprehensive system statistics")
        print("\n🚀 The Living Codex can now fully understand and query itself!")

def main():
    """Main function to demonstrate self-representation query capabilities"""
    
    print("🌟 Living Codex Self-Representation Query Demo")
    print("=" * 70)
    
    try:
        # Create and demonstrate query capabilities
        query_demo = SelfRepresentationQueryDemo()
        query_demo.demonstrate_query_capabilities()
        
        print("\n" + "=" * 70)
        print("🎉 Self-Representation Query Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Complete file system understanding and querying")
        print("   • Water state-based file categorization")
        print("   • Content-based search and analysis")
        print("   • Meta-circular file identification")
        print("   • Comprehensive system statistics")
        print("\n🚀 The Living Codex can now fully understand and query itself!")
        
    except Exception as e:
        print(f"❌ Error running self-representation query demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
