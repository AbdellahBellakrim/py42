# Python Packaging: Understanding the Fundamentals

## Part 1: The Core Concepts

### What Problem Does Packaging Solve?

Let's start with a real scenario:

**Without Packaging:**
```
You write some useful Python code: calculator.py
Your friend wants to use it.
You email them calculator.py
They put it in their project folder
They import it: from calculator import add
```

**Problems:**
- What if your code needs other libraries (like `requests`)?
- Your friend has to manually install those too
- What if you update calculator.py? You have to email it again
- What if they want to use it in 5 different projects? Copy it 5 times?
- How do they know which Python version it needs?

**With Packaging:**
```
You create a package called "mycalculator"
You publish it to PyPI (Python Package Index)
Your friend types: pip install mycalculator
Done! It automatically handles everything
```

### The Three Fundamental Questions

Every package answers three questions:

1. **WHAT is being packaged?** (your Python code)
2. **HOW to build it?** (the build system)
3. **WHO/WHAT/WHERE?** (metadata: name, version, dependencies)

Let's explore each one deeply.

---

## Part 2: Understanding Python Modules and Packages

### Module vs Package vs Distribution Package

**Module** = A single Python file
```python
# calculator.py is a module
def add(a, b):
    return a + b
```

**Package** = A directory with an `__init__.py` file and modules inside
```
mymath/               # This is a package
├── __init__.py      # This makes it a package!
├── calculator.py    # A module inside the package
└── geometry.py      # Another module
```

**Distribution Package** = What you install with pip (the .whl or .tar.gz file)
- It's a compressed file containing your package(s)
- It includes metadata about dependencies, version, etc.

### Why Does `__init__.py` Exist?

This file tells Python: "Hey, this directory is a package, not just a random folder!"

**What happens without it:**
```python
# Won't work if mymath/ has no __init__.py
from mymath import calculator  # Error!
```

**What happens with it:**
```python
# Works because mymath/ has __init__.py
from mymath import calculator  # Success!
```

**What goes inside `__init__.py`?**

Option 1: Leave it empty (just makes the directory a package)
```python
# __init__.py (empty file)
```

Option 2: Make imports easier for users
```python
# __init__.py
from .calculator import add, subtract
from .geometry import area_circle

# Now users can do:
# from mymath import add
# Instead of:
# from mymath.calculator import add
```

---

## Part 3: Understanding Import Paths

### How Python Finds Your Code

When you do `import mypackage`, Python searches in order:

1. **Current directory** (where you ran python from)
2. **PYTHONPATH** (environment variable)
3. **Site-packages** (where pip installs things)

### The Import Problem (Why "src" Layout Exists)

**Scenario with Flat Layout:**
```
myproject/
├── mypackage/
│   ├── __init__.py
│   └── code.py
├── tests/
│   └── test_code.py
└── pyproject.toml
```

When you run tests from `myproject/`:
```python
# test_code.py
from mypackage import code  # Which one does it import?
```

Python might import from `myproject/mypackage/` (your source code)
OR from `site-packages/mypackage/` (your installed package)

**You don't know which one!** This causes bugs when your source code differs from installed code.

**Solution: src Layout**
```
myproject/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── code.py
├── tests/
│   └── test_code.py
└── pyproject.toml
```

Now `src/` is NOT in Python's path by default. The only way to import is from the installed package. This forces you to install your package properly, ensuring tests run against the real thing.

---

## Part 4: Understanding the Build Process

### What Does "Building" Mean?

Building converts your source code into a distributable format.

**The Build Process:**
```
Your source code
        ↓
Build tool (Hatchling/Poetry/etc.)
        ↓
Creates distribution files:
  - .whl (wheel) - binary format, fast to install
  - .tar.gz (sdist) - source format, works everywhere
```

### Why Two Formats?

