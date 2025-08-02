import requests
import json

def test_SV003_Request_404():
    url = "https://api.restful-api.dev/"

    list_url = url + "objectss" #(el patch objectss esta mal escrito por tener doble s al final)

    payload = json.dumps({
    "name": "Apple tablet X",
    "data": {
    "year": 2024,
    "price": 1549.99,
    "CPU model": "Intel Core i7",
    "Hard Disk size": "4 TB"
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", list_url, headers=headers, data=payload)
    
    # aqui puse el codigo 200 para que em test falle indicando que el estado general es 404.
    assert response.status_code == 200

    print(response.text)