import subprocess
import sys


def main():
    print("Setup script executed.")
    # Run the build command
    print("Building package...")
    build_process = subprocess.run(
        [sys.executable, "-m", "build"],
        check=False
    )
    if build_process.returncode != 0:
        print("Build failed.")
        sys.exit(1)
    # Install the package
    print("Installing package...")
    whl_path = "./dist/ft_package-0.0.1-py3-none-any.whl"
    install_process = subprocess.run(
        [sys.executable, "-m", "pip", "install", whl_path],
        check=False
    )
    if install_process.returncode != 0:
        print("Installation failed.")
        sys.exit(1)
    print("Package built and installed successfully.")
    # List the installed package
    print("\nListing package:")
    subprocess.run([sys.executable, "-m", "pip", "list"], check=False)
    # Show package details
    print("\nPackage details:")
    subprocess.run([sys.executable, "-m", "pip", "show", "-v", "ft_package"])


if __name__ == "__main__":
    main()
