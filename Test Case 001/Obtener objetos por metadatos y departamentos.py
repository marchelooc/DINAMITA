import pytest
import requests

@pytest.mark.smoketest
def test_001_Obtener_objetos_por_metadatos_departamentos():
    # Descripcion: Se debe obtener una lista completa de todos los objetos cuyos datos fueron actualizados
    # el 22 de octubre de 2018 y que pertenezcan a los departamentos 3, 9, 12

    #Ambiente
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?metadataDate=2018-10-22&departmentIds=3|9|12"

    #Pasos
    # 1. Enviar peticion GET
    list_url = url + "objects"
    # 2. Clic en el boton SEND
    response = requests.get(list_url)
    # 3. Verificar que se reciba una respuesta con codigo 200
    assert response.status_code == 200