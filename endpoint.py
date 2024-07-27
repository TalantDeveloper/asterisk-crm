import requests
from requests.auth import HTTPBasicAuth
import json

# Replace these variables with your actual ARI credentials and Asterisk server details
ARI_USERNAME = 'asterisk'
ARI_PASSWORD = '@Botirjon06'
ASTERISK_HOST = '172.16.0.117'
ARI_PORT = '8088'  # Default ARI port

# The URL for originating a call
ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/channels'

# Data for originating a call
data = {
    "endpoint": "PJSIP/1001",  # Replace with the actual endpoint
    "extension": "2001",  # Replace with the actual extension
    "context": "default",
    "priority": 1,
    "callerId": "TestCall"
}

# Make the POST request to the ARI
response = requests.post(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD), data=json.dumps(data))

# Check the response status
if response.status_code == 200:
    # Parse the JSON response
    call_response = response.json()
    print("Call Response:", call_response)
else:
    print(f"Failed to originate call. Status code: {response.status_code}, Response: {response.text}")

