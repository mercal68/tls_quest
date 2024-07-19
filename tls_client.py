# Get access to a server's url through a token to get a secret word
# Run this terminal command: curl -s "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google" | jq -r .access_token


# Run this app to access a GCP server as tls_client.py
import os
import requests

def get_secret_word():
    url = os.environ["SECRET_URL"]
    response = requests.get(url)
    print(f"The secret message is: {response.text}")

if __name__ == "__main__":
    get_secret_word()