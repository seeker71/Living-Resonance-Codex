#!/bin/bash

# 🚀 Living Codex Containerized Ecosystem Deployment Script
# This script deploys the complete water state ecosystem using Docker/Kubernetes

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
ECOSYSTEM_NAME="living-codex"
DEPLOYMENT_TYPE=${1:-"docker"} # docker or kubernetes
SCALE_ICE=${2:-3}
SCALE_WATER=${3:-5}
SCALE_VAPOR=${4:-10}
SCALE_PLASMA=${5:-3}

echo -e "${CYAN}🌊 Living Codex Containerized Ecosystem Deployment${NC}"
echo -e "${BLUE}================================================${NC}"
echo -e "Deployment Type: ${YELLOW}${DEPLOYMENT_TYPE}${NC}"
echo -e "Scaling: ICE=${SCALE_ICE}, WATER=${SCALE_WATER}, VAPOR=${SCALE_VAPOR}, PLASMA=${SCALE_PLASMA}"
echo ""

# Function to check prerequisites
check_prerequisites() {
    echo -e "${BLUE}🔍 Checking prerequisites...${NC}"
    
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}❌ Docker not found. Please install Docker first.${NC}"
        exit 1
    fi
    
    if ! docker compose version &> /dev/null; then
        echo -e "${RED}❌ Docker Compose not found. Please install Docker Compose first.${NC}"
        exit 1
    fi
    
    if [ "$DEPLOYMENT_TYPE" = "kubernetes" ]; then
        if ! command -v kubectl &> /dev/null; then
            echo -e "${RED}❌ kubectl not found. Please install kubectl first.${NC}"
            exit 1
        fi
        
        if ! kubectl cluster-info &> /dev/null; then
            echo -e "${RED}❌ Kubernetes cluster not accessible. Please check your cluster.${NC}"
            exit 1
        fi
    fi
    
    echo -e "${GREEN}✅ Prerequisites check passed${NC}"
}

# Function to build Docker images
build_images() {
    echo -e "${BLUE}🔨 Building Docker images...${NC}"
    
    # Build ICE bootstrap image
    echo -e "${YELLOW}Building ICE bootstrap image...${NC}"
    docker build -f docker/Dockerfile.ice -t living-codex:ice-latest ..
    
    # Build WATER service image
    echo -e "${YELLOW}Building WATER service image...${NC}"
    docker build -f docker/Dockerfile.water -t living-codex:water-latest ..
    
    # Build VAPOR interaction image
    echo -e "${YELLOW}Building VAPOR interaction image...${NC}"
    docker build -f docker/Dockerfile.vapor -t living-codex:vapor-latest ..
    
    # Build PLASMA streaming image
    echo -e "${YELLOW}Building PLASMA streaming image...${NC}"
    docker build -f docker/Dockerfile.plasma -t living-codex:plasma-latest ..
    
    echo -e "${GREEN}✅ All images built successfully${NC}"
}

# Function to deploy with Docker Compose
deploy_docker() {
    echo -e "${BLUE}🐳 Deploying with Docker Compose...${NC}"
    
    cd docker
    
    # Start the ecosystem
    echo -e "${YELLOW}Starting Living Codex ecosystem...${NC}"
    docker compose up -d
    
    # Wait for services to be ready
    echo -e "${YELLOW}Waiting for services to be ready...${NC}"
    sleep 30
    
    # Check service health
    check_health_docker
    
    cd ..
}

# Function to deploy with Kubernetes
deploy_kubernetes() {
    echo -e "${BLUE}☸️ Deploying with Kubernetes...${NC}"
    
    cd docker/k8s
    
    # Update scaling in deployment files
    sed -i.bak "s/replicas: [0-9]*/replicas: ${SCALE_ICE}/" living-codex-deployment.yaml
    sed -i.bak "s/replicas: [0-9]*/replicas: ${SCALE_WATER}/" living-codex-deployment.yaml
    sed -i.bak "s/replicas: [0-9]*/replicas: ${SCALE_VAPOR}/" living-codex-deployment.yaml
    sed -i.bak "s/replicas: [0-9]*/replicas: ${SCALE_PLASMA}/" living-codex-deployment.yaml
    
    # Apply deployments
    echo -e "${YELLOW}Applying Kubernetes deployments...${NC}"
    kubectl apply -f living-codex-deployment.yaml
    
    # Wait for deployments to be ready
    echo -e "${YELLOW}Waiting for deployments to be ready...${NC}"
    kubectl wait --for=condition=available --timeout=300s deployment/living-codex-ice
    kubectl wait --for=condition=available --timeout=300s deployment/living-codex-water
    kubectl wait --for=condition=available --timeout=300s deployment/living-codex-vapor
    kubectl wait --for=condition=available --timeout=300s deployment/living-codex-plasma
    
    # Check service health
    check_health_kubernetes
    
    cd ../..
}

