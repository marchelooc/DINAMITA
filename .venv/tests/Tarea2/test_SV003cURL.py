#cURL para un caso de request 404 (el endpoint esta mal escrito y no exite)

import requests
import json

url = "https://api.restful-api.dev/objectss"

payload = json.dumps({
"name": "Apple tablet X",
"data": {
"year": 2019,
"price": 1849.99,
"CPU model": "Intel Core i9",
"Hard Disk size": "1 TB"
}
})
headers = {
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)