import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

payload = {}
headers = {
'Cookie': 'incap_ses_1727_1662004=TXtgZSvij31kEud0tIn3F9sdjWgAAAAAHblnGNIqiXWt3WND8iQPKg==; visid_incap_1662004=6rg7yOcVQSiWeMXP6+UrC2gjgGgAAAAAQUIPAAAAAADj817Sk9wh5uw1BmABaQhS'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
