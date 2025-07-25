import requests
import pytest 

@pytest.mark.smoke
def testCase001ObtenerListaEstudiantes ():
  url = "https://backend.clubinfinitychess.com/"
  #Pasos
  #1. Seleccionar GET
  lista_url = url + "obtenerEstudiantes/Modulo%204"
  
  #2. Click boton send
  response = requests.get(lista_url)
  
  assert response.status_code == 200
  
  #Verificar la respuesta
