# Tree-sitter Code Parser Integration

The Living Codex now includes a generic Tree-sitter-based code parser that can analyze any programming language file and provide a powerful query API for navigating syntax nodes.

## 🚀 Features

### **Generic Language Support**
- **Python**: Functions, classes, methods, imports, etc.
- **JavaScript/TypeScript**: Functions, classes, arrow functions, JSX
- **HTML**: Elements, attributes, tags, structure
- **CSS**: Selectors, properties, rules
- **JSON**: Objects, arrays, key-value pairs
- **YAML**: Documents, mappings, sequences
- **SQL**: Queries, statements, clauses
- **Bash/Shell**: Commands, functions, variables
- **Lua**: Functions, tables, statements
- **And many more...**

### **Core Capabilities**
- **Automatic Language Detection**: Based on file extension and MIME type
- **Syntax Tree Generation**: Full parse tree with node relationships
- **Query API**: Run Tree-sitter queries to find specific patterns
- **CLI Integration**: Built into the Living Codex CLI
- **Graceful Fallbacks**: Works even when Tree-sitter isn't available

## 📦 Installation

### **Required Dependencies**
```bash
pip install tree_sitter>=0.21.0
pip install tree_sitter_languages>=1.10.2
```

### **Optional Dependencies**
The parser gracefully handles missing Tree-sitter libraries and shows helpful error messages.

## 🛠️ Usage

### **1. Basic Parsing**

```python
from src.core.code_parser import CodeParser

# Initialize parser
parser = CodeParser()

# Parse a file
with open('example.py', 'r') as f:
    code = f.read()

# Get syntax tree
tree = parser.to_syntax_tree(code, file_path='example.py')
print(f"Root: {tree.type}")
print(f"Children: {len(tree.children)}")
```

### **2. Running Queries**

```python
# Find all function definitions
query = "(function_definition name: (identifier) @name)"
results = parser.query(code, query, file_path='example.py')

for match in results:
    for capture in match['captures']:
        if capture['name'] == 'name':
            print(f"Function: {capture['text']}")
            print(f"Position: {capture['start_point']} -> {capture['end_point']}")
```

### **3. CLI Commands**

The parser is integrated into the Living Codex CLI:

```bash
# Start CLI
python codex_cli.py

# Parse a file
code-parse example.py

# Run a query
code-query example.py "(function_definition name: (identifier) @name)"
```

## 🔍 Query Examples

### **Python Queries**

```bash
# Find all functions
code-query file.py "(function_definition name: (identifier) @name)"

# Find all classes
code-query file.py "(class_definition name: (identifier) @name)"

# Find function calls
code-query file.py "(call function: (identifier) @func)"

# Find imports
code-query file.py "(import_statement name: (dotted_name) @module)"

# Find string literals
code-query file.py "(string) @string"
```

### **JavaScript Queries**

```bash
# Find function declarations
code-query file.js "(function_declaration name: (identifier) @name)"

# Find arrow functions
code-query file.js "(arrow_function) @arrow_func"

# Find class declarations
code-query file.js "(class_declaration name: (identifier) @name)"

# Find variable declarations
code-query file.js "(variable_declarator name: (identifier) @var)"
```

### **HTML Queries**

```bash
# Find all elements
code-query file.html "(element (tag_name) @tag)"

# Find headings
code-query file.html "(element (tag_name) @tag (text) @text)"

# Find links
code-query file.html "(element (tag_name) @tag (attribute (attribute_name) @attr))"
```

## 🏗️ Architecture

### **Core Components**

1. **`CodeParser`**: Main parser class with language detection
2. **`SyntaxNode`**: Lightweight representation of parse tree nodes
3. **`AssetTypeDetector`**: Automatic language detection from file extensions
4. **CLI Integration**: Commands for parsing and querying

### **Language Detection**

The parser automatically detects languages using:
1. **File Extension**: `.py` → Python, `.js` → JavaScript, etc.
2. **MIME Type**: `text/x-python` → Python, `text/javascript` → JavaScript
3. **Fallback**: Unknown extensions default to markdown for structure

### **Error Handling**

