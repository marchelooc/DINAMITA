import pytest
import requests

def test_SV002_Request_400():
    url = "https://api.restful-api.dev/"
    
    list_url = url + "objects"

    payload = ""
    headers = {}

    response = requests.request("POST", list_url, headers=headers, data=payload)

    assert response.status_code == 400
    
    print(response.text)