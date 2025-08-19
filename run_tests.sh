#!/bin/bash

echo "🌊 Living Codex Phase 4 - Automated Test Suite"
echo "==============================================="
echo

echo "Installing Python dependencies..."
pip3 install -r test_requirements.txt

echo
echo "Starting automated test suite..."
python3 automated_test_suite.py

echo
echo "Test suite completed."
