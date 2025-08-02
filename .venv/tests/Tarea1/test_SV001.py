import requests
import pytest

@pytest.mark.smoke

def test_sv001_Obtener_una_lista_de_IDs_de_los_objetos_del_departamento_1():
    #Descripción: El usuario debe obtener la cantidad y una lista de IDs del departamento 1.
    
    #Ambiente
    url = "https://collectionapi.metmuseum.org/"
    
    #Pasos
    # 1 Abrir el postman
    # 2 seleccionar GET
    # 3 llamar al recurso
    list_url = url + "public/collection/v1/objects?departmentIds=1"
    
    payload = {}
    headers = {
    'Cookie': 'incap_ses_1727_1662004=YVRnQz9AfSCloDG5ton3F1YwjmgAAAAAr/GS2Nnews3Nt2ln9rHQdA==; visid_incap_1662004=6rg7yOcVQSiWeMXP6+UrC2gjgGgAAAAAQUIPAAAAAADj817Sk9wh5uw1BmABaQhS'
    }
    
    # 4 click en el boton SEND
    response = requests.request("GET", list_url, headers=headers, data=payload)
    
    # 5 verificar que el estado sea 200
    assert response.status_code == 200

    # 6 verificar que el resultado muestre un entero y un arreglo. 
    print(response.text)