**Wheel (.whl)** - Think of it like a .zip file
- Pre-built, ready to install
- Fast installation (just unzip to site-packages)
- Platform-specific if it has C extensions
- Example: `mypackage-0.1.0-py3-none-any.whl`
  - `py3` = Python 3
  - `none` = no specific ABI
  - `any` = works on any platform

**Source Distribution (.tar.gz)** - Think of it like raw ingredients
- Contains your source code + instructions
- Needs to be built during installation
- Slower to install but more compatible
- Fallback when wheel isn't available

### What is a Build Backend?

A build backend is the tool that actually creates these distribution files.

**The Build Backend's Job:**
1. Read `pyproject.toml`
2. Find all your Python files
3. Bundle them together
4. Add metadata (name, version, dependencies)
5. Create the .whl and .tar.gz files

**Popular Build Backends:**

**Hatchling** - Modern, simple
- Good defaults
- Fast
- Easy to configure

**Setuptools** - The original, most compatible
- Been around forever
- Handles complex scenarios
- More configuration needed

**Poetry** - All-in-one tool
- Manages dependencies
- Manages virtual environments
- Builds packages
- More opinionated

---

## Part 5: Understanding pyproject.toml

### The Evolution of Configuration

**Old Way (before 2016):**
```python
# setup.py
from setuptools import setup

setup(
    name="mypackage",
    version="0.1.0",
    packages=["mypackage"],
    install_requires=["requests"],
)
```
Problems: Python code for configuration, hard to read, inconsistent

**Middle Way (2016-2020):**
```ini
# setup.cfg
[metadata]
name = mypackage
version = 0.1.0
```
Better: Declarative, but still needed setup.py

**Modern Way (2021+):**
```toml
# pyproject.toml (one file for everything!)
[project]
name = "mypackage"
version = "0.1.0"
dependencies = ["requests"]
```

### The Structure of pyproject.toml

Think of it as three sections:

**Section 1: Build System** (How to build)
```toml
[build-system]
requires = ["hatchling"]       # What tool to use
build-backend = "hatchling.build"  # Which part of the tool
```
This tells pip: "When someone installs my package, use Hatchling to build it"

**Section 2: Project Metadata** (What and Who)
```toml
[project]
name = "mypackage"           # WHAT: Package name
version = "0.1.0"            # WHAT: Version
description = "..."          # WHAT: Brief description
authors = [{name = "..."}]   # WHO: Creator
dependencies = ["requests"]  # WHAT NEEDS: Other packages
requires-python = ">=3.8"    # WHAT NEEDS: Python version
```

**Section 3: Tool Configuration** (Tool-specific settings)
```toml
[tool.hatchling]
# Settings specific to Hatchling

[tool.pytest]
# Settings for pytest

[tool.ruff]
# Settings for ruff linter
```

---

## Part 6: Understanding Dependencies

### What Are Dependencies?

Dependencies are other packages your package needs to work.

**Example:**
```python
# Your code in mypackage/api.py
import requests  # You're using the requests library

def fetch_data(url):
    response = requests.get(url)
    return response.json()
```

You MUST declare `requests` as a dependency:
```toml
[project]
dependencies = ["requests"]
```

### Why Declare Dependencies?

When someone installs your package:
```bash
pip install mypackage
```

pip automatically installs `requests` too! Without declaring it, your code would crash with "ModuleNotFoundError: No module named 'requests'"

### Version Constraints

**Why constrain versions?**
- Different versions have different features
- Newer versions might break your code
- You need to specify what works

**Common patterns:**
```toml
dependencies = [
    "requests>=2.28.0",      # Minimum version: need feature X added in 2.28
    "numpy>=1.20,<2.0",      # Compatible range: avoid breaking changes in 2.0
    "pandas~=1.5.0",         # Compatible release: 1.5.0 to 1.5.9 OK, 1.6.0 not OK
    "click==8.0.0",          # Exact version: (rarely needed, avoid if possible)
]
```

**Philosophy:**
- Be as loose as possible (don't break other people's setups)
- Be as strict as necessary (ensure your code works)

