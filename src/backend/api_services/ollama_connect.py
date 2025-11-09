import os, requests

OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
r = requests.post(
    f"{OLLAMA}/api/generate",
    json={"model": "phi3:mini", "prompt": "Hello, how are you?", "stream": False},
    timeout=120
)
print(r.json().get("response",""))