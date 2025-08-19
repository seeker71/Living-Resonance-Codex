use serde::{Deserialize, Serialize};
use chrono::{DateTime, Utc};
use uuid::Uuid;
use std::collections::HashMap;

// ============================================================================
// CORE TRAITS - Universal properties like water
// ============================================================================

/// Trait for entities that can flow and adapt like water
pub trait Flowing {
    fn flow_state(&self) -> FlowState;
    fn can_adapt(&self) -> bool;
    fn resonance_level(&self) -> f64;
}

/// Trait for entities that can transform and evolve
pub trait Transformable {
    fn transform(&mut self, new_state: &str) -> Result<(), String>;
    fn evolution_stage(&self) -> EvolutionStage;
}

/// Trait for entities that can resonate and connect
pub trait Resonant {
    fn resonance_frequency(&self) -> f64;
    fn can_resonate_with(&self, other: &dyn Resonant) -> bool;
    fn resonance_strength(&self, other: &dyn Resonant) -> f64;
}

// ============================================================================
// ENUMS - States and stages like water phases
// ============================================================================

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum FlowState {
    Solid,      // Ice - structured, rigid
    Liquid,     // Water - flowing, adaptive
    Gas,        // Vapor - expansive, free
    Plasma,     // Energy - transformative, powerful
    Colloidal,  // Suspension - complex, emergent
    Crystalline, // Ordered - coherent, aligned
    Living,     // Organic - evolving, conscious
    Wave,       // Wave - oscillating, rhythmic
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum EvolutionStage {
    Potential,      // Seed state
    Emerging,       // Growing
    Mature,         // Stable
    Transforming,   // Changing
    Transcending,   // Evolving
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum ContextType {
    Scientific(ScientificContext),
    Symbolic(SymbolicContext),
    Water(WaterContext),
    Hybrid(Vec<ContextType>),
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum ScientificContext {
    Empirical,      // Observable, measurable
    Theoretical,    // Conceptual, abstract
    Experimental,   // Testable, verifiable
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum SymbolicContext {
    Archetypal,     // Universal patterns
    Cultural,       // Social meanings
    Personal,       // Individual experience
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum WaterContext {
    Phase,          // State transitions
    Flow,           // Movement patterns
    Coherence,      // Alignment patterns
}

// ============================================================================
// CORE DATA STRUCTURES - Pure data, separate from logic
// ============================================================================

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FractalNode {
    pub id: String,
    pub name: String,
    pub water_state: FlowState,
    pub archetype: Vec<String>,
    pub resonance: f64,
    pub fractal_level: u32,
    pub contexts: Vec<ContextType>,
    pub parent_id: Option<String>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
    pub metadata: HashMap<String, serde_json::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Contribution {
    pub id: String,
    pub node_id: String,
    pub user_id: String,
    pub content: String,
    pub resonance: f64,
    pub timestamp: DateTime<Utc>,
    pub fractal_context: Option<ContextType>,
    pub metadata: HashMap<String, serde_json::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct StorageStats {
    pub version: String,
    pub fractal_level: u32,
    pub total_contributions: usize,
    pub total_nodes: usize,
    pub total_subnodes: usize,
    pub total_users: usize,
    pub total_size: u64,
    pub last_updated: DateTime<Utc>,
    pub fractal_expansion: FractalExpansionStats,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FractalExpansionStats {
    pub total_fractal_dimensions: usize,
    pub contexts: Vec<ContextType>,
    pub level_breakdown: HashMap<u32, usize>,
}

// ============================================================================
// IMPLEMENTATIONS - Business logic separated from data
// ============================================================================

impl FractalNode {
    pub fn new(
        id: String,
        name: String,
        water_state: FlowState,
        archetype: Vec<String>,
        resonance: f64,
        fractal_level: u32,
        parent_id: Option<String>,
    ) -> Self {
        let now = Utc::now();
        Self {
            id,
            name,
            water_state,
            archetype,
            resonance,
            fractal_level,
            contexts: Vec::new(),
            parent_id,
            created_at: now,
            updated_at: now,
            metadata: HashMap::new(),
        }
    }

    pub fn add_context(&mut self, context: ContextType) {
        self.contexts.push(context);
        self.updated_at = Utc::now();
    }

    pub fn get_context_count(&self) -> usize {
        self.contexts.len()
    }

    pub fn has_context(&self, context_type: &ContextType) -> bool {
        self.contexts.contains(context_type)
    }

    pub fn get_contexts_by_type(&self, context_type: &str) -> Vec<&ContextType> {
        self.contexts.iter()
            .filter(|c| match c {
                ContextType::Scientific(_) => context_type == "scientific",
                ContextType::Symbolic(_) => context_type == "symbolic",
                ContextType::Water(_) => context_type == "water",
                ContextType::Hybrid(_) => context_type == "hybrid",
            })
            .collect()
    }
}

impl Contribution {
    pub fn new(
        node_id: String,
        user_id: String,
        content: String,
        resonance: f64,
        fractal_context: Option<ContextType>,
    ) -> Self {
        Self {
            id: Uuid::new_v4().to_string(),
            node_id,
            user_id,
            content,
            resonance,
            timestamp: Utc::now(),
            fractal_context,
            metadata: HashMap::new(),
        }
    }

    pub fn add_metadata(&mut self, key: String, value: serde_json::Value) {
        self.metadata.insert(key, value);
    }
}

// ============================================================================
// TRAIT IMPLEMENTATIONS - Water-like behavior
// ============================================================================

impl Flowing for FractalNode {
    fn flow_state(&self) -> FlowState {
        self.water_state.clone()
    }

    fn can_adapt(&self) -> bool {
        matches!(self.water_state, FlowState::Liquid | FlowState::Gas | FlowState::Colloidal)
    }

    fn resonance_level(&self) -> f64 {
        self.resonance
    }
}

impl Transformable for FractalNode {
    fn transform(&mut self, new_state: &str) -> Result<(), String> {
        let new_flow_state = match new_state {
            "solid" => FlowState::Solid,
            "liquid" => FlowState::Liquid,
            "gas" => FlowState::Gas,
            "plasma" => FlowState::Plasma,
            "colloidal" => FlowState::Colloidal,
            "crystalline" => FlowState::Crystalline,
            "living" => FlowState::Living,
            _ => return Err(format!("Unknown state: {}", new_state)),
        };
        
        self.water_state = new_flow_state;
        self.updated_at = Utc::now();
        Ok(())
    }

    fn evolution_stage(&self) -> EvolutionStage {
        match self.fractal_level {
            1 => EvolutionStage::Mature,
            2 => EvolutionStage::Transforming,
            _ => EvolutionStage::Transcending,
        }
    }
}

impl Resonant for FractalNode {
    fn resonance_frequency(&self) -> f64 {
        self.resonance * 100.0 // Convert to frequency range
    }

    fn can_resonate_with(&self, other: &dyn Resonant) -> bool {
        let freq_diff = (self.resonance_frequency() - other.resonance_frequency()).abs();
        freq_diff < 10.0 // Within resonance range
    }

    fn resonance_strength(&self, other: &dyn Resonant) -> f64 {
        if self.can_resonate_with(other) {
            let freq_diff = (self.resonance_frequency() - other.resonance_frequency()).abs();
            1.0 / (1.0 + freq_diff / 10.0) // Inverse relationship
        } else {
            0.0
        }
    }
}

// ============================================================================
// DEFAULT IMPLEMENTATIONS
// ============================================================================

impl Default for StorageStats {
    fn default() -> Self {
        Self {
            version: "3.0.0".to_string(),
            fractal_level: 2,
            total_contributions: 0,
            total_nodes: 0,
            total_subnodes: 0,
            total_users: 0,
            total_size: 0,
            last_updated: Utc::now(),
            fractal_expansion: FractalExpansionStats {
                total_fractal_dimensions: 3,
                contexts: vec![
                    ContextType::Scientific(ScientificContext::Empirical),
                    ContextType::Symbolic(SymbolicContext::Archetypal),
                    ContextType::Water(WaterContext::Phase),
                ],
                level_breakdown: HashMap::new(),
            },
        }
    }
}

// ============================================================================
// UTILITY FUNCTIONS - Pure functions, no side effects
// ============================================================================

pub fn create_context_combination(
    scientific: Option<ScientificContext>,
    symbolic: Option<SymbolicContext>,
    water: Option<WaterContext>,
) -> Vec<ContextType> {
    let mut contexts = Vec::new();
    
    if let Some(sci) = scientific {
        contexts.push(ContextType::Scientific(sci));
    }
    if let Some(sym) = symbolic {
        contexts.push(ContextType::Symbolic(sym));
    }
    if let Some(wat) = water {
        contexts.push(ContextType::Water(wat));
    }
    
    contexts
}

pub fn calculate_resonance_multiplier(context: &ContextType) -> f64 {
    match context {
        ContextType::Scientific(ScientificContext::Empirical) => 0.8,
        ContextType::Scientific(ScientificContext::Theoretical) => 0.85,
        ContextType::Scientific(ScientificContext::Experimental) => 0.75,
        ContextType::Symbolic(SymbolicContext::Archetypal) => 0.9,
        ContextType::Symbolic(SymbolicContext::Cultural) => 0.85,
        ContextType::Symbolic(SymbolicContext::Personal) => 0.8,
        ContextType::Water(WaterContext::Phase) => 0.8,
        ContextType::Water(WaterContext::Flow) => 0.85,
        ContextType::Water(WaterContext::Coherence) => 0.9,
        ContextType::Hybrid(_) => 0.95, // Hybrid contexts have highest resonance
    }
}

