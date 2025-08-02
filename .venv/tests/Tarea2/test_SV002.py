import pytest
import requests

def test_SV002_Agregar_un_item_sin_body_para_generar_un_error_400():
    url = "https://api.restful-api.dev/"
    
    list_url = url + "objects"

    payload = ""
    headers = {}

    response = requests.request("POST", list_url, headers=headers, data=payload)

    assert response.status_code == 400
    
    print(response.text)