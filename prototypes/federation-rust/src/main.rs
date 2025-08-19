use axum::{
    extract::{Path, State},
    http::{Method, StatusCode},
    response::Json,
    routing::{get, post},
    Router, Server,
};
use serde_json::{json, Value};
use std::sync::Arc;
use tower_http::cors::{Any, CorsLayer};
use tracing::{info, error};

mod models;
mod storage;

use storage::{FractalStorage, NodeStorage, ContributionStorage, FractalExpansionStorage, StorageMetadata};

// ============================================================================
// SERVER CONFIGURATION - Flexible settings like water adapting to containers
// ============================================================================

#[derive(Debug, Clone)]
pub struct ServerConfig {
    pub host: String,
    pub port: u16,
    pub storage_path: String,
    pub enable_cors: bool,
    pub log_level: String,
    pub fractal_levels: Vec<u32>,
}

impl Default for ServerConfig {
    fn default() -> Self {
        Self {
            host: "0.0.0.0".to_string(),
            port: 8789,
            storage_path: "./rust-fractal-storage".to_string(),
            enable_cors: true,
            log_level: "info".to_string(),
            fractal_levels: vec![1, 2],
        }
    }
}

// ============================================================================
// MAIN SERVER - Water-like flow and adaptation
// ============================================================================

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize tracing
    tracing_subscriber::fmt::init();
    
    info!("Living Codex Phase 6 - Rust Fractal Federation Server");
    info!("============================================================");
    info!("Starting server on http://localhost:8789");
    info!("Fractal levels: 1 (base nodes) + 2 (expanded contexts)");
    info!("Contexts: scientific, symbolic, water");
    info!("============================================================");
    
    // Initialize fractal storage with default config
    info!("Initializing fractal storage...");
    let storage = match FractalStorage::new("./rust-fractal-storage").await {
        Ok(storage) => {
            info!("Storage initialized successfully");
            Arc::new(storage)
        },
        Err(e) => {
            error!("Failed to initialize storage: {}", e);
            return Err(e.into());
        }
    };
    
    info!("Storage ready, configuring server...");
    
    // Configure CORS
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods([Method::GET, Method::POST])
        .allow_headers(Any);
    
    // Build router with trait-based endpoints
    let app = Router::new()
        .route("/", get(root))
        .route("/health", get(health_check))
        .route("/storage/stats", get(get_storage_stats))
        .route("/contributions/:content_hash", get(get_contribution))
        .route("/contributions/node/:node_id", get(get_node_contributions))
        .route("/contributions/user/:user_id", get(get_user_contributions))
        .route("/inbox", post(post_to_inbox))
        .route("/outbox", get(get_outbox))
        .route("/fractal/expand/:node_id", get(get_fractal_expansion))
        .route("/fractal/nodes/:node_id", get(get_fractal_node))
        .route("/fractal/context/:context", get(get_fractal_context))
        .route("/fractal/levels", get(get_fractal_levels))
        .route("/.well-known/webfinger", get(webfinger))
        .route("/actor", get(get_actor))
        .route("/federation/peers", get(get_federation_peers))
        .route("/federation/sync", get(federation_sync))
        .layer(cors)
        .with_state(storage);
    
    info!("Router configured, starting server...");
    
    // Start server with proper error handling
    info!("Attempting to bind to 127.0.0.1:8789...");
    let addr = match "127.0.0.1:8789".parse::<std::net::SocketAddr>() {
        Ok(addr) => {
            info!("Successfully parsed address: {}", addr);
            addr
        },
        Err(e) => {
            error!("Failed to parse address 127.0.0.1:8789: {}", e);
            return Err(format!("Address parse error: {}", e).into());
        }
    };
    
    info!("Server listening on http://localhost:8789");
    info!("Starting axum server...");
    
    // Start the server using axum 0.6 compatible syntax
    match Server::bind(&addr).serve(app.into_make_service()).await {
        Ok(_) => {
            info!("Server stopped normally");
            Ok(())
        },
        Err(e) => {
            error!("Server error: {}", e);
            Err(e.into())
        }
    }
}

// ============================================================================
// ROOT AND INFO ENDPOINTS - Server identity and capabilities
// ============================================================================

