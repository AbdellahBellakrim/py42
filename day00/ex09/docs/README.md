# ft_package

A sample Python package demonstrating how to create and distribute a Python package.

## Description

This is a simple package built with modern Python packaging tools (`pyproject.toml` and setuptools).

## Requirements

- Python >= 3.10
- pip

## Installation

### Option 1: Install from source (editable mode)

```bash
cd /Users/abdellah/Desktop/py42/day00/ex09
pip install -e .
```

### Option 2: Build and install

```bash
# Install build tools
pip install build

# Build the package
python -m build

# Install from the built package
pip install dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
import ft_package

# Your code here
```

## Verify Installation

```bash
pip show ft_package
```

## Uninstall

```bash
pip uninstall ft_package
```

## Author

**Abdellah Bellakrim**  
Email: bellakrim2032@gmail.com

## License

MIT