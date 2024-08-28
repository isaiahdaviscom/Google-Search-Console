# Google Search Console API                     # Python Client Library - Service Account Authentication 

# Import built-in modules
import os                                       # Import the os module for environment variables and file paths
import json                                     # Import the json module for JSON file operations

# Import third-party libraries
from dotenv import load_dotenv, find_dotenv     # Import the load_dotenv and find_dotenv functions from the dotenv package
from google.oauth2 import service_account       # Import the service_account module from the google.oauth2 package
from googleapiclient.discovery import build     # Import the build function from the googleapiclient.discovery module
from googleapiclient.errors import HttpError    # Import the HttpError class from the googleapiclient.errors module
from datetime import datetime, timedelta        # Import the datetime and timedelta classes from the datetime module

# Variables                                     # Definition Hierarchy - 1. Constants, 2. Variables, 3. Functions
# SCOPES = ''                                   # OAuPth 2.0 scopes for the Google Search Console API
# API_SERVICE_NAME = ''                         # Name of the Google Search Console API service
# API_VERSION = ''                              # Version of the Google Search Console API
# service_account_file = ''                     # Path to the service account JSON key file
# credentials = ''                              # Credentials object for the service API
# env_path = ''                                 # Path to the .env file
# env_loaded = False                            # Flag to check if the .env file is loaded

# Set Variables
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
API_SERVICE_NAME = 'searchconsole'
API_VERSION = 'v1'
API_SECRET_NAME = 'GSC_CLIENT_SECRET'
env_path = find_dotenv()
env_loaded = load_dotenv(dotenv_path=env_path)  # Load the .env file
service_account_file = os.getenv(API_SECRET_NAME)
service = ''
credentials = ''

# Functions
def _initialize ():
    # service_account_secrets = {}              # JSON object to store the service account secrets
    # site_url = ''                             # URL of the website to query
    # service = ''                              # Service object for the Google Search Console API
    # response = {}                             # JSON object to store the API response
    service_account_secrets = getSecretsByName(API_SECRET_NAME)
    site_url = service_account_secrets['site_url']
    # print(json.dumps(service_account_secrets, indent=4))
    credentials = service_account.Credentials.from_service_account_info(service_account_secrets)
    service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    response = service.sites().get(siteUrl=site_url).execute()
    print(response)

# Function > Support

# Get Variables (Environment Variables)
def getVariables():
    return {
        'SCOPES': SCOPES,
        'API_SERVICE_NAME': API_SERVICE_NAME,
        'API_VERSION': API_VERSION,
        'API_SECRET_NAME': API_SECRET_NAME,
        'env_path': env_path,
        'env_loaded': env_loaded,
        'service_account_file': service_account_file,
        'service': service,
        'credentials': credentials
    }

# Get Secrets by Name (Service Name)
def getSecretsByName(serviceName):
    # Check if the path is valid
    if service_account_file and os.path.exists(service_account_file):
        # Open and read the JSON file
        with open(service_account_file, 'r') as file:
            secret_data = json.load(file)
        
        # Print the contents of the client_secret.json file
    else:
        print("The client_secret.json file path is invalid or does not exist.")
    return secret_data[serviceName]

# Get Search Console Data (Search Analytics)
def get_search_console_data(self, site_url, start_date, end_date, dimensions=['query'], row_limit=5000):
        request_body = {
            'startDate': start_date,
            'endDate': end_date,
            'dimensions': dimensions,
            'rowLimit': row_limit
        }
        response = self.service.searchanalytics().query(siteUrl=site_url, body=request_body).execute()
        return response.get('rows', [])

# Format Search Console Data
def format_search_console_data(data):
    formatted_data = []
    for row in data:
        entry = {
            'query': row['keys'][0],
            'clicks': row['clicks'],
            'impressions': row['impressions'],
            'ctr': row['ctr'],
            'position': row['position']
        }
        formatted_data.append(entry)
    return formatted_data

_initialize()

# class GoogleSearchConsole:
#     def __init__(self):
#         pass

#     def getVariables(self):
#         return getVariables()

#     def getSecretsByName(self, serviceName):
#         return getSecretsByName(serviceName)
    
#     def get_search_console_data(self, site_url, start_date, end_date, dimensions=['query'], row_limit=5000):
#         return get_search_console_data(self, site_url, start_date, end_date, dimensions, row_limit)
    
#     @staticmethod
#     def format_search_console_data(data):
#         return format_search_console_data(data)

#     def initialize(self):
#         _initialize()