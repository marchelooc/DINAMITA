import pytest
import requests

# Prioridad: High

@pytest.mark.smoke

def Obtener_una_lista_de_los_IDs_de_los_objetos_del_departamento_1():
#   ***Descripción: El usuario debe obtener la cantidad de objetos del departamento 1 y una lista de IDs (objectIDs).***

# Ambiente
url = "https://collectionapi.metmuseum.org/public/collection/v1/"

#Pasos
# 1 Abrir el postman
# 2 seleccionar GET
# 3 llamar al recurso objects?departmentIds=1
list_url = url + "objects?departmentIds=1"
# 4 click en el boton SEND
response = requests.get(list_url)
# 5 verificar que el estado sea 200
assert response.status_code == 200
# 6 verificar que el resultado muestre un entero y un arreglo. 