#!/bin/bash

# Build script for the simple-calculator package

set -e

echo "Building simple-calculator package..."

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info

# Install build dependencies
echo "Installing build dependencies..."
python3 -m pip install --upgrade build twine

# Build the package
echo "Building distribution packages..."
python -m build

# Verify the build
echo "Verifying the build..."
twine check dist/*

echo "Build complete! Distribution files are in the dist/ directory."
echo ""
echo "To install locally, run:"
echo "  python3 -m pip install dist/*.whl"
echo ""
echo "To test the package:"
echo "  python3 -m pip install -e ."
