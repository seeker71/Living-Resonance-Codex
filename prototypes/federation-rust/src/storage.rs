use crate::models::{
    FractalNode, Contribution, StorageStats,
    FlowState, ContextType, ScientificContext, SymbolicContext, WaterContext,
    calculate_resonance_multiplier
};
use anyhow::{Result, anyhow};
use serde_json;
use std::collections::HashMap;
use std::fs;
use std::path::Path;
use std::sync::Arc;
use tokio::sync::RwLock;
use sha2::{Sha256, Digest};
use hex;
use tracing::{info, warn, error};

// ============================================================================
// STORAGE TRAITS - Abstract interfaces like water's universal properties
// ============================================================================

/// Trait for storing and retrieving fractal nodes
pub trait NodeStorage {
    async fn store_node(&self, node: &FractalNode) -> Result<()>;
    async fn get_node(&self, node_id: &str) -> Option<FractalNode>;
    async fn get_all_nodes(&self) -> Vec<FractalNode>;
    async fn delete_node(&self, node_id: &str) -> Result<()>;
}

/// Trait for storing and retrieving contributions
pub trait ContributionStorage {
    async fn store_contribution(&self, contribution: Contribution) -> Result<serde_json::Value>;
    async fn get_contribution(&self, content_hash: &str) -> Option<Contribution>;
    async fn get_node_contributions(&self, node_id: &str) -> serde_json::Value;
    async fn get_user_contributions(&self, user_id: &str) -> serde_json::Value;
}

/// Trait for managing fractal expansions and contexts
pub trait FractalExpansionStorage {
    async fn expand_node_fractally(&self, base_node: &mut FractalNode) -> Result<()>;
    async fn get_fractal_expansion(&self, node_id: &str) -> Result<serde_json::Value>;
    async fn get_context_nodes(&self, context: &ContextType) -> Vec<FractalNode>;
}

/// Trait for storage statistics and metadata
pub trait StorageMetadata {
    async fn get_storage_stats(&self) -> StorageStats;
    async fn update_stats(&self) -> Result<()>;
    async fn get_storage_size(&self) -> u64;
}

// ============================================================================
// CONFIGURATION - Flexible settings like water adapting to containers
// ============================================================================

#[derive(Debug, Clone)]
pub struct StorageConfig {
    pub base_path: String,
    pub max_nodes: usize,
    pub max_contributions: usize,
    pub enable_persistence: bool,
    pub fractal_levels: Vec<u32>,
    pub supported_contexts: Vec<ContextType>,
    pub resonance_threshold: f64,
}

impl Default for StorageConfig {
    fn default() -> Self {
        Self {
            base_path: "./rust-fractal-storage".to_string(),
            max_nodes: 1000,
            max_contributions: 10000,
            enable_persistence: true,
            fractal_levels: vec![1, 2],
            supported_contexts: vec![
                ContextType::Scientific(ScientificContext::Empirical),
                ContextType::Scientific(ScientificContext::Theoretical),
                ContextType::Scientific(ScientificContext::Experimental),
                ContextType::Symbolic(SymbolicContext::Archetypal),
                ContextType::Symbolic(SymbolicContext::Cultural),
                ContextType::Symbolic(SymbolicContext::Personal),
                ContextType::Water(WaterContext::Phase),
                ContextType::Water(WaterContext::Flow),
                ContextType::Water(WaterContext::Coherence),
            ],
            resonance_threshold: 0.5,
        }
    }
}

// ============================================================================
// MAIN STORAGE STRUCTURE - Orchestrates all storage operations
// ============================================================================

pub struct FractalStorage {
    config: StorageConfig,
    nodes: Arc<RwLock<HashMap<String, FractalNode>>>,
    contributions: Arc<RwLock<HashMap<String, Contribution>>>,
    stats: Arc<RwLock<StorageStats>>,
    node_contexts: Arc<RwLock<HashMap<ContextType, Vec<String>>>>, // Context -> Node IDs
}

impl FractalStorage {
    pub async fn new(storage_path: &str) -> Result<Self> {
        info!("Creating new FractalStorage with path: {}", storage_path);
        
        let config = StorageConfig {
            base_path: storage_path.to_string(),
            ..Default::default()
        };
        
        info!("Storage config created");
        
        let storage = Self {
            config,
            nodes: Arc::new(RwLock::new(HashMap::new())),
            contributions: Arc::new(RwLock::new(HashMap::new())),
            stats: Arc::new(RwLock::new(StorageStats::default())),
            node_contexts: Arc::new(RwLock::new(HashMap::new())),
        };
        
        info!("Storage structure created, ensuring directories exist...");
        storage.ensure_storage_exists()?;
        
        info!("Directories ready, initializing fractal nodes...");
        storage.initialize_fractal_nodes().await?;
        
        info!("Fractal nodes initialized successfully");
        Ok(storage)
    }

