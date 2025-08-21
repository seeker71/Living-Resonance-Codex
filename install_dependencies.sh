#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "========================================"
echo "Living Resonance Codex - macOS Installer"
echo "========================================"
echo ""
echo -e "${BLUE}Note: This script will install dependencies using Homebrew and official installers${NC}"
echo ""

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Check if running as root (not recommended for macOS)
if [[ $EUID -eq 0 ]]; then
    print_status $RED "ERROR: This script should NOT be run as root on macOS"
    print_status $RED "Please run without sudo"
    exit 1
fi

print_status $BLUE "Starting dependency installation..."
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    print_status $YELLOW "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to PATH for current session
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        export PATH="/opt/homebrew/bin:$PATH"
    elif [[ -f "/usr/local/bin/brew" ]]; then
        export PATH="/usr/local/bin:$PATH"
    fi
    
    # Verify Homebrew installation
    if command -v brew &> /dev/null; then
        print_status $GREEN "Homebrew installed successfully"
    else
        print_status $RED "Failed to install Homebrew"
        print_status $YELLOW "Please install manually from https://brew.sh"
        exit 1
    fi
else
    print_status $GREEN "Homebrew is already installed"
fi

# Install Python
echo ""
print_status $YELLOW "Installing Python..."
if ! command -v python3 &> /dev/null; then
    brew install python@3.12
    if command -v python3 &> /dev/null; then
        print_status $GREEN "Python installed successfully"
    else
        print_status $RED "Failed to install Python"
        exit 1
    fi
else
    print_status $GREEN "Python is already installed"
fi

# Install Node.js
echo ""
print_status $YELLOW "Installing Node.js..."
if ! command -v node &> /dev/null; then
    brew install node@20
    if command -v node &> /dev/null; then
        print_status $GREEN "Node.js installed successfully"
    else
        print_status $RED "Failed to install Node.js"
        exit 1
    fi
else
    print_status $GREEN "Node.js is already installed"
fi

# Install Rust via rustup
echo ""
print_status $YELLOW "Installing Rust via rustup..."
print_status $YELLOW "Checking for existing Rust installations..."

# Check if Rust is already installed
if [[ -d "$HOME/.cargo" ]] || [[ -d "$HOME/.rustup" ]]; then
    print_status $YELLOW "Rust installation detected. Checking if it's working..."
    if command -v rustc &> /dev/null; then
        print_status $GREEN "Existing Rust installation is working"
    else
        print_status $RED "Existing Rust installation is broken. Please remove ~/.cargo and ~/.rustup directories"
        print_status $YELLOW "Then restart your terminal before running this script"
        exit 1
    fi
else
    print_status $YELLOW "No existing Rust installation found. Installing via rustup..."
    
    # Download and install rustup
    print_status $YELLOW "Installing Rust via rustup..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain stable --profile default -y
    
    if [[ $? -eq 0 ]]; then
        print_status $GREEN "Rust installed successfully via rustup!"
        
        # Source cargo environment for current session
        source "$HOME/.cargo/env"
        
        # Verify installation
        print_status $YELLOW "Verifying Rust installation..."
        rustup --version
        cargo --version
        rustc --version
        
        print_status $GREEN "Rust installation completed successfully!"
    else
        print_status $RED "Rust installation failed"
        print_status $RED "Please check the error messages above"
        exit 1
    fi
fi

# Install Git (if not already installed)
echo ""
print_status $YELLOW "Checking for Git..."
if ! command -v git &> /dev/null; then
    print_status $YELLOW "Installing Git..."
    brew install git
    if command -v git &> /dev/null; then
        print_status $GREEN "Git installed successfully"
    else
        print_status $RED "Failed to install Git"
        exit 1
    fi
else
    print_status $GREEN "Git is already installed"
fi

# Verify installations
echo ""
print_status $BLUE "Verifying installations..."
echo ""

# Check Python
if command -v python3 &> /dev/null; then
    print_status $GREEN "✓ Python:"
    python3 --version
else
    print_status $RED "✗ Python not found"
fi

# Check pip
if command -v pip3 &> /dev/null; then
    print_status $GREEN "✓ pip:"
    pip3 --version
else
    print_status $RED "✗ pip not found"
fi

# Check Node.js
if command -v node &> /dev/null; then
    print_status $GREEN "✓ Node.js:"
    node --version
else
    print_status $RED "✗ Node.js not found"
fi

