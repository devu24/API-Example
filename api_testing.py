import requests

url = "http://127.0.0.1:8000/multiply"
data = {
    "a": 3,
    "b": 2
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)