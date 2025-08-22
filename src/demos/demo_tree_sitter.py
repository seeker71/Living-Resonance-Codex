#!/usr/bin/env python3
"""
Tree-sitter Code Parser Demo
Showcases the generic programming language parser and query API
"""

import os
import sys
from pathlib import Path

def create_sample_files():
    """Create sample code files for demonstration"""
    samples_dir = Path("tree_sitter_samples")
    samples_dir.mkdir(exist_ok=True)
    
    # Python sample
    python_file = samples_dir / "sample.py"
    with open(python_file, 'w') as f:
        f.write('''#!/usr/bin/env python3
"""
Sample Python file for Tree-sitter demonstration
"""

def calculate_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number"""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

class MathOperations:
    """Simple math operations class"""
    
    def __init__(self, base_value: int):
        self.base = base_value
    
    def add(self, value: int) -> int:
        """Add a value to the base"""
        return self.base + value
    
    def multiply(self, value: int) -> int:
        """Multiply base by a value"""
        return self.base * value

if __name__ == "__main__":
    math_ops = MathOperations(10)
    result = math_ops.add(5)
    print(f"Result: {result}")
''')
    
    # JavaScript sample
    js_file = samples_dir / "sample.js"
    with open(js_file, 'w') as f:
        f.write('''// Sample JavaScript file for Tree-sitter demonstration

function greetUser(name) {
    return `Hello, ${name}!`;
}

class Calculator {
    constructor(initialValue = 0) {
        this.value = initialValue;
    }
    
    add(x) {
        this.value += x;
        return this;
    }
    
    subtract(x) {
        this.value -= x;
        return this;
    }
    
    getResult() {
        return this.value;
    }
}

const calc = new Calculator(10);
const result = calc.add(5).subtract(2).getResult();
console.log(`Result: ${result}`);
''')
    
    # HTML sample
    html_file = samples_dir / "sample.html"
    with open(html_file, 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tree-sitter Demo</title>
</head>
<body>
    <header>
        <h1>Living Codex - Tree-sitter Demo</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="home">
            <h2>Welcome</h2>
            <p>This is a sample HTML file for demonstrating Tree-sitter parsing.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Living Codex</p>
    </footer>
</body>
</html>
''')
    
    return [str(python_file), str(js_file), str(html_file)]

def demo_parsing():
    """Demonstrate basic parsing capabilities"""
    print("🧩 Tree-sitter Code Parser Demo")
    print("=" * 50)
    
    try:
        from ..core.code_parser import CodeParser
        
        # Create sample files
        print("📝 Creating sample code files...")
        sample_files = create_sample_files()
        
        for file_path in sample_files:
            print(f"   📄 {file_path}")
        
        print("\n🔍 Testing basic parsing...")
        
        # Test parsing each file
        for file_path in sample_files:
            try:
                with open(file_path, 'r', encoding='utf8') as f:
                    code = f.read()
                
                parser = CodeParser()
                tree = parser.parse(code, file_path=file_path)
                
                print(f"\n📁 {os.path.basename(file_path)}:")
                print(f"   Root type: {tree.root_node.type}")
                print(f"   Children: {len(tree.root_node.children)}")
                
                # Show first few children
                for i, child in enumerate(tree.root_node.children[:3]):
                    print(f"   Child {i+1}: {child.type} ({len(child.children)} sub-children)")
                
            except Exception as e:
                print(f"   ❌ Error parsing {file_path}: {e}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Tree-sitter not available: {e}")
        print("💡 Install with: pip install tree_sitter tree_sitter_languages")
        return False
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        return False

def demo_queries():
    """Demonstrate Tree-sitter query capabilities"""
    print("\n🔎 Testing Tree-sitter Queries")
    print("=" * 50)
    
    try:
        from ..core.code_parser import CodeParser
        
        # Test queries on Python file
        python_file = "tree_sitter_samples/sample.py"
        if not os.path.exists(python_file):
            print("❌ Python sample file not found")
            return
        
        with open(python_file, 'r', encoding='utf8') as f:
            code = f.read()
        
        parser = CodeParser()
        
        # Query 1: Find function definitions
        print("\n1️⃣ Finding function definitions:")
        query1 = "(function_definition name: (identifier) @name)"
        results1 = parser.query(code, query1, file_path=python_file)
        
        if results1:
            for i, match in enumerate(results1):
                for cap in match['captures']:
                    if cap['name'] == 'name':
                        print(f"   Function: {cap['text']}")
        else:
            print("   No functions found")
        
        # Query 2: Find class definitions
        print("\n2️⃣ Finding class definitions:")
        query2 = "(class_definition name: (identifier) @name)"
        results2 = parser.query(code, query2, file_path=python_file)
        
        if results2:
            for i, match in enumerate(results2):
                for cap in match['captures']:
                    if cap['name'] == 'name':
                        print(f"   Class: {cap['text']}")
        else:
            print("   No classes found")
        
        # Query 3: Find method definitions
        print("\n3️⃣ Finding method definitions:")
        query3 = "(function_definition name: (identifier) @name)"
        results3 = parser.query(code, query3, file_path=python_file)
        
        if results3:
            for i, match in enumerate(results3):
                for cap in match['captures']:
                    if cap['name'] == 'name':
                        print(f"   Method: {cap['text']}")
        else:
            print("   No methods found")
        
        # Test JavaScript queries
        js_file = "tree_sitter_samples/sample.js"
        if os.path.exists(js_file):
            print("\n4️⃣ Testing JavaScript queries:")
            with open(js_file, 'r', encoding='utf8') as f:
                js_code = f.read()
            
            # Find function declarations
            js_query = "(function_declaration name: (identifier) @name)"
            js_results = parser.query(js_code, js_query, file_path=js_file)
            
            if js_results:
                for match in js_results:
                    for cap in match['captures']:
                        if cap['name'] == 'name':
                            print(f"   Function: {cap['text']}")
            
            # Find class declarations
            js_class_query = "(class_declaration name: (identifier) @name)"
            js_class_results = parser.query(js_code, js_class_query, file_path=js_file)
            
            if js_class_results:
                for match in js_class_results:
                    for cap in match['captures']:
                        if cap['name'] == 'name':
                            print(f"   Class: {cap['text']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Query demo failed: {e}")
        return False

def demo_cli_integration():
    """Show how to use the CLI commands"""
    print("\n💻 CLI Integration Demo")
    print("=" * 50)
    
    print("The Tree-sitter parser is integrated into the Living Codex CLI:")
    print()
    print("📋 Available Commands:")
    print("   code-parse <file>     - Parse a source file and show structure")
    print("   code-query <file> <query> [lang] - Run Tree-sitter queries")
    print()
    print("🔍 Example Queries:")
    print("   # Find Python functions:")
    print("   code-query sample.py \"(function_definition name: (identifier) @name)\"")
    print()
    print("   # Find JavaScript classes:")
    print("   code-query sample.js \"(class_declaration name: (identifier) @name)\"")
    print()
    print("   # Find HTML headings:")
    print("   code-query sample.html \"(element (tag_name) @tag)\"")
    print()
    print("💡 To start the CLI:")
    print("   python codex_cli.py")
    print()
    print("💡 To test parsing:")
    print("   python codex_cli.py")
    print("   code-parse tree_sitter_samples/sample.py")

def cleanup():
    """Clean up demo files"""
    try:
        import shutil
        if os.path.exists("tree_sitter_samples"):
            shutil.rmtree("tree_sitter_samples")
            print("🗑️  Cleaned up demo files")
    except Exception as e:
        print(f"⚠️  Cleanup warning: {e}")

def main():
    """Main demo function"""
    print("🚀 Living Codex - Tree-sitter Code Parser Demo")
    print("=" * 70)
    
    # Run demos
    parsing_success = demo_parsing()
    
    if parsing_success:
        query_success = demo_queries()
        if query_success:
            demo_cli_integration()
    
    print("\n" + "=" * 70)
    if parsing_success:
        print("✅ Demo completed successfully!")
        print("💡 The Tree-sitter parser is now integrated into the Living Codex CLI")
        print("💡 Try: python codex_cli.py")
        print("💡 Then: code-parse <file> or code-query <file> <query>")
    else:
        print("❌ Demo failed - Tree-sitter dependencies may not be installed")
        print("💡 Install with: pip install tree_sitter tree_sitter_languages")
    
    # Ask about cleanup
    cleanup_choice = input("\n🗑️  Clean up demo files? (y/N): ").strip().lower()
    if cleanup_choice == 'y':
        cleanup()
        print("✅ Cleanup complete")
    else:
        print("📁 Demo files preserved for inspection")
        print("💡 Files are in: tree_sitter_samples/")

if __name__ == "__main__":
    main()