    pub async fn with_config(config: StorageConfig) -> Result<Self> {
        let storage = Self {
            config,
            nodes: Arc::new(RwLock::new(HashMap::new())),
            contributions: Arc::new(RwLock::new(HashMap::new())),
            stats: Arc::new(RwLock::new(StorageStats::default())),
            node_contexts: Arc::new(RwLock::new(HashMap::new())),
        };
        
        storage.ensure_storage_exists()?;
        storage.initialize_fractal_nodes().await?;
        
        Ok(storage)
    }

    fn ensure_storage_exists(&self) -> Result<()> {
        let path = Path::new(&self.config.base_path);
        if !path.exists() {
            fs::create_dir_all(path)?;
        }
        
        let nodes_path = path.join("nodes");
        let contributions_path = path.join("contributions");
        let contexts_path = path.join("contexts");
        
        for dir_path in [nodes_path, contributions_path, contexts_path] {
            if !dir_path.exists() {
                fs::create_dir_all(&dir_path)?;
            }
        }
        
        Ok(())
    }

    async fn initialize_fractal_nodes(&self) -> Result<()> {
        info!("Starting fractal node initialization...");
        
        let base_nodes = vec![
            ("codex:Void", "Void", FlowState::Plasma, vec!["Potential".to_string(), "Infinite".to_string(), "Source".to_string()], 1.0),
            ("codex:Field", "Field", FlowState::Gas, vec!["Connectivity".to_string(), "Information".to_string(), "Flow".to_string()], 0.8),
            ("codex:Pattern", "Pattern", FlowState::Crystalline, vec!["Form".to_string(), "Rhythm".to_string(), "Order".to_string()], 0.9),
            ("codex:Flow", "Flow", FlowState::Liquid, vec!["Movement".to_string(), "Change".to_string(), "Process".to_string()], 0.85),
            ("codex:Coherence", "Coherence", FlowState::Crystalline, vec!["Alignment".to_string(), "Resonance".to_string(), "Unity".to_string()], 0.95),
            ("codex:Resonance", "Resonance", FlowState::Wave, vec!["Vibration".to_string(), "Harmony".to_string(), "Sync".to_string()], 0.88),
            ("codex:Transformation", "Transformation", FlowState::Colloidal, vec!["Change".to_string(), "Evolution".to_string(), "Metamorphosis".to_string()], 0.82),
            ("codex:Integration", "Integration", FlowState::Colloidal, vec!["Unity".to_string(), "Wholeness".to_string(), "Synthesis".to_string()], 0.87),
            ("codex:Emergence", "Emergence", FlowState::Living, vec!["Novelty".to_string(), "Spontaneity".to_string(), "Creation".to_string()], 0.83),
            ("codex:Wisdom", "Wisdom", FlowState::Living, vec!["Knowledge".to_string(), "Understanding".to_string(), "Insight".to_string()], 0.92),
            ("codex:Consciousness", "Consciousness", FlowState::Living, vec!["Awareness".to_string(), "Experience".to_string(), "Presence".to_string()], 0.96),
            ("codex:Breath", "Breath", FlowState::Gas, vec!["Life".to_string(), "Energy".to_string(), "Spirit".to_string()], 0.78),
        ];

        info!("Created {} base nodes, expanding them fractally...", base_nodes.len());

        for (i, (node_id, name, water_state, archetype, resonance)) in base_nodes.iter().enumerate() {
            info!("Processing base node {}/{}: {}", i + 1, base_nodes.len(), name);
            
            let mut base_node = FractalNode::new(
                node_id.to_string(),
                name.to_string(),
                water_state.clone(),
                archetype.clone(),
                *resonance,
                1,
                None,
            );
            
            // Expand into fractal contexts
            info!("Expanding node '{}' fractally...", name);
            self.expand_node_fractally(&mut base_node).await?;
            
            // Store the base node
            info!("Storing expanded node '{}'...", name);
            self.store_node(&base_node).await?;
            
            info!("Node '{}' processed successfully", name);
        }
        
        info!("All fractal nodes initialized successfully");
        Ok(())
    }

