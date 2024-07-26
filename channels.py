
import requests
from requests.auth import HTTPBasicAuth

# Replace these variables with your actual ARI credentials and Asterisk server details
ARI_USERNAME = 'asterisk'
ARI_PASSWORD = '@Botirjon06'
ASTERISK_HOST = '192.168.30.56'
ARI_PORT = '8088'  # Default ARI port

# The URL for fetching channel data
ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/endpoints'

# Make the GET request to the ARI
response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

# Check the response status
if response.status_code == 200:
    # Parse the JSON response2003
    channels_data = response.json()
    print("Channels Data:", channels_data)
else:
    print(f"Failed to get channels data. Status code: {response.status_code}, Response: {response.text}")