- **Missing Dependencies**: Clear error messages with installation instructions
- **Parse Errors**: Graceful fallbacks and detailed error reporting
- **File Issues**: Comprehensive validation and helpful error messages

## 📊 Performance

### **Optimizations**
- **Lazy Loading**: Language grammars loaded only when needed
- **Memory Efficient**: Streaming file operations for large files
- **Caching**: Tree-sitter parsers reused across operations

### **Scalability**
- **Large Files**: Handles files up to several MB efficiently
- **Multiple Languages**: Supports parsing mixed-language projects
- **Batch Operations**: Can process multiple files in sequence

## 🔧 Advanced Usage

### **Custom Language Hints**

```python
# Force specific language parsing
tree = parser.to_syntax_tree(code, file_path='file.txt', language_hint='python')
```

### **Complex Queries**

```bash
# Find functions with type hints
code-query file.py "(function_definition parameters: (parameters parameter_list: (typed_parameter name: (identifier) @name type: (type) @type)))"

# Find nested function calls
code-query file.py "(call function: (identifier) @func arguments: (argument_list (call) @nested_call))"
```

### **Query Captures**

Tree-sitter queries use captures to extract specific information:

```bash
# Capture multiple parts of a function
code-query file.py "(function_definition name: (identifier) @name parameters: (parameters) @params body: (block) @body)"
```

## 🧪 Testing

### **Demo Script**

Run the comprehensive demo:

```bash
python demo_tree_sitter.py
```

This creates sample files and demonstrates:
- Basic parsing capabilities
- Query functionality
- CLI integration
- Error handling

### **Sample Files**

The demo creates:
- `sample.py`: Python file with functions and classes
- `sample.js`: JavaScript file with functions and classes
- `sample.html`: HTML file with structure and elements

## 🚨 Troubleshooting

### **Common Issues**

1. **"Tree-sitter not available"**
   ```bash
   pip install tree_sitter tree_sitter_languages
   ```

2. **"Language not supported"**
   - Check file extension
   - Use `language_hint` parameter
   - Verify Tree-sitter language support

3. **"Parse error"**
   - Check file encoding (UTF-8 recommended)
   - Verify file syntax is valid
   - Try with different language hint

### **Debug Mode**

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🔮 Future Enhancements

### **Planned Features**
- **Language Server Protocol**: Integration with LSP for IDE support
- **Semantic Analysis**: Go beyond syntax to understand meaning
- **Code Generation**: Generate code from parsed structures
- **Refactoring Tools**: Automated code transformation
- **Dependency Analysis**: Parse import/require statements

### **Language Support**
- **Rust**: Full Rust language support
- **Go**: Go language parsing
- **C#**: C# language support
- **PHP**: PHP 8+ support
- **Ruby**: Modern Ruby syntax

## 📚 Resources

### **Tree-sitter Documentation**
- [Tree-sitter Official Docs](https://tree-sitter.github.io/tree-sitter/)
- [Query Syntax Reference](https://tree-sitter.github.io/tree-sitter/using-parsers#query-syntax)
- [Language Grammar Examples](https://github.com/tree-sitter/tree-sitter)

### **Query Examples**
- [Tree-sitter Queries](https://github.com/tree-sitter/tree-sitter/tree/master/queries)
- [Language-Specific Queries](https://github.com/tree-sitter/tree-sitter/tree/master/queries)

### **Community**
- [Tree-sitter GitHub](https://github.com/tree-sitter/tree-sitter)
- [Tree-sitter Discussions](https://github.com/tree-sitter/tree-sitter/discussions)

## 🎯 Use Cases

### **Code Analysis**
- **Static Analysis**: Find patterns, anti-patterns, and issues
- **Metrics**: Count functions, classes, complexity
- **Documentation**: Generate API documentation from code

### **Refactoring**
- **Find References**: Locate all usages of functions/variables
- **Rename Operations**: Safe renaming across codebase
- **Code Migration**: Transform code between language versions

### **Learning & Education**
- **Code Examples**: Extract and analyze code patterns
- **Syntax Learning**: Understand language constructs
- **Best Practices**: Identify coding standards and patterns

---

**The Tree-sitter integration transforms the Living Codex into a powerful code analysis platform, capable of understanding and navigating any programming language with precision and efficiency.** 🚀
