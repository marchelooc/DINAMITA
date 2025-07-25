import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

payload = {}
headers = {
  'Cookie': 'visid_incap_1662004=NUsu9M5dQe6dQglJ7tSY5REjgGgAAAAAQUIPAAAAAACHApHYhaBxewyAOOr7yc+A'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