async fn root() -> Json<Value> {
    Json(json!({
        "name": "Living Codex Phase 6 - Rust Fractal Federation",
        "version": "3.0.0",
        "status": "active",
        "fractal_levels": [1, 2],
        "architecture": "trait-based",
        "flexibility": "water-like",
        "endpoints": {
            "current_level": [
                "/storage/stats",
                "/contributions/{hash}",
                "/contributions/node/{node_id}",
                "/contributions/user/{user_id}",
                "/inbox",
                "/outbox"
            ],
            "next_fractal_level": [
                "/fractal/expand/{node_id}",
                "/fractal/nodes/{node_id}",
                "/fractal/context/{context}",
                "/fractal/levels"
            ]
        }
    }))
}

// ============================================================================
// STORAGE ENDPOINTS - Data management through traits
// ============================================================================

async fn get_storage_stats(State(storage): State<Arc<FractalStorage>>) -> Json<Value> {
    let stats = storage.get_storage_stats().await;
    Json(json!(stats))
}

async fn get_contribution(
    State(storage): State<Arc<FractalStorage>>,
    Path(content_hash): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    let contribution = storage.get_contribution(&content_hash).await;
    match contribution {
        Some(c) => Ok(Json(json!(c))),
        None => Err(StatusCode::NOT_FOUND),
    }
}

async fn get_node_contributions(
    State(storage): State<Arc<FractalStorage>>,
    Path(node_id): Path<String>,
) -> Json<Value> {
    let contributions = storage.get_node_contributions(&node_id).await;
    Json(contributions)
}

async fn get_user_contributions(
    State(storage): State<Arc<FractalStorage>>,
    Path(user_id): Path<String>,
) -> Json<Value> {
    let contributions = storage.get_user_contributions(&user_id).await;
    Json(contributions)
}

// ============================================================================
// ACTIVITYPUB ENDPOINTS - Federation and social features
// ============================================================================

async fn post_to_inbox(
    State(storage): State<Arc<FractalStorage>>,
    Json(payload): Json<Value>,
) -> Result<Json<Value>, StatusCode> {
    // Parse ActivityPub Create activity
    let activity_type = payload.get("type").and_then(|v| v.as_str()).unwrap_or("");
    let actor = payload.get("actor").and_then(|v| v.as_str()).unwrap_or("anonymous");
    let object = payload.get("object");
    
    if activity_type != "Create" || object.is_none() {
        return Err(StatusCode::BAD_REQUEST);
    }
    
    let obj = object.unwrap();
    let node_id = obj.get("nodeId").and_then(|v| v.as_str()).unwrap_or("");
    let content = obj.get("content").and_then(|v| v.as_str()).unwrap_or("");
    let resonance = obj.get("resonance").and_then(|v| v.as_f64()).unwrap_or(0.5);
    
    // Create contribution with default context
    let contribution = models::Contribution::new(
        node_id.to_string(),
        actor.to_string(),
        content.to_string(),
        resonance,
        None, // Will be determined by the node's contexts
    );
    
    match storage.store_contribution(contribution).await {
        Ok(result) => Ok(Json(json!({
            "status": "accepted",
            "result": result
        }))),
        Err(_) => Err(StatusCode::INTERNAL_SERVER_ERROR),
    }
}

async fn get_outbox(State(storage): State<Arc<FractalStorage>>) -> Json<Value> {
    let stats = storage.get_storage_stats().await;
    
    Json(json!({
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": "/outbox",
        "type": "OrderedCollection",
        "totalItems": stats.total_contributions,
        "orderedItems": []
    }))
}

// ============================================================================
// FRACTAL ENDPOINTS - Context-based expansion and exploration
// ============================================================================

async fn get_fractal_expansion(
    State(storage): State<Arc<FractalStorage>>,
    Path(node_id): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    match storage.get_fractal_expansion(&node_id).await {
        Ok(expansion) => Ok(Json(expansion)),
        Err(_) => Err(StatusCode::NOT_FOUND),
    }
}

async fn get_fractal_node(
    State(storage): State<Arc<FractalStorage>>,
    Path(node_id): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    let node = storage.get_node(&node_id).await;
    match node {
        Some(n) => {
            let mut node_data = json!(n);
            if n.fractal_level == 1 {
                node_data["fractal_context"] = json!("base_node");
                node_data["expansion_available"] = json!(true);
                node_data["context_count"] = json!(n.contexts.len());
            } else {
                node_data["fractal_context"] = json!("context_node");
                node_data["expansion_available"] = json!(false);
                node_data["parent_context"] = json!(n.parent_id);
            }
            Ok(Json(node_data))
        },
        None => Err(StatusCode::NOT_FOUND),
    }
}

