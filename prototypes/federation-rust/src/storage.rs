use crate::models::{FractalNode, Contribution, StorageStats, FractalExpansionStats};
use anyhow::{Result, anyhow};
use serde_json;
use std::collections::HashMap;
use std::fs;
use std::path::Path;
use std::sync::Arc;
use tokio::sync::RwLock;
use sha2::{Sha256, Digest};
use hex;

pub struct FractalStorage {
    storage_path: String,
    nodes: Arc<RwLock<HashMap<String, FractalNode>>>,
    contributions: Arc<RwLock<HashMap<String, Contribution>>>,
    stats: Arc<RwLock<StorageStats>>,
}

impl FractalStorage {
    pub fn new(storage_path: &str) -> Result<Self> {
        let storage = Self {
            storage_path: storage_path.to_string(),
            nodes: Arc::new(RwLock::new(HashMap::new())),
            contributions: Arc::new(RwLock::new(HashMap::new())),
            stats: Arc::new(RwLock::new(StorageStats::default())),
        };
        
        storage.ensure_storage_exists()?;
        storage.initialize_fractal_nodes()?;
        
        Ok(storage)
    }

    fn ensure_storage_exists(&self) -> Result<()> {
        let path = Path::new(&self.storage_path);
        if !path.exists() {
            fs::create_dir_all(path)?;
        }
        
        let nodes_path = path.join("nodes");
        let contributions_path = path.join("contributions");
        
        if !nodes_path.exists() {
            fs::create_dir_all(&nodes_path)?;
        }
        if !contributions_path.exists() {
            fs::create_dir_all(&contributions_path)?;
        }
        
        Ok(())
    }

    fn initialize_fractal_nodes(&self) -> Result<()> {
        let base_nodes = vec![
            ("codex:Void", "Void", "Plasma", vec!["Potential", "Infinite", "Source"], 1.0),
            ("codex:Field", "Field", "Vapor", vec!["Connectivity", "Information", "Flow"], 0.8),
            ("codex:Pattern", "Pattern", "Structured", vec!["Form", "Rhythm", "Order"], 0.9),
            ("codex:Flow", "Flow", "Liquid", vec!["Movement", "Change", "Process"], 0.85),
            ("codex:Coherence", "Coherence", "Crystalline", vec!["Alignment", "Resonance", "Unity"], 0.95),
            ("codex:Resonance", "Resonance", "Wave", vec!["Vibration", "Harmony", "Sync"], 0.88),
            ("codex:Transformation", "Transformation", "Phase", vec!["Change", "Evolution", "Metamorphosis"], 0.82),
            ("codex:Integration", "Integration", "Colloidal", vec!["Unity", "Wholeness", "Synthesis"], 0.87),
            ("codex:Emergence", "Emergence", "Complex", vec!["Novelty", "Spontaneity", "Creation"], 0.83),
            ("codex:Wisdom", "Wisdom", "Living", vec!["Knowledge", "Understanding", "Insight"], 0.92),
            ("codex:Consciousness", "Consciousness", "Aware", vec!["Awareness", "Experience", "Presence"], 0.96),
            ("codex:Breath", "Breath", "Vapor", vec!["Life", "Energy", "Spirit"], 0.78),
        ];

        for (node_id, name, water_state, archetype, resonance) in base_nodes {
            let mut base_node = FractalNode::new(
                node_id.to_string(),
                name.to_string(),
                water_state.to_string(),
                archetype.clone(),
                resonance,
                1,
                None,
            );
            
            // Expand into fractal subnodes
            self.expand_node_fractally(&mut base_node)?;
            
            // Store the base node
            self.store_node(&base_node).await?;
        }
        
        Ok(())
    }

    fn expand_node_fractally(&self, base_node: &mut FractalNode) -> Result<()> {
        let node_name = &base_node.name;
        let contexts = vec!["scientific", "symbolic", "water"];
        let subcontexts = vec!["empirical", "theoretical", "experimental"];
        
        for context in &contexts {
            for subcontext in &subcontexts {
                let subnode_id = format!("{}:{}:{}", base_node.id, context, subcontext);
                let subnode_name = format!("{} {} {}", node_name, context, subcontext);
                
                let resonance_multiplier = match (context.as_str(), subcontext.as_str()) {
                    ("scientific", "empirical") => 0.8,
                    ("scientific", "theoretical") => 0.85,
                    ("scientific", "experimental") => 0.75,
                    ("symbolic", "empirical") => 0.9,
                    ("symbolic", "theoretical") => 0.95,
                    ("symbolic", "experimental") => 0.85,
                    ("water", "empirical") => 0.8,
                    ("water", "theoretical") => 0.85,
                    ("water", "experimental") => 0.75,
                    _ => 0.8,
                };
                
                let subnode = FractalNode::new(
                    subnode_id,
                    subnode_name,
                    base_node.water_state.clone(),
                    base_node.archetype.clone(),
                    base_node.resonance * resonance_multiplier,
                    2,
                    Some(base_node.id.clone()),
                );
                
                base_node.add_subnode(subnode);
            }
        }
        
        Ok(())
    }

    pub async fn store_node(&self, node: &FractalNode) -> Result<()> {
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

    pub async fn get_node(&self, node_id: &str) -> Option<FractalNode> {
        let nodes = self.nodes.read().await;
        nodes.get(node_id).cloned()
    }

    pub async fn store_contribution(&self, contribution: Contribution) -> Result<serde_json::Value> {
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

    pub async fn get_contribution(&self, content_hash: &str) -> Option<Contribution> {
        let contributions = self.contributions.read().await;
        contributions.values().find(|c| {
            self.generate_content_hash(&c.content) == content_hash
        }).cloned()
    }

    pub async fn get_node_contributions(&self, node_id: &str) -> serde_json::Value {
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

    pub async fn get_user_contributions(&self, user_id: &str) -> serde_json::Value {
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

    pub async fn get_storage_stats(&self) -> StorageStats {
        let stats = self.stats.read().await;
        stats.clone()
    }

    pub async fn get_fractal_expansion(&self, node_id: &str) -> Result<serde_json::Value> {
        let nodes = self.nodes.read().await;
        let base_node = nodes.get(node_id)
            .ok_or_else(|| anyhow!("Node not found: {}", node_id))?;
        
        if base_node.fractal_level != 1 {
            return Err(anyhow!("Only base nodes can be expanded"));
        }
        
        let mut grouped_subnodes: HashMap<String, HashMap<String, FractalNode>> = HashMap::new();
        grouped_subnodes.insert("scientific".to_string(), HashMap::new());
        grouped_subnodes.insert("symbolic".to_string(), HashMap::new());
        grouped_subnodes.insert("water".to_string(), HashMap::new());
        
        for (sub_id, subnode) in &base_node.subnodes {
            if sub_id.contains(":scientific:") {
                grouped_subnodes.get_mut("scientific").unwrap().insert(sub_id.clone(), subnode.clone());
            } else if sub_id.contains(":symbolic:") {
                grouped_subnodes.get_mut("symbolic").unwrap().insert(sub_id.clone(), subnode.clone());
            } else if sub_id.contains(":water:") {
                grouped_subnodes.get_mut("water").unwrap().insert(sub_id.clone(), subnode.clone());
            }
        }
        
        Ok(serde_json::json!({
            "base_node": base_node,
            "subnodes": grouped_subnodes,
            "total_subnodes": base_node.subnodes.len(),
            "contexts": vec!["scientific", "symbolic", "water"]
        }))
    }

    fn generate_content_hash(&self, content: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(content.as_bytes());
        hex::encode(hasher.finalize())
    }
}

