import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?metadataDate=2018-10-22&departmentIds=3|9|12"

payload = {}
headers = {
  'Cookie': 'visid_incap_1662004=7wUdu9GvTI2Z0LwXM8yzexsjgGgAAAAAQUIPAAAAAADa9P5v9iP/IGBcsXTe+RJG'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
