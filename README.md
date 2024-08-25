# SEO Insight

- [SEO Insight](#seo-insight)
  - [Folder and File Descriptions](#folder-and-file-descriptions)
    - [`/src`](#src)
    - [`/tests`](#tests)
    - [`/env`](#env)
    - [`/scripts`](#scripts)
    - [`/docs`](#docs)
    - [Root-Level Files](#root-level-files)

## Folder and File Descriptions

### `/src`

The `src` folder contains the main application code.

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`/api`**: Contains modules for interacting with external APIs.
  - **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`google_search_console.py`**: Contains the logic for interacting with the Google Search Console API.
  - **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`siteimprove.py`**: Contains the logic for interacting with the Siteimprove API.
  
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`/config`**: Holds configuration files for the application.
  - **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`settings.py`**: General configuration settings for the application.
  - **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`secrets.py`**: Handles the loading and management of secrets, potentially using tools like `keyring`.
  
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`/utils`**: Contains utility functions and helper modules.
  - **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`helpers.py`**: Contains reusable utility functions that can be used across the application.

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`main.py`**: The main entry point for the application, where the main logic is executed.

### `/tests`

This directory contains all unit tests for the application, ensuring that the code works as expected.

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`test_google_search_console.py`**: Unit tests for the logic interacting with the Google Search Console API.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`test_siteimprove.py`**: Unit tests for the logic interacting with the Siteimprove API.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`test_helpers.py`**: Unit tests for the utility functions defined in `helpers.py`.

### `/env`

The `env` directory holds environment-specific configuration files.

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`.env.development`**: Environment variables specific to the development environment, such as API keys and debug settings.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`.env.production`**: Environment variables specific to the production environment, ensuring a secure and stable setup.

### `/scripts`

Contains utility scripts used for various tasks, such as managing secrets or running the application.

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`set_secrets.py`**: Script to securely store secrets using tools like `keyring`.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`manage.py`**: A general-purpose management script that can be used for tasks like setting up the environment, running the server, or deploying the application.

### `/docs`

This directory holds all project documentation.

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`README.md`**: The main project documentation, typically providing an overview, setup instructions, and usage guidelines.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`setup_guide.md`**: Detailed instructions on setting up the development and production environments, including configuring the application and deploying it.

### Root-Level Files

- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`.gitignore`**: Specifies files and directories that should be ignored by version control, such as environment files and compiled Python files.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`requirements.txt`**: Lists the Python dependencies required for the project, used by `pip` to install the necessary packages.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`setup.py`**: A setup script for packaging and distributing the application, typically used if you plan to make the project installable as a package.
- **[🡵](https://github.com/isaiahdaviscom/SEO-Insight/blob/main/src/api/google_search_console.py)`README.md`**: The primary documentation for the project, providing an overview, setup instructions, and other key information.
