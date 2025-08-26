#!/usr/bin/env python3
"""
Code Navigation API Demo - Living Codex
Demonstrates how code files can be navigated through the Living Codex system
"""

import os
import sys
import json
from pathlib import Path

# Add src to path for modular components
sys.path.insert(0, str(Path(__file__).parent.parent))

def create_sample_code_files():
    """Create sample code files for demonstration"""
    samples_dir = Path("code_navigation_samples")
    samples_dir.mkdir(exist_ok=True)
    
    # Python sample
    python_file = samples_dir / "sample_module.py"
    with open(python_file, 'w') as f:
        f.write('''#!/usr/bin/env python3
"""
Sample Python module for code navigation demonstration
"""

import os
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class User:
    """User data model"""
    id: int
    name: str
    email: str
    active: bool = True
    
    def to_dict(self) -> Dict[str, any]:
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'active': self.active
        }

class UserManager:
    """Manages user operations"""
    
    def __init__(self):
        self.users: List[User] = []
    
    def add_user(self, user: User) -> bool:
        """Add a new user"""
        if not self._validate_user(user):
            return False
        self.users.append(user)
        return True
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def _validate_user(self, user: User) -> bool:
        """Validate user data"""
        return (
            user.id > 0 and
            user.name and
            '@' in user.email
        )

def main():
    """Main function"""
    manager = UserManager()
    
    # Add some users
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com")
    
    manager.add_user(user1)
    manager.add_user(user2)
    
    print(f"Added {len(manager.users)} users")

if __name__ == "__main__":
    main()
''')
    
    # JavaScript sample
    js_file = samples_dir / "sample_lib.js"
    with open(js_file, 'w') as f:
        f.write('''// Sample JavaScript library for code navigation demonstration

/**
 * Utility functions for data processing
 */
class DataProcessor {
    constructor() {
        this.cache = new Map();
    }
    
    /**
     * Process array data with transformation
     */
    processArray(data, transformFn) {
        if (!Array.isArray(data)) {
            throw new Error('Input must be an array');
        }
        
        return data.map(transformFn).filter(item => item !== null);
    }
    
    /**
     * Cache results for performance
     */
    getCached(key, computeFn) {
        if (this.cache.has(key)) {
            return this.cache.get(key);
        }
        
        const result = computeFn();
        this.cache.set(key, result);
        return result;
    }
}

/**
 * Math utility functions
 */
const MathUtils = {
    /**
     * Calculate factorial
     */
    factorial(n) {
        if (n <= 1) return 1;
        return n * this.factorial(n - 1);
    },
    
    /**
     * Check if number is prime
     */
    isPrime(n) {
        if (n < 2) return false;
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) return false;
        }
        return true;
    }
};

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { DataProcessor, MathUtils };
}
''')
    
    # HTML sample
    html_file = samples_dir / "sample_app.html"
    with open(html_file, 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample App - Code Navigation Demo</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        .header { background: #f0f0f0; padding: 20px; border-radius: 5px; }
        .content { margin: 20px 0; }
        .footer { text-align: center; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>Sample Application</h1>
            <p>This is a sample HTML file for demonstrating code navigation</p>
        </header>
        
        <main class="content">
            <section id="features">
                <h2>Features</h2>
                <ul>
                    <li>Responsive design</li>
                    <li>Semantic HTML structure</li>
                    <li>Clean CSS styling</li>
                </ul>
            </section>
            
            <section id="about">
                <h2>About</h2>
                <p>This demonstrates how HTML files can be parsed and navigated.</p>
            </section>
        </main>
        
        <footer class="footer">
            <p>&copy; 2024 Living Codex - Code Navigation Demo</p>
        </footer>
    </div>
    
    <script>
        // Sample JavaScript functionality
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Sample app loaded successfully');
            
            // Add some interactivity
            const features = document.querySelectorAll('#features li');
            features.forEach(item => {
                item.addEventListener('click', function() {
                    this.style.color = this.style.color === 'blue' ? 'black' : 'blue';
                });
            });
        });
    </script>
</body>
</html>
''')
    
    return [str(python_file), str(js_file), str(html_file)]

def demo_code_navigation():
    """Demonstrate code navigation capabilities"""
    print("🧭 Code Navigation API Demo")
    print("=" * 50)
    
    try:
        # Import required modules
        from core.code_navigation_api import CodeNavigationAPI
        from core.code_parser import CodeParser
        from core.database_persistence_system import DatabasePersistenceSystem
        
        # Create sample files
        print("📝 Creating sample code files...")
        sample_files = create_sample_code_files()
        
        for file_path in sample_files:
            print(f"   📄 {file_path}")
        
        print("\n🔧 Initializing systems...")
        
        # Initialize database and code parser
        database = DatabasePersistenceSystem(db_type="sqlite", db_path="code_navigation_demo.db")
        code_parser = CodeParser()
        code_nav_api = CodeNavigationAPI(database, code_parser)
        
        print("✅ Systems initialized successfully")
        print(f"🔤 Available languages: {', '.join(code_nav_api.get_available_languages())}")
        
        print("\n📁 Adding code files to navigation system...")
        
        # Add each sample file to the navigation system
        added_files = []
        for file_path in sample_files:
            print(f"\n🔍 Adding: {os.path.basename(file_path)}")
            result = code_nav_api.parse_and_store_code_file(file_path)
            
            if result.success:
                print(f"   ✅ Successfully added")
                print(f"   Language: {result.metadata.get('language', 'unknown')}")
                print(f"   Parse time: {result.execution_time:.3f}s")
                added_files.append(result.data)
            else:
                print(f"   ❌ Failed: {getattr(result, 'error_message', 'Unknown error')}")
        
        if not added_files:
            print("\n❌ No files were added successfully")
            return False
        
        print(f"\n✅ Successfully added {len(added_files)} files to navigation system")
        
        print("\n🔍 Demonstrating code exploration...")
        
        # Explore the first added file
        first_file = added_files[0]
        file_id = f"code_file_{first_file.content_hash[:8]}"
        
        print(f"\n📁 Exploring: {first_file.file_name}")
        structure_result = code_nav_api.get_code_file_structure(file_id)
        
        if structure_result.success:
            code_file = structure_result.data
            content = code_file.content
            
            # Handle both string and dict content types
            if isinstance(content, str):
                try:
                    content_dict = json.loads(content)
                except json.JSONDecodeError:
                    content_dict = {}
            else:
                content_dict = content
            
            print(f"   Path: {content_dict.get('file_path', 'Unknown')}")
            print(f"   Language: {content_dict.get('language', 'Unknown')}")
            print(f"   Size: {content_dict.get('file_size', 0)} bytes")
            print(f"   Lines: {content_dict.get('metadata', {}).get('line_count', 0)}")
            
            if hasattr(code_file, 'syntax_nodes') and code_file.syntax_nodes:
                print(f"   Syntax nodes: {len(code_file.syntax_nodes)}")
            else:
                print("   Syntax tree: Not stored")
        else:
            print(f"   ❌ Failed to explore: {getattr(structure_result, 'error_message', 'Unknown error')}")
        
        print("\n🔍 Demonstrating code search...")
        
        # Search for specific terms
        search_terms = ["class", "function", "def"]
        for term in search_terms:
            print(f"\n   Searching for: '{term}'")
            search_result = code_nav_api.search_code_files(term)
            
            if search_result.success and search_result.data:
                print(f"   Found {len(search_result.data)} files")
                for node in search_result.data[:2]:  # Show first 2
                    content = node.content
                    # Handle both string and dict content types
                    if isinstance(content, str):
                        try:
                            content_dict = json.loads(content)
                        except json.JSONDecodeError:
                            content_dict = {}
                    else:
                        content_dict = content
                    
                    if isinstance(content_dict, dict):
                        print(f"     • {content_dict.get('file_name', 'Unknown')} ({content_dict.get('language', 'Unknown')})")
            else:
                print("   No files found")
        
        print("\n📊 Showing code navigation statistics...")
        
        stats = code_nav_api.get_code_file_stats()
        if "error" not in stats:
            print(f"   Total code files: {stats.get('total_code_files', 0)}")
            print(f"   Total syntax nodes: {stats.get('total_syntax_nodes', 0)}")
            print(f"   Available languages: {len(stats.get('available_languages', []))}")
            
            if 'language_breakdown' in stats:
                print("   Language breakdown:")
                for lang, count in stats['language_breakdown'].items():
                    print(f"     • {lang}: {count} files")
        else:
            print(f"   ❌ Error getting stats: {stats['error']}")
        
        print("\n🎯 Code Navigation Demo completed successfully!")
        print("💡 You can now use the CLI to explore these code files:")
        print("   python codex_cli.py")
        print("   code-stats")
        print("   code-search class")
        print("   code-explore <file_id>")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're running from the correct directory")
        return False
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        return False

def cleanup():
    """Clean up demo files"""
    try:
        import shutil
        if os.path.exists("code_navigation_samples"):
            shutil.rmtree("code_navigation_samples")
            print("🗑️  Cleaned up sample code files")
        
        if os.path.exists("code_navigation_demo.db"):
            os.remove("code_navigation_demo.db")
            print("🗑️  Cleaned up demo database")
            
    except Exception as e:
        print(f"⚠️  Cleanup warning: {e}")

def main():
    """Main demo function"""
    print("🚀 Living Codex - Code Navigation API Demo")
    print("=" * 70)
    
    # Run the demo
    success = demo_code_navigation()
    
    print("\n" + "=" * 70)
    if success:
        print("✅ Demo completed successfully!")
        print("💡 The code navigation API is now integrated into the Living Codex CLI")
        print("💡 Try: python codex_cli.py")
        print("💡 Then: code-stats, code-search <term>, code-explore <id>")
    else:
        print("❌ Demo failed - check the error messages above")
    
    # Ask about cleanup
    cleanup_choice = input("\n🗑️  Clean up demo files? (y/N): ").strip().lower()
    if cleanup_choice == 'y':
        cleanup()
        print("✅ Cleanup complete")
    else:
        print("📁 Demo files preserved for inspection")
        print("💡 Files are in: code_navigation_samples/")
        print("💡 Database: code_navigation_demo.db")

if __name__ == "__main__":
    main()