async fn get_fractal_context(
    State(storage): State<Arc<FractalStorage>>,
    Path(context): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    let valid_contexts = vec!["scientific", "symbolic", "water"];
    if !valid_contexts.contains(&context.as_str()) {
        return Err(StatusCode::BAD_REQUEST);
    }
    
    // Get all nodes for this context
    let all_nodes = storage.get_all_nodes().await;
    let context_nodes = storage::group_nodes_by_context(&all_nodes);
    
    let context_key = context.to_string();
    let nodes = context_nodes.get(&context_key).cloned().unwrap_or_default();
    
    Ok(Json(json!({
        "context": context,
        "nodes": nodes,
        "count": nodes.len(),
        "description": format!("All {} lens nodes across the Living Codex", context)
    })))
}

async fn get_fractal_levels(State(storage): State<Arc<FractalStorage>>) -> Json<Value> {
    let stats = storage.get_storage_stats().await;
    
    Json(json!({
        "fractal_levels": [1, 2],
        "current_max_level": 2,
        "level_descriptions": {
            "1": "Base nodes - Core concepts of the Living Codex",
            "2": "Context nodes - Expanded perspectives across scientific, symbolic, and water-state lenses"
        },
        "level_statistics": {
            "level_1": {
                "name": "Base Nodes",
                "count": stats.total_nodes,
                "description": "Primary ontological concepts"
            },
            "level_2": {
                "name": "Context Nodes",
                "count": stats.total_subnodes,
                "description": "Expanded perspectives and deeper wisdom"
            }
        },
        "expansion_dimensions": {
            "scientific": "Empirical, theoretical, and experimental perspectives",
            "symbolic": "Archetypal, cultural, and personal meanings",
            "water": "Phase transitions, flow dynamics, and coherence patterns"
        }
    }))
}

// ============================================================================
// FEDERATION ENDPOINTS - Inter-server communication
// ============================================================================

async fn webfinger() -> Json<Value> {
    Json(json!({
        "subject": "acct:fractal@localhost",
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": "http://localhost:8789/actor"
            },
            {
                "rel": "http://www.w3.org/ns/activitystreams#inbox",
                "type": "application/activity+json",
                "href": "http://localhost:8789/inbox"
            },
            {
                "rel": "http://www.w3.org/ns/activitystreams#outbox",
                "type": "application/activity+json",
                "href": "http://localhost:8789/outbox"
            }
        ]
    }))
}

async fn get_actor() -> Json<Value> {
    Json(json!({
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": "http://localhost:8789/actor",
        "type": "Person",
        "name": "Living Codex Rust Fractal Federation",
        "summary": "Phase 6 federation server with trait-based architecture",
        "inbox": "http://localhost:8789/inbox",
        "outbox": "http://localhost:8789/outbox",
        "preferredUsername": "fractal",
        "fractal_capabilities": {
            "levels": [1, 2],
            "contexts": ["scientific", "symbolic", "water"],
            "expansion": true,
            "architecture": "trait-based",
            "flexibility": "water-like"
        }
    }))
}

async fn get_federation_peers() -> Json<Value> {
    Json(json!({
        "peers": [
            {
                "id": "nodejs@localhost:8787",
                "url": "http://localhost:8787",
                "capabilities": ["phase4", "federation", "storage"],
                "status": "active"
            },
            {
                "id": "python@localhost:8788",
                "url": "http://localhost:8788",
                "capabilities": ["phase4", "phase5", "federation", "fractal_expansion"],
                "status": "active"
            },
            {
                "id": "rust@localhost:8789",
                "url": "http://localhost:8789",
                "capabilities": ["phase4", "phase5", "phase6", "federation", "fractal_expansion", "trait_architecture", "water_like"],
                "status": "active"
            }
        ]
    }))
}

async fn federation_sync() -> Json<Value> {
    Json(json!({
        "synced": true,
        "timestamp": chrono::Utc::now(),
        "fractal_levels_synced": [1, 2],
        "architecture": "trait-based",
        "flexibility": "water-like"
    }))
}

async fn health_check() -> Json<Value> {
    Json(json!({
        "status": "ok",
        "message": "Server is running"
    }))
}

