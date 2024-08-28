# Setup guide for development and production environments

This project interacts with the Google Search Console API to retrieve and process site data. The project is structured as a Python package and includes utilities for authenticating with the API, retrieving data, and formatting results.

- [Setup guide for development and production environments](#setup-guide-for-development-and-production-environments)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
  - [Folder Structure](#folder-structure)

## Prerequisites

- Python 3.7 or higher
- Access to [Google Cloud Console](https://console.cloud.google.com/) to create a service account
- Access to [Google Search Console](https://search.google.com/search-console/) with verified site ownership

## Project Setup

  1. **Clone the Repository:**

```cmd
git clone https://github.com/your-username/google-search-console-python.git
```

```cmd
cd google-search-console-python
```

2. **Create a Virtual Environment:**
  
  **On Windows:**

  ```bash
  python -m venv .venv
  ```

  ```bash
  python -m venv .venv
  ```

## Folder Structure

This document outlines the recommended folder structure for your project, providing an organized way to manage source code, tests, scripts, configuration files, and documentation.

```plaintext
/project_root
│
├── /src
│   ├── __init__.py
│   ├── /api
│   │   ├── __init__.py
│   │   ├── google_search_console.py
│   │   └── siteimprove.py
│   ├── /config
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── secrets.py
│   ├── /utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py
│
├── /tests
│   ├── __init__.py
│   ├── test_google_search_console.py
│   ├── test_siteimprove.py
│   └── test_helpers.py
│
├── /env
│   ├── .env.development
│   └── .env.production
│
├── /scripts
│   ├── set_secrets.py
│   └── manage.py
│
├── /docs
│   ├── README.md
│   └── setup_guide.md
│
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```
