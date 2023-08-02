import os
import subprocess

def install_dependency(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
    except subprocess.CalledProcessError:
        print(f"Error installing {package_name}. Please check your internet connection and try again.")
        exit(1)

def main():
    dependencies = ["numpy", "cairocffi", "imageio"]

    for package in dependencies:
        print(f"Installing {package}...")
        install_dependency(package)
        print(f"{package} installed successfully!")

    print("All dependencies have been installed.")

if __name__ == "__main__":
    import sys

    if os.name != 'posix':
        print("This script is intended for Unix-like systems. It may not work on Windows.")
        print("Please install the required dependencies manually.")
        exit(1)

    main()
