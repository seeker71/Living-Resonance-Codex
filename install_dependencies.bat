@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Living Resonance Codex - Windows Installer
echo ========================================
echo.
echo %BLUE%Note: This script now uses rustup for Rust installation%RESET%
echo %BLUE%If you have existing Rust installations, consider running%RESET%
echo %BLUE%cleanup_rust_chocolatey.bat first for a clean setup%RESET%
echo.

:: Check if running as administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: This script must be run as Administrator
    echo Right-click on the script and select "Run as administrator"
    pause
    exit /b 1
)

:: Set colors for output
set "GREEN=[92m"
set "YELLOW=[93m"
set "RED=[91m"
set "BLUE=[94m"
set "RESET=[0m"

echo %BLUE%Starting dependency installation...%RESET%
echo.

:: Install Python
echo.
echo %YELLOW%Installing Python...%RESET%
where python >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%Downloading Python installer...%RESET%
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python-installer.exe'"
    if exist "python-installer.exe" (
        echo %YELLOW%Installing Python...%RESET%
        start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        del python-installer.exe
        echo %GREEN%Python installed successfully%RESET%
    ) else (
        echo %RED%Failed to download Python installer%RESET%
        pause
        exit /b 1
    )
) else (
    echo %GREEN%Python is already installed%RESET%
)

:: Install Node.js
echo.
echo %YELLOW%Installing Node.js...%RESET%
where node >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%Downloading Node.js installer...%RESET%
    powershell -Command "Invoke-WebRequest -Uri 'https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi' -OutFile 'nodejs-installer.msi'"
    if exist "nodejs-installer.msi" (
        echo %YELLOW%Installing Node.js...%RESET%
        start /wait msiexec /i nodejs-installer.msi /quiet /norestart
        del nodejs-installer.msi
        echo %GREEN%Node.js installed successfully%RESET%
    ) else (
        echo %RED%Failed to download Node.js installer%RESET%
        pause
        exit /b 1
    )
) else (
    echo %GREEN%Node.js is already installed%RESET%
)

:: Install Rust via rustup
echo.
echo %YELLOW%Installing Rust via rustup...%RESET%
echo %YELLOW%Checking for existing Rust installations...%RESET%

:: Check if Rust is already installed
set "RUST_EXISTS="
if exist "%USERPROFILE%\.cargo" set "RUST_EXISTS=1"
if exist "%USERPROFILE%\.rustup" set "RUST_EXISTS=1"

if defined RUST_EXISTS (
    echo %YELLOW%Rust installation detected. Checking if it's working...%RESET%
    rustc --version >nul 2>&1
    if %errorLevel% equ 0 (
        echo %GREEN%Existing Rust installation is working%RESET%
    ) else (
        echo %RED%Existing Rust installation is broken. Please run cleanup_rust_chocolatey.bat first%RESET%
        echo %YELLOW%Then restart your computer before running this script%RESET%
        pause
        exit /b 1
    )
) else (
    echo %YELLOW%No existing Rust installation found. Installing via rustup...%RESET%
    
    :: Download rustup installer
    echo %YELLOW%Downloading rustup installer...%RESET%
    powershell -Command "Invoke-WebRequest -Uri 'https://win.rustup.rs/x86_64' -OutFile 'rustup-init.exe'"
    
    if exist "rustup-init.exe" (
        echo %YELLOW%Installing Rust via rustup with MSVC toolchain...%RESET%
        rustup-init.exe --default-toolchain stable-msvc --profile default -y
        
        if %errorLevel% equ 0 (
            echo %GREEN%Rust installed successfully via rustup!%RESET%
            
            :: Add Cargo bin to PATH for current session
            set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
            
            :: Verify installation
            echo %YELLOW%Verifying Rust installation...%RESET%
            rustup --version
            cargo --version
            rustc --version
            
            echo %GREEN%Rust installation completed successfully!%RESET%
        ) else (
            echo %RED%Rust installation failed%RESET%
            echo %RED%Please check the error messages above%RESET%
            pause
            exit /b 1
        )
        
        :: Clean up installer
        del rustup-init.exe
    ) else (
        echo %RED%Failed to download rustup installer%RESET%
        echo %RED%Please install Rust manually from https://rustup.rs%RESET%
        pause
        exit /b 1
    )
)

:: Install Git (if not already installed)
echo.
echo %YELLOW%Checking for Git...%RESET%
where git >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%Downloading Git installer...%RESET%
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe' -OutFile 'git-installer.exe'"
    if exist "git-installer.exe" (
        echo %YELLOW%Installing Git...%RESET%
        start /wait git-installer.exe /VERYSILENT /NORESTART
        del git-installer.exe
        echo %GREEN%Git installed successfully%RESET%
    ) else (
        echo %RED%Failed to download Git installer%RESET%
        pause
        exit /b 1
    )
) else (
    echo %GREEN%Git is already installed%RESET%
)

:: Refresh environment variables
set "PATH=%PATH%;C:\Python312;C:\Python312\Scripts;C:\Program Files\nodejs"

:: Verify installations
echo.
echo %BLUE%Verifying installations...%RESET%
echo.

:: Check Python
python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo %GREEN%✓ Python: %RESET%
    python --version
) else (
    echo %RED%✗ Python not found%RESET%
)

