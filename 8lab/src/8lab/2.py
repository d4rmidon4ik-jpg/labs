import requests

response = requests.get("https://httpbin.org/get")
print(f"Status: {response.status_code}")

try:
    r = requests.get("https://google.com")
    print(f"Google доступен: {r.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Google недоступен: {e}")