### Types of Dependencies

**Runtime Dependencies** (dependencies)
```toml
dependencies = ["requests"]  # Needed to run your package
```

**Development Dependencies** (optional-dependencies)
```toml
[project.optional-dependencies]
dev = ["pytest", "ruff"]  # Only needed for development
docs = ["sphinx"]         # Only needed to build documentation
test = ["pytest", "coverage"]  # Only needed for testing
```

Install with:
```bash
pip install mypackage           # Just runtime deps
pip install mypackage[dev]      # Runtime + dev deps
pip install mypackage[dev,docs] # Multiple optional groups
```

---

## Part 7: Understanding Installation

### What Does "pip install" Actually Do?

**Regular Install:**
```bash
pip install mypackage
```

Steps:
1. Download the .whl file from PyPI
2. Unzip it into `site-packages/mypackage/`
3. Create a `mypackage-0.1.0.dist-info/` folder with metadata
4. Your package is now in Python's path

**Editable Install (Development Mode):**
```bash
pip install -e .
```

The `-e` flag means "editable". Steps:
1. Creates a `.egg-link` file pointing to your source code
2. Your source code stays where it is
3. Python imports directly from your source
4. **Changes to code are immediately active** (no reinstall needed!)

This is CRITICAL for development. Without it, every time you change code, you'd need to reinstall.

### Understanding the Dot (.)

```bash
pip install -e .
              ↑
              What does this mean?
```

The `.` means "current directory". pip looks for `pyproject.toml` in the current directory and installs from there.

You can also specify a path:
```bash
pip install -e /path/to/myproject
pip install -e ../sibling-project
```

---

## Part 8: Understanding Distribution

### What is PyPI?

**PyPI (Python Package Index)** = The "App Store" for Python packages
- Central repository where packages live
- Anyone can upload
- Anyone can download with `pip install`
- URL: https://pypi.org

**TestPyPI** = Practice version of PyPI
- Test your uploads here first
- URL: https://test.pypi.org

### How Distribution Works

**The Journey:**
```
1. You build your package
   → Creates .whl and .tar.gz in dist/

2. You upload to PyPI
   → Files stored on PyPI servers

3. User runs pip install mypackage
   → pip downloads from PyPI
   → pip installs to their Python environment

4. User imports your code
   → from mypackage import something
```

### Understanding Wheels in Detail

A wheel filename tells you a lot:
```
mypackage-0.1.0-py3-none-any.whl
│         │      │   │    │
│         │      │   │    └─ Platform (any = all platforms)
│         │      │   └────── ABI (none = no compiled code)
│         │      └────────── Python version (py3 = Python 3)
│         └───────────────── Version
└─────────────────────────── Package name
```

**Pure Python package** (no C extensions):
- `py3-none-any.whl` - works everywhere

**Compiled package** (has C extensions):
- `cp311-cp311-win_amd64.whl` - only for Python 3.11 on Windows 64-bit
- Needs different wheels for different platforms

---

## Part 9: Understanding Versioning

### Semantic Versioning (SemVer)

Format: `MAJOR.MINOR.PATCH`

**MAJOR** (1.0.0 → 2.0.0)
- Breaking changes
- Users need to update their code
- Example: You rename a function

**MINOR** (1.0.0 → 1.1.0)
- New features
- Backward compatible
- Example: You add a new function

**PATCH** (1.0.0 → 1.0.1)
- Bug fixes
- Backward compatible
- Example: You fix a crash

**Pre-releases:**
- `1.0.0a1` - Alpha (very early)
- `1.0.0b1` - Beta (feature complete, testing)
- `1.0.0rc1` - Release candidate (almost ready)

### Why Versioning Matters

**For Users:**
```toml
dependencies = ["mypackage>=1.0.0,<2.0.0"]
```
This says: "I need version 1.x.x, but 2.0.0 might break my code"

**For You:**
- Tells users what to expect
- Signals breaking changes
- Helps with bug tracking

