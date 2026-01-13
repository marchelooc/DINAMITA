#cURL para un caso de request 400 (POST sin body)

import requests

url = "https://api.restful-api.dev/objects"

payload = ""
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
