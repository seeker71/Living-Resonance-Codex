@echo off
REM ============================================================================
REM Living Resonance Codex - Rust and Chocolatey Cleanup Script
REM Run this script as Administrator to completely remove Rust and Chocolatey
REM ============================================================================

echo ========================================
echo Living Resonance Codex - Cleanup Script
echo ========================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: This script must be run as Administrator
    echo Right-click on the script and select "Run as administrator"
    pause
    exit /b 1
)

echo Running as Administrator - proceeding with cleanup...
echo.

echo Step 1: Stopping any running Rust processes...
taskkill /f /im cargo.exe >nul 2>&1
taskkill /f /im rustc.exe >nul 2>&1
taskkill /f /im rustup.exe >nul 2>&1

echo Step 2: Removing rustup installation...
if exist "%USERPROFILE%\.cargo" (
    echo Removing %USERPROFILE%\.cargo...
    rmdir /s /q "%USERPROFILE%\.cargo" 2>nul
)

if exist "%USERPROFILE%\.rustup" (
    echo Removing %USERPROFILE%\.rustup...
    rmdir /s /q "%USERPROFILE%\.rustup" 2>nul
)

echo Step 3: Removing Chocolatey Rust installation...
if exist "C:\ProgramData\chocolatey\bin\cargo.exe" (
    echo Removing Cargo from Chocolatey...
    del /f /q "C:\ProgramData\chocolatey\bin\cargo.exe" 2>nul
)

if exist "C:\ProgramData\chocolatey\bin\rustc.exe" (
    echo Removing Rustc from Chocolatey...
    del /f /q "C:\ProgramData\chocolatey\bin\rustc.exe" 2>nul
)

if exist "C:\ProgramData\chocolatey\bin\rustup.exe" (
    echo Removing Rustup from Chocolatey...
    del /f /q "C:\ProgramData\chocolatey\bin\rustup.exe" 2>nul
)

if exist "C:\ProgramData\chocolatey\lib\rust" (
    echo Removing Rust library from Chocolatey...
    rmdir /s /q "C:\ProgramData\chocolatey\lib\rust" 2>nul
)

echo Step 4: Removing Chocolatey completely...
if exist "C:\ProgramData\chocolatey" (
    echo Removing Chocolatey installation...
    rmdir /s /q "C:\ProgramData\chocolatey" 2>nul
)

if exist "C:\ProgramData\chocolatey" (
    echo Chocolatey removal failed - may need manual cleanup
) else (
    echo Chocolatey removed successfully
)

echo Step 5: Cleaning up PATH environment variables...
echo Removing Rust-related paths from system PATH...

REM Get current PATH and remove Rust-related entries
for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path 2^>nul') do set "CURRENT_PATH=%%b"

REM Remove Rust-related paths
set "CLEAN_PATH=%CURRENT_PATH%"
set "CLEAN_PATH=%CLEAN_PATH:C:\ProgramData\chocolatey\bin;=%"
set "CLEAN_PATH=%CLEAN_PATH:;C:\ProgramData\chocolatey\bin=%"
set "CLEAN_PATH=%CLEAN_PATH:%USERPROFILE%\.cargo\bin;=%"
set "CLEAN_PATH=%CLEAN_PATH:;%USERPROFILE%\.cargo\bin=%"

REM Update system PATH
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /d "%CLEAN_PATH%" /f >nul 2>&1

echo Step 6: Final verification...
echo.
echo Checking for remaining Rust installations...

set "RUST_FOUND="
if exist "%USERPROFILE%\.cargo" set "RUST_FOUND=1"
if exist "%USERPROFILE%\.rustup" set "RUST_FOUND=1"
if exist "C:\ProgramData\chocolatey\bin\cargo.exe" set "RUST_FOUND=1"
if exist "C:\ProgramData\chocolatey\bin\rustc.exe" set "RUST_FOUND=1"

if defined RUST_FOUND (
    echo WARNING: Some Rust files may still exist
    echo You may need to manually remove them
) else (
    echo SUCCESS: All Rust installations appear to be removed
)

echo.
echo ========================================
echo Cleanup completed!
echo ========================================
echo.
echo Next steps:
echo 1. Restart your computer to ensure all PATH changes take effect
echo 2. Run the new install script to install Rust properly via rustup
echo.
pause
