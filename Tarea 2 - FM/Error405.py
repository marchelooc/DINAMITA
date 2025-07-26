# ID: 001
import pytest
import requests


# Prioridad: Media
# Categoria: Smoke

@pytest.mark.smoke
@pytest.mark.negative
# Titulo: Modificar los departamentos
def Modificar_los_departamentos():

  # Descripción: El usuario debe modificar  todos los datos de los departamentos
  # Ambiente: Acceso al metmuseum.com
  url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"


  # Pasos
  # 1 Seleccionar el método GET
  # 2 Llamar a los departamentos
  headers = {
    'Cookie': 'incap_ses_1723_1662004=HXtjB7QIOjf+s0MrvFPpF1gZhGgAAAAAFwTeX7tFX1hEsLg7WPHndg==; visid_incap_1662004=NUsu9M5dQe6dQglJ7tSY5REjgGgAAAAAQUIPAAAAAACHApHYhaBxewyAOOr7yc+A'
  }

  # 3 Click en el botón Send
  response = requests.request("PUT", url, headers=headers, data=payload)

  # 4 Verificar que el estado correcto sea 405
  assert response.status_code == 405

  print(response.text)
