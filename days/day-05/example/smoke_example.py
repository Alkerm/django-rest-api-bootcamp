"""
Day 5 worked example - sending HTTP requests from Python with `requests` (Notes API).

requests.get / post / put / patch / delete(url, json=..., headers=..., timeout=...)
    response.status_code   -> 200, 201, 404 ...
    response.json()        -> the parsed JSON body (dict or list)
"""
import requests

BASE_URL = "http://127.0.0.1:8000"
TIMEOUT = 60  # always set a timeout so a sleeping/broken server cannot hang your script

# 1) log in -> token
response = requests.post(
    f"{BASE_URL}/api/auth/token/",
    json={"username": "sara", "password": "sara-demo-pass"},   # json= sends a JSON body + Content-Type header
    timeout=TIMEOUT,
)
print(response.status_code)                 # 200
token = response.json()["token"]

# 2) authenticated requests
headers = {"Authorization": f"Token {token}"}
response = requests.post(f"{BASE_URL}/api/notes/", json={"text": "Smoke"}, headers=headers, timeout=TIMEOUT)
note_id = response.json()["id"]             # 201 -> the new note

response = requests.get(f"{BASE_URL}/api/notes/{note_id}/", headers=headers, timeout=TIMEOUT)
print(response.status_code, response.json()["text"])   # 200 Smoke

response = requests.delete(f"{BASE_URL}/api/notes/{note_id}/", headers=headers, timeout=TIMEOUT)
print(response.status_code)                 # 204 - no body, so do NOT call response.json() here
