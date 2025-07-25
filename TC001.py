import requests
import pytest 
#Titulo: Obtener lista estudiantes de la sede "Modulo 4"
#Descripcion: Obtener todos los estudiantes registrados en la sede "Modulo 4"
#Prioridad: Alta
#Pre-Condicion: Inicio sesion como usuario Gerente
#Resultado esperado: Se deberia de obtener lista de estudiantes de la sede Modulo 4
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
