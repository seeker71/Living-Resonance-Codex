@echo off
REM ============================================================================
REM Living Resonance Codex - Windows Clean Install Script
REM This script installs dependencies without Chocolatey conflicts
REM Run as Administrator for best results
REM ============================================================================

setlocal enabledelayedexpansion

echo ========================================
echo Living Resonance Codex - Clean Installer
echo ========================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo WARNING: Not running as Administrator
    echo Some installations may fail due to permissions
    echo.
)

echo Starting clean dependency installation...
echo.

REM Step 1: Install Python (if not present)
echo Step 1: Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo Python not found. Installing Python...
    echo Downloading Python installer...
    
    REM Download Python 3.12 (latest stable)
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python-installer.exe'"
    
    if exist "python-installer.exe" (
        echo Installing Python...
        python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        del python-installer.exe
        
        REM Refresh PATH
        call refreshenv.cmd 2>nul
        if not exist "refreshenv.cmd" (
            echo Refreshing PATH manually...
            set "PATH=%PATH%;C:\Python312;C:\Python312\Scripts"
        )
    ) else (
        echo Failed to download Python installer
        echo Please install Python manually from https://python.org
    )
) else (
    echo Python is already installed
)

REM Step 2: Install Node.js (if not present)
echo.
echo Step 2: Checking Node.js installation...
node --version >nul 2>&1
if %errorLevel% neq 0 (
    echo Node.js not found. Installing Node.js...
    echo Downloading Node.js installer...
    
    REM Download Node.js LTS
    powershell -Command "Invoke-WebRequest -Uri 'https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi' -OutFile 'nodejs-installer.msi'"
    
    if exist "nodejs-installer.msi" (
        echo Installing Node.js...
        msiexec /i nodejs-installer.msi /quiet /norestart
        del nodejs-installer.msi
        
        REM Refresh PATH
        call refreshenv.cmd 2>nul
        if not exist "refreshenv.cmd" (
            echo Refreshing PATH manually...
            set "PATH=%PATH%;C:\Program Files\nodejs"
        )
    ) else (
        echo Failed to download Node.js installer
        echo Please install Node.js manually from https://nodejs.org
    )
) else (
    echo Node.js is already installed
)

REM Step 3: Install Rust via rustup (clean installation)
echo.
echo Step 3: Installing Rust via rustup...
echo Checking for existing Rust installations...

set "RUST_EXISTS="
if exist "%USERPROFILE%\.cargo" set "RUST_EXISTS=1"
if exist "%USERPROFILE%\.rustup" set "RUST_EXISTS=1"
if exist "C:\ProgramData\chocolatey\bin\cargo.exe" set "RUST_EXISTS=1"

if defined RUST_EXISTS (
    echo WARNING: Rust installation detected!
    echo Please run cleanup_rust_chocolatey.bat as Administrator first
    echo Then restart your computer before running this script
    echo.
    pause
    exit /b 1
)

echo No existing Rust installation found. Proceeding with rustup...
echo Downloading rustup installer...

REM Download rustup
powershell -Command "Invoke-WebRequest -Uri 'https://win.rustup.rs/x86_64' -OutFile 'rustup-init.exe'"

if exist "rustup-init.exe" (
    echo Installing Rust via rustup...
    echo This will install the MSVC toolchain (recommended for Windows)
    
    REM Install with MSVC toolchain
    rustup-init.exe --default-toolchain stable-msvc --profile default -y
    
    if %errorLevel% equ 0 (
        echo Rust installed successfully!
        
        REM Add Cargo bin to PATH for current session
        set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
        
        REM Verify installation
        echo Verifying Rust installation...
        rustup --version
        cargo --version
        rustc --version
        
        echo.
        echo Rust installation completed successfully!
    ) else (
        echo Rust installation failed
        echo Please check the error messages above
    )
    
    REM Clean up installer
    del rustup-init.exe
) else (
    echo Failed to download rustup installer
    echo Please install Rust manually from https://rustup.rs
)

REM Step 4: Install Python dependencies
echo.
echo Step 4: Installing Python dependencies...

REM Ensure pip is available
python -m ensurepip --user --upgrade

REM Install federation-python dependencies
if exist "prototypes\federation-python\requirements.txt" (
    echo Installing federation-python dependencies...
    cd prototypes\federation-python
    python -m pip install --user -r requirements.txt
    cd ..\..
)

REM Install graph dependencies
if exist "prototypes\graph\requirements.txt" (
    echo Installing graph dependencies...
    cd prototypes\graph
    python -m pip install --user -r requirements.txt
    cd ..\..
)

REM Step 5: Install Node.js dependencies
echo.
echo Step 5: Installing Node.js dependencies...

REM Install federation Node.js dependencies
if exist "prototypes\federation\package.json" (
    echo Installing federation Node.js dependencies...
    cd prototypes\federation
    npm install
    cd ..\..
)

REM Install viz dependencies
if exist "prototypes\viz\package.json" (
    echo Installing viz dependencies...
    cd prototypes\viz
    npm install
    cd ..\..
)

REM Step 6: Build Rust prototype
echo.
echo Step 6: Building Rust prototype...

REM Add Cargo bin to PATH if not already there
if not "%PATH%" == "%PATH%;%USERPROFILE%\.cargo\bin" (
    set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
)

if exist "prototypes\federation-rust\Cargo.toml" (
    echo Building federation-rust...
    cd prototypes\federation-rust
    cargo build
    
    if %errorLevel% equ 0 (
        echo Rust prototype built successfully!
    ) else (
        echo Rust prototype build failed
        echo This may indicate a toolchain issue
    )
    
    cd ..\..
)

REM Step 7: Final verification
echo.
echo ========================================
echo Installation Summary
echo ========================================
echo.

echo Checking installed tools:
echo.

REM Check Python
python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo ✓ Python: 
    python --version
) else (
    echo ✗ Python not found
)

REM Check pip
python -m pip --version >nul 2>&1
if %errorLevel% equ 0 (
    echo ✓ pip: 
    python -m pip --version
) else (
    echo ✗ pip not found
)

REM Check Node.js
node --version >nul 2>&1
if %errorLevel% equ 0 (
    echo ✓ Node.js: 
    node --version
) else (
    echo ✗ Node.js not found
)

REM Check npm
npm --version >nul 2>&1
if %errorLevel% equ 0 (
    echo ✓ npm: 
    npm --version
) else (
    echo ✗ npm not found
)

REM Check Rust (only if rustup was used)
if exist "%USERPROFILE%\.cargo\bin\cargo.exe" (
    echo ✓ Rust (rustup): 
    cargo --version
) else (
    echo ✗ Rust not found
)

echo.
echo ========================================
echo Installation completed!
echo ========================================
echo.
echo Next steps:
echo 1. Restart your terminal to ensure all PATH variables are loaded
echo 2. Test the prototypes:
echo    - Python: cd prototypes\federation-python && python fractal_server.py
echo    - Node.js: cd prototypes\federation && npm start
echo    - Rust: cd prototypes\federation-rust && cargo run
echo.
echo If you encounter any issues, check the error messages above
echo.
pause