    async fn expand_node_fractally(&self, base_node: &mut FractalNode) -> Result<()> {
        // Create all possible context combinations
        let scientific_contexts = vec![
            ScientificContext::Empirical,
            ScientificContext::Theoretical,
            ScientificContext::Experimental,
        ];
        
        let symbolic_contexts = vec![
            SymbolicContext::Archetypal,
            SymbolicContext::Cultural,
            SymbolicContext::Personal,
        ];
        
        let water_contexts = vec![
            WaterContext::Phase,
            WaterContext::Flow,
            WaterContext::Coherence,
        ];
        
        // Add contexts to the base node
        for sci_context in &scientific_contexts {
            let context = ContextType::Scientific(sci_context.clone());
            base_node.add_context(context.clone());
            
            // Store context mapping
            self.add_node_to_context(&context, &base_node.id).await;
        }
        
        for sym_context in &symbolic_contexts {
            let context = ContextType::Symbolic(sym_context.clone());
            base_node.add_context(context.clone());
            
            self.add_node_to_context(&context, &base_node.id).await;
        }
        
        for wat_context in &water_contexts {
            let context = ContextType::Water(wat_context.clone());
            base_node.add_context(context.clone());
            
            self.add_node_to_context(&context, &base_node.id).await;
        }
        
        Ok(())
    }

    async fn add_node_to_context(&self, context: &ContextType, node_id: &str) {
        let mut contexts = self.node_contexts.write().await;
        contexts.entry(context.clone())
            .or_insert_with(Vec::new)
            .push(node_id.to_string());
    }

    fn generate_content_hash(&self, content: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(content.as_bytes());
        hex::encode(hasher.finalize())
    }
}

// ============================================================================
// TRAIT IMPLEMENTATIONS - Concrete storage behavior
// ============================================================================

impl NodeStorage for FractalStorage {
    async fn store_node(&self, node: &FractalNode) -> Result<()> {
        let mut nodes = self.nodes.write().await;
        nodes.insert(node.id.clone(), node.clone());
        
        // Update stats
        let mut stats = self.stats.write().await;
        if node.fractal_level == 1 {
            stats.total_nodes += 1;
        } else {
            stats.total_subnodes += 1;
        }
        stats.last_updated = chrono::Utc::now();
        
        Ok(())
    }

    async fn get_node(&self, node_id: &str) -> Option<FractalNode> {
        let nodes = self.nodes.read().await;
        nodes.get(node_id).cloned()
    }

    async fn get_all_nodes(&self) -> Vec<FractalNode> {
        let nodes = self.nodes.read().await;
        nodes.values().cloned().collect()
    }

    async fn delete_node(&self, node_id: &str) -> Result<()> {
        let mut nodes = self.nodes.write().await;
        nodes.remove(node_id);
        Ok(())
    }
}

impl ContributionStorage for FractalStorage {
    async fn store_contribution(&self, contribution: Contribution) -> Result<serde_json::Value> {
        let mut contributions = self.contributions.write().await;
        contributions.insert(contribution.id.clone(), contribution.clone());
        
        // Update stats
        let mut stats = self.stats.write().await;
        stats.total_contributions += 1;
        stats.last_updated = chrono::Utc::now();
        
        // Generate content hash
        let content_hash = self.generate_content_hash(&contribution.content);
        
        Ok(serde_json::json!({
            "id": contribution.id,
            "content_hash": content_hash,
            "node_id": contribution.node_id,
            "resonance": contribution.resonance,
            "timestamp": contribution.timestamp
        }))
    }

    async fn get_contribution(&self, content_hash: &str) -> Option<Contribution> {
        let contributions = self.contributions.read().await;
        contributions.values().find(|c| {
            self.generate_content_hash(&c.content) == content_hash
        }).cloned()
    }

    async fn get_node_contributions(&self, node_id: &str) -> serde_json::Value {
        let contributions = self.contributions.read().await;
        let node_contributions: Vec<&Contribution> = contributions
            .values()
            .filter(|c| c.node_id == node_id)
            .collect();
        
        serde_json::json!({
            "contributions": node_contributions,
            "count": node_contributions.len()
        })
    }

    async fn get_user_contributions(&self, user_id: &str) -> serde_json::Value {
        let contributions = self.contributions.read().await;
        let user_contributions: Vec<&Contribution> = contributions
            .values()
            .filter(|c| c.user_id == user_id)
            .collect();
        
        serde_json::json!({
            "contributions": user_contributions,
            "count": user_contributions.len()
        })
    }
}

impl FractalExpansionStorage for FractalStorage {
    async fn expand_node_fractally(&self, base_node: &mut FractalNode) -> Result<()> {
        self.expand_node_fractally(base_node).await
    }

