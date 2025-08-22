#!/usr/bin/env python3
"""
Markdown Language Ontology Integration
Explores how Markdown as a markup language can be described using our Codex representation,
enabling the Codex system to host its own specifications in a structured, self-referential way.
"""

import json
from typing import List, Dict, Any, Optional
from enhanced_fractal_api import EnhancedFractalAPI, NodeCreate, NodeUpdate

class MarkdownLanguageOntology:
    """Integrates Markdown markup language concepts into our fractal ontological framework"""
    
    def __init__(self, api: EnhancedFractalAPI):
        self.api = api
        self._bootstrap_markdown_ontology()
    
    def _bootstrap_markdown_ontology(self):
        """Bootstrap the Markdown language ontology into the fractal system"""
        
        print("🔧 Bootstrapping Markdown Language Ontology...")
        
        # Create the Markdown language ontology root
        markdown_ontology = self.api._create_generic_node(
            node_id="markdown_language_ontology",
            node_type="markdown_language_ontology",
            name="Markdown Markup Language Ontology",
            content="Complete ontological framework for understanding Markdown as a markup language, enabling self-referential documentation within the Codex system",
            parent_id="programming_language_ontology",
            children=[],
            metadata={
                "language_type": "markdown",
                "frequency": 741.0,
                "chakra": "throat",
                "water_state": "structured_hexagonal",
                "abstraction_level": "meta_implementation",
                "version": "CommonMark",
                "paradigm": ["markup", "documentation", "structured_text", "self_referential"]
            },
            structure_info={
                "fractal_depth": 4,
                "language_type": "markdown_integration",
                "parent_ontology": "programming_language_ontology"
            }
        )
        
        # Add to programming ontology's children
        self.api._add_child_to_parent("programming_language_ontology", "markdown_language_ontology")
        
        # Create the three core ontological layers for Markdown
        self._create_markdown_syntax_ontology()      # Ice - Markup Blueprint
        self._create_markdown_semantics_ontology()   # Water - Document Flow
        self._create_markdown_implementation_ontology() # Vapor - Actual Documents
        
        # Create Markdown document examples
        self._create_markdown_document_examples()
        
        print("✅ Markdown Language Ontology bootstrapped successfully!")
    
    def _create_markdown_syntax_ontology(self):
        """Create the Markdown syntax ontology (Ice - Markup Blueprint)"""
        
        print("   🔧 Creating Markdown Syntax Ontology (Ice - Markup Blueprint)...")
        
        # Create the ice layer for Markdown syntax
        syntax_layer = self.api._create_generic_node(
            node_id="markdown_syntax_ice_layer",
            node_type="markdown_syntax_ice",
            name="Markdown Syntax Ice Layer — Markup Blueprint",
            content="The frozen, structured layer that defines Markdown's syntax rules, markup patterns, and document structure - the blueprint for all Markdown documents",
            parent_id="markdown_language_ontology",
            children=[],
            metadata={
                "water_state": "ice",
                "frequency": 963.0,
                "chakra": "crown",
                "representation": "blueprint",
                "state": "frozen",
                "purpose": "markup_definition",
                "syntax_type": "markdown_specification"
            },
            structure_info={
                "fractal_depth": 5,
                "layer_type": "ice_markup_blueprint",
                "parent_ontology": "markdown_language_ontology"
            }
        )
        
        # Add to Markdown ontology's children
        self.api._add_child_to_parent("markdown_language_ontology", "markdown_syntax_ice_layer")
        
        # Create syntax components
        syntax_components = {
            "block_elements": {
                "name": "Block Elements",
                "content": "Markdown block-level elements that create document structure",
                "metadata": {
                    "component_type": "block_definition",
                    "water_state": "ice",
                    "frequency": 963.0,
                    "chakra": "crown",
                    "representation": "blueprint",
                    "examples": ["headings", "paragraphs", "lists", "blockquotes", "code_blocks", "horizontal_rules"]
                }
            },
            "inline_elements": {
                "name": "Inline Elements",
                "content": "Markdown inline elements that format text within blocks",
                "metadata": {
                    "component_type": "inline_definition",
                    "water_state": "ice",
                    "frequency": 852.0,
                    "chakra": "third_eye",
                    "representation": "blueprint",
                    "examples": ["emphasis", "strong", "code", "links", "images", "strikethrough"]
                }
            },
            "syntax_patterns": {
                "name": "Syntax Patterns",
                "content": "Regular expression patterns and parsing rules for Markdown",
                "metadata": {
                    "component_type": "pattern_definition",
                    "water_state": "ice",
                    "frequency": 741.0,
                    "chakra": "throat",
                    "representation": "blueprint",
                    "examples": ["heading_patterns", "list_patterns", "link_patterns", "emphasis_patterns"]
                }
            },
            "document_structure": {
                "name": "Document Structure",
                "content": "Rules for organizing Markdown documents and sections",
                "metadata": {
                    "component_type": "structure_definition",
                    "water_state": "ice",
                    "frequency": 639.0,
                    "chakra": "heart",
                    "representation": "blueprint",
                    "examples": ["front_matter", "toc", "sections", "hierarchical_organization"]
                }
            }
        }
        
        for comp_id, comp_data in syntax_components.items():
            component_node = self.api._create_generic_node(
                node_id=f"syntax_comp_{comp_id}",
                node_type="syntax_component",
                name=comp_data["name"],
                content=comp_data["content"],
                parent_id="markdown_syntax_ice_layer",
                children=[],
                metadata=comp_data["metadata"],
                structure_info={
                    "fractal_depth": 6,
                    "component_type": "ice_markup_blueprint",
                    "parent_layer": "markdown_syntax_ice_layer"
                }
            )
            
            # Add to syntax layer's children
            self.api._add_child_to_parent("markdown_syntax_ice_layer", f"syntax_comp_{comp_id}")
    
    def _create_markdown_semantics_ontology(self):
        """Create the Markdown semantics ontology (Water - Document Flow)"""
        
        print("   🔧 Creating Markdown Semantics Ontology (Water - Document Flow)...")
        
        # Create the water layer for Markdown semantics
        semantics_layer = self.api._create_generic_node(
            node_id="markdown_semantics_water_layer",
            node_type="markdown_semantics_water",
            name="Markdown Semantics Water Layer — Document Flow",
            content="The flowing, dynamic layer that defines how Markdown documents are parsed, rendered, and flow through different output formats",
            parent_id="markdown_language_ontology",
            children=[],
            metadata={
                "water_state": "liquid",
                "frequency": 639.0,
                "chakra": "heart",
                "representation": "recipe",
                "state": "flowing",
                "purpose": "document_flow",
                "processing_model": "parse_and_render"
            },
            structure_info={
                "fractal_depth": 5,
                "layer_type": "water_document_flow",
                "parent_ontology": "markdown_language_ontology"
            }
        )
        
        # Add to Markdown ontology's children
        self.api._add_child_to_parent("markdown_language_ontology", "markdown_semantics_water_layer")
        
        # Create semantics components
        semantics_components = {
            "parsing_model": {
                "name": "Parsing Model",
                "content": "How Markdown text is parsed into an abstract syntax tree",
                "metadata": {
                    "component_type": "parsing_definition",
                    "water_state": "liquid",
                    "frequency": 639.0,
                    "chakra": "heart",
                    "representation": "recipe",
                    "examples": ["lexical_analysis", "syntax_parsing", "ast_construction", "error_handling"]
                }
            },
            "rendering_pipeline": {
                "name": "Rendering Pipeline",
                "content": "How parsed Markdown is transformed into different output formats",
                "metadata": {
                    "component_type": "rendering_definition",
                    "water_state": "liquid",
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "representation": "recipe",
                    "examples": ["html_output", "pdf_generation", "text_processing", "format_conversion"]
                }
            },
            "document_flow": {
                "name": "Document Flow",
                "content": "How documents flow through different processing stages",
                "metadata": {
                    "component_type": "flow_definition",
                    "water_state": "liquid",
                    "frequency": 417.0,
                    "chakra": "sacral",
                    "representation": "recipe",
                    "examples": ["preprocessing", "transformation", "post_processing", "validation"]
                }
            },
            "metadata_processing": {
                "name": "Metadata Processing",
                "content": "How document metadata is extracted and processed",
                "metadata": {
                    "component_type": "metadata_definition",
                    "water_state": "liquid",
                    "frequency": 396.0,
                    "chakra": "root",
                    "representation": "recipe",
                    "examples": ["front_matter", "yaml_metadata", "json_metadata", "custom_fields"]
                }
            }
        }
        
        for comp_id, comp_data in semantics_components.items():
            component_node = self.api._create_generic_node(
                node_id=f"semantics_comp_{comp_id}",
                node_type="semantics_component",
                name=comp_data["name"],
                content=comp_data["content"],
                parent_id="markdown_semantics_water_layer",
                children=[],
                metadata=comp_data["metadata"],
                structure_info={
                    "fractal_depth": 6,
                    "component_type": "water_document_flow",
                    "parent_layer": "markdown_semantics_water_layer"
                }
            )
            
            # Add to semantics layer's children
            self.api._add_child_to_parent("markdown_semantics_water_layer", f"semantics_comp_{comp_id}")
    
    def _create_markdown_implementation_ontology(self):
        """Create the Markdown implementation ontology (Vapor - Actual Documents)"""
        
        print("   🔧 Creating Markdown Implementation Ontology (Vapor - Actual Documents)...")
        
        # Create the vapor layer for Markdown implementation
        implementation_layer = self.api._create_generic_node(
            node_id="markdown_implementation_vapor_layer",
            node_type="markdown_implementation_vapor",
            name="Markdown Implementation Vapor Layer — Actual Documents",
            content="The living, dynamic layer that represents actual Markdown documents, rendered output, and runtime representations",
            parent_id="markdown_language_ontology",
            children=[],
            metadata={
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "state": "living",
                "purpose": "document_implementation",
                "implementation_type": "live_documents"
            },
            structure_info={
                "fractal_depth": 5,
                "layer_type": "vapor_document_implementation",
                "parent_ontology": "markdown_language_ontology"
            }
        )
        
        # Add to Markdown ontology's children
        self.api._add_child_to_parent("markdown_language_ontology", "markdown_implementation_vapor_layer")
        
        # Create implementation components
        implementation_components = {
            "source_documents": {
                "name": "Source Documents",
                "content": "Actual Markdown source files and content",
                "metadata": {
                    "component_type": "document_implementation",
                    "water_state": "vapor",
                    "frequency": 852.0,
                    "chakra": "third_eye",
                    "representation": "cells",
                    "examples": ["markdown_files", "document_content", "source_text", "raw_markdown"]
                }
            },
            "rendered_output": {
                "name": "Rendered Output",
                "content": "Processed and rendered document output",
                "metadata": {
                    "component_type": "output_implementation",
                    "water_state": "vapor",
                    "frequency": 741.0,
                    "chakra": "throat",
                    "representation": "cells",
                    "examples": ["html_output", "pdf_documents", "formatted_text", "web_pages"]
                }
            },
            "document_objects": {
                "name": "Document Objects",
                "content": "Parsed document representations and metadata",
                "metadata": {
                    "component_type": "object_implementation",
                    "water_state": "vapor",
                    "frequency": 639.0,
                    "chakra": "heart",
                    "representation": "cells",
                    "examples": ["parsed_ast", "document_metadata", "section_objects", "content_nodes"]
                }
            },
            "interactive_features": {
                "name": "Interactive Features",
                "content": "Dynamic and interactive document capabilities",
                "metadata": {
                    "component_type": "interactive_implementation",
                    "water_state": "vapor",
                    "frequency": 528.0,
                    "chakra": "solar_plexus",
                    "representation": "cells",
                    "examples": ["live_preview", "collapsible_sections", "search_functionality", "navigation"]
                }
            }
        }
        
        for comp_id, comp_data in implementation_components.items():
            component_node = self.api._create_generic_node(
                node_id=f"implementation_comp_{comp_data['name'].lower().replace(' ', '_')}",
                node_type="implementation_component",
                name=comp_data["name"],
                content=comp_data["content"],
                parent_id="markdown_implementation_vapor_layer",
                children=[],
                metadata=comp_data["metadata"],
                structure_info={
                    "fractal_depth": 6,
                    "component_type": "vapor_document_implementation",
                    "parent_layer": "markdown_implementation_vapor_layer"
                }
            )
            
            # Add to implementation layer's children
            self.api._add_child_to_parent("markdown_implementation_vapor_layer", f"implementation_comp_{comp_data['name'].lower().replace(' ', '_')}")
    
    def _create_markdown_document_examples(self):
        """Create concrete examples of Markdown documents as blueprints and actual content"""
        
        print("   🔧 Creating Markdown Document Examples...")
        
        # Create the examples section
        examples_section = self.api._create_generic_node(
            node_id="markdown_document_examples",
            node_type="markdown_examples",
            name="Markdown Document Examples",
            content="Concrete examples showing how Markdown documents are described as blueprints (ice) and implemented as actual content (vapor)",
            parent_id="markdown_language_ontology",
            children=[],
            metadata={
                "example_type": "document_demonstration",
                "frequency": 741.0,
                "chakra": "throat",
                "water_state": "structured_hexagonal",
                "abstraction_level": "concrete_implementation"
            },
            structure_info={
                "fractal_depth": 5,
                "example_type": "document_demonstration",
                "parent_ontology": "markdown_language_ontology"
            }
        )
        
        # Add to Markdown ontology's children
        self.api._add_child_to_parent("markdown_language_ontology", "markdown_document_examples")
        
        # Create specific document examples
        self._create_specification_document_example(examples_section)
        self._create_api_documentation_example(examples_section)
        self._create_tutorial_document_example(examples_section)
    
    def _create_specification_document_example(self, examples_section):
        """Create a specification document example showing blueprint and implementation"""
        
        print("     🔧 Creating Specification Document Example...")
        
        # Create the specification document blueprint (Ice)
        spec_blueprint = self.api._create_generic_node(
            node_id="specification_document_blueprint",
            node_type="document_blueprint",
            name="Specification Document Blueprint (Ice)",
            content="Blueprint definition of a specification document showing structure, sections, and content organization",
            parent_id="markdown_document_examples",
            children=[],
            metadata={
                "water_state": "ice",
                "frequency": 963.0,
                "chakra": "crown",
                "representation": "blueprint",
                "document_type": "specification",
                "blueprint_elements": ["title_structure", "section_hierarchy", "content_organization", "metadata_format"]
            },
            structure_info={
                "fractal_depth": 6,
                "blueprint_type": "document_structure",
                "parent_examples": "markdown_document_examples"
            }
        )
        
        # Add to examples section's children
        self.api._add_child_to_parent("markdown_document_examples", "specification_document_blueprint")
        
        # Create the specification document implementation (Vapor)
        spec_implementation = self.api._create_generic_node(
            node_id="specification_document_implementation",
            node_type="document_implementation",
            name="Specification Document Implementation (Vapor)",
            content="Actual Markdown content implementation of the specification document",
            parent_id="markdown_document_examples",
            children=[],
            metadata={
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "document_type": "specification",
                "implementation_language": "markdown",
                "content_lines": 35
            },
            structure_info={
                "fractal_depth": 6,
                "implementation_type": "actual_document",
                "parent_examples": "markdown_document_examples"
            }
        )
        
        # Add to examples section's children
        self.api._add_child_to_parent("markdown_document_examples", "specification_document_implementation")
        
        # Create the actual Markdown content
        spec_content = self.api._create_generic_node(
            node_id="specification_document_content",
            node_type="document_content",
            name="Specification Document Markdown Content",
            content='''# Living Codex System Specification

## Overview

The Living Codex System is a fractal, self-referential knowledge system that represents all information as interconnected nodes in a unified ontological framework.

## Core Principles

### 1. Fractal Nature
- **Self-similarity**: Every level of the system exhibits similar patterns
- **Recursive structure**: Components are defined in terms of themselves
- **Infinite depth**: Exploration can continue to any level of detail

### 2. Water State Ontology
- **Ice (Blueprint)**: Frozen, structured definitions and blueprints
- **Water (Recipe)**: Flowing, dynamic processes and transformations
- **Vapor (Cells)**: Living, evolving instances and implementations

### 3. Meta-Circular Design
- **Self-description**: The system describes its own structure
- **Self-evolution**: The system can modify and improve itself
- **Self-reference**: All concepts are represented within the system

## Architecture

### Node Structure
Each node in the system contains:
- **Node ID**: Unique identifier
- **Node Type**: Classification of the node
- **Content**: Actual information content
- **Metadata**: Properties and attributes
- **Structure Info**: Fractal and ontological information

### Fractal Layers
1. **Meta-Implementation Layer**: Highest level of abstraction
2. **System Architecture Layer**: Core system design
3. **Implementation Layer**: Concrete implementations
4. **Content Layer**: Actual knowledge and data

## Implementation

### Technology Stack
- **Backend**: Python with FastAPI
- **Database**: SQLite for persistence
- **API**: RESTful interface for all operations
- **Frontend**: Interactive web interface (planned)

### Key Features
- **Universal Node System**: Everything is represented as nodes
- **Dynamic Evolution**: System grows through curiosity and exploration
- **Graph Integration**: Seamless integration with graph databases
- **Living Documents**: All documentation is explorable and evolvable

## Future Evolution

The Living Codex System is designed to evolve continuously through:
- **Curiosity-driven exploration**
- **AI-assisted knowledge discovery**
- **Community-driven development**
- **Autonomous system improvement**

---

*This specification is itself a living document within the Living Codex System.*''',
            parent_id="specification_document_implementation",
            children=[],
            metadata={
                "content_type": "markdown_source",
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "file_extension": ".md",
                "syntax_highlighting": "markdown"
            },
            structure_info={
                "fractal_depth": 7,
                "content_type": "actual_document",
                "parent_implementation": "specification_document_implementation"
            }
        )
        
        # Add to implementation's children
        self.api._add_child_to_parent("specification_document_implementation", "specification_document_content")
    
    def _create_api_documentation_example(self, examples_section):
        """Create an API documentation example showing blueprint and implementation"""
        
        print("     🔧 Creating API Documentation Example...")
        
        # Create the API documentation blueprint (Ice)
        api_doc_blueprint = self.api._create_generic_node(
            node_id="api_documentation_blueprint",
            node_type="document_blueprint",
            name="API Documentation Blueprint (Ice)",
            content="Blueprint definition of API documentation showing endpoint structure and response formats",
            parent_id="markdown_document_examples",
            children=[],
            metadata={
                "water_state": "ice",
                "frequency": 963.0,
                "chakra": "crown",
                "representation": "blueprint",
                "document_type": "api_documentation",
                "blueprint_elements": ["endpoint_structure", "request_response_formats", "authentication_details", "example_usage"]
            },
            structure_info={
                "fractal_depth": 6,
                "blueprint_type": "document_structure",
                "parent_examples": "markdown_document_examples"
            }
        )
        
        # Add to examples section's children
        self.api._add_child_to_parent("markdown_document_examples", "api_documentation_blueprint")
        
        # Create the API documentation implementation (Vapor)
        api_doc_implementation = self.api._create_generic_node(
            node_id="api_documentation_implementation",
            node_type="document_implementation",
            name="API Documentation Implementation (Vapor)",
            content="Actual Markdown content implementation of the API documentation",
            parent_id="markdown_document_examples",
            children=[],
            metadata={
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "document_type": "api_documentation",
                "implementation_language": "markdown",
                "content_lines": 42
            },
            structure_info={
                "fractal_depth": 6,
                "implementation_type": "actual_document",
                "parent_examples": "markdown_document_examples"
            }
        )
        
        # Add to examples section's children
        self.api._add_child_to_parent("markdown_document_examples", "api_documentation_implementation")
        
        # Create the actual Markdown content
        api_doc_content = self.api._create_generic_node(
            node_id="api_documentation_content",
            node_type="document_content",
            name="API Documentation Markdown Content",
            content='''# Living Codex API Documentation

## Overview

The Living Codex API provides comprehensive access to all knowledge and meta-knowledge in the fractal node system.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API operates without authentication. All endpoints are publicly accessible.

## Core Endpoints

### Node Operations

#### Create Node
```http
POST /nodes
```

**Request Body:**
```json
{
  "node_type": "example_node",
  "name": "Example Node",
  "content": "This is an example node content",
  "parent_id": "fractal_system_root",
  "metadata": {
    "frequency": 528.0,
    "chakra": "solar_plexus",
    "water_state": "crystalline"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "node_id": "generated_node_id",
  "message": "Node created successfully"
}
```

#### Get Node
```http
GET /nodes/{node_id}
```

**Response:**
```json
{
  "node_id": "example_id",
  "node_type": "example_node",
  "name": "Example Node",
  "content": "Node content",
  "parent_id": "fractal_system_root",
  "children": [],
  "metadata": {...},
  "structure_info": {...}
}
```

### Knowledge Navigation

#### Navigate Knowledge
```http
POST /navigate
```

**Request Body:**
```json
{
  "node_id": "target_node_id",
  "depth": 3,
  "include_relationships": true
}
```

### Knowledge Querying

#### Query Knowledge
```http
POST /query
```

**Request Body:**
```json
{
  "query": "water states",
  "node_type": null,
  "max_results": 100,
  "include_metadata": true
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `400`: Bad Request
- `404`: Not Found
- `500`: Internal Server Error

## Rate Limiting

Currently, no rate limiting is implemented. Please use the API responsibly.

---

*This documentation is generated from the Living Codex System itself.*''',
            parent_id="api_documentation_implementation",
            children=[],
            metadata={
                "content_type": "markdown_source",
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "file_extension": ".md",
                "syntax_highlighting": "markdown"
            },
            structure_info={
                "fractal_depth": 7,
                "content_type": "actual_document",
                "parent_implementation": "api_documentation_implementation"
            }
        )
        
        # Add to implementation's children
        self.api._add_child_to_parent("api_documentation_implementation", "api_documentation_content")
    
    def _create_tutorial_document_example(self, examples_section):
        """Create a tutorial document example showing blueprint and implementation"""
        
        print("     🔧 Creating Tutorial Document Example...")
        
        # Create the tutorial document blueprint (Ice)
        tutorial_blueprint = self.api._create_generic_node(
            node_id="tutorial_document_blueprint",
            node_type="document_blueprint",
            name="Tutorial Document Blueprint (Ice)",
            content="Blueprint definition of a tutorial document showing learning progression and content structure",
            parent_id="markdown_document_examples",
            children=[],
            metadata={
                "water_state": "ice",
                "frequency": 963.0,
                "chakra": "crown",
                "representation": "blueprint",
                "document_type": "tutorial",
                "blueprint_elements": ["learning_objectives", "progressive_structure", "examples_and_exercises", "assessment_criteria"]
            },
            structure_info={
                "fractal_depth": 6,
                "blueprint_type": "document_structure",
                "parent_examples": "markdown_document_examples"
            }
        )
        
        # Add to examples section's children
        self.api._add_child_to_parent("markdown_document_examples", "tutorial_blueprint")
        
        # Create the tutorial document implementation (Vapor)
        tutorial_implementation = self.api._create_generic_node(
            node_id="tutorial_document_implementation",
            node_type="document_implementation",
            name="Tutorial Document Implementation (Vapor)",
            content="Actual Markdown content implementation of the tutorial document",
            parent_id="markdown_document_examples",
            children=[],
            metadata={
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "document_type": "tutorial",
                "implementation_language": "markdown",
                "content_lines": 38
            },
            structure_info={
                "fractal_depth": 6,
                "implementation_type": "actual_document",
                "parent_examples": "markdown_document_examples"
            }
        )
        
        # Add to examples section's children
        self.api._add_child_to_parent("markdown_document_examples", "tutorial_implementation")
        
        # Create the actual Markdown content
        tutorial_content = self.api._create_generic_node(
            node_id="tutorial_document_content",
            node_type="document_content",
            name="Tutorial Document Markdown Content",
            content='''# Getting Started with the Living Codex System

## Introduction

Welcome to the Living Codex System! This tutorial will guide you through the fundamental concepts and help you get started with exploring and contributing to this living knowledge system.

## Prerequisites

- Basic understanding of Python
- Familiarity with REST APIs
- Curiosity and willingness to explore

## Learning Objectives

By the end of this tutorial, you will be able to:
- Understand the core concepts of the Living Codex System
- Navigate through the fractal knowledge structure
- Create and modify nodes in the system
- Query and explore knowledge using the API
- Contribute to the system's evolution

## Core Concepts

### 1. Fractal Nature
The Living Codex System is built on the principle of **fractal self-similarity**. This means:
- Every level of the system exhibits similar patterns
- You can explore from the highest abstraction to the finest detail
- The system is infinitely deep and explorable

### 2. Water State Ontology
The system uses a unique ontological framework based on water states:
- **Ice (Blueprint)**: Frozen, structured definitions
- **Water (Recipe)**: Flowing, dynamic processes
- **Vapor (Cells)**: Living, evolving instances

### 3. Universal Node System
Everything in the system is represented as nodes:
- Knowledge concepts
- System structure
- Documentation
- Code implementations
- Even the system itself!

## Hands-On Practice

### Exercise 1: Explore the System
1. Start the Living Codex API server
2. Navigate to the system overview endpoint
3. Explore the fractal structure
4. Identify different node types

### Exercise 2: Create Your First Node
1. Use the API to create a new knowledge node
2. Add metadata and structure information
3. Link it to existing nodes
4. Query for your newly created node

### Exercise 3: Navigate Knowledge
1. Start from a high-level concept
2. Navigate deeper into the fractal structure
3. Follow relationships between nodes
4. Discover unexpected connections

## Next Steps

After completing this tutorial:
- Explore the advanced features
- Contribute new knowledge nodes
- Experiment with different node types
- Join the community discussion

## Resources

- [API Documentation](./api_documentation.md)
- [System Specification](./system_specification.md)
- [Community Forum](https://github.com/living-codex/community)

---

*This tutorial is itself a living document that evolves with the system.*''',
            parent_id="tutorial_implementation",
            children=[],
            metadata={
                "content_type": "markdown_source",
                "water_state": "vapor",
                "frequency": 852.0,
                "chakra": "third_eye",
                "representation": "cells",
                "file_extension": ".md",
                "syntax_highlighting": "markdown"
            },
            structure_info={
                "fractal_depth": 7,
                "content_type": "actual_document",
                "parent_implementation": "tutorial_implementation"
            }
        )
        
        # Add to implementation's children
        self.api._add_child_to_parent("tutorial_implementation", "tutorial_content")
    
    def demonstrate_markdown_ontology(self):
        """Demonstrate the Markdown language ontology integration"""
        
        print("\n🔍 Demonstrating Markdown Language Ontology")
        print("=" * 60)
        
        # Show the three ontological layers for Markdown
        print("   🌊 Three Ontological Layers for Markdown:")
        print("      • Ice Layer (Syntax) - Markup Blueprint, Syntax Rules")
        print("      • Water Layer (Semantics) - Document Flow, Processing")
        print("      • Vapor Layer (Implementation) - Actual Documents, Content")
        
        # Show the document examples
        print("\n   📚 Markdown Document Examples:")
        print("      • Specification Document - System specification and overview")
        print("      • API Documentation - API endpoints and usage")
        print("      • Tutorial Document - Learning guide and exercises")
        
        # Show the ontological mapping
        print("\n   🔗 Ontological Mapping:")
        print("      • Syntax (Ice) → Blueprint for all Markdown documents")
        print("      • Semantics (Water) → Recipe for document processing")
        print("      • Implementation (Vapor) → Living document instances")
        
        print("\n   ✅ Markdown Language Ontology demonstration complete!")
    
    def explore_self_referential_capabilities(self):
        """Explore how Markdown enables self-referential documentation within the Codex system"""
        
        print("\n🔍 Exploring Self-Referential Capabilities")
        print("=" * 60)
        
        self_referential_features = {
            "Documentation within Documentation": {
                "description": "Markdown documents can reference and describe other documents",
                "example": "API docs reference system specs, tutorials reference both",
                "benefit": "Complete documentation coverage"
            },
            "System Self-Description": {
                "description": "The Codex system can document its own structure",
                "example": "System specification documents the system itself",
                "benefit": "Full self-awareness and understanding"
            },
            "Living Documentation": {
                "description": "Documents can evolve and update as the system changes",
                "example": "API docs update when new endpoints are added",
                "benefit": "Always current and accurate"
            },
            "Fractal Documentation": {
                "description": "Documentation can be explored at multiple levels",
                "example": "From high-level overview to detailed implementation",
                "benefit": "Adaptable to different user needs"
            }
        }
        
        for feature, details in self_referential_features.items():
            print(f"\n   🔍 {feature}:")
            print(f"      📝 {details['description']}")
            print(f"      💡 Example: {details['example']}")
            print(f"      ✅ Benefit: {details['benefit']}")
    
    def demonstrate_document_evolution(self):
        """Demonstrate how Markdown documents evolve from blueprint to implementation"""
        
        print("\n🚀 Demonstrating Document Evolution")
        print("=" * 60)
        
        evolution_stages = [
            {
                "stage": "Syntax Definition (Ice)",
                "description": "Markdown syntax rules define the blueprint for all valid documents",
                "example": "Heading patterns, list structures, link formats",
                "water_state": "ice",
                "representation": "blueprint"
            },
            {
                "stage": "Semantic Specification (Water)",
                "description": "Document semantics define how content flows and is processed",
                "example": "Parsing rules, rendering pipelines, metadata processing",
                "water_state": "liquid",
                "representation": "recipe"
            },
            {
                "stage": "Document Blueprint (Ice)",
                "description": "Specific document structure and content organization",
                "example": "Section hierarchy, content outline, metadata requirements",
                "water_state": "ice",
                "representation": "blueprint"
            },
            {
                "stage": "Content Implementation (Vapor)",
                "description": "Actual Markdown content that implements the document",
                "example": "Source text, rendered output, interactive features",
                "water_state": "vapor",
                "representation": "cells"
            }
        ]
        
        for i, stage in enumerate(evolution_stages):
            print(f"\n   {i+1}. {stage['stage']} ({stage['water_state'].upper()})")
            print(f"      📝 {stage['description']}")
            print(f"      💡 Example: {stage['example']}")
            print(f"      🧬 Representation: {stage['representation']}")

def main():
    """Main function to demonstrate Markdown language ontology"""
    
    print("🌟 Markdown Language Ontology Integration")
    print("=" * 60)
    
    try:
        # Initialize the enhanced API
        api = EnhancedFractalAPI("fractal_system.db")
        
        # Create and demonstrate Markdown language ontology
        markdown_ontology = MarkdownLanguageOntology(api)
        markdown_ontology.demonstrate_markdown_ontology()
        markdown_ontology.explore_self_referential_capabilities()
        markdown_ontology.demonstrate_document_evolution()
        
        print("\n" + "=" * 60)
        print("🎉 Markdown Language Ontology Demo Completed!")
        print("\n🌟 What We've Demonstrated:")
        print("   • Three ontological layers: Syntax (Ice), Semantics (Water), Implementation (Vapor)")
        print("   • Markdown syntax structure and document features")
        print("   • Document examples: Specification, API Docs, Tutorial")
        print("   • Complete evolution from blueprint to implementation")
        print("   • Self-referential capabilities within the Codex system")
        print("\n🚀 Markdown is now fully integrated, enabling self-documentation!")
        
    except Exception as e:
        print(f"❌ Error running Markdown language ontology demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
