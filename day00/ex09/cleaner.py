import subprocess
import shutil
import sys
from pathlib import Path


def main():
    """Clean up build artifacts and uninstall the package."""
    print("Starting cleanup...")
    # Uninstall the package
    print("\n[1/5] Uninstalling ft_package...")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "ft_package"], check=False)

    # Remove build directories
    dirs_to_remove = [
        "build",
        "dist",
        "src/ft_package.egg-info",
        "ft_package.egg-info",
        "__pycache__",
        ".pytest_cache",
        ".eggs"
    ]

    print("\n[2/5] Removing build directories...")
    for dir_name in dirs_to_remove:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"  ✓ Removed {dir_name}/")
        else:
            print(f"  - {dir_name}/ not found (skipped)")

    # Remove __pycache__ from subdirectories
    print("\n[3/5] Cleaning __pycache__ from subdirectories...")
    for pycache in Path(".").rglob("__pycache__"):
        shutil.rmtree(pycache)
        print(f"  ✓ Removed {pycache}")

    # Remove .pyc files
    print("\n[4/5] Removing .pyc files...")
    pyc_count = 0
    for pyc_file in Path(".").rglob("*.pyc"):
        pyc_file.unlink()
        pyc_count += 1
    print(f"  ✓ Removed {pyc_count} .pyc file(s)")
    # Verify package is uninstalled
    print("\n[5/5] Verifying uninstallation...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "show", "ft_package"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("  ✓ Package successfully uninstalled")
    else:
        print("  ⚠ Warning: Package may still be installed")

    print("\n✅ Cleanup complete!")


if __name__ == "__main__":
    main()
