import requests

TOKEN="https://httpbin.org/get"
headers = { "Authorization": f"bearer {TOKEN}",
"Accept": "application/vnd.httpbin+json"
}
url = "https://httpbin.org/get"
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())
