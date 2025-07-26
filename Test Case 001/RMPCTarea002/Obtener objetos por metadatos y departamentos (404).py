import pytest
import requests


@pytest.mark.smoketest
def RETarea002_Obtener_objetos_por_metadatos_departamentos ():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?metadataDate=DRTG-10-22&departmentIds=3|9|12"

    lista_url = url + "objects"
    response = requests.get(lista_url)
    assert response.status_code == 400