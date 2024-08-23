import os

# Define the folder structure
folders = [
    "src",
    "src/api",
    "src/config",
    "src/utils",
    "tests",
    "env",
    "scripts",
    "docs",
]

# Define the files to be created
files = {
    "src/__init__.py": "",
    "src/api/__init__.py": "",
    "src/api/google_search_console.py": "# Google Search Console API logic\n",
    "src/api/siteimprove.py": "# Siteimprove API logic\n",
    "src/config/__init__.py": "",
    "src/config/settings.py": "# Configuration settings\n",
    "src/config/secrets.py": "# Secrets management\n",
    "src/utils/__init__.py": "",
    "src/utils/helpers.py": "# Utility functions\n",
    "src/main.py": "# Main entry point of the application\n",
    "tests/__init__.py": "",
    "tests/test_google_search_console.py": "# Unit tests for Google Search Console API logic\n",
    "tests/test_siteimprove.py": "# Unit tests for Siteimprove API logic\n",
    "tests/test_helpers.py": "# Unit tests for utility functions\n",
    "env/.env.development": "# Development environment variables\n",
    "env/.env.production": "# Production environment variables\n",
    "scripts/set_secrets.py": "# Script to set secrets in keyring\n",
    "scripts/manage.py": "# General-purpose management script\n",
    "docs/README.md": "# Project documentation\n",
    "docs/setup_guide.md": "# Setup guide for development and production environments\n",
    ".gitignore": "*.pyc\n__pycache__/\nenv/\n.env*\n",
    "requirements.txt": "# Project dependencies\n",
    "setup.py": "# Setup script for packaging and distribution\n",
    "README.md": "# Project overview and instructions\n",
}

# Create folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder: {folder}")

# Create files
for file_path, file_content in files.items():
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(file_content)
        print(f"Created file: {file_path}")

print("Folder structure created successfully.")
