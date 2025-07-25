import requests
import pytest 

#Titulo: Obtener lista estudiantes sin sede
#Descripcion: Obtener todos los estudiantes registrados pero sin especificar una sede
#Prioridad: Alta
#Pre-Condicion: Inicio sesion como usuario Gerente
#Resultado esperado: Se deberia de mostrarme error 404
@pytest.mark.smoke
def testCase001ObtenerListaEstudiantes ():
  url = "https://backend.clubinfinitychess.com/"
  #Pasos
  #1. Seleccionar GET
  lista_url = url + "obtenerEstudiantes"
  
  #2. Click boton send
  response = requests.get(lista_url)
  
  assert response.status_code == 404
  
  #Verificar la respuesta
