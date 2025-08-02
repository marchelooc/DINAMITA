import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1"

payload = {}
headers = {
'Cookie': 'incap_ses_1727_1662004=YVRnQz9AfSCloDG5ton3F1YwjmgAAAAAr/GS2Nnews3Nt2ln9rHQdA==; visid_incap_1662004=6rg7yOcVQSiWeMXP6+UrC2gjgGgAAAAAQUIPAAAAAADj817Sk9wh5uw1BmABaQhS'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