    async fn get_fractal_expansion(&self, node_id: &str) -> Result<serde_json::Value> {
        let nodes = self.nodes.read().await;
        let base_node = nodes.get(node_id)
            .ok_or_else(|| anyhow!("Node not found: {}", node_id))?;
        
        if base_node.fractal_level != 1 {
            return Err(anyhow!("Only base nodes can be expanded"));
        }
        
        // Group contexts by type
        let mut context_groups: HashMap<String, Vec<&ContextType>> = HashMap::new();
        context_groups.insert("scientific".to_string(), Vec::new());
        context_groups.insert("symbolic".to_string(), Vec::new());
        context_groups.insert("water".to_string(), Vec::new());
        
        for context in &base_node.contexts {
            match context {
                ContextType::Scientific(_) => {
                    context_groups.get_mut("scientific").unwrap().push(context);
                },
                ContextType::Symbolic(_) => {
                    context_groups.get_mut("symbolic").unwrap().push(context);
                },
                ContextType::Water(_) => {
                    context_groups.get_mut("water").unwrap().push(context);
                },
                ContextType::Hybrid(_) => {
                    // Hybrid contexts can go in multiple groups
                    context_groups.get_mut("scientific").unwrap().push(context);
                    context_groups.get_mut("symbolic").unwrap().push(context);
                    context_groups.get_mut("water").unwrap().push(context);
                },
            }
        }
        
        Ok(serde_json::json!({
            "base_node": base_node,
            "contexts": context_groups,
            "total_contexts": base_node.contexts.len(),
            "context_types": vec!["scientific", "symbolic", "water"]
        }))
    }

    async fn get_context_nodes(&self, context: &ContextType) -> Vec<FractalNode> {
        let contexts = self.node_contexts.read().await;
        let node_ids = contexts.get(context).cloned().unwrap_or_default();
        
        let nodes = self.nodes.read().await;
        node_ids.iter()
            .filter_map(|id| nodes.get(id).cloned())
            .collect()
    }
}

impl StorageMetadata for FractalStorage {
    async fn get_storage_stats(&self) -> StorageStats {
        let stats = self.stats.read().await;
        stats.clone()
    }

    async fn update_stats(&self) -> Result<()> {
        let mut stats = self.stats.write().await;
        stats.last_updated = chrono::Utc::now();
        
        // Recalculate totals
        let nodes = self.nodes.read().await;
        let contributions = self.contributions.read().await;
        
        stats.total_nodes = nodes.values().filter(|n| n.fractal_level == 1).count();
        stats.total_subnodes = nodes.values().filter(|n| n.fractal_level > 1).count();
        stats.total_contributions = contributions.len();
        
        Ok(())
    }

    async fn get_storage_size(&self) -> u64 {
        // Calculate approximate storage size
        let nodes = self.nodes.read().await;
        let contributions = self.contributions.read().await;
        
        let node_size: usize = nodes.values().map(|n| {
            serde_json::to_string(n).unwrap_or_default().len()
        }).sum();
        
        let contribution_size: usize = contributions.values().map(|c| {
            serde_json::to_string(c).unwrap_or_default().len()
        }).sum();
        
        (node_size + contribution_size) as u64
    }
}

// ============================================================================
// UTILITY FUNCTIONS - Pure functions for data manipulation
// ============================================================================

pub fn filter_nodes_by_resonance(nodes: &[FractalNode], min_resonance: f64) -> Vec<FractalNode> {
    nodes.iter()
        .filter(|node| node.resonance >= min_resonance)
        .cloned()
        .collect()
}

pub fn sort_nodes_by_resonance(nodes: &mut [FractalNode]) {
    nodes.sort_by(|a, b| b.resonance.partial_cmp(&a.resonance).unwrap_or(std::cmp::Ordering::Equal));
}

pub fn group_nodes_by_context(nodes: &[FractalNode]) -> HashMap<String, Vec<FractalNode>> {
    let mut groups: HashMap<String, Vec<FractalNode>> = HashMap::new();
    
    for node in nodes {
        for context in &node.contexts {
            let context_key = match context {
                ContextType::Scientific(_) => "scientific".to_string(),
                ContextType::Symbolic(_) => "symbolic".to_string(),
                ContextType::Water(_) => "water".to_string(),
                ContextType::Hybrid(_) => "hybrid".to_string(),
            };
            
            groups.entry(context_key)
                .or_insert_with(Vec::new)
                .push(node.clone());
        }
    }
    
    groups
}

