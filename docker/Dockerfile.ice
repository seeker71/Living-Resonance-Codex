# 🧊 ICE Bootstrap Pod - Immutable, Self-Containing
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV ICE_POD_ID=ice-pod-001
ENV ICE_POD_STATE=ICE

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ICE bootstrap system
COPY src/core/ src/core/
COPY src/platform/ src/platform/
COPY src/ontology/ src/ontology/
COPY tests/ tests/
COPY docs/ docs/
COPY scripts/ scripts/

# Create ICE core storage
RUN mkdir -p /app/ice_core

# Create bootstrap script
RUN echo '#!/bin/bash\n\
echo "🧊 ICE Pod ${ICE_POD_ID} starting..."\n\
echo "State: ${ICE_POD_STATE}"\n\
echo "Ready to bootstrap Living Codex system..."\n\
\n\
# Start bootstrap process\n\
python src/core/minimal_ice_bootstrap.py\n\
\n\
# Keep pod running for discovery\n\
while true; do\n\
    echo "🧊 ICE Pod ${ICE_POD_ID} - State: ${ICE_POD_STATE}"\n\
    sleep 30\n\
done' > /app/start_ice.sh && chmod +x /app/start_ice.sh

# Expose ports
EXPOSE 5000 5001 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Start ICE bootstrap
CMD ["/app/start_ice.sh"]
