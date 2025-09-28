import requests

# Simple direct test
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi:latest",
        "prompt": "Say hello",
        "stream": False
    }
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text[:200]}")
