# ID: 001
import pytest
import requests

@pytest.mark.smoke
def Obtener_lista_de_los_departamentos():
    # Descripción: El usuario debe obtener todos los datos de los departamentos

    # Ambiente: Acceso al metmuseum.com
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

    # Pasos
    # 1 Seleccionar el método GET
    headers = {
      'Cookie': 'incap_ses_1723_1662004=SAN5NXcrw13ZVRAqvFPpF7TFgmgAAAAAx/0r9jDzUA1Oo7JKLjzXfA==; visid_incap_1662004=NUsu9M5dQe6dQglJ7tSY5REjgGgAAAAAQUIPAAAAAACHApHYhaBxewyAOOr7yc+A'
    }
    # 2 Llamar a los departamentos
    # 3 Click en el botón Send
    response = requests.request("GET", url, headers=headers, data=payload)

    #4 Verificar que el estado correcto sea 200
    assert response.status_code == 200

    # Prioridad: Media
