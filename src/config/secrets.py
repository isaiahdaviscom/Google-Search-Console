# Secrets management
import os

# Load secrets from environment variables
API_KEY = os.environ.get('GSC_CLIENT_SECRET')

print(API_KEY)