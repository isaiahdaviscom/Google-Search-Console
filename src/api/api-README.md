# Application Platform Interfaces (APIs)

- [Application Platform Interfaces (APIs)](#application-platform-interfaces-apis)
  - [Overview](#overview)
    - [Files in the Folder](#files-in-the-folder)
    - [Usage Example](#usage-example)

## Overview

This folder contains the modules that handle interactions with external APIs. This folder is essential for organizing the logic that communicates with third-party services, ensuring that all API-related code is centralized and easy to manage.

### Files in the Folder

- **`__init__.py`**
  - This file makes the **/api** directory a Python package. It’s typically empty but can be used to initialize package-level variables or import specific components of the package for easier access.

- **`google_search_console.py`**
  - **Purpose**: This module contains the logic for interacting with the Google Search Console API. It includes functions to authenticate, query search analytics data, and process the information retrieved from Google Search Console.
  - **Key Functions**:
    - `get_search_console_data(site_url, start_date, end_date)`: Retrieves search analytics data for a specified site within a given date range.
    - `authenticate()`: Handles authentication with Google Search Console using service account credentials.
  - **Usage**: Import and use this module to integrate Google Search Console data into your application.

- **`siteimprove.py`**
  - **Purpose**: This module contains the logic for interacting with the Siteimprove API. It handles API requests to retrieve SEO-related data, such as search volumes and keyword performance metrics.
  - **Key Functions**:
    - `get_siteimprove_data()`: Sends a request to the Siteimprove API to retrieve SEO data, such as keyword search volumes.
    - `authenticate()`: Handles authentication with the Siteimprove API using API keys.
  - **Usage**: Import and use this module to pull Siteimprove data into your application for SEO analysis or reporting.

### Usage Example

Here is an example of how you might use the modules within the **/api** folder:

```python
from src.api.google_search_console import get_search_console_data
from src.api.siteimprove import get_siteimprove_data

# Example usage: Retrieve data from Google Search Console
site_url = 'https://example.com'
start_date = '2024-01-01'
end_date = '2024-01-31'
gsc_data = get_search_console_data(site_url, start_date, end_date)

# Example usage: Retrieve data from Siteimprove
siteimprove_data = get_siteimprove_data()

# Combine or process the data as needed
```
