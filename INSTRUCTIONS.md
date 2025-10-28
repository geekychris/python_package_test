# Package Build and Deployment Instructions

## Overview

This package can be installed directly from a git repository using pip, without needing PyPI. The GitHub Actions workflow automatically builds releases when you push tags.

## Package Structure

```
python_package/
├── calculator/           # Package source code
│   ├── __init__.py
│   └── calculator.py
├── tests/               # Tests
│   ├── __init__.py
│   └── test_calculator.py
├── .github/
│   └── workflows/
│       └── release.yml  # GitHub Actions workflow
├── pyproject.toml       # Package configuration
├── README.md
├── LICENSE
├── .gitignore
├── build.sh            # Build script
└── INSTRUCTIONS.md     # This file
```

## Local Development and Testing

### 1. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

### 2. Install in editable mode

```bash
pip install -e .
```

### 3. Test the package

```bash
# Install pytest if needed
pip install pytest

# Run tests
pytest tests/
```

### 4. Try it out in Python

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(5, 3))      # 8
print(calc.multiply(4, 7)) # 28
```

## Building the Package Locally

### Option 1: Use the build script

```bash
chmod +x build.sh
./build.sh
```

### Option 2: Manual build

```bash
# Install build tools
pip install build twine

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build
python -m build

# Verify
twine check dist/*
```

This creates:
- `dist/simple_calculator-0.1.0-py3-none-any.whl` (wheel format)
- `dist/simple-calculator-0.1.0.tar.gz` (source distribution)

## Git Repository Setup

### 1. Initialize git repository

```bash
git init
git add .
git commit -m "Initial commit: simple calculator package"
```

### 2. Create a GitHub repository

1. Go to https://github.com/new
2. Create a new repository (e.g., "simple-calculator")
3. Don't initialize with README (you already have one)

### 3. Push to GitHub

```bash
git remote add origin https://github.com/yourusername/simple-calculator.git
git branch -M main
git push -u origin main
```

## Installing from Git Repository

Once pushed to GitHub, anyone can install it:

```bash
# Install from GitHub
pip install git+https://github.com/yourusername/simple-calculator.git

# Install a specific version/tag
pip install git+https://github.com/yourusername/simple-calculator.git@v0.1.0

# Install from a specific branch
pip install git+https://github.com/yourusername/simple-calculator.git@development
```

## Creating Releases with GitHub Actions

The included GitHub Actions workflow (`.github/workflows/release.yml`) automatically builds and creates releases when you push a version tag.

### 1. Update version

Edit `pyproject.toml` and `calculator/__init__.py` to update the version number.

### 2. Commit changes

```bash
git add .
git commit -m "Bump version to 0.2.0"
git push
```

### 3. Create and push a tag

```bash
git tag v0.2.0
git push origin v0.2.0
```

The GitHub Action will:
- Build the package
- Create a GitHub release
- Attach the distribution files (.whl and .tar.gz)

### 4. Install the specific release

```bash
pip install git+https://github.com/yourusername/simple-calculator.git@v0.2.0
```

## Without GitHub Actions (Manual Release)

If you don't want to use GitHub Actions:

1. Build locally: `./build.sh`
2. Create a git tag: `git tag v0.1.0 && git push origin v0.1.0`
3. Create a GitHub release manually and upload `dist/*` files

Users can still install from git:

```bash
pip install git+https://github.com/yourusername/simple-calculator.git
```

## Installing from Local Git Repository

For testing before pushing to GitHub:

```bash
pip install git+file:///Users/chris/code/warp_experiments/python_package
```

## Troubleshooting

### Build fails

- Ensure you have Python 3.8 or higher
- Update pip: `pip install --upgrade pip`
- Install build tools: `pip install build wheel setuptools`

### Import error after installation

- Verify installation: `pip list | grep simple-calculator`
- Check package name matches in `pyproject.toml` and imports

### GitHub Actions workflow doesn't run

- Ensure the workflow file is in `.github/workflows/`
- Check you've pushed a tag (not just a commit)
- Verify GitHub Actions is enabled in your repository settings

## Next Steps

1. Update `pyproject.toml` with your actual name, email, and repository URL
2. Add more functionality to the calculator
3. Add more tests in `tests/`
4. Set up continuous integration for running tests on every push
5. Consider publishing to PyPI for easier installation (optional)
