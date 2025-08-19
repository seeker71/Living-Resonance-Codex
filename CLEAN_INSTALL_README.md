# Living Resonance Codex - Clean Installation Guide

This guide explains how to completely remove existing Rust installations and perform a clean installation using the official rustup method.

## 🧹 **Cleanup Scripts**

### **Option 1: Batch Script (Recommended for most users)**
- **File**: `cleanup_rust_chocolatey.bat`
- **Usage**: Right-click → "Run as administrator"
- **What it does**:
  - Stops all running Rust processes
  - Removes rustup installation (`%USERPROFILE%\.cargo`, `%USERPROFILE%\.rustup`)
  - Removes Chocolatey Rust installation (`C:\ProgramData\chocolatey\bin\cargo.exe`, etc.)
  - Removes Chocolatey completely
  - Cleans up PATH environment variables
  - Verifies complete removal

### **Option 2: PowerShell Script**
- **File**: `cleanup_rust_chocolatey.ps1`
- **Usage**: Right-click → "Run as administrator"
- **Same functionality** as the batch script but in PowerShell

## 🚀 **Installation Scripts**

### **Option 1: Original Install Script (Updated)**
- **File**: `install_dependencies.bat`
- **Usage**: Run as Administrator
- **What it does**:
  - Installs Chocolatey package manager
  - Installs Python via Chocolatey
  - Installs Node.js via Chocolatey
  - **Installs Rust via rustup** (MSVC toolchain)
  - Installs Git via Chocolatey
  - Installs all prototype dependencies
  - Builds and tests all prototypes

### **Option 2: Clean Install Script**
- **File**: `install_dependencies_clean.bat`
- **Usage**: Run normally (administrator recommended)
- **What it does**:
  - Installs Python 3.12 (if not present)
  - Installs Node.js LTS (if not present)
  - Installs Rust via rustup with MSVC toolchain
  - Installs all Python dependencies
  - Installs all Node.js dependencies
  - Builds the Rust prototype
  - Provides comprehensive verification

### **Option 3: PowerShell Script**
- **File**: `install_dependencies_clean.ps1`
- **Usage**: Run normally (administrator recommended)
- **Same functionality** as the clean batch script but in PowerShell

## 📋 **Step-by-Step Process**

### **Step 1: Clean Up Existing Installations**
1. **Close all terminals/command prompts**
2. **Right-click** on `cleanup_rust_chocolatey.bat` (or `.ps1`)
3. Select **"Run as administrator"**
4. Wait for the cleanup to complete
5. **Restart your computer** (important for PATH changes)

### **Step 2: Clean Installation**
1. **Open a new terminal** (doesn't need to be admin)
2. **Navigate** to your project directory
3. **Choose your installation method**:
   - **Option A**: Run `install_dependencies.bat` as Administrator (uses Chocolatey + rustup)
   - **Option B**: Run `install_dependencies_clean.bat` (clean install via rustup only)
4. Wait for all installations to complete
5. **Restart your terminal** to ensure PATH is loaded

### **Step 3: Verify Installation**
The install script will automatically verify:
- ✅ Python and pip
- ✅ Node.js and npm
- ✅ Rust (rustup), Cargo, and rustc
- ✅ All prototype dependencies
- ✅ Rust prototype compilation

## 🔧 **What Gets Installed**

### **Python**
- **Version**: 3.12.3 (latest stable)
- **Source**: Official Python installer
- **Features**: pip, PATH integration

### **Node.js**
- **Version**: 20.11.1 LTS (latest LTS)
- **Source**: Official Node.js installer
- **Features**: npm, PATH integration

### **Rust**
- **Method**: rustup (official Rust toolchain manager)
- **Toolchain**: stable-msvc (Microsoft Visual C++ backend)
- **Components**: rustc, cargo, rustup
- **Location**: `%USERPROFILE%\.cargo\bin`

### **Dependencies**
- **Python**: FastAPI, Uvicorn, Neo4j, NetworkX, etc.
- **Node.js**: Three.js, Vite, server dependencies
- **Rust**: Tokio, Axum, Serde, Tower, etc.

## ⚠️ **Important Notes**

### **Why Clean Installation?**
- **Avoids conflicts** between Chocolatey and rustup
- **MSVC toolchain** is more reliable on Windows
- **Proper PATH management** prevents confusion
- **Official rustup** is the recommended Rust installation method

### **Prerequisites**
- **Windows 10/11** (64-bit)
- **Internet connection** for downloads
- **Administrator access** for cleanup (optional for install)

### **Troubleshooting**
- **If cleanup fails**: Some files may be locked; restart and try again
- **If install fails**: Check error messages and ensure no existing Rust installation
- **PATH issues**: Always restart terminal after installation

## 🎯 **Expected Results**

After successful installation:
- **Python**: `python --version` shows 3.12.3
- **Node.js**: `node --version` shows v20.11.1
- **Rust**: `rustc --version` shows 1.89.0 or newer
- **All prototypes**: Can compile and run successfully

## 🔄 **Alternative: Manual Installation**

If scripts fail, you can install manually:
1. **Python**: Download from https://python.org
2. **Node.js**: Download from https://nodejs.org
3. **Rust**: Run `winget install Rust.Rust` or download from https://rustup.rs

## 📞 **Support**

If you encounter issues:
1. Check the error messages in the scripts
2. Ensure you're running cleanup as administrator
3. Restart your computer after cleanup
4. Check that no existing Rust installation remains

---

**Remember**: The key is to completely remove existing Rust installations before installing via rustup. This prevents toolchain conflicts and ensures a stable development environment.