# Check npm
if command -v npm &> /dev/null; then
    print_status $GREEN "✓ npm:"
    npm --version
else
    print_status $RED "✗ npm not found"
fi

# Check Rust
if command -v rustc &> /dev/null; then
    print_status $GREEN "✓ Rust:"
    rustc --version
else
    print_status $RED "✗ Rust not found"
fi

# Check Cargo
if command -v cargo &> /dev/null; then
    print_status $GREEN "✓ Cargo:"
    cargo --version
else
    print_status $RED "✗ Cargo not found"
fi

# Install Python dependencies
echo ""
print_status $BLUE "Installing Python dependencies..."
echo ""

# Federation Python dependencies
if [[ -f "prototypes/federation-python/requirements.txt" ]]; then
    print_status $YELLOW "Installing federation-python dependencies..."
    cd prototypes/federation-python
    pip3 install -r requirements.txt
    if [[ $? -eq 0 ]]; then
        print_status $GREEN "federation-python dependencies installed successfully"
    else
        print_status $RED "Failed to install federation-python dependencies"
    fi
    cd ../..
else
    print_status $YELLOW "federation-python requirements.txt not found"
fi

# Graph dependencies
if [[ -f "prototypes/graph/requirements.txt" ]]; then
    print_status $YELLOW "Installing graph dependencies..."
    cd prototypes/graph
    pip3 install -r requirements.txt
    if [[ $? -eq 0 ]]; then
        print_status $GREEN "graph dependencies installed successfully"
    else
        print_status $RED "Failed to install graph dependencies"
    fi
    cd ../..
else
    print_status $YELLOW "graph requirements.txt not found"
fi

# Install Node.js dependencies
echo ""
print_status $BLUE "Installing Node.js dependencies..."
echo ""

# Viz dependencies
if [[ -f "prototypes/viz/package.json" ]]; then
    print_status $YELLOW "Installing viz dependencies..."
    cd prototypes/viz
    npm install
    if [[ $? -eq 0 ]]; then
        print_status $GREEN "viz dependencies installed successfully"
    else
        print_status $RED "Failed to install viz dependencies"
    fi
    cd ../..
else
    print_status $YELLOW "viz package.json not found"
fi

# Build Rust dependencies
echo ""
print_status $BLUE "Building Rust dependencies..."
echo ""

# Ensure Cargo bin is in PATH for Rust builds
if [[ ":$PATH:" != *":$HOME/.cargo/bin:"* ]]; then
    export PATH="$HOME/.cargo/bin:$PATH"
fi

if [[ -f "prototypes/federation-rust/Cargo.toml" ]]; then
    print_status $YELLOW "Building federation-rust..."
    cd prototypes/federation-rust
    cargo build
    if [[ $? -eq 0 ]]; then
        print_status $GREEN "federation-rust built successfully"
    else
        print_status $RED "Failed to build federation-rust"
        print_status $YELLOW "This may indicate a toolchain issue"
    fi
    cd ../..
else
    print_status $YELLOW "federation-rust Cargo.toml not found"
fi

# Test installations
echo ""
print_status $BLUE "Testing installations..."
echo ""

# Test Python
print_status $YELLOW "Testing Python..."
python3 -c "print('Python is working!')"
if [[ $? -eq 0 ]]; then
    print_status $GREEN "✓ Python test passed"
else
    print_status $RED "✗ Python test failed"
fi

# Test Node.js
print_status $YELLOW "Testing Node.js..."
node -e "console.log('Node.js is working!')"
if [[ $? -eq 0 ]]; then
    print_status $GREEN "✓ Node.js test passed"
else
    print_status $RED "✗ Node.js test failed"
fi

# Test Rust
print_status $YELLOW "Testing Rust..."
rustc --version
if [[ $? -eq 0 ]]; then
    print_status $GREEN "✓ Rust test passed"
else
    print_status $RED "✗ Rust test failed"
fi

echo ""
print_status $GREEN "========================================"
print_status $GREEN "Installation completed!"
print_status $GREEN "========================================"
echo ""
print_status $BLUE "Next steps:"
echo "1. Restart your terminal to ensure all PATH variables are loaded"
echo "2. Navigate to any prototype directory and run the appropriate commands:"
echo "   - Python: python3 script.py"
echo "   - Node.js: npm start"
echo "   - Rust: cargo run"
echo ""
print_status $YELLOW "Press Enter to exit..."
read
