import requests

api_url = "https://httpbin.org/get"
TOKEN = "mytoken"

headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(api_url, headers=headers)
data = response.json()
authenticated = data.get("headers", {}).get("Authorization") == f"Bearer {TOKEN}"
print(authenticated)
