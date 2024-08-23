# Project documentation
- [Project documentation](#project-documentation)
  - [Folder and File Descriptions](#folder-and-file-descriptions)
    - [`/src`](#src)
    - [`/tests`](#tests)
    - [`/env`](#env)
    - [`/scripts`](#scripts)
    - [`/docs`](#docs)
    - [Root-Level Files](#root-level-files)
  - [Folder Structure](#folder-structure)

## Folder and File Descriptions

### [`/src`](www.google.com)

The `src` folder contains the main application code.

- **[`/api`](www.google.com)**: Contains modules for interacting with external APIs.
  - **`google_search_console.py`**: Contains the logic for interacting with the Google Search Console API.
  - **`siteimprove.py`**: Contains the logic for interacting with the Siteimprove API.
  
- **[`/config`](www.google.com)**: Holds configuration files for the application.
  - **`settings.py`**: General configuration settings for the application.
  - **`secrets.py`**: Handles the loading and management of secrets, potentially using tools like `keyring`.
  
- **[`/utils`](www.google.com)**: Contains utility functions and helper modules.
  - **`helpers.py`**: Contains reusable utility functions that can be used across the application.

- **`main.py`**: The main entry point for the application, where the main logic is executed.

### [`/tests`](www.google.com)

This directory contains all unit tests for the application, ensuring that the code works as expected.

- **`test_google_search_console.py`**: Unit tests for the logic interacting with the Google Search Console API.
- **`test_siteimprove.py`**: Unit tests for the logic interacting with the Siteimprove API.
- **`test_helpers.py`**: Unit tests for the utility functions defined in `helpers.py`.

### [`/env`](www.google.com)

The `env` directory holds environment-specific configuration files.

- **`.env.development`**: Environment variables specific to the development environment, such as API keys and debug settings.
- **`.env.production`**: Environment variables specific to the production environment, ensuring a secure and stable setup.

### [`/scripts`](www.google.com)

Contains utility scripts used for various tasks, such as managing secrets or running the application.

- **`set_secrets.py`**: Script to securely store secrets using tools like `keyring`.
- **`manage.py`**: A general-purpose management script that can be used for tasks like setting up the environment, running the server, or deploying the application.

### [`/docs`](www.google.com)

This directory holds all project documentation.

- **`README.md`**: The main project documentation, typically providing an overview, setup instructions, and usage guidelines.
- **`setup_guide.md`**: Detailed instructions on setting up the development and production environments, including configuring the application and deploying it.

### Root-Level Files

- **`.gitignore`**: Specifies files and directories that should be ignored by version control, such as environment files and compiled Python files.
- **`requirements.txt`**: Lists the Python dependencies required for the project, used by `pip` to install the necessary packages.
- **`setup.py`**: A setup script for packaging and distributing the application, typically used if you plan to make the project installable as a package.
- **`README.md`**: The primary documentation for the project, providing an overview, setup instructions, and other key information.

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
