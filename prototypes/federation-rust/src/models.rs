use serde::{Deserialize, Serialize};
use chrono::{DateTime, Utc};
use uuid::Uuid;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FractalNode {
    pub id: String,
    pub name: String,
    pub water_state: String,
    pub archetype: Vec<String>,
    pub resonance: f64,
    pub fractal_level: u32,
    pub subnodes: std::collections::HashMap<String, FractalNode>,
    pub parent_id: Option<String>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

impl FractalNode {
    pub fn new(
        id: String,
        name: String,
        water_state: String,
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
            subnodes: std::collections::HashMap::new(),
            parent_id,
            created_at: now,
            updated_at: now,
        }
    }

    pub fn add_subnode(&mut self, subnode: FractalNode) {
        self.subnodes.insert(subnode.id.clone(), subnode);
        self.updated_at = Utc::now();
    }

    pub fn get_subnode_count(&self) -> usize {
        self.subnodes.len()
    }

    pub fn get_context_subnodes(&self, context: &str) -> Vec<&FractalNode> {
        self.subnodes
            .values()
            .filter(|node| node.id.contains(&format!(":{}:", context)))
            .collect()
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Contribution {
    pub id: String,
    pub node_id: String,
    pub user_id: String,
    pub content: String,
    pub resonance: f64,
    pub timestamp: DateTime<Utc>,
    pub fractal_context: Option<String>,
}

impl Contribution {
    pub fn new(
        node_id: String,
        user_id: String,
        content: String,
        resonance: f64,
        fractal_context: Option<String>,
    ) -> Self {
        Self {
            id: Uuid::new_v4().to_string(),
            node_id,
            user_id,
            content,
            resonance,
            timestamp: Utc::now(),
            fractal_context,
        }
    }
}

#[derive(Debug, Serialize, Deserialize)]
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

#[derive(Debug, Serialize, Deserialize)]
pub struct FractalExpansionStats {
    pub total_fractal_dimensions: usize,
    pub contexts: Vec<String>,
    pub level_breakdown: std::collections::HashMap<u32, usize>,
}

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
                contexts: vec!["scientific".to_string(), "symbolic".to_string(), "water".to_string()],
                level_breakdown: std::collections::HashMap::new(),
            },
        }
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ActivityPubCreate {
    #[serde(rename = "type")]
    pub activity_type: String,
    pub actor: String,
    pub object: ActivityPubObject,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ActivityPubObject {
    #[serde(rename = "type")]
    pub object_type: String,
    pub node_id: String,
    pub content: String,
    pub resonance: f64,
    pub fractal_context: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct FractalExpansionResponse {
    pub base_node: FractalNode,
    pub subnodes: std::collections::HashMap<String, std::collections::HashMap<String, FractalNode>>,
    pub total_subnodes: usize,
    pub contexts: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct FractalLevelsResponse {
    pub fractal_levels: Vec<u32>,
    pub current_max_level: u32,
    pub level_descriptions: std::collections::HashMap<u32, String>,
    pub level_statistics: std::collections::HashMap<String, LevelStats>,
    pub expansion_dimensions: std::collections::HashMap<String, String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct LevelStats {
    pub name: String,
    pub count: usize,
    pub description: String,
}