# Function to check Docker service health
check_health_docker() {
    echo -e "${BLUE}🏥 Checking service health...${NC}"
    
    cd docker
    
    # Check ICE bootstrap
    if docker compose ps ice-bootstrap | grep -q "Up"; then
        echo -e "${GREEN}✅ ICE bootstrap service is running${NC}"
    else
        echo -e "${RED}❌ ICE bootstrap service is not running${NC}"
    fi
    
    # Check WATER services
    if docker compose ps water-web | grep -q "Up"; then
        echo -e "${GREEN}✅ WATER web service is running${NC}"
    else
        echo -e "${RED}❌ WATER web service is not running${NC}"
    fi
    
    # Check VAPOR interaction
    if docker compose ps vapor-interaction | grep -q "Up"; then
        echo -e "${GREEN}✅ VAPOR interaction service is running${NC}"
    else
        echo -e "${RED}❌ VAPOR interaction service is not running${NC}"
    fi
    
    # Check PLASMA streaming
    if docker compose ps plasma-streaming | grep -q "Up"; then
        echo -e "${GREEN}✅ PLASMA streaming service is running${NC}"
    else
        echo -e "${RED}❌ PLASMA streaming service is not running${NC}"
    fi
    
    cd ..
}

# Function to check Kubernetes service health
check_health_kubernetes() {
    echo -e "${BLUE}🏥 Checking service health...${NC}"
    
    # Check pod status
    echo -e "${YELLOW}Pod Status:${NC}"
    kubectl get pods -l app=living-codex
    
    # Check service status
    echo -e "${YELLOW}Service Status:${NC}"
    kubectl get services -l app=living-codex
    
    # Check deployment status
    echo -e "${YELLOW}Deployment Status:${NC}"
    kubectl get deployments -l app=living-codex
}

# Function to display ecosystem information
display_ecosystem_info() {
    echo -e "${CYAN}🌊 Living Codex Ecosystem Information${NC}"
    echo -e "${BLUE}=====================================${NC}"
    
    if [ "$DEPLOYMENT_TYPE" = "docker" ]; then
        echo -e "🌐 Web Interface: ${YELLOW}http://localhost:5001${NC}"
        echo -e "🔌 API Service: ${YELLOW}http://localhost:5002${NC}"
        echo -e "☁️ Interaction: ${YELLOW}http://localhost:5003${NC}"
        echo -e "⚡ Streaming: ${YELLOW}http://localhost:5004${NC}"
        echo -e "🔍 Discovery: ${YELLOW}http://localhost:8500${NC}"
        echo -e "📊 Monitoring: ${YELLOW}http://localhost:9090${NC}"
    else
        echo -e "🌐 Web Interface: ${YELLOW}http://localhost:80${NC}"
        echo -e "🔌 API Service: ${YELLOW}http://localhost:80/api${NC}"
        echo -e "☁️ Interaction: ${YELLOW}http://localhost:80/interaction${NC}"
        echo -e "⚡ Streaming: ${YELLOW}http://localhost:80/streaming${NC}"
    fi
    
    echo ""
    echo -e "${GREEN}🎉 Living Codex ecosystem deployed successfully!${NC}"
    echo -e "${CYAN}The system is now ready to serve the community with:${NC}"
    echo -e "  🧊 ICE: Bootstrap and system reconstruction"
    echo -e "  💧 WATER: Stable, operational services"
    echo -e "  ☁️ VAPOR: Temporary, contextual interactions"
    echo -e "  ⚡ PLASMA: Real-time, collaborative streaming"
}

# Function to cleanup
cleanup() {
    echo -e "${YELLOW}🧹 Cleaning up temporary files...${NC}"
    
    if [ "$DEPLOYMENT_TYPE" = "docker" ]; then
        echo -e "${GREEN}✅ Docker deployment cleanup completed${NC}"
    else
        cd docker/k8s
        rm -f living-codex-deployment.yaml.bak
        cd ../..
        echo -e "${GREEN}✅ Kubernetes deployment cleanup completed${NC}"
    fi
}

# Main deployment flow
main() {
    echo -e "${PURPLE}🚀 Starting Living Codex deployment...${NC}"
    
    # Check prerequisites
    check_prerequisites
    
    # Build images
    build_images
    
    # Deploy based on type
    if [ "$DEPLOYMENT_TYPE" = "docker" ]; then
        deploy_docker
    else
        deploy_kubernetes
    fi
    
    # Display ecosystem information
    display_ecosystem_info
    
    # Cleanup
    cleanup
    
    echo -e "${GREEN}🎉 Deployment completed successfully!${NC}"
}

# Handle script interruption
trap 'echo -e "\n${RED}❌ Deployment interrupted${NC}"; cleanup; exit 1' INT TERM

# Run main function
main "$@"
