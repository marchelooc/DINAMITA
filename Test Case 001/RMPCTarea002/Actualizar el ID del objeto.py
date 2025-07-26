import pytest
import requests


def RETarea002_Actualizar_el_ID_del_Objeto():
    url = "https://api.restful-api.dev/objects/ERFADCVCXVASD"

    lista_url = url + "objects"
    response = requests.request("PATCH", lista_url)
    assert response.status_code == 404
