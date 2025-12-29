import requests

response = requests.get("https://httpbin.org/get")
print(f"Status: {response.status_code}")
print(f"JSON: {response.json()}")

try:
    r = requests.get("https://google.com", timeout=3)
    print(f"Google доступен: {r.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Google недоступен: {e}")
