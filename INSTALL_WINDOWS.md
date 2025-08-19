# Windows Installation Guide

This guide will help you install all the necessary dependencies for the Living Resonance Codex prototypes on Windows.

## Prerequisites

- Windows 10 or later
- Administrator privileges (required for installing software)
- Internet connection

## Installation Options

We provide the following installation script:

### Batch Script
- **File**: `install_dependencies.bat`
- **Usage**: Right-click and "Run as Administrator"

## What Gets Installed

### Core Tools
- **Chocolatey**: Package manager for Windows
- **Python**: Latest stable version with pip
- **Node.js**: Latest LTS version with npm
- **Rust**: Latest stable version with Cargo
- **Git**: Version control system

### Prototype Dependencies

#### Python Prototypes
- **federation-python**: FastAPI, Uvicorn, Pydantic, and other web framework dependencies
- **graph**: Neo4j driver, NetworkX, Matplotlib, NumPy, Pandas, and other graph processing libraries
- **resonance**: Basic Python dependencies (included with Python installation)

#### Node.js Prototypes
- **federation**: Basic Node.js server dependencies
- **viz**: Three.js, Vite, and visualization dependencies

#### Rust Prototypes
- **federation-rust**: Tokio, Axum, Serde, and other async web framework dependencies

## Installation Steps

### Method 1: PowerShell (Recommended)

1. **Right-click** on `install_dependencies.ps1`
2. Select **"Run as administrator"**
3. If prompted about execution policy, type `Y` and press Enter
4. Wait for the installation to complete
5. Restart your terminal/PowerShell

### Method 2: Batch File

1. **Right-click** on `install_dependencies.bat`
2. Select **"Run as administrator"**
3. Wait for the installation to complete
4. Restart your command prompt

### Method 3: Command Line

#### PowerShell (as Administrator):
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
.\install_dependencies.ps1
```

#### Command Prompt (as Administrator):
```cmd
install_dependencies.bat
```

## Advanced Usage

The PowerShell script supports command-line parameters:

```powershell
# Skip installing Chocolatey (if already installed)
.\install_dependencies.ps1 -SkipChocolatey

# Skip installing Python (if already installed)
.\install_dependencies.ps1 -SkipPython

# Skip installing Node.js (if already installed)
.\install_dependencies.ps1 -SkipNode

# Skip installing Rust (if already installed)
.\install_dependencies.ps1 -SkipRust

# Skip installing all dependencies (only install core tools)
.\install_dependencies.ps1 -SkipDependencies

# Combine multiple options
.\install_dependencies.ps1 -SkipChocolatey -SkipPython
```

## Verification

After installation, the script will:

1. **Verify** all tools are properly installed
2. **Install** all prototype dependencies
3. **Test** basic functionality
4. **Report** success/failure for each component

## Troubleshooting

### Common Issues

1. **"Access Denied" errors**
   - Ensure you're running as Administrator
   - Right-click the script and select "Run as administrator"

2. **Execution Policy errors (PowerShell)**
   - The script automatically sets execution policy for the session
   - If issues persist, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

3. **Chocolatey installation fails**
   - Check internet connection
   - Ensure Windows Defender/antivirus isn't blocking the download
   - Try running the PowerShell installation command manually

4. **Python/pip not found after installation**
   - Restart your terminal/PowerShell
   - Check if Python is in your PATH: `echo $env:PATH`
   - Manually add Python to PATH if needed

5. **Node.js/npm not found after installation**
   - Restart your terminal/PowerShell
   - Check if Node.js is in your PATH: `echo $env:PATH`
   - Manually add Node.js to PATH if needed

### Manual Installation

If the automated script fails, you can install tools manually:

1. **Python**: Download from [python.org](https://python.org)
2. **Node.js**: Download from [nodejs.org](https://nodejs.org)
3. **Rust**: Download from [rustup.rs](https://rustup.rs)
4. **Git**: Download from [git-scm.com](https://git-scm.com)

## Post-Installation

After successful installation:

1. **Restart** your terminal/PowerShell
2. **Navigate** to any prototype directory
3. **Run** the appropriate commands:

```bash
# Python prototypes
cd prototypes/federation-python
python fractal_server.py

cd prototypes/graph
python loader.py

cd prototypes/resonance
python score.py

# Node.js prototypes
cd prototypes/federation
npm start

cd prototypes/viz
npm run dev

# Rust prototypes
cd prototypes/federation-rust
cargo run
```

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all prerequisites are met
3. Run the script with verbose output
4. Check Windows Event Viewer for system errors
5. Verify your antivirus isn't blocking installations

## Notes

- The script automatically handles PATH environment variables
- All installations use the latest stable versions
- Dependencies are installed globally (system-wide)
- The script is idempotent - running it multiple times is safe
- Chocolatey packages are automatically updated if newer versions exist
