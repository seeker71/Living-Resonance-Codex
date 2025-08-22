#!/bin/bash

# Living Codex macOS Setup Script
# This script helps set up Neo4j and configure the system on macOS

echo "🚀 Living Codex macOS Setup Script"
echo "=================================="
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo "✅ Homebrew installed successfully!"
else
    echo "✅ Homebrew is already installed"
fi

echo ""
echo "🔧 Installing Neo4j..."

# Install Neo4j
if ! brew list neo4j &> /dev/null; then
    brew install neo4j
    echo "✅ Neo4j installed successfully!"
else
    echo "✅ Neo4j is already installed"
fi

echo ""
echo "🗄️  Setting up Neo4j..."

# Check if Neo4j service is running
if brew services list | grep -q "neo4j.*started"; then
    echo "✅ Neo4j service is already running"
else
    echo "🔄 Starting Neo4j service..."
    brew services start neo4j
    echo "✅ Neo4j service started!"
fi

echo ""
echo "🔑 Setting up Neo4j password..."

# Check if password is already set
if ! grep -q "dbms.security.auth_enabled=false" /opt/homebrew/etc/neo4j/neo4j.conf 2>/dev/null; then
    echo "⚠️  Neo4j requires a password to be set"
    echo "   The default password is 'neo4j'"
    echo "   You'll be prompted to change it on first login"
    echo ""
    echo "💡 To set a custom password:"
    echo "   1. Stop Neo4j: brew services stop neo4j"
    echo "   2. Set password: neo4j-admin set-initial-password your_password"
    echo "   3. Start Neo4j: brew services start neo4j"
else
    echo "✅ Neo4j password already configured"
fi

echo ""
echo "🌐 Neo4j Browser will be available at: http://localhost:7474"
echo "   Username: neo4j"
echo "   Password: (the password you set)"

echo ""
echo "🔍 Checking Neo4j status..."

# Wait a moment for Neo4j to fully start
sleep 5

# Check if Neo4j is responding
if curl -s http://localhost:7474 > /dev/null; then
    echo "✅ Neo4j is running and accessible!"
else
    echo "⚠️  Neo4j might still be starting up..."
    echo "   Please wait a few more minutes and try again"
fi

echo ""
echo "📦 Installing Python dependencies..."

# Install Python dependencies
if [ -f "requirements_real_systems.txt" ]; then
    pip install -r requirements_real_systems.txt
    echo "✅ Python dependencies installed!"
else
    echo "⚠️  requirements_real_systems.txt not found"
    echo "   Please run: pip install neo4j psycopg2-binary requests aiohttp"
fi

echo ""
echo "🎉 Setup Complete!"
echo "=================="
echo ""
echo "Next steps:"
echo "1. Open Neo4j Browser: http://localhost:7474"
echo "2. Login with username 'neo4j' and your password"
echo "3. Run the setup wizard: python setup_api_keys.py"
echo "4. Test the system: python integrated_real_systems_demo.py"
echo ""
echo "Happy exploring! 🌟"
