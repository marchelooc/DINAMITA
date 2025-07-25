#ID12
import requests
#import pytest

#@pytest.mark.functional
def Obtener_la_lista_de_departamentos():  

    #DESCRIPCIÓN:El usuario debe de obtener los datos de un departamento en este caso llegaria a ser su id y su descripción
    #AMBIENTE:
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    #PASOS:
    #2 copiar y pegar la url en el campo
    #3 seleccionar la opción "GET"
    payload = {}
    headers = {
    'Cookie': 'incap_ses_1721_1662004=yJ6rOGfVaU+ro27evjjiFwEkgGgAAAAAyTmGAugBJ6kcncc03tDTIA==; visid_incap_1662004=3yZiV9hCSTappTI8YmOPSAEkgGgAAAAAQUIPAAAAAACifHRNUag9WnmIVdLJhzZY'
    }
    #4 presionar el botón "SEND"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    #5 comparar resultados
    assert response.status_code ==200
 