---

## Part 10: Putting It All Together

### The Complete Picture

Let's trace the entire lifecycle:

**1. Development Phase**
```
You write code in: src/mypackage/
You write tests in: tests/
You configure in: pyproject.toml
You install with: pip install -e .
```

**2. Building Phase**
```
You run: python -m build
Build backend reads: pyproject.toml
It creates: dist/mypackage-0.1.0-py3-none-any.whl
            dist/mypackage-0.1.0.tar.gz
```

**3. Testing Phase**
```
You test the built package:
  Create new environment
  Install from wheel
  Run tests
  Verify it works
```

**4. Publishing Phase**
```
You upload with: twine upload dist/*
Twine sends files to: PyPI servers
PyPI makes it available: pip install mypackage works!
```

**5. Usage Phase**
```
User runs: pip install mypackage
pip downloads: .whl from PyPI
pip extracts: files to site-packages/
User imports: from mypackage import something
```

### Minimal Working Example

Here's the absolute minimum to create a package:

**Directory structure:**
```
mypackage/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── main.py
└── pyproject.toml
```

**src/mypackage/__init__.py:**
```python
def hello():
    return "Hello from mypackage!"
```

**pyproject.toml:**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mypackage"
version = "0.1.0"
```

**That's it!** Now you can:
```bash
pip install -e .           # Install for development
python -m build            # Build distribution files
pip install dist/*.whl     # Install from wheel
```

---

## Part 11: Common Questions Answered

### Q: Why can't I just share .py files?

**You can!** But packaging gives you:
- Automatic dependency installation
- Version management
- Easy updates
- Professional distribution
- Reusability across projects

### Q: What's the difference between package name and module name?

**Package name** (in pyproject.toml):
- Used for `pip install package-name`
- Can have hyphens: `my-awesome-package`

**Module name** (directory name):
- Used for `import module_name`
- Must be valid Python identifier: `my_awesome_package`

Convention: Use hyphens in package name, underscores in module name.

### Q: Do I need both .whl and .tar.gz?

For most projects, yes:
- .whl = Fast installation for most users
- .tar.gz = Fallback for compatibility

But if you only build one, .whl is usually sufficient.

### Q: When do I need a build backend other than Hatchling?

**Stick with Hatchling if:**
- Pure Python package
- Simple structure
- Just getting started

**Consider Poetry if:**
- You want dependency management built-in
- You want virtual environment management
- You want an all-in-one tool

**Consider Setuptools if:**
- You have C extensions
- You need custom build logic
- Working with legacy code

### Q: What's the difference between pyproject.toml and requirements.txt?

**pyproject.toml:**
- Defines package dependencies (what your package needs)
- Part of the package
- Distributed with the package

**requirements.txt:**
- Lists exact versions for reproducible environments
- Not distributed
- Used for development/deployment
- Can include development tools

Often you have both:
- pyproject.toml: `requests>=2.28.0` (flexible)
- requirements.txt: `requests==2.28.1` (exact)

---

## Summary: The Mental Model

Think of packaging like publishing a book:

**Your code** = The manuscript
**Package structure** = Table of contents, chapters
**pyproject.toml** = The book's metadata (title, author, ISBN)
**Build backend** = The printing press
**.whl file** = The paperback book
**PyPI** = The bookstore
**pip install** = Buying and taking home the book
**import** = Opening and reading the book

Every part has a purpose, and they all work together to get your code from your computer to someone else's!

---

## Next Steps for Learning

1. **Start small**: Create a minimal package (like the example above)
2. **Install it locally**: Use `pip install -e .`
3. **Import and use it**: See it work
4. **Add complexity gradually**: More modules, dependencies, tests
5. **Build it**: Run `python -m build`
6. **Read the files**: Look inside the .whl (it's just a zip!)
7. **Publish to TestPyPI**: Practice the full workflow

The best way to understand is to do it yourself. Start with something tiny and build up!