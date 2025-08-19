use axum::{
    extract::{Path, State},
    http::{HeaderValue, Method, StatusCode},
    response::Json,
    routing::{get, post},
    Router,
};
use serde_json::{json, Value};
use std::sync::Arc;
use tower_http::cors::{Any, CorsLayer};
use tracing::{info, error};

mod models;
mod storage;

use storage::FractalStorage;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize tracing
    tracing_subscriber::fmt::init();
    
    info!("Living Codex Phase 6 - Rust Fractal Federation Server");
    info!("============================================================");
    info!("Starting server on http://localhost:8789");
    info!("Fractal levels: 1 (base nodes) + 2 (expanded subnodes)");
    info!("Contexts: scientific, symbolic, water");
    info!("============================================================");
    
    // Initialize fractal storage
    let storage = Arc::new(FractalStorage::new("./rust-fractal-storage")?);
    
    // Configure CORS
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods([Method::GET, Method::POST])
        .allow_headers(Any);
    
    // Build router
    let app = Router::new()
        .route("/", get(root))
        .route("/storage/stats", get(get_storage_stats))
        .route("/contributions/:content_hash", get(get_contribution))
        .route("/contributions/node/:node_id", get(get_node_contributions))
        .route("/contributions/user/:user_id", get(get_user_contributions))
        .route("/inbox", post(post_to_inbox))
        .route("/outbox", get(get_outbox))
        .route("/fractal/expand/:node_id", get(get_fractal_expansion))
        .route("/fractal/nodes/:node_id", get(get_fractal_node))
        .route("/fractal/subnodes/:node_id", get(get_fractal_subnodes))
        .route("/fractal/context/:context", get(get_fractal_context))
        .route("/fractal/levels", get(get_fractal_levels))
        .route("/.well-known/webfinger", get(webfinger))
        .route("/actor", get(get_actor))
        .route("/federation/peers", get(get_federation_peers))
        .route("/federation/sync", get(federation_sync))
        .layer(cors)
        .with_state(storage);
    
    // Start server
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8789").await?;
    info!("Server listening on http://localhost:8789");
    
    axum::serve(listener, app).await?;
    Ok(())
}

// Root endpoint
async fn root() -> Json<Value> {
    Json(json!({
        "name": "Living Codex Phase 6 - Rust Fractal Federation",
        "version": "3.0.0",
        "status": "active",
        "fractal_levels": [1, 2],
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
                "/fractal/subnodes/{node_id}",
                "/fractal/context/{context}",
                "/fractal/levels"
            ]
        }
    }))
}

// Storage stats endpoint
async fn get_storage_stats(State(storage): State<Arc<FractalStorage>>) -> Json<Value> {
    let stats = storage.get_storage_stats().await;
    Json(json!(stats))
}

// Get contribution by hash
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

// Get node contributions
async fn get_node_contributions(
    State(storage): State<Arc<FractalStorage>>,
    Path(node_id): Path<String>,
) -> Json<Value> {
    let contributions = storage.get_node_contributions(&node_id).await;
    Json(contributions)
}

// Get user contributions
async fn get_user_contributions(
    State(storage): State<Arc<FractalStorage>>,
    Path(user_id): Path<String>,
) -> Json<Value> {
    let contributions = storage.get_user_contributions(&user_id).await;
    Json(contributions)
}

// Post to inbox (ActivityPub)
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
    let fractal_context = obj.get("fractalContext").and_then(|v| v.as_str()).map(|s| s.to_string());
    
    let contribution = models::Contribution::new(
        node_id.to_string(),
        actor.to_string(),
        content.to_string(),
        resonance,
        fractal_context,
    );
    
    match storage.store_contribution(contribution).await {
        Ok(result) => Ok(Json(json!({
            "status": "accepted",
            "result": result
        }))),
        Err(_) => Err(StatusCode::INTERNAL_SERVER_ERROR),
    }
}

// Get outbox
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

// Get fractal expansion
async fn get_fractal_expansion(
    State(storage): State<Arc<FractalStorage>>,
    Path(node_id): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    match storage.get_fractal_expansion(&node_id).await {
        Ok(expansion) => Ok(Json(expansion)),
        Err(_) => Err(StatusCode::NOT_FOUND),
    }
}

// Get fractal node
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
                node_data["subnode_count"] = json!(n.subnodes.len());
            } else {
                node_data["fractal_context"] = json!("subnode");
                node_data["expansion_available"] = json!(false);
                node_data["parent_context"] = json!(n.parent_id);
            }
            Ok(Json(node_data))
        },
        None => Err(StatusCode::NOT_FOUND),
    }
}

// Get fractal subnodes
async fn get_fractal_subnodes(
    State(storage): State<Arc<FractalStorage>>,
    Path(node_id): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    let node = storage.get_node(&node_id).await;
    match node {
        Some(n) => {
            if n.fractal_level != 1 {
                return Err(StatusCode::BAD_REQUEST);
            }
            
            let expansion = storage.get_fractal_expansion(&node_id).await.unwrap();
            Ok(Json(expansion))
        },
        None => Err(StatusCode::NOT_FOUND),
    }
}

// Get fractal context
async fn get_fractal_context(
    State(storage): State<Arc<FractalStorage>>,
    Path(context): Path<String>,
) -> Result<Json<Value>, StatusCode> {
    let valid_contexts = vec!["scientific", "symbolic", "water"];
    if !valid_contexts.contains(&context.as_str()) {
        return Err(StatusCode::BAD_REQUEST);
    }
    
    // For now, return a simplified response
    // In a full implementation, we'd scan all nodes for this context
    Ok(Json(json!({
        "context": context,
        "nodes": {},
        "count": 0,
        "description": format!("All {} lens subnodes across the Living Codex", context)
    })))
}

// Get fractal levels
async fn get_fractal_levels(State(storage): State<Arc<FractalStorage>>) -> Json<Value> {
    let stats = storage.get_storage_stats().await;
    
    Json(json!({
        "fractal_levels": [1, 2],
        "current_max_level": 2,
        "level_descriptions": {
            1: "Base nodes - Core concepts of the Living Codex",
            2: "Fractal subnodes - Expanded perspectives across scientific, symbolic, and water-state lenses"
        },
        "level_statistics": {
            "level_1": {
                "name": "Base Nodes",
                "count": stats.total_nodes,
                "description": "Primary ontological concepts"
            },
            "level_2": {
                "name": "Fractal Subnodes",
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

// WebFinger endpoint
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

// Actor endpoint
async fn get_actor() -> Json<Value> {
    Json(json!({
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": "http://localhost:8789/actor",
        "type": "Person",
        "name": "Living Codex Rust Fractal Federation",
        "summary": "Phase 6 federation server with fractal node expansion",
        "inbox": "http://localhost:8789/inbox",
        "outbox": "http://localhost:8789/outbox",
        "preferredUsername": "fractal",
        "fractal_capabilities": {
            "levels": [1, 2],
            "contexts": ["scientific", "symbolic", "water"],
            "expansion": true
        }
    }))
}

// Federation peers
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
                "capabilities": ["phase4", "phase5", "phase6", "federation", "fractal_expansion", "multi_implementation"],
                "status": "active"
            }
        ]
    }))
}

// Federation sync
async fn federation_sync() -> Json<Value> {
    Json(json!({
        "synced": true,
        "timestamp": chrono::Utc::now(),
        "fractal_levels_synced": [1, 2]
    }))
}

