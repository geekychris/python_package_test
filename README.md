# Simple Calculator

A simple Python calculator package with basic arithmetic operations.

## Installation

### Install from Git Repository

You can install this package directly from a git repository:

```bash
# Install from GitHub (replace with your actual repository URL)
pip install git+https://github.com/yourusername/simple-calculator.git

# Install from a specific branch
pip install git+https://github.com/yourusername/simple-calculator.git@main

# Install from a specific tag/version
pip install git+https://github.com/yourusername/simple-calculator.git@v0.1.0

# Install from a local git repository
pip install git+file:///path/to/local/repo
```

### Install from Local Directory (for development)

```bash
# Install in editable mode
pip install -e .

# Regular install
pip install .
```

## Usage

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(3, 7)   # 21
result = calc.divide(15, 3)    # 5.0
result = calc.power(2, 3)      # 8
```

## Building the Package

### Prerequisites

- Python 3.8 or higher
- pip (comes with Python)

### Build Steps

1. **Create a virtual environment** (recommended to avoid system package conflicts):

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

2. **Install build tools**:

```bash
python3 -m pip install --upgrade build twine
```

3. **Clean previous builds** (if any):

```bash
rm -rf build/ dist/
```

4. **Build the package**:

```bash
python3 -m build
```

5. **Verify the build** (optional but recommended):

```bash
twine check dist/*
```

This will create a `dist/` directory with:
- `simple_calculator-0.1.0-py3-none-any.whl` (wheel format)
- `simple_calculator-0.1.0.tar.gz` (source distribution)

### Quick Build (All-in-One)

Alternatively, use the provided build script:

```bash
chmod +x build.sh
source venv/bin/activate  # Activate venv first
./build.sh
```

Note: The build script assumes you're already in an activated virtual environment.

## Development

1. Clone the repository
2. Install in editable mode: `pip install -e .`
3. Make your changes
4. Test your changes

## License

MIT License