:: Check pip
pip --version >nul 2>&1
if %errorLevel% equ 0 (
    echo %GREEN%✓ pip: %RESET%
    pip --version
) else (
    echo %RED%✗ pip not found%RESET%
)

:: Check Node.js
node --version >nul 2>&1
if %errorLevel% equ 0 (
    echo %GREEN%✓ Node.js: %RESET%
    node --version
) else (
    echo %RED%✗ Node.js not found%RESET%
)

:: Check npm
npm --version >nul 2>&1
if %errorLevel% equ 0 (
    echo %GREEN%✓ npm: %RESET%
    npm --version
) else (
    echo %RED%✗ npm not found%RESET%
)

:: Check Rust
rustc --version >nul 2>&1
if %errorLevel% equ 0 (
    echo %GREEN%✓ Rust: %RESET%
    rustc --version
) else (
    echo %RED%✗ Rust not found%RESET%
)

:: Check Cargo
cargo --version >nul 2>&1
if %errorLevel% equ 0 (
    echo %GREEN%✓ Cargo: %RESET%
    cargo --version
) else (
    echo %RED%✗ Cargo not found%RESET%
)

:: Install Python dependencies
echo.
echo %BLUE%Installing Python dependencies...%RESET%
echo.

:: Federation Python dependencies
if exist "prototypes\federation-python\requirements.txt" (
    echo %YELLOW%Installing federation-python dependencies...%RESET%
    cd prototypes\federation-python
    pip install -r requirements.txt
    if %errorLevel% neq 0 (
        echo %RED%Failed to install federation-python dependencies%RESET%
    ) else (
        echo %GREEN%federation-python dependencies installed successfully%RESET%
    )
    cd ..\..
) else (
    echo %YELLOW%federation-python requirements.txt not found%RESET%
)

:: Graph dependencies
if exist "prototypes\graph\requirements.txt" (
    echo %YELLOW%Installing graph dependencies...%RESET%
    cd prototypes\graph
    pip install -r requirements.txt
    if %errorLevel% neq 0 (
        echo %RED%Failed to install graph dependencies%RESET%
    ) else (
        echo %GREEN%graph dependencies installed successfully%RESET%
    )
    cd ..\..
) else (
    echo %YELLOW%graph requirements.txt not found%RESET%
)

:: Install Node.js dependencies
echo.
echo %BLUE%Installing Node.js dependencies...%RESET%
echo.

:: (Removed) Phase 4 Node federation prototype dependencies
:: The old Node federation prototype has been removed. Viz now targets the Phase 5 Python server.

:: Viz dependencies
if exist "prototypes\viz\package.json" (
    echo %YELLOW%Installing viz dependencies...%RESET%
    cd prototypes\viz
    npm install
    if %errorLevel% neq 0 (
        echo %RED%Failed to install viz dependencies%RESET%
    ) else (
        echo %GREEN%viz dependencies installed successfully%RESET%
    )
    cd ..\..
) else (
    echo %YELLOW%viz package.json not found%RESET%
)

:: Build Rust dependencies
echo.
echo %BLUE%Building Rust dependencies...%RESET%
echo.

:: Ensure Cargo bin is in PATH for Rust builds
if not "%PATH%" == "%PATH%;%USERPROFILE%\.cargo\bin" (
    set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
)

if exist "prototypes\federation-rust\Cargo.toml" (
    echo %YELLOW%Building federation-rust...%RESET%
    cd prototypes\federation-rust
    cargo build
    if %errorLevel% neq 0 (
        echo %RED%Failed to build federation-rust%RESET%
        echo %YELLOW%This may indicate a toolchain issue%RESET%
    ) else (
        echo %GREEN%federation-rust built successfully%RESET%
    )
    cd ..\..
) else (
    echo %YELLOW%federation-rust Cargo.toml not found%RESET%
)

:: Test installations
echo.
echo %BLUE%Testing installations...%RESET%
echo.

:: Test Python
echo %YELLOW%Testing Python...%RESET%
python -c "print('Python is working!')"
if %errorLevel% equ 0 (
    echo %GREEN%✓ Python test passed%RESET%
) else (
    echo %RED%✗ Python test failed%RESET%
)

:: Test Node.js
echo %YELLOW%Testing Node.js...%RESET%
node -e "console.log('Node.js is working!')"
if %errorLevel% equ 0 (
    echo %GREEN%✓ Node.js test passed%RESET%
) else (
    echo %RED%✗ Node.js test failed%RESET%
)

:: Test Rust
echo %YELLOW%Testing Rust...%RESET%
rustc --version
if %errorLevel% equ 0 (
    echo %GREEN%✓ Rust test passed%RESET%
) else (
    echo %RED%✗ Rust test failed%RESET%
)

echo.
echo %GREEN%========================================%RESET%
echo %GREEN%Installation completed!%RESET%
echo %GREEN%========================================%RESET%
echo.
echo %BLUE%Next steps:%RESET%
echo 1. Restart your terminal/command prompt to ensure all PATH variables are loaded
echo 2. Navigate to any prototype directory and run the appropriate commands:
echo    - Python: python script.py
echo    - Node.js: npm start
echo    - Rust: cargo run
echo.
echo %YELLOW%Press any key to exit...%RESET%
pause >nul
