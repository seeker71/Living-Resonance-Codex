@echo off
echo 🌊 Living Codex Phase 4 - Automated Test Suite
echo ================================================
echo.

echo Installing Python dependencies...
pip install -r test_requirements.txt

echo.
echo Starting automated test suite...
python automated_test_suite.py

echo.
echo Test suite completed. Press any key to exit.
pause >nul
