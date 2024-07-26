import requests
from requests.auth import HTTPBasicAuth

# Replace these variables with your actual ARI credentials and Asterisk server details
ARI_USERNAME = 'your_username'
ARI_PASSWORD = 'your_password'
ASTERISK_HOST = 'your_asterisk_host'
ARI_PORT = '8088'  # Default ARI port

# The URL for fetching bridge data
ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/bridges'

# Make the GET request to the ARI
response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

# Check the response status
if response.status_code == 200:
    # Parse the JSON response
    bridges_data = response.json()
    print("Bridges Data:", bridges_data)
else:
    print(f"Failed to get bridges data. Status code: {response.status_code}, Response: {response.text}